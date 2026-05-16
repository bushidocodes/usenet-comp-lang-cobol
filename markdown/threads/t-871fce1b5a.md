[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# UNISYS: assembler translation assistance

_12 messages · 6 participants · 1998-09_

---

### UNISYS: assembler translation assistance

- **From:** sff5ky@aol.com (Sff5ky)
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980923005600.UAA11369@ladder01.news.aol.com>`

```
I am attempting to convert some old COBOL68 programs with inline ASSEMBLER code
to fit ANSI85.  Would also like to find assistance for mapping PIC 9 COMP
fields to an equivalent ANSI85 data type and what does 'INTRINSIC TRANSLATE'
using source-field, trans-table, giving result-field
. 
.
    ENTER SYMBOLIC.
       MVN 1 NCRVAR:1:+100
       MVN 0000  NCRVAR:4:+200
    ENTER COBOL.
       READ NCRVAR
.
.
        ADD 1 TO NCR-REC-NO.
 012-NCR-COPY.
     ENTER SYMBOLIC.
        BOT 01 80 NCRVAR:+200
        NEQ 012-NCR-COPY
        SUB NCRVAR:6:+210 NCRVAR:6:+234 NCR-REC-SIZE.
     ENTER COBOL.
        MOVE SPACES TO NCR-STARCOM-PRINT.
.
.
     IF NCR-RECD-LNGTH NOT > ZERO
         MOVE 1 TO END-TRLR-FLAG
         GO TO 030-EXIT.
     ENTER SYMBOLIC.
       MVN TRLR-ADDR IX1.
       INC TRLR-ADDR IX1.
       MVALUE NCR-TRLR-AREA:DSP:IX1:2 TRLR-LNGTH-X.
     ENTER COBOL.
     MOVE TRLR-LNGTH TO WORK-4.
.
.
     MOVE DEC-VALUE TO TRLR-LNGTH
                       CNT-LNGTH.
     ENTER SYMBOLIC.
       MVN TRLR-ADDR IX1.
       INC TRLR-ADDR IX1.
       MVN 0         IX2.
 030-MV-LOOP.
       MVALUE NCR-TRLR-AREA:DSP:IX1:00 NCR-STARCOM-SVTRLR:DSP:IX2:
       INC 200 IX1.
       INC 200 IX2.
       DEC 100 CNT-LNGTH.
       GTR 030-MV-LOOP.
     ENTER COBOL.
     SUBTRACT TRLR-LNGTH FROM NCR-RECD-LNGTH.
     ADD TRLR-LNGTH TO TRLR-ADDR.
.
.
     MOVE ZERO TO NA-TRLR-LNGTH.
     ENTER SYMBOLIC.
       MVN NA-TRLR-ADDR IX1.
       INC NA-TRLR-ADDR IX1.
       MVALUE NCR-NA-SUB-TRLRS:DSP:IX1:1 NA-TRLR-LNGTH-X:DSP:+1:1.
     ENTER COBOL.
     MOVE NA-TRLR-LNGTH TO WORK-4.
.
.
     MOVE DEC-VALUE TO NA-TRLR-LNGTH
                       CNT-LNGTH.
     ENTER SYMBOLIC.
       MVN NA-TRLR-ADDR IX1.
       INC NA-TRLR-ADDR IX1.
       MVN 0            IX2.
*
 056-MV-LOOP.
       MVALUE NCR-NA-SUB-TRLRS:DSP:IX1:00
           NCR-NA-SUB-TRLR:DSP:IX2:00.
       INC 200 IX1.
       INC 200 IX2.
       DEC 100 CNT-LNGTH.
       GTR 056-MV-LOOP.
     ENTER COBOL.
     SUBTRACT NA-TRLR-LNGTH FROM TRLR-LNGTH.
     ADD NA-TRLR-LNGTH TO NA-TRLR-ADDR.
.
.
     MOVE NCR-NAME-LINE(SUB1) TO WORK-BYTES.
     ENTER SYMBOLIC.
       TRN 35 WORK-BYTES ASC-TO-EBC WORK-BYTES.
     ENTER COBOL.
     IF WORK-BYTES NOT = SPACES
```

#### ↳ Re: UNISYS: assembler translation assistance

- **From:** "grant mc" <grantmc@voyager.co.nz>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ua7fi$j47$2@reader1.reader.news.ozemail.net>`
- **References:** `<19980923005600.UAA11369@ladder01.news.aol.com>`

```
Can you provide a little information. Specifically what model machine is
this code from? The A-Series system since 1984 hasn't offered an assembler
and from the look of the code you've provided it looks more like some old
intrinsic functions from a software product, probably from a B-Series
machine. I've got a heap of very old manuals so might be able to help you.

PIC 9 COMP are simply hex code without the F character and are stored in a
half byte. You can store them like this because we know the item is a
number. COMP items can be held together and thus don't waste any space.
Where as if we declare items mixed between display and comp then half bytes
are lost.

Grant Mc
Sff5ky wrote in message <19980923005600.UAA11369@ladder01.news.aol.com>...
>I am attempting to convert some old COBOL68 programs with inline ASSEMBLER
code
>to fit ANSI85.  Would also like to find assistance for mapping PIC 9 COMP
>fields to an equivalent ANSI85 data type and what does 'INTRINSIC
TRANSLATE'
>using source-field, trans-table, giving result-field
>.
…[79 more quoted lines elided]…
>
```

#### ↳ Re: UNISYS: assembler translation assistance

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wb5O1.327$R_4.752508@news3.mia.bellsouth.net>`
- **References:** `<19980923005600.UAA11369@ladder01.news.aol.com>`

```
What you see below appears to be from the Unisys V Series (the old Burroughs
Medium Systems).  I have written a lot of Medium Systems assembly, and a fair
amount of ENTER SYMBOLIC code, though it's been a while.  I still have a copy
of the Medium Systems Assembler Reference, but I no longer have the COBOL 68
manual, and I don't recall the construct 'MVALUE'.  But I will try to give you
a bit of help.  Note that this system addresses digits (half bytes), so the
index register values will be twice the number of bytes.  Lengths and offsets
will be in bytes for DISPLAY fields and digits for COMP fields.
```

##### ↳ ↳ Re: UNISYS: assembler translation assistance

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CJbO1.1211$_G3.985767@news2.mia.bellsouth.net>`
- **References:** `<19980923005600.UAA11369@ladder01.news.aol.com> <Wb5O1.327$R_4.752508@news3.mia.bellsouth.net>`

```
Judson McClendon wrote:
>Sff5ky wrote:
>>
…[4 more quoted lines elided]…
>equivalent to COBOL 85: MOVE 1 TO NCRVAR(51:1).

Sorry, that offset could be in bytes or digits, depending on NCRVAR
being display or comp.  If NCRVAR is display, read this:

MoVe Numeric 1 to field NCRVAR:length 1:offset +100 (+100 bytes)
equivalent to COBOL 85: MOVE 1 TO NCRVAR(101:1).
```

###### ↳ ↳ ↳ Re: UNISYS: assembler translation assistance

- **From:** sff5ky@aol.com (Sff5ky)
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980923223636.00295.00000216@ngol05.aol.com>`
- **References:** `<CJbO1.1211$_G3.985767@news2.mia.bellsouth.net>`

```

In article <CJbO1.1211$_G3.985767@news2.mia.bellsouth.net>, "Judson McClendon"
<judmc123@bellsouth.net> writes:

>
>Sorry, that offset could be in bytes or digits, depending on NCRVAR
…[4 more quoted lines elided]…
>

I'm a bit confused as NCRVAR is the FILE rather than a field

 FILE-CONTROL.
     SELECT NCRVAR               ASSIGN TO TAPE-PE
                                 NO TRANSLATION.
*
 FILE SECTION.
 FD  NCRVAR.
*
 01  NCR-STARCOM-REC-LITTLE         PIC X(3000).
*
 01  NCR-STARCOM-REC-BIG            PIC X(30000).
*
 01  NCR-INPUT-DATA.
     03  FILLER                     PIC X(3).
     03  NCR-REC-ID                 PIC 9(16)   COMP.
     03  FILLER                     PIC X(2989).


Hope that this helps in explaining what the assembler code is doing.
```

###### ↳ ↳ ↳ Re: UNISYS: assembler translation assistance

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8KrO1.1536$OX1.1532639@news4.mia.bellsouth.net>`
- **References:** `<CJbO1.1211$_G3.985767@news2.mia.bellsouth.net> <19980923223636.00295.00000216@ngol05.aol.com>`

```
Sff5ky wrote:
>
>Judson McClendon writes:
…[26 more quoted lines elided]…
>Hope that this helps in explaining what the assembler code is doing.

Wow, that is Not Good.  A reference to the file name itself refers to
the FIB (File Information Block), constructed by the compiler in the
executable, and maintained by the MCP and compiler generated code
during file I/O.  One good thing is it tells us the reference is COMP,
so the offsets and lengths are in digits.  I have done a lot of 'FIB
fiddling', and used to know the FIB like the back of my hand.  But it
has been so long (>20 years), I don't remember the details.  The COBOL
68 compiler generated code to do record blocking/de-blocking, which
increased the speed of blocked sequential files significantly.  I once
disassembled the code and used a similar technique in a file conversion
utility program.

I pretty much ignored the COBOL code before, but looking at the code
now, it appears that the BOT in 012-NCR-COPY is checking something
like if the next record is in the buffer.  That's a guess, of course,
and I don't know why the test would be done after the READ.  The SUB
following possibly computes the physical block size from the read.
Sorry, but that's the best I can do without a FIB layout.
```

###### ↳ ↳ ↳ Re: UNISYS: assembler translation assistance

_(reply depth: 5)_

- **From:** "DENDEN" <DENDEN@prodigy.net>
- **Date:** 1998-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bde88c$b808eca0$LocalHost@denny-s-pc>`
- **References:** `<CJbO1.1211$_G3.985767@news2.mia.bellsouth.net> <19980923223636.00295.00000216@ngol05.aol.com> <8KrO1.1536$OX1.1532639@news4.mia.bellsouth.net>`

```
If it would be of any help, I have an old Burroughs yellowed parchment
named "The Truth About FIBS". This is from my B-2500 days and I didn't do
much Assembler programming then. According to this, a "1" at FIB position
100 indicates a "read forward". As I recall, some of these tricks were used
to handle "off-brand" tapes, such as IBM and NCR :). And this particular
file smells of variable length, to boot.  This type of code was used to
handle record marks, record lengths, etc. I'm wondering if the input file
could be dumped and checked for such things. If it is in fact such a file,
it might be better to forget about the Assembler code entirely, and come up
with a COBOL routine that redefines the buffer area into the possible
record sizes. I.E., 3000, 6000, 9000, etc. up to 30,000. The Unisys DMPALL
can help in determining what's what. Ain't this stuff fun nowadays? <G>.

Denny
```

###### ↳ ↳ ↳ Re: UNISYS: assembler translation assistance

_(reply depth: 6)_

- **From:** sff5ky@aol.com (Sff5ky)
- **Date:** 1998-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980925165625.00294.00000408@ngol05.aol.com>`
- **References:** `<01bde88c$b808eca0$LocalHost@denny-s-pc>`

```

In article <01bde88c$b808eca0$LocalHost@denny-s-pc>, "DENDEN"
<DENDEN@prodigy.net> writes:

>f it would be of any help, I have an old Burroughs yellowed parchment
>named "The Truth About FIBS". This is from my B-2500 days and I didn't do
…[10 more quoted lines elided]…
>


I am reasonably certain that you are correct in your assumptions.  I know that
the  filein question was an NCR extract and I suspect that the file was of
variable length records.  Unfortunately, I am no longer in a UNISYS site and I
am merely attempting to migrate the code into the current compiler without
benefit of a test file for validation.

If all this assembler stuff was for dealing with Variable length records, why
couldn't the program have been developed with standard COBOL syntax to begin
with?  (Pardon my ignorance  here,  just asking dumb questions.)

Thanks for any assistance you can provide.
```

###### ↳ ↳ ↳ Re: UNISYS: assembler translation assistance

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tq4P1.3302$R_4.3034890@news3.mia.bellsouth.net>`
- **References:** `<01bde88c$b808eca0$LocalHost@denny-s-pc> <19980925165625.00294.00000408@ngol05.aol.com>`

```
Sff5ky wrote:
>
>If all this assembler stuff was for dealing with Variable length records, why
>couldn't the program have been developed with standard COBOL syntax to begin
>with?  (Pardon my ignorance  here,  just asking dumb questions.)

The problem comes when you have a tape from another system which is formatted
in a way that your operating system and HLL compiler won't handle properly.
Sometimes there are even hardware considerations.  For example, the Burroughs
Medium Systems tape hardware could not write an odd number of bytes to a block,
and the operating system could not handle odd byte record lengths.  There was
a good efficiency reason for this, but it made reading an odd record length a
problem.  Sometimes you could handle it in COBOL, sometimes you needed assembly.
I used to do a fair amount of media conversion, and sometimes using assembly is
the only, or perhaps the quickest or most efficient, way to get things done.
On the other hand, sometimes programmers just want to bit-fiddle a little. :-)
There may be good reasons why ENTER SYMBOLIC was used here, but perhaps not.
You would have had to been there at the time to know for sure, I suspect.
```

###### ↳ ↳ ↳ Re: UNISYS: assembler translation assistance

_(reply depth: 7)_

- **From:** "DENNIS A BROUSE" <DENDEN@prodigy.net>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6unrlk$212e$1@newssvr04-int.news.prodigy.com>`
- **References:** `<01bde88c$b808eca0$LocalHost@denny-s-pc> <19980925165625.00294.00000408@ngol05.aol.com>`

```
Judson hit the nail on the head with his reply to your question on "Why use
assembler?".  For whatever reason, old  Burroughs systems did not handle odd
length records, for example 133 character print lines. But with print lines
it didn't matter much.  You could fgure it out from the report.  With media
conversion, one way was to use assembler calls.  But since your FD shows
3000 to 30000 characters, that may or may not be the situation here.  If the
site cannot provide you with a dump of the tape, it's going to be real tough
to figure it out for sure. If the old program is still running, they could
also dump the program while it is executing, and you might be able to use
that. Good luck!

Denny
```

###### ↳ ↳ ↳ Re: UNISYS: assembler translation assistance

_(reply depth: 8)_

- **From:** Rodger Whitlock <totototo+newsgroups@mail.pacificcoast.net>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NwUlch5n1GzV@vmsmail.gov.bc.ca>`
- **References:** `<01bde88c$b808eca0$LocalHost@denny-s-pc> <19980925165625.00294.00000408@ngol05.aol.com> <6unrlk$212e$1@newssvr04-int.news.prodigy.com>`

```
It strikes me that if you look at the program that now creates the 
tape being read with the assistance of Assembler, you will discover 
that it goes to enormous lengths to accurately mimic an archaic NCR 
format. You should look at, and repair/upgrade/simplify, both the 
writing and reading programs, if possible. You might be lucky and 
find that they are both running (or going to run) on the same 
platform.
```

##### ↳ ↳ Re: UNISYS: assembler translation assistance

- **From:** trblshtr@my-dejanews.com
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uc7le$p00$1@nnrp1.dejanews.com>`
- **References:** `<19980923005600.UAA11369@ladder01.news.aol.com> <Wb5O1.327$R_4.752508@news3.mia.bellsouth.net>`

```
In article <Wb5O1.327$R_4.752508@news3.mia.bellsouth.net>,
  "Judson McClendon" <judmc123@bellsouth.net> wrote:
> What you see below appears to be from the Unisys V Series (the old Burroughs
> Medium Systems).  I have written a lot of Medium Systems assembly, and a fair
> amount of ENTER SYMBOLIC code, though it's been a while.  I still have a copy
> of the Medium Systems Assembler Reference, but I no longer have the COBOL 68
> manual, and I don't recall the construct 'MVALUE'.  But I will try to give you

Boy, that goes way back.  You are correct, i think, regarding the Burroughs
systems.  If i recall correctly (which is becoming more and more questionable
as I get older) the 'mvalue' served to convert from binary in the symbolic
world to bcd in the cobol??  Wonder if I still have the old manuals up in
the attic somewhere.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
