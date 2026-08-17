# quotes.status

**Type:** record field
**State:** **ghost**, empty field
**Lives at:** column `status` on [quotes](quotes.md)
**Source of truth:** the column's own value distribution, and the July 2026 ruling that followed it

## What it is

A status column on every one of about 24,000 quotes. 100% populated, clean
sensible-looking values dominated by `With Client` and `Quote`.

**`Successful`: 44.** Across sixteen years.

## The search that proved it

Searched every loader and report script for the column. It **is** written, once, by the
nightly loader faithfully copying the source column. Downstream it is read **zero** times
for any analytical purpose, and its only two other appearances are comments in the loader
and the chase digest telling you not to use it.

Sharper than "nothing touches it", and it is the correction the search forced. A populated
field with a real writer and no reader is a better-evidenced ghost than one merely
asserted to be orphaned.

## What a reader will conclude if they trust it

A conversion rate of about **0.2%**. Plausible as a business fact, alarming enough to be
escalated, specific enough to be believed, from a fully-populated column in a table that
is otherwise trustworthy. Nothing warns.

This is the shape of every ghost: **it answers.**

## The trap behind the trap

Kill the 0.2% and a second wrong answer waits. Count quotes with a row in
[quote_orders](quote-orders.md) inside its window, allow 90 days to settle, and you get
roughly **three in four**, stable across six cuts.

**Also wrong**, for a reason no query fixes. The denominator is not "quotes we gave", it
is **"quotes somebody chose to enter"**. A quote keyed in when the job looks serious, or
after it landed, is in the table. A price given over the phone and lost never was.
Historic practice was looser still. The losses are missing from the bottom, so the
fraction climbs.

| Defect | Effect |
|---|---|
| `status` unmaintained | Gives 0.2%. Absurd, so it gets caught |
| `quote_orders` coverage-bounded | Older quotes read unconverted either way |
| **Quote population self-selected** | Denominator missing its losses. Unfixable by query |

The third is the dangerous one: a careful reader defeats the first two and lands on 76%
feeling rigorous.

## One question you can ask, one you cannot

**"Did this quote convert?"** Answerable, as a fact, from
[quote_orders](quote-orders.md) inside its window. That is what the chase digest runs on.

**"What is our conversion rate?"** Not answerable here. Ruled July 2026: the job system
holds what was quoted, the project board holds what happened to it. The rate lives outside
this map, and no card here carries one.

## Hits

- Nothing reads it. The loader writes it and no consumer consults it.
- [quote_orders](quote-orders.md) is not a dependant, but it **disproves** this one.

## Does not hit

- **A conversion rate.** What its name promises, and what this territory cannot produce.
- **[quote_orders](quote-orders.md), as a replacement.** Right answer to a *different*
  question. Building a rate from it carries the population problem straight across.
