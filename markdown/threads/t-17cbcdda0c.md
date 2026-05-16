[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MS Cobol 4.5 an large Programs

_6 messages · 5 participants · 2000-11_

---

### MS Cobol 4.5 an large Programs

- **From:** "Hans Jakschik" <SPECTRA.Soft@t-online.de>
- **Date:** 2000-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8u6aqn$huq$01$1@news.t-online.com>`

```
Hi!

Using Microsoft Cobol 4.5 for many years  I'm now trying to compile, link
and animate a very large program. Although everything worked fine with small
and medium-sized programms I now get strange loading errors. e.g. Code 170
(System program not found: ADIS.EXE or CHECK.G06). ANIM-directive is
ignored,....
Seems if something is wrong with main memory allocation.

Can you send me an example of a COBOL.DIR, CONFIG.SYS and AUTOEXEC.BAT and
the appropiate BAT-files to compile, link and animate large programs?
Do you have an idea how to solve this problem.

Platform is WIN98. Free memory is 602K.

Thanks in advance!

Hans
```

#### ↳ Re: MS Cobol 4.5 an large Programs

- **From:** Alain Chappuis <Alain.Chappuis@medecine.unige.ch>
- **Date:** 2000-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A06B5CE.17A4C3E8@medecine.unige.ch>`
- **References:** `<8u6aqn$huq$01$1@news.t-online.com>`

```


Hans Jakschik a écrit :
> 
> Hi!
…[5 more quoted lines elided]…
> ignored,....

I think that you did not linked your modules with adis.obj...

Alain.
```

#### ↳ Re: MS Cobol 4.5 an large Programs

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BuWN5.6451$pj3.29744@news1.atl>`
- **References:** `<8u6aqn$huq$01$1@news.t-online.com>`

```
Your easiest upgrade path is probably MERANT Micro Focus Net Express
3.1, but prepare yourself for sticker shock! :-)
```

##### ↳ ↳ Net Exprss Cost (was: MS Cobol 4.5 an large Programs

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8uapcu$muk$1@slb1.atl.mindspring.net>`
- **References:** `<8u6aqn$huq$01$1@news.t-online.com> <BuWN5.6451$pj3.29744@news1.atl>`

```
I don't usually get into "cost" threads (of former employers - or other
COBOL vendors) but as long as Judson brought up this topic, I would like to
suggest that non-MERANT COBOL customers in the US might want to go to the

   http://www.cobolreport.com/

web page and "click" on the banner at the top of the page where it talks
about

 "Limited Time, Special Offer
   Net Express only $999!"
```

###### ↳ ↳ ↳ Re: Net Exprss Cost (was: MS Cobol 4.5 an large Programs

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RhcO5.601$Ik.1221@news2.atl>`
- **References:** `<8u6aqn$huq$01$1@news.t-online.com> <BuWN5.6451$pj3.29744@news1.atl> <8uapcu$muk$1@slb1.atl.mindspring.net>`

```
Thanks, Bill!  I have a friend that will probably jump on that like
a chicken on a bug (my farm background, you know).  The normal cost
is like $3650.
```

#### ↳ Re: MS Cobol 4.5 an large Programs

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-11-07T08:23:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A07BC06.BF661F20@Azonic.co.nz>`
- **References:** `<8u6aqn$huq$01$1@news.t-online.com>`

```
> Using Microsoft Cobol 4.5 for many years  I'm now trying to compile, link
> and animate a very large program. Although everything worked fine with small
…[9 more quoted lines elided]…
> Platform is WIN98. Free memory is 602K.

I am surprised that it works at all. MS tends to try to force everyone
into upgrade frenzies by making sure that older versions (or competitors
latest) stop working on newer Windows.

The ANIM directive should be writing .IDY and other files that are used
by the Animator and the object code should be produced as .INT.  You may
need to force .INT format using OPT"0".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
