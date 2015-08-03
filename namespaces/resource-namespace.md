# Resource Namespace

This document extends [Refract][] [Data Structure Namespace][] to define REST Resource data structure elements.

## Content

<!-- TOC depth:3 withLinks:1 updateOnSave:0 -->
- [Resource Namespace](#resource-namespace)
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

## Resource Elements

### Resource (Element)

The Resource representation with its available transitions and attributes.

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

    - `parameters` (Href Variables) - Input parameters.

        Definition of any input URI path segments or URI query parameters for this transition.

        If `href` and `parameters` attributes aren't set, the parent `resource`
        element `hrefVariables` SHOULD be used to resolve the transition input
        parameters.

    - `attributes` (Data Structure) - Input attributes.

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
    - `method` (string) - HTTP request method.
    - `href` (Href) - A concrete URI for the request.

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
