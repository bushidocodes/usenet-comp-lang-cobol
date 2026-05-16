[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Request for testing of Reltive File status

_38 messages · 8 participants · 2009-05_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Request for testing of Reltive File status

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-14T14:58:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com>`

```
I may have asked for this a while ago, but I am trying to find out what as many 
compilers/run-times do with this program as possible.  I am particularly 
interested in which compilers do NOT return a FS=24 when you try and write a 
relative record with a key of zero.  As I recall, some compilers yield other 2x 
values.

You can respond on the list or to me privately.  (As far as I can guess, I don't 
think that compiler directives/options should make a difference, however, if you 
want to try various options, please do so). This will probably NOT work with 
pre-85 Standard compilers - not only is it "mixed case" but I don't think they 
supported variable length relative files.

Depending on your environment, you will probably have to modify the "ASSIGN TO" 
clause and *may* need to "pre-allocate" the relative file.

Sample code follows:

       Identification Division.
        Program-Id. relfs.
       Environment Division.
        Input-Output Section.
         File-Control.
           Select RelFile Assign RelName
               Access Dynamic
               Organization Relative
               Status Rel-FS
               Relative Key RelKey .
       Data Division.
        File Section.
       FD  RelFile
           Record Varying in Size
               From 1 to 999
               Depending on RelLen.
       01  RelRec.
           05  RR-Elem occurs 1 to 999 times
                   Depending on RelLen
                     Pic X(01).
        Working-Storage Section.
       01  RF-Stuff.
           05  RelName  Pic X(08) Value "relftest".
           05  Rel-FS  Pic X(02).
               88  RFS-OK   Value "00".
               88  RFS-24   Value "24".
           05  RelKey  Pic 9(03).
           05  RelLen  Pic 9(03).
       Procedure Division.
        Mainline.
           Perform Create-File
           Stop Run
            .
        Create-File.
           Open Output RelFile
           If RFS-OK
               Move Zero to RelKey
               Move 123 to RelLen
               Move all "x" to RelRec
               Write RelRec
                   Invalid Key
                       If RFS-24
                           Display "Test Passes, FS=24"
                       Else
                           Display "Invalid FS:"  Rel-FS
                       End-If
               End-Write
               Close RelFile
           Else
               Display "Bad FS on OPEN:" Rel-FS
           End-IF
            .
```

#### ↳ Re: Request for testing of Reltive File status

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-16T13:13:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com>`

```
Has anyone been able to run this test yet?  I haven't gotten any answers on-list 
or off-list.

I am particularly interested in what results come from CURRENT versions of
 - IBM Enterprise COBOL
 - IBM ILE COBOL (or whatever the iSeries compiler is called now)
 - Micro Focus (with and without .NET)
 - Alchemy (formerly Fujitsu)
```

##### ↳ ↳ Re: Request for testing of Reltive File status

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-16T12:22:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com>`

```
On May 17, 6:13 am, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> Has anyone been able to run this test yet?  I haven't gotten any answers on-list
> or off-list.
…[5 more quoted lines elided]…
>  - Alchemy (formerly Fujitsu)


> possible.  I am particularly
> >interested in which compilers do NOT return a FS=24 when you try and write a
> >relative record with a key of zero.  As I recall, some compilers yield other 2x
> >values.

> >           05  Rel-FS  Pic X(02).
> >               88  RFS-OK   Value "00".
> >               88  RFS-24   Value "24".

When testing a file status for success only the first byte should be
checked for zero. The second byte may contain additional information.


Fujitsu Cobol for Linux 7.3

STATISTICS: HIGHEST SEVERITY CODE=I, PROGRAM UNIT=1
Test Passes, FS=24
```

###### ↳ ↳ ↳ Succesful Status code (was: Request for testing of Reltive File status

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-16T15:04:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com>`

```
<riplin@Azonic.co.nz> wrote in message 
news:13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com...
On May 17, 6:13 am, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
<snip>
> > 05 Rel-FS Pic X(02).
> > 88 RFS-OK Value "00".
> > 88 RFS-24 Value "24".

When testing a file status for success only the first byte should be
checked for zero. The second byte may contain additional information.

As previously stated (and as I will continue to state when you claim this), this 
is ONLY true if you consider the "0x" values other than "00" to be successful.

In the sample code provided, the only time RFS-OK was used was after an OPEN. 
In that case, anything other than "00" would have been impossible.  If it DID 
happen, I would have wanted to treat it as a failure.

Bottom-Line:
  Checking for "00" is the BEST way to check for "00".  If your program logic is 
intended to treat other "0x" values as successful, THEN you should include them 
in your "successful" check.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-16T15:45:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uBFPl.420448$rp7.167265@en-nntp-02.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com>`

```
OOPS - what I added and was responding to wasn't clear

Hopefully, clearer below:
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-16T14:54:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com>`

```
On May 17, 8:04 am, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> <rip...@Azonic.co.nz> wrote in message
>
…[14 more quoted lines elided]…
>

The standard states that the first byte being zero indicates
'success'. If you wish to treat a successful code other than a success
then perhaps you should do so.

> In the sample code provided, the only time RFS-OK was used was after an OPEN.
> In that case, anything other than "00" would have been impossible.  If it DID
> happen, I would have wanted to treat it as a failure.

No it is _not_ impossible after an OPEN. '05' after an open indicates
that an optional file did not exist and either has been created or can
be read. It does not indicate failure and requires that the file be
CLOSEd (which a failure code does not).

>
> Bottom-Line:
>   Checking for "00" is the BEST way to check for "00".  If your program logic is
> intended to treat other "0x" values as successful, THEN you should include them
> in your "successful" check.

No. You are wrong that yours is the 'best' way.

A first byte of zero indicates that the action of the statement has
been completed successfully. If you want some successful results to be
treated as failures you should make that explicit rather than using
code that apparently does not understand how Cobol works.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-16T22:37:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com>`

```
You can think what you want about what is "successful" and what is not.  To me, 
the term "successful" I/O means that FOR THIS PROGRAM, what has happened is 
successful and processing for "good results" should proceed.  NOT successful 
means that what has happened is something that the logic FOR THIS PROGRAM that 
should follow is for the "unsuccessful" path.

P.S. Please show me where I had an OPTIONAL phrase for the file in my program. 
Hence a "05" could NOT occur (for that Open in that program).

NOTE:
  This is why for IBM mainframes when opening VSAM files, it is GOOD to include 
"97" in the list of "successful' codes for an OPEN.  The Standard explicitly 
says this is UNSUCCESSFUL, but for every COBOL program that I know in THAT 
environment,  GOOD programming logic treats this successful.

NOTE2:
  IBM mainframe shops who know about CBLQDA can tell you that what the standard 
says is "successful" is NOT what most (almost all?) application programs in such 
environments want to treat as successful.

This is a "generalization" (general rule) that, unlike most that we discuss in 
this forum, I really do think is so close to universal that the difference in 
nondetectable.  Application programs should treat status codes according to what 
their specific programs need to do and NOT based on the "label" that the 
Standard places on something.

If your application logic needs to treat "02" "05" or "0?" as successful, the do 
so.  If hour application logic needs to "lump" these with unsuccessful values, 
then do so.  The fact that there *ARE* other "0x" file status codes is important 
to realize; whether they should be treated as successful or not is NOT a 
universal condition and should be tailored to the specific needs of "your" 
application.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-17T01:34:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com>`

```
On May 17, 3:37 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> You can think what you want about what is "successful" and what is not.  To me,
> the term "successful" I/O means that FOR THIS PROGRAM, what has happened is
> successful and processing for "good results" should proceed.  NOT successful
> means that what has happened is something that the logic FOR THIS PROGRAM that
> should follow is for the "unsuccessful" path.

No. Wrong. The standard defines what is successful for each statement.
ie if the OPEN, READ, WRITE, etc does what the operation requests then
it is defined to be 'successful' regardless of what the program logic
does with this information.

You are confusing what the file status is reporting with program logic
that has deal with this.

> P.S. Please show me where I had an OPTIONAL phrase for the file in my program.
> Hence a "05" could NOT occur (for that Open in that program).

In some compilers, such as MicroFocus it is possible to set the
default to OPTIONAL with compiler options, it need not be specified in
the source code.


> NOTE:
>   This is why for IBM mainframes when opening VSAM files, it is GOOD to include
> "97" in the list of "successful' codes for an OPEN.  The Standard explicitly
> says this is UNSUCCESSFUL, but for every COBOL program that I know in THAT
> environment,  GOOD programming logic treats this successful.

As I understand '97' a repeat of the OPEN will get a successful (0x)
file status.

If the file has been successfully OPENed I would expect a CLOSE
required before a second OPEN statement. Fortunately it is unlikely to
be an issue though I am aware of it.

> NOTE2:
>   IBM mainframe shops who know about CBLQDA can tell you that what the standard
> says is "successful" is NOT what most (almost all?) application programs in such
> environments want to treat as successful.

You are confusing a 'successful' file operation (as reported by file
status) with 'required by the program'.

> This is a "generalization" (general rule) that, unlike most that we discuss in
> this forum, I really do think is so close to universal that the difference in
…[6 more quoted lines elided]…
> then do so.  

You are confusing a 'successful' file operation (as reported by file
status) with 'required by the program'.

> The fact that there *ARE* other "0x" file status codes is important
> to realize; whether they should be treated as successful or not is NOT a
> universal condition and should be tailored to the specific needs of "your"
> application.

Having a test for "00" as successful is a bug trap. It may seem like a
simple and necessary change to the program to make the file OPEN I-O.
The site default configuration may then give a perfectly valid '05'
indicating that the OPEN statement was successful.

Clearly recognising that the file status reports success based on what
action the _statement_ requests should make more reliable programs.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-17T04:40:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com>`

```
You are confusing what the standard says with how programs are written.

A program is written to take certain actions for successful I/O and other 
actions for unsuccessful I/O.  What the Standard says is successful is NOT what 
the program is required to consider successful (and vice versa).

I have (not often, but on occasion) even seen cases where a program is trying to 
verify that a file does NOT exist.  Therefore, getting a "00" for an OPEN INPUT 
for that file is treated as UNSUCCESSFUL for that part of the program logic.

Clearly, this is a "terminology" issue.  When I am writing a program, I care 
about what are paths for successful (as far as my program goes) logic paths - 
while you care about the handling of what the standard defines as successful I/O 
all being "lumped" together (initially) and then divided by specific status 
code.

Would you be any happier if my original code had been something like:

 01  Rel-File-Status  Pic X(02).
      88  RFS-OK  Value "00".
      88  RFS-Not-OK Value "01" thru "09" "0A" thru "0Z" "0a" thru "0z".
      88  RFS-what-i-am-checking-for  Value "24".

and I still never check for RFS-Not-OK after an OPEN because I only wanted to 
process "00" as "OK" for this program?

   * * * *

P.S.  When Micro Focus has a compiler-option that "implies" OPTIONAL for files - 
even when this is not specified in the source code, this is an EXTENSION - just 
like "NOTRUNC" is an extension for them - or CBLQDA(OFF) is an extension for IBM 
mainframes.  MF also has (had?) directives to use '74 rather than '85 status 
values?  Is that relevant to this discussion too?
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-17T13:20:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b825455a-dc93-4339-8da6-54dea6e187bd@g22g2000pra.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com> <MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com>`

```
On May 17, 9:40 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> You are confusing what the standard says with how programs are written.
>

No, I am not. The file status is a specific item that is indicating
particular things about the results of a single file statement. It is
this statement (OPEN, WRITE, etc) that it is reporting 'success' on.

It neither knows nor cares what the program does with that
information.


> A program is written to take certain actions for successful I/O and other
> actions for unsuccessful I/O.

You are correctly using 'success' here, but your program is not
detecting all possible forms of 'success'.

What I am saying is that using '00' is incorrect for detecting
'success'. This may be a bug-trap if the program is modified or used
as a template for another.

In particular it is often that the file status and its values are held
in a copybook to save retyping, or to follow site requirements (such
as having '97' as 'success'.

> What the Standard says is successful is NOT what
> the program is required to consider successful (and vice versa).
>

And here you are using 'success' to mean (in the context of file
status) something completely different. Conjoining these leads to
ambiguities in the program, confusion in 'the next programmer' and bug
traps.

In any case, checking the file status _correctly_ makes zero
difference to whatever your program does with the information
provided.

Regardless of whether your program treats 'success' as 'what I wanted'
or as 'what I didn't want' it is still preferable to know that it
really is 'success' or not rather than "'success' except sometimes it
is but I didn't know that".


> I have (not often, but on occasion) even seen cases where a program is trying to
> verify that a file does NOT exist.  Therefore, getting a "00" for an OPEN INPUT
> for that file is treated as UNSUCCESSFUL for that part of the program logic.
>

The file status is indicating 'success' of the file statement (OPEN)
and neither knows nor cares whether the program treats this result as
'what I want' or 'what I don't want'.

You are conflating two means of success and causing ambiguity and
confusion which may mislead 'the next programmer'.

I would also point out that getting some other '0x' code should also
be treated the same as '00'. Regardless of whether you have ever seen
another '0x', or even whether it would not occur in the current
system, there is no loss in checking the first byte for '0'.

> Clearly, this is a "terminology" issue.  When I am writing a program, I care
> about what are paths for successful (as far as my program goes) logic paths -
> while you care about the handling of what the standard defines as successful I/O
> all being "lumped" together (initially) and then divided by specific status
> code.

Exactly. You are confusing "file status success" for your program
logic.


> Would you be any happier if my original code had been something like:
>
…[6 more quoted lines elided]…
> process "00" as "OK" for this program?

What have you got against the other 'success' codes ?


>    * * * *
>
…[5 more quoted lines elided]…
>

ANS'74 also defined the first byte being '0' as 'success' regardless
of any value in the second byte.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-17T21:50:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g24Ql.251739$5Z3.100499@en-nntp-05.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com> <MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com> <b825455a-dc93-4339-8da6-54dea6e187bd@g22g2000pra.googlegroups.com>`

```
(were back to no ">" on replies to Richard - but not to other people), so I will 
top post and respond to one particular par there, Concerning

"Regardless of whether your program treats 'success' as 'what I wanted'
or as 'what I didn't want' it is still preferable to know that it
really is 'success' or not rather than "'success' except sometimes it
is but I didn't know that"."

and

> Would you be any happier if my original code had been something like:
>
…[6 more quoted lines elided]…
> process "00" as "OK" for this program?

What have you got against the other 'success' codes ?

 * * * * *

This is the CRUX of the mater.  To me (and yes, to me this is a "best practice 
rule").  The program logic should "lump together" the processing of tile status 
based on what the program logic "wants to do".

Consider my specific small test program.  I really do NOT want to treat "05" the 
same as "00".  I want to treat it as something where I want to skip the rest of 
the logic of the program and just "let the program end reporting a non-zero 
status value".

If, however, anyone DOES (eventually) test my program with Enterprise COBOL, I 
would hope that they would place "97" with "00" - as I would want the logic to 
work the same for both of these (for an RRDS file).

My original program used "RFS-OK" as the 88-level name and that describes "00" 
(not "05") exactly.  It means that the OPEN (only place this 88-level was used) 
was OK for the continued processing of the program as written.  If ANY other 
file status "05" "9q" or whatever were to occur, then I wanted the program to 
jump immediately to the "bad open for this program" logic.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-17T21:22:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a29e387-2d60-4253-b864-f3d2b579c169@a5g2000pre.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com> <MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com> <b825455a-dc93-4339-8da6-54dea6e187bd@g22g2000pra.googlegroups.com> <g24Ql.251739$5Z3.100499@en-nntp-05.dc1.easynews.com>`

```
On May 18, 2:50 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:

>
> This is the CRUX of the mater.  To me (and yes, to me this is a "best practice
> rule").  

What I entirely disagree with is that this is 'best practice'.

> The program logic should "lump together" the processing of tile status
> based on what the program logic "wants to do".
…[4 more quoted lines elided]…
> status value".

I disagree that is 'best practice'. If you want to specifically ignore
'success' then 'best practice' would make this explicit.

Otherwise 'the next programmer' could be confused about why the
program did not work.


> If, however, anyone DOES (eventually) test my program with Enterprise COBOL, I
> would hope that they would place "97" with "00" - as I would want the logic to
…[6 more quoted lines elided]…
> jump immediately to the "bad open for this program" logic.

Sounds like post-hoc justification to me.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-17T23:58:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FV5Ql.372013$PS5.120365@en-nntp-07.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com> <MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com> <b825455a-dc93-4339-8da6-54dea6e187bd@g22g2000pra.googlegroups.com> <g24Ql.251739$5Z3.100499@en-nntp-05.dc1.easynews.com> <5a29e387-2d60-4253-b864-f3d2b579c169@a5g2000pre.googlegroups.com>`

```
This was not "post hoc justification" - this is the way that I have (always/) 
coded.  I do file status checking for what I want my program to do AFTER an I/O 
statement.  If the value is one of those that I have coded for, then I expect 
the processing to continue for that condition.  If the returned file status is 
NOT something that I have explicitly coded for in my "main processing", then I 
want to go to the "all other processing" logic.

The only change to the original code that I would make (after all of this 
discussion) is that I would change,

"           05  Rel-FS  Pic X(02).
               88  RFS-OK   Value "00".
               88  RFS-24   Value "24".
"
to
"           05  Rel-FS  Pic X(02).
               88  RFS-OK   Value "00"
    *          add file status "97" to this if using IBM mainframe COBOL
                    .
               88  RFS-24   Value "24".
"

This program was "designed" to go to "not handled" or "other" logic when any 
file status other than those 2 (or 3) values occurred.

 * * * * * *

I shouldn't actually say the only change.  After I sent the original note, I 
realized that I had left the relative file as "variable length" which added a 
complexity that wasn't really needed for what I wanted tested.

So far, only Richard has actually run the original test program (with Fujitsu) 
and I am still interested in what other compilers do with it.
```

###### ↳ ↳ ↳ Re: Succesful Status code - Relative File status when writing RRN=0

_(reply depth: 12)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2009-05-19T03:20:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ApQl.249090$4m1.64030@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<FV5Ql.372013$PS5.120365@en-nntp-07.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com> <MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com> <b825455a-dc93-4339-8da6-54dea6e187bd@g22g2000pra.googlegroups.com> <g24Ql.251739$5Z3.100499@en-nntp-05.dc1.easynews.com> <5a29e387-2d60-4253-b864-f3d2b579c169@a5g2000pre.googlegroups.com> <FV5Ql.372013$PS5.120365@en-nntp-07.dc1.easynews.com>`

```
William M. Klein wrote:
> This was not "post hoc justification" - this is the way that I have (always/) 
> coded.  I do file status checking for what I want my program to do AFTER an I/O 
…[31 more quoted lines elided]…
> 

Bill,

I finally got around to running this:

********************************* TOP OF DATA ******
PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1
Invocation parameters:
XREF(FULL),NORENT,X(FULL)
Options in effect:
     NOADATA
       ADV
       APOST
       ARITH(EXTEND)
       AWO
       BUFSIZE(27998)
     NOCICS
       CODEPAGE(1140)
     NOCOMPILE(E)
     NOCURRENCY
       DATA(31)
     NODATEPROC
     NODBCS
     NODECK
       DIAGTRUNC
     NODLL
     NODUMP
       DYNAM
     NOEXIT
     NOEXPORTALL
       FASTSRT
       FLAG(I,W)
     NOFLAGSTD
       INTDATE(LILIAN)
       LANGUAGE(EN)
       LIB
       LINECOUNT(60)
     NOLIST
       MAP
     NOMDECK
     NONAME
       NSYMBOL(DBCS)
     NONUMBER
       NUMPROC(NOPFD)
       OBJECT
       OFFSET
       OPTIMIZE(FULL)
       OUTDD(SYSOUT)
       PGMNAME(COMPAT)
     NORENT
       RMODE(ANY)
     NOSEQUENCE
       SIZE(MAX)
       SOURCE
       SPACE(1)
     NOSQL
       SQLCCSID
     NOSSRANGE
       TERM
     NOTEST
     NOTHREAD
       TRUNC(OPT)
     NOVBREF
     NOWORD
PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1
* Statistics for COBOL program RELFS:
*    Source records = 52
*    Data Division statements = 9
*    Procedure Division statements = 13
End of compilation 1,  program RELFS,  no statements flagged.
Return code 0
******************************** BOTTOM OF DATA **********************

  SDSF OUTPUT DISPLAY XXXXXXXXT JOB00510  DSID 101 LINE 0 OLUMNS 02- 81
  COMMAND INPUT ===>                                   SCROLL ===> PAGE
********************************* TOP OF DATA ************************
Test Passes, FS=24
******************************** BOTTOM OF DATA **********************
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 11)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-05-18T15:05:20-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pt7315pp5urnn5j5at4q7s3pcri1kv3t7q@4ax.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com> <MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com> <b825455a-dc93-4339-8da6-54dea6e187bd@g22g2000pra.googlegroups.com> <g24Ql.251739$5Z3.100499@en-nntp-05.dc1.easynews.com> <5a29e387-2d60-4253-b864-f3d2b579c169@a5g2000pre.googlegroups.com>`

```
On Sun, 17 May 2009 21:22:07 -0700 (PDT), riplin@Azonic.co.nz wrote:

>On May 18, 2:50ï¿½pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
>wrote:
…[20 more quoted lines elided]…
>

Success means that the I-O request completed and opened the file or
read the record or otherwise was able to honor the request.  The
non-zero second byte could indicate things have gone wrong and some
exception action should be taken depending on the system.  I had
rarely if ever run into the 0X status code in the 30 years that I had
been coding programs that checked status code.  Since most of the time
the programs would shut down with an unknown error code, this would
have come to my attention on the support side.  This was in an IBM
environment where normally only VSAM files had status codes.  In what
cases have people seen 0X codes other than 00?   
>
>> If, however, anyone DOES (eventually) test my program with Enterprise COBOL, I
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-18T13:37:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8%hQl.291402$Za7.196706@en-nntp-08.dc1.easynews.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com> <MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com> <b825455a-dc93-4339-8da6-54dea6e187bd@g22g2000pra.googlegroups.com> <g24Ql.251739$5Z3.100499@en-nntp-05.dc1.easynews.com> <5a29e387-2d60-4253-b864-f3d2b579c169@a5g2000pre.googlegroups.com> <pt7315pp5urnn5j5at4q7s3pcri1kv3t7q@4ax.com>`

```
The most common  non-"00" code that you might get on an OPEN; is "05" if you 
have used an "OPTIONAL" phrase in the Select/Assign clause *and* the file wasn't 
actually present.

For those from the IBM (LE) mainframe environment, this gets into the wonderful 
world of CBLQDA(ON) - where files are "created" when there isn't a JCL DD for 
them.  This is such a *HATED* (but required by the Standard) behavavior, that I 
findi it pretty unlikely that any IBM mainframe person has ever seen a test for 
this.  For OPEN INPUT, the OPEN is considered successful (ANSI definition) but 
the first read gets an "at end" condition.  Again, not a behavior that I think 
many IBM mainframe shops would want.

Bottom-Line:
  If you don't code the OPTIONAL phrase (or as Micro Focus has - have an 
extension that lets you make this the defaul), then you won't ever see any "0x" 
file status code on an OPEN (unless/unitl some vendor creates an implementer 
defined "0x" value - that I don't think any have yet)

  *  * * * *

Actually a LITTLE more likely to be in IBM mainframe code is a test for "07". 
It is defined as:
  "The input-output statement is successfully executed but a CLOSE statement 
with the NO REWIND, REEL/UNIT, or FOR REMOVAL phrase or for an OPEN statement 
with the NO REWIND phrase references a physical file on a non-reel/unit medium"

I think that there were programs that used to use "NO REWIND" for tape files - 
but when they converted such files to DASD, this status could occur.  The 
chances were that they PROBABLY wanted the program to "continue" after such an 
OPEN, but this may depend upon WHY they had the "NO REWIND" phrase in the first 
place.  I haven't seen that prhase in years, but it probably does still exist in 
some legacy code.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-18T12:23:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<24e207e8-9cce-48cd-9397-f437e8c73ada@v35g2000pro.googlegroups.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <9aab7cdd-4c05-4c1c-8016-9d3caff42e8f@w31g2000prd.googlegroups.com> <MYQPl.68124$iW4.62210@en-nntp-01.dc1.easynews.com> <b825455a-dc93-4339-8da6-54dea6e187bd@g22g2000pra.googlegroups.com> <g24Ql.251739$5Z3.100499@en-nntp-05.dc1.easynews.com> <5a29e387-2d60-4253-b864-f3d2b579c169@a5g2000pre.googlegroups.com> <pt7315pp5urnn5j5at4q7s3pcri1kv3t7q@4ax.com>`

```
On May 19, 6:05 am, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> On Sun, 17 May 2009 21:22:07 -0700 (PDT), rip...@Azonic.co.nz wrote:
> >On May 18, 2:50 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
…[5 more quoted lines elided]…
> exception action should be taken depending on the system.

No. A '0x' file status is not 'wrong'. For example you will only
byte2='2', duplicate key, if the file has 'duplicates allowed'
otherwise you would get a '22' status (which does indicate 'wrong').


>  I had
> rarely if ever run into the 0X status code in the 30 years that I had
…[4 more quoted lines elided]…
> cases have people seen 0X codes other than 00?  

I get them frequently because I use 'duplicates allowed' and optional
files (so they create automatically as required).
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-18T19:51:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<guse7r$i2v$1@reader1.panix.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <5a29e387-2d60-4253-b864-f3d2b579c169@a5g2000pre.googlegroups.com> <pt7315pp5urnn5j5at4q7s3pcri1kv3t7q@4ax.com> <24e207e8-9cce-48cd-9397-f437e8c73ada@v35g2000pro.googlegroups.com>`

```
In article <24e207e8-9cce-48cd-9397-f437e8c73ada@v35g2000pro.googlegroups.com>,
 <riplin@Azonic.co.nz> wrote:

[snip]

>No. A '0x' file status is not 'wrong'. For example you will only
>byte2='2', duplicate key, if the file has 'duplicates allowed'
>otherwise you would get a '22' status (which does indicate 'wrong').

Depends on the context.  If I'm writing a rec a 22 means the primary key 
already exists, that's neither necessarily right or wrong.  Without 
making any fancy 88s for the example:

WRITE CUSTMAST FROM WK-REC
    INVALID KEY
        IF CUSTMAST-FILSTAT = '22'
            REWRITE CUSTMAST FROM WK-REC

...etc.

Not right, not wrong... just what is happening.

DD
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-18T15:30:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<067d11f8-5e26-40c5-9383-d5272a8f4863@w35g2000prg.googlegroups.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <5a29e387-2d60-4253-b864-f3d2b579c169@a5g2000pre.googlegroups.com> <pt7315pp5urnn5j5at4q7s3pcri1kv3t7q@4ax.com> <24e207e8-9cce-48cd-9397-f437e8c73ada@v35g2000pro.googlegroups.com> <guse7r$i2v$1@reader1.panix.com>`

```
On May 19, 7:51 am, docdw...@panix.com () wrote:
> In article <24e207e8-9cce-48cd-9397-f437e8c73...@v35g2000pro.googlegroups.com>,
>
…[19 more quoted lines elided]…
> Not right, not wrong... just what is happening.

A '22' means that the record was not written. An '02' means that the
record was written.

I would not have the code that you have written above in my system and
would consider it to be wrong. For creating a new record I always READ
the primary key first so that I know whether it is an update (REWRITE)
or an insert (WRITE). If the WRITE then fails on a '22' it is because
some other user has intervened and created the record between my READ
(which was unsuccessful) and the WRITE. Overwriting with the REWRITE
would then be wrong.

I am surprised that you think that overwriting some record is
acceptable, it would destroy data.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-19T14:30:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<guufp8$ee9$1@reader1.panix.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <24e207e8-9cce-48cd-9397-f437e8c73ada@v35g2000pro.googlegroups.com> <guse7r$i2v$1@reader1.panix.com> <067d11f8-5e26-40c5-9383-d5272a8f4863@w35g2000prg.googlegroups.com>`

```
In article <067d11f8-5e26-40c5-9383-d5272a8f4863@w35g2000prg.googlegroups.com>,
 <riplin@Azonic.co.nz> wrote:
>On May 19, 7:51?am, docdw...@panix.com () wrote:
>> In article
…[23 more quoted lines elided]…
>A '22' means that the record was not written.

According to 
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/6.2.40.3?SHELF=&DT=20020920180651&CASE=&FS=TRUE>

--begin quoted text:

When an invalid key condition occurs: 

If the INVALID KEY phrase is specified, imperative-statement-1 is 
executed. (See Table 34 in topic 6.1.8.9.1). 

Otherwise, the WRITE statement is unsuccessful and the contents of 
record-name are unaffected (except for QSAM files). 

--end quoted text:

I assume that your statement of 'A '22' means that the record was not 
written' was intended to agree with the manual's '... the WRITE statement 
is unsuccessful'.

>An '02' means that the
>record was written.

According to 
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/6.1.8.9.1?DT=20020920180651&FS=TRUE&ScrollTOP=TBLKEYVAL#TBLKEYVAL>

A high-order digit of '0' has a Meaning of 'Successful Completion'.  Of 
the five possible low-order digits (0, 2, 4, 5, 7) only 2 is specified for 
an input-putput operation.  A WRITE is a subset of an input-output 
operation... but that those are extraneous data.  The syllogism which 
results is:

A high-order digit of the Status Key is defined as having a Meaning of 
'Successful Completion' of the attempted I-O operation.

The Status Key '02' has a high-order digit of '0'.

The Status Key of '02' is defined as having a Meaning of 'Successful 
Completion' of the attempted I-o operation.

Quod erat demonstrandum.

>
>I would not have the code that you have written above in my system and
>would consider it to be wrong.

Were you to consider it to be incorrect, Mr Plinston, you appear would be 
at odds with the manual.

>For creating a new record I always READ
>the primary key first so that I know whether it is an update (REWRITE)
…[3 more quoted lines elided]…
>would then be wrong.

When creating a new record on a multi-user system I build the record in 
WORKING-STORAGE and then wait for the operator to press the key which 
signals a WRITE is to be performed.  I then READ based on the key and make 
decisions based on the kind of system, transaction flow and how the users 
have specified they want updates of existing records handled... you know, 
do what *they* want, not what I Know Is Best For Them.

>I am surprised that you think that overwriting some record is
>acceptable, it would destroy data.

I am surprised that your experience seems not to have included updating 
widgets-on-hand or seats-available-on-a-flight data, which change 
constantly and, thus, are subject to constant destruction-and-re-creation.

Different situations, Mr Plinston, require different solutions... what 
happens, at the machine level, when one encounters a DUPEKEY does (or, 
more precisely, should) not.

DD
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 16)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-19T12:09:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e08248e2-1a53-4eb4-bbad-ef2d24d1fed9@k19g2000prh.googlegroups.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <24e207e8-9cce-48cd-9397-f437e8c73ada@v35g2000pro.googlegroups.com> <guse7r$i2v$1@reader1.panix.com> <067d11f8-5e26-40c5-9383-d5272a8f4863@w35g2000prg.googlegroups.com> <guufp8$ee9$1@reader1.panix.com>`

```
On May 20, 2:30 am, docdw...@panix.com () wrote:
> In article <067d11f8-5e26-40c5-9383-d5272a8f4...@w35g2000prg.googlegroups.com>,

>
> >I would not have the code that you have written above in my system and
…[3 more quoted lines elided]…
> at odds with the manual.

I did not say that the statements or file status were 'incorrect' at
all.

What would be wrong, if that code were in _my_ system (please note the
qualification this time), is that after detecting that a record exists
with a WRITE statement you overwrite that record.

> >For creating a new record I always READ
> >the primary key first so that I know whether it is an update (REWRITE)
…[10 more quoted lines elided]…
> do what *they* want, not what I Know Is Best For Them.

That may be so in your systems, but not in mine. If a READ had
previously determined whether the record existed then it would be
known whether a WRITE or a REWRITE is required. If either of those
gives an unsucessful file status then there is a problem that needs to
be dealt with, and not by simply overwriting existing data.

> >I am surprised that you think that overwriting some record is
> >acceptable, it would destroy data.
…[4 more quoted lines elided]…
>

I am not sure how you determined what you think is my experience.

I gave an example of how a wrongness may occur, you appear to have
dismissed that situation. Perhaps your experience of multi-user shared
file systems is rather less than mine.


> Different situations, Mr Plinston, require different solutions... what
> happens, at the machine level, when one encounters a DUPEKEY does (or,
> more precisely, should) not.

Which is why my comments were qualified to be my systems. If you had
noticed that then you may have been less tedious in your response.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 17)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-19T19:33:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<guv1ij$nf6$1@reader1.panix.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <067d11f8-5e26-40c5-9383-d5272a8f4863@w35g2000prg.googlegroups.com> <guufp8$ee9$1@reader1.panix.com> <e08248e2-1a53-4eb4-bbad-ef2d24d1fed9@k19g2000prh.googlegroups.com>`

```
In article <e08248e2-1a53-4eb4-bbad-ef2d24d1fed9@k19g2000prh.googlegroups.com>,
 <riplin@Azonic.co.nz> wrote:
>On May 20, 2:30?am, docdw...@panix.com () wrote:
>> In article
…[10 more quoted lines elided]…
>all.

That is not what I stated, Mr Plinston, as the initial use of the 
subjunctive mood ('Were you to... ') was intended to indicate.  My 
apologies for my lack of clarity.

>
>What would be wrong, if that code were in _my_ system (please note the
>qualification this time), is that after detecting that a record exists
>with a WRITE statement you overwrite that record.

What seems to be wrong, Mr Plinston, is that you appear to be 
extrapolating from a simple, common example to a series of specifics which 
were not specified nor addressed.  If one wishes to go from the dermis to 
the bone it is best to address the intervening layers specifically, as 
they vary from one portion of the anatomy to the next, just as going from 
a simple example to the more complex may vary from one kind of system to 
the next.

>
>> >For creating a new record I always READ
…[13 more quoted lines elided]…
>That may be so in your systems, but not in mine.

I'll try to keep that in mind when you are signing my paychecks, Mr 
Plinston.  Until then, I do what *they* (the signers of my paychecks) want 
(as long as I do not feel it compromises my professional integrity).

I do not own systems, Mr Plinston; what I code is paid for by others... 
and - up to a point - they call the tune.

>If a READ had
>previously determined whether the record existed then it would be
>known whether a WRITE or a REWRITE is required.

Only at the time of the READ, Mr Plinston... have you ever worked on a 
multi-user system where a data-entry clerk READ a record, made some 
updates... and then went to lunch for a half-hour?  What I showed was a 
way of dealing with such a situation

>If either of those
>gives an unsucessful file status then there is a problem that needs to
>be dealt with, and not by simply overwriting existing data.

Perhaps it is because a different data entry clerk created, altered or 
deleted the record in the interim... a lot of things happen during 
lunches, or so I have seen.

>
>> >I am surprised that you think that overwriting some record is
…[7 more quoted lines elided]…
>I am not sure how you determined what you think is my experience.

Any one of a variety of ways... a Muse descended upon me, I was seized by 
a Spirit of Malice, a little birdie whispered in my ear... or something 
just smelled like something else I had seen.

>
>I gave an example of how a wrongness may occur, you appear to have
>dismissed that situation. Perhaps your experience of multi-user shared
>file systems is rather less than mine.

You gave an example, Mr Plinston, and I responded to it in a manner which 
appears to have given you cause to think.  I conclude that you had thought 
because you wrote.  If you were writing without thinking then... well, 
perhaps that is a path best left untrodden.

>
>
…[5 more quoted lines elided]…
>noticed that then you may have been less tedious in your response.

I cannot apologise for being tedious, Mr Plinston, as I have no idea how 
short your attention span for things beyond what constitute Your Systems 
(caps intended) might be.  

If others may have learned something from what I posted then they may have 
learned how such matters might be dealt with outside of Your Systems (caps 
intended).  It is a wide, wonderful world out there, Mr Plinston... and I 
try to add to it.

DD
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-19T14:34:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62cedc77-83a3-4ee7-a5b9-6e734a929d89@x1g2000prh.googlegroups.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <067d11f8-5e26-40c5-9383-d5272a8f4863@w35g2000prg.googlegroups.com> <guufp8$ee9$1@reader1.panix.com> <e08248e2-1a53-4eb4-bbad-ef2d24d1fed9@k19g2000prh.googlegroups.com> <guv1ij$nf6$1@reader1.panix.com>`

```
On May 20, 7:33 am, docdw...@panix.com () wrote:
> In article <e08248e2-1a53-4eb4-bbad-ef2d24d1f...@k19g2000prh.googlegroups.com>,
>
…[16 more quoted lines elided]…
> apologies for my lack of clarity.

So your conclusion that I would be "at odds with the manual" was based
on what I may say, rather than anything that I did actually say.


> >What would be wrong, if that code were in _my_ system (please note the
> >qualification this time), is that after detecting that a record exists
…[8 more quoted lines elided]…
> the next.

I made no comment about what may be right or wrong in the systems that
you worked on, but only that the code as written would be wrong in any
of the systems that I own or have worked on.


> >> >For creating a new record I always READ
> >> >the primary key first so that I know whether it is an update (REWRITE)
…[28 more quoted lines elided]…
> way of dealing with such a situation

It may be _a_ way, but not one that I, or my users, would find
acceptable.

> >If either of those
> >gives an unsucessful file status then there is a problem that needs to
…[4 more quoted lines elided]…
> lunches, or so I have seen.

That may well be, but the snippet of code in the situation you have
described would simply destroy the data that the other clerk had
created or amended.

There may be two situations if the record has been read initially: it
exists or it does not. Hopefully a reasonable system will be able to
lock the record to prevent changes in the interim.

The data items are amended or created as appropriate. If the record
did not exist then a WRITE should be used, if it fails then an error
should be reported as it has been created between the READ and the
WRITE. Or at the very least the record should be READ and the
amendments applied to the existing data before the REWRITE.

If the record did exist then a REWRITE (without the WRITE) should be
used to update the data. A 'with lock' on the READ would ensure that
no changes (or DELETE) to the record intervened.

Doing a WRITE after a READ WITH LOCK (or similar) could release the
lock. This would potentially allow another user to obtain a lock on
that record making the REWRITE fail, or could allow the other user to
LOCK and REWRITE before your REWRITE leading to data loss.


> >> >I am surprised that you think that overwriting some record is
> >> >acceptable, it would destroy data.
…[9 more quoted lines elided]…
> just smelled like something else I had seen.

Those would account for its accuracy, or lack thereof.


> >I gave an example of how a wrongness may occur, you appear to have
> >dismissed that situation. Perhaps your experience of multi-user shared
…[23 more quoted lines elided]…
> try to add to it.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 19)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-20T18:54:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gv1jkh$l10$1@reader1.panix.com>`
- **References:** `<8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <e08248e2-1a53-4eb4-bbad-ef2d24d1fed9@k19g2000prh.googlegroups.com> <guv1ij$nf6$1@reader1.panix.com> <62cedc77-83a3-4ee7-a5b9-6e734a929d89@x1g2000prh.googlegroups.com>`

```
In article <62cedc77-83a3-4ee7-a5b9-6e734a929d89@x1g2000prh.googlegroups.com>,
 <riplin@Azonic.co.nz> wrote:
>On May 20, 7:33?am, docdw...@panix.com () wrote:
>> In article
…[21 more quoted lines elided]…
>on what I may say, rather than anything that I did actually say.

Mr Plinston, I used the subjunctive and apologised if that caused a lack 
of clarity.  If you need instruction as to the use of the subjunctive I'd 
suggest you look elsewhere.

>
>
…[14 more quoted lines elided]…
>of the systems that I own or have worked on.

Mr Plinston, I know of nobody who has unlimited experience in all systems; 
if you are such a person then a lack in my experience might seem to be 
remedied.

[snip]

>> >If a READ had
>> >previously determined whether the record existed then it would be
…[8 more quoted lines elided]…
>acceptable.

That you or your users do not sign the paychecks which indicate 
satisfaction with that way, Mr Plinston - others have, you know - in no 
wise lessens it as '_a_ (emphasis original) way'.

>
>> >If either of those
…[9 more quoted lines elided]…
>created or amended.

That might just be one of the many reasons for not judging a full system 
by a code snippet, Mr Plinston.  This might be a valuable lesson.

>
>There may be two situations if the record has been read initially: it
>exists or it does not. Hopefully a reasonable system will be able to
>lock the record to prevent changes in the interim.

There may be many things, Mr Plinston... this is why textbooks have many 
chapters.  If you expect all situations in all dialects to be covered in 
each and every posting you might find yourself disappointed.

LOCKing might be a subject for one of the other chapters.

[snip]

>> >I am not sure how you determined what you think is my experience.
>>
…[4 more quoted lines elided]…
>Those would account for its accuracy, or lack thereof.

And others might account for other accuracies, Mr Plinston... what is 
obvious to one can be incomprehensible to others.

>> >I gave an example of how a wrongness may occur, you appear to have
>> >dismissed that situation. Perhaps your experience of multi-user shared
…[5 more quoted lines elided]…
>> perhaps that is a path best left untrodden.

Such as... what is shown above.  If examples which give you cause to think 
are not to your liking then... you've been posting to UseNet long enough 
to, perhaps, have been able to generate a solution.

DD
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-17T23:48:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77absvF1gaqhkU1@mid.individual.net>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com>`

```
William M. Klein wrote:
> You can think what you want about what is "successful" and what is
> not.  To me, the term "successful" I/O means that FOR THIS PROGRAM,
…[76 more quoted lines elided]…
> code that apparently does not understand how Cobol works.

Hmmm... I watched this thread with interest, not being sure of my own 
position because I can't remember the last time I accesssed a file rather 
than a database.

It seems a pity that heat is being generated, and I do think that saying 
Bill Klein "apparently doesn't understand how COBOL works" is unnecessary 
and out of order, Richard. He's the last person anyone could say that 
about...

Still, Bill WAS emphatic about what he wrote and all of us need to be 
careful about what we call the BEST way to do ANYTHING...

For my money, (and I expect abuse from both of you :-)), it all seems to 
hinge on this word "success".

The standard says if the first digit is 0 that represents "success" (Richard 
pointed this out), but definitions of "success" can vary by program (Bill's 
position...)

If you define "success" as meaning that the I/O completed without anything 
disastrous enough to stop processing, IRRESPECTIVE of the program logic, 
then Richard and the standard have to be considered "correct".

But Bill's point that what may be OK for the Standard, and what may be OK 
for a specific piece of code, can differ... is also worth considering.

Let's not forget that the inclusion of a FS clause is a means of continuing, 
EVEN AFTER something disastrous HAS occurred. The language designers have 
given the programmer a "final say"...

("We cannot know how you intend to process so we'll let you carry on, even 
if no data was obtained, the Block Mux is fried, and the disk is on fire... 
Your call. By the way, you might need to know that something terrible 
happened (or it didn't), or you might just want to know that although your 
attempt wasn't perfect we mostly managed to get what you wanted, so we'll 
set these status bytes to indicate a "level" of "success". '00' means 
everything worked fine, God's in his Heaven, all's right with the World... 
'0x' means it was pretty much OK as far as we're concerned but we have to 
admit it wasn't "perfect"; we may have taken some additional action to 
ensure you got data, but the data transfer was "successful". Anything else, 
is bad news of varying degree...)

The problem arises because the FS is ALWAYS completely comprehensive, but we 
are usually not interested in ALL possible returns from it. As a result, 
many programmers only look at 'perfect' and forget that sometimes 'OK' would 
be adequate.

Also, on the occasions when we ARE interested in things other than 'perfect' 
we usually have program specific actions to carry out, so it makes it hard 
to write a general purpose "error action" module that will work under all 
circumstances, because the things it needs to do under certain circumstances 
will vary in different programs. ('Perfect' however, doesn't vary; if the 
return is good, we invariably want to continue. and if it isn't, we don't... 
That is why many programmers check '00', when they should in fact be 
checking '0x'...)

There would appear to be two options:

1. Only check the specific thngs you are interested in. (This seems to be 
efficient, but leads to many people only checking '00'... maybe they forget 
that 'OK' is (most times) OK...)

2. Devise a comprehensive error checking routine that covers all possible 
returns. (As Bill pointed out, you really can't do this because the 
circumstances and required actions vary in different programs.)

Given that the original intent of the Standard writers (as paraphrased 
above) is kept in mind, then it makes sense to check for both 'perfect' and 
'OK' as being equivalent, (if they are, and most of the time they will be), 
and 'BAD' as a separate failure case.

Given that '00' is a subset of '0x' it seems to me that checking the first 
digit for zero makes sense

If you check the first digit, it really isn't too hard to build a decision 
tree that can be used as a "constrained general purpose" error detection 
routine. Use an EVALUATE or nested IF and you can include "perfection" level 
easily as an extension of "OK" level.  Although it is a general purpose 
routine, it is constrained to only the things that crop up all the time, and 
not EVERY ONE of the possible FS returns.

There are around 40 possible FS returns. Compare this with ESQL where the 
SQLSTATE has over 400 possible values. You HAVE to check for only the ones 
you are specifically interested in and then use a "catch all" for the rest. 
(In OO programming you can catch an exception object which has properties 
you can show to a user, like the error code that was encountered and a text 
message explaining what it means...)

In the unlikely event that I would put down my LINQ chainsaw and go back to 
using a stone adze, I think I am persuaded to checking the first digit of 
the FS.

But I don't think it is important enough to get excited about... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 7)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2009-05-17T17:52:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<77absvF1gaqhkU1@mid.individual.net>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net>`

```
Pete Dashwood wrote:
> William M. Klein wrote:
>> (snip) 

Pete, I enjoyed your comments, which I thought were very reasonable.

These comments apply to batch programming with IBM Enterprise COBOL for 
z/OS.

I always define file status and check it for VSAM files only.  I never 
define file status or check it for QSAM.  Why?  Because the z/OS default 
behavior is good enough for me.  If a plain sequential file has an error 
on open, close, read, or write, the batch job terminates abnormally.  It 
is trivially easy to recover from backups and rerun, once the real 
problem is resolved.

I have never seen an open statement for a VSAM file that had a file 
status of "0x", where the first character was a zero and the second 
character was not a zero.  So checking for "00" or for only the first 
character begin zero would get the same result.  If I find that this 
behavior changes in the future, than I might change my error-handling 
approach.

I have been bit by the file status "97" situation, so I usually add code 
to allow "00" or "97" when opening a VSAM file.  If my batch COBOL 
program is forced to abend in a situation where I am in control, then my 
clean-up routine will attempt to close any VSAM files defined to the 
program.  I hope that will prevent a file status "97" for the next user.

As far as I can tell, "97" is an IBM extension, and "0x" is a non-IBM 
extension.  It won't kill me to make a few minor source code changes if 
a COBOL program is moved from one platform to another.

If a batch program has QSAM files, VSAM files, and DB2, the DB2 connect 
is always done after opening all the QSAM & VSAM files, for reasons that 
should be obvious.

I'm not saying this is the only way to do this in an IBM z/OS batch 
COBOL environment, or the best way, but it works pretty well for me.

Kind regards,
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-17T12:37:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b0ea7017-fcd1-4b40-b7fd-ed355e15e869@f28g2000pra.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net>`

```
On May 18, 5:52 am, Arnold Trembley <arnold.tremb...@worldnet.att.net>
wrote:
> Pete Dashwood wrote:
> > William M. Klein wrote:
…[26 more quoted lines elided]…
>

How many programmers check the file status after a CLOSE ?  In
principle it should return a file status of '0x' to indicate success,
but it could return a non-success indication if the file was not open,
or more importantly if there was an actual error on closing. For
example if the final block of writes failed in transferring to the
media.


> As far as I can tell, "97" is an IBM extension, and "0x" is a non-IBM
> extension.  

No. ANS'74 standard defines status byte 1 alone as being zero means
'successful completion'. It happens that in the case of '0' '74 does
not define additional information for 'successful' and '85 does.

I agree that '97' is an anomoly and an IBMism, it should be a '0x'
status but the standard does not allow implementations to add codes
except those with '9' in the first byte.

> It won't kill me to make a few minor source code changes if
> a COBOL program is moved from one platform to another.
…[10 more quoted lines elided]…
> --http://arnold.trembley.home.att.net/
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-17T14:29:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a5a6712-38c1-4d3d-9b04-28c4ef985e29@b7g2000pre.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net> <b0ea7017-fcd1-4b40-b7fd-ed355e15e869@f28g2000pra.googlegroups.com>`

```
On May 18, 7:37 am, rip...@Azonic.co.nz wrote:
> On May 18, 5:52 am, Arnold Trembley <arnold.tremb...@worldnet.att.net>
> wrote:
…[45 more quoted lines elided]…
>

I was actually wrong here. ANS'74 does define '02' as a file status
that indicates 'success with additional information' (for READ, WRITE
or REWRITE).
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-05-17T22:00:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb4Ql.305596$Yx2.3915@en-nntp-06.dc1.easynews.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net> <b0ea7017-fcd1-4b40-b7fd-ed355e15e869@f28g2000pra.googlegroups.com>`

```

<riplin@Azonic.co.nz> wrote in message 
news:b0ea7017-fcd1-4b40-b7fd-ed355e15e869@f28g2000pra.googlegroups.com...
On May 18, 5:52 am, Arnold Trembley <arnold.tremb...@worldnet.att.net>
wrote:
<much snippage>

Concering the statement,

"I agree that '97' is an anomoly and an IBMism, it should be a '0x'
status but the standard does not allow implementations to add codes
except those with '9' in the first byte."

Not true, "the Standard" (i.e. the only currently support3ed COBOL Standard, the 
(ANSI or) ISO 2002 Standard, explicitly added as a new feature "implementer 
defined 0x" values. There is an existing SHARE (IBM user group) enhancement 
request for IBM to provide an (optional) way of converting "97" to a "0x" value. 
Part of the problem here, is that IBM has (another) extension that allows the 
file status field to be defined as
  Pic  99
rather than
  Pic XX

This worked fine for the pre'02 Standard values, but doesn't work now.  (It 
would never have worked for some vendors, such as Micro Focus that used the 
second byte of "9x" values as a "binary' field with up to 255 possible values. 
However, this is not something that IBM ever did.)

  * * * *

The possibility of implementer-defined "0x" values, actually gets back to the 
original question.

If the implementor DOES include new "0x" values (that do not require a 
re-compile, but only a new run-time), then which is it MORE likely that 
applications would want:
 - to treat the new values with the "00" logic - (without any changes to source 
code)
          or
 - to treat the new values with "other than 00" values?

My guess (and this, too would be application specific) would be that if a 
program was written not knowing about new "0x" values, that they would want it 
to "fail" when a new run-time value occured.  This would allow the application 
"maintainer" to take PRO-ACTIVE steps to "deal" with the new value.  They may 
well end up "lumping it" with the existing "00" - or 00, 02, 05, values, but 
they may also decide that for this program the best place to "lump" this 
situation w ould be with "bad" (not UNSUCCESSFUL) values.
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-17T21:30:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29ec3228-9920-4b71-86fc-1100e9ea5979@a5g2000pre.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net> <b0ea7017-fcd1-4b40-b7fd-ed355e15e869@f28g2000pra.googlegroups.com> <eb4Ql.305596$Yx2.3915@en-nntp-06.dc1.easynews.com>`

```
On May 18, 3:00 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> <rip...@Azonic.co.nz> wrote in message
>
…[13 more quoted lines elided]…
> defined 0x" values.

You are quite correct and I was wrong. The 2002 standard _does_ allow
implementor '0x' values and this makes it even more necessary to only
test byte 1 as being '0' to indicate success (ie the file statement
working as coded).

I should have stated that "the standard _did*_ not allow
implementations to add codes ..." (*at the time '97' was added).
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-18T14:17:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77bup8F1giui6U1@mid.individual.net>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net>`

```
Arnold Trembley wrote:
> Pete Dashwood wrote:
>> William M. Klein wrote:
…[3 more quoted lines elided]…
>
Thanks Arnold.


> These comments apply to batch programming with IBM Enterprise COBOL
> for z/OS.
…[6 more quoted lines elided]…
> once the real problem is resolved.

That sounds sensible to me.

>
> I have never seen an open statement for a VSAM file that had a file
> status of "0x", where the first character was a zero and the second
> character was not a zero.  So checking for "00" or for only the first
> character begin zero would get the same result.

So it wouldn't hurt to check '0x' ?  :-)  (And it is one byte less to 
compare... :-))

> If I find that this
> behavior changes in the future, than I might change my error-handling
…[7 more quoted lines elided]…
> "97" for the next user.

Yes, I think that is pretty standard practice. It certainly WAS in the days 
when I was using VSAM.
>
> As far as I can tell, "97" is an IBM extension, and "0x" is a non-IBM
> extension.  It won't kill me to make a few minor source code changes
> if a COBOL program is moved from one platform to another.

But it would be better not to have to, wouldn't it?

Still, even if you DID implement error checking as "perfect", "OK", and 
"bad" you STILL can't generalise it for all situations, so you might as well 
continue doing what you are doing, and check specific codes on specific 
accesses. That is really the nub of this whole discussion.

For myself, I'd check '0x' (just for aesthetics, really...) but I accept it 
really makes no difference in your particular environment.

>
> If a batch program has QSAM files, VSAM files, and DB2, the DB2
…[5 more quoted lines elided]…
>

And has for generations of IBM mainframe programmers...

Pete.
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 8)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-05-19T16:53:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4A12E416.6F0F.0085.0@efirstbank.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net>`

```
>>> On 5/17/2009 at 11:52 AM, in message
<O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net>, Arnold
Trembley<arnold.trembley@worldnet.att.net> wrote:
> Pete Dashwood wrote:
>> William M. Klein wrote:
…[41 more quoted lines elided]…
> COBOL environment, or the best way, but it works pretty well for me.

I agree with this post.

:-)

I wish VSAM worked the same as QSAM in that the program abends if there is
an invalid file status.  If that were the case there would be a lot less
coding to handle error conditions when all I am going to do is force the
program to abend anyway.

I wouldn't call "0x" a non-IBM extension though.  It is standard Cobol, not
an extension.

Frank
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-20T15:06:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77hae6F1h7n4oU1@mid.individual.net>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net> <4A12E416.6F0F.0085.0@efirstbank.com>`

```
Frank Swarbrick wrote:
>>>> On 5/17/2009 at 11:52 AM, in message
> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net>, Arnold
…[57 more quoted lines elided]…
> there is an invalid file status.

While I have every sympathy with your position, Frank, I can't agree with 
it.

This is where you have to try and see it from the point of view of the 
compiler writer or Standards definer...

What do you do if there is an error? Well, you do the obvious things like 
tell the programmer, but then just blow his task away? Ouch! What if there 
is some inconceivable situation where it really SHOULDN'T be blown away? 
Suppose he needs a chance to clean up other related files? (this doesn't 
really happen with QSAM... these files are usually not used as Master files 
with linked relationships which require random access, like VSAM...).

But the real clincher is: "Whose responsibility is it for the run unit?" 
Obviously, it has to be the application programmer's, rather than the 
compiler writer's... So, you give him the last word and let him decide what 
he wants to do.

Most of the time (almost always, in fact) he will want to fold his tent and 
close up shop, but ONE day there will be that situation where he CANNOT do 
that and still retain data integrity.

If anything, I would say QSAM should work the way VSAM does. (But I 
understand why it doesn't... :-))


> If that were the case there would
> be a lot less coding to handle error conditions when all I am going
> to do is force the program to abend anyway.

And there would be much more wailing and gnashing of teeth from sites who 
use their own VSAM database and have linked relationships between 
datasets...
>
> I wouldn't call "0x" a non-IBM extension though.  It is standard
> Cobol, not an extension.

Yep. Just as long as someone implements it... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Succesful Status code

_(reply depth: 10)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-05-20T10:49:24-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e728151q8rrivkb6tht02j4iejqiqivuas@4ax.com>`
- **References:** `<QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <O9YPl.241864$4m1.211611@bgtnsc05-news.ops.worldnet.att.net> <4A12E416.6F0F.0085.0@efirstbank.com> <77hae6F1h7n4oU1@mid.individual.net>`

```
On Wed, 20 May 2009 15:06:58 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Frank Swarbrick wrote:
>>>>> On 5/17/2009 at 11:52 AM, in message
…[71 more quoted lines elided]…
>with linked relationships which require random access, like VSAM...).

Take a look at the defaults for VSAM when status code is not
specified.  Would they be adequate if READ/WRITE/REWRITE/START INVALID
KEY ware used.  You can do QSAM using status code and I had an
application where it was necessary.  
>
>But the real clincher is: "Whose responsibility is it for the run unit?" 
…[25 more quoted lines elided]…
>Pete.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-17T14:57:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d5de46a6-dc99-4fe9-8928-3842e5358f6c@j9g2000prh.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net>`

```
On May 17, 11:48 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> > A first byte of zero indicates that the action of the statement has
> > been completed successfully. If you want some successful results to be
…[10 more quoted lines elided]…
> about...

I have no problem with being criticised for what I actually wrote, but
I do object to being criticised for other's misreadings.

I did not say that Bill did not understand Cobol, I said that the code
"apparently does not understand how Cobol works".


> Still, Bill WAS emphatic about what he wrote and all of us need to be
> careful about what we call the BEST way to do ANYTHING...
…[11 more quoted lines elided]…
>

Exactly. For a file status there is only one meaning of 'success': the
file operation statement completed what it was asked to do.


> But Bill's point that what may be OK for the Standard, and what may be OK
> for a specific piece of code, can differ... is also worth considering.
…[13 more quoted lines elided]…
> admit it wasn't "perfect";

'Success' is success. The file system was asked to do something and it
completed its task perfectly.

The additional information does not imply 'imperfection'.

For example on a READ an '02' indicates that another record exists
with a duplicate key. Successive sequential reads along that key will
continue indicating '02' until the last of that duplicate key value is
found when it returns a '00'. Thus the number of records with that key
value can be counted or in other ways processed.

If a WRITE returns an '02' it indicates that the write created a
duplicate key value. If this is a 'fault' then why does your SELECT
allow duplicates ?

Given that an '02' has written the record it would be wrong to treat
'02' as a 'failure'.

> we may have taken some additional action to
> ensure you got data, but the data transfer was "successful". Anything else,
> is bad news of varying degree...)
>

> The problem arises because the FS is ALWAYS completely comprehensive, but we
> are usually not interested in ALL possible returns from it. As a result,
…[52 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-18T14:03:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77btvdF1gu92dU1@mid.individual.net>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <d5de46a6-dc99-4fe9-8928-3842e5358f6c@j9g2000prh.googlegroups.com>`

```
riplin@Azonic.co.nz wrote:
> On May 17, 11:48 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[17 more quoted lines elided]…
>
Sounds like a lack of responsibility to me... "It wasn't me, Guv, it was 
those idiots who can't read properly..." :-)

> I did not say that Bill did not understand Cobol, I said that the code
> "apparently does not understand how Cobol works".

Bobbing and weaving.

Bill wrote the code.

As "the code" is not sentient, it could NEVER "understand how COBOL works". 
If you use the word "understand" you cannot be referring to something that 
has no capacity for that. Why not just accept that you were irritated when 
you wrote it and that affected what you said?

Most frequent posters here say something regrettable occasionally. (Not 
mentioning any names but just follow my eyes... Dashwood looks down and 
shuffles uncomfortably as the sound of a desert wind whistles softly and a 
tumbleweed rolls past...). Usually, accepting responsibility for it, is very 
helpful for everyone concerned.

>
>
…[18 more quoted lines elided]…
>


I don't think so. If there were "only one meaning of success" there would be 
only one file status for it. There is "success" and there is "qualified 
success". I chose to refer to them as "perfect" and "OK".

>
>> But Bill's point that what may be OK for the Standard, and what may
…[19 more quoted lines elided]…
> completed its task perfectly.

If that were the case, then there would be no need for any '0x' code, OTHER 
than '00'.

It didn't do it "perfectly" and that is the whole point of recognising that 
the transfer was "OK".

>
> The additional information does not imply 'imperfection'.
>
it does, within the context I defined for "imperfect".

> For example on a READ an '02' indicates that another record exists
> with a duplicate key. Successive sequential reads along that key will
> continue indicating '02' until the last of that duplicate key value is
> found when it returns a '00'. Thus the number of records with that key
> value can be counted or in other ways processed.

Sure, but the "imperfection" here is that here is "more". It wasn't just a 
simple "Get me this..."   "OK, I got it". It was "OK, I got it but there's 
more..."

>
> If a WRITE returns an '02' it indicates that the write created a
> duplicate key value. If this is a 'fault' then why does your SELECT
> allow duplicates ?

I think you have a very black and white concept of what is a 'fault'.  It 
ISN'T a 'fault'; it is an "imperfection" inasmuch as it is not a simply 
perfect execution. As noted above, there is more. It's not wrong, it is just 
not perfect either. (Remember, I'm using "imperfect" here to mean "not 
perfect"...)
>
> Given that an '02' has written the record it would be wrong to treat
> '02' as a 'failure'.

Exactly, but you shouldn't treat it as "perfect" either. There are times 
when you will want to know and there are other times when you don't want to 
know because you don't care. It depends on specific program contexts and 
cirumstances. That was the point that Bill was making.
>
>> we may have taken some additional action to
…[59 more quoted lines elided]…
>>
Pete.
```

###### ↳ ↳ ↳ Re: Succesful Status code (was: Request for testing of Reltive File status

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-05-17T21:00:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcdd4ae7-32ef-4f89-8632-e6b1dc272042@p6g2000pre.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com> <QmDPl.296067$Yx2.290693@en-nntp-06.dc1.easynews.com> <13af114a-68fb-4673-91c8-ede68237289d@g31g2000pra.googlegroups.com> <x%EPl.63845$iW4.17548@en-nntp-01.dc1.easynews.com> <8056df4a-6551-4b3a-9983-22feb0e020c1@y6g2000prf.googlegroups.com> <qELPl.300673$Yx2.222053@en-nntp-06.dc1.easynews.com> <77absvF1gaqhkU1@mid.individual.net> <d5de46a6-dc99-4fe9-8928-3842e5358f6c@j9g2000prh.googlegroups.com> <77btvdF1gu92dU1@mid.individual.net>`

```
On May 18, 2:03 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> rip...@Azonic.co.nz wrote:
> > On May 17, 11:48 pm, "Pete Dashwood"
…[32 more quoted lines elided]…
> you wrote it and that affected what you said?

Actually I very seldom get irritated by the content of the messages
and did not do so in this case, or in any in this thread, not even by
yours.

So, no, I will not 'admit' to something that is not true.

I was commenting on the code and not on the coder.

I do recall a self assessment review back in the late 60s where one
question had a set of answers where 'D' was 'Takes criticism of work
done as a personal affront'.

>
> Most frequent posters here say something regrettable occasionally. (Not
…[3 more quoted lines elided]…
> helpful for everyone concerned.

Your point being ?


> >> Still, Bill WAS emphatic about what he wrote and all of us need to be
> >> careful about what we call the BEST way to do ANYTHING...
…[19 more quoted lines elided]…
>

There is only one code for 'success', that being byte 1 with a value
of '0'.

Byte 2 does not 'qualify' the success at all, it adds additional
information.

> I chose to refer to them as "perfect" and "OK".
>

There is no such qualification, either the operation worked or it did
not. Either the file is OPEN or it is not OPEN. It is never
'imperfectly open' or 'partially open' or 'close enough'.

The additional information _adds_ to the status, it does not subtract
or reduce the 'success'.


> >> But Bill's point that what may be OK for the Standard, and what may
> >> be OK for a specific piece of code, can differ... is also worth
…[21 more quoted lines elided]…
> than '00'.

Then you misunderstand the information provided by a file status. Byte
2 is _additional_ information and not part of 'success'. Byte 2 does
not modify how successful the action has been.


> It didn't do it "perfectly" and that is the whole point of recognising that
> the transfer was "OK".

No. You are wrong. If Byte 1 is a '0' then the operation was completed
_perfectly_.

The file is OPEN, the record has been READ, the WRITE put every byte
to the media.


> > The additional information does not imply 'imperfection'.
>
> it does, within the context I defined for "imperfect".
>

The file status reports only in the context of a file operation
statement.


> > For example on a READ an '02' indicates that another record exists
> > with a duplicate key. Successive sequential reads along that key will
…[6 more quoted lines elided]…
> more..."

There is no 'imperfection'. If the test was done for Byte 1 being zero
then the indication is that the READ was 100% perfect, it was exactly
what was asked for, it was successful.

If you need to then you will use the additional information as
required.



> > If a WRITE returns an '02' it indicates that the write created a
> > duplicate key value. If this is a 'fault' then why does your SELECT
…[6 more quoted lines elided]…
> perfect"...)

In the case of a WRITE the result is 'perfect' if the bytes are
successfully transferred from the record buffer to the media. That is
indicated by byte 1 being '0'.

It is only a 'fault' or 'not perfect' if the WRITE does not result in
the bytes being on the media.

If you want to avoid an '02' status then do not have 'duplicates
allowed' in the select.


> > Given that an '02' has written the record it would be wrong to treat
> > '02' as a 'failure'.
…[5 more quoted lines elided]…
>

If you 'don't want to know' and only test success by the file status
having '00' after a WRITE then you may find that the program takes the
wrong action when an '02' (or other success) occurs.


> >> we may have taken some additional action to
> >> ensure you got data, but the data transfer was "successful".
…[60 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

#### ↳ Re: Request for testing of Reltive File status

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2009-05-18T19:57:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7d9e542-14a8-4337-935d-a08412b9bfd7@b6g2000pre.googlegroups.com>`
- **References:** `<GJ_Ol.55293$iW4.23123@en-nntp-01.dc1.easynews.com>`

```
On May 14, 1:58 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> I may have asked for this a while ago, but I am trying to find out what as many
> compilers/run-times do with this program as possible.  I am particularly
…[70 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

Here's what I get. Compiler is Compaq COBOL V2.8-1286.

==================================
   Welcome to OpenVMS (TM) Alpha Operating System, Version V8.3 on
node PWS600

$ sd [.cobol]
$ dire

Directory SYS$SYSDEVICE:[JLC.COBOL]

RELNAME.DAT;2       X.COB;6             X.EXE;1             X.LIS;2
X.OBJ;4

Total of 5 files.

$ run x
Invalid FS:23
$

==================================

HTH,

Jeff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
