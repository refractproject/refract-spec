# Changelog
All notable changes to the Refract project will be documented in this file.

## Unreleased changes
- Moved Compact Refract out of base specification

## [0.6.0] - 2015-12-15

### Breaking

#### API Description Namespace
- Changed `href` in HTTP Request Message from type `Href` to `Templated Href`
- Added `hrefVariables` as an attribute to HTTP Request Message.

#### Parse Result Namespace
- Added Origin Link Relation
- Added Inferred Link Relation

## [0.4.0] - 2015-08-15

### Breaking

#### API Description Namespace
- Changed Data Structure.
- Clarified relation between Copy in `content` and `description` in `attributes`.
- Added Copy to the following:
  - Resource
  - Transition
  - HTTP Transaction
  - HTTP Message Payload
- Corrected `content` of HTTP Headers.

## [0.3.0] - 2015-08-07

### Breaking

#### Refract
- Renamed `class` metadata property to `classes`. [[RFC 0003]]

#### Namespaces
- Merged API and Resource namespaces. [[RFC 0002]]
  - Renamed `parameters` to `hrefVariables`
  - Renamed `attributes` to `data`
  - Added `contentTypes` to `Transition` element
- Renamed MSON namespace to Data Structures namespace. [[RFC 0001]]

## [0.2.0] - 2015-05-28

- Use member elements in objects.
- API namespace.
- Canonical resource namespace.
- Simplify attributes, meta, and object properties.
- MSON namespace.
- Add referencing.

## [0.1.0] - 2015-02-09

- Initial release.

[0.4.0]: https://github.com/refractproject/refract-spec/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/refractproject/refract-spec/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/refractproject/refract-spec/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/refractproject/refract-spec/tree/v0.1.0

[RFC 0004]: https://github.com/refractproject/rfcs/blob/master/text/0004-clarify-api-namespace.md
[RFC 0003]: https://github.com/refractproject/rfcs/blob/master/text/0003-class-rename.md
[RFC 0002]: https://github.com/refractproject/rfcs/blob/master/text/0002-clarity-api-description.md
[RFC 0001]: https://github.com/refractproject/rfcs/blob/master/text/0001-mson-rename.md
