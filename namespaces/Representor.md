# Representor Namespace

This document extends [Refract](../refract-spec.md) Specification to describe the [Representor](https://github.com/the-hypermedia-project/charter) DOM.

## Representor (Object Element)

The Representor represents a Hypermedia Resource, with it's available links, transitions and attributes.

### Properties

- `links` - (array[Link]) - The links from this resource.
- `transitions` - (array[Transition]) - The available transitions from this resource.
- `representors` - (array[Representor]) - The embedded links (resources) from this resource.
- `attributes` - (object) - Any properties of the resource.
- `metadata` - (object) _ Meta Attributes, for example, may include a `title` and `description`.

## Link (Object Element)

A link element representing a link and it's relation from the Representor.

### Properties

- `relation` - (string, required) - The relation from the Representor to this link.
- `uri` - (string, required) - The URI for this link.

### Example

```json
{
    "element": "object",
    "content": [
        {
            "key": {
                "element": "string",
                "content": "relation"
            },
            "value": {
                "element": "string",
                "content": "self"
            }
        }, {
            "key": {
                "element": "string",
                "content": "uri"
            },
            "value": {
                "element": "string",
                "content": "https://polls.apiblueprint.org/questions/1"
            }
        }
    ]
}
```

## Transition (Object Element)

A transition is an available progression from one state to another state.

### Properties

- `relation` - (string, required) - The relation of this transition from the current resource.
- `uri` - (string, required) - The URI for this transition.
- `parameters` (array[Input Property])
- `attributes` (array[Input Property])

### Example

```json
{
    "element": "object",
    "content": [
        {
            "key": {
                "element": "string",
                "content": "relation"
            },
            "value": {
                "element": "string",
                "content": "update"
            }
        }, {
            "key": {
                "element": "string",
                "content": "uri"
            },
            "value": {
                "element": "string",
                "content": "https://polls.apiblueprint.org/questions/1"
            }
        }
    ]
}
```

## Input Property

An Input Property is used to describe a potential property or attribute used to perform a transition.

### Properties

- `name` (string, required) - The name for this property.
- `type` (string) - The type of element used to represent the properties value.
- `defaultValue` (Any Type) - An optional default value for this property.

### Example

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
                "content": "username"
            }
        }, {
            "key": {
                "element": "string",
                "content": "type"
            },
            "value": {
                "element": "string",
                "content": "string"
            }
        }
    ]
}
```

