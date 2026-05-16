[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How many records in a line sequentila file?

_20 messages · 7 participants · 2009-06_

---

### How many records in a line sequentila file?

- **From:** "Paul H" <NoSpamphobergNoSpam@att.net>
- **Date:** 2009-06-03T00:05:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net>`

```
Is there a way to ask exactly how many records are in a file, without having 
to open the file, then read and count the records?  TIA, Paul
```

#### ↳ Re: How many records in a line sequentila file?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-03T13:10:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h05sol$2rj$1@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net>`

```
In article <4a2604c0$0$23751$bbae4d71@news.suddenlink.net>,
Paul H <NoSpamphobergNoSpam@att.net> wrote:
>Is there a way to ask exactly how many records are in a file, without having 
>to open the file, then read and count the records?  TIA, Paul 

Getting a solution that Actually Works For You is usually facilitated by 
mentioning things like the Operating System under which you are working 
and the version of COBOL with which you're coding... but all that aside...

... if there exists in your environment a way to determine the size of 
file in question then it should not be too difficult to call/invoke that 
particular subroutine/API/method/object and cobble together something like 
DIVIDE WS-SIZE-OF-FILE BY FUNCTION LENGTH (RECORD-SIZE) GIVING 
WS-NUMBER-OF-RECORDS...

... or something like that.  Be warned that a) I coded the above from 
memory and consulting The Manual might save a bit of debugging time and b) 
depending on Stuff the call/invoke might not give an accurate result if 
the file has not been CLOSEd.

DD
```

##### ↳ ↳ Re: How many records in a line sequentila file?

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-06-03T08:19:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3NuVl.31040$Ws1.11130@nlpi064.nbdc.sbc.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h05sol$2rj$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:h05sol$2rj$1@reader1.panix.com...
> In article <4a2604c0$0$23751$bbae4d71@news.suddenlink.net>,
> Paul H <NoSpamphobergNoSpam@att.net> wrote:
>>Is there a way to ask exactly how many records are in a file, without 
>>having
>>to open the file, then read and count the records?  TIA, Paul

> ... if there exists in your environment a way to determine the size of
> file in question then it should not be too difficult to call/invoke that
> particular subroutine/API/method/object and cobble together something like
> DIVIDE WS-SIZE-OF-FILE BY FUNCTION LENGTH (RECORD-SIZE) GIVING
> WS-NUMBER-OF-RECORDS...

While that works for files with fixed record length, in general the answer 
for the 'generic' line sequential ("text") file is no.  BTW, in above 
formula, don't forget to include the size of the record separator in the 
record length before doing the match.

The very definition of "line sequential" files suggests they are used when 
you ALWAYS access the data starting at the beginning and read it in order; 
otherwise you would have selected a different "ORGANIZATION"  when you 
designed it.

Of course, there's no reason you could not maintain another file containing 
the current record count....

MCM
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-03T14:30:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h061ek$ati$1@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h05sol$2rj$1@reader1.panix.com> <3NuVl.31040$Ws1.11130@nlpi064.nbdc.sbc.com>`

```
In article <3NuVl.31040$Ws1.11130@nlpi064.nbdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:h05sol$2rj$1@reader1.panix.com...
>> In article <4a2604c0$0$23751$bbae4d71@news.suddenlink.net>,
…[14 more quoted lines elided]…
>record length before doing the match.

Now I'm confused... rare occurrence, eh?  Given:

FD  OUTFIL.
01  OUTREC1.
    05  FILLER1 PIC X(5).
    05  FILLER2 PIC 9(5).
    05  FILLER3 PIC X(5).

... I was concluding that if the SELECT did not include ORGANIZATION LINE 
SEQUENTIAL then FUNCTION LENGTH (OUTREC1) would return 15 while if the 
SELECT included ORGANIZATION LINE SEQUENTIAL the FUNCTION LENGTH would 
include it... but according to 
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/4.2.5.1.4?SHELF=&DT=20020920180651&CASE=&FS=TRUE> 
this is not the case FOR THIS COMPILER AND VERSION: 'The delimiter is not 
counted in the length of the record', directly contrary to my assumption.

>
>The very definition of "line sequential" files suggests they are used when 
>you ALWAYS access the data starting at the beginning and read it in order; 
>otherwise you would have selected a different "ORGANIZATION"  when you 
>designed it.

Curious... has anyone done any diddling about with ORGANIZATION LINE 
SEQUENTIAL and the results of an OPEN APPEND?  According to the URL given 
above it is not in the 'Verboten!' list... FOR THAT COMPILER AND VERSION, 
of course.

DD
```

##### ↳ ↳ Re: How many records in a line sequentila file?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-04T02:09:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78neg2F1n51p3U1@mid.individual.net>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h05sol$2rj$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <4a2604c0$0$23751$bbae4d71@news.suddenlink.net>,
> Paul H <NoSpamphobergNoSpam@att.net> wrote:
…[18 more quoted lines elided]…
> result if the file has not been CLOSEd.

... or if the records are variable length, which line sequential records 
actually are... :-)

Pete.
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-03T14:33:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h061k6$ati$2@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h05sol$2rj$1@reader1.panix.com> <78neg2F1n51p3U1@mid.individual.net>`

```
In article <78neg2F1n51p3U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> ... or something like that.  Be warned that a) I coded the above from
>> memory and consulting The Manual might save a bit of debugging time
…[4 more quoted lines elided]…
>actually are... :-)

'actually are'?  I'll accept 'can be', Mr Dashwood, given 
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/4.2.5.1.4?SHELF=&DT=20020920180651&CASE=&FS=TRUE> 
which states that 'Upon writing, any trailing blanks are removed prior to 
adding the record delimiter'... but if there are no trailing blanks what 
is there to vary in length?

DD
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 4)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-06-03T16:23:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<usxVl.28011$c45.21002@nlpi065.nbdc.sbc.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h05sol$2rj$1@reader1.panix.com> <78neg2F1n51p3U1@mid.individual.net> <h061k6$ati$2@reader1.panix.com>`

```
In article <h061k6$ati$2@reader1.panix.com>, docdwarf@panix.com () wrote:
>In article <78neg2F1n51p3U1@mid.individual.net>,
>Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[17 more quoted lines elided]…
>is there to vary in length?

FD ... RECORD VARYING ....
01 record-1          PIC X(80).
01 record-2          PIC X(60).
..
MOVE ALL "1" TO record-1
WRITE record-1
MOVE ALL "2" TO record-2
WRITE record-2
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-03T18:57:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h06h2o$roo$2@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <78neg2F1n51p3U1@mid.individual.net> <h061k6$ati$2@reader1.panix.com> <usxVl.28011$c45.21002@nlpi065.nbdc.sbc.com>`

```
In article <usxVl.28011$c45.21002@nlpi065.nbdc.sbc.com>,
Doug Miller <spambait@milmac.com> wrote:
>In article <h061k6$ati$2@reader1.panix.com>, docdwarf@panix.com () wrote:
>>In article <78neg2F1n51p3U1@mid.individual.net>,
>>Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>>>... or if the records are variable length, which line sequential records 
>>>actually are... :-)
…[15 more quoted lines elided]…
>WRITE record-2

Ummmmm... you left out the SELECT, which might have allowed one to 
determine whether these are defined as SEQUENTIAL or LINE SEQUENTIAL.

DD
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 6)_

- **From:** spambait@milmac.com (Doug Miller)
- **Date:** 2009-06-03T20:22:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oYAVl.28028$c45.2589@nlpi065.nbdc.sbc.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <78neg2F1n51p3U1@mid.individual.net> <h061k6$ati$2@reader1.panix.com> <usxVl.28011$c45.21002@nlpi065.nbdc.sbc.com> <h06h2o$roo$2@reader1.panix.com>`

```
In article <h06h2o$roo$2@reader1.panix.com>, docdwarf@panix.com () wrote:
>In article <usxVl.28011$c45.21002@nlpi065.nbdc.sbc.com>,
>Doug Miller <spambait@milmac.com> wrote:
…[27 more quoted lines elided]…
>determine whether these are defined as SEQUENTIAL or LINE SEQUENTIAL.

Ummmmm.... check the thread title. Including the SELECT would have been 
redundant.
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-04T13:27:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h08i37$58j$1@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <usxVl.28011$c45.21002@nlpi065.nbdc.sbc.com> <h06h2o$roo$2@reader1.panix.com> <oYAVl.28028$c45.2589@nlpi065.nbdc.sbc.com>`

```
In article <oYAVl.28028$c45.2589@nlpi065.nbdc.sbc.com>,
Doug Miller <spambait@milmac.com> wrote:
>In article <h06h2o$roo$2@reader1.panix.com>, docdwarf@panix.com () wrote:
>>In article <usxVl.28011$c45.21002@nlpi065.nbdc.sbc.com>,
…[31 more quoted lines elided]…
>redundant.

My error and apologies, Mr Miller... I'll have to give UseNet postings 
more of the attention that they e'er-so-frequently deserve.

DD
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-04T13:11:17+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78ol9nF1nianeU1@mid.individual.net>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h05sol$2rj$1@reader1.panix.com> <78neg2F1n51p3U1@mid.individual.net> <h061k6$ati$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <78neg2F1n51p3U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[16 more quoted lines elided]…
> blanks what is there to vary in length?

Oh Dear, trusting to the argument from Authority and not actually thinking 
about it? I shun your quoted reference, having used Line Sequential files 
for over 20 years and knowing how they actually operate. (I am not saying 
the reference is "wrong", just that you may not be familiar with this type 
of file organization...)

> but if there are no trailing
> blanks what is there to vary in length?

The individual string which comprises each record.

Consider...

This is a string
Here's another one
They're NOT the same length
Even AFTER the trailing blanks are stripped out
or not
Of course, any number of given records
COULD be exactly the same length
like this one (24 chars)
and this one  (24 chars)
but that would be purely coincidental and just a case where the variable 
length
happened to be the same variable

HTH,

Pete.
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-04T13:47:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h08j9b$r7u$1@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <78neg2F1n51p3U1@mid.individual.net> <h061k6$ati$2@reader1.panix.com> <78ol9nF1nianeU1@mid.individual.net>`

```
In article <78ol9nF1nianeU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <78neg2F1n51p3U1@mid.individual.net>,
…[21 more quoted lines elided]…
>about it?

No, Mr Dashwood... Reading The Fine Manual, citing it and in absence of 
anything other of an assertion of 'my experience is better!'... giving 
more weight to an IBM Manual than to a UseNet posting.

Heresy, I know.

>I shun your quoted reference, having used Line Sequential files 
>for over 20 years and knowing how they actually operate. (I am not saying 
>the reference is "wrong", just that you may not be familiar with this type 
>of file organization...)

I'll see your 'shun', Mr Dashwood, and raise you a 'under what OS can you 
post an example showing that the manual cited is wrong?'

DD
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-05T23:22:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78sdfuF1nssi2U1@mid.individual.net>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <78neg2F1n51p3U1@mid.individual.net> <h061k6$ati$2@reader1.panix.com> <78ol9nF1nianeU1@mid.individual.net> <h08j9b$r7u$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <78ol9nF1nianeU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[37 more quoted lines elided]…
> you post an example showing that the manual cited is wrong?'

Why would I do that, after stating quite explicitly that I don't think it is 
wrong?

I took care to point out that I don't believe the manual quoted is wrong, 
just your interpretation of it may not have been complete.

You asked a question; I answered it with examples.

Generally, a person might find that to be "helpful"...

You made no comment on that, preferring to expunge it and go with a 
reference to some pseudo poker game which you have already lost.

Pete.
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-05T14:02:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0b8i5$6fu$2@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <78ol9nF1nianeU1@mid.individual.net> <h08j9b$r7u$1@reader1.panix.com> <78sdfuF1nssi2U1@mid.individual.net>`

```
In article <78sdfuF1nssi2U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <78ol9nF1nianeU1@mid.individual.net>,
…[42 more quoted lines elided]…
>wrong?

For the reason that an OS can provide a platform for independent 
experimentation and verification which, to the best of my knowledge, 'what 
you think' cannot.

>
>I took care to point out that I don't believe the manual quoted is wrong, 
>just your interpretation of it may not have been complete.
>
>You asked a question; I answered it with examples.

I asked 'under what OS can you post an example showing that the manual 
cited is wrong?'... and there was no existing OS offered in answer.

[snip]

>You made no comment on that, preferring to expunge it and go with a 
>reference to some pseudo poker game which you have already lost.

If 'winning', Mr Dashwood, consists of accepting of 'I think' instead of 
'here is an OS - and even some code! - which demonstrates my assertions' 
then I believe I'll prefer losing just about any day.

DD
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz
- **Date:** 2009-06-05T14:09:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba7d2f2e-50c8-4d46-87b6-b16c14d7287d@s21g2000vbb.googlegroups.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <78ol9nF1nianeU1@mid.individual.net> <h08j9b$r7u$1@reader1.panix.com> <78sdfuF1nssi2U1@mid.individual.net> <h0b8i5$6fu$2@reader1.panix.com>`

```
On Jun 6, 2:02 am, docdw...@panix.com () wrote:
> In article <78sdfuF1nssi...@mid.individual.net>,

>
> ><http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3lr10/4...>
…[36 more quoted lines elided]…
> cited is wrong?'... and there was no existing OS offered in answer.

You are being a prat. The manual you quoted is for a specific system
and it ius unlikely to be wrong on issues for _that_ system.

Providing information for _other_ systems has no impact or effect on
the rightness or wrongness of the manual to that system, as has
already been pointed out several times.

The question you asked was 'what is there to vary in length'. The
answer already provided is: the record (01) area; and/or the implicit
record area of, say, a WRITE .. FROM. But this may vary in _different_
implementations.

For example ICL DRS20 CIS COBOL (ICL TP R92584/00) states (7.2.2) that
"Line Sequential files always map onto DRS20 SAM file." These are
nominally fixed length records without terminators but are Run Length
Encoded and maintained by the DRX OS with record header information.

So your manual would be wrong if it were describing _that_ system.

The Fujitsu Compilers (up to version 7 at least) on Windows and Linux
also, by default, do not strip trailing spaces from Line Sequential
files.

So your manual would be wrong if it were describing _that_ system.

You would be wrong if you were asserting that the manual you quoted
from is a general description on Line Sequential files on all systems.
If you were not asserting that then why you asking for a reference for
a _different_ system that made you manual 'wrong' ?

Your rather tedious arguments just shows that Peter's (and my)
experience is rather wider than yours.

LINE SEQUENTIAL is not part of ANS85 (though it is of 02) and is an
extension in all pre-02 compilers. Regardless of that, the
representation of the file on media is implementation dependent and
will vary as required by the system.

> [snip]
>
…[5 more quoted lines elided]…
> then I believe I'll prefer losing just about any day.

You had already lost the game before your alleged 'see and raise'
because Peter had 'seen you' with his """I am not saying the reference
is "wrong"""", and all you could show was a singleton manual against
Peter's 'full house'.
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-06T14:02:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78u129F1o735nU1@mid.individual.net>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <78ol9nF1nianeU1@mid.individual.net> <h08j9b$r7u$1@reader1.panix.com> <78sdfuF1nssi2U1@mid.individual.net> <h0b8i5$6fu$2@reader1.panix.com> <ba7d2f2e-50c8-4d46-87b6-b16c14d7287d@s21g2000vbb.googlegroups.com>`

```
riplin@Azonic.co.nz wrote:
> On Jun 6, 2:02 am, docdw...@panix.com () wrote:
>> In article <78sdfuF1nssi...@mid.individual.net>,
>
>>
<snipped>
>
> You had already lost the game before your alleged 'see and raise'
> because Peter had 'seen you' with his """I am not saying the reference
> is "wrong"""", and all you could show was a singleton manual against
> Peter's 'full house'.

I had to smile at this. :-)

It is a very graphic analogy. Nice one, Richard.

Can you imagine if the three of us sat down to an actual poker game?

I would have to insist that everyone played with their sleeves rolled up :-)

I believe the question as to what is left to vary has been well answered 
(not just by  my examples, but by other posts also).

I believe that Doc's quoted manual is accurate for the system it is written 
for (I said that already)

Is there need for futher acrimony?

Pete.
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-07T02:39:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0f993$32k$2@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h0b8i5$6fu$2@reader1.panix.com> <ba7d2f2e-50c8-4d46-87b6-b16c14d7287d@s21g2000vbb.googlegroups.com> <78u129F1o735nU1@mid.individual.net>`

```
In article <78u129F1o735nU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>riplin@Azonic.co.nz wrote:
>> On Jun 6, 2:02 am, docdw...@panix.com () wrote:
…[10 more quoted lines elided]…
>I had to smile at this. :-)

I was taught, Mr Dashwood, that smiling at the behaviors of those whose 
actions may be the results of already-have admitted syndromes which lead 
to odd actions to be in bad taste... but perhaps things are otherwise in 
the Antipodes.

Now... has anyone put together any code?   Been a while since it was 
suggested - I wonder by who - that it might help to have some around.

DD
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-07T02:31:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0f8qp$32k$1@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <78sdfuF1nssi2U1@mid.individual.net> <h0b8i5$6fu$2@reader1.panix.com> <ba7d2f2e-50c8-4d46-87b6-b16c14d7287d@s21g2000vbb.googlegroups.com>`

```
In article <ba7d2f2e-50c8-4d46-87b6-b16c14d7287d@s21g2000vbb.googlegroups.com>,
 <riplin@Azonic.co.nz> wrote:

[snip]

>You are being a prat.

M Pinston, I would say it is my opionion that you are, according to my 
sound reason, a person who exhitibts behaviors which 'prat' would be 
insufficient to describe... mbut this is a Family Newsgroup, what I would 
do is not, in this case, what I *will* do and I is hope your day is 
pleasant.

DD
```

##### ↳ ↳ Re: How many records in a line sequentila file?

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-03T11:33:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h0674932kt8@news5.newsguy.com>`
- **In-Reply-To:** `<h05sol$2rj$1@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h05sol$2rj$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <4a2604c0$0$23751$bbae4d71@news.suddenlink.net>,
> Paul H <NoSpamphobergNoSpam@att.net> wrote:
…[5 more quoted lines elided]…
> and the version of COBOL with which you're coding...

Indeed, it will depend on the representation of a line-sequential file
in this environment, and whether the metadata in question (number of
records) is maintained at all.

In Unix and Windows, for example, "line-sequential" files are
typically just OS files, using standard filesystems, which keep such
files as byte streams and have no notion of record delimiters. The
only size metadata those systems keep is the total file length, and
the records are variable-length, so there is no  alternative to
reading the file and counting the records.

Other environments may represent line-sequential files in other ways,
and keep other metadata.
```

###### ↳ ↳ ↳ Re: How many records in a line sequentila file?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-03T18:59:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h06h70$roo$3@reader1.panix.com>`
- **References:** `<4a2604c0$0$23751$bbae4d71@news.suddenlink.net> <h05sol$2rj$1@reader1.panix.com> <h0674932kt8@news5.newsguy.com>`

```
In article <h0674932kt8@news5.newsguy.com>,
Michael Wojcik  <mwojcik@newsguy.com> wrote:
>docdwarf@panix.com wrote:
>> In article <4a2604c0$0$23751$bbae4d71@news.suddenlink.net>,
…[10 more quoted lines elided]…
>records) is maintained at all.

Mr Wojcik, this is a well-thought-out, reasonable response without any 
nitpickery or questions about how the situation applies to the Albegensian 
Heresy.  Does it actually belong here?

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
