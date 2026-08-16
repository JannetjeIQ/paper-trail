# Naming collisions

Where one word means two things.

This file is **territory-specific**. Rewrite it for every territory you map. The
section below is filled for the worked example, and is there to show the shape and the
level of specificity required.

---

## Why this file exists separately

A collision is not a card, because it is not a noun. It is a property of the language
of the territory. It belongs in one place where a reader can check a word before they
trust it.

Collisions are also where `Does not hit` lines come from. If you have not found the
collisions, your wrong-neighbour lines will be invented, and an invented wrong
neighbour teaches a boundary that is not real.

## How to find them

Four sweeps over the inventory, in order of yield:

1. **Same column name, two tables.** Highest yield in any record territory. Almost
   always the two mean different things, or one of them is dead.
2. **Same word, different layer.** A word that names a record, a folder and a document.
   The reader will not know which one you mean, and neither will they know which one
   the person who wrote the source meant.
3. **Plain English versus local meaning.** A word from ordinary speech that has been
   narrowed or inverted here. These are the most dangerous, because the reader has no
   reason to look them up.
4. **The same object under two names.** The reverse case. Less dangerous, still costly:
   the reader concludes there are two things and goes looking for the second.

## How to write one

| Field | Requirement |
|---|---|
| The word | Exactly as it appears |
| Meaning A / Meaning B | Where each lives, what each means |
| Which one a stranger assumes | Name it. This is the point of the row |
| Cost of taking the wrong one | The specific wrong output, not "confusion" |

If you cannot state the cost concretely, it is not a collision, it is a synonym.

---

# Filled: the worked territory

The records and files behind quoting, approving and invoicing a job at a signage and
fit-out company. Source paths are given as they appear in the private workspace; a
reader of this repo cannot open them, and that is fine, because the point is that the
card cites rather than copies.

---

### `total`

| | |
|---|---|
| **A** | `orders.total` is **net, excluding VAT**. `orders.vat` sits on top. Gross is the sum of the two. |
| **B** | `quotes.total` is ex-VAT on strong evidence but formally unproven: the quote dataset carries no VAT column to check against. |
| **C** | In the system's own invoicing screens, the word **"gross" means pre-discount**, not VAT-inclusive. |
| **Stranger assumes** | That a figure labelled `total` includes VAT, as it would on an invoice, and that "gross" means with-VAT. |
| **Cost** | Every reported figure moves by 23%. Worse, comparing a quote value against an order value across the unresolved basis manufactures a 23% shortfall that is not real. |

Note the history, because it is instructive: this was formally contested inside the
territory for months, settled by population evidence, and **the schema document still
carries the old wrong claim on one line**. The card must therefore point at the
guardrail that settled it, not at the schema doc that describes it.

### `status`

| | |
|---|---|
| **A** | `orders.status` is maintained and load-bearing. Cancelled orders are excluded from all analysis on the strength of it. |
| **B** | `quotes.status` is **dead**. Across about 24,000 quotes and sixteen years it records 44 as successful. |
| **Stranger assumes** | That a column of the same name in a sibling table is maintained to the same standard. |
| **Cost** | A win rate. It will be roughly 0.2%, it will look alarming, and it is an artefact of an unused field. |

### `rep`

| | |
|---|---|
| **A** | `rep_code` is the person who **worked the order**. Per-order, historically accurate. This is the reporting lens. |
| **B** | `owner_code` is the person who **owns the client**. A current snapshot, overwritten when ownership changes, so it is wrong for any historical question. |
| **Also** | Two codes appearing in `rep_code` are operations administrators, not sales representatives. |
| **Stranger assumes** | That "owner" is the more authoritative of the two, because it sounds senior. |
| **Cost** | Sales performance attributed to whoever owns the account today, including for orders worked years ago by someone else, plus two non-salespeople appearing in the rankings. |

### `quote`

| | |
|---|---|
| **A** | A row in the `quotes` table. About 24,000 of them, back to 2010. |
| **B** | A folder in `quoting/<end-client-slug>/`. A few dozen, only for jobs currently in flight. |
| **C** | The client-facing document inside that folder. |
| **Stranger assumes** | These are the same population at three levels of detail. |
| **Cost** | "How many open quotes do we have" returns either about forty or several thousand depending on which noun was reached, and neither answer is wrong. |

### `order`

| | |
|---|---|
| **A** | A row in `orders`. Every won job for sixteen years. |
| **B** | A folder in `orders/<slug>/`. A handful, only for jobs needing working files. |
| **Stranger assumes** | That the absence of a folder means the job does not exist. |
| **Cost** | A delivery list built from folders, missing almost everything. |

### `invoice`

| | |
|---|---|
| **A** | A row in `invoices`. **Coverage starts April 2024.** Nothing earlier exists. |
| **B** | An invoice in the accounting package, which is the actual financial record. |
| **C** | An invoice raised in the **previous** accounting system, pre-2024, referenced in order statuses and present nowhere in the data. |
| **Stranger assumes** | The invoice table is complete. |
| **Cost** | Any pre-2024 revenue question silently returns zero rows and reads as "we invoiced nothing". |

### `accounts_code`

| | |
|---|---|
| **Looks like** | A customer key. It is short, uppercase, and sits on the customer record. |
| **Is** | A free-text accounts shorthand, blank on about 78% of customers, explicitly not a join key. Records join on **name**. |
| **Stranger assumes** | The obvious key is the key. Every schema they have ever seen worked that way. |
| **Cost** | Joins silently drop about four fifths of customers. The query runs. The answer is confidently partial. |

### `last_email_date`

| | |
|---|---|
| **Looks like** | When the quote was sent to the client. Populated on about a quarter of rows. |
| **Is** | When a quote was emailed **from within the system**. Quotes sent by ordinary email and keyed in afterwards are blank. |
| **Stranger assumes** | Blank means never issued. |
| **Cost** | A finding that three quarters of all quotes were never sent to anyone. It is false, it is dramatic, and it is the exact shape of thing that gets escalated before it gets checked. |
