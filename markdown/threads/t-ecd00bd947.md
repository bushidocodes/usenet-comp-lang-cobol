[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Does COBOL constants exist?

_5 messages · 5 participants · 1995-12_

---

### Does COBOL constants exist?

- **From:** "niklas...." <ua-author-9433876@usenetarchives.gap>
- **Date:** 1995-12-02T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49rur2$lk6@mn5.swip.net>`

```
Hello,

I was just wondering if it is possible to declare true constants in COBOL, e.g the name gets
expanded into a value during compile time.

Thanks,

Niklas Iveslatt
```

#### ↳ Re: Does COBOL constants exist?

- **From:** "sal..." <ua-author-6588933@usenetarchives.gap>
- **Date:** 1995-12-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecd00bd947-p2@usenetarchives.gap>`
- **In-Reply-To:** `<49rur2$lk6@mn5.swip.net>`
- **References:** `<49rur2$lk6@mn5.swip.net>`

```
In <49rur2$l.··.@mn5··p.net>, nik··.@mai··t.se (Niklas Iveslatt) writes:
› Hello,
› 
…[6 more quoted lines elided]…
› 
I don't know that it is a part of the ANSI 85 standard, but both Acucobol &
Microfocus COBOLs allow you to define literal constants as working-storage
level 78 items. The syntax is:

78 This-is-the-constant value 250.

You can use This-is-the-constant anywhere you might use the literal 250
including occurs clauses. eg

01 A-large-table.
05 table-row occurs This-is-the-constant times.

I find it really handy.

Sal Cambareri -- SSC Consulting, Inc.
sal··.@tel··t.com or 71763,32··.@com··e.com
e puro si movi
```

#### ↳ Re: Does COBOL constants exist?

- **From:** "vod..." <ua-author-40038@usenetarchives.gap>
- **Date:** 1995-12-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecd00bd947-p3@usenetarchives.gap>`
- **In-Reply-To:** `<49rur2$lk6@mn5.swip.net>`
- **References:** `<49rur2$lk6@mn5.swip.net>`

```
Niklas Iveslatt (nik··.@mai··t.se) wrote:
: I was just wondering if it is possible to declare true constants
: in COBOL, e.g the name gets expanded into a value during compile time.

In Micro Focus Cobol, the 78 level declaration accepts only a VALUE,
and represents that value at compile time. I don't know if this is
in any standard or is only a Micro Focus feature.

78 NAMES-MAX VALUE 150.
01 NAMES-TABLE.
05 NAMES-ENT pic x(30) occurs NAMES-MAX times.

Victor Odhner Phoenix Arizona USA
```

#### ↳ Re: Does COBOL constants exist?

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1995-12-03T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecd00bd947-p4@usenetarchives.gap>`
- **In-Reply-To:** `<49rur2$lk6@mn5.swip.net>`
- **References:** `<49rur2$lk6@mn5.swip.net>`

```
Constants are *not* a part of the current ANSI/ISO COBOL
Standard.

Ther *are* included in many implementations (as an extension) -
and are still under development/consideration for the next COBOL
Standard.
```

#### ↳ Re: Does COBOL constants exist?

- **From:** "gordon...." <ua-author-10958913@usenetarchives.gap>
- **Date:** 1995-12-04T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecd00bd947-p5@usenetarchives.gap>`
- **In-Reply-To:** `<49rur2$lk6@mn5.swip.net>`
- **References:** `<49rur2$lk6@mn5.swip.net>`

```
nik··.@mai··t.se (Niklas Iveslatt) wrote:

› Hello,
› 
…[6 more quoted lines elided]…
› 
Well, in Unisys A Series COBOL85 you set a compiler directive around the
working-storage items that you would like to be constants. It works quite well
actully. It would look something like this:

$ OPT3
77 value22 PIC 9(2) VALUE 22.
77 value44 PIC 9(2) VALUE 44.
.
.
.
$ RESET OPT3

I am sure other compilers have the same possibility to optimize the COBOL
working-storage.

Hope this helps
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
