[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fatal error

_20 messages · 10 participants · 2003-09 → 2003-10_

---

### Fatal error

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-09-22T19:17:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bknhsj$cc8$1@hercules.btinternet.com>`

```
Anybody know what the following Netexpress error means.

C:\sources\qpsdb>cbllink QPS_UPDATE.cbl
Micro Focus Net Express - CBLLINK utility
Version 4.0.38 Copyright (C) 1984-2003 Micro Focus International Ltd.

Micro Focus Net Express V4
Version 4.0.38 Copyright (C) 1984-2003 Micro Focus International Ltd.
URN AXCGG/AA0/00000
* Checking complete with no errors - starting code generation
* Generating QPS_UPDATE
* 001-F Internal error 38. Contact technical support
ERROR: (9) Program indicated failure




I don't think I can contact technical support since I don't have a support
contract.

Any ideas gratefully received
```

#### ↳ Re: Fatal error

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-23T00:10:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309222310.2177cdef@posting.google.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com>`

```
"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote 

> * Generating QPS_UPDATE
> * 001-F Internal error 38. Contact technical support
> ERROR: (9) Program indicated failure

Run out of disk space ?

Specified output directory doesn't exist ?
```

##### ↳ ↳ Re: Fatal error

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-09-23T07:18:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkos4e$9td$1@hercules.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0309222310.2177cdef@posting.google.com...
> "Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote
>
…[6 more quoted lines elided]…
> Specified output directory doesn't exist ?

Nope 36 Gb available and I didn't specify an output directory.


Steve
```

###### ↳ ↳ ↳ Re: Fatal error

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-09-23T12:41:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkpf28$nta$1@titan.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com>`

```

"Steve Rainbird" <steve.rainbird@nospam.mssint.com> wrote in message
news:bkos4e$9td$1@hercules.btinternet.com...
>
> "Richard" <riplin@Azonic.co.nz> wrote in message
…[16 more quoted lines elided]…
>

If anybody from Microfocus cares this is what causes your compiler to crash.
(I know the code is crap but the compiler should not abort like it does).

       data  division.
       working-storage section.
       77  77-int pic 9(12).
       77  77-int-part pic s9(11)v9(4) comp.
       77  77-dec-part pic s9(1)v9(16) comp.
       procedure division.
       main section.
           divide 1 into 77-int
             giving 77-int-part
             remainder 77-dec-part
           stop run.

This gives
Micro Focus Net Express - CBLLINK utility
Version 4.0.38 Copyright (C) 1984-2003 Micro Focus International Ltd.

Micro Focus Net Express V4
Version 4.0.38 Copyright (C) 1984-2003 Micro Focus International Ltd.
URN AXCGG/AA0/00000
* Checking complete with no errors - starting code generation
* Generating xx
* 001-F Internal error 38. Contact technical support
ERROR: (9) Program indicated failure

regards

Steve
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 4)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-23T20:54:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030923165417.29142.00000072@mb-m24.aol.com>`
- **References:** `<bkpf28$nta$1@titan.btinternet.com>`

```
But isn't this just uninitialized data?

  77  77-int pic 9(12).

Dividing uninitialized data could cause a runtime error. That is not
impossible.

as in 

divide 1 into 77-int
             giving 77-int-part
             remainder 77-dec-part


Perhaps you have only presented a portion of the code. 

Your actual code presented is 
<<
 main section.
           divide 1 into 77-int
             giving 77-int-part
             remainder 77-dec-part
           stop run.
>>

Do not know if you are just sketching it to give a flavor of the frustration or
if this is failry exact.  You would be perhaps better off with a period at the
end of the arithmetic statement (divide) and before the stop run.

Arithmetic statements can have certain conditional clauses (on error, not on
error) and you may have found a weakness in the compiler that does not see the
stop run statement.

I am not trying to be picky, just helpful. If the posting is exact, then the
recommendation would be to init all numerics, and dress up the procedures with
any and all available  scope delimiters (like period).

If your code was meant as a sketch, sorry for my excess focus on detail. 

If there is anything after that stop run, like a paragraph that does I/O, you
could get a drop through that sends out spurious error messages 

Best Wishes,
Bob Rayhawk
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 5)_

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2003-09-23T22:22:25+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8be1nv0ot055b1ovjofhjo96sp2g7mar1s@4ax.com>`
- **References:** `<bkpf28$nta$1@titan.btinternet.com> <20030923165417.29142.00000072@mb-m24.aol.com>`

```
On 23 Sep 2003 20:54:17 GMT, rkrayhawk@aol.com (RKRayhawk) wrote:

>But isn't this just uninitialized data?
>
…[3 more quoted lines elided]…
>impossible.
The error is when COMPILING the program. He can't even run it!!.





Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-09-23T18:00:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tYycnbszUbMWTe2iU-KYuQ@giganews.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com>`

```
Steve Rainbird wrote:
> If anybody from Microfocus cares this is what causes your compiler to
> crash. (I know the code is crap but the compiler should not abort
…[24 more quoted lines elided]…
> ERROR: (9) Program indicated failure

MF is like an undertaker. They get paid to care. If they don't get paid...
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-23T23:24:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PC4cb.1047$RW4.468@newsread4.news.pas.earthlink.net>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com>`

```
What do you think the compiler could say any clearer than

   "Contact technical support"

If you aren't currently paid up for support, then you DO have a problem, but
I can't say that I think it is Micro Focus' problem.

That message seems about as clear as any message that a compiler could issue
when an "internal" error occurs.
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 5)_

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-09-24T14:52:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bksb2u$8t1$2@titan.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com> <PC4cb.1047$RW4.468@newsread4.news.pas.earthlink.net>`

```
It could say,

Problem at line nnnn contact technical support

Then at least I would have had some idea where the problem was.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:PC4cb.1047$RW4.468@newsread4.news.pas.earthlink.net...
> What do you think the compiler could say any clearer than
>
>    "Contact technical support"
>
> If you aren't currently paid up for support, then you DO have a problem,
but
> I can't say that I think it is Micro Focus' problem.
>
> That message seems about as clear as any message that a compiler could
issue
> when an "internal" error occurs.
>
…[30 more quoted lines elided]…
> > (I know the code is crap but the compiler should not abort like it
does).
> >
> >        data  division.
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 6)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-09-24T17:34:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DAkcb.157068$3o3.11227707@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com> <PC4cb.1047$RW4.468@newsread4.news.pas.earthlink.net> <bksb2u$8t1$2@titan.btinternet.com>`

```

Steve Rainbird <steve.rainbird@nospam.mssint.com> wrote in message news:bksb2u$8t1$2@titan.btinternet.com...
> It could say,
>
> Problem at line nnnn contact technical support
>
> Then at least I would have had some idea where the problem was.

 When I encounter an issue such as this, I experiment,
one change at a time, until I isolate the cause of the problem.

I saw a number of things that I didn't like in the code sample.

However, those are really different issues.

Your main point, which I agree with, is that exception errors
are almost always handled in an inexcusably obtuse manner.

This holds true for IBM, Microsoft, Compuware and the vast
majority of applications programmers. who fail to realize
that, for example, the technically-oriented gibberish that they
just included in the online screen's message field does nothing
to advise the user that they need to add a customer to the
customer master file, or a part number to the part master file.

They justify this sort of thinking by 'rationalizing' that
"the part had to exist for the order to be booked in the first place,
 so if it is missing here then we have a serious problem".
They failed to anticipate that the part may be deleted after
the order was created, due to a programmer failing to insert
the necessary edits in a part master maintenance program,
or perhaps subsequent program maintenance created a path
which caused such an edit to be bypassed.

The technical data can and should be sent via email
to an applications support mailing list or group.
The message returned to the user, such as the compiler diagnostic,
should be in non-technical plain English, or the appropriate foreign language.
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-24T21:24:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YXncb.2113$NX3.786@newsread3.news.pas.earthlink.net>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com> <PC4cb.1047$RW4.468@newsread4.news.pas.earthlink.net> <bksb2u$8t1$2@titan.btinternet.com> <DAkcb.157068$3o3.11227707@bgtnsc05-news.ops.worldnet.att.net>`

```
I may be mistaken, but it seems to me that the original example is similar
to IBM (mainframe) compilers getting a U-level message.  What is happened is
that INTERNALLY something "totally unexpected" has happened and that there
is no "associated" line causing the problem.  Often this is due to some "it
can never happen" size limitation has been exceeded or some COMBINATION of
restrictions have been violated.

If it truly turns out that the original message WAS caused by a single
"statement" (much less line) in the source code, then the vendor (Micro
Focus) should fix the message.  If, as I suspect, it was a combination of
"problems" then I still think this is the best possible message.
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 4)_

- **From:** Wiggy <wignomore@btopenworld.com>
- **Date:** 2003-09-24T00:14:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bkqnla$eho$1@hercules.btinternet.com>`
- **In-Reply-To:** `<bkpf28$nta$1@titan.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com>`

```
Steve Rainbird wrote:
> If anybody from Microfocus cares this is what causes your compiler to crash.
> (I know the code is crap but the compiler should not abort like it does).
…[23 more quoted lines elided]…
> ERROR: (9) Program indicated failure

Steve, just to confirm my response on the cobolportal forum, I'm 
following up on this with MF Development.

Simon.
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 5)_

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-09-24T14:44:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bksaji$ju5$1@hercules.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com> <bkqnla$eho$1@hercules.btinternet.com>`

```

"Wiggy" <wignomore@btopenworld.com> wrote in message
news:bkqnla$eho$1@hercules.btinternet.com...
> Steve Rainbird wrote:
> > If anybody from Microfocus cares this is what causes your compiler to
crash.
> > (I know the code is crap but the compiler should not abort like it
does).
> >
> >        data  division.
…[27 more quoted lines elided]…
>

Yes thanks Simon.
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 4)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-26T00:19:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vn7j3rru9bd187@corp.supernews.com>`
- **In-Reply-To:** `<bkpf28$nta$1@titan.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com>`

```
Steve Rainbird wrote:

> If anybody from Microfocus cares this is what causes your compiler to crash.
> (I know the code is crap but the compiler should not abort like it does).
> 
>        data  division.

I don't believe the Identification Division is optional in any version 
of COBOL.  Yes, the compiler shouldn't crap out, but looking at your 
output...

> Micro Focus Net Express V4
> Version 4.0.38 Copyright (C) 1984-2003 Micro Focus International Ltd.
…[4 more quoted lines elided]…
> ERROR: (9) Program indicated failure

Note that the code is found to contain no errors, and it appears it may 
be assigning the program name XX to it.  Don't know if that's the 
problem or not, but it's where I would start looking - the program's 
gotta have a name.  :)
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-26T06:52:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CmRcb.4782$NX3.2632@newsread3.news.pas.earthlink.net>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com> <vn7j3rru9bd187@corp.supernews.com>`

```
Believe it or not, the Identification Division *IS* optional in Micro
Focus - where the LRM includes the following,

"Another way to identify the first source element defined in a file is with
the basename, which is derived from the filename of the file containing the
source element. "
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-09-26T16:42:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F746D98.CB535D03@shaw.ca>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com> <vn7j3rru9bd187@corp.supernews.com> <CmRcb.4782$NX3.2632@newsread3.news.pas.earthlink.net>`

```


"William M. Klein" wrote:

> Believe it or not, the Identification Division *IS* optional in Micro
> Focus - where the LRM includes the following,
…[4 more quoted lines elided]…
>

To emphasize Bill's comments as they relate to Micro Focus allowing you to
ignore 'red tape' syntax :-

Non-OO - Procedural :-

*>---------------------
display 'Hello World'
*>---------------------

OO :-

*>------------------------------------
Method-id. "PB-CancelCountry".
*>------------------------------------
*> I could have Local-storage section variables in here.
invoke os-CountryDialog "hide"
invoke os-Treeview "removeSelection"
invoke os-Treeview "show"
End Method "PB-CancelCountry".
*>------------------------------------

For the latter, I only need the syntax "Linkage Section and Procedure
Division........" where I have either/both   "using..xxx. returning.yyy"

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 5)_

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-09-26T07:55:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl0rdb$3oa$1@titan.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com> <vn7j3rru9bd187@corp.supernews.com>`

```
The source was called xx.cbl the object is called xx.  Its just an example.

"LX-i" <LXi0007@Netscape.net> wrote in message
news:vn7j3rru9bd187@corp.supernews.com...
> Steve Rainbird wrote:
>
> > If anybody from Microfocus cares this is what causes your compiler to
crash.
> > (I know the code is crap but the compiler should not abort like it
does).
> >
> >        data  division.
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fatal error

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-10-23T20:03:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vpguigroptkq71@corp.supernews.com>`
- **In-Reply-To:** `<bl0rdb$3oa$1@titan.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <217e491a.0309222310.2177cdef@posting.google.com> <bkos4e$9td$1@hercules.btinternet.com> <bkpf28$nta$1@titan.btinternet.com> <vn7j3rru9bd187@corp.supernews.com> <bl0rdb$3oa$1@titan.btinternet.com>`

```
Steve Rainbird wrote:

> The source was called xx.cbl the object is called xx.  Its just an example.

That's what I get for commenting even though I haven't used MicroFocus 
since COBOL class several years ago.  Sorry...

(history below, since it's been almost a month...)

> 
> "LX-i" <LXi0007@Netscape.net> wrote in message
…[47 more quoted lines elided]…
> 
```

#### ↳ Re: Fatal error

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-09-23T17:59:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Po2cnRwSJovHTe2iU-KYuQ@giganews.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com>`

```
Steve Rainbird wrote:
> Anybody know what the following Netexpress error means.
>
…[18 more quoted lines elided]…
> Any ideas gratefully received

Since MF won't or can't fix the problem, you have no choice but to quit
doing whatever it is you're doing that causes the message. Find another way
to accomplish the results you want.

On the other hand, are you sure you don't have a maintenance contract? I
notice the copyright date on the compiler is 2003.
```

##### ↳ ↳ Re: Fatal error

- **From:** "Steve Rainbird" <steve.rainbird@nospam.mssint.com>
- **Date:** 2003-09-24T14:52:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bksb2u$8t1$1@titan.btinternet.com>`
- **References:** `<bknhsj$cc8$1@hercules.btinternet.com> <Po2cnRwSJovHTe2iU-KYuQ@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:Po2cnRwSJovHTe2iU-KYuQ@giganews.com...
> Steve Rainbird wrote:
> > Anybody know what the following Netexpress error means.
…[22 more quoted lines elided]…
> doing whatever it is you're doing that causes the message. Find another
way
> to accomplish the results you want.
>
…[3 more quoted lines elided]…
>

This was the reply when I wanted to tell them about a bug before

Dear Steve,

I've just received the mail below concerning your Web Request for help.

It would seem that when you purchased the licence no maintenance was decided
to be taken out with it. I'm afraid that without it you are not entitled to
any technical assistance or free of charge product updates.

If you would be interested in receiving a quote for maintenance do let me
know.

Many thanks

Tami Carwell-Cooke

Micro Focus Support Net Telesales

Tel + 44 (0) 1635 565532

Fax + 44 (0) 1635 565525



I have found that if its a real bug then if I start up a discussion here or
on the Microfocus forum then someone from microfocus will pick it up and
report it.

I realise its my companies fault, actually not my company I'm a contactor,
but I don't really want a fix I just want to report a bug.





Regards
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
