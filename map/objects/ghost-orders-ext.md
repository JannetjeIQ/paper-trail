# orders_ext

**Type:** record
**State:** **ghost**, removed target
**Lives at:** nowhere in the current store. **Still constructed and read by three scripts.**
**Formerly at:** a side table in the pre-July-2026 manual build

## What it is

A table that no longer exists, whose name is still live in code.

It used to carry the fields that would not fit on the main order record: rep, owner,
status, completion date, invoice number. The July 2026 rebuild moved all of them onto
[orders](orders.md) directly, and the side table went with the build that made it.

## The search that proved it

Two searches. The second is the one that matters.

**Does the table exist?** Listed every table in the store. Seven: customers, invoices,
order_lines, orders, purchase_orders, quote_orders, quotes. **No `orders_ext`.** Settled.

**Does anything still reach for it?** Searched the whole scripts folder for the name.
**Twenty-five hits across three files.** Nineteen are in the superseded manual CSV build,
which creates and drops the table. The other two files are report scripts that read it.

So this is not a dead name. It is a **live name pointing at nothing.** Any of those three
scripts, run today against the current store, fails or returns empty.

That correction came from running the search. The earlier draft of this card said the
table "lives nowhere", which was true of the database and wrong about the territory.

## Why that makes it worse, not weaker

A ghost with no callers is inert. This one has three, and one is an entire build script
that would construct a parallel database if anyone ran it.

The danger is not the crash, it is the **diagnosis**. The obvious reading of
"no such table: orders_ext" is that the store is broken or the rebuild dropped something.
It is neither. Every field this table held sits on [orders](orders.md) under the same
names.

## What a reader will conclude if they trust it

That the store is missing data, and a restore or rebuild is needed. They will hunt for a
backup, or re-derive columns that already exist one table over.

## Hits

- Nothing live depends on it, because it does not exist.
- Three scripts **name** it and would fail on it. Naming is not depending, but a reader
  who opens any of those three meets this ghost before they meet this card.

## Does not hit

- **[orders](orders.md)**, in the sense of being attached. But orders is where every
  field this ghost once held now lives, which is the only thing a reader landing here
  needs. Go there.
- **The current nightly build.** The live loader never references this table. The script
  that does is itself superseded, which makes it a leftover carrying a ghost.
