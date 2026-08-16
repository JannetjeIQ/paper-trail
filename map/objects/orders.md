# orders

**Type:** record
**State:** live
**Lives at:** table `orders` in [jobs.sqlite](jobs-sqlite.md)
**Source of truth:** `<records-kb>/data-dictionary.md` section `orders`, **except on the VAT basis**, where the workspace guardrail overrides it. See Traps.

## What it is

One row per won job. Tens of thousands of them. The spine of the whole territory: quotes
point forward into it, and lines, invoices and purchase orders all hang off it. The
order number is the join key for everything downstream.

## Why it is shaped that way

The July 2026 rebuild flattened what used to be two tables into one. Rep, owner,
status, completion date and invoice number used to live on a side table and now sit
directly on this record. That side table is a [ghost](ghost-orders-ext.md) and still
appears in older queries.

## Traps

- **`total` is NET, excluding VAT.** `vat` sits alongside it and gross is the sum.
  This was contested inside the business for months and settled by two independent
  checks: across every order in the store the ratio of vat to total is exactly
  0.23, plus the historic and reduced rates, which only holds if total excludes VAT; and a live test
  order priced at 100 read back as a total of 100 with VAT of 23.
  **The data dictionary still carries the old, wrong claim on one line.** This is the
  clearest case in the territory of the rule that a card, and a schema doc, lose to the
  thing that was actually verified.
- **Two rep columns, and the obvious one is wrong.** `rep_code` is who worked the
  order: per-order, historically accurate, and the correct reporting lens. `owner_code`
  is who owns the client **today**, overwritten when ownership changes, therefore wrong
  for any historical question. Two of the codes appearing in `rep_code` are operations
  administrators rather than salespeople and must be excluded from rep reporting.
- **Cancelled orders must be excluded.** Several thousand rows. This is a standing
  rule, not a judgement call. Every analysis carries the exclusion.
- **Status strings are inconsistent by design and by accident.** There are many
  completion variants, and at least one exists in two casings. Match on a pattern, not
  on equality.
- A minority of recent orders have a blank invoice number. That is in-flight work, not
  an error.

## Hits

- `order_lines`, `invoices`, `purchase_orders` : all join on order number. A change to how orders are keyed breaks all three.
- [quote_orders](quote-orders.md) : joins on order number. Its coverage bound is expressed in order numbers.
- [invoicing_check.py](invoicing-check.md) : reads status and total to find under-invoiced jobs.
- Every revenue, rep and client figure the business quotes : this table is the source.

## Does not hit

- **The `orders/` folders.** A few dozen folders against tens of thousands of records. Absence of a
  folder says nothing about the job. See [the orders convention](orders-folder.md).
- **`customers.owner_code`.** Same name, sitting on the customer record rather than the
  order. Changing a client's owner does not rewrite the history on this table, which is
  precisely why `rep_code` is the reporting lens.
