#!/usr/bin/env python3
"""Check a map against the rules in rules.md and reference/card-types.md.

The constraints in this repo are worth nothing if nobody enforces them. This
script enforces the ones a machine can. Run it before you publish a map.

    python check_map.py                 # checks ./map
    python check_map.py path/to/map     # checks another map
    python check_map.py --strict        # warnings become failures

Exit code 0 if every check passes, 1 otherwise.

What it CAN check (structure, and the rules that are structural):
  - the catalog exists, and every card it names resolves
  - every card carries Type, State, Lives at
  - State is one of the four permitted values
  - Type is one of the six permitted card types
  - every card has BOTH a Hits and a Does not hit section  (rules.md s5)
  - every ghost card cites the search that proved absence   (rules.md s4)
  - no card exceeds its line budget, which differs by state (card-types.md)
  - every relative link in the map resolves
  - no card is orphaned: the catalog reaches all of them
  - no em dashes (house style)

What it CANNOT check, and you must still do by hand:
  - whether a state is TRUE. Live/leftover/ghost is a judgement about use, and
    no script can see a human opening a file every Monday. This is why the walk
    has a mandatory human gate at step 3.
  - whether a Does not hit line names the RIGHT wrong neighbour.
  - whether a card copied its source. Section 6 is a judgement call.
  - whether a cold reader can actually wander. That is COLD-WALK.md's job.

Passing this script means the map is well formed. It does not mean it is true.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

STATES = {"live", "leftover", "ghost", "unverified"}
TYPES = {"record", "store", "config", "convention", "process", "boundary", "record field"}
BUDGET = {"ghost": 80, "default": 62}  # card-types.md, budget differs by state

fails: list[str] = []
warns: list[str] = []


def fail(msg: str) -> None:
    fails.append(msg)


def warn(msg: str) -> None:
    warns.append(msg)


def field(text: str, name: str) -> str | None:
    m = re.search(rf"^\*\*{name}:\*\*\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def check_card(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    rel = path.name
    n = len(text.splitlines())

    for required in ("Type", "State", "Lives at"):
        if not field(text, required):
            fail(f"{rel}: missing **{required}:**")

    raw_state = (field(text, "State") or "").lower()
    state = next((s for s in STATES if s in raw_state), None)
    if not state:
        fail(f"{rel}: State is not one of {sorted(STATES)} (got {raw_state!r})")

    raw_type = (field(text, "Type") or "").lower()
    if not any(t in raw_type for t in TYPES):
        fail(f"{rel}: Type is not one of the closed set (got {raw_type!r})")

    # rules.md s5: BOTH sections, always, even when the answer is "nothing"
    if not re.search(r"^##\s+Hits\s*$", text, re.M):
        fail(f"{rel}: no '## Hits' section (rules.md s5)")
    if not re.search(r"^##\s+Does not hit\s*$", text, re.M):
        fail(f"{rel}: no '## Does not hit' section (rules.md s5)")

    # rules.md s4: a ghost must cite the search that proved absence
    if state == "ghost" and not re.search(r"search that proved", text, re.I):
        fail(f"{rel}: ghost with no cited search (rules.md s4)")

    budget = BUDGET["ghost"] if state == "ghost" else BUDGET["default"]
    if n > budget:
        warn(f"{rel}: {n} lines, over the {budget}-line budget for a {state or '?'} card")

    if "—" in text:
        fail(f"{rel}: contains an em dash")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    strict = "--strict" in sys.argv
    root = Path(args[0]) if args else Path(__file__).parent / "map"

    if not root.is_dir():
        print(f"no map directory at {root}")
        return 1

    catalog = next((p for p in root.iterdir() if p.name.lower() == "catalog.md"), None)
    if not catalog:
        print(f"FAIL  no CATALOG.md in {root}")
        return 1

    cards = sorted((root / "objects").glob("*.md")) if (root / "objects").is_dir() else []
    if not cards:
        print(f"FAIL  no cards in {root / 'objects'}")
        return 1

    for c in cards:
        check_card(c)

    # every relative link across the whole map must resolve
    for p in [catalog, *cards]:
        for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
            t = m.group(1)
            if t.startswith(("http", "#", "<")):
                continue
            if not (p.parent / t).resolve().exists():
                fail(f"{p.name}: broken link -> {t}")

    # no orphans: the catalog must reach every card
    linked = {
        Path(m.group(1)).name
        for m in re.finditer(r"\[[^\]]+\]\(([^)]+\.md)\)", catalog.read_text(encoding="utf-8"))
    }
    for c in cards:
        if c.name not in linked:
            fail(f"{c.name}: orphan, not reachable from the catalog")

    ghosts = sum(
        1 for c in cards if "ghost" in (field(c.read_text(encoding="utf-8"), "State") or "").lower()
    )

    print(f"\ncheck_map.py  {root}")
    print(f"  {len(cards)} cards, {ghosts} ghosts, catalog links to {len(linked)}\n")
    for w in warns:
        print(f"  WARN  {w}")
    for f in fails:
        print(f"  FAIL  {f}")

    hard = fails + (warns if strict else [])
    print(f"\n{'FAILED' if hard else 'PASSED'}: {len(fails)} failures, {len(warns)} warnings\n")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
