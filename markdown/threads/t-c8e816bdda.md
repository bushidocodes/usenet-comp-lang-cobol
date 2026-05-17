[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating and writing to a variable number of files

_8 messages · 7 participants · 1998-07 → 1998-08_

---

### Creating and writing to a variable number of files

- **From:** "bob kenney" <ua-author-528242@usenetarchives.gap>
- **Date:** 1998-07-18T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35B276DC.118E@ici.net>`

```
I would like to read a datafile & look at a particular data field and
add the record to a file with that name.

The problem is a little easier since the file names have already been
stored in a WS-ARRAY. Also, the format of all of the files are the
same.

Is there a way that you can use the OCCURS qualifier in the file
definition section?

Thanks,

________     __                        
        \  _ \_\o
         \(_)/ _\.       __o
  bob     \   (_)      _`\-\,
           \__________(_)/ (_)______
```

#### ↳ Re: Creating and writing to a variable number of files

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c8e816bdda-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35B276DC.118E@ici.net>`
- **References:** `<35B276DC.118E@ici.net>`

```
You can use occurs in any data description, including a record.
EG:
fd myfile
whatever your cobol likes
data record is array-record.
01 array-record occurs 15 times.
02 file-name picture x(8).
02 file-extension picture x(3).
```

#### ↳ Re: Creating and writing to a variable number of files

- **From:** "dave johnson" <ua-author-6589126@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c8e816bdda-p3@usenetarchives.gap>`
- **In-Reply-To:** `<35B276DC.118E@ici.net>`
- **References:** `<35B276DC.118E@ici.net>`

```
Bob Kenney wrote in message <35B··.@i··.net>...
› I would like to read a datafile & look at a particular data field and
› add the record to a file with that name.
…[10 more quoted lines elided]…
› --
Think Bob is being a bit more ambitious here - as I read it, you are
reading an input file which contains the filename of an output file, so
ideally, you'd want a SELECT file ASSIGN TO WS-ARRAY(n).

Don't think you can do that (certainly hope not, you'll get yourself into
all sorts of trouble, possibly). If you could (dynamically allocate a
physical file to a logical file during execution), the overhead would
be horrendous - each WRITE would have to OPEN EXTEND, WRITE
CLOSE, so.........

If you have a fixed number of files, you could define FDs for all of them
then either open them all at the start (advantage, any file you haven't
written to will be empty, so the following process wouldn't pick up data
from the last run), or forget the SELECT/FD and code an external
module in a language which supports dynamic filenames (Pascal/C).
You may find that you need to have a separate OPEN and maintain
'this file is open' flags in your program (for efficiency), also a bulk
CLOSE (if open) at end of run.

Another alternative is to write the output to one file with a 'file number'
prefix on each record. If you also write a 'control file' with prefix and
filename, you could write a post-process module (in another language)
which split the output into separate files.

Give us a bit more info about the application and you'll be deluged!

DaveJ.
```

#### ↳ Re: Creating and writing to a variable number of files

- **From:** "ken foskey" <ua-author-3204800@usenetarchives.gap>
- **Date:** 1998-07-22T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c8e816bdda-p4@usenetarchives.gap>`
- **In-Reply-To:** `<35B276DC.118E@ici.net>`
- **References:** `<35B276DC.118E@ici.net>`

```
I assume you mean if the record contains file1 then you want to write it
to file1 if it contains file2 then write it to file2 and so on. The
cobol answer is no to my knowledge. The only way to my knowledge is
IF type-1
write file1 from data-item
else if type2
write file2 from data-item
... and so on ....
endif. (of course :-) )

If you are MVS take a look at DF sort which can separate a file based
upon a data item into several files. But this is not a cobol answer.

In MVS You can also call an assembler routine to close and open the one
DD name and if the data is sorted into order the cobol stays the same
but the 'real' filename is changing.

Hope this helps
KEn

Bob Kenney wrote:
› 
› I would like to read a datafile & look at a particular data field and
…[7 more quoted lines elided]…
› definition section?
```

#### ↳ Re: Creating and writing to a variable number of files

- **From:** "c5..." <ua-author-17074191@usenetarchives.gap>
- **Date:** 1998-07-24T16:45:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c8e816bdda-p5@usenetarchives.gap>`
- **In-Reply-To:** `<35B276DC.118E@ici.net>`
- **References:** `<35B276DC.118E@ici.net>`

```
In article <35B··.@i··.net>,
rmk··.@i··.net wrote:
› I would like to read a datafile & look at a particular data field and
› add the record to a file with that name.
…[17 more quoted lines elided]…
› 

I do not know how to use an occurs qualifier in the file definition section,
but do know a trick that allows one to change files on the fly by calling a
two-line Cobol program. When a COBOL program calls a program, the address of
the parm fields is stored in register 1. Normally, the address points to a
fullword that contains the address where the first parm begins. The next
fullword contains the address where the second parm begins and so on. If you
specify the actual cobol name of the file that is used in the select-assign
statement as the first parameter when you call another program, it will
cause register 1 to point to a fullword that indicates the address of the dcb
for that file in the select-assign statement. The layout for the dcb in main
storage is as follows: the first 40 bytes contain DCB info and then 8 bytes
contain the DDNAME:

Register 1 ----> 00000F0A + (This is the location in storage where there is
| one fullword for each parm passed)
|
+-> 00000F0A 00001A0C 00003B0C (These are two fullwords
that point to the location in storage where the first two parms are stored)
|
Parm1 +--> 00001A0C ---> DCB info DDNAME
| +------------------+-------+
| 40 bytes 8 bytes
Parm2 +--> 00003B0C ---> NEWDDNM

So if you pass two parameters to a subprogram, one of which contains the
COBOL name of a file that has been defined in a select assign, and the other
which contains the ddname of a file that you want to swap to, you can overlay
the orignal DDNAME for the file with a new one. This is possible because we
know the layout of the information about a file in main storage, and we know
that the ddname is placed 40 positions after the start.

This technique does not allow you to change lrecl or recfm, and all of the
files that are going to be used still have to be predefined in the JCL with
DDNAME and Dataset names. But the technique does allow you to change on the
fly which ddname you are pointing to while you are inside your cobol program.

Here is an example:

Main Program:

SELECT IO-ANY-FILE ASSIGN TO IOANY.

FD IO-ANY-FILE
(USUAL FD INFO)
01 IO-ANY-REC PIC X(133).

WORKING-STORAGE SECTION.
01 WS-NEWDD-PASSED PIC X(8).

PROCEDURE DIVISION. MOVE 'NEWDDNM' TO WS-NEWDD-PASSED. CALL 'DDNAMR' USING
IO-ANY-FILE (note: IO-ANY-FILE is not defined as a regular WS-NEWDD-PASSED.
variable in COBOL - it is just the file name specified in the select and
fd) OPEN OUTPUT IO-ANY-FILE (note: this actually opens file defined in jcl
with ddname NEWDDNM) WRITE IO-ANY-REC. ETC....

Called Program:

PROGRAM-ID. DDNAMR. (note: stands for ddname rename)
LINKAGE SECTION.
01 DCB.
05 FILLER PIC X(40).
05 DDNAME PIC X(8).
01 DCB-DDNAME-PASSED PIC X(8).
PROCEDURE DIVISION.
MOVE DCB-NAME-PASSED TO DDNAME. (note: this overlays original ddname of IOANY
with NEWDDNM).
GOBACK.

Good Luck,
Wade Harvey

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

##### ↳ ↳ Re: Creating and writing to a variable number of files

- **From:** "am" <ua-author-33177@usenetarchives.gap>
- **Date:** 1998-08-05T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c8e816bdda-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c8e816bdda-p5@usenetarchives.gap>`
- **References:** `<35B276DC.118E@ici.net> <gap-c8e816bdda-p5@usenetarchives.gap>`

```
i am not quite sure if this is what I needed (too). I am programming in
Cobol for
9+ years (not a newbie, definitely not homework ;o)) ). But definetely
needs
your advice....

This is my problem. I need to send out email messages from a COBOL program
to notify a number of recipients of the status of certain processes. the
number of different
messages is variable and so does the number of recipients. I need to be
able to distribute the messages. i need to know how to allocate to multiple
files (which the
presented solution helps, if limited to a fixed number of outputs).
-- now i am not sure if this can be done: format & submit a batch JCL/job
from a Cobol batch program.
I am not sure if I have seen this done with a previous client but I could
be wrong, I was doing
CICS/COBOL then. - I am contemplating in formatting a JCL that would
IEBGENER the
the records into files and then next step is to send it to the emailing
software(and/or FTP)...

somebody... help!!!!!! can somebody tell me how or what to look for; if it
CAN'T be done,
what's a good alternative?

Aedehl


c5··.@my-··s.com wrote in article <6parp5$nc8$1.··.@nnr··s.com>...

| I do not know how to use an occurs qualifier in the file definition
section,
| but do know a trick that allows one to change files on the fly by calling
a
| two-line Cobol program. When a COBOL program calls a program, the
address of
| the parm fields is stored in register 1. Normally, the address points to
a
| fullword that contains the address where the first parm begins. The
next
| fullword contains the address where the second parm begins and so on. If
you
| specify the actual cobol name of the file that is used in the
select-assign
| statement as the first parameter when you call another program, it will
| cause register 1 to point to a fullword that indicates the address of the
dcb
| for that file in the select-assign statement. The layout for the dcb in
main
| storage is as follows: the first 40 bytes contain DCB info and then 8
bytes
| contain the DDNAME:
|
| Register 1 ----> 00000F0A + (This is the location in storage where
there is
| | one fullword for each parm passed)
| |
| +-> 00000F0A 00001A0C 00003B0C (These are two
fullwords
| that point to the location in storage where the first two parms are
stored)
| |
| Parm1 +--> 00001A0C ---> DCB info DDNAME
…[5 more quoted lines elided]…
| COBOL name of a file that has been defined in a select assign, and the
other
| which contains the ddname of a file that you want to swap to, you can
overlay
| the orignal DDNAME for the file with a new one. This is possible because
we
| know the layout of the information about a file in main storage, and we
know
| that the ddname is placed 40 positions after the start.
|
| This technique does not allow you to change lrecl or recfm, and all of
the
| files that are going to be used still have to be predefined in the JCL
with
| DDNAME and Dataset names. But the technique does allow you to change on
the
| fly which ddname you are pointing to while you are inside your cobol
program.
|
| Here is an example:
…[12 more quoted lines elided]…
| PROCEDURE DIVISION. MOVE 'NEWDDNM' TO WS-NEWDD-PASSED. CALL 'DDNAMR'
USING
| IO-ANY-FILE (note: IO-ANY-FILE is not defined as a regular
WS-NEWDD-PASSED.
| variable in COBOL - it is just the file name specified in the select
and
| fd) OPEN OUTPUT IO-ANY-FILE (note: this actually opens file defined in
jcl
| with ddname NEWDDNM) WRITE IO-ANY-REC. ETC....
|
…[9 more quoted lines elided]…
| MOVE DCB-NAME-PASSED TO DDNAME. (note: this overlays original ddname of
IOANY
| with NEWDDNM).
| GOBACK.
…[6 more quoted lines elided]…
|
```

###### ↳ ↳ ↳ Re: Creating and writing to a variable number of files

- **From:** "am" <ua-author-33177@usenetarchives.gap>
- **Date:** 1998-08-05T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c8e816bdda-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c8e816bdda-p6@usenetarchives.gap>`
- **References:** `<35B276DC.118E@ici.net> <gap-c8e816bdda-p5@usenetarchives.gap> <gap-c8e816bdda-p6@usenetarchives.gap>`

```
thanks. found it. i'm sending the formatted JCL to the Internal reader...
```

###### ↳ ↳ ↳ Re: Creating and writing to a variable number of files

- **From:** "edste..." <ua-author-8362724@usenetarchives.gap>
- **Date:** 1998-08-06T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c8e816bdda-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c8e816bdda-p6@usenetarchives.gap>`
- **References:** `<35B276DC.118E@ici.net> <gap-c8e816bdda-p5@usenetarchives.gap> <gap-c8e816bdda-p6@usenetarchives.gap>`

```
I have written and submitted jcl from within a CICS program. Never
thought of doing it from a batch pgm, but it seems the fundamental
technique would be the same. If you realize that when you do it from
a CICS pgm you are actually writing to a 'file' whose DD entry in the
CICS startup deck is defined as a system internal reader (I believe
there is a thread on this subject right now) I don't know why you
couldn't do it from a batch program as well:

PROGRAM-ID. MYPGM.

SELECT MYJCL
ASSIGN INTRDR.

FD INTRDR.
01 JCL-REC PIC X(80).

WRITE JCL-REC FROM WS-JCL-STRING


//MYJCL JOB .....
//STEP1 EXEC PGM=MYPGM
//INTRDR DD SYSOUT= (get some help from your CICS systems
programmer)

My syntax my be off. I haven't been on the mainframe for a few years,
but this should give you the idea.
On 6 Aug 1998 16:02:56 GMT, "AM" wrote:

› now i am not sure if this can be done: format & submit a batch JCL/job
› from a Cobol batch program. 
› I am not sure if I have seen this done with a previous client but I could
› be wrong, I was doing
› CICS/COBOL then

Ed Stevens/TN
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
