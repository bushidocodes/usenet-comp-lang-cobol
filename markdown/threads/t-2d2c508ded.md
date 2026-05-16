[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to use a subprogram with cics extension in an non-cics batch program.

_5 messages · 5 participants · 1999-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Re: How to use a subprogram with cics extension in an non-cics batch program.

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%XF74.6793$Ld6.56617@typhoon.columbus.rr.com>`
- **References:** `<KQ654.1366$b67.9115@news1.online.no> <8332av$o13$1@nntp4.atl.mindspring.net>`

```
>If you subprogram has EXEC CICS statements in it, then you cannot use it in
>batch.


Incorrect. As long as the CICS commands are not referenced in the subprogram
it will work just fine. Either way, compile it, run it, and check the
results.
```

#### ↳ Re: How to use a subprogram with cics extension in an non-cics batch program.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83obhi$9r2$1@nntp1.atl.mindspring.net>`
- **References:** `<KQ654.1366$b67.9115@news1.online.no> <8332av$o13$1@nntp4.atl.mindspring.net> <%XF74.6793$Ld6.56617@typhoon.columbus.rr.com>`

```

Gumbo <a@a.com> wrote in message
news:%XF74.6793$Ld6.56617@typhoon.columbus.rr.com...
> >If you subprogram has EXEC CICS statements in it, then you cannot use it
in
> >batch.
>
>
> Incorrect. As long as the CICS commands are not referenced in the
subprogram
> it will work just fine. Either way, compile it, run it, and check the
> results.
>
>

You darn well better TRANSLATE it before you compile it - unless you have a
compiler that understands "EXEC CICS ... END-EXEC" as "COBOL syntax".
```

#### ↳ Re: How to use a subprogram with cics extension in an non-cics batch program.

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38602F64.89A359B2@techie.com>`
- **References:** `<KQ654.1366$b67.9115@news1.online.no> <8332av$o13$1@nntp4.atl.mindspring.net> <%XF74.6793$Ld6.56617@typhoon.columbus.rr.com>`

```
And you better look at how it gets called!  CICS translator sticks
a extra parameters in front of those you have for the PROCEDURE
DIVISION.  You batch caller won't.

Gumbo wrote:
> 
> >If you subprogram has EXEC CICS statements in it, then you cannot use it in
…[4 more quoted lines elided]…
> results.
```

##### ↳ ↳ Re: How to use a subprogram with cics extension in an non-cics batch program.

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385FD77A.C94623D5@worldnet.att.net>`
- **References:** `<KQ654.1366$b67.9115@news1.online.no> <8332av$o13$1@nntp4.atl.mindspring.net> <%XF74.6793$Ld6.56617@typhoon.columbus.rr.com> <38602F64.89A359B2@techie.com>`

```
Jared Thomas wrote:
> 
> And you better look at how it gets called!  CICS translator sticks
> a extra parameters in front of those you have for the PROCEDURE
> DIVISION.  You batch caller won't.

But it could. Been there, done that. I think this is the same thread on
which I had some private email with the poster. He's got too many CICS
functions, e.g., WRITEQ TS, READQ TS, ENQ. to make one source run in
both environments. The best advice I've seen is to write two drivers,
one for each environment, which call a 3th program which does all the
work. As always, YMMV.

Bill Lynch
```

###### ↳ ↳ ↳ Re: How to use a subprogram with cics extension in an non-cics batch program.

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.12ca9dcd1f02b989989693@news.transport.com>`
- **References:** `<KQ654.1366$b67.9115@news1.online.no> <8332av$o13$1@nntp4.atl.mindspring.net> <%XF74.6793$Ld6.56617@typhoon.columbus.rr.com> <38602F64.89A359B2@techie.com> <385FD77A.C94623D5@worldnet.att.net>`

```
In article <385FD77A.C94623D5@worldnet.att.net>, wblynch@worldnet.att.net 
says...
> Jared Thomas wrote:
> > 
…[12 more quoted lines elided]…
> 

When possible, we now write our subroutines as DB2 stored procedures.  
They can be called from both batch and online via the "SQL CALL" 
instruction.

Pete
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
