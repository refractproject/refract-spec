# MSON Namespace

This document extends [Refract][] Specification with new element types necessary to build [MSON][] Refract.

## Content

<!-- TOC depth:3 withLinks:1 updateOnSave:0 -->
- [MSON Namespace](#mson-namespace)
    - [Content](#content)
    - [About this Document](#about-this-document)
    - [Expanded Element](#expanded-element)
    - [Base Element](#base-element)
        - [Type comparison](#type-comparison)
- [MSON Refract Elements](#mson-refract-elements)
    - [MSON Element (Element)](#mson-element-element)
        - [Properties](#properties)
    - [Boolean Type (Boolean Element)](#boolean-type-boolean-element)
    - [String Type (String Element)](#string-type-string-element)
    - [Number Type (Number Element)](#number-type-number-element)
    - [Array Type (Array Element)](#array-type-array-element)
    - [Object Type (Object Element)](#object-type-object-element)
    - [Enum Type (MSON Element)](#enum-type-mson-element)
        - [Properties](#properties)
        - [Examples](#examples)
    - [Examples](#examples)
        - [Anonymous Object Type](#anonymous-object-type)
        - [Type Attributes](#type-attributes)
        - [Default Value](#default-value)
        - [One Of](#one-of)
        - [Mixin](#mixin)
        - [Named Type](#named-type)
        - [Variable Value](#variable-value)
        - [Variable Property Name](#variable-property-name)
        - [Variable Type Name](#variable-type-name)
<!-- /TOC -->

## About this Document

This document conforms to RFC 2119, which says:

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

[MSON][] is used throughout this document.

## Inheritance and Expanded Element

MSON is built around the idea of defining recursive data structures. To provide abstraction, for convenience reasons and to not repeat ourselves, these structures can be named (using an _identifier_) and reused. In [MSON][], the reusable data structures are called _Named Types_.

By default, Refract does not enforce inheritance of data, though element definitions are inherited from the defined element types. To inherit data in Refract, the `extend` element is used to merge one or more elements into a final element. In the MSON namespace, however, when the data is defined, it inherits data from the element definition. MSON itself uses inheritance this way, and the MSON Refract namespace mimics the behavior to provide simplicity and consistency across MSON representations.

Often, before an MSON Refract can be processed, referenced _Named Types_ have to be resolved. Resolving references to _Named Types_ is tedious and error prone. As such an MSON processor can resolve references to produce a complete MSON Refract. That is, a Refract that does not include unresolved references to other data structures. This is referred to as _reference expansion_ or simply _expansion_.

In other words, an expanded element is one that does not contain any _Identifier_ (defined below) referencing any other elements than those defined in MSON namespaces.

The expanded Refract MUST, however, keep the track of what data structure was expanded and what from where.

### Example

Extending the element "A" to form new element "B":

```json
{
  "element": "extend",
  "meta": {
    "id": "B"
  },
  "content": [
    {
      "element": "string",
      "meta": {
        "id": "A"
      },
      "content": "base element content"
    },
    {
      "element": "string",
      "content": "derived content"
    }
  ]
}
```

In MSON refract, the following is equivalent:

```json
{
  "element": "string",
  "meta": {
    "id": "A"
  },
  "content": "base element content"
}
```

```json
{
  "element": "A",
  "meta": {
    "id": "B"
  },
  "content": "derived content"
}
```

Finally, using the `extend` element to expand the MSON refract for id "B":

```json
{
  "element": "extend",
  "meta": {
    "id": "B"
  },
  "content": [
    {
      "element": "string",
      "meta": {
        "ref": "A"
      },
      "content": "base element content"
    },
    {
      "element": "string",
      "content": "derived content"
    }
  ]
}
```

## Base Element

In MSON, every data structure is a sub-type of another data structure, and, therefore, it is directly or indirectly derived from one of the MSON _Base Types_. This is expressed as an inheritance of elements in MSON Refract. Where the predecessor of an element is referred to as element's _Base Element_.

Note: Not every MSON _Base Type_ is presented in Refract primitive types and vice versa – see the table below.

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

# MSON Refract Elements

## MSON Element (Element)

Base element for every MSON element.

The MSON Element adds attributes representing MSON _Type Definition_ and _Type Sections_.

Note: In MSON Refract _Nested Member Types_ _Type Section_ is the `content` of the element.

### Properties

- `attributes`
    - `typeAttributes` (array) - _Type Definition_ attributes list, see _Type Attribute_  

      Type attributes of a type definition.

      Note, if `sample` (or `default`) attribute is specified the value SHOULD be stored in the `samples` (or `default`) property instead of the element's `content`.

      - Items
          - (enum[string])
              - required - This element is required in parent's content
              - optional - This element is optional in parent's content
              - fixed - The `content` value is immutable.

    - `variable` (boolean)

      The `content` value is either a _Variable Type Name_, or _Variable Property Name_.

      Note, if the `content` is a _Variable Value_ the `sample` type attribute
      should be used instead (see `typeAttributes`).

    - `samples` (array) - Array of alternative sample values for _Member Types_

          The type of items in `samples` array attribute MUST match the type of element's `content`.

    - `default` - Default value for _Member Types_

          The type of of `default` attribute MUST match the type of element's `content`.

    - `validation` - Not used, reserved for a future use


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

## Enum Type (MSON Element)

Enumeration type. Exclusive list of possible elements. The elements in content's array MUST be interpreted as mutually exclusive.

### Properties

- `element`: enum (string, fixed)
- `content` (array[[MSON Element][]])

### Examples

#### MSON

```
- tag (enum[string])
    - red
    - green
```

#### MSON Refract

```json
{
    "element": "object",
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "tag"
                },
                "value": {
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

#### MSON Refract

```json
{
    "element": "object",
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "id"
                },
                "value": {
                    "element": "string",
                    "content": "42"
                }
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

#### MSON Refract

```json
{
    "element": "object",
    "content": [
        {
            "element": "member",
            "attributes": {
                "typeAttributes": [
                    "required",
                    "fixed"
                ]
            },
            "content": {
                "key": {
                    "element": "string",
                    "content": "id"
                },
                "value": {
                    "element": "string",
                    "content": "42"
                }
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

#### MSON Refract

```json
{
    "element": "object",
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "id"
                },
                "value": {
                    "element": "number",
                    "attributes": {
                        "default": 0
                    }
                }
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

#### MSON Refract

```json
{
    "element": "object",
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "city"
                }
            }
        },
        {
            "element": "select",
            "content": [
                {
                    "element": "option",
                    "content": [
                        {
                            "element": "member",
                            "content": {
                                "key": {
                                    "element": "string",
                                    "content": "state"
                                }
                            }
                        }
                    ]
                },
                {
                    "element": "option",
                    "content": [
                        {
                            "element": "member",
                            "content": {
                                "key": {
                                    "element": "string",
                                    "content": "province"
                                }
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

#### MSON Refract

Using the `ref` element to reference an the content of an element.

```json
{
    "element": "object",
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "id"
                }
            }
        },
        {
            "element": "ref",
            "content": {
                "href": "User",
                "path": "content"
            }
        }
    ]
}
```

Using `extend` to merge objects together.

```json
{
    "element": "extend",
    "content": [
        {
            "element": "object",
            "content": [
                {
                    "element": "member",
                    "content": {
                        "key": {
                            "element": "string",
                            "content": "id"
                        }
                    }
                }
            ]
        },
        {
            "element": "ref",
            "content": "User"
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

#### MSON Refract

```json
{
    "element": "object",
    "meta": {
        "id": "Address",
        "title": "Address",
        "description": "Description is here! Properties to follow."
    },
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "stree"
                }
            }
        }
    ]
}
```

### Referencing & Expansion

#### MSON

```markdown
# User (object)
- name

# Customer (User)
- id
```

#### MSON Refract

```json
{
    "element": "object",
    "meta": {
        "id": "User"
    },
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "name"
                }
            }
        }
    ]
}
```

```json
{
    "element": "User",
    "meta": {
        "id": "Customer"
    },
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "id"
                }
            }
        }
    ]
}
```

#### Expanded MSON Refract

```json
{
    "element": "extend",
    "meta": {
        "id": "Customer"
    },
    "content": [
        {
            "element": "object",
            "meta": {
                "ref": "User"
            },
            "content": [
                {
                    "element": "member",
                    "content": {
                        "key": {
                            "element": "string",
                            "content": "id"
                        }
                    }
                }
            ]
        },
        {
            "element": "object",
            "content": [
                {
                    "element": "member",
                    "content": {
                        "key": {
                            "element": "string",
                            "content": "id"
                        }
                    }
                }
            ]
        }
    ]
}
```

### Variable Value

#### MSON

```markdown
- p: *42*
```

#### MSON Refract

```json
["object", {}, {}, [
  ["member", {}, {}, {
    "key": ["string", {}, {}, "p"],
    "value": ["string", {}, {"samples": [42]}, null]
  }]
]]
```

### Variable Property Name

#### MSON

```markdown
- *rel (Relation)*
```

#### MSON Refract

```json
["object", {}, {}, [
  ["member", {}, {}, {
    "key": ["Relation", {}, {"variable": true}, "rel"],
    "value": ["string", {}, {}, null]
  }]
]]
```

### Variable Type Name

**Proposal – not yet implemented**

Note this needs an introduction of a new MSON namespace element for any type - `generic`.

#### MSON

```markdown
- p (array[*T*])
```

#### MSON Refract

```json
["object", {}, {}, [
  ["member", {}, {}, {
    "key": ["string", {}, {}, "p"],
    "value": ["array", {}, {}, [
        ["generic", {}, {}, "T"]
    ]]
  }]
]]
```

---

[Refract]: https://github.com/refractproject/refract-spec/blob/master/refract-spec.md
[MSON]: https://github.com/apiaryio/mson
[MSON Specification]: https://github.com/apiaryio/mson/blob/master/MSON%20Specification.md
[MSON Element]: #mson-element-element
