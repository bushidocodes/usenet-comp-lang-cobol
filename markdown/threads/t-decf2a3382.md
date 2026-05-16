[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem w/MF COBOL and MQDISC

_6 messages · 5 participants · 2003-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Problem w/MF COBOL and MQDISC

- **From:** paul.davis@watkins.com (paul davis)
- **Date:** 2003-07-14T11:48:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83569b3d.0307140723.33cd71f@posting.google.com>`

```
We are getting the following error message in our AIX 4.3.3
environment when we run a Micro Focus v 2.2 COBOL program and do a
MQDISC (MQ v 5.3) in the program:

Execution error : file 'WMTEST6'
error code: 114, pc=0, call=1, seg=0
114     Attempt to access item beyond bounds of memory (Signal 11)

We are compiling the program using Net Express v 3.1.11 and publishing
the executable to AIX.

Could you please cut and paste the following program and compile and
run it in your environment and see if you get the same error message?

Here is the test program I am using:

       PROGRAM-ID.               WMTEST6.
       AUTHOR.                   John Doe.
       INSTALLATION.             ABCDEF Co.
       DATE-WRITTEN.             July 14, 2003.
       DATE-COMPILED.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER.  IBM-AIX.

       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

       DATA DIVISION.

      *================================================================*
       WORKING-STORAGE SECTION.
      *================================================================*

       01  MQAPI-HCONN                 PIC S9(09).
       01  MQAPI-COMPLETION-CODE       PIC S9(09).
       01  MQAPI-REASON-CODE           PIC S9(09).

      *================================================================*
       PROCEDURE DIVISION.
      *================================================================*

           DISPLAY '*** BEFORE CONNECT'.

           CALL 'MQCONN' USING 'AQD2',
                               MQAPI-HCONN
                               MQAPI-COMPLETION-CODE
                               MQAPI-REASON-CODE.

           DISPLAY '*** AFTER CONNECT'.

           CALL 'MQDISC' USING MQAPI-HCONN,
                               MQAPI-COMPLETION-CODE,
                               MQAPI-REASON-CODE.

           DISPLAY '*** AFTER DISCONNECT'.


Thanks for your help.
```

#### ↳ Re: Problem w/MF COBOL and MQDISC

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-14T20:29:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f13117e.22255693@news.optonline.com>`
- **References:** `<83569b3d.0307140723.33cd71f@posting.google.com>`

```
paul.davis@watkins.com (paul davis) wrote:

>We are getting the following error message in our AIX 4.3.3
>environment when we run a Micro Focus v 2.2 COBOL program and do a
…[57 more quoted lines elided]…
>Thanks for your help.

My guess is the connection fails, then it gets a bad pointer when you try to
disconnect a connection that doesn't exist. Try displaying MQAPI-COMPLETION-CODE
after the connect.

Aren't the three variables supposed to be COMP? It will work ok the way you
wrote it, will use the first four bytes of the nine byte variables, but the
display will be meaningless.
```

#### ↳ Re: Problem w/MF COBOL and MQDISC

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-15T00:36:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-BB5DC8.00362015072003@corp.supernews.com>`
- **References:** `<83569b3d.0307140723.33cd71f@posting.google.com>`

```
In article <83569b3d.0307140723.33cd71f@posting.google.com>,
 paul.davis@watkins.com (paul davis) wrote:

> We are getting the following error message in our AIX 4.3.3
> environment when we run a Micro Focus v 2.2 COBOL program and do a
…[57 more quoted lines elided]…
> Thanks for your help.

I'm not an AIX guru, but I think MQ calls are standard across various 
platforms.  What is the 'AQD2' literal parm?

As much as I recall the first parm on a connect call was the HCONN.  
Perhaps you are warming your feet in your literal pool on that first 
call.

I freely admit that I might have the Qmgr out of order, but in that case 
a literal is totally inappropriate as it could be up to 64 bytes.  You 
might want to try:

   01 MQAPI-QMGR         PIC X(64) value 'AQD2'.

Maybe that will fix it.
```

##### ↳ ↳ Re: Problem w/MF COBOL and MQDISC

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2003-07-15T09:14:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf0cp6$8ud$1@hyperion.microfocus.com>`
- **References:** `<83569b3d.0307140723.33cd71f@posting.google.com> <joe_zitzelberger-BB5DC8.00362015072003@corp.supernews.com>`

```
I just checked the MQSeries docs, where they provide a COBOL example -- see
http://publibfp.boulder.ibm.com/epubs/html/csqzal09/csqzal09tfrm.htm . The
parameter block should be defined thus :

*    W02 - Data fields derived from the PARM field
 01  W02-MQM                     PIC X(48) VALUE SPACES.
*    W03 - MQM API fields
 01  W03-HCONN                   PIC S9(9) BINARY.
 01  W03-COMPCODE                PIC S9(9) BINARY.
 01  W03-REASON                  PIC S9(9) BINARY.

SimonT.
```

###### ↳ ↳ ↳ Re: Problem w/MF COBOL and MQDISC

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-15T16:07:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f141e2e.91049630@news.optonline.com>`
- **References:** `<83569b3d.0307140723.33cd71f@posting.google.com> <joe_zitzelberger-BB5DC8.00362015072003@corp.supernews.com> <bf0cp6$8ud$1@hyperion.microfocus.com>`

```
"Simon Tobias" <Simon.Tobias@nospam.microfocus.com> wrote:

>I just checked the MQSeries docs, where they provide a COBOL example -- see
>http://publibfp.boulder.ibm.com/epubs/html/csqzal09/csqzal09tfrm.htm . The
…[7 more quoted lines elided]…
> 01  W03-REASON                  PIC S9(9) BINARY.

The first parameter to MQCONN is the queue name. If you're getting it from a
PARM, as in the textbook example, then it needs to be a named variable. If
you're hard-coding it, as Paul did, a literal is fine. The COBOL function will
take care of string termination with null; you don't have to pad it with spaces.
```

###### ↳ ↳ ↳ Re: Problem w/MF COBOL and MQDISC

_(reply depth: 4)_

- **From:** davidmckinney@hotmail.com (David McKinney)
- **Date:** 2003-07-28T21:36:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b73e9a33.0307282036.13d0620d@posting.google.com>`
- **References:** `<83569b3d.0307140723.33cd71f@posting.google.com> <joe_zitzelberger-BB5DC8.00362015072003@corp.supernews.com> <bf0cp6$8ud$1@hyperion.microfocus.com> <3f141e2e.91049630@news.optonline.com>`

```
Was this problem ever resolved? We're getting the exact same problem
with an MQDISC call, but none of the suggested solutions are relevant
to us. We've just upgraded from MQ v5.2 to MQ v5.3 and the problem has
only reared its ugly head since the upgrade. All of our COBOL MQ
programs seem to be affected.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
