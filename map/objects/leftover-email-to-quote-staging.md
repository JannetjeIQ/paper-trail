# email-to-quote/quotes/

**Type:** convention
**State:** **leftover**
**Lives at:** `10-delivery/IQ_Estimator/email-to-quote/`
**Superseded by:** [quoting/&lt;end-client-slug&gt;/](quoting-folder.md), July 2026

## What it is

The retired staging path for output from the email-to-quote pipeline. Pipeline jobs
used to be written here and were later moved by hand into the quoting folders. Since
July 2026 the pipeline writes straight into `quoting/<end-client-slug>/`.

## Why it is still here, and why that is fine

Two reasons, and both are honest.

1. **The pipeline code still lives at this path.** Only the quote **output** moved. The
   assembly step and the spreadsheet builder are here and are live. The folder is not
   dead, one convention inside it is.
2. **The central logs live here and must stay here.** The pricing feedback log and the
   quote outcomes log are read as one series by the calibration loop. They are
   explicitly not to be moved into per-job folders.

This is the difference between a leftover and a ghost, and it is worth pausing on. The
path resolves. Live code sits in it. What is retired is one specific use of it: as the
place quote output lands. A reader who deletes the folder because "quotes moved" takes
the pipeline and the calibration history with it.

## Traps

- Old job output still sits here from before the consolidation. It is real history and
  it is **not** where anything current lives. Reading it as the live quote set gives a
  stale and partial picture.
- The retirement is recorded in one sentence in the destination's `CONTEXT.md`. If you
  had not read that sentence, nothing about this folder would tell you it was
  superseded. That is the normal condition of a leftover: it looks completely alive
  from the inside.

## Hits

- The calibration loop : it reads the central logs kept here. Moving them breaks it quietly, with no error.
- [engine.js](engine-js.md) : the pipeline assembly step here is a consumer of the engine.

## Does not hit

- **Current quote work.** Nothing lands here now. A folder here is history.
- **The pricing rates.** Nothing in this folder holds a rate. See
  [rates.json](rates-json.md).
