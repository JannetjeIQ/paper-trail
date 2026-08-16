# Walk order

The order of the walk, and the gates between steps. Do not reorder. Each step exists
because doing it later produces a specific failure, named below.

---

## Step 0. Take the edge

Before opening anything, get the boundary in writing:

- Which folder, records or system is in scope
- Who the later reader is, and whether they are a model
- What they will be about to change when they arrive

**Gate:** if the edge is "the whole business" or "our systems", stop and narrow it.

*Skipped it? You will map for two hours and produce a catalog with no stopping
condition, which is a brochure.*

---

## Step 1. Read the front doors only

Open the things the territory offers a newcomer: the root README, the CONTEXT or
CLAUDE file, the index, the schema doc, the folder listing at depth one.

Do not open leaf files yet.

You are looking for two things: the **claimed** shape, and the **names**. You are not
yet believing any of it.

*Skipped it? You will discover the territory's vocabulary halfway through and rename
everything, which is rule 9 broken.*

---

## Step 2. Inventory the nouns

Flat list. Name, location, one clause, provisional type, provisional state.

Include anything the front doors named, plus anything you saw that they did not name.
The gap between those two sets is the most productive thing on the walk. A front door
that names something no longer there has given you a ghost. A directory holding
something no front door names has given you either a leftover or an undocumented live
object, and you must find out which.

**Gate:** apply the noun test from `rules.md` section 2. Cut instances. Cut anything
nothing depends on by name. If more than about twenty-five survive, the edge is too
wide. Go back to step 0.

*Skipped it? You card whatever you opened first.*

---

## Step 3. Establish state, with evidence

For each surviving noun, find the thing that proves it live: the script that reads it,
the query that selects it, the job that writes it, the recent instance built against
it.

Cannot find one? Do not promote a guess. Mark it `unverified` and record what would
settle it. Then look specifically for supersession: a newer noun doing the same job.
If you find one, the old noun is a **leftover**. If you find nothing behind the name at
all, it is a **ghost**, and you name which of the three ghost shapes it is.

**Gate: show the human the state split before writing any card.**

This is the only mandatory human checkpoint in the walk. State is what you are most
likely to get wrong from outside and what is most expensive to get wrong. The person
who owns the territory can settle in one sentence what would take you twenty file
opens, and they are the only one who knows which of the plans on the shelf were ever
built.

*Skipped it? A wish gets mapped as live, and the next reader builds against a world
that does not exist. This is the failure the whole form is designed to prevent.*

---

## Step 4. Trace the movements

For each pair of nouns, ask: does one feed, join, read, graduate to, supersede or
assert about the other? Name the key, the column, the line or the sentence that makes
it true.

Movements you cannot point at do not exist. Drop them.

*Skipped it? `Hits` becomes vague, and a vague `Hits` is worse than none: it reads as
checked when it was assumed.*

---

## Step 5. Find the collisions

Sweep the noun list for words that appear in more than one place meaning more than one
thing. Same column name in two tables. Same word for a record and a folder. A word
whose plain-English meaning differs from its meaning here.

Write them into `reference/naming-collisions.md` before you write cards. The
collisions decide half your `Does not hit` lines.

*Skipped it? You write a glossary. The reader takes the wrong door confidently.*

---

## Step 6. Write the catalog first

One row per noun: name, type, state, one clause, and the question that should send a
reader to it.

The last column is the one people forget and the one the reader actually uses. A cold
model does not scan for "the noun I need". It scans for "the question I am holding".

**Gate:** can a stranger find the front door from this alone? If the catalog needs a
paragraph of preamble to make sense, the rows are not carrying enough.

---

## Step 7. Write one card per noun

Follow the card shape in `reference/card-types.md`. Cite, do not copy. Fill `Hits` and
`Does not hit` on every card, including the ones where the answer is "nothing".

Write them in catalog order so you notice duplication. Two cards that keep referring
to each other for basic identity are one noun, or a two-hop violation. Fix at the card,
not with a cross-link.

---

## Step 8. Walk it cold

Take three questions the later reader will actually arrive with. Answer each using
**only** the catalog and one card.

Record what happened, including the failures. If a question took three cards, or
landed on the wrong one, the map is wrong. Fix the map and say in the record what you
changed.

A map that has never been walked cold is a draft. Publishing the cold walk, failures
included, is the difference between claiming it works and showing it.

*Skipped it? You shipped a map that only works for the person who drew it, which is
the one thing it was for.*
