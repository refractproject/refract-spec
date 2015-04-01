# Representor Namespace

This document extends [Refract](../refract-spec.md) Specification to describe the [Representor](https://github.com/the-hypermedia-project/charter) DOM.

## Resource (Object Element)

The Resource represents a Hypermedia Resource, with it's available relations, transitions and attributes.

### Properties

- `element`: resource (string, fixed)
- `content`: (object)
    - `relations` - (array[Relation]) - The relations from this resource.
    - `transitions` - (array[Transition]) - The available transitions from this resource.
    - `resources` - (array[Resource]) - The embedded relations (resources) from this resource.
    - `attributes` - (object) - Any properties of the resource.
    - `relation` - (string) - An optional relation to this resource.

## Relation (Object Element)

A relation element representing a relation to another resource.

### Properties

- `element`: relation (string, fixed)
- `content`: (object)
    - `relation` - (string, required) - The relation from the Resource to this resource.
    - `uri` - (string, required) - The URI for this relation.

### Example

```json
{
    "element": "relation",
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

- `element`: transition (string, fixed)
- `content`: (object)
    - `relation` - (string, required) - The relation of this transition from the current resource.
    - `uri` - (string, required) - The URI for this transition.
    - `parameters` (array[Input Property])
    - `attributes` (array[Input Property])

### Example

```json
{
    "element": "transition",
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

- `element`: property (string, fixed)
- `content`: (object)
    - `name` (string, required) - The name for this property.
    - `type` (string) - The type of element used to represent the properties value.
    - `defaultValue` (Any Type) - An optional default value for this property.

### Example

```json
{
    "element": "property",
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

