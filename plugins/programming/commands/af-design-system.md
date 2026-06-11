---
description: Set up the design system — ThemeExtension token palettes accessed via BuildContext extensions (context.colors/text/icons), raw hex in one class, atoms.
---

# /af-design-system — design tokens + context surface

Use this to stand up the design system, add a token (color / text style /
decoration / spacing) or token group, add an icon or a token-consuming
component, or migrate a widget off a hardcoded `Color(0x...)` / `Theme.of`.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/09-design-system.md`. Do not read
the others — feature Views style themselves through the `context.*` surface this
command defines.

## Steps (rename `App`/`Example` to the real name)

1. **Raw palette (the ONLY hex).** Copy
   `assets/templates/design_system/app_color.dart`; add brand/neutral/feedback
   literals to `AppColor` (`@protected static const`, private `_()` ctor). Use a
   `MaterialColor` swatch where `.shade*` is needed. Widgets NEVER read `AppColor`.
2. **Token groups.** Colors → copy `app_colors_theme.dart`, map semantic fields
   onto `AppColor.*`. Other groups (`AppTextTheme`, `AppIconsTheme`,
   `AppDecorationTheme`, `AppSpacingTheme`) → follow the same quartet in
   `app_theme.dart`. Every field MUST appear in: field decl, `._` ctor,
   `copyWith`, AND `lerp` — thread it through all four or `lerp` drops it.
3. **ThemeData.** In `app_theme.dart` list EVERY token group in
   `extensions: <ThemeExtension<dynamic>>[...]`. Non-const decorations attach via
   `.copyWith(extensions: [...])` after the const groups.
4. **Context surface.** In `app_context_extensions.dart` add one thin getter per
   group: `AppColorsTheme get colors => AppColorsTheme.of(this);`. This is the
   ENFORCED access path widgets import.
5. **Wire the app.** Pass `theme: appDarkTheme` to `MaterialApp` (already wired
   in the app scaffold).
6. **Atoms.** Copy `app_icons.dart` (`enum AppIcons`: asset path + a11y label)
   and `app_icon.dart` (renderer). Declare the SVG assets in `pubspec.yaml`.
7. **Components.** Copy `example_component.dart`; style entirely from `context.*`,
   optional override param falling back to a token
   (`color ?? context.colors.primary`). No raw `Color`, `Theme.of`, or `AppColor`
   in a component body.

## Wire / verify

- `of()` uses `!` — a token group missing from `ThemeData.extensions` throws at
  the first `context.x` call. Adding a group = update its class file AND the
  `extensions` list.
- `flutter analyze`; verify tokens resolve below `MaterialApp` at runtime.
