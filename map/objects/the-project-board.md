# The project board

**Type:** boundary
**State:** live, outside this territory
**Lives at:** a separate SaaS project board, not in this territory
**Source of truth:** the board itself, for anything about what happened to a quote

*Added after a cold walk found the map telling readers to leave without naming where to
go. See `../../COLD-WALK.md`, walk 5.*

## What it is

The wall at the outcome end of this territory, and the answer to the question this map
keeps refusing.

Ruled July 2026: **the job system holds what was quoted, the project board holds what
happened to it.** Everything in this map is the first half of that sentence. This card is
the door to the second.

## What crosses, and in which direction

| Crosses | Direction | Notes |
|---|---|---|
| Quote raised, with its number | job system → board | Keyed by a person. No integration mapped here |
| Won, lost, stalled, reason | **board only** | Does not exist on this side, in any column |
| Owner and stage of a live opportunity | board only | |
| The order, once won | job system | The board does not hold order or invoice records |

About 98% of quotes reach the board, measured by a capture-gap script on this side. That
figure describes **arrival**, not outcome, and says nothing about whether the outcome
field was then filled in.

## What is true on the other side that is not true here

- **Outcome is tracked deliberately there.** Not as a by-product. That is the whole point
  of the July 2026 ruling.
- **The population is still not every quote given.** Crossing this wall fixes the dead
  field and the coverage bound. It does not fix the fact that a price given verbally and
  lost may never have been recorded anywhere. Ask what the board's own denominator is
  before quoting a rate from it.
- **A capture-gap check on this side needs a fresh board pull.** The default archived
  snapshot is dated and will flag recent quotes as missing purely because it pre-dates
  them.

## Hits

- Any conversion, win-rate or pipeline question : this is where it goes. This map cannot answer it.
- [quotes](quotes.md) : the board is keyed on quote numbers originating there.

## Does not hit

- **[quote_orders](quote-orders.md).** Independent of the board entirely. It is the job
  system's own internal mapping, and a quote can convert there while the board says
  nothing, or the reverse.
- **Any record in this map.** Nothing flows back. Marking something won on the board
  changes no column on this side, ever.
