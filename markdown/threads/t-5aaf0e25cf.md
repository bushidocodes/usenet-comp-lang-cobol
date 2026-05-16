[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Alternative to ELIF

_5 messages · 3 participants · 1998-12_

---

### Re: Alternative to ELIF

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3670b40e.176161996@netnews>`
- **References:** `<36695DD8.4D90@swbell.net> <74bpqo$mnt@dfw-ixnews4.ix.netcom.com>`

```
'Twas Sat, 5 Dec 1998 11:15:33 -0600, when "William M. Klein"
<wmklein@ix.netcom.com> illuminated comp.lang.cobol thusly:

>
>Michael C. Kasten wrote in message <36695DD8.4D90@swbell.net>...
…[10 more quoted lines elided]…
>   This is NOT standard-conforming source code.  

But it's accepted by most compilers.
```

#### ↳ Re: Alternative to ELIF

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74qu1j$17g@sjx-ixn6.ix.netcom.com>`
- **References:** `<36695DD8.4D90@swbell.net> <74bpqo$mnt@dfw-ixnews4.ix.netcom.com> <3670b40e.176161996@netnews>`

```

Randall Bart wrote in message <3670b40e.176161996@netnews>...
>'Twas Sat, 5 Dec 1998 11:15:33 -0600, when "William M. Klein"
><wmklein@ix.netcom.com> illuminated comp.lang.cobol thusly:
…[17 more quoted lines elided]…
>--


Randall,
  If they do accept it, what do they do when the "C" (in the sample) is an
in-line perform? (P.S. as asked by another person, which compilers DO accept
this?)
```

##### ↳ ↳ Re: Alternative to ELIF

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-12-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36732abb.33176457@netnews>`
- **References:** `<36695DD8.4D90@swbell.net> <74bpqo$mnt@dfw-ixnews4.ix.netcom.com> <3670b40e.176161996@netnews> <74qu1j$17g@sjx-ixn6.ix.netcom.com>`

```
'Twas Fri, 11 Dec 1998 04:59:15 -0600, when "William M. Klein"
<wmklein@ix.netcom.com> illuminated comp.lang.cobol thusly:
>Randall Bart wrote in message <3670b40e.176161996@netnews>...
>>'Twas Sat, 5 Dec 1998 11:15:33 -0600, when "William M. Klein"
…[21 more quoted lines elided]…
>in-line perform? 

An in-line PERFORM *must* be terinated by END-PERFORM.  But even assuming
this compiler allows optional END-PERFORM, as in your END-ADD example, the
terminator pairs to the closest possible verb.

>(P.S. as asked by another person, which compilers DO accept
>this?)

Unisys A Series Cobol85 accepts it when FEDLEVEL is set to 5.  I'll try
setting the FEDLEVEL down to see if it gets flagged.  I know it worked on
some PC Cobol.  I usually put all my terminators in nested statements, but
I've never had a compiler berate me when I didn't.  Most of the programs I
work on have non-ANSI database sysntax, so I prefer to have most such
flagging options turned off.
```

##### ↳ ↳ Re: Alternative to ELIF

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36771fcf.92055862@news1.ibm.net>`
- **References:** `<36695DD8.4D90@swbell.net> <74bpqo$mnt@dfw-ixnews4.ix.netcom.com> <3670b40e.176161996@netnews> <74qu1j$17g@sjx-ixn6.ix.netcom.com>`

```
On Fri, 11 Dec 1998 04:59:15 -0600, "William M. Klein"
<wmklein@ix.netcom.com> wrote:

>
>Randall Bart wrote in message <3670b40e.176161996@netnews>...
…[26 more quoted lines elided]…
>

Bot MicroFocus (as far back as 3.1) and CA-Realia (as far back as 4.2)
both accept the inline perform with no internal statements.

Fujitsu and VMS COBOL do not.  I have not tried it using COBOL for
this and that.
```

##### ↳ ↳ Re: Alternative to ELIF

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3677207c.92228357@news1.ibm.net>`
- **References:** `<36695DD8.4D90@swbell.net> <74bpqo$mnt@dfw-ixnews4.ix.netcom.com> <3670b40e.176161996@netnews> <74qu1j$17g@sjx-ixn6.ix.netcom.com>`

```
On Fri, 11 Dec 1998 04:59:15 -0600, "William M. Klein"
<wmklein@ix.netcom.com> wrote:


>>>>    PERFORM
>>>>      IF A ...
…[15 more quoted lines elided]…
>this?)

There I go again - commenting without reading - the post was talking
about the above and *I* was talking about

PERFORM VARYING CNTR FROM 1 BY 1 UNTIL CNTR > 10
END-PERFORM

As opposed to the standard comforming versoin which needs a CONTINUE
in it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
