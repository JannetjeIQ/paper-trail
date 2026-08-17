# Worked example

One territory, walked end to end, with the reasoning shown.

The finished map is in `map/`. This file is not that map. It is the **decisions** that
produced it: what was cut, what was reclassified, and where the judgement was hard.
Read this to learn the method. Read `map/CATALOG.md` to use the result.

---

## The territory

The records and files behind how a job gets quoted, approved and invoiced at an Irish
signage and fit-out company. Sixteen years of job records, the pricing engine
that decides what a job costs, and two folder conventions holding the paperwork.

**Later reader:** a model with no memory, holding one question. Occasionally a new
account manager inheriting a book of work.

**Why this territory qualifies.** In force, someone will change it, and it has wiring.
It is also not a failure and not a methodology, which rules out most of what is
tempting to map in a workspace you know well.

---

## Step 0. Taking the edge

The first offered edge was "how we quote and invoice", which is a process, not a
territory. Processes have no catalog because they have no nouns, only sequence, and
mapping one produces a tour.

The edge that worked: **the records and files a new hand has to understand before they
touch quoting.** That has an inside and an outside. The accounting package is outside.
Design production is outside. Anything about people is outside.

That single decision is what makes everything downstream possible.

---

## Step 2. The inventory, and what got cut

Thirty-one candidate nouns. Eighteen survived. The cuts are more instructive than the
survivors.

| Cut | Why |
|---|---|
| Roughly forty individual client quote folders | **Instances.** The convention they follow is the noun. They are not |
| `order_lines`, `purchase_orders` | Live, real, and **nothing arrives at them directly**. Every question routes through `orders` first. Recorded in the catalog as a deliberate omission, with the condition that would make them necessary |
| The data dictionary | The hardest cut. See below |
| Several rate sections inside the config | Contents of a noun, not nouns |
| The reporting API | Collapsed into the build script. Nobody reaches for the API without going through the loader |

### The hard cut: the data dictionary

It is the single most useful file in the territory. Every model that has ever queried
these records read it first. The instinct to card it was strong.

It failed the noun test. **Nothing depends on it by name.** No script opens it. It has
readers, not dependants, and a card for it would have been a card about orientation
rather than about wiring.

It also would not fit the closed set in `reference/card-types.md`, and the temptation
at that moment was to add a seventh type for documentation. That temptation is exactly
what the closed set exists to defeat. A type invented to accommodate one awkward noun
makes the next hundred maps worse.

**What was done instead**, and this is the better answer anyway: the dictionary appears
on the `jobs.sqlite` card as **the thing that is not the source of truth**.

> Source of truth: the build script. **Not the data dictionary.**

The dictionary has drifted twice: it states the wrong VAT basis on one column, and it
says the store is built from five reports when it is built from seven. Both were found
by reading the loader. That drift is far more useful to a later reader as a warning on
the store's card than it would have been as a card of its own.

---

## Step 3. The state split, and the gate

Eighteen nouns: fourteen live, one leftover, three ghosts.

The gate exists because this is the column that cannot be established from outside.
Two examples of it earning its place:

**One thing looked dead and is live.** The retired staging folder for pipeline output.
Quote output moved out of it in July 2026, which reads as retirement. But the pipeline
**code** still lives there, and so do two central logs the calibration loop reads as
one series. Marked **leftover**, not ghost, with an explicit line saying that deleting
the folder takes the pipeline and the calibration history with it.

**One thing looked alive and is a ghost.** A markup-percentage band on every customer
record. Populated, plausible, and the most pricing-looking field in the entire
territory. It is defunct and has been for years. Nothing in the data says so. The only
thing standing between a reader and a wrong price is somebody having written it down.

Neither of those could have been settled by reading files. Both came from the gate.

---

## Step 6. The catalog

Full version in `map/CATALOG.md`. The shape that matters:

| Card | Type | What it is | **Open this when you are asking** |
|---|---|---|---|
| `quote_orders` | record | The system's own quote-to-order mapping | "Did this quote convert?" |
| `rates.json` | config | Single source of truth for what things cost | "Where does a price come from?" |
| `quotes.status` | **ghost** | A status column nobody maintains | *(listed under ghosts, with what a reader will wrongly conclude)* |

**The fourth column is the whole design.** A cold reader does not scan for the noun
they need, because they do not yet know its name. They scan for the question they are
holding. A catalog whose rows are titled by noun and described by definition is an
index, and a reader has to already know the territory to use it, which is the one thing
they do not have.

Both cold-walk failures in `COLD-WALK.md` were failures of that column.

---

## A card, and what makes it a card rather than a schema entry

From `map/objects/orders.md`, the trap that matters most:

> **`total` is NET, excluding VAT.** [...] This was contested inside the business for
> months and settled by two independent checks: across every order in the store the ratio of vat
> to total is exactly 0.23 [...]; and a live test order priced at 100 read back as a
> total of 100 with VAT of 23. **The data dictionary still carries the old, wrong claim
> on one line.**

Three things are happening there and none of them are in the schema.

It states the **basis**, which is what the reader needs. It states the **evidence**,
because this was genuinely contested and a reader who finds the contrary claim
elsewhere needs to know which one to believe and why. And it names **where the wrong
claim still lives**, so that finding it does not reopen a settled question.

A schema entry would say `total REAL`. That is true and it is worth nothing.

Note also what the card does **not** contain: no revenue figures, no client names, no
reproduction of the table definition. It points. The test in `rules.md` section 6 is
whether the source could be rebuilt from the card. It could not. Correct.

---

## A second card, teaching the opposite rule

`rates.json` is the config file every price in the business comes from. Roughly thirty
sections: product rates, crew rates, studio rates, travel bands, rounding, minimum
margins. Its card contains **not one figure from it**, and says so:

> This card does not reproduce a single figure from it, deliberately. Rates change, cards
> do not, and a card carrying a stale price is worse than no card at all. Open the file.
> That is what citing means.

Set the two cards side by side and they teach opposite halves of the same rule.

`orders` shows **when a fact belongs in a card**: the VAT basis was contested for months,
so the card carries the basis, the evidence, and where the wrong claim still lives.
Without that, a reader who stumbles on the contradiction reopens a settled argument.

`rates.json` shows **when a fact must stay out**: the numbers are the most useful thing
in the file and are exactly what must not be copied, because they move.

What its card carries instead is the shape of the traps. Travel is charged per attendance
day, not once per job. A half day is not pro rata. Wastage is applied to net area and
never shown to the client. Each gets "corrected" by well-meaning readers who assume the
file is wrong, so the card's job is to say **read the note before changing the value**.

Test from `rules.md` section 6: could you rebuild the rate file from its card? No.
Correct.

---

## The ghost, in full

`quotes.status`. A status column on about 24,000 quotes, 100% populated, tidy values,
sitting on an otherwise trustworthy table.

Across sixteen years it records **44 quotes as successful**.

The card's job is not to say the column is broken. It is to say **what a reader will
conclude if they trust it**: a win rate of about 0.2%.

That is the damage, and the reason ghosts are the highest-value cards in any map. The
number is not obviously wrong. A low win rate is a plausible business fact. It is
alarming enough to be escalated, specific enough to be believed, and it comes from a
fully-populated column in a table nothing else is wrong with. The query looks correct.
Nothing warns.

**A ghost answers.** That is what separates it from a leftover, and it is why it gets a
card of its own rather than a line in a caveats list.

---

## One change, and what it hits

**The change:** raise an install crew rate.

**Catalog → "Where does a price come from?" → `rates.json`. One card. Stop.**

**Hits:**

- `engine.js` reads the file at run time. The next quote priced uses the new number.
- `validate.js` **will fail**. The golden tests reconstruct real historical quotes from
  current rates, so a rate change breaks the cases that reproduce quotes priced at the
  old one. The card says this is correct behaviour and says what to do: update the case
  and record why. Do not loosen the tolerance.
- Any downstream consumer declared as a reader of the file.

**Does not hit:**

- **Historical quotes and orders.** Nothing recalculates, ever. Reporting will not move.
  A reader who expects it to move will conclude the change did not take, and will change
  it again.
- **The customer pricing band.** The most pricing-looking field in the system, and a
  ghost. It has never fed this file.

That second bullet under `Does not hit` is the line that distinguishes a map from a
glossary. It is not information about the thing you opened. It is information about the
thing you were about to open next, and be wrong about.

---

## A second change, compressed

**The change:** raise the row cap on the quote-to-order report so conversion can be
measured further back.

**Hits:** the report definition in the live system; the loader that reads it; the
coverage floor in the chase digest, which is derived from this bound and must move with
it; and the reporting server itself, which **crashes** on the uncapped version, which is
why the cap exists at all.

**Does not hit:** `quotes.status`. Still a ghost, still not conversion, still the first
place someone will look.

Both changes land on one card. Neither reader needed to read the territory. That is the
bar.
