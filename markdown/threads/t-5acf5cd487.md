[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL on AS/400...HELP!!!!

_6 messages · 6 participants · 1998-09_

**Topics:** [`AS/400, iSeries, RPG`](../topics.md#as400)

---

### COBOL on AS/400...HELP!!!!

- **From:** "William R. Fink" <bfink@apci.net>
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6udi25$nsf@mhstl1.monsanto.com>`

```
I know next to nothing about the AS/400.  I need to know the proper way to
set up a library, and file, and a queue for compiling a COBOL program.
Additionally, I need to know how to compile and run COBOL.

I have had some luck setting up everything, and even compiling; but can not
find my compiler listings.


Are there any AS/400 people out there that could help?  Are there any web
sites for AS/400 programmers?

Bill Fink
bfink@apci.net
```

#### ↳ Re: COBOL on AS/400...HELP!!!!

- **From:** terrywin.nospam.@spectra.net (Terry Winchester)
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360aabf2.2862311@supernews.spectra.net>`
- **References:** `<6udi25$nsf@mhstl1.monsanto.com>`

```
On Thu, 24 Sep 1998 08:32:18 -0500, "William R. Fink" <bfink@apci.net>
wrote:

>I know next to nothing about the AS/400.  I need to know the proper way to
>set up a library, and file, and a queue for compiling a COBOL program.
…[13 more quoted lines elided]…
>
Bill,

Your compiler output generally will go to the default queue set up
under your user profile.  Use the WRKSPLF command to see _all_
of your printed output that is currently linked to your present
user-id.  Then you will see what output queue is assigned to
your compile listing.

Terry
```

#### ↳ Re: COBOL on AS/400...HELP!!!!

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uenmq$4jc@lotho.delphi.com>`
- **References:** `<6udi25$nsf@mhstl1.monsanto.com>`

```

Well, all the IBM Docs are online, and there are tons of 
other places to get help. :) 

The AS/400 porting center is probably a good place to start:
	http://www.softmall.ibm.com/as400/porting/

-Paul


William R. Fink (bfink@apci.net) wrote:
: I know next to nothing about the AS/400.  I need to know the proper way to
: set up a library, and file, and a queue for compiling a COBOL program.
: Additionally, I need to know how to compile and run COBOL.

: I have had some luck setting up everything, and even compiling; but can not
: find my compiler listings.


: Are there any AS/400 people out there that could help?  Are there any web
: sites for AS/400 programmers?

: Bill Fink
: bfink@apci.net
```

##### ↳ ↳ Re: COBOL on AS/400...HELP!!!!

- **From:** blarkin713@my-dejanews.com
- **Date:** 1998-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uiut3$ubi$1@nnrp1.dejanews.com>`
- **References:** `<6udi25$nsf@mhstl1.monsanto.com> <6uenmq$4jc@lotho.delphi.com>`

```
To find your spoolfile, use the WRKSPLF command. It will show all your spool
files.

Also, when you compile, make sure you prompt the command or option with F4,
and make sure you have specified the listing be printed.

Also, Try www.as400/ibm/com - Almost every IBM AS/400 manual is online there.
The site is being remodeled, but the manuals are out there.

Bob Larkin
blarkin@wt.net
In article <6uenmq$4jc@lotho.delphi.com>,
  paulr@bix.com (paulr) wrote:
>
> Well, all the IBM Docs are online, and there are tons of
…[21 more quoted lines elided]…
>


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: COBOL on AS/400...HELP!!!!

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#$8p$5X69GA.184@upnetnews03>`
- **References:** `<6udi25$nsf@mhstl1.monsanto.com> <6uenmq$4jc@lotho.delphi.com> <6uiut3$ubi$1@nnrp1.dejanews.com>`

```
More better you use the URL http://www.as400.ibm.com for AS/400 info.

blarkin713@my-dejanews.com wrote in message
<6uiut3$ubi$1@nnrp1.dejanews.com>...
>To find your spoolfile, use the WRKSPLF command. It will show all your
spool
>files.
>
…[3 more quoted lines elided]…
>Also, Try www.as400/ibm/com - Almost every IBM AS/400 manual is online
there.
>The site is being remodeled, but the manuals are out there.
>
…[14 more quoted lines elided]…
>> : I know next to nothing about the AS/400.  I need to know the proper way
to
>> : set up a library, and file, and a queue for compiling a COBOL program.
>> : Additionally, I need to know how to compile and run COBOL.
>>
>> : I have had some luck setting up everything, and even compiling; but can
not
>> : find my compiler listings.
>>
>> : Are there any AS/400 people out there that could help?  Are there any
web
>> : sites for AS/400 programmers?
>>
…[7 more quoted lines elided]…
>http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: COBOL on AS/400...HELP!!!!

- **From:** esinger@cybernospam.net (Jim Essinger)
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3611095e.37208637@news.cyberhighway.net>`
- **References:** `<6udi25$nsf@mhstl1.monsanto.com> <6uenmq$4jc@lotho.delphi.com> <6uiut3$ubi$1@nnrp1.dejanews.com>`

```
I am a COBOL programmer on the AS/400.  There are many different
factors that affect the output from a compile. Files are found in the
library list.  If it is not setup correctly the program will not run,
or run with the wrong set of files.  Are you using the Program
Development Manager (PDM) to code and test?  

 If you have questions I would be glad to help.  Email me and I will
answer.

On Sat, 26 Sep 1998 14:49:07 GMT, blarkin713@my-dejanews.com wrote:

>To find your spoolfile, use the WRKSPLF command. It will show all your spool
>files.
…[38 more quoted lines elided]…
>http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
