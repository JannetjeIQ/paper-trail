# Card types

The closed set. Six types. Every card is exactly one of them.

If a noun does not fit, it is one of three things: not a noun, two nouns wearing one
name, or a sign that the territory boundary is wrong. It is never a seventh type. Do
not add one.

---

## 1. `record`

A row shape. One instance per thing in the world.

Examples: a database table, an object type in a SaaS tool, a work-order type, a ticket.

Card must carry: the **join key** other records use to reach it, and any column whose
plain reading is wrong.

## 2. `store`

A container that holds records, and the thing that fills it.

Examples: a SQLite file, a base, a board, a warehouse table, a PST.

Card must carry: **how it is rebuilt or refreshed**, and **the window it covers**. A
store that covers 2024 onward will silently answer a 2019 question with zero rows.
Coverage is the single most misread property of a store.

## 3. `config`

A file read at run time whose values change behaviour.

Examples: a rates file, a mapping table, an env file, a threshold set, a template.

Card must carry: **who reads it** and **what drifts from it**. Configs breed copies.
The copy is the danger, so name it.

Never copy the values in. Cite the file.

## 4. `convention`

A rule about shape that both humans and scripts depend on, and which nothing enforces.

Examples: a folder naming pattern, a required member file, a status suffix, an
ordering rule.

Card must carry: **what breaks when it is not followed**, and **whether anything
checks**. Almost always nothing checks. Say so plainly. An unenforced convention is
the most common source of a leftover.

## 5. `process`

Something that moves data or work from one noun to another. Scheduled, triggered or
hand-run.

Examples: a sync script, a nightly job, a report build, a documented handoff between
two people.

Card must carry: **its trigger**, **what it reads**, **what it writes**, and whether a
human is in the loop. A process with a human step is not automated, however much of it
is code, and the later reader has to know where the human stands.

## 6. `boundary`

An edge where this territory hands off to a system you do not control.

Examples: an accounting package, a client portal, a supplier's system, an API you
consume, a person outside the team.

Card must carry: **what crosses**, **in which direction**, and **what is true on the
other side that is not true here**. Boundaries are where assumptions die. A figure that
means one thing inside and another thing outside belongs on a boundary card and in
`naming-collisions.md`.

Boundary cards are short. You are not mapping the other side. You are marking the wall
and naming the door.

---

## Card shape

Every card, every type, same skeleton.

### The line budget, and why it differs by type

| Card state | Budget |
|---|---|
| `live`, `leftover`, `unverified` | **62 lines** |
| `ghost` | **80 lines** |

Not a concession. A ghost card carries three things the others do not: the **search that
proved absence**, the **wrong conclusion** a reader reaches by trusting it, and the
**correct alternative** to send them to instead. That is structurally more content, and
squeezing it to the same length means dropping the evidence, which is the one part that
must never go.

The budget exists to stop a card becoming a chapter, not to hit a number. **If you find
yourself cutting evidence to fit, the budget is wrong and you should change it and say
so, rather than cut.** That is exactly what happened here: the first version of this file
set one figure for every card, three ghost cards broke it, and the honest fix was to
distinguish the states rather than gut the cards. `check_map.py` enforces both figures.

```markdown
# <exact name as it appears in the territory>

**Type:** record | store | config | convention | process | boundary
**State:** live | leftover | ghost | unverified
**Lives at:** <path or location>
**Source of truth:** <the file that wins if this card and it disagree>

## What it is
Two or three sentences. What it holds or does.

## Why it is shaped that way
The decision behind the shape. Where you know it, cite it. Where you do not, say
"reason not recorded". This is the field that makes a map worth more than the schema.

## Traps
Only the things whose plain reading is wrong. Nothing that is already obvious from
the source. If there are none, delete the section.

## Hits
- <noun> : <mechanism>

## Does not hit
- <the wrong neighbour> : <why not, one clause>
```

Delete any section that would be empty, except `Hits` and `Does not hit`. Those two
are always present, even when the answer is "nothing" or "no common wrong turn found".
An absent `Hits` reads as "not yet mapped". An explicit "nothing" reads as
"safe to move", which is the answer the reader came for.
