[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question: File Status - IBM QSAM

_10 messages · 8 participants · 2003-09_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Question: File Status - IBM QSAM

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2003-09-12T03:36:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com>`

```
   I've been programming in COBOL on an IBM Mainframe for about 5 years. I
have seen various ways of handling file errors for QSAM files (i.e. flat
files; sequential files), and I have been told various things regarding
possible errors.
   One thing that I have been told is that you should always check File
Status after an OPEN. I agree with that, since various IO or JCL errors can
cause a file to fail to open.
   But what about READ, WRITE, and CLOSE? I've seen programs which check
Status for all of these, and others which do not. I am told that it is not
necessary, since, if the file was opened successfully, any further error
except End of File (IO error, out of space, etc.) will abend the program,
and any check of Status will never occur.
   Again, I am *only* talking about QSAM files, reading or writing
sequentially. Any comments?
```

#### ↳ Re: Question: File Status - IBM QSAM

- **From:** Paul Knudsen <paul@jupada.com>
- **Date:** 2003-09-12T04:17:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dsh2mv878l6l45n2udlv7mthuqtnghqvuh@4ax.com>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com>`

```
On Fri, 12 Sep 2003 03:36:56 GMT, "William Bub"
<fathafluff@hotmail.com> wrote:

>   I've been programming in COBOL on an IBM Mainframe for about 5 years. I
>have seen various ways of handling file errors for QSAM files (i.e. flat
…[12 more quoted lines elided]…
>
William:  Forgive that mail;  thought I was still in listserv.  :(

I never bother checking status in QSAM.  If there's a problem the
system console gives adequate information.  Whey clutter up the
program?  

(Yes...I know this will probably start a flame.  Shields are up.)

----------------------------------------------
The hell with space aliens.  Dedicate your spare computer
time to fighting disease.
http://www.stanford.edu/group/pandegroup/folding/
```

##### ↳ ↳ Re: Question: File Status - IBM QSAM

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-09-12T07:13:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F61722E.E1D82F74@worldnet.att.net>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com> <dsh2mv878l6l45n2udlv7mthuqtnghqvuh@4ax.com>`

```
Paul Knudsen wrote:
> 
> I never bother checking status in QSAM.  If there's a problem the
…[3 more quoted lines elided]…
> (Yes...I know this will probably start a flame.  Shields are up.)

No flame.  I never bother checking for errors on QSAM files either. 
The runtime environment error checking is good enough.
```

###### ↳ ↳ ↳ Re: Question: File Status - IBM QSAM

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-12T14:17:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2Ak8b.202$Aq2.40@newsread1.news.atl.earthlink.net>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com> <dsh2mv878l6l45n2udlv7mthuqtnghqvuh@4ax.com> <3F61722E.E1D82F74@worldnet.att.net>`

```
It seems to me that the "basic question" is whether you want to place logic
in your program to "handle" situations that might occur for QSAM files that
cannot be checked by a <not> AT END or not.

If you WANT to "recover" in your own logic for other "errors" (conditions),
then use a file status key and/or a declarative to handle all "non-normal"
situations.  If you only want to ABEND when such situations arise, then do
NOT use any file status field or any declarative.

P.S.  Also make certain that you understand and set correctly the CBLQDA
run-time option.
```

###### ↳ ↳ ↳ Re: Question: File Status - IBM QSAM

_(reply depth: 4)_

- **From:** Paul Knudsen <paul@jupada.com>
- **Date:** 2003-09-14T01:49:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q7i7mv48ftqg4qcmu9h5p8eb4mijcgk2nm@4ax.com>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com> <dsh2mv878l6l45n2udlv7mthuqtnghqvuh@4ax.com> <3F61722E.E1D82F74@worldnet.att.net> <2Ak8b.202$Aq2.40@newsread1.news.atl.earthlink.net>`

```
On Fri, 12 Sep 2003 14:17:34 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>It seems to me that the "basic question" is whether you want to place logic
>in your program to "handle" situations that might occur for QSAM files that
…[8 more quoted lines elided]…
>run-time option.

Excellent point.  I can't imagine any situations where you'd want to
continue if a file was unusable, but there might be some.
----------------------------------------------
The hell with space aliens.  Dedicate your spare computer
time to fighting disease.
http://www.stanford.edu/group/pandegroup/folding/
```

#### ↳ Re: Question: File Status - IBM QSAM

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-09-12T08:16:53-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F61AB25.417C46E4@istar.ca>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com>`

```
In response to the posting below, either specify the FILE STATUS option
on the SELECT statement and check all I-O because the run-time is
deferring handling to the program or don't specify FILE STATUS and let
the run-time abend the program on serious errors.  If you specify FILE
STATUS and don't check the result of a write, upon an out of space
condition the WRITE will fail and the program will continue normally.  A
lot of data can be put to the bit bucket this way without any
indication.

Clark Morris

William Bub wrote:
> 
>    I've been programming in COBOL on an IBM Mainframe for about 5 years. I
…[12 more quoted lines elided]…
> sequentially. Any comments?
```

#### ↳ Re: Question: File Status - IBM QSAM

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-12T11:27:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%4i8b.138901$3o3.9879824@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com>`

```

"William Bub" <fathafluff@hotmail.com> wrote in message
news:sbb8b.52295$yG2.33756@twister.nyroc.rr.com...
|    I've been programming in COBOL on an IBM Mainframe for about 5 years. I
| have seen various ways of handling file errors for QSAM files (i.e. flat
…[3 more quoted lines elided]…
| Status after an OPEN. I agree with that, since various IO or JCL errors
can
| cause a file to fail to open.

Once you include checking file status, you disable system error checking.
Leave the file status out, if you want the system to handle the errors.

|    But what about READ, WRITE, and CLOSE? I've seen programs which check
| Status for all of these, and others which do not.

Again, once file status is used, you MUST use it.

|I am told that it is not
| necessary, since, if the file was opened successfully, any further error
| except End of File (IO error, out of space, etc.) will abend the program,
| and any check of Status will never occur.

Not true, if you specify file status, the system will still recognize AT
END, and INVALID KEY if they are coded.

|    Again, I am *only* talking about QSAM files, reading or writing
| sequentially. Any comments?

The best thing to do is leave the file status out, and let the system handle
all errors.
```

#### ↳ Re: Question: File Status - IBM QSAM

- **From:** "Vince Coen" <Vince_Coen@f609.n257.z2.fidonet.org>
- **Date:** 2003-09-12T14:51:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1063378035@f609.n257.z2.fidonet.ftn>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com>`

```
Hello William!

12 Sep 03 03:36, William Bub wrote to All:

 WB>    One thing that I have been told is that you should always check
 WB> File Status after an OPEN. I agree with that, since various IO or JCL
 WB> errors can cause a file to fail to open.
 WB>    But what about READ, WRITE, and CLOSE? I've seen programs which
 WB> check Status for all of these, and others which do not. I am told that
 WB> it is not necessary, since, if the file was opened successfully, any
 WB> further error except End of File (IO error, out of space, etc.) will
 WB> abend the program, and any check of Status will never occur.
 WB>    Again, I am *only* talking about QSAM files, reading or writing
 WB> sequentially. Any comments?

I have always written checks for all IO. That way I control what the program 
or procedure will do and not the operating system.

There are instances where you can get a IO failure and need to perform a 
specific action and not a abend.

Vince
```

#### ↳ Re: Question: File Status - IBM QSAM

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-13T03:27:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M8w8b.53326$Mb2.1727646@twister.tampabay.rr.com>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com>`

```
I always use an error declarative section for exception on input and output.

I give each file a file status and in the generic exception message handler
I write a list of each of the
filenames and the current file status.

I prefer this because you can set the return code to be a nice OPC catchable
number like 99 which flags in a job scheduler.  A true abend general freaks
out system people and creates an unecessary dump in any report management
system.

You can get the same information by not handling it but it looks amateurish
to just let it abend when it's simple enough to not allow it.

I would also follow any local standards....we had a contractor add FILE
STATUS at a time when they were not used to each of the programs they had to
update (don't know why)...unfortunately they didn't always check it and it
would abend in some strange places when the read would fail and not be
caught.

I have often had the same thoughts with a DB2 Close Cursor.  Typically this
is the last action and catching it makes no difference....what do you do
with an exception if you're just closing up the program anyway.

JCE




"William Bub" <fathafluff@hotmail.com> wrote in message
news:sbb8b.52295$yG2.33756@twister.nyroc.rr.com...
>    I've been programming in COBOL on an IBM Mainframe for about 5 years. I
> have seen various ways of handling file errors for QSAM files (i.e. flat
…[3 more quoted lines elided]…
> Status after an OPEN. I agree with that, since various IO or JCL errors
can
> cause a file to fail to open.
>    But what about READ, WRITE, and CLOSE? I've seen programs which check
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Question: File Status - IBM QSAM

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-13T11:53:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nzD8b.137288$0v4.10067732@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<sbb8b.52295$yG2.33756@twister.nyroc.rr.com> <M8w8b.53326$Mb2.1727646@twister.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:M8w8b.53326$Mb2.1727646@twister.tampabay.rr.com...
| I always use an error declarative section for exception on input and
output.
|
| I give each file a file status and in the generic exception message
handler
| I write a list of each of the
| filenames and the current file status.
|
| I prefer this because you can set the return code to be a nice OPC
catchable
| number like 99 which flags in a job scheduler.  A true abend general
freaks
| out system people and creates an unecessary dump in any report management
| system.

Sometimes I WANT to freak them out.

|
| You can get the same information by not handling it but it looks
amateurish
| to just let it abend when it's simple enough to not allow it.

It's a matter of preference.
I prefer having the system check, at least it will handle things
consistently.
An untrapped error could be harder to fix, since the end result could be
erroneous data getting into the system.

|
| I would also follow any local standards....we had a contractor add FILE
| STATUS at a time when they were not used to each of the programs they had
to
| update (don't know why)...unfortunately they didn't always check it and it
| would abend in some strange places when the read would fail and not be
| caught.
|
| I have often had the same thoughts with a DB2 Close Cursor.  Typically
this
| is the last action and catching it makes no difference....what do you do
| with an exception if you're just closing up the program anyway.

Times change, now I can send an e-mail to have someone look into the problem
before it becomes something serious.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
