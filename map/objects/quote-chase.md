# quote_chase.py

**Type:** process
**State:** live
**Lives at:** `30-systems/scripts/printlogic/quote_chase.py`
**Source of truth:** itself, and its docstring, which records the reasoning

*Added after a cold walk found no door for the question "which quotes are still open?".
See `../../COLD-WALK.md`, walk 1.*

## What it is

The open-quote chase digest. Lists recent quotes with no order against them, grouped by
the person who raised them and aged, so each account manager gets a short list of what
is still sitting with a client. Optionally enriched with project-board state.

Default window is 90 days and a minimum value floor, both adjustable.

## Why it is shaped that way

**"Open" is decided by absence from [quote_orders](quote-orders.md), and nothing else.**
A quote with no row in the system's own quote-to-order mapping is open. That is a fact
rather than an inference, and the distinction is the entire reason the script is
trusted.

It replaced an inference-based version in July 2026 that matched quotes to orders on
client, value and description. That version failed three ways, each of which looked
plausible until it was checked. The failures are recorded on
[quote_orders](quote-orders.md). The standing instruction is not to reinstate the
inference under any circumstances.

## Traps

- **It refuses to report beyond a coverage floor, and that refusal is a feature.**
  The floor exists because [quote_orders](quote-orders.md) is built from a capped
  report. Widening the window without first raising the cap turns every older quote
  into a false "still open", and the digest would then chase clients about work that
  was delivered a year ago.
- The board enrichment takes a **fresh** board pull. The default archived snapshot is
  dated, and passing it will flag recent quotes as missing from the board purely
  because the snapshot pre-dates them.
- It reports, it does not chase. A person reads the digest and decides. Nothing here
  contacts a client.

## Hits

- [quote_orders](quote-orders.md) : the sole input for the open/closed decision. Its coverage bound sets this script's floor.
- [quotes](quotes.md) : the population being aged.
- The account managers' week : this is the input to a real recurring task.

## Does not hit

- **[quotes.status](ghost-quotes-status.md).** The obvious column for "is this quote
  still open" and a ghost. The script explicitly refuses it, and its docstring says so.
- **Forecasting.** An aged list of unconverted quotes is not a pipeline value. Nothing
  here weights, probability-adjusts or forecasts, and the underlying data cannot
  support it.
