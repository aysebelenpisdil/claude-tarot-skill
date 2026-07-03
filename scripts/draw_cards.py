import argparse
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    spreads = json.loads((ROOT / "references" / "spreads.json").read_text())
    cards = json.loads((ROOT / "references" / "cards.json").read_text())
    parser = argparse.ArgumentParser()
    parser.add_argument("--spread", required=True, choices=[s["id"] for s in spreads])
    parser.add_argument("--deck", default="rws", choices=["rws", "thoth"])
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()
    spread = next(s for s in spreads if s["id"] == args.spread)
    rng = random.Random(args.seed) if args.seed is not None else random.SystemRandom()
    deck = list(cards)
    rng.shuffle(deck)
    cut = rng.randrange(len(deck))
    deck = deck[cut:] + deck[:cut]
    drawn = []
    for i, pos in enumerate(spread["positions"]):
        card = deck[i]
        entry = {
            "position": i + 1,
            "position_name": pos["name"],
            "position_meaning": pos["meaning"],
            "card": card["name"],
            "element": card["element"],
            "orientation": "reversed" if rng.random() < 0.5 else "upright",
            "lookup_file": f"references/books/extracted/{card['id']:02d}_{card['slug']}.md",
        }
        if args.deck == "thoth" and "thoth_name" in card:
            entry["thoth_name"] = card["thoth_name"]
        drawn.append(entry)
    print(json.dumps({"spread": spread["id"], "deck": args.deck, "cards": drawn}, indent=2))


main()
