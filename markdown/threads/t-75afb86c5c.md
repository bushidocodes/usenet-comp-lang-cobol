[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NUMVAL function's parameter - no easy way to test ?

_4 messages · 3 participants · 1995-01_

---

### NUMVAL function's parameter - no easy way to test ?

- **From:** "g_m..." <ua-author-17087869@usenetarchives.gap>
- **Date:** 1995-01-23T14:54:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3g11hk$3ed@ccnet.ccnet.com>`

```
How to test the suiteability of the NUMVAL functionï¿½s parameter
before you blowup or survive after it ?

01 D pic x(3) value "1 ".
01 badD pic x(3) value "A "


D will not test numeric, but is a good numeric string to NUMVAL
badD will not test numeric, and causes a runtime error if passed
to NUMVAL.

Compiler is Tandem COBOL85, D20.03
```

#### ↳ Re: NUMVAL function's parameter - no easy way to test ?

- **From:** "vla..." <ua-author-758196@usenetarchives.gap>
- **Date:** 1995-01-27T23:01:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-75afb86c5c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3g11hk$3ed@ccnet.ccnet.com>`
- **References:** `<3g11hk$3ed@ccnet.ccnet.com>`

```
This fix may be a DEC extention. Check your Tandem manual to see if it
will work.

NUMERIC and ALPHABETIC are classes in Cobol. You can create your own
class if you need something that is not in one of the predefined classes.

In SPECIAL-NAMES you need something like this:
CLASS NUMERIC-AND-SPACES IS "0" THRU "9", " ".

Then in the PROCEDURE DEVISION you can use it like this:
IF D NUMERIC-AND-SPACES
MOVE NUMVAL (D) TO ....

Hope this is what you need.

Mike Grethen
Illinois Institute of Technology
Chicago
e-mail acs··.@vax··t.edu

I'm not lost, I'm exploring.
```

##### ↳ ↳ Re: NUMVAL function's parameter - no easy way to test ?

- **From:** "r..." <ua-author-2587243@usenetarchives.gap>
- **Date:** 1995-01-30T07:30:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-75afb86c5c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-75afb86c5c-p2@usenetarchives.gap>`
- **References:** `<3g11hk$3ed@ccnet.ccnet.com> <gap-75afb86c5c-p2@usenetarchives.gap>`

```
In article <3gcfi3$6.··.@new··l.com>
vla··.@a··.com "Vlashko" writes:
› Subject: Re: NUMVAL function's parameter - no easy way to test ?
› NUMERIC and ALPHABETIC are classes in Cobol.
…[3 more quoted lines elided]…
› IF D NUMERIC-AND-SPACES

There is a baffling error message in the Micro Focus
Personal Cobol 2.0 compiler for DOS:

01 WSX PIC XX.
MOVE ZEROS TO WSX.
IF WSX ZEROS DISPLAY "ZEROS".
** CONFIGURATION missing

CONFIGURATION ??!? Equals sign, it should be IF WSX = ZEROS.

But the compiler thinks you forgot to declare ZEROS as a CLASS
in the CONFIGURATION section. Don't understand ZEROS, it thinks.

Now see the error it gives when you try to define the class:

SPECIAL-NAMES. CLASS ZEROS IS ZERO
** User-name required.

Aha, now the compiler knows ZEROS is a reserved word meaning 0.
You can't trick a smart compiler that way, oh no :-)

Richard Ross-Langley  +44(0)1727 852801
Mine of Information Ltd,  PO BOX 1000,  St Albans AL3 5NY,  GB
=== Independent Computer Consultancy * Established in 1977 ===
```

##### ↳ ↳ Re: NUMVAL function's parameter - no easy way to test ?

- **From:** "g_m..." <ua-author-17087869@usenetarchives.gap>
- **Date:** 1995-01-30T11:47:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-75afb86c5c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-75afb86c5c-p2@usenetarchives.gap>`
- **References:** `<3g11hk$3ed@ccnet.ccnet.com> <gap-75afb86c5c-p2@usenetarchives.gap>`

```
In article <3gcfi3$6.··.@new··l.com>, vla··.@a··.com (Vlashko) says:

› 
› NUMERIC and ALPHABETIC are classes in Cobol.  You can create your own
…[4 more quoted lines elided]…
› 
Thanks but this won't cut it. The SPECIAL NAMES, CLASS clause does not
describe a production, only a set of characters allowed in any combination.

01 D pic x(4) value "1 2".

would pass your class test but NUMVAL would puke on it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
