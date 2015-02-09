# Refract Document Format Specification

## Introduction

This document is the full spec for the Refract, a recursive data structure for expressing complex structures, relationships, and metadata.

## About this Document

This document conforms to RFC 2119, which says:

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

[MSON](https://github.com/apiaryio/mson) is used throughout this document to describe and define data structures.

## Data Structure

Refract provides a single structure for data, which will be referred to throughout this document as an element. All elements found in a Refract document SHOULD conform to the element structure as defined here.

### Element

The Refract Element contains three properties, `element`, `attributes`, and `content`, as defined below. This Element can be used recursively throughout the document, even as a value for each of its own properties.

#### Properties

- `element` (enum, required)

    The `element` property defines the type of element. It MAY be a string that references an element type, or it MAY be an `element` itself that provides additional data about the element type.

    - Members
        - (string)
        - (Element)

- `attributes` (enum)

    The `attributes` property defines attributes about the given instance of the element, as specified by the `element` property. It MAY be an array of elements, or it MAY be an object. The keys of the object SHOULD be defined element types with valid values for the corresponding element types.

    - Members
        - (object)
        - array[Element]

- `content` (enum)

    The `content` property defines the content of the instance of the specified element type. The value MAY be any of the JSON primitive types, an element, or an array of elements.

    - Members
        - (null)
        - (string)
        - (number)
        - (boolean)
        - (array)
        - (object)
        - (Element)
        - array[Element]

#### Example

An simple element may look like this, where `foo` is the element type, `id` is an attribute for the `foo` element, and `content` is a string with a value of `bar`.

```json
{
  "element": "foo",
  "attributes": {
    "id": 4
  },
  "content": "bar"
}
```

##### XML Representation

The example of above would be represented like this in XML.

```xml
<foo id="4">bar</foo>
```

It may also resemble a simple JSON structure, though JSON does not afford attributes.

##### JSON Representation

The example above would be represented like this in idiomatic JSON.

```json
{
  "foo": "bar"
}
```

### Compact Format

In addition to expressing Refract Elements as objects with `element`, `attributes`, and `content` properties, these elements can be expressed as a tuple.

#### Compact Element (array)
- (enum, required) - Name of the element
    - (string)
    - Compact Element
- (enum, optional) - Attributes of the element
    - (object)
    - array[Compact Element]
- (enum) - Element content with any of the following types
  - (null)
  - (string)
  - (number)
  - (boolean)
  - (array)
  - (object)
  - (Compact Element)
  - array[Compact Element]

#### Example

This example will show a JSON object represented as both a normal Refract Element and a Compact Element.

```json
{
  "foo": "bar"
}
```

##### Refract Element Representation

It can be expressed in the normal Refract element structure.

```json
{
  "element": "foo",
  "attributes": {},
  "content": "bar"
}
```

##### Compact Element Representation

This is how it would expressed in the compact version.

```json
["foo", {}, "bar"]
```

## References

- [MicroXML](https://dvcs.w3.org/hg/microxml/raw-file/tip/spec/microxml.html)
- [JsonML](http://www.jsonml.org/)
- [Adding Namespaces to JSON](http://www.goland.org/jsonnamespace/)
- [draft-saintandre-json-namespaces-00](https://tools.ietf.org/html/draft-saintandre-json-namespaces-00)
