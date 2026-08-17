# Cold walk

Step 8 of `reference/walk-order.md`, performed on the map in `map/`.

Four questions a later reader actually arrives with, answered using **only** the
catalog and one card. Recorded as they went, including the two that failed and what
changed as a result.

**Read `LIMITS.md` first.** These walks were run by the cartographer against its own
map, which is the weakest form of this test. What it can prove and what it cannot is
set out there.

---

## Walk 1: FAILED, map changed

**Question:** "Which quotes are still open and need chasing?"

**What happened.** Opened the catalog. Scanned the right-hand column. Nothing matched.
The nearest row was `quotes`, whose question is "What did we quote, to whom, when?",
which is not the question. Opened `quotes` anyway, because that is what a reader under
time pressure does. The card is about the record, not about openness. It mentions a
chase script in one `Hits` line and moves on.

**Two hops did not land.** A third hop was needed, into a card that did not exist.

**Diagnosis.** `quote_chase.py` was referenced by three cards and carded by none. It
had been treated as plumbing behind `quote_orders` rather than as a noun. It fails the
noun test in `rules.md` section 2 only if you read the test carelessly: things do
depend on it by name, and more to the point a reader arrives at it directly, holding a
question no other card answers.

**Fix.** Added `map/objects/quote-chase.md` and a catalog row whose question column
reads "Which quotes are still open and need chasing?". Re-walked: catalog, one card,
stop.

**The general lesson**, which is now the reason step 8 exists at all: a map built by
walking a territory is organised around **what is there**. A reader arrives organised
around **what they want**. Those two orderings are not the same, and only the cold walk
exposes the gap.

---

## Walk 2: FAILED, map changed

**Question:** "Is this revenue figure inc or ex VAT?"

**What happened.** VAT is not a noun and has no catalog row, correctly. But the reader
holding this question has no route at all: they would have to already know that the
answer lives in the Traps section of `orders`, and if they knew that they would not be
asking.

**Diagnosis.** Cross-cutting traps have no door. `reference/naming-collisions.md` held
the answer the whole time and the catalog mentioned it only in a passing clause about
similar names.

**Fix.** Rewrote that part of the catalog to name the colliding words explicitly
(`total`, `status`, `rep`, `quote`, `order`, `invoice`) and to state that the
collisions file does not count against the two-hop budget. It is a dictionary, not a
card, and a reader should be able to check a word without spending a hop.

**The general lesson.** A two-hop budget spent on a **word** rather than a **thing** is
a waste of the reader's only currency. Words get a free lookup.

---

## Walk 3: passed

**Question:** "We are raising an install rate. What breaks?"

Catalog, right-hand column, "Where does a price come from?" → `rates.json`. One card.

The card gave the change surface without any figures in it: the engine reads the file
at run time, and the golden tests reconstruct real historical quotes from these rates,
so **they will fail, and failing is correct**. The card says what to do about that
(update the case and record why, do not loosen the tolerance), which is the actual
thing the reader needed and the thing they would most plausibly get wrong.

`Does not hit` earned its place twice. Nothing recalculates historically, so reporting
will not move and the reader must not read that stillness as the change not taking.
And the pricing-looking field on the customer record is a ghost that has never fed this
file.

**Stopped after one card.** Correct outcome.

---

## Walk 4: passed, and this is the one that matters

**Question:** "What is our quote win rate?"

This is the trap question in this territory. A reader arriving with it will find a
fully-populated `status` column on a trustworthy table and get an answer of about 0.2%,
which is plausible, alarming, and false.

Catalog, right-hand column, "Did this quote convert?" → `quote_orders`. One card.

The card gave the authoritative source, and its `Does not hit` line named the wrong
neighbour by name: the instinct on being told conversion is unreliable is to reach for
the status column, and that column is a ghost. From there the reader can take a free
lookup at the ghost card if they want the number that would have been wrong.

It also gave the hard bound, which is the part a glossary would have omitted: coverage
starts around mid-2025. Outside that window the table does not say "unconverted", it
says nothing, and the two are easy to confuse.

**The reader gets a correct, bounded answer without ever touching the ghost.** That is
the whole product.

---

## Walk 5: a genuinely cold agent. PASSED, and found three defects

Walks 1 to 4 were self-administered, which `LIMITS.md` admits is the weakest form of this
test. Walk 5 was not. A separate model with **no memory of this territory, this repo, or
the conversation that built it** got one path, `map/CATALOG.md`, one question, and an
instruction not to read the method files.

**Question:** *"I want to report our quote win rate to my board next week. What number do I
use, and where does it come from?"*

The trap question. The naive answer sits in a fully-populated column.

### What it did

Three files, in order: the catalog, `quote_orders`, `ghost-quotes-status`. Two cards.
Inside budget.

**It reached the correct answer**, that no defensible number exists in this territory, and
it got there by being stopped twice. Its own words:

> After reading `quote_orders.md`, its own "Does not hit" section stopped me from reaching
> for `quotes.status` next.

> Having already discounted 0.2% and landed on the "sounds right" 76% figure, it stopped me
> a second time. That second catch is the one that actually mattered. Without it I'd have
> reported 76% to the board with confidence.

That is the product working. A cold reader defeats the obvious trap, walks into the subtle
one, and the map catches it.

### The defects it found

Reported blunt, on request. Three held. One did not.

**1. No routing row for the actual question. CONFIRMED, fixed.** Nothing in the catalog
said "win rate". The nearest row was per-quote, "Did this quote convert?", so the reader
had to guess that *conversion* meant *win rate*. The boundary section now has routing rows
using the words a reader would actually bring.

**2. The map says leave without naming where to go. CONFIRMED, fixed.** Two cards told the
reader outcome lives on "the project board" and no card existed for it. Its words: *"a
business owner with a board meeting next week gets told what not to trust and nothing about
where to look instead."* That breaks this map's own rule in `reference/card-types.md`, that
a boundary card marks the wall **and names the door**. Added
[the project board](map/objects/the-project-board.md).

**3. The two-hop rule is stated obliquely. CONFIRMED, fixed.** It appeared only in a
subordinate clause about a file exempt from it, so the agent had to infer both that the rule
existed and what its number was. Now the first line of the catalog.

**4. "A reader landing on `quotes.md` gets none of the warnings." OVERSTATED, rejected as
written.** That card already warned off `status` explicitly. But checking it surfaced a real
weaker version: the warning covered the dead field and not the population problem, so that
path was saved from the first trap and not the third. `quotes.md` now carries both.

**An agent's finding is evidence, not a verdict.** Acting on the fourth as written would
have added a warning that was already there and missed the actual gap beside it.

---

## What the walks changed

| Walk | Outcome | Change to the map |
|---|---|---|
| 1 | Failed, three hops | New card and catalog row for `quote_chase.py` |
| 2 | Failed, no route | Catalog names the colliding words, grants them a free lookup |
| 3 | Passed | None |
| 4 | Passed | None |
| 5 | **Passed, cold agent** | Boundary routing rows, the project board card, two-hop rule stated outright, population trap added to `quotes` |

Three of the five walks changed the map. Walks 1 and 2 failed outright. Walk 5 passed and
still produced four findings, three of which held.

The pattern across all of them is one defect wearing different clothes: **the map was
indexed by the territory rather than by the reader's question.** Every fix moved it toward
the reader. That defect is invisible from the inside, which is why the walk is step 8 and
why walk 5, run by something that had never seen the territory, was worth more than the
four before it put together.
