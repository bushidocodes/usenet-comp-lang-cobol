[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Move corresponding question

_7 messages · 6 participants · 1995-06_

---

### Move corresponding question

- **From:** "cst..." <ua-author-8526434@usenetarchives.gap>
- **Date:** 1995-06-20T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3s9dti$pa0@news1.digex.net>`

```
I have a question about MOVE in Micro Focus. As I understand it, the following would work correctly with MOVE CORR but not with a simple MOVE. Is this true?

01 REC1
02 F1 PIC X(4).
02 F2 PIC X(4).
02 F3 PIC X(4).

01 REC2
02 A PIC X(4).
02 B PIC X(4).
02 C PIC X(4).

MOVE REC1 TO A.

---
=======================================================================
= Charles Stump, Director of Business Development, cst··.@lev··h.com =
=======================================================================
= Leverage Technologists, Inc. = Reverse Engineering, =
= 6701 Democracy Blvd. = Reengineering, =
= Bethesda, MD 20817 = Maintenance, and =
= Suite 324 = Quality Assurance =
= (301)309-8783 = tools and services. =
= http://stout.levtech.com/ = =
=======================================================================
```

#### ↳ Re: Move corresponding question

- **From:** "cst..." <ua-author-8526434@usenetarchives.gap>
- **Date:** 1995-06-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f2cd5dec0e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3s9dti$pa0@news1.digex.net>`
- **References:** `<3s9dti$pa0@news1.digex.net>`

```
Umm...sorry about that..I made a typo in the last post. The post should have been:

01 REC1
02 F1 PIC X(4).
02 F2 PIC X(4).
02 F3 PIC X(4).

01 REC2
02 A PIC X(4).
02 B PIC X(4).
02 C PIC X(4).

MOVE REC1 TO REC2.

The goal is to get the values of F1 F2 and F3 into A B and C respectively.

Again, sorry about that last post!
```

##### ↳ ↳ Re: Move corresponding question

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1995-06-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f2cd5dec0e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f2cd5dec0e-p2@usenetarchives.gap>`
- **References:** `<3s9dti$pa0@news1.digex.net> <gap-f2cd5dec0e-p2@usenetarchives.gap>`

```
. Umm...sorry about that..I made a typo in the last post.
. The post should have been:
.
. 01 REC1
. 02 F1 PIC X(4).
. 02 F2 PIC X(4).
. 02 F3 PIC X(4).
.
. 01 REC2
. 02 A PIC X(4).
. 02 B PIC X(4).
. 02 C PIC X(4).
.
. MOVE REC1 TO REC2.
.
. The goal is to get the values of F1 F2 and F3 into
. A B and C respectively.
.

This will do what you want. The 12 bytes of REC1 will be moved
to the 12 bytes of REC2.
This has absolutely nothing to do with MOVE CORRESPONDING however.
MOVE CORR moves elementary data items that correspond by BOTH
name AND level number. Example:


01 REC1
02 F1 PIC X(4) VALUE '1234'.
02 F2 PIC X(4) VALUE '5678'.
02 F3 PIC X(4) VALUE 'ABCD'.

01 REC2
02 F3 PIC X(4).
02 F2 PIC X(4).
02 F1 PIC X(4).

MOVE CORRESPONDING REC1 TO REC2.

The result will be the data elements of REC1 being moved
into REC2 in reverse order.
The data in REC2 = ABCD56781234

--END
```

##### ↳ ↳ Re: Move corresponding question

- **From:** "s98..." <ua-author-7885444@usenetarchives.gap>
- **Date:** 1995-06-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f2cd5dec0e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f2cd5dec0e-p2@usenetarchives.gap>`
- **References:** `<3s9dti$pa0@news1.digex.net> <gap-f2cd5dec0e-p2@usenetarchives.gap>`

```
In article <3s9vkq$2.··.@new··x.net>
cst··.@lev··h.com (Charles Stump) writes:

› 
› Umm...sorry about that..I made a typo in the last post. The post should have been:
…[13 more quoted lines elided]…
› The goal is to get the values of F1 F2 and F3 into A B and C respectively.



MOVE CORRESPONDING applies to copying data from two *different* records
with the *same* field names. For example:

01 REC1
02 A PIC X(4).
02 B PIC X(4).
02 C PIC X(4).

01 REC2
02 A PIC X(4).
02 B PIC X(4).
02 C PIC X(4).

MOVE CORRESPONDING REC1 TO REC2.
```

#### ↳ Re: Move corresponding question

- **From:** "wcl..." <ua-author-17087533@usenetarchives.gap>
- **Date:** 1995-06-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f2cd5dec0e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3s9dti$pa0@news1.digex.net>`
- **References:** `<3s9dti$pa0@news1.digex.net>`

```
In <3s9dti$p.··.@new··x.net>, cst··.@lev··h.com (Charles Stump) writes:
› I have a question about MOVE in Micro Focus. As I understand it, the following would work correctly with MOVE CORR but not with a simple MOVE. Is this true?
› 
…[11 more quoted lines elided]…
› 

What do you mean by work correctly? if you want to moce F1 to A, F2 to B
and F3 to C you simplye move REC1 to REC2. With MOVE REC1 TO A, you are moving
a 12 byte alphanumeric field to a four byte alphanumeric field, losing 8 bytes
in the process. The fields B and C will not be modified. MOVE CORRESPONDING
will move lower-level fields with the same name.
› =======================================================================
› = Charles Stump, Director of Business Development, cst··.@lev··h.com =
…[23 more quoted lines elided]…
›
```

#### ↳ Re: Move corresponding question

- **From:** "gber..." <ua-author-8474860@usenetarchives.gap>
- **Date:** 1995-06-20T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f2cd5dec0e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3s9dti$pa0@news1.digex.net>`
- **References:** `<3s9dti$pa0@news1.digex.net>`

```
In <3s9dti$p.··.@new··x.net>, cst··.@lev··h.com (Charles Stump) writes:
>I have a question about MOVE in Micro Focus. As I understand it, the
>following would work correctly with MOVE CORR but not with a simple MOVE.
>Is this true?
-->
01 REC1
02 F1 PIC X(4).
02 F2 PIC X(4).
02 F3 PIC X(4).

01 REC2
02 A PIC X(4).
02 B PIC X(4).
02 C PIC X(4).

MOVE REC1 TO A.
--->
Whenever you do something you shouldn,'t, you become subject to
the whim of the specific compiler. What *should* happen is, a "W"
level truncation message and a generated move of 4 bytes.

MOVE CORR. should not work because it does't apply to this case.
The structures REC1 and REC2 have no CORRESPONDING elements.
Ie. REC2 does not contain an element F1, F2, or F3.
Regards,
Gary
```

#### ↳ Re: Move corresponding question

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-06-22T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f2cd5dec0e-p7@usenetarchives.gap>`
- **In-Reply-To:** `<3s9dti$pa0@news1.digex.net>`
- **References:** `<3s9dti$pa0@news1.digex.net>`

```
In article <3s9dti$p.··.@new··x.net>
cst··.@lev··h.com (Charles Stump) writes:

› 
› I have a question about MOVE in Micro Focus. As I understand it, the following would work correctly with MOVE CORR but not with a simple MOVE. Is
…[16 more quoted lines elided]…
› 
Hello:
I would code the above as this:
move rec1 to rec2.

or
move f1 to a
move f2 to b
move f3 to c.

The following is a better candidate for move corresponding.
Moveing like named variables in different record layouts is more proper.

01 ws-system-date.
05 YY pic x(02).
05 mm pic x(02).
05 dd pic x(02).

01 ws-formated-date.
05 mm pic x(02).
05 filler pic x(01) value '/'.
05 dd pic x(02).
05 filler pic x(01) value '/'.
05 yy pic x(02).

accept ws-system-date from date.
move corresponding ws-system-date to ws-formated-date.

would result in 06/23/95
but move ws-system-date to ws-formated-date
would result in:
950623 with trailing spaces.
Remember:
left justify and fill with spaces on alpha MOVES...



Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
