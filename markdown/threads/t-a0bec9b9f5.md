[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Right Justify Alphanumeric Field

_10 messages · 5 participants · 2006-03_

---

### Right Justify Alphanumeric Field

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-17T22:06:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<121mubbqcqf6591@corp.supernews.com>`

```
This is another candidate for the FAQ.

-----
       1 input-field pic x(50).
       1 output-field pic x(50) justified right.
       1 p binary pic 9(4).
    ...
           move function length (input-field) to p
           perform varying p from p by -1
             until p < 2
                   or input-field (p:1) not = space
               continue
           end-perform
           move input-field (1:p) to output-field
-----
Tested using Micro Focus COBOL 3.2.24
with ANS85 flagging.
```

#### ↳ Re: Right Justify Alphanumeric Field

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-03-18T11:44:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com>`
- **References:** `<121mubbqcqf6591@corp.supernews.com>`

```
On Fri, 17 Mar 2006 22:06:04 -0500, "Rick Smith" <ricksmith@mfi.net>
wrote:

>This is another candidate for the FAQ.
>
…[12 more quoted lines elided]…
>-----
Non portable.

Not all compilers have implemented the intrinsic functions.
>Tested using Micro Focus COBOL 3.2.24
>with ANS85 flagging.
>
>


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Right Justify Alphanumeric Field

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-18T11:39:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<121odvt4139fo21@corp.supernews.com>`
- **References:** `<121mubbqcqf6591@corp.supernews.com> <7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com>`

```

"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com...
> On Fri, 17 Mar 2006 22:06:04 -0500, "Rick Smith" <ricksmith@mfi.net>
> wrote:
…[16 more quoted lines elided]…
> Non portable.

Well, I realize Fujitsu requires
            compute p = function length (input-field)

> Not all compilers have implemented the intrinsic functions.

Two of the four solutions given in the FAQ use intrinsic
functions, three use reference modification, and three use
lowercase letters. None of the solutions will work on a
compiler that pre-dates COBOL 85.

> >Tested using Micro Focus COBOL 3.2.24
> >with ANS85 flagging.

Here is the COBOL 74 code.
-----
      $SET FLAG"ANS74" FLAGAS"S"
       IDENTIFICATION DIVISION.
       PROGRAM-ID. RJUST74.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. PC.
       OBJECT-COMPUTER. PC.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  P COMP PIC 9(4) VALUE 50.
       01  INPUT-FIELD.
           02 INPUT-CHAR PIC X OCCURS 1 TO 50 DEPENDING ON P.
       01  OUTPUT-FIELD PIC X(50) JUSTIFIED RIGHT.
       PROCEDURE DIVISION.
       BEGIN.
           PERFORM DUMMY VARYING P FROM P BY -1
             UNTIL P < 2
                   OR INPUT-CHAR (P) NOT = SPACE.
           MOVE INPUT-FIELD TO OUTPUT-FIELD.
           MOVE 50 TO P
           DISPLAY OUTPUT-FIELD.
           STOP RUN.
       DUMMY.
           EXIT.
-----
This was tested by using different values of INPUT-FIELD
within the Animator (R).
```

###### ↳ ↳ ↳ Re: Right Justify Alphanumeric Field

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-03-18T23:12:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hd4p121dru6uj6glochs46u36bteg7iaac@4ax.com>`
- **References:** `<121mubbqcqf6591@corp.supernews.com> <7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com> <121odvt4139fo21@corp.supernews.com>`

```
On Sat, 18 Mar 2006 11:39:21 -0500, "Rick Smith" <ricksmith@mfi.net>
wrote:

>
>"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
…[29 more quoted lines elided]…
>compiler that pre-dates COBOL 85.
Use of intrinsic functions has nothing to do with a compiler being
COBOL-85 compliant or not.
Intrinsic functions were introduced afterwards, and are part of the
"1989 Intrinsic Functions amendment". I am sure Bill or another of the
standards group will be able to mention the correct document and date
of introduction.

So I still say, and now I highlight, that your code is not portable
between FULLY 1985 compliant compilers.


Snip remainding 1974 code.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Right Justify Alphanumeric Field

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-18T20:31:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<121pd5bihqdb069@corp.supernews.com>`
- **References:** `<121mubbqcqf6591@corp.supernews.com> <7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com> <121odvt4139fo21@corp.supernews.com> <hd4p121dru6uj6glochs46u36bteg7iaac@4ax.com>`

```

"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:hd4p121dru6uj6glochs46u36bteg7iaac@4ax.com...
> On Sat, 18 Mar 2006 11:39:21 -0500, "Rick Smith" <ricksmith@mfi.net>
> wrote:
…[41 more quoted lines elided]…
> between FULLY 1985 compliant compilers.

Ok? I accept that there may be compilers that conform
to X3.23-1985 and not conform to X3.23a-1989. What
I do not understand is why you seem to object to the code
being a "candidate for the FAQ" when there are already two
solutions in the FAQ that fail *your test* for portability;
even though the code does not fail any test required in the
FAQ.
```

###### ↳ ↳ ↳ Re: Right Justify Alphanumeric Field

_(reply depth: 5)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-03-19T14:11:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32pq125rg920vuapqeq5biut1hcqt9mhdn@4ax.com>`
- **References:** `<121mubbqcqf6591@corp.supernews.com> <7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com> <121odvt4139fo21@corp.supernews.com> <hd4p121dru6uj6glochs46u36bteg7iaac@4ax.com> <121pd5bihqdb069@corp.supernews.com>`

```
On Sat, 18 Mar 2006 20:31:28 -0500, "Rick Smith" <ricksmith@mfi.net>
wrote:

>
>"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
>news:hd4p121dru6uj6glochs46u36bteg7iaac@4ax.com...
>> On Sat, 18 Mar 2006 11:39:21 -0500, "Rick Smith" <ricksmith@mfi.net>
snip

>Ok? I accept that there may be compilers that conform
>to X3.23-1985 and not conform to X3.23a-1989. What
…[4 more quoted lines elided]…
>FAQ.
Sorry if you have taken it that way. I was not objecting to this being
added to the FAQ. 

I was originally stating that it was not portable code accross 85
compilers (which you flagging "with ANS85 flagging." seemed to suggest
would work with all 85 compliant compilers.

My second reply to you was just to highlight this fact. nothing else.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ What Standard? (was: Right Justify Alphanumeric Field

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-03-19T17:18:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZngTf.30091$Tl3.10095@fe06.news.easynews.com>`
- **References:** `<121mubbqcqf6591@corp.supernews.com> <7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com> <121odvt4139fo21@corp.supernews.com> <hd4p121dru6uj6glochs46u36bteg7iaac@4ax.com> <121pd5bihqdb069@corp.supernews.com> <32pq125rg920vuapqeq5biut1hcqt9mhdn@4ax.com>`

```
"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message 
news:32pq125rg920vuapqeq5biut1hcqt9mhdn@4ax.com...
> On Sat, 18 Mar 2006 20:31:28 -0500, "Rick Smith" <ricksmith@mfi.net>
> wrote:
>
<snip>>
> I was originally stating that it was not portable code accross 85
> compilers (which you flagging "with ANS85 flagging." seemed to suggest
…[5 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com

Interesting question:  What does "85 Standard compiler" mean today?

1) "Third Standard COBOL" was amended twice.  As far as ANSI (and ISO) go, there 
was only "amended Third Standard COBOL" - as of 1991 and later.

2) The Intrinsic Functions  Module was an OPTIONAL module in Amended Third 
Standard COBOL.  HOWEVER, it was a required module in the (US only) FIPS 
Standard.

3) As far as ANSI and ISO go, there is no longer any recognized "85 Standard" 
(or Amended Third Standard COBOL).  The only CURRENTLY recognized Standard is 
the '02 Standard.  (For which there is a published and approved ISO, not ANSI, 
Technical Report - which is NOT the same thing as an "amendment").

4) Referring to an "85 Standard compiler" has as much meaning today as referring 
to a '74 or '68 Standard compiler.  It has whatever meaning the vendor gives it, 
as it has no "Standard" (or portable) definition.

5) During the life time of the "'85 Standard" - one needed to tell which level 
(subset) of the Standard was conformed to AS well as which optional modules were 
included.   The only "truly portable" source code would conform to the minimum 
subset with no optional modules.  I don't personally remember ANY compiler that 
was that limited, but there might have been one.  (I know there were some 
intermediate subset compilers with few or no optional modules).

P.S.  I know that Micro Focus documents what both
  FLAG"ANS85"
     and
  FLAGSTD

used for flagging.
```

###### ↳ ↳ ↳ Re: What Standard? (was: Right Justify Alphanumeric Field

_(reply depth: 7)_

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2006-03-21T06:20:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dvo5ve$6o2$1@theodyn.ncf.ca>`
- **References:** `<121mubbqcqf6591@corp.supernews.com> <7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com> <121odvt4139fo21@corp.supernews.com> <hd4p121dru6uj6glochs46u36bteg7iaac@4ax.com> <121pd5bihqdb069@corp.supernews.com> <32pq125rg920vuapqeq5biut1hcqt9mhdn@4ax.com> <ZngTf.30091$Tl3.10095@fe06.news.easynews.com>`

```
"William M. Klein" (wmklein@nospam.netcom.com) writes:
> 
> 4) Referring to an "85 Standard compiler" has as much meaning today as referring 
> to a '74 or '68 Standard compiler.  It has whatever meaning the vendor gives it, 
> as it has no "Standard" (or portable) definition.

All those versions could be confusing, particularly to comp sci undergrads
with hearing deficits or attention deficits.

I remember coming across 
   Cobalt-60
as one response when marking mid-terms for a prof who had asked students
to name 3 high level languages.
```

##### ↳ ↳ Re: Right Justify Alphanumeric Field

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-03-18T10:42:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<121oe3p5dgveq9b@news.supernews.com>`
- **References:** `<121mubbqcqf6591@corp.supernews.com> <7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com>`

```
Frederico Fonseca wrote:
> On Fri, 17 Mar 2006 22:06:04 -0500, "Rick Smith" <ricksmith@mfi.net>
> wrote:
…[18 more quoted lines elided]…
> Not all compilers have implemented the intrinsic functions.

And, of course, doesn't handle imbedded spaces. However,

COMPUTE p = FUNCTION STORED-CHAR-LENGTH(input-field)
MOVE input-field(1:p) TO output-field

works okay for imbedded spaces (assuming you have certain functions).

Alternatively,

INSPECT input-field TALLYING p FOR CHARCTERS BEFORE 'bb' (double-blank)

would work, unless you had an imbedded double blank.
```

###### ↳ ↳ ↳ Re: Right Justify Alphanumeric Field

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-03-18T12:30:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<121oh0qdf1aefd1@corp.supernews.com>`
- **References:** `<121mubbqcqf6591@corp.supernews.com> <7pqn125975aro59cj2gmtlgbks3kavonj5@4ax.com> <121oe3p5dgveq9b@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message
news:121oe3p5dgveq9b@news.supernews.com...
> Frederico Fonseca wrote:
> > On Fri, 17 Mar 2006 22:06:04 -0500, "Rick Smith" <ricksmith@mfi.net>
…[21 more quoted lines elided]…
> And, of course, doesn't handle imbedded spaces.

Huh!? Are you saying that compilers that don't implement
intrinsic functions, don't handle imbedded spaces?

You cannot be referring to the code!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
