---
description: Set up or extend the dio gateway/client/interceptor/endpoints backend-call layer (AbstractGateway, LoggedClient/NonLoggedClient, auth + refresh, ResponseDto envelope).
---

# /af-gateway — backend transport layer

Use this when the task is between a repository and the wire: bootstrap the
network layer, add an endpoint family or a concrete client, wire/reorder
interceptors, add an SSL-pinned host, or stand up a gRPC channel. To write the
repository that consumes these clients, use `/af-repository` instead.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/06-gateway-backend.md`. The
`AppError` funnel it mentions is owned by `04-usecases.md` — only read that if
`DioException.asAppError()` / the `AppError` hierarchy does not yet exist.

## Steps (rename `App`/`Feature`/`Example` to the real name)

1. **Base client.** Copy `assets/templates/gateway/abstract_gateway.dart`
   (`DioForNative` base: options, HTTP adapter choice, SSL hook, the ordered
   interceptor assembly, and the `LoggedClient`/`NonLoggedClient` families).
2. **Interceptors.** Copy `token_interceptor.dart`,
   `refresh_token_interceptor.dart`, `retry_interceptor.dart` into
   `lib/gateway/interceptor/`. Order is load-bearing:
   debug → retry → logger → encrypt → apiKey → **refresh → token** (refresh
   BEFORE token-inject). `additionalInterceptors` returns `[refresh, token]`.
3. **Concrete clients.** Copy `assets/templates/gateway/app_client.dart`. Keep
   all three singletons; the refresh-only client MUST stay a plain
   `NonLoggedClient` (no auth interceptors) or refresh recurses on a 401.
4. **Endpoints.** Copy `assets/templates/gateway/endpoints.dart`; add private
   prefix consts + public paths. Use `{param}` placeholders + `Endpoints.fill(...)`.
5. **(gRPC, optional)** Copy `abstract_grpc_gateway.dart`; point the channel at
   `env.grpcUrl` and expose the generated `...ServiceClient` getters.
6. Replace any real host with `https://api.example.com`.

## Wire / verify

- **DI**: `registerLazySingleton` the interceptors, `registerSingleton` the
  clients (constructor-inject the interceptors) in `gateway_binding.dart` /
  `service_binding.dart` — see `/af-di`.
- Confirm `DioException.asAppError()` maps 401 → `Logout`, offline →
  `NetworkException`, parsed body → `Default`, else → `UnknownException`, and the
  synthetic-401 path routes to `Logout`.
- `flutter analyze`; verify SSL pinning on a real prod build.
