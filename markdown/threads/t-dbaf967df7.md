[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SYSLIB - Cannot locate copybook

_3 messages · 2 participants · 2000-09_

---

### SYSLIB - Cannot locate copybook

- **From:** patrick_finnegan@my-deja.com
- **Date:** 2000-09-06T15:25:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p5nk3$mfi$1@nnrp1.deja.com>`

```


We are moving a COBOLII mainframe application to to AIX.  The AIX IBM
compiler cannot find copy libraries unless the file names are qualified
with full extensions.

e.g

 COPY ig14700.         >   not found

 COPY "ig14700.cpy".   >   found

Both statements use the same compile SYSLIB which is defined as:

export SYSLIB=/ultd/app/pfs/r431cib/XTOR/COBCOPY
export SYSLIB=$SYSLIB:/ultd/app/pfs/r431cib/COBCOPY
export SYSLIB=$SYSLIB:/ultd/app/pfs/r431cib/SQLCOPY
export SYSLIB=$SYSLIB:/usr/lpp/cics/include

We can run the code through a rexx script to generate the quotes plus
filename extensions but is this really necessary?

The IBM compiler is 1.1.1.2 running on AIX 4.3.3.13.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: SYSLIB - Cannot locate copybook

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-06T11:49:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p5sip$ung$1@nntp9.atl.mindspring.net>`
- **References:** `<8p5nk3$mfi$1@nnrp1.deja.com>`

```
What is your COBCPYEXT environment variable set to?  Also, is your file
really defined with a "cpy" and not "CPY" extension?  I know that UNIX-like
systems are often case sensitive, and this COULD be your problem.
```

##### ↳ ↳ Re: SYSLIB - Cannot locate copybook

- **From:** patrick_finnegan@my-deja.com
- **Date:** 2000-09-07T17:20:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p8ioq$26n$1@nnrp1.deja.com>`
- **References:** `<8p5nk3$mfi$1@nnrp1.deja.com> <8p5sip$ung$1@nntp9.atl.mindspring.net>`

```
We had already the checked that the library names matched the
literals.  The problem was caused by the IBM Cobol compiler resolving
literals to upper case e.g  call copy1 gets resolved to COPY1 but the
file name is copy1.cpy.  I changed the copy file names to uppercase and
everything worked ok.  So now call copy1 gets resolved to COPY1 which
matches COPY1.cpy



In article <8p5sip$ung$1@nntp9.atl.mindspring.net>,
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> What is your COBCPYEXT environment variable set to?  Also, is your
file
> really defined with a "cpy" and not "CPY" extension?  I know that
UNIX-like
> systems are often case sensitive, and this COULD be your problem.
>
…[7 more quoted lines elided]…
> > We are moving a COBOLII mainframe application to to AIX.  The AIX
IBM
> > compiler cannot find copy libraries unless the file names are
qualified
> > with full extensions.
> >
…[13 more quoted lines elided]…
> > We can run the code through a rexx script to generate the quotes
plus
> > filename extensions but is this really necessary?
> >
…[7 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
