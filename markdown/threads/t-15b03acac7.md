[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MVS Call Chain

_5 messages · 3 participants · 2000-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### MVS Call Chain

- **From:** "searcher" <mangogwr@bellsouth.net>
- **Date:** 2000-09-07T22:22:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3Yt5.4$ju4.3741@news2.mia>`

```
After 20 something years of programing, I've never NEEDED to know
the original 'load' module.  The Jobname/Number sometimes, but never
so far the first pgm.

Whatever is the reason?
```

#### ↳ Re: MVS Call Chain

- **From:** "John Cloughly" <jcloughly@earthlink.net>
- **Date:** 2000-09-08T15:18:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cr7u5.31876$C42.1407254@newsread2.prod.itd.earthlink.net>`
- **References:** `<a3Yt5.4$ju4.3741@news2.mia>`

```

"searcher" <mangogwr@bellsouth.net> wrote in message
news:a3Yt5.4$ju4.3741@news2.mia...
> After 20 something years of programing, I've never NEEDED to know
> the original 'load' module.  The Jobname/Number sometimes, but never
…[5 more quoted lines elided]…
>
Let's see 2000 minus 1979 = 21.  I got you beat by 1 year.  (LOL)

Most often I've seen this tactic used in assembler to fool batch programs
into being used by CICS.  Or, to switch parm areas depending on who's
calling.  In OO land this could be a entrance into the objects private code.

But this time is different...
First it's a Cobol only environment.  This particuar chain structure is used
by numerous root modules in a huge application.  The linkage is max out.
Now the client wants a new root to grab information only a module (x) levels
deep can supply.  They want to make the mod only to the specific module
which has the data.  They want the new code to execute only when the new
root module is used.  AND, they don't want to pass a switch or extra I/O for
a file to pass parms.  The only solution I've figured is to have the root
create a temp storage area.  The new code at module (x) deep will identify
the root and if it's a hit get the temp storage and fill it.  Again this
would be a no brainer in Assembler.
```

##### ↳ ↳ Re: MVS Call Chain

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-08T22:05:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8%gu5.5$ju4.3783@news2.mia>`
- **References:** `<a3Yt5.4$ju4.3741@news2.mia> <cr7u5.31876$C42.1407254@newsread2.prod.itd.earthlink.net>`

```
Consider using a data element or file that is 'GLOBAL'.

John Cloughly <jcloughly@earthlink.net> wrote in message
news:cr7u5.31876$C42.1407254@newsread2.prod.itd.earthlink.net...
>
> "searcher" <mangogwr@bellsouth.net> wrote in message
…[13 more quoted lines elided]…
> calling.  In OO land this could be a entrance into the objects private
code.
>
> But this time is different...
> First it's a Cobol only environment.  This particuar chain structure is
used
> by numerous root modules in a huge application.  The linkage is max out.
> Now the client wants a new root to grab information only a module (x)
levels
> deep can supply.  They want to make the mod only to the specific module
> which has the data.  They want the new code to execute only when the new
> root module is used.  AND, they don't want to pass a switch or extra I/O
for
> a file to pass parms.  The only solution I've figured is to have the root
> create a temp storage area.  The new code at module (x) deep will identify
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MVS Call Chain

- **From:** chipling@hotmail.com
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C78E3B.63894360@hotmail.com>`
- **References:** `<a3Yt5.4$ju4.3741@news2.mia> <cr7u5.31876$C42.1407254@newsread2.prod.itd.earthlink.net>`

```
John,

Why don't you do a search on your production source programs for the called
sub-module.

Rgds,
Chip Ling

John Cloughly wrote:

> "searcher" <mangogwr@bellsouth.net> wrote in message
> news:a3Yt5.4$ju4.3741@news2.mia...
…[24 more quoted lines elided]…
> would be a no brainer in Assembler.
```

###### ↳ ↳ ↳ Re: MVS Call Chain

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T1Tx5.171$5p.2058@news2.mia>`
- **References:** `<a3Yt5.4$ju4.3741@news2.mia> <cr7u5.31876$C42.1407254@newsread2.prod.itd.earthlink.net> <39C78E3B.63894360@hotmail.com>`

```
I posted a response about two weeks back, but my DSL ISP (who I'm dropping)
has had big problems.

I had suggested, using an EXTERNAL or GLOBAL data item.



<chipling@hotmail.com> wrote in message
news:39C78E3B.63894360@hotmail.com...
> John,
>
> Why don't you do a search on your production source programs for the
called
> sub-module.
>
…[17 more quoted lines elided]…
> > Most often I've seen this tactic used in assembler to fool batch
programs
> > into being used by CICS.  Or, to switch parm areas depending on who's
> > calling.  In OO land this could be a entrance into the objects private
code.
> >
> > But this time is different...
> > First it's a Cobol only environment.  This particuar chain structure is
used
> > by numerous root modules in a huge application.  The linkage is max out.
> > Now the client wants a new root to grab information only a module (x)
levels
> > deep can supply.  They want to make the mod only to the specific module
> > which has the data.  They want the new code to execute only when the new
> > root module is used.  AND, they don't want to pass a switch or extra I/O
for
> > a file to pass parms.  The only solution I've figured is to have the
root
> > create a temp storage area.  The new code at module (x) deep will
identify
> > the root and if it's a hit get the temp storage and fill it.  Again this
> > would be a no brainer in Assembler.
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
