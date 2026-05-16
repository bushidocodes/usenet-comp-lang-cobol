[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol compiler under Linux

_11 messages · 8 participants · 2001-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Cobol compiler under Linux

- **From:** "Yoyo" <yoyothebest@multimania.com>
- **Date:** 2001-04-11T23:01:44+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad4c650$0$192$456d72a3@news.skynet.be>`

```
I have been looking for months and I haven't been able to find good free
compiler under Linux.
Under Windows there is Fujitsu Cobol (not the best I think). Is there
somebody here that can tell me what I should use under Linux.

I am wondering if anybody here use Cobol because he love it. Me I have been
forced to learn it for my cursus but I hated it (compare to the C++). You?

Yoyo
```

#### ↳ Re: Cobol compiler under Linux

- **From:** qIroS <qIroS@tlhIngan.co.uk>
- **Date:** 2001-04-12T08:32:04+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be>`

```
ghItlh "Yoyo" <yoyothebest@multimania.com> 

>I have been looking for months and I haven't been able to find good free
>compiler under Linux.
…[7 more quoted lines elided]…
>

Tinycobol is currently the most functional free compiler for linux.

Horses for courses. Comparing languages is emotive.
```

##### ↳ ↳ Re: Cobol compiler under Linux

- **From:** "Onder OZ" <kucuk_calik@yahoo.com>
- **Date:** 2001-04-12T12:00:51+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b3ncm$p5a2@baran22.ttnet.net.tr>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be> <02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com>`

```
Does TinyCOBOL run on SCO-UNIX as well? I Tried hard but couldn't succeed.

SCO-UNIX OpenServer 5,
GCC (downloaded from www.sco.com/skunkware)
i even couldn't compile the compiler :)

TYFH

Onder OZ

"qIroS" <qIroS@tlhIngan.co.uk>, haber iletisinde �unlar�
yazd�:02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com...
> ghItlh "Yoyo" <yoyothebest@multimania.com>
>
…[5 more quoted lines elided]…
> >I am wondering if anybody here use Cobol because he love it. Me I have
been
> >forced to learn it for my cursus but I hated it (compare to the C++).
You?
> >
> >Yoyo
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol compiler under Linux

- **From:** qIroS <qIroS@tlhIngan.co.uk>
- **Date:** 2001-04-12T11:42:42+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ek1bdtk5clse169shoi2qs08mhk3qeq6an@4ax.com>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be> <02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com> <9b3ncm$p5a2@baran22.ttnet.net.tr>`

```
ghItlh "Onder OZ" <kucuk_calik@yahoo.com> 

>Does TinyCOBOL run on SCO-UNIX as well? I Tried hard but couldn't succeed.
>

I've not tried it, sorry.
```

###### ↳ ↳ ↳ Re: Cobol compiler under Linux

- **From:** David Essex <dessex@arvotek.net>
- **Date:** 2001-04-13T02:54:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD6A29D.907344D6@arvotek.net>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be> <02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com> <9b3ncm$p5a2@baran22.ttnet.net.tr>`

```
Onder OZ wrote:
> 
> Does TinyCOBOL run on SCO-UNIX as well? I Tried hard but couldn't succeed.
…[3 more quoted lines elided]…
> i even couldn't compile the compiler :)

TinyCOBOL will run on IA32 platforms only.

The only currently supported platforms are Linux, FreeBSD, and Win32
(using the Cygwin emulation layer). 

There was an unconfirmed report that it ran on Solaris for IA32.

However since TinyCOBOL generates GNU assembler (ATT type), it may be
(and I stress MAYBE) possible to port it to run on SCO.


David Essex
```

##### ↳ ↳ Re: Cobol compiler under Linux

- **From:** "Charles F. Townsend" <ctowns@ix.netcom.com>
- **Date:** 2001-04-19T06:00:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ADEE162.4BF7FFE9@ix.netcom.com>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be> <02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com>`

```
I believe there are three COBOL compilers that will run under Linux: Micro Focus
(Merant), AcuCobol(AcuCorp) and PERCobol(LegacyJ).  I a little partial to the
LegacyJ PERCobol compiler.

Charles Townsend
LegacyJ


qIroS wrote:

> ghItlh "Yoyo" <yoyothebest@multimania.com>
>
…[13 more quoted lines elided]…
> Horses for courses. Comparing languages is emotive.
```

###### ↳ ↳ ↳ Re: Cobol compiler under Linux

- **From:** qIroS <qIroS@tlhIngan.co.uk>
- **Date:** 2001-04-19T18:17:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4a7udtc210ik7l58e0sgn60l7rpmk277uc@4ax.com>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be> <02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com> <3ADEE162.4BF7FFE9@ix.netcom.com>`

```
ghItlh "Charles F. Townsend" <ctowns@ix.netcom.com> 

>I believe there are three COBOL compilers that will run under Linux: Micro Focus
>(Merant), AcuCobol(AcuCorp) and PERCobol(LegacyJ).  I a little partial to the
…[3 more quoted lines elided]…
>LegacyJ

Yes but as the original poster was requiring a free compiler, the
above products (including yours) won't solve the posters problem.

That is unless you plan on releasing an unlimited evaluation version
for people to experiment with?
```

###### ↳ ↳ ↳ Re: Cobol compiler under Linux

_(reply depth: 4)_

- **From:** "Charles F. Townsend" <ctowns@ix.netcom.com>
- **Date:** 2001-04-20T07:21:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AE045F4.67D04B4B@ix.netcom.com>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be> <02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com> <3ADEE162.4BF7FFE9@ix.netcom.com> <4a7udtc210ik7l58e0sgn60l7rpmk277uc@4ax.com>`

```
I suppose nothing will solve the poster's problem.

If all the poster wants to do is experiment, they can download an evaluation version
of the LegacyJ PERCobol compiler and experiment for a few days. If a commercial
compiler is desired then purchase a compiler from one of the four companies offering
a COBOL compiler on Linux (AcuCorp, LegacyJ, Liant or Merant).  Tom, I got your
message about Liant's compiler on Linux.

Charles Townsend
LegacyJ

qIroS wrote:

> ghItlh "Charles F. Townsend" <ctowns@ix.netcom.com>
>
…[11 more quoted lines elided]…
> for people to experiment with?
```

###### ↳ ↳ ↳ Re: Cobol compiler under Linux

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2001-04-19T12:59:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xJFD6.5$I22.1547@nnrp1.sbc.net>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be> <02madtsp8hqcair6uqsonvrbrfhdn6msb7@4ax.com> <3ADEE162.4BF7FFE9@ix.netcom.com>`

```
Aw, Chuck...

You forgot RM/COBOL (Liant)!

;-)

Regards,
Tom Morrison
Liant

Charles F. Townsend <ctowns@ix.netcom.com> wrote in message
news:3ADEE162.4BF7FFE9@ix.netcom.com...
> I believe there are three COBOL compilers that will run under Linux: Micro
Focus
> (Merant), AcuCobol(AcuCorp) and PERCobol(LegacyJ).  I a little partial to
the
> LegacyJ PERCobol compiler.
>
> Charles Townsend
> LegacyJ
```

#### ↳ Re: Cobol compiler under Linux

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-04-12T22:39:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad589b0_4@my.newsfeeds.com>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be>`

```
I use COBOL because I love it.

(That's one...)

Pete.

Yoyo wrote in message <3ad4c650$0$192$456d72a3@news.skynet.be>...
>I have been looking for months and I haven't been able to find good free
>compiler under Linux.
…[8 more quoted lines elided]…
>



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

#### ↳ Re: Cobol compiler under Linux

- **From:** "Steven O. Ellis" <soellis@soltec.net>
- **Date:** 2001-04-28T18:44:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AEB55C7.5D149850@soltec.net>`
- **References:** `<3ad4c650$0$192$456d72a3@news.skynet.be>`

```
I use COBOL because the type of programming I do requires COBOL --
that's
what my employers use.

Anyway, COBOL is a workhorse.  The functionality is there, the syntax is
readily grasped, and you aren't going to spend a lot of time debugging
syntactical errors.  I respect COBOL, and I can have fun with it at
times.
But my employers are paying me for timely code maintenance and
enhancement, 
that is, production.  

My two cents.


Yoyo wrote:
> 
> I have been looking for months and I haven't been able to find good free
…[7 more quoted lines elided]…
> Yoyo
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
