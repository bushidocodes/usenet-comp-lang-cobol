[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mainframe simulator

_9 messages · 8 participants · 2006-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Mainframe simulator

- **From:** Xavier.Deepak@gmail.com
- **Date:** 2006-04-14T03:25:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com>`

```
Hi, does anyone know what mainframe software I should use on Windows
for developing and testing mainframe components using cobol,
jcl,rexx,... with vsam files and db2 databases.

Is there any such environment for a single user??? I've seen stuff on
the net like microfocus mainframe express, workbench, etc, but am not
sure what would work for my purpose and what wouldn't...

Would appreciate any pointers..

Thanks,
Xavier.
```

#### ↳ Re: Mainframe simulator

- **From:** docdwarf@panix.com ()
- **Date:** 2006-04-14T11:10:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1nvuu$hr$1@reader1.panix.com>`
- **References:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com>`

```
In article <1145010342.440468.58160@e56g2000cwe.googlegroups.com>,
 <Xavier.Deepak@gmail.com> wrote:
>Hi, does anyone know what mainframe software I should use on Windows
>for developing and testing mainframe components using cobol,
>jcl,rexx,... with vsam files and db2 databases.

I've usually found the best one to work with is the one that the Project 
Director has recommended the team use; working with a different one can 
make for... difficulties.

>
>Is there any such environment for a single user??? I've seen stuff on
>the net like microfocus mainframe express, workbench, etc, but am not
>sure what would work for my purpose and what wouldn't...

A better suggestion might be made if more of 'your purpose' were known.

>
>Would appreciate any pointers..

How about a sharp stick in the ear?  *There's* a point-er!

DD
```

##### ↳ ↳ Re: Mainframe simulator

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-04-14T14:08:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S1O%f.52448$K11.24004@clgrps12>`
- **References:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com> <e1nvuu$hr$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:e1nvuu$hr$1@reader1.panix.com...
> In article <1145010342.440468.58160@e56g2000cwe.googlegroups.com>,
> <Xavier.Deepak@gmail.com> wrote:
…[13 more quoted lines elided]…
> A better suggestion might be made if more of 'your purpose' were known.

    Actually, I believe I'm in a similar situation as the OP. I've started 
looking at IBM ILE COBOL/400 code, which to my understand is meant to run in 
a specific environment (AS/400?), but all I've got around me are Windows XP 
and Linux machines running on x86 processors. If there were an "AS/400 
emulator" available for WinXP, that might come in handy for me.

    - Oliver
```

###### ↳ ↳ ↳ Re: Mainframe simulator

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2006-04-14T10:31:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TmO%f.6$%h4.102501@news.sisna.com>`
- **References:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com> <e1nvuu$hr$1@reader1.panix.com> <S1O%f.52448$K11.24004@clgrps12>`

```
Oliver,

>  I've started looking at IBM ILE COBOL/400 code, which to my understand is 
> meant to run in a specific environment (AS/400?), but all I've got around 
> me are Windows XP

The fact that I don't know any AS/400 environment emulators of course does 
not mean they don't exist but...
The major issue to convert from ILE to Win will be a screen handling which 
is very specific to as400.
If you have a lot of them it would be hard to run on Windows and might not 
make sense to convert.
The rest of the specific stuff usually done not in cobol but in CL so you 
might need to look at it to convert to C/C++ or even simple CMD files (but 
the calls from Cobol will be different).
ILE is more strict in compiling than all win-based cobols and more strict in 
runtime regarding "decimal data errors" which you might not get on Win.

With 390 it's less complicated

>> <Xavier.Deepak@gmail.com> wrote:
>>>Hi, does anyone know what mainframe software I should use on Windows

Yes, MF Express will handle most of your 390 needs including CICS, VSAM and 
DB2 and even to work in EBCDIC.
It's pretty expensive but I can't name any other good 390 emulators. At 
least nothing to compare with.

Regards,
Sergey


"Oliver Wong" <owong@castortech.com> wrote in message 
news:S1O%f.52448$K11.24004@clgrps12...
>
> <docdwarf@panix.com> wrote in message 
…[24 more quoted lines elided]…
>    - Oliver
```

###### ↳ ↳ ↳ Re: Mainframe simulator

- **From:** docdwarf@panix.com ()
- **Date:** 2006-04-14T14:37:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1oc2d$em0$1@reader1.panix.com>`
- **References:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com> <e1nvuu$hr$1@reader1.panix.com> <S1O%f.52448$K11.24004@clgrps12>`

```
In article <S1O%f.52448$K11.24004@clgrps12>,
Oliver Wong <owong@castortech.com> wrote:
>
><docdwarf@panix.com> wrote in message news:e1nvuu$hr$1@reader1.panix.com...

[snip]

>> A better suggestion might be made if more of 'your purpose' were known.
>
…[4 more quoted lines elided]…
>emulator" available for WinXP, that might come in handy for me.

A search on Google for 'winxp "as400 emulator"' (no ', include ") brought 
up a few results; some of them might suit your needs.

DD
```

###### ↳ ↳ ↳ Re: Mainframe simulator

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2006-04-15T14:38:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1r0ha02ulc@news3.newsguy.com>`
- **References:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com> <e1nvuu$hr$1@reader1.panix.com> <S1O%f.52448$K11.24004@clgrps12>`

```

In article <S1O%f.52448$K11.24004@clgrps12>, "Oliver Wong" <owong@castortech.com> writes:
> 
>     Actually, I believe I'm in a similar situation as the OP. I've started 
> looking at IBM ILE COBOL/400 code, which to my understand is meant to run in 
> a specific environment (AS/400?), but all I've got around me are Windows XP 
> and Linux machines running on x86 processors.

Yes, the ILE languages are for the IBM "System i5" machines, formerly
iSeries, formerly AS/400.  (ILE COBOL is actually the second IBM
COBOL implementation for the '400; the first was COBOL/400, renamed
"OPM COBOL/400" when ILE COBOL was introduced.)

Though i5/OS (the "native" i5 OS, though the machines can also run
AIX, and with additional hardware Linux and Windows), formerly
OS/400, is UNIX-branded, it's not at all like Windows or Linux.  For
that matter, the i5 machines aren't at all like x86 systems.  (They're
capability machines, with a single address space for all running jobs
that all OS objects are mapped to, with strong access protection;
there's a decent write-up in Wikipedia.)

That said, COBOL is for the most part COBOL.  Most of the i5-specific
stuff would be in screen handling if the application uses i5 green-
screen terminal I/O (and not, say, a web front end), in inter-
language programming, and in the development environment.  The native
i5 filesystem (IFS) is a library-based flat (non-hierarchical)
filesystem, but a typical COBOL app shouldn't care about that.

> If there were an "AS/400 
> emulator" available for WinXP, that might come in handy for me.

There may be some, but the i5's unusual and proprietary architecture 
makes emulation tricky and expensive.  There was an emulation
product available years ago that ran under AIX on RS/6000s, but I've
never seen it in action.

IBM 370-family mainframes are actually easier to emulate, because
their specifications are very well documented.  Thus we have the
Hercules open-source 370 emulator, for example.  The 400's inner
workings are less well known.
```

#### ↳ Re: Mainframe simulator

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-04-14T15:53:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B6Wdnf0sVrZ9ut3ZRVn-jw@adelphia.com>`
- **In-Reply-To:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com>`
- **References:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com>`

```
Xavier.Deepak@gmail.com wrote:
> Hi, does anyone know what mainframe software I should use on Windows
> for developing and testing mainframe components using cobol,
…[11 more quoted lines elided]…
>   
Xavier,
Google on "T3 Technologies" and "IBM PartnerWorld for Developers".

With a little digging, you will learn that T3 Technologies can supply 
you with a Thinkpad laptop that runs z/OS (even in 64-bit mode, I 
think), and PartnerWorld entitles you to IBM software that runs on that 
machine.

I have not attempted to participate in these programs myself, but if I 
were going to develop IBM mainframe software, I would definitely check 
it out very closely.
Colin Campbell
```

#### ↳ Re: Mainframe simulator

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-04-15T03:15:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VyZ%f.167308$Y53.13954@fe07.news.easynews.com>`
- **References:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com>`

```
You don't say WHAT mainframe - or what operating system.  This is usually a 
"symptom" of IBM MVS (OS/390, z/OS) mindset - which your references to "REXX" 
and "JCL" seems to confirm. ASSUMING that this is your environment, then the two 
leaders (IMHO) are:

  - Micro Focus - Mainframe Express "family of products"
 - IBM - WebSphere Developer for zSeries

Computer Associates (I can't remember what the "Realia" family is called this 
week <G>> also has a history of providing such facilities, but I don't 
(personally) think they are keeping up with what is available with z/OS (if that 
is important to you).

Fujitsu has also been a player in this field.  However, if you look at their 
documentation, they REALLY seem (to me) to make life difficult for such 
development.  Just try and find the "ADDRESS OF" special register in their 
documentation to see what I mean.

   ****

NONE of these products are inexpensive (if you want the latest version with 
ongoing support).  If you actually have an IBM mainframe, then some of these 
products do come with "enterprise editions" that are RELATIVELY price 
appropriate for LARGE development sites.

NOTE:
  The mention in another reply to this thread about the "IBM partner/developer" 
program is also a good answer if you do NOT want an "emulation" environment 
running under Windows - but instead want a "individual user" z/OS system. 
(There are LOTS of restrictions on getting into the program but it does provide 
the best way to keep current with what is actually available with IBM).

P.S.  If talking about IBM VSE there are different answers.  If you are talking 
about "OS/400" (ILE COBOL, iSeries, etc) then there are different answers for 
doing that development under Windows.

P.P.S.  If you are interested in developing under Linux or Unix-type systems, 
then there are different answers for that as well.
```

#### ↳ Re: Mainframe simulator

- **From:** "R.Freitag" <rfr-mailbox@gmx.de>
- **Date:** 2006-04-15T21:13:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1rff3$o7$1@newsreader3.netcologne.de>`
- **References:** `<1145010342.440468.58160@e56g2000cwe.googlegroups.com>`

```
Xavier.Deepak@gmail.com wrote:

> Hi, does anyone know what mainframe software I should use on Windows
> for developing and testing mainframe components using cobol,
> jcl,rexx,... with vsam files and db2 databases.

http://www.bsp-gmbh.com/turnkey/

perhaps??

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
