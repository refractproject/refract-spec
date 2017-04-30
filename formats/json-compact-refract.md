# JSON Compact Refract

JSON Compact Refract is a serialization format Refract for the purpose of
removing a lot of the object keys that are repeated throughout the full
serialization of Refract, as seen in the Refract specification. It also allows
for expressing structures in a tuple, which resembles other formats like XML or
Lisp.

## Element (array)

The Element is a tuple where each item has a specific meaning. The
first item is the element name, the second is the meta attribute section, the
third is the attribute section, and the fourth is the content section.

A Refract element MUST be serialised as the following data structure as a JSON
array.

- (string, required) - Name of the element
- (object, nullable, required) - Meta attributes of the element instance
    - `id` (Element) - Unique Identifier, MUST be unique throughout the document
    - `ref` (Ref Element) - Pointer to referenced element or type
    - `classes` (Array Element[String Element]) - Array of classifications for given element
    - `title` (String Element) - Human-readable title of element
    - `description` (String Element) - Human-readable description of element
    - `links` (Array Element[Link Element]) - Meta links for a given element
- (object, nullable, required) - Attributes of the element instance
- (enum, required) - Element content with any of the following types
    - Element
    - array[Element]
    - string
    - boolean
    - number
    - null
    - Key Value Pair

## Key Value Pair (array)

A Key Value Pair MUST be serialised a JSON array with the following values:

- (string, fixed): pair
- (Element, required) - Key
- (Element, optional) - Value

## Example

If I have a String Element with the value `Hello` it would be serialised in
JSON Compact Refract as:

```json
["string", null, null, "Hello"]
```

In this example, meta attributes and attributes are both required, even if the
objects are empty. This is because this format relies on the structure of the
array in order to determine values.

If I attach a title meta attribute, the example would then be serialised as
follows:

```json
[
  "string",
  {
    "title": ["string", null, null, "My Title"]
  },
  null,
  "Hello"
]
```

See the [examples directory](examples/) for further examples.

## Pros and Cons

The benefits as mentioned are that this is a more concise format. In some
cases, it may even be easier to write, or convert from other formats such as
XML or Lisp.

One downside of this format is that it is less self-explanatory and harder to
understand as a human.
