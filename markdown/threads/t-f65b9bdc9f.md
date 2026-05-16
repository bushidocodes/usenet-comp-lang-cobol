[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# In search of a PL/I - COBOL for OS/390 comparison

_2 messages · 2 participants · 1999-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: In search of a PL/I - COBOL for OS/390 comparison

- **From:** robin <robin_v@bigpond.com>
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.pl1,comp.lang.cobol
- **Message-ID:** `<KOlL3.418$_4.1086@newsfeeds.bigpond.com>`

```
"Denis" <grosnou@antispam.skynet.be> writes: > Hello,
> I'm trying to compare the COBOL & PL/I languages in order to write
> recommendations for our developers. Both language are available. Thousands
…[24 more quoted lines elided]…
> Many thanks in advance

My observations of COBOL and PL/I are:
.
It is quicker to write and to debug PL/I programs compared to the COBOL
equivalent.
.
A PL/I source program is about one-third shorter than its COBOL counterpart.
Thus the human resource cost of entering the source is less for PL/I.
.
COBOL programs take longer to reach a succesful compilation because:
.
	(1) the COBOL program has 33% more lines: more typos to correct;
	(2) the COBOL source is column sensitive: errors waste time for nothing;
	(3) COBOL has some 300 reserved words: inadvertant use of a keyword as
	    a variable name wastes time. (PL/I has no reserved words.)
.
COBOL programs take longer to debug, following successful compilation.
This is on account of the superior debug facilities of PL/I:
.
	* simple statements to write out variables (e.g., PUT DATA);
	* error trapping and display of variables, at the point where the
	  error occurs.
	* precise location of the statement in error;
	* enabling fixed-point and floating-point checks for overflow/underflow
	  for any part of or the whole program.
	* enabling checks for subscript violations for any part of or the whole
	  program;
	* enabling checks for substring violations for any part of or the whole
	  program;
	* trapping of computational errors, subscript errors, and substring
	  errors.
PL/I is largely machine-independent.
Optimization can be confined to specific regions of program, maintaining
statement order.
Specific sections of the program or the whole program can be highly optimized.
```

#### ↳ Re: In search of a PL/I - COBOL for OS/390 comparison

- **From:** deskware@my-deja.com
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.pl1,comp.lang.cobol
- **Message-ID:** `<7tl8a6$rr0$1@nnrp1.deja.com>`
- **References:** `<KOlL3.418$_4.1086@newsfeeds.bigpond.com>`

```
If you want to physically compare your COBOL and PL/I code, VACE
Maintenance Workbench can help you with this -- it decomposes both COBOL
and PL/I code into an on-screen navigable chart.  Check it out at
http://www.cobolscript.com/products.htm .

In article <KOlL3.418$_4.1086@newsfeeds.bigpond.com>,
  robin <robin_v@bigpond.com> wrote:
> "Denis" <grosnou@antispam.skynet.be> writes: > Hello,
> > I'm trying to compare the COBOL & PL/I languages in order to write
> > recommendations for our developers. Both language are available.
Thousands
> > of COBOL modules as thousands of PL/I modules are currently used in
> > production with language environment.
> > The comparison must be based on COBOL for OS/390 v 2.1 and PL/I for
OS/390 v
> > 1.1.1 running on OS/390 v1.3 with language environment v1.7 The OO
COBOL
> > extensions must not be considered, only the 'standard' COBOL
statements are
> > used.
> > The main criteria are:
…[6 more quoted lines elided]…
> > - Limits in the management of  memory (Limits in working-storage
size, size
> > of arrays...)
> > - Arithmetic limits & precisions (integers, floating points,
packed-decimal
> > variables...)
> > - Performance at execution (Quality of the compiler & optimizer)
> > - ILC with COBOL, PL/I, Assembler (For example PL/I fetch
limitations).
> > - ...?
> >
> > I've already gathered many information from the Language Reference
> > appendices sections for of each language but there are still large
gaps.
> >
> > Many thanks in advance
…[3 more quoted lines elided]…
> It is quicker to write and to debug PL/I programs compared to the
COBOL
> equivalent.
> .
> A PL/I source program is about one-third shorter than its COBOL
counterpart.
> Thus the human resource cost of entering the source is less for PL/I.
> .
…[3 more quoted lines elided]…
> 	(2) the COBOL source is column sensitive: errors waste time for
nothing;
> 	(3) COBOL has some 300 reserved words: inadvertant use of a
keyword as
> 	    a variable name wastes time. (PL/I has no reserved words.)
> .
…[4 more quoted lines elided]…
> 	* error trapping and display of variables, at the point where
the
> 	  error occurs.
> 	* precise location of the statement in error;
> 	* enabling fixed-point and floating-point checks for
overflow/underflow
> 	  for any part of or the whole program.
> 	* enabling checks for subscript violations for any part of or
the whole
> 	  program;
> 	* enabling checks for substring violations for any part of or
the whole
> 	  program;
> 	* trapping of computational errors, subscript errors, and
substring
> 	  errors.
> PL/I is largely machine-independent.
> Optimization can be confined to specific regions of program,
maintaining
> statement order.
> Specific sections of the program or the whole program can be highly
optimized.
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
