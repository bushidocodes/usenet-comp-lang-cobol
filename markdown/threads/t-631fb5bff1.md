[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New COBOL student

_10 messages · 7 participants · 1998-11_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### New COBOL student

- **From:** jim777@my-dejanews.com
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73611r$dau$1@nnrp1.dejanews.com>`

```
I'm in the process of learing COBOL. I've just completed the text 'TEACH
YOURSELF COBOL IN 21 DAYS'. The text did a nice job explaning the basics. At
any rate, now that I've learned enough to be a threat to platforms
everywhere, could some of you experienced COBOL programmers give me some idea
of what I should study next? For example, I've been told that I should learn
DB2, VSAM, CICS, JCL. Is this true? What should I do next, in the real-world
of COBOL shops?

P.S. Our family lives in the Twin Cities area. I would gladly hire a COBOL
tutor if someone is in this area.

Thanks,

jimausterman@hotmail.com

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: New COBOL student

- **From:** aziola@aol.com (AZIOLA)
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981121083804.16647.00000979@ng-fr1.aol.com>`
- **References:** `<73611r$dau$1@nnrp1.dejanews.com>`

```
jcljclJCLJCLJCLJCL

YOU GOTTA LEARN JCL!....COBOL IS WORTHLESS IN MOST PLATFORMS IF YOU DONT KNOW
JCL....IT'S WHAT RUNS THE COBOL PROGRAMS IN A MAINFRAME ENVIRONMENT!..GOOD LUCK
'Only the Paranoid Survive...'- Andy Grove, Intel CEO
```

##### ↳ ↳ Re: New COBOL student

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981121103439.19943.00000309@ngol05.aol.com>`
- **References:** `<19981121083804.16647.00000979@ng-fr1.aol.com>`

```

In article <19981121083804.16647.00000979@ng-fr1.aol.com>, aziola@aol.com
(AZIOLA) writes:

>cljclJCLJCLJCLJCL
>
>YOU GOTTA LEARN JCL!....COBOL IS WORTHLESS IN MOST PLATFORMS IF YOU DONT KNOW
>JCL....IT'S WHAT RUNS THE COBOL PROGRAMS IN A MAINFRAME 

That is ASSUMing that the MainFrame environment is IBM or IBM-clone(Amdahl).

Not all environments are set on the use of JCL.  There are mainframe platforms
that permit straight up execution of programs just as on the PC.  Filenames are
supplied internally or via control files or via command line overrides.
```

###### ↳ ↳ ↳ Re: New COBOL student

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981121232824.25467.00000642@ngol04.aol.com>`
- **References:** `<19981121103439.19943.00000309@ngol05.aol.com>`

```

In article <19981121103439.19943.00000309@ngol05.aol.com>, sff5ky@aol.comxxx123
(Sff5ky) writes:

>That is ASSUMing that the MainFrame environment is IBM or IBM-clone(Amdahl).
>

Worse yet, it is assuming IBM MVS or OS/390 enviornment.

There are actually more VSE licenses than MVS + OS/390 licenses, and teh JCL
for VSE is significantly different from MVS & OS/390.
Mark A. Young
```

###### ↳ ↳ ↳ Re: New COBOL student

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3658484c.142824041@news1.ibm.net>`
- **References:** `<19981121103439.19943.00000309@ngol05.aol.com> <19981121232824.25467.00000642@ngol04.aol.com>`

```
On 22 Nov 1998 04:28:24 GMT, mark0young@aol.com (Mark0Young) wrote:

>
>In article <19981121103439.19943.00000309@ngol05.aol.com>, sff5ky@aol.comxxx123
…[9 more quoted lines elided]…
>Mark A. Young

I'm at an OS/390 shop now - but I came from a VSE shop.  What I can't
figure out, is if there are so many more licenses for VSE how come
there are VERY  FEW job postings/ads that mention VSE?  I just find it
strange.  When I started looking for my current job, all I ran into
were people requiring MVS - not one VSE position (other than the one
at your location) presented itself.
```

###### ↳ ↳ ↳ Re: New COBOL student

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<739qeb$2m9@sjx-ixn10.ix.netcom.com>`
- **References:** `<19981121103439.19943.00000309@ngol05.aol.com> <19981121232824.25467.00000642@ngol04.aol.com> <3658484c.142824041@news1.ibm.net>`

```

Thane Hubbell wrote in message <3658484c.142824041@news1.ibm.net>...
>On 22 Nov 1998 04:28:24 GMT, mark0young@aol.com (Mark0Young) wrote:
>
>>
>>In article <19981121103439.19943.00000309@ngol05.aol.com>,
sff5ky@aol.comxxx123
>>(Sff5ky) writes:
>>
>>>That is ASSUMing that the MainFrame environment is IBM or
IBM-clone(Amdahl).
>>>
>>
>>Worse yet, it is assuming IBM MVS or OS/390 enviornment.
>>
>>There are actually more VSE licenses than MVS + OS/390 licenses, and teh
JCL
>>for VSE is significantly different from MVS & OS/390.
>>Mark A. Young
…[7 more quoted lines elided]…
>


although it is a GROSS oversimplification (with lots of exceptions), the
average MVS shop has 50+ (often hundreds) of application and systems
programmers - while the average VSE shop has less than 50 (and often less
than 10 application programmers).  Another issue is how much VSE code is
"purchased" versus home-grown (lots) versus that in MVS shops (some - but
usually well under half).  All of this adds up to significantly less demand
for application programmers for VSE than MVS (even though the licenses go
the other way).

P.S.  The same is true (if more so) for AS/400 which has more licenses than
VSE (as I recall) but even fewer application programming openings.
```

###### ↳ ↳ ↳ Re: New COBOL student

_(reply depth: 5)_

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981124010759.27057.00001094@ngol02.aol.com>`
- **References:** `<3658484c.142824041@news1.ibm.net>`

```

In article <3658484c.142824041@news1.ibm.net>, redsky@ibm.net (Thane Hubbell)
writes:

>What I can't
>figure out, is if there are so many more licenses for VSE how come
>there are VERY  FEW job postings/ads that mention VSE?

I think William has it. MVS and OS/390 is designed to make use of IBM larger
mainframes, and that is where one typically finds many programmers, dollars to
pay top price, etc.

VSE is desinged to be sleek and have less overhead, so typically there are
fewer programmers at a VSE shop, and it is relativley common to purchase
packages rather than develop in-house, or at least to have major applications
be purchased systems. Also, since VSE shops are smaller, they tend to not be
able to pay top dollar for a programmer, making it counterproductive to
advertise in the papers against higher-paying MVS shops.

Also, many VSE licenses are for companies that have MVS for main processing and
use VSE machines as nodes controlled by a central MVS site, or program in a
central location and deploy applications at their offices in other states.

Mark A. Young
```

###### ↳ ↳ ↳ Re: New COBOL student

_(reply depth: 6)_

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981124013121.25361.00001206@ngol01.aol.com>`
- **References:** `<19981124010759.27057.00001094@ngol02.aol.com>`

```

In article <19981124010759.27057.00001094@ngol02.aol.com>, mark0young@aol.com
(Mark0Young) writes:

>VSE is desinged to be sleek and have less overhead

I forgot to add: so VSE would run efficiently on the lower end of the IBM
mainframes. (In fact, it couldn't make use of multiple processors until
relatively recently, and even then, using VSE's "Turbo Dispatcher", a partition
can be serviced by only one processor at a time during its "time slice".
Contrast that to MVS that can have multiple processors working on the same
partition at the same time, e.g., typical of CICS and DB/2 under MVS.)

Mark A. Young
```

##### ↳ ↳ Re: New COBOL student

- **From:** "GoJaye" <Gojaye@geocities.com>
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<739d9f$t5u$1@sulu.ctsi.net>`
- **References:** `<73611r$dau$1@nnrp1.dejanews.com> <19981121083804.16647.00000979@ng-fr1.aol.com>`

```
Agreed.....JCL is the lifeblood......
AZIOLA wrote in message <19981121083804.16647.00000979@ng-fr1.aol.com>...
>jcljclJCLJCLJCLJCL
>
>YOU GOTTA LEARN JCL!....COBOL IS WORTHLESS IN MOST PLATFORMS IF YOU DONT
KNOW
>JCL....IT'S WHAT RUNS THE COBOL PROGRAMS IN A MAINFRAME ENVIRONMENT!..GOOD
LUCK
>'Only the Paranoid Survive...'- Andy Grove, Intel CEO
```

#### ↳ Re: New COBOL student

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981121103441.19943.00000310@ngol05.aol.com>`
- **References:** `<73611r$dau$1@nnrp1.dejanews.com>`

```

In article <73611r$dau$1@nnrp1.dejanews.com>, jim777@my-dejanews.com writes:

>everywhere, could some of you experienced COBOL programmers give me some idea
>of what I should study next? For example, I've been told that I should learn
>DB2, VSAM, CICS, JCL. Is this true? What should I do next, in the real-world
>of COBOL shops?


This sounds as if you are in an area dominated by IBM, that being the case it
is probably advisable to know a little JCL in order to handle COMPILE processes
and subsequent program execution processes.   Most JCL can be picked up in a
couple of weeks.  I personally have had little to no use/exposure to CICS,
VSAM, DB2 in the 20+ years of programming for the Financial industry.  
DB2 would be a good next choice although it might be better to look at
something that covers DataBase design in general over a platform specific
course.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
