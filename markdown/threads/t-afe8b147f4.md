[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Please Help me

_2 messages · 2 participants · 2001-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Please Help me

- **From:** "Paulo Pinto" <ct1ete@mail.telepac.pt>
- **Date:** 2001-02-03T16:36:21
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95hcfc$jbm$1@venus.telepac.pt>`

```
Hi all,

I have some applications developed under COBOL Workbench 3.4.3 and I would
like to change to a new product because it's going to be discontinued.

1) What do you recommend me ??
2) I've been told about NETEXPRESS (what do you think?)

If I choose Netexpress do I need to change the programs ??

How about the runtime costs ?????

Thanks in advance

Paulo Pinto
ct1ete@mail.telepac.pt
```

#### ↳ Re: Please Help me

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-04T09:34:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A7D2214.DFCF3CD6@Azonic.co.nz>`
- **References:** `<95hcfc$jbm$1@venus.telepac.pt>`

```
> 
> I have some applications developed under COBOL Workbench 3.4.3 and I would
> like to change to a new product because it's going to be discontinued.

That doesn't mean that your copy will stop working.

> 1) What do you recommend me ??
> 2) I've been told about NETEXPRESS (what do you think?)
> 
> If I choose Netexpress do I need to change the programs ??

3.4 creates programs for DOS, OS/2 (16 bit) and Windows 3.x.  Netexpress
is for Windows 95 and NT (and later) only.  It will produce console apps
that look like DOS, but if yopu need DOS or Win 3.x then you won't
change.

Windows API programs will require conversion.  DOS based ADIS programs
will only require changes if you have used DOS specific routines (such
as CALL x"84") or other DOSisms.
 
> How about the runtime costs ?????

With 3.4 you can produce free distributable programs as long as you
follow the list in the book.

With NetExpress you must buy run-times or application-servers (or
whatever they call them.  There is supposed to be a way around this if
you ask nicely and are a small company.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
