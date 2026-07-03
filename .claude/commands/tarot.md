---
description: Tarot reading — spread menu or spread suggestion for your question
---

Follow the tarot skill (`.claude/skills/tarot/SKILL.md`) for all rules, including the strict-mode manifest check, which runs before anything else.

User input: "$ARGUMENTS"

- If the input is empty, read `references/spreads.json` and present the spread menu: every spread with its name, card count and one-line description. Mark spreads whose `requires_method` file is missing under `references/books/extracted/methods/` as disabled with the note that the user's books do not cover this method. Close the menu with: the user can either pick a spread or simply write their question, and you will suggest the fitting spread.
- If the input names a spread, start that reading.
- If the input is a question, suggest the most fitting available spread for it (with one sentence of why), confirm, then start the reading.

Then run the reading exactly as the skill prescribes.
