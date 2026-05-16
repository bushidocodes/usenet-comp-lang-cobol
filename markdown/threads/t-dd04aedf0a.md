[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# status code 97

_16 messages · 5 participants · 2009-03_

---

### status code 97

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-03-05T16:55:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49B00413.6F0F.0085.0@efirstbank.com>`

```
Enterprise Cobol for z/OS...

Is there by chance an APAR or something that will make it so that a file
status of '97' (For VSAM only:  OPEN statement execution successful:  File
integrity verified.) is implicitly converted to a file status of '00'?

Although documented in the VSE Cobol manual, I have never in my life seen
this status returned when opening a VSAM file on VSE.

z/OS is another matter.  I just got my first one.  (The last job that used
the file was cancelled, obviously causing the need for "integrity
verification" when we reran the program.)

Because we've never seen it, none of our programs are coded to expect it.

Since I could not care less if the "file integrity was verified" I'd just as
soon receive the '00' status code, rather than making changes to hundreds of
programs to handle status '97' as being OK!

Ideas?

Frank
```

#### ↳ Re: status code 97

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-06T02:04:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<goq0b4$1n6$2@reader1.panix.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com>`

```
In article <49B00413.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>Enterprise Cobol for z/OS...

[snip]

>Since I could not care less if the "file integrity was verified" I'd just as
>soon receive the '00' status code, rather than making changes to hundreds of
>programs to handle status '97' as being OK!
>
>Ideas?

1) Make the solution JCL-dependent, eg run an IDCAMS VERIFY step before 
each program-running VSAM-using step.

2) Change the copybook that is part of your system standard for FILE 
STATUS checking to include 88  GOOD-IO VALUES '00' '97'.

('But... those solutions require... work!')

DD
```

#### ↳ Re: status code 97

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-03-05T20:07:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Iz%rl.20256$9j5.751@en-nntp-01.dc1.easynews.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com>`

```
Nope, It is relatively unusual (even on MVS), but when it happens, it happens. 
(As I recall, it MAY be impacted by SHAREOPTIONS and where/how you open and 
close and share VSAM files).

In your case, Frank, I would STRONGLY recommend that you have your "IBM 
contacts" submit an "MR" (Marketing Requirement) indicating that it is a 
"migration inhibitor" (VSE to MVS) *and* reference SHARE requirement:

 SSLNGC0413615  Optional (ISO 2002) "0x" file-status code for current "97"

As indicated in that requirement, IBM is "semi-non-conforming" when they issue a 
"9x" file status for a "successful" OPEN.  In fact, they play word games (or did 
at one time) and CLAIM that this is an "unsuccessful" OPEN< but that it is 
TREATED AS IF it were successful.

Of course, if IBM *did* provide a "0x" file status value for this, it would only 
work if you are checking the first byte of the returned value and NOT if you are 
checking for "00" after an OPEN.
```

##### ↳ ↳ Re: status code 97

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-03-09T13:17:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49B516FB.6F0F.0085.0@efirstbank.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <Iz%rl.20256$9j5.751@en-nntp-01.dc1.easynews.com>`

```
Thanks for the information, Bill.

I did some more testing and the only time I was able to intentionally create
a 'status 97' issue is when:
- The file is opened for I-O
- The job is *cancelled*

If both of these are true then the next time the job runs it gets a file
status '97' when opening the file.

This is not to say there are not other situations that will cause this to
occur...

Shareoptions seems not to matter.  (Or at least the two I checked (1 3) and
(2 3) got the same result.

At this point I am going to do the following:
1) Let programmers know what file status '97' means.  Let them know that if
their code does not handle this status as a successful open that they can
most likely just rerun the job and it will run OK (since Cobol did an
implicit verify when it opened it and got the '97').
2) Let programmers know that they can code status '97' as an "OK" status on
an open, and would possibly want to if they keep getting this status code.
3) Let programmers know on the other hand that the '97' status should be
rare, and if they are getting it often then most likely something else is
amiss.

In fact, the fact that it is rare and should not happen for 'normal'
processing tells me that you perhaps *shouldn't* just treat '97' as
"everything is ok" and ignore it.  Seems to me that even if you elect to
continue processing it would be nice to know that the 97 status occured.

The SHARE requirement seems worthwhile, but would not help in our situation
since we only consider '00' (and occasionally '05') to be valid.  I do
realize that 0x codes are all "open OK".  But honestly, just coding for '00'
and sometimes '05' has worked for us.  Seems to me an '04' or '07' can
always be avoided with proper coding and file definitions.  An '02' can
occur only on files that use alternatate indexes, and we have very few of
these.  In those few cases then '02' can be explicitly coded as being OK.

It is interesting to note that DECLARATIVES processing considers '97' to be
a valid open.  (Of course this appears to be contrary to the documentation
which states that an error procedure can be executed "Upon recognition of an
IBM-defined condition that causes file status key 1 to be set to 9.")  So if
we used declaratives processing for all file error handling we'd be good to
go!  :-)

No perfect answer, alas.  We'll see how it goes!

Frank
```

###### ↳ ↳ ↳ Re: status code 97

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-10T15:49:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gp6262$s59$1@reader1.panix.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <Iz%rl.20256$9j5.751@en-nntp-01.dc1.easynews.com> <49B516FB.6F0F.0085.0@efirstbank.com>`

```
In article <49B516FB.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:

[snip]

>At this point I am going to do the following:
>1) Let programmers know what file status '97' means.

Mr Swarbrick, it sounds like that a 'new' compiler has been introduced and 
minimal attention has been paid to informing/training the programming 
staff about its functions and capabilities, down to the simplest changes 
in what changes have been made to what FILE STATUS returns and how to deal 
with it.

Those who did so... deserve exactly what they get.  If you are dealing 
with bankers then explain it to them in banking terms: handling things in 
this manner is LOSING THEM MONEY and, quite possibly, COMPROMISING THE 
INTEGRITY OF FINANCIAL DATA.

I know I am old enough to have seen this happen again and again, at 
different institutions in different places... and still it doth make my 
blood nigh boil.

DD
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-03-10T17:18:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bGBtl.33810$rp7.6191@en-nntp-02.dc1.easynews.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <Iz%rl.20256$9j5.751@en-nntp-01.dc1.easynews.com> <49B516FB.6F0F.0085.0@efirstbank.com> <gp6262$s59$1@reader1.panix.com>`

```
Doc,
  If you have missed previous notes/threads, what is happening is more than a 
"change of compilers" it is a (partial?) migration from VSE to MVS.  I can't 
believe that this is being done without "training" - but with such a "major" 
change, it is entirely possible that WHAT to "teach" is hard to do.

For example, in this case, both the VSE and MVS versions of IBM's compilers 
document the "97" file status code, but (apparently) the VSE compiler/run-time 
wasn't encountering it, where the MVS one is.
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-11T00:23:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gp7094$md$4@reader1.panix.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <49B516FB.6F0F.0085.0@efirstbank.com> <gp6262$s59$1@reader1.panix.com> <bGBtl.33810$rp7.6191@en-nntp-02.dc1.easynews.com>`

```
In article <bGBtl.33810$rp7.6191@en-nntp-02.dc1.easynews.com>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>Doc,
>  If you have missed previous notes/threads, what is happening is more than a 
…[6 more quoted lines elided]…
>wasn't encountering it, where the MVS one is.

I recalled that this was about a VSE-to-MVS conversion, Mr Klein... in 
which case training, training and *more* training is needed.  That 
something like this is researched and the resulting policy dictated by a 
.sig reading Senior Analyst indicates, to me, that not enough is being 
done... but what do I know about how to do things successfully, I am a 
consultant/contractor/hired gun and when I leave the errors become 'mine' 
and the successes belong to whoever takes over my work.

DD
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 4)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-03-11T17:11:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49B7F0AB.6F0F.0085.0@efirstbank.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <Iz%rl.20256$9j5.751@en-nntp-01.dc1.easynews.com> <49B516FB.6F0F.0085.0@efirstbank.com> <gp6262$s59$1@reader1.panix.com>`

```
>>> On 3/10/2009 at 9:49 AM, in message <gp6262$s59$1@reader1.panix.com>,
<docdwarf@panix.com> wrote:
> In article <49B516FB.6F0F.0085.0@efirstbank.com>,
> Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
…[23 more quoted lines elided]…
> blood nigh boil.

Sort of, but not exactly.  We are migrating from z/VSE to z/OS, and
therefore migrating from Cobol for VSE/ESA to Enterprise Cobol for z/OS.  We
would like to automate any migration changes required to the Cobol code, and
it is my thought (and only mine) that trying to start handling status '97'
will be more difficult than it's worth.

Perhaps I am wrong.  At this point management has not been informed of the
issue, and thus no management decision has been made.  Certainly I will
inform management, but I wanted to get in some testing first to see how
often we run in to the status '97' issue.

At this point I do not see how any data could be corrupted.  Can you explain
better why treating status '97' as an error condition instead of a success
condition would cause said corruption?

Frank
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T01:10:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gp9ndr$mph$1@reader1.panix.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <49B516FB.6F0F.0085.0@efirstbank.com> <gp6262$s59$1@reader1.panix.com> <49B7F0AB.6F0F.0085.0@efirstbank.com>`

```
In article <49B7F0AB.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>>>> On 3/10/2009 at 9:49 AM, in message <gp6262$s59$1@reader1.panix.com>,
><docdwarf@panix.com> wrote:
…[12 more quoted lines elided]…
>> deal  with it.

[snip]

>Sort of, but not exactly.  We are migrating from z/VSE to z/OS, and
>therefore migrating from Cobol for VSE/ESA to Enterprise Cobol for z/OS.

If the compiler used in the Old Environment is not the same as the 
compiler used in the New Environment then... a 'new' compiler has been 
introduced.

>We
>would like to automate any migration changes required to the Cobol code, and
>it is my thought (and only mine) that trying to start handling status '97'
>will be more difficult than it's worth.

In an earlier posting I believe you mentioned that you were taking it upon 
yourself to notify other programmers what a 97 was.  If they don't know 
what it is... what happened, they all slept through class?  All of the 
notebooks and cheat-sheets got eaten by silverfish?  What is being done to 
make sure that the people who keep the data - THE LIFEBLOOD OF THE 
INSTITUTION - as clean as possible by learning what new tools are 
available?

>
>Perhaps I am wrong.  At this point management has not been informed of the
>issue, and thus no management decision has been made.

Now I am very confused... you are migrating platforms and management's not 
been informed?  What are you doing, sneaking in hardware through the 
loading-dock at night?

>Certainly I will
>inform management, but I wanted to get in some testing first to see how
>often we run in to the status '97' issue.

As someone who has coded for a few years might be able to tell you: any 
time you perform an IO operation against a dataset you will, most likely,  
be successful in that operation or you will not be successful.  If you are 
successful then you go on your merry way... assuming that success is what 
was desired.  If you are not successful then you Do Something Else, 
depending on what kind of 'unsuccess' you encounter (READ/NOTFND, 
WRITE/DUPEREC, etc.)

>
>At this point I do not see how any data could be corrupted.  Can you explain
>better why treating status '97' as an error condition instead of a success
>condition would cause said corruption?

At this point, Mr Swarbrick, my blood has cooled sufficiently to suggest 
to your management that Someone Needs Training and that keeping the bank's 
data - THE LIFEBLOOD OF THE INSTITUTION - pure needs careful, skilled and 
well-educated consideration.

Please also ask them if they had their money in an institution which paid 
such scant attention to its programmer's familiarity with the environment 
and tools necessary for keeping the data - THE LIFEBLOOD (etc) - pure as 
they seem to be doing... would they be looking for another place to 
deposit their funds?

I know it isn't your fault, Mr Swarbrick... I also know that the knowledge 
these people are looking for is hard-won and Worth Money.  Any 
instititution which seeks to maintain its technical capacities by 
instituting processes found written by 'some guy on the UseNet' deserves 
what it gets.

(I recall reading a ComputerWorld article, in the early 1980s, about the 
Chief of DP at Carnegie Mellon Bank in Pittsburgh. (note to those not 
familiar with the market: this was not, by any standard, at that time a 
small institution)  He had an idea about using one of them new-fangled PCs 
to manage microfiched data... and had to go through four levels of 
management to get approval for the US$20,000 test.  The system worked and 
generated an ROI of 500% in a single year... and yet he still had to do 
this dog-and-pony stuff for a piddling sum.)

(Start to tell folks 'There's only so much even one as mighty as I can do 
alone... what kind of training are we going to get for the rest of the 
crew?'  Keep hammering that home... oh, and brush up your brag-sheet, too, 
because - in my experience - they're either going to fire you for asking 
reasonable questions or they're going to expect folks to 'pick things up 
as they go along'... and the bank will be bought out within a very short 
time.)

DD
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-03-11T20:45:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1OZtl.5344$5Z3.3083@en-nntp-05.dc1.easynews.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <49B516FB.6F0F.0085.0@efirstbank.com> <gp6262$s59$1@reader1.panix.com> <49B7F0AB.6F0F.0085.0@efirstbank.com> <gp9ndr$mph$1@reader1.panix.com>`

```
Doc, (and others),
  I have deleted the entire thread up to this point, to simply repeat one of 
Frank's questions:

If an IBM  site make zero changes to COBOL to handle file status "97" what 
problems (especially corruption of data) can possibly happen?

Given the nature of this specific file status value, I can't see any possible 
problems.  I can see a "few" possible situations:

1) A COBOL program *only* treats "00" as successful, and, therefore, treats "97" 
as any other "error".  In such cases, the program will "end" or take whatever 
steps it does for other "bad" values.  Probably a restart will happen and all 
will be well.

2) A COBOL program doesn't do any file status checking and uses "system abend" 
as the way that non-expected file status values are handled.  Again, I think 
that no data will be corrupted and (probably) the program will be restarted 
(with a verified) file.

3) Something in the program allows the program to continue executing after an 
"undetected" fs=97.  In that case, the file was verified and opened successfully 
and the program should run as expected.

So, I repeat, in this SPECIFIC CASE (that of FS=97) exactly what problems may 
occur if NOTHING is done to existing program (as a mass project) and program are 
fixed when/if they actually encounter FS=97?
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T13:44:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpb3k5$dsj$1@reader1.panix.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <49B7F0AB.6F0F.0085.0@efirstbank.com> <gp9ndr$mph$1@reader1.panix.com> <1OZtl.5344$5Z3.3083@en-nntp-05.dc1.easynews.com>`

```
In article <1OZtl.5344$5Z3.3083@en-nntp-05.dc1.easynews.com>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>Doc, (and others),
>  I have deleted the entire thread up to this point, to simply repeat one of 
…[3 more quoted lines elided]…
>problems (especially corruption of data) can possibly happen?

What can possibly happen is/are any and all problems can happen which 
would be the result of a lack of training and familiarity of the 
programming staff with the tools they are expected to use to maintain data 
integrity.

My apologies to all if I've been a bit obscure about this... part of my 
personality, I guess, I am a mystery wrapped in an enigma with a chewy 
nougat center... but I see this question about a change in FILE STATUS 
values as a symptom of a much larger problem.

>
>Given the nature of this specific file status value, I can't see any possible 
>problems.

Given the nature of the specific question as a *symptom*, not an 
end-in-itsself, I see the institution in which it exists being 
extinguished in a remarkably short time... but maybe I'm just being a 
Gloomy Gus.  Numbness in an arm isn't anything special, just use the other 
arm for things which require sensitivity... until you realise that 
numbness in the arm is a symptom of a stroke and one's life might be 
threatened.

By the nature of this interchange I see Mr Swarbrick's institution's life 
being threatened by a poorly planned and slipshod implementation of an 
Operating System (and probably hardware) upgrade... and I *have*, in the 
past, seen companies go under because of such things.

Hence my advice: harp, continously, on training and get your brag-sheet in 
order.  To my mind this is as necessary as 'douse the fire, stir the 
ashes and douse again'.

DD
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 8)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-03-12T09:49:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<49B8DAC5.6F0F.0085.0@efirstbank.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <49B7F0AB.6F0F.0085.0@efirstbank.com> <gp9ndr$mph$1@reader1.panix.com> <1OZtl.5344$5Z3.3083@en-nntp-05.dc1.easynews.com> <gpb3k5$dsj$1@reader1.panix.com>`

```
>>> On 3/12/2009 at 7:44 AM, in message <gpb3k5$dsj$1@reader1.panix.com>,
<docdwarf@panix.com> wrote:
> In article <1OZtl.5344$5Z3.3083@en-nntp-05.dc1.easynews.com>,
> William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>>Doc, (and others),
>>  I have deleted the entire thread up to this point, to simply repeat one

> of 
>>Frank's questions:
…[40 more quoted lines elided]…
> ashes and douse again'.

I am honestly perplexed by this.  This is not a willy-nilly, slipshod
project.  We are not just going to recompile programs and move data to the
new environment and hope everything goes well.  We are going to test every
single program multiple times in the new environment.  As we run in to
unknowns, as we already have and certainly will continue to do, we will
address them appropriately at that time.  This is not the case of us hiring
a bunch of contractors to do a conversion of a system they've never used
before.  This is an inhouse system being converted by inhouse developers who
are very familiar with all aspects of the systems.

There's no possibly way we could be trained, ahead of time, on all of the
possible issues we'll run in to.  File status '97' and it's effects are
barely documented in IBM's own documentation.  What if we had this wondering
training on all of the features of Enterprise Cobol and they didn't mention
the use of file status '97'.  Would we be OK because we could just "blame"
our training?  And what makes you think we are not getting training, anyway?
 Certainly we are.  But no amount of training is going to cover everything
that we'll need to know.

I realize that you have a low opinion of all managers, but I can assure you
that we do not have the type of management that you appear to always work
for.  I've worked here for 17 years.  I know.

Frank
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-03-12T18:33:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gpbkhm$g35$1@reader1.panix.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <1OZtl.5344$5Z3.3083@en-nntp-05.dc1.easynews.com> <gpb3k5$dsj$1@reader1.panix.com> <49B8DAC5.6F0F.0085.0@efirstbank.com>`

```
In article <49B8DAC5.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:

[snip]

>I am honestly perplexed by this.  This is not a willy-nilly, slipshod
>project.

My error and apologies, Mr Swarbrick; if I was working from bad 
assumptions then my conclusions, however solid the logic used to reach 
them, may well be equally bad.

[snip]

>I realize that you have a low opinion of all managers, but I can assure you
>that we do not have the type of management that you appear to always work
>for.

I have not met all managers, Mr Swarbrick, and as a result I've not formed 
an opinion of such; as I've stated before my observations and conclusions 
are based on the managers I have encountered on my various assignments 
over the decades I've plied my trade.

DD
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 9)_

- **From:** Joel C Ewing <jREMOVEcCAPSewing@acm.org>
- **Date:** 2009-03-14T14:55:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_YTul.43264$l71.21161@newsfe23.iad>`
- **In-Reply-To:** `<49B8DAC5.6F0F.0085.0@efirstbank.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <49B7F0AB.6F0F.0085.0@efirstbank.com> <gp9ndr$mph$1@reader1.panix.com> <1OZtl.5344$5Z3.3083@en-nntp-05.dc1.easynews.com> <gpb3k5$dsj$1@reader1.panix.com> <49B8DAC5.6F0F.0085.0@efirstbank.com>`

```
Frank Swarbrick wrote:
>>>> On 3/12/2009 at 7:44 AM, in message <gpb3k5$dsj$1@reader1.panix.com>,
> <docdwarf@panix.com> wrote:
…[70 more quoted lines elided]…
> 
Having gone through VSE to MVS conversion many (20+) years ago, I 
remember being hit by this as well, although it seems like it seems like 
in our case it didn't hit until we changed to some flavor of COBOL II on 
MVS.

There is no exposure with treating a "97" as a failure and terminating 
the program, employing your usual problem diagnostic procedures 
including a VERIFY, and then restarting.  We found that the main 
confusion from the programmer's/maintainer's standpoint is that the 
documentation says that the problem was automatically resolved, which 
implies that a job restart would always work.  Unfortunately, the 
typical deliberately-programmed response from a detected OPEN "failure" 
was to either ABEND the program or terminate the program without a 
CLOSE, either of which could return the file to an opened-for-output and 
un-closed state, resulting in another OPEN 97 failure on restart.  By 
treating the "97" as a success, you get the benefit of the auto-verify 
and avoid a problem call; but neither approach should be an integrity 
exposure.

There typically has to be some other problem to get into this state in 
the first place.  With us the most typical case was that the job step 
would succeed on the OPEN of the file that would later get the "97" 
failure, but fail on some later file OPEN (file still OPEN in CICS, bad 
JCL, whatever), the program would terminate or ABEND during file-open 
initialization without closing anything, and the 97 failure would occur 
on a subsequent restart after the original failure had been fixed. 
Depending on your environment, this could be either a minor annoyance or 
a major one; but a circumvention that should always work with programs 
that have not yet been converted to accept OPEN 97's is to do a VERIFY 
on all VSAM files potentially opened by the failed step prior to a 
restart attempt, not just fixing the file that reported the original 
problem.
```

###### ↳ ↳ ↳ Re: status code 97

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-03-12T11:57:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p6jir4linprk0ukos1bnq5li3p4c92vae8@4ax.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com> <49B516FB.6F0F.0085.0@efirstbank.com> <gp6262$s59$1@reader1.panix.com> <49B7F0AB.6F0F.0085.0@efirstbank.com> <gp9ndr$mph$1@reader1.panix.com> <1OZtl.5344$5Z3.3083@en-nntp-05.dc1.easynews.com>`

```
On Wed, 11 Mar 2009 20:45:02 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>1) A COBOL program *only* treats "00" as successful, and, therefore, treats "97" 
>as any other "error".  In such cases, the program will "end" or take whatever 
>steps it does for other "bad" values.  Probably a restart will happen and all 
>will be well.

In most cases restarts aren't that expensive.   Sometimes they are.
Analysis is recommended.

(And don't disguise the '97' from the operators who need to decide
whether to restart or not).
```

#### ↳ Re: status code 97

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-03-06T09:59:34-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adl2r45b1frsh83hptjr922sb5ocrlv6uj@4ax.com>`
- **References:** `<49B00413.6F0F.0085.0@efirstbank.com>`

```
We have a called program which came with our system a couple of
decades ago which opens a VSAM file and passes back a failure value if
the status isn't "00".    Because it was used all over the place, we
lived with it rather than comply with the testing standards needed to
implement the change, while gradually moving away from using it.

One thing I did for a job that used it was add another step that
opened and closed the file.   It was a waste of resources, but it was
better than abending the job.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
