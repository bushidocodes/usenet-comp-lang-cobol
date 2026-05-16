[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol convert program Job Request

_21 messages · 7 participants · 2007-02_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Migration and conversion`](../topics.md#migration)

---

### Cobol convert program Job Request

- **From:** jacodeguy@gmail.com
- **Date:** 2007-02-21T09:40:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com>`

```
Hi everyone.

I have a cobol file (from microfocus) (.mst and .idx about 6 meg
uncompressed).  and the header:

      $SET REMOVE(LENGTH) NOTRUNC
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

       SELECT NOT OPTIONAL IL-BLDG-SKETCH
          ASSIGN "B-SKETCH.MST"
          ORGANIZATION INDEXED
          ACCESS MODE DYNAMIC
          LOCK MODE MANUAL
          RECORD KEY TABLE-NAME OF SKETCH-RECORD
          FILE STATUS SKETCH-STATUS.

       FILE SECTION.

	   FD IL-BLDG-SKETCH.
	   01 PT-REC.
	   	03 PT-KEY.
	    	05 PT-PROP-NO  PIC X(20).
	     	05 PT-SEQ      PIC X.
	   	03 PT-GRAPHICS.
	    	05 PT-TABLE OCCURS 200 TIMES.
	       		07 PT-X      PIC S9(4) COMP.
	       		07 PT-Y      PIC S9(4) COMP.
	   	03 PT-END        PIC S9(4) COMP.
	   	03 PT-SCALE      PIC 9V9(4) COMP.


I am not a cobol programmer, so I'd like to hire someone to convert
this file to CSV for me.  I'd like the source and be able to run it
myself, if possible.  I do not own microfocus cobol, so I am wondering
if there is a free alternative (I have both windows and linux boxes
available).  I'm hoping tiny/open/free/gnu Cobol will be able to read
microfocus files.

This is a one time data conversion, but we might get a "newer" file
right before the official convert, so I might have to run this more
than once.

Please email me directly at andy at camavision.com (or this newgroup,
I'll try to watch it for a while), if you are interested.

Please include a price quote (I'm thinking in the $100 range).

Thanks,

-Andy
```

#### ↳ Re: Cobol convert program Job Request

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-02-21T16:07:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172102866.572823.270760@a75g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com>`

```
On Feb 22, 6:40 am, jacode...@gmail.com wrote:
> Hi everyone.
>
…[34 more quoted lines elided]…
> microfocus files.

Microfocus Cobol can write several different formats of INDEXED
files.  If the file is 'Level II' format then it may be readable as a
sequential file by many systems as it will be fixed records in the
data file.  If the file is C2 or other then this may be more difficult
to get another system to read it.

> This is a one time data conversion, but we might get a "newer" file
> right before the official convert, so I might have to run this more
…[7 more quoted lines elided]…
> Thanks,

It seems to me that PT-END may indicate the number of PT-TABLE used
and thus should be in the range 1 - 200.  Or perhaps to the next
available 2-201.
```

##### ↳ ↳ Re: Cobol convert program Job Request

- **From:** jacodeguy@gmail.com
- **Date:** 2007-02-21T18:44:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172112252.693984.161400@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1172102866.572823.270760@a75g2000cwd.googlegroups.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com>`

```

> > available).  I'm hoping tiny/open/free/gnu Cobol will be able to read
> > microfocus files.
…[5 more quoted lines elided]…
> to get another system to read it.

I got this from the rebuild program:

b-sketch.mst /i
Rebuild successful - records read =      7396

File : B-SKETCH.MST
  Record length -       826
  Organization - Indexed
  Recording mode - Fixed
  Record length -   826
  Keys description :
  Key           Start             Length
    0:              1                +21

Does that help?  It says fixed "recording length", I'm hoping thats a
fixed length record of 826 bytes.  And.. hopefully.. a Level II file
that will be useable.

>
> It seems to me that PT-END may indicate the number of PT-TABLE used
> and thus should be in the range 1 - 200.  Or perhaps to the next
> available 2-201.

I have other documentation about what the different fields mean.  If I
can get the data into csv I can use it from there.

What would be an easy way to test this.  I can zip up the files and
put them some place if anyone wanted to write a test program to see if
they can be read.  Or, with a little help, I'd be happy to install
tiny/open cobol and try something myself.  (Or whatever cobol you
prefer... I know nothing :-) )

Thanks for your time,

-Andy
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-02-21T19:48:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172116081.373824.74200@a75g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<1172112252.693984.161400@q2g2000cwa.googlegroups.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com>`

```
On Feb 22, 3:44 pm, jacode...@gmail.com wrote:
> > > available).  I'm hoping tiny/open/free/gnu Cobol will be able to read
> > > microfocus files.
…[23 more quoted lines elided]…
> that will be useable.

A hexdump of the first couple of Kb would show the format. What OS is
this on, what version of Microfocus ?


> > It seems to me that PT-END may indicate the number of PT-TABLE used
> > and thus should be in the range 1 - 200.  Or perhaps to the next
…[9 more quoted lines elided]…
> prefer... I know nothing :-) )

Did you want each CSV record to have 200 X and Y fields, less
depending on PT-END or one line per X/Y pair ?
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 4)_

- **From:** jacodeguy@gmail.com
- **Date:** 2007-02-22T07:06:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172156802.650230.278850@s48g2000cws.googlegroups.com>`
- **In-Reply-To:** `<1172116081.373824.74200@a75g2000cwd.googlegroups.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com>`

```
On Feb 21, 9:48 pm, "Richard" <rip...@Azonic.co.nz> wrote:
> On Feb 22, 3:44 pm, jacode...@gmail.com wrote:
>
…[46 more quoted lines elided]…
> depending on PT-END or one line per X/Y pair ?

The program was written for windows/dos, I'm not sure of the version.
from the rebuild util I get this header:
XM V1.4.6 - The Micro Focus DOS Extender Copyright (c) 1987-1996 Micro
Focus Ltd
URN AXCPA/000000000    [Protocol:
DPMI]                                  Ref 022
Micro Focus COBOL File Management Utility
Version 3.4.23 Copyright (C) 1985-1996 Micro Focus Ltd.

So does 3.4.23 sound right?  I can run on windows or linux (I'd prefer
linux) however.

I'd like one record to be one line of text.  (all 200 pairs on one
line).  And just dump them all.

Here is a hex dump.  I hope the wrapping doesnt kill it

==========================================================================
0000: 30 7E 00 00 00 00 00 00   30 31 31 30 31 38 31 34 | 0~......
01101814
0010: 30 30 31 36 31 36 30 31   31 30 31 38 31 34 30 30 |
0016160110181400
0020: 31 36 31 36 00 3E 00 02   00 00 00 00 00 00 00 00 |
1616.>..........
0030: 01 00 00 00 00 00 00 00   03 3A 00 00 03 3A 00 00
| .........:...:..
0040: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0050: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0060: 00 00 00 00 00 00 00 00   00 00 00 00 41 00 20 2E
| ............A. .
0070: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0080: 43 3A 30 31 2D 30 30 30   2D 30 30 31 2D 30 30 20 | C:
01-000-001-00
0090: 20 20 20 20 20 20 41 FF   D8 00 10 00 01 00 09 00 |
A.Ø.......
00A0: 21 00 0D 00 21 00 35 00   37 00 35 00 37 00 25 FF | !...!.
5.7.5.7.%.
00B0: CD 00 25 00 33 00 0D 00   21 00 0D FF FC 00 06 FF | Í.%.
3...!...ü...
00C0: D8 00 0E 00 02 00 07 00   21 00 19 00 0F 00 19 00 |
Ø.......!.......
00D0: 0F 00 25 FF DF 00 25 FF   DF 00 19 00 02 00 02 FF | ..%.ß.
%.ß.......
00E0: D8 00 09 00 04 00 07 00   21 00 0D 00 15 00 0D 00 |
Ø.......!.......
00F0: 15 00 19 FF DF 00 19 FF   DF 00 0D 00 03 00 03 FF
| ....ß...ß.......
0100: D8 00 09 00 05 00 07 00   33 00 0D 00 3F 00 0D 00 | Ø.......
3...?...
0110: 3F 00 25 FF CD 00 25 FF   CD 00 0D FF D8 00 09 00 | ?.%.Í.
%.Í...Ø...
0120: 06 00 07 00 21 00 35 FF   DF 00 3B 00 39 00 3B 00 | ....!.5.ß.;.
9.;.
0130: 39 00 35 FF DF 00 35 FF   F8 00 00 FF D8 00 0E 00 | 9.5.ß.
5.ø...Ø...
0140: 07 00 07 00 37 00 25 00   39 00 25 FF C7 00 35 FF | ....7.%.
9.%.Ç.5.
0150: C9 00 35 FF C9 00 25 00   04 00 00 FF D8 00 05 00 | ..
5...%.....Ø...
0160: 0B 00 07 00 21 00 25 00   09 00 25 00 09 00 3B FF | ....!.%...
%...;.
0170: DF 00 3B FF DF 00 25 00   00 00 00 00 00 00 00 00 | ß.;.ß.
%.........
0180: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0190: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
01A0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
01B0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
01C0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
01D0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
01E0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
01F0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0200: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0210: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0220: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0230: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0240: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0250: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0260: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0270: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0280: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0290: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
02A0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
02B0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
02C0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
02D0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
02E0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
02F0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0300: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0310: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0320: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0330: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0340: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0350: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0360: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0370: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0380: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0390: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
03A0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
03B0: 00 00 00 00 00 00 00 00   38 00 4E 20 43 3A 30 31 | ........8.N
C:01
03C0: 2D 30 30 30 2D 30 30 36   2D 30 30 20 20 20 20 20 |
-000-006-00
03D0: 20 20 41 FF D8 00 10 00   01 00 0B 00 0D 00 21 00 |
A.Ø.........!.
03E0: 0D 00 31 00 1F 00 31 00   1F 00 35 00 2F 00 35 00 | ..
1...1...5./.5.
03F0: 2F 00 1B 00 17 00 1B 00   17 00 21 00 0D 00 21 00
| /.........!...!.
0400: 00 FF FE FF D8 00 0E 00   02 00 07 00 1F 00 1B FF
| ....Ø...........
0410: CF 00 1B 00 31 00 09 00   1F 00 09 FF E1 00 1B 00 | ....
1...........
0420: 00 00 03 FF D8 00 0E 00   04 00 07 00 1F 00 35 00
| ....Ø.........5.
0430: 1F 00 47 00 35 00 47 FF   CB 00 35 FF E1 00 35 00 | ..G.5.G.Ë.
5...5.
0440: 04 FF FE FF D8 00 09 00   06 00 07 00 1F 00 31 FF
| ....Ø.........1.
0450: E1 00 36 00 0D 00 36 00   0D 00 31 FF E1 00 31 00 | ..
6...6...1...1.
0460: 00 FF FF FF D8 00 02 00   07 00 0B 00 1F 00 15 00
| ....Ø...........
0470: 1F 00 1B FF E9 00 1B FF   E9 00 21 FF F3 00 21 FF
| ..........!.ó.!.
0480: F3 00 15 FF EC 00 12 FF   E7 00 15 FF E1 00 15 FF |
ó...ì...ç.......
0490: FE FF FE 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
04A0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
04B0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
04C0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
04D0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
04E0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
04F0: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0500: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0510: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0520: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0530: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0540: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0550: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0560: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................
0570: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
| ................


Thanks much

-Andy
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 5)_

- **From:** jacodeguy@gmail.com
- **Date:** 2007-02-22T07:12:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172157144.642604.107070@v33g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<1172156802.650230.278850@s48g2000cws.googlegroups.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com>`

```
Ok... that looks crappy...  try this link instead:

http://camavision.com/dn/bsketchdump.txt

-Andy
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 6)_

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-02-22T11:29:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12tro992hdae6b8@corp.supernews.com>`
- **In-Reply-To:** `<1172157144.642604.107070@v33g2000cwv.googlegroups.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com>`

```
jacodeguy@gmail.com wrote:
> Ok... that looks crappy...  try this link instead:
> 
> http://camavision.com/dn/bsketchdump.txt

It looks like there's a 128-byte header followed by the records.  Each 
826-byte record is preceded by a 2-byte prefix ("C:").  The first 21 
bytes of each record do in fact look like an alpha key.

The rest of the record doesn't seem to match the layout.  For one thing, 
it's too short;  200 repetitions of pairs of S9(4) COMP should take 1200 
bytes.  And I don't think the all of the data looks like signed packed 
decimal.

Any idea what the sending system thinks is in the first few records?

Louis
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-02-22T13:54:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12trpnnipu134f5@corp.supernews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com>`

```

"Louis Krupp" <lkrupp@pssw.nospam.com.invalid> wrote in message
news:12tro992hdae6b8@corp.supernews.com...
> jacodeguy@gmail.com wrote:
> > Ok... that looks crappy...  try this link instead:
…[3 more quoted lines elided]…
> It looks like there's a 128-byte header followed by the records.

Typical of Mirco Focus Indexed Files and Variable
Lengrh Files.

>  Each
> 826-byte record is preceded by a 2-byte prefix ("C:").

This a record descriptor which consists of a 4-bit type
followed by the 12-bit record length. (x"433A" means,
type "4" record with length 826 bytes.)

>  The first 21
> bytes of each record do in fact look like an alpha key.
…[4 more quoted lines elided]…
> decimal.

The record matches the layout perfectly!
Micro Focus S9(4) COMP is two bytes binary
and 9V9(4) COMP is three bytes binary.
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 8)_

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-02-22T12:51:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12trt1a54h7u12b@corp.supernews.com>`
- **In-Reply-To:** `<12trpnnipu134f5@corp.supernews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com>`

```
Rick Smith wrote:
> "Louis Krupp" <lkrupp@pssw.nospam.com.invalid> wrote in message
> news:12tro992hdae6b8@corp.supernews.com...
…[29 more quoted lines elided]…
> 

How do you fit a sign and four digits into two bytes?  (Or am I being 
unusually dense today?)

Louis
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-02-22T13:04:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dntrt2h55hn1slcseq3e52jsgh0i71bhuq@4ax.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com>`

```
On Thu, 22 Feb 2007 12:51:05 -0700, Louis Krupp
<lkrupp@pssw.nospam.com.invalid> wrote:

>> The record matches the layout perfectly!
>> Micro Focus S9(4) COMP is two bytes binary
…[6 more quoted lines elided]…
>unusually dense today?)

A byte holds 16 bits - 15 plus the sign.  +9999d = 10011100001111b
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 10)_

- **From:** Louis Krupp <lkrupp@pssw.nospam.com.invalid>
- **Date:** 2007-02-23T06:35:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ttrcun99qn608@corp.supernews.com>`
- **In-Reply-To:** `<dntrt2h55hn1slcseq3e52jsgh0i71bhuq@4ax.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <dntrt2h55hn1slcseq3e52jsgh0i71bhuq@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 22 Feb 2007 12:51:05 -0700, Louis Krupp
> <lkrupp@pssw.nospam.com.invalid> wrote:
…[11 more quoted lines elided]…
> 

So I *was* dense.  I was thinking "packed decimal" for no really good 
reason...

Louis
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 9)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-02-22T12:06:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172174815.695241.198480@l53g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<12trt1a54h7u12b@corp.supernews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com>`

```
On Feb 23, 8:51 am, Louis Krupp <lkr...@pssw.nospam.com.invalid>
wrote:


> > The record matches the layout perfectly!
> > Micro Focus S9(4) COMP is two bytes binary
…[3 more quoted lines elided]…
> unusually dense today?)

In binary (as stated). The value in 16 bit can be -32368 to 32367
which is a larger range than -9999 to 9999.

COMP (in this case) however is byte reversed compared to intel format
being big-endian.
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-02-22T15:35:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12trvl1q5rqfp29@corp.supernews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <1172174815.695241.198480@l53g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:1172174815.695241.198480@l53g2000cwa.googlegroups.com...
[snip]
> In binary (as stated). The value in 16 bit can be -32368 to 32367
> which is a larger range than -9999 to 9999.

Pedantically, the range is -32768 to +32767, which
is the range that applies when the NOTRUNC
compiler directive is used, as is true in the case
of the record layout in question. [Important for any
who may wish to write the requested program.]
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-02-22T20:57:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<btnDh.224493$Dx5.69429@fe10.news.easynews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <1172174815.695241.198480@l53g2000cwa.googlegroups.com> <12trvl1q5rqfp29@corp.supernews.com>`

```
Also important that the NOIBMCOMP directive is in effect.  This is important for 
why you can have 3 (or 1) byte binary fields.
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 10)_

- **From:** jacodeguy@gmail.com
- **Date:** 2007-02-22T13:00:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172178058.861073.181220@q2g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1172174815.695241.198480@l53g2000cwa.googlegroups.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <1172174815.695241.198480@l53g2000cwa.googlegroups.com>`

```
On Feb 22, 2:06 pm, "Richard" <rip...@Azonic.co.nz> wrote:
> On Feb 23, 8:51 am, Louis Krupp <lkr...@pssw.nospam.com.invalid>
> wrote:
…[12 more quoted lines elided]…
> being big-endian.

I have some printouts of what the sketch should look like, I cannot
find the first record (pin 01-000-001-00), but I do have the second
(pin 01-000-006-00).  Based on looking at the printout, I think the
first part should be like this:

01-000-006-00, A, -40, 16, 1, 11, 13, 33, 13, 49, 31, 49, 31, 53, 47,
53, 47, 27, 23, 27, 23, 33, 13, 33, 0, -2,

C I can do, and would love too, but a little rusty.  The bytes and
strings I think I can get out, but I'm not sure about the S9(4) COMP
(two bytes reversed) thing.

if I have:

byte *buffer;
fread(buffer, 2, f);
// lets pretened I just read a comp, you previously said:
// "Just byte switch the COMP fields."
// How would I do that?
int x = (buffer[1] << 16) && buffer[0];  // something like this?

-Andy
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-02-22T16:34:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ts32qvk9jtc7@corp.supernews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <1172174815.695241.198480@l53g2000cwa.googlegroups.com> <1172178058.861073.181220@q2g2000cwa.googlegroups.com>`

```

<jacodeguy@gmail.com> wrote in message
news:1172178058.861073.181220@q2g2000cwa.googlegroups.com...
> On Feb 22, 2:06 pm, "Richard" <rip...@Azonic.co.nz> wrote:
> > On Feb 23, 8:51 am, Louis Krupp <lkr...@pssw.nospam.com.invalid>
…[34 more quoted lines elided]…
> int x = (buffer[1] << 16) && buffer[0];  // something like this?

Just the reverse and a bit different.

int x = (buffer[0] << 8) && buffer[1];

I did it a bit differently. [Using C++, as a better C.]
See Get_PT_TwoByteComp, below.

-----
#include <stdio.h>

struct TwoByteComp {
 unsigned char c[2];
};

struct ThreeByteComp {
 unsigned char c[3];
};

struct {
 unsigned char RecordDescriptor[2];
 struct {
  char PT_PROP_NO[20]; // not nul terminated
  char PT_SEQ;
 } PT_KEY;
 struct {
  struct {
   TwoByteComp PT_X; // big-endian
   TwoByteComp PT_Y; // big-endian
  } PT_TABLE[200];
 } PT_GRAPHICS;
 TwoByteComp PT_END; // big endian
 ThreeByteComp PT_SCALE; // big-endian
} PT_REC;

signed short Get_PT_TwoByteComp (TwoByteComp *comp) {
 return (signed short) (comp->c[0]*256+comp->c);
}

double Get_PT_SCALE (ThreeByteComp *comp ) {
 return (double) ((comp->c[0]*65536+comp->c[1]*256
  +comp->c[2])/10000.0);
}

bool IsValidRecord (void) {
 return ((PT_REC.RecordDescriptor[0]>>4)==4);
}

void main (void) {
 printf ("%d\n", sizeof (PT_REC));
 return;
}
-----

The output is 828, which is the size of the record
with the descriptor.

This might give you some ideas.
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 12)_

- **From:** jacodeguy@gmail.com
- **Date:** 2007-02-22T14:04:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172181884.310009.214830@t69g2000cwt.googlegroups.com>`
- **In-Reply-To:** `<12ts32qvk9jtc7@corp.supernews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <1172174815.695241.198480@l53g2000cwa.googlegroups.com> <1172178058.861073.181220@q2g2000cwa.googlegroups.com> <12ts32qvk9jtc7@corp.supernews.com>`

```
On Feb 22, 3:34 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
> <jacode...@gmail.com> wrote in message
>
…[104 more quoted lines elided]…
> This might give you some ideas.

Sweet!  Yes, that seems to work.  Only little bug was this line:

> signed short Get_PT_TwoByteComp (TwoByteComp *comp) {
>  return (signed short) (comp->c[0]*256+comp->c);
> }

should be:
return (signed short) (comp->c[0]*256+comp->c[1]);  //with the [1]

Wow, I have not done it all yet, but got the pin and the first x,y.  I
think I'm golden.

Thank you all very very much.  Richard and Rick, I'd love to pay you
back.  If you'd like to split the $100 please email me at andy at
camavision.com where I can send the check.  Or if you had a wish list
online someplace just let me know.  Or, if there is anything else I
can do to return the favor.

Thanks again,

-Andy
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 13)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-02-22T17:43:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ts75raqd4bq72@corp.supernews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <1172174815.695241.198480@l53g2000cwa.googlegroups.com> <1172178058.861073.181220@q2g2000cwa.googlegroups.com> <12ts32qvk9jtc7@corp.supernews.com> <1172181884.310009.214830@t69g2000cwt.googlegroups.com>`

```

<jacodeguy@gmail.com> wrote in message
news:1172181884.310009.214830@t69g2000cwt.googlegroups.com...
> On Feb 22, 3:34 pm, "Rick Smith" <ricksm...@mfi.net> wrote:
[snip]
> Sweet!  Yes, that seems to work.  Only little bug was this line:
>
…[5 more quoted lines elided]…
> return (signed short) (comp->c[0]*256+comp->c[1]);  //with the [1]

This sometimes happens with untested C/C++ programs!
A missing subscript can't get past the syntax check in COBOL,
though.

> Wow, I have not done it all yet, but got the pin and the first x,y.  I
> think I'm golden.
…[3 more quoted lines elided]…
> camavision.com where I can send the check.

Send it all to Richard. He was willing to do it in COBOL.
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 14)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-02-23T14:01:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172268086.729813.140090@a75g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<12ts75raqd4bq72@corp.supernews.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <1172174815.695241.198480@l53g2000cwa.googlegroups.com> <1172178058.861073.181220@q2g2000cwa.googlegroups.com> <12ts32qvk9jtc7@corp.supernews.com> <1172181884.310009.214830@t69g2000cwt.googlegroups.com> <12ts75raqd4bq72@corp.supernews.com>`

```
On Feb 23, 11:43 am, "Rick Smith" <ricksm...@mfi.net> wrote:
> <jacode...@gmail.com> wrote in message

> > Thank you all very very much.  Richard and Rick, I'd love to pay you
> > back.  If you'd like to split the $100 please email me at andy at
> > camavision.com where I can send the check.
>
> Send it all to Richard. He was willing to do it in COBOL.

If you set a fire for a man he will be warm for a day, if you set him
on fire he will be warm for the rest of his life.
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-02-24T11:59:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5499urF200fb0U1@mid.individual.net>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com> <1172157144.642604.107070@v33g2000cwv.googlegroups.com> <12tro992hdae6b8@corp.supernews.com> <12trpnnipu134f5@corp.supernews.com> <12trt1a54h7u12b@corp.supernews.com> <1172174815.695241.198480@l53g2000cwa.googlegroups.com> <1172178058.861073.181220@q2g2000cwa.googlegroups.com> <12ts32qvk9jtc7@corp.supernews.com> <1172181884.310009.214830@t69g2000cwt.googlegroups.com> <12ts75raqd4bq72@corp.supernews.com> <1172268086.729813.140090@a75g2000cwd.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1172268086.729813.140090@a75g2000cwd.googlegroups.com...
> On Feb 23, 11:43 am, "Rick Smith" <ricksm...@mfi.net> wrote:
>> <jacode...@gmail.com> wrote in message
…[9 more quoted lines elided]…
>
Or at least until the Corner Office Idiot pisses all over him... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Cobol convert program Job Request

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2007-02-22T10:42:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1172169743.919579.258090@s48g2000cws.googlegroups.com>`
- **In-Reply-To:** `<1172156802.650230.278850@s48g2000cws.googlegroups.com>`
- **References:** `<1172079649.002897.77680@v33g2000cwv.googlegroups.com> <1172102866.572823.270760@a75g2000cwd.googlegroups.com> <1172112252.693984.161400@q2g2000cwa.googlegroups.com> <1172116081.373824.74200@a75g2000cwd.googlegroups.com> <1172156802.650230.278850@s48g2000cws.googlegroups.com>`

```
On Feb 23, 4:06 am, jacode...@gmail.com wrote:

> The program was written for windows/dos, I'm not sure of the version.
> from the rebuild util I get this header:
…[8 more quoted lines elided]…
> linux) however.

3.4.xx is DOS compiler. It can do Windows 3.1 and OS/2
16 bit.

The first 128 bytes is a file header. This indicates C2 format which
is the default for version 3.4. This makes it harder to deal with in
other systems.

No problem for a Microfocus program, and I could send one that does
not require a runtime licence, but I doubt that other Cobol would
access it, not free ones anyway.


==========================================================================
> 0000: 30 7E 00 00 00 00 00 00   30 31 31 30 31 38 31 34 | 0~......
> 01101814
…[3 more quoted lines elided]…
> 1616.>..........
 [snip]
> 0070: 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00
> | ................

This is a data record. Two byte record header. Prop-No of
01-000-001-00, Seq A.

The record header needs to be interpreted. The first 4 bits give
record type (0100=user record). Then 12 bit length.

> 0080: 43 3A 30 31 2D 30 30 30   2D 30 30 31 2D 30 30 20 | C:
> 01-000-001-00
…[3 more quoted lines elided]…
> 5.7.5.7.%.
  [snip]

END is 2 bytes 0038 Scale 3 bytes 004E20. Two byte header, Prop-No
01-000-006-00 Seq A.

> 03B0: 00 00 00 00 00 00 00 00   38 00 4E 20 43 3A 30 31 | ........8.N
> C:01
…[3 more quoted lines elided]…
> A.Ø.........!.

This could be relatively easy in C, at least it is fixed length and
uncompressed. Just byte switch the COMP fields.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
