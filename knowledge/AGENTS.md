# Personal Knowledge Base Schema

This knowledge base follows the LLM Wiki pattern: raw sources stay immutable, while wiki pages are maintained as a persistent, interlinked synthesis.

## Layers

1. `raw/`: source files exactly as received.
2. `wiki/`: curated Markdown pages generated from sources and conversations.
3. `index.md` and `log.md`: navigation and chronological maintenance records.

## Ingest Rules

- Preserve private source material in `raw/`.
- Do not publish phone numbers, home addresses, birth dates, guardian names, or other sensitive personal information.
- Create or update topic pages when a source adds meaningful evidence.
- Add source references at the bottom of each wiki page.
- Update `index.md` after each ingest.
- Append a dated entry to `log.md`.

## Page Types

- `profile.md`: public personal profile and positioning.
- `learning-map.md`: academic, activities, and growth trajectory.
- `experience.md`: leadership, work, awards, and practical experience.
- `website-plan.md`: website information architecture and visual direction.

## Query Rules

- Read `index.md` first.
- Answer from wiki pages when possible.
- If a new synthesis is useful, file it as a wiki page.
- Flag contradictions, missing sources, or stale claims.
