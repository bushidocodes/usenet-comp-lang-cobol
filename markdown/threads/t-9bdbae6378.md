[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# problem with opening mutiple files

_8 messages · 4 participants · 2001-01_

---

### problem with opening mutiple files

- **From:** "Tim Paridaens" <Tim.Paridaens@Pandora.be>
- **Date:** 2001-01-09T11:34:27+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93ep8a$2u0$1@news1.skynet.be>`

```
Hello,

Can somebody help me?
When I try to open two files in my program ( The first one is sequential,
and my intension is to write some of the data of the first one to the
second, index-sequential organized file.)
He does not recognize the second program.

Here below you will find the program I have written so far:


                            FILE-CONTROL.
   11                          SELECT inschryv ASSIGN TO disc, "inschryv"
   12                          organization is sequential
   13                          access mode is sequential
   14                          file status is stat1.
   15                          SELECT tweede ASSIGN TO disc, "tweede"
   16                          organization is indexed
   17                          access mode is sequential
   18                          record key is herkenning
   19                          alternate record key is naam-s with
duplicates
   20                          file status is stat.
   21                     DATA DIVISION.
   22                     FILE SECTION.
   23                     FD inschryv.
   24                     01 leerling.
   25                         03 Naam pic x(30).
   26                         03 Geb-datum pic x(6).
   27                         03 Nation pic x(15).
   28                        03 Klas pic xxx.
   29                        03 Filler pic xx.
   30                    FD tweede.
   31                    01 herkenning.
   32                        03 klas-s pic xxx.
   33                        03 naam-s pic x(30).
   34                    01 geboortedatum pic x(6).
   35                    01 punten.
   36                        03 semester occurs 2.
   37                            05 vakken occurs 5 pic 99.
   38
   39                     WORKING-STORAGE SECTION.
   40                     77 sw PIC 9.
   41                        88 EOF value 1.
   42                    77 stat1 pic xx.
   43                    77 stat PIC XX.
   44                     77 x PIC X.
   45                     PROCEDURE DIVISION.
   46    000002           HOOFD.
   47
   48    000005              OPEN I-O inschryv.


RM/COBOL-85 (VER 2.01)  FOR DOS 2.00+          01/09/01  11:20:19 PAGE   2
SOURCE FILE: EERSTE.CBL                 OPTIONS: L

 LINE   DEBUG     PG/LN
A...B.......2.........3.........4.........5.........6.........7..ID.....8
EXAMEN-1

   49    000012              Open output tweede.
                                         $     $
*****   1) E 207: FILE-NAME INVALID  (SCAN SUPPRESSED)
*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E
*****   2) I   5: SCAN RESUME
*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I
***** LAST DIAGNOSTIC AT LINE:     15

   50    000015              Read inschryv at end move 1 to sw.
   51    000030              perform wegschrijven until eof.
   52    000042              close inschryv
   53    000049              close tweede
                                   $
*****   1) E 207: FILE-NAME INVALID  (SCAN SUPPRESSED)
*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E
***** LAST DIAGNOSTIC AT LINE:     49

   54    000052              STOP RUN.
                             $
*****   1) I   5: SCAN RESUME
*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I
***** LAST DIAGNOSTIC AT LINE:     53

   55    000055          Wegschrijven.
   56
   57    000058              move naam to naam-s
   58    000065              move geb-datum to geboortedatum
   59    000072              move klas to klas-s
   60    000079              write tweede invalid key perform fout.
                                   $                  $
*****   1) E 206: FILE-NAME ILLEGAL  (SCAN SUPPRESSED)
*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E*E
*****   2) I   5: SCAN RESUME
*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I*I
***** LAST DIAGNOSTIC AT LINE:     54

   61    000087          fout.
   62    000090              display "Er is iets mis"
   63    000096              accept x.



E 210:  FILE RECORD KEY DATA END  *E*E*E*E*E*E*E*E*E*E:  TWEEDE
I   4:  RECORD KEY DATA-NAME IS *I*I*I*I*I*I*I*I*I*I*I:  HERKENNING
                                                           OF TWEEDE

E 210:  FILE RECORD KEY DATA END  *E*E*E*E*E*E*E*E*E*E:  TWEEDE
I   4:  RECORD KEY DATA-NAME IS *I*I*I*I*I*I*I*I*I*I*I:  NAAM-S
                                                           OF HERKENNING
                                                           OF TWEEDE


RM/COBOL-85 (VER 2.01)  FOR DOS 2.00+          01/09/01  11:20:19 PAGE   3
SOURCE FILE: EERSTE.CBL                 OPTIONS: L

PROGRAM SUMMARY STATISTICS
EXAMEN-1


READ ONLY SIZE =                       462 (X"000001CE") BYTES

READ/WRITE SIZE =                      278 (X"00000116") BYTES

OVERLAYABLE SEGMENT SIZE =               0 (X"00000000") BYTES

TOTAL SIZE (LESS I/O BUFFERS) =        740 (X"000002E4") BYTES       63
LINES

    6 ERRORS         0 WARNINGS     FOR PROGRAM EXAMEN-1

LAST DIAGNOSTIC AT LINE:    60



OBJECT VERSION LEVEL =   2

Does someone knows the problem?
```

#### ↳ Re: problem with opening mutiple files

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-09T08:37:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93f7na$ooo$1@slb1.atl.mindspring.net>`
- **References:** `<93ep8a$2u0$1@news1.skynet.be>`

```
I am taking a WILD guess on this - because "basically" the code looks
reasonable to me (up to the first OPEN syntax error - once you get that,
everything else is "bound" to fail).

Your two Select statements start

 SELECT inschryv ASSIGN TO disc, "inschryv"
    and
 SELECT tweede ASSIGN TO disc, "tweede"

is "disc" a documented word to use (with this compiler) at this place in the
SELECT statement? If not, I think that it is TRYING to assign both files to
the SAME external medium - and this means that it couldn't be opened in both
Sequential and Indexed organization at the same time.

Depending on that (old) RM compiler, I would consider either taking out
"disc" or POSSIBLY changing it to "disk" - check your documentation to see
which the compiler is expecting.
```

#### ↳ Re: problem with opening mutiple files

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2001-01-09T18:07:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pokm5t83p49ijfhvmsognl70rblriuelvc@4ax.com>`
- **References:** `<93ep8a$2u0$1@news1.skynet.be>`

```
On Tue, 9 Jan 2001 11:34:27 +0100, "Tim Paridaens"
<Tim.Paridaens@Pandora.be> wrote:

.....>   30                    FD tweede.
>   31                    01 herkenning.
>   32                        03 klas-s pic xxx.
…[4 more quoted lines elided]…
>   37                            05 vakken occurs 5 pic 99.
change the above code to
>   31                    01 herkenning.
>   32                        03 klas-s pic xxx.
…[4 more quoted lines elided]…
>   37                            05 vakken occurs 5 pic 99.
```

#### ↳ Re: problem with opening mutiple files

- **From:** "COMPULAAT AUTOMATISERING" <compulaat @tip.nl>
- **Date:** 2001-01-09T23:53:21
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93g3kf$f6i$1@nereid.worldonline.nl>`
- **References:** `<93ep8a$2u0$1@news1.skynet.be>`

```
Tim Paridaens heeft geschreven in bericht <93ep8a$2u0$1@news1.skynet.be>...


Hello,
Can somebody help me?
When I try to open two files in my program ( The first one is sequential,
and my intension is to write some of the data of the first one to the
second, index-sequential organized file.)
He does not recognize the second program.
Here below you will find the program I have written so far:
                            FILE-CONTROL.

*********************PB-START

           SELECT INSCHRYV ASSIGN     TO RANDOM   "INSCHRYV"
                  ORGANIZATION                      IS LINE SEQUENTIAL
                  ACCESS MODE                       IS SEQUENTIAL
                  FILE STATUS                           IS STAT1.

*********************PB-END

   11                          SELECT inschryv ASSIGN TO disc, "inschryv"
   12                          organization is sequential
   13                          access mode is sequential
   14                          file status is stat1.

*********************PB-START

           SELECT TWEEDE ASSIGN   TO RANDOM   "TWEEDE"
                  ORGANIZATION                IS INDEXED
                  ACCESS MODE                 IS DYNAMIC
                  RECORD KEY                    IS HERKENNING
                  ALTERNATE
                  RECORD KEY                    IS HERKENNING WITH
DUPLICATES
                  FILE STATUS                     IS STAT.

*********************PB-END

   15                          SELECT tweede ASSIGN TO disc, "tweede"
   16                          organization is indexed
   17                          access mode is sequential
   18                          record key is herkenning
   19                          alternate record key is naam-s with
duplicates
   20                          file status is stat.
   21                     DATA DIVISION.
   22                     FILE SECTION.

********************PB-START

       FD  INSCHRYV LABEL RECORDS ARE STANDARD.
       01  INSCHRYV-RECORD.
             03 NAAM                 PIC X(30).
             03 GEB-DATUM    PIC X(06).
             03 NATION              PIC X(15).
             03 KLAS                  PIC X(03).
             03 FILLER              PIC X(02).

********************PB-END

   23                     FD inschryv.
   24                     01 leerling.
   25                         03 Naam pic x(30).
   26                         03 Geb-datum pic x(6).
   27                         03 Nation pic x(15).
   28                        03 Klas pic xxx.
   29                        03 Filler pic xx.

********************PB-START

       FD  TWEEDE LABEL RECORDS ARE STANDARD.
       01  TWEEDE-RECORD.
             03 TWEEDE-KEY.
                  05 KLAS-S                         PIC X(3).
                  05 TWEEDE-ALT-KEY.
                        07 NAAM-S                  PIC X(30).
             03 GEBOORTEDATUM       PIC X(6).
             03 PUNTEN.
                  05 SEMESTER
OCCURS 2.
                       07 VAKKEN                  PIC 9(2)          OCCURS
5.

********************PB-END

   30                    FD tweede.
   31                    01 herkenning.
   32                        03 klas-s pic xxx.
   33                        03 naam-s pic x(30).
   34                    01 geboortedatum pic x(6).
   35                    01 punten.
   36                        03 semester occurs 2.
   37                            05 vakken occurs 5 pic 99.
   38
   39                     WORKING-STORAGE SECTION.
   40                     77 sw PIC 9.

********************PB-START

                             88 WS-EOF   VALUE  1.
REM   * Gebruik nooit RM-eigen-woorden als variabele !

********************PB-END

   41                        88 EOF value 1.
   42                    77 stat1 pic xx.
   43                    77 stat PIC XX.
   44                     77 x PIC X.
   45                     PROCEDURE DIVISION.
   46    000002           HOOFD.
   47

********************PB-START

                             OPEN INPUT INSCHRYV.
REM   *          IF NOT-EXIST THEN PERFORM END-PROGRAM.

********************PB-END

   48    000005              OPEN I-O inschryv.
RM/COBOL-85 (VER 2.01)  FOR DOS 2.00+          01/09/01  11:20:19 PAGE   2
SOURCE FILE: EERSTE.CBL                 OPTIONS: L
LINE   DEBUG     PG/LN
A...B.......2.........3.........4.........5.........6.........7..ID.....8
EXAMEN-1

********************PB-START

                             OPEN I-O TWEEDE.
REM   *          IF NOT-EXIST THEN OPEN OUTPUT TWEEDE
REM   *                                                CLOSE
TWEEDE
REM   *                                                 OPEN     I-O
TWEEDE.

********************PB-END

   49    000012              Open output tweede.
                                         $     $

********************PB-START

       START-LEZEN.
            READ INSCHRYF NEXT
                        AT END MOVE  1 TO SW
                                       GO TO EINDE-PROGRAMMA.
            PERFORM WEGSCHRIJVEN-TWEEDE.
            GO TO START-LEZEN.
       EINDE-PROGRAMMA.
            CLOSE INSCHRYV   TWEEDE.
       END-RUN.
REM   *    perform wegschrijven until eof. KAN NIET !!!

********************PB-END

   50    000015              Read inschryv at end move 1 to sw.
   51    000030              perform wegschrijven until eof.
   52    000042              close inschryv
   53    000049              close tweede
                                   $
   54    000052              STOP RUN.
                             $
   55    000055          Wegschrijven.
   56
   57    000058              move naam to naam-s
   58    000065              move geb-datum to geboortedatum
   59    000072              move klas to klas-s
   60    000079              write tweede invalid key perform fout.
                                   $                  $
   61    000087          fout.
   62    000090              display "Er is iets mis"
   63    000096              accept x.
Does someone knows the problem?

Does dit help you een beetje verder?
mvg.
Piet van 'Het Compulaat'
```

#### ↳ Re: problem with opening mutiple files

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 2001-01-10T13:06:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a5c6090$0$30008$4156c999@news.netdirect.net>`
- **References:** `<93ep8a$2u0$1@news1.skynet.be>`

```
In article <93ep8a$2u0$1@news1.skynet.be>, "Tim Paridaens" <Tim.Paridaens@Pandora.be> wrote:
>Hello,
>
…[30 more quoted lines elided]…
>   30                    FD tweede.

Problem is right here. "FD" begins one column left of where it belongs. 
(Compare it to the previous FD.)
```

##### ↳ ↳ Re: problem with opening mutiple files

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-10T11:03:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93i4ju$u04$1@slb3.atl.mindspring.net>`
- **References:** `<93ep8a$2u0$1@news1.skynet.be> <3a5c6090$0$30008$4156c999@news.netdirect.net>`

```
The person who asked the original question received a private email reply -
but just so people know the "actual" problem was that they had alternate
keys starting at the same position as the primary key  - and this is a
"no-no" in Standard COBOL.

FYI,
  An "FD" may begin ANYWHERE in the A-Margin (if your compiler still
requires A-/B-margin checking).  They do NOT need to start in the same
place.
```

###### ↳ ↳ ↳ Re: problem with opening mutiple files

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2001-01-12T22:13:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a5f839a$0$1499$7ea90a65@news.netdirect.net>`
- **References:** `<93ep8a$2u0$1@news1.skynet.be> <3a5c6090$0$30008$4156c999@news.netdirect.net> <93i4ju$u04$1@slb3.atl.mindspring.net>`

```
In article <93i4ju$u04$1@slb3.atl.mindspring.net>, "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
>The person who asked the original question received a private email reply -
>but just so people know the "actual" problem was that they had alternate
>keys starting at the same position as the primary key  - and this is a
>"no-no" in Standard COBOL.
>
And how would this affect the compiler's ability to recognize the name of the 
FD as a valid identifier? No, I think you're on the wrong track here.

>FYI,
>  An "FD" may begin ANYWHERE in the A-Margin (if your compiler still
>requires A-/B-margin checking).  They do NOT need to start in the same
>place.
>
You missed my point entirely -- which was precisely that in this program the 
keyword FD does *not* begin in Area A. Even in compilers that don't enforce 
A/B margin checking, there is still a continuation column, is there not? And I 
think the original poster has his FD beginning in the continuation column.

I tried compiling the program myself. My compiler (Tandem Cobol85) never says 
a thing about a conflict between the primary and alternate key offsets, but it 
complains like hell when the FD begins in the continuation column.

Obviously his record definition is faulty. But I still think the biggest part 
of his problem is that the FD begins one column left of where it should.

I'd be interested in seeing a followup from the original poster.
```

###### ↳ ↳ ↳ Re: problem with opening mutiple files

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-01-12T18:09:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93o6ao$k81$1@nntp9.atl.mindspring.net>`
- **References:** `<93ep8a$2u0$1@news1.skynet.be> <3a5c6090$0$30008$4156c999@news.netdirect.net> <93i4ju$u04$1@slb3.atl.mindspring.net> <3a5f839a$0$1499$7ea90a65@news.netdirect.net>`

```
The reply that I reported came from the vendor of the compiler in question.
You are correct that if the FD began in column 7 - that could WELL cause a
serious problem.  However, that was NOT how the code actually "appeared" (in
the text that was passed back and forth via private email).

There are a VARIETY of compilers that do different things when an FD, a
Select/Assign, or an I/O statement "has a problem".  There is NOTHING in the
Standard that makes the type of compiler error that you receive "portable".

Once the Select/Assign clause pointed to "incorrect" Alternate Keys "all
bets were off" for the rest of the source code.

Personally, I believe that the message that was issued was NOT very
user-friendly - but it certainly was a "legitimate" recognition that
SOMETHING was wrong.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
