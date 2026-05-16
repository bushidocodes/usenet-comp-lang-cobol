[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ALLOCATE revisited

_5 messages · 3 participants · 2006-07_

---

### ALLOCATE revisited

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-05T10:46:14+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e8fu8p$re1$00$1@news.t-online.com>`

```
I am still having problems understanding this.
Consider :
ALLOCATE based-item-in-whatever-storage RETURNING pointer-1.
.....
ALLOCATE based-item-in-whatever-storage RETURNING pointer-2.

Are consecutive ALLOCATE's allowed without an intervening FREE ?
When yes, does the ALLOCATE return new storage or the previously
allocated storage ? (ie. In the example above is pointer-1 equal pointer-2?)

Roger
```

#### ↳ Re: ALLOCATE revisited

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-07-05T15:04:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ao3du9agpl2b5@corp.supernews.com>`
- **References:** `<e8fu8p$re1$00$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:e8fu8p$re1$00$1@news.t-online.com...
> I am still having problems understanding this.
> Consider :
…[4 more quoted lines elided]…
> Are consecutive ALLOCATE's allowed without an intervening FREE ?

Yes, even if the same based item is used for each allocation.

> When yes, does the ALLOCATE return new storage or the previously
> allocated storage ?

For this and all similar examples, new storage.

> (ie. In the example above is pointer-1 equal pointer-2?)

No. 'pointer-1' contains the address of the first allocation;
'pointer-2' and the implicit pointer for 'based-item-in-whatever-storage'
contain the address of the second allocation.
```

##### ↳ ↳ Re: ALLOCATE revisited

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-08T21:13:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2eVrg.13993$B62.635@fe07.news.easynews.com>`
- **References:** `<e8fu8p$re1$00$1@news.t-online.com> <12ao3du9agpl2b5@corp.supernews.com>`

```
To go a little farther,

If you coded:

    ALLOCATE based-item-in-whatever-storage RETURNING pointer-1.
    ALLOCATE based-item-in-whatever-storage RETURNING pointer-1.

with no statements in-between, the storage allocated by the first statement 
would be (almost) impossible ever to free.  You would get a second allocation 
and have "lost" the addressability to the first obtained storage.

(Or at least this is how I remember the definition).
```

###### ↳ ↳ ↳ Re: ALLOCATE revisited

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-07-10T09:57:22+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e8t19a$mcp$00$1@news.t-online.com>`
- **References:** `<e8fu8p$re1$00$1@news.t-online.com> <12ao3du9agpl2b5@corp.supernews.com> <2eVrg.13993$B62.635@fe07.news.easynews.com>`

```
Nice to see you back Bill.
Hope you had a nice time.

OK. Further clarification requested.
(Abbreviated syntax)
WORKING-STORAGE
01  MYFLD   PIC X  BASED.

ALLOCATE MYFLD INITIALIZED.

How do I FREE this ?
According to standard, I can't do a
FREE MYFLD.

"1) The data item referenced by data-name-1 shall be of category 
data-pointer."

Does this mean I have to :
FREE ADDRESS OF MYFLD

?

Roger

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:2eVrg.13993$B62.635@fe07.news.easynews.com...
> To go a little farther,
>
…[44 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: ALLOCATE revisited

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-07-10T16:28:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qevsg.105238$LI3.101170@fe12.news.easynews.com>`
- **References:** `<e8fu8p$re1$00$1@news.t-online.com> <12ao3du9agpl2b5@corp.supernews.com> <2eVrg.13993$B62.635@fe07.news.easynews.com> <e8t19a$mcp$00$1@news.t-online.com>`

```
That certainly looks like a "good way" to FREE it.  Otherwise, either use a 
RETURNING clause to the ALLOCATE or a Pointer to the BASED item.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
