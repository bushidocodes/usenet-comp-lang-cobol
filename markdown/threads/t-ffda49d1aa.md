[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# C++ Translation to Cobol

_12 messages · 9 participants · 2001-05_

---

### C++ Translation to Cobol

- **From:** "Joseph Lazarus" <brenjoe@worldnet.att.net>
- **Date:** 2001-05-01T02:20:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net>`

```
Can anyone help me translate this code in C++ to Cobol, much appreciated.

#include <iostream.h>

void main()

{
int sum = 0;
int x;
cout<< "Enter a number: ";

cin>> x;

for (int i = 1; i <= x; ++i)

sum = sum + i;

cout <<sum  <<endl;

}
```

#### ↳ Re: C++ Translation to Cobol

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-05-01T03:36:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-e7LG5bYlZM8W@24-108-102-82.ivideon.com>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net>`

```
On Tue, 1 May 2001 02:20:12, "Joseph Lazarus" 
<brenjoe@worldnet.att.net> wrote:

> Can anyone help me translate this code in C++ to Cobol, much appreciated.
> 
…[20 more quoted lines elided]…
> 

If this is a contest do I get a prize?

       identification division.
       program-id. thing.
       author.     Lorne Sunley.

       environment division.
       input-output section.
       file-control.

       data division.
       file section.

       working-storage section.
       01  in-number      pic 9(9).
       01  work-total      pic 9(9).
       procedure division.
       001-start section.
       010-start.

            display "enter a number: " with no advancing
            accept in-number
            move zero to work-total
            perform varying idx from 1 by 1 until idx = in-number

                compute work-total = work-total + idx

            end-perform
            display " "
            display total

       end program thing.
```

##### ↳ ↳ Re: C++ Translation to Cobol

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-05-01T11:43:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5E7622B230FFF1B2.B8D7E54ECAF29D85.7A7ADF67B501B584@lp.airnews.net>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net> <ZpzG4UNLyRNq-pn2-e7LG5bYlZM8W@24-108-102-82.ivideon.com>`

```
On Tue, 01 May 2001 03:36:30 GMT, lsunley@mb.sympatico.ca enlightened
us:

>On Tue, 1 May 2001 02:20:12, "Joseph Lazarus" 
><brenjoe@worldnet.att.net> wrote:
…[56 more quoted lines elided]…
>       end program thing.

Sorry you don't win the prize because your Cobol code has an error!

Line in error:

display total

total was neither previously defined nor part of a calculation.
Correct statement should be:

display work-total.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

God created lesbians, So that feminists wouldn't breed.


DON'T DRILL in the Artic National Wildlife Refuge
Read the facts and sign a petition at:

http://www.savepolarbears.org/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: C++ Translation to Cobol

- **From:** alex <me@broke.com>
- **Date:** 2001-05-01T16:08:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AEF25C7.231533B1@broke.com>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net> <ZpzG4UNLyRNq-pn2-e7LG5bYlZM8W@24-108-102-82.ivideon.com> <5E7622B230FFF1B2.B8D7E54ECAF29D85.7A7ADF67B501B584@lp.airnews.net>`

```
SkippyPB wrote:

> On Tue, 01 May 2001 03:36:30 GMT, lsunley@mb.sympatico.ca enlightened
> us:
…[87 more quoted lines elided]…
> Steve

what about idx?  lorne, you flunk....
```

###### ↳ ↳ ↳ Re: C++ Translation to Cobol

_(reply depth: 4)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-05-01T23:49:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-jq0FS9SIQX3Z@24-108-102-82.ivideon.com>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net> <ZpzG4UNLyRNq-pn2-e7LG5bYlZM8W@24-108-102-82.ivideon.com> <5E7622B230FFF1B2.B8D7E54ECAF29D85.7A7ADF67B501B584@lp.airnews.net> <3AEF25C7.231533B1@broke.com>`

```
On Tue, 1 May 2001 21:08:23, alex <me@broke.com> wrote:

> SkippyPB wrote:
> 
…[93 more quoted lines elided]…
> 

Rats, I was really looking forward to that all expense paid trip to 
Disney World

This is what happens when you don't compile and test your code....(or 
desk check it properly :-)
```

###### ↳ ↳ ↳ Re: C++ Translation to Cobol

_(reply depth: 5)_

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-05-02T04:29:23+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9cnr5t$h3l$1@news6.svr.pol.co.uk>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net> <ZpzG4UNLyRNq-pn2-e7LG5bYlZM8W@24-108-102-82.ivideon.com> <5E7622B230FFF1B2.B8D7E54ECAF29D85.7A7ADF67B501B584@lp.airnews.net> <3AEF25C7.231533B1@broke.com> <ZpzG4UNLyRNq-pn2-jq0FS9SIQX3Z@24-108-102-82.ivideon.com>`

```
'God created lesbians, So that feminists wouldn't breed' should read
'God created lesbians, So that I can watch' :)

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-jq0FS9SIQX3Z@24-108-102-82.ivideon.com...
> On Tue, 1 May 2001 21:08:23, alex <me@broke.com> wrote:
>
…[8 more quoted lines elided]…
> > > >> Can anyone help me translate this code in C++ to Cobol, much
appreciated.
> > > >>
> > > >> #include <iostream.h>
…[93 more quoted lines elided]…
> Lorne Sunley
```

###### ↳ ↳ ↳ Re: C++ Translation to Cobol

_(reply depth: 6)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-05-02T23:11:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zu0I6.19397$sP6.863739@news3.aus1.giganews.com>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net> <ZpzG4UNLyRNq-pn2-e7LG5bYlZM8W@24-108-102-82.ivideon.com> <5E7622B230FFF1B2.B8D7E54ECAF29D85.7A7ADF67B501B584@lp.airnews.net> <3AEF25C7.231533B1@broke.com> <ZpzG4UNLyRNq-pn2-jq0FS9SIQX3Z@24-108-102-82.ivideon.com> <9cnr5t$h3l$1@news6.svr.pol.co.uk>`

```

"Alister Munro" <alister@specsoft.freeserve.co.uk> wrote in message
news:9cnr5t$h3l$1@news6.svr.pol.co.uk...
> 'God created lesbians, So that feminists wouldn't breed' should read
> 'God created lesbians, So that I can watch' :)

Trust me on this: you DON'T want to watch.
```

###### ↳ ↳ ↳ Re: C++ Translation to Cobol

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-05-03T10:54:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C0C502C8EBF50058.46F5CA49A69B6CB8.876334F9888E7CF1@lp.airnews.net>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net> <ZpzG4UNLyRNq-pn2-e7LG5bYlZM8W@24-108-102-82.ivideon.com> <5E7622B230FFF1B2.B8D7E54ECAF29D85.7A7ADF67B501B584@lp.airnews.net> <3AEF25C7.231533B1@broke.com> <ZpzG4UNLyRNq-pn2-jq0FS9SIQX3Z@24-108-102-82.ivideon.com> <9cnr5t$h3l$1@news6.svr.pol.co.uk> <zu0I6.19397$sP6.863739@news3.aus1.giganews.com>`

```
On Wed, 02 May 2001 23:11:27 GMT, "Jerry P" <jerryp@bisusa.com>
enlightened us:

>
>"Alister Munro" <alister@specsoft.freeserve.co.uk> wrote in message
…[5 more quoted lines elided]…
>

And you have film to prove this?  :)

Ciao,

          ////
         (o o)
-oOO--(_)--OOo-

God created lesbians, So that feminists wouldn't breed.


DON'T DRILL in the Artic National Wildlife Refuge
Read the facts and sign a petition at:

http://www.savepolarbears.org/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: C++ Translation to Cobol

_(reply depth: 8)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-05-04T01:03:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fdnI6.60312$8j.7869782@bin1.nnrp.aus1.giganews.com>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net> <ZpzG4UNLyRNq-pn2-e7LG5bYlZM8W@24-108-102-82.ivideon.com> <5E7622B230FFF1B2.B8D7E54ECAF29D85.7A7ADF67B501B584@lp.airnews.net> <3AEF25C7.231533B1@broke.com> <ZpzG4UNLyRNq-pn2-jq0FS9SIQX3Z@24-108-102-82.ivideon.com> <9cnr5t$h3l$1@news6.svr.pol.co.uk> <zu0I6.19397$sP6.863739@news3.aus1.giganews.com> <C0C502C8EBF50058.46F5CA49A69B6CB8.876334F9888E7CF1@lp.airnews.net>`

```

"SkippyPB" <swiegand@neo.rr.com.nospam> wrote in message
news:C0C502C8EBF50058.46F5CA49A69B6CB8.876334F9888E7CF1@lp.airnews.net
...
> On Wed, 02 May 2001 23:11:27 GMT, "Jerry P" <jerryp@bisusa.com>
> enlightened us:
…[4 more quoted lines elided]…
> >> 'God created lesbians, So that feminists wouldn't breed' should
read
> >> 'God created lesbians, So that I can watch' :)
> >
…[4 more quoted lines elided]…
>

It's a dirty job, but someone has to do it.
```

#### ↳ Re: C++ Translation to Cobol

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-05-01T10:57:04+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<miqsetg8eogrgs09d4j2fcj5s0dmhkrkn8@4ax.com>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net>`

```
On Tue, 01 May 2001 02:20:12 GMT "Joseph Lazarus" <brenjoe@worldnet.att.net>
wrote:

:>Can anyone help me translate this code in C++ to Cobol, much appreciated.

:>#include <iostream.h>

:>void main()

:>{
:>int sum = 0;
:>int x;
:>cout<< "Enter a number: ";

:>cin>> x;

:>for (int i = 1; i <= x; ++i)

:>sum = sum + i;

Why not avoid the loop?

if (x < 1) sum = 0;
else sum = ((x + 1) * x) / 2;

:>cout <<sum  <<endl;

:>}
```

##### ↳ ↳ Re: C++ Translation to Cobol

- **From:** Anonymous <anonymous@anonymous.anonymous>
- **Date:** 2001-05-03T02:02:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3af0164d_2@anonymous>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net> <miqsetg8eogrgs09d4j2fcj5s0dmhkrkn8@4ax.com>`

```
Congratulations Binyamin!

(As usual, your solution is efficient, effective, and elegant.)

I was wondering if anyone would use this method.

The story goes that when Gauss was 8 years old, he and his classmates were
misbehaving. The teacher gave them an imposition. Add up all the numbers
from 1 to 100.

Gauss immediately wrote down 5050 and exclaimed, "There it lies!" (probably
"Da, ist er!" actually...<G>) He had intuitively realised that he could "add
the extremities and fold in the middle". To this day it is known as Gauss'
algorithm.

I believe that the lesson here is that it is important to UNDERSTAND what is
required, not just do what is asked. The exercise was "Translate this C++
into COBOL". What it should have been was "Duplicate this C++ functionality
in COBOL".

Your solution was infinitely better.

Pete Dashwood (lurking as Anonymous...)




Binyamin Dissen wrote in message ...
>On Tue, 01 May 2001 02:20:12 GMT "Joseph Lazarus"
<brenjoe@worldnet.att.net>
>wrote:
>
…[31 more quoted lines elided]…
>Director, Dissen Software, Bar & Grill - Israel


  --------== Posted Anonymously via Newsfeeds.Com ==-------
     Featuring the worlds only Anonymous Usenet Server
    -----------== http://www.newsfeeds.com ==----------
```

#### ↳ Re: C++ Translation to Cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-05-01T15:14:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AEEC4BB.27724F30@Azonic.co.nz>`
- **References:** `<w3pH6.6162$kA1.293981@bgtnsc04-news.ops.worldnet.att.net>`

```
Joseph Lazarus wrote:
> 
> Can anyone help me translate this code in C++ to Cobol, much appreciated.
…[18 more quoted lines elided]…
> }

Homework is it ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
