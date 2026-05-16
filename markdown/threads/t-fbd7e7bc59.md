[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# More than one tapes in Cobol 85 / VSE

_4 messages · 4 participants · 1999-08_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### More than one tapes in Cobol 85 / VSE

- **From:** "Dirk Kalle" <rewe.dortmund.kalle@t-online.de>
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7op8c5$rlq$1@news04.btx.dtag.de>`

```
We have problems, if we work with more than 1 tapes in a Cobol-Program.
We can read the first Input-Tape, then we make a close of Input-Tape.
Then we want read the next Tape (after Open) and get an error.
If you have an Idea, answer me please.

Thanks

Dirk Kalle
REWE Dortmund
Groï¿½handel eG
```

#### ↳ Re: More than one tapes in Cobol 85 / VSE

- **From:** allenmc@my-deja.com
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7opggi$f9i$1@nnrp1.deja.com>`
- **References:** `<7op8c5$rlq$1@news04.btx.dtag.de>`

```
In article <7op8c5$rlq$1@news04.btx.dtag.de>,
  "Dirk Kalle" <rewe.dortmund.kalle@t-online.de> wrote:
> We have problems, if we work with more than 1 tapes in a Cobol-
Program.
> We can read the first Input-Tape, then we make a close of Input-Tape.
> Then we want read the next Tape (after Open) and get an error.
…[8 more quoted lines elided]…
>
What file status are you getting when you open the file for the second
tape?


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

#### ↳ Re: More than one tapes in Cobol 85 / VSE

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7opikg$nu6@dfw-ixnews3.ix.netcom.com>`
- **References:** `<7op8c5$rlq$1@news04.btx.dtag.de>`

```
There were several APARs against close (especially WITH LOCK - as I recall)
for VS COBOL II on VSE.  If you have access to IBMLink (or equivalent) check
for those - or check with IBM support about this topic.
```

#### ↳ Re: More than one tapes in Cobol 85 / VSE

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1999-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<628D89614F176495.E51B548EC6813A4B.5871FAC59F645658@lp.airnews.net>`
- **References:** `<7op8c5$rlq$1@news04.btx.dtag.de>`

```
On Tue, 10 Aug 1999 15:07:45 +0200, "Dirk Kalle"
<rewe.dortmund.kalle@t-online.de> enlightened us:

>We have problems, if we work with more than 1 tapes in a Cobol-Program.
>We can read the first Input-Tape, then we make a close of Input-Tape.
…[9 more quoted lines elided]…
>

What is the error?  What is the platform?  What compiler?  

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Some days your the dog.  Some days your the hydrant.


 Steve
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
