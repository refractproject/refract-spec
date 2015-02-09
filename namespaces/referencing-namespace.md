# Referencing Namespace

This namespace defines elements and attributes that may be used to provide the ability to reference and classify elements and namespaces.

This document includes the elements as defined in the Refract specification.

## Referencing and Identifying Elements

These elements provide the means to identify elements with unique or reused qualifiers.

### Ref (Element)

The `ref` element provides a way to reference elements and namespaces with a URI. The context the `ref` element is found in determines what exactly it references. Additionally, the referenced

#### Properties

- `element`: ref (string, required)
- `content` (string, required) - The URI of the referenced item

### ID (Element)

The `id` element provides a document-wide unique identifier. It MUST be unique for the entire document in which is found. When used as an attribute for another element, it defines the unique ID for that element, and MAY be used in the fragment identifier to link to that element.

#### Properties

- `element`: id (string, required)
- `content` (string, required) - The unique identifier for an element

#### Example

This example shows the `id` element used as an attribute to provide a unique identifier.

```json
{
  "element": "foo",
  "attributes": {
    "id": "my-foo"
  },
  "content": "bar"
}
```

In this example, the `foo` element has an `id` of `my-foo`, which can be used to reference this specific instance of the `foo` element.

### Roles (Element)

The `roles` element allows for giving specific roles to element based on the context in which they are found. The roles MAY be reused throughout the document to provide more specific classification, uses, and roles of elements. It provides element reuse without the need for extending or creating new elements.

#### Properties

- `element`: roles (string, required)
- `content` (array[string])

#### Example

This example shows the `roles` element being used as an attribute.

```json
{
  "element": "user",
  "attributes": {
    "roles": ["customer"]
  },
  "content": [
    {
      "element": "id",
      "content": 4
    }
  ]
}
```

Using `roles`, the `user` element is given a more specific classification as a customer.

## Namespacing

Namespacing provides a way to do the following in a document:

- Include elements directly from other documents
- Define a prefix for referencing elements in defined namespaces

This functionality exists to provide extendability and prevent name collisions in the event that two or more namespace specify the same element name.

### Require (Element)

The `require` element allows for including elements from namespaces or defining prefixes for namespaces that may be used throughout the document.

#### Properties

- `element`: require (string, required)
- `content` (array[Namespace])

### Namespace (Element)

The `namespace` element is used for defining and referencing namespaces depending on its context. When used in a `require` element, it defines namespaces and their prefixes. When used in elements like `type` (defined below), it references the specified namespace.

It MAY also be used as an attribute if defined by the particular namespace or element, and its used depends on how it is defined to be used.

#### Properties

- `element`: namespace (string, required)
- `attributes`
    - `prefixAs` (string, optional) - Unique name to be used to reference this namespace throughout the document.
- `content` (string, required) - Resolvable URI of namespace, which MAY be relative or absolute

#### Example

```json
{
  "element": "require",
  "content": [
    {
      "element": "namespace",
      "content": "http://example.com/foo"
    },
    {
      "element": "namespace",
      "attributes": {
        "prefixAs": "bar"
      },
      "content": "http://example.com/bar"
    }
  ]
}
```

There are two namespaces used here, one without the prefix and one with the prefix.

- The first namespace defined for `http://example.com/foo` MUST have all of its elements available in the document in which it is required. If there is a conflict in element names, the namespace defined latest in the document MUST receive precedence.
- The second namespace for `http://example.com/bar` has a prefix specified, which means its elements will MUST NOT be included in the document by default, but MUST be made available for referencing using the given prefix. If there is a conflict in prefix names, the prefix defined last MUST receive precedence.

### Type (Element)

The `type` element provides a way to add additional data about an element. In regards to how it is defined here, it is used for specifying a namespace in which the element may be found.

#### Properties

- `element`: type (string, required)
- `attributes`
   - `ref` (string) - Link directly to an element using the element's ID in the fragment identifier
   - `namespace` (string) - Specify the namespace in which the element may be found
   - `prefix` (string) - Specify the prefix of the required namespace in which the element may be found
- `content` (string, required) - The name of the element

#### Example

```json
{
  "element": "items",
  "content": [
    {
      "element": "foo",
      "content": 1
    },
    {
      "element": {
        "element": "type",
        "attributes": {
          "ref": "http://example.com/bar#foo"
        },
        "content": "foo"
      },
      "content": 2
    },
    {
      "element": {
        "element": "type",
        "attributes": {
          "namespace": "http://example.com/bar"
        },
        "content": "foo"
      },
      "content": 3
    },
    {
      "element": {
        "element": "type",
        "attributes": {
          "prefix": "bar"
        },
        "content": "foo"
      },
      "content": 4
    }
  ]
}
```

This example shows an `items` element that has four elements as its content.

- The first element shows the `foo` element used in the normal way. This assumes that `foo` has already been either defined in this namespace or included from another namespace.
- The second element shows the `foo` element using the `ref` attribute to link directly to where the `foo` element is defined
- The third element shows the `foo` element using the `namespace` attribute to link to the namespace in which the `foo` element is defined
- The fourth element shows the `foo` element using the `prefix` attribute to reference a namespace that has been included
