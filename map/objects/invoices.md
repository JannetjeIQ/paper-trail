# invoices

**Type:** record
**State:** live, **coverage-bounded**
**Lives at:** table `invoices` in [jobs.sqlite](jobs-sqlite.md)
**Source of truth:** `<records-kb>/data-dictionary.md` section `invoices`

## What it is

Invoice records against orders. A few thousand rows. Net, VAT and total are separate
columns here, so unlike [orders](orders.md) there is no basis ambiguity. Every row
matches an order.

## Why it is shaped that way

It only exists from **a hard start date in 2024**. Before that date the business invoiced
from a different accounting system, and those invoices were never migrated. The table
is not incomplete by accident: it starts when the current system started.

## Traps

- **The coverage floor is the whole story.** Any question touching a period before that date returns zero rows and reads as "nothing was invoiced". Order statuses from
  that era assert that invoicing happened elsewhere, which is the only evidence that
  survives. Scope every query to the floor and say so in the answer.
- **`paid` is not reliable.** It is carried through from the source and is not
  maintained to the standard the column name implies. Do not build a debtors position
  on it. The money answer lives across
  [the accounting boundary](accounting-boundary.md).
- **Void invoices exist and must be excluded** from any invoiced total, or reissued
  invoices double-count.
- Deposit invoicing is normal: a job can legitimately carry an invoice worth a fraction
  of the order value with the balance still to come. That pattern is the reason
  [invoicing_check.py](invoicing-check.md) exists.

## Hits

- [invoicing_check.py](invoicing-check.md) : sums this table net against order net to find shortfalls.
- [orders](orders.md) : joins on order number. Orders must be deduped first or the join fans out.

## Does not hit

- **The financial record.** This is a record that an invoice was raised in the
  production system. It is not the ledger, it is not the debtors position, and it is
  not what the accountant works from. See
  [the accounting boundary](accounting-boundary.md).
- **Pre-2024 revenue.** Not a gap to be filled by widening a date range. The rows do
  not exist anywhere in this store.
