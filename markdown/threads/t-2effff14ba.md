[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol OS/390 to C OS/390 V2R6

_3 messages · 3 participants · 1999-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Cobol OS/390 to C OS/390 V2R6

- **From:** Roland Schiradin <schiradi@tap.de>
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D1F48F.3BD75D87@tap.de>`

```
Hi,

just to let you know I have made some test and can confirm that IBM
drop the "#pragma linkage(xxxx,COBOL)" requirement with C OS/390 V2R6.

This mean you don't have to tell C who is the calling program and how
the parameters
list looks.

I'll expand my test-programs from time to time. Next step is C to Cobol
and
PL1 to Cobol. After that I 'll release my source/jcl on www.cbttape.org
File321


Roland
```

#### ↳ Re: Cobol OS/390 to C OS/390 V2R6

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uzrA2.15045$OS5.15022241@news3.mia>`
- **References:** `<36D1F48F.3BD75D87@tap.de>`

```
well NO DUH.  That's why it called LE - Language Environment.
All programs COMPILED (not necessarily assembled) expect
to find the address of passed parms in R1 and return them in R1
and return any return-code in R15.  ALSO, for variable number of parms
the LAST item in the list has it's 0 bit (leftmost) set ON.  That way
all system SVC routines and system subs / compiled subs can
see the 'end of the list'

You can stop your 'testing'.  As long as your on OS/390, it'll work

Roland Schiradin wrote in message <36D1F48F.3BD75D87@tap.de>...
>Hi,
>
…[20 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol OS/390 to C OS/390 V2R6

- **From:** Roland.Schiradin@t-online.de (Roland Schiradin)
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aucmk$vqc$1@news00.btx.dtag.de>`
- **References:** `<36D1F48F.3BD75D87@tap.de> <uzrA2.15045$OS5.15022241@news3.mia>`

```
James King schrieb in Nachricht ...
>well NO DUH.  That's why it called LE - Language Environment.
>All programs COMPILED (not necessarily assembled) expect
…[4 more quoted lines elided]…
>see the 'end of the list'
This is no true for ILC between Cobol and  C OS/390 V2R4.
C have a different calling convention.

Roland
>
>You can stop your 'testing'.  As long as your on OS/390, it'll work
…[26 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
