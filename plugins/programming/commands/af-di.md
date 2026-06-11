---
description: Wire dependency injection — add or order an AbstractBinding (get_it) for a layer or feature, in the two-phase ordered bootstrap.
---

# /af-di — wire dependency injection

Use this when you add a binding for a new layer or feature, register a
Controller / use case / repository, or fix init order / a "not registered"
error. A trivial rename does not need this; adding or ordering a registration
does.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/03-di.md`. Do not read the layer
references — this command only wires what they produce.

## Steps (rename `Example`/`Feature` to the real name)

1. **Bootstrap a fresh app (once).** Copy `assets/templates/di/abstract_binding.dart`
   and `app_di.dart` into `lib/di/`. Keep the two ordered lists and the order:
   `Environment` first in phase 1, `Domain` last in phase 1; phase 2 spreads the
   infra prefix (`.skip(...)`) then appends mappers + features. Call
   `setupBasicInfrastructure()` then `setupRemainingBindings()` from `main`.
2. **Add a feature binding.** Copy `assets/templates/di/example_feature_binding.dart`
   to `lib/feature/<feature>/di/<feature>_binding.dart`. `registerFactory(() =>
   <Feature>Controller(it()))` — Controllers are FACTORY (fresh `RxNotifier`
   state per screen), bare `it()` per dep.
3. **Add a layer registration.** Open the matching
   `lib/di/<layer>/<layer>_binding.dart` (copy
   `assets/templates/di/example_layer_binding.dart` for a new one). Bind
   data/domain/repository by **interface**, eager:
   `it.registerSingleton<IFooRepository>(FooRepository(it(), it()));`. Use cases
   go in the single `DomainBinding`. Anything depending on the async DB must
   `await it.getAsync<AbstractDatabase>()`.

## Wire / verify

- **Append `const <Feature>Binding()` to `_listOfBinding` in `app_di.dart`** in
  the features section — a binding not in the list NEVER registers. Grep for
  `_listOfBinding` rather than reading the whole file.
- Order in `_listOfBasicInfrastructure` is load-bearing: env first, domain last
  among infra; register a thing before whatever depends on it.
- Kinds: data/domain/repository → eager `registerSingleton<I>`; cheap services →
  `registerLazySingleton`; DB → `registerSingletonAsync`; Controllers →
  `registerFactory`. Keep exactly one registration per type.
- Preserve codegen markers (`//REPOSITORY_BINDING`, `//DATA_SOURCE_BINDING`).
- `flutter analyze`; app must boot without a resolution throw.
