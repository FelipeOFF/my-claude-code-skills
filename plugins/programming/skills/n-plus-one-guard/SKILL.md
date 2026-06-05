---
name: n-plus-one-guard
description: |
  Detecta e previne N+1 de queries SQL e chamadas HTTP/serviço redundantes
  dentro de uma mesma request. Use ao revisar endpoints, escrever ORM
  (Django/SQLAlchemy/Prisma), suspeitar de latência por loop de queries, ou
  ao montar guardrails de teste que travam o nº máximo de queries por rota.
  Triggers: "N+1", "query count", "queries demais", "eager loading",
  "select_related", "prefetch", "DataLoader", "loop de queries".
source: authored
upstream: https://github.com/FelipeOFF/n-plus-one-guard-skill
license: MIT
added: 2026-06-05
---

# N+1 Query Guard

Guardrail contra **N+1** e contra múltiplas queries/chamadas redundantes na
mesma request HTTP. O objetivo não é só "achar o N+1 de hoje" — é instalar um
**teto de queries por endpoint** que falha o CI quando alguém reintroduz o
problema.

## Quando ativar

- Revisando um endpoint/handler que itera sobre uma coleção e acessa relação por item.
- Latência cresce linear com o tamanho do payload (10 itens = 11 queries, 100 = 101).
- Antes de mergear código que toca ORM, serializers, ou resolvers GraphQL.
- Ao montar a suíte de testes de uma rota nova (instalar o teto desde o início).

## O modelo mental

Uma request HTTP deve ter um **orçamento de queries** conhecido e pequeno,
idealmente **O(1)** no tamanho da entrada. N+1 é o caso em que o custo vira
**O(n)**: 1 query para a lista + N queries para hidratar cada item.

```
# N+1 (ruim) — 1 + N
orders = Order.objects.all()              # 1 query
for o in orders:
    print(o.customer.name)                # +1 query por order

# O(1) — eager load
orders = Order.objects.select_related("customer")   # 1 query (JOIN)
for o in orders:
    print(o.customer.name)                # 0 queries extras
```

O mesmo vale para **chamadas HTTP/serviço**: um loop que faz `requests.get()`
por item é o N+1 da camada de rede. A cura é a mesma família: **batch** /
**bulk** / **cache por request**.

## Passo 1 — Medir (interceptar e contar)

Não confie no olho. Instrumente a contagem de queries por request e logue
quando estourar um limite. Padrões por stack:

| Stack | Como contar queries numa request |
|---|---|
| Django | `len(connection.queries)` com `DEBUG=True`, ou `CaptureQueriesContext`, ou `django-silk` / `nplusone` |
| SQLAlchemy | event listener em `before_cursor_execute` incrementando um contador no escopo da request |
| Prisma | `prisma.$on("query", ...)` contando eventos |
| Rails/AR | `ActiveSupport::Notifications.subscribe("sql.active_record")` |
| Qualquer | middleware que zera um contador no início da request e loga no fim |

Esqueleto de **interceptor por request** (framework-agnóstico):

```python
# Conta queries no escopo de UMA request e expõe o total para asserts/logs.
import contextvars

_query_count = contextvars.ContextVar("query_count", default=0)

def on_query_executed(*_args):          # plugar no hook de query do ORM
    _query_count.set(_query_count.get() + 1)

class QueryCountMiddleware:
    """Zera no começo da request, loga/alerta se passar do teto."""
    def __init__(self, app, soft_limit=20):
        self.app, self.soft_limit = app, soft_limit
    async def __call__(self, scope, receive, send):
        token = _query_count.set(0)
        try:
            await self.app(scope, receive, send)
        finally:
            n = _query_count.get()
            if n > self.soft_limit:
                log.warning("high_query_count", path=scope.get("path"), queries=n)
            _query_count.reset(token)
```

## Passo 2 — Travar o teto em teste (o guardrail que importa)

A medição vira **guardrail** quando um teste afirma "esta rota faz no máximo
K queries". Assim a regressão falha o CI, não a produção.

```python
# pytest — assert do orçamento de queries por endpoint
def test_orders_list_query_budget(client, django_assert_max_num_queries):
    # 1 (orders) + 1 (customers via select_related) + 1 (auth) = teto 3.
    with django_assert_max_num_queries(3):
        client.get("/api/orders")
```

```python
# Stack sem helper nativo: use o contador do interceptor.
def test_budget(client, query_counter):
    query_counter.reset()
    client.get("/api/orders?limit=100")
    assert query_counter.total <= 4, f"N+1 suspeito: {query_counter.total} queries"
    # O teste é por DESIGN independente de N: rode com 1, 10, 100 itens —
    # o teto não pode escalar com a quantidade.
```

**Teste anti-N+1 robusto:** rode o endpoint com 1 item e com N itens e afirme
que a contagem **não cresce** com N. Um teto fixo que passa com 1 item mas
não é testado com muitos esconde o bug.

```python
@pytest.mark.parametrize("size", [1, 25])
def test_query_count_is_constant_in_size(client, query_counter, seed_orders):
    counts = []
    for size in (1, 25):
        seed_orders(size)
        query_counter.reset(); client.get("/api/orders"); counts.append(query_counter.total)
    assert counts[0] == counts[1], f"queries escalam com N: {counts}"
```

## Passo 3 — Allowlist para tetos legítimos

Nem todo endpoint é O(1) e tudo bem. Mantenha um **allowlist versionado** com
o teto justificado por rota, para o guardrail global não virar ruído.

```yaml
# query_budgets.yaml — teto por rota, com justificativa obrigatória
"/api/orders":            { max_queries: 3,  reason: "list + select_related customer" }
"/api/dashboard":         { max_queries: 9,  reason: "5 widgets independentes, batch impraticável" }
"/api/reports/heavy":     { max_queries: 40, reason: "export agregado; aceito, roda async" }
```

Um teste parametrizado lê o YAML e afirma cada rota contra seu teto. Subir o
teto exige editar o arquivo (= aparece no diff, exige justificativa no review).

## Passo 4 — Curar o N+1

| Sintoma | Cura |
|---|---|
| Loop acessa relação 1:1 / FK | **JOIN eager**: `select_related` (Django), `joinedload` (SQLAlchemy), `include` (Prisma) |
| Loop acessa relação 1:N / M:N | **Prefetch em 2 queries**: `prefetch_related` (Django), `selectinload` (SQLAlchemy) |
| Campos vindos de resolvers (GraphQL) | **DataLoader**: agrupa chaves do mesmo tick e faz 1 query batch |
| Loop de `requests.get()` por item | **Batch endpoint** / `asyncio.gather` com 1 chamada bulk / cache por request |
| Mesma query repetida na request | **memoization por request** (cache no escopo da request, não global) |
| Contagem agregada por item | Mover agregação pro banco (`annotate`, `GROUP BY`) em vez de Python |

Regra de ouro: **resolva no banco, em batch, ou em cache de request** — nunca
num loop que toca I/O por item.

## Checklist de review

- [ ] Endpoint testado com N grande, não só N=1.
- [ ] Existe assert de teto de queries (não só "passou").
- [ ] Loops que acessam relação usam eager/prefetch.
- [ ] Chamadas HTTP em loop viraram batch/bulk.
- [ ] Teto novo/elevado tem justificativa no allowlist.
- [ ] Agregações pesadas estão no banco, não em Python.

## Anti-padrões

- "Funciona local" com 3 registros — N+1 só dói com dados reais. Teste com volume.
- Subir o teto silenciosamente pra "fazer o teste passar" — derrota o guardrail.
- Cache global onde precisa ser por-request (vaza dados entre usuários).
- `prefetch_related` seguido de `.filter()` na relação em Python (refaz query).
