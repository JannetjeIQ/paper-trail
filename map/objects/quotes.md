# quotes

**Type:** record
**State:** live
**Lives at:** table `quotes` in [jobs.sqlite](jobs-sqlite.md)
**Source of truth:** `<records-kb>/data-dictionary.md`, section `quotes`, read against the build script

## What it is

Quote headers. About 24,000 rows, January 2010 to the present. One row per quote raised in
the system. The primary key is the quote number, and every one is unique.

This is the record of **what was quoted**. It is not the record of what happened next.
That distinction was settled by a ruling in July 2026 and it is the most important
sentence on this card: **the system holds what was quoted, the project board holds
what happened to it.**

## Why it is shaped that way

The quotes report was added to the store late, in July 2026, to answer conversion
questions that had previously been guessed at. It arrived without a lines table,
because the tens of thousands of quote lines in the source carry no usable key
and are dropped at build. So a quote here is a header and a total, never a breakdown.

## Traps

- **`status` is dead.** It has its own card: [quotes.status](ghost-quotes-status.md).
  Read that before you use this table for anything resembling a win rate.
- **`total` is ex-VAT on strong evidence, not proof.** The dataset exposes no VAT
  column, so there is nothing to check it against. The evidence is that every one of
  the non-zero values is a whole euro, with no cents anywhere, which is what
  you get from ex-VAT prices rounded to the euro and not what you get from a VAT
  calculation. Treat as ex-VAT, say so when you report, and do not compare a quote
  value to an order value without stating both bases.
- **`last_email_date` is a channel flag, not an issuance flag.** Populated on about a
  quarter of rows. Blank means "not emailed from inside the system", not "never sent".
  Quotes sent by ordinary email and keyed in afterwards are the normal case. Read as
  issuance, this column manufactures a finding that three quarters of all quotes were
  never sent.
- **`description` contains typos and always will.** It is free text typed under time
  pressure. Two records for the same job routinely spell the site differently. Fuzzy
  match, never match exactly.
- `accounts_code` is filled on about half the rows and is **not** a join key. See
  [customers](customers.md).

## Hits

- [quote_orders](quote-orders.md) : the only supported route from a quote to an order. Joins on quote number.
- [customers](customers.md) : joins on customer name. Two rows do not match, which is normal.
- `quote_chase.py` : the open-quote chase digest reads this table and the link table together.

## Does not hit

- **`order_lines`.** The obvious move to get quote detail is to add the quote relation
  to the order-lines report. It **crashes the reporting server**. There is no quote
  lines table and there is not going to be one by that route.
- **The `quoting/` folders.** Different population entirely: about 24,000 records
  against a few dozen live folders. See [the quoting convention](quoting-folder.md).
