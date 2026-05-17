[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What's the shortest possible COBOL program?

_17 messages · 11 participants · 1997-07 → 1997-08_

---

### What's the shortest possible COBOL program?

- **From:** "spk..." <ua-author-17071408@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33cb0b63.20334013@news.dt1.sdca.home.com>`

```

Just for fun:
I once taught a COBOL class, and one of the exercises was this:

What is the shortest COBOL program you can write? RULES:

* It must be portable, i.e. ANS standard COBOL.
* It must take an input and make an output.

I scored by the number of lines necessary, but a byte count
would be a good measure, too.

Any takers?

P.S. No fair cloning an existing program! ;-)
```

#### ↳ Re: What's the shortest possible COBOL program?

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33cb0b63.20334013@news.dt1.sdca.home.com>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com>`

```

spk··.@c··.com wrote:
› Just for fun:
›  I once taught a COBOL class, and one of the exercises was this:
…[11 more quoted lines elided]…
› P.S. No fair cloning an existing program!  ;-)

The smallest compilable Cobol program on my machine (Tandem
Himalaya K2000) appears to be:

identification division.
program-id. a.
environment division.
data division.
procedure division.
z.
```

##### ↳ ↳ Re: What's the shortest possible COBOL program?

- **From:** "kiki" <ua-author-795227@usenetarchives.gap>
- **Date:** 1997-07-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p2@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p2@usenetarchives.gap>`

```

The proc
z.
is not required.

really dlmiller_at_inetdirect_dot_netDoug Miller
wrote in article <5qg60c$d80$1.··.@use··s.com>...
› spk··.@c··.com wrote:
›› Just for fun:
…[23 more quoted lines elided]…
›
```

#### ↳ Re: What's the shortest possible COBOL program?

- **From:** "alan russell" <ua-author-1025782@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<33cb0b63.20334013@news.dt1.sdca.home.com>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com>`

```

How about the following:

IDENTIFICATION DIVISION. [or ID DIVISION]
PROGRAM-ID. A.
ENVIRONMENT DIVISION. [optional in some environments]
DATA DIVISION.
WORKING-STORAGE SECTION.
01 Z PIC X.
PROCEDURE DIVISION.
ACCEPT Z. DISPLAY Z. STOP RUN.

Admitedly not a terribly useful program, but it does meet your rules.
Alan Russell, PhD
Rus··.@ap··i.com     (work)
AHR··.@a··.com      (home)
http://members.aol.com/AHRussell
-----------------------------------------------------------
The opinions expressed are mine alone and not those of the company I work
for.


spk··.@c··.com wrote in article
<33c··.@new··e.com>...
> Just for fun:
>   I once taught a COBOL class, and one of the exercises was this:
…[12 more quoted lines elided]…
>
```

##### ↳ ↳ Re: What's the shortest possible COBOL program?

- **From:** "wds" <ua-author-1064034@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p4@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap>`

```

Alan Russell wrote:
› 
› How about the following:
…[36 more quoted lines elided]…
›› 

The ACCEPT and DISPLAY unnecessarily lengthen the program.

Reply Addr:-->WDavid dot Simon at atl dot frb dot org<--
-------------------De··y@Spa··r.Trasher----------------
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

- **From:** "wds" <ua-author-1064034@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p5@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p5@usenetarchives.gap>`

```

WDS wrote:
› 
› Alan Russell wrote:
…[44 more quoted lines elided]…
› -------------------De··y@Spa··r.Trasher----------------

Oops... Forgot about the input and output.
Reply Addr:-->WDavid dot Simon at atl dot frb dot org<--
-------------------De··y@Spa··r.Trasher----------------
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

_(reply depth: 4)_

- **From:** "alan russell" <ua-author-1025782@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p6@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p5@usenetarchives.gap> <gap-c1c91fcdf4-p6@usenetarchives.gap>`

```

While this will not qualify for the shortest, below is an *actual* program
running at our company (written by myself) which actually does work. The
purpose of this program is simply to check *any* sequential input file
(that's why the "BLOCK CONTAINS 0 RECORD CONTAINS 0" clause) to see if it
has any records and to set a condition code to be checked in the JCL to,
for example, bypass a series of processing steps if there is no input.

ID DIVISION.

PROGRAM-ID. A5C610.

ENVIRONMENT DIVISION.

INPUT-OUTPUT SECTION.

FILE-CONTROL.

SELECT IN-FILE ASSIGN TO UT-S-INFILE.

DATA DIVISION.

FILE SECTION.

FD IN-FILE LABEL STANDARD

BLOCK CONTAINS 0 RECORD CONTAINS 0.

01 IN-REC PIC X(80).

PROCEDURE DIVISION.

OPEN INPUT IN-FILE.

MOVE 0 TO RETURN-CODE

READ IN-FILE

AT END MOVE 16 TO RETURN-CODE.

CLOSE IN-FILE.

GOBACK.
```

##### ↳ ↳ Re: What's the shortest possible COBOL program?

- **From:** "spk..." <ua-author-17071408@usenetarchives.gap>
- **Date:** 1997-07-21T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p4@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap>`

```

Well, the WORKING-STORAGE entry only requires 1 space after the
level number.

The line after PROCEDURE DIVISION line may start in the first column
of AREA-B and requires only one period.
Also, I believe the STOP RUN is not required, but the standard
probably wants it (is this true?).
Which leaves:

123456789012345678901234567890=====
IDENTIFICATION DIVISION.
PROGRAM-ID. A.
ENVIRONMENT DIVISION.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 Z PIC X.
PROCEDURE DIVISION.
ACCEPT Z DISPLAY Z.
123456789012345678901234567890=====
total: 8 lines, 155 bytes

-steve


On 15 Jul 1997 11:08:24 GMT, "Alan Russell" wrote:
› How about the following:
› 
…[36 more quoted lines elided]…
››
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

- **From:** "jody-..." <ua-author-17071913@usenetarchives.gap>
- **Date:** 1997-07-24T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p8@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p8@usenetarchives.gap>`

```

Actually, I believe with the 85 Standard, the only thing required in a
COBOL program is the Identification and Environment division headers.
That would take it down to two lines. I may be wrong but I think I
remember reading that in one of my reference books.

Jody Richardson
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

_(reply depth: 4)_

- **From:** "spk..." <ua-author-17071408@usenetarchives.gap>
- **Date:** 1997-07-25T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p9@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p8@usenetarchives.gap> <gap-c1c91fcdf4-p9@usenetarchives.gap>`

```

But don't forget the rules (from the original post):
›› What is the shortest COBOL program you can write? RULES:
››
›› * It must be portable, i.e. ANS standard COBOL.
›› * It must take an input and make an output.



On Fri, 25 Jul 1997 03:41:35 GMT, jody-.··@wor··t.net (Jody &
Mimi Richardson) wrote:

› Actually, I believe with the 85 Standard, the only thing required in a
› COBOL program is the Identification and Environment division headers.
…[3 more quoted lines elided]…
› Jody Richardson
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

_(reply depth: 4)_

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1997-07-26T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p9@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p8@usenetarchives.gap> <gap-c1c91fcdf4-p9@usenetarchives.gap>`

```

On Fri, 25 Jul 1997 03:41:35 GMT, jody-.··@wor··t.net (Jody &
Mimi Richardson) wrote:

› Actually, I believe with the 85 Standard, the only thing required in a
› COBOL program is the Identification and Environment division headers.
…[3 more quoted lines elided]…
› Jody Richardson
nope. environment division is optional. without checking my notes, i
think id division and program-id will compile and execute -- i've done
it. works fine for creating stub programs for later enhancement.

David d.s··.@ix.··m.com
____________________________________
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

_(reply depth: 5)_

- **From:** "lindy mayfield" <ua-author-13980060@usenetarchives.gap>
- **Date:** 1997-07-30T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p11@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p8@usenetarchives.gap> <gap-c1c91fcdf4-p9@usenetarchives.gap> <gap-c1c91fcdf4-p11@usenetarchives.gap>`

```

David wrote:
› 
› On Fri, 25 Jul 1997 03:41:35 GMT, jody-.··@wor··t.net (Jody &
…[10 more quoted lines elided]…
› it.   works fine for creating stub programs for later enhancement.


This compiled with a return code of 0 under IBM COBOL for MVS and VM 1.2.1.

ID DIVISION.
PROGRAM-ID. A.
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

_(reply depth: 4)_

- **From:** "spk..." <ua-author-17071408@usenetarchives.gap>
- **Date:** 1997-07-26T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p9@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p8@usenetarchives.gap> <gap-c1c91fcdf4-p9@usenetarchives.gap>`

```

But don't forget the rules (from the original post):
›› What is the shortest COBOL program you can write? RULES:
››
›› * It must be portable, i.e. ANS standard COBOL.
›› * It must take an input and make an output.



On Fri, 25 Jul 1997 03:41:35 GMT, jody-.··@wor··t.net (Jody &
Mimi Richardson) wrote:

› Actually, I believe with the 85 Standard, the only thing required in a
› COBOL program is the Identification and Environment division headers.
…[3 more quoted lines elided]…
› Jody Richardson
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

_(reply depth: 4)_

- **From:** "donts..." <ua-author-8744626@usenetarchives.gap>
- **Date:** 1997-07-27T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p9@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p8@usenetarchives.gap> <gap-c1c91fcdf4-p9@usenetarchives.gap>`

```

On Fri, 25 Jul 1997 03:41:35 GMT, jody-.··@wor··t.net (Jody &
Mimi Richardson) wrote:

› Actually, I believe with the 85 Standard, the only thing required in a
› COBOL program is the Identification and Environment division headers.
…[3 more quoted lines elided]…
› Jody Richardson
The Environment Division is optional but Program-id is not. The
shortest legal program remains:

identification division.
program-id. shorty.

George Trudeau, Town of Falmouth
"Visit our short COBOL program at
http://www.town.falmouth.ma.us/hello.html"
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

_(reply depth: 5)_

- **From:** "steve and janice schindler" <ua-author-17072714@usenetarchives.gap>
- **Date:** 1997-07-28T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p14@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p8@usenetarchives.gap> <gap-c1c91fcdf4-p9@usenetarchives.gap> <gap-c1c91fcdf4-p14@usenetarchives.gap>`

```

Don't forget IDENTIFICATION DIVISION can be abbreviated as ID DIVISION.
```

###### ↳ ↳ ↳ Re: What's the shortest possible COBOL program?

_(reply depth: 6)_

- **From:** "donts..." <ua-author-8744626@usenetarchives.gap>
- **Date:** 1997-08-03T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1c91fcdf4-p15@usenetarchives.gap>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com> <gap-c1c91fcdf4-p4@usenetarchives.gap> <gap-c1c91fcdf4-p8@usenetarchives.gap> <gap-c1c91fcdf4-p9@usenetarchives.gap> <gap-c1c91fcdf4-p14@usenetarchives.gap> <gap-c1c91fcdf4-p15@usenetarchives.gap>`

```

On Tue, 29 Jul 1997 17:02:02 -0500, "Steve and Janice Schindler"
wrote:

› Don't forget IDENTIFICATION DIVISION can be abbreviated as ID DIVISION.
›
›
Only as a non-standard extension, or perhaps in this case it's a
non-standard contraction.

George Trudeau
```

#### ↳ Re: What's the shortest possible COBOL program?

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1c91fcdf4-p17@usenetarchives.gap>`
- **In-Reply-To:** `<33cb0b63.20334013@news.dt1.sdca.home.com>`
- **References:** `<33cb0b63.20334013@news.dt1.sdca.home.com>`

```

In a sudden flurry of activity, spk··.@c··.com wrote:
› Just for fun:
›  I once taught a COBOL class, and one of the exercises was this:
…[11 more quoted lines elided]…
› P.S. No fair cloning an existing program!  ;-)
IDENTIFICATION DIVISION.

PROGRAM-ID. SHORT.

ENVIRONMENT DIVISION.

INPUT-OUTPUT SECTION.

FILE-CONTROL.

SELECT INPUT-FILE ASSIGN TO UT-S-INPT.
SELECT PRINT-FILE ASSIGN TO UT-S-PRINT.

DATA DIVISION.

FILE SECTION.

FD INPUT-FILE.
01 INPUT-REC PIC X(80).

FD PRINT-FILE
LABEL RECORDS ARE OMITTED.
01 PRINT-LINE PIC X(80).
WORKING STORAGE SECTION.
01 WS-RECORD PIC X(80).
PROCEDURE DIVISION.

OPEN INPUT-FILE PRINT-FILE.
READ INPUT-FILE INTO WS-RECORD.
WRITE PRINT-LINE FROM WS-RECORD.
CLOSE INPUT-FILE PRINT-FILE.
STOP RUN.

Well, there you go. If you want to make it shorter by bytes, then
get rid of the WS-RECORD definition, change the READ INTO to a READ
and the WRITE FROM to a WRITE, then just MOVE INPUT-REC TO PRINT-LINE.

If you really want to get technical about the INPUT/OUTPUT
rules, this would be shorter:

IDENTIFICATION DIVISION.
PROGRAM-ID. SHORTER.
ENVIRONMENT DIVISION.

DATA DIVISION.

PROCEDURE DIVISION.
EXIBIT CURRENT-DATE.

STOP RUN.

Dave

The opinions expressed in this post are purely my own.
You may e-mail replies to: ren··.@d··.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
