[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Copybook mapper.

_8 messages · 6 participants · 2003-08_

---

### Cobol Copybook mapper.

- **From:** "Ron Davis" <rdavis@ozemail.com.au>
- **Date:** 2003-08-18T11:17:26+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au>`

```


Hi

I'm searching for a facility which will take a COBOLcopybook and produce
storage map from it (similar to the Record Print Facility of FileAid, which
I'm ditching at my site) This will be used in conjunction for COBOL For
OS/390 at a mainframe site.

It need to handle arrays (tables) and redefines etc.  In the case of tables
it should print out a record for each table element, eg, 05 ELEMENT(3,3)
PIC XXX  and the offset from the start of the Level 1 for that structure.

Any help would be appreciated, especially by email to
ron.davis@dva.gov.au...

I'm trying to write one but it's proving a real pig!

Cheers

Ron Davis
```

#### ↳ Re: Cobol Copybook mapper.

- **From:** "Hugh Candlin" <hugh.candlin@worldnet.att.net>
- **Date:** 2003-08-18T03:06:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0pX%a.103121$3o3.7210865@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au>`

```

Ron Davis <rdavis@ozemail.com.au> wrote in message
news:TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au...
>
>
…[3 more quoted lines elided]…
> storage map from it (similar to the Record Print Facility of FileAid,
which
> I'm ditching at my site) This will be used in conjunction for COBOL For
> OS/390 at a mainframe site.
>
> It need to handle arrays (tables) and redefines etc.  In the case of
tables
> it should print out a record for each table element, eg, 05 ELEMENT(3,3)
> PIC XXX  and the offset from the start of the Level 1 for that structure.
…[4 more quoted lines elided]…
> I'm trying to write one but it's proving a real pig!

There should be a compiler option that will provide that,
or most of it, but I don't remember what it is called.
I think it only maps the first occurrence item/group of an array,
but I'm pretty sure that it remaps the redefines for you.
I remember cutting and pasting some of them into my PDS
to help me with problem diagnosis, and to include in specs.
```

#### ↳ Re: Cobol Copybook mapper.

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-18T15:18:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f404640_3@news.athenanews.com>`
- **References:** `<TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au>`

```
Ron,

I think Hugh's advice is good.

It's a long time ago, and I may be confusing compilers, but you could try
OPTION SYM, MAP.

(I think it provides the generated Assembler code and all the DSECTs. (these
are what you need ?)).

I have something that does a map of Record layouts (I wrote it myself) but
without knowing exactly what you are hoping to get and in what format, I
don't know how suitable it would be.

Try the compiler options; at least they won't cost you anything...<G>.

Pete

"Ron Davis" <rdavis@ozemail.com.au> wrote in message
news:TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au...
>
>
…[3 more quoted lines elided]…
> storage map from it (similar to the Record Print Facility of FileAid,
which
> I'm ditching at my site) This will be used in conjunction for COBOL For
> OS/390 at a mainframe site.
>
> It need to handle arrays (tables) and redefines etc.  In the case of
tables
> it should print out a record for each table element, eg, 05 ELEMENT(3,3)
> PIC XXX  and the offset from the start of the Level 1 for that structure.
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Cobol Copybook mapper.

- **From:** "Ron Davis" <rdavis@ozemail.com.au>
- **Date:** 2003-08-18T14:59:01+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B2Z%a.66$Cn1.3991@nnrp1.ozemail.com.au>`
- **References:** `<TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au>`

```
Hi!

Thanks for the replies so far, I'm aware of the MAP option and am using in
the program I'm writing (I actually compile the copybook in a "do nothing"
program and then work with the compiler output) but it doesn't do all I need
by a long way.

If anybody wants more info email me at ron.davis@dva.gov.au and send I'll
send you a copybook and the results of the FileAid analysis so you can get a
btter idea of what I need and the issues.

Cheers

RonD
```

##### ↳ ↳ Re: Cobol Copybook mapper.

- **From:** "Hugh Candlin" <hugh.candlin@worldnet.att.net>
- **Date:** 2003-08-18T05:26:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csZ%a.104313$0v4.7297256@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au> <B2Z%a.66$Cn1.3991@nnrp1.ozemail.com.au>`

```

Ron Davis <rdavis@ozemail.com.au> wrote in message
news:B2Z%a.66$Cn1.3991@nnrp1.ozemail.com.au...
> Hi!
>
> Thanks for the replies so far, I'm aware of the MAP option and am using
in
> the program I'm writing (I actually compile the copybook in a "do
nothing"
> program and then work with the compiler output) but it doesn't do all I
need
> by a long way.
>
> If anybody wants more info email me at ron.davis@dva.gov.au and send I'll
> send you a copybook and the results of the FileAid analysis so you can
get a
> btter idea of what I need and the issues.

Just post a sample here.
That is what the newsgroup is for.
If people took everything to email,
the NG would lose much of its utility.
```

#### ↳ Re: Cobol Copybook mapper.

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-08-18T10:41:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4320b.8944$Ih1.3219858@newssrv26.news.prodigy.com>`
- **References:** `<TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au>`

```
"Ron Davis" <rdavis@ozemail.com.au> wrote in message
news:TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au...
> It need to handle arrays (tables) and redefines etc.  In the case of
tables
> it should print out a record for each table element, eg, 05 ELEMENT(3,3)
> PIC XXX  and the offset from the start of the Level 1 for that structure.

It's old, it's ugly, it runs on a PC under MS-DOS not OS/390, but....

The price is right (free), but it works and the offsets from the start of
each '01' are in decimal rather than hex. (Hmm, if you're familar with IBM
mainframe software, "ugly but it works" should make you feel right at home).

Get file COBFD.ZIP from the Flexus download page at
http://www.flexus.com/download.html  or just use the direct link:
ftp://ftp.flexus.com/cobfd.zip

(Yes, I have been threatening for several years to update this to a
Windows(r) version. Maybe 2003 will be the year).

And please speak kindly of me ...
```

#### ↳ Re: Cobol Copybook mapper.

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-08-18T11:48:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8230b.103788$3o3.7246222@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au>`

```

"Ron Davis" <rdavis@ozemail.com.au> wrote in message
news:TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au...
|
|
…[3 more quoted lines elided]…
| storage map from it (similar to the Record Print Facility of FileAid,
which
| I'm ditching at my site) This will be used in conjunction for COBOL For
| OS/390 at a mainframe site.
|
| It need to handle arrays (tables) and redefines etc.  In the case of
tables
| it should print out a record for each table element, eg, 05 ELEMENT(3,3)
| PIC XXX  and the offset from the start of the Level 1 for that structure.
…[9 more quoted lines elided]…
|

Ron,

I did this once using REXX.
Compile a null program with the copybook, and process the DMAP output.

I don't recall what it did with OCCURS.
If you want to write your own, REXX would be my language of choice.
```

#### ↳ Re: Cobol Copybook mapper.

- **From:** Alain Feler <member15854@dbforums.com>
- **Date:** 2003-08-18T08:30:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3255531.1061209842@dbforums.com>`
- **References:** `<TOV%a.25$Cn1.2292@nnrp1.ozemail.com.au>`

```

I found this somewhere (on CobolReport.com probably).

It is free, and it works. Here is the doc, cut a bit to stay below the
10,000 bytes limit of dbForum:





                   Tal Systems' COBOL FD Analyzer - COBFD

                            Version 1.50 August 1999

                      by Michael Mattias dba Tal Systems



   COBFD is a tool for COBOL programmers. Very simply, what it
   does is parse

   a COBOL source file (either a copylib or complete source),
   identifies all

   group and  elementary data items, then breaks down all '01' and
   subordinate

   group items into their components and produces a report file
   showing the

   size in bytes and the offset within the '01' record of every
   subordinate

   data item. All group and elementary data items are included.
   The user has

   an option to include the input file in the report output (follows
   analysis).



   COBFD supports all levels of REDEFINES and OCCURS: REDEFINES
   which OCCUR,

   OCCURS which OCCUR while REDEFINE'ing an item which OCCURS; OCCUR'ing

   group items with mixed data types. These are typically the greatest

   challenges to counting bytes "by hand".



   COBFD runs on MS-DOS and compatible PC's and requires DOS 2.0
   or higher.

   It will run in a DOS session under Windows(r).It is a single user

   program; there is no provision for sharing files, but the program has

   been run on a network.



   The program creates and deletes an internal workfile, COBFD@@.WRK, in

   the  user's current directory.



   Both the input and output files are user-specified at run time.
   The output

   file is 80 bytes per record, formatted, with page headers (all text).

   The user must provide a file viewer/printer for screen or
   printed output.



   COBFD is [.....] intended as advertising for the author.



   To use the COBFD program interactively:



      COBFD <Enter>



   You will be given a screen with boxes for input file and output file.

   (The mouse is not enabled on this screen).



   To use the COBFD program from the command line or in a batch
   file, enter

   four parameters separated by semicolons, commas or spaces:



   [drive]:[path]COBFD
   SourceFile;OutputFile;IncludeSource;Append;CompStorage



   SourceFile     = Cobol input file, drive/path optional

   OutputFile     = Disk File for report, drive/path optional

   IncludeSource  = Y or N (any other character is an error)

   Append         = Y will append the report to the specified
   output file

                    if found, or create a new output file if not found.

                    N will always open the report file OUTPUT, erasing

                    any previous report file.

   CompStorage    = Used for COMP, COMP-4 and COMP-5 only. B is
   byte storage;

                    storage is based on the minimum bumber of whole
                    bytes

                    required. W is Word storage; data sizes are rounded

                    up to the next 2, 4 or 8 bytes.

                    For reference: IBM mainframe COBOL uses WORD
                    storage;

                    Microfoucus Personal Cobol for MS-DOS uses BYTE
                    storage.

                    Consult your COBOL system manual and/or compile
                    scripts

                    for the option used with your programs.



   COBFD /H   or COBFD /?

   Displays the syntax for the command-line options.



   Sample Batch files:



   COBFD  File1.cbl;Report1.txt;Y;N;W

   COBFD  File2.Cbl;Report1.txt;Y;Y:B



   Another batch file:



   IF exist LIBFILE.TXT del libfile.txt

   FOR %%F IN (*.cbl) DO COBFD %%F;LIBFILE.TXT;Y;Y;W



   Print one report file, LIBFILE.TXT, containing all *.cbl files in

   the current directory.(word storage)



   What Tal Systems' COBFD COBOL FD Analyzer assumes:



   A valid COBOL FD. If PICTURE clauses are missing or illegal,
   sentences are

   not terminated with a period, or levels are inconsistent, the program

   will return unreliable data, generally without a warning.



   If column seven (7) of the input file is non-blank, the line is
   a comment.



   All PICTURE, OCCURS, REDEFINES, USAGE DISPLAY|COMP|SIGN
   SEPARATE and other

   COBOL keywords appear in columns 13-72 . These clauses may,
   however, span

   multiple physical lines with comment lines interspersed. The
   order in which

   keywords appear is immaterial. A COBOL sentence is not
   terminated until

   a non-quoted period is found.



   The QUOTE character is the first double-quote (") or apostrophe (')
   found

   in a non-comment input record. The QUOTE character is redefined for
   each

   file processed during a program run; i.e., the user can process
   multiple

   files, some using quote and others using apostrophe as the literal
   delimiter.



   A REDEFINES clause below the '01' level assumes that the area being

   redefined is the same size as the redefined area. (Not an ANSI COBOL

   requirement). If this is not true, the program will appear to finish

   normally, but the data may be erroneous. REDEFINES is ignored at the

   '01' dataname level.



   When parsing the input file, if the first two words in a non-
   comment line

   are PROCEDURE and DIVISION, the program stops looking for data;
   however,

   if printing the input file, it prints the entire file.



   RENAMES ('66-level') clauses are not supported



   SYNC clauses are not supported.



   PICTURE clauses containing "P" (scaled numeric) are not supported.



   POINTER and PROCEDURE POINTER data items are not supported



   USAGE BINARY is considered USAGE COMPUTATIONAL.



   USAGE PACKED-DECIMAL is considered USAGE COMPUTATIONAL-3



   COMP, COMP-4 AND COMP-5 are used for Binary integers. COMP-3 is

   Binardy-coded-decimal, often called "packed."



   Only EJECT, SKIP1, SKIP2, COPY and ++INCLUDE are recognized as

   compiler directives (treated as comments). Other directives may

   cause the program to insert an extra SYSTEM-GENERATED-01-DATANAME

   in the output following the directive. The offset information should

   not be affected unless the unsupported directive is contained within

   the physical boundaries of an explicit or implicit '01' dataname.



   No form of COPY is supported; but copylibs themselves may be
   analyzed.



   If an '01' record is not found as the first COBOL data item,
   the system

   creates one with the name SYSTEM-GENERATED-01-DATANAME. This
   allows the

   program to be used with copylibs not containing an '01 -level'
   dataname.





   COBFD is a copyright product. It may be freely used and
   distributed without

   payment or registration. However, it may not be distributed for
   monetary

   consideration, either standalone or "bundled" with other utilities,

   applications or instructional material without the permission of the

   copyright owner.



   Distribution to individual programmers is encouraged.



   Copyright 1996, 1998 Michael C. Mattias dba Tal Systems, Racine WI
   USA.



   The author would appreciate any comments, remarks, bug reports, or

   desired enhancements be submitted to:



   Michael C. Mattias dba Tal Systems

   5329 Charles St.

   Racine, WI 53402-2119 USA

   414-681-3895

   EMail  michael.mattias@gte.net



** ENDS **
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
