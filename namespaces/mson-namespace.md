# MSON Namespace

This document extends [Refract][] Specification with new element types necessary to build [MSON][] DOM.

# Content

This namespace defines following elements:

1. General-purpose elements
    1. [Select](#select-distinct-element)
    1. [Option](#option-distinct-element)

1. MSON DOM-specific elements
    1. [MSON Element](#mson-element-distinct-element)
    1. [Boolean Type](#boolean-type-jsonboolean-type)
    1. [String Type](#string-type-jsonstring-type)
    1. [Number Type](#number-type-jsonnumber-type)
    1. [Array Type](#array-type-jsonarray-type)
    1. [Object Type](#object-type-jsonobject-type)
    1. [Property Type](#property-type-jsonproperty-type)
    1. [Enum Type](#enum-type-mson-element)

# About this Document

This document conforms to RFC 2119, which says:

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

[MSON][] is used throughout this document.

## Expanded Element

MSON is built around the idea of defining recursive data structures. To provide abstraction, for convenience reasons and to not repeat ourselves, these structures can be named (using an _identifier_) and reused. In [MSON][], the reusable data structures are called _Named Types_.

Often, before an MSON DOM can be processed, referenced _Named Types_ have to be resolved. Resolving references to _Named Types_ is tedious and error prone. As such an MSON processor can resolve references to produce a complete MSON DOM. That is, a DOM that does not include unresolved references to other data structures. This is referred to as _reference expansion_ or simply _expansion_.

In other words, an expanded element is one that does not contain any _Identifier_ (defined bellow) referencing any other elements than those defined in JSON or MSON namespaces.

The expanded DOM MUST, however, keep the track of what data structure was expanded and what from where.

## Base Element

In MSON, every data structure is a sub-type of another data structure, and, therefore, it is directly or indirectly derived from one of the MSON _Base Types_. This is expressed as an inheritance of elements in MSON DOM. Where the predecessor of an element is referred to as element's _Base Element_.

Note: Not every MSON _Base Type_ is presented in JSON namespace primitive types and vice versa, see the table bellow:

### Type comparison

| JSON primitive |      Refract     | MSON Base Type | MSON Namespace |
|:--------------:|:----------------:|:--------------:|:--------------:|
|     boolean    |  Boolean Element |     boolean    |  Boolean Type  |
|     string     |  String Element  |     string     |   String Type  |
|     number     |  Number Element  |     number     |   Number Type  |
|      array     |   Array Element  |      array     |   Array Type   |
|        -       |         -        |      enum      |    Enum Type   |
|     object     |  Object Element  |     object     |   Object Type  |
|      null      |   Null Element   |        -       |        -       |
|        -       | Property Element |        -       |  Property Type |

# General Purpose Elements

General purpose elements defined inside MSON namespaces but possibly reusable in another domain.

## Select (Element)

Element representing selection of options. Every item of content array represents one possible option.

### Properties

- `element`: select (string, fixed)
- `content` (array[Option])

## Option (Element)

One choice in the selection.

### Properties

- `element`: option (string fixed)
- `content` (enum)
    - (Element)
    - (array[Element])

### Examples

```html
<select>
  <option>Volvo</option>
  <option>Saab</option>
</select>
```

```json
{
    "element": "select",
    "content": [
        {
            "element": "option",
            "content": [
                {
                    "element": "string",
                    "content": "volvo"
                }
            ]
        }
        {
            "element": "option",
            "content": [
                {
                    "element": "string",
                    "content": "Saab"
                }
            ]
        }
    ]
}
```

# MSON DOM Elements

## MSON Element (Element)

Base element for every MSON element.

The MSON Element adds attributes representing MSON _Type Definition_ and _Type Sections_.

Note: In MSON DOM _Nested Member Types_ _Type Section_ is the `content` of the element.

### Properties

- `attributes`
    - `typeAttributes` (array) - _Type Definition_ attributes list, see _Type Attribute_  
        - (enum[string])
            - required
            - optional
            - fixed
            - sample
            - default
    - `variable` (boolean) - Element content is _Variable Value_
    - `sample` (MSON Element) - Alternative sample value for _Member Types_
    - `default` (MSON Element) - Default value for _Member Types_
    - `validation` - Not used, reserved for a future use
    - `description` - Combined description of an MSON Element

## Boolean Type (Boolean Element)

- Include [MSON Element][]

## String Type (String Element)

- Include [MSON Element][]

## Number Type (Number Element)

- Include [MSON Element][]

## Array Type (Array Element)

- Include [MSON Element][]

## Object Type (Object Element)

- Include [MSON Element][]
- `content` (array, required)
    - (Property Element)
    - (Select)

## Property Type (Property Element)

- Include [MSON Element][]

## Enum Type (MSON Element)

Enumeration type. Exclusive list of possible elements. The elements in content's array MUST be interpreted as mutually exclusive.

### Properties

- `element`: enum (string, fixed)
- `content` (array[MSON Element])

### Examples

#### MSON

```
- tag (enum[string])
    - red
    - green
```

#### MSON DOM

```json
{
    "element": "object",
    "content": [
        {
            "element": "property",
            "attributes": {
                "name": "tag"
            },
            "content": {
                "element": "enum",
                "content": [
                    {
                        "element": "string",
                        "content": "red"
                    },
                    {
                        "element": "string",
                        "content": "green"
                    }
                ]
            }
        }
    ]
}
```

## Examples

### Anonymous Object Type

#### MSON

```
- id: 42
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
                "content": "42"
            }
        }
    ]
}
```

### Type Attributes

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

### Default Value

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

### One Of

#### MSON

```
- city
- One Of
    - state
    - province
```

#### MSON DOM

```json
{
    "element": "object",
    "content": [
        {
            "element": "property",
            "attributes": {
                "name": "city"
            }
        },
        {
            "element": "select",
            "content": [
                {
                    "element": "option",
                    "content": [
                        {
                            "element": "property",
                            "attributes": {
                                "name": "state"
                            }
                        }
                    ]
                },
                {
                    "element": "option",
                    "content": [
                        {
                            "element": "property",
                            "attributes": {
                                "name": "province"
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
```

### Mixin

#### MSON

```
- id
- Include User
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
            }
        }
        {
            "element": "ref",
            "content": "#User"
        }
    ]
}
```

**versus new refract?**

```json
{
    "element": "object",
    "content": [
        {
            "element": "property",
            "attributes": {
                "name": "id"
            }
        }
        {
            "element": "extend",
            "content": {
                "element": "ref",
                "content": "#User"
            }
        }
    ]
}
```

### Named Type

#### MSON

```
# Address (object)

Description is here! Properties to follow.

## Properties

- street
```

#### MSON DOM

```json
{
    "element": "object",
    "attributes": {
        "id": "Address",
        "description": "Description is here! Properties to follow."
    },
    "content": [
        {
            "element": "property",
            "attributes": {
                "name": "street"
            }
        }
    ]
}
```

**versus new refract?**

```json
{
    "element": "type"
    bah how do I inherit from object and yet add properties? 
}
```



[Refract]: https://github.com/refractproject/refract-spec/blob/master/refract-spec.md
[JSON Namespace]: https://github.com/refractproject/refract-spec/blob/master/namespaces/json-namespace.md
[MSON]: https://github.com/apiaryio/mson
[MSON Specification]: https://github.com/apiaryio/mson/blob/master/MSON%20Specification.md
