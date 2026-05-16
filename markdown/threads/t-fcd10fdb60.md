[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Quick 'n Dirty Unpacking of COMP-3?

_27 messages · 8 participants · 2004-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Quick 'n Dirty Unpacking of COMP-3?

- **From:** docdwarf@panix.com
- **Date:** 2004-05-07T07:51:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7ft8s$sis$1@panix5.panix.com>`

```

So... there's this file, see, that all-of-a-sudden someone Absolutely Must
Have ftp'd from the mainframe to a Unix box... not too often, only every
week or so.  LRECL=6000 and it contains COMP-3 fields... lots of COMP-3
fields... when I pull up the layout in ISPF editor and f COMP-3 all it
tells me there are 1,067 hits.

(Further research revealed no other type of non-DISPLAY numerics, no COMP 
or COMP-n or BINARY or POINTERs)

First thing I do is look for FileAid jobs I have that do something 
similar... and then I remember that there's no FileAid on the system.

Next thing I do is check the almost-FileAid they have, something called 
MAX... it can reformat based on COBOL layouts.  I take a copy of the 
file's layout, edit it to c 'COMP-3' '' all, put it into a program 
skeleton and compile it to determine the new LRECL (9116), code up a 
jobstream to let 'er rip... and it runs...

... and it runs...

... and it runs some more, after three hours of wall-time it blows up on a
B37 (space error)... whoopsie... didn't code SPACE= to be a bit more than
a third larger.  (The output I got - gotta love ,CATLG,CATLG - looked
pretty good for what got through.)  While it is running I figure, just for
laffs, to code some COBOL using the two layouts I already have...
something really complex, like:

OPEN INPUT INFILE OUTPUT OUTFILE.            
PERFORM UNTIL NO-MORE-INPUT                  
    READ INFILE INTO WK-INREC                
        AT END SET NO-MORE-INPUT TO TRUE     
        NOT AT END                           
            ADD 1 TO INREC-CTR               
            MOVE CORR WK-INREC TO WK-OUTREC  
            WRITE OUTREC FROM WK-OUTREC      
            ADD 1 TO OUTREC-CTR              
    END-READ                                 
END-PERFORM.                                 
DISPLAY 'INRECS  READ ', INREC-CTR.          
DISPLAY 'OUTRECS WRIT ', OUTREC-CTR.         
CLOSE INFILE OUTFILE.                        
GOBACK.                                      

(Notice the blithe use of MOVE CORR... kids, don't try this at home!)

... and I cobb together a jobstream, and wing it off...

... and Baby's not Happy, she blows up on record 1 with a S0C7 
(non-numeric data exception)... so there's at least one record with 
garbage data in it...

... and where there's one there's often a chance for more.

So... while the MAX job is running again, with a larger SPACE= for the
outfile I figured I'd ask if there is, once again, a Really Obvious
Solution that I'm missing... in this case one that would obviate the need
for me to code over a thousand IF FLD1 NOT NUMERIC MOVE +0 TO FLD1 (and
similar) statements.

Thanks for your time.

DD
```

#### ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-07T13:35:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com>`

```
Doc,
  I know that I shouldn't speak without researching FIRST, but a MOVE CORR
getting a S0C7 seems "odd" to me.  I didn't think that simply MOVING a COMP-3
field to a numeric display would get a S0C7 with bad data.  It may be "silly"
but did you initialize
    INREC-CTR

before you did
 ADD 1 TO INREC-CTR

P.S.  Do make your Unix stuff work "better" did you also add SIGN is SEPARATE
for your numeric output fields?
```

##### ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** docdwarf@panix.com
- **Date:** 2004-05-07T10:20:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7g5uk$bab$1@panix5.panix.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net>`

```
In article <fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>Doc,
>  I know that I shouldn't speak without researching FIRST, but a MOVE CORR
…[6 more quoted lines elided]…
> ADD 1 TO INREC-CTR

Hmmmmm... you mean coding something like:

01  INREC-CTR PIC 9(8) VALUE 0. 
01  OUTREC-CTR PIC 9(8) VALUE 0.

... in WORKING-STORAGE?  Already done, aye... but for more laffs I 
recompiled with a LIST and submitted another run...

CEE3207S The system detected a data exception (System Completion 
Code=0C7).

Program Unit: SKELPRG2 Entry: SKELPRG2 Statement: 3077 Offset: +000005FA

Let's see...

003077      2  307900                 MOVE CORR WK-INREC TO WK-OUTREC

... looks familiar... and the dump shows:

3067 01 INREC-CTR        9(8) DISP        00000001
3068 01 OUTREC-CTR       9(8) DISP        00000000

... and upon entering the Temple of Truth provided by the PMAP... errrr,
LIST... 5FA shows:

0005FA  F822 D0F8 5F5E          ZAP   248(3,13),3934(3,5)     TS2=0                             
ANN-UNIF-ALLOW*

(line wrapped)

... hmmmmm... and when I put INITIALIZE WK-OUTREC and INITIALIZE WK-INREC
right before the PERFORM, recompile and resubmit... I get another S0C7,
still in the MOVE CORR but at displacement 3B5A... INREC-CTR still 1,
OUTREC-CTR still 0...pull up the listing, check for three baker five able
and find...

003B5A  F822 D108 4F5E          ZAP   264(3,13),3934(3,4)     TS2=0                             
ANN-UNIF-ALLOW*

... smells mighty familiar.

>
>P.S.  Do make your Unix stuff work "better" did you also add SIGN is SEPARATE
>for your numeric output fields?

I'll wait until I get some output before I present the Great Magic to 
other folks and ask if they want leading or trailing signs...

... and that way they can stratch their heads, intone 'That's a goooood 
question' and have a bunch o' meetings.

Greatly appreciate your time, Mr Klein.

DD
```

##### ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-05-07T14:26:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040507102627.23382.00000989@mb-m14.aol.com>`
- **References:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net>`

```
Bill Klein writes ...

>Doc,
>  I know that I shouldn't speak without researching FIRST, but a MOVE CORR
>getting a S0C7 seems "odd" to me.  I didn't think that simply MOVING a COMP-3
>field to a numeric display would get a S0C7 with bad data. 

It may depend on the compiler NUMPROC option. If the MOVE CORR generates UNPKs,
it will not S0C7, but if it generates EDs, ED instructions can S0C7 if bad data
is found.

Kind regards,



-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** docdwarf@panix.com
- **Date:** 2004-05-07T10:51:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7g7qf$dq3$1@panix5.panix.com>`
- **References:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net> <20040507102627.23382.00000989@mb-m14.aol.com>`

```
In article <20040507102627.23382.00000989@mb-m14.aol.com>,
S Comstock <scomstock@aol.com> wrote:
>Bill Klein writes ...
>
…[7 more quoted lines elided]…
>is found.

The standard compile JCL here sets NUMPROC(MIG)... as noted in my response 
to Mr Klein the MOVE CORRis blowing up on a ZAP; browsing the LISTing 
shows UNPKs, as well, and no EDs.

DD
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-05-07T13:12:16-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7gcfr$sm0$1@news.eusc.inter.net>`
- **In-Reply-To:** `<c7g7qf$dq3$1@panix5.panix.com>`
- **References:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net> <20040507102627.23382.00000989@mb-m14.aol.com> <c7g7qf$dq3$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> In article <20040507102627.23382.00000989@mb-m14.aol.com>,
> S Comstock <scomstock@aol.com> wrote:
…[18 more quoted lines elided]…
> DD
SIGN IS SEPARATE is almost guaranteed to generate either ZAP (zero add 
packed) or CP (compare packed) for each field.  There may be another 
option that also affects sign processing in addition to NUMPROC.  You 
could try playing with the NUMPROC option but I think that COBOL 
believes in forcing the sign nibble.  The more interesting question is 
what is the data really like and do you have all of the record 
descriptions related to this file.  This looks like an interesting 
exercise because other things should be blowing up with the quality of 
data so far.  Note the first and last records may be unique.
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2004-05-07T14:26:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7gkd2$81l$1@panix5.panix.com>`
- **References:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net> <20040507102627.23382.00000989@mb-m14.aol.com> <c7g7qf$dq3$1@panix5.panix.com> <c7gcfr$sm0$1@news.eusc.inter.net>`

```
In article <c7gcfr$sm0$1@news.eusc.inter.net>,
Clark F. Morris, Jr. <cfmtech@istar.ca> wrote:
>docdwarf@panix.com wrote:
>> In article <20040507102627.23382.00000989@mb-m14.aol.com>,
…[23 more quoted lines elided]…
>believes in forcing the sign nibble.

I believe that no matter what I do I'm going to get UNPKs and ZAPS 
generated with COMP-3 fields... but my beliefs have been trampled in the 
past.

>The more interesting question is 
>what is the data really like and do you have all of the record 
>descriptions related to this file.

The data are really full of trash and I have the only record description 
related to the file... ain't Life grand?

>This looks like an interesting 
>exercise because other things should be blowing up with the quality of 
>data so far.  Note the first and last records may be unique.

Thanks much for your time.

DD
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-07T18:41:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uLQmc.11441$V97.8410@newsread1.news.pas.earthlink.net>`
- **References:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net> <20040507102627.23382.00000989@mb-m14.aol.com> <c7g7qf$dq3$1@panix5.panix.com> <c7gcfr$sm0$1@news.eusc.inter.net> <c7gkd2$81l$1@panix5.panix.com>`

```
Doc,
  I would be curious if compiling with NUMPROC(PFD) produced any ZAP's in the
LIST output.  Although I wouldn't recommend that option to my "worst enemy" for
most applications, it MIGHT do what you want for this one.
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2004-05-07T15:02:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7gmgv$dv9$1@panix5.panix.com>`
- **References:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net> <c7gcfr$sm0$1@news.eusc.inter.net> <c7gkd2$81l$1@panix5.panix.com> <uLQmc.11441$V97.8410@newsread1.news.pas.earthlink.net>`

```
In article <uLQmc.11441$V97.8410@newsread1.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>Doc,
>  I would be curious if compiling with NUMPROC(PFD) produced any ZAP's in the
>LIST output.  Although I wouldn't recommend that option to my "worst enemy" for
>most applications, it MIGHT do what you want for this one.

Well, another belief half-trampeled... the LISTing shows UNPKs by the 
score but nary a ZAP.  The job runs to completion and shows final DISPLAYs 
of:

INRECS  READ 00068353
OUTRECS WRIT 00068353

... and (including a SORT to copy a VSAM to a &&TEMP for flatfile 
processing) runs in 2min 24sec wall-time, with a total CPU time of 8.52.

The other job - the MAXBAT - was timed out after about 4.5 hrs on the wall
and burning 9999.21 in CPU...  someone's gonna be really happy about that.

Greatly appreciate the intelligence, Mr Klein... come Monday and I'll 
diddle a bit with SIGN SEPARATE clauses.

DD
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 8)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-05-07T17:04:21-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7gq2k$32i$1@news.eusc.inter.net>`
- **In-Reply-To:** `<c7gmgv$dv9$1@panix5.panix.com>`
- **References:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net> <c7gcfr$sm0$1@news.eusc.inter.net> <c7gkd2$81l$1@panix5.panix.com> <uLQmc.11441$V97.8410@newsread1.news.pas.earthlink.net> <c7gmgv$dv9$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

> In article <uLQmc.11441$V97.8410@newsread1.news.pas.earthlink.net>,
> William M. Klein <wmklein@nospam.netcom.com> wrote:
…[9 more quoted lines elided]…
> of:

For those of you not familiar with the idiosyncrasies of NUMPROC on IBM 
mainframes, NUMPROC(PFD) which I THINK corresponds to the COBOL standard 
assumes C or D for the sign nibble on signed field and F in the sign 
nibble for unsigned fields.  This is interpreted to mean that a field 
with an F zone will be treated as NOT NUMERIC.  If you have the 
misfortune to have CSP (Cross System Product?) superseded by Visual Gen 
IIRC, you are in trouble because it forces all positive sign nibbles to 
F.  There probably are other joys that William is aware of that I have 
not had the displeasure of encountering.  Since Doc found that 
NUMPROC(PFD) worked, I would be curious as to the code generated by a 
direct MOVE CORR from packed to sign is separate and a MOVE CORR packed 
to unpacked, then MOVE CORR to SIGN IS SEPARATE.
> 
> INRECS  READ 00068353
…[11 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2004-05-10T09:01:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7nug1$f8k$1@panix5.panix.com>`
- **References:** `<fgMmc.11113$V97.2698@newsread1.news.pas.earthlink.net> <uLQmc.11441$V97.8410@newsread1.news.pas.earthlink.net> <c7gmgv$dv9$1@panix5.panix.com> <c7gq2k$32i$1@news.eusc.inter.net>`

```
In article <c7gq2k$32i$1@news.eusc.inter.net>,
Clark F. Morris, Jr. <cfmtech@istar.ca> wrote:
>Since Doc found that 
>NUMPROC(PFD) worked, I would be curious as to the code generated by a 
>direct MOVE CORR from packed to sign is separate and a MOVE CORR packed 
>to unpacked, then MOVE CORR to SIGN IS SEPARATE.

This might be a subject for future experimentation... right now I have a 
file that needs to get out.

Thanks to all for their time and expertise.

DD
```

#### ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-05-09T09:39:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-4FD62B.09391409052004@corp.supernews.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com>`

```
In article <c7ft8s$sis$1@panix5.panix.com>, docdwarf@panix.com wrote:

> So... there's this file, see, that all-of-a-sudden someone Absolutely Must
> Have ftp'd from the mainframe to a Unix box... not too often, only every
…[60 more quoted lines elided]…
> 

Sort would do this with INREC and OUTREC processing -- but a thousand of 
those will get tedious.

Why not write a program to read the copybook and generate an IF/MOVE 
sequence for every field?
```

##### ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** docdwarf@panix.com
- **Date:** 2004-05-10T09:03:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7nujb$fev$1@panix5.panix.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-4FD62B.09391409052004@corp.supernews.com>`

```
In article <joe_zitzelberger-4FD62B.09391409052004@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:

[snip]

>Why not write a program to read the copybook and generate an IF/MOVE 
>sequence for every field?

Because a solution which does not require this exists... ain't Life grand?

DD
```

#### ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-05-09T09:41:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-97017B.09413209052004@corp.supernews.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com>`

```
In article <c7ft8s$sis$1@panix5.panix.com>, docdwarf@panix.com wrote:

> So... there's this file, see, that all-of-a-sudden someone Absolutely Must
> Have ftp'd from the mainframe to a Unix box... not too often, only every
…[60 more quoted lines elided]…
> 

One other thought, you could set an LE resume point at the top of your 
read loop and use an LE Condition Handler to bypass the offending 
record.
```

##### ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** docdwarf@panix.com
- **Date:** 2004-05-10T09:05:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7nun0$gmj$1@panix5.panix.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-97017B.09413209052004@corp.supernews.com>`

```
In article <joe_zitzelberger-97017B.09413209052004@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <c7ft8s$sis$1@panix5.panix.com>, docdwarf@panix.com wrote:

[snip]

>> So... while the MAX job is running again, with a larger SPACE= for the
>> outfile I figured I'd ask if there is, once again, a Really Obvious
…[9 more quoted lines elided]…
>record.

An interesting thought... how might you suggest such an offending record
be handled without over a thousand IF FLD1 NOT NUMERIC MOVE +0 TO FLD1
(and similar) statements?

DD
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-05-11T08:49:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-FED725.08494111052004@corp.supernews.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-97017B.09413209052004@corp.supernews.com> <c7nun0$gmj$1@panix5.panix.com>`

```
In article <c7nun0$gmj$1@panix5.panix.com>, docdwarf@panix.com wrote:

> In article <joe_zitzelberger-97017B.09413209052004@corp.supernews.com>,
> Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[22 more quoted lines elided]…
> 

Your exit receives a pointer defined when you register the exit, as well 
as the offset and type of condition.  You could, for all SOC7 
conditions, inspect the field in question and replace it with a proper 
numeric zero.  Then resume execution.

This would be slightly harder than typing a thousand "IF NOT NUMERIC 
MOVE 0" statements -- but it might be fun to write.
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-05-11T10:24:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7qnnl$dlj$1@panix5.panix.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-97017B.09413209052004@corp.supernews.com> <c7nun0$gmj$1@panix5.panix.com> <joe_zitzelberger-FED725.08494111052004@corp.supernews.com>`

```
In article <joe_zitzelberger-FED725.08494111052004@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <c7nun0$gmj$1@panix5.panix.com>, docdwarf@panix.com wrote:
>
…[28 more quoted lines elided]…
>numeric zero.  Then resume execution.

How interesting... is there some way to relate this pointer and offset to 
a data-name outside of relating it to the result of a LIST compile?

>
>This would be slightly harder than typing a thousand "IF NOT NUMERIC 
>MOVE 0" statements -- but it might be fun to write.

I am a consultant/contractor/hired gun... if it were fun it would have
been assigned to someone else.

DD
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 5)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-05-12T19:32:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-41D71E.19325312052004@corp.supernews.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-97017B.09413209052004@corp.supernews.com> <c7nun0$gmj$1@panix5.panix.com> <joe_zitzelberger-FED725.08494111052004@corp.supernews.com> <c7qnnl$dlj$1@panix5.panix.com>`

```
In article <c7qnnl$dlj$1@panix5.panix.com>, docdwarf@panix.com wrote:

> In article <joe_zitzelberger-FED725.08494111052004@corp.supernews.com>,
> Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[34 more quoted lines elided]…
> a data-name outside of relating it to the result of a LIST compile?

Yes, when you register the condition handler whatever pointer you pass 
is the pointer handed to your program.  So it could, for example, be a 
pointer to the record in question.  That would not save you from doing 
several hunderd "IF NUMERICS".

However, one of the data items that LE will provide in cases of an abend 
is the address of the offending instruction.  IIRC there is only 1 
packed decimal format (unless EDIT is another format, can't remember 
now):

   DECIMAL-OPCODE   OFFSET1(LENGTH1,BASE1),OFFSET2(LENGTH2,BASE2)

The bit layout is (agian, from memory):

   OP......LEN1LEN2OFFSET1.....BAS1OFFSET2.....BAS2
   1      89   1  1           2   3            4  4 
               3  6           8   2            5  8

A bit of bit twiddling could convert the bases and offsets into a 
pointer.  You could then inspect storage at that pointer for the given 
length for a valid packed number.

If either or both operands were invalid, replace with a packed zero and 
instruct LE to retry the operation.


> >This would be slightly harder than typing a thousand "IF NOT NUMERIC 
> >MOVE 0" statements -- but it might be fun to write.
…[4 more quoted lines elided]…
> DD

The more I think about it, the more I think this would be easier to do 
in assembler.  With Cobol, it would be troublesom to get the base 
register values -- they are available as part of the condition 
information with LE, but I'm not sure how to get them without my 
references handy.
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-05-13T09:43:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7vu15$97r$1@panix5.panix.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-FED725.08494111052004@corp.supernews.com> <c7qnnl$dlj$1@panix5.panix.com> <joe_zitzelberger-41D71E.19325312052004@corp.supernews.com>`

```
In article <joe_zitzelberger-41D71E.19325312052004@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <c7qnnl$dlj$1@panix5.panix.com>, docdwarf@panix.com wrote:
>
…[41 more quoted lines elided]…
>several hunderd "IF NUMERICS".

So let me see if I have this right.  If I try to use a MOVE CORR on a 
record which contains trash data which have not been tested with hundreds 
of IF NUMERIC statements then I get a S0C7...

... from which I could recover, using the condition handler, so that I 
could then check the data of the offending record using hundreds of IF 
NUMERIC statements.

Oh joy.

>
>However, one of the data items that LE will provide in cases of an abend 
…[14 more quoted lines elided]…
>length for a valid packed number.

Golly gee, this just gets better and better!  Now 'all I gotta do' is 
capture an ABEND, 'twiddle the bits' to get the bases, offsetes and 
lengths (we are, after all, dealing with SS instructions here), do the 
hokey-pokey and turn myself about!

>
>If either or both operands were invalid, replace with a packed zero and 
…[14 more quoted lines elided]…
>references handy.

The more I thought about it the more I realised that hundreds of IF 
NUMERICs were in order... until I talked to my tech lead...

... who said 'Oh, in that file (a VSAM KSDS) there are two kinds of 
records, a Type 4 which is the real data record and a Type 1 which is a 
pointer record to another Type 4.  Just skip the Type 1 recs since they're 
full of garbage.'

So... I coded for that condition and ran again... and she's-a blow-em-up, 
real good, but this time on a different field, one awaaaaaaay on down in 
the record description.  I went back to my tech lead and said 'This field 
and the one immediately following it... they were added recently, weren't 
they, out of end-of-record filler and as a result frequently contain 
spaces, low-values or other garbage, right?'

'Gosh... how did you know that?'

'It... smelled that way.'

So... I went back and coded:

PERFORM UNTIL NO-MORE-INPUT                                  
    READ INFILE INTO WK-INREC                                
        AT END SET NO-MORE-INPUT TO TRUE                     
        NOT AT END                                           
            ADD 1 TO INREC-CTR                               
            IF FLD1 OF WK-INREC NOT = '1'              
                ADD 1 TO NOT-1-CTR                           
                IF FLD28 OF WK-INREC NOT NUMERIC      
                    MOVE +0 TO FLD28 OF WK-INREC      
                END-IF                                       
                IF FLD29 OF WK-INREC NOT NUMERIC            
                   MOVE +0 TO FLD29 OF WK-INREC 
                END-IF                                       
                MOVE CORR WK-INREC TO WK-OUTREC              
                WRITE OUTREC FROM WK-OUTREC     
                ADD 1 TO OUTREC-CTR             
            END-IF                              
            IF FLD1 OF WK-INREC = '1'     
                ADD 1 TO TYP-1-CTR              
            END-IF                              
    END-READ                                    
END-PERFORM.                                    

(I realise the second test of FLD1 could have been an 'ELSE'; my memory 
is, admittedly, porous and I find it more clear to explicitly code a 
second condition than rely on recalling the earlier condition... clarity 
being in the mind of the beholder and all that.)

(wow... I just re-read the code and even with those newfangled inlines and 
scope-delimiters... looks like *someone* took McCracken's book rather 
seriously, doesn't it?)

... and I went back and changed my compile stream from NUMPROG(PFD) to 
NUMPROC(MIG) because I remember getting warning about that...

... and she runs like a watch.

So what comes next?  My guess is... someone on the receiving end will want 
to modify the data and I'll get tasked with converting the file back from 
display numerics to COMP-3 fields... and recombining it with the recs that 
got left out... oh, and since the other platform doesn't have the 
mainframe's data-validation routines could I do... something to make sure 
they're not sending trash back up?

Thanks to all for the input.

DD
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 7)_

- **From:** rjones0@hotmail.com (Robert Jones)
- **Date:** 2004-05-13T13:45:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dd8322.0405131245.786c4bdd@posting.google.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-FED725.08494111052004@corp.supernews.com> <c7qnnl$dlj$1@panix5.panix.com> <joe_zitzelberger-41D71E.19325312052004@corp.supernews.com> <c7vu15$97r$1@panix5.panix.com>`

```
message snipped

I haven't used them for quite a while, but would products such as
Fileaid or DFSORT be able to do this job for you.

Another possibility is to get promoted, then you can use a tool called
a programmer!

Robert
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-05-13T18:08:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c80rl9$g5o$1@panix5.panix.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-41D71E.19325312052004@corp.supernews.com> <c7vu15$97r$1@panix5.panix.com> <6dd8322.0405131245.786c4bdd@posting.google.com>`

```
In article <6dd8322.0405131245.786c4bdd@posting.google.com>,
Robert Jones <rjones0@hotmail.com> wrote:
>message snipped
>
>I haven't used them for quite a while, but would products such as
>Fileaid or DFSORT be able to do this job for you.

From:

<http://groups.google.com/groups?selm=c7ft8s%24sis%241%40panix5.panix.com&output=gplain>

--begin quoted text:

First thing I do is look for FileAid jobs I have that do something 
similar... and then I remember that there's no FileAid on the system.

Next thing I do is check the almost-FileAid they have, something called 
MAX... it can reformat based on COBOL layouts.

--end quoted text

>
>Another possibility is to get promoted, then you can use a tool called
>a programmer!

Setting aside the fact that I am a consultant/contractor/hired gun and 
such folks rarely get promoted...

From:

<http://groups.google.com/groups?selm=37D27F27.8D1F5D0A%40home.com&output=gplain>

--begin quoted text:

... I do not believe that I am capable of lowering the quality of my
thinking far enough to be a manager.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 9)_

- **From:** berlutte@sympatico.ca
- **Date:** 2004-05-13T19:49:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qm78a0dt3ea3l88ti69hiukbrtvbgmcfjq@4ax.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-41D71E.19325312052004@corp.supernews.com> <c7vu15$97r$1@panix5.panix.com> <6dd8322.0405131245.786c4bdd@posting.google.com> <c80rl9$g5o$1@panix5.panix.com>`

```
On 13 May 2004 18:08:41 -0400, docdwarf@panix.com wrote:

>... I do not believe that I am capable of lowering the quality of my
>thinking far enough to be a manager.

Shades of Barb Bush's 'beautiful mind'!

Have you heard the news, old mule?

http://www.madcowprod.com/

The leader of the two Israelis arrested after leading police on a high
speed chase in a moving van last Saturday in rural Tennessee is the
son of the spokesman for the Likud Party of Israeli Prime Minister
Ariel Sharon, the MadCowMorningNews has learned. 

The arrested Israeli 'mover,' Shmuel Dahan, 23, is himself a former
spokesman, for the National Union of Israeli Students which represents
the country's 150,000 university students. 
========================================================
*They* don't look like happy campers are they?  

I thought that since yer such a vigilant patriot, such event would
surely put you to sleep, nay?

This catatonic state is spreadin' o'er much o'  the suburbia *and*
exurbia:
http://context.themoscowtimes.com/stories/2004/04/30/120.html

Freepers had Berg in the cross-hair:
http://www.breakfornews.com/NickBergEnemiesList.htm

Tzar Caoui had an artificial leg, that is until he died last January.

*Ski* masks in Iraq and a Gitmo orange jumpsuit, this is dadaism
rebirth fer sure, ain't it, old noose?

Fresh:
http://www.khilafah.com/home/category.php?DocumentID=9529&TagID=2
ABC all-time little weasel Brian Ross farted another master 
NSAFBICIA stinky for the burbs' nouveaux riches

Executioner wore gold ring - forbidden by Islam

A close examination of the tape shows none of the five masked men is
wearing gloves, so federal officials are trying to determine if there
are any tell-tale tattoos on their hands. One of the clues the FBI and
CIA is studying is the large gold ring Zarqawi is wearing on his right
hand, giving off a glare several times during the six-minute tape.

Wadda clue! 

HAHAHAHAHARRRGHH
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 9)_

- **From:** berlutte@sympatico.ca
- **Date:** 2004-05-13T21:15:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o7h8a0hm72o4jtgfpn6lg4295c3g4q71af@4ax.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-41D71E.19325312052004@corp.supernews.com> <c7vu15$97r$1@panix5.panix.com> <6dd8322.0405131245.786c4bdd@posting.google.com> <c80rl9$g5o$1@panix5.panix.com>`

```
On 13 May 2004 18:08:41 -0400, docdwarf@panix.com wrote:

By the by, do you remember them white plastic resin chairs?

http://www.libertyforum.org/showflat.php?Cat=&Board=news_members&Number=1469025&t=-1#Post1469025



Fresher:
http://www.libertypost.org/cgi-bin/readart.cgi?ArtNum=49565
But CBS News National Security Correspondent David Martin reports on
what is turning into a bizarre mystery with a connection to 9/11. 

U.S. officials say the FBI questioned Berg in 2002 after a computer
password Berg used in college turned up in the possession of Zaccarias
Moussaoui, the al Qaeda operative arrested shortly before 9/11 for his
suspicious activity at a flight school in Minnesota. 

The bureau had already dismissed the connection between Berg and
Moussaoui as nothing more than a college student who had been careless
about protecting his password.
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 5)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-14T00:58:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40a41280.240503906@news.optonline.net>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-97017B.09413209052004@corp.supernews.com> <c7nun0$gmj$1@panix5.panix.com> <joe_zitzelberger-FED725.08494111052004@corp.supernews.com> <c7qnnl$dlj$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

>I am a consultant/contractor/hired gun... if it were fun it would have
>been assigned to someone else.

I too am a contractor/hired gun, and I get assigned the fun projects because
application dweebs, intellectually limited to PERFORM 1000-10-FOO THRU
1000-10-EXIT, can't figure out how to do them. Build a tool? They don't have a
clue.

As a furinstance, I just wrote two shells enabling Oracle External Procedures in
Cobol. SAP has been trying to figure it out for five years without success.
They're still using clunky Oracle pipes which single-thread applications.

It cannot be done 100% in Cobol because the Oracle listener loads its target
with options incompatible with the Micro Focus runtime. The trick is to write a
C shell that loads a Cobol shell (bound to the MF runtime) with the right
options. The Cobol shell can then load and run *thread-safe* Cobol apps,
compiled to .gnt or .so. Making a MF Cobol app thread-safe requires one compiler
option -- reentrant(2) -- and no change to the source code.

Rented programmers can be whores or gun slingers. The choice is theirs, not the
employer's. Step up to the plate, hit a few home runs, and you too can do Real
Programming .. without regard to employment or pecking order.
```

###### ↳ ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-05-13T22:13:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c81a0v$aou$1@panix5.panix.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <joe_zitzelberger-FED725.08494111052004@corp.supernews.com> <c7qnnl$dlj$1@panix5.panix.com> <40a41280.240503906@news.optonline.net>`

```
In article <40a41280.240503906@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[6 more quoted lines elided]…
>clue.

Oh, I *cannot* resist... they seem to have hired one as a contractor,
though.

[snip]

>Rented programmers can be whores or gun slingers. The choice is theirs, not the
>employer's. Step up to the plate, hit a few home runs, and you too can do Real
>Programming .. without regard to employment or pecking order.

Mr Wagner, you have no idea how... profoundly sports metaphors motivate 
me, whether intoned by you or another.  Do be so kind as to give a shout 
when you've run out of platitudes and started on plongitudes, will you?

DD
```

#### ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-12T00:12:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40a165ff.65243754@news.optonline.net>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
[top-posted reply]

What you need is a tool that reads Cobol descriptions of the input and output
files, and interpretively performs the copy with accepable speed. I've written
some heavy-duty tools to do that .. heavy-duty meaning multiple record formats,
multiple segments, arrays within segments, header and trailer records, multiple
'tables' within a file, etc.

If I have nothing to do in the next month, which is likely, I'll write it for
you, gratis. It will be a good demo of parsing and appling lexicography to
Cobol.

In the 'good (bad)' old days, such a tool had to spit machine language into RAM
and finally jump to it. A JIT compiler. I did that when I wrote DYL240. 

Nowadays, an interpreter is fast enough .. if it's better than MAX. Interpreters
are not always so slow. I wrote one six years ago for Sears, who used it for all
their Y2K testing.  It ran on million-record files with acceptable speed. It was
100% Cobol. 

Robert


>
>So... there's this file, see, that all-of-a-sudden someone Absolutely Must
…[56 more quoted lines elided]…
>similar) statements.
```

##### ↳ ↳ Re: Quick 'n Dirty Unpacking of COMP-3?

- **From:** docdwarf@panix.com
- **Date:** 2004-05-11T21:55:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7s05t$9qo$1@panix5.panix.com>`
- **References:** `<c7ft8s$sis$1@panix5.panix.com> <40a165ff.65243754@news.optonline.net>`

```
In article <40a165ff.65243754@news.optonline.net>,
Robert Wagner <robert.deletethis@wagner.net> wrote:
>docdwarf@panix.com wrote:
>[top-posted reply]
…[9 more quoted lines elided]…
>Cobol.

Truly, Mr Wagner, it would be greater generosity than I deserve.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
