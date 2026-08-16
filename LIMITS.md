# Limits

Where this cartographer, and the map in `map/`, can be wrong. Read before trusting
either.

---

## Limits of the cartographer

**It cannot verify state on its own.** Live, leftover and ghost are judgements about
what is *used*, and use is often invisible from inside a folder. A file with no
readers in the repository may be opened by hand every Monday. The walk therefore has a
mandatory human gate at step 3, and the quality of the map's most valuable column
depends entirely on somebody answering honestly at that gate. A cartographer run with
nobody to ask should mark far more things `unverified` than feels comfortable.

**It maps what it can see.** Territories with a component behind an API, a login, or in
somebody's head will come back with a boundary card and a gap named in the catalog.
That is the correct output and it is still a partial map.

**It is bad at territories with no vocabulary.** The method leans on the territory's
own names. A codebase with meaningless names, or a folder tree with no conventions,
gives it very little to work with, and the map will be thinner than the territory
deserves.

**The noun ceiling is a real constraint.** Above roughly twenty-five nouns the catalog
stops being scannable and the map degrades toward an index. The instruction is to
narrow the territory, which means some bodies of work need three maps rather than one
big one. It will not tell you where the seams are. You have to decide that.

**It has no opinion about whether the territory is any good.** By design. A badly
designed system gets a clear map of a badly designed system. If you want the flaws
named, that is an auditor, and this is not one.

---

## Limits of the worked map in `map/`

**The cold walks were self-administered.** The cartographer wrote the map and then
walked it. That is the weakest form of the test and it is worth being blunt about what
it can and cannot show.

It **can** show a structural miss: walk 1 found a question with no door, and the
finding stands regardless of who ran it, because the door was either there or it was
not. It **cannot** show whether the language lands for someone who does not already
know the domain. The person walking already knew what a quote-to-order link was. A
genuine stranger walk, by a person or a model with no exposure to this territory, has
not been run and would probably find more.

**Row counts are as at the last rebuild.** They are in the map as scale, not as truth,
and are not maintained. If one matters to your work, query it.

**The map is redacted, and you should know exactly how.** The territory is a real
business that did not consent to publishing its internal structure. So:

| Redacted | How it appears |
|---|---|
| Real file paths | Role placeholders: `<records-kb>/`, `<scripts>/`, `<delivery>/` |
| The job-management system's name, and its report names | "the job system"; reports unnamed |
| Absolute row counts and record identifiers | Scale only, and only where a contrast depends on it |
| Client identities, rates, values, exact dates | Generalised to roles, or dropped |

**What is verbatim:** every ghost, every naming collision, every coverage bound, the
three ways an earlier inference-matching approach failed, and why the pricing golden
tests are supposed to break.

The honest caveat: **you cannot verify any of it.** You cannot open the sources the
cards cite. You are taking the traps on trust. Judge the map on whether its reasoning
is the shape of something lived rather than something invented, because that is the
only signal available to you here, and be appropriately sceptical.

The honest defence: `rules.md` section 6 already forbids a card from carrying values,
reproduced schema, or enough detail to rebuild the source. The redaction removed almost
nothing the rules permitted in the first place. A map that survives redaction was
obeying the rule. One that collapses was a photocopy.

**The map has a date and no maintenance promise.** It was walked in August 2026. Two
things in it are actively moving: a client-categorisation exercise was in flight, and
one folder-graduation rule is described two slightly different ways in two live
documents. Both are marked in place. Anything else that has drifted since is not
marked, because a map cannot know what happened after it was drawn.

**Two live tables are deliberately not carded.** Order lines and purchase orders. The
reasoning is in the catalog. If your work is supplier costs, this map is not sufficient
for you and you should say so rather than working around the gap.

---

## The failure mode to watch for

The map is most dangerous exactly where it is most useful: a reader consults it
**instead of** reading the source. That is what it is for. It also means a confident
wrong line will be believed and acted on by someone who has deliberately chosen not to
check.

Two defences, and neither is optional.

Every card names its source of truth and states that the source wins. When a card and
the file disagree, the card is wrong. Do not reconcile them in your head and proceed.

And the map is dated. Treat any card older than about six months as a claim about the
past rather than a description of the present. A map that is never re-walked becomes,
in time, the most authoritative-looking ghost in the territory.
