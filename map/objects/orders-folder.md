# orders/&lt;slug&gt;/

**Type:** convention
**State:** live
**Lives at:** `<delivery>/orders/`
**Source of truth:** `<delivery>/orders/CONTEXT.md`

## What it is

One folder per won job that needs working files: client artwork, signed purchase
orders, drawings, site photos, call notes. A short working slug for a name. A handful
exist.

Folders arrive here from [quoting](quoting-folder.md) when a quote is accepted, or
directly when a job opens with no prior quote-staging folder.

## Why it is shaped that way

**There is no graduation step out.** Folders stay here through the full delivery
lifecycle and remain after the job closes. There is no live-versus-archived move in
this workspace at all. That is a deliberate choice: the alternative is a second
convention about when something is finished, and finishing is exactly the thing nobody
maintains.

The consequence is that presence in this folder means "this job had working files at
some point", and nothing else. It is not a work-in-progress list, and it must not be
read as one.

## Traps

- **This is not the delivery pipeline.** A handful of folders against tens of thousands of
  order records. The overwhelming majority of jobs never get a folder because they
  never needed one.
- Nothing enforces the convention or prunes it. An old closed job and a live one look
  identical from the outside. The `CONTEXT.md` inside is the only thing that will tell
  you which is which, and only if someone kept it current.
- Safety documentation for a job lives in a **separate** folder tree keyed by job,
  not inside this one. Following the folder alone will miss it.

## Hits

- [quoting/&lt;end-client-slug&gt;/](quoting-folder.md) : the upstream source of most of these folders.
- The linked safety-documentation pack, where one exists.

## Does not hit

- **[orders](orders.md), the record.** Same word, different thing, wildly different
  population. Creating a folder does not create an order and deleting one does not
  touch a record. If you want to know what the business sold, you want the table. If
  you want the signed purchase order for one specific job, you want the folder.
- **Any status.** The folder carries no state. A job's status lives on the record.
