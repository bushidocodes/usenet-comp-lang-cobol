[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL COPYBOOK

_1 message · 1 participant · 1998-07_

---

### Re: COBOL COPYBOOK

- **From:** findit@end.of.message (Siegen)
- **Date:** 1998-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<359f7b83.19225649@news.comcen.com.au>`
- **References:** `<1998051502112800.WAA00804@ladder03.news.aol.com> <1998051503403000.XAA17845@ladder01.news.aol.com> <01bd8020$4adf5120$cef63bc0@mv-stevencc.mv.unisys.com> <6jr7gi$65v@sjx-ixn2.ix.netcom.com>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote:

:> Charles Stevens wrote in message
[snip]

:> >>   01  :PREFIX:-MASTER-REC.

:> >>  COPY bookname REPLACING ==:PREFIX:== BY ==M01==.
:> >> (The colons were used above to help set apart pieces 
:> >> that the REPLACING language could work on.)


:> >While some implementations would allow this, others would 
:> >not. Programs that make use of this feature may not be portable 
:> >to other systems.

:>   This is NOT true.  Using colons to delimit a prefix to 
:> be replaced will work with ANY compiler that conforms to 
:> the ANS'85 Standard.  It is true that older compilers 
:> (ANS'74 or earlier) will not accept this - but those
:> are pretty well disappearing as Y2K support becomes 
:> more important.

:> Bottom-line - the sample code will work and will be portable 
:> to any ANS'85 conforming compiler.
I still use the MicroSoft/MicroFocus Version 3.00
cobol compiler for D.O.S. 
It is set to use ANS85 features.

"COPY bookname REPLACING ==:PREFIX:== BY ==M01==."
This compiler rejects the colons and stops after
"swearing" at me in microsoftese.

If I omit the colons, it still won't do the
copy-replacing unless EACH LINE to be so modified
is expressly coded!! --- funnily enough though, it
compiles O.K. as far as when, in the "procedure
division", it encounters a use of the NEW field
name then stops after telling me that it has NOT
been declared.

e.g. of what works:

"COPY bookname REPLACING ==w100-field1== BY
==z999-field1=="

So, I have to do this for every field, therefore
it's easier just to create another library with
the fields already renamed to the new name.

Other ANS85 features work as they should.

(My "Fujitsu" compiler is much more civillised
though.)


-- Siegen 
---------------------- 
Please remove the letter "x" from my email address, should you wish
to email me.
(rodsp@comxcen.com.au)
---------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
