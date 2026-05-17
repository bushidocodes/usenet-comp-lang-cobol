[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accessing progress database via cobol

_3 messages · 3 participants · 1998-07_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Accessing progress database via cobol

- **From:** "h. blakely williford" <ua-author-9633586@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35B63768.372D3416@NOSPAM.fuller.com>`

```
Hello World!

We inherited an AIX system running progress and would like to read the
database through the cobol language. The cobol compiler that is on the
aix box is acucobol 3.2gl. If we need to use a different cobol compiler
we are open to that.

We've talked with acucobol and they sent us some product for the PC --
to act as a "gate way" between cobol and progress -- odd because we
don't need a PC to do this on our mvs system.

There is 'somthing' on this same PC that allows Windows-9x programs to
access the Progress data. My guess is that there is another product on
the aix system to talk back to the PC. Is this what an 'odbc' driver
is?

Note that what we need to do is best done in cobol not in the PC tools.

As I said we've done this before on our mvs system reading and writting
to our idms data base so we know that it is possable; or is this
somthing that just can not be done with so called modern tools?

Any comments, help, flames (not too hot), are welcome; as the persons
that we inherited this system from are not telling us anything.

Thank you for your time.
```

#### ↳ Re: Accessing progress database via cobol

- **From:** "wolfgang grossbauer" <ua-author-12437406@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cccca3b840-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35B63768.372D3416@NOSPAM.fuller.com>`
- **References:** `<35B63768.372D3416@NOSPAM.fuller.com>`

```
Hi Blakely,
I have a common usable COBOL interface to access PROGRESS (and ORACLE
and INFORMIX). It is running under UNIX SVR5 (I guess AIX is kinda UNIX?)
and is linked to the MicroFocus COBOL runtime system.
You define a control-file (TCSDBS.TAB) which contains the names of the RDBMS
tables. The system then knows if to access PROGRESS or COBOL file. There are
some more things to do but basically that's it.
This interface is part of a system, called TCS, to operate mainframe apps on
UNIX.

Wolfgang Grossbauer
MAGRO Salzburg
```

##### ↳ ↳ Re: Accessing progress database via cobol

- **From:** "geoff" <ua-author-7004835@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cccca3b840-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cccca3b840-p2@usenetarchives.gap>`
- **References:** `<35B63768.372D3416@NOSPAM.fuller.com> <gap-cccca3b840-p2@usenetarchives.gap>`

```
In article <35b··0@new··c.at>, "Wolfgang Grossbauer" wrote:
› Hi Blakely,
›    I have a common usable COBOL interface to access PROGRESS (and ORACLE
…[6 more quoted lines elided]…
› UNIX.

But you're leaving out details here. What way does the COBOL get
to the Progress database? Have you written HLC calls and probuild
a new executable? Are you using ESQL? It's not quite as easy
as you make out because you need to take a lot of time to make that
interface.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
