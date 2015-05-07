# API Namespace

This document extends [Refract][] [Resource Namespace][] to define REST API data structure elements.

## Content

<!-- TOC depth:2 withLinks:1 updateOnSave:1 -->
- [API Namespace](#api-namespace)
	- [Content](#content)
	- [About this Document](#about-this-document)
	- [Category (Element)](#category-element)
	- [Copy (Element)](#copy-element)
<!-- /TOC -->

## About this Document

This document conforms to [RFC 2119][], which says:

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

[MSON][] is used throughout this document.

## Category (Element)

Grouping element – a set of elements forming a logical unit of an API such as
group of related resources or data structures.

A category element MAY include additional classification of the category.
The classification MAY hint what is the content or semantics of the category.
The classification MAY be extended and MAY contain more than one classes.

For example a `category` element may be classified both as `resourceGroup` and
`dataStructures` to denote it includes both resource and data structures.

### Properties

- `element`: category (string, fixed)
- `meta`
    - `class` (array, fixed)
        - (enum[string])
            - api - Category is a API top-level group.
            - resourceGroup - Category is a set of resource.
            - dataStructures - Category is a set of data structures.
            - scenario - Reserved. Category is set of steps.
- `content` (array[Element])

### Example

```json
{
    "element": "category",
    "meta": {
        "class": "api",
        "title": "Polls API"
    },
    "content": [
        {
            "element": "category",
            "meta": {
                "class": "resourceGroup",
                "title": "Question",
                "description": "Resources related to questions in the API."
            },
            "content": []
        }
    ]
}
```

## Copy (Element)

Copy element represents a copy text. A textual information in API description.
Its content is a string and it MAY include information about the media type
of the copy's content.

If a Copy element the parent's element `description` metadata MAY include its
content.

The Copy element MAY appear as a content of any element defined in the base
namespaces.

### Properties

- `element`: copy (string, fixed)
- `attributes` (object)
    - `contentType` (string) - Optional media type of the content E.g. text/html or text/plain.
- `content` (string)

### Example

Given an API description with following layout:


- Group
    - Copy "Lorem Ipsum"
    - Resource "A"
    - Resource "B"
    - Copy "Dolor Sit Amet"

```json
{
    "element": "category",
    "meta": {
        "description": "Lorem Ipsum\nDolor Sit Amet"
    },
    "content": [
        {
            "element": "copy",
            "content": "Lorem Ipsum"
        },
        {
            "element": "resource"
        },
        {
            "element": "resource"
        },
        {
            "element": "copy",
            "content": "Dolor Sit Amet"
        }
    ]
}
```

---

[MSON]: https://github.com/apiaryio/mson
[Refract]: ../refract-spec.md
[MSON Namespace]: mson-namespace.md
[Resource Namespace]: resource-namespace.md
