[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol and VSAM I/O

_9 messages · 5 participants · 2009-08 → 2009-09_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Cobol and VSAM I/O

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-08-28T17:38:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4A9815F9.6F0F.0085.0@efirstbank.com>`

```
Enterprise Cobol for z/OS:

Can someone explain the following?  We have a Cobol program that as
incorrectly coded in that it has a VSAM file that does not have a FILE
STATUS clause.  Specifically, it looks like this:

SELECT OPTIONAL FFND-MTCE-FILE     
       ASSIGN TO AS-FFMNTFL.

In migrating this from VSE to z/OS we kept the Cobol as above but
accidentally created the file as QSAM.  (Mostly we're converting all ESDS
files to QSAM, but this and a few others are remaining as ESDS because they
are also defined to CICS.)

Anyway, when we ran the program it blew up:

IGZ0020S A logic error occurred.  Neither FILE STATUS nor a declarative was
specified for file FFMNTFL in program 
         FFND02 at relative location X'0CE8'.  The status code was 47.      
                                     
         From compile unit FFND02 at entry point FFND02 at statement 444 at
compile unit offset +00000CE8 at entry
         offset +00000CE8 at address 0F127CE8.                              
                                     

What I find puzzling is not that it blew up on the READ and not on the OPEN.
 I wouldn't expect the open to abend because (though I can't find the
documentation at the moment) VSAM files that do not have a FILE STATUS
phrase do not (in most cases, though apparently not all!) abend when there
is an I/O error.  So what makes this particular situation so different that
the read actually causes an abend, when in most other cases it would just
continue on it's merry way?

Personally I prefer the way QSAM is handled in that if there is an I/O error
and there is no FILE STATUS then the program does abend.  For instance:

IGZ0035S There was an unsuccessful OPEN or CLOSE of file FFMNTFL in program
FILETST1 at relative location X'03B2'.   
         Neither FILE STATUS nor an ERROR declarative were specified. The
status code was 96.                        
         From compile unit FILETST1 at entry point FILETST1 at statement 20
at compile unit offset +000003B2 at entry
         offset +000003B2 at address 0DC003B2.                              
                                        

I can't for the life of me figure out why they decided that VSAM files
shouldn't behave in this same manner.

Ah well, just another one of those things.  The least they could do is flag
as an error (or at least a warning) a VSAM file SELECT that does not have a
FILE STATUS clause.  That won't force you to check it, but at least it gives
you a hint that you might want to!  :-)

....a bit later....
I think I've sort of figured it out, though I can't say it makes much sense.
 According to the Cobol 2002 standard (I don't have the 1985 one): 
"Certain classes of I-O status values indicate fatal exception conditions.
These are: any that begin with the digit 3
or 4, and any that begin with the digit 9 that the implementor defines as
fatal. If the value of the I-O status for an
input-output operation indicates a fatal exception condition, the
implementor determines what action is taken after
the execution of any applicable USE EXCEPTION procedure, or if none applies,
after completion of the normal
input-output control system error processing. The implementor may either
continue or terminate the execution of
the run unit. If the implementor chooses to continue execution of the run
unit, control is transferred to the end of
the statement that produced the fatal exception condition unless the rules
for that statement define other behavior.
Any NOT AT END or NOT INVALID KEY phrase specified for that statement is
ignored."

In this case the VSAM file is getting a '37' on the open, and then the '47'
on the read.  (I know about the '37' only because I added a FILE STATUS
clause and ran it again.)  So perhaps IBM considers '3x' errors to be "fatal
but OK to continue" for VSAM and '4x' errors "fatal, abend".  Or something
like that.  Makes no sense to me.  Sounds like they can work either way and
still conform to the standard, though.

I wonder if it's worth submitting a requirement to have VSAM file act like
QSAM files when it comes to the lack of the FILE STATUS clause.  I
personally find coding to check for I/O errors tedious if I'm just going to
end up terminating the program anyway.  Might as well just let it abend
unless it's a condition that I expect and actually want to handle and
continue, rather than just terminating.  Those are rare cases, in my
experience.

Frank
```

#### ↳ Re: Cobol and VSAM I/O

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-08-28T18:27:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4A98218A.6F0F.0085.0@efirstbank.com>`
- **References:** `<4A9815F9.6F0F.0085.0@efirstbank.com>`

```
>>> On 8/28/2009 at 5:38 PM, in message
<4A9815F9.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick<Frank.Swarbrick@efirstbank.com> wrote:
> Enterprise Cobol for z/OS:
> 
…[6 more quoted lines elided]…
> 

I just realized the probably reason why FILE STATUS was not coded for this
file.  It's used as the input for an internal sort, ie:
SORT SORT-FILE                              
   ON ASCENDING KEY SORT-KEY                
   USING FFND-MTCE-FILE                     
   OUTPUT PROCEDURE 1000-MAINTENANCE-REPORT.

Since the program did, in fact, abend, I guess it's OK to leave it as is. 
But I do wonder what the "proper" way of error handling is for this
particular case.  Is the use of DECLARATIVES error procedures the only other
option?

Hmm, I just added this (after adding FILE STATUS IS FFND-MTCE-STATUS to the
SELECT):

 DECLARATIVES.                                         
                                                       
 FFND-MTCE-FILE-ERROR SECTION.                         
     USE AFTER ERROR PROCEDURE ON FFND-MTCE-FILE.      
 FFND-MTCE-FILE-ERR-START.                             
     DISPLAY 'ERROR ON FFND-MTCE-FILE' FFND-MTCE-STATUS
       UPON CONSOLE                                    
     GOBACK.                                           
                                                       
 END DECLARATIVES.                                     

And now I get this!

IGZ0012S There was an invalid attempt to end a sort or merge.               
                                      
         From compile unit FFND02 at entry point FFND02 at statement 457 at
compile unit offset +00000D02 at entry 
         offset +00000D02 at address 0F127D02.                              
                                      

What on earth is the proper way to handle this?

Frank
```

##### ↳ ↳ Re: Cobol and VSAM I/O

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-08-29T12:10:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1idmm.582098$op1.107961@en-nntp-05.dc1.easynews.com>`
- **References:** `<4A9815F9.6F0F.0085.0@efirstbank.com> <4A98218A.6F0F.0085.0@efirstbank.com>`

```
Frank (et al),
  There really are several issues here.  I have some comments (in no particular 
order):

NOTE:
   This is an IBM (z/OS specifically) "centric" note.  I am WELL aware different 
"answers" (issues) apply for COBOL elsewhere.

1) Be very careful using DECLARATIVES with (to detect problems) with files used 
with SORT (merge).  When FASTSRT is used (which I strongly recommend), it is 
specially documented that "non-conforming" behavior occurs.  What is 
non-conforming is that DECLARATIVES are "ignored".

2) As far as relying on (or even expecting) "ABENDs" with "unsuccessful" file 
I/O (when n0 declaratives or file status checking is done), this is NOT a good 
idea for QSAM or VSAM.  It is a LOT like relying on ABENDs for "S0C7" in the 
days of OS/VS COBOL and DOS/VS COBOL.  You are "relying" on the system to catch 
"bad data" for a case that the manual says "results are UNpredictable".  Like 
S0C7, you may THINK that the system will always catch such problems, but like 
S0C7, what is true today may well change in the future.  ESPECIALLY if you ever 
think that you might "port" your application to another O/S, this is a really, 
REALLY bad idea.  You should explicitly check file status codes after file I/O 
for VSAM *and* QSAM.

3) Having said what I did above, it is very unlikely (IMHO) that IBM would ever 
change the behavior of VSAM files "to behave like QSAM" files when bad file 
statuses occur - even if requested to and even if under the control of a 
compiler or run-time option.  Too many existing applications expect the current 
behavior for this to be intentionally changed.

4)  Like declaratives for SORTs, you should be aware that IBM only "guarantees" 
ANSI conforming behavior for QSAM sequential files and does NOT guarantee such 
for ESDS VSAM files.  (I can't remember where the problems are for these, but I 
do remember that they exist)

5) I *do* recommend the use of both the two-byte and the six-byte file status 
fields for VSAM files.  The 2nd field really can provide good debugging 
information in some "obscure" cases - and it never "gets in the way" of using 
the ANSI two-byte field.

6) Remember to include "97" in the "good" values for VSAM files *and* remember 
to handle "0x" (not "00") values in your logic - when appropriate for the 
specific file type and statement.

7) If all else "fails", you may want to look at a site-wide LE condition handler 
to detect (and process) some file status situations that aren't caught 
otherwise.

8) For QSAM files, there is a (relatively) little known requirement documented 
at:
   http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3pg50/1.9.3

which says,
  "If you use the FILE STATUS clause, be sure to check the key and take 
appropriate action based on its value. If you do not check the key, your program 
might continue, but the results will probably not be what you expected."

remember this when creating JCL for COBOL programs with file status checking for 
QSAM files.
```

###### ↳ ↳ ↳ Re: Cobol and VSAM I/O

- **From:** Robert Jones <rjones0@hotmail.com>
- **Date:** 2009-08-31T06:26:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5fdf7cb-4b6a-4e79-b1d0-db4a056c24c3@v2g2000vbb.googlegroups.com>`
- **References:** `<4A9815F9.6F0F.0085.0@efirstbank.com> <4A98218A.6F0F.0085.0@efirstbank.com> <1idmm.582098$op1.107961@en-nntp-05.dc1.easynews.com>`

```
On Aug 29, 6:10 pm, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> Frank (et al),
>   There really are several issues here.  I have some comments (in no particular
…[121 more quoted lines elided]…
>

I fully agree with Bill's erudite exposition, which I couldn't have
done anywhere near as well.

However, I would note that historically, it used to be the case that
omitting File Status altogether resulted in much more informative
error reporting via IEC messages in the event of an abend, and with
much less effort in respect of program coding.  When I stopped
programming around 12 years ago there weren't even the supplementary
File Status codes, or at least I wasn't aware of them then!

Robert
```

###### ↳ ↳ ↳ Re: Cobol and VSAM I/O

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-08-31T16:54:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4A9C0032.6F0F.0085.0@efirstbank.com>`
- **References:** `<4A9815F9.6F0F.0085.0@efirstbank.com> <4A98218A.6F0F.0085.0@efirstbank.com> <1idmm.582098$op1.107961@en-nntp-05.dc1.easynews.com>`

```
Comments interspersed...

>>>On 8/29/2009 at 11:10 AM, in message
<1idmm.582098$op1.107961@en-nntp-05.dc1.easynews.com>, William M.
Klein<wmklein@nospam.ix.netcom.com> wrote:
> Frank (et al),
>   There really are several issues here.  I have some comments (in no 
…[13 more quoted lines elided]…
> non-conforming is that DECLARATIVES are "ignored".

Can you be more specific?  If I don't use DECLARATIVES then what *do* I use
to do error checking?

Doing some experimentation it appears that if one uses FASTSRT then one can
use the SORT-RETURN special register like this:

     sort sort-file                            
         on ascending key sort-key             
         using ffnd-mtce-file-vsam             
         output procedure 1000-do-it           
     if sort-return > 0                        
         move sort-return to return-code       
         display 'error in sort1: ' sort-return
         goback                                
     end-if                                    
     exit.                                     

We have never used this in the past, and in fact have never used FASTSRT.  I
don't know the reason why.  Seems like we should probably go this way.

And actually, I found the following documentation for NOFASTSRT:
"When you compile with the NOFASTSRT option, the sort process does not check
for errors in open, close, or input or output operations for files that you
reference in the USING or GIVING phrase of the SORT statement. Therefore,
you might need to check whether SORT completed successfully."
From
http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3pg50/1.12.14.

It then goes on to give a couple of options how to do this.  It gives three
options, but recommends only two:

1) Omit FILE STATUS clause and don't use DECLARATIVES.  The program will
abend if there is an I/O error.  [*]
3) Use the FILE STATUS clause *and* a DECLARATIVES error procedure.  On
error set SORT-RETURN to 16 and then make sure that you check SORT-RETURN
after the sort statement to make sure is succeeded. [**]

[*] This is how we've were doing it, but again its worth noting for the VSAM
file that an error on the open does *not* cause an abend.  It's only the
error on the read that causes the abend.  Which led me to my original
question.

[**] This answers my other question.  Don't do a GOBACK/STOP RUN (which was
what I had tried).  Set SORT-RETURN and then check it.
 
> 2) As far as relying on (or even expecting) "ABENDs" with "unsuccessful" 
> file 
…[16 more quoted lines elided]…
> for VSAM *and* QSAM.

I disagree.  If there is a guarantee (as there seems to be for QSAM) that
I/O errors will always, when FILE STATUS is not present, cause an abend, why
should I not make use of this?

What is easier to debug?  This?
IGZ0200W A file attribute mismatch was detected. File FFND-MTCE-FILE-QSAM in
program SORTTST1 was defined as a        
         physical sequential file and the file specified in the ASSIGN
clause was a VSAM data set.                    
IGZ0035S There was an unsuccessful OPEN or CLOSE of file FFMNTFL2 in program
SORTTST1 at relative location X'0532'.   
         Neither FILE STATUS nor an ERROR declarative were specified. The
status code was 39.                         
         From compile unit SORTTST1 at entry point SORTTST1 at statement 32
at compile unit offset +00000532 at entry 
         offset +00000532 at address 0DC00532.                              
                                         

Or this?
Error opening file FFMNTFL2; status=39

I say the former.

Which is not to say that I don't see your point.  Certainly it would be bad
news for me if I was to convert programs with this feature (abend on I/O) to
a system that did not have such a guarantee.

As it is most of our files are currently ESDS and use FILE STATUS et al, so
they will continue to even when we convert them to QSAM, so we should be in
pretty good shape no matter what my personal preference is.

We use regular sequential files mostly for report files.  In these cases we
do not use FILE STATUS.  Do you think we should?
 
> 3) Having said what I did above, it is very unlikely (IMHO) that IBM 
> would ever 
…[5 more quoted lines elided]…
> behavior for this to be intentionally changed.

I am under no illusions that this change would ever be made.  :-)
 
> 4)  Like declaratives for SORTs, you should be aware that IBM only 
> "guarantees" 
…[4 more quoted lines elided]…
> do remember that they exist)

I'm curious about what you mean here.  Can you elaborate?
 
> 5) I *do* recommend the use of both the two-byte and the six-byte file 
> status 
…[7 more quoted lines elided]…
> to handle "0x" (not "00") values in your logic - when appropriate for the

> specific file type and statement.

This one still bugs the heck out of me.  I wonder what chance I'd have
getting a compile or run-time option (not sure which would be appropriate)
to eliminate the possibility of file status "97".  Is there actually anyone
out there who both treats file status 97 as a successful open *and* does
something special when it is received (other than just treating it as of 00
was received)?  If no one is doing that, then what is even the point of its
existence?
 
> 7) If all else "fails", you may want to look at a site-wide LE condition 
> handler 
> to detect (and process) some file status situations that aren't caught 
> otherwise.

Hmm, there's a thought.  I'll look in to it.  Though from what I recall, a
VSAM I/O error does not cause any sort of LE condition, so how could it be
caught by LE?
 
> 8) For QSAM files, there is a (relatively) little known requirement 
> documented 
…[11 more quoted lines elided]…
> QSAM files.

What does this mean "check the key"?  I assume they mean the file status
field, since QSAM files don't have keys (do they??).

What is "little known" about this?

Something I do find interesting is this (note that the following two
statements are not the same.  One is for QSAM and one for VSAM:

"If you do not code a FILE STATUS key or a declarative, serious QSAM
processing errors will cause a message to be issued and a Language
Environment condition to be signaled, which will cause an abend if you
specify the runtime option ABTERMENC(ABEND)."

"If you do not code a file status key or a declarative, serious VSAM
processing errors will cause a message to be issued and a Language
Environment condition to be signaled, which will cause an abend if you
specify the runtime option ABTERMENC(ABEND)."

Does this mean that an open error is not a serious error in VSAM but it is
in QSAM?  Are these "serious errors" documented somewhere?


Here is one more question.  If using FILE STATUS checking does it ever make
sense to use the "AT END" and "INVALID KEY" clauses?  If I don't use FILE
STATUS, or use it in conjunction with DECLARATIVES I might have something
like this:

PERFORM UNTIL CTF-EOF
   READ CARD-TYPE-FILE             
   AT END CONTINUE                 
   NOT AT END                      
      PERFORM 0200-CARD-TYPE-RECORD
   END-READ                        
END-PERFORM

(actually if the above doesn't use FILE STATUS at all then AT END would set
an EOF flag, but otherwise it's the same).

But if I use FILE STATUS checking I would do something like this:

PERFORM UNTIL CTF-EOF
   READ CARD-TYPE-FILE             
   EVALUATE TRUE
   WHEN CTF-OK
      PERFORM 0200-CARD-TYPE-RECORD
   WHEN CTF-EOF
      CONTINUE
   WHEN OTHER
      ...ERROR STUFF HERE...
   END-READ                        
END-PERFORM


However I have seen this and think it's a bad mismash of the two:

PERFORM UNTIL CTF-AT-END
   READ CARD-TYPE-FILE             
   AT END
      SET CTF-AT-END TO TRUE
   END-READ
   IF CTF-SUCCESSFUL
      PERFORM 0200-CARD-TYPE-RECORD
   ELSE
      ...ERROR STUFF HERE...
   END-IF
END-PERFORM

I just made that example up, but I know I've seen something like it, and I
think it's pointless.  You should use one method or the other, but not both.
 Am I wrong?

Thanks!
Frank
```

###### ↳ ↳ ↳ Re: Cobol and VSAM I/O

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-09-01T14:19:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h7jai2$sma$1@reader1.panix.com>`
- **References:** `<4A9815F9.6F0F.0085.0@efirstbank.com> <4A98218A.6F0F.0085.0@efirstbank.com> <1idmm.582098$op1.107961@en-nntp-05.dc1.easynews.com> <4A9C0032.6F0F.0085.0@efirstbank.com>`

```
In article <4A9C0032.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>Comments interspersed...

Usually grumpiness interspersed between the interspersions.

[snip]

>From
>http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3pg50/1.12.14.
…[16 more quoted lines elided]…
>what I had tried).  Set SORT-RETURN and then check it.

Standard Interview Question Number 564 from... oh, aways back when:

'What should you do after every OPEN, CLOSE, READ, WRITE or REWRITE?'

'Check the FILE-STATUS associated with the dataset involved in the 
action.'

(The first time I was asked that I got this puzzled look on my face and 
used an ascending vocal inflection (indicating a question, usually) in my 
response... I could not believe someone was asking me what I thought was 
the equivalent of 'What do you do before leaving the lavatory?' 'Check to 
make sure one's zipper/buttons is/are shut'.  The interviewer said this 
was the first time he'd heard anyone answer that question correctly on the 
first go.)

I've worked on sites where knowledge of DECLARATIVES was 
minimal-to-nonexistent; I have never worked on a site where at least 
*familiarity* (if not the practise of using) FILE STATUS was equally 
alien.

[snip]

>I disagree.  If there is a guarantee (as there seems to be for QSAM) that
>I/O errors will always, when FILE STATUS is not present, cause an abend, why
>should I not make use of this?

Assuming any sort of guarantee in data processing is not, in my 
experience, a Very Good Idea.

'What does a programmer do when given an 80-character record?'

'Reserve ten characters for future use.'

Checks for NUMERIC, ON SIZE, INVALID KEY/FILE STATUS... these are there 
for their reasons.  Has anyone out there received A Guarantee from a 
Corner-Office Idiot (or, even worse... A Salesperson!) that 'this field 
will *never* be zero!' or 'There'll *always* a Master File record for any 
given Order File record'... and gotten the 2:am call when there ain't?

>
>What is easier to debug?  This?
…[16 more quoted lines elided]…
>I say the former.

I say that it depends on who is doing the debugging.

[snip]

>Here is one more question.  If using FILE STATUS checking does it ever make
>sense to use the "AT END" and "INVALID KEY" clauses?  If I don't use FILE
…[12 more quoted lines elided]…
>an EOF flag, but otherwise it's the same).

Ow... been a few years but I'd say that if a FILE STATUS is coded for 
CARD-TYPE-FILE the AT END condition populates it with a 10.

]snip]

>However I have seen this and think it's a bad mismash of the two:
>
…[14 more quoted lines elided]…
> Am I wrong?

That depends on the criteria for 'right'.  Consider the Ancient Scenario:

PROCEDURE DIVISION.

    PERFORM 0000-HOUSEKEEPING  THRU  0000-EXIT.
    PERFORM 5000-MAIN-LINE     THRU  5000-EXIT
     UNTIL NO-MORE-INPUT.
    PERFORM 9000-EOJ           THRU  9000-EXIT.
    GOBACK.
...

0000-HOUSEKEEPING.

    PERFORM 6000-READ-CARDFILE  THRU  6000-EXIT.
    IF NO-MORE-INPUT
        (do stuff for empty dataset)
        GO TO 0000-EXIT.

...

6000-READ-CARDFILE.

    READ CARDFILE  INTO  WS-CARDREC
        AT END  MOVE 'N' TO WS-MORECARDS-IND.
    ADD 1 TO CARDRECS-READ-CTR.

6000-EXIT.

Now... I know this violates all the rules about periods/full-stops and 
inline performs and bunch of other stylistic stuff...

... and I my experience has also shown me that this kind of simple, 
1977-era coding runs for decades and can be dealt with by the archetypical 
2-year programmer.  I am not against such newfangled fripperies as 'SET 
NO-MORE-INPUT TO TRUE', no... but I'm not about to go through a library of 
several thousand programs to change and test without the budget to do so, 
either, as the Bean Counters and the Users and everyone else have 
expressed annoyance at such things.

(note - in the Really Oldene Dayse one was taught to always check for 
MORE-INPUT before NO-MORE-INPUT as the assumption was that... there was 
going to be more input and checking for the less-common condition was 
wasteful... every CPU-second costs money, y'know)

DD
```

###### ↳ ↳ ↳ Re: Cobol and VSAM I/O

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-01T08:52:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<otcq95tivn05u8iv0dbr109o0chg6lor22@4ax.com>`
- **References:** `<4A9815F9.6F0F.0085.0@efirstbank.com> <4A98218A.6F0F.0085.0@efirstbank.com> <1idmm.582098$op1.107961@en-nntp-05.dc1.easynews.com> <4A9C0032.6F0F.0085.0@efirstbank.com> <h7jai2$sma$1@reader1.panix.com>`

```
On Tue, 1 Sep 2009 14:19:46 +0000 (UTC), docdwarf@panix.com () wrote:

>>[**] This answers my other question.  Don't do a GOBACK/STOP RUN (which was
>>what I had tried).  Set SORT-RETURN and then check it.
…[6 more quoted lines elided]…
>action.'

While that has been automatic for decades, what I hadn't is checking
SORT-RETURN.   At least until I needed it once.

>Checks for NUMERIC, ON SIZE, INVALID KEY/FILE STATUS... these are there 
>for their reasons.  Has anyone out there received A Guarantee from a 
>Corner-Office Idiot (or, even worse... A Salesperson!) that 'this field 
>will *never* be zero!' or 'There'll *always* a Master File record for any 
>given Order File record'... and gotten the 2:am call when there ain't?

Sometimes programmers just assume.   Coding SSAN as PIC 9(09) DISPLAY
never made sense, and these days packed-decimal or binary has lost its
advantage.   And requiring Zip codes to be numeric is US centric (and
might someday be changed).

It's easy to see such with Web pages when they won't accept 9 digit
zip codes, with or without dashes, require phone numbers to be of
particular formats, etc.
```

###### ↳ ↳ ↳ Re: Cobol and VSAM I/O

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-01T08:29:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3tbq95t4orabmieunp56t2019p88i8qmhs@4ax.com>`
- **References:** `<4A9815F9.6F0F.0085.0@efirstbank.com> <4A98218A.6F0F.0085.0@efirstbank.com> <1idmm.582098$op1.107961@en-nntp-05.dc1.easynews.com> <4A9C0032.6F0F.0085.0@efirstbank.com>`

```
On Mon, 31 Aug 2009 16:54:10 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>
>This one still bugs the heck out of me.  I wonder what chance I'd have
…[5 more quoted lines elided]…
>existence?

The point of its existence is to make life difficult for programmers.
It has no redeeming value.
```

###### ↳ ↳ ↳ Re: Cobol and VSAM I/O

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-09-01T08:31:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bvbq95pijdhcqj4e9sinebenn02roeoa7i@4ax.com>`
- **References:** `<4A9815F9.6F0F.0085.0@efirstbank.com> <4A98218A.6F0F.0085.0@efirstbank.com> <1idmm.582098$op1.107961@en-nntp-05.dc1.easynews.com> <4A9C0032.6F0F.0085.0@efirstbank.com>`

```
On Mon, 31 Aug 2009 16:54:10 -0600, "Frank Swarbrick"
<Frank.Swarbrick@efirstbank.com> wrote:

>(actually if the above doesn't use FILE STATUS at all then AT END would set
>an EOF flag, but otherwise it's the same).

Where I use FILE STATUS, I don't use AT END nor declaratives.   And I
use FILE STATUS wherever I can.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
