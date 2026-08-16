# customers

**Type:** record
**State:** live
**Lives at:** table `customers` in [jobs.sqlite](jobs-sqlite.md)
**Source of truth:** `<records-kb>/data-dictionary.md` section `customers`

## What it is

The client master list. A few thousand rows. One per trading name. Carries address,
primary contact, a segment category and the account owner.

## Why it is shaped that way

It is sixteen years of a sales team typing client names into a box. There was never a
mandatory customer code, so the **name is the key**, and everything joins on it. This
is the defining constraint of the territory and the reason the folder conventions carry
an explicit anchor block rather than a code in the folder name.

## Traps

- **`accounts_code` looks like the key and is not.** Blank on about 78% of rows,
  free-text where present, explicitly ruled out as a join key. Joining on it silently
  drops four fifths of the client base. The query runs, the answer is confidently
  partial, and nothing warns you. This is the highest-frequency wrong turn in the
  territory.
- **The same client can exist more than once** under spelling variants, because the
  key is a typed name. Fuzzy match when counting clients.
- **`category` is about half noise.** There is a known valid list of segment tags.
  Anything outside it is free text somebody typed once. A categorisation exercise on
  this column was still in flight when this map was walked.
- **`owner_code` is a current snapshot with no history.** It is overwritten when an
  account changes hands, and there is no record of the change. At least one known
  ownership transfer from 2015 is invisible here. For anything historical, use
  `rep_code` on [orders](orders.md).

## Hits

- [orders](orders.md), [quotes](quotes.md) : both join to this table on name. Renaming a client here orphans nothing, because the join is by value, but it does split their history in two.
- The quoting and orders folder conventions : both carry a billing-customer anchor sourced from this table.

## Does not hit

- **The end client.** Many jobs bill through an intermediary: a print reseller, a
  design practice, a main contractor. The name on this record is **who pays**, which is
  frequently not who the work was for. A report of "our clients" built from this table
  is a report of who we invoice.
- **Contacts beyond the first.** There is only ever a primary contact here. A secondary
  contacts table was named in the older build and does not exist in the current store.
