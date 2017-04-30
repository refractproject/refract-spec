# Refract Examples

This directory contains examples of serialise Refract elements.

## Formats

Examples are supplied for the following formats:

- JSON Serialisation (`.json`)
- Compact JSON Serialisation (`.compact.json`)

## Files

### Element (`element`)

A basic element with a primitive value as content.

- element: string
- content: Hello World

### Element Element (`element-element`)

An element which has an element as content.

- element: item
- content (Element)
    - element: string
    - content: value

### Element Array (`element-array`)

An element which has an array of elements as content.

- element: array
- content (array)
    - (Element)
        - element: string
        - content: Hello World

### Element Key Value Pair (`element-kv`)

- element: member
- content
    - key (Element)
        - element: string
        - content: Name
    - value (Element)
        - element: string
        - content: Doe

### Element Title Meta (`element-meta-title`)

- element: string
- meta
    - title (Element)
        - element: string
        - content: Name
- content: Doe

### Element Attributes (`element-attributes`)

- element: string
- attributes
    - method (Element)
        - element: string
        - content: GET
- content: /
