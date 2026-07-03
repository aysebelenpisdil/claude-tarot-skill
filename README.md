# claude-tarot-skill

Book-faithful tarot readings inside [Claude Code](https://claude.com/claude-code).
Bring your own tarot books as PDFs; every card interpretation is synthesized
exclusively from *your* books — never from the model's general tarot knowledge.

## How it works

- You place your tarot book PDFs (any number) in `references/books/`.
- `/tarot-setup` digests them into one file per card under
  `references/books/extracted/`, each section carrying page references, plus
  method files (elements, reversals, spread methods) when your books cover them.
- Card draws are done by a script using `random.SystemRandom` — randomness is
  never left to the model.
- Before interpreting any card, the skill must read that card's extracted
  file. If your books answer, web search is forbidden; only where your books
  are completely silent may outside information appear, and it is always
  explicitly marked as coming from outside your source books.

**Strict mode:** until extraction is complete (all 78 cards plus method
checks), the skill refuses to read at all and points you to `/tarot-setup`.
No books, no readings.

Your PDFs and everything generated from them are gitignored and never leave
your machine. Do not share the `extracted/` content — it is derived from
copyrighted books and is for your personal use only.

## Installation

```
git clone https://github.com/<you>/claude-tarot-skill.git
cd claude-tarot-skill
cp /path/to/your-tarot-books/*.pdf references/books/
claude
```

Then run `/tarot-setup` once and follow along. Extraction is resumable — if
the session is interrupted, run it again and it continues where it stopped.

## Commands

| Command | What it does |
|---|---|
| `/tarot` | Spread menu, or write your question and get a spread suggestion |
| `/tarot-daily` | Immediate one-card daily draw, no menu |
| `/tarot-info [spread]` | Spread catalog, or the full position map of one spread |
| `/tarot-setup` | Build or resume the extraction knowledge base |

## Spreads

Seven spreads, from a one-card daily to the Celtic Cross — see
[SPREADS.md](SPREADS.md). The `horoscope` (12 astrological houses) and
`tree-of-life` (10 Sephiroth) spreads are enabled only if your books cover
those methods; otherwise they appear disabled in the menu.

## Decks

`--deck rws` (default) or `--deck thoth`. Same 78-card structure; the Thoth
deck uses its own card names (Lust, Adjustment, Art, Disks, the
Princess–Prince court). Meanings still come from your books.

## Disclaimer

For entertainment and self-reflection only. Readings make no claims about
future events and never substitute for medical, legal, or financial advice.

## License

[MIT](LICENSE) — covers the skill's code and instructions. Your books and
anything extracted from them are yours and stay out of the repo.
