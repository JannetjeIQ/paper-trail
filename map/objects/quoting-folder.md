# quoting/&lt;end-client-slug&gt;/

**Type:** convention
**State:** live
**Lives at:** `<delivery>/quoting/`
**Source of truth:** `<delivery>/quoting/CONTEXT.md`

## What it is

One folder per opportunity, pre-acceptance. A few dozen live at any time, named with a
human end-client slug. Inside: the client's request and attachments, a `CONTEXT.md`, and
the quote document moving draft to review to final. Pipeline jobs also carry priced JSON
and two spreadsheets, internal and client.

Two intake routes land here: hand-authored quotes, and pipeline output. That
consolidation happened in July 2026 and is why a
[leftover staging path](leftover-email-to-quote-staging.md) still exists.

## Why it is shaped that way

Because **there is no reliable customer code** in the job system, see
[customers](customers.md), so a folder cannot be named after a client key. There is not
one to name it after.

The convention resolves this with an **anchor block inside `CONTEXT.md`** rather than in
the folder name: billing customer, end client where it differs, and the quote or order
number once raised. The anchor sits inside, the folder name stays human.

Inventing a reference code is barred by a standing rule: the real reference is always the
system's own quote or order number. An invented one teaches everyone downstream a
reference that resolves nowhere.

## Traps

- **Nothing enforces any of this.** No script validates the folder name or confirms the
  `CONTEXT.md` anchor is filled. It holds because people follow it. Expect a proportion
  to be missing the anchor, and expect it to be the ones you need.
- **Billing customer and end client are routinely different.** Jobs bill through
  resellers, design practices and main contractors. The folder is named for the end
  client, the record filed against the payer. Take the folder name as the client and you
  will not find the job in [orders](orders.md).
- The central feedback and outcomes logs stay central. Do not tidy them into the job
  folder they refer to.

## Hits

- [orders/&lt;slug&gt;/](orders-folder.md) : on acceptance the folder graduates. A move, not a copy.
- The pricing engine's central logs : per-job outputs reference them.

## Does not hit

- **[quotes](quotes.md).** No link either way. About 24,000 records against a few dozen
  folders. "How many open quotes" answered from folders and from records gives two
  numbers that are both right and thousands apart.
- **The pricing engine code.** Only its **output** lands here. Changing a quote document
  changes nothing about how the next one is priced.
- **A resolution of the drift below.** The source says an accepted quote moves "up one
  level" into delivery proper; the destination says folders arrive into `orders/`. Both
  in force, same move described differently. Marked, not resolved: the owner's call.
