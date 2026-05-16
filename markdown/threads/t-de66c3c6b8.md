[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CALL, identifier-2, and address-identifiers

_4 messages · 3 participants · 2003-04_

---

### CALL, identifier-2, and address-identifiers

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-21T15:22:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b81juc$h7m$1@slb6.atl.mindspring.net>`

```
I don't know if this agrees or not with Rick's earlier post, but I received
the following clarification from the J4 chair  (that I think makes sense)
concerning "identifier-2" of the CALL statement,

"If you explicitly code BY REFERENCE address-identifier, the compiler should
diagnose that as a syntax error. If you don't code any BY phrase on the CALL
statement, the argument will be passed by content."
```

#### ↳ Re: CALL, identifier-2, and address-identifiers

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-21T15:25:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b81k3q$2od$1@slb6.atl.mindspring.net>`
- **References:** `<b81juc$h7m$1@slb6.atl.mindspring.net>`

```
OOPS - out of context this *might* confuse some (who don't ready the subject
of this thread).  The following *only* applies to an address-identifier used
as identifier-2.  OBVIOUSLY,  the "normal" default (for
NON-address-identifiers) when no BY clause is used is "BY REFERENCE" and
coding an explicit BY REFERENCE is allowed for all non-address-identifier
identifier-2's that are otherwise "legal".
```

#### ↳ Re: CALL, identifier-2, and address-identifiers

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-21T18:02:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va8qn8t16dklc8@corp.supernews.com>`
- **References:** `<b81juc$h7m$1@slb6.atl.mindspring.net>`

```
Unfortunately, it does not agree. The quote appears to be the
result of applying GR(9), page 425, which pertains to Format 3.
The discussion referenced SR(11), page 422, which pertains
to Formats 1 and 2.

GR(5), page 424, which pertains to Formats 1 and 2, suggests
that the absence of any BY ... means that BY REFERENCE is
assumed; that is, implied. The specification of class pointer in
SR(11) means that every use of an address-identifier with
BY REFERENCE is a syntax error; thus only BY CONTENT
may be used with an address-identifier in Formats 1 and 2.
I had, perhaps wrongly, assumed that SR(11) might not apply.

Assuming that SR(11) does apply, the implications are that
existing code that uses [BY REFERENCE] ADDRESS OF
will get a syntax error when conformance checking is enabled.
This applies to Micro Focus, and apparently to IBM COBOL II
and later, the fix is to use BY CONTENT ADDRESS OF or
add a program prototype.

The LRM for MF COBOL/2 3.2, for both MF and VSC2
syntax, GR(16) page 4-343, is written such that the standard
COBOL SR(11) would not have applied.

The questions are:

1. Does CALL SR(11) apply to address-identifiers?
2. Was it intended to apply?
3. Did I miss something?

FDIS, page 421, CALL SR(3),
"3) Identifier-2 shall reference an address-identifier or a data
item defined in the file, working-storage, local-storage, linkage,
or communication section. If the BY REFERENCE phrase is
specified or implied, identifier-2 shall not be defined in the
working-storage or file section of a factory or an instance object."

FDIS, page 421 CALL SR(4),
"4) If the BY REFERENCE phrase is not specified or implied
for an identifier-2 or if identifier-2 is an address-identifier,
identifier-2 is a sending operand."

FDIS, page 421, CALL SR(5),
"5) If the BY REFERENCE phrase is specified or implied for
an identifier-2 and identifier-2 is not an address-identifier,
it is a receiving operand."

FDIS, page 422, CALL SR(11),
"FORMATS 1 AND 2
11) If the BY REFERENCE phrase is specified or implied for
an identifier-2, that identifier shall be neither a strongly-typed
group item nor a data item of class object or pointer."

FDIS, page 424, CALL GR(5),
"FORMATS 1 AND 2
5) Both the BY CONTENT and BY REFERENCE phrases are
transitive across the parameters that follow them until another
BY CONTENT or BY REFERENCE phrase is encountered. If
neither the BY CONTENT nor the BY REFERENCE phrase is
specified prior to the first parameter, the BY REFERENCE
phrase is assumed."

FDIS, page 425, CALL GR(9),
"9) If an argument is specified without any of the keywords BY
REFERENCE, BY CONTENT, or BY VALUE, the manner used
for passing this argument is determined as follows:
    a) When the BY REFERENCE phrase is specified or implied
         for the corresponding formal parameter:
        1. if the argument meets the requirements of syntax rule 3,
            BY REFERENCE is assumed;
        2. if the argument does not meet the requirements of syntax
            rule 3, BY CONTENT is assumed.
    b) When the BY VALUE phrase is specified or implied for the
        corresponding formal parameter, BY VALUE is assumed."

LRM, MF COBOL/2 3.2, page 4-343, GR(16),
"If the BY REFERENCE OF ADDRESS (sic) phase is specified
or implied then the object program operates as if an additional
data item had been declared with USAGE POINTER and that
data item passed BY REFERENCE with a value acquired by a
SET data item ADDRESS OF identifier-3 statement."

William M. Klein <wmklein@ix.netcom.com> wrote in message
news:b81juc$h7m$1@slb6.atl.mindspring.net...
> I don't know if this agrees or not with Rick's earlier post, but I
received
> the following clarification from the J4 chair  (that I think makes sense)
> concerning "identifier-2" of the CALL statement,
>
> "If you explicitly code BY REFERENCE address-identifier, the compiler
should
> diagnose that as a syntax error. If you don't code any BY phrase on the
CALL
> statement, the argument will be passed by content."
>
> --
> Bill Klein
>  wmklein <at> ix.netcom.com
```

#### ↳ Re: CALL, identifier-2, and address-identifiers

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-21T21:03:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-97EABE.21030921042003@corp.supernews.com>`
- **References:** `<b81juc$h7m$1@slb6.atl.mindspring.net>`

```
In article <b81juc$h7m$1@slb6.atl.mindspring.net>,
 "William M. Klein" <wmklein@ix.netcom.com> wrote:

> I don't know if this agrees or not with Rick's earlier post, but I received
> the following clarification from the J4 chair  (that I think makes sense)
…[8 more quoted lines elided]…
>  wmklein <at> ix.netcom.com


I'm not sure I'm wild about that.  I've used things like:

   Call SOME-PROGRAM using address of RETURN-DATA-STRUC-IN-LINKAGE

with the IBM compiler and I find it a useful shorthand for:
   
   1 A-POINTER POINTER.
   ...
   Call SOME-PROGRAM using A-POINTER
   Set address of RETURN-DATA-STRUC-IN-LINKAGE to A-POINTER

This was expecially useful before the v2.2 Cobol for OS/390 compiler 
when I had to include a tiny subprogram to get a reference to a working 
storage item.

I can see the reason to default to BY CONTENT, but I would like the 
option to pass BY REFERENCE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
