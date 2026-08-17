# Paper Trail

**A cartographer for a body of work someone else has to change.** Point it at a repo, a
delivery folder, a vault, or a set of live business records, and it leaves behind a
**map**: a catalog and a set of noun cards a cold reader can enter, use once, and leave.

The sample map it ships with is the paper trail of a job: the records and files that
carry work from "what would that cost" to "we invoiced it".

No knowledge of the territory required. That is the whole point. The expertise lives in
the map, not in the person who drew it.

The later reader is usually **a model** with no memory, a limited window, and one
question. Sometimes it is a new developer, a contractor, or a hire inheriting a book of
work. Same map, same job.

---

## The one rule

**Load the catalog. Open one card. Stop.**

Never load the whole `objects/` folder. Never add the territory to the project.

Two clarifications, because this rule is easy to misread in opposite directions:

- **The cartographer itself loads whole.** These five files are about 30KB and they are
  the instrument. That is not a violation.
- **The map does not.** A catalog that must be read top to bottom is a tour. A card set
  that must be loaded whole is a photocopy. Neither is a map, and both defeat the
  reason for building one.

If answering a question takes three cards, the map is wrong. Fix the map. Do not work
around it.

---

## What it is not

| | |
|---|---|
| Not a **tour guide** | No plot, no walkthrough, no "how the week goes" |
| Not an **auditor** | It marks what is dead. It does not list what is wrong |
| Not a **diagnostician** | It never explains why something failed. Different form, different week |
| Not a **second spec** | Cards cite the source and lose to it. If they disagree, the file wins |

It also refuses two inputs outright: **a failure** (that is working backward from a
break, which is a different job) and **a methodology** (mapping a skill, a prompt
system, or a folder system about folder systems). Use the method. Do not map the method.

---

## Setup

1. Create a Claude project.
2. Add `identity.md`, `rules.md`, `examples.md`, and the whole `reference/` folder.
   Keep the folder structure. That is the cartographer.
3. Do **not** add `map/`. It is sample output, not instruction. Add it only if you want
   to study the shape of a finished map.
4. Optionally set project instructions to: *"Follow identity.md and rules.md. Walk in
   the order set out in reference/walk-order.md."*

Then, in a new conversation:

> You are the cartographer. Walk `<territory>`. The later reader is `<a cold model / a
> new hire / a contractor>`, and when they arrive they will be about to change
> `<something>`. Start at step 0.

**It will stop and ask you one question**, at step 3, before writing anything. It will
show you which objects it believes are live, which are leftovers, and which are ghosts.
**Answer that honestly.** State is the one thing it cannot establish from outside and
the one thing that is expensive to get wrong. A wish marked live is how the next reader
builds against a world that does not exist.

Then it writes `CATALOG.md` and one card per noun. That is the product.

---

## How a cold model walks a finished map

You have no memory of this territory. Do not try to acquire one.

1. Read `CATALOG.md`. Nothing else yet.
2. Scan the right-hand column for **the question you are holding**, not for a noun. You
   do not yet know the territory's names, and its names are not always what you expect.
3. Open **that one card**.
4. Read `Hits` to know what else you are about to move. Read `Does not hit` to know
   which neighbour you were about to be wrong about.
5. If you are about to change behaviour, open the source the card cites.
   **The source wins. The card is a pointer, not a copy.**
6. Stop. Do not open the next card for context.

If a word feels obvious, check `reference/naming-collisions.md` first. It is a
dictionary, not a card, and it does not cost you a hop. In most territories several
names mean two things.

If the catalog has no row for your noun, **say so**. Do not infer one from a
similar-sounding name.

---

## What is in this folder

| File | Job |
|---|---|
| `identity.md` | Who the cartographer is, what it can walk, what it refuses |
| `rules.md` | How it maps: nouns, movements, live/leftover/ghost, Hits, the refusals |
| `examples.md` | One real territory walked, with the reasoning and the hard cuts shown |
| `reference/card-types.md` | The closed set of six card types, and the card shape |
| `reference/walk-order.md` | Nine steps, the gates between them, and what breaks if you skip one |
| `reference/naming-collisions.md` | Where one word means two things. Rewritten per territory |
| `LIMITS.md` | Where this can be wrong. Read before trusting it |
| `check_map.py` | Enforces the structural rules. Run it before publishing a map |
| `COLD-WALK.md` | Five real walks. Two failed, and walk 5 was a genuinely cold agent |
| `map/` | The finished sample map. Output, not instruction |

---

## The sample territory

`map/` holds a real map: the records and files behind how a job gets quoted, approved
and invoiced at an Irish signage and fit-out company. Sixteen years of job records, the
pricing engine that decides what a job costs, and the two folder conventions holding the
paperwork. Nineteen cards, of which one is a leftover and three are ghosts.

The later reader there is explicitly a model: a session that has to answer a question
against those records without loading them.

**The rules are enforced, not just stated.** Run `python check_map.py`. Every card must
carry both Hits and Does not hit, every ghost must cite the search that proved its absence,
no card may be orphaned from the catalog, every link must resolve, and each card has a line
budget. It passes clean in `--strict`. It did not on the first run, and writing the ghost
searches corrected two cards that were wrong.

**The map is redacted, and deliberately so.** Real file paths are replaced by role
placeholders (`<records-kb>/`, `<scripts>/`, `<delivery>/`), the job-management system
is not named, client identities are generalised to roles, and no rate or absolute
figure appears anywhere.

What survives verbatim is everything that makes it a map rather than a schema dump:
every ghost, every naming collision, every coverage bound, the three ways an earlier
inference-matching approach failed, and the reason the pricing golden tests are
*supposed* to break. None of that depends on knowing the vendor or the path.

This is worth noticing rather than apologising for. `rules.md` section 6 already
forbids a card from carrying values, reproduced schema, or anything that would let you
rebuild the source from the card. A map that redacts cleanly is a map that was obeying
that rule. One that cannot be redacted without collapsing was a photocopy.

**Five cold walks, and the failures are published.** Two of the first four failed
outright. Walk 5 handed the catalog and one question to a separate model with no memory of
this territory: it reached the right answer in two hops, and still found four defects, of
which three held under checking and one was overstated. All of it is in `COLD-WALK.md`,
including which finding was rejected and why.

Left standing on purpose. A map never walked cold is a draft, and one walked but reporting
only its successes is a brochure.

---

Built on interpretable context methodology. Folders as architecture, each file doing
one job, and the reader never has to eat the tree.
