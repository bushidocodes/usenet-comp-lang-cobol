[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Language-Environment Cobol for MVS&VM zOS 1.2?

_5 messages · 4 participants · 2002-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Language-Environment Cobol for MVS&VM zOS 1.2?

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2002-07-27T15:55:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020727.15550279@04307839700-0001.dialin.t-online>`
- **References:** `<20020724.18084264@04307839700-0001.dialin.t-online> <5cu3kuklom8dul4dnj9lh4v7tov3u8n9ns@4ax.com>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 27.07.02, 01:42:06, schrieb Michael Todd <mikltodd@comcast.net> zum 
Thema Re: Language-Environment Cobol for MVS&VM zOS 1.2?:


> Because you are specifying "recording mode v" IBM COBOL automatically 
adds a length attribute to the front of each
> record.  That's why the record length is longer than 220.  That all in 
the IBM manuals, by the way.  If you read the
> records with a COBOL program, the lengths will not be part of the 
record area (they're stripped off as the records are
> read).  Utility programs and other languages (especially assembler) 
may "see" the record lengths as part of the
> reocord-- it depends upon how they define the file.

I dont know, how cobol is working on a pc or in dos/vse but since my 
early days of computing cobol is only using a pointer inside the 
file-section:

if you use this in an MVS-environment:

FD File recording mode v....
01 short-rec pic x(20).
01 log-rec pic x(1000).

An you are moving the long-rec at the ent of the qsam-buffer, you will 
get a systemabend 0C4.

So if you use this:
01 tab pic s9(04) comp occurs 10 indexed by ind-tab.

And this smal code:

set ind-tab to 1
set ind-tab down by 3

move tab (ind-tab) to...

you will have acces to the rdw-bytes of the current record. This migt 
be work only if you use the compiler directive NOSSRANGE :-)

the records are stored:
aabbxxyyssssssxxyysssssss....

aa --> is the block-length-field
bb --> spare bytes
xx --> is the rdw
yy --> spare bytes
ss --> content of the record

the aa+bb fields can only accessed at a new block.

And here some information from DCB: Construct a Data Control Block 
(BPAM) IBM-Book:

    LRECL=absexp (maximum value is 32760)
       specifies the length, in bytes, for fixed-length records, or it
       specifies the maximum length, in bytes, for variable-length and
       undefined-length records.  The value specified in LRECL cannot 
exceed
       the value specified in BLKSIZE.

>snip>

       Variable-length records:  the value specified in LRECL must 
include
       the maximum data length (up to 32752 bytes) plus 4 bytes for 
the
       record-descriptor word (RDW).

<snip>

there is nothing that say: must specify the maximum data....
it can be more....

have a nice day

Andreas
```

#### ↳ Variable length records in IBM COBOL 85 was Re: Language-Environment Cobol for MVS&VM zOS 1.2?

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2002-07-28T20:03:59-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D44785F.D8112EC7@istar.ca>`
- **References:** `<20020724.18084264@04307839700-0001.dialin.t-online> <5cu3kuklom8dul4dnj9lh4v7tov3u8n9ns@4ax.com> <20020727.15550279@04307839700-0001.dialin.t-online>`

```
The maximum length of the COBOL record must agree with the maximum
length in the Data Set Label (COBOL length + 4) for non-VSAM or the
maximum length as defined in the Catalog for VSAM files (COBOL record
length).  While I believe that this protection should be that the COBOL
maximum length is not less than the length specified for the file in the
data set label or Catalog that is not what the ANSI idiots specified. 
For non-VSAM files you can get around this by coding LRECL in the JCL
for the file so that it agrees with the COBOL record length.  Similar
overrides can be used for TSO (see the manual or help for TSO commands).
In the COBOL program you can code the FD to have RECORD VARYING
DEPENDING ON YOUR-UNSIGNED-NUMERIC-FIELD and then MOVE LARGEST-RECORD (1
: YOUR-UNSIGNED-NUMERIC-FIELD) TO YOUR-WORKING-STORAGE-RECORD.  For best
results YOUR-UNSIGNED-NUMERIC-FIELD should USAGE BINARY.  

In CICS the point is moot because your COBOL program should not contain
any FD's and should use CICS commands to access all files.

Andreas Lerch wrote:
> 
> >>>>>>>>>>>>>>>>>> Ursprï¿½ngliche Nachricht <<<<<<<<<<<<<<<<<<
…[76 more quoted lines elided]…
> Andreas
```

##### ↳ ↳ Re: Variable length records in IBM COBOL 85 was Re: Language-Environment Cobol for MVS&VM zOS 1.2?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-07-29T01:04:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ai2ltm$anv$1@slb7.atl.mindspring.net>`
- **References:** `<20020724.18084264@04307839700-0001.dialin.t-online> <5cu3kuklom8dul4dnj9lh4v7tov3u8n9ns@4ax.com> <20020727.15550279@04307839700-0001.dialin.t-online> <3D44785F.D8112EC7@istar.ca>`

```
Clark,
  Although I mentioned (in a previous post) that "fixed file attribute"
checking is a requirement of the ANSI Standard and *not* something that IBM
came up with - there is another side to this story.

In one of the very earliest "interpretation" requests of the '85 Standard,
ANSI (via the J4 technical committee) made it ABUNDANTLY clear that it is up
to EACH implementor exactly what "attributes" they do and do not check.  In
fact, this was made explicit in an Amendment to the ANSI Standard.

Therefore,  your statement (below),
 "While I believe that this protection should be that the COBOL maximum
length is not less than the length specified for the file in the data set
label or Catalog that is not what the ANSI idiots specified."

is "slightly" misleading.  It was IN DEED, IBM and not ANSI (or ISO) that
decided to do this "checking".

Personally, I don't think it is a "bad" idea to make certain that anything
that you specify in your COBOL source code actually MATCHES the way the file
"exists" on outside media.  I think that everyone would have been "happier"
if IBM had done an extension similar to "BLOCK CONTAINS 0 RECORDS" that says
to "check the file attributes" - to say "check the file attributes for the
record length or lengths".  But as they didn't, I don't (again personally)
think that it is such a bad idea to have the code match the file.
```

###### ↳ ↳ ↳ Re: Variable length records in IBM COBOL 85 was Re: Language-Environment Cobol for MVS&VM zOS 1.2?

- **From:** Andreas Lerch <andreaslerch@t-online.de>
- **Date:** 2002-07-29T16:50:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020729.16500267@mis.configured.host>`
- **References:** `<20020724.18084264@04307839700-0001.dialin.t-online> <5cu3kuklom8dul4dnj9lh4v7tov3u8n9ns@4ax.com> <20020727.15550279@04307839700-0001.dialin.t-online> <3D44785F.D8112EC7@istar.ca> <ai2ltm$anv$1@slb7.atl.mindspring.net>`

```
Hello,

>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 29.07.02, 06.04.32, schrieb "William M. Klein" 
<wmklein@nospam.ix.netcom.com> zum Thema Re: Variable length records in 
IBM COBOL 85 was Re: Language-Environment Cobol for MVS&VM zOS 1.2?:


> Clark,
>   Although I mentioned (in a previous post) that "fixed file 
attribute"
> checking is a requirement of the ANSI Standard and *not* something 
that IBM
> came up with - there is another side to this story.

> In one of the very earliest "interpretation" requests of the '85 
Standard,
> ANSI (via the J4 technical committee) made it ABUNDANTLY clear that it 
is up
> to EACH implementor exactly what "attributes" they do and do not 
check.  In
> fact, this was made explicit in an Amendment to the ANSI Standard.

> Therefore,  your statement (below),
>  "While I believe that this protection should be that the COBOL 
maximum
> length is not less than the length specified for the file in the data 
set
> label or Catalog that is not what the ANSI idiots specified."

> is "slightly" misleading.  It was IN DEED, IBM and not ANSI (or ISO) 
that
> decided to do this "checking".

> Personally, I don't think it is a "bad" idea to make certain that 
anything
> that you specify in your COBOL source code actually MATCHES the way 
the file
> "exists" on outside media.  I think that everyone would have been 
"happier"
> if IBM had done an extension similar to "BLOCK CONTAINS 0 RECORDS" 
that says
> to "check the file attributes" - to say "check the file attributes for 
the
> record length or lengths".  But as they didn't, I don't (again 
personally)
> think that it is such a bad idea to have the code match the file.

Thank you, thats what i mean

Andreas Lerch
```

###### ↳ ↳ ↳ Re: Variable length records in IBM COBOL 85 was Re: Language-Environment Cobol for MVS&VM zOS 1.2?

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2002-07-30T10:49:20-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D469960.322D49C7@istar.ca>`
- **References:** `<20020724.18084264@04307839700-0001.dialin.t-online> <5cu3kuklom8dul4dnj9lh4v7tov3u8n9ns@4ax.com> <20020727.15550279@04307839700-0001.dialin.t-online> <3D44785F.D8112EC7@istar.ca> <ai2ltm$anv$1@slb7.atl.mindspring.net>`

```
My rant came about from dealing with SMF (Systems Management Facility)
accounting and performance records.  The maximum record length had been
specified differently for different files.  The mainframe system
function can deal with that (SMF is an operating system component) in
the production of the files so in this instance I was getting protection
I neither wanted nor needed.  In general, I would be content with
allowing RECORD 0 VARYING DEPENDING ON and this probably would be a good
cross platform extension.  There also may be value in not having the
check in instances where there are subset and superset versions of files
with different fixed lengths for the records depending on the file but a
common base.   
"William M. Klein" wrote:
> 
> Clark,
…[126 more quoted lines elided]…
> > > Andreas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
