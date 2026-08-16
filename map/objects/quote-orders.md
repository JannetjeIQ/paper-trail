# quote_orders

**Type:** record
**State:** live, **coverage-bounded**
**Lives at:** table `quote_orders` in [printlogic-sqlite](printlogic-sqlite.md)
**Source of truth:** the report definition in the live system, mirrored by `build_db_api.py`

## What it is

The system's own mapping from quote number to order number. About 2,270 pairs.
Composite key, both columns. This is the **authoritative answer to "did this quote
convert?"** and it is the only acceptable answer.

## Why it is shaped that way

Before it existed, conversion was inferred by matching quotes to orders on client,
value and description. That inference failed three ways, all of them recorded:

- **Value alone missed split orders.** One quote delivered as two orders of half the
  value each read as unconverted.
- **Description alone over-matched.** A single small order was assigned to five
  different quotes at a repeat-business client, because the job descriptions were
  near-identical.
- It produced a 34-item list of quotes said to be missing their order number. When
  this table arrived, **every one of the 34 was wrong**. None of those quotes had an
  order at all.

That history is why the rule on this card is absolute rather than a preference.

## Traps

- **Coverage is capped and the cap is invisible.** The source report is limited to
  5,000 rows sorted by order number descending, because the uncapped version crashes
  the reporting server. In practice it covers orders from roughly mid-2025 onward.
  **A quote older than that reads as unconverted whether it converted or not.**
- The consumer script enforces a coverage floor of 1 September 2025 for exactly this
  reason, and within that floor coverage is about 99.7%. Any analysis that widens the
  window without raising the report cap is producing false negatives, at scale, silently.
- The source emits one row per order **line**, so pairs repeat. They are deduped at
  load. If you ever read the raw report, they will not be.

## Hits

- `quote_chase.py` : reads this to age open quotes. Its coverage floor is set from this table's bound.
- Any conversion, win-rate or pipeline figure : this table is the input. There is no second source.

## Does not hit

- **`quotes.status`.** The instinct on being told "conversion is unreliable" is to
  reach for the status column instead. That column is a
  [ghost](ghost-quotes-status.md). This table exists **because** that column is dead.
- **Anything before mid-2025.** Not a data-quality caveat, a hard edge. Outside the
  window this table does not answer the question, it answers "no", which is a
  different thing.
