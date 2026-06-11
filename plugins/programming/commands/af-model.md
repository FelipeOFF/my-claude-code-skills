---
description: Add a data model — freezed + json_serializable DTO (req/res), enum, sealed union, custom converter, domain entity + toEntity() mapper.
---

# /af-model — add a data model

Use this when modeling data: a request body the app sends, a response it
receives (nested objects, lists of child DTOs), a `@JsonValue` enum, a
sealed/union type, a custom `JsonConverter`, or a plain domain entity plus the
`toEntity()` mapper. The repo that returns these DTOs and decodes the envelope is
`/af-repository`; mappers and enum labels as extensions are `/af-feature`'s glue.

## Read exactly one reference

Read ONLY `skills/absolute-flutter/references/13-model-freezed.md`. Touch
`05-repository.md` only for the shared `ResponseDTO<T>`/`PageDto<T>` envelopes,
and `10-extensions.md` only when adding enum-label / DTO-mapper extensions.

## Steps (rename `Example`/`Item` to the real concern)

1. **Pick direction + folder.** Sending → `model/<concern>/req/`. Receiving →
   `model/<concern>/res/`. Copy the matching template from
   `assets/templates/model/` (`example_request_dto.dart` /
   `example_response_dto.dart`) and rename `Example` throughout (class, file,
   fields).
2. **Declare fields.** One `const factory X({ ... }) = _X;` with `@JsonKey(name:
   'wireKey')` on every field. Response fields all nullable; request fields
   nullable (omit-on-null) or `@Default(...)`. `fromJson` is the LAST factory.
3. **Enums / unions as needed.** Wire-mapped enum → `@JsonValue` per constant
   (`example_enum.dart`). One-of-N value → freezed union with named const
   factories + a `fromStatus` mapping (`example_sealed_model.dart`). Keep
   labels/icons OFF the model — put them in an extension.
4. **Custom converter (only if freezed can't map the type).** Copy
   `assets/templates/config/json_converter.dart` into `common/helper/`, set the
   `<DartType, WireType>` args, annotate the field with `@XSerializer()`.
5. **Domain entity + mapper (only if warranted).** If a call site needs
   non-nullable / reshaped fields, copy `example_entity.dart` +
   `example_mapper_ext.dart`; the mapper defaults the DTO's nullable fields.
   Otherwise return the DTO directly.
6. **Codegen.** `dart run build_runner build --delete-conflicting-outputs` to
   emit the `.freezed.dart` / `.g.dart` siblings for every DTO touched. Commit
   them; never hand-edit.

## Wire / verify

- Nested freezed DTOs need `explicit_to_json: true` in `build.yaml` — without it
  nested `toJson` silently emits `Instance of '...'`.
- A method (e.g. `toEntity()`) on a frozen class needs a `const X._();` private
  ctor; prefer an extension to avoid it.
- `flutter analyze` (generated files are analyzer-excluded — a lint is in YOUR
  source).
