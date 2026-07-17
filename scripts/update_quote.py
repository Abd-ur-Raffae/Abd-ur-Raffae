#!/usr/bin/env python3
"""
Daily-quote updater for the GitHub profile README.

Picks a quote from quotes.json based on the day-of-year (so it changes
every day and is stable within a day), then replaces whatever sits between
the <!-- QUOTE:START --> and <!-- QUOTE:END --> markers in README.md.

Run locally:   python scripts/update_quote.py
Run in CI:     invoked by .github/workflows/daily-quote.yml
"""

import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
QUOTES = ROOT / "quotes.json"

START = "<!-- QUOTE:START -->"
END = "<!-- QUOTE:END -->"


def pick_quote(quotes):
    """Deterministic per-day selection so re-runs on the same day are stable."""
    day_of_year = datetime.date.today().timetuple().tm_yday
    return quotes[day_of_year % len(quotes)]


def build_block(entry):
    quote = entry["quote"].strip().rstrip(".")
    author = entry["author"].strip()
    return (
        f"{START}\n"
        f"> ### *\"{quote}.\"*\n"
        f"> **— {author}**\n"
        f"{END}"
    )


def main():
    quotes = json.loads(QUOTES.read_text(encoding="utf-8"))
    if not quotes:
        print("No quotes found in quotes.json", file=sys.stderr)
        return 1

    entry = pick_quote(quotes)
    new_block = build_block(entry)

    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        re.DOTALL,
    )
    if not pattern.search(readme):
        print("Quote markers not found in README.md", file=sys.stderr)
        return 1

    updated = pattern.sub(new_block, readme)

    if updated == readme:
        print("Quote unchanged — nothing to commit.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"Updated quote to: \"{entry['quote']}\" — {entry['author']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
