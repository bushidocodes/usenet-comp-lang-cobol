[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Two questions about VA COBOL,one is for language,the other is for tool.

_14 messages · 6 participants · 2002-07_

---

### Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** heyanchun@163.net (He Yanchun)
- **Date:** 2002-07-03T23:26:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96959ca4.0207032226.2c22e02@posting.google.com>`

```
I use VA COBOL 3.0.5 to develop. And when i want to read a file using
following code, i can not get the right return.

......

Environment division.
Input-Output Section.
File-control.
    Select Compare-file Assign to "d:\mywork\test\compare.txt"
           organization is Sequential
           Access Mode Is Sequential
           FILE STATUS IS FS-CODE.

Data Division.
File Section.
FD Compare-file.
01 compare-field.
    05 first-para             PIC X(10).
    05 second-para            PIC X(10).

Working-Storage Section.
......
01 FS-CODE  PIC X(2).

Procedure Division.

    Initialize Program-work-field Program-flags.
    display fs-code
    Open I-O Compare-file
    display fs-code
    Read Compare-file Into Program-Work-Field
    at end
        display 'at end'
    not at end
        display 'in the read'
    display fs-code
    ...... 
    Close Compare-file


The file "d:\mywork\test\compare.txt" is my defined using UltraEdit,as
1234567890abcdefghij
1234567890abcdefghij
1234567890abcdefghij
1234567890abcdefghij

And i got the output like this:
     ----------display before open
39   ----------display after open
     ----------display after read
but actually not read the file, i mean the "Program-Work-Field" is
still empty.

And if i change "organization is Sequential" to "organization is
indexed" or "organization is relative" ,i got the same output.But
change to "organization is line Sequential", the output change to:
     ----------display before open
00   ----------display after open
     ----------display after read

but still not read,the "Program-Work-Field" is empty.

What's wrong with my code or file? Please help me out! Thank you!

The second question is about VA COBOL tool.

When i create a new Non-GUI project, and click "Edit a new file"
button,
and then in the Program edit window,i change profile to cbl,and then
i begin to enter the code,but when i enter "Enter" after a line, and
then
the Program Edit window will no response.

What's wrong with my operation.
Please help me!

He Yanchun
```

#### ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-07-04T10:37:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RzVU8.4198$Bd2.145@nwrddc01.gnilink.net>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com>`

```
He Yanchun <heyanchun@163.net> wrote in message
news:96959ca4.0207032226.2c22e02@posting.google.com...
> I use VA COBOL 3.0.5 to develop. And when i want to read a file using
> following code, i can not get the right return.
…[6 more quoted lines elided]…
> What's wrong with my code or file? Please help me out! Thank you!

Code '39'  after the open means the open failed. Refer to your manual for
the exact meaning of the code.

Since the OPEN failed, the READ cannot succeed (it's an attempt to read an
unopened file). If you did a DISPLAY FS-CODE after the read, you'd see the
appropriate file status for that, too.

MCM
```

#### ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-07-04T08:50:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KvXU8.21060$2w.355535@news20.bellglobal.com>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com>`

```
Why are you opening it "I/O" when you want to READ the file?


Donald

"He Yanchun" <heyanchun@163.net> wrote in message
news:96959ca4.0207032226.2c22e02@posting.google.com...
> I use VA COBOL 3.0.5 to develop. And when i want to read a file using
> following code, i can not get the right return.
…[74 more quoted lines elided]…
> He Yanchun
```

#### ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-07-04T13:15:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7UXU8.548943$%y.36241951@bin4.nnrp.aus1.giganews.com>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com>`

```

"He Yanchun" <heyanchun@163.net> wrote in message
news:96959ca4.0207032226.2c22e02@posting.google.com...
> I use VA COBOL 3.0.5 to develop. And when i want to read a file using
> following code, i can not get the right return.
…[36 more quoted lines elided]…
>

1. Usually you can't do both input and output on a sequential file. So, you
should OPEN INPUT.

2. Starting with "Read..." there better be a period somewhere or the "Close"
statement is part of the action undertaken after the first successful read
operation. I recommend:

   READ...
      AT END ...
      NOT AT END ...
      END-READ.

3. Your program only reads one record then quits. Consider:

   READ
   PERFORM UNTIL FS-CODE NOT = '00'
      DISPLAY 'in the read' (or other processing)
      READ
      END-PERFORM.

This is the so-called 'priming read' technique. A slightly longer version
is:

   MOVE 'N' TO EOF-FLAG.
   PERFORM UNTIL EOF-FLAG NOT = 'N'
      READ
         AT END MOVE 'Y' TO EOF-FLAG
         END-READ
      IF EOF-FLAG = 'N'
         DISPLAY 'in the read' (or other processing)
      ELSE
         CLOSE
      END-IF
   END-PERFORM.
```

##### ↳ ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** heyanchun@163.net (He Yanchun)
- **Date:** 2002-07-04T18:10:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96959ca4.0207041710.34fbcdab@posting.google.com>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <7UXU8.548943$%y.36241951@bin4.nnrp.aus1.giganews.com>`

```
I follow your recommend. But the program still can not read a single record.
Now my question is, whether COBOL can READ the files which are manually created
just like my file or not.

Thank a lot!

He Yanchun
"JerryMouse" <nospam@bisusa.com> wrote in message news:<7UXU8.548943$%y.36241951@bin4.nnrp.aus1.giganews.com>...
> 1. Usually you can't do both input and output on a sequential file. So, you
> should OPEN INPUT.
…[31 more quoted lines elided]…
>    END-PERFORM.
```

##### ↳ ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-05T07:52:02+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D254212.77AE4A5E@Azonic.co.nz>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <7UXU8.548943$%y.36241951@bin4.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:
> 
> 
…[4 more quoted lines elided]…
>       END-PERFORM.

When testing a file status code for successful operation only the first
digit should be checked for zero.  Checking both characters for '00' may
give false failure signals.  The first character of zero indicates
success, the 2nd character may indicate additional information.  Thus
'02' also indicates successful read for example.
```

###### ↳ ↳ ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-07-04T23:09:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bB4V8.276180$_j6.13634745@bin3.nnrp.aus1.giganews.com>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <7UXU8.548943$%y.36241951@bin4.nnrp.aus1.giganews.com> <3D254212.77AE4A5E@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3D254212.77AE4A5E@Azonic.co.nz...
> JerryMouse wrote:
> >
…[11 more quoted lines elided]…
> '02' also indicates successful read for example.

Not on a sequential file, it doesn't.

My compiler lists the following non-'00' status codes:

02 - Duplicate key (either read or write)
04 - Record length does not conform to fixed attributes
05 - Bad open when OPTIONAL clause present
07 - Open or Close issued with NO REWIND specified
```

###### ↳ ↳ ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-06T15:49:27+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D270377.882F0AC9@Azonic.co.nz>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <7UXU8.548943$%y.36241951@bin4.nnrp.aus1.giganews.com> <3D254212.77AE4A5E@Azonic.co.nz>`

```
JerryMouse wrote:
>
> > When testing a file status code for successful operation only the first
…[12 more quoted lines elided]…
> 07 - Open or Close issued with NO REWIND specified

Those are _sucessful_ completions of the operation with additional
information - exactly as I stated.  

For example an '02' indicates that the record has been read or written
successfully and there is a duplicate key where this has been specified
as 'WITH DUPLICATES'.  If the read or write failed because there was a
duplicate key and these were _not_ allowed the the status would be '22'.

The '05' indicates an OPTIONAL file did not exist when it was OPENed for
input.  This is a _successful_ operation because the file is specified
as OPTIONAL.  Even though the file does not exist it has been 'OPENed'
correctly and may be READ, but the AT END or INVALID KEY path will be
taken.  The file should also be CLOSEd before the program finishes.

The '07' indicates that the file has been successfully closed but was
not rewound, as requested.

These are examples of exactly why only the first byte should be tested
for success and the 2nd byte is additional information.  In fact these
are the only code defined in ANS85 in this category, but the next
standard may define more - programs that only test for '00' may give
false failure messages when the next standard system is installed.
```

##### ↳ ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-05T12:16:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D25801C.30E4077@Azonic.co.nz>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <7UXU8.548943$%y.36241951@bin4.nnrp.aus1.giganews.com>`

```
JerryMouse wrote:
> 
> 1. Usually you can't do both input and output on a sequential file. 

There is no such restriction on disk files.  A disk SEQUENTIAL file can
always be open in I-O mode for READing and REWRITEing.  Certainly it
need to be open OUTPUT or EXTEND for WRITEing new records.

> So, you should OPEN INPUT.

Only if he doesn't want to REWRITE.
```

#### ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-05T08:02:13+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D254475.BE2ADB60@Azonic.co.nz>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com>`

```
He Yanchun wrote:
> 
> The file "d:\mywork\test\compare.txt" is my defined using UltraEdit,as
…[17 more quoted lines elided]…
>      ----------display after read

You cannot create a 'SEQUENTIAL' file (or a RELATIVE or INDEXED) using a
text editor.  These file types are not just random groups of bytes but
have additional bytes in them that give them a structure.  For example
they may have header information that describes to the Cobol program
what the record length is and there may be record size counts.

A 'LINE SEQUENTIAL' file, however, _is_ just groups of bytes with a
CR/LF record terminators and can be created by a text editor.

When you say in your program that the file is 'SEQUENTIAL' (or RELATIVE
or INDEXED) with a record size as in the FD then the '39' status is
telling you: "No it isn't".

You need to read the data you have created as a LINE SEQUENTIAL file and
if you need it as a SEQUENTIAL or INDEXED you need to write this from
your program.
```

##### ↳ ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-07-04T23:16:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LH4V8.122202$Ca2.6598069@bin2.nnrp.aus1.giganews.com>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <3D254475.BE2ADB60@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3D254475.BE2ADB60@Azonic.co.nz...
> He Yanchun wrote:
> >
…[27 more quoted lines elided]…
> CR/LF record terminators and can be created by a text editor.

Well he COULD create the required sequential file with a text editor by
defining his file as:

FD Compare-file.
01 compare-field.
    05 first-para             PIC X(10).
    05 second-para            PIC X(10).
    05  filler-crlf            PIC X(2).

to account for the extra carriage-return/line-feed silently inserted by the
text editor. Or since he had only four records in his file, he COULD have
typed:

"1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcde
fghij"

into the text editor and his original FD would have worked.
```

###### ↳ ↳ ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** "Al Shannon" <shannon@allover.com>
- **Date:** 2002-07-05T20:13:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zftV8.1$AY2.1396@news.sjc.globix.net>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <3D254475.BE2ADB60@Azonic.co.nz> <LH4V8.122202$Ca2.6598069@bin2.nnrp.aus1.giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:LH4V8.122202$Ca2.6598069@bin2.nnrp.aus1.giganews.com...
>
> "Richard Plinston" <riplin@Azonic.co.nz> wrote in message
…[24 more quoted lines elided]…
> to account for the extra carriage-return/line-feed silently inserted by
the
> text editor. Or since he had only four records in his file, he COULD have
> typed:
>
>
"1234567890abcdefghij1234567890abcdefghij1234567890abcdefghij1234567890abcde
> fghij"
>
> into the text editor and his original FD would have worked.
>
>

Not true.  Richard Plinston is correct.  Relative, Sequential, and Indexed
files are created and manipulated using the selected record-oriented
filesystem STL or Btrieve (think VSAM on the mainframe).  Text editors
create stream files, defined in VA COBOL as Line-Sequential organization.

Al...
```

##### ↳ ↳ Re: Two questions about VA COBOL,one is for language,the other is for tool.

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-06T16:02:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D270694.6C8E19@Azonic.co.nz>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <3D254475.BE2ADB60@Azonic.co.nz>`

```
Jerrymouse wrote:
> > A 'LINE SEQUENTIAL' file, however, _is_ just groups of bytes with a
> > CR/LF record terminators and can be created by a text editor.
…[11 more quoted lines elided]…
> text editor. 

No.  Not necessarily.  It may work on some system _if_ the sequential
files are defined only as fixed length records with no other formatting
_and_ he can guarantee that the editor will put the line ends at the
correct place.  However, I don't know that VA Cobol will work with such
files, I do know that many Cobol systems certainly will not, they write
a file header with information about record length and other details
prior to the first record.

In fact because VA Cobol failed on the OPEN as a SEQUENTIAL file I would
take this as prima-face evidence that it tried to check some header
information and based its '39' status on not finding it.  If the system
only used fixed block records as you postulate then it would have no
basis to report a '39' failure, but would only fail after finding the
last record incomplete.

> Or since he had only four records in his file, he COULD have
> typed:
…[4 more quoted lines elided]…
> into the text editor and his original FD would have worked.

No. Wrong.
```

##### ↳ ↳ Could you tell me the difference between STL or Btrieve

- **From:** "Al Shannon" <shannon@allover.com>
- **Date:** 2002-07-08T21:43:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F%tW8.3$AY2.9894@news.sjc.globix.net>`
- **References:** `<96959ca4.0207032226.2c22e02@posting.google.com> <3D254475.BE2ADB60@Azonic.co.nz>`

```
I received some questions via e-mail:

        I want to know more about STL or Btrieve (VSAM on the mainframe),
and the difference among them. Perhaps include QSAM.

        And could you please tell me which filesystem has been used on NT or
AS/400.


For detailed information see the VA COBOL Programming Guide "Chapter 7.
Processing files" available online at

http://www-3.ibm.com/software/ad/cobol/va/library/

From the Programming Guide:

    Record-oriented files that are organized as sequential, relative,
indexed, or line
sequential (byte stream) files are accessed through a file system. You can
use
file-system functions to create and manipulate the records in any of these
types of
files.
    VisualAge COBOL supports the following file systems:
    The STL file system, which provides the basic facilities for local
files. It is
provided with VisualAge COBOL, and supports sequential, relative, and
indexed
files.
    The VSAM file system, which allows you to read and write files on remote
systems such as OS/390. It is provided with VisualAge COBOL, and supports
sequential, relative, and indexed files.
    The Btrieve file system, which allows you to access Btrieve files.
Btrieve is a
separate product available from Pervasive Software.
    Tip: By using the Btrieve file system, you can access files created by
VisualAge
CICS Enterprise Application Development.
    Most programs will have the same results on all file systems. However,
files
written using one file system cannot be read using a different file system.
You can select a file system by setting the assignment-name environment
variable
or by using the FILESYS run-time option. All the file systems allow you to
use
COBOL statements to read or write COBOL files.


VSAM and QSAM are mainframe (MVS, zOS) record-oriented filesystem access
methods used by mainframe COBOL.

STL is available on OS/2, Windows, and AIX.  The last I checked, Btrieve is
available on OS/2 and Windows.

Al...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
