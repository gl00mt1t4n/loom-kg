---
id: properties
type: index
domain: Systems
links:
  - [[Root Index]]
  - [[Registries/Tags|Tags]]
---

# Properties

Controlled properties for normal KG notes.

## Required

| Property | Meaning |
|---|---|
| `id` | unique kebab-case node ID |
| `type` | one approved type |
| `domain` | one approved primary domain |

## Optional

| Property | Meaning |
|---|---|
| `date` | `YYYY-MM-DD` |
| `sources` | URLs, paths, observations, source references |
| `links` | important wikilinks or node IDs |
| `tags` | approved broad tags only |
| `hashtags` | informal human-only labels |
| `revisit_if` | condition that should trigger review |
| `linear` | task ID(s), if using Linear |
| `course` | course identifier, if useful |
| `superseded_by` | replacement note ID or wikilink |

## Approved types

- `index`
- `concept`
- `decision`
- `thesis`
- `system`
- `tombstone`

## Starter domains

- `Learning`
- `Work`
- `Systems`
- `Decisions`

Agents should replace the starter domains with the user's chosen domains during setup.
