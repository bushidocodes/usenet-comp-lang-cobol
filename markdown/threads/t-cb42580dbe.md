[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Data/print file conversion

_8 messages · 8 participants · 1997-01_

---

### Data/print file conversion

- **From:** "ph..." <ua-author-17072630@usenetarchives.gap>
- **Date:** 1997-01-06T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1997Jan7.045926.25241@RedBrick.COM>`

```

Hi folks.

I have a data extraction problem that I can't seem to figure out.

I'm writing some fairly simple COBOL programs to process data files generated
by a COBOL app and extract the data, writing it out to print files with proper
number formatting etc. for import into a data warehouse.

One file has a 50-character description field, and on about 10% of the records
there is an embedded CR or CR/LF combination in the data field. This messes up
my print lines, since the line gets split in two and the data loader chokes.

Is there any way within COBOL to check for, and remove, an embedded control
character? My source books have no info whatsoever. I could simply replace the
character at that position (seems to be a fixed point in the field) with a
blank, but then I lose the character in the other 90% of the lines.

Any ideas?

Thanks -
- Paul
```

#### ↳ Re: Data/print file conversion

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-01-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb42580dbe-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan7.045926.25241@RedBrick.COM>`
- **References:** `<1997Jan7.045926.25241@RedBrick.COM>`

```

Paul Horn wrote:
› 
› Hi folks.
…[19 more quoted lines elided]…
›  - Paul

If your COBOL compiler supports hex constants, you might try something like
this:

INSPECT DESCRIPTION REPLACING ALL X'0D' BY SPACES.
INSPECT DESCRIPTION REPLACING ALL X'0A' BY SPACES.

This assumes that I have correctly remembered the hex values for carriage
return and line feed as '0D' and '0A'.

Alternatively, you could redefine your description field as a single
dimension array of bytes, then loop through each description field changing
all undesirable characters to spaces. For ASCII or EBCDIC, you might say:

IF DESCRIPTION-BYTE (SUB1) IS LESS THAN SPACE
MOVE SPACE TO DESCRIPTION-BYTE (SUB1).

I hope this helps.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Data/print file conversion

- **From:** "lebl..." <ua-author-14800849@usenetarchives.gap>
- **Date:** 1997-01-06T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb42580dbe-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan7.045926.25241@RedBrick.COM>`
- **References:** `<1997Jan7.045926.25241@RedBrick.COM>`

```

I don't remember the hex value for a CR or a LF. Let's assume CR is
X'20', and LF is X'21'. Try the following INSPECT's to change the
CR/LF to spaces.

INSPECT DESCRIPTION-FIELD, REPLACING ALL X'20' BY SPACE
INSPECT DESCRIPTION-FIELD, REPLACING ALL X'21' BY SPACE

You could define the CR and LF constants in WORKING-STORAGE, rather
than hard coding the constants in the program.

Hope this helps.

Dilbert

ph··.@lin··e.com (Paul Horn) wrote:

› Hi folks.
› 
…[18 more quoted lines elided]…
› - Paul
```

#### ↳ Re: Data/print file conversion

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-01-07T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb42580dbe-p4@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan7.045926.25241@RedBrick.COM>`
- **References:** `<1997Jan7.045926.25241@RedBrick.COM>`

```

*Paul Horn wrote:
*>
*> Hi folks.
*>
*> I have a data extraction problem that I can't seem to figure out.
*>
*> I'm writing some fairly simple COBOL programs to process data files
*generated
*> by a COBOL app and extract the data, writing it out to print files
*with proper
* number formatting etc. for import into a data warehouse.
*>
*> One file has a 50-character description field, and on about 10% of
the *records
*> there is an embedded CR or CR/LF combination in the data field. This
*messes up
*> my print lines, since the line gets split in two and the data loader
*chokes.
*>
*> Is there any way within COBOL to check for, and remove, an embedded
*control
*> character? My source books have no info whatsoever. I could simply
*replace the
*> character at that position (seems to be a fixed point in the field)
*with a
*> blank, but then I lose the character in the other 90% of the lines.
*>
*> Any ideas?
*>
*> Thanks -
*> - Paul


The CR/LF characters are delimiters which mark the end of an ASCII
text records (generally). Most Cobol compilers (I use CA-Realia) will
incorporate this behind the scenes when a READ/WRITE statement is
issued.

This means that the CR/LF (X"0D0A") characters won't be available to
you using a typical READ statement, unless the compiler has some option
of telling it to return it. I wrote an application which would convert
mainframe-type print files to PC-print file and vice-versa. I had to
use the DOS interface calls provided by Realia to open and read the
files to get the CR/LF information. This was the only way to get the
information. While this works, it can be very tedius. You are
generally dealing with a buffer-of-information-at-a-time, which means
you have to parse out several records delimited by the CR/LF contained
within the buffer. In addition, tab control characters, X"09", if
present, may also have to be accounted for and expanded, depending on
the application.

mike dodas
```

#### ↳ Re: Data/print file conversion

- **From:** "michael zenner" <ua-author-17073272@usenetarchives.gap>
- **Date:** 1997-01-08T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb42580dbe-p5@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan7.045926.25241@RedBrick.COM>`
- **References:** `<1997Jan7.045926.25241@RedBrick.COM>`

```

Paul Horn wrote:
› 
› Hi folks.
…[19 more quoted lines elided]…
›  - Paul

All of the suggestions that you have received up to this point are good,
but if you are using MF COBOL, then check the ORGANIZATION on your
SELECT statement, and see if it's [RECORD] SEQUENTIAL or LINE
SEQUENTIAL. I don't have my manual, but one is to read a file with
carriage return linefeeds to delimit the end of record, while the other
is based in the fixed length defined in the program.

If the program is using, I believe, LINE SEQUENTIAL, then it isn't
checking for the CR/LF as record terminator... or is that RECORD
SEQUENTIAL(?).
```

##### ↳ ↳ Re: Data/print file conversion

- **From:** "bill wood" <ua-author-185550@usenetarchives.gap>
- **Date:** 1997-01-10T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb42580dbe-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cb42580dbe-p5@usenetarchives.gap>`
- **References:** `<1997Jan7.045926.25241@RedBrick.COM> <gap-cb42580dbe-p5@usenetarchives.gap>`

```

LINE SEQUENTIAL will terminate a record when it hits the CR/LF regardless
of the number of characters it has read into the record. If there is no CR
or CR/LF the record is terminated by the record size of the FD. I've had
similar problems in the past and I used a SEQUENTIAL select statement and
then parsed the record.

Michael Zenner wrote in article
<32D··.@pac··l.net>...
› Paul Horn wrote:
›› 
…[41 more quoted lines elided]…
›
```

#### ↳ Re: Data/print file conversion

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-01-11T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb42580dbe-p7@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan7.045926.25241@RedBrick.COM>`
- **References:** `<1997Jan7.045926.25241@RedBrick.COM>`

```

ph··.@lin··e.com (Paul Horn) wrote:

› Hi folks.
› 
…[18 more quoted lines elided]…
› - Paul
As I understand it, among few, that your line OUTPUT is split because
of imbedded line feeds and carriage returns in a data element picked
up from another file.

If this is the case:
1) you must be reading the file as other than LINE SEQUENTIAL and
receiving the entire data element
2) you then move this element (via matching logic?) to sepecific print
lines.

All you need do is translate the imbedded x'0A' and x'0D' to a more
preferred character, possibly space (x'20') or some other character to
later identify and correct the problem (some prefer the character '?')
When you then print the report, the line will not be split.

JR


and stir with a Runcible spoon...
```

#### ↳ Re: Data/print file conversion

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-01-12T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cb42580dbe-p8@usenetarchives.gap>`
- **In-Reply-To:** `<1997Jan7.045926.25241@RedBrick.COM>`
- **References:** `<1997Jan7.045926.25241@RedBrick.COM>`

```

In message <<199··.@Red··k.COM>> ph··.@lin··e.com writes:
› 
› Is there any way within COBOL to check for, and remove, an embedded control 
› character? My source books have no info whatsoever. I could simply replace the 
› character at that position (seems to be a fixed point in the field) with a 
› blank, but then I lose the character in the other 90% of the lines.

With ASCII all control characters have a value less than space.
Using reference notation:

PERFORM
VARYING I FROM 1 BY 1
UNTIL I > LENGTH OF Description-Filed

IF Description-Field(I:1) < SPACE
MOVE SPACE TO Description-Field(I:1)
END-IF
END-PERFORM

I am sure that you can do this more efficiently and elegently.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
