---
description: Generate a complete vertical feature slice — Page/View + Controller(rx_notifier) + State + UseCase + Repository(interface+impl) + Gateway call + DI binding + route.
---

# /af-feature — full vertical feature slice

Use this when the user asks for a whole screen/feature end-to-end ("add a login
screen", "create a settings feature"). It crosses several concerns; for a single
piece (one use case, one repo, one route) use the granular command instead.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/08-mvvm-rxnotifier.md` — it is the
View/Controller spine and walks the vertical. Pull a second reference ONLY when
you reach that part of the slice: `04-usecases.md` for the use case,
`05-repository.md` for the repo/DTO, `03-di.md` for binding order,
`11-navigation.md` for the route. Read each only as you wire it.

## Steps (rename the anchors `Example`/`Feature`/`Item` to the real name)

1. **Controller.** Copy `assets/templates/mvvm/example_controller.dart` to
   `lib/feature/<feature>/controller/<feature>_controller.dart`. Use the
   rx_field idiom (`final RxNotifier<T> _x; T get x; set x`), inject use cases as
   `final` private fields, run logic via `execSingle` / `execCallback` (never
   unwrap `Either` by hand), and `dispose` every notifier.
2. **Page/View.** Copy `assets/templates/mvvm/example_page.dart` to
   `lib/feature/<feature>/page/<feature>_page.dart`. `_State extends
   BaseState<<Feature>Page, <Feature>Controller>`; read state ONLY inside
   `RxBuilder` (smallest subtree per change).
3. **UseCase.** Copy `assets/templates/usecase/example_use_case.dart` to
   `lib/domain/<feature>/<verb>_<noun>_use_case.dart`. Depend on the repo
   INTERFACE; write only `execute` (pure happy path, no try/catch).
4. **Repository.** Copy `i_example_repository.dart` + `example_repository.dart`
   from `assets/templates/repository/` to `lib/repository/<feature>/`. Impl
   injects `LoggedClient`, decodes the `ResponseDTO<T>` envelope, returns the DTO.
   Copy `example_dto.dart` for the DTO.
5. **Gateway call.** Add the path to `Endpoints` (template
   `assets/templates/gateway/endpoints.dart`) — the repo references
   `Endpoints.<name>`, never a literal.
6. **DI binding.** Copy `assets/templates/mvvm/example_binding.dart` to
   `lib/feature/<feature>/di/<feature>_binding.dart` →
   `registerFactory(() => <Feature>Controller(it()))`. Register the use case in
   `domain_binding.dart` and the repo (by interface) in `repository_binding.dart`.
7. **Route.** Add the `AppRouter` enum value + feature navigation + typed
   `context.pushTo<Feature>(...)` per `/af-navigation`.

## Wire / verify

- **Append `const <Feature>Binding()` to the features list in `app_di.dart`** —
  the binding file alone does nothing until it is in the list.
- Controllers are `registerFactory`; repos/use-cases are `registerSingleton`.
- Run `dart run build_runner build --delete-conflicting-outputs`, then
  `flutter analyze`.
