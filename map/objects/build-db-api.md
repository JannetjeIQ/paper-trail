# build_db_api.py

**Type:** process
**State:** live
**Lives at:** `30-systems/scripts/printlogic/build_db_api.py`
**Source of truth:** itself. When it and the data dictionary disagree, this file wins.

## What it is

The nightly rebuild. Pulls **seven** reports from the print-shop system's reporting API
and writes [printlogic.sqlite](printlogic-sqlite.md) from scratch: customers, orders,
order lines, invoices, purchase orders, quotes, and the quote-to-order link.

It is the only writer of the store. Every shape question in this territory is
ultimately a question about this file.

## Why it is shaped that way

It replaced a hand-exported build in July 2026. The reporting API returns
human-readable values rather than numeric keys, which is why the store has no ids and
joins on text. That is a property of the source, inherited, not a design choice made
here.

It drops rows on purpose, and the drops are the part readers most need to know about.

## Traps

- **It drops data silently, by design.** Test-customer orders are excluded. Quote-only
  lines are dropped at the order-lines step, which is why there is no quote lines table
  and why about 31,000 quote lines are simply unavailable. Legacy rows with impossible
  dates are nulled on load. None of this is visible from the store.
- **Two named things do not exist here.** A secondary contacts table and an off-system
  pipeline list were both part of the older manual build and were not carried across.
  Owner-history overrides went the same way. They are named in comments and in the
  documentation. Reaching for them by name will fail. They are **never-built ghosts**
  in the current world, recorded here rather than given their own cards because nothing
  downstream depends on them.
- **The documentation undercounts the reports.** The data dictionary says five in one
  place and six in another. It is seven. A small thing, and a clean illustration of why
  this file is the source of truth and that one is orientation.
- Report row caps are a real constraint, not a tuning parameter. At least one report
  crashes the reporting server uncapped. See [quote_orders](quote-orders.md).

## Hits

- [printlogic.sqlite](printlogic-sqlite.md) : rebuilt entirely by this script. Every table, every index.
- Every reporting script downstream : they read a store whose shape this file decides.

## Does not hit

- **The live print-shop system.** Read-only. It pulls, it never writes back.
- **[rates.json](rates-json.md) or the pricing engine.** Different half of the
  territory entirely. Pricing and records touch only through a human keying a quote in.
