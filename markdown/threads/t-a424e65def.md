[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VSAM Error Code 04

_9 messages · 6 participants · 2006-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### VSAM Error Code 04

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2006-11-07T15:54:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com>`

```
This is embarrasing.  I've been a Cobol programmer for nearly 30
years.  I've done Systems work, CICS work, VM work and coded on IBM
mainframes op systems from DOS through z/OS.  But for the life of me,
I cannot figure out what is wrong with what is essentially a simple
program.  Hopefully, someone here will say, "You dummy!  You forgot
to..." whatever.

Here are the specifics:

I have the following Select Statement:

SELECT MASTER01-IN
    ASSIGN TO MAST01I
   ORGANIZATION IS INDEXED
    ACCESS MODE IS SEQUENTIAL
    FILE STATUS IS WS-FILE-STATUS
    RECORD KEY IS MAST01-KEY.

Then we have the following FD:

FD  MASTER01-IN.
01  MASTER01-RECORD.
     03  MAST01-KEY           PIC  X(19).
     03  FILLER                     PIC (2481).

Pretty simple, yes?  The file is opened with no errors.  A simple read
is done:

READ MASTER01-IN.

WS-FILE-STATUS is checked and we find that it contains 04.  The entire
return code is 0004.  This says that there is a conflict between the
record length and fixed file attributes.

However, a LISTCAT shows the file is not fixed.  It has a MAXIMUM
record length of 2500 and an Average record length of 1440.  The first
record on file (according to a File Aid dump) says the length is 1600
and something long, well within the allocated 2500 bytes.

Just for kicks, I added 4 bytes to the record length and tried again.
This time I got a 0039 error code - file attributes conflict of actual
vs. specified.

The file is used in online without any problems.  I'm trying to access
it in a batch Cobol program.  What have I missed?  What have I done
wrong?  Someone PLEASE give me a clue.

Thanks.



          ////
         (o o)
-oOO--(_)--OOo-


"I was such an ugly baby...My mother never breast fed me.
She told me that she only liked me as a friend..."
-- RODNEY DANGERFIELD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: VSAM Error Code 04

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2006-11-07T21:08:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bt1l21gi03mhrsrckg0ti5hi0nhl1nl0i@4ax.com>`
- **References:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com>`

```
On Tue, 07 Nov 2006 15:54:19 -0500, SkippyPB
<swiegand@neo.rr.NOSPAM.com> wrote:

>This is embarrasing.  I've been a Cobol programmer for nearly 30
>years.  I've done Systems work, CICS work, VM work and coded on IBM
…[3 more quoted lines elided]…
>to..." whatever.

Either add a RECORD VARYING DEPENDING ON field-x clause to the FD or a
second 01 level describing an average length record.
>
>Here are the specifics:
…[55 more quoted lines elided]…
>Steve
```

#### ↳ Re: VSAM Error Code 04

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-11-07T14:04:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1162937077.389984.306310@b28g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com>`
- **References:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com>`

```

SkippyPB wrote:

> WS-FILE-STATUS is checked and we find that it contains 04.  The entire
> return code is 0004.  This says that there is a conflict between the
> record length and fixed file attributes.

When testing File Status for success it is necessary to only test the
first byte for being zero. This indicates successful completion (in
this case a read). The second byte may contain additional information
in which case a test for '00' incorrectly shows that it 'failed' even
though the operation was successful.

The problem seems to be that you have no mechanism by which the system
can tell you the length of the actual record read.  As the record area
is only changed to the point of the end of the record then junk will
remain beyond that point, but you are not being told where that point
is because there is no indicator to hold the length.
```

##### ↳ ↳ Re: VSAM Error Code 04

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-11-08T07:28:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p8q3l29368ev95vs03rok1s912345h5lbo@4ax.com>`
- **References:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com> <1162937077.389984.306310@b28g2000cwb.googlegroups.com>`

```
On 7 Nov 2006 14:04:37 -0800, "Richard" <riplin@Azonic.co.nz> wrote:

>When testing File Status for success it is necessary to only test the
>first byte for being zero. This indicates successful completion (in
>this case a read). The second byte may contain additional information
>in which case a test for '00' incorrectly shows that it 'failed' even
>though the operation was successful.

Although "97" also indicates successful open on IBM mainframes.
```

#### ↳ Re: VSAM Error Code 04

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-11-07T14:08:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1162937326.668093.205630@m73g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com>`
- **References:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com>`

```

SkippyPB wrote:

> This says that there is a conflict between the
> record length and fixed file attributes.
>
> However, a LISTCAT shows the file is not fixed.

It is 'fixed (file attributes)' not '(fixed file) attributes'.  That
is: the fixed attributes of the file.
```

#### ↳ Re: VSAM Error Code 04

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-11-07T23:10:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ln84h.797341$Jn2.508278@fe10.news.easynews.com>`
- **References:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com>`

```
Clark gave this answer (in general), but to be specific,

Change

FD  MASTER01-IN.
 01  MASTER01-RECORD.
     03  MAST01-KEY           PIC  X(19).
     03  FILLER                     PIC (2481).

to

 FD  MASTER01-IN
     Record Varying in size from 1 to 2500.
 01  MASTER01-RECORD.
     03  MAST01-KEY           PIC  X(19).
     03  FILLER                     PIC (2481).

you could add a "depending on" to the new line - pointing to a WS item to "get" 
the size of each record, but it isn't required.

alternatively (as an IBM extension) you could add
  Record Format V

****

When you have no RECORD CONTAINS/VARYING or RECORD FORMAT clause and have only 
one 01-level (with no OCCURS in it), then IBM mainframe COBOL "defaults" to 
fixed rather than variable format.

P.S.  For future reference - if working in an IBM environment (as VSAM implies), 
then you MAY want to think about also using "file status 2" (not to be confused 
with the 2nd byte of the "normal" file status field).  For more information on 
it, see:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr31/4.2.13

OTOH,  I usually find the COBOL status values (FS1) to be enough to figure out 
the problem and when I start looking at VSAM return codes and stuff it confuses 
me more than it helps <G>.
```

#### ↳ Re: VSAM Error Code 04

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2006-11-07T18:21:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4rcppcFqoho7U1@mid.individual.net>`
- **References:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com>`

```
I'm assuming that the records vary in length, up to 2500 bytes.

FD  MASTER01-IN
    RECORD VARYING FROM 1 TO 2500 CHARACTERS
    DEPENDING ON MASTER01-LEN.
01  MASTER01-RECORD.
     03  MAST01-KEY           PIC  X(19).
     03  FILLER                     PIC (2481).

WORKING-STORAGE SECTION.
77  MASTER01-LEN              PIC 9(5) VALUE ZERO.

After each read MASTER01-LEN will contain the actual length of the record
read.

By the way, as my programming mentor loves to say "All VSAM files are
variable".  That is to say that you cannot define a "fixed length record"
VSAM file.  You can define a file with RECORDS(100, 32000) and happily write
1 byte records to it.  This does not mean that the file has a fixed record
size of 32000 nor does it mean that it has a fixed record size of 1.  It
simply means that each variable length record can be up to 32000 bytes, and
in this case each variable length record is 1 byte long.

The "average record length" is only useful when defining a number of records
rather than the number of tracks or cylinders.

If any of the above is incorrect please blame my mentor.  :-)

My the way, if MASTER01-IN contains only records of *specific* record sizes
then you can "simplify" it with something like:
FD  MASTER01-IN.
01  MASTER01-RECORD.
     03  MAST01-KEY           PIC  X(19).
     03  FILLER                     PIC (2481).
01  MASTER01-REC2    PIC X(100).
01  MASTER01-REC3    PIC X(1000).
01  MASTER01-REC4    PIC X(1600).

This assumes that there's some way to distinguish between the different
record types, such as maybe something in the key.  Without knowing how
you're using it its hard to say more.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> SkippyPB<swiegand@neo.rr.NOSPAM.com> 11/07/06 1:54 PM >>>
This is embarrasing.  I've been a Cobol programmer for nearly 30
years.  I've done Systems work, CICS work, VM work and coded on IBM
mainframes op systems from DOS through z/OS.  But for the life of me,
I cannot figure out what is wrong with what is essentially a simple
program.  Hopefully, someone here will say, "You dummy!  You forgot
to..." whatever.

Here are the specifics:

I have the following Select Statement:

SELECT MASTER01-IN
    ASSIGN TO MAST01I
   ORGANIZATION IS INDEXED
    ACCESS MODE IS SEQUENTIAL
    FILE STATUS IS WS-FILE-STATUS
    RECORD KEY IS MAST01-KEY.

Then we have the following FD:

FD  MASTER01-IN.
01  MASTER01-RECORD.
     03  MAST01-KEY           PIC  X(19).
     03  FILLER                     PIC (2481).

Pretty simple, yes?  The file is opened with no errors.  A simple read
is done:

READ MASTER01-IN.

WS-FILE-STATUS is checked and we find that it contains 04.  The entire
return code is 0004.  This says that there is a conflict between the
record length and fixed file attributes.

However, a LISTCAT shows the file is not fixed.  It has a MAXIMUM
record length of 2500 and an Average record length of 1440.  The first
record on file (according to a File Aid dump) says the length is 1600
and something long, well within the allocated 2500 bytes.

Just for kicks, I added 4 bytes to the record length and tried again.
This time I got a 0039 error code - file attributes conflict of actual
vs. specified.

The file is used in online without any problems.  I'm trying to access
it in a batch Cobol program.  What have I missed?  What have I done
wrong?  Someone PLEASE give me a clue.

Thanks.



          ////
         (o o)
-oOO--(_)--OOo-


"I was such an ugly baby...My mother never breast fed me.
She told me that she only liked me as a friend..."
-- RODNEY DANGERFIELD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: VSAM Error Code 04

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2006-11-08T13:30:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b84l29jcj33vnn859qdf1so0fo7lp68rn@4ax.com>`
- **References:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com> <4rcppcFqoho7U1@mid.individual.net>`

```
On Tue, 7 Nov 2006 18:21:46 -0700, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> enlightened us:

>I'm assuming that the records vary in length, up to 2500 bytes.
>
…[95 more quoted lines elided]…
>

Thanks to Clark, Frank, and Bill.  That was the solution I finally
came up with myself after a good nights sleep.

Note to Bill:  On the IBM Mainframe, if your Select says Organization
is Indexed, Cobol ZOS will give you a S (serious) compile error if you
put a Recording Mode is V in the FD.

Note to Richard:  I didn't try it but I'm guessing that the return
code of 04 did not put a record into the record area.  I might have
abended for some other cause had I not checked both bytes and abended
the read myself.  Besides you need to check for 10 to know you are at
end of file.

Thanks again.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I was such an ugly baby...My mother never breast fed me.
She told me that she only liked me as a friend..."
-- RODNEY DANGERFIELD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: VSAM Error Code 04

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-11-08T12:53:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1163019208.226241.89310@e3g2000cwe.googlegroups.com>`
- **In-Reply-To:** `<8b84l29jcj33vnn859qdf1so0fo7lp68rn@4ax.com>`
- **References:** `<urr1l2psaknq4umoae6dqgg88tkqv0b599@4ax.com> <4rcppcFqoho7U1@mid.individual.net> <8b84l29jcj33vnn859qdf1so0fo7lp68rn@4ax.com>`

```

SkippyPB wrote:

> Note to Richard:  I didn't try it but I'm guessing that the return
> code of 04 did not put a record into the record area.

The first byte of the file status being zero indicates _successful_
completion. The record will be in the record area.  The '4' indicates
that it cannot tell you how long the record is.  If you had several 01
levels of different lengths or an ODO then it would not need to tell
you the length because it would be based on data items in the record.

If you had DEPENDING ON then it could tell you the length, or more
importantly, you could tell it the length when writing by 01 level,
ODO, or DEPENDING ON.  One or more of those mechanisms should be used.

> I might have
> abended for some other cause had I not checked both bytes and abended
> the read myself.

You must have some way of determining which parts of the records are
valid and which are beyond the data read in, probably some sort of ODO
or perhaps a record type in the key.  Your use of that would prevent
'abended for some other cause', or fail to prevent, regardless of the
'04' status.

> Besides you need to check for 10 to know you are at end of file.

That is irrelevant to (wrongly) testing for "00".

What is wrong with AT END ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
