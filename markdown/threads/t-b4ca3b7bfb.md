[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# newbees question

_2 messages · 2 participants · 1999-04_

---

### newbees question

- **From:** "Camp David" <dvdwaaij@advantage.nl>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7eo106$c1@news3.euro.net>`

```
L.S.

Is there anybody who can explain why I need to Bind a Package and Bind a
Plan after that .
What happens with the Database (DB2), DBRM and the LOAD when you bind the
Package?
What happens with the Database (DB2), DBRM and the LOAD when you bind the
Plan?

TXS,

David
```

#### ↳ Re: newbees question

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3710B398.887AB9B9@zip.com.au>`
- **References:** `<7eo106$c1@news3.euro.net>`

```
Camp David wrote:
> 
> L.S.
…[6 more quoted lines elided]…
> Plan?


When the DB2 precompiler goes through your program it extracts the
actual SQL used and leaves behind some magic numbers for DB2's
reference.  One of these critical numbers is the timestamp to ensure
that they match (and they often don't :-) )

Once the compile is sucessfuly (generally) the DBRM is copied into DB2
into a table with all the references.  It also optionally can check the
database for the optimal way to execute these statements and generate
'optimised' sql (my term).  If you do not run RUNSTATS first the
optimisation result will not be right!

The other things you should check are packages.  It allows multiple
versions of the program to be active.  This is handy if you want to run
the production compile and the development compile versions without
having to rebind all the time.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
