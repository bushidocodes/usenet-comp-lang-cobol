[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# mf cobol question - student

_8 messages · 6 participants · 1999-09 → 1999-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Tutorials, books, learning`](../topics.md#learning)

---

### mf cobol question - student

- **From:** "Pat" <patp@cpinternet.com>
- **Date:** 1999-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WDfI3.546$Yn5.3038@newsfeed.slurp.net>`

```
Hi,

I'm using Micro Focus 2.0, and can't seem to get my DISPLAY statements in
color.  I've tried   -with foreground-color is XX-, which will work on one
line only.  If I try to make the next line (display) a different color, it
overwrites the first line.  I'm not sure if I can describe it properly -
here's the code....

200-DISPLAY-SALESPER-RECORD.
           DISPLAY " "
               WITH BLANK SCREEN
           DISPLAY "                 NAME: " SR-NAME
               WITH FOREGROUND-COLOR IS 5
           DISPLAY " "
           DISPLAY " "
           DISPLAY " "
           DISPLAY " "
           DISPLAY "   SALESPERSON REGION: " SR-REGION
               WITH FOREGROUND-COLOR IS 1

           DISPLAY " "

Now, I have a bunch of  -display " " - in there, trying to get some blank
lines in.  But still, the "salesperson region" overwrites the "name".  Also,
I tried to do two "with" clauses (blank screen and color) many different
ways and couldn't get a clean compile.

Hope this makes some sense, I'm not so good at explaining, I think.  Our
book doesn't really explain it and I'm just flying by the seat of my pants.
Our teacher isn't knowledgeable on MF, either.

Thanks,
Pat
```

#### ↳ Re: mf cobol question - student

- **From:** "Pat" <patp@cpinternet.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A3BI3.663$QP5.4552@newsfeed.slurp.net>`
- **References:** `<WDfI3.546$Yn5.3038@newsfeed.slurp.net>`

```
Thanks, Jimmy and Gael, for your help with my MF cobol color text display
question.  Using line and column works like a charm.  Didn't see that
covered in our textbook, either.  Now I get to be one up on the teacher!!

Thanks again,
Pat
```

##### ↳ ↳ Re: mf cobol question - student

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F2E9E5.1DA55BE3@home.com>`
- **References:** `<WDfI3.546$Yn5.3038@newsfeed.slurp.net> <A3BI3.663$QP5.4552@newsfeed.slurp.net>`

```
Pat wrote:
> 
> Thanks, Jimmy and Gael, for your help with my MF cobol color text display
…[4 more quoted lines elided]…
> Pat

We were both pleased to help. I assume you are only taking a cursory
look at SCREEN SECTION, and moving on to other things. However if you
are interested, contact Gael for some of the old DOS examples, I'm
thinking of ADMOUSE.CBL.

I can see them groaning at Newbury, "Here he goes again" - ADMOUSE.CBL
is the very program they didn't turn into an EXCELLENT OO/GUI demo
program, showing how to do sub-panes, two-dimensional, right-justified
entry fields and selecting a 'hit' using the mouse.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: mf cobol question - student

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4dJI3.9601$K33.71934@news1.mia>`
- **References:** `<WDfI3.546$Yn5.3038@newsfeed.slurp.net> <A3BI3.663$QP5.4552@newsfeed.slurp.net> <37F2E9E5.1DA55BE3@home.com>`

```
James J. Gavan wrote:
>Pat wrote:
>>
…[7 more quoted lines elided]…
>thinking of ADMOUSE.CBL.

Pat, you might want to check out chapter 25 of Sams "COBOL Unleashed".
It covers Screen Section with complete program examples.
```

###### ↳ ↳ ↳ Re: mf cobol question - student

_(reply depth: 4)_

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf0ca1$00d21860$8616063e@default>`
- **References:** `<WDfI3.546$Yn5.3038@newsfeed.slurp.net> <A3BI3.663$QP5.4552@newsfeed.slurp.net> <37F2E9E5.1DA55BE3@home.com> <4dJI3.9601$K33.71934@news1.mia>`

```


Judson McClendon <judmc123@bellsouth.net> wrote in article
<4dJI3.9601$K33.71934@news1.mia>...
> James J. Gavan wrote:
> >Pat wrote:
> >>
> >> Thanks, Jimmy and Gael, for your help with my MF cobol color text
display
> >> question.  Using line and column works like a charm.  Didn't see that
> >> covered in our textbook, either.  Now I get to be one up on the
teacher!!
> >
> >We were both pleased to help. I assume you are only taking a cursory
…[11 more quoted lines elided]…
> 

Yeah, I've got that book, kinda cool, it has some stuff about oracle that I
did'nt know.


Simon R Hart
Eaton.
```

#### ↳ Re: mf cobol question - student

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F1A370.BABF54DC@home.com>`
- **References:** `<WDfI3.546$Yn5.3038@newsfeed.slurp.net>`

```
Pat wrote:
> 

> here's the code....
> 
…[13 more quoted lines elided]…
>
Oooh. It's a while since I did anything for DOS-type display. Your code
looks like straight ANSI display, but it can't be, because you are using
Foreground-color etc - so it has to be SCREEN SECTION. Try using LIN and
COL values to move down the screen - unless I'm completely out of wack.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: mf cobol question - student

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 1999-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ssmra$rp6$1@hyperion.mfltd.co.uk>`
- **References:** `<WDfI3.546$Yn5.3038@newsfeed.slurp.net> <37F1A370.BABF54DC@home.com>`

```
Pat,
    The comments made by James below are absolutely correct (except for
SCREEN SECTION, you are not using that). To give you a little more
information, ANSI standard ACCEPTs and DISPLAYs are sent directly to the
screen at the current position, the position being updated after each.
Extended ACCEPTs and DISPLAYs ie those with colour information and/or
positioning are handled separately and the module used keeps its own current
position, so mixing ADIS and ANSI ACCEPTs is prone to exactly the sort of
peculiarities you have encountered. Therefore I would recommend that if you
want to use colour, remove the DISPLAY " " lines and add

AT LINE 4 COLUMN 1

or

AT 0401

(both do the same).

I hope this helps.



James J. Gavan wrote in message <37F1A370.BABF54DC@home.com>...
>Pat wrote:
>>
…[22 more quoted lines elided]…
>Jimmy, Calgary AB
```

#### ↳ Re: mf cobol question - student

- **From:** melifra@satlink.com (Melifra)
- **Date:** 1999-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u2eme$3dk$1@ul3.satlink.com>`
- **References:** `<WDfI3.546$Yn5.3038@newsfeed.slurp.net>`

```
 Usted "Pat" <patp@cpinternet.com> escribio :

>Hi,

>I'm using Micro Focus 2.0, and can't seem to get my DISPLAY statements in
>color.  I've tried   -with foreground-color is XX-, which will work on one
>line only.  If I try to make the next line (display) a different color, it
>overwrites the first line.  I'm not sure if I can describe it properly -
>here's the code....

>200-DISPLAY-SALESPER-RECORD.
>           DISPLAY " "
…[8 more quoted lines elided]…
>               WITH FOREGROUND-COLOR IS 1

>           DISPLAY " "

>Now, I have a bunch of  -display " " - in there, trying to get some blank
>lines in.  But still, the "salesperson region" overwrites the "name".  Also,
>I tried to do two "with" clauses (blank screen and color) many different
>ways and couldn't get a clean compile.

>Hope this makes some sense, I'm not so good at explaining, I think.  Our
>book doesn't really explain it and I'm just flying by the seat of my pants.
>Our teacher isn't knowledgeable on MF, either.

>Thanks,
>Pat

000100 01  TIT. 
  0200     05  LINE 01 COLUMN 01       PICTURE X(51) FROM
000300         'C.Rivadavia V.2000 (4/99)                          '
000400                     HIGHLIGHT   FOREGROUND-COLOR    07
000500                                 BACKGROUND-COLOR    01.
000600     05  LINE 01 COLUMN 52       PICTURE X(29) FROM
000700         '                      Melifra'
000800                     HIGHLIGHT   FOREGROUND-COLOR    07
000900                                 BACKGROUND-COLOR    01.
       01  BAS.
018600     05  LINE 24 COLUMN 01       PICTURE X(51) FROM
018700         '���������������������������������������������������'
018800                     HIGHLIGHT   FOREGROUND-COLOR    07
018900                                 BACKGROUND-COLOR    01.
019000     05  LINE 24 COLUMN 52       PICTURE X(29) FROM
019100         '�����������������������������'
019200                     HIGHLIGHT   FOREGROUND-COLOR    07
019300                                 BACKGROUND-COLOR    01.
****************************************************************************************************************
             Procedure Division.
             main section.
             main-01.
                           display TIT  BAS.
****************************************************************************************************************
                           display PROPA.
 
000100  01  PROPA.
000200     05  LINE 02 COLUMN 01       PICTURE X(51) FROM
000300         '���������������������������������������������������'
000400                     HIGHLIGHT   FOREGROUND-COLOR    03
000500                                 BACKGROUND-COLOR    01.
000600     05  LINE 02 COLUMN 52       PICTURE X(29) FROM
000700         '���������������������������ͻ'
000800                     HIGHLIGHT   FOREGROUND-COLOR    03
000900                                 BACKGROUND-COLOR    01.
001000     05  LINE 03 COLUMN 01       PICTURE X(26) FROM
001100         '������������������������ͻ'
001200                     HIGHLIGHT   FOREGROUND-COLOR    03
001300                                 BACKGROUND-COLOR    01.
001400     05  LINE 03 COLUMN 27       PICTURE X(24) FROM
001500         '������������������������'
001600                                 FOREGROUND-COLOR    02
001700                                 BACKGROUND-COLOR    01.
001800     05  LINE 03 COLUMN 51       PICTURE X(27) FROM
001900         '�������������������������ͻ'
002000                     HIGHLIGHT   FOREGROUND-COLOR    03
002100                                 BACKGROUND-COLOR    01.
002200     05  LINE 03 COLUMN 78       PICTURE X(01) FROM
002300         '�'
002400                                 FOREGROUND-COLOR    02
002500                                 BACKGROUND-COLOR    01.
002600     05  LINE 03 COLUMN 79       PICTURE X(01) FROM
002700         '�'
002800                                 FOREGROUND-COLOR    03
002900                                 BACKGROUND-COLOR    01.
003000     05  LINE 03 COLUMN 80       PICTURE X(01) FROM
003100         '�'
003200                     HIGHLIGHT   FOREGROUND-COLOR    03
003300                                 BACKGROUND-COLOR    01.
003400     05  LINE 04 COLUMN 01       PICTURE X(02) FROM
003500         '��'
003600                     HIGHLIGHT   FOREGROUND-COLOR    03
003700                                 BACKGROUND-COLOR    01.
003800     05  LINE 04 COLUMN 03       PICTURE X(23) FROM
003900         '���������������������Ŀ'
004000                     HIGHLIGHT   FOREGROUND-COLOR    07
004100                                 BACKGROUND-COLOR    01.
004200     05  LINE 04 COLUMN 26       PICTURE X(01) FROM
004300         '�'
004400                     HIGHLIGHT   FOREGROUND-COLOR    03
004500                                 BACKGROUND-COLOR    01.
004600     05  LINE 04 COLUMN 27       PICTURE X(01) FROM
004700         '�'
004800                                 FOREGROUND-COLOR    02
004900                                 BACKGROUND-COLOR    01.
005000     05  LINE 04 COLUMN 28       PICTURE X(23) FROM
005100         '�����������������������'
005200                                 FOREGROUND-COLOR    03
005300                                 BACKGROUND-COLOR    01.
005400     05  LINE 04 COLUMN 51       PICTURE X(01) FROM
005500         '�'
005600                     HIGHLIGHT   FOREGROUND-COLOR    03
005700                                 BACKGROUND-COLOR    01.
005800     05  LINE 04 COLUMN 52       PICTURE X(25) FROM
005900         '�����������������������Ŀ'
006000                     HIGHLIGHT   FOREGROUND-COLOR    07
006100                                 BACKGROUND-COLOR    01.
006200     05  LINE 04 COLUMN 77       PICTURE X(01) FROM
006300         '�'
006400                     HIGHLIGHT   FOREGROUND-COLOR    03
006500                                 BACKGROUND-COLOR    01.
006600     05  LINE 04 COLUMN 78       PICTURE X(01) FROM
006700         '�'
006800                                 FOREGROUND-COLOR    02

Regards - Saludos
Daniel Fernandez
E-mail: melifra@satlink.com
Comodoro Rivadavia - Chubut - Patagonia Argentina
             Capital del viento
==================================================
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
