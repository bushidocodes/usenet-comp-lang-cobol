[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Edit VSAM?

_21 messages · 13 participants · 2000-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Edit VSAM?

- **From:** petert@my-deja.com
- **Date:** 2000-10-11T06:22:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```
Is there any easy way to edit/update a VSAM KSDS without writing a cobol
program?  I just want to change 1 byte.......
Thanks
Peter


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Edit VSAM?

- **From:** tscoffey@my-deja.com
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s1j66$p8$1@nnrp1.deja.com>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```
In article <8s10vf$j0p$1@nnrp1.deja.com>,
  petert@my-deja.com wrote:
> Is there any easy way to edit/update a VSAM KSDS without writing a
cobol
> program?  I just want to change 1 byte.......
> Thanks
…[4 more quoted lines elided]…
>

If you have FileAid, you can use it.

You could perhaps do it with SyncSort.
Use 1 sort to separate the record(s) you want to change from the ones
you don't. Use a second to edit the changing records. Use a third
to re-combine the file by key. Then do an IDCAMS reload.

To use a VSAM KSDS as SyncSort input, you need to tell SyncSort
what the record type and length are.
RECORD TYPE=F,LENGTH=xxxx   for a KSDS with fixed record size
RECORD TYPE=V,LENGTH=(max,,,min,average) for a KSDS with variable
recsize.


Tim


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Edit VSAM?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UKYE5.587$8k7.19177@paloalto-snr1.gtei.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```
File-Aid can do this (this is the easy way).

An EzTrieve Program to change one byte wouldn't be too bad.

I don't know REXX, but I would not be surprised if a 'change one byte'
script is pretty easy.

Or, you could always IDCAMS/REPRO the KSDS to a QSAM file, edit that with
the TSO Editor, and reload the KSDS with another IDCAMS/REPRO. (DFSORT and
SyncSort could be used to replace IDCAMS/REPRO in this scenario).

Probably some other ways, too.
```

##### ↳ ↳ Re: Edit VSAM?

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-10-12T02:29:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E521DC.4D8A3B69@optonline.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <UKYE5.587$8k7.19177@paloalto-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> File-Aid can do this (this is the easy way).
…[4 more quoted lines elided]…
> script is pretty easy.

While REXX is a terrific language (IMHO, anyway), it doesn't have a VSAM
interface.

Someone suggested REPROing a record into a flat file, editing it (in
ISPF), then REPROing it back into the file. Sounds like a workable
solution in a low volume situation.

LiamD
```

###### ↳ ↳ ↳ Re: Edit VSAM?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m8hF5.25$7%6.21225@dfiatx1-snr1.gtei.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <UKYE5.587$8k7.19177@paloalto-snr1.gtei.net> <39E521DC.4D8A3B69@optonline.net>`

```
Liam Devlin <liamddd@optonline.net> wrote in message
news:39E521DC.4D8A3B69@optonline.net...
> Michael Mattias wrote:
> >
…[9 more quoted lines elided]…
>

Hmm... I guess I am not going to get that surprise. I'll file that info
away, though; nice to know even if I am not a REXX user.

MCM
```

###### ↳ ↳ ↳ Re: Edit VSAM?

- **From:** dallasgard@my-deja.com
- **Date:** 2000-10-31T18:46:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tn42q$62g$1@nnrp1.deja.com>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <UKYE5.587$8k7.19177@paloalto-snr1.gtei.net> <39E521DC.4D8A3B69@optonline.net>`

```
In article <39E521DC.4D8A3B69@optonline.net>,
  LiamD@optoffline.not wrote:
> Michael Mattias wrote:
> >
> > File-Aid can do this (this is the easy way).
> >
> > An EzTrieve Program to change one byte
wouldn't be too bad.
> >
> > I don't know REXX, but I would not be
surprised if a 'change one byte'
> > script is pretty easy.
>
> While REXX is a terrific language (IMHO,
anyway), it doesn't have a VSAM

Here is something I did using SYNCSORT to copy a
flat file to an IAM file (VSAM replacement)
converting ZD to PD with a workaround, using CASE
commands, to pack a 16 character Cardholder
number when neither File-aid nor SYNCSORT would
handle a numeric field greater than 15 bytes. The
CASE feature could easily be used to translate
one value to another.

 SORT FIELDS=COPY
 OUTFIL FILES=1,
 OUTREC=(1,10,ZD,PD,12,5,ZD,PD,18,1,
         CHANGE=(1,C'1',X'01',
         C'2',X'02',
         C'3',X'03',
         C'4',X'04',
         C'5',X'05',
         C'6',X'06',
         C'7',X'07',
         C'8',X'08',
         C'9',X'09',
         C'0',X'00'),
         19,15,ZD,PD)

> interface.
>
> Someone suggested REPROing a record into a flat
file, editing it (in
> ISPF), then REPROing it back into the file.
Sounds like a workable
> solution in a low volume situation.
>
> LiamD
>



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Edit VSAM?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E476D0.3B2849CB@brazee.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```


petert@my-deja.com wrote:
> 
> Is there any easy way to edit/update a VSAM KSDS without writing a cobol
> program?  I just want to change 1 byte.......
> Thanks
> Peter

Third party tools allow you to edit KSDS.  But you can REPRO the file to
a flat file, edit it, then REPRO it back.
```

#### ↳ Re: Edit VSAM?

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s2hdc$s0l$1@nnrp1.deja.com>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```
In article <8s10vf$j0p$1@nnrp1.deja.com>,
  petert@my-deja.com wrote:
> Is there any easy way to edit/update a VSAM KSDS without writing a
cobol
> program?  I just want to change 1 byte.......
> Thanks
…[4 more quoted lines elided]…
>

MacKinney Systems has an inexpensive but very good VSAM Edit product as
well as many other products.

Their address is ===> http://www.mackinney.com/

HTH....

Bill


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Edit VSAM?

- **From:** "Seekermike" <seeker@dwx.com>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39e4e801@news.dwx.com>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```
Be very careful if you REPRO a VSAM file to DASD and use ISPF option 3.4 to
edit it!  Truncation of the rightmost bytes can occur!  I got bit by this
last week.  From now on, I'm using Fileaid to edit my files.


<petert@my-deja.com> wrote in message news:8s10vf$j0p$1@nnrp1.deja.com...
> Is there any easy way to edit/update a VSAM KSDS without writing a cobol
> program?  I just want to change 1 byte.......
…[5 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Edit VSAM?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E4EDBE.B7B5AE4D@brazee.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <39e4e801@news.dwx.com>`

```
If you have Fileaid, it is a no brainer.

I have had truncation problems when the system gets confused between
fixed and variable.  I forget the solution, but it is a good point -
always check your work and have a backup!

Seekermike wrote:
> 
> Be very careful if you REPRO a VSAM file to DASD and use ISPF option 3.4 to
…[11 more quoted lines elided]…
> > Before you buy.
```

###### ↳ ↳ ↳ Re: Edit VSAM?

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-10-12T02:30:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E5222A.773E2C8D@optonline.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <39e4e801@news.dwx.com> <39E4EDBE.B7B5AE4D@brazee.net>`

```
Howard Brazee wrote:
> 
> If you have Fileaid, it is a no brainer.
…[9 more quoted lines elided]…
> > last week.  From now on, I'm using Fileaid to edit my files.

If the VSAM file is variable, make sure your flat file is, too!

LiamD
```

#### ↳ Re: Edit VSAM?

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s2v4s017sv@enews4.newsguy.com>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```
It takes all of what, 20-30 minutes to code, compile, and run a COBOL 
program to do something like this.

In the time it took you to post the message, get a response, etc. you'd be
done by now.

We have File-Aid.  Used it once, will never use it again.  Displays and
if..then is fine for me.

Just some food for thought.

Jeff

----------
In article <8s10vf$j0p$1@nnrp1.deja.com>, petert@my-deja.com wrote:


> Is there any easy way to edit/update a VSAM KSDS without writing a cobol
> program?  I just want to change 1 byte.......
…[5 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Edit VSAM?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E5BB3E.17EB828A@brazee.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <8s2v4s017sv@enews4.newsguy.com>`

```


Jeff Baynard wrote:
> 
> It takes all of what, 20-30 minutes to code, compile, and run a COBOL
> program to do something like this.

Good point but...
 
> In the time it took you to post the message, get a response, etc. you'd be
> done by now.
> 
> We have File-Aid.  Used it once, will never use it again.  Displays and
> if..then is fine for me.

When I had it, I used it a lot.  It takes a minute to look at and/or
change a file, instead of the 20-30 minutes to create a program.  And
when I want to adjust my test data a different way, it takes me another
minute, instead of another 10-15 minutes to modify my program.

So he uses a minute writing his request (and if he's reading the
newsgroup anyway, the only other cost is having a couple of replies he's
interested in).  And from now on, he might know a way to modify his data
in 5 minutes instead of the 20-30 minute way he knows how to do now. 
(Next time he may want a more complicated edit/change)
```

##### ↳ ↳ Re: Edit VSAM?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-10-12T00:58:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C08F5.80$B_2.6130@iad-read.news.verio.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <8s2v4s017sv@enews4.newsguy.com>`

```
In article <8s2v4s017sv@enews4.newsguy.com>,
Jeff Baynard <union27@macconnect.com> wrote:

[snippage]

>We have File-Aid.  Used it once, will never use it again.

Now *that's* a Right Fair Trial and Evaluation if I ever heard of one...
oh, and I am the King of England, too.

>Displays and
>if..then is fine for me.

Might you be so kind as to say how you manage to get those DISPLAYs to
work under CICS 4.1?

DD
```

##### ↳ ↳ Re: Edit VSAM?

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-10-12T02:33:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E522C3.C711993A@optonline.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <8s2v4s017sv@enews4.newsguy.com>`

```
Jeff Baynard wrote:
> 
> It takes all of what, 20-30 minutes to code, compile, and run a COBOL
…[3 more quoted lines elided]…
> done by now.

If it's a test file, maybe (but I don't think I could do this
consistently in 20-30 minutes). If it's a production file, not so. If
it's online to CICS then it's MUCH more difficult.

LiamD
```

###### ↳ ↳ ↳ Re: Edit VSAM?

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<04C9F2FA10AA671A.228EDE83C35E31D3.B331D205D7A2C450@lp.airnews.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <8s2v4s017sv@enews4.newsguy.com> <39E522C3.C711993A@optonline.net>`

```
On Thu, 12 Oct 2000 02:33:00 GMT, Liam Devlin <liamddd@optonline.net>
enlightened us:

>Jeff Baynard wrote:
>> 
…[10 more quoted lines elided]…
>LiamD

Actually, if it is an online CICS VSAM file you need to fix and you
don't have a utility like File-Aid, CECI is about as simple as you can
get.  This assumes you know the key of the record you want to change
and you have security to run CECI.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

If the force in Yoda is so strong, construct a sentence with 
words in the proper order then why can't he?

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Edit VSAM?

_(reply depth: 4)_

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-10-13T02:16:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E6706F.FE4CAA5A@optonline.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <8s2v4s017sv@enews4.newsguy.com> <39E522C3.C711993A@optonline.net> <04C9F2FA10AA671A.228EDE83C35E31D3.B331D205D7A2C450@lp.airnews.net>`

```
SkippyPB wrote:
> 
> On Thu, 12 Oct 2000 02:33:00 GMT, Liam Devlin <liamddd@optonline.net>
…[19 more quoted lines elided]…
> and you have security to run CECI.

It's also possible to write a utility program which performs certain
simple & common repairs, e.g., marking the control record for an async
transaction that abended "complete", so it can be restarted. I'd much
rather do this than mess around with CECI and be a byte off, or
something. If you feel like it, you can also make your utility a little
more general purpose (which I have not done - the compliance people
aren't happy with the above, but we can justify it and demonstrate that
we do not have the ability to modify any financial data - if it were
general purpose they'd be in orbit). 

As always, YMMV,
LiamD
```

###### ↳ ↳ ↳ Re: Edit VSAM?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-10-12T03:14:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001011231444.03174.00002183@ng-fh1.aol.com>`
- **References:** `<39E522C3.C711993A@optonline.net>`

```
We have Fileaid - and just had a 3 hr free tutorial from CA on it as well - and
lots of free neato manuals.  I love it.

In any event....

If that 1 byte is part of the key (assuming a KSDS file) then you'd be better
off doing the IDCAMS REPRO to a flat file, change the byte, SORT it, and the
REPRO it back.

VSAM KSDS gets very upset if you don't have things in the proper order.


As for the DISPLAY question with CICS.  I believe it will work, think we had a
few programs with that in it (gotta check on this) and it goes to the console
assuming that's how the region is configured.  Definately not to any printers. 
Usually use the write to console command instead.  We have some very strange
CICS programs.

Eileen
```

#### ↳ Re: Edit VSAM?

- **From:** petert@my-deja.com
- **Date:** 2000-10-12T05:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8s3ggv$lcu$1@nnrp1.deja.com>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```
Thanks all for your suggestions.....
I ended up writing a small pgm in Cobol but might try the repro to QSAM
amd edit just for the exercise.
Ta
Peter

In article <8s10vf$j0p$1@nnrp1.deja.com>,
  petert@my-deja.com wrote:
> Is there any easy way to edit/update a VSAM KSDS without writing a
cobol
> program?  I just want to change 1 byte.......
> Thanks
…[4 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Edit VSAM?

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-10-13T02:17:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39E670B2.97B95BB6@optonline.net>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com> <8s3ggv$lcu$1@nnrp1.deja.com>`

```
petert@my-deja.com wrote:
> 
> Thanks all for your suggestions.....
> I ended up writing a small pgm in Cobol but might try the repro to QSAM
> amd edit just for the exercise.

Don't forget the "REPLACE" option when you REPRO your updated records
back into your VSAM dataset.

LiamD
```

#### ↳ Re: Edit VSAM?

- **From:** sbricklin@aol.com (SBRICKLIN)
- **Date:** 2000-10-13T01:17:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001012211741.26635.00001581@ng-fa1.aol.com>`
- **References:** `<8s10vf$j0p$1@nnrp1.deja.com>`

```
FileAid can help, you can use sort also
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
