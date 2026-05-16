[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Initializing a FILLER

_8 messages · 6 participants · 1999-02_

---

### Initializing a FILLER

- **From:** "Erlend Moen" <erlend@disys.no>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7975em$4mj$1@troll.powertech.no>`

```
Recently, I was debugging an old program, and the error I found was that the
programmer was trying to initialize a field defined as FILLER. The intention
was to fill the complete field with spaces, but it didn't do anything with
the field at all. This program demonstrates the "problem":

       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTINIT.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       77  WS-JA                    PIC X.
       01  WS-TEST-FIELD            PIC X(30).
       01  WS-TEST-FIELD-R REDEFINES WS-TEST-FIELD.
           03  WS-TEST-STRING       PIC X(10).
           03  WS-TEST-NUMBER       PIC 9(10).
           03  FILLER               PIC X(10).

       PROCEDURE DIVISION.
       MAIN SECTION.
       MAIN-010.

           MOVE    ALL "A"          TO WS-TEST-FIELD.
           DISPLAY WS-TEST-FIELD.

           INITIALIZE WS-TEST-FIELD-R.
           MOVE    "Number...:"     TO WS-TEST-STRING.
           MOVE    12345            TO WS-TEST-NUMBER.
           DISPLAY WS-TEST-FIELD-R.

           ACCEPT WS-JA.
           STOP RUN.

       MAIN-EXIT.
           EXIT.

The problem is easily solved of course by renaming FILLER to a dummy-name,
but I must admit that I have never imagined that a filler defines as PIC X
won't be filled with spaces when I initialize it...

Can anyone explain for me why it is so?

Regards,
Erlend Moen
DI Systemer AS
Norway
```

#### ↳ Re: Initializing a FILLER

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<797mlc$1ohk$1@news-inn.inet.tele.dk>`
- **References:** `<7975em$4mj$1@troll.powertech.no>`

```

Erlend Moen skrev i meddelelsen <7975em$4mj$1@troll.powertech.no>...
>Recently, I was debugging an old program, and the error I found was that
the
>programmer was trying to initialize a field defined as FILLER. The
intention
>was to fill the complete field with spaces, but it didn't do anything with
>the field at all. This program demonstrates the "problem":
> [..program...]


It would be very bothersome for me if an initialize did indeed clear the
fillers. I use a lot of code like

01 print-line.
  05 filler                   pic x(?) value "some fixed text".
  05 variable-text     pic x(?).
  05 filler                   pic x(?) value "more fixed text".
  05 some-number  pic 9(?).

Then, I send the complete line to the printer or a text file. Sometimes, I
want to clear the fields, and so
use an

initialize print-line.

Now, if this were to clear my fixed texts, I wouldn't be very unhappy!

Kennet
```

##### ↳ ↳ Re: Initializing a FILLER

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b75227.7478673@news3.ibm.net>`
- **References:** `<7975em$4mj$1@troll.powertech.no> <797mlc$1ohk$1@news-inn.inet.tele.dk>`

```
On Tue, 2 Feb 1999 21:17:39 +0100, "kennet" <kennet@post11.tele.dk> wrote:


>
>01 print-line.
…[11 more quoted lines elided]…
>Now, if this were to clear my fixed texts, I wouldn't be very unhappy!


Oh, And I WOULD be very unhappy <g>

with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: Initializing a FILLER

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<797sq7$3j50$1@news-inn.inet.tele.dk>`
- **References:** `<7975em$4mj$1@troll.powertech.no> <797mlc$1ohk$1@news-inn.inet.tele.dk> <36b75227.7478673@news3.ibm.net>`

```

Volker Bandke skrev i meddelelsen <36b75227.7478673@news3.ibm.net>...
>On Tue, 2 Feb 1999 21:17:39 +0100, "kennet" <kennet@post11.tele.dk> wrote:
>>
…[6 more quoted lines elided]…
>


Oops. Guess I'd be unhappy about it as well! And I wonder why my programs
never work...
You put in an extra "not" here and there in the source - hey, what's the
difference. :)

Kennet
```

###### ↳ ↳ ↳ Re: Initializing a FILLER

- **From:** "kennet" <kennet@post11.tele.dk>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<797srs$ui0$1@news-inn.inet.tele.dk>`
- **References:** `<7975em$4mj$1@troll.powertech.no> <797mlc$1ohk$1@news-inn.inet.tele.dk> <36b75227.7478673@news3.ibm.net>`

```

Volker Bandke skrev i meddelelsen <36b75227.7478673@news3.ibm.net>...
>On Tue, 2 Feb 1999 21:17:39 +0100, "kennet" <kennet@post11.tele.dk> wrote:
>>
…[6 more quoted lines elided]…
>


Oops. Guess I'd be unhappy about it as well! And I wonder why my programs
never work...
You put in an extra "not" here and there in the source - hey, what's the
difference. :)

Kennet
```

##### ↳ ↳ Re: Initializing a FILLER

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36B7708C.229B950D@NOSPAMhome.com>`
- **References:** `<7975em$4mj$1@troll.powertech.no> <797mlc$1ohk$1@news-inn.inet.tele.dk>`

```
kennet wrote:

> It would be very bothersome for me if an initialize did indeed clear the
> fillers. I use a lot of code like
…[13 more quoted lines elided]…
> Now, if this were to clear my fixed texts, I wouldn't be very unhappy!

But wouldn't it be lovely to be able to INITIALIZE TO DEFAULT or
something to get back the VALUE clause values?
```

###### ↳ ↳ ↳ Re: Initializing a FILLER

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7982ip$f3b@sjx-ixn9.ix.netcom.com>`
- **References:** `<7975em$4mj$1@troll.powertech.no> <797mlc$1ohk$1@news-inn.inet.tele.dk> <36B7708C.229B950D@NOSPAMhome.com>`

```

Howard Brazee wrote in message <36B7708C.229B950D@NOSPAMhome.com>...
>kennet wrote:
>
…[9 more quoted lines elided]…
>> Then, I send the complete line to the printer or a text file. Sometimes,
I
>> want to clear the fields, and so
>> use an
…[6 more quoted lines elided]…
>something to get back the VALUE clause values?

So nice that both options exist in the draft of the next Standard, i.e. an
option to initialize filler and an option to initialize to the "original"
VALUE clause.

Contact *YOU* vendor of choice to see when they expect to make such options
available as extensions - because given the current rate of lack of
approval, you sure won't want to wait until the draft is approved!
```

#### ↳ Re: Initializing a FILLER

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36B72CAF.D14E07F1@ASPMnetdoor.com>`
- **References:** `<7975em$4mj$1@troll.powertech.no>`

```
When you use INITIALIZE, the compiler creates the equivalent statements MOVE
ZERO TO ..
or MOVE SPACE TO for each field under the group you named in INTIALIZE.  Since
you can't code MOVE SPACE TO FILLER, the INITIALIZE statement can't do that for
you either.  A value clause on a stand-alone filler would work (not the case
here though).  HTH

Erlend Moen wrote:

>
>        WORKING-STORAGE SECTION.
…[29 more quoted lines elided]…
> Can anyone explain for me why it is so?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
