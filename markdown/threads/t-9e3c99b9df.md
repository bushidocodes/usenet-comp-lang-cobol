[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dumb Question 2: Start syntax

_11 messages · 6 participants · 2004-06_

---

### Dumb Question 2: Start syntax

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-06-23T02:35:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net>`

```
Also, is there a quick was to seek (START) an indexed file on a key to the
end of a file?

Obviously, START  FILENAME
                     KEY IS LESS THAN KEY-VALUE

won't do it, wouldn't even make any sense.

I could START it with a key that has the maximum key value in it, but if
memory
serves me right, a START where there is a an INVALID KEY combination,
such as seeking >= a key that is maxed, results in an undefined condition
- at least in LE COBOL.

Sorry to sound so dumb, I switch languages on a daily basis, and I am not
where I can
get at my handy notebook with answers for each language.

Paul
```

#### ↳ Re: Dumb Question 2: Start syntax

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-06-23T02:48:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net>`

```
START LESS  THAN and READ PREVIOUS are in the ISO 2002 Standard.  Several
compilers have had these as extensions.  The 2002 Standard also supports LAST
(and FIRST) key words for the START statement.

Tell us your compiler and we'll tell you how to do this.  (For compilers withOUT
this "built-in functionality" - it is medium common to have "compliments"
alternate record keys to read backwards.  But this is a "file design" question.)
```

##### ↳ ↳ Re: Dumb Question 2: Start syntax

- **From:** paul@raulersons.com (Paul Raulerson)
- **Date:** 2004-06-23T07:45:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b475f.0406230645.66237660@posting.google.com>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net> <ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net>`

```
I'm not sure why the return post did not show up, i think I must have e-mailed 
it back to Bill and the nospam trap caught it. 

The compiler is:
  5769CB1 V4R4M0  990521 LN  IBM ILE COBOL for AS/400 

Which I think equates to version 3.8 or something similar. The compiler does
support READ fn PRIOR RECORD, but if you set start to find a key with 
HIGH-VALUES, the result appears to be undetermined. The following code
(in a demo module) produces an error 46. 

0118.00        PROCEDURE DIVISION.                
0118.01        START-PROGRAM.                     
0118.02            OPEN I-O IT02                  
0118.03            MOVE HIGH-VALUES TO IT02-TITLE 
0118.04            START IT02                     
0118.05               KEY >= IT02-TITLE           
0118.06               WITH NO LOCK                
0118.09               END-START                   
0118.11            READ IT02 PRIOR RECORD  
0118.12              WITH NO LOCK       
0118.13              END-READ                     
0118.14            DISPLAY IT02-FILE-STATUS 
0148.00            GOBACK.                  


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net>...
> START LESS  THAN and READ PREVIOUS are in the ISO 2002 Standard.  Several
> compilers have had these as extensions.  The 2002 Standard also supports LAST
…[31 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Dumb Question 2: Start syntax

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-06-23T17:01:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PHiCc.11378$w07.8525@newsread2.news.pas.earthlink.net>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net> <ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net> <7b475f.0406230645.66237660@posting.google.com>`

```
WOW ... a question about ANS COBOL V4 !!! (last in service about 1982)

That compiler was originally written for ISAM not even VSAM (and also supports
BDAM rather than VSAM RRDS).

I do have a couple of manuals for it (still around) but any suggestions for
COBOL code that might work for this compiler will only cause you MORE problems
when you move to a "current" compiler.

P.S.  Are you aware that IBM doesn't even support its object code with the LE
run-time libraries.  You *must* be on OS/VS COBOL to get that level of support.
```

###### ↳ ↳ ↳ Re: Dumb Question 2: Start syntax

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-06-23T18:03:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xBjCc.15238$Wr.2376@newsread1.news.pas.earthlink.net>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net> <ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net> <7b475f.0406230645.66237660@posting.google.com> <PHiCc.11378$w07.8525@newsread2.news.pas.earthlink.net>`

```
Call me WRONG.

I have been corrected "off-list".  This is ILE COBOL (for OS/400) and *not* ANS
COBOL V4.

I'll need to let someone else answer questions about its keyed-file access.
```

###### ↳ ↳ ↳ Re: Dumb Question 2: Start syntax

_(reply depth: 4)_

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-06-24T00:43:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ospCc.25051$a61.14077@nwrddc01.gnilink.net>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net> <ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net> <7b475f.0406230645.66237660@posting.google.com> <PHiCc.11378$w07.8525@newsread2.news.pas.earthlink.net>`

```
<grin> Not *quite* that bad Bill. It is the current compiler on the AS/400,
but it is more than a little
behind the z/OS versions.

-Paul

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:PHiCc.11378$w07.8525@newsread2.news.pas.earthlink.net...
> WOW ... a question about ANS COBOL V4 !!! (last in service about 1982)
>
> That compiler was originally written for ISAM not even VSAM (and also
supports
> BDAM rather than VSAM RRDS).
>
> I do have a couple of manuals for it (still around) but any suggestions
for
> COBOL code that might work for this compiler will only cause you MORE
problems
> when you move to a "current" compiler.
>
> P.S.  Are you aware that IBM doesn't even support its object code with the
LE
> run-time libraries.  You *must* be on OS/VS COBOL to get that level of
support.
>
> -- 
…[4 more quoted lines elided]…
> > I'm not sure why the return post did not show up, i think I must have
e-mailed
> > it back to Bill and the nospam trap caught it.
> >
…[3 more quoted lines elided]…
> > Which I think equates to version 3.8 or something similar. The compiler
does
> > support READ fn PRIOR RECORD, but if you set start to find a key with
> > HIGH-VALUES, the result appears to be undetermined. The following code
…[19 more quoted lines elided]…
> > > START LESS  THAN and READ PREVIOUS are in the ISO 2002 Standard.
Several
> > > compilers have had these as extensions.  The 2002 Standard also
supports
> LAST
> > > (and FIRST) key words for the START statement.
> > >
> > > Tell us your compiler and we'll tell you how to do this.  (For
compilers
> withOUT
> > > this "built-in functionality" - it is medium common to have
"compliments"
> > > alternate record keys to read backwards.  But this is a "file design"
> question.)
…[6 more quoted lines elided]…
> > > > Also, is there a quick was to seek (START) an indexed file on a key
to the
> > > > end of a file?
> > > >
…[5 more quoted lines elided]…
> > > > I could START it with a key that has the maximum key value in it,
but if
> > > > memory
> > > > serves me right, a START where there is a an INVALID KEY
combination,
> > > > such as seeking >= a key that is maxed, results in an undefined
condition
> > > > - at least in LE COBOL.
> > > >
> > > > Sorry to sound so dumb, I switch languages on a daily basis, and I
am not
> > > > where I can
> > > > get at my handy notebook with answers for each language.
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Dumb Question 2: Start syntax

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-06-23T19:35:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g7jjd0dkrl8j45p510fipnh176inqt94lm@4ax.com>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net> <ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net> <7b475f.0406230645.66237660@posting.google.com>`

```
On 23 Jun 2004 07:45:54 -0700, paul@raulersons.com (Paul Raulerson) 
wrote:
Top posting corrected.

>
>"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net>...
…[33 more quoted lines elided]…
>> >

>I'm not sure why the return post did not show up, i think I must have e-mailed 
>it back to Bill and the nospam trap caught it. 
…[22 more quoted lines elided]…
>

The "correct" way to do this is

start filex ...
  invalid key
     read filex last record
     end read
 not invalid key
     read filex prior
     end read
end start

error 46 is correct on this case as you have an invalid key, hence the
following read will issue an error 46.

ALWAYS code an invalid key on a start, or use file-status validation
before the next file operation on the same logical file.




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Dumb Question 2: Start syntax

_(reply depth: 4)_

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-06-24T00:46:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TvpCc.25063$a61.11625@nwrddc01.gnilink.net>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net> <ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net> <7b475f.0406230645.66237660@posting.google.com> <g7jjd0dkrl8j45p510fipnh176inqt94lm@4ax.com>`

```
Well, I'll be. That READ fn LAST RECORD works. I don't believe that I, in my
staggering
ignorance, have came across that before. Is this just a 400 thing, or does
it exist on z/OS
as well?

-Paul

"Frederico Fonseca" <real-email-in-msg-spam@email.com> wrote in message
news:g7jjd0dkrl8j45p510fipnh176inqt94lm@4ax.com...
> On 23 Jun 2004 07:45:54 -0700, paul@raulersons.com (Paul Raulerson)
> wrote:
…[3 more quoted lines elided]…
> >"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:<ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net>...
> >> START LESS  THAN and READ PREVIOUS are in the ISO 2002 Standard.
Several
> >> compilers have had these as extensions.  The 2002 Standard also
supports LAST
> >> (and FIRST) key words for the START statement.
> >>
> >> Tell us your compiler and we'll tell you how to do this.  (For
compilers withOUT
> >> this "built-in functionality" - it is medium common to have
"compliments"
> >> alternate record keys to read backwards.  But this is a "file design"
question.)
> >>
> >> -- 
…[4 more quoted lines elided]…
> >> > Also, is there a quick was to seek (START) an indexed file on a key
to the
> >> > end of a file?
> >> >
…[5 more quoted lines elided]…
> >> > I could START it with a key that has the maximum key value in it, but
if
> >> > memory
> >> > serves me right, a START where there is a an INVALID KEY combination,
> >> > such as seeking >= a key that is maxed, results in an undefined
condition
> >> > - at least in LE COBOL.
> >> >
> >> > Sorry to sound so dumb, I switch languages on a daily basis, and I am
not
> >> > where I can
> >> > get at my handy notebook with answers for each language.
…[5 more quoted lines elided]…
> >I'm not sure why the return post did not show up, i think I must have
e-mailed
> >it back to Bill and the nospam trap caught it.
> >
…[3 more quoted lines elided]…
> >Which I think equates to version 3.8 or something similar. The compiler
does
> >support READ fn PRIOR RECORD, but if you set start to find a key with
> >HIGH-VALUES, the result appears to be undetermined. The following code
…[38 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Dumb Question 2: Start syntax

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-06-23T15:28:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BLSdnZnR_PpAekTdRVn-sQ@giganews.com>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net> <ic6Cc.14711$Wr.10730@newsread1.news.pas.earthlink.net> <7b475f.0406230645.66237660@posting.google.com>`

```
Paul Raulerson wrote:
> I'm not sure why the return post did not show up, i think I must have
> e-mailed
…[9 more quoted lines elided]…
> (in a demo module) produces an error 46.

Piss on it. WRITE your own high-values record before you do anything else.
Then, when you finish with the file, DELETE your high-values record.

READ my-file KEY = {high-values}
   INVALID KEY
      MOVE HIGH-VALUES TO {record}
      WRITE my-record
   END-READ

START {myfile}KEY = {high-values}
 ...
```

#### ↳ Re: Dumb Question 2: Start syntax

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-06-23T03:11:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0406230211.d61b09d@posting.google.com>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net>`

```
Paul,

I believe you're using Mainframe LE?

The standard solution I use (and these days it is only on VERY old
stuff; everything else is migrated to RDB) would be START REVERSED
ORDER followed by GET NEXT. This is only available on Fujitsu, though,
as far as I know.

In ancient times, as Bill pointed out, it was fairly widespread to use
an alternate reversed key for ISAM/VSAM files that needed reversed
reading frequently. This was horrendously inefficient (hardware was
slower in those days and dynamic updates using alternate keys were a
nightmare) and some sites found it easier to set up a series of IDCAMS
steps as a single batch job that unloaded and sorted into reversed
sequence, producing a sequential file. This could then be processed
sequentially with the keys on it used to access the original ISAM/VSAM
file.

I don't know how widespread it is today, but when we set up KSDSs in
the old days we used to write a dummy record to them with High Values
in it. This was supposed to help the splitting of control areas and
intervals when subsequent maintenance occurred. If it is still normal
practice, then you could do a START = HIGH-VALUES followed by GET
PREV.

Other than that, I can't think of any bright ideas to enable you to
quickly get to EOF.

Here's a final not-so-bright idea...

Go and have a talk to your friendly neighbourhood sysprog. It MIGHT be
possible to check the index component of the KSDS or ISAM file and
determine the highest key in it...(the trick is to get the format of
it; sysprog should have access to this.)

Pete.

 



"PAUL RAULERSON" <pkraulerson@verizon.net> wrote in message news:<406Cc.23917$a61.23908@nwrddc01.gnilink.net>...
> Also, is there a quick was to seek (START) an indexed file on a key to the
> end of a file?
…[16 more quoted lines elided]…
> Paul
```

##### ↳ ↳ Re: Dumb Question 2: Start syntax

- **From:** paul@raulersons.com (Paul Raulerson)
- **Date:** 2004-06-23T07:49:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b475f.0406230649.71cee728@posting.google.com>`
- **References:** `<406Cc.23917$a61.23908@nwrddc01.gnilink.net> <b3638c46.0406230211.d61b09d@posting.google.com>`

```
dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote in message news:<b3638c46.0406230211.d61b09d@posting.google.com>...
> Paul,
> 
> I believe you're using Mainframe LE?
> 
 I wish. :) 

<snip>
> 
> Here's a final not-so-bright idea...
…[7 more quoted lines elided]…
> 
 I guess I could certianly do that. It didn't even occur to me to do
so. Thanks for pointing it out. I would have to modify a couple dozen
reports to filter out the extraneous record, but that is doable.

Thanks 
-Paul
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
