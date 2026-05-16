[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Converting old IBM code to ANSI 85

_29 messages · 9 participants · 2011-12 → 2012-01_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`Migration and conversion`](../topics.md#migration)

---

### Converting old IBM code to ANSI 85

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-12-29T13:12:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com>`

```
I am entering a program from a source listing for conversion
from IBM to Micro Focus. The SELECT clause is not compatible
with ANSI. Following are, what I believe, the essential parts
of the source for one problem.

...
       date-written. 12/25/76.
       date-compiled. 03/14/78.
...
       source-computer. ibm-360-f40.
       object-computer. ibm-360-f40.
       input-output section.
       file-control.
           select work-file assign to sys001-da-2314-d-ijsysxx
               access mode is random
               actual key is key-relative.
       i-o-control.
       data division.
       file section.
       fd  work-file recording mode is f
                   record contains 1250 characters
                   label records are standard
                   data record is work-rec.
       01  work-rec                    pic x(1250).
       working-storage section.
       01  key-relative.
           03  key-rel                 pic s9(9) comp.
           03  key-rel-x               redefines key-rel
                                       pic x(4).
           03  key-rel-key             pic x(4).
...
       write-disk.
           move rel-key-x to key-rel-key.
           compute key-rel = key-rel / 5.
           write work-rec from i-o-buffers (blk-id)
               invalid key display msg-1 upon console
               go to abort-job.
       xwrite-disk.
       read-disk.
           move rel-key-x to key-rel-key.
           compute key-rel = key-rel / 5.
           read work-file into i-o-buffers (blk-id)
               invalid key display msg-2 upon console
               go to abort-job.
       xread-disk.
...

According to GC28-6403-0 "IBM System/360 Disk Operating System
Subset American National Standard COBOL", organization "d" is
for direct files with relative track addressing. Then, in the
"actual key" clause, "key-relative" contains "key-rel" (the
relative track number) and "key-rel-key" (the record identifier).

Furthermore, the "key-rel / 5" in "write-disk" and "read-disk"
appears to limit the number of records per "2314" track to 5,
which seems about right from my memory (7200 / 1250 = 5.76).

Now, if I have done my "homework" correctly, the changes will
be:

a. Redo the SELECT clause for ANSI relative files with
   "relative key is key-rel".
b. Remove the references to "key-rel-x" and "key-rel-key".
c. Eliminate the COMPUTE statement in "write-disk" and
   "read-disk".

It is likely to be much more than a week before I complete
the entering of the source code; but I thought I would ask
for comments on this problem. So, any comments?
```

#### ↳ Re: Converting old IBM code to ANSI 85

- **From:** docdwarf@panix.com ()
- **Date:** 2011-12-30T01:07:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdj2sf$hb3$1@reader1.panix.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com>`

```
In article <1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com>,
Rick Smith  <rs847925@gmail.com> wrote:

[snip]

>...
>       date-written. 12/25/76.
>       date-compiled. 03/14/78.

In lower case, too!  IKFCBL00 was very tolerant.

>...
>       source-computer. ibm-360-f40.
>       object-computer. ibm-360-f40.

The names of the mighty rumble like distant thunder.

>       input-output section.
>       file-control.
>           select work-file assign to sys001-da-2314-d-ijsysxx
>               access mode is random

Bingo.

[snip]

>Now, if I have done my "homework" correctly, the changes will
>be:
…[5 more quoted lines elided]…
>   "read-disk".

This appears to be an appropriate remediation.

My next step would be to determine the transaction volume handled by this 
program and see if changes in technology in the past 
three-decades-and-change might allow for rewriting with indexed files.

DD
```

##### ↳ ↳ Re: Converting old IBM code to ANSI 85

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-12-30T03:54:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com>`

```
On Dec 29, 8:07 pm, docdw...@panix.com () wrote:
> In article <1cd2a4b3-c242-40a4-a3a4-68129794f...@z19g2000vbe.googlegroups.com>,
> Rick Smith  <rs847...@gmail.com> wrote:

[snip]

> >Now, if I have done my "homework" correctly, the changes will
> >be:
…[11 more quoted lines elided]…
> three-decades-and-change might allow for rewriting with indexed files.

There was never more than 3000 cards input. The program appears to
use the work file only for table overflow. The program ran in a 96Kb
partititon, as I recall. Since I have about 16Mb available, I may just
expand the table, though ISAM may be more reasonable considering my
intended use.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

- **From:** docdwarf@panix.com ()
- **Date:** 2011-12-30T12:47:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdkbt9$iu6$1@reader1.panix.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com>`

```
In article <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com>,
Rick Smith  <rs847925@gmail.com> wrote:
>On Dec 29, 8:07?pm, docdw...@panix.com () wrote:

[snip]

>> My next step would be to determine the transaction volume handled by this
>> program and see if changes in technology in the past
…[6 more quoted lines elided]…
>intended use.

That's a possibility, of course.  Assuming that this 3000-card input file 
is used mostly for lookups a way I've dealt with that in the past was to 
sort the file and load it into an Occurs Depending On table in the 
HOUSKEEPING section.

SEARCH ALL and you're on your way... and the table load routines are built 
so that when you get close to your limit the program starts to throw 
messages to show that the volume being passed might require redesign.

DD
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 4)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-12-30T10:17:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1954f173-bc21-4fd5-86ea-390ab624873a@o14g2000vbo.googlegroups.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <jdkbt9$iu6$1@reader1.panix.com>`

```
On Dec 30, 7:47 am, docdw...@panix.com () wrote:
> In article <f52bdb82-5a59-437d-88e5-7dcab2732...@d8g2000vbb.googlegroups.com>,
> Rick Smith  <rs847...@gmail.com> wrote:

[snip]

> >There was never more than 3000 cards input. The program appears to
> >use the work file only for table overflow. The program ran in a 96Kb
…[11 more quoted lines elided]…
> messages to show that the volume being passed might require redesign.

The program is segmented with segment numbers 0 and 50 - 54, in order.
I have almost finished entering segment 51, which builds the table.
Perhaps, when I finish entering segment 52, I will have a better idea
how the table is used. But, like a mystery, it is fun thinking about
the possibilities. Maybe a hash table would be a good choice.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-12-31T03:10:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdlufh$bvu$1@reader1.panix.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <jdkbt9$iu6$1@reader1.panix.com> <1954f173-bc21-4fd5-86ea-390ab624873a@o14g2000vbo.googlegroups.com>`

```
In article <1954f173-bc21-4fd5-86ea-390ab624873a@o14g2000vbo.googlegroups.com>,
Rick Smith  <rs847925@gmail.com> wrote:

[snip]

>The program is segmented with segment numbers 0 and 50 - 54, in order.
>I have almost finished entering segment 51, which builds the table.
>Perhaps, when I finish entering segment 52, I will have a better idea
>how the table is used. But, like a mystery, it is fun thinking about
>the possibilities. Maybe a hash table would be a good choice.

On the one hand... one does not know how to write the program until the 
program is written, sure, but it'd be a shame to enter segment 54 and find 
out that some fundamental assumptions used in previous constructs are now 
seen in different light.

On the other hand... what fun's a mystery if the answer is already known?  
As long as what's implemented into Prod can be maintained at 2:am by a 
two-year programmer then Life is Good.

DD
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 6)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-12-31T03:00:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<535036c3-6fd7-4cd9-abf4-7491b26993ef@b32g2000yqn.googlegroups.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <jdkbt9$iu6$1@reader1.panix.com> <1954f173-bc21-4fd5-86ea-390ab624873a@o14g2000vbo.googlegroups.com> <jdlufh$bvu$1@reader1.panix.com>`

```
On Dec 31, 3:10 am, docdw...@panix.com () wrote:
> On the other hand... what fun's a mystery if the answer is already known?
> As long as what's implemented into Prod can be maintained at 2:am by a
> two-year programmer then Life is Good.
>

You start them young at your shop? Child labour is so Dickensian.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-12-31T12:33:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdmvf2$a2c$1@reader1.panix.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <1954f173-bc21-4fd5-86ea-390ab624873a@o14g2000vbo.googlegroups.com> <jdlufh$bvu$1@reader1.panix.com> <535036c3-6fd7-4cd9-abf4-7491b26993ef@b32g2000yqn.googlegroups.com>`

```
In article <535036c3-6fd7-4cd9-abf4-7491b26993ef@b32g2000yqn.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Dec 31, 3:10?am, docdw...@panix.com () wrote:
>> On the other hand... what fun's a mystery if the answer is already known?
…[4 more quoted lines elided]…
>You start them young at your shop? Child labour is so Dickensian.

One plays the personnel-hand one is dealt by Management, aye.

DD
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 5)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2012-01-02T22:45:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YJvMq.271833$Dk.264080@en-nntp-02.dc1.easynews.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <jdkbt9$iu6$1@reader1.panix.com> <1954f173-bc21-4fd5-86ea-390ab624873a@o14g2000vbo.googlegroups.com>`

```
"Rick Smith" <rs847925@gmail.com> wrote in message 
news:1954f173-bc21-4fd5-86ea-390ab624873a@o14g2000vbo.googlegroups.com...
On Dec 30, 7:47 am, docdw...@panix.com () wrote:
> In article 
> <f52bdb82-5a59-437d-88e5-7dcab2732...@d8g2000vbb.googlegroups.com>,
> Rick Smith <rs847...@gmail.com> wrote:

[snip]

The program is segmented with segment numbers 0 and 50 - 54, in order.
I have almost finished entering segment 51, which builds the table.
Perhaps, when I finish entering segment 52, I will have a better idea
how the table is used. But, like a mystery, it is fun thinking about
the possibilities. Maybe a hash table would be a good choice.

Rick,
  When you are working with old IBM COBOL source code with segments, do make 
certain that you check on the rules for "reffeshable" and pemantent 
segments - and the segment-limit clause, etc. You might want to check out:
  http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3mg50/4.1.7

and look for several items related to segmentation.  When working with your 
"old" program you need to know if it was compiled with LANGLVL(1) or 
LANGLVL(2) to determine how some segmentation worked.  The former is 
"sorf-of" ANS'68 and the later is ANSI'74.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-12-30T09:43:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com>`

```
Rick Smith wrote:
>>
>> This appears to be an appropriate remediation.
…[10 more quoted lines elided]…
> intended use.

ISAM (or equivalent) will indeed be appropriate. Some may root for SEARCH or 
SEARCH ALL, but you may still reach an internal limit on array sizes. Plus, 
with ISAM, advances in operating systems and compilers will be doing the 
work in memory anyway. In other words, there won't be the overhead of disk 
access that was common on 60's era computers.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 4)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2011-12-30T10:54:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com>`

```
On Dec 30, 10:43 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Rick Smith wrote:

[snip]

> > There was never more than 3000 cards input. The program appears to
> > use the work file only for table overflow. The program ran in a 96Kb
…[8 more quoted lines elided]…
> access that was common on 60's era computers.

The current program does not save the output -- it prints a
report. For my intended use and after some adaptations, I want
to save the output for use in a program yet to be considered
and think ISAM would be a good choice for that purpose.

I have moved tables into files, both relative and indexed, in
production programs on PCs, without any complaints of degradation
in performance; so I know of what you speak. However, this is
not a production program, as such, and sometimes it is simply
more fun to do the exotic. <g>
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-12-30T20:06:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com>`

```
Rick Smith wrote:
> On Dec 30, 10:43 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
>> Rick Smith wrote:
…[25 more quoted lines elided]…
> more fun to do the exotic. <g>

I know what you mean. I once had a colleague who wrote a subroutine in 
Fortran using different numbers of ampersands for variable names. As in:

&&&& = SQRT (&& + 4 * &&)

I think he named the subroutine PHUQUE.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 6)_

- **From:** Doug Miller <doug_at_milmacdotcom@example.com>
- **Date:** 2011-12-30T22:23:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdlv76$3t4$1@dont-email.me>`
- **In-Reply-To:** `<LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com>`

```
On 12/30/2011 9:06 PM, HeyBub wrote:

> I know what you mean. I once had a colleague who wrote a subroutine in
> Fortran using different numbers of ampersands for variable names. As in:
>
> &&&&  = SQRT (&&  + 4 *&&)

I once worked with a programmer whose every program contained variables 
with names such as A0001, A00001, A000001, A0000001, A0000011, and the like.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 7)_

- **From:** Lüko Willms <lueko.willms@domain.invalid>
- **Date:** 2011-12-31T14:06:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4eff08e8$0$3702$6e1ede2f@read.cnntp.org>`
- **In-Reply-To:** `<jdlv76$3t4$1@dont-email.me>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me>`

```
Am 31.12.2011 04:23, schrieb Doug Miller:
> I once worked with a programmer whose every program contained variables
> with names such as A0001, A00001, A000001, A0000001, A0000011, and the
> like.

    And this not in Assembler, but in COBOL, right?


Cheers,
L.W.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2012-01-01T03:52:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdolag$opl$1@reader1.panix.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <4eff08e8$0$3702$6e1ede2f@read.cnntp.org>`

```
In article <4eff08e8$0$3702$6e1ede2f@read.cnntp.org>,
L?ko Willms  <lueko.willms@t-online.de> wrote:
>Am 31.12.2011 04:23, schrieb Doug Miller:
>> I once worked with a programmer whose every program contained variables
…[3 more quoted lines elided]…
>    And this not in Assembler, but in COBOL, right?

It has been said that a Real Programmer can write FORTRAN in any language.

DD
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 9)_

- **From:** Doug Miller <doug_at_milmacdotcom@example.com>
- **Date:** 2011-12-31T23:19:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdomu7$7k9$2@dont-email.me>`
- **In-Reply-To:** `<jdolag$opl$1@reader1.panix.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <4eff08e8$0$3702$6e1ede2f@read.cnntp.org> <jdolag$opl$1@reader1.panix.com>`

```
On 12/31/2011 10:52 PM, docdwarf@panix.com wrote:
> In article<4eff08e8$0$3702$6e1ede2f@read.cnntp.org>,
> L?ko Willms<lueko.willms@t-online.de>  wrote:
…[5 more quoted lines elided]…
>>     And this not in Assembler, but in COBOL, right?

No, that was in Assembler, but it's still a damned bad idea.
>
> It has been said that a Real Programmer can write FORTRAN in any language.
>
LOL! I've certainly had the misfortune of working with COBOL programs 
that were written like that.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 7)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-12-31T17:24:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me>`

```
Doug Miller wrote:
> On 12/30/2011 9:06 PM, HeyBub wrote:
>
…[6 more quoted lines elided]…
> A0000011, and the like.

It's was worse than I originally reported. We had an abbreviate print chain 
on our 1403 printer (for speed). My colleague's ampersands were rolled to 
pound signs (the print chain did not have the "&" character). Maintenance 
programmers, looking at the program listing and trying to make a change, 
experienced really big brain explosions.

Ever work with a hex dump of a program listing?
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 8)_

- **From:** Doug Miller <doug_at_milmacdotcom@example.com>
- **Date:** 2011-12-31T20:05:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdobik$sb1$1@dont-email.me>`
- **In-Reply-To:** `<A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com>`

```
On 12/31/2011 6:24 PM, HeyBub wrote:
> Doug Miller wrote:
>> On 12/30/2011 9:06 PM, HeyBub wrote:
…[16 more quoted lines elided]…
>
Many, many times. My first job after graduation was writing and 
maintaining business applications using ALC on an IBM 370-145. I stayed 
there nearly four years before moving on to a shop that was a little bit 
more up-to-date.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 9)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-12-31T21:40:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mo2dnQRew6VdSGLTnZ2dnUVZ_uGdnZ2d@earthlink.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com> <jdobik$sb1$1@dont-email.me>`

```
Doug Miller wrote:
> On 12/31/2011 6:24 PM, HeyBub wrote:
>> Doug Miller wrote:
…[20 more quoted lines elided]…
> little bit more up-to-date.

Maybe I wasn't clear: A hex dump of the SOURCE CODE!
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 10)_

- **From:** Doug Miller <doug_at_milmacdotcom@example.com>
- **Date:** 2011-12-31T23:18:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdomr9$7k9$1@dont-email.me>`
- **In-Reply-To:** `<mo2dnQRew6VdSGLTnZ2dnUVZ_uGdnZ2d@earthlink.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com> <jdobik$sb1$1@dont-email.me> <mo2dnQRew6VdSGLTnZ2dnUVZ_uGdnZ2d@earthlink.com>`

```
On 12/31/2011 10:40 PM, HeyBub wrote:
> Doug Miller wrote:
>> On 12/31/2011 6:24 PM, HeyBub wrote:
…[23 more quoted lines elided]…
> Maybe I wasn't clear: A hex dump of the SOURCE CODE!

Sorry, you did say "program listing" didn't you. My bad. No, I don't 
think I've ever done that. Not sure I can imagine why one might ever 
need to...
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 11)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-01-01T04:56:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<de2509ac-4679-409e-b3f9-b77934b7c434@a17g2000yqj.googlegroups.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com> <jdobik$sb1$1@dont-email.me> <mo2dnQRew6VdSGLTnZ2dnUVZ_uGdnZ2d@earthlink.com> <jdomr9$7k9$1@dont-email.me>`

```
On Jan 1, 4:18 am, Doug Miller <doug_at_milmacdot...@example.com>
wrote:
> On 12/31/2011 10:40 PM, HeyBub wrote:
>
…[34 more quoted lines elided]…
>

Don't Hex dumps of abends contain a hex dump of the program?
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 12)_

- **From:** Doug Miller <doug_at_milmacdotcom@example.com>
- **Date:** 2012-01-01T12:03:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jdq3ld$utp$1@dont-email.me>`
- **In-Reply-To:** `<de2509ac-4679-409e-b3f9-b77934b7c434@a17g2000yqj.googlegroups.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com> <jdobik$sb1$1@dont-email.me> <mo2dnQRew6VdSGLTnZ2dnUVZ_uGdnZ2d@earthlink.com> <jdomr9$7k9$1@dont-email.me> <de2509ac-4679-409e-b3f9-b77934b7c434@a17g2000yqj.googlegroups.com>`

```
On 1/1/2012 7:56 AM, Alistair Maclean wrote:
> On Jan 1, 4:18 am, Doug Miller<doug_at_milmacdot...@example.com>
> wrote:
…[38 more quoted lines elided]…
> Don't Hex dumps of abends contain a hex dump of the program?

Not the source code.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 11)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2012-01-02T21:24:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EOidneKxae9j6Z_SnZ2dnUVZ_v-dnZ2d@earthlink.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com> <jdobik$sb1$1@dont-email.me> <mo2dnQRew6VdSGLTnZ2dnUVZ_uGdnZ2d@earthlink.com> <jdomr9$7k9$1@dont-email.me>`

```
Doug Miller wrote:
> On 12/31/2011 10:40 PM, HeyBub wrote:
>> Doug Miller wrote:
…[28 more quoted lines elided]…
> need to...

To discover the difference between "&" and "#" in the source code inasmuch 
as they both map to the same print character. That is, "&#" in a program 
listing prints as "##". Absolutely ghastly.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 10)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2012-01-02T22:52:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9QvMq.111340$rt7.88731@en-nntp-05.dc1.easynews.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com> <jdobik$sb1$1@dont-email.me> <mo2dnQRew6VdSGLTnZ2dnUVZ_uGdnZ2d@earthlink.com>`

```
"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:mo2dnQRew6VdSGLTnZ2dnUVZ_uGdnZ2d@earthlink.com...
> Doug Miller wrote:
>> On 12/31/2011 6:24 PM, HeyBub wrote:
>>> Doug Miller wrote:
>>>> On 12/30/2011 9:06 PM, HeyBub wrote:
<snip>>
> Maybe I wasn't clear: A hex dump of the SOURCE CODE!
>
In the "olde dayse", (before Hex-literals) we would use full screen editors 
(or punch cards, or whatever) to put "non-printable" chacters into 
alphanumeric literals.  When you were working wth these, you HOPED for an 
online editor to be able to run "hex" on or off, so that you could see what 
was in the literals.  When working with a dump, you sure HOPED that it 
showed the hex value of what was in them.

Now, I will say, I have never worked with a "general" hex dumpof a procedure 
division source listing.  I hope the dump had the "printable" version to the 
side.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 8)_

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2012-01-02T13:22:57+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4f01a1b7$0$292$14726298@news.sunsite.dk>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <jdj2sf$hb3$1@reader1.panix.com> <f52bdb82-5a59-437d-88e5-7dcab2732d65@d8g2000vbb.googlegroups.com> <CqWdneeuh7yBQWDTnZ2dnUVZ_jWdnZ2d@earthlink.com> <1e02fba3-65f7-4400-9758-4fe51f92b333@d8g2000vbb.googlegroups.com> <LNednYcRbvKP82PTnZ2dnUVZ_rCdnZ2d@earthlink.com> <jdlv76$3t4$1@dont-email.me> <A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com>`

```
HeyBub wrote:

> Doug Miller wrote:
>> On 12/30/2011 9:06 PM, HeyBub wrote:
…[13 more quoted lines elided]…
> and trying to make a change, experienced really big brain explosions.

Such shortcuts were quite common in those days, especially when working
with printer chains of mostly 64 characters (and sometimes less than
64, missing the lower case letters).

> Ever work with a hex dump of a program listing?

Not me, while having the source cards at hand the & was quite
distinguishable from the pound character punch code. In those days we
were used to recognize those codes.
```

###### ↳ ↳ ↳ Re: Converting old IBM code to ANSI 85

_(reply depth: 8)_

- **From:** Fritz Wuehler <fritz@spamexpire-201201.rodent.frell.theremailer.net>
- **Date:** 2012-01-02T21:59:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fa5c878b7512555b3e9d36da6baf5330@msgid.frell.theremailer.net>`
- **References:** `<A7CdnUsGNdwIBGLTnZ2dnUVZ_tednZ2d@earthlink.com>`

```
> Ever work with a hex dump of a program listing? 

Program listings?! Ahaahaha. We don't need no steenkin' program listings!

> 
>
```

#### ↳ Re: Converting old IBM code to ANSI 85

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-01-02T13:01:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9ab9f29-4b69-4ed3-bfc6-c27b13f3767c@t16g2000vba.googlegroups.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com>`

```
On Dec 29 2011, 4:12 pm, Rick Smith <rs847...@gmail.com> wrote:

[snip]

> Now, if I have done my "homework" correctly, the changes will
> be:
…[5 more quoted lines elided]…
>    "read-disk".

At the end of segment 51 is became quite clear that the
disk file was holding two distinct "tables". Furthermore,
they were being maintained as doubly-linked lists. Thus,
each time a record was added, it was necessary to update
a pointer in the previous record. With the direct access
file, this was "read-update-write"; but, for a relative
file, this needed to be "read-update-rewrite". Though
not a big problem, I determined that the number of records
would be less that 200, so I commented all the statements
related to the file, added a table of 200 records, and
changed the 'write-disk' and 'read-disk' procedures to
reference the table. The actual number for the data I used
was 129. Problem solved and thanks to all!
```

#### ↳ Re: Converting old IBM code to ANSI 85

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2012-01-02T22:38:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tDvMq.297560$lT4.161572@en-nntp-07.dc1.easynews.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com>`

```
Rick,
  What you are doing is convering the old IBM extension for handling 
(proprietary BDAM files to ANSI/ISO Standard RElative Files.
The place you want to look is in the current Migration Guide, at:
   http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3mg50/4.1.4.2.1

What you have listed seems "right" on a cursory look, but I would suggest 
you check out the manual to see what else might be needed.

It has been a LONG time sicne I worked with "native COBOL language for BDAM, 
but as I recall it did NOT include file status field support, so you probaby 
want to add that as well.

"Rick Smith" <rs847925@gmail.com> wrote in message 
news:1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com...
>I am entering a program from a source listing for conversion
> from IBM to Micro Focus. The SELECT clause is not compatible
…[66 more quoted lines elided]…
> for comments on this problem. So, any comments?
```

##### ↳ ↳ Re: Converting old IBM code to ANSI 85

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-01-02T23:31:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38f6a154-d5e6-4dda-b11e-fc07ebba45ab@q11g2000vbq.googlegroups.com>`
- **References:** `<1cd2a4b3-c242-40a4-a3a4-68129794fbbd@z19g2000vbe.googlegroups.com> <tDvMq.297560$lT4.161572@en-nntp-07.dc1.easynews.com>`

```
On Jan 2, 11:38 pm, "Bill Klein" <wmkl...@noreply.ix.netcom.com>
wrote:
> Rick,
>   What you are doing is convering the old IBM extension for handling
> (proprietary BDAM files to ANSI/ISO Standard RElative Files.
> The place you want to look is in the current Migration Guide, at:
>    http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3mg50/4.1.4.2.1

I actually looked at that guide, last week. You had mentioned it
in a post a few years back. The guide was not particularly
helpful to me because IBM's conversion product would migrate
the file to VSAM or require separating the file and code into
an OS/VS program and link to Enterprise COBOL using LE.

I also looked at the Micro Focus Compatibility Guide where
it recommended conversion to relative files, but provided no
specific information reguarding the conversion of ACTUAL KEY
to RELATIVE KEY.

It was then I pulled out the old manuals to find what was
"really" required.

> What you have listed seems "right" on a cursory look, but I would suggest
> you check out the manual to see what else might be needed.

Having done the research, reviewed comments, and experienced
the effects of making the changes, I finally, as posted a few
hours ago, threw it all into a table!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
