[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Date manipulation

_66 messages · 19 participants · 2003-12_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### Date manipulation

- **From:** Kindrick Ownby <kownby@sonic.net>
- **Date:** 2003-12-20T01:08:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net>`

```

I have a vague recollection from Y2K discussions
that there exists a numeric constant such that
if you multiplied a date in the form yymmdd by
it you could extract the same date in the form
mmddyy from the long product - does anyone here
have knowledge of this?

TIA,

Kindrick
```

#### ↳ Re: Date manipulation

- **From:** docdwarf@panix.com
- **Date:** 2003-12-19T21:17:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bs0bfj$ed7$1@panix5.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net>`

```
In article <DiNEb.3912$XF6.86150@typhoon.sonic.net>,
Kindrick Ownby  <kownby@sonic.net> wrote:
>
>I have a vague recollection from Y2K discussions
…[4 more quoted lines elided]…
>have knowledge of this?

Yes, I have knowledge of this... and my knowledge is that what you want 
can be found by searching http://groups.google.com for three of the terms 
you have mentioned here.

Now... please do your own homework.

DD
```

#### ↳ Re: Date manipulation

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-12-20T07:48:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9TEb.218537$Ec1.7823254@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net>`

```

Kindrick Ownby <kownby@sonic.net> wrote in message news:DiNEb.3912$XF6.86150@typhoon.sonic.net...
>
> I have a vague recollection from Y2K discussions
…[4 more quoted lines elided]…
> have knowledge of this?


01  DT-MMDDYY     PIC 9(06)  VALUE 0.
01  DT-YYMMDD     PIC 9(06)  VALUE 0.

** CHANGE MMDDYY to YYMMDD

     [Population of DT-MMDDYY goes here]

     COMPUTE DT-YYMMDD = DT-MMDDYY * 10000.01.

** CHANGE YYMMDD TO MMDDYY

     [Population of DT-YYMMDD goes here]

     COMPUTE DT-MMDDYY = DT-YYMMDD * 100.0001.
```

##### ↳ ↳ Re: Date manipulation

- **From:** Kindrick Ownby <kownby@sonic.net>
- **Date:** 2003-12-22T19:38:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YKHFb.4400$XF6.98704@typhoon.sonic.net>`
- **In-Reply-To:** `<g9TEb.218537$Ec1.7823254@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <g9TEb.218537$Ec1.7823254@bgtnsc05-news.ops.worldnet.att.net>`

```

Thanks to all who responded to my query for factors
that can be used to change a date of the form mmddyy
to the form yymmdd, and vice versa.

Re the move corresponding suggestions - I neglected
to say that the context is not COBOL, but rather a
date field within a query function on the archaic IBM
System/36 platform.

At 69 and about ready to hang it up, I got a chuckle
at the suggestion to do my own homework. :-)

Again, thanks to all.

Kindrick

Hugh Candlin wrote:
> Kindrick Ownby <kownby@sonic.net> wrote in message news:DiNEb.3912$XF6.86150@typhoon.sonic.net...
> 
…[22 more quoted lines elided]…
>      COMPUTE DT-MMDDYY = DT-YYMMDD * 100.0001.
```

###### ↳ ↳ ↳ Re: Date manipulation

- **From:** docdwarf@panix.com
- **Date:** 2003-12-22T18:36:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bs7v50$fik$1@panix5.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <g9TEb.218537$Ec1.7823254@bgtnsc05-news.ops.worldnet.att.net> <YKHFb.4400$XF6.98704@typhoon.sonic.net>`

```
In article <YKHFb.4400$XF6.98704@typhoon.sonic.net>,
Kindrick Ownby  <kownby@sonic.net> wrote:

[snip]

>At 69 and about ready to hang it up, I got a chuckle
>at the suggestion to do my own homework. :-)

At 69 you might marvel at those of greater antiquity who have learned how 
to search the Google archives of newsgroups.

DD
```

#### ↳ Re: Date manipulation

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-20T09:06:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031220100734.678$QU@news.newsreader.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net>`

```
"Kindrick Ownby" <kownby@sonic.net> wrote:
>
> I have a vague recollection from Y2K discussions
…[4 more quoted lines elided]…
> have knowledge of this?


      *
      ******************************************************************
      *                                                                *
      *                 M M D D Y Y   T O   Y Y M M D D                *
      *                                                                *
      *                                                                *
      *    CONVERTS A DATE IN FORM (MMDDYY) TO (YYMMDD) FORM           *
      *                                                                *
      *    NOTE: THE DATE FIELDS *MUST* BE DEFINED AS PIC 9(06)        *
      *                                                                *
      ******************************************************************
      *
           COMPUTE WS-YYMMDD = WS-MMDDYY * 10000.01 .
      *
      *
      ******************************************************************
      *                                                                *
      *                 Y Y M M D D   T O   M M D D Y Y                *
      *                                                                *
      *                                                                *
      *    CONVERTS A DATE IN FORM (YYMMDD) TO (MMDDYY) FORM           *
      *                                                                *
      *    NOTE: THE DATE FIELDS *MUST* BE DEFINED AS PIC 9(06)        *
      *                                                                *
      ******************************************************************
      *
           COMPUTE WS-MMDDYY = WS-YYMMDD * 100.0001 .

      *
      *
      ******************************************************************
      *                                                                *
      *             M M D D Y Y Y Y   T O   Y Y Y Y M M D D            *
      *                                                                *
      *                                                                *
      *    CONVERTS A DATE IN FORM (MMDDYYYY) TO (YYYYMMDD) FORM       *
      *                                                                *
      *    NOTE: THE DATE FIELDS *MUST* BE DEFINED AS PIC 9(08)        *
      *                                                                *
      ******************************************************************
      *
           COMPUTE WS-YYYYMMDD = WS-MMDDYYYY * 10000.0001 .
      *
      *
      ******************************************************************
      *                                                                *
      *             Y Y Y Y M M D D   T O   M M D D Y Y Y Y            *
      *                                                                *
      *                                                                *
      *    CONVERTS A DATE IN FORM (YYYYMMDD) TO (MMDDYYYY) FORM       *
      *                                                                *
      *    NOTE: THE DATE FIELDS *MUST* BE DEFINED AS PIC 9(08)        *
      *                                                                *
      ******************************************************************
      *
           COMPUTE WS-MMDDYYYY = WS-YYYYMMDD * 10000.0001 .
      *
```

#### ↳ Re: Date manipulation

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-12-20T21:02:35+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net>`

```
On Sat, 20 Dec 2003 01:08:51 GMT Kindrick Ownby <kownby@sonic.net> wrote:

:>I have a vague recollection from Y2K discussions
:>that there exists a numeric constant such that
:>if you multiplied a date in the form yymmdd by
:>it you could extract the same date in the form
:>mmddyy from the long product - does anyone here
:>have knowledge of this?

Yes.

But you are better off doing the three MOVEs - easier to understand and
faster.
```

##### ↳ ↳ Re: Date manipulation

- **From:** "Ron" <NoSpam@NoMoSpam.ORG>
- **Date:** 2003-12-20T15:14:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h7ecnYuqdOohJnmiXTWQlg@giganews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com>`

```
> But you are better off doing the three MOVEs - easier to understand and
> faster.

Agreed on the moves...
Actually only two moves are necessary but whatever...
move date1 (1:2) to date2 (5:2)
move date2 (3:4) to date2 (1:4) ...

or some varient thereof with group levels.
```

###### ↳ ↳ ↳ Re: Date manipulation

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-12-21T08:42:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FE54F87.6D050AD6@worldnet.att.net>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com>`

```
Ron wrote:
> 
> > But you are better off doing the three MOVEs - easier to understand and
…[7 more quoted lines elided]…
> or some varient thereof with group levels.

You are much better off doing the moves.  Computing the date might
fail if the date field contains non-numerics.  Also, on an IBM
mainframe, the generated code is much more efficient.  The optimizer
generates only two MVC (Move Character) instructions.  The compute
generates several instructions, and uses packed decimal arithmetic
which is slower that plain old moves.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-21T07:20:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IOKdna_N3uqQA3ii4p2dnA@giganews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <3FE54F87.6D050AD6@worldnet.att.net>`

```
Arnold Trembley wrote:
> Ron wrote:
>>
…[15 more quoted lines elided]…
> which is slower that plain old moves.

My two cents: I agree the two-move solution is superior in that it is easier
to maintain. But do not base coding decisions on micro-efficiency.

While micro-efficiency, as Arnold points out, is superior in this case, it
may well not be in another. Choosing a technique on the basis of what
happens down in the weeds is contra-indicated where it leads to
impentetrable code. And even then the results will mostly make no
discernable difference in the throughput.
```

###### ↳ ↳ ↳ Re: Date manipulation

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-12-21T08:53:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3FE551F0.8C9F3983@worldnet.att.net>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com>`

```
Ron wrote:
> 
> > But you are better off doing the three MOVEs - easier to understand and
…[7 more quoted lines elided]…
> or some varient thereof with group levels.

You are much better off doing the moves.  Computing the date might
fail if the date field contains non-numerics.  Also, on an IBM
mainframe, the generated code is much more efficient.  The optimizer
generates only two MVC (Move Character) instructions.  The compute
generates several instructions, and uses packed decimal arithmetic
which is slower that plain old moves.
```

###### ↳ ↳ ↳ Re: Date manipulation

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-22T13:32:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com>`

```
"Ron" <NoSpam@NoMoSpam.ORG> wrote:
>
> Actually only two moves are necessary but whatever...
> move date1 (1:2) to date2 (5:2)
> move date2 (3:4) to date2 (1:4) ...

I agree with you about the two moves, but I really don't think using
address modification on fixed field moves like this is a good idea,
from a maintenance standpoint. Address modification is great for use
in scan loops, and with STRING/UNSTRING, or otherwise where
you cannot use group levels effectively. And in a few other specific
and clear (and not likely to change) situations like extracting the first
character of a name. But for fixed field moves, always use:

> or some varient thereof with group levels.

Yes! :-)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-23T10:48:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fe7671e_3@news.athenanews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com...
> "Ron" <NoSpam@NoMoSpam.ORG> wrote:
> >
…[6 more quoted lines elided]…
> from a maintenance standpoint.

Why not? It is highly efficient (resolved at compile time) and self
documenting.

How does it complicate maintenance to know what offset and length of a field
is being moved?

> Address modification is great for use
> in scan loops, and with STRING/UNSTRING, or otherwise where
…[3 more quoted lines elided]…
>

Disagree strongly. These are arbitrary rules based  entirely on style (your
opinion) and presented as "good practice".

I have no problem with you doing things this way; I have a problem with you
presenting YOUR way as being the best (or only) way...

Pete.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-22T18:16:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dLudnZGLT8WhFHqi4p2dnA@giganews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <3fe7671e_3@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote in message
> news:d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com...
…[27 more quoted lines elided]…
> with you presenting YOUR way as being the best (or only) way...

I originally agreed with you, Pete. Then I thought it's possible a
maintenance programmer might be after all occurrances of

TODAYS-DATE-MM

And miss it if it was referenced as TODAYS-DATE(3:2).
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-23T16:14:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fe7b393_7@news.athenanews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <3fe7671e_3@news.athenanews.com> <dLudnZGLT8WhFHqi4p2dnA@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:dLudnZGLT8WhFHqi4p2dnA@giganews.com...
> Peter E.C. Dashwood wrote:
> > "Judson McClendon" <judmc@sunvaley0.com> wrote in message
> > news:d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com...
> >> "Ron" <NoSpam@NoMoSpam.ORG> wrote:
> >>>
<snip>

> I originally agreed with you, Pete. Then I thought it's possible a
> maintenance programmer might be after all occurrances of
…[4 more quoted lines elided]…
>
Yes, that COULD happen. But think it through...

If our maintenance programmer DID miss an instance, his fix wouldn't work.
(If it DID work, then the instance he missed did not require to be changed).

It wouldn't be too long before he found the problem.

It is not the "responsibility" of the person coding to try and consider HOW
a maintenance programmer MIGHT approach maintaining this code in the future;
it is the coder's responsibility to ensure that what he codes is clear and
well documented. (I contend that refmodding meets these critieria, but I
also agree that people not used to refmodding may find it strange. Should I
then bring my code down to the "lowest common deniminator" because the
person maintaining it is not properly trained and does not fully understand
the Language? I have worked on sites where PERFORM...VARYING was forbidden
for exactly this reason... I have seen sites where no ELSE was ever allowed
with IF, for the same reason. It just gets ridiculous... I call myself a
COBOL Programmer; it is not unreasonable to expect other people who do so
too to at least KNOW the Language.

If I was the hypothetical maintenance programmer we postulated above, I
would do my search on "TODAYS-DATE" and check every reference whether it
involved the month field or not. I would not miss the refmodding.

Pete.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-23T08:07:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L6-dnbXsu6eS0XWiRVn-iw@giganews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <3fe7671e_3@news.athenanews.com> <dLudnZGLT8WhFHqi4p2dnA@giganews.com> <3fe7b393_7@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
>> I originally agreed with you, Pete. Then I thought it's possible a
>> maintenance programmer might be after all occurrances of
…[11 more quoted lines elided]…
> It wouldn't be too long before he found the problem.

Your point is well-taken. However, I remind you of the FUNCTIONAL
INDETERMINACY THEOREM (F.I.T):

   "In Complex Systems, Malfunction And Even
   Total Nonfunction May Not Be Detectable For
   Long Periods, If Ever.

The programmer may never get another chance to find/fix the problem in that
the system may never give any indication it is failing.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-24T11:41:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fe8c506_7@news.athenanews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <3fe7671e_3@news.athenanews.com> <dLudnZGLT8WhFHqi4p2dnA@giganews.com> <3fe7b393_7@news.athenanews.com> <L6-dnbXsu6eS0XWiRVn-iw@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:L6-dnbXsu6eS0XWiRVn-iw@giganews.com...
> Peter E.C. Dashwood wrote:
> >> I originally agreed with you, Pete. Then I thought it's possible a
…[21 more quoted lines elided]…
> The programmer may never get another chance to find/fix the problem in
that
> the system may never give any indication it is failing.
>
Hahaha!

So, it isn't a problem then, is it <G>?

(Dunno 'bout you, but I only fix things when they DO give an indication they
are failing...)

Pete.

>
>
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 9)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-23T19:57:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qsOdndblJc0Eb3WiRVn-hw@giganews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <3fe7671e_3@news.athenanews.com> <dLudnZGLT8WhFHqi4p2dnA@giganews.com> <3fe7b393_7@news.athenanews.com> <L6-dnbXsu6eS0XWiRVn-iw@giganews.com> <3fe8c506_7@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
>>
>> Your point is well-taken. However, I remind you of the FUNCTIONAL
…[14 more quoted lines elided]…
> indication they are failing...)

Well, even if the system does give an "indication," one must recognize the
symptom. You should be familiar with "Hireling's Hypnosis:"

   "A trance-like state, a suspension of normal
   mental activity, induced by membership in
   a system."

Example: A large private medical clinic and hospital installed a new
computerized billing system. One day the system printed out a bill for
exactly $111.11 for every one of the more than 50,000 patients who had
attended the clinic during the preceding year.

Everybody working that day - operators, programmers, office clerks, and
twelve employees specially hired to handle the unexpectedly large volume of
bills to fold, stuff, and stamp them - did nothing to stop the error. The
system had hypnotized them. Garbage in, Gospel out.

Of course the people who GOT the bills were not hypnotized by the system (at
least most weren't).
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-24T12:59:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<43613b3050d91f187c2e51d26d71db6f@news.teranews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <3fe7671e_3@news.athenanews.com> <dLudnZGLT8WhFHqi4p2dnA@giganews.com> <3fe7b393_7@news.athenanews.com> <L6-dnbXsu6eS0XWiRVn-iw@giganews.com> <3fe8c506_7@news.athenanews.com> <qsOdndblJc0Eb3WiRVn-hw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:
>
> Example: A large private medical clinic and hospital installed a new
…[6 more quoted lines elided]…
> bills to fold, stuff, and stamp them - did nothing to stop the error...

This is an excellent example of why I *NEVER* give authorization for
companies to automatically take money from my checking account to
pay bills. That amount could have been $1,111.11 or $11,111.11 or
$111,111.11 or even $1,111,111.11 just as easily. Even if you don't
have $1,111,111.11 in your checking account (like I do ;-), there would
be overdraft charges. I would much rather they be after me for their
money than me be after them for my money. :-)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-24T08:26:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsc460$o7o$1@panix1.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <3fe8c506_7@news.athenanews.com> <qsOdndblJc0Eb3WiRVn-hw@giganews.com> <43613b3050d91f187c2e51d26d71db6f@news.teranews.com>`

```
In article <43613b3050d91f187c2e51d26d71db6f@news.teranews.com>,
Judson McClendon <judmc@sunvaley0.com> wrote:
>"JerryMouse" <nospam@bisusa.com> wrote:
>>
…[11 more quoted lines elided]…
>pay bills.

Well... first off I have my doubts about any tale that cites an un-named 
company at an unspecified time... and I have my doubts about a story where 
the workload suddenly and unpredictably increases and *nobody* complains 
about More Stuff To Do...

... but this automatic credit/debit stuff can work to your advantage, if 
you have the audacity to, say, commit tax fraud; I remember a consulting 
gig I had at (un-named company) in Kansas City, MO in (unspecified time) 
where one hospital had just bought out another one and was converting the 
bought-out hospital's payroll system - McCormick & Dodge? - to their own 
in-house system.  The buying hospital's programmers were confused by some 
odd results they were getting...

... and it turned out that the President of the bought-out hospital was 
the beneficiary of some rather... creative accounting; it seems that he'd 
had a pre-tax deduction applied to his payroll profile, one which would, 
every week, automatically take out one hundred pre-tax dollars...

... and then somehow - *must* have been an accident because *everyone* 
denied knowing *anything* about this - the VSAM file containing the 
employee profiles got changed... and the sign-nibble on the COMP-3 field 
for this deduction went from negative to positive, giving the man a 
'negative deduction'...

... so every time his paycheck was calculated the programs would subtract 
negative one hundred pre-tax dollars, in effect giving him an additional 
one hundred tax-free dollars.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 12)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-24T07:53:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gKOdnegEmebOB3SiRVn-hw@giganews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <3fe8c506_7@news.athenanews.com> <qsOdndblJc0Eb3WiRVn-hw@giganews.com> <43613b3050d91f187c2e51d26d71db6f@news.teranews.com> <bsc460$o7o$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <43613b3050d91f187c2e51d26d71db6f@news.teranews.com>,
> Judson McClendon <judmc@sunvaley0.com> wrote:
…[50 more quoted lines elided]…
> one hundred tax-free dollars.

I, too, am skeptical of an anecdotal folk tale that does not identify the
salient facts but consist only of a city, an industry, and a claim of
eye-witness access. The underlying example, however, of even an urban legend
can furnish good teachings.

Yet in your case, there was no malfunction. The program was doing exactly
what it was supposed to do. The claims of ignorance were obviously not
"Hireling Hypnosis," but instead were most likely "Cover Your Ass."

The French have a word for this, but I don't know what it is.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-24T08:57:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsc60s$cgk$1@panix1.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <43613b3050d91f187c2e51d26d71db6f@news.teranews.com> <bsc460$o7o$1@panix1.panix.com> <gKOdnegEmebOB3SiRVn-hw@giganews.com>`

```
In article <gKOdnegEmebOB3SiRVn-hw@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:
>> In article <43613b3050d91f187c2e51d26d71db6f@news.teranews.com>,
…[55 more quoted lines elided]…
>eye-witness access.

But *mine* can be verified by a Google search... see?

<http://groups.google.com/groups?selm=3574AD20.66B2%40erols.com&oe=UTF-8&output=gplain>

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 14)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-24T14:11:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<089959f2e1285850e205d33768489149@news.teranews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <43613b3050d91f187c2e51d26d71db6f@news.teranews.com> <bsc460$o7o$1@panix1.panix.com> <gKOdnegEmebOB3SiRVn-hw@giganews.com> <bsc60s$cgk$1@panix1.panix.com>`

```
<docdwarf@panix.com> wrote:
>
> But *mine* can be verified by a Google search... see?

Doc, may we assume from this that 'Google' = 'Gospel'?  ;-)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-24T09:58:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsc9hs$lgl$1@panix1.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <gKOdnegEmebOB3SiRVn-hw@giganews.com> <bsc60s$cgk$1@panix1.panix.com> <089959f2e1285850e205d33768489149@news.teranews.com>`

```
In article <089959f2e1285850e205d33768489149@news.teranews.com>,
Judson McClendon <judmc@sunvaley0.com> wrote:
><docdwarf@panix.com> wrote:
>>
>> But *mine* can be verified by a Google search... see?
>
>Doc, may we assume from this that 'Google' = 'Gospel'?  ;-)

I don't know about that... but it has been the source of good news, at 
times.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 14)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-24T17:21:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78OdnQAXMq3pgneiRVn-hA@giganews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <43613b3050d91f187c2e51d26d71db6f@news.teranews.com> <bsc460$o7o$1@panix1.panix.com> <gKOdnegEmebOB3SiRVn-hw@giganews.com> <bsc60s$cgk$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
>
> But *mine* can be verified by a Google search... see?
>
>
<http://groups.google.com/groups?selm=3574AD20.66B2%40erols.com&oe=UTF-8&out
put=gplain>
>

And mine can be verified by looking at a book:

"Systemantics," by John Gall, New York Times Books, 1975, p44
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-24T20:04:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsdd24$690$1@panix5.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <gKOdnegEmebOB3SiRVn-hw@giganews.com> <bsc60s$cgk$1@panix1.panix.com> <78OdnQAXMq3pgneiRVn-hA@giganews.com>`

```
In article <78OdnQAXMq3pgneiRVn-hA@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>docdwarf@panix.com wrote:
>>
…[9 more quoted lines elided]…
>"Systemantics," by John Gall, New York Times Books, 1975, p44

A 'book'?  I read one of those, once, and it didn't do anything for me... 
who uses those anymore, anyhow?

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 16)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-12-25T17:24:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0312251724.495f3971@posting.google.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <gKOdnegEmebOB3SiRVn-hw@giganews.com> <bsc60s$cgk$1@panix1.panix.com> <78OdnQAXMq3pgneiRVn-hA@giganews.com> <bsdd24$690$1@panix5.panix.com>`

```
docdwarf@panix.com wrote in message news:<bsdd24$690$1@panix5.panix.com>...
> In article <78OdnQAXMq3pgneiRVn-hA@giganews.com>,
> JerryMouse <nospam@bisusa.com> wrote:
…[16 more quoted lines elided]…
> DD


Books are used to hold down tinfoil caps in strong winds.

(By strong I mean over 30 Knots.  Below that speed, Egg Salad works fine).
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-25T20:48:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsg40u$586$1@panix5.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <78OdnQAXMq3pgneiRVn-hA@giganews.com> <bsdd24$690$1@panix5.panix.com> <bfdfc3e8.0312251724.495f3971@posting.google.com>`

```
In article <bfdfc3e8.0312251724.495f3971@posting.google.com>,
Thane Hubbell <thaneh@softwaresimple.com> wrote:
>docdwarf@panix.com wrote in message news:<bsdd24$690$1@panix5.panix.com>...
>> In article <78OdnQAXMq3pgneiRVn-hA@giganews.com>,
…[21 more quoted lines elided]…
>(By strong I mean over 30 Knots.  Below that speed, Egg Salad works fine).

Under 30 knots, then, things are fit to be tied.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 18)_

- **From:** Habitant <berlutte@sympatico.ca>
- **Date:** 2003-12-27T19:37:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba9suv46qg18a9vq051ohh5bfejvdhvql4@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <78OdnQAXMq3pgneiRVn-hA@giganews.com> <bsdd24$690$1@panix5.panix.com> <bfdfc3e8.0312251724.495f3971@posting.google.com> <bsg40u$586$1@panix5.panix.com>`

```
On 25 Dec 2003 20:48:14 -0500, docdwarf@panix.com wrote:

>>(By strong I mean over 30 Knots.  Below that speed, Egg Salad works fine).
>
>Under 30 knots, then, things are fit to be tied.

Kites comes to mind, aye!
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 12)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2003-12-26T10:26:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h43ouvcesecmn1s1mq2hfvij176u91c3un@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <3fe8c506_7@news.athenanews.com> <qsOdndblJc0Eb3WiRVn-hw@giganews.com> <43613b3050d91f187c2e51d26d71db6f@news.teranews.com> <bsc460$o7o$1@panix1.panix.com>`

```
On 24 Dec 2003 08:26:24 -0500, docdwarf@panix.com wrote:

>... and it turned out that the President of the bought-out hospital was 
>the beneficiary of some rather... creative accounting; it seems that he'd 
…[8 more quoted lines elided]…
>

That doesn't work, does it? A tax-free deduction is before the tax
calculation, a tax-free addition is after the tax calculation -
there's more than a sign involved.
>... so every time his paycheck was calculated the programs would subtract 
>negative one hundred pre-tax dollars, in effect giving him an additional 
>one hundred tax-free dollars.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-26T09:00:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bshet8$58g$1@panix5.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <43613b3050d91f187c2e51d26d71db6f@news.teranews.com> <bsc460$o7o$1@panix1.panix.com> <h43ouvcesecmn1s1mq2hfvij176u91c3un@4ax.com>`

```
In article <h43ouvcesecmn1s1mq2hfvij176u91c3un@4ax.com>,
Ian Dalziel  <iandalziel@lineone.net> wrote:
>On 24 Dec 2003 08:26:24 -0500, docdwarf@panix.com wrote:
>
…[14 more quoted lines elided]…
>there's more than a sign involved.

That's one way of doing it... but as there are some deductions which are
taxable and others which are not taxable I can see a structure in the
program which would determine this by, say, a flag set for the deduction
and queried during processing (IF DEDN-TXBL-SW = 'Y' PERFORM
DEDUCT-THE-TAX-RITUAL or suchlike); such a structure would allow, at the
level for the data, a change in the status of a deduction from taxable to
non-taxable without any code alterations.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 14)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2003-12-26T14:38:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jhouvgk3h1ub1ggrc96ahilfpj0vgi8sn@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <43613b3050d91f187c2e51d26d71db6f@news.teranews.com> <bsc460$o7o$1@panix1.panix.com> <h43ouvcesecmn1s1mq2hfvij176u91c3un@4ax.com> <bshet8$58g$1@panix5.panix.com>`

```
On 26 Dec 2003 09:00:08 -0500, docdwarf@panix.com wrote:

>In article <h43ouvcesecmn1s1mq2hfvij176u91c3un@4ax.com>,
>Ian Dalziel  <iandalziel@lineone.net> wrote:
…[25 more quoted lines elided]…
>

Doesn't work like that, though, does it? "Taxable" and "Non-taxable"
are shorthand for pre- and post- tax deductions. My point (feeble
though it may have been) was that benefit to the recipient works the
opposite way round for payments and deductions - a pre-tax deduction
is "non-taxable" but a pre-tax payment is "taxable".

Even if you performed the tax calculation separately on each
payment/deduction, the difference would be the same - if you're paying
it out, it's good if what comes out of your pocket is reduced by the
tax percentage. If you're receiving it, you'd prefer what arrives in
your pocket not to have been reduced.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-26T14:23:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsi1sc$7dj$1@panix5.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <h43ouvcesecmn1s1mq2hfvij176u91c3un@4ax.com> <bshet8$58g$1@panix5.panix.com> <8jhouvgk3h1ub1ggrc96ahilfpj0vgi8sn@4ax.com>`

```
In article <8jhouvgk3h1ub1ggrc96ahilfpj0vgi8sn@4ax.com>,
Ian Dalziel  <iandalziel@lineone.net> wrote:
>On 26 Dec 2003 09:00:08 -0500, docdwarf@panix.com wrote:
>
…[29 more quoted lines elided]…
>Doesn't work like that, though, does it?

That depends on the system, I believe.

>"Taxable" and "Non-taxable"
>are shorthand for pre- and post- tax deductions.

That is one way to see them... another way is 'are taxes of any sort to be 
applied to this income' or 'is this income to be considered free of 
taxation'.

>My point (feeble
>though it may have been) was that benefit to the recipient works the
>opposite way round for payments and deductions - a pre-tax deduction
>is "non-taxable" but a pre-tax payment is "taxable".

... and my point is that this is one way of doing it.  Another way is to 
say 'here we have a quantity to be applied against the paycheck; is this 
quantity taxable or not?  if it is taxable then apply the quantity in a 
fashion which shows taxation, if not then not.'

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 16)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2003-12-26T22:34:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <h43ouvcesecmn1s1mq2hfvij176u91c3un@4ax.com> <bshet8$58g$1@panix5.panix.com> <8jhouvgk3h1ub1ggrc96ahilfpj0vgi8sn@4ax.com> <bsi1sc$7dj$1@panix5.panix.com>`

```
On 26 Dec 2003 14:23:56 -0500, docdwarf@panix.com wrote:

>... and my point is that this is one way of doing it.  Another way is to 
>say 'here we have a quantity to be applied against the paycheck; is this 
>quantity taxable or not?  if it is taxable then apply the quantity in a 
>fashion which shows taxation, if not then not.'

You're not listening, are you? Think about it - is it good to apply
the quantity in a way which shows taxation, or is it not? Apply the
question to payments and deductions, and see whether the answer is the
same.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-26T18:21:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsifqh$sc5$1@panix5.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8jhouvgk3h1ub1ggrc96ahilfpj0vgi8sn@4ax.com> <bsi1sc$7dj$1@panix5.panix.com> <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com>`

```
In article <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com>,
Ian Dalziel  <iandalziel@lineone.net> wrote:
>On 26 Dec 2003 14:23:56 -0500, docdwarf@panix.com wrote:
>
…[5 more quoted lines elided]…
>You're not listening, are you?

I'm trying to... and respond, as well.

>Think about it - is it good to apply
>the quantity in a way which shows taxation, or is it not?

If the status is untaxed then it should be applied as such, either 
positively or negatively.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 18)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2003-12-27T10:53:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8jhouvgk3h1ub1ggrc96ahilfpj0vgi8sn@4ax.com> <bsi1sc$7dj$1@panix5.panix.com> <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com> <bsifqh$sc5$1@panix5.panix.com>`

```
On 26 Dec 2003 18:21:53 -0500, docdwarf@panix.com wrote:

>In article <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com>,
>Ian Dalziel  <iandalziel@lineone.net> wrote:
…[16 more quoted lines elided]…
>

<sigh> :-)

Sure, but an "untaxed" deduction in that sense effectively comes out
of TAXED income - if it is paid with no reference to tax, it reduces
the net payment by its full amount.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 19)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-27T08:33:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsk1mq$59d$1@panix5.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com> <bsifqh$sc5$1@panix5.panix.com> <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com>`

```
In article <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com>,
Ian Dalziel  <iandalziel@lineone.net> wrote:
>On 26 Dec 2003 18:21:53 -0500, docdwarf@panix.com wrote:
>
…[24 more quoted lines elided]…
>the net payment by its full amount.

And as I stated earlier that is one way to consider a deduction.  Another
way to consider it is that a deduction is a portion of income which is
subject to tax calculations, just as certain kinds of income (dividends,
say, or 1099-paid income) are not subject to tax calculations.  If the
portion of income which is not subject to tax calculations is to be 
subtracted (a deduction) and this portion is a negative amount then the 
result is a net addition.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 20)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2003-12-27T14:04:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g34ruvktos452r31ej95sgp5c0dfbda8uu@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com> <bsifqh$sc5$1@panix5.panix.com> <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com> <bsk1mq$59d$1@panix5.panix.com>`

```
On 27 Dec 2003 08:33:14 -0500, docdwarf@panix.com wrote:

>In article <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com>,
>Ian Dalziel  <iandalziel@lineone.net> wrote:
…[35 more quoted lines elided]…
>

Absolutely - no argument about that at all. Now let's go back and look
at what we were talking about :

"... and it turned out that the President of the bought-out hospital
was the beneficiary of some rather... creative accounting; it seems
that he'd had a pre-tax deduction applied to his payroll profile, one
which would, every week, automatically take out one hundred pre-tax
dollars...

... and then somehow - *must* have been an accident because *everyone*
denied knowing *anything* about this - the VSAM file containing the 
employee profiles got changed... and the sign-nibble on the COMP-3
field for this deduction went from negative to positive, giving the
man a 'negative deduction'...

... so every time his paycheck was calculated the programs would
subtract negative one hundred pre-tax dollars, in effect giving him an
additional one hundred tax-free dollars."

OK? Now what I am saying is A PRE-TAX ADDITION IS NOT TAX-FREE!
It would have to be post-tax to be tax-free  -  if it is pre-tax the
tax calculation will deduct tax from it.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 21)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-27T09:21:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsk4gp$8i2$1@panix1.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com> <bsk1mq$59d$1@panix5.panix.com> <g34ruvktos452r31ej95sgp5c0dfbda8uu@4ax.com>`

```
In article <g34ruvktos452r31ej95sgp5c0dfbda8uu@4ax.com>,
Ian Dalziel  <iandalziel@lineone.net> wrote:
>On 27 Dec 2003 08:33:14 -0500, docdwarf@panix.com wrote:
>
…[60 more quoted lines elided]…
>tax calculation will deduct tax from it.

Ahhhhhhh, I see!  My error and apologies for the sloppiness of my 
terminology; my intention in using the term 'pre-tax' (which you are 
entirely correct in interpreting as 'applied before taxes') was to 
indicate that the deduction was 'untaxed'.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 22)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2003-12-27T14:31:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jp5ruvs0f8vosrqoi3310nek89np1fss6h@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com> <bsk1mq$59d$1@panix5.panix.com> <g34ruvktos452r31ej95sgp5c0dfbda8uu@4ax.com> <bsk4gp$8i2$1@panix1.panix.com>`

```
On 27 Dec 2003 09:21:13 -0500, docdwarf@panix.com wrote:

>In article <g34ruvktos452r31ej95sgp5c0dfbda8uu@4ax.com>,
>Ian Dalziel  <iandalziel@lineone.net> wrote:
…[68 more quoted lines elided]…
>

<phew!>
You would be right with a deduction - that's what I tried to say
(obviously not very clearly). To be "untaxed" a deduction has to be
pre-tax, but an addition has to be post-tax.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 23)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-27T21:53:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bslgjt$aoi$1@panix1.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <g34ruvktos452r31ej95sgp5c0dfbda8uu@4ax.com> <bsk4gp$8i2$1@panix1.panix.com> <jp5ruvs0f8vosrqoi3310nek89np1fss6h@4ax.com>`

```
In article <jp5ruvs0f8vosrqoi3310nek89np1fss6h@4ax.com>,
Ian Dalziel  <iandalziel@lineone.net> wrote:
>On 27 Dec 2003 09:21:13 -0500, docdwarf@panix.com wrote:
>
…[76 more quoted lines elided]…
>

Well... glad we got that one straightened out.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 21)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-12-27T14:49:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8_gHb.15562$aw2.8776302@newssrv26.news.prodigy.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com> <bsifqh$sc5$1@panix5.panix.com> <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com> <bsk1mq$59d$1@panix5.panix.com> <g34ruvktos452r31ej95sgp5c0dfbda8uu@4ax.com>`

```
"Ian Dalziel" <iandalziel@lineone.net> wrote in message
news:g34ruvktos452r31ej95sgp5c0dfbda8uu@4ax.com...
>
> OK? Now what I am saying is A PRE-TAX ADDITION IS NOT TAX-FREE!

Near as I can figure, in the U.S. **NOTHING** is 'tax- free'  and the best
you can hope for is "tax deferred."

MCM
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 19)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-12-27T06:03:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0312270603.2a008e61@posting.google.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8jhouvgk3h1ub1ggrc96ahilfpj0vgi8sn@4ax.com> <bsi1sc$7dj$1@panix5.panix.com> <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com> <bsifqh$sc5$1@panix5.panix.com> <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com>`

```
I suspect that any individual or organisation would be best advised to
do their tax calculations and calculate taxable and non-taxable
payments the way their country's tax office tells them to do it, or
hire accountants and lawyers to advise them appropriately if they
think otherwise.

Robert
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 20)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2003-12-27T14:10:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fl4ruvs0c73vuv5g4b7l63fvuguqr9atse@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8jhouvgk3h1ub1ggrc96ahilfpj0vgi8sn@4ax.com> <bsi1sc$7dj$1@panix5.panix.com> <5ndpuvs9apbu2h66u3s9d0ammq4ho7fhje@4ax.com> <bsifqh$sc5$1@panix5.panix.com> <hvoquv0ri8tnhagbufe40r5bfl0pec3rmv@4ax.com> <fcd09c56.0312270603.2a008e61@posting.google.com>`

```
On 27 Dec 2003 06:03:31 -0800, robert@jones0086.freeserve.co.uk
(Robert Jones) wrote:

>I suspect that any individual or organisation would be best advised to
>do their tax calculations and calculate taxable and non-taxable
…[3 more quoted lines elided]…
>

I suspect you are entirely correct.

And?
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 9)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-12-24T04:06:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031223230607.26181.00001425@mb-m15.aol.com>`
- **References:** `<3fe8c506_7@news.athenanews.com>`

```
>From: "Peter E.C. Dashwood" dashwood@enternet.co.nz 
>Date: 12/23/03 5:41 PM Eastern Standard Time

>
>(Dunno 'bout you, but I only fix things when they DO give an indication they
>are failing...)
>
>

You obviously haven't or don't work for any government...

Government way...
If it ain't broke fix it till it is :)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-25T01:00:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fe9805a_8@news.athenanews.com>`
- **References:** `<3fe8c506_7@news.athenanews.com> <20031223230607.26181.00001425@mb-m15.aol.com>`

```

"YukonMama" <yukonmama@aol.com> wrote in message
news:20031223230607.26181.00001425@mb-m15.aol.com...
> >From: "Peter E.C. Dashwood" dashwood@enternet.co.nz
> >Date: 12/23/03 5:41 PM Eastern Standard Time
>
> >
> >(Dunno 'bout you, but I only fix things when they DO give an indication
they
> >are failing...)
> >
…[5 more quoted lines elided]…
> If it ain't broke fix it till it is :)

It's funny you should say that, Eileen.

In my reckless youth (before I went contract) I DID work for the New Zealand
Governement (or "Civil Service" as we call it...well, that's ONE of the
things we call it <G>).

I found myself working in an area where we computed pay for other Civil
Service employees. The process and procedure worked very well, but the
"Boss" kept "fixing it" (when it wasn't, in fact, "broken"...). On one
occasion I reversed one of her "fixes" because it was impossible to get a
correct result with it in place. She noticed, and abused me in front of the
entire office. Had she been a man, there is no doubt I would have hit her.
As it was, I picked up my coat, left, and have never worked for any
country's Civil Service from that day to this)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-23T15:53:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58d2174486004d81d63d5f4178c0218e@news.teranews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <3fe7671e_3@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> > "Ron" <NoSpam@NoMoSpam.ORG> wrote:
…[10 more quoted lines elided]…
> documenting.

Self documenting? Not! The form "date2 (3:4) to date2 (1:4)" tells
you nothing about what part of date2 you are moving. You must
examine both the definition of date2 and, if all references to it
are like this, also the procedure code that uses it. Why do we have
data names in the first place? Clarity! Consider, if date2 is defined
ONLY as 9(08), no redefines, and EVERY reference to parts of
date2 are by reference, how are you going to know what the format
is? You must examine the actual references to date2 and decipher
them, which may not be easy, because, since all the references to
parts of date2 are by address modification, you will need to find a
move between date2 and a date field whose structure is known. If
the same procedure (definition and reference) is followed on all
the date fields, then only if a move between date2 and a standard
date field is found will you know what the format is. :-)

> How does it complicate maintenance to know what offset and length of a field
> is being moved?

None. It is the NOT knowing the name (sense) of the data that is
being moved that is the problem. :-)

> > Address modification is great for use
> > in scan loops, and with STRING/UNSTRING, or otherwise where
…[8 more quoted lines elided]…
> presenting YOUR way as being the best (or only) way...

I have no problem with you being ignorant of how human perception
works, vis-a-vis programming techniques; I have a problem with you
assuming YOUR lack of knowledge applies to all of us... ;-)

Pete, has it occurd to you that someone can know something for a fact,
that can be studied and easily demonstrated, yet you are unaware of it?
Trust me, this can happen. Just because you are unaware, or disagree,
with a provable fact, is no proof that it is incorrect. I have absolutely
no doubt of the CERTAINTY that using address modification in the
way you suggest is LESS CLEAR than using well named fields. Not
only is it logically obvious to me, but clearly understood and well
documented characterists of human perception, and years of actual
trials I have done, are clear enough proof for me. Simple proof by
reductio ad absurdum makes it obvious that this is true, because if you
continually applied this principle to all such references, the result
would be only address modification references into a huge, undefined
memory pool (i.e. machine language references). If data names are
better understood than pure memory references in general, they are
also better understood here, since precisely the same principles apply.
:-)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-23T15:15:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bs9m75$j0t$1@peabody.colorado.edu>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com>`

```

On 22-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> > move date1 (1:2) to date2 (5:2)
> > move date2 (3:4) to date2 (1:4) ...
…[7 more quoted lines elided]…
> character of a name. But for fixed field moves, always use:

I agree with you with one possible exception:

  DISPLAY 'SIPR702 BEGAN ' FUNCTION CURRENT-DATE (5:2)
                       '/' FUNCTION CURRENT-DATE (07:2)
                       '/' FUNCTION CURRENT-DATE (01:4)
                       ' ' FUNCTION CURRENT-DATE (09:2)
                       ':' FUNCTION CURRENT-DATE (11:2)
                       ':' FUNCTION CURRENT-DATE (13:2).

If I saw that in a program I was maintaining, I would not be confused, and it
may be marginally more clear than moving the date to a work field for the
display.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-23T16:05:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46d36a4c5a52b71a8d1d9ed549fba82b@news.teranews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> > >
…[22 more quoted lines elided]…
> display.

Yes, because FUNCTION CURRENT-DATE has a clearly defined
standard format. Even then, unless you remember the exact format of
FUNCTION CURRENT-DATE, it is not immediately obvious which
fields are which. And even if you do remember the exact format, you
would probably still have to stop and do a bit of mental arithmetic to
know which fields you are extracting, and in what order. Using a field
broken down into (well) named components is *always* immediately
obvious, which is why we usually do it that way, of course. :-)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 5)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-12-23T16:40:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0312231640.595d6b41@posting.google.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<bs9m75$j0t$1@peabody.colorado.edu>...
> On 22-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:
> 
…[22 more quoted lines elided]…
> display.

That means you invoke the function 6 times and in a date rollover you
can get "trash".  Not likely - but possible.  Better I think would be

Move Function Current-Date to current-date-def

01  Current-date-def.
    03  CD-YYYY Pic 9(4).
    03  C-MM    pic 9(4).
    03  C-DD    Pic 9(4).
    03  C-HH    Pic 9(2).
    03  C-MI    Pic 9(2).
    03  C-SS    Pic 9(2).



Display ....... using reference modififcation or just the fields of
current-date-def instead of a reference modification of 6 invocations
of the function!
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-24T05:31:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cx9Gb.3590$lo3.1076@newsread2.news.pas.earthlink.net>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com>`

```
Thane,
  Are you certain of this (at least in the 2002 Standard)?  I thought that there
had been a "fix" (based on an interpretation of the '89 Amendment) that says
that functions are evaluated "once" at the beginning of a statement - in order
to "solve" the Function RANDOM issues?

I have NOT checked this, so I could be mistaken on this.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-29T14:18:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bspd3s$mmc$1@peabody.colorado.edu>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com>`

```

On 23-Dec-2003, thaneh@softwaresimple.com (Thane Hubbell) wrote:

> That means you invoke the function 6 times and in a date rollover you
> can get "trash".  Not likely - but possible.  Better I think would be
…[15 more quoted lines elided]…
> of the function!

Six invokes for a command used once in a program is nothing.   Decisions such as
this should be made solely on maintenance efficiency, not run-time efficiency.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T18:15:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>
> Six invokes for a command used once in a program is nothing.   Decisions such as
> this should be made solely on maintenance efficiency, not run-time efficiency.

If that code is in a transaction routine that is called 1000 times a second,
the overhead isn't 'nothing'. And what about turning over midnight after
the first call and before the last call? Remember Murphy's Law. :-)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-29T19:20:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bspuov$cq1$1@peabody.colorado.edu>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com>`

```

On 29-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> > Six invokes for a command used once in a program is nothing.   Decisions
> > such as
…[5 more quoted lines elided]…
> the first call and before the last call? Remember Murphy's Law. :-)

But you will notice that the code said:
  DISPLAY 'SIPR702 BEGAN ' FUNCTION CURRENT-DATE (5:2)
                       '/' FUNCTION CURRENT-DATE (7:2)
                       '/' FUNCTION CURRENT-DATE (1:4)
                       ' ' FUNCTION CURRENT-DATE (09:2)                 hour
                       ':' FUNCTION CURRENT-DATE (11:2)
                       ':' FUNCTION CURRENT-DATE (13:2).

Saying when a program starts doesn't happen 1000 times a second.

I was under the impression that this gets converted into one call though.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T20:39:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<daafb13fde2441d0f8a7b261e4f169f7@news.teranews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[13 more quoted lines elided]…
> Saying when a program starts doesn't happen 1000 times a second.

True. But saying when a transaction began processing might. ;-)

> I was under the impression that this gets converted into one call though.

I would think this should be the case, even if COBOL standards do not
dictate it. A compiler would be pretty inept not to detect and optimize
such a pattern. :-)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 10)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-12-29T22:55:41+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r151vvs0neb48om0q5ite324a6utrtt7ub@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu> <daafb13fde2441d0f8a7b261e4f169f7@news.teranews.com>`

```
On Mon, 29 Dec 2003 20:39:56 GMT "Judson McClendon" <judmc@sunvaley0.com>
wrote:

:>"Howard Brazee" <howard@brazee.net> wrote:

:>> "Judson McClendon" <judmc@sunvaley0.com> wrote:

:>> > If that code is in a transaction routine that is called 1000 times a second,
:>> > the overhead isn't 'nothing'. And what about turning over midnight after
:>> > the first call and before the last call? Remember Murphy's Law. :-)

:>> But you will notice that the code said:
:>>   DISPLAY 'SIPR702 BEGAN ' FUNCTION CURRENT-DATE (5:2)
:>>                        '/' FUNCTION CURRENT-DATE (7:2)
:>>                        '/' FUNCTION CURRENT-DATE (1:4)
:>>                        ' ' FUNCTION CURRENT-DATE (09:2)                 hour
:>>                        ':' FUNCTION CURRENT-DATE (11:2)
:>>                        ':' FUNCTION CURRENT-DATE (13:2).

:>> Saying when a program starts doesn't happen 1000 times a second.

:>True. But saying when a transaction began processing might. ;-)

:>> I was under the impression that this gets converted into one call though.

:>I would think this should be the case, even if COBOL standards do not
:>dictate it. A compiler would be pretty inept not to detect and optimize
:>such a pattern. :-)

REXX has a requirement/definition that all TIME/DATE based functions in one
statement will all use the same clock value, even if the statement is complex
enough to require much time between the separate function calls.

Does COBOL?
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-29T14:38:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0312291438.63031a9f@posting.google.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> But you will notice that the code said:
>   DISPLAY 'SIPR702 BEGAN ' FUNCTION CURRENT-DATE (5:2)
…[6 more quoted lines elided]…
> Saying when a program starts doesn't happen 1000 times a second.

It does if 'SIPR702' is a sub program CALLed for each transaction.
 
> I was under the impression that this gets converted into one call though.

How would the compiler do that ?
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-29T18:45:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsqeai$n6p$1@panix1.panix.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu> <217e491a.0312291438.63031a9f@posting.google.com>`

```
In article <217e491a.0312291438.63031a9f@posting.google.com>,
Richard <riplin@Azonic.co.nz> wrote:
>"Howard Brazee" <howard@brazee.net> wrote 
>
…[10 more quoted lines elided]…
>It does if 'SIPR702' is a sub program CALLed for each transaction.

... and if your Production Review process is such that it allows such a 
thing to happen then your organisation deserves everything which might 
happen to it.

DD
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T14:18:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bss1fh$rkl$1@peabody.colorado.edu>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu> <217e491a.0312291438.63031a9f@posting.google.com>`

```

On 29-Dec-2003, riplin@Azonic.co.nz (Richard) wrote:

> > I was under the impression that this gets converted into one call though.
>
> How would the compiler do that ?

By having a little bit of smarts.  It isn't difficult to see that the same
function was called 6 times in one display statement.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 11)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-12-30T17:56:35+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ue73vvo0bpqsdlevi4of7h9i217s2uhr53@4ax.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu> <217e491a.0312291438.63031a9f@posting.google.com> <bss1fh$rkl$1@peabody.colorado.edu>`

```
On Tue, 30 Dec 2003 14:18:25 GMT "Howard Brazee" <howard@brazee.net> wrote:

:>On 29-Dec-2003, riplin@Azonic.co.nz (Richard) wrote:

:>> > I was under the impression that this gets converted into one call though.

:>> How would the compiler do that ?

:>By having a little bit of smarts.  It isn't difficult to see that the same
:>function was called 6 times in one display statement.

How does the compiler know that each time the same result will be returned? 

Perhaps a static variable or random number affects the result?
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T16:15:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bss8bi$k0l$1@peabody.colorado.edu>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu> <217e491a.0312291438.63031a9f@posting.google.com> <bss1fh$rkl$1@peabody.colorado.edu> <ue73vvo0bpqsdlevi4of7h9i217s2uhr53@4ax.com>`

```

On 30-Dec-2003, Binyamin Dissen <postingid@dissensoftware.com> wrote:

> :>> > I was under the impression that this gets converted into one call
> though.
…[8 more quoted lines elided]…
> Perhaps a static variable or random number affects the result?

It assumes that a display statement is meant to act as though it was
instantaneous.

It's easy enough to do - the question is whether or not that is the way it's
supposed to work.   I was under the impression that that IS the way it is
supposed to work, and that is the way it does work in my environment.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-30T10:51:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0312301051.2a015cf4@posting.google.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu> <217e491a.0312291438.63031a9f@posting.google.com> <bss1fh$rkl$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote

> > > I was under the impression that this gets converted into one call though.
> >
…[3 more quoted lines elided]…
> function was called 6 times in one display statement.

And what if it was FUNCTION RANDOM that was being called 6 times ? 
Would the compiler think that it is a good idea to make that just one
call ?

How about FUNCTION READ_NEXT_RECORD ?
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T20:36:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bssnkl$s9$1@peabody.colorado.edu>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu> <217e491a.0312291438.63031a9f@posting.google.com> <bss1fh$rkl$1@peabody.colorado.edu> <217e491a.0312301051.2a015cf4@posting.google.com>`

```

On 30-Dec-2003, riplin@Azonic.co.nz (Richard) wrote:

> > > > I was under the impression that this gets converted into one call
> > > > though.
…[10 more quoted lines elided]…
> How about FUNCTION READ_NEXT_RECORD ?

It depends on how the compiler was written and what the standards were.

You're gradually changing the questions from how a compiler could do something
to whether it is a good idea for it to do something similar.    The compiler can
be written however the standards say it should be written.   I didn't make the
decisions, but I thought I read that this particular function was only called
once per statement.   I did say "I was under the impression", which seemed when
I wrote it to be enough waffling.
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-31T23:23:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6bba8487c3fa9ffc7b3dee70dca177de@news.teranews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com> <bspuov$cq1$1@peabody.colorado.edu> <217e491a.0312291438.63031a9f@posting.google.com> <bss1fh$rkl$1@peabody.colorado.edu> <217e491a.0312301051.2a015cf4@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
> "Howard Brazee" <howard@brazee.net> wrote
> > >
…[9 more quoted lines elided]…
> How about FUNCTION READ_NEXT_RECORD?

Richard, that brings up a thought, relative to the OO threads now ongoing.
What about those Universal Object References Thane was mentioning, in
this context? I can see where you could potentially get a very different
result from early and late binding in this case. In one case the compiler
knows, in the other it doesn't. Implementation might be a bit tricky.

No criticism of OO here, it is the ramifications of the concept that I'm
curious about. :-)
```

###### ↳ ↳ ↳ Re: Date manipulation

_(reply depth: 8)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-29T18:49:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xKKdndDtQKYKVm2iRVn-gQ@giganews.com>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net> <8579uv03o7bt44rtm3vk6diftvj2014bn6@4ax.com> <h7ecnYuqdOohJnmiXTWQlg@giganews.com> <d14aee019cf2a7fd54fe17a24339da7a@news.teranews.com> <bs9m75$j0t$1@peabody.colorado.edu> <bfdfc3e8.0312231640.595d6b41@posting.google.com> <bspd3s$mmc$1@peabody.colorado.edu> <8c4cee85a6472bf6db0fb07534a2af2a@news.teranews.com>`

```
Judson McClendon wrote:
> "Howard Brazee" <howard@brazee.net> wrote:
>>
…[8 more quoted lines elided]…
> the first call and before the last call? Remember Murphy's Law. :-)

There's not much that CAN take place in 1 milli-second, but I understand
your point.

Still, coding for micro-efficiency is a pitiful waste of resources (it
should even be illegal).
```

#### ↳ Re: Date manipulation

- **From:** "Francis ANDRE" <francis.andre@easynet.fr>
- **Date:** 2003-12-20T21:15:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fe4adfd$0$397$afc38c87@news.easynet.fr>`
- **References:** `<DiNEb.3912$XF6.86150@typhoon.sonic.net>`

```
Why don't you use MOVE CORRESPONDING???  (fast.... just 3 moves of
2 bytes instead of a full decimal multiplication)?? and easy to do in one
sentence

01  DT-MMDDYY     PIC 9(06)  VALUE 0.
01  DT-MMDDYY-R REDEFINES DT-MMDDYY.
      02  MM                PIC 9(2).
      02  DD                  PIC 9(2).
      02  YY                  PIC 9(2).


01  DT-YYMMDD     PIC 9(06)  VALUE 0.
01  DT-YYMMDD-R REDEFINES DT-YYMMDD.
      02  YY                  PIC 9(2).
      02  MM                PIC 9(2).
      02  DD                  PIC 9(2).

MOVE CORRESPONDING DT-YYMMDD-R TO DT-DDMMYY-R

Regards

FA


"Kindrick Ownby" <kownby@sonic.net> a �crit dans le message de news:
DiNEb.3912$XF6.86150@typhoon.sonic.net...
>
> I have a vague recollection from Y2K discussions
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
