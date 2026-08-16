# orders_ext

**Type:** record
**State:** **ghost**, removed target
**Lives at:** nowhere. Verified absent from the current store.
**Formerly at:** a side table in the pre-July-2026 manual build

## What it is

A table that no longer exists.

It used to carry the fields that would not fit on the main order record: rep, owner,
status, completion date, invoice number. The July 2026 rebuild moved all of them onto
[orders](orders.md) directly, and the side table went away with the build that made it.

## Why it is still a hazard

Because the name outlived the table. It appears in older saved queries, in analysis
written against the previous build, and in the working memory of anyone who learned
this territory before mid-2026, human or model.

A query joining to it does not return a subtly wrong answer. It **fails**, which is the
kindest thing a ghost can do. The hazard is not the failure, it is the diagnosis: the
obvious reading of the error is that the database is broken or the rebuild dropped a
table. It is neither. The fields were promoted and are all still there, on the record
next door.

The previous manual store is preserved as a separate backup file. It is not the current
world and must not be queried as though it were.

## What a reader will conclude if they trust it

That the store is missing data. They will go looking for a restore, or rebuild
something that already exists, when the columns they want are sitting on
[orders](orders.md) under the same names.

## Hits

- Nothing live. It has no dependants because it has no existence.

## Does not hit

- **[orders](orders.md).** Not in the sense of being attached to it. But orders is where
  every field this ghost used to hold now lives, which is the only thing a reader who
  lands here needs to be told. Go there.
