[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# split keys

_4 messages · 3 participants · 1998-08_

---

### Re: split keys

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35E62D0C.38D02B64@siber.com>`
- **References:** `<6rumus$4pm$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-qXUCdE5UDsVx@Dwight_Miller.iix.com> <6rva41$glq@dfw-ixnews10.ix.netcom.com> <6rveus$svn$1@news.igs.net> <6s07a0$hcj@sjx-ixn1.ix.netcom.com> <6s146o$imt$1@news.igs.net>`

```
Donald Tees wrote:
> 
> >ALTERNATE RECORD KEY IS record-key-name-1
…[6 more quoted lines elided]…
> standard (as outlined above), and could not get it to work.  

The really correct way to convert split keys 
is to replace split key with a list of its components
everywhere where its encountered.

All Fujitsu statements that might potentially take
a split key (READ and START) take the list of keys,
not just one key. I think this is a standard extension
by Fujitsu specifically designed to handle "unsplit" split
keys.

Example:

You have C-KEY = KEY-1 KEY-2 in your file definition
         READ ... KEY IS C-KEY

Replace "C-KEY = KEY-1 KEY-2" with "KEY-1 KEY-2" in the file
definition
and replace "C-KEY" with "KEY-1 KEY-2" in the READ
statement.

By the way, mf2fsc can do this work for you automatically.

You can download evaluation copy from
http://www.siber.com/sct/tools/mf2fsc/

Vadim Maslov
```

#### ↳ Re: split keys

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6s77fh$r93@sjx-ixn2.ix.netcom.com>`
- **References:** `<6rumus$4pm$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-qXUCdE5UDsVx@Dwight_Miller.iix.com> <6rva41$glq@dfw-ixnews10.ix.netcom.com> <6rveus$svn$1@news.igs.net> <6s07a0$hcj@sjx-ixn1.ix.netcom.com> <6s146o$imt$1@news.igs.net> <35E62D0C.38D02B64@siber.com>`

```

Vadim Maslov wrote in message <35E62D0C.38D02B64@siber.com>...
   <snip>
>All Fujitsu statements that might potentially take
>a split key (READ and START) take the list of keys,
…[3 more quoted lines elided]…
>

  This approach is neither Standard nor is it portable to other COBOLs.  Nor
is it the approach that will work with the draft of the next COBOL Standard.
This doesn't mean you shouldn't use it today - for Fujitsu - but it
significantly farther away from what will be Standard (in the next Standard)
than the Micro Focus approach.
```

##### ↳ ↳ Re: split keys

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 1998-08-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35E72623.D50CD7DC@siber.com>`
- **References:** `<6rumus$4pm$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-qXUCdE5UDsVx@Dwight_Miller.iix.com> <6rva41$glq@dfw-ixnews10.ix.netcom.com> <6rveus$svn$1@news.igs.net> <6s07a0$hcj@sjx-ixn1.ix.netcom.com> <6s146o$imt$1@news.igs.net> <35E62D0C.38D02B64@siber.com> <6s77fh$r93@sjx-ixn2.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Vadim Maslov wrote in message <35E62D0C.38D02B64@siber.com>...
…[11 more quoted lines elided]…
> than the Micro Focus approach.

What I meant to say here, is:

This is a non-stnadard extension of the standard
which helps Fujitsu to address the split key problem.

Whether deviating from standard is good or bad,
I don't know. Deviating from the standard certainly 
helped Micro Focus by making their programs 
difficult to migrate to other compilers.

Vadim Maslov
```

##### ↳ ↳ Re: split keys

- **From:** Tom Morrison <t.morrison@liant.com>
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EAABF4.BF241E46@liant.com>`
- **References:** `<6rumus$4pm$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-qXUCdE5UDsVx@Dwight_Miller.iix.com> <6rva41$glq@dfw-ixnews10.ix.netcom.com> <6rveus$svn$1@news.igs.net> <6s07a0$hcj@sjx-ixn1.ix.netcom.com> <6s146o$imt$1@news.igs.net> <35E62D0C.38D02B64@siber.com> <6s77fh$r93@sjx-ixn2.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Vadim Maslov wrote in message <35E62D0C.38D02B64@siber.com>...
…[12 more quoted lines elided]…
> than the Micro Focus approach.

One possible way of "staying standard" would be to use a (possibly
large) REPLACE statement which would allow one to code standard I/O
statements in the procedure division, thereby isolating the nonstandard
damage to the SELECT statement, which are usually in copybooks.  Beware
of the scope rules on the REPLACE statement, however.

When Fujitsu later supports the standard, or you wish to change compiler
vendors, you should be able to remove the REPLACE statement, edit the
SELECT statement copybooks, and be done.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
