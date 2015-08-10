# Refract Document Format Specification

## Introduction

This document is the full spec for the Refract, a recursive data structure for expressing complex structures, relationships, and metadata.

## About this Document

This document conforms to RFC 2119, which says:

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

[MSON](https://github.com/apiaryio/mson) is used throughout this document to describe and define data structures.

## Base Element

Refract provides a single structure for data, which will be referred to throughout this document as an element. All elements found in a Refract document SHOULD conform to the element structure as defined here.

### Element (object)

The Refract Element contains four properties: `element`, `meta`, `attributes`, and `content`, as defined below. This Element MAY be used recursively throughout the document, even as a value for each of its own meta or attributes.

#### Properties

- `element` (string, required)

    The `element` property defines the name of element. It MUST be a string that references an element, which SHOULD be defined.

- `meta` (enum)

    The `meta` property is a reserved object for Refract-specific values. When `meta` is an object, it MAY contain elements itself. The element definition SHOULD be used when interacting with `meta` and its properties and values.

  - Members
      - (object)
          - `id` - Unique Identifier, MUST be unique throughout the document
          - `ref` (Link) - Link to referenced element or type
          - `classes` (array[string]) - Array of classifications for given element
          - `prefix` (string) - Prefix in which element MAY be found
          - `namespaces` (array[Link]) - Include elements from given namespaces or prefix elements from given namespace
          - `title` (string) - Human-readable title of element
          - `description` (string) - Human-readable description of element
      - (array[Member Element])

- `attributes` (enum)

    The `attributes` property defines attributes about the given instance of the element, as specified by the `element` property. When `attributes` is an object, it MAY contain elements itself. The element definition SHOULD be used when interacting with `attributes` and its properites and values.

    - Members
        - (object)
        - (array[Member Element])

- `content` (enum)

    The `content` property defines the content of the instance of the specified element. The value MAY be any of the Refract primitive types.

    - Members
        - (null)
        - (string)
        - (number)
        - (boolean)
        - (array)
        - (object)
        - (Element)

#### Example

An element MAY look like this, where `foo` is the element name, `id` is a meta attribute for the `foo` element, and `content` is a string with a value of `bar`. Here, the `id` is `baz` and MAY be used for referencing.

```json
{
  "element": "foo",
  "meta": {
    "id": "baz"
  },
  "content": "bar"
}
```

### Compact Format

In addition to expressing Refract Elements as objects with `element`, `meta`, `attributes`, and `content` properties, these elements MUST be expressed as a tuple.

#### Compact Element (array)

The Compact Element is a tuple where each item has a specific meaning. The first item is the element name, the second is the meta attribute section, the third is the attribute section, and the fourth is the content section.

##### Members

- (string, required) - Name of the element
- (enum, required) - Meta attributes of the element instance. See meta attributes above for full Refract representation
    - (object)
    - (array[Compact Element])
- (enum, required) - Attributes of the element instance
    - (object)
    - (array[Compact Element])
- (enum, required) - Element content with any of the following types
  - (null)
  - (string)
  - (number)
  - (boolean)
  - (array)
  - (object)
  - (Compact Element)
  - (array[Compact Element])

##### Example

Below is a Refract element `foo` that is expressed in the normal Refract representation.

```json
{
  "element": "foo",
  "content": "bar"
}
```

This is how it would represented in the compact version.

```json
["foo", {}, {}, "bar"]
```

## Primitive Elements

Primitive Elements extend upon the base Element to define elements based on the Primitive Types of Refract.

A Refract document MUST support each of these primitive elements. These elements MAY be extended or replaced based on namespaces provided in any root or parent element.

### Null Element (Element)

A `Null Element` is an element that has a Null Type as its value. It extends upon the Refract Element.

#### Properties

- `element`: null (string, fixed)
- `content` (null)

#### Example

In JSON, `null` is represented as `null`.

```json
null
```

In Refract, it is represented as a `Null Element` element.

```json
{
  "element": "null",
  "content": null
}
```

### String Element (Element)

A String Element provides an element for Refract String Types.

#### Properties

- `element`: string (string, fixed)
- `content` (string)

#### Examples

In JSON, an example of a string is:

```json
"foobar"
```

In Refract, this string is expanded to a String Element.

```json
{
  "element": "string",
  "content": "foobar"
}
```

### Number Element (Element)

A Number Element provides an element for Refract Number Types.

#### Properties
- `element`: number (string, fixed)
- `content` (number)

#### Examples

In JSON, a number is represented as:

```json
400
```

In Refract, this number is expanded to a Number Element.

```json
{
  "element": "number",
  "content": 400
}
```
### Boolean Element (Element)

A Boolean Element provides an element for Refract Boolean Types.

#### Properties
- `element`: boolean (string, fixed)
- `content` (boolean)

#### Examples

In JSON, an example of a boolean is:

```json
true
```

In Refract, this boolean is expanded to a Boolean Element.

```json
{
  "element": "boolean",
  "content": true
}
```

### Array Element (Element)

An Array Element provides an element for Refract Array Types.

#### Properties

- `element`: array (string, fixed)
- `content` (array[Element])

#### Examples

In JSON, an example of an array is:

```json
["abc", 400, true]
```

In Refract, this boolean is expanded to a Array Element.

```json
{
  "element": "array",
  "content": [
    {
      "element": "string",
      "content": "foo"
    },
    {
      "element": "number",
      "content": 400
    },
    {
      "element": "boolean",
      "content": true
    }
  ]
}
```

### Object Element (Element)

A Object Element provides an element for Refract Object Types. When the content of an `object` element includes an `extend`, `select`, or `ref` element, the referenced or resulting elements MUST be a `member` element. The properties of the object SHOULD be unique to the object in which they are found.

#### Properties

- `element`: object (string, fixed)
- `content` (enum)
    - (object)
    - (array[Member Element])
    - (Extend Element)
    - (Select Element)
    - (Ref Element)

#### Examples

In JSON, an example of an object is:

```json
{
  "foo": "bar"
}
```

In Refract, this object MAY Be expanded to include an array of elements as its content.

```json
{
  "element": "object",
  "content": [
    {
      "element": "member",
      "content": {
        "key": {
          "element": "string",
          "content": "foo"
        },
        "value": {
          "element": "string",
          "content": "bar"
        }
      }
    }
  ]
}
```

### Member Element (Element)

A Member Element is any element with a key-value pair as the content. See [Object Element](#object-element-element) for examples of how this is used.

#### Properites

- `element` member (string, fixed)
- `content` (object)
    - `key` (Element, required) - Key for the member
    - `value` (Element, optional) - Value for the member

## Referencing and Linking

These elements and definitions are provided as part of the base specification for the purpose of identifying, referencing, and linking to elements.

### Ref Element (Element)

The `ref` element MAY be used to reference elements in remote documents or elements in the local document. The `ref` element transcludes the contents of the element into the document in which it is referenced.

#### Properties

- `element` ref (string, fixed)
- `content` (Link, required)

#### Examples

Elements MAY be referenced in remote or local documents.

##### Referencing Remote Element

```json
{
  "element": "ref",
  "content": "http://example.com/document#foo"
}
```

##### Referencing Local Elements

```json
{
  "element": "ref",
  "content": "foo"
}
```

##### Referencing Elements in Prefixed Namespace

This references the element with the ID of `foo` in the prefixed namespace of `ns`.

```json
{
  "element": "ref",
  "content": {
    "prefix": "ns",
    "href": "foo"
  }
}
```

##### Reference Parts of Elements

Given an element instance of:

```json
{
  "element": "array",
  "meta": {
    "id": "colors"
  },
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
```

And given an array where a reference is used as:

```json
{
  "element": "array",
  "content": [
    {
      "element": "string",
      "content": "blue"
    },
    {
      "element": "ref",
      "content": {
        "href": "colors",
        "path": "content"
      }
    }
  ]
}
```

The resulting dereferenced array is:

```json
{
  "element": "array",
  "content": [
    {
      "element": "string",
      "content": "blue"
    },
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
```

### Link (enum)

A link is an object for providing URLs to local elements, prefixed elements, and remote elements or documents. The following rules apply.

1. When referencing an element in the local namespace, the `id` of the element MAY be used
1. When referencing remote elements, an absolute URL or relative URL MAY be used
1. When a URL fragment exists in the URL given, it references the element with the matching `id` in the given namespace. The URL fragment MAY need to be URL decoded before making a match.
1. When a URL fragment does not exist, the URL references the root element
1. When the `prefix` is used, it references an element in a defined prefixed namespace
1. When `path` is used, it references the given property of the referenced element
1. When `path` is used in an element that includes the data of the link (such as with `ref`), the referenced path MAY need to be converted to a refract structure in order to be valid

#### Members

- (string) - A URL to a namespace or an ID of an element in the current namespace
- (object)  - A prefixed link
    - `prefix` (string) - Prefix of namespace
    - `href` (string, required) - URL or ID of element in prefixed namespace
    - `path` (enum) - Path of referenced element to transclude instead of element itself
        - meta - The meta data of the referenced element
        - attributes - The attributes of the referenced element
        - content - The content of the referenced element

## Namespacing

Namespaces provide a way to include element definitions and constraints into another document. The following rules and constraints apply to namespaces.

1. If there is a conflict, the namespaced element defined or referenced last MUST take precedence
1. Types defined within the local namespace MUST take precedence over referenced namespaces
1. Prefixed namespaces are only accessible through using a prefix
1. Namespaces apply to the element in which they are introduced and all child elements
1. Namespaces MUST not include the elements nor the data in the elements referenced, but rather include the constraints and conditions around the types defined within that namespace

### Example Using Both String and Object Namespace Elements

This example shows a namespace being included by way of a string, and a prefixed namespace.

```json
{
  "element": "foo",
  "meta": {
    "namespaces": [
      "http://example.com/namespace1",
      { "prefix": "ns2", "href": "http://example.com/namespace2" }
    ]
  }
}
```

## Extend and Select Elements

Elements by default do not include any of the attributes or content from the element in which they reference. An element MAY be extended in order to inherit from other elements using the `extend` element.

Additionally, the `select` element is provided to give multiple possibilities for a given content.

### Extend Element (Element)

The `extend` element provides a way to a way to multiply inherit one or more elements to form a new element. The `extend` element MUST NOT affect the original elements being extended, and MUST define a new instance of an element.

The `extend` element MUST do a deep merge of the elements found in the `content`, but MUST NOT include the `id`, `namespaces` and `prefix` meta attributes from the content elements in the final element. Each element found in the `content` MUST derive from the same primitive element. The elements are merged from first to last.

#### Properties

- `element` extend (string, fixed)
- `content` (array[Element]) - Array of elements to be merged

#### Examples

```json
{
  "element": "extend",
  "content": [
    {
      "element": "foo",
      "attributes": {
        "baz": "bar"
      },
      "content": "first"
    },
    {
      "element": "foo",
      "content": "second"
    }
  ]
}
```

The value for this new element would be the following.

```json
{
  "element": "foo",
  "attributes": {
    "baz": "bar"
  },
  "content": "second"
}
```

Elements MAY also be referenced when using extend. Here is an element defined and given an ID of `bar`.

```json
{
  "element": "foo",
  "meta": {
    "id": "bar"
  },
  "content": "second"
}
```

Here is an extend element referencing the previously `bar` element.

```json
{
  "element": "extend",
  "content": [
    {
      "element": "foo",
      "content": "first"
    },
    {
      "element": "ref",
      "content": "bar"
    }
  ]
}
```

The resulting element would be the following. Note that the `id` was not included in the final element.

```json
{
  "element": "foo",
  "content": "second"
}
```

### Select Element (Element)

#### Properties

- `element` select (string, fixed)
- `content` (array[Option Element])

#### Examples

This example uses a Select Element to provide multiple options for the properties of an Object Element. One option is the value of the the key `firstName` is "John," and the other option is the value of the key `giveName` is "John."

```json
{
  "element": "object",
  "content": [
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
                  "content": "firstName"
                },
                "value": {
                  "element": "string",
                  "content": "John"
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
                  "content": "givenName"
                },
                "value": {
                  "element": "string",
                  "content": "John"
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

For the above example, if the first option is chosen, the resulting object will look like this:

```json
{
  "firstName": "John"
}
```

If the second option is chosen, it will look like this:

```json
{
  "givenName": "John"
}
```

### Option Element (Element)

The Option Element provides a way to give one or more elements that MAY be the value of the Select Element in which it is found. For examples, see the Select Element section.

#### Properties

- `element` option (string, fixed)
- `content` (array[Element])

## Defining New Elements

When an element is given an ID, it creates a new type of element. When instances of the new element are used, they MAY conform to the definition of the referenced element.

Elements do not inherit data from the referenced element, though they do inherit the definition. This means that a referenced element MAY define what an element MAY look like, but it does not define what it MUST look like, nor does it define data for each instance.

When it is desired to inherit attributes, use the Extend Element and Ref Element together to accomplish this.

### Example

The element below is a string element with an ID of "foo."

```json
{
  "element": "string",
  "meta": { "id": "foo" },
  "attributes": {
    "bar": "baz"
  },
  "content": "Hello World"
}
```

Since an ID was given, `foo` MAY now be used for creating new instances.

```json
{
  "element": "foo",
  "content": "new instance"
}
```

What this says is that this element MAY have an attribute of `bar` that is equal to `baz` and MAY have content that is like "Hello World." The instance of `foo` MUST not inherit any data from `foo`, though it does inherit the definition of the element where the ID is `foo`.

## References

- [MicroXML](https://dvcs.w3.org/hg/microxml/raw-file/tip/spec/microxml.html)
- [JsonML](http://www.jsonml.org/)
- [Adding Namespaces to JSON](http://www.goland.org/jsonnamespace/)
- [draft-saintandre-json-namespaces-00](https://tools.ietf.org/html/draft-saintandre-json-namespaces-00)
