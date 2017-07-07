# Refract

Refract is a recursive data structure for expressing complex structures, relationships, and metadata.

## Documents

- [Full Specification](refract-spec.md)
- [Data Structure Namespace](namespaces/data-structure-namespace.md)
- [API Description Namespace](namespaces/api-description-namespace.md)
- [Parse Result Namespace](namespaces/parse-result-namespace.md)

## Version

**Current Version**: 0.7.0

**Note**: This specification is currently in development and may change before getting to a more stable 1.0 version. Please be mindful of this if using this production environments.

## Serialization Formats

- [JSON Refract](formats/json-refract.md)
- [JSON Compact Refract](formats/json-compact-refract.md)

## Libraries

- [Minim (JavaScript)](https://github.com/smizell/minim)
- [Refract (Python)](https://github.com/kylef/refract.py)

## About

Refract is a structure for handling all sorts and kinds of data across all sorts and kinds of formats. That's a very general-purpose description for a general-purpose structure. To get an idea of what Refract does, we'll walk through some of its uses with some examples along the way.

### As a way to annotate data

Refract provides the ability to take data structures and add a layer on top of it for the purpose of annotating and adding semantic data. Refract is not the first structure to try and tackle this task, though it does take a different approach. Instead of creating an entirely different structure to describe the data, Refract's approach is to expand the existing structure (we call it "refracting" a structure). Here is an example to show our point.

Take the following simple object which contains a name and email.

- name: John Doe
- email: john@example.com

Using Refract, we can expand this out and add some human-readable titles and descriptions. As JSON that may look as follows:

```json
{
  "element": "object",
  "content": [
    {
      "element": "member",
      "meta": {
        "title": {
          "element": "string",
          "content": "Name"
        },
        "description": {
          "element": "string",
          "content": "Name of a person"
        }
      },
      "content": {
        "key": {
          "element": "string",
          "content": "name"
        },
        "value": {
          "element": "string",
          "content": "John Doe"
        }
      }
    },
    {
      "element": "member",
      "meta": {
        "title": {
          "element": "string",
          "content": "Email",
        },
        "description": {
          "element": "string",
          "content": "Email address for the person"
        }
      },
      "content": {
        "key": {
          "element": "string",
          "content": "email"
        },
        "value": {
          "element": "string",
          "content": "john@example.com"
        }
      }
    }
  ]
}
```

We added some semantic data to the existing data, but we did so while retaining the semantic structure of the data with the `object` and `string` elements. **This means there is no semantic difference in the Refract structure and the original JSON structure**. It also means we can add extra semantics on top of these structural ones.

Just some notes on Refract, the `meta` section shown here is reserved for Refract-specific properties for each element. These properties provide ways to address and link to data, add human-readable data as such, and even include profile of defined elements.

### As a unifying structure

If you have a keen eye, you may have noticed the similarities between the JSON example above and XML. XML has elements, attributes, and content. If you caught this and wanted to ask if we simply turned JSON into XML, you'd be asking a fair question.

Refract is actually meant to provide these cross-format similarities. It means that a JSON structure may be refracted and converted to XML. It also means an XML document may be converted into Refract. This also goes for YAML, HTML, CSV, and many other formats. Refract is a way to unify these structures.

Since we said we'd include examples, let's look at moving XML over into Refract.

```xml
<person name="John Doe" email="john@example.com">
```

This example in refracted form would look like this. Notice that we're using `attributes` instead of `meta` because `attributes` are free to be used.

```json
{
  "element": "person",
  "attributes": {
    "name": {
      "element": "string",
      "content": "John Doe"
    },
    "email": {
      "element": "string",
      "content": "john@example.com"
    }
  }
}
```

Because we can go back and forth between JSON, XML, and other formats, we are now free to use toolsets across formats. That means we could use XSLT to transform JSON documents.

### As a queryable structure

Refract is meant to free you from the structure of your documents, similar to how XML does with things like XPATH or the DOM. It means we can now query JSON documents as if there was an underlying DOM, which **decouples our clients from our structure and our structure from our data**.

### As a model for client libraries

Lastly, Refract is meant to provide a model for client libraries. As mentioned, it decouples our clients from structure and data. It also means we only have to deal with one thing and that is an element. Elements can be of different types with different definitions, but only having one kind of thing to work great simplifies our client library's needs.

## Authors

- [Stephen Mizell](https://github.com/smizell)
- [Mark Foster](https://github.com/fosrias)
- [Zdenek Nemec](https://github.com/zdne)
- [Daniel G. Taylor](https://github.com/danielgtaylor)
- [Kyle Fuller](https://fuller.li)
