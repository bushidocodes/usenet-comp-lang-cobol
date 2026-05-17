[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PACKED-DECIMAL/COMP-3

_3 messages · 3 participants · 1998-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### PACKED-DECIMAL/COMP-3

- **From:** "dirk haar" <ua-author-4538476@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<352D3C5F.D7B64441@ebs-net.com>`

```
Anyone who wants to know the different COBOL data formats should send me
his fax number.
Those data formats are equal for every COBOL compiler as COBOL has to
comply to CODASYL specifications.
I won't use your number for any other purposes. Give me some time to
answer.
Dirk
```

#### ↳ Re: PACKED-DECIMAL/COMP-3

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b518fdcb7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<352D3C5F.D7B64441@ebs-net.com>`
- **References:** `<352D3C5F.D7B64441@ebs-net.com>`

```

You are mistaken in MULTIPLE ways.

1) CODASYL (or at least the COBOL part) is "dead" and has been for several
years.

2) There never was a requirement that compilers conform to the CODASYL JOD
(Journal of Development). The only "requirement" was conformance to the
ANSI Standard (and/or FIPS certification)

3) Even the JOD did *not* specify what any of the COMP-n values meant. (and
for ANSI, all the COMP-n values *are* extensions)

4) There is no requirement for even COMP as to how it is stored. (There is a
"rumor" - which is currently false - that the ANSI Standard requires COMP to
be the "most efficient" storage mechanism. This is no where in the current
Standard.)

5) The truth is that COMP-1 thru COMP-9 are truly implemented in different
methods on different machines with different compilers. Taking a simple
example, if you have a usage COMP field on a PC, depending on the vendor:

A) some compilers allow one byte binary fields - while others always
allocate 2-bytes even for a PIC S9(01) field.
B) some compilers use big-endian and others use little-endian storage
(and if you don't understand these terms, that is fine - but it means you
don't understand PC storage formats and wouldn't understand how different
compilers use different storage methods)

*****

Bottom-line: COMP and COMP-n storage is vendor/platform specific and anyone
who tells you that there is a single "definition" is simply wrong. (As a
matter of fact, the ANSI definition for USAGE BINARY and USAGE
Packed-Decimal leaves a lot to the implementor as well - but at least the
Standard gives some "clues" about how they are stored.)
```

##### ↳ ↳ Re: PACKED-DECIMAL/COMP-3

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-08T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1b518fdcb7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1b518fdcb7-p2@usenetarchives.gap>`
- **References:** `<352D3C5F.D7B64441@ebs-net.com> <gap-1b518fdcb7-p2@usenetarchives.gap>`

```

William M. Klein wrote:

› 4) There is no requirement for even COMP as to how it is stored. (There is a
› "rumor" - which is currently false - that the ANSI Standard requires COMP to
› be the "most efficient" storage mechanism.  This is no where in the current
› Standard.)

The standard never required COMP to be the *most* efficient data
representation, in fact it never required it to be more efficient than
DISPLAY. I believe JOD said that COMP and COMP-n were various different
data representations, and may have said that ideally COMP was the most
efficient, but I don't think that was ever written as a requirement.
COMP was necessarily not floating point, because it had to have a PIC.

Do we mean storage efficient or speed efficient? Different
representations might be more speed efficient for different data
ranges. This happens especially with floating point, but under JOD COMP
was necessarily not floating point, because it had to have a PIC.
Floating point COMP-n fileds don't have PIC, which is hell to the
compiler writer -- it looks like a group USAGE.

› A) some compilers allow one byte binary fields - while others always
› allocate 2-bytes even for a PIC S9(01) field.

Some compilers allow half byte decimal fields. On Unisys A Series, PIC
9 COMP occupies four bits.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \  
e    |\ Todd McCormick jailed for using Marinol with prescription:
Y    |/        http://marijuanamagazine.com/toc/articles/toddheld.html
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
