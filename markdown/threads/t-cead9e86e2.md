[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I hope this is worthy... re: variable length files

_3 messages · 2 participants · 1997-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### I hope this is worthy... re: variable length files

- **From:** "raymond d. horst" <ua-author-17072853@usenetarchives.gap>
- **Date:** 1997-10-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34505d51.0@snn.softcom.net>`

```

I am currently working on a program that requires I read a fixed length
records from file one, convert the internal data and write to a fixed length
record in file two; simple enough. However, the specifications require that
al this is unknown until the program is executing and the user tells the
program what file to process.

These files may never have the same record length, but will always have
fixed record lengths. In addition, the file specification for the output
file are determined by the specifications of the input file. Thus, the
input and output can have variable lengths for the purposes of programming.

I have figured out how do everything in the specifications. By using
intrinsics to determine the statistics, once the file names are known, I can
create the output file. This all works until I attempt to write to the
output file. In debug mode, I can display the record complex; I just can't
write it to the damn output file.

The code is written in post ANSI '85 COBOLII on an HP3000 computer running
MPE 5.O [5.5?]. The error I am getting is as follows:

File status is 44
RECORD SIZE DOES NOT MATCH FD DESCRIPTION [44] WRITE (COBERR 672)

This is annoying because the record array is the same number of bytes as the
fixed length output file. The file configuration is:

FILE-CONTROL.
SELECT INPUT-FILE ASSIGN TO "INFILE".
SELECT OUTPUTFILE ASSIGN TO "OUTFILE".

DATA DIVISION.

FILE SECTION.
FD INPUT-FILE.
RECORD IS VARYING FROM 2 TO 2024.
01 INPUT-RECORD.
05 FILLER PIC X(2024).
FD OUTFILE
RECORD IS VARYING FROM 2 TO 2024
DEPENDING ON
W02-OUTPUT-LENGTH.
01 OUTFILE.
05 FILLER PIC X
OCCURS 2 TO 2024
TIMES
DEPENDING ON
W02-OUTPUT-LENGTH.

The HP manuals say the standard has changed and the output file will default
to the maximum value of the occurs, but this problem does not go away when
the maximum value is enforced.

Any takers?

Ray < rdh··.@sof··m.net >

No soliciting! My Email address in not for sale!
```

#### ↳ Re: I hope this is worthy... re: variable length files

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1997-10-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cead9e86e2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34505d51.0@snn.softcom.net>`
- **References:** `<34505d51.0@snn.softcom.net>`

```

Raymond D. Horst wrote:
› I am currently working on a program that requires I read a fixed length
› records from file one, convert the internal data and write to a fixed length
…[10 more quoted lines elided]…
›             RECORD IS VARYING     FROM 2 TO 2024
...

Does the HP system make a distinction in the external file structure
between files with fixed vs. variable record lengths? In the MVS world
this would be a distinction between RECFM=FB and RECFM=VB (where
physical blocks and records contain extra RDW & BDW control info), and a
COBOL program under MVS is only able to associate a specific FD with one
or the other, not both. Adding "VARYING" to the record definition would
force INPUT-FILE and OUTFILE to be RECFM=VB under MVS and you would not
be able to OPEN the file if the physical file referenced was RECFM=FB.
Perhaps there are other alternatives in the HP environment, but in MVS
this would be easier to solve using Assembler I/O routines rather than
COBOL I/O, or by changing the input & output files to RECFM=VB files
that just happen to have all records the same size.

Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

##### ↳ ↳ Re: I hope this is worthy... re: variable length files

- **From:** "raymond d. horst" <ua-author-17072853@usenetarchives.gap>
- **Date:** 1997-10-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cead9e86e2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cead9e86e2-p2@usenetarchives.gap>`
- **References:** `<34505d51.0@snn.softcom.net> <gap-cead9e86e2-p2@usenetarchives.gap>`

```

Thanks for your help... As it turned out [as it usually does], the problem
was of my own doing.

On the HP at the system level, a file defined in bytes is indicated by using
a negative value or when defined in words, a positive value. When in
COBOLII everything is considered in bytes with alignment to word boundaries
required in native mode [not terribly important, unless you are calling
other programs].

When I create the file, I used an intrinsic to make an external function
call to build the file. I used the same value to test and specify the
number of bytes to write to the file. I forgot, however, to drop the sign,
which completely befuddled the program. This became apparent, once I got
some sleep [I woke up realizing what I had done].

The program works and is now in production. Let the games begin...

Raymond D. Horst

Joel C. Ewing wrote in message <62t916$j.··.@bol··k.net>...
› 
› Does the HP system make a distinction in the external file structure
…[14 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
