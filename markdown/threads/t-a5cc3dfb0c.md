[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Overriding 01 level

_4 messages · 4 participants · 1998-07_

---

### Overriding 01 level

- **From:** "Alp" <alonp@cry-sys.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ofsc2$5bo$1@lnews.actcom.co.il>`

```
Hi all,

I'd like to know if there is a MF COBOL II compiler option to override an 01
level
within a copy book.

for example:

01 MYCOPY.   COPY COPYB.

COPYB contains the following statement:
01 EMP.
 03 ....

This syntax was possible in COBOL VS but not in COBOL II


Thanks in advance

Alon
```

#### ↳ Re: Overriding 01 level

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35AC0E05.7770@sprynet.com>`
- **References:** `<6ofsc2$5bo$1@lnews.actcom.co.il>`

```
Alp wrote:
> 
> Hi all,
…[13 more quoted lines elided]…
> This syntax was possible in COBOL VS but not in COBOL II

I had no idea that was possible, but it seems like a rather bad idea, and I'm
glad I've never seen it used.  Are you sure it actually worked, though?  It seems
like after the copy we'd get

01 MYCOPY.
01 EMP.
  03 ....

Which of course would cause a syntax error...

In any case, how about:

COPY COPYB REPLACING ==EMP.== BY ==MYCOPY.==.

Not wonderful, but I think it should work (assuming I don't have a syntax
error there...)
```

##### ↳ ↳ What happened was...

- **From:** "Bud Vitoff" <BudVitoff@worldnet.att.net>
- **Date:** 1998-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6oh85h$jnc@bgtnsc03.worldnet.att.net>`
- **References:** `<6ofsc2$5bo$1@lnews.actcom.co.il> <35AC0E05.7770@sprynet.com>`

```


Frank Swarbrick <infocat@sprynet.com> wrote in article
<35AC0E05.7770@sprynet.com>...
(snipped)> > 
> > 01 MYCOPY.   COPY COPYB.
> > 
…[6 more quoted lines elided]…
> I had no idea that was possible, but it seems like a rather bad idea, and
I'm
> glad I've never seen it used.  Are you sure it actually worked, though? 
It seems
> like after the copy we'd get
> 
…[4 more quoted lines elided]…
> Which of course would cause a syntax error...

Nope.  What happened was that your  01 line (minus the copy phrase) would
replace the first line of the copy member.

> 
> In any case, how about:
> 
> COPY COPYB REPLACING ==EMP.== BY ==MYCOPY.==.


Yes, that works just fine.
```

#### ↳ Re: Overriding 01 level

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-lLrIweonNqfi@Dwight_Miller.iix.com>`
- **References:** `<6ofsc2$5bo$1@lnews.actcom.co.il>`

```
On Tue, 14 Jul 1998 15:10:13, "Alp" <alonp@cry-sys.com> wrote:

> Hi all,
> 
…[7 more quoted lines elided]…
> 

Why not leave the 01 Mycopy. out?


> COPYB contains the following statement:
> 01 EMP.
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
