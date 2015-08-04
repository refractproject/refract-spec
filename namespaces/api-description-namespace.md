# API Description Namespace

This document extends [Refract][] [Data Structure Namespace][] to define REST Resource data structure elements.

## Content

<!-- TOC depth:3 withLinks:1 updateOnSave:0 -->
- [API Description Namespace](#api-description-namespace)
    - [Content](#content)
    - [About this Document](#about-this-document)
    - [Supporting Data Types](#supporting-data-types)
        - [Href (string)](#href-string)
        - [Templated Href (string)](#templated-href-string)
        - [Href Variables (Object Type)](#href-variables-object-type)
        - [Data Structure (Data Structure Element)](#data-structure-data-structure-element)
        - [Asset (Element)](#asset-element)
    - [Resource Elements](#resource-elements)
        - [Resource (Element)](#resource-element)
        - [Transition (Element)](#transition-element)
        - [Category (Element)](#category-element)
        - [Copy (Element)](#copy-element)
    - [Protocol-specific Elements](#protocol-specific-elements)
        - [HTTP Transaction (Element)](#http-transaction-element)
        - [HTTP Headers (Array Type)](#http-headers-array-type)
        - [HTTP Message Payload (Element)](#http-message-payload-element)
        - [HTTP Request Message (HTTP Message Payload)](#http-request-message-http-message-payload)
        - [HTTP Response Message (HTTP Message Payload)](#http-response-message-http-message-payload)

<!-- /TOC -->

## About this Document

This document conforms to [RFC 2119][], which says:

> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

[MSON][] is used throughout this document.

## Supporting Data Types

### Href (string)

The value of the `Href` type  SHOULD be resolved as a URI-Reference per [RFC 3986][] and MAY be a relative reference to a URI.
The value of the `Href` type MUST NOT be a URI Template.

### Templated Href (string)

The value of `Templated Href` type is to be used as a URI Template, as defined in [RFC 6570][].
The value of the `Templated Href` type is a template used to determine the target URI of the related resource or transition.
The value of the `Templated Href` type SHOULD be resolved as a URI-Reference per [RFC 3986][] and MAY be a relative reference to a URI.

### Href Variables (Object Type)

The definition is a Data Structure namespace `Object Type` where keys are respective URI Template variables.

#### Properties

- `element`: hrefVariables (string, fixed)

### Data Structure (Data Structure Element)

Data structure definition using Data Structure namespace elements.

#### Properties

- `element`: dataStructure (string, fixed)

### Asset (Element)

Arbitrary data asset.

#### Properties

- `element`: asset (string, fixed)
- `meta`
    - `class` (array, fixed)
        - (enum[string])
            - messageBody - Asset is an example of message-body
            - messageBodySchema - Asset is an schema for message-body
- `attributes` (object)
    - `contentType` (string) - Optional media type of the asset
    - `href` (Href) - Link to the asset
- `content` (string) - A textual representation of the asset

## API Description Elements

### Resource (Element)

The Resource representation with its available transitions and its data.

#### Properties

- `element`: resource (string, fixed)
- `attributes` (object)
    - `href` (Templated Href) - URI Template of this resource.
    - `hrefVariables` (Href Variables) - Definition of URI Template variables used in the `href` property.
- `content` (array)
    - (Transition) - State transition available for this resource.

        The `content` MAY include multiple `Transition` elements.

    - (Data Structure) - Data structure representing the resource.

        The `content` MUST NOT include more than one `Data Structure`.

#### Example

```json
{
    "element": "resource",
    "meta": {
        "title": "Question",
        "description": "A Question object has the following attributes."
    },
    "attributes": {
        "href": "/questions/{question_id}",
        "hrefVariables": {
            "element": "hrefVariables",
            "content": [
                {
                    "element": "member",
                    "content": {
                        "key": {
                            "element": "string",
                            "content": "question_id"
                        }
                    }
                }
            ]
        }
    },
    "content": [
        {
            "element": "dataStructure"
        }
    ]
}
```

### Transition (Element)

A transition is an available progression from one state to another state.
Exercising a transition initiates a transaction.

The content of this element is array of protocol-specific transactions.

Note: At the moment only the HTTP protocol is supported.

#### Properties

- `element`: transition (string, fixed)
- `attributes` (object)
    - `relation` - (string) - Link relation type as specified in [RFC 5988][].

        The value of `relation` attribute SHOULD be interpreted as a link relation
        between transition's parent resource and the transition's target resource
        as specified in the `href` attribute.

    - `href` (Templated Href) - The URI template for this transition.

        If present, the value of the `href` attribute SHOULD be used to resolve
        target URI of the transition.

        If not set, the parent `resource` element `href` attribute SHOULD be
        used to resolve the target URI of the transition.

    - `hrefVariables` (Href Variables) - Input parameters.

        Definition of any input URI path segments or URI query parameters for this transition.

        If `href` and `hrefVariables` attributes aren't set, the parent `resource`
        element `hrefVariables` SHOULD be used to resolve the transition input
        parameters.

    - `data` (Data Structure) - Input attributes.

        Definition of any input message-body attribute for this transition.

- `content` (array[HTTP Transaction]) - Array of transaction examples.

    Transaction examples are protocol-specific examples of REST transaction
    that was initialized by exercising a transition.

    For the time being this namespace defines only HTTP-specific transaction
    data structures.

#### Example

```json
{
    "element": "transition",
    "attributes": {
        "relation": "update",
        "href": "https://polls.apiblueprint.org/questions/{question_id}"
    },
    "content": null
}
```

### Category (Element)

Grouping element – a set of elements forming a logical unit of an API such as
group of related resources or data structures.

A category element MAY include additional classification of the category.
The classification MAY hint what is the content or semantics of the category.
The classification MAY be extended and MAY contain more than one classes.

For example a `category` element may be classified both as `resourceGroup` and
`dataStructures` to denote it includes both resource and data structures. It
may also include the `transitions` classification to denote it includes
transitions.

#### Properties

- `element`: category (string, fixed)
- `meta`
    - `class` (array, fixed)
        - (enum[string])
            - api - Category is a API top-level group.
            - resourceGroup - Category is a set of resource.
            - dataStructures - Category is a set of data structures.
            - scenario - Reserved. Category is set of steps.
            - transitions - Category is a group of transitions.
- `attributes`
    - `meta` (array[Member Element]) - Arbitrary metadata

        Note the "class" of the Member Element can be used to distinguish the
        source of metadata as follows:

        - Class `user` - User-specific metadata. Metadata written in the source.
        - Class `adapter` - Serialization-specific metadata. Metadata provided by adapter.

- `content` (array[Element])

#### Example

```json
{
    "element": "category",
    "meta": {
        "class": [
            "api"
        ],
        "title": "Polls API"
    },
    "attributes": {
        "meta": [
            {
              "element": "member",
              "meta": {
                  "class": ["user"]
              },
              "content": {
                  "key": {
                      "element": "string",
                      "content": "HOST",
                  },
                  "value": {
                      "element": "string",
                      "content": "http://polls.apiblueprint.org/"
                  }
              }
            }
        ]
    },
    "content": [
        {
            "element": "category",
            "meta": {
                "class": [
                    "resourceGroup"
                ],
                "title": "Question",
                "description": "Resources related to questions in the API."
            },
            "content": []
        }
    ]
}
```

### Copy (Element)

Copy element represents a copy text. A textual information in API description.
Its content is a string and it MAY include information about the media type
of the copy's content.

If an element contains a Copy element, the element's `description` metadata
MAY include the Copy element's content.

The Copy element MAY appear as a content of any element defined in the base
namespaces.

#### Properties

- `element`: copy (string, fixed)
- `attributes` (object)
    - `contentType`: *text/plain* (string) - Optional media type of the content.
- `content` (string)

#### Example

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

## Protocol-specific Elements

### HTTP Transaction (Element)

Example of an HTTP Transaction. The example's content consist of a request-response
message pair. A transaction example MUST contain exactly one HTTP request and one HTTP response message.

#### Properties

- `element`: httpTransaction (string, fixed)
- `content` (array, fixed) - Request response message pair (tuple).

    The array MUST contain exactly two elements.

    - Elements
        - (HTTP Request Message)
        - (HTTP Response Message)

#### Example

```json
{
    "element": "httpTransaction",
    "content": [
        {
            "element": "httpRequest",
            "attributes": {
                "method": "GET",
                "href": "https://polls.apiblueprint.org/questions/1"
            },
            "content": null
        },
        {
            "element": "httpResponse",
            "attributes": {
                "statusCode": 200
            },
            "content": [
                {
                    "element": "asset",
                    "meta": {
                        "class": "messageBody"
                    },
                    "attributes": {
                      "contentType": "application/json"
                    },
                    "content": "{\"name\": \"John\"}"
                }
            ]
        }
    ]
}
```

### HTTP Headers (Array Type)

Ordered array of HTTP header-fields.

The `name` meta attribute value of every element in the `content` SHOULD be
interpreted as HTTP header field-name as defined in [RFC 7230][].

#### Properties

- `element`: `httpHeaders`
- `content` (array)
    - (Element)
        - `meta`
            - `name` (string) - HTTP header field-name.

#### Example

```json
{
    "element": "httpHeaders",
    "content": [
        {
            "element": "member",
            "content": {
                "key": {
                    "element": "string",
                    "content": "Content-Type"
                },
                "value": {
                    "element": "string",
                    "content": "application/json"
                }
            }
        }
    ]
}
```

### HTTP Message Payload (Element)

Payload of an HTTP message. Its metadata in the form of headers and data in form
of Data structure or assets.

#### Properties

- `attributes`
    - `headers` (HTTP Headers)
- `content` (array)
    - (Data Structure) - Data structure describing the payload.

        The `content` MUST NOT contain more than one `Data Structure`.

    - (Asset) - A data asset associated with the payload's body.

        This asset MAY represent payload body or body's schema.

        The `content` SHOULD NOT contain more than one asset of its respective type.

### HTTP Request Message (HTTP Message Payload)

HTTP request message.

#### Properties

- `element`: httpRequest (string, fixed)
- `attributes`
    - `method` (string) - HTTP request method. The method value SHOULD be inherited from a parent transition if it is unset.
    - `href` (Href) - A concrete URI for the request. The href SHOULD be inherited from a parent transition by expanding the href and hrefVariables if unset.

### HTTP Response Message (HTTP Message Payload)

HTTP response message.

#### Properties

- `element`: httpResponse (string, fixed)
- `attributes`
    - `statusCode` (number) - HTTP response status code.

---


[MSON]: https://github.com/apiaryio/mson
[Refract]: ../refract-spec.md
[Data Structure Namespace]: data-structure-namespace.md

[RFC 2119]: https://datatracker.ietf.org/doc/rfc2119/
[RFC 3986]: https://datatracker.ietf.org/doc/rfc3986/
[RFC 5988]: http://datatracker.ietf.org/doc/rfc5988/
[RFC 6570]: https://datatracker.ietf.org/doc/rfc6570/
[RFC 7230]: http://datatracker.ietf.org/doc/rfc7230/
