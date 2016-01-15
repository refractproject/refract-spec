# Compact Refract

Compact Refract is a serialization format Refract for the purpose of removing a
lot of the object keys that are repeated throughout the full serialization of
Refract, as seen in the Refract specification. It also allows for expressing
structures in a tuple, which resembles other formats like XML or Lisp.

## Dependencies

- [Refract Base
Specification](https://github.com/refractproject/refract-spec/blob/master/refract-spec.md)

## Data Structures

### Compact Element (array)

The Compact Element is a tuple where each item has a specific meaning. The
first item is the element name, the second is the meta attribute section, the
third is the attribute section, and the fourth is the content section.

#### Members

- (string, required) - Name of the element
- (object, required) - Meta attributes of the element instance.
  - `id` - Unique Identifier, MUST be unique throughout the document
  - `ref` (Element Pointer) - Pointer to referenced element or type
  - `classes` (array[string]) - Array of classifications for given element
  - `title` (string) - Human-readable title of element
  - `description` (string) - Human-readable description of element
  - `links` (array[Link Element]) - Meta links for a given element
- (object, required) - Attributes of the element instance
- (enum, required) - Element content with any of the following types
  - (null)
  - (string)
  - (number)
  - (boolean)
  - (array)
  - (object)
  - (Compact Element)
  - (array[Compact Element])

## Example

In the base specification, serialization looks something like this for JSON:

```json
{
  "element": "foo",
  "content": "bar"
}
```

In Compact Refract, this same example looks like this:

```json
["foo", {}, {}, "bar"]
```

In this example, meta attributes and attributes are both required, even if the
objects are empty. This is because this format relies on the structure of the
array in order to determine values.

## Pros and Cons

The benefits as mentioned are that this is a more concise format. In some
cases, it may even be easier to write, or convert from other formats such as
XML or Lisp.

One downside of this format is that there is no simple way to distinguish a
normal array from a Compact Refract array. This makes it hard to embed Refract
within normal data structures, requiring that either the entire structure be
converted to Compact Refract, or that the user relies on domain-specific
information.
