# engine.js

**Type:** process
**State:** live
**Lives at:** `10-delivery/IQ_Estimator/pricing-engine/engine.js`
**Source of truth:** itself, guarded by `validate.js` in the same folder

## What it is

The pricing engine. Around two dozen exported functions, one per priceable thing:
area-based products, letters, wayfinding, install, studio time, survey, hoarding,
framing, banners, and so on. It takes a described scope and returns priced lines.

The division of labour is the important part and it is a deliberate rule:
**the model classifies and maps, the engine does the arithmetic.** No price is ever
produced by a language model reasoning about what something should cost. That is what
makes a quote reproducible.

## Why it is shaped that way

Because the failure mode it was built against is a plausible invented number. A model
asked to price a job will produce something that looks right, cannot be traced, and
cannot be defended to a client who asks why. Putting the arithmetic in code and the
rates in [rates.json](rates-json.md) means every line of a quote can be walked back to
a rule.

`validate.js` is the load-bearing half of that promise. It reconstructs **real sent
quotes** from the current rates and asserts the engine still reproduces them, each case
citing its source quote. It is a regression harness against the business's own history.

## Traps

- **A failing golden test after a rate change is correct behaviour, not a bug.** The
  historical quote was priced at the old rate. The right response is to update the case
  and record why, not to loosen the tolerance.
- The engine reads rates at run time. It holds no defaults of its own. If a key is
  missing from the config the failure is immediate, which is intended.
- Feedback and calibration logs are kept **centrally**, not inside individual job
  folders, because the calibration loop reads them as one series. Moving them into
  per-job folders breaks that loop quietly.

## Hits

- [rates.json](rates-json.md) : read at run time. The two are one unit; neither is meaningful alone.
- `validate.js` : every engine change must survive it.
- The priced output in a [quoting folder](quoting-folder.md) : the priced and client-facing files are engine output.

## Does not hit

- **[quotes](quotes.md) in the print-shop system.** The engine prices a job. A human
  then raises the quote in the system, or does not. There is no write path from the
  engine into the records at all, and the two populations do not reconcile.
- **Historical pricing.** See [rates.json](rates-json.md). Nothing is recalculated
  retrospectively, ever.
