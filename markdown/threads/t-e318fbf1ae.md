[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Lower case to upper case conversion

_9 messages · 6 participants · 2003-04_

---

### Lower case to upper case conversion

- **From:** "Beverly" <Beverly.Owens@work.com>
- **Date:** 2003-04-03T08:49:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com>`

```
I'm processing a file from a PC system and the descriptions are in upper
and lower case.  I would like to transform them to all upper case before
posting to the mainframe database.  Is there an easy way to do this besides
running each character thru a conversion?

TIA
Beverly
```

#### ↳ Re: Lower case to upper case conversion

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2003-04-03T14:06:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030403090636.04330.00000035@mb-fh.aol.com>`
- **References:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com>`

```
Beverly Owens writes ...

>I'm processing a file from a PC system and the descriptions are in upper
>and lower case.  I would like to transform them to all upper case before
>posting to the mainframe database.  

Why? Mainframes work with mixed case data just fine.

> Is there an easy way to do this besides
>running each character thru a conversion?

move function upper-case(instring) to outstring


Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: Lower case to upper case conversion

- **From:** "Beverly" <Beverly.Owens@work.com>
- **Date:** 2003-04-03T09:29:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6hgg3$qo6$1@mailgate2.lexis-nexis.com>`
- **References:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com> <20030403090636.04330.00000035@mb-fh.aol.com>`

```

"S Comstock" <scomstock@aol.com> wrote in message
news:20030403090636.04330.00000035@mb-fh.aol.com...
> Beverly Owens writes ...
>
…[4 more quoted lines elided]…
> Why? Mainframes work with mixed case data just fine.

It works fine but looks a little sloppy on reports when descriptions are
mixed between all upper and a mix of upper and lower.

Thanks..................
>
> > Is there an easy way to do this besides
…[14 more quoted lines elided]…
> USA
```

#### ↳ Re: Lower case to upper case conversion

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-03T15:17:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6hjan$okv$1@peabody.colorado.edu>`
- **References:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com>`

```

On  3-Apr-2003, "Beverly" <Beverly.Owens@work.com> wrote:

> I'm processing a file from a PC system and the descriptions are in upper
> and lower case.  I would like to transform them to all upper case before
> posting to the mainframe database.  Is there an easy way to do this besides
> running each character thru a conversion?

One way is to use your mainframe editor to convert it.   For instance if you
edit it in TSO, you can use the command line command:
C P'<' P'>' ALL
```

#### ↳ Re: Lower case to upper case conversion

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2003-04-03T11:04:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6hll3$3ck$1@slb3.atl.mindspring.net>`
- **References:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com>`

```
Hello,

        When you're about to convert them, are they still ASCII or have they
already been converted to EBCDIC?

        What version of COBOL are you executing?

        With the advent of COBOL2, the INSPECT command included the
CONVERTING keyword. With CONVERTING, if you setup your FROM and TO
character-strings as literals, COBOL will generate a single "TR" (Translate)
instruction, thus saving your a CALL to a COBOL Run-Time module. And yes,
I've been referred to as a CPU-Nazi ;o)

        With the advent of COBOL/370, the FUNCTION LOWER-CASE and UPPER-CASE
were added but the INSPECT CONVERTING with literals (COBOL2) is still more
efficient.

        Prior to COBOL2, you could convert from low-case to upper-case using
binary arithmetic, with the code being executed in-line.

        03  WS-LETTER PIC S9(04) COMP.
*
        MOVE +129 TO WS-LETTER.
        ADD +64 TO WS-LETTER.
*
        In the above example, decimal 129 (X'81') is a lower-case 'a' in
EBCDIC. By adding +64, it then becomes an upper-case 'A' (X'C1')

        Or you can use a table.

        03  WS-LETTER PIC S9(04) COMP VALUE +162.
        03  WS-LETTER-TBL-REC.
               05  FILLER PIC X(13) VALUE 'ABCDEFGHIJKLM'.
               05  FILLER PIC X(13) VALUE 'NOPQRSTUVWXYZ'.
        03  WS-LETTER-TBL REDEFINES WS-LETTER-TBL-REC
                                               OCCURS 26 TIMES PIC X(01).
        03  WS-SUB PIC S9(04) COMP.
*
        IF (WS-LETTER NOT <  129 AND
              WS-LETTER NOT > 137)
              COMPUTE WS-SUB = (WS-LETTER - 128)
        ELSE
               IF (WS-LETTER NOT <  145 AND
                     WS-LETTER NOT >  153)
                     COMPUTE WS-SUB = (WS-LETTER - 135)
               ELSE
                      COMPUTE WS-SUB = (WS-LETTER - 143).
*
        At this point, WS-SUB points to the table entry that contains the
corresponding upper-case letter. In this example, WS-SUB is equal to 19
(lower-case and upper-case 's').

HTH....

Bill

"Beverly" <Beverly.Owens@work.com> wrote in message
news:b6he6c$q4h$1@mailgate2.lexis-nexis.com...
> I'm processing a file from a PC system and the descriptions are in upper
> and lower case.  I would like to transform them to all upper case before
> posting to the mainframe database.  Is there an easy way to do this
besides
> running each character thru a conversion?
>
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Lower case to upper case conversion

- **From:** "Beverly" <Beverly.Owens@work.com>
- **Date:** 2003-04-03T11:49:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6hom8$1ea$1@mailgate2.lexis-nexis.com>`
- **References:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com> <b6hll3$3ck$1@slb3.atl.mindspring.net>`

```
Thanks to everyone.  I ended up using the Inspect converting all lower-case
to upper-case.
Lower-case and Upper-case are the alphabet defined in working-storage in
upper and lower values.  I don't do a lot of coding anymore and hadn't run
across the need to do something like this for quite some time.

I guess I was just being picky about the lower case but it looks like crap
on the printed report with a mix of both......

Thanks
Beverly (who is now happy her report will be in all UPPER case)



"WOB" <wobconsult@sprynet.com> wrote in message
news:b6hll3$3ck$1@slb3.atl.mindspring.net...
> Hello,
>
>         When you're about to convert them, are they still ASCII or have
they
> already been converted to EBCDIC?
>
…[4 more quoted lines elided]…
> character-strings as literals, COBOL will generate a single "TR"
(Translate)
> instruction, thus saving your a CALL to a COBOL Run-Time module. And yes,
> I've been referred to as a CPU-Nazi ;o)
>
>         With the advent of COBOL/370, the FUNCTION LOWER-CASE and
UPPER-CASE
> were added but the INSPECT CONVERTING with literals (COBOL2) is still
more
> efficient.
>
>         Prior to COBOL2, you could convert from low-case to upper-case
using
> binary arithmetic, with the code being executed in-line.
>
…[38 more quoted lines elided]…
> > I'm processing a file from a PC system and the descriptions are in
upper
> > and lower case.  I would like to transform them to all upper case
before
> > posting to the mainframe database.  Is there an easy way to do this
> besides
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Lower case to upper case conversion

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-04-03T13:57:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E8CAE2D.38F3B633@attglobal.net>`
- **References:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com> <b6hll3$3ck$1@slb3.atl.mindspring.net> <b6hom8$1ea$1@mailgate2.lexis-nexis.com>`

```
Beverly,
I wonder why you think that BEVERLY looks better than Beverly?  You could just
as well have fixed the data that is all upper case to change each word so that
characters 2 thru n were lower case, leaving character 1 as is.  Then all the
data in your report would be consistent, and would conform to the rules for
written language.

We used only upper case in the "old days" because computer printers ran faster
if the print trains didn't include those other 26 characters.  That doesn't
apply to today's laser printers on just about any platform.

More nostalgia:
Your users don't refer to their reports as "tab runs", do they?  (I can still
find bins at work which are labeled "tab runs only", meaning that computer
generated reports are to be put here for recycling.  The term "tab run"
referred to reports that were generated using an EAM (Electronic Accounting
Machine) called a Tabulator, which could be programmed using wired connections,
somewhat resembling a telephone switchboard.  I started in this business in
1966, and the company still had a few EAM's around, and a few guys who just
loved to "wire" them.  I never learned how.)
=====
Beverly wrote:

> (snip)
> Thanks
> Beverly (who is now happy her report will be in all UPPER case)
```

#### ↳ Re: Lower case to upper case conversion

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-04-03T13:32:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0304031332.dbdbc31@posting.google.com>`
- **References:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com>`

```
"Beverly" <Beverly.Owens@work.com> wrote in message news:<b6he6c$q4h$1@mailgate2.lexis-nexis.com>...
> I'm processing a file from a PC system and the descriptions are in upper
> and lower case.  I would like to transform them to all upper case before
…[4 more quoted lines elided]…
> Beverly

Forgive me if this is a repeat.  You didn't mention COBOL but did
mention database.  If this is DB2 or some other SQL accessible
database maybe you can convert during the load using %UPPER%.
```

##### ↳ ↳ Re: Lower case to upper case conversion

- **From:** "Beverly" <Beverly.Owens@work.com>
- **Date:** 2003-04-03T17:26:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6icf3$3ln$1@mailgate2.lexis-nexis.com>`
- **References:** `<b6he6c$q4h$1@mailgate2.lexis-nexis.com> <bfdfc3e8.0304031332.dbdbc31@posting.google.com>`

```

"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0304031332.dbdbc31@posting.google.com...
> "Beverly" <Beverly.Owens@work.com> wrote in message
news:<b6he6c$q4h$1@mailgate2.lexis-nexis.com>...
> > I'm processing a file from a PC system and the descriptions are in
upper
> > and lower case.  I would like to transform them to all upper case
before
> > posting to the mainframe database.  Is there an easy way to do this
besides
> > running each character thru a conversion?
> >
…[5 more quoted lines elided]…
> database maybe you can convert during the load using %UPPER%.

Should have given more details.  I'm using COBOL II on an IDMS database.
In another post I mentioned I was able to use INSPECT with CONVERTING to
solve the problem.  It's been so long since I did much coding and I wasn't
sure which approach to take.

Thanks
Beverly
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
