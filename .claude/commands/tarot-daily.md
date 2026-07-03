---
description: Daily one-card draw, no menu
---

Follow the tarot skill (`.claude/skills/tarot/SKILL.md`) for all rules, including the strict-mode manifest check, which runs before anything else.

Skip all menus. Draw immediately with `python3 scripts/draw_cards.py --spread daily-one` (add `--deck thoth` only if the user asked for it: "$ARGUMENTS"), read the card's `lookup_file`, and deliver the day's reading as a psychological mirror per the skill's narration rules.
