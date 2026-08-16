# rates.json

**Type:** config
**State:** live
**Lives at:** `10-delivery/IQ_Estimator/pricing-engine/rates.json`
**Source of truth:** itself. It is the declared single source of truth for pricing.

## What it is

One JSON file holding every rate the business quotes from: product rates by square
metre, install crew rates, studio hourly rates, travel bands, rounding rules, minimum
margins, and per-partner exceptions. Roughly thirty top-level sections. It carries its
own version and a last-updated date.

**This card does not reproduce a single figure from it, deliberately.** Rates change,
cards do not, and a card carrying a stale price is worse than no card at all. Open the
file. That is what citing means.

## Why it is shaped that way

It was built by reconciling values that had drifted across a spreadsheet, a quoting
app and people's heads, and ruling on each one. The file's own note says the point out
loud: do not hand-edit drifted copies elsewhere, the engine and every downstream
consumer read **this** file.

The structure encodes commercial policy, not just numbers. Rounding rules, minimum job
value, minimum margin split by one-off versus repeat, and a default contingency all
live here as data rather than as judgement, which is what makes the engine's output
defensible.

## Traps

- **Copies are the danger, not the values.** Any rate that appears in a spreadsheet, an
  app screen or a document is a copy and is drifting from the moment it is written. The
  test for whether a rate is real is whether it is in this file.
- **Several rules here are counter-intuitive and get "corrected" by well-meaning
  readers.** Travel is charged per attendance day rather than once per job. A half day
  is not pro rata and only applies as spillover beyond a full day. Wastage is applied
  to net area and never shown to the client. Each of these has a note in the file
  explaining itself. Read the note before changing the value.
- **At least one partner is a standing exception** to a rule that otherwise always
  applies. Exceptions live in the file, not in someone's memory, which is the point.
- Prices are ex-VAT throughout unless a section says otherwise.

## Hits

- [engine.js](engine-js.md) : reads this file at run time. A key rename breaks pricing immediately and loudly.
- `validate.js` : the golden tests reconstruct real sent quotes from these rates. Change a rate and tests that reproduce historical quotes will fail, correctly. Expect it and update the case, do not silence it.
- The quoting app and any downstream agent handoff : all declared readers of this file.

## Does not hit

- **Historical quotes and orders.** Nothing recalculates. A rate change applies to the
  next quote priced, not to anything already in [quotes](quotes.md) or
  [orders](orders.md). A reader who changes a rate expecting reporting to move will see
  nothing move, and will conclude wrongly that the change did not take.
- **The customer pricing band in the print-shop system.** That is a
  [ghost](ghost-pricing-band.md) and has never fed this file.
