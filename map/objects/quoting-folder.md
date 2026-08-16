# quoting/&lt;end-client-slug&gt;/

**Type:** convention
**State:** live
**Lives at:** `<delivery>/quoting/`
**Source of truth:** `<delivery>/quoting/CONTEXT.md`

## What it is

One folder per opportunity, pre-acceptance. A few dozen live at any time. The folder
name is a human end-client slug. Inside: the client's request and attachments, a
`CONTEXT.md`, and the quote document as it moves from draft to review to final.
Pipeline-produced jobs also carry their priced JSON and two spreadsheets, one internal
and one for the client.

Two intake routes land in the same place: quotes authored by hand, and quotes produced
by the email-to-quote pipeline. That consolidation happened in July 2026 and is the
reason a [leftover staging path](leftover-email-to-quote-staging.md) still exists.

## Why it is shaped that way

Because **there is no reliable customer code** in the job system. See
[customers](customers.md). A folder therefore cannot be named after a client key,
because there is not one to name it after.

The convention resolves this by putting an **anchor block inside `CONTEXT.md`** rather than
in the folder name: the billing customer, the end client where it differs, and the
quote or order number once one is raised. The anchor is inside the folder, and the
folder name stays human.

The rule against inventing a reference code is explicit and standing: the real
reference is always the system's own quote or order number. A folder that carries an
invented code teaches everyone downstream a reference that does not resolve anywhere.

## Traps

- **Nothing enforces any of this.** No script validates the folder name, no check
  confirms `CONTEXT.md` exists or that the the job system header is filled. It holds because people
  follow it. Expect a proportion of folders to be missing the anchor, and expect that
  proportion to be exactly the folders you need.
- **Billing customer and end client are routinely different.** Jobs bill through
  resellers, design practices and main contractors. The folder is named for the end
  client and the record is filed against the payer. If you take the folder name as the
  client, you will not find the job in [orders](orders.md).
- The central feedback and outcomes logs stay central. Do not tidy them into the job
  folder they refer to.

## Hits

- [orders/&lt;slug&gt;/](orders-folder.md) : on acceptance, the folder graduates. That is a move, not a copy.
- The pricing engine's central logs : per-job outputs reference them.

## Does not hit

- **[quotes](quotes.md).** No link, in either direction. There are about 24,000 records
  and a few dozen folders. A folder does not create a record and a record does not
  create a folder. "How many open quotes" answered from folders and answered from
  records gives two numbers that are both right and thousands apart.
- **The pricing engine code.** The engine lives elsewhere and only its **output** lands
  here. A change to a quote document changes nothing about how the next one is priced.

## An honest note on drift

The source document says an accepted quote moves "up one level" into delivery proper,
while the destination convention says folders arrive into `orders/`. Both are in force
and they describe the same move slightly differently. Marked here rather than resolved,
because resolving it is the territory owner's call, not the cartographer's.
