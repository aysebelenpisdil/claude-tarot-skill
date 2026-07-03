---
description: Spread catalog, or the full position map of one spread
---

Source of truth: `references/spreads.json`. Read it first. `SPREADS.md` may be used for supporting prose, never for structure.

User input: "$ARGUMENTS"

- If the input is empty, present the catalog: every spread with its name, id, card count and description. Mark spreads whose `requires_method` file is missing under `references/books/extracted/methods/` as disabled ("your books do not cover this method"). Mention that `/tarot-info <spread-id>` shows the full detail of one spread.
- If the input names a spread (by id or name), present its deep detail: what it is for, when to choose it, and the complete position map — every position with its name and meaning, in order. For `deep-intuitive`, include its warning. For conditional spreads, state whether they are currently enabled.

This command only informs; it never draws cards. Answer in the user's language.
