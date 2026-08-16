# The customer pricing band

**Type:** record field
**State:** **ghost**, empty field
**Lives at:** a markup-percentage band on the customer record in the job system
**Source of truth:** the standing house rule that declares it defunct

## What it is

A field on every customer record holding a percentage, presented as that client's
governing gross-profit markup band. It looks exactly like the answer to "what margin do
we work at for this client".

It is defunct. It has been for long enough that nobody remembers it being used.

## What a reader will conclude if they trust it

That pricing is governed per-client by a stored percentage, and therefore that pricing
questions are answered by reading a customer record.

They would then either quote from a number nobody has maintained, or, worse, build
tooling that reads it. Both produce prices that are wrong in a way that is very hard to
trace afterwards, because the number came from the system and looked official.

## Where pricing actually comes from

[rates.json](rates-json.md), applied by [engine.js](engine-js.md), with commercial
judgement on top. Minimum margins are held as policy in the rates file, split by one-off
versus repeat work. They are a floor, applied at the job, not a per-client band.

## Why it is worth a card at all

Because it is the purest example of the category in this territory. It is a populated
field, on a live record, in a live system, that means nothing. There is no error, no
null, no warning. The only thing standing between a reader and a wrong price is
somebody having written down that the field is dead.

That sentence is the entire value of a map.

## Hits

- Nothing. Nothing reads it and nothing writes it.

## Does not hit

- **Pricing.** Despite being, by name and by placement, the most pricing-looking field
  in the whole territory.
