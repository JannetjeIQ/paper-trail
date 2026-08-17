# quotes.status

**Type:** record field
**State:** **ghost**, empty field
**Lives at:** column `status` on [quotes](quotes.md)
**Source of truth:** the column's own value distribution, and the July 2026 ruling that followed it

## What it is

A status column on every one of about 24,000 quotes. 100% populated, clean
sensible-looking values dominated by `With Client` and `Quote`. **Nothing writes to it and
nothing reads it.**

**`Successful`: 44.** Across sixteen years.

It ships with the job system. This business never wired it up, because quote outcome is
tracked elsewhere by decision. The field is not neglected, it is **unused**, and those are
different states with the same symptom.

## What a reader will conclude if they trust it

A conversion rate of about **0.2%**.

The number is not obviously broken: a low win rate is a plausible business fact, alarming
enough to be escalated, specific enough to be believed, from a fully-populated column in
a table that is otherwise trustworthy. Nothing warns.

This is the shape of every ghost: **it answers.**

## The trap behind the trap

Kill the 0.2% and a second wrong answer is waiting.

Do it "properly" instead, counting quotes with a row in
[quote_orders](quote-orders.md) inside its coverage window and allowing 90 days to settle,
and you get roughly **three in four**. Stable across six cuts, too.

**That number is also wrong**, for a reason no care with the query will fix. The
denominator is not "quotes we gave", it is **"quotes somebody chose to enter"**. A quote
keyed in when the job looks serious, or after it has already landed, is in the table. A
price given over the phone and lost never was. Historic practice was looser still. The
losses are missing from the bottom of the fraction, so the fraction climbs.

Three defects, stacked, each sufficient alone:

| Defect | Effect |
|---|---|
| `status` unmaintained | Gives 0.2%. Absurd, so it gets caught |
| `quote_orders` coverage-bounded | Older quotes read unconverted either way |
| **Quote population self-selected** | Denominator missing its losses. Unfixable by query |

The third is the dangerous one, because a careful reader defeats the first two and lands
on 76% feeling rigorous.

## One question you can ask, one you cannot

**"Did this specific quote convert?"** Answerable, as a fact. Use
[quote_orders](quote-orders.md) inside its window. That is what the chase digest runs on.

**"What is our conversion rate?"** Not answerable here. Not from this column, not from the
link table, not from both.

Ruled July 2026 and standing: **the job system holds what was quoted, the project board
holds what happened to it.** That is why this column is empty of meaning, and why the rate
lives outside this map. No card here carries a conversion figure, deliberately.

## Hits

- Nothing. No script reads it, no process writes it. That is what makes it a ghost rather
  than a leftover.
- [quote_orders](quote-orders.md) is not a dependant, but it **disproves** this one. If
  you open one other card, open that.

## Does not hit

- **A conversion rate.** The thing its name promises, and the thing this territory cannot
  produce, because the recorded quote population is self-selected.
- **[quote_orders](quote-orders.md), as a replacement.** Right answer to a *different*
  question. Reaching for it to build a rate carries the population problem across, and the
  result looks rigorous.
