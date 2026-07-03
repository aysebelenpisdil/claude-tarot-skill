---
description: Extract per-card knowledge from the user's tarot book PDFs (resumable)
---

Build or resume the extraction knowledge base under `references/books/extracted/`.

## Preconditions

1. List PDF files in `references/books/`. If there are none, stop and tell the user to place their tarot book PDFs there (see `references/books/README.md`). Any number of books is supported.
2. Read `references/books/extracted/manifest.json` if it exists. If it does not, create the directories `extracted/` and `extracted/methods/` and initialize the manifest (schema below).
3. If the manifest exists but its `books` list does not match the PDFs currently present, tell the user which books are new or missing and ask whether to (a) extract the new book additively into the existing files or (b) rebuild from scratch.

## Manifest schema

`references/books/extracted/manifest.json`:

```json
{
  "books": [{"file": "example.pdf", "title": "Example Book Title"}],
  "cards": {"00_fool": "done"},
  "methods": {
    "elements": "done | not_covered",
    "reversals": "done | not_covered",
    "spreads": "done | not_covered",
    "horoscope": "done | not_covered",
    "tree_of_life": "done | not_covered"
  }
}
```

A card key is present only once its file is fully written. A method key set to `not_covered` means the books were checked and are silent on it — that is a completed state, not a pending one. Extraction is complete when all 78 card keys are `done` and all 5 method keys are present.

## Extraction rules (non-negotiable)

- Every sentence you write into an extracted file must come from the books. Never fill gaps from general tarot knowledge. If a book does not cover a card or an orientation, write `Not covered in this book.` for that section.
- Every book section must carry page references (e.g. `(pp. 88-90)`).
- Synthesize meaning in your own words; do not copy long verbatim passages.
- Write one section per book, in the order the books appear in the manifest.
- All extracted files are in English.

## Card extraction

Card identity comes from `references/cards.json`. The target file for each card is `references/books/extracted/{id:02d}_{slug}.md`. If a book uses Thoth naming, locate the card via its `thoth_name`.

Work through each book's card-meanings section sequentially (find it via the table of contents), reading page ranges with the Read tool. For each card, write:

```markdown
# {id:02d} {name}

## {Book Title} (pp. X-Y)

### Upright
{synthesis}

### Reversed
{synthesis, or "Not covered in this book."}
```

Update the manifest after every card file is written, so an interrupted run resumes exactly where it stopped: on start, skip every card already marked `done`.

## Method extraction

After the cards (or when resuming past them), check each book for these topics and write the corresponding file under `extracted/methods/` only if at least one book genuinely covers it:

- `elements.md` — elemental attributions and element interaction rules
- `reversals.md` — the book's approach to reversed cards
- `spreads.md` — spread methods and position meanings the books teach
- `horoscope.md` — the 12-house horoscope spread method
- `tree_of_life.md` — the Tree of Life / Sephiroth spread method

If the books are silent on a topic, do not create the file; record `not_covered` in the manifest. The `horoscope` and `tree-of-life` spreads stay disabled unless their method file exists.

## Completion

When the manifest is complete, report: number of cards extracted per book, which methods were covered, and which of the two conditional spreads are now enabled. Then recommend a spot-check: pick 3-5 random cards, show their page references, and ask the user to verify them against the PDFs. This validates extraction fidelity — the canary test used elsewhere only validates reading fidelity to the extracted files.
