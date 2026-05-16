[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sha-1 on cobol2

_21 messages · 9 participants · 2005-08_

---

### Sha-1 on cobol2

- **From:** Karlos <jcv@email.pt>
- **Date:** 2005-08-04T19:17:07+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com>`

```
Hi everyone,

Can someone help me. I need to code the sha-1 in cobol2 and don't know
how. Any sugestions?

Thanks a lot

Karlos
```

#### ↳ Re: Sha-1 on cobol2

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2005-08-04T22:24:47+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lqq4f1df9mohjcnarg6o2cpkfnogbqe1en@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com>`

```
On Thu, 04 Aug 2005 19:17:07 +0100 Karlos <jcv@email.pt> wrote:

:>Can someone help me. I need to code the sha-1 in cobol2 and don't know
:>how. Any sugestions?

Does COBOL have shift instructions?

Without them, this will be quite painful.
```

##### ↳ ↳ Re: Sha-1 on cobol2

- **From:** Karlos <jcv@email.pt>
- **Date:** 2005-08-04T21:27:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6eu4f1p07dh7tabvvpr5m209qttqmmtspd@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <lqq4f1df9mohjcnarg6o2cpkfnogbqe1en@4ax.com>`

```
I don't think so.
Can you tell me how to get the sha-1 value on a string?
Do you know of any application that reads a txt file and gives another
file with the sha-1 value added to each record?

Thanks

Regards

On Thu, 04 Aug 2005 22:24:47 +0300, Binyamin Dissen
<postingid@dissensoftware.com> wrote:

>On Thu, 04 Aug 2005 19:17:07 +0100 Karlos <jcv@email.pt> wrote:
>
…[5 more quoted lines elided]…
>Without them, this will be quite painful.
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-04T21:28:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9MvIe.747014$Cl1.304847@fe03.news.easynews.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <lqq4f1df9mohjcnarg6o2cpkfnogbqe1en@4ax.com> <6eu4f1p07dh7tabvvpr5m209qttqmmtspd@4ax.com>`

```
When you say "Cobol2" - exactly what compiler are you talking about?  Certainly 
Micro Focus has "shift" routines - as does IBM (for LE environments).
```

##### ↳ ↳ Re: Sha-1 on cobol2

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-08-05T00:16:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11f5q3mgdl9in42@corp.supernews.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <lqq4f1df9mohjcnarg6o2cpkfnogbqe1en@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com> wrote in message
news:lqq4f1df9mohjcnarg6o2cpkfnogbqe1en@4ax.com...
> On Thu, 04 Aug 2005 19:17:07 +0100 Karlos <jcv@email.pt> wrote:
>
…[5 more quoted lines elided]…
> Without them, this will be quite painful.

Actually, the circular left shift from SHA1 is fairly easy.

----- subprogram
      $set notrunc
       identification division.
       program-id. cls.
      * performs circular left shift
      * of n bits on a 32-bit word
       data division.
       working-storage section.
       01 div pic 9(9) binary.
       01 mul pic 9(9) binary.
       01 new-left pic 9(9) binary.
       01 new-right pic 9(9) binary.
       linkage section.
       01 bits pic 9(9) binary.
       01 word pic 9(9) binary.
       procedure division using bits word.
       begin.
           compute div = 2 ** (32 - bits)
           compute mul = 2 ** bits
           divide word by div giving new-right
               remainder new-left
           compute word = new-left * mul + new-right
           goback.
       end program cls.
-----
```

#### ↳ Re: Sha-1 on cobol2

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-04T21:53:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7wIe.35763$iG6.25362@tornado.tampabay.rr.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com>`

```

The short answer is.

Write some code, find a compiler, link edit and execute. It's not hard :^)

But...

Why the "need" to code in Cobol2?  Let me rephrase that to avoid answering a 
question with a question which is no answer at all......I don't understand 
why you have a need to do this in COBOL, perhaps you have considered other 
alternatives such as using an pre-written C library. There are many versions 
available online - I'm sure that some have a licence that you can work with.

JCE


"Karlos" <jcv@email.pt> wrote in message 
news:spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com...
> Hi everyone,
>
…[5 more quoted lines elided]…
> Karlos
```

##### ↳ ↳ Re: Sha-1 on cobol2

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-05T13:14:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ICJIe.158894$HI.131858@edtnps84>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <j7wIe.35763$iG6.25362@tornado.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote in message 
news:j7wIe.35763$iG6.25362@tornado.tampabay.rr.com...
>
> The short answer is.
>
> Write some code, find a compiler, link edit and execute. It's not hard :^)

    That's exactly what I was thinking of posting, but decided not to; the 
original poster doesn't state whether his (her?) problem is not knowing the 
SHA-1 algorithm, not knowing COBOL, something else, or some combination of 
the three.

> But...
>
…[5 more quoted lines elided]…
> licence that you can work with.

    Plus the SHA-1 algorithm is publicly available as part of a NIST 
standard, so chances are very high you could get a library with that 
functionality for free. If you enter "SHA-1" into Wikipedia, you get pseudo 
code, and links to implementations in various languages (though not in 
COBOL).

    - Oliver
```

#### ↳ Re: Sha-1 on cobol2

- **From:** Karlos <jcv@email.pt>
- **Date:** 2005-08-05T17:56:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com>`

```
Hi all,

I'm talking about mainframe cobol mvs system.
If I find a routine that could be called by a cobol program that would
be ok.

All I want is...
ex: I've got a string lets say --> 0200123456789020.0020000001098765
and from there get the sha-1 crytogram and add at the end of the
string.

Thanks a lot to everyone

Karlos

On Thu, 04 Aug 2005 19:17:07 +0100, Karlos <jcv@email.pt> wrote:

>Hi everyone,
>
…[5 more quoted lines elided]…
>Karlos
```

##### ↳ ↳ Re: Sha-1 on cobol2

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-08-05T17:31:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CnNIe.158924$HI.46111@edtnps84>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com>`

```

"Karlos" <jcv@email.pt> wrote in message 
news:6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com...
> Hi all,
>
> I'm talking about mainframe cobol mvs system.
> If I find a routine that could be called by a cobol program that would
> be ok.

    See my post about going to Wikipedia (http://www.wikipedia.org/), 
searching for "SHA-1", and receiving lots of free implementations.

    - Oliver
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

- **From:** Karlos <jcv@email.pt>
- **Date:** 2005-08-05T19:37:17+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gec7f1lefa3u42vr4crp2i435n9ver0bk2@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com> <CnNIe.158924$HI.46111@edtnps84>`

```
Thanks a lot Oliver

On Fri, 05 Aug 2005 17:31:14 GMT, "Oliver Wong" <owong@castortech.com>
wrote:

>
>"Karlos" <jcv@email.pt> wrote in message 
…[11 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Sha-1 on cobol2

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-05T21:50:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<faRIe.954938$3V6.595518@fe04.news.easynews.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com>`

```
If you are running in an LE environment, then to accomplish a "bit shift" you 
use the LE callable service: CEESISHF

See:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea3151/2.3.3

P.S.
   Your original message used the term "Cobol2" - if you are actually still used 
(the now long unsupported) VS COBOL II compiler, this will be a problem.  You 
still haven't told me/us what compiler you are using, so I can't tell if this is 
or isn't a problem for you.
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

- **From:** Karlos <jcv@email.pt>
- **Date:** 2005-08-06T16:43:03+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bim9f1te0irdkopgvomh1smnakjc9hhcfs@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com> <faRIe.954938$3V6.595518@fe04.news.easynews.com>`

```
Hi 

I'm using the mvs cobol 390 compiler

Regards



On Fri, 05 Aug 2005 21:50:03 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>If you are running in an LE environment, then to accomplish a "bit shift" you 
>use the LE callable service: CEESISHF
…[8 more quoted lines elided]…
>or isn't a problem for you.
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-06T16:46:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kP5Je.888576$pI6.460926@fe06.news.easynews.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com> <faRIe.954938$3V6.595518@fe04.news.easynews.com> <bim9f1te0irdkopgvomh1smnakjc9hhcfs@4ax.com>`

```
There isn't a compiler by that name - and there are several that meet that 
description.  If you have manuals for your compiler (online or printed) they 
should tell you the compiler's name.  If you look at a listing, it will tell you 
the product number.
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

_(reply depth: 5)_

- **From:** Karlos <jcv@email.pt>
- **Date:** 2005-08-08T18:15:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o4ff1lkd7edjr495mv4khdj2jm1ppaufh@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com> <faRIe.954938$3V6.595518@fe04.news.easynews.com> <bim9f1te0irdkopgvomh1smnakjc9hhcfs@4ax.com> <kP5Je.888576$pI6.460926@fe06.news.easynews.com>`

```
Willian,

Its OS/390 cobol compiler. Dont forguet...its main frame.
But tomorrow I'll check a compilation



On Sat, 06 Aug 2005 16:46:09 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>There isn't a compiler by that name - and there are several that meet that 
>description.  If you have manuals for your compiler (online or printed) they 
>should tell you the compiler's name.  If you look at a listing, it will tell you 
>the product number.
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

- **From:** Clark Morris <cfmtech@istar.ca>
- **Date:** 2005-08-06T13:22:49-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0cn9f1tm686eftv8u39ep7n9qbvu9ukt1f@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <6667f19pdkv1tdg3kjr3eoomu4k31enhd3@4ax.com> <faRIe.954938$3V6.595518@fe04.news.easynews.com>`

```
Given the call overheads, wouldn't doing the appropriate multiply's
and divides be faster?

I replaced a pair of called subroutines for packing and unpacking bit
switches with not overly efficient performed paragraphs for that
reason.

On Fri, 05 Aug 2005 21:50:03 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>If you are running in an LE environment, then to accomplish a "bit shift" you 
>use the LE callable service: CEESISHF
…[8 more quoted lines elided]…
>or isn't a problem for you.
```

#### ↳ Re: Sha-1 on cobol2

- **From:** Karlos <jcv@email.pt>
- **Date:** 2005-08-10T18:59:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<04gkf1hf5c1rd6i904ti6k10esu98uooq8@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com>`

```
version is IBM VS COBOL II

On Thu, 04 Aug 2005 19:17:07 +0100, Karlos <jcv@email.pt> wrote:

>Hi everyone,
>
…[5 more quoted lines elided]…
>Karlos
```

##### ↳ ↳ Re: Sha-1 on cobol2

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-08-10T20:26:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tptKe.110670$_I2.39079@fe03.news.easynews.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <04gkf1hf5c1rd6i904ti6k10esu98uooq8@4ax.com>`

```
Then you are out-of-luck (in more ways than one) - especially for bit-twiddling.

Not only is that compiler LONG out-of-service (from IBM), it means that you may 
NOT use any of the LE callable services - for bit manipulation.

You really should find out from your systems people WHY you are still using that 
VERY old compiler.
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

- **From:** Karlos <jcv@email.pt>
- **Date:** 2005-08-11T18:40:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373nf1tmupgve8jteapnpu67ifoplrathp@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <04gkf1hf5c1rd6i904ti6k10esu98uooq8@4ax.com> <tptKe.110670$_I2.39079@fe03.news.easynews.com>`

```
Well ... maybe it's because of money.

Anyway... I think the only way is to get the file from the main frame
the with a VB or C program to get the corresponding SHA-1 and add to
the  record.

Thanks a lot everibody.

By the way... where can I get Fujitso netcobol craked?

On Wed, 10 Aug 2005 20:26:01 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Then you are out-of-luck (in more ways than one) - especially for bit-twiddling.
>
…[4 more quoted lines elided]…
>VERY old compiler.
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

_(reply depth: 4)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-08-12T00:10:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hORKe.6833$dJ5.6334@tornado.tampabay.rr.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <04gkf1hf5c1rd6i904ti6k10esu98uooq8@4ax.com> <tptKe.110670$_I2.39079@fe03.news.easynews.com> <373nf1tmupgve8jteapnpu67ifoplrathp@4ax.com>`

```
"Karlos" <jcv@email.pt> wrote in message 
news:373nf1tmupgve8jteapnpu67ifoplrathp@4ax.com...
> Well ... maybe it's because of money.
>
…[6 more quoted lines elided]…
> By the way... where can I get Fujitso netcobol craked?

Probably on a very illegal site...also not a good idea to ask this...and 
piracy sucks...but thanks for asking.

JCE
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

_(reply depth: 5)_

- **From:** Russell <rws0203nospam@comcast.net>
- **Date:** 2005-08-12T08:04:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns96B05C4DFCC65rws0203comcastnet@216.196.97.131>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <04gkf1hf5c1rd6i904ti6k10esu98uooq8@4ax.com> <tptKe.110670$_I2.39079@fe03.news.easynews.com> <373nf1tmupgve8jteapnpu67ifoplrathp@4ax.com> <hORKe.6833$dJ5.6334@tornado.tampabay.rr.com>`

```
"jce" <defaultuser@hotmail.com> wrote in news:hORKe.6833$dJ5.6334
@tornado.tampabay.rr.com:

> "Karlos" <jcv@email.pt> wrote in message 
> news:373nf1tmupgve8jteapnpu67ifoplrathp@4ax.com...
…[16 more quoted lines elided]…
> 

    	If you are determined to do this, I suggest that you do it off of the 
network (eg turn ALL other pc's off), and back up your pc with ghost or 
something similar.  Your pc is almost certainly going to be hosed when you 
are done.  Copy booty to cd or floppy, and restore image.

    	Most of the sites I have looked at seem to be full of spyware and 
virus's.  Not worth the trouble.

    	And how do you know the crack is safe?
```

###### ↳ ↳ ↳ Re: Sha-1 on cobol2

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-08-12T19:08:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d64ac$42fd3a0e$45491c57$20026@KNOLOGY.NET>`
- **In-Reply-To:** `<373nf1tmupgve8jteapnpu67ifoplrathp@4ax.com>`
- **References:** `<spm4f15afhf10l9kvhlknu9jrj31mnjgln@4ax.com> <04gkf1hf5c1rd6i904ti6k10esu98uooq8@4ax.com> <tptKe.110670$_I2.39079@fe03.news.easynews.com> <373nf1tmupgve8jteapnpu67ifoplrathp@4ax.com>`

```
Karlos wrote:
> 
> By the way... where can I get Fujitso netcobol craked?

I imagine if you bought the CD's, a hammer could probably make 'em 
cracked...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
