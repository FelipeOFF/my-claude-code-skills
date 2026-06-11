---
description: Set up the full push notifications (FCM + local notifications, 3 lifecycle handlers) and deep-link (Branch + deferred-nav) stack.
---

# /af-push-deeplink — push notifications + deep linking

Use this to stand up push notifications (FCM delivers data-only, the app renders
via local notifications) and/or inbound deep links (Branch behind an interface,
held until the user authenticates, then driving go_router). For ordinary in-app
navigation use `/af-navigation` instead.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/12-push-deeplink.md`. Touch
`04`/`05`/`11` only for the specific shared symbol you must create (token use
case, `PushResponseDto`, the `AppRouter` enum).

## Steps (rename `App`/`Feature`/`Example` to the real name)

1. **Firebase config.** Run `flutterfire configure`; confirm
   `lib/firebase/firebase_options.dart` exists.
2. **Push facade.** Copy `assets/templates/push_deeplink/push_notification_service.dart`.
   Wire the two store helpers + `AppDI.setupBasicInfrastructure()` to the real
   cache/DI. Ensure `PushResponseDto` exists (`code`, `title`, `message`,
   `image`, `icon`). The notification payload carries only `code`; the full DTO
   persists keyed by `code`.
3. **Token use case.** Add `SavePushTokenUseCase` (FCM token → repository) and
   register it (`/af-usecase`).
4. **Bootstrap order.** Copy `bootstrap_snippet.dart`:
   `registerBackgroundMessageHandler()` BEFORE `Firebase.initializeApp`, push
   `init()` after, Branch init last + non-blocking. The bg handler MUST be a
   top-level `@pragma('vm:entry-point')` function.
5. **Deep link interface + impl.** Copy `deep_link_service.dart`,
   `branch_deep_link_service.dart` (only file importing the vendor SDK),
   `deep_link_data.dart`. Persist-then-emit; validate Branch sessions (drop
   heartbeats); recursively string-key the map.
6. **Deferred-nav cubit + consumer.** Copy `deep_link_navigation_cubit.dart` +
   `deep_link_navigation_consumer.dart`. (This Cubit is the one app-global
   cross-cutting exception — do NOT model feature logic this way.) Provide the
   cubit above the router; wrap the shell child with
   `DeepLinkNavigationConsumer` (`listenWhen: prev.status != curr.status`).
7. **Native setup.** Follow `assets/templates/push_deeplink/platform_setup.md`
   for Android channel/Branch keys/intent-filters and iOS
   entitlements/Info.plist/AppDelegate. For iOS rich media add the Notification
   Service Extension target with `NotificationService.swift`.

## Wire / verify

- Android `default_notification_channel_id` MUST equal the Dart `_channel` id
  (`high_importance_channel`).
- iOS rich images need the extension + payload `mutable-content: 1` + `image`
  URL; call `contentHandler` in `defer` and implement
  `serviceExtensionTimeWillExpire`.
- Resume test: tap a link on login → held (`awaitingAuthentication`) → log in →
  fires (`navigationReady`); a killed-app link re-drives via
  `_processStoredFromPreviousSession`. Replace any real host with
  `https://api.example.com`.
