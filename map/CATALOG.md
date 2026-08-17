# Catalog: quoting, approving and invoicing a job

**Territory.** The records and files that carry a job from "a client asked what it
would cost" to "we invoiced it", at an Irish signage and fit-out company.

**Later reader.** A model with no memory of this territory, holding one question,
about to either answer it or change something. Sometimes a new account manager
inheriting a book of work.

**Edge.** Sixteen years of job records in one system, the pricing engine that
sets what a job costs, and the two folder conventions that hold the paperwork. Out of
scope: design production, installation scheduling, the accounting package (marked as a
boundary), and anything about people or performance.

**Walked.** August 2026. Row counts are scale, not truth: they were right at the last
rebuild and are not maintained here.

---

## How to use this page

**The rule: two hops. This page, then one card. Then stop.**

Find your question in the right-hand column and open that one card. If it answers you,
you are finished, even if a neighbouring card looks interesting. If you have opened
three cards, the map has failed and should be fixed rather than worked around.

One exception, and it is free: `../reference/naming-collisions.md` is a dictionary, not
a card. Looking a word up there costs you no hops.

Do not open the `objects/` folder as a whole. There are nineteen cards. Reading them all
would take longer than reading the source, which defeats the point of this page existing.

If your noun is not in this table, it is not in this territory. Say so. Do not reach
for the nearest similar name.

**Before you trust any of these words, check them.** Seven names in this territory mean
two things, including `total`, `status`, `rep`, `quote`, `order` and `invoice`. They
are listed with their costs in `../reference/naming-collisions.md`. That file is not a
card and does not count against your two hops. Read it when a word feels obvious.

---

## Live objects

| Card | Type | What it is | Open this when you are asking |
|---|---|---|---|
| [jobs.sqlite](objects/jobs-sqlite.md) | store | The queryable copy of the whole system, rebuilt nightly | "Where do I actually run a query, and how fresh is it?" |
| [quotes](objects/quotes.md) | record | Every quote raised since 2010, about 24,000 | "What did we quote, to whom, when?" |
| [quote_orders](objects/quote-orders.md) | record | The system's own quote-to-order mapping | "Did this quote convert?" |
| [orders](objects/orders.md) | record | Every won job, tens of thousands | "What did we sell, who worked it, what was it worth?" |
| [invoices](objects/invoices.md) | record | Invoice records, a fixed 2024 start date onward only | "Was this job invoiced, and paid?" |
| [customers](objects/customers.md) | record | The client master list, a few thousand | "Who is this client and how do I join to them?" |
| [rates.json](objects/rates-json.md) | config | Single source of truth for what things cost | "Where does a price come from?" |
| [engine.js](objects/engine-js.md) | process | Turns a scope into priced lines | "Why did the quote come out at that number?" |
| [quoting/&lt;end-client-slug&gt;/](objects/quoting-folder.md) | convention | One folder per opportunity, pre-acceptance | "Where does the paperwork for a live quote live?" |
| [orders/&lt;slug&gt;/](objects/orders-folder.md) | convention | One folder per won job needing working files | "Where does the paperwork for a won job live?" |
| [build_db.py](objects/build-db.md) | process | Nightly rebuild of the store from seven reports | "Why is this column missing, or this row dropped?" |
| [quote_chase.py](objects/quote-chase.md) | process | Aged digest of quotes with no order against them | "Which quotes are still open and need chasing?" |
| [invoicing_check.py](objects/invoicing-check.md) | process | Weekly digest of complete-but-not-fully-invoiced jobs | "How do we catch a job we forgot to finish invoicing?" |

## Boundary

Two questions this map cannot answer. These cards name the wall and the door.

| Card | Type | What it is | Open this when you are asking |
|---|---|---|---|
| [the project board](objects/the-project-board.md) | boundary | Where quote outcome is actually tracked | **"What is our win rate / conversion rate?"** or "did we win this one?" |
| [the accounting package](objects/accounting-boundary.md) | boundary | Where the money record actually lives | "Which system wins on a financial figure?" or "who owes us?" |

## Leftover

| Card | State | What it is | Why it is still here |
|---|---|---|---|
| [email-to-quote/quotes/](objects/leftover-email-to-quote-staging.md) | leftover | The retired staging path for pipeline output | Superseded, still resolves, still holds old jobs |

## Ghosts

Read these before trusting anything that carries their name. Each one returns a value.
None of the values mean what they appear to mean.

| Card | Ghost shape | What a reader will wrongly conclude |
|---|---|---|
| [quotes.status](objects/ghost-quotes-status.md) | empty field | That our quote win rate is about 0.2% |
| [orders_ext](objects/ghost-orders-ext.md) | removed target | That a query written last year still runs |
| [the customer pricing band](objects/ghost-pricing-band.md) | empty field | That each client has a governing markup percentage |

---

## The shape in one picture

```
                        rates.json ──reads── engine.js
                                                │
                                                ▼
  quoting/<end-client-slug>/ ─────────── the priced quote document
            │                                   │
            │ graduates to                      │ keyed into
            ▼                                   ▼
     orders/<slug>/                          quotes ──┐
                                                      │ quote_orders
                                                      ▼
                                                   orders
                                                      │
                                        ┌─────────────┼──────────────┐
                                        ▼             ▼              ▼
                                   order_lines    invoices   purchase_orders
                                                      │
                                                      ▼
                                          the accounting package (boundary)

  All of the above lands in jobs.sqlite nightly, via build_db.py.
```

The two columns of that picture are the thing a stranger most needs to see. The left
column is **folders**, made by people, holding a few dozen live jobs. The right column
is **records**, made by the system, holding sixteen years. They carry the same words
and they are not the same population. That is the first trap in this territory and it
is the reason `quote` and `order` each have two cards' worth of meaning.

---

## What is not mapped, and why

- `order_lines` and `purchase_orders` exist and are live. They are not carded because
  no question in the reader's actual arrival set reaches them without going through
  `orders` first. If your work is supplier costs, they need cards. Say so and add them.
- The pricing engine's calibration and feedback loop is real and is out of scope here.
- Two further absences, a secondary contacts table and an off-system pipeline list,
  are named in the build script but do not exist in the current store. They are
  recorded on the [build_db.py](objects/build-db.md) card rather than given
  ghost cards of their own, because nothing downstream reaches for them by name.
