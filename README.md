# Refract

Refract is a a recursive data structure for expressing complex structures, relationships, and metadata.

## Documents

- [Full Specification](refract-spec.md)
- [MSON Namespace](namespaces/mson-namespace.md)

## Version

**Current Version**: 0.1.0

**Note**: This specification is currently in development and may change before getting to a more stable 1.0 version. Please be mindful of this if using this production environments.

## Libraries

- [Minim (JavaScript)](https://github.com/smizell/minim)

## About

The purpose of Refract is to provide a structure for data that is not coupled to the data itself. While this is a departure from how JSON is currently used, it is a way of future-proofing clients.

### Why Refract?

Over and over, standards are created to provide additional layers of data on top of existing data. In the web world, we see this with media types, link relations, profiles, etc., where data and its semantics are being defined in different documents and in different structures.

Additionally, we see JSON formats that couple the representation of data to the structure of the JSON document. Clients are written to utilize this structure, which means if data changes, structure changes, and if structure changes, clients break.

The aim of Refract is to provide a standard structure to prevent clients from breaking in this way. In Refract, the data is decoupled from the structure. It provides a way to focus on semantics at any level rather than worry about the documents structure.

### Annotating JSON

Because of this separation, Refract provides the ability to annotate existing JSON without breaking the structure of the JSON document. XML provides the ability to add attributes about elements, but unfortunately idiomatic JSON does not. Refract can be used to add these attributes.

Many other formats try to annotate JSON by adding properties into the structure of the JSON document. While the aim of this was to provide simplicity, it does not add clarity, as it is mainly two documents merged together.

#### Example

Here is an example of a JSON document of a place.

```json
{
  "name": "The Empire State Building",
  "description": "The Empire State Building is a 102-story landmark in New York City.",
  "image": "http://www.civil.usherbrooke.ca/cours/gci215a/empire-state-building.jpg"
}
```

JSON-LD is a format used to annotate JSON structures by adding in semantics and linked data. Here is how the JSON above would be modified to include semantic linked data.

```json
{
  "@context": {
    "name": "http://schema.org/name",
    "description": "http://schema.org/description",
    "image": {
      "@id": "http://schema.org/image",
      "@type": "@id"
    }
  },
  "name": "The Empire State Building",
  "description": "The Empire State Building is a 102-story landmark in New York City.",
  "image": "http://www.civil.usherbrooke.ca/cours/gci215a/empire-state-building.jpg"
}
```

Instead of merging documents, Refract takes a different approach that creates a layer on top of the existing structure.

```json
{
  "element": "object",
  "content": [
    {
      "key": {
        "element": "string",
        "content": "name"
      },
      "value": {
        "element": "string",
        "meta": {
          "ref": "http://schema.org/name"
        },
        "content": "The Empire State Building"
      }
    },
    {
      "key": {
        "element": "string",
        "content": "description"
      },
      "value": {
        "element": "string",
        "meta": {
          "ref": "http://schema.org/description"
        },
        "content": "The Empire State Building is a 102-story landmark in New York City."
      }
    },
    {
      "key": {
        "element": "string",
        "content": "image"
      },
      "value": {
        "element": "string",
        "meta": {
          "ref": "http://schema.org/image"
        },
        "content": "http://www.civil.usherbrooke.ca/cours/gci215a/empire-state-building.jpg"
      }
    }
  ]
}
```

Refract is not meant to be a replacement for JSON-LD. The purpose of this example is to show the approach that Refract uses in annotating existing JSON structures by expanding them into a new structure that can be easily annotated.


### Richer Data Structures

In addition to providing the ability to annotate existing documents, Refract can be used to create more complex data structures. As mentioned above, XML provides the ability to add attributes to element values, while JSON alone does not have this ability. Refract is meant to be a recursive structure that can do what XML does, but in JSON, and in ways that XML does not provide.

For example, XML cannot provide ways to include meta data about attributes. Refract elements may be used in the content of elements, but also in attributes and even the element name itself.

Because of this, Refract can also be used for JSON documents as well as annotating XML documents.


### Simpler SDKs

Using this data structure allows for writing small, reusable classes that define methods that can be used for each element. Rather than writing an SDK that conforms to a specific data structure, SDKs may be written that provide APIs to elements. Libraries can then be written separate from the structure of data to allow for data to evolve over time.

### JSON Document Object Model

Since JSON libraries can be found in most platforms and languages, Refract provides a structure for cross-platform and cross-language object models.

Additionally, this means that Refract documents could be queried in the same fashion the DOM is queried, providing a more flexible structure.

## Uses

- Replace brittle and complex JSON structures
- Recursively annotate existing JSON structures
- Create markup languages that cross boundaries between formats such as XML and JSON
- Provide a JSON version of an existing XML document structure

## Authors

- [Stephen Mizell](https://github.com/smizell)
- [Mark Foster](https://github.com/fosrias)
- [Zdenek Nemec](https://github.com/zdne)
