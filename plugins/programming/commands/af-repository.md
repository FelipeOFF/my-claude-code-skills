---
description: Add a repository (interface + impl + DTO + envelope decode) and its DI binding.
---

# /af-repository — add a repository

Use this when adding a repository for a new backend resource, adding a method to
an existing one, or wiring a DTO + its envelope decode. The use case that calls
it and owns the `Either`/error funnel is `/af-usecase`; the client + endpoints it
depends on are `/af-gateway`.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/05-repository.md`. Touch
`06-gateway-backend.md` only if the `LoggedClient` / `Endpoints` it needs do not
yet exist.

## Steps (rename `Example`/`Item`/`Feature` to the real concern)

1. **Interface + impl, side by side** in `lib/repository/<concern>/`. Copy
   `i_example_repository.dart` + `example_repository.dart` from
   `assets/templates/repository/`. Interface is `I`-prefixed; impl `implements
   IFoo` with a positional constructor injecting `LoggedClient`.
2. **Contract.** Each method `Future<ReturnDto> verbNoun(Param p)`. Reads return
   the DTO (or `ResponseDTO<PageDto<Dto>>` for lists); mutations return
   `Future<void>`/`Future<bool>`. Import only the DTOs + request params.
3. **Impl body.** `await _client.<verb>(Endpoints.x, ...)` then
   `ResponseDTO<Dto>.fromJson(safeMapOf(response.data), (j) => Dto.fromJson(safeMapOf(j)))`
   and return `.data ?? const Dto()`. Let exceptions propagate — do NOT catch or
   touch `Either` here.
4. **DTO.** Copy `assets/templates/repository/example_dto.dart`; declare wire
   fields (all nullable), keep the `const Dto._();` private ctor, add `toEntity()`
   only if a call site needs the domain entity. No separate mapper-class layer.
5. **Shared envelopes (once per app)** if missing: copy `response_dto.dart`,
   `page_dto.dart` into `model/api/common/` and `safe_map.dart` into `common/util/`.
6. **Endpoint.** Add the path constant to `Endpoints` (`/af-gateway`).
7. **Codegen.** `dart run build_runner build --delete-conflicting-outputs` for
   the `.freezed.dart` / `.g.dart` parts.

## Wire / verify

- **DI**: in `repository_binding.dart` add
  `it.registerSingleton<IFoo>(FooRepository(it()));` immediately ABOVE the
  load-bearing `//REPOSITORY_BINDING` anchor (never delete/move it). One `it()`
  per dependency.
- `flutter analyze`.
