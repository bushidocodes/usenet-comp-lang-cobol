[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to do data validation on special characters!

_9 messages · 8 participants · 2000-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to do data validation on special characters!

- **From:** lany0001@my-deja.com
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gav1s$jfq$1@nnrp1.deja.com>`

```
Hi,there:
I am new to Cobol and I'm now doing data validation on an employee
record file. One of the data fields 'Employee Address' should only
contain letters and numbers, not special characters.
But how can I make my program identify those addresses with special
characters(example:%100@park&cross$30217).
The only way I can think of is to
1,list all the special characters in the value clause in the working-
storage section.
2.Then use INSPECT to tally special character(s)
3.If the result of tally >0, Then move the data to err-list.
Program excerpt:
WORKING-STORAGE SECTION.
...
01 SPECIAL-CHARACTERS.
   88  SPE-CHA     PIC X(24) VALUE '!@#$%^&*()-_+={}|[]\?/<>'.

PROCEDURE DIVISION.
...
   INSPECT IN-ADDRESS TALLYING SPE-CHA FOR ALL CHARACTERS
   IF SPE-CHA > 0
      MOVE IN-ADDRESS TO ERR-LIST
      PERFORM 300-ERR-RTN
   END IF.
But it didn't work. Is the syntex wrong or is my logic wrong? Is there
other way(better way) to do this?
Thanks in advance!
lany0001@unf.edu





Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: How to do data validation on special characters!

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39298455.93695B53@boeing.com>`
- **References:** `<8gav1s$jfq$1@nnrp1.deja.com>`

```

> Program excerpt:
> WORKING-STORAGE SECTION.
…[12 more quoted lines elided]…
> other way(better way) to do this?

two things -- your level 88 needs to be 24 one byte fields -- but you
can byte check your field (one at a time) checking for ranges of ok
values such as.  It seems there are always at least 3 correct ways to
solve any problem

evaluate byte
 when 0 through 9 
   ok (check next byte)
 when a through Z
   ok (check next byte)
 when spaces
   ok (check next byte)
 when other
   bad information
end-evaluate


	Susan A
```

##### ↳ ↳ Re: How to do data validation on special characters!

- **From:** "William C. Bub" <fathafluff@hotmail.com>
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3929c812_2@nebula.superior.net>`
- **References:** `<8gav1s$jfq$1@nnrp1.deja.com> <39298455.93695B53@boeing.com>`

```
Wouldn't it be safer to split:
    when a through Z
       ok (check next byte)
into two pieces:
   when a through z
      ok (check next byte)
   when A through Z
      ok (check next byte)
since there could possibly be invalid characters between z and A which
should be rejected.



> two things -- your level 88 needs to be 24 one byte fields -- but you
> can byte check your field (one at a time) checking for ranges of ok
…[15 more quoted lines elided]…
> Susan A
```

###### ↳ ↳ ↳ Re: How to do data validation on special characters!

- **From:** newsuser@linux2.johnmckown.net (John McKown)
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn8ijk2m.nkr.newsuser@linux2.johnmckown.net>`
- **References:** `<8gav1s$jfq$1@nnrp1.deja.com> <39298455.93695B53@boeing.com> <3929c812_2@nebula.superior.net>`

```
On Mon, 22 May 2000 19:52:11 -0400, William C. Bub 
<fathafluff@hotmail.com> wrote:
]>Wouldn't it be safer to split:
]>    when a through Z
]>       ok (check next byte)
]>into two pieces:
]>   when a through z
]>      ok (check next byte)
]>   when A through Z
]>      ok (check next byte)
]>since there could possibly be invalid characters between z and A which
]>should be rejected.
]>
 
One major problem with that. In EBCDIC (OS/390 character set), the alphabetic
characters are grouped (a..i) (j..r) (s..z) (A..I) (J..R) (S..Z) with other
non-alphabetics between the groups!
```

#### ↳ Re: How to do data validation on special characters!

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39298df2.76821918@news.cox-internet.com>`
- **References:** `<8gav1s$jfq$1@nnrp1.deja.com>`

```
I agree with John. Set up a class in Special names then check your
field against it:

ie 

if data-field not alphanumeric-x.

Alphanumeric-x is the class you define in special names.


On Mon, 22 May 2000 09:35:56 GMT, lany0001@my-deja.com wrote:

>Hi,there:
>I am new to Cobol and I'm now doing data validation on an employee
…[32 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: How to do data validation on special characters!

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YzhW4.2868$kx3.331465@news2.mia>`
- **References:** `<8gav1s$jfq$1@nnrp1.deja.com>`

```
First off, those are not valid addresses.
They may be valid EMail addresses.
Redefine the field as a PIC X occurs n times.
Loop thru checking each position for
IF ws-name-char(WS-SUB) not numeric
  and not alphabetic
    move SPACE to ws-name-char(WS-SUB)

<lany0001@my-deja.com> wrote in message news:8gav1s$jfq$1@nnrp1.deja.com...
> Hi,there:
> I am new to Cobol and I'm now doing data validation on an employee
…[32 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: How to do data validation on special characters!

- **From:** newsuser@linux2.johnmckown.net (John McKown)
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn8ii7j2.mcl.newsuser@linux2.johnmckown.net>`
- **References:** `<8gav1s$jfq$1@nnrp1.deja.com>`

```
On Mon, 22 May 2000 09:35:56 GMT, lany0001@my-deja.com 
<lany0001@my-deja.com> wrote:
>Hi,there:
>I am new to Cobol and I'm now doing data validation on an employee
…[3 more quoted lines elided]…
>characters(example:%100@park&cross$30217).
	[snip]
Use a class test. I don't have my COBOL manual right here, but I think you
can simply do something like:

IF VARIABLE-NAME IS NOT ALPHABETIC THEN
  ... error code ..
END-IF

Hope this gets you on the right course.

John
```

#### ↳ Re: How to do data validation on special characters!

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gb9mg$1aj$1@news.igs.net>`
- **References:** `<8gav1s$jfq$1@nnrp1.deja.com>`

```
The reason that your 88 did not work is that you have it defined wrong.  You
do not want an X(24) field, you want 24 X(1) fields.

lany0001@my-deja.com wrote in message <8gav1s$jfq$1@nnrp1.deja.com>...
>Hi,there:
>I am new to Cobol and I'm now doing data validation on an employee
…[32 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: How to do data validation on special characters!

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gdbc5$4km$1@news.inet.tele.dk>`
- **References:** `<8gav1s$jfq$1@nnrp1.deja.com>`

```
Hey, you've got yourself a quit complex task here.
Try to write down all the rules for acceptable data before coding your
program.
Something like:

1. Letters A-Z, a-z and Space are valid
2. Quote is valid after a letter
3. '&' is valid after a letter and perhaps a space
4. Dots are valid after a letter
5. etc. etc.etc.

If you really look at it, you must admit that it can be a hell of a task for
someone new to cobol. Are you shure that you got it right? Doesn't the input
have any structure you could benefit from?

To me et looks as if you have taken a customer file into an editor, and that
the structure could be

01    Cust-rec.
    05 Cust-id        pic 9(5)  comp.
    05 Cust-name   pic X(20).
    05 Credit-limit   pic X(10).
:-)))

This is probably not the case, but what I am trying to tell you is: "Study
the input before creating the program logic".

Let us see what you find out to do.

Regards
Ib
lany0001@my-deja.com skrev i meddelelsen <8gav1s$jfq$1@nnrp1.deja.com>...
>Hi,there:
>I am new to Cobol and I'm now doing data validation on an employee
…[32 more quoted lines elided]…
>Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
