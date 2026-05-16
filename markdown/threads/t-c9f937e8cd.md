[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DATE-problem

_6 messages · 4 participants · 1999-12 → 2000-01_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### DATE-problem

- **From:** Michael Stoll <tsc.stoll@t-online.de>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386BD69F.DB9CD3F3@t-online.de>`

```
Hi,

I've a problem with the DATE command in COBOL-Program. Which alternative
gives to use another command than DATE, because the Program
gives in 01.01.2000 back : 10.00.01
So I think I must use another command. In the program gives a section:

ACCEPT FIELD FROM DATE. and the content from date   is 100001 at
01.01.2000

How can I solve this problem ???

Ciao Michael
```

#### ↳ Re: DATE-problem

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84gta9$hgq$1@nntp9.atl.mindspring.net>`
- **References:** `<386BD69F.DB9CD3F3@t-online.de>`

```
Any ANSI conforming implementation will provide you the output of ACCEPT FROM
DATE as

    YYMMDD

Therefore, I think you are looking at your "output" incorrectly and it is
actually returning 000101 on Jan 1, 2000.  HOWEVER, if what you really want
is output from the statement in CCYYMMDD format, then tell us which compiler
you are using.  Many have already adopted (as an extension) an optional word
that will become Standard when/if the next Standard is approved, so you can
say

    Accept my-date-field from Date YYYYMMDD.

Tell us your compiler (release and operating system) and we can tell you if
it is there yet.
```

##### ↳ ↳ Re: DATE-problem

- **From:** Michael Stoll <tsc.stoll@t-online.de>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386C8DB2.D8BFCAD9@t-online.de>`
- **References:** `<386BD69F.DB9CD3F3@t-online.de> <84gta9$hgq$1@nntp9.atl.mindspring.net>`

```
Hi,

at this moment I don't know the version of the compiler. I must look
next week which compiler it is.

Thnk you
Michael


William M. Klein schrieb:
> 
> Any ANSI conforming implementation will provide you the output of ACCEPT FROM
…[33 more quoted lines elided]…
> > Ciao Michael
```

#### ↳ Re: DATE-problem

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84h2bh$hdk$1@nnrp1.deja.com>`
- **References:** `<386BD69F.DB9CD3F3@t-online.de>`

```
In article <386BD69F.DB9CD3F3@t-online.de>,
  Michael Stoll <tsc.stoll@t-online.de> wrote:
> Hi,
>
> I've a problem with the DATE command in COBOL-Program. Which
alternative
> gives to use another command than DATE, because the Program
> gives in 01.01.2000 back : 10.00.01
…[8 more quoted lines elided]…
>

Assuming that your environment is IBM-Mainframe, you must change your
ACCEPT Verb to issue a CALL of the IBM-Supplied Sub-Program "IGZEDT4",
passing an 8-byte numeric parameter. The returned date value will have
a format of CCYYMMDD. Note that your system MUST have the fix for APAR
PN76666. You'll need to confirm this with your Systems personnel.

Alternatively, if your IBM system is using the LE environment, you
could also issue a CALL to CEELOCTM.

However, none of this would apply to a COBOL3 environment, where you
can use the FUNCTION CURRENT-DATE.

Have an uneventful Y2K.

Cheers,

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: DATE-problem

- **From:** Michael Stoll <tsc.stoll@t-online.de>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386C8D2D.39BA5E09@t-online.de>`
- **References:** `<386BD69F.DB9CD3F3@t-online.de> <84h2bh$hdk$1@nnrp1.deja.com>`

```
WOB Consulting schrieb:
> 
> In article <386BD69F.DB9CD3F3@t-online.de>,
…[36 more quoted lines elided]…
> Before you buy.

The environment is a siemens nixdorf Targon/35 with operating system
TOS 4.5 and MicroFocus Cobol II Compiler I must look next week
where it stand.

Thanks Michael
```

#### ↳ Re: DATE-problem

- **From:** "Julian Brett" <julian@rubiconcs.co.uk>
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<946835180.9417.0.nnrp-13.9e98ac08@news.demon.co.uk>`
- **References:** `<386BD69F.DB9CD3F3@t-online.de>`

```
Hi.

I've just seen this problem occur elsewhere.  I believe that you meant
100010.  It seems that MF Cobol II returns 100 for the year value of the
call to DATE, and therefore you are really losing one of the characters
which makes up the day value (YYMMDD) as everything else is shifted.  A call
to DATE will only return a 6 digit field.

If you ACCEPT FIELD FROM DAY, you get 10000, instead of 00001, so this
doesn't help either.

===
Julian Brett.
===


Michael Stoll wrote in message <386BD69F.DB9CD3F3@t-online.de>...
>Hi,
>
…[10 more quoted lines elided]…
>Ciao Michael
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
