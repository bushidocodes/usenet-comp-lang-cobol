[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Embeded Signs >> HELP

_5 messages · 5 participants · 1999-05_

---

### Embeded Signs >> HELP

- **From:** Bogy@Texas.NEt (Peter Gilchrist)
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373af715.9414984@news.texas.net>`

```
Using MF cobol, I have an input file containg embeded signs.  What is
the easiest way to xlate the character to a leading and separate sign
? (as in the example below).

000000000788u 000000001637q

-000000007886 +000000016372

Of course I would need the translation for eack "u", "q", etc in order
to program in the conversion.  I hope there is a REDEFINES that would
help be out better.

Please help !
```

#### ↳ Re: Embeded Signs >> HELP

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-dy4my9THciVf@Dwight_Miller.iix.com>`
- **References:** `<373af715.9414984@news.texas.net>`

```
On Thu, 13 May 1999 16:03:35, Bogy@Texas.NEt (Peter Gilchrist) wrote:

> Using MF cobol, I have an input file containg embeded signs.  What is
> the easiest way to xlate the character to a leading and separate sign
…[11 more quoted lines elided]…
> 

You can define a field in working-storage as "Separate Leading" and 
then just MOVE the data to that field.  

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Embeded Signs >> HELP

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hf0t1$nda$1@news.ses.cio.eds.com>`
- **References:** `<373af715.9414984@news.texas.net>`

```
Peter,

Look up the following in any COBOL book or vendor language reference
manual: LEADING SIGN IS SEPARATE.



Peter Gilchrist <Bogy@Texas.NEt> wrote in message
news:373af715.9414984@news.texas.net...
> Using MF cobol, I have an input file containg embeded signs.  What
is
> the easiest way to xlate the character to a leading and separate
sign
> ? (as in the example below).
>
…[4 more quoted lines elided]…
> Of course I would need the translation for eack "u", "q", etc in
order
> to program in the conversion.  I hope there is a REDEFINES that
would
> help be out better.
>
> Please help !
>
```

##### ↳ ↳ Re: Embeded Signs >> HELP

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373b8b56.13512428@netnews>`
- **References:** `<373af715.9414984@news.texas.net> <7hf0t1$nda$1@news.ses.cio.eds.com>`

```
'Twas Thu, 13 May 1999 11:08:18 -0600, when "ChrisOsborne"
<chris_n_osborne@yahoo.com> illuminated comp.lang.cobol thusly:

> Look up the following in any COBOL book or vendor language reference
> manual: LEADING SIGN IS SEPARATE.

SIGN IS LEADING SEPARATE
```

#### ↳ Re: Embeded Signs >> HELP

- **From:** philhickling@my-dejanews.com
- **Date:** 1999-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hk8u6$95n$1@nnrp1.deja.com>`
- **References:** `<373af715.9414984@news.texas.net>`

```
In article <373af715.9414984@news.texas.net>,
  Bogy@Texas.NEt (Peter Gilchrist) wrote:
> Using MF cobol, I have an input file containg embeded signs.  What is
> the easiest way to xlate the character to a leading and separate sign
…[12 more quoted lines elided]…
> Can't you just move the field to another, edited field?  Thus you
have 2 definitions:
77  FIELD-1     PIC S9(13).
77  FIELD-2     PIC +9(13).
and one comand:
    MOVE FIELD-1 TO FIELD-2.
If you define FIELD-2 as -9(13) only minus signs would show;  with a +
then both + & 1 signs show.

Phil


--== Sent via Deja.com http://www.deja.com/ ==--
---Share what you know. Learn what you don't.---
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
