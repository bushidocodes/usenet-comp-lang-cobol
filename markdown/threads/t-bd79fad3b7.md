[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Data Decimal Error

_8 messages · 5 participants · 2008-06_

---

### Data Decimal Error

- **From:** msalatino2002@yahoo.com
- **Date:** 2008-06-18T21:58:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com>`

```
COBOL group, I need your help.

I am trying to used a parm (packed decimal) and move it to a zoned
decimal field.  I keep getting a data decimal error as the end result.

Here are code extracts:

      WORKING-STORAGE SECTION.

       01  WORK-DATE-IN.
            05  WS-MONTH          PIC 9(02).
            05  WS-DAY               PIC 9(02).
            05  WS-YEAR             PIC 9(03).

       01  WORK-DATE-OUT
            05  WS-YEAR             PIC 9(03).
            05  WS-MONTH          PIC 9(02).
            05  WS-DAY               PIC 9(02).
       :
       :
       01  P-RPTPARMS.
       :
       :
         03  P-RXRXDATTO         PIC S9(7)  VALUE ZEROS..

       LINKAGE SECTION.
       01  RPTPARMS.
       :
       :
         03  RXRXDATTO             PIC S9(7)  COMP-3.
      *       RX DATE TO
       :
       :

       PROCEDURE DIVISION USING RPTPARMS,  TERMINALID, USERID,
                                                      DRV-FIELDS.
       :
       :
            MOVE RXRXDATTO    TO WORK-DAT-OUT.
      * This is where my program crashes
            IF WS-YEAR-O < 50
               ADD 100 TO WS-YEAR-O.
            :
            :
            STOP RUN.

What do you think?  Should I move RXRXDATTO to P-RXRXDATTO and then
move P-PXRXDATTO?

Thanks for helping me out!!!

Best regards,

Mark
```

#### ↳ Re: Data Decimal Error

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-06-18T22:39:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12576203-5844-4036-82b2-97d5b587ecbd@x1g2000prh.googlegroups.com>`
- **References:** `<5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com>`

```
On Jun 19, 4:58 pm, msalatino2...@yahoo.com wrote:
> COBOL group, I need your help.
>
…[36 more quoted lines elided]…
>             MOVE RXRXDATTO    TO WORK-DAT-OUT.

RXRXDATTO is 4 bytes long. The MOVE is to a group field that is 7
bytes long.The first 4 bytes will contain packed bytes which will not
be valid for the fields, the last 3 will be spaces.

>       * This is where my program crashes
>             IF WS-YEAR-O < 50
>                ADD 100 TO WS-YEAR-O.

WS-YEAR-O (which is not actually defined that way) contains non-
numeric data.

>             :
>             :
…[3 more quoted lines elided]…
> move P-PXRXDATTO?

That will make a difference because P-RXRXDATTO is 7 bytes long and
the MOVE to WORK-DATE-OUT will leave those fields with correct numeric
data.


> Thanks for helping me out!!!
>
> Best regards,
>
> Mark
```

##### ↳ ↳ Re: Data Decimal Error

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-19T07:47:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ozs6k.4863$L_.2803@flpi150.ffdc.sbc.com>`
- **References:** `<5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com> <12576203-5844-4036-82b2-97d5b587ecbd@x1g2000prh.googlegroups.com>`

```
It's not just the number of bytes, it's the format. MOVEing a COMP-3 numeric 
to a DISPLAY (zoned) numeric as a group (character) move puts invalid 
characters in those display/zoned  fields.

You have to unpack the input number using arithmetic and move it to the
individual pieces.
eg, if the PIC 9(07) COMP-3 field is YYMMDD

  COMPUTE    WS-YY =      YYMMDD / 10000
  COMPUTE    WS-MM =        (YYMMDD MOD 10000) / 100
  COMPUTE    WS-DD  =   YYMMDD MOD 10000


MCM
```

###### ↳ ↳ ↳ Re: Data Decimal Error

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-06-19T14:38:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5194491d-2150-455a-988b-1966114f30e4@w34g2000prm.googlegroups.com>`
- **References:** `<5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com> <12576203-5844-4036-82b2-97d5b587ecbd@x1g2000prh.googlegroups.com> <ozs6k.4863$L_.2803@flpi150.ffdc.sbc.com>`

```
On Jun 20, 12:47 am, "Michael Mattias" <mmatt...@talsystems.com>
wrote:
> It's not just the number of bytes, it's the format. MOVEing a COMP-3 numeric
> to a DISPLAY (zoned) numeric as a group (character) move puts invalid
> characters in those display/zoned  fields.

That was covered in my message

> You have to unpack the input number using arithmetic and move it to the
> individual pieces.
…[4 more quoted lines elided]…
>   COMPUTE    WS-DD  =   YYMMDD MOD 10000

No, you don't _HAVE_TO_ use arithmetic.  A MOVE to a display numeric,
as suggested, will unpack it to characters and then a group MOVE, or a
redefine, will leave it with valid numeric data in the subsidiary
fields.
```

###### ↳ ↳ ↳ Re: Data Decimal Error

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-20T00:04:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3es63$2bl$1@reader2.panix.com>`
- **References:** `<5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com> <12576203-5844-4036-82b2-97d5b587ecbd@x1g2000prh.googlegroups.com> <ozs6k.4863$L_.2803@flpi150.ffdc.sbc.com> <5194491d-2150-455a-988b-1966114f30e4@w34g2000prm.googlegroups.com>`

```
In article <5194491d-2150-455a-988b-1966114f30e4@w34g2000prm.googlegroups.com>,
Richard  <riplin@azonic.co.nz> wrote:
>On Jun 20, 12:47�am, "Michael Mattias" <mmatt...@talsystems.com>
>wrote:

[snip]

>> You have to unpack the input number using arithmetic and move it to the
>> individual pieces.
…[6 more quoted lines elided]…
>No, you don't _HAVE_TO_ use arithmetic.

Mr Plinston, I barely know the reasons for *my* doing anything, let alone 
anyone else... but it might be, possibly, that Mr Mattias went a bit 
overboard while providing a sarcastic-yet-functional solution to a 
question he saw as a variant of 'please do my job for me'.

DD
```

###### ↳ ↳ ↳ Re: Data Decimal Error

_(reply depth: 5)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-20T07:20:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MoN6k.8956$jI5.6355@flpi148.ffdc.sbc.com>`
- **References:** `<5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com> <12576203-5844-4036-82b2-97d5b587ecbd@x1g2000prh.googlegroups.com> <ozs6k.4863$L_.2803@flpi150.ffdc.sbc.com> <5194491d-2150-455a-988b-1966114f30e4@w34g2000prm.googlegroups.com> <g3es63$2bl$1@reader2.panix.com>`

```
<docdwarf@panix.com> wrote in message news:g3es63$2bl$1@reader2.panix.com...
> In article 
> <5194491d-2150-455a-988b-1966114f30e4@w34g2000prm.googlegroups.com>,
…[19 more quoted lines elided]…
> question he saw as a variant of 'please do my job for me'.

Ok, so I missed that possibility. I was focused  on the OPs working-storage, 
which did not use a DISPLAY numeric elementary item as the destination 
operand.

And DD, my effort at assistance was neither sarcastic nor overboard.. at 
least those were not my intentions.

Gimme a break, huh? I ain't wrote no COBOL since 2001.  This group is how I 
avoid TOTAL brain dump... assuming I can find posts relating to the COBOL 
programming language amongst all the philosophy, religion, politics... and 
sadly, name-calling.


MCM
```

###### ↳ ↳ ↳ Re: Data Decimal Error

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-20T12:50:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g3g93a$4bc$1@reader2.panix.com>`
- **References:** `<5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com> <5194491d-2150-455a-988b-1966114f30e4@w34g2000prm.googlegroups.com> <g3es63$2bl$1@reader2.panix.com> <MoN6k.8956$jI5.6355@flpi148.ffdc.sbc.com>`

```
In article <MoN6k.8956$jI5.6355@flpi148.ffdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:g3es63$2bl$1@reader2.panix.com...
>> In article 
…[27 more quoted lines elided]…
>least those were not my intentions.

Ha... that's what they *always* say, when they get caught.  Think of it as 
a compliment, of sorts; such an error and the resulting unnecessary code 
(there was some 'Look, Ma, I'm a Programmer!' code posted during Y2K 
remediation-time that involved such jiggery-pokery) might have, coming 
from one such as you, been sarcasm... that indicates a higher estimation 
of your abilities.

DD
```

#### ↳ Re: Data Decimal Error

- **From:** "billious" <billious_1954@hotmail.com>
- **Date:** 2008-06-19T21:31:48+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<485a60eb$0$20808$a82e2bb9@reader.athenanews.com>`
- **References:** `<5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com>`

```

<msalatino2002@yahoo.com> wrote in message 
news:5a850a4a-4088-40b6-8ee1-f116f8485ffb@y38g2000hsy.googlegroups.com...
> COBOL group, I need your help.
>
…[51 more quoted lines elided]…
> Mark

Personally, I'd use

       01  WORK-DATE-OUT
            05  WS-YEAR             PIC 9(03).
            05  WS-MONTH          PIC 9(02).
            05  WS-DAY               PIC 9(02).
       01  WORK-DATE-OUT-9
          REDEFINES  WORK-DATE-OUT PIC 9(07).

then

           MOVE RXRXDATTO    TO WORK-DATE-OUT-9.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
