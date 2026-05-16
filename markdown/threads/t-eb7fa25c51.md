[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help

_5 messages · 5 participants · 1998-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: help

- **From:** "jeff" <tinman@ync.net>
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71n933$f64$1@supernews.com>`
- **References:** `<71m8i7$18g$1@supernews.com>`

```
its me i read the replys and u way that u need to see the code so here it is



       1500-CREATE-REPORT SECTION.


       1600-CREATE-REPORT.
            OPEN OUTPUT PRINT-FILE
            MOVE "N" TO EOF-FLAG
            RETURN EMPSORT-WORK-FILE
            PERFORM UNTIL EOF-FLAG = "Y"
                WRITE PRINT-RECORD FROM HEAD1 AFTER PAGE
                WRITE PRINT-RECORD FROM HEAD2 AFTER 5
                WRITE PRINT-RECORD FROM HEAD3 AFTER 10
                PERFORM UNTIL EOF-FLAG = "Y"

                MOVE EWR-NAME TO DL-NAME
                MOVE EWR-MM TO DL-BD-MM
                MOVE EWR-DD TO DL-BD-DD
                MOVE EWR-YY TO DL-BD-YY
                WRITE PRINT-RECORD FROM DETAIL-LINE AFTER 1






    jeff wrote in message <71m8i7$18g$1@supernews.com>...
    im write a sort program for school for a lab and i keep get a "imperative statement missing when i tell it to perform until eof-flag = "y"
    i move "n" to the eof-flag after it read all my records then released then to my sort work file
     
    thanx for the help
    jeff :)
```

#### ↳ Re: help

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981103160021.24009.00003275@ng-fd1.aol.com>`
- **References:** `<71n933$f64$1@supernews.com>`

```
"jeff" <tinman@ync.net>
Date: Tue, 3 Nov 1998 10:00:02 -0600

listed code 
>>
       1500-CREATE-REPORT SECTION.
       1600-CREATE-REPORT.
            OPEN OUTPUT PRINT-FILE
            MOVE "N" TO EOF-FLAG
            RETURN EMPSORT-WORK-FILE
            PERFORM UNTIL EOF-FLAG = "Y"
                WRITE PRINT-RECORD FROM HEAD1 AFTER PAGE
                WRITE PRINT-RECORD FROM HEAD2 AFTER 5
                WRITE PRINT-RECORD FROM HEAD3 AFTER 10
                PERFORM UNTIL EOF-FLAG ="Y"

                MOVE EWR-NAME TO DL-NAME
                MOVE EWR-MM TO DL-BD-MM
                MOVE EWR-DD TO DL-BD-DD
                MOVE EWR-YY TO DL-BD-YY
                WRITE PRINT-RECORD FROM DETAIL-LINE AFTER 1
<<
and commented
>>.
    im write a sort program for school for a lab and i keep get a =
"imperative statement missing when i tell it to perform until eof-flag =
= "y"
    i move "n" to the eof-flag after it read all my records then =
released then to my sort work file
    thanx for the help
<<

With the listed code, the most likely statement to be needing an imperative
statement is the OPEN.

The PRINT-FILE probably already exists, due to previous attempted runs, or
cannot be created (because of failure to meet the SELECT / ASSIGN statement
requirements).

You are learning a good lessson. You will return to the issue a million times. 
If you code an I/O statement of any kind, you definitely need a status code
check. OPEN, RETURN, WRITE all need specific checks.   

You definitely need checks after each and every WRITE.  You will find your self
doing MOVES and performing a common WRITE routine soon, to reduce the number of
WRITE/check status statement sequences.

You need to check the status after every I/O, whether the I/O is performed by
your native COBOL code directly, or by IMS, DB2 (or any SQL) or CICS.  You can
not assume that any initial function like OPEN, just works. You must check it. 
The same is true for CLOSE!

I agree with the other poster who commented to the effect that  a
                PERFORM UNTIL EOF-FLAG ="Y"
within a 
           PERFORM UNTIL EOF-FLAG = "Y"
is highly suspicious.

An advanced tip here is that it is usually weak to PERFORM until a specific
value.  Instead it is better to PERFORM until not a specific value.
For example,
     MOVE 'N' to EOF-FLAG
     PERFORM UNTIL NOT EOF-FLAG="N" 
This way you can post other 'not okay' values in the flag (like "E" for
unexpected Error), and shunt the loop.  Also allows the program to stop as a
side effect of damaged working storage (such a bug in population of flag or a
wild subscript).

With time you will learn to establish a FILE STATUS field associated with each
file.  You can initialize this, and set up a group of acceptable values as an
88 level. Then perform until not acceptable-condition.  Then anything
unexpected or otherwise educational will halt the program. Recommend that you
use the structure init-okay/perform until NOT okay for everything as a first
approach.

With the amount of I/O you are undertaking, and it is ambitious for an early
program, you would do well to modularize more.  Generally, and this is not
intended to start a grand style debate, just a way to get you out of trouble
for a while, every I/O statement can have its own paragraph.

A classical techinque, called HIPO, isolates each specific Input, Process and
Output to a separately performed paragraph, (not that you have to become an old
geezer, just to code COBOL, but it helps to do one thing at a time).

This approach will help you when you move on to the large scale I/O support
facilities.  Error handling in CICS, DB2 and IMS can get very involved because
a lot can happen each time you let go of control of the executable environment.
 It is much more so today than in the past that the service modules will pass
control back to you rather than abend. So you need to not only understand many
error conditions, but you need to be very fluid in your ability to structure
the program to deal with the unexpected.

Generally, if you have an I/O statement, and you do not follow it with a status
check (and there are no old-style declaratives), then that code is essentially
wrong. You have got to keep coding the status code checks. 

It will be much easier to code and debug I/O paragraphs if you keep all of the
processing of the buffer (MOVES to/from the buffer) isolated to it's own
conditionally performed paragraph.

As an aside, you probably would benefit from the use of explicit scope
terminators.  If you code an inline PERFORM, use an END-PERFORM.  It will help
those who read your code to understand it, and you are the most likely one to
read it.

Best Wishes, 


Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: help

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71o4u3$4s9$1@news.igs.net>`
- **References:** `<71m8i7$18g$1@supernews.com> <71n933$f64$1@supernews.com>`

```

jeff wrote in message <71n933$f64$1@supernews.com>...
its me i read the replys and u way that u need to see the code so here it is

It is a bit hard to know where to start ... the code that you
have shown makes very little sense.  But let's start with
some basics.

The flag that you have named EOF-FLAG never gets changed
to "Y" anywhere in your code sample at all.  Whatever else is
wrong, the code would run forever.  The norm is something along
the line of:

    open input data-file.
    move "N" to EOF-FLAG.
    read data-file at end
        move "Y" to EOF-FLAG
        do something about an empty file here.
    perform write-report until EOF-FLAG is equal to "Y".

write-report.
    do a bunch of writing here.
    read data-file at end
        move "Y" to EOF-FLAG.


There is also no termination anywhere below, which is probably
what is causing you to get the error message.  Sentences end
in periods.  There are none below.  It never ends. The in-line
perform also needs a terminator.

       1500-CREATE-REPORT SECTION.


       1600-CREATE-REPORT.
            OPEN OUTPUT PRINT-FILE
            MOVE "N" TO EOF-FLAG
            RETURN EMPSORT-WORK-FILE
            PERFORM UNTIL EOF-FLAG = "Y"
                WRITE PRINT-RECORD FROM HEAD1 AFTER PAGE
                WRITE PRINT-RECORD FROM HEAD2 AFTER 5
                WRITE PRINT-RECORD FROM HEAD3 AFTER 10
                PERFORM UNTIL EOF-FLAG = "Y"

                MOVE EWR-NAME TO DL-NAME
                MOVE EWR-MM TO DL-BD-MM
                MOVE EWR-DD TO DL-BD-DD
                MOVE EWR-YY TO DL-BD-YY
                WRITE PRINT-RECORD FROM DETAIL-LINE AFTER 1






    jeff wrote in message <71m8i7$18g$1@supernews.com>...
    im write a sort program for school for a lab and i keep get a
"imperative statement missing when i tell it to perform until eof-flag = "y"
    i move "n" to the eof-flag after it read all my records then released
then to my sort work file

    thanx for the help
    jeff :)
```

##### ↳ ↳ Re: help

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1998-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36410E01.C9CE127C@ix.netcom.com>`
- **References:** `<71m8i7$18g$1@supernews.com> <71n933$f64$1@supernews.com> <71o4u3$4s9$1@news.igs.net>`

```
You need to put in END-PERFORM's to matcht the inline performs.

Donald Tees wrote:

> jeff wrote in message <71n933$f64$1@supernews.com>...
> its me i read the replys and u way that u need to see the code so here it is
…[52 more quoted lines elided]…
>     jeff :)
```

#### ↳ Re: help

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981103131747.29493.00001854@ngol08.aol.com>`
- **References:** `<71n933$f64$1@supernews.com>`

```

In article <71n933$f64$1@supernews.com>, "jeff" <tinman@ync.net> writes:

>            PERFORM UNTIL EOF-FLAG =3D "Y"
>                WRITE PRINT-RECORD FROM HEAD1 AFTER PAGE
…[9 more quoted lines elided]…
>

Are you coding in-line PERFORMs in both cases? Do you end the scope of each one
with an END-PERFORM?
Mark A. Young
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
