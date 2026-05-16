[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with Cobol for MVS

_4 messages · 4 participants · 1999-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Problem with Cobol for MVS

- **From:** hebertgi@connectmmic.net
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3694D04B.35CC@connectmmic.net>`

```
Good Morning,

At work we are experiencing a problem with Cobol for MVS (1.2.1) under
L.E. v1 r6.0.  
The problem we are having is as follows:

Within the working storage section the variable WRP-ENT-L3-LITTERAL is
defined as below.

01   WRP-ENTETE-LIGNE3-626.
        05 PIC X(01)   VALUE SPACES.
        05 PIC X(07)   VALUE 'NO'.
        05 PIC X(21)   VALUE 'NOM'.
          .
          .
        05   WRP-ENT-L3-LITTERAL             PIC X(23)   VALUE SPACES.

Then within our procedure DIVISION we have an IF statment which moves a
word (ex.  problem) into the WRP-ENT-L3-LITTERAL variable which is then
asked to be printed.

Example:
                   IF   WRP-CIE = '01'
                          MOVE 'PROBLEM'  TO WRP-ENT-L3-LITTERAL
                   END-IF

                   WRITE DETAIL-LINE FROM WRP-ENTETE-LIGNE3-626.


Our problem is that the word (WRP-ENT-L3-LITTERAL) does not get printed
and a line of dots (ex...............) is printed instead. Trying to
figure out our problem we
have realized that the variable without using DISPLAYs was a packed
numeric
field even though it was defined as an alphanumeric field in our working
storage.

We have found that if we DISPLAY the variable anywhere in the program
the
word will be printed properly.  We have also realized that if we execute
the same program with version Cobol II but without any DISPLAYs, our
variable is printed properly without an difficulties.

Would you have an answer for our problem?  Why would the variable be
printed with the DISPLAY command with Cobol for MVS and for Cobol II we
do
not need to place any DISPLAYs within the program?

Thank You for your time and cooperation.
```

#### ↳ Re: Problem with Cobol for MVS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<772p1n$js6@dfw-ixnews8.ix.netcom.com>`
- **References:** `<3694D04B.35CC@connectmmic.net>`

```
I am not positive from your description exactly WHICH field is the field
which contains packed-decimal data - but is defined as alphanumeric.
Possibly, if you could clear this, up I could answer more accurately.
HOWEVER,  I do have one other possible "solution".  Is it possible that your
VS COBOL II compile was done with the NOOPT compiler option (no
optimization) and that your  COBOL for MVS compile was done with OPT?
"Unpacking" could be something that was optimized out of your newer compile.

In general, I think you should compare your compiler options for the two
compiles and see what is different.  This (rather than the DISPLAY
statement) *may* explain the difference.


hebertgi@connectmmic.net wrote in message <3694D04B.35CC@connectmmic.net>...
>Good Morning,
>
…[46 more quoted lines elided]…
>Thank You for your time and cooperation.
```

#### ↳ Re: Problem with Cobol for MVS

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3698928A.CDB1DDB0@zip.com.au>`
- **References:** `<3694D04B.35CC@connectmmic.net>`

```
This sounds like a memory over write a table is being addressed past
it's boundaries.   Compile with SSRANGE in the compile options to check
whether you are and if you compile TEST(PATH,SYM) it will even give you
theline number.

Good Luck
Ken

hebertgi@connectmmic.net wrote:
> 
> Good Morning,
…[4 more quoted lines elided]…
> 
..snip..
> Example:
>                    IF   WRP-CIE = '01'
…[8 more quoted lines elided]…
> have realized that the variable without using DISPLAYs was a packed
..snip..
```

#### ↳ Re: Problem with Cobol for MVS

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yj5m2.2783$hE2.17329949@storm.twcol.com>`
- **References:** `<3694D04B.35CC@connectmmic.net>`

```
What it looks like is that you may be looking at the wrong offset to
determine where the value stored in WRP-ENT-L3-LITTERAL actually is in the
written record. To verify this use Fileaid to look at the written record to
see what is actually being written. If you do not have fileaid, look at the
cross reference in the compile listing off to the left of the source code.
This may be in hexadecimal format, I haven't looked at those in a while.

From what you have written it sounds like not all of the fields are being
filled in thus everywhere in the record where there is not a value filled
in, hex'00' or low-values, is being filled in by default. Thus if you look
at the wrong place in the output record you will see '..........', but if
you DISPLAY the individual field WRP-ENT-L3-LITTERAL you will see the
correct value.

>Within the working storage section the variable WRP-ENT-L3-LITTERAL is
>defined as below.
…[8 more quoted lines elided]…
>




>Then within our procedure DIVISION we have an IF statment which moves a
>word (ex.  problem) into the WRP-ENT-L3-LITTERAL variable which is then
…[16 more quoted lines elided]…
>storage.

Once again verify proper offset from COBOL listing

>
>We have found that if we DISPLAY the variable anywhere in the program
…[3 more quoted lines elided]…
>variable is printed properly without an difficulties.

may be caused by compiler options, verify different compiles have same
compiler options. If you cant change them in the compile, use the PROCESS or
CBL statements in the source to override.

>
>Would you have an answer for our problem?  Why would the variable be
>printed with the DISPLAY command with Cobol for MVS and for Cobol II we
>do
>not need to place any DISPLAYs within the program?

Confused about this one. Are you saying when you have a DISPLAY in the
program for both compiles the record is written to the output file
correctly, or is it simply being DISPLAYED to DD SYSOUT properly?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
