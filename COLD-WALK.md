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

## What the walks changed

| Walk | Outcome | Change to the map |
|---|---|---|
| 1 | Failed, three hops | New card and catalog row for `quote_chase.py` |
| 2 | Failed, no route | Catalog now names the colliding words and grants them a free lookup |
| 3 | Passed | None |
| 4 | Passed | None |

Two of four failed on the first pass. Both failures were the same failure in different
clothes: **the map was indexed by the territory rather than by the reader's question.**
That is the defect this form is most prone to, it is invisible from the inside, and it
is why step 8 is not optional.
