---
description: Add a single use case (extends AbstractUseCase, returns Either<AppError,T>) and wire it into a Controller + DI.
---

# /af-usecase — add one use case

Use this when a Controller needs to *do something* that is not pure UI state:
load data, submit a form, run a multi-step flow. One use case = one action = one
file. Pure UI toggles are `RxNotifier` fields, not use cases.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/04-usecases.md`. Do not read the
others — the Controller-side ladder you wire into is summarized there. Touch
`05-repository.md` only if the repository the use case calls does not yet exist.

## Steps (rename `Feature`/`Example`/`Item` to the real name)

1. **Pick the base + PARAM.** Single value out → `AbstractUseCase<PARAM,
   RESULT>`; live source → `AbstractStreamUseCase`. No input → `void`; one value
   → that type; many → a colocated `<Name>Params` class below the use case.
2. **Copy a template.** Repo pass-through or params object → copy
   `assets/templates/usecase/example_use_case.dart`. Composes other use cases →
   `assets/templates/usecase/example_orchestrating_use_case.dart`. Save to
   `lib/domain/<feature>/<verb>_<noun>_use_case.dart`.
3. **Depend on the repo INTERFACE** (`IExampleRepository`) as a `final` private
   field; `const` constructor when there is no logic. Never import a repo impl or
   Dio.
4. **Write only `execute`** — pure happy path: call the repo / compose sub-use-
   cases, return `RESULT` or throw. No try/catch, no dartz, no `Either` (the base
   `call()` is the single boundary).
5. **One-time base scaffold** (if missing): copy `abstract_use_case.dart`,
   `abstract_stream_use_case.dart`, `app_error.dart`, `dio_error_mapper.dart`,
   `either_helpers.dart` from `assets/templates/usecase/` into `lib/domain/`.

## Wire / verify

- **Register in `domain_binding.dart`**: `it.registerSingleton(<Feature>UseCase(it()));`
  — `registerSingleton` (use cases are stateless), one `it()` per dependency.
- **Invoke from the Controller** via `execSingle(param, useCase)` /
  `execCallback(...)` — never `.call()` + manual `fold` in the Controller.
- Run `dart run build_runner build --delete-conflicting-outputs` if a DTO
  changed, then `flutter analyze`.
