---
description: Map an EXISTING Flutter project against this architecture — report each concern as Present / Partial / Missing with evidence, then a prioritized adoption plan referencing which command closes each gap.
---

# /af-map-project — audit an existing Flutter project

Use this on the user's CURRENT working-directory Flutter project to report which
parts of this architecture exist, which are partial, and which are missing — with
a prioritized adoption plan. This command **does NOT generate an app or edit
code**: it globs `lib/`, reads `pubspec.yaml`, greps for marker symbols, and
writes a report only.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/01-architecture.md` for the target
shape, plus the concern index table in `skills/absolute-flutter/SKILL.md` (the 12
concerns + which reference owns each). Do NOT read the leaf references — grep the
project instead of reading whole files.

## Scan (read-only)

1. Read `pubspec.yaml`; note presence of `rx_notifier`, `dartz`, `get_it`,
   `dio`, `drift`, `go_router`, `firebase_messaging`, Branch.
2. Glob `lib/` for the folder layout. Grep for each concern's marker symbol:

   | # | Concern | Marker(s) to grep | Command to close |
   |---|---|---|---|
   | 1 | architecture / tree | `lib/feature`, `lib/domain`, `lib/repository`, layered split | `/af-bootstrap` |
   | 2 | dart-conventions | `package:<pkg>/` imports vs `../`; `analysis_options.yaml` lint rules | (manual) |
   | 3 | di | `AbstractBinding`, `AppDI`, `_listOfBinding` | `/af-di` |
   | 4 | usecases | `AbstractUseCase`, sealed `AppError`, `Either<` | `/af-usecase` |
   | 5 | repository | `I*Repository` + impl pairs, `ResponseDTO`, `toEntity()` | `/af-repository` |
   | 6 | gateway-backend | `AbstractGateway`, `LoggedClient`, interceptors, `Endpoints` | `/af-gateway` |
   | 7 | cache-database | `drift`, `FuCache`, read-through TTL | (cache reference) |
   | 8 | mvvm-rxnotifier | `BaseController`, `RxNotifier`, `RxBuilder`, `BaseState` | `/af-feature` |
   | 9 | design-system | `ThemeExtension`, `context.colors`, single `AppColor` hex class | `/af-design-system` |
   | 10 | extensions | `common/` mixins, per-type extensions | (extensions reference) |
   | 11 | navigation | `enum AppRouter`, `go_router`, `BaseNavigation`, `pushTo*` | `/af-navigation` |
   | 12 | push-deeplink | `firebase_messaging`, `onBackgroundMessage`, `DeepLinkService` | `/af-push-deeplink` |

3. Flag anti-patterns as **refactorable**: `flutter_bloc`/Cubit carrying feature
   logic, relative `../` lib imports, raw `Color(0x...)` / `Theme.of` in widgets,
   `DioException` handling outside `asAppError()`, `Either` unwrapped in a
   Controller, status-code checks scattered outside the funnel.

## Report (do not edit code)

For EACH of the 12 concerns output: **Present / Partial / Missing**, one line of
**evidence** (file path or grep hit, or "no match"), and the **command** to close
the gap. Then a **prioritized adoption plan** ordered inside-out:

1. Error model + use-case base (`/af-usecase`)
2. DI bootstrap (`/af-di`)
3. Gateway/transport (`/af-gateway`)
4. Repository layer (`/af-repository`)
5. Design system + navigation (`/af-design-system`, `/af-navigation`)
6. Feature slices / MVVM migration (`/af-feature`) — UI last
7. Push + deep links if relevant (`/af-push-deeplink`)

Keep it a gap report + plan. Generate nothing.
