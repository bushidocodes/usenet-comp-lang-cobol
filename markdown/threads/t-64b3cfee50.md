[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# delete

_3 messages · 3 participants · 1999-04 → 1999-05_

---

### delete

- **From:** dupavoy@aol.combatSPAM (Dupavoy)
- **Date:** 1999-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990423102811.09928.00000487@ng144.aol.com>`

```
I would like to use the delete command instead
of doing the following:
move spaces to bookauthor
                        booktitle
                        bookprice

I also get an error because bookprice has an PIC 9(4) not an PIC X(4).


***********************************
-CPR--subscribe@onelist.com   
 - Computer PRogramming list

PCHelpDesk-subscribe@onelist.com 
- PC software/hardware list
*******************************************
```

#### ↳ Re: delete

- **From:** Simon Martens <smart@sunshine.nl>
- **Date:** 1999-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372205FA.324BBD1A@sunshine.nl>`
- **References:** `<19990423102811.09928.00000487@ng144.aol.com>`

```
Hello,

You asked two questions, so I'll give you two answers.

First: you want to delete fields in stead of initializing them.

Is there any good reason for deleting them? By moving spaces
into them or by stating "INITIALIZE BOOKAUTHOR, BOOKTITLE,
BOOKPRICE" you erase their contents, to be able to use them
again, and that is okay and superfluous.

It is okay, because it is safe programming. It is superfluous
for experienced programmers who do not need this kind of
strong protection against logical errors any more. If you
move "P.P. Cooper" into a field BOOKAUTHOR that has p.e.
PIC X(20), then after Cooper's name the computer will fill
spaces for you, so that the name that was there before and
that maybe contained 13 characters, will be totally erased.

The command DELETE can only be used for records, not for fields.
This command destroys the container, not only the contents!
So if you would succeed in deleting your 3 fields, after that
the programm would't be able to use them any more. Is that what
you want the programm to do? Then code your PROCEDURE DIVISION
in such a way that after having used these fields, the program
avoids them.

Second: how to move SPACES to a field with PIC 9(4)? Move ZERO
unless the output file is a printed report. If it is a report,
in your DATA DIVISION create a group item for BOOKPRICE as
follows:
     01  BOOKPRICE-X.
         05  BOOKPRICE           PIC 9(4).
After that, in your PROCEDURE DIVISION code this:
         MOVE SPACES TO BOOKPRICE-X
That is all there is to it.

Good luck!

- Simon -


Dupavoy wrote:
> 
> I would like to use the delete command instead
…[13 more quoted lines elided]…
> *******************************************
```

#### ↳ Re: delete

- **From:** "ChrisOsborne" <chris.osborne@eds.com>
- **Date:** 1999-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gl5mq$7j6$1@news.ses.cio.eds.com>`
- **References:** `<19990423102811.09928.00000487@ng144.aol.com>`

```
Dupavoy,

On the DELETE command: Can I see the code?


In addition, you may not MOVE spaces to a numeric display item.
Spaces are non-numeric.  If you want the bytes occupying that field to
have x'40' (or ascii equivalent), then redefine those bytes as PIC
X(4), and move the spaces to the redefined field.  Of course, any math
operation on the original numeric field will fail after this move, but
since you have a reason to move spaces to it, I doubt the code will be
doing math on the numeric field after it has spaces in it.


Sincerely,
      Chris Osborne



Dupavoy <dupavoy@aol.combatSPAM> wrote in message
news:19990423102811.09928.00000487@ng144.aol.com...
> I would like to use the delete command instead
> of doing the following:
…[4 more quoted lines elided]…
> I also get an error because bookprice has an PIC 9(4) not an PIC
X(4).
>
>
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
