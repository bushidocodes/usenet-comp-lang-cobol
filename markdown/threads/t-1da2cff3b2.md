[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is wrong with my program???????

_10 messages · 8 participants · 1998-08_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### What is wrong with my program???????

- **From:** "ds..." <ua-author-813600@usenetarchives.gap>
- **Date:** 1998-08-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`

```
Can anyone PLEASE, I'M BEGGING YOU, OH PRETTY PLEASE, tell me what is wrong
with the SELECT VENDOR-FILE statement, lines 10 - 15 ???
The program is as follows:

IDENTIFICATION DIVISION.
PROGRAM-ID. VNDNEW01.

*add a record to an indexed vendor file

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.

SELECT VENDOR-FILE
ASSIGN TO "vendor"
ORGANIZATION IS INDEXED
ACCESS MODE IS DYNAMIC
RECORD KEY IS VENDOR-NUMBER.

DATA DIVISION.
FILE SECTION.

FD VENDOR-FILE
LABEL RECORDS ARE STANDARD.
01 VENDOR-RECORD.
05 VENDOR-NUMBER PIC 9(5).
05 VENDOR-NAME PIC X(30).
05 VENDOR-ADDRESS-1 PIC X(30).
05 VENDOR-ADDRESS-2 PIC X(30).
05 VENDOR-CITY PIC X(20).
05 VENDOR-STATE PIC X(2).
05 VENDOR-ZIP PIC X(10).
05 VENDOR-CONTACT PIC X(30).
05 VENDOR-PHONE PIC X(15).

WORKING-STORAGE SECTION.

PROCEDURE DIVISION.
PROGRAM-BEGIN.
OPEN I-O VENDOR-FILE.
PERFORM MAIN-PROCESS.
CLOSE VENDOR-FILE.


PROGRAM-DONE.
STOP RUN.

MAIN-PROCESS.
PERFORM INIT-VENDOR-RECORD.
PERFORM ENTER-VENDOR-FIELDS.
WRITE VENDOR-RECORD.

INIT-VENDOR-RECORD.
MOVE SPACE TO VENDOR-RECORD.
MOVE ZEROES TO VENDOR-NUMBER.

ENTER-VENDOR-FIELDS.
PERFORM ENTER-VENDOR-NUMBER.
PERFORM ENTER-VENDOR-NAME.
PERFORM ENTER-VENDOR-ADDRESS-1.
PERFORM ENTER-VENDOR-ADDRESS-2.
PERFORM ENTER-VENDOR-CITY.
PERFORM ENTER-VENDOR-STATE.
PERFORM ENTER-VENDOR-ZIP.
PERFORM ENTER-VENDOR-CONTACT.
PERFORM ENTER-VENDOR-PHONE.

ENTER-VENDOR-NUMBER.
DISPLAY "ENTER VENDOR NUMBER (00001-99999)".
ACCEPT VENDOR-NUMBER.

ENTER-VENDOR-NAME.
DISPLAY "ENTER VENDOR NAME".
ACCEPT VENDOR-NAME.

ENTER-VENDOR-ADDRESS-1.
DISPLAY "ENTER VENDOR ADDRESS-1".
ACCEPT VENDOR-ADDRESS-1.

ENTER-VENDOR-ADDRESS-2.
DISPLAY "ENTER VENDOR ADDRESS-2".
ACCEPT VENDOR-ADDRESS-2.

ENTER-VENDOR-CITY.
DISPLAY "ENTER VENDOR CITY".
ACCEPT VENDOR-CITY.

ENTER-VENDOR-STATE.
DISPLAY "ENTER VENDOR STATE".
ACCEPT VENDOR-STATE.

ENTER-VENDOR-ZIP.
DISPLAY "ENTER VENDOR ZIP".
ACCEPT VENDOR-ZIP.

ENTER-VENDOR-CONTACT.
DISPLAY "ENTER VENDOR CONTACT".
ACCEPT VENDOR-CONTACT.

ENTER-VENDOR-PHONE.
DISPLAY "ENTER VENDOR PHONE".
ACCEPT VENDOR-PHONE.
```

#### ↳ Re: What is wrong with my program???????

- **From:** "vlfa..." <ua-author-17075520@usenetarchives.gap>
- **Date:** 1998-08-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`

```
Well ...is "assign to 'vendor'" a vaild disk directory ??

What platform are you on...?

Vern......Project Consultant in Cincinnati for the Progeni Corp.
```

##### ↳ ↳ Re: What is wrong with my program???????

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1da2cff3b2-p2@usenetarchives.gap>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com> <gap-1da2cff3b2-p2@usenetarchives.gap>`

```
On 18 Aug 1998 23:58:46 GMT, vlf··.@a··.com (VLFarmer) wrote:

› Well ...is "assign to 'vendor'" a vaild disk directory ??
›
› What platform are you on...?
›
› Vern......Project Consultant in Cincinnati for the Progeni Corp.
Under RM/COBOL and ACUCOBOL it is.
(on DOS/WINDOWS and UNIX operating system).
I think that with MICROFOCUS it is also true.

Frederico Fonseca
```

#### ↳ Re: What is wrong with my program???????

- **From:** "rich rohde" <ua-author-17074938@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p4@usenetarchives.gap>`
- **In-Reply-To:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`

```
This appears to be one of those programs in 'Teach Yourself COBOL in 21
Days' page 276 and is a follow-up to VNDBLD01 on page 273. If VNDBLD01 was
no run correctly then VNDNEW01 will not work and you will get a file
management error.

Rich

Dsl8r wrote in message <199··.@lad··l.com>...
› Can anyone PLEASE, I'M BEGGING YOU, OH PRETTY PLEASE, tell me what is wrong
› with the SELECT VENDOR-FILE statement, lines 10 - 15 ???
…[102 more quoted lines elided]…
›
```

#### ↳ Re: What is wrong with my program???????

- **From:** "antonio labrador" <ua-author-17074120@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p5@usenetarchives.gap>`
- **In-Reply-To:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`

```
Hi, I'm Spanish

The program runs good.

Bye
```

#### ↳ Re: What is wrong with my program???????

- **From:** "pa..." <ua-author-6589140@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p6@usenetarchives.gap>`
- **In-Reply-To:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`

```

Well, other than LABEL RECORDS being obsolete and
as useful as a broken lightbulb, I at least don't
see anything wrong with it.


Perhaps you can tell us what the error you are getting is?
You *did* create the file first, didn't you? And it *is*
supposed to be an indexed file, right? (You know you
cannot create this file with a text editor.)

Yours,
-Paul



Dsl8r (ds··.@a··.com) wrote:
: Can anyone PLEASE, I'M BEGGING YOU, OH PRETTY PLEASE, tell me what is wrong
: with the SELECT VENDOR-FILE statement, lines 10 - 15 ???
: The program is as follows:

: IDENTIFICATION DIVISION.
: PROGRAM-ID. VNDNEW01.

: *add a record to an indexed vendor file

: ENVIRONMENT DIVISION.
: INPUT-OUTPUT SECTION.
: FILE-CONTROL.

: SELECT VENDOR-FILE
: ASSIGN TO "vendor"
: ORGANIZATION IS INDEXED
: ACCESS MODE IS DYNAMIC
: RECORD KEY IS VENDOR-NUMBER.

: DATA DIVISION.
: FILE SECTION.

: FD VENDOR-FILE
: LABEL RECORDS ARE STANDARD.
: 01 VENDOR-RECORD.
: 05 VENDOR-NUMBER PIC 9(5).
: 05 VENDOR-NAME PIC X(30).
: 05 VENDOR-ADDRESS-1 PIC X(30).
: 05 VENDOR-ADDRESS-2 PIC X(30).
: 05 VENDOR-CITY PIC X(20).
: 05 VENDOR-STATE PIC X(2).
: 05 VENDOR-ZIP PIC X(10).
: 05 VENDOR-CONTACT PIC X(30).
: 05 VENDOR-PHONE PIC X(15).

: WORKING-STORAGE SECTION.

: PROCEDURE DIVISION.
: PROGRAM-BEGIN.
: OPEN I-O VENDOR-FILE.
: PERFORM MAIN-PROCESS.
: CLOSE VENDOR-FILE.


: PROGRAM-DONE.
: STOP RUN.

: MAIN-PROCESS.
: PERFORM INIT-VENDOR-RECORD.
: PERFORM ENTER-VENDOR-FIELDS.
: WRITE VENDOR-RECORD.

: INIT-VENDOR-RECORD.
: MOVE SPACE TO VENDOR-RECORD.
: MOVE ZEROES TO VENDOR-NUMBER.

: ENTER-VENDOR-FIELDS.
: PERFORM ENTER-VENDOR-NUMBER.
: PERFORM ENTER-VENDOR-NAME.
: PERFORM ENTER-VENDOR-ADDRESS-1.
: PERFORM ENTER-VENDOR-ADDRESS-2.
: PERFORM ENTER-VENDOR-CITY.
: PERFORM ENTER-VENDOR-STATE.
: PERFORM ENTER-VENDOR-ZIP.
: PERFORM ENTER-VENDOR-CONTACT.
: PERFORM ENTER-VENDOR-PHONE.

: ENTER-VENDOR-NUMBER.
: DISPLAY "ENTER VENDOR NUMBER (00001-99999)".
: ACCEPT VENDOR-NUMBER.

: ENTER-VENDOR-NAME.
: DISPLAY "ENTER VENDOR NAME".
: ACCEPT VENDOR-NAME.

: ENTER-VENDOR-ADDRESS-1.
: DISPLAY "ENTER VENDOR ADDRESS-1".
: ACCEPT VENDOR-ADDRESS-1.

: ENTER-VENDOR-ADDRESS-2.
: DISPLAY "ENTER VENDOR ADDRESS-2".
: ACCEPT VENDOR-ADDRESS-2.

: ENTER-VENDOR-CITY.
: DISPLAY "ENTER VENDOR CITY".
: ACCEPT VENDOR-CITY.
:
: ENTER-VENDOR-STATE.
: DISPLAY "ENTER VENDOR STATE".
: ACCEPT VENDOR-STATE.

: ENTER-VENDOR-ZIP.
: DISPLAY "ENTER VENDOR ZIP".
: ACCEPT VENDOR-ZIP.

: ENTER-VENDOR-CONTACT.
: DISPLAY "ENTER VENDOR CONTACT".
: ACCEPT VENDOR-CONTACT.
:
: ENTER-VENDOR-PHONE.
: DISPLAY "ENTER VENDOR PHONE".
: ACCEPT VENDOR-PHONE.
```

##### ↳ ↳ Re: What is wrong with my program???????

- **From:** "lookin'" <ua-author-915283@usenetarchives.gap>
- **Date:** 1998-08-26T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1da2cff3b2-p6@usenetarchives.gap>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com> <gap-1da2cff3b2-p6@usenetarchives.gap>`

```
On 19 Aug 1998 01:19:56 GMT, pa··.@b··.com (paulr) wrote:

› 
› Well, other than LABEL RECORDS being obsolete and 
…[7 more quoted lines elided]…
› cannot create this file with a text editor.) 
 
› Dsl8r (ds··.@a··.com) wrote:
› : Can anyone PLEASE, I'M BEGGING YOU, OH PRETTY PLEASE, tell me what is wrong
…[32 more quoted lines elided]…
› :            WRITE VENDOR-RECORD.
[snip rest of code]

I am not sure what platform you are using or what error you are
receiving, but there are a few things you might want to look at.

1. Some compilers require the data name specified by the
RECORD KEY clause to have an alphanumeric picture.
You could solve this by creating a new key name that has
a PIC X(5) picture, and then using REDEFINES for you numeric
VENDOR-NUMBER field.

2. While probably not useful, the LABEL RECORDS clause is not
likely to be causing you a problem.

3. Creation of a new indexed file is implementor-dependent.
ï¿½ Some implementations require the file to first be created
via a separate utility program, and then its records
written after opening the file in the I-O mode. If this
is the case in your implementation, then your method should
work, assuming that the new file is created first.
ï¿½ Other implementations will allow you to directly create a
new indexed file by opening the file I-O, as your program
is doing.
ï¿½ Still other implementations will require you to first open
the file OUTPUT. If you do this, then the ACCESS MODE must
be RANDOM; otherwise, open the file OUTPUT, then close it,
and then reopen it I-O (access can be DYNAMIC).
4. Most implementors will require you to either use an INVALID KEY
clause on your WRITE statement or to have a USE procedure in the
DECLARATIVES portion of your program to handle the file.

I hope some of this may point you toward your problem. Good luck.

Reply Addr:-->WDavid dot Simon at ATL dot frb dot org<--
-------------------De··y@Spa··r.Trasher----------------
```

#### ↳ Re: What is wrong with my program???????

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p8@usenetarchives.gap>`
- **In-Reply-To:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`

```
Under RM/COBOL and ACUCOBOL this code is correct.
for this program to work like it is then you will
need the indexed file to be created by another program.

It also does not test for invalid key on the write but
that is homework.

Frederico Fonseca
```

#### ↳ Re: What is wrong with my program???????

- **From:** "ds..." <ua-author-813600@usenetarchives.gap>
- **Date:** 1998-08-19T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p9@usenetarchives.gap>`
- **In-Reply-To:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`

```
The problem has been solved, I think. It appears that, in the program, I
needed to add:

INVALID KEY
DISPLAY "RECORD ALREADY ON FILE".
at some point in the program. This solved the compile problem. It is not
running as of yet, but I am sure that I will get it going when I work on it in
the morning.

My thanks to all of you who took the time to read and reply to my problem. I
am new to the newsgroup thing, but all of you have shown me what a wonderful
and powerful resource it can be. Thank you all!!!

Daniel
```

#### ↳ Re: What is wrong with my program???????

- **From:** "ribamar ferreira" <ua-author-17074406@usenetarchives.gap>
- **Date:** 1998-08-23T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1da2cff3b2-p10@usenetarchives.gap>`
- **In-Reply-To:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`
- **References:** `<1998081821220400.RAA06547@ladder03.news.aol.com>`

```
Sorry but you don't identify what environmment you are using ??

1- Well, you don't specify a file-status to indexed file
(You must specify this file status and test them)

2 - A VSAM file open at I-O must not to be empty (in COBOL II at VSE
environmment)

3 - Are you making a COBOL program to run in PC ??
(I am say this because you get fields in a one to one basis therefore
this is no a CICS environmment and VM is not apropriate do this)


So, I can not help you before know what environmment. Good luck.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
