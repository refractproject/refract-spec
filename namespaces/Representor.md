# Representor Namespace

This document extends [Refract](../refract-spec.md) Specification to describe the [Representor](https://github.com/the-hypermedia-project/charter) DOM.

## Resource (Element)

The Resource represents a Hypermedia Resource, with its available transitions and attributes.

### Properties

- `element`: resource (string, fixed)
- `attributes` (object)
    - `relation` - (string) - An optional relation to this resource, applicable when embedded in another resource.
- `content` (object)
    - `transitions` - (array[Transition]) - The available transitions from this resource.
    - `resources` - (array[Resource]) - Any embedded (resources) from this resource.
    - `attributes` - (object) Any attributes/properties for the resource.

## Transition (Object Element)

A transition is an available progression from one state to another state.

### Properties

- `element`: transition (string, fixed)
- `attributes` (object, required)
    - `relation` - (string, required) - The relation of this transition from the current resource.
    - `suggestedContentTypes` (array[string]) - A collection of suggested content types to encode the attributes, ordered by preference.
- `content` (object, required)
    - `parameters` ([Object Type][]) - A collection of parameters for this transition.
    - `attributes` ([Object Type][]) - A collection of possible attributes for this transition.
    - `uri` (string, required) - The URI for this transition.

### Example

```json
{
    "element": "transition",
    "attributes": {
      "relation": "update"
    },
    "content": "https://polls.apiblueprint.org/questions/1"
}
```

[Object Type]: https://github.com/refractproject/refract-spec/blob/master/namespaces/mson-namespace.md#object-type-object-element

