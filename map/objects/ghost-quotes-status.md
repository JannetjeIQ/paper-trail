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

## What a reader will conclude if they trust it

A conversion rate of about **0.2%**.

The number is not obviously broken: a low win rate is a plausible business fact,
alarming enough to be escalated, specific enough to be believed, from a fully-populated
column in a table that is otherwise trustworthy. Nothing about the query looks wrong.
Nothing warns.

This is the shape of every ghost: **it answers.**

## The size of the error

Computed properly, from [quote_orders](quote-orders.md) and inside its coverage window,
the figure is **roughly three in four**.

Not 0.2%. Around a 400-fold error, from a column that returns a clean value with no
warning of any kind.

The band is stated rather than a number, on purpose. It held between about 75% and 80%
across six independent cuts: three quote windows crossed with two settling lags of 90
and 180 days. Windows that stable are worth reporting as a band and worth nothing as a
decimal.

**How to redo it, because you should not trust this line either.** Count quotes dated
inside the coverage window, allow at least 90 days for them to settle, and count how
many have a row in `quote_orders`. Two caveats travel with the answer: it is a count of
quotes, not a value, and it will read high if quotes are sometimes raised as paperwork
for work already agreed.

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
- [quote_orders](quote-orders.md) is not a dependant, but it is the object that
  **disproves** this one and replaces it. If you open one other card, open that.

## Does not hit

- **Conversion.** The one thing its name promises. The real answer is
  [quote_orders](quote-orders.md), which exists precisely because this column does not
  work, and which has a hard coverage bound you must read first.
