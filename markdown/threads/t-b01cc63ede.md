[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Conversion Issue - MF OC 4.2 to Server Express 4.0

_4 messages · 3 participants · 2004-11_

---

### Conversion Issue - MF OC 4.2 to Server Express 4.0

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2004-11-08T10:47:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0411081047.bcf9401@posting.google.com>`

```
Given the following procedure division source code:

    display "Hello"
      at line 01 col 01
    end-display

    display "There"
      at line +1 col 01
    end-display


I get the following complier error:


        12       at line +1 col 01
    *  65-S******************
    **    Unsigned integer required
    cob64: error(s) in compilation: testme.cbl


This same code compiles fine under OC 4.2. Was this a "feature" on 4.2
that was really a bug, because I cannot find any supporting docs.

Had anyone else seen this behavior?

Thanks in advance.

Chris
```

#### ↳ Re: Conversion Issue - MF OC 4.2 to Server Express 4.0

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-11-08T11:01:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cmofpl$1l7g$1@si05.rsvl.unisys.com>`
- **References:** `<8cc07162.0411081047.bcf9401@posting.google.com>`

```
Can't speak to an extension that allows it, but I do note that ISO/IEC
1989:2002 prohibits signed data items and literals in this context.

What's it mean to MF OC 4.2 if the code has a *minus* sign, given that line
and column positions can't be less than 1 in standard COBOL?

    -Chuck Stevens

"Chris" <ctaliercio@yahoo.com> wrote in message
news:8cc07162.0411081047.bcf9401@posting.google.com...
> Given the following procedure division source code:
>
…[25 more quoted lines elided]…
> Chris
```

#### ↳ Re: Conversion Issue - MF OC 4.2 to Server Express 4.0

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-08T21:03:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CaRjd.2618283$yk.414247@news.easynews.com>`
- **References:** `<8cc07162.0411081047.bcf9401@posting.google.com>`

```
Check for your "dialect" settings with the two compiles.  My *guess* is that 
some dialect is turned on or off in one that isn't on in the other.
```

#### ↳ Re: Conversion Issue - MF OC 4.2 to Server Express 4.0

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2004-11-08T17:19:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0411081719.171783cc@posting.google.com>`
- **References:** `<8cc07162.0411081047.bcf9401@posting.google.com>`

```
ctaliercio@yahoo.com (Chris) wrote in message news:<8cc07162.0411081047.bcf9401@posting.google.com>...
> Given the following procedure division source code:
> 
…[25 more quoted lines elided]…
> Chris


Just to clarify, under OC 4.2, you would end up with the following
output:

Hello
There

The 'LINE +1' is interpretted as "go to the next line" - which is
exactly the behavior I am looking for. Again, I can't find the
documentation to support this, but it definitely works under MF OC
4.2.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
