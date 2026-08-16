# quotes.status

**Type:** record field
**State:** **ghost**, empty field
**Lives at:** column `status` on [quotes](quotes.md)
**Source of truth:** the column's own value distribution, and the July 2026 ruling that followed it

## What it is

A status column on every one of about 24,000 quotes. 100% populated, clean
sensible-looking values, dominated by `With Client` and `Quote`. **Nothing writes to it
and nothing reads it.**

**`Successful`: 44.** Across sixteen years.

It ships with the job system. This business never wired it up, because quote outcome is
tracked elsewhere by decision. The field is not neglected, it is **unused**, and those
are different states with the same symptom.

## The contradiction that closes it

You do not have to judge whether 44 "looks low". Two objects in the same store disagree
outright:

| Object | Says |
|---|---|
| `quotes.status` | 44 quotes were ever won |
| [orders](orders.md) | **tens of thousands of won jobs** exist, each accepted and paid for |

An order **is** a won quote that became work. Both cannot be true, and orders is the
table the business invoices from.

That is the cleanest proof of a ghost available: not an argument about plausibility, but
a live object next door holding the contradiction. Note the limit. It kills the 0.2% and
does **not** replace it, because orders and quotes span different periods and not every
order began as a quote in this table.

## What a reader will conclude if they trust it

A conversion rate of about **0.2%**.

The number is not obviously broken: a low win rate is a plausible business fact,
alarming enough to be escalated, specific enough to be believed, from a fully-populated
column in a table that is otherwise trustworthy. Nothing about the query looks wrong.
Nothing warns.

This is the shape of every ghost: **it answers.**

## Where the answer actually lives

Ruled July 2026 and standing: **the job system holds what was quoted, the project board
holds what happened to it.** Two systems, one question each. That decision is why this
column is empty of meaning.

Use **[quote_orders](quote-orders.md)** inside its coverage window, the job system's own
quote-to-order mapping, bounded to roughly mid-2025 onward with a hard edge. Outside
that window, the project board.

No card here carries a conversion figure, deliberately. Ratios go stale, and a stale
number in a card a reader has chosen not to check becomes the most authoritative-looking
ghost in the territory.

## Hits

- Nothing. No script reads it, no process writes it. That is what makes it a ghost
  rather than a leftover.
- [orders](orders.md) is not a dependant, but it **disproves** this one. If you open one
  other card, open that.

## Does not hit

- **Conversion.** The one thing its name promises. The real answer is
  [quote_orders](quote-orders.md), which exists precisely because this column does not
  work, and which has a hard coverage bound you must read first.
