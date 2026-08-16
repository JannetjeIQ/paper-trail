# The accounting package

**Type:** boundary
**State:** live, outside this territory
**Lives at:** a separate cloud accounting system, plus an outsourced bookkeeping firm
**Source of truth:** the accounting package, for anything financial

## What it is

The wall at the money end of this territory. The job system records that an
invoice was **raised**. The accounting package records what was **owed, received and
reconciled**. Bookkeeping is outsourced, so there are people on the other side of this
wall as well as a system.

## What crosses, and in which direction

| Crosses | Direction | Notes |
|---|---|---|
| Invoice raised | production system → accounting | Not by an integration. Reconciled by people |
| Payment received | accounting only | Never reaches the production system reliably |
| Debtors position | accounting only | Does not exist on this side |
| Pre-2024 invoice history | neither | Sat in a **previous** accounting system, migrated to neither |

There is no live integration mapped in this territory. Treat the join as human.

## What is true on the other side that is not true here

- **The financial figures are the real ones.** If a figure from
  [invoices](invoices.md) disagrees with the accounting package, the accounting package
  is right and the production record is a production record.
- **Payment is knowable there and is not knowable here.** The `paid` flag on this side
  is not maintained to the standard the name implies.
- **Their reporting is on a different calendar and a different basis.** Anything you
  hand across the wall must state its basis explicitly, because "total" does not mean
  the same thing on both sides. See `../reference/naming-collisions.md`.

## Hits

- Any figure you send outward : it will be read against the accounting package and must state its basis.
- [invoicing_check.py](invoicing-check.md) : its output crosses this wall to a person, weekly.

## Does not hit

- **[orders](orders.md) and [invoices](invoices.md).** Nothing flows back. Marking
  something paid or corrected in accounting changes nothing on this side, ever, and the
  production record will keep saying what it always said.
- **[the debtors question you probably arrived with].** If the question is who owes us
  money, you are in the wrong territory. This card is a wall, not a door: it tells you
  to leave, and where to go.
