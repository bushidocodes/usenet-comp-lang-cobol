[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rewriting data using REWRITE ?

_16 messages · 10 participants · 2001-09_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Rewriting data using REWRITE ?

- **From:** "mpoetschik" <mpoetschik@t-online.de>
- **Date:** 2001-09-19T19:03:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9oaj34$n1h$05$1@news.t-online.com>`

```
Hi,
Iï¿½ve a (beginner)question:
As goal we have to solve the problem how to restore a complete dataset
initially coming from a external file (located on the harddisk, i.e.
"C:adress.dat"
This needs to be sorted in an alphabetical order, displayed on the screen
and restored at the same position / in the same file.
Trying this with REWRITE I always failed: MF personal cobol compliler tells
me mostly :
"Rewrite in sequential mode not preceded by successfull read" (Error 143) or
compiles succesfully but doesn`t write data at all.

What can I do?
```

#### ↳ Re: Rewriting data using REWRITE ?

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-09-19T17:27:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4A4q7.383489$NK1.36654032@bin3.nnrp.aus1.giganews.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com>`

```

On 19-Sep-2001, "mpoetschik" <mpoetschik@t-online.de> wrote:

> I�ve a (beginner)question:
> As goal we have to solve the problem how to restore a complete dataset
…[9 more quoted lines elided]…
> compiles succesfully but doesn`t write data at all.

For this type of problem, I don't like to touch the existing dataset -
instead I prefer to create a new dataset, verify that it is correct, and
back up the old one.   Then, and only then, do I swap out the old one with
the restored data.
```

#### ↳ Re: Rewriting data using REWRITE ?

- **From:** jraben@cascinc.com (Jeff Raben)
- **Date:** 2001-09-19T18:52:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ba8e84f.7705270@news.bullseyetelecom.net>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com>`

```
"mpoetschik" <mpoetschik@t-online.de> wrote:

>Hi,
>I�ve a (beginner)question:
…[12 more quoted lines elided]…
>
If you are sorting, in the OUTPUT procedure you can open the file
OUTPUT (after CLOSING it in the INPUT procedure) and WRITE not REWRITE
the records.  
Either WRITE or REWRITE would make the job non-restartable anyways as
you would be destroying the file on the fly and if the program failed
in the middle of (RE)WRITING the file would not be in its original or
readable state.

JR



and stir with a Runcible spoon...
```

#### ↳ Re: Rewriting data using REWRITE ?

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-09-19T22:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com>`

```
1. REWRITE applies only to the last record read; you can't, for example,
rewrite a file.

2. I'm not sure of your requirement: "This (an external file) needs to be
sorted... displayed (presumably sorted)... and restored at the same
position..." This doesn't make sense in that if you are restoring
(presuambly the same data) to the same location in the same file you might
as well be collecting bits of string too short to be of any use.

3. If you want to create a new file from the contents of an old (backup?)
file where the new file is identical in content to the old file save that
the new file is sorted, well, that's a common task and is a reasonable task.

Please advise.


"mpoetschik" <mpoetschik@t-online.de> wrote in message
news:9oaj34$n1h$05$1@news.t-online.com...
> Hi,
> I�ve a (beginner)question:
…[5 more quoted lines elided]…
> Trying this with REWRITE I always failed: MF personal cobol compliler
tells
> me mostly :
> "Rewrite in sequential mode not preceded by successfull read" (Error 143)
or
> compiles succesfully but doesn`t write data at all.
>
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Rewriting data using REWRITE ?

- **From:** "mpoetschik" <mpoetschik@t-online.de>
- **Date:** 2001-09-20T19:36:13+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9od9bt$g4a$00$1@news.t-online.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com>`

```
What I mean is:

1. read file from C: anyname.dat (content: a,g,t,d,s,b)
2. sort the contend (a,b,d,g,s,t)
3. Overwrite (rewrite) the old file with the now sorted data at
C:anyname.dat.


"JerryP" <news@bisusa.com> schrieb im Newsbeitrag
news:Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com...
> 1. REWRITE applies only to the last record read; you can't, for example,
> rewrite a file.
…[9 more quoted lines elided]…
> the new file is sorted, well, that's a common task and is a reasonable
task.
>
> Please advise.
…[9 more quoted lines elided]…
> > This needs to be sorted in an alphabetical order, displayed on the
screen
> > and restored at the same position / in the same file.
> > Trying this with REWRITE I always failed: MF personal cobol compliler
> tells
> > me mostly :
> > "Rewrite in sequential mode not preceded by successfull read" (Error
143)
> or
> > compiles succesfully but doesn`t write data at all.
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-09-20T19:03:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f4rq7.6555$J64.302818@paloalto-snr2.gtei.net>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com>`

```
mpoetschik <mpoetschik@t-online.de> wrote in message
news:9od9bt$g4a$00$1@news.t-online.com...
> What I mean is:
>
…[4 more quoted lines elided]…
>

Oh, an inplace sort!

Best bet is (not tried, but I don't see why it wouldn't work)...

 0500-INPLACE-SORT.
     SORT SORT-FILE
    ......
       USING ORIGINAL-FILE
         GIVING TEMP-FILE
    END-SORT

   SORT SORT-FILE
      ...
      USING TEMP-FILE
        GIVING ORIGINAL-FILE
   END-SORT

 EXIT.


If your system/media support it:
  SORT SORT-FILE
    ...
   USING ORIGINAL- FILE
   GIVING  ORIGINAL-FILE


Or you can
  SORT SORT-FILE
     ....
     USING  ORIGINAL-FILE
        OUTPUT PROCEDURE  REWRITE-ORIGINAL-FILE

REWRITE-ORIGINAL-FILE.

  OPEN I-O ORIGINAL-FILE
  MOVE ZERO TO EOF-SORT-SW
  PERFORM UNTIL EOF-SORT
    RETURN BUFFER
      AT END
       SET EOF-SORT TO TRUE
     NOT AT END
      READ ORIGINAL-FILE
      REWRITE ORGINAL-FILE-RECORD FROM BUFFER
   END-RETURN
 END-PERFORM
 CLOSE ORIGINAL-FILE
 EXIT.

MCM
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-09-20T14:31:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9odg8o$jhn$1@slb5.atl.mindspring.net>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com> <f4rq7.6555$J64.302818@paloalto-snr2.gtei.net>`

```
Actually, unless I am missing a rule in the (existing) ANSI/ISO Standard, it
is entirely "legal" to have both the USING and GIVING files reference the
same physical file.

HAVING SAID THAT, in anything other than a "small class assignment" - I
think that is an AWFUL idea and should be avoided like the "plague".  The
chances of "corrupting" your file in a "real world/production" environment
with this type of logic seems way to dangerous to me.  OTOH, I do think it
is legal and if you are trying to "sort in place" a file that you don't care
if it gets corrupted, I think it should work.

P.S.  As long as we are "back" at this being a homework assignment rather
than a "real world" question, you may want to find out if the "point" of the
assignment is to use the COBOL SORT verb - or to create an "algorithm" for
doing a file sort without using the COBOL SORT verb.  Both of these are
fairly "typical" assignments - for beginning programmers - but have very
different solutions.
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

_(reply depth: 5)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-09-20T21:01:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010920170143.23460.00001453@mb-cp.aol.com>`
- **References:** `<9odg8o$jhn$1@slb5.atl.mindspring.net>`

```

>Actually, unless I am missing a rule in the (existing) ANSI/ISO Standard, it
>is entirely "legal" to have both the USING and GIVING files reference the
…[7 more quoted lines elided]…
>if it gets corrupted, I think it should work.

SORT ... USING... GIVING...
Is valid in the Unisys environment and is used as a common practice in nightly
batch update processing.   Usually, the files are 'extracts' from some master
file or transaction history file for subsequent reporting processes.  At least
that is what my 20 years of experience has seen.

Most of these programs massage the data  in one order for internal reporting
and then massage the same data into another order for client reporting, or
vice-versa.

Sometimes the same data is presented in 2 to 4 different views and each
requires a different sort criteria.   I have found this to be from attempts to
minimize disk space consumption and reduce file write requirements of an
updating program (nightly turn-around performance issues).
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-09-21T11:01:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C6Fq7.4$T%.20000@paloalto-snr1.gtei.net>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com> <f4rq7.6555$J64.302818@paloalto-snr2.gtei.net> <9odg8o$jhn$1@slb5.atl.mindspring.net>`

```
William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:9odg8o$jhn$1@slb5.atl.mindspring.net...
> Actually, unless I am missing a rule in the (existing) ANSI/ISO Standard,
it
> is entirely "legal" to have both the USING and GIVING files reference the
> same physical file.
…[5 more quoted lines elided]…
> is legal and if you are trying to "sort in place" a file that you don't
care
> if it gets corrupted, I think it should work.

Hmm, sorry I didn't see the "homework" aspects of this. Had that been the
case I would have given a  three-word-hint: "SORT" "USING" "GIVING"

That said, let me address your concern. If this is a "batch update" program,
I'd say there's a good chance the file was backed up in a previous job step;
but I don't know why I'd even bother with a program which sorts a file in
place. Seems to me any program using this file 'downstream' could do its own
sorting. (Or the program which created it could have produced the output in
sorted order easily enough).

But... I think we've all seen some, uh, mm, er, 'creative' system designs so
I'm not in shock or anything .....

MCM
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-09-20T19:07:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BAA3FB1.7C1E180B@home.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com>`

```


mpoetschik wrote:

> What I mean is:
>
…[4 more quoted lines elided]…
>

You started out your original message, "As a goal.....". I think we would all be
on the same wavelength if you quote us EXACTLY the text of the test question.
Frankly, 'what you mean' and 'what you are being asked to do', may be entirely
two different things <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

_(reply depth: 4)_

- **From:** "mpoetschik" <mpoetschik@t-online.de>
- **Date:** 2001-09-20T21:30:23+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9odg1v$4l4$01$1@news.t-online.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com> <3BAA3FB1.7C1E180B@home.com>`

```
I would like to, but unfortunately itï¿½s in german language. So most of your
guys wouldnï¿½t understand it, right?

"James J. Gavan" <jjgavan@home.com> schrieb im Newsbeitrag
news:3BAA3FB1.7C1E180B@home.com...
>
>
…[10 more quoted lines elided]…
> You started out your original message, "As a goal.....". I think we would
all be
> on the same wavelength if you quote us EXACTLY the text of the test
question.
> Frankly, 'what you mean' and 'what you are being asked to do', may be
entirely
> two different things <G>
>
> Jimmy, Calgary AB
>
>
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-09-20T21:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BAA5A2F.625A52C4@home.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com> <3BAA3FB1.7C1E180B@home.com> <9odg1v$4l4$01$1@news.t-online.com>`

```


mpoetschik wrote:

> I would like to, but unfortunately itï¿½s in german language. So most of your
> guys wouldnï¿½t understand it, right?

Well, post it in German. There are a few 'Anglos' who are proficient in
German,
(not me - I didn't get much beyond "Eine bier bitte" <G>), and besides,
I'm
sure Volker Bandke will understand - and give you a very precise
solution in
German !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

_(reply depth: 6)_

- **From:** "mpoetschik" <mpoetschik@t-online.de>
- **Date:** 2001-09-22T10:05:57+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ohgmj$sk4$03$1@news.t-online.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com> <3BAA3FB1.7C1E180B@home.com> <9odg1v$4l4$01$1@news.t-online.com> <3BAA5A2F.625A52C4@home.com>`

```
Ok, Iï¿½ll try it now:

Die Aufgabe:
Schreiben Sie ein Unterprogramm, welches die sortierte Tabelle unter dem
alten Namen abspeichert und die alte Datei damit ï¿½berschreibt !

Dies ist der vorgegebene Sourcecode:

      IDENTIFICATION DIVISION.

       PROGRAM-ID.         ILS8.
       AUTHOR.              MARTIN POETSCHIK.

       ENVIRONMENT DIVISION.

       CONFIGURATION SECTION.
       SPECIAL-NAMES.      DECIMAL-POINT IS COMMA.

       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       SELECT EINGABEDATEI
           ASSIGN TO DISK
           ACCESS IS SEQUENTIAL.

       DATA DIVISION.

       FILE SECTION.
       FD EINGABEDATEI
           LABEL RECORD IS STANDARD
           VALUE OF FILE-ID IS "C:/ADRESS1.DAT".
       01      SPEICHERSATZ.
           05      S-NACHNAME          PIC X(25).
           05      S-VORNAME       PIC X(25).
           05      S-STRASSE       PIC X(25).
           05      S-PLZ           PIC X(5).
           05      S-ORT           PIC X(25).

       WORKING-STORAGE SECTION.

       01      V-SATZ OCCURS 11 TIMES.
           05      V-NACHNAME      PIC X(25).
           05      V-VORNAME       PIC X(25).
           05      V-STRASSE       PIC X(25).
           05      V-PLZ           PIC X(5).
           05      V-ORT           PIC X(25).

       01          AUSGABESATZ.
           05      A-NACHNAME      PIC X(19).
           05      FILLER          PIC X.
           05      A-VORNAME       PIC X(17).
           05      FILLER          PIC X.
           05      A-STRASSE       PIC X(17).
           05      FILLER          PIC X.
           05      A-PLZ           PIC X(5).
           05      FILLER          PIC X.
           05      A-ORT           PIC X(19).
         77        ZAEHLER         PIC 9(6) VALUE ALL ZERO.
         77        RS-ZAEHLER       PIC 9(6) VALUE ALL ZERO.
         77        LAUFZAEHLER     PIC 9(2) VALUE ALL ZERO.
         77        TAUSCHZAEHLER   PIC 9(2) VALUE ALL ZERO.
         77        CPOSITION       PIC 9999 VALUE 0301.

       PROCEDURE DIVISION.

       VORLAUF.
           DISPLAY SPACE AT 0101.
           OPEN OUTPUT EINGABEDATEI.
           PERFORM KOPFZEILE.

       HAUPTPROGRAMM.
           PERFORM TABELLE-EINLESEN UNTIL ZAEHLER = 10.
           MOVE 00000 TO ZAEHLER.
           PERFORM SORTIEREN UNTIL LAUFZAEHLER = 9.
           PERFORM LISTE UNTIL ZAEHLER = 10.
           MOVE SPACE TO SPEICHERSATZ.

       NACHLAUF.
           MOVE 000000 TO ZAEHLER.
           PERFORM ZAEHLSCHLEIFE UNTIL ZAEHLER = 000003.
           DISPLAY SPACE AT 0101.
           DISPLAY "SORTIERPROGRAMM BEENDET" AT 0250 WITH REVERSE-VIDEO.
           CLOSE EINGABEDATEI.
           STOP RUN.

       TABELLE-EINLESEN.
           COMPUTE ZAEHLER = ZAEHLER + 1.
           READ EINGABEDATEI INTO V-SATZ(ZAEHLER) AT END MOVE 00010 TO
           ZAEHLER.

       SORTIEREN.
           COMPUTE LAUFZAEHLER = LAUFZAEHLER + 1.
           MOVE 00 TO TAUSCHZAEHLER.
           PERFORM TAUSCHEN UNTIL TAUSCHZAEHLER = 9.

       TAUSCHEN.
           COMPUTE TAUSCHZAEHLER = TAUSCHZAEHLER + 1.
           IF V-NACHNAME(TAUSCHZAEHLER) > V-NACHNAME(TAUSCHZAEHLER + 1)
           THEN MOVE V-SATZ(TAUSCHZAEHLER) TO V-SATZ(11)
                MOVE V-SATZ(TAUSCHZAEHLER + 1) TO V-SATZ(TAUSCHZAEHLER)
                MOVE V-SATZ(11) TO V-SATZ(TAUSCHZAEHLER + 1).

       LISTE.
           COMPUTE ZAEHLER = ZAEHLER + 1.
           MOVE SPACE TO AUSGABESATZ.
           MOVE V-NACHNAME(ZAEHLER)    TO A-NACHNAME.
           MOVE V-VORNAME(ZAEHLER)     TO A-VORNAME.
           MOVE V-STRASSE(ZAEHLER)     TO A-STRASSE.
           MOVE V-PLZ(ZAEHLER)         TO A-PLZ.
           MOVE V-ORT(ZAEHLER)         TO A-ORT.
           COMPUTE CPOSITION = CPOSITION + 100.
           DISPLAY AUSGABESATZ         AT CPOSITION.

       KOPFZEILE.
           DISPLAY "AUFLISTUNG ALLER DATENSAETZE" AT 0101 WITH
           REVERSE-VIDEO.
           DISPLAY "NACHNAME"          AT 0201 WITH REVERSE-VIDEO.
           DISPLAY "VORNAME"           AT 0221 WITH REVERSE-VIDEO.
           DISPLAY "STRASSE"           AT 0239 WITH REVERSE-VIDEO.
           DISPLAY "PLZ"               AT 0257 WITH REVERSE-VIDEO.
           DISPLAY "ORT"               AT 0262 WITH REVERSE-VIDEO.

       ZAEHLSCHLEIFE.
           COMPUTE ZAEHLER = ZAEHLER + 1.
           DISPLAY ZAEHLER AT 2574 WITH REVERSE-VIDEO.


"James J. Gavan" <jjgavan@home.com> schrieb im Newsbeitrag
news:3BAA5A2F.625A52C4@home.com...
>
>
> mpoetschik wrote:
>
> > I would like to, but unfortunately itï¿½s in german language. So most of
your
> > guys wouldnï¿½t understand it, right?
>
…[8 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-09-25T04:37:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BB00B25.B483BCA4@home.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com> <3BAA3FB1.7C1E180B@home.com> <9odg1v$4l4$01$1@news.t-online.com> <3BAA5A2F.625A52C4@home.com> <9ohgmj$sk4$03$1@news.t-online.com>`

```


mpoetschik wrote:

> Ok, Iï¿½ll try it now:
>
…[122 more quoted lines elided]…
>

So Martin,

No takers in German and Ich sprecht kein Deutsch. Ich hab fergessen !
Fortunately COBOL is 'universal' enough to get a handle on what you are doing.
So back to what you originally wrote :-
----------------
"Iï¿½ve a (beginner)question:
As goal we have to solve the problem how to restore a complete dataset
initially coming from a external file (located on the harddisk, i.e.
"C:adress.dat"
This needs to be sorted in an alphabetical order, displayed on the screen
and restored at the same position / in the same file.
Trying this with REWRITE I always failed: MF personal cobol compliler tells
me mostly :
"Rewrite in sequential mode not preceded by successful read" (Error 143) or
compiles successfully but doesn't write data at all.

What can I do?"
--------------------------

Well what you didn't do was supply the TEST question - all you've done is give
us your SOLUTION - and it is wrong. Without seeing the QUESTION I find it hard
to believe an instructor would impose a *slick* (sophisticated)  one-file sort
on beginners

Pseudo code - you give it a try and get back to us and we can give you some
short-cut tips.

1.    Open INPUT Sequential (EINGABEDATEI). You are currently opening it as
        OUTPUT - you can't open an output Sequential and hope to read from it.

        (Your - OPEN OUTPUT EINGABEDATEI)

2. Now you do your :-

    TABELLE-EINLESEN.
           COMPUTE ZAEHLER = ZAEHLER + 1.
           READ EINGABEDATEI INTO V-SATZ(ZAEHLER) AT END
            MOVE 00010 TO  ZAEHLER.

    This would be easier if you coded :-

        perform  TABELLE-EINLESEN.

  TABELLE-EINLESEN.
        perform varying n from 1 by 1 until n > 10
           READ EINGABEDATEI INTO V-SATZ(n)
                    AT END Exit-Perform
           End-read

Note you are assuming here you have a MAXIMUM of 10 incoming records - but it
could be less or more ? Maybe the instructor told you to expect a fixed 10
records ?

3. I have a copy of Personal COBOL somewhere but unfortunately can't find it.
Does it have the feature Table Sort. If so take a look, you can sort the table
quite simply.:-
----------------------------------------------------
A table sort using the entire element for sequencing:

working-storage section.
       01      V-SATZ OCCURS 11 TIMES.
           05      V-NACHNAME      PIC X(25).
           05      V-VORNAME       PIC X(25).
           05      V-STRASSE       PIC X(25).
           05      V-PLZ           PIC X(5).
           05      V-ORT           PIC X(25).
   . . .
procedure division.
   . . .
   sort V-SATZ ascending.

----------------- That's it !

4. Now you display the sorted table - performing LISTE 10 times :-

        LISTE.
            perform varying n from 1 by 1 until n  > 10

        *> Note using n or p or whatever is a lot shorter to type than using
        *> ZAEHLER all the time

                      MOVE SPACE TO AUSGABESATZ.
                      MOVE V-NACHNAME(ZAEHLER)    TO A-NACHNAME.
                      MOVE V-VORNAME(ZAEHLER)     TO A-VORNAME.
                      MOVE V-STRASSE(ZAEHLER)     TO A-STRASSE.
                      MOVE V-PLZ(ZAEHLER)         TO A-PLZ.
                      MOVE V-ORT(ZAEHLER)         TO A-ORT.
                      COMPUTE CPOSITION = CPOSITION + 100.
                      DISPLAY AUSGABESATZ         AT CPOSITION.
            End-perform

5. I REALLY don't like this rewriting of your input file. Better, OPEN an
OUTPUT Sequential EINGABEDATE2 and now :-

    WRITE-SORTED-RECORDS.
        perform varying n from 1 by 1 until n > 10
            move the Working-Storage fields to the OUT-record fields
            then WRITE EINGABEDATE2 record
       End-perform

Yes you can REWRITE a sequential, but it assumes you are REWRITING the record
you are currently pointing at with your last READ NEXT. And I can see no
difference in format between your SPEICHERSATZ and V-SATZ . So even if you did
do a REWRITE you are replacing it with EXACTLY the same. Surely what you are
really after is to get an output file sorted ASCENDING by NACHNAME, VORNAME
etc.

If you have on-line help check "SORT statement format 1 (file)". Michael's-
suggestion -  Micro Focus requires three files - input filename-1, (if
required, temporary filename-2),  and output giving filename-3.

You give it a shot - beat the challenge and you will feel as pleased as punch
with yourself. Then come back to us with the result - and we can give you some
short-cut tips on some things you are doing.

PS : I *REALLY* would like to see the TEST question given to you. Put it
through Babelfish translating from German to English <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Rewriting data using REWRITE ?

_(reply depth: 7)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-09-25T16:50:21+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g51rt0q7b2pkamo9vafdn4untf2nutnlv@4ax.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com> <Qz8q7.384856$NK1.36943788@bin3.nnrp.aus1.giganews.com> <9od9bt$g4a$00$1@news.t-online.com> <3BAA3FB1.7C1E180B@home.com> <9odg1v$4l4$01$1@news.t-online.com> <3BAA5A2F.625A52C4@home.com> <9ohgmj$sk4$03$1@news.t-online.com>`

```
Well, 

I have been on an extended weekend trip, done some fishing in a
Norwegian Fjord, had a generally good time, and come late to this
thread.

The translation:

Create a subprogram which will write the sorted table back to a file
with the original name, thus overwriting the original file.  

This is the provided source

</translation>

Taking a short glance at the program I am not sure that this is really
the source as provided by the instructor.


....
OPEN OUTPUT EINGABEDATEI

followed by

READ EINGABEDATEI INTO ....


does not really make sense to me.

Also, any instructor using this "structure" (like falling through from
one paragraph to the next, as happens here,) should take a seat in the
student area of the classroom .....

And finally, I really don't see the problem.  The table has been read
in, sorted, why not just use


>HAUPTPROGRAM.
            ...
>           PERFORM LISTE UNTIL ZAEHLER = 10.
            CLOSE EINGABEDATEI
            PERFORM MY-SUB-ROUTINE
>           MOVE SPACE TO SPEICHERSATZ.
            CLOSE EINGABEDATEI


MY-SUB-ROUTINE.
   OPEN OUTPUT EINGABEDATEI
   PERFORM VARYING LAUFZAEHLER FROM .... until ...
      WRITE SPECIHERSATZ FROM V-SAtz(LAUFZAEHLER)
   END-PERFORM
   .


On Sat, 22 Sep 2001 10:05:57 +0200, "mpoetschik"
<mpoetschik@t-online.de> wrote:

>Ok, Iï¿½ll try it now:
>
…[71 more quoted lines elided]…
>           PERFORM LISTE UNTIL ZAEHLER = 10.

>           MOVE SPACE TO SPEICHERSATZ.
>
…[69 more quoted lines elided]…
>

                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      A cannibal only opens his mouth to change your feet.
      
        (Another Wisdom from my fortune cookie jar)         
______________________________________________________________________________
Posted Via Binaries.net = SPEED+RETENTION+COMPLETION = http://www.binaries.net
```

#### ↳ Re: Rewriting data using REWRITE ?

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-09-20T20:28:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wjsq7.7912$p77.27326@www.newsranger.com>`
- **References:** `<9oaj34$n1h$05$1@news.t-online.com>`

```
In article <9oaj34$n1h$05$1@news.t-online.com>, mpoetschik says...
>

From what I understand Rewrite is used to read a record, change the record in
local storage, and then to rewrite it so it will be different.

If you are using an external file first you have to find the record you want to
change into local storage, copy the different data to it, and then rewrite it
from local storage.  You have to make sure you have the correct Record to
rewrite.  

There may be a file restore program that just resores your file from a backup
also.  Most operating systems have utilities or commands to accomplish this.


>Hi,
>I�ve a (beginner)question:
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
