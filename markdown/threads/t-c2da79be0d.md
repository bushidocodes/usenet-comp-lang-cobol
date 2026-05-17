[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol650 LINK (help)

_5 messages · 5 participants · 1996-09_

---

### Cobol650 LINK (help)

- **From:** "steve phillips" <ua-author-821793@usenetarchives.gap>
- **Date:** 1996-09-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bba1b1$705dcf20$2c8680c2@smidmore.idiscover.co.uk>`

```

I'm attempting to compile my own cobol code using the "cobol650" compiler.
I've succesfully created the .lst & .obj files and have now reached a point
where I need to create a link to the LIB. The problem is that I get an
error after typing in the link command ie. LINK FILENAME.COB,,,COBOL650. I
can only assume there is an error in the syntex that i'm using, I've tried
all the permutations I can think of without success. Are the three commas
required? Or do they represent a switch? The filename I'm using is
"add-ten.cob". Please could someone enlighten me as to the correct syntex
as i've now run out of ideas.

Home Page : http://www.cybercity.hko.net/london/smidmore/index.html

Do you know someone who has gone missing?

email details and a picture (jpeg, gif, bmp) and i'll include them on my
Missing Persons web site.
```

#### ↳ Re: Cobol650 LINK (help)

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1996-09-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2da79be0d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bba1b1$705dcf20$2c8680c2@smidmore.idiscover.co.uk>`
- **References:** `<01bba1b1$705dcf20$2c8680c2@smidmore.idiscover.co.uk>`

```

Steve Phillips (st··.@smi··o.uk) wrote:
: I'm attempting to compile my own cobol code using the "cobol650" compiler.
: I've succesfully created the .lst & .obj files and have now reached a point
: where I need to create a link to the LIB. The problem is that I get an
: error after typing in the link command ie. LINK FILENAME.COB,,,COBOL650. I
(snip)


If you use a period in the library name, then you must use the complete
name (Instead of COBOL650. use COBOL650 or COBOL650.LIB).

The line I use in my batch file is:

link %1,,,cobol650,,
```

##### ↳ ↳ Re: Cobol650 LINK (help)

- **From:** "your_name" <ua-author-96199@usenetarchives.gap>
- **Date:** 1996-09-14T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2da79be0d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2da79be0d-p2@usenetarchives.gap>`
- **References:** `<01bba1b1$705dcf20$2c8680c2@smidmore.idiscover.co.uk> <gap-c2da79be0d-p2@usenetarchives.gap>`

```

Jack Yazel wrote:
› 
› Steve Phillips (st··.@smi··o.uk) wrote:
 
› : error after typing in the link command ie. > : LINK FILENAME.COB,,,COBOL650.
›    (snip)
…[6 more quoted lines elided]…
›       link %1,,,cobol650,,

You may have simply mistyped your example, but I thought I would point
out that one of the most common mistakes when compiling from the command
line is to continue typing the original program's extension.

COBOL translates the program into machine code which is not yet combined
with code to emulate READ, WRITE, etc. This machine code is stored in
filename.OBJ; the link command adds additional code to the program and
creates the finished product. Make sure that you either do NOT specify
an extension, as in "LINK filename,,,COBOL650,," or you specify it as
".OBJ", as in "LINK filename.OBJ,,,COBOL650,,".

Now, I'm going to go see if adding that extra comma fixes the problem
of LINK not finding "COBLIB.LIB" or "COBAPI.LIB". If anyone knows what
that is all about, please let me know.

Thanks,
Ken Hartness
csc··.@sh··u.edu
```

###### ↳ ↳ ↳ Re: Cobol650 LINK (help)

- **From:** "csc..." <ua-author-17086101@usenetarchives.gap>
- **Date:** 1996-09-17T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2da79be0d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c2da79be0d-p3@usenetarchives.gap>`
- **References:** `<01bba1b1$705dcf20$2c8680c2@smidmore.idiscover.co.uk> <gap-c2da79be0d-p2@usenetarchives.gap> <gap-c2da79be0d-p3@usenetarchives.gap>`

```

Hmmm, my apologies for those who tried to reply directly to me by
e-mail. I must have been using some other news-reader.

› Now, I'm going to go see if adding that extra comma fixes the problem
› of LINK not finding "COBLIB.LIB" or "COBAPI.LIB".  If anyone knows 
…[5 more quoted lines elided]…
› csc··.@sh··u.edu

Is anyone else having this trouble? I borrowed a linker from another
compiler, so maybe it's just that linker. Or maybe the version I
downloaded doesn't have all the libraries included.
```

#### ↳ Re: Cobol650 LINK (help)

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-09-16T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2da79be0d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bba1b1$705dcf20$2c8680c2@smidmore.idiscover.co.uk>`
- **References:** `<01bba1b1$705dcf20$2c8680c2@smidmore.idiscover.co.uk>`

```

In message <<01bba1b1$705dcf20$2c8··.@smi··o.uk>> "Steve Phillips" writes:
› I've succesfully created the .lst & .obj files and have now reached a point
› where I need to create a link to the LIB. The problem is that I get an
› error after typing in the link command ie. LINK FILENAME.COB,,,COBOL650. I

And you don't think that it would be useful to mention what the
error message actually says ?

› can only assume there is an error in the syntex that i'm using, I've tried
› all the permutations I can think of without success.  Are the three commas
› required?  Or do they represent a switch?  The filename I'm using is
› "add-ten.cob".  Please could someone enlighten me as to the correct syntex
› as i've now run out of ideas.

Why are you trying to link the source code ?

Try LINK filename.OBJ,,,Cobol650;
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
