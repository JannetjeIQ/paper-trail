# Rules

How you map. These are constraints, not suggestions. If a rule and a nice-looking map
disagree, the rule wins.

---

## 1. Inventory before cards

You do not write a single card until you can answer, out loud, for the whole
territory:

- What are the nouns?
- Which of them are dead?

If you start writing cards during the walk, you will card whatever you happen to open
first, and the map will be shaped by your reading order rather than by the territory.

The inventory is a flat list: name, where it lives, one clause on what it is, and a
state guess. It is disposable. Its only job is to force the second question before
you commit prose to the first.

**Gate:** show the inventory and the state split to the human before writing cards.
State is the one thing you will get wrong from the outside, and it is the one thing
that is expensive to get wrong.

---

## 2. What counts as a noun

A noun earns a card if **something else in the territory depends on it by name**.

That is the whole test. Not "is it important", not "is it big". Dependency by name.

Nouns are usually one of:

- A **record type** (a table, an object, a row shape)
- A **file that is read by something** (a config, a rate sheet, a template)
- A **folder with a convention** (a naming rule, a required member file)
- A **process that produces or consumes the above** (a script, a scheduled job, a
  handoff)

Not nouns:

- **Instances.** One client folder is not a noun. The convention that all client
  folders follow is.
- **Adjectives.** "Legacy", "active", "v2". These are states, and states go on the
  card of the thing they describe.
- **The territory itself.** The catalog covers that. A card for the whole territory is
  a brochure.
- **Anything with no inbound dependency.** If nothing names it, the later reader will
  never arrive at it, and a card nobody arrives at is weight.

**Ceiling.** If you have more than about twenty-five nouns, you have either taken too
wide a territory or you are carding instances. Split the territory or raise the
altitude. A catalog a reader has to scroll is a catalog they will skim, and a skimmed
catalog sends them to the wrong card.

---

## 3. What counts as a movement

A movement is a **named, traceable dependency** between two nouns. One of:

| Movement | Meaning |
|---|---|
| `feeds` | A writes data that B reads |
| `joins on` | A and B are linked by a specific key. Name the key |
| `reads` | A consumes B at run time and would change behaviour if B changed |
| `graduates to` | An instance of A becomes an instance of B, and stops being A |
| `supersedes` | A replaced B. B may still exist |
| `asserts about` | A makes a claim about B that is not enforced by anything |

`asserts about` is the most useful and the most often missed. Documentation, a README,
a convention in a CONTEXT file: these all assert, and nothing stops them going stale.
An assertion is a movement because the later reader will act on it.

**Every movement must be traceable.** You must be able to point at the line of code,
the column name, the config key or the sentence that creates it. If you cannot, it is
not a movement, it is your inference, and it does not go on the map.

---

## 4. Live, leftover, ghost

Every card carries exactly one state in its header. This is the highest-value line in
the map and the easiest one to fake.

### Live
Something reads it or writes it now, and you can point at what.
Evidence: a script that opens it, a query that selects it, a folder created against
its convention this quarter, a scheduled job.

### Leftover
Real, still present, no longer the path. Superseded but not removed.
Evidence: a successor exists and is live, and the leftover still resolves.
**Leftovers are honest.** They are not errors. Say what replaced them and whether
anything still reads them, because something usually does.

### Ghost
A name with no wiring. It resolves, it looks like an object, nothing is behind it.

Ghosts come in three shapes, and you should name which:
- **Empty field.** A column or setting that exists and is never maintained. It will
  return values. The values mean nothing.
- **Removed target.** A name still referenced by something that no longer exists.
- **Never-built.** A name from a plan that was written down and not implemented.

**Ghosts are tripwires.** They do not look dead from the inside. A ghost field returns
a number, and the later reader will report that number. Mark the ghost, and on the card
say **what a reader will conclude if they trust it**, because that conclusion is the
actual damage.

### The default
When you cannot evidence a state, mark it **`state: unverified`** and say what evidence
would settle it. Do not guess.

Guessing `live` is the worst failure available to you: the reader builds against a
wish. Guessing `ghost` is the second worst: the reader deletes something load-bearing.
`unverified` costs the reader one check. Say what to check.

---

## 5. Hits and Does not hit

Every card carries both. A card without them is a glossary entry.

**Hits.** If the reader changes this noun, what else moves. Each entry names the other
noun and the mechanism, in that order. Not "affects reporting". Rather: "`orders`
rebuild, because the loader reads this column by name at build time."

If a change hits nothing, write **`Hits: nothing.`** That is a real and valuable answer.
It tells the reader they can move.

**Does not hit.** The obvious next noun that is the **wrong** one. This is the line
that makes the map worth more than the source.

Choose it by asking: *what would a competent reader assume is attached here, and be
wrong about?* Usually it is:

- A **name collision.** Something that shares a word with this noun and is unrelated.
- A **broken chain.** The link they expect exists but the data does not flow.
- A **stale successor.** They will reach for the old thing because it is better known.

Name it, and say **why** it does not hit in one clause. Without the why, the reader
assumes you were careless.

If nothing plausible is a wrong neighbour, write **`Does not hit: no common wrong
turn found.`** Do not invent one to fill the field. A manufactured wrong neighbour
teaches a false boundary.

---

## 6. Cite the source. Never copy it

A card **points**. It does not contain.

Cite with a path, and where it helps, a line or a symbol. The card says what the thing
is, why it is shaped that way, and what it touches. The **source** says what it
currently does.

**When the card and the source disagree, the source wins and the card is wrong.**
Say that on the card, in the card's own words, so the reader knows the direction of
authority without being told twice.

You must **not** put into a card:

- Values that change: rates, prices, thresholds, credentials, current row counts as
  fact. (Row counts as **scale**, "about 24,000", are fine and useful. Row counts as
  **truth** go stale in a week.)
- Reproduced code, schemas or config. Cite the file.
- Full column lists where the shape is the point rather than the columns. Cite the
  data dictionary and name only the columns that carry a trap.

Test: **if the source file were deleted, would the card still let someone rebuild it?**
If yes, you wrote a photocopy. Cut it back.

---

## 7. Do not slurp the shelves

You are also bound by the walking rule you are writing for others.

While mapping, open what you need to establish a noun, a movement or a state, and no
more. You do not need to read every file to map the territory. You need to read enough
to place it.

When you cannot establish something within a reasonable number of looks, **stop and
ask**, or mark it `unverified`. Do not keep opening files hoping the answer appears.
Silent churn is how a map turns into a photocopy: you end up having read everything,
and so you write everything.

The map's whole promise is that nobody has to eat the tree. You do not get an
exemption.

---

## 8. Two hops, then stop

The catalog names the noun. The card explains it. That is two hops, and it is the
budget.

If answering "what is X" requires the catalog, then a card, then another card, the
map has failed. Fix it by moving the needed line onto the first card, not by telling
the reader to read both.

Cross-links between cards are for **what else moves**, not for **what this is**. A
card that cannot stand alone is a chapter.

---

## 9. Write in the territory's own words

Use the names that appear in the source: the real table names, the real column names,
the real folder names, the real filenames. Do not improve them, do not normalise
casing, do not rename to something clearer.

The reader will search for the string they saw. If your map calls it something nicer,
they will not find it, and worse, they will believe there are two things.

Where the territory's own name is genuinely ambiguous, that is a **collision**, and it
goes in `reference/naming-collisions.md`. Record it. Do not resolve it by inventing a
third name.

---

## 10. Never fabricate

Every claim on every card traces to something you actually saw.

If you did not see it, you have three honest moves: mark it `unverified`, name it as a
gap in the catalog, or ask. You do not have a fourth.

This matters more here than in most work, because a map is consumed by readers who
have deliberately chosen not to check. That is what a map is for. A confident wrong
line in a card will be believed and acted on, and the reader has no way to catch it,
because catching it would mean reading the thing the map exists to spare them.

A gap you name costs the reader one lookup. A gap you fill costs them the wrong build.
