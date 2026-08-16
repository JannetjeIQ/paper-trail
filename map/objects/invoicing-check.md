# invoicing_check.py

**Type:** process
**State:** live
**Lives at:** `<scripts>/invoicing_check.py`
**Source of truth:** itself, and its docstring, which records the reasoning

## What it is

A weekly check for jobs that are **complete but not fully invoiced**. It writes a
paste-ready digest for the person who does invoicing, copied to the director.

The case it exists for: a deposit invoice was raised, the job finished, and the final
invoice on completion never was. The order looks invoiced because an invoice exists.
The money is short.

## Why it is shaped that way

Its design decisions are worth reading because each one is a scar:

- **It compares net against net.** Order net against invoice net, which sidesteps the
  VAT-basis ambiguity that was live and unresolved when it was written. Gross is shown
  for context and never used in the arithmetic. The ambiguity has since been settled
  (see [orders](orders.md)) and the script's approach remains correct anyway.
- **It dedupes orders to one row per number first**, because duplicate order rows from
  the July 2026 rebuild would otherwise fan the invoice join into a product and inflate
  every total.
- **It excludes void invoices and cancelled orders.**
- **"Completed" is matched as a pattern**, not an equality, because there are many
  completion status variants and at least one exists in two casings.
- The "no invoice at all" section is scoped to the 2024 invoice floor and further
  excludes statuses that assert invoicing happened in the previous accounting system.

## Traps

- **A human sends it.** The script writes a file. It does not email anyone. It is
  automation up to the point of the send and manual after it, and a reader who assumes
  the digest goes out on its own will assume the check is running when it is not.
- Its threshold is a floor in euros, adjustable at the command line. A default that
  looks like a bug is a deliberate noise filter.

## Hits

- [orders](orders.md) and [invoices](invoices.md) : reads both. Any change to status vocabulary or the VAT basis changes what this finds.
- The invoicing person's week : this is the input to a real recurring task.

## Does not hit

- **The debtors position.** This finds jobs we have not billed. It says nothing about
  whether billed work has been paid. Those are different problems with different owners
  and the `paid` flag here is not trustworthy for the second one. See
  [the accounting boundary](accounting-boundary.md).
- **Anything before that date.** Bounded by the invoice floor, and it says so in its
  own scoping rather than returning a confident nothing.
