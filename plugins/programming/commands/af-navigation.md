---
description: Add a go_router route via the enum route table + per-feature BaseNavigation + typed context.pushToXxx extension.
---

# /af-navigation — add a route

Use this to add a screen + its route, a bottom-nav tab, a typed navigation call,
a page transition, or to wire deep-link redirect logic. The View/Controller a
route builds is `/af-feature`; this command only wires the route.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/11-navigation.md`. The deep-link
state machine it mentions is owned by `12-push-deeplink.md` — read that only if
you are wiring inbound deep links, not for an ordinary route.

## Steps (rename `Feature`/`Example`/`Home` to the real name)

1. **Infrastructure (once per app).** Copy from
   `assets/templates/navigation/`: `app_router_enum.dart` (save as
   `navigation/app_router.dart`), `router.dart`, `app_go_route.dart`,
   `transitions.dart`, `base_navigation.dart`, and `nav_context_ext.dart` (into
   `common/util/`). `app_widget.dart` uses `routerConfig: AppRouter.config`.
2. **Add the enum value.** In `app_router.dart` add one `AppRouter` value:
   `featureDetail('/feature/:featureId', 'FeatureDetail')`. Use `:param` for path
   params; flag `isBottomNavigation: true` for a tab, `requiresAuthentication:
   false` for a public screen (default `true`). Never use raw path/name strings
   at a call site.
3. **Feature navigation.** Create
   `navigation/feature/<feature>_navigation.dart` extending `BaseNavigation`,
   returning an `AppGoRoute(router: AppRouter.featureDetail, defaultTransition:
   Transitions.slideLeft, builder: (c, s) => FeaturePage(featureId:
   s.pathParameters['featureId'] ?? ''))`. The builder forwards only ROUTE inputs
   and returns a `const` page (it resolves its Controller from DI).
4. **Register.** Add one line to `AppNavigations.listOfNavigation` in
   `app_navigations.dart`: `FeatureNavigation()`. The root `router.dart` never
   grows.
5. **Typed call site.** In `nav_context_ext.dart` add
   `Future<void> pushToFeature(String id) => pushNamed(AppRouter.featureDetail.name,
   pathParameters: {'featureId': id});`. Call as `context.pushToFeature(id)`.
6. **Bottom-nav tab?** Add a `mainXxx` value (`isBottomNavigation: true`) and an
   `AppGoRoute(... parentNavigatorKey: NavigationKey.mainNavigatorKey, pageBuilder:
   (c, s) => const NoTransitionPage(child: TabPage()))` inside the `ShellRoute`
   in `shell_route.dart`.

## Wire / verify

- `pushNamed` takes `.name`; `go`/`initialLocation` take `.path` — do not mix.
- go_router 14: use `state.uri.path` / `state.uri.queryParameters` /
  `state.pathParameters`, never `state.location`.
- Keep the enum file at `navigation/app_router.dart` (no `app_routers.dart`
  alias). `flutter analyze`.
