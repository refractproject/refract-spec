# MSON Namespace

This document extends [Refract][]'s [JSON Namespace][] with elements necessary to
build [MSON][] DOM.

# Content

This namespace defines following elements:

1. General-use elements
    1. [Id Element](#id-element-distinct-element)
    1. [Distinct Element](#distinct-element-element)
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

# Terminology

This specification uses terminology from [MSON Specification][]. In addition, the terms defined in this namespace are described below.

## Expanded Element

MSON is built around the idea of defining recursive data structures. To provide abstraction, for convenience reasons and to not repeat ourselves, these structures can be named (using an _identifier_) and reused. In [MSON][], the reusable data structures are called _Named Types_.

Often, before an MSON DOM can be processed referenced _Named Types_ have to be resolved. Resolving references to _Named Types_ is tedious and error prone. As such parser can resolve references and produce a complete MSON DOM, that is a DOM that does not include unresolved references to other data structures. This is referred to as _reference expansion_ or simply _expansion_.

In other words, an expanded element  is one that does not contain any _Identifier_ (defined bellow) referencing any other elements than those defined in JSON or MSON namespaces.

The expanded DOM MUST, however, keep the track of what data structure was expanded and what from where.

## Base Element

In MSON, every data structure is a sub-type of another data structure, and, therefore, it is directly or indirectly derived from one of the MSON _Base Types_. This is expressed as an inheritance of elements in MSON DOM. Where the predecessor of an element is referred to as element's _Base Element_.

Note: Not every MSON _Base Type_ is presented in JSON namespace primitive types and vice versa, see the table bellow:

### JSON Namespace vs. MSON built-in types

| JSON primitive |   JSON Namespace   | MSON Base Type |   MSON Namespace   |
|:--------------:|:------------------:|:--------------:|:------------------:|
|     boolean    |  JSON:Boolean Type |     boolean    |  MSON:Boolean Type |
|     string     |  JSON:String Type  |     string     |  MSON:String Type  |
|     number     |  JSON:Number Type  |     number     |  MSON:Number Type  |
|      array     |   JSON:Array Type  |      array     |   MSON:Array Type  |
|        -       |          -         |      enum      |   MSON:Enum Type   |
|     object     |  JSON:Object Type  |     object     |  MSON:Object Type  |
|      null      |   JSON:Null Type   |        -       |          -         |
|        -       | JSON:Property Type |        -       | MSON:Property Type |


# General Elements Definition

General elements defined inside MSON namespaces but possibly reusable in another domain.

## Identifier (Enum)

Identifier of an element in the MSON namespace. The identifier MUST be either directly a `string` value or an `Id Element` element.

### Members

- (string)
- (Id Element)

## Id Element (Distinct Element)

Element representing an identifier in the MSON namespace.

### Properties

- `element`: id (string, required, fixed)
- `content` (string, required)

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

## Select (Distinct Element)

Element representing selection of options. Every item of content array represents one possible option.

### Properties

- `element`: select (string, required, fixed)
- `content` (array[Option])

## Option (Distinct Element)

One choice in the selection.

### Properties

- `element`: option (string, required, fixed)
- `content` (enum)
    - (Distinct Element)
    - (array[Distinct Element])

#### Example

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

# MSON DOM Elements Definition

## MSON Element (Distinct Element)

Base element for all MSON elements.

The MSON Element adds attributes representing MSON _Type Definition_ and _Type Sections_. Note in MSON DOM _Nested Member Types_ _Type Section_ is the `content` of the element.

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
    - `sample` (MSON Element) - Alternative sample _Member Types_ value
    - `default` (MSON Element) - Default value for _Member Types_
    - `validation` - Not used, reserved for a future use
    - `description` - Combined description of an MSON Element

## Boolean Type (JSON:Boolean Type)

- Include MSON Element

## String Type (JSON:String Type)

- Include MSON Element

## Number Type (JSON:Number Type)

- Include MSON Element

## Array Type (JSON:Array Type)

- Include MSON Element

## Object Type (JSON:Object Type)

- Include MSON Element

## Property Type (JSON:Property Type)

- Include MSON Element

## Enum Type (MSON Element)

Enumeration type. Exclusive list of possible elements. The elements in content's array MUST be interpreted as mutually exclusive.

### Properties

- `element`: enum (string, required, fixed)
- `content` (array[MSON Element])

### Example

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
            "element": "User"
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

[Refract]: https://github.com/refractproject/refract-spec/blob/master/refract-spec.md
[JSON Namespace]: https://github.com/refractproject/refract-spec/blob/master/namespaces/json-namespace.md
[MSON]: https://github.com/apiaryio/mson

[MSON Specification]: https://github.com/apiaryio/mson/blob/master/MSON%20Specification.md
