[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "API" problem

_4 messages · 2 participants · 1998-09_

---

### "API" problem

- **From:** "Tony Tynan" <ttynan@iol.ie>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bde1ba$79b65100$3a307dc2@default>`

```

Help would be great.......

Got "Microsoft COBOL For DOS and OS/2 Systems"  Version 4, on floppies. 
Installed it with SETUP from the FDs and took the defaults.

With sleeves rolled up ready to banish 30-yr old COBOL cobwebs.............

Problem:  On entering the COBOL verb (followed by a demo filename from the
set)   I get the message
'The Application Program Interface (API) entered will only work in
Microsoft Operating System/2  mode'

A .BAT proggie in the DEMO dir. will, however appear to run OK

I won't bore the readership (yet!) with the various investigations I've
done like like  RTFM'ing and checking that the right .DLLs  & not the DLE's
(or vice versa) or otherwise that are supposed to be there are there,   but
if anybody can say " Aha! you have to add this line to your CONFIG etc or
change that line...   I'd be most grateful and would save much further
head-banging off wall.

This problem is the same on my-

a)  Olde DX2-66 486 PC and  (DOS 6.2 and WFW 3.z)
b)  PII 233 m/c running Win 95 booted in MS-DOS ( 7.z  I expect)

Many thanks
```

#### ↳ Re: "API" problem

- **From:** "Paddy Coleman" <pc@microfocus.com>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tr8ma$kth@hyperion.mfltd.co.uk>`
- **References:** `<01bde1ba$79b65100$3a307dc2@default>`

```
Tony,

The EXEs that you are trying to run are bound i.e. they run on both DOS and
OS/2.
They determine which by looking at the type of memory manager that is
present
(if memory serves).  In your case you have loaded the DOS EMM386 program
which fools the EXEs in to thinking it is OS/2.  As it is not you get the
error
message you described.

As far as I am aware the solution is to:

1)  Remove EMM386 from your environment whilst running COBOL.
2)  Upgrade to a later version of COBOL which was released after EMM386 and
can cope.

Hope this helps.

Paddy Coleman
Team Leader, Distributed Computing Support (WinTel)
Micro Focus International.




Tony Tynan wrote in message <01bde1ba$79b65100$3a307dc2@default>...
>
>Help would be great.......
…[25 more quoted lines elided]…
>Many thanks
```

##### ↳ ↳ Re: "API" problem

- **From:** "Tony Tynan" <ttynan@iol.ie>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bde268$c3b5f540$1a307dc2@default>`
- **References:** `<01bde1ba$79b65100$3a307dc2@default> <6tr8ma$kth@hyperion.mfltd.co.uk>`

```
Paddy

Very many thanks for the tip.   I'll look into it straight away and revert
asap.  

Rgds

PS I've had some trouble in the past arising from  EMM386 Vs.  other memory
managers loaded - but can't remember the details.

 
Paddy Coleman <pc@microfocus.com> wrote in article
<6tr8ma$kth@hyperion.mfltd.co.uk>...
> Tony,
> 
> The EXEs that you are trying to run are bound i.e. they run on both DOS
and
> OS/2.
etc
```

##### ↳ ↳ Re: "API" problem

- **From:** "Tony Tynan" <ttynan@iol.ie>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bde280$f6073280$3c307dc2@default>`
- **References:** `<01bde1ba$79b65100$3a307dc2@default> <6tr8ma$kth@hyperion.mfltd.co.uk>`

```
Many thanks for this help which has fixed current problem.  no reference to
EMM386 in my AUTO or CONFIG files, but it was snuck in there in the
\WINDOWS dir, so,  I temporarily renamed it and rebooted without any ill
effects. (Mustn't forget to restore it though)  Now I just plough ahead
'til I meet the (inevitable) next challenge!  Out with pessimism, say I.

Regards again
Paddy Coleman <pc@microfocus.com> wrote in article
<6tr8ma$kth@hyperion.mfltd.co.uk>...
> Tony,
> .  In your case you have loaded the DOS EMM386 program
…[3 more quoted lines elided]…
> (Snipped)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
