# JSON Namespace

This spec defines JSON primitive types to be used in a Refract document structure. Each type defined here extends the Refract Element as defined in the Refract specification.

## Primitive Types
Primitive Types extend upon the Refract Element to create elements for the following JSON types:

- null
- string
- number
- boolean
- array
- object

Each of these JSON types can be expanded into a Refract Primitive Type that can also be extended. A Refract document MUST support each of these element types by default. These types MAY be extended or replaced based on namespaces provided in any root or parent element.

### Null Type (Refract Element)
A `Null Type` is a type that simply has `null` as its value. It extends upon the `Refract Element` and defines a specific content of `null`.

#### Properties
- `element`: null (string, fixed)
- `content`: null (null, fixed)

#### Example

In JSON, `null` is represented as `null`.

```json
null
```

In Refract, it is represented as a `Null Type` element.

```json
{
  "element": "null",
  "attributes": {},
  "content": null
}
```

### String Type (Refract Element)

A `String Type` allows for values that are JSON strings.

#### Properties
- `element`: string (string, fixed)
- `content` (string, required)

#### Examples

In JSON, an example of a string is:

```json
"foobar"
```

In Refract, this string is expanded to a `String Type`.

```json
{
  "element": "string",
  "attributes": {},
  "content": "foobar"
}
```

### Number Type (Refract Element)

A `Number Type` allows for values that are JSON numbers.

#### Properties
- `element`: number (string, fixed)
- `content` (number, required)

#### Examples

In JSON, a number is represented as:

```json
400
```

In Refract, this number is expanded to a `Number Type`.

```json
{
  "element": "number",
  "attributes": {},
  "content": 400
}
```
### Boolean Type (Refract Element)

A `Boolean Type` allows for values that are JSON boolean.

#### Properties
- `element`: boolean (string, fixed)
- `content` (boolean, required)

#### Examples

In JSON, an example of a boolean is:

```json
true
```

In Refract, this boolean is expanded to a `Boolean Type`.

```json
{
  "element": "boolean",
  "attributes": {},
  "content": true
}
```

### Array Type (Refract Element)

An `Array Type` allows for JSON arrays.

#### Properties
- `element`: array (string, fixed)
- `content` (array[Refract Element], required)


#### Examples

In JSON, an example of an array is:

```json
["foo", 400, true]
```

In Refract, this boolean is expanded to a `Boolean Type`.

```json
{
  "element": "array",
  "attributes": {},
  "content": [
    {
      "element": "string",
      "attributes": {},
      "content": "foo"
    },
    {
      "element": "number",
      "attributes": {},
      "content": 400
    },
    {
      "element": "boolean",
      "attributes": {},
      "content": true
    }
  ]
}
```

### Property Type (Refract Element)

A `Property Type` allows for values that can be used in `Object Type` elements.

#### Properties
- `element`: property (string, fixed)
- `attributes`
    - `name` (string, required) - Name of property
- `content` (Refract Element, required) - Any element that extends Refract Element

Conditions:

- Values for `name` MUST be valid JSON property names / keys.

#### Examples

This type does not have a JSON equivalent apart from `Object Type` elements. To see how this element is used, view the `Object Type` definition.

### Object Type (Refract Element)

A `Boolean Type` allows for values that are JSON boolean.

#### Properties
- `element`: object (string, fixed)
- `content` (array[Property Type], required)

#### Examples

In JSON, an example of an object is:

```json
{
  "foo": "bar"
}
```

In Refract, this object is expanded to a `Object Type`.

```json
{
  "element": "object",
  "attributes": {},
  "content": [
    {
      "element": "property",
      "attributes": {
        "name": "foo"
      },
      "content": {
        "element": "string",
        "attributes": {},
        "content": "bar"
      }
    }
  ]
}
```

## Example

This example will show a simple JSON document that is expanded to the Refract Format and then compacted into the compact structure.

### JSON Sample

```json
{
  "id": 1,
  "name": "A green door",
  "price": 12.50,
  "tags": [ "home", "green" ]
}
```

### JSON Sample to Refract Format

This is the above JSON document expanded to the Refract Format. It allows for adding attributes about each of the properties and values in the JSON document.

```json
{
  "element": "object",
  "attributes": {},
  "content": [
    {
      "element": "property",
      "attributes": {
        "name": "id"
      },
      "content": {
        "element": "number",
        "attributes": {},
        "content": 1
      }
    },
    {
      "element": "property",
      "attributes": {
        "name": "name"
      },
      "content": {
        "element": "string",
        "attributes": {},
        "content": "A green door"
      }
    },
    {
      "element": "property",
      "attributes": {
        "name": "price"
      },
      "content": {
        "element": "number",
        "attributes": {},
        "content": 12.50
      }
    },
    {
      "element": "property",
      "attributes": {
        "name": "tags"
      },
      "content": {
        "element": "array",
        "attributes": {},
        "content": [
          {
            "element": "string",
            "attributes": {},
            "content": "home"
          },
          {
            "element": "string",
            "attributes": {},
            "content": "green"
          }
        ]
      }
    }
  ]
}
```

### Refract Format Compacted

This is an example of the JSON document above represented in the compact form.

```json
["object", {}, [
  ["property", { "name": "id" },
    ["number", {}, 1]],
  ["property", { "name": "name" },
    ["string", {}, "A green door"]],
  ["property", { "name": "price" },
    ["number", {}, 12.50]],
  ["property", { "name": "tags" },
    ["array", {},
      ["string", {}, "home"],
      ["string", {}, "green"]]]]]
```

## References

- [The application/json Media Type for JavaScript Object Notation](http://tools.ietf.org/html/rfc4627)
