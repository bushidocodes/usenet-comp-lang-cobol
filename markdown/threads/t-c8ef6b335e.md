[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# string mixed to string in CAPITALS

_41 messages · 13 participants · 1999-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### string mixed to string in CAPITALS

- **From:** "Alberto Santamaria Garcia" <kikesan@euskalnet.net>
- **Date:** 1999-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fcs5t$jj39@eui1nw.euskaltel.es>`

```
HOW CAN I CONVERT ANY STRING IN COBOL TO A STRING WITH ONLY CAPITALS
CHARACTERS?
```

#### ↳ Re: string mixed to string in CAPITALS

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371a03ff.145502977@news1.ibm.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es>`

```
On Sun, 18 Apr 1999 16:11:56 +0200, "Alberto Santamaria Garcia"
<kikesan@euskalnet.net> wrote:

>HOW CAN I CONVERT ANY STRING IN COBOL TO A STRING WITH ONLY CAPITALS
>CHARACTERS?
>

Function Upper-Case - but it looks like you already figured that out.
<G>
```

#### ↳ Re: string mixed to string in CAPITALS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fd087$37i@sjx-ixn6.ix.netcom.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es>`

```
Look at the intrinsic function -
   UPPER-CASE
```

##### ↳ ↳ Re: string mixed to string in CAPITALS

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ffj1a$f0a$1@nnrp1.dejanews.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd087$37i@sjx-ixn6.ix.netcom.com>`

```
In article <7fd087$37i@sjx-ixn6.ix.netcom.com>,
  "William M. Klein" <wmklein at ix dot netcom dot com> wrote:
> Look at the intrinsic function -
>    UPPER-CASE

Bill,

How about the standard? Does FUNCTION UPPER-CASE have to respect locale
characters like the french '����' or the german ���?

IBM COBOL for OS/390 & VM 2.1.1 leaves them 'asis' which is not at all
correct.

Daniel

------------------------------------------------------------------------
visit us at http://www.winterthur.com

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ffk79$9f3@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd087$37i@sjx-ixn6.ix.netcom.com> <7ffj1a$f0a$1@nnrp1.dejanews.com>`

```
The current ('85 with '89 Intrinsic Function) Standard thinks that only
"un-accented" characters are alphabetic.  Therefore, UPPER-CASE and similar
functions will NOT work (or may not work - depending on the implementation
extensions) correctly.  The draft of the next Standard *does* add support
for "locales" - which includes the ability to work correctly with
accented-characters.

NOTE: For IBM COBOL for OS/390 & VM (mentioned in this note), I am checking
into whether there are already LE routines that will do this.  I think that
CEESTXF may work in this area - but I am not certain.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fgrg8$407@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd087$37i@sjx-ixn6.ix.netcom.com> <7ffj1a$f0a$1@nnrp1.dejanews.com> <7ffk79$9f3@dfw-ixnews4.ix.netcom.com>`

```


> NOTE: For IBM COBOL for OS/390 & VM (mentioned in this note), I am
checking
> into whether there are already LE routines that will do this.  I think
that
> CEESTXF may work in this area - but I am not certain.
>
>

I have checked with my "usually reliable sources" and there is currently no
LE (CEE) callable routine for doing Upper-Case/Lower-Case conversion based
on "locale" (i.e. including European - and other - accented characters).  I
have passed this on to the project leader of the SHARE "COBOL & LE" project
for consideration as a new requirement.  My guess is that this is something
that would get a BETTER reply if submitted by the European GUIDE or SHARE
groups - but I will see if it can also be progressed in the US.  If any
reader of this NG is active in the European group, please let me know
(private email is OK) and we can see if this can get progressed.

As stated earlier, the NEXT Standard will include support for this - but the
most optimistic estimate is that it will be come official in 2002 - and when
(if?) IBM would/will ever implement it is another question.

P.S. I think that the CEESTXF callable service IS usable for determining if
an upper-case and lower-case letter ARE equivalent (even with accents) - but
it can't be used to do the actual conversion.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 5)_

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fhdlr$3ud$1@nnrp1.dejanews.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd087$37i@sjx-ixn6.ix.netcom.com> <7ffj1a$f0a$1@nnrp1.dejanews.com> <7ffk79$9f3@dfw-ixnews4.ix.netcom.com> <7fgrg8$407@dfw-ixnews4.ix.netcom.com>`

```
In article <7fgrg8$407@dfw-ixnews4.ix.netcom.com>,
  "William M. Klein" <wmklein at ix dot netcom dot com> wrote:

> I have checked with my "usually reliable sources" and there is currently no
> LE (CEE) callable routine for doing Upper-Case/Lower-Case conversion based
…[6 more quoted lines elided]…
> (private email is OK) and we can see if this can get progressed.

At COBOL working group of the german GSE (GUIDE SHARE EUROPE) last november,
this requirement was passed. If it could be progressed in US and/or other
european countries, IBM would certainly be more positive about that. The
actual answer from IBM to this requirement is <NONE> (requirement number
DACOBD98001).

Daniel

------------------------------------------------------------------------
visit us at http://www.winterthur.com

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: string mixed to string in CAPITALS

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fd809$i66$1@news.igs.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es>`

```
inspect stringname converting "abcdefghijklmnopqrstuvwxyz" to
"ABCDEFGHIJKLMNOPQRSTUVWXYZ".

Alberto Santamaria Garcia wrote in message
<7fcs5t$jj39@eui1nw.euskaltel.es>...
>HOW CAN I CONVERT ANY STRING IN COBOL TO A STRING WITH ONLY CAPITALS
>CHARACTERS?
>
>
```

##### ↳ ↳ Re: string mixed to string in CAPITALS

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IyJS2.686$km2.205729@news2.mia>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net>`

```
Donald Tees wrote:
>
>Alberto Santamaria Garcia wrote:
…[5 more quoted lines elided]…
>"ABCDEFGHIJKLMNOPQRSTUVWXYZ".

The advantage of Donald's method is that it also works in COBOL 74 as
well as the current draft standard (at least the last draft I saw :).
Some of my clients still use COBOL 74, and I must write a lot of code
which works across versions.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371B6EAC.AE4BA05B@NOSPAMhome.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia>`

```
> >inspect stringname converting "abcdefghijklmnopqrstuvwxyz" to
> >"ABCDEFGHIJKLMNOPQRSTUVWXYZ".
…[4 more quoted lines elided]…
> which works across versions.

On the other hand, it doesn't work with ANSI 68, where EXAMINE works. 
TRANSFORM works for both, but doesn't work for modern COBOLs, but
upper_case works.  It appears that nothing works for all COBOLs.   I
have no idea why syntax has been futzed around so much.  What was wrong
with EXAMINE and TRANSFORM?  I'm guessing they were extensions which
lost.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 4)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371CCE2F.5ABC@compaq.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <371B6EAC.AE4BA05B@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> > >inspect stringname converting "abcdefghijklmnopqrstuvwxyz" to
…[3 more quoted lines elided]…
> > well as the current draft standard (at least the last draft I saw :).

No it does not.  It works in COBOL 85, not COBOL 74.  See below.

> > Some of my clients still use COBOL 74, and I must write a lot of code
> > which works across versions.
…[6 more quoted lines elided]…
> lost.

EXAMINE (which was in the '68 standard) was replaced by INSPECT in the 
'74 standard.  EXAMINE was too limited and rather than changing the 
syntax of EXAMINE it was decided to replace the statement entirely.  I 
wasn't part of this, but I think it was felt that replacing the 
statement worked better.  Implementors could keep EXAMINE as an 
extension (which almost all of them did) until it faded away.

INSPECT in the '74 standard did not have a CONVERTING option.  That 
was added to the '85 standard.  Primarily because of the IBM 
extension, TRANSFORM.  It was decided that rather than adding a new 
statement we could easily change one that was already in the standard 
that does that kind of thing anyhow.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fg65u$gb8$1@news.igs.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia>`

```
Interestingly enough, it should also be able to take care of weird character
sets ...

Judson McClendon wrote in message ...
>Donald Tees wrote:
>>
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fg7p4$fuc$1@news.cerf.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net>`

```
Donald Tees wrote in message <7fg65u$gb8$1@news.igs.net>...
>Interestingly enough, it should also be able to take care of weird
character
>sets ...

And what is weird? Non english?

Cheesle
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fgrtm$4c9@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net>`

```
I wouldn't use "weird" - but I would say that if a character is not in the
ISO 646 "portable" character set (and notice this is an ISO Standard, not an
ANSI one) - then the character is at least "non-universal in Roman scripts".

FYI - (Plug for next Standard)
   The advantage of using the enhancements in the next Standard over using
the INSPECT verb is that you need not "hard code" the conversion at compile
time.  Instead, you (the COBOL run-time) automatically gets these
equivalency values at run-time.  This is particularly important for cases
where one "language" uses one set of values as valid lower-cases for a
specific upper-case graphic - and another language uses another set of
value.  It is also nice in that the exact same "object code" can run in
France with one (locale-based) result, in Germany with another, and Sweden
with still another.

FINALLY,  you might want to check with your specific vendor to see if they
already provide a facility for doing this.  (I have checked and IBM COBOL
for OS/390 & VM does *not* support this - but I think that Micro Focus'
"NLS" support might provide this already.)
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aBOS2.269$_N.107537@news3.mia>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net>`

```
Cheesle wrote:
>Donald Tees wrote:
>>Interestingly enough, it should also be able to take care of weird
>>character sets ...
>
>And what is weird? Non english?

Your chip is showing again. ;-)  Should we take offense that you did
not capitalize 'English'?  Loosen up a little, okay? :-)
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 6)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fi4tq$b9o$1@news.cerf.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia>`

```
Judson McClendon wrote in message ...
>Should we take offense that you did not capitalize 'English'?

You got me there :-)

>Loosen up a little, okay? :-)

I would be happy to, but you in the US have no idea of how much trouble you
have caused us by not paying attention to the rest of the world in this
matter. I must however admit the support has improved significantly the
latter years.

It is anyway of great concern to me that American software companies does
not keep this in mind, there was a particular reason that I questioned
Donald on this, as his suggestion, although elegant fails for any other
language. This, while there indeed are solutions that open up for language
independence, like INSPECT REPLACING.

Cheesle
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_u8T2.1207$oH.399439@news3.mia>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net>`

```
Cheesle wrote:
>Judson McClendon wrote:
>>Should we take offense that you did not capitalize 'English'?
…[7 more quoted lines elided]…
>this matter.

I'm sure you are correct.  On the other hand, Americans get tired of
being whacked on by people, especially when they do it using technology
we created, often with funds we gave them, okay. :-)  Such is life, we
are all most interested in our own backyards.  We Americans don't sit
around and plot how we can offend the rest of the world. ;-)  We, just
like you, are simply tending to our own interests.  After all, if it
were not for the huge American market, would companies in other countries
be concerned about American interests?  Of course not, they are looking
after their own interests too.  The United States has been blessed in
many ways, and currently has enormous worldwide influence because of it.
It wasn't always this way, and surely won't always be this way.  It is
human nature that this affects how U.S. companies and citizens view their
country, the world, and themselves, and how others view us.  So would it
affect your country or any other.  We are all human here.  But there is
nothing malevolent in it on our part.  How many countries can you name,
other than your own, that you would sleep better if the U.S. was gone and
they assumed the position that the U.S. has now?  If your country had a
terrible natural disaster or was attacked by somebody, from where would
you most expect help to come?  We're not the 'bad guys', just give us a
break, okay? :-)
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 8)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fkres$et5$1@news.cerf.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia>`

```
Judson McClendon wrote in message <_u8T2.1207$oH.399439@news3.mia>...
>I'm sure you are correct.  On the other hand, Americans get tired of
>...

Generally speaking; well said. You made good points and I have to agree,
except for:

>How many countries can you name, other than your own, that you would sleep
better if the U.S. was >gone and they assumed the position that the U.S. has
now?

I think I have most Norwegian with me in saying that we sleep pretty well
the way US is today. Both countries are a part of the western culture and
are politically the same. There certainly are other countries that would
want US down and away, but for Norway? No way.

>If your country had a terrible natural disaster

I would be surprised if we were to get any help at all. Being one of the
richest countries in the world (way more rich pr. man than the US) we would
fix a natural disaster on our own.\

>was attacked by somebody, from where would you most expect help to come?

England, France, Germany, US and others. That's why we're a part of NATO.

>We're not the 'bad guys', just give us a break, okay? :-)

Nor did I say you were, calm down. As I have stated before english is not my
native tongue, hence my speeches may become more offending than expected,
for that case I apologize. It may not have been clear but I targeted the
American Standard committee and in particular IBM. Although both are from
the US and have a lot of influence I was not targeting US. What's most
important; There was made a mistake once, and I just want that i won't
happen again.

BTW: Regarding technological inventions, did you know that the very first
Object Oriented programming language was from Norway (Simula), that the
research around that was the basics that made Xerox' do what later on became
Apple Lisa? In these days of war, it may make sense to mention that the hand
granate also were invented by a Norwegian :-)

Hm, this is way of the subject of this NG :-)

Have a sunny day!

Cheesle
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371E09D2.21CF488C@NOSPAMhome.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net>`

```
> BTW: Regarding technological inventions, did you know that the very first
> Object Oriented programming language was from Norway (Simula), that the
…[8 more quoted lines elided]…
> Cheesle

Yes.  And it wasn't developed because of some style or theory about
objects, it was developed because it fit the needs of the application.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 10)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fl7fh$ive$1@news.cerf.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com>`

```
Howard Brazee wrote in message <371E09D2.21CF488C@NOSPAMhome.com>...
>Yes.  And it wasn't developed because of some style or theory about
>objects, it was developed because it fit the needs of the application.

If you are referring to Simula, I have to disagree, it was developed because
of a theory that human should program the way the think, given that
procedural top-down were inhuman. Simula were not targeting a particular
application niche. So... I for one would call it a theory, however I may be
the only one.

Cheesle
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 11)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371e3eef.30849606@news.enter.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.no> wrote:

>Howard Brazee wrote in message <371E09D2.21CF488C@NOSPAMhome.com>...
>>Yes.  And it wasn't developed because of some style or theory about
…[10 more quoted lines elided]…
>

Cheesle:

I'm not sure if I agree 100%.  I think that human thought can and does
occur in many different forms, depending upon the specific
circumstances.  I also believe that humans generally adapt their
thinking to the specific circumstance at hand.

I believe that the way a soldier thinks under fire (reactionary) is a
much different thought process than when a person is following
directions to a strange new place (very procedural..ergo "top down").

There are many differences in the two scenarios.  I consider the
soldier to be thinking in more of an "event" type mode...in other
words, he doesn't really know what will happen next, so whatever
happens next, he will react to that specific event.

But the person following directions is thinking in more of a
procedural approach.

1.  Go down this road first.
2.  Turn left at second stop light.
3.  etc.

Just my opinion.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 12)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7flkm0$nhq$1@news.cerf.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net> <371e3eef.30849606@news.enter.net>`

```
Bob Wolfe wrote in message <371e3eef.30849606@news.enter.net>...
>But the person following directions is thinking in more of a
>procedural approach.
…[3 more quoted lines elided]…
>3.  etc.

Guess you are right, depends on the environment. On the other side, what if
there suddenly came a truck in 80 miles an hour to the right of the person
:-)

Just kidding!

Cheesle
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 13)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371f8171.27371420@news.enter.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net> <371e3eef.30849606@news.enter.net> <7flkm0$nhq$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.no> wrote:

>Bob Wolfe wrote in message <371e3eef.30849606@news.enter.net>...
>>But the person following directions is thinking in more of a
…[14 more quoted lines elided]…
>

Cheesle:

If that happened, then they would have to go into "mixed thought"
mode...procedural for the directions and event driven to avoid the
speeding truck!!

Kind of like writing a COBOL application with a Visual Basic front
end!

;-)


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 14)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fsg9e$m8b$1@news.igs.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net> <371e3eef.30849606@news.enter.net> <7flkm0$nhq$1@news.cerf.net> <371f8171.27371420@news.enter.net>`

```

Bob Wolfe wrote in message <371f8171.27371420@news.enter.net>...
>"Cheesle" <cheesle@online.no> wrote:
>
…[8 more quoted lines elided]…
>>Guess you are right, depends on the environment. On the other side, what
if
>>there suddenly came a truck in 80 miles an hour to the right of the person
>>:-)
…[15 more quoted lines elided]…
>

Don't know about you Bob, but when I have a truck headed for me,
I do not use a Basic routine to get out of the way.  For that case, I
have a high speed assembler routine triggered at the interrupt level.
;<0
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 15)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AHlU2.9505$L61.3053105@news1.mia>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net> <371e3eef.30849606@news.enter.net> <7flkm0$nhq$1@news.cerf.net> <371f8171.27371420@news.enter.net> <7fsg9e$m8b$1@news.igs.net>`

```
Donald Tees wrote:
>
>Don't know about you Bob, but when I have a truck headed for me,
>I do not use a Basic routine to get out of the way.  For that case, I
>have a high speed assembler routine triggered at the interrupt level.
>;<0

Actually, I think many of those reactions are hard-wired, and work
before the interrupt gets to the CPU. ;-)
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 16)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ftpag$fdp$1@news.igs.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net> <371e3eef.30849606@news.enter.net> <7flkm0$nhq$1@news.cerf.net> <371f8171.27371420@news.enter.net> <7fsg9e$m8b$1@news.igs.net> <AHlU2.9505$L61.3053105@news1.mia>`

```
Naw.  Small kids have to be taught to get out of the way of cars.
BTW, that is a clear cut case where a jump instruction warranted.
Programming it so that you immediately returned to the same spot
would be embarrassing.  Might even cause a crash.  ;<)

Judson McClendon wrote in message ...
>Donald Tees wrote:
>>
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 15)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37231a56.616967@news3.ibm.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net> <371e3eef.30849606@news.enter.net> <7flkm0$nhq$1@news.cerf.net> <371f8171.27371420@news.enter.net> <7fsg9e$m8b$1@news.igs.net>`

```
On Sat, 24 Apr 1999 09:20:28 -0400, "Donald Tees" <donald@willmack.com> wrote:


>
>Don't know about you Bob, but when I have a truck headed for me,
…[4 more quoted lines elided]…
>
I hope it is a not maskable interruot, and also that you are enabled for interrupts....
with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 16)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ftpm4$fo4$1@news.igs.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net> <371e3eef.30849606@news.enter.net> <7flkm0$nhq$1@news.cerf.net> <371f8171.27371420@news.enter.net> <7fsg9e$m8b$1@news.igs.net> <37231a56.616967@news3.ibm.net>`

```

Volker Bandke wrote in message <37231a56.616967@news3.ibm.net>...
>On Sat, 24 Apr 1999 09:20:28 -0400, "Donald Tees" <donald@willmack.com>
wrote:
>>
>I hope it is a not maskable interrupt, and also that you are enabled for
interrupts....


Yes.  And level triggered.  Push, JMP(now).
;<)
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 15)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372468d7.4553839@news.enter.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <aBOS2.269$_N.107537@news3.mia> <7fi4tq$b9o$1@news.cerf.net> <_u8T2.1207$oH.399439@news3.mia> <7fkres$et5$1@news.cerf.net> <371E09D2.21CF488C@NOSPAMhome.com> <7fl7fh$ive$1@news.cerf.net> <371e3eef.30849606@news.enter.net> <7flkm0$nhq$1@news.cerf.net> <371f8171.27371420@news.enter.net> <7fsg9e$m8b$1@news.igs.net>`

```
"Donald Tees" <donald@willmack.com> wrote:

[snip]
>Don't know about you Bob, but when I have a truck headed for me,
>I do not use a Basic routine to get out of the way.  For that case, I
>have a high speed assembler routine triggered at the interrupt level.
>;<0

Donald:

You're absolutely correct...the last thing that I would want to have
happen as the image of the truck hits my retina is to receive an error
message like:

VBRUN300.DLL NOT FOUND - LEAP_OUT_OF_WAY PROGRAM TERMINATED

;-)


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fgnit$qv7$1@news.igs.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net>`

```
I consider weird to be any language where upper and lower case do not match,
such as Russian.  At least that is the sort of situation I was referring to.

Cheesle wrote in message <7fg7p4$fuc$1@news.cerf.net>...
>Donald Tees wrote in message <7fg65u$gb8$1@news.igs.net>...
>>Interestingly enough, it should also be able to take care of weird
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 6)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fi5uo$bkv$1@news.cerf.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <7fgnit$qv7$1@news.igs.net>`

```
Donald Tees wrote in message <7fgnit$qv7$1@news.igs.net>...
>I consider weird to be any language where upper and lower case do not
match,
>such as Russian.  At least that is the sort of situation I was referring
to.

Then it is time for school :-)

Example:
Norwegian has three special letters, which in the early days where not found
to have demand enough to be offered a place in the sunshine of the American
Standard comitee. Which indeed makes sense, as long as there is just above 4
million of us in the world. The fact that the ignorant attitude of the
American Standard comitee also affected millions of French, German,
Portugeese, Spanish and many more is another story.

What Norwegian developers had to do, to fit their special letters into the
127 available characters was to replace other, indeed useful characters.
Thus, [\] and {|} became the special ��� and ��� (I hope you are able to
read them).
Fair enough as long as one was inside Norway. But, you may imagine how many
hilarious experiences you get, when the system switch (\ for windows/dos) is
used.

Though, IBM knew their responsibility, being an international corporation
they set up an extended ASCII set in order to make a solution to this. Which
would have been great, if it wasn't for the bad work they performed. If you
look once more at the special characters, you notice they are represented in
both lowercase and uppercase. As we all know, uppercase letters are supposed
to be sorted before lowercase letters, not so with IBM extended, in their
lack of knowledge, they placed the letters quite random, thus causing a
simple sorting by value impossible to perform. Unfortunately, this became a
standard.

As for EBCDIC I don't know, I am not familiar with that set.

Luckily, though I may say a lot of bad things about Microsoft, character
sets is something they have done proper. Although the letters are put in
randomly, they are in correct order, such that upper case will sort before
lowercase in sense of values.

You may say that it is not the business of US software developers to pay
attention to this subject, I cannot argue with you on that. What I would
make a point of here, is that the weird positioning of letters in the ASCII,
IBM charactersets are done by US developers /commitees. Not by the affected
countries themself.

Finally, it is not my intention to start a war here, if anything is to be
considered offending of what I have written it is due to the fact that
english is not my native tongue. I just wanted to attempt to describe what a
problem this really is.

Cheesle
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371CD2D9.AC1D90BA@NOSPAMhome.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <7fgnit$qv7$1@news.igs.net> <7fi5uo$bkv$1@news.cerf.net>`

```
> Luckily, though I may say a lot of bad things about Microsoft, character
> sets is something they have done proper. Although the letters are put in
> randomly, they are in correct order, such that upper case will sort before
> lowercase in sense of values.

Is there any historical reason for upper case going before lower case? 
Or where non-alphabetic characters should sort?  Or how accented
characters should sort?  

I certainly don't think users would think the following are in order:

Abc
CBA
abc

In real life every variation of A should go before any variation of B. 
Check your dictionary - it doesn't have all capitalized words before all
lower case words.

Let's say we are using Unicode and have five different symbols which can
be placed over the letter "e".  How do we sort the data using COBOL so
that they appear in the correct order to users?  We probably have to
train them to our way of handling non-alpha characters, but we should
adjust to their existing concepts of alpha.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 8)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fimt9$ljb$1@news.cerf.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <7fgnit$qv7$1@news.igs.net> <7fi5uo$bkv$1@news.cerf.net> <371CD2D9.AC1D90BA@NOSPAMhome.com>`

```
Howard Brazee wrote in message <371CD2D9.AC1D90BA@NOSPAMhome.com>...
>Is there any historical reason for upper case going before lower case?

Good question! I don't know, may be just a coincident?

>In real life every variation of A should go before any variation of B.
>Check your dictionary - it doesn't have all capitalized words before all
>lower case words.

Agree.

>Let's say we are using Unicode and have five different symbols which can
>be placed over the letter "e".  How do we sort the data using COBOL so
>that they appear in the correct order to users?  We probably have to
>train them to our way of handling non-alpha characters, but we should
>adjust to their existing concepts of alpha.

Well, if on Windows, there are API functions that are locale sensitive which
will fix that.

Cheesle
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fj1qg$qc0@sjx-ixn5.ix.netcom.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <7fgnit$qv7$1@news.igs.net> <7fi5uo$bkv$1@news.cerf.net> <371CD2D9.AC1D90BA@NOSPAMhome.com>`

```
Interesting to read this note today.  I was just reading some comments on
the proposed (looks like it needs more work) ISO Standard on character
ordering.  The entire document that I was reading was too LONG to post here,
but I thought you might want to read a section on sorting upper-/lower-case,
(If you are interested in the WHOLE thing - contact your national body
organization for ISO and ask for information on,
 "FCD 14651 - Method for Comparing Character Strings and Description of a
Common Tailorable Ordering Template"

Interesting quote (semi-long) follows,

"> 3. The third decomposition breaks ties for quasi-homographs different
> only because upper-case and lower-case characters are used. This time,
> the tradition is well established in English and German dictionaries,
…[41 more quoted lines elided]…
> along with the actual syntax for ordering caps before smalls. "
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371DD59F.89D172DE@NOSPAMhome.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <7fgnit$qv7$1@news.igs.net> <7fi5uo$bkv$1@news.cerf.net> <371CD2D9.AC1D90BA@NOSPAMhome.com> <7fj1qg$qc0@sjx-ixn5.ix.netcom.com>`

```
> > August (month)  May (month)
> > august (venerable)      may (be able)
…[3 more quoted lines elided]…
> > mass (heap)

So how do the following sort out in various countries and character
codes?

Cï¿½op
Coop
coop
Coï¿½p
coï¿½p
Coo2
[oop
$oop
Doop
Boop

How would users want them to sort?
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 9)_

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371e8597.3479388@netnews>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <7fgnit$qv7$1@news.igs.net> <7fi5uo$bkv$1@news.cerf.net> <371CD2D9.AC1D90BA@NOSPAMhome.com> <7fj1qg$qc0@sjx-ixn5.ix.netcom.com>`

```
'Twas Tue, 20 Apr 1999 18:13:42 -0500, when "William M. Klein"
<wmklein@nospam.netcom.com> illuminated comp.lang.cobol thusly:

>> This time,
>> the tradition is well established in English and German dictionaries,
>> where lower case always precedes upper case in homographs, 

>> This is, as we have said many times to SC22/WG20, incorrect. Lower case
>> does not precede upper case in English. The concise Oxford dictionary of
…[9 more quoted lines elided]…
>> mass (heap)

FYI, The American Heritage Desk Dictionary (c) 1981 (the only dictionary I
have at hand) lists lower case before capitals.  I know of no official
standard.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fimut$9q6$1@news.igs.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <7fgnit$qv7$1@news.igs.net> <7fi5uo$bkv$1@news.cerf.net>`

```
Cheesle wrote in message
<large snippage>

>You may say that it is not the business of US software developers to pay
>attention to this subject, I cannot argue with you on that. What I would
>make a point of here, is that the weird positioning of letters in the
ASCII,
>IBM charactersets are done by US developers /commitees. Not by the affected
>countries themself.


(I am not in the U.S., BTW)  I chose the wrong adjective in using "weird",
as it could be contrued offensive.  I am sorry, as that was not my intent.
The real point of the message is that the inspect translating method can be
used with any character set, not just the English one.  Theoretically, the
upper case function should be smart enough to handle all of the character
sets available, but I doubt that they do.
>
>Finally, it is not my intention to start a war here, if anything is to be
>considered offending of what I have written it is due to the fact that
>english is not my native tongue. I just wanted to attempt to describe what
a
>problem this really is.


I have been aware of the problem for quite some time, as I also have
programmed in French. My other languages (Hebrew, Latin and Greek), I have
never written code for.  In fact, I don't think I've even read anything in
any of them that was written after about the year 300. ;<)  I am glad of
that, as handling *those* character sets ... I would not know where to
start. I think Hebrew would be the worst ... I've noticed one poster in here
from Israel, how do you handle points?

Certainly, I never took offense at your post ... I wasn't sure if you were
annoyed or not, so I just answered it factually.
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

_(reply depth: 8)_

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fks29$f66$1@news.cerf.net>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es> <7fd809$i66$1@news.igs.net> <IyJS2.686$km2.205729@news2.mia> <7fg65u$gb8$1@news.igs.net> <7fg7p4$fuc$1@news.cerf.net> <7fgnit$qv7$1@news.igs.net> <7fi5uo$bkv$1@news.cerf.net> <7fimut$9q6$1@news.igs.net>`

```
Donald Tees wrote in message <7fimut$9q6$1@news.igs.net>...
>Theoretically, the upper case function should be smart enough to handle all
of the character
>sets available, but I doubt that they do.

Upper/Lower is a difficult task indeed. In my opinion it should be a
function of the host (OS) not of the language itself, both because of its
complex nature but also because it would ensure strings equal between
applications developed in the different languages.

I prefer the INSPECT REPLACING statement as it is very dynamic, may be too
dynamic. Your suggestion of adding 0x20 although very common is strictly
limited to the ASCII.

>Certainly, I never took offense at your post ...

I pleased to hear that.

>I wasn't sure if you were annoyed or not

A little bit may be :-) But more as a result of dealing with the sorting
throughout the years than your statement in particular.

Have a sunny day!

Cheesle
```

##### ↳ ↳ Re: string mixed to string in CAPITALS

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990419085745.20551.00004049@ng-fi1.aol.com>`
- **References:** `<7fd809$i66$1@news.igs.net>`

```
take hex value and add 020h?
```

###### ↳ ↳ ↳ Re: string mixed to string in CAPITALS

- **From:** "Cheesle" <cheesle@online.no>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ffi53$7gr$1@news.cerf.net>`
- **References:** `<7fd809$i66$1@news.igs.net> <19990419085745.20551.00004049@ng-fi1.aol.com>`

```
Twymer wrote in message <19990419085745.20551.00004049@ng-fi1.aol.com>...
>take hex value and add 020h?

That's cool as long as you are american, australian or english. Check out
another country and you're out of luck.

Cheesle
```

#### ↳ Re: string mixed to string in CAPITALS

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371B345A.340E4B75@NOSPAMhome.com>`
- **References:** `<7fcs5t$jj39@eui1nw.euskaltel.es>`

```
Alberto Santamaria Garcia wrote:
> 
> HOW CAN I CONVERT ANY STRING IN COBOL TO A STRING WITH ONLY CAPITALS
> CHARACTERS?


With a modern compiler use the UPPER-CASE function.  With older
compilers, the INSPECT, EXAMINE, or TRANSFORM verbs can be used.

BTW, newsgroups work better with mixed case.  Upper case is yelling, or
in this NG, is used to indicate COBOL code (as in my example above).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
