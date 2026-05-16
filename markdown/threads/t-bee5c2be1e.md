[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call external Application for example Word

_2 messages · 2 participants · 2001-09_

---

### Call external Application for example Word

- **From:** "Thomas H���rkens" <thoerkens@rsw-orga.de>
- **Date:** 2001-09-20T16:09:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<datco9.tbb.ln@gw1.rsw-orga.de>`

```
Hello,

i work with the ACU-BENCH 5.1 from ACUCORP

i search for the syntax to resolve the following questions


    how can i start a external Application like Word, Excel ..... ?
    how can i modify the text in Word-Documents  ?
    how can i replace Text or a Variable in Word-Documents ?
    how can i call the PrintPreview of an Word-Document ?

I'm awfully sorry that i can't exact describe this problems because my
English is terribly

Thanks for your help

Tom
```

#### ↳ Re: Call external Application for example Word

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 2001-09-28T22:06:23+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VtqqLRUPZOt7IwlS@rcav8r.demon.co.uk>`
- **References:** `<datco9.tbb.ln@gw1.rsw-orga.de>`

```
Hi Thomas,

Your English is much better than my German! Ask Peter Kaiser in our
Friedrichsdorf office if you don't believe me...  ;^)

To answer your question, you need to use the AXDEFGEN program supplied
with version 5.1 to create an '.def' file for Word, this is copied into
your special names section. You can then use the features of Word
through some special syntax. An example is shown here:

CREATE APPLICATION OF WORD, HANDLE IN WORD-APP.
MODIFY WORD-APP, VISIBLE = 0.
MODIFY WORD-APP DOCUMENTS::OPEN(WS-FILE, 0, 1)
        GIVING WORD-DOC.
MODIFY WORD-DOC PRINT-PREVIEW().
MODIFY WORD-APP, VISIBLE = 1.


To be honest, to have this work to its best you need to understand a
reasonable amount about using Word as a COM object (or whatever they're
calling it this week!). You can get this through the MSDN I believe.

If it would help, please send me an email at <neaton@acucorp.com> and
I'll send you a ZIP file with an example in it.

Please do also talk to the people in the Acucorp Deutschland office,
they'd be very happy to help too.

Cheers

Nigel

In article <datco9.tbb.ln@gw1.rsw-orga.de>, Thomas Hï¿½rkens
<thoerkens@rsw-orga.de> writes
>Hello,
>
…[17 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
