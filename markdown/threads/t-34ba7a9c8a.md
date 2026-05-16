[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# decompiler

_5 messages · 4 participants · 2000-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### decompiler

- **From:** "Michael S. Morris" <mmorris@kc.rr.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NGQh4.5779$uI1.89882@typhoon2.kc.rr.com>`

```
I hope someone can help.  I'm looking for a decompiler for Cobol.  I have a
program that I need to see the source code to get the database layouts for
the data files.  Unless someone can help me determine how to read the data
files without decompiling the program.  MSAccess will not touch the files.

Thanks in advance
```

#### ↳ HOW: Re: decompiler

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000120235745.03571.00000651@ng-cn1.aol.com>`
- **References:** `<NGQh4.5779$uI1.89882@typhoon2.kc.rr.com>`

```
What platform?  Any kind of information on the whther the files are keyed or
indexed in some way?  How are the files created?

The few decompilers I've seen are somewhat difficult to use well, requiring a
better than casual knowledge of ASM on the platform the program executes on. 
I've never seen one that takes the code back to COBOL, only to Assembler, but
such a tool may exist.  You might also check some of the data recovery services
- they may have a way of "parsing" the data files to extract useful
information.
Asimov, Heinlein, and Zappa
Still the best
```

##### ↳ ↳ Re: HOW: Re: decompiler

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38886B70.643FF4B1@NOSPAMwebaccess.net>`
- **References:** `<NGQh4.5779$uI1.89882@typhoon2.kc.rr.com> <20000120235745.03571.00000651@ng-cn1.aol.com>`

```
My take on a decompiler is that they are like having a house decompiler:

If you take the house apart to its smallest components (assembler), you
can be fairly accurate in what they were.  But if you built the house
from bigger components (COBOL commands), it is harder to tell where one
pre-assembled piece started and another one ended.  It's especially hard
if your optimizer shaved pieces of one component, moving pieces from one
wall to another.  And most of the structure of a program is for our
(programmer) use only.  Once the house or program is built, the
methodology used is gone, all you have is the results.  We can make
educated guesses, but that's about all.

That might be sufficient.  An archeologist can rebuild an old building
if he doesn't care whether he built it exactly the same way as the
original builder did.  But the use of a decompiler has to be in
determining what the program does so that it can be re-built.  But isn't
it just as effective to ask the users what it does?
```

###### ↳ ↳ ↳ Re: HOW: Re: decompiler

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 2000-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000124005820.03560.00001234@ng-ce1.aol.com>`
- **References:** `<38886B70.643FF4B1@NOSPAMwebaccess.net>`

```
>  But the use of a decompiler has to be in
>determining what the program does so that it can be re-built.  But isn't
>it just as effective to ask the users what it does?

For all but the most simple of programs, my experience is that the users will
not know - If they are more than usually quick, they will know which screen
they enter individual data items, and they may know report names, and
sometimes, depending on how the output is identified and routed, will know the
name of the job that produces it.  But you can not expect a user to know that a
program will validate the transaction record's fields, report errors and
re-queue the records with errors for correction, apply the updates to a
journal, several working files for reports, and more than 7 DB2 data bases. 
This is an actual description of a program I had to change during Y2K that I
particularly remember.
Asimov, Heinlein, and Zappa
Still the best
```

#### ↳ Re: decompiler

- **From:** "Jeff Lanam" <jeff.lanam@.n.o.s.p.a.m.compaq.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86aa5t$cd7$1@mailint03.im.hou.compaq.com>`
- **References:** `<NGQh4.5779$uI1.89882@typhoon2.kc.rr.com>`

```

Michael S. Morris wrote in message ...
>I hope someone can help.  I'm looking for a decompiler for Cobol.  I have a
>program that I need to see the source code to get the database layouts for
>the data files.  Unless someone can help me determine how to read the data
>files without decompiling the program.  MSAccess will not touch the files.
>

If all you need is the structure of the records, you may not need to
decompile
the whole program.  If you can get a description of the interface to the
language
run-time library, you might be able to examine the calls to the I/O
routines.
These should have parameters which specify the types of the data items
being read. I'm making a lot of assumptions here about the implementation,
of course.  Contact your compiler vendor.

Someone compared decompiling an object program to disassembling
a pre-fab house back to its components.  I'd say it's closer to turning a
cake back into flour, butter and eggs.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
