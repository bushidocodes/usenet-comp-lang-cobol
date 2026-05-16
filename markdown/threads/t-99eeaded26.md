[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# long varchar

_9 messages · 7 participants · 2002-01_

---

### long varchar

- **From:** "Tim Cordsen" <tim.cordsen@web.de>
- **Date:** 2002-01-07T12:15:08+01:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<a1bvvr$sjt6@doiftp1.volkswagen.de>`

```
Hallo!
Wer kann mir bei einem Zugriff auf eine Long Varchar Variable helfen?
Ich versuche mit einem fetch into unter anderem auch diese Variable zu
f�llen, bekomme aber immer die Precompiler-Fehlermeldung: UNDEFINED OR
UNUSABLE HOST VARIABLE "..."
Wer kann mir sagen wie ich diese Variable behandeln mu�?

Vielen Dank im Voraus f�r die Hilfe.

Tim Cordsen

P.S. IBM OS390 mit COBOL und DB2
```

#### ↳ Re: long varchar

- **From:** Serge Rielau <srielau@ca.ibm.com>
- **Date:** 2002-01-07T09:47:37-05:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<3C39B509.454CFCC0@ca.ibm.com>`
- **References:** `<a1bvvr$sjt6@doiftp1.volkswagen.de>`

```
Translation:

Hi,
Who can help me accessing a Long Varchar variable?
When doing a FETCH INTO I get the follwing error message from the
precompiler:
'UNDEFINED OR UNUSABLE HOST VARIABLE "..."'
Can anyone tell be how I have to treat this variable.
Thanks in advance
--------------
I don't know Cobol, so I can't help there....
```

##### ↳ ↳ Re: long varchar

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2002-01-07T17:38:03+00:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<%1l_7.7315$cD4.11584@www.newsranger.com>`
- **References:** `<a1bvvr$sjt6@doiftp1.volkswagen.de> <3C39B509.454CFCC0@ca.ibm.com>`

```
Well - I can't help because I don't know DB2 - but if I recall correctly, there
is a way to use VARCHAR2 (long Var Char fields) using DB2 and COBOL - it should
be documented in the DB2 docs.

In article <3C39B509.454CFCC0@ca.ibm.com>, Serge Rielau says...
>
>Translation:
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: long varchar

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-01-08T02:32:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020107213259.12283.00000179@mb-mu.aol.com>`
- **References:** `<3C39B509.454CFCC0@ca.ibm.com>`

```
>Subject: Re: long varchar
>From: Serge Rielau srielau@ca.ibm.com 
>Date: 1/7/02 9:47 AM Eastern Standard Time

>--------------
>I don't know Cobol, so I can't help there....
…[3 more quoted lines elided]…
>IBM Software Lab, Canada

You don't know SQL?????!!!!!!  It's the pre-compiler that is giving this error.
 Any language using embeded SQL would have this error.

sheesh
```

##### ↳ ↳ Re: long varchar

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-01-08T03:17:05+00:00
- **Newsgroups:** comp.lang.cobol,comp.databases.ibm-db2
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-WrMFLxe7ydlY@thishost>`
- **References:** `<a1bvvr$sjt6@doiftp1.volkswagen.de> <3C39B509.454CFCC0@ca.ibm.com>`

```
On Mon, 7 Jan 2002 14:47:37 UTC, Serge Rielau <srielau@ca.ibm.com> 
wrote:

> Translation:
> 
…[14 more quoted lines elided]…
> 

If I do that with IBM Visualage COBOL the LONG VARCHAR variable has to
be defined as

01  longvarchar.
    49  length-varchar  pic s9(4) comp-5.
    49  data-varchar     pic x(32000). (more or less)

The Application Development Guide talks about this....
 
Any definition other than level number 49 fails with the "unusable 
host variable" error
```

#### ↳ Re: long varchar

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-01-08T02:30:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020107213051.12283.00000177@mb-mu.aol.com>`
- **References:** `<a1bvvr$sjt6@doiftp1.volkswagen.de>`

```
>From: "Tim Cordsen" tim.cordsen@web.de 
>Date: 1/7/02 6:15 AM Eastern Standard Time

>Precompiler-Fehlermeldung: UNDEFINED OR
>UNUSABLE HOST VARIABLE "..."

I don't understand German (I'm assuming German) but I do recognize this error
and I know Cobol and DB2 so... (If someone wants to translate this for me???)

The first thing to look at is the spelling of the variable in Working-Storage,
the next thing to look at is the spelling in the program - do they match?  Did
you use a hyphen instead of an underscore if a multiple word variable
(part-number instead of part_number)?

Next if using as part of a WHERE clause and the working storage field is not
defined as COMP-3 then it doesn't like it either.

WHERE PART_NUMBER = :WS-PART-NUMBER

In Working-Storage WS-PART-NUMBER should be defined as PIC S9(??) COMP-3.
(where ?? is your length).  It cannot be a group item or just a PIC 9 - it must
be COMP-3.

Check all these out first.  It's these problems that give me that error the
most.

Eileen
```

##### ↳ ↳ Re: long varchar

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-01-08T03:31:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C3A68FE.4E6F288D@shaw.ca>`
- **References:** `<a1bvvr$sjt6@doiftp1.volkswagen.de> <20020107213051.12283.00000177@mb-mu.aol.com>`

```


YukonMama wrote:

> >From: "Tim Cordsen" tim.cordsen@web.de
> >Date: 1/7/02 6:15 AM Eastern Standard Time
…[6 more quoted lines elided]…
>

.....................
>Hallo!
>Wer kann mir bei einem Zugriff auf eine Long Varchar Variable helfen?
…[3 more quoted lines elided]…
>Wer kann mir sagen wie ich diese Variable behandeln muï¿½?

>Vielen Dank im Voraus fï¿½r die Hilfe.
..........................

OK - just this once. Next time use Babelfish yourself ! Ich sprecht kein Deutsch
<G> :-

    http://babel.altavista.com/sites/babelfish/tr

..................
Hello! Who can help me with an access to a Long Varchar variable? I try to fill
this variable with one fetch into among other things also, however always get the
Precompiler error message: UNDEFINED OR UNUSABLE HOST VARIABLE
 "... " who can say to me as I this variable to treat must? Thank you in advance
for
the assistance.
.....................

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: long varchar

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-01-09T03:17:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020108221714.07250.00000530@mb-cf.aol.com>`
- **References:** `<3C3A68FE.4E6F288D@shaw.ca>`

```
>From: "James J. Gavan" jjgavan@shaw.ca 
>Date: 1/7/02 10:31 PM Eastern Standard Time
>

>OK - just this once. Next time use Babelfish yourself ! Ich sprecht kein
>Deutsch
><G> :-

LOL - actually I ment for my answer to be translated :).  Hmmm....


Babel Fish Translation, Auf Deutsch:  
 Ich verstehe nicht Deutsches (mich annehme Deutschen), aber ich erkenne diesen
Fehler und ich kenne COBOL und DB2 so..., (wenn jemand dieses fï¿½r mich
ï¿½bersetzen mï¿½chte???), Die erste zu betrachtende Sache ist der Spelling der
Variable in Working-Storage, die folgende zu betrachtende Sache ist der
Spelling im Programm - passen sie zusammen? Verwendeten Sie einen Bindestrich
anstelle von einem Unterstreichen wenn eine mehrfache Wortvariable (Teil-Zahl
anstelle vom part_number)? Zunï¿½chst beim Verwenden als Teil, WO Klausel und das
Arbeitsspeicherfeld nicht definiert wird, da COMP-3 dann es es nicht auch nicht
mag. WO PART_NUMBER =:WS-PART-NUMBER In Working-Storage sollte WS-PART-NUMBER
als PIC S9(definiert werden??), COMP-3. (wo?? ist Ihre Lï¿½nge). Es kann nicht
eine Datengruppe oder gerade ein PIC 9 sein - es muï¿½ COMP-3 sein. ï¿½berprï¿½fen
Sie alle diese heraus ersten. Es ist diese Probleme, die mir diesen Fehler
geben, der am meisten ist. Eileen   
 

 I hope this isn't gobblety gook :)
```

#### ↳ Re: long varchar

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-09T13:14:10+13:00
- **Newsgroups:** comp.databases.ibm-db2,comp.lang.cobol
- **Message-ID:** `<3c3b8dc3_11@Usenet.com>`
- **References:** `<a1bvvr$sjt6@doiftp1.volkswagen.de>`

```
Have you defined the Host Variable correctly in BEGIN DECLARE... END
DECLARE?

A long VarChar may need to have a length field preceding it. (It's a while
since I used DB2, but check the IBM manual)

For example...

myVarChar   VARCHAR(36)  NOT NULL

on the Database, may require...

01  myVarChar.
      12 myVCLen       pic s9(4) comp.
      12 myVCData     pic x occurs 36
                                           depending on myVCLen.

...in the DECLARE section.

Post in English to reach the widest audience and improve your chaces of
getting help...

Pete.



Tim Cordsen <tim.cordsen@web.de> wrote in message
news:a1bvvr$sjt6@doiftp1.volkswagen.de...
> Hallo!
> Wer kann mir bei einem Zugriff auf eine Long Varchar Variable helfen?
…[11 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
