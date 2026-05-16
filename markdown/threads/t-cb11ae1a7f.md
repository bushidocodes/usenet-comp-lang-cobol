[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# conflicting variables names on differents records.

_9 messages · 3 participants · 2006-04_

---

### conflicting variables names on differents records.

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-04-06T20:16:45+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44355b11$0$31480$ba620e4c@news.skynet.be>`

```
In that declaration I got many errors that cames from the ENR-LIV and 
ENR-TMP containing the same variables names I need for moving them in corr 
mode.
How to fix that ?

   DATA DIVISION.
        FILE SECTION.

         FD FLIVRE LABEL RECORD STANDARD;
            VALUE OF FILE-ID IS "FLIVRE.DAT".

         01 ENR-LIV.
>            02 CODE PIC X(5).
>            02 TITRE PIC X(30).
…[3 more quoted lines elided]…
>            02 QT-RESTE PIC 99; COMP-0.

         FD FTHEME LABEL RECORD STANDARD;
            VALUE OF FILE-ID IS "FTHEME.DAT".

         01 ENR-THE.
              02 DESC PIC X(20).
              02 RAYON PIC X(8).
              02 QT-MAX PIC 99.

        WORKING-STORAGE SECTION.

         01 ENR-TMP.
>            02 CODE PIC X(5).
>            02 TITRE PIC X(30).
…[3 more quoted lines elided]…
>            02 QT-RESTE PIC 99; COMP-0.
*-------------------------------------
0077:Unrecognizable element is ignored.  CODE
0077:Unrecognizable element is ignored.  TITRE
0077:Unrecognizable element is ignored.  AUTHEUR
0077:Unrecognizable element is ignored.  THEME
  77         PROCEDURE DIVISION.
** Compiling Procedure Division...
0211:Statement deleted due to erroneous syntax. TITRE
 212
0215:Statement deleted due to erroneous syntax. TITRE
 216
** Generating Object Code...
0001:/F/Key declaration of this file is not correct.
*-------------------------------------
Moreover I got that message for a flag I used elsewhere without that error 
msg.

>       77 FLG PIC 9.
>            88 OK PIC 9; VALUE 1.
>            88 KO PIC 9; VALUE 0.
*-------------------------------------
0074:Clause other than VALUE deleted.
0074:VALUE disallowed--OCCURS/REDEFINES/type/size conflict. VALUE
  74              88 OK PIC 9; VALUE 1.
0075:Clause other than VALUE deleted.
0075:VALUE disallowed--OCCURS/REDEFINES/type/size conflict. VALUE
  75              88 KO PIC 9; VALUE 0.
**-----------------------------------
```

#### ↳ Re: conflicting variables names on differents records.

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-04-06T12:58:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1144353508.544473.273660@g10g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<44355b11$0$31480$ba620e4c@news.skynet.be>`
- **References:** `<44355b11$0$31480$ba620e4c@news.skynet.be>`

```
Hello

It is always helpful to specify the compiler version (including the
supplier's name) and operating system that you are using.  If nothing
else, it may enable us to post links to relevant manuals when we don't
know the answers ourselves.  Bill Klein's FAQ, which was posted just
before your message has a good set of links, which probably include the
supplier of your compiler.

It would also help to post the contents of the Environment Division so
we can see the SELECT statements for the files.

I have never seen the VALUE OF clause of the FD statement in use (can't
even remember if there is one in the standard), it looks as though it
is there to do what a SELECT statement should do, but I haven't got and
don't know the relevant manual for your compiler.

You should check whether your compiler supports free-format coding
lines or requires fixed format.  If fixed format only, then the
starting column of each statement must be within the appropriate
margin, e.g. the 01 of an 01 level must start in columns 8-11 and the
02 of an 02 level must start in column 12 or greater up to 70/71.  Your
manual will explain which statements must start where.

For condition names i.e. 88 level items, the PIC clause is not allowed
and is not relevant,  since the reference is to the data name to which
it belongs in this case the condition names OK and KO belong to the
data name FLG.

Robert
```

##### ↳ ↳ Re: conflicting variables names on differents records.

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-04-06T23:32:13+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<443588e1$0$13564$ba620e4c@news.skynet.be>`
- **References:** `<44355b11$0$31480$ba620e4c@news.skynet.be> <1144353508.544473.273660@g10g2000cwb.googlegroups.com>`

```
Thanks for the answer, u were right about the level 88, it cannot contains
PIC's descriptions...
I use an old microsoft COBOL v2.20 compiler under XP, the  but I do not have
the manual. The margin rules are followed so the error is else.

Here's the environment...

      ENVIRONMENT DIVISION.
        CONFIGURATION SECTION.
         SOURCE-COMPUTER. CPU1.
         OBJECT-COMPUTER. CPU1.
         SPECIAL-NAMES.
      *    DECIMAL-POINTS IS COMA.
           CURRENCY SIGN IS 'E'.

        INPUT-OUTPUT SECTION.
         FILE-CONTROL.
           SELECT FLIVRE ASSIGN TO DISK
                  ORGANIZATION INDEXED;
                  ACCESS MODE DYNAMIC;
                  RECORD CODE;
                  ALTERNATE RECORD TITRE;
                  ALTERNATE RECORD AUTHEUR DUPLICATES;
                  ALTERNATE RECORD THEME DUPLICATES;
                  STATUS SLIV.

           SELECT FTHEME ASSIGN TO DISK
                  ORGANIZATION RELATIVE;
                  ACCESS MODE DYNAMIC;
                  RELATIVE CLE-THE;
                  STATUS STHE.
```

###### ↳ ↳ ↳ Re: conflicting variables names on differents records.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-04-07T03:39:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z9lZf.369322$fe6.298967@fe01.news.easynews.com>`
- **References:** `<44355b11$0$31480$ba620e4c@news.skynet.be> <1144353508.544473.273660@g10g2000cwb.googlegroups.com> <443588e1$0$13564$ba620e4c@news.skynet.be>`

```
I don't think I have ever seen a "RECORD" clause in a Select/Assign statement.
```

###### ↳ ↳ ↳ Re: conflicting variables names on differents records.

_(reply depth: 4)_

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-04-07T12:21:57+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44363d46$0$26309$ba620e4c@news.skynet.be>`
- **References:** `<44355b11$0$31480$ba620e4c@news.skynet.be> <1144353508.544473.273660@g10g2000cwb.googlegroups.com> <443588e1$0$13564$ba620e4c@news.skynet.be> <z9lZf.369322$fe6.298967@fe01.news.easynews.com>`

```
It is the short version for RECORD KEY IS "field"...

"William M. Klein" <wmklein@nospam.netcom.com> a �crit dans le message de 
news: z9lZf.369322$fe6.298967@fe01.news.easynews.com...
>I don't think I have ever seen a "RECORD" clause in a Select/Assign 
>statement.
…[43 more quoted lines elided]…
>
```

#### ↳ Re: conflicting variables names on differents records.

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-04-07T03:38:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q8lZf.369320$fe6.257594@fe01.news.easynews.com>`
- **References:** `<44355b11$0$31480$ba620e4c@news.skynet.be>`

```
"CODE" is a reserved word - which may be causing some of the problems.
```

##### ↳ ↳ Re: conflicting variables names on differents records.

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-04-07T12:33:16+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44363fed$0$13889$ba620e4c@news.skynet.be>`
- **References:** `<44355b11$0$31480$ba620e4c@news.skynet.be> <Q8lZf.369320$fe6.257594@fe01.news.easynews.com>`

```
I've tryed with another name "COD", but I got the same error msg...
maybe because we can't use an alternate key following a primary key ?
*------------------------------------------
?0211:Statement deleted due to erroneous syntax. TITRE
? 212
?0215:Statement deleted due to erroneous syntax. TITRE
? 216
*-------------------------------------------
207        I3-ANL1.
208           MOVE COD OF ENR-LIV TO COD OF ENR-TMP.
209           DISPLAY "TITRE ?".
210           ACCEPT TITRE OF ENR-LIV.
211           READ FLIVRE KEY IS TITRE.
212
213       CHK4.
214           ACCEPT TITRE OF ENR-LIV.
215           READ FLIVRE KEY IS TITRE.







"William M. Klein" <wmklein@nospam.netcom.com> a �crit dans le message de 
news: Q8lZf.369320$fe6.257594@fe01.news.easynews.com...
> "CODE" is a reserved word - which may be causing some of the problems.
>
…[75 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: conflicting variables names on differents records.

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-04-07T12:40:52+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<443641b5$0$22085$ba620e4c@news.skynet.be>`
- **References:** `<44355b11$0$31480$ba620e4c@news.skynet.be> <Q8lZf.369320$fe6.257594@fe01.news.easynews.com> <44363fed$0$13889$ba620e4c@news.skynet.be>`

```
I just checked with only one record of ENR-LIV and there is no error. The 
problem is cause by the presence of two instance off same var names...

"gianluigi beuzard" <gbeuzard@skynet.be> a �crit dans le message de news: 
44363fed$0$13889$ba620e4c@news.skynet.be...
> I've tryed with another name "COD", but I got the same error msg...
> maybe because we can't use an alternate key following a primary key ?
…[103 more quoted lines elided]…
>
```

#### ↳ Re: conflicting variables names on differents records.

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-04-07T13:04:47+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4436474f$0$30253$ba620e4c@news.skynet.be>`
- **References:** `<44355b11$0$31480$ba620e4c@news.skynet.be>`

```
Voila, I forgot to specify the source field in the select statement ... Now 
it works.
-----------------------------------------------
           SELECT FLIVRE ASSIGN TO DISK
                  ORGANIZATION INDEXED;
                  ACCESS MODE DYNAMIC;
                  RECORD COD OF ENR-LIV; <<
                  ALTERNATE RECORD TITRE OF ENR-LIV; <<
                  ALTERNATE RECORD AUTHEUR OF ENR-LIV DUPLICATES; <<
                  ALTERNATE RECORD THEME OF ENR-LIV DUPLICATES; <<
                  STATUS SLIV.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
