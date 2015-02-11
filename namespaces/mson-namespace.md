# MSON Namespace

This document extends [Refract][]'s [JSON Namespace][] with elements necessary to
build [MSON][] DOM.

# Terminology

## Expanded Element

MSON is built around the idea of defining recursive data structures. To provide abstraction, for convenience reasons and to not repeat ourselves these structures can be named and reused. In MSON, the reusable data structures are called _Named Types_.

Often, before an MSON DOM can be processed referenced _Named Types_ have to be resolved. Resolving references to _Named Types_ is tedious and error prone. As such parser can resolve references and produce a complete MSON DOM, that is a DOM that does not include unresolved references to other data structures. This is referred to as _reference expansion_ or simply _expansion_.

In other words, an expanded element is such an element that does not contain _Identifier_ (defined bellow) to any other elements but those defined in JSON or MSON namespaces.

The expanded DOM MUST, however, keeps the track of what data structure was expanded and what from where.

## Base Element

In MSON, every data structure is a sub-type of another data structure, and, in transition, it is directly or indirectly derived from one of the MSON _Base Types_. This is expressed as an inheritance of elements in MSON DOM. Where the predecessor of an element is referred to as element's _Base Element_.

Note not every MSON _Base Type_ is presented in JSON namespace primitive types and vice versa, see the table bellow:

### JSON Namespace vs. MSON built-in types

| JSON Namespace |   MSON  |
|:--------------:|:-------:|
|     boolean    | boolean |
|     string     |  string |
|     number     |  number |
|      array     |  array  |
|     &nbsp;     |   enum  |
|     object     |  object |
|      null      |  &nbsp; |

# MSON DOM Elements Definition

## Identifier (Enum)

Identifier of an element in MSON DOM.

### Members

- (string)
- (Distinct Element)
    - `element`: id
    - `content`: (string)

## Distinct Element (Element)

Abstract element representing an element that can be referenced or is a reference to another element.

### Properties

- `element` (Identifier, required) - identifier of this element's base element
- `attributes`
    - `id` (Identifier) - identifier of this element
    - `ref` (Identifier) - reference to expanded element


### Example

```json
{
    "element": "number",
    "attributes": {
        "id": "my-number"
    },
    "content": 42
}
```

which is identical to:

```json
{
    "element": {
        "element": "id",
        "content": "number"
    },
    "attributes": {
        "id": "my-number"
    },
    "content": 42
}
```

and can be referred to as a _base element_:

```json
{
    "element": "my-number"
}
```

which _expands_ to:

```json
{
    "element": "number",
    "attributes": {
        "ref": "my-number"
    },
    "content": 42
}
```

## MSON Element (Distinct Element)

- `attributes`
    - `typeAttributes` (array[enum])
        - required (string)
        - fixed (string)
        - variable (string)
    - `sample`
    - `default`
    - `validation`
    - `description`


### Example

#### MSON

```
- id: 1
```

#### MSON DOM

```json
{
    "element": "object",
    "content": [
        {
            "element": "property",
            "attributes": {
                "name": "id"
            },
            "content": {
                "element": "string",
                "content": "1"
            }
        }
    ]
}
```


#### MSON

```
- id: 42 (required, fixed)
```

#### MSON DOM

```json
{
    "element": "object",
    "content": [
        {
            "element": "property",
            "attributes": {
                "name": "id",
                "typeAttributes": ["required", "fixed"]
            },
            "content": {
                "element": "string",
                "content": "42"
            }
        }
    ]
}
```

#### MSON

```
- id (number)
    - default: 0
```

#### MSON DOM

```json
{
    "element": "object",
    "content": [
        {
            "element": "property",
            "attributes": {
                "name": "id",
                "default": {
                    "element": "number",
                    "content": 0
                }
            },
            "content": {
                "element": "number",
                "content": null
            }
        }
    ]
}
```

## Enum Type (MSON Element)

- `element`: enum (string, required, fixed)
- `content` (array[MSON Element])

### Example

#### MSON

```
TODO:
```

#### MSON DOM

```json
TODO:
```

TODO:
- one of
- mixin
- named type example




[Refract]: https://github.com/refractproject/refract-spec/blob/master/refract-spec.md
[JSON Namespace]: https://github.com/refractproject/refract-spec/blob/master/namespaces/json-namespace.md
[MSON]: https://github.com/apiaryio/mson
