# JSON Refract Serialisation

This document describes how Refract can be serialised into other forms such as
JSON along with including all serialisation guidelines.

A Refract element MUST be serialised fully as the following data structure as a
JSON object:

- element (required, string)
- meta (optional, object)
- attributes (optional, object)
- content (optional, enum)
    - Element
    - array[Element]
    - string
    - boolean
    - number
    - null
    - Key Value Pair

## Properties

### Element

The element name MUST always be present and it MUST contain the name of the
Refract element as a string.

### Meta

Meta will contain all the meta properties, this SHOULD NOT be present in the
serialisation if there are no meta properties. When there are any meta
properties set, the meta SHOULD be serialised. Meta SHOULD contain a JSON
object which matches the keys and values described in the Refract
specification. All values in the object must be Refracted elements.

### Attributes

Attributes will contain all the attributes of an element, this SHOULD NOT be
present in the serialisation if there are no attributes. When there are any
attributes set, the attributes SHOULD be serialised. Attributes SHOULD contain
a JSON object which contains the attributes in the Refract specification. All
attribute values in the JSON object must be Refracted elements.

### Content

The content of an element MUST be one of the following types:

- Element - Another JSON serialised element
- array[Element] - An array of JSON serialised elements
- string - A JSON string
- boolean - A JSON boolean value (true/false)
- number - A JSON number
- null - A JSON null (`null`)
- Key Value Pair (object) - A JSON object representing a key-value pair
    - key (required, Element) - A required key
    - value (Element) - An optional value

An element is not required to have content.

## Examples

### An element

```json
{
  "element": "string"
}
```

### An element with content

```json
{
  "element": "string",
  "content": "Doe"
}
```

### An element with metadata and content

```json
{
  "element": "string",
  "meta": {
    "title": {
      "element": "string",
      "content": "Name"
    }
  },
  "content": "Doe"
}
```

### An element with metadata, attributes and content

```json
{
  "element": "string",
  "meta": {
    "title": {
      "element": "string",
      "content": "Person"
    }
  },
  "attributes": {
    "address": {
      "element": "string",
      "content": "49 Featherstone Street, London, EC1Y 8SY"
    }
  },
  "content": "Doe"
}
```

### An element with Key Value Pair as content

```json
{
  "element": "member",
  "content: {
    "key": {
      "element": "string",
      "content": "Name"
    },
    "value": {
      "element": "string",
      "content": "Doe"
    }
  }
}
```

### An element with array of elements as content

```json
{
  "element": "dns-resource",
  "content": [
    {
      "element": "dns-record",
      "attributes": {
        "ttl": {
          "element": "number",
          "content": 86400
        }
      },
      "content": "_sip._tcp.example.com"
    }
  ]
}
```
