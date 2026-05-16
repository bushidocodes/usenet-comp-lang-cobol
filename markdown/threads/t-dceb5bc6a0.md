[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu PowerCOBOL: Opinions re file access techniques

_2 messages · 2 participants · 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu PowerCOBOL: Opinions re file access techniques

- **From:** jgwolfe@netcom.ca (Gerry Wolfe)
- **Date:** 1999-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37d706d5.4339669@nntp.netcom.ca>`

```
Greetings... I've been a lurker for a while, and now have a few
questions

My background is about 30 years usage of COBOL and ASM, and 13 years
teaching at a local polyech/university.  I've used Fujitsu (r4) COBOL
in batch COBOL (*it's great*) and am now building a club management
system in PowerCOBOL to learn the PC aspects...

A few questions / requests for advice...

Q1: Tutorials show INVOKEs using MS/Access and SQL under a server
environment.  They are both ODBC-accessed -- is it safe to assume that
I could use SQL statements against a MS/Access database?

Q2: None of the PowerCOBOL tutorials address file access with the
traditional SELECT / FD / READ etc COBOL verbs.  Again, I assume this
is available???

Q3: What about the relative merits of the INVOKE vs SQL vs traditional
COBOL READ/WRITE access of data under PowerCOBOL.  I'm wondering about
"robustness",  control, performance etc.

Q4: Any suggestions on how to build an environment where the
application can define data file paths?  For example, it would be
great to provide a Tools|Preferences|DataFiles|Path approach for users
to identify where they would like to keep the data files.

Q5: Any suggestions on how to build a file environment that would make
it difficult for a user/client to access passwords etc. outside the
application?

advTHANKSance to those who have more experience...

rgds, G.
```

#### ↳ Re: Fujitsu PowerCOBOL: Opinions re file access techniques

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lwFB3.675$q%5.33870@typhoon01.swbell.net>`
- **References:** `<37d706d5.4339669@nntp.netcom.ca>`

```

Gerry Wolfe <jgwolfe@netcom.ca> wrote in message
news:37d706d5.4339669@nntp.netcom.ca...
>
> Q1: Tutorials show INVOKEs using MS/Access and SQL under a server
> environment.  They are both ODBC-accessed -- is it safe to assume
that
> I could use SQL statements against a MS/Access database?

Yes. If you have the MSA (or SQL or FoxPro or whatever) drivers.
>
> Q2: None of the PowerCOBOL tutorials address file access with the
> traditional SELECT / FD / READ etc COBOL verbs.  Again, I assume
this
> is available???

Sure. ISAM, Relative, Sequential, Line Sequential, etc.
One feature I like (coming from Realia COBOL) is file and record
locking for all file types.
>
> Q3: What about the relative merits of the INVOKE vs SQL vs
traditional
> COBOL READ/WRITE access of data under PowerCOBOL.  I'm wondering
about
> "robustness",  control, performance etc.

All the standard arguments apply: With SQL you can change
database orginazation or easily access the data with other
programs. Some programming techniques are easier with ODBC
techniques. With ODBC, there is a learning curve and, sometimes,
a performance penalty (though slight).
>
> Q4: Any suggestions on how to build an environment where the
> application can define data file paths?  For example, it would be
> great to provide a Tools|Preferences|DataFiles|Path approach for
users
> to identify where they would like to keep the data files.

The easiest way is during the installation of the resultant program
suite. Fujiusu provides a scaled-down version of InstallShield and
one of the parameters there asks the user for a destination. FJ
programs
and their associated run times are LARGE. One DLL in our suite is
approaching 2MB and so far we are up to about 30MB worth of
executable code for a POS/Inventory system. But that's normal for
a Windows application. Get a CD duplicator (I know where they
can be had for $2200 - the unattended kind. Does a stack of 50 at
up to 8X.).
>
> Q5: Any suggestions on how to build a file environment that would
make
> it difficult for a user/client to access passwords etc. outside the
> application?

Hash the password file.

Have fun.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
