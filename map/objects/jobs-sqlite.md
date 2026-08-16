# jobs.sqlite

**Type:** store
**State:** live
**Lives at:** `<records-kb>/jobs.sqlite`
**Source of truth:** the build script, `<scripts>/build_db.py`. Not the data dictionary. See Traps.

## What it is

A local, queryable copy of the job-management system, rebuilt nightly from
seven API report pulls. Seven tables, of which six matter to this territory. It is the
only place anyone actually runs a query. Nobody queries the live system.

It is a **copy**, and it is **derived**. Every oddity in it is either an oddity in the
source system or a decision made by the build script, and telling those two apart is
the single most useful skill in this territory.

## Why it is shaped that way

It replaced a hand-exported build in July 2026. The switch to the reporting API
changed the shape underneath: the API returns human-readable values rather than
numeric foreign keys, so **there are no numeric ids anywhere**. Records join on text:
order number, customer name. Those joins are indexed but not enforced, and a handful
of orphan rows on each side are normal rather than a fault.

## Traps

- **Each table has its own coverage window, and none of them announce it.** Quotes go
  back to 2010. Orders go back sixteen years. Invoices start at a fixed date in 2024. The
  quote-to-order link covers roughly mid-2025 onward. A query spanning all four
  silently returns the intersection, and the answer looks complete.
- **The data dictionary is documentation, not the loader.** It is the best orientation
  in the territory and it has drifted at least twice: it describes the wrong VAT basis
  on one column, and it says the store is built from five reports when it is seven. If
  the dictionary and the build script disagree, **the build script wins**. If the build
  script and the live system disagree, the live system wins.
- Duplicate order rows exist as an artefact of the July 2026 rebuild. Anything joining
  orders to invoices must dedupe to one row per order number first, or the join fans
  out into a product and every total is inflated.

## Hits

- `build_db.py` : it is the only writer. Any schema question is a question about it.
- Every reporting script : they all open this file. A column rename here breaks all of them at once.
- `orders`, `quotes`, `invoices`, `customers`, `quote_orders` : they are contents of this store, not independent systems.

## Does not hit

- **The live job system.** This is strictly read-only and downstream. Nothing
  you do to this file changes a record anyone in the business can see. A reader who
  fixes bad data here has fixed nothing, and it will be gone at the next rebuild.
- **The accounting package.** No connection in either direction. See
  [the accounting boundary](accounting-boundary.md).
