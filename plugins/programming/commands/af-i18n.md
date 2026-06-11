---
description: Add a localized string (edit ARB -> intl_utils:generate -> context.s.key) or set up i18n from scratch — asks which languages to support — incl MaterialApp wiring.
---

# /af-i18n — localization

Use this to add a user-facing string, add a placeholder or ICU plural, read a
string from non-widget code, switch the app's locale at runtime, or wire i18n
into a fresh app. Strings always go through l10n — never hardcode UI text.

## Ask which languages first

i18n here is **language-agnostic** — any locale works (`en`, `pt`, `es`, `fr`,
`de`, `ja`, `zh`, `ar`, `he`, …), Latin or not, LTR or RTL. Before scaffolding
i18n or adding the first locale, **ask the user which languages to support** with
`AskUserQuestion` (multi-select; offer a few common ones and let them add their
own). Then:

- create one `lib/res/l10n/intl_<code>.arb` per chosen language, all with the
  SAME keys (translate the values, or leave the English value as a clearly-marked
  TODO to translate);
- set `main_locale` in the `flutter_intl:` block to the primary language;
- `supportedLocales` derives automatically from the ARB files present — never
  hand-list it.

The shipped templates demo `en` + `pt`, but `ja` or `ar` is the identical move: a
new `intl_<code>.arb` with the same keys + `dart run intl_utils:generate`.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/14-i18n.md`. The codegen config
(`flutter_intl:` block, analyzer excludes) already ships under
`assets/templates/config/` — do not re-emit it.

## Add a localized string (the common path)

1. **Edit `lib/res/l10n/intl_en.arb`** (main locale): add the key, value, and a
   `@key` metadata block (`description`; plus a `placeholders` block if it has a
   `{placeholder}` or is an ICU plural — type plural counts as `int`).
2. **Edit EVERY other locale** (`intl_pt.arb`, …) with the SAME key. A key only
   in `en` falls back to `en` and is never translated.
3. **Regenerate:** `dart run intl_utils:generate` (separate pass from
   `build_runner`). Rewrites `lib/generated/l10n.dart`.
4. **Use it.** Widget: `context.s.keyName` (import
   `package:app/common/util/localization_context_ext.dart`). Non-widget code:
   `AppLocalizations.current.keyName`. Placeholders are method args:
   `context.s.greeting('Alex')`, `context.s.itemsCount(3)`.

## Set up i18n from scratch (once per app)

1. For each language the user picked, create `lib/res/l10n/intl_<code>.arb`
   (start from `assets/templates/i18n/intl_en.arb` as the key template;
   `intl_pt.arb` shows a translated mirror). Keys must be identical across all.
2. Copy `localization_context_ext.dart` to `lib/common/util/` (the `context.s`
   shortcut).
3. Copy `locale_change_service.dart` to `lib/common/service/`; register it:
   `it.registerLazySingleton<LocaleChangeService>(LocaleChangeService.new);`
   (see `/af-di`).
4. Wire `MaterialApp.router` from `app_localization_wiring.dart` — the four
   `localizationsDelegates` (`AppLocalizations.delegate` +
   `GlobalMaterial/Widgets/Cupertino` from
   `package:flutter_localizations/flutter_localizations.dart`),
   `supportedLocales: AppLocalizations.delegate.supportedLocales`, and
   `locale: _locale`.
5. `dart run intl_utils:generate`, then `flutter analyze`.

## Wire / verify

- `class_name` is `AppLocalizations` (set in the `flutter_intl:` pubspec block).
  Use `AppLocalizations.of(context)` / `AppLocalizations.current`, not `S`.
- `lib/generated/**` is gitignored + analyzer-excluded; never hand-edit it. Run
  `intl_utils:generate` after every ARB change.
- `context.s` for l10n collides with the design-system spacing `context.s` if
  both are imported into one file — keep them in separate import scopes (see the
  gotchas in `14-i18n.md`).
