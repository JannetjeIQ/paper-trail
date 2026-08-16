# quotes.status

**Type:** record field
**State:** **ghost**, empty field
**Lives at:** column `status` on [quotes](quotes.md)
**Source of truth:** the column's own value distribution, and the July 2026 ruling that followed it

## What it is

A status column on every one of about 24,000 quotes. It is 100% populated. It returns
a clean set of sensible-looking values. **Nobody has maintained it since the field
existed.**

## The number that settles it

Across about 24,000 quotes and sixteen years, the values are dominated by
`With Client` and `Quote`, with a scatter of `Created`, `Not Taken Up`, `Expected` and
`Waiting for Outsourced Prices`.

**`Successful`: 44.**

Forty-four wins in sixteen years is not a win rate. It is an unused field.

## What a reader will conclude if they trust it

They will report a conversion rate of about **0.2%**.

That is the damage, and it is worth being precise about why it is so dangerous. The
number is not obviously broken. A low win rate is a plausible business fact. It is
alarming enough to be escalated, specific enough to be believed, and it comes from a
column that is fully populated with tidy values in a table that is otherwise
trustworthy. Nothing about the query looks wrong. Nothing warns.

This is the shape of every ghost: **it answers.**

## The ruling

Made in July 2026 and standing: **the job system holds what was quoted, the
project board holds what happened to it.** Never report a win rate, a conversion
percentage or a pipeline forecast from this column.

## Hits

- Nothing. No script reads it. No process writes it. That is what makes it a ghost
  rather than a leftover.

## Does not hit

- **Conversion.** The one thing its name promises. The real answer is
  [quote_orders](quote-orders.md), which exists precisely because this column does not
  work, and which has a hard coverage bound you must read before using it.
