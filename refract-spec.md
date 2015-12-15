# Refract Document Format Specification

## Introduction

This document is the full spec for the Refract, a recursive data structure for expressing complex structures, relationships, and metadata.

## About this Document

This document conforms to RFC 2119, which says:

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

[MSON](https://github.com/apiaryio/mson) is used throughout this document to describe and define data structures.

## Media Type for Specification Format

The proposed media type for this spec are as follows.

* `application/vnd.refract` for Full Refract
* `application/vnd.compact-refract` for Compact Refract
* `application/vnd.embedded-refract` for Embedded Refract

Any custom media type in this project SHOULD append the name of the profile to these base media types separated by a period (i.e. `application/vnd.refract.my-custom-type`).

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
          - `ref` (Element Pointer) - Pointer to referenced element or type
          - `classes` (array[string]) - Array of classifications for given element
          - `title` (string) - Human-readable title of element
          - `description` (string) - Human-readable description of element
          - `links` (array[Link Element]) - Meta links for a given element
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

## Primitive Elements

Primitive Elements extend upon the base Element to define elements based on the Primitive Types of Refract.

A Refract document MUST support each of these primitive elements. These elements MAY be extended or replaced based on profiles provided, either by way of a profile link relation or other means such as HTTP Link Headers.

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

## Referencing and Element Pointers

These elements and definitions are provided as part of the base specification for the purpose of identifying, referencing, and pointing to elements and their respective meta, attributes, or content.

### Ref Element (Element)

The `ref` element MAY be used to reference elements in remote documents or elements in the local document. The `ref` element transcludes the contents of the element into the document in which it is referenced.

#### Properties

- `element` ref (string, fixed)
- `content` (Element Pointer, required) - Points to an element or an element's properties

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

### Element Pointer (enum)

A pointer is an object for providing URLs to local elements and remote elements or documents. The following rules apply.

1. When referencing an element in the local document, the `id` of the element MAY be used
1. When referencing remote elements, an absolute URL or relative URL MAY be used
1. When a URL fragment exists in the URL given, it references the element with the matching `id` in the given document. The URL fragment MAY need to be URL decoded before making a match.
1. When a URL fragment does not exist, the URL references the root element
1. When `path` is used, it references the given property of the referenced element
1. When `path` is used in an element that includes the data of the pointer (such as with `ref`), the referenced path MAY need to be converted to a refract structure in order to be valid

#### Members

- (string) - A URL to an ID of an element in the current document
- (object)  - The URL and path of the referenced element
    - `href` (string, required) - URL or ID of element
    - `path` (enum) - Path of referenced element to transclude instead of element itself
        - meta - The meta data of the referenced element
        - attributes - The attributes of the referenced element
        - content - The content of the referenced element

## Link Element (Element)

Hyperlinking MAY be used to link to other resources, provide links to instructions on how to process a given element (by way of a profile or other means), and may be used to provide meta data about the element in which it's found. The meaning and purpose of the hyperlink is defined by the link relation according to [RFC 5988](https://tools.ietf.org/html/rfc5988).

### Properties

- `element`: link (string, fixed)
- `attributes`
    - `relation` (string) - Link relation type as specified in [RFC 5988](https://tools.ietf.org/html/rfc5988).
    - `href` (string) - The URI for the given link

### Example

The following shows a link with the relation of `foo` and the URL of `/bar`.

```json
{
  "element": "link",
  "attributes": {
    "relation": "foo",
    "href": "/bar"
  }
}
```

## Profiles

The primary means by which users can provide semantic definitions and other meta information is through a profile. A profile MAY provide semantic information about an element and its data, it MAY provide specific instructions about elements such as how inheritance should work or how elements should be processed, and it MAY be used to modify understanding of existing elements in other profiles. The usage is a profile is not limited to these descriptions, and SHOULD be left up to the profile author to define its use.

To point to a profile, you MAY use the [profile link relation](https://www.ietf.org/rfc/rfc6906.txt) as a meta link in your root element or in any other element. Profile links may also be found outside of the document itself in places like the [HTTP Link Header](http://www.w3.org/wiki/LinkHeader).

Below is an example of how a profile link is used as a meta link in Refract.

```js
{
  "element": "foo",
  "meta": {
    "links": [
      {
        "element": "link",
        "attributes": {
          "relation": "profile",
          "href": "http://example.com/profiles/foo"
        }
      }
    ]
  },
  "content": "bar"
}
```

The example shows a `foo` element with a `profile` link. This profile link informs the parser this particular element conforms to a specific profile.

## Extend and Select Elements

Elements by default do not include any of the attributes or content from the element in which they reference. An element MAY be extended in order to inherit from other elements using the `extend` element.

Additionally, the `select` element is provided to give multiple possibilities for a given content.

### Extend Element (Element)

The `extend` element provides a way to a way to multiply inherit one or more elements to form a new element. The `extend` element MUST NOT affect the original elements being extended, and MUST define a new instance of an element.

The `extend` element MUST do a deep merge of the elements found in the `content`, but MUST NOT include the `id` meta attribute from the content elements in the final element. Each element found in the `content` MUST derive from the same primitive element. The elements are merged from first to last.

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
