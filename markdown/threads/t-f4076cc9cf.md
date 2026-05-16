[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Any Suggestions? (Extreme Programming)

_26 messages · 11 participants · 1999-12_

---

### Re: Any Suggestions? (Extreme Programming)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <3842BDE8.942020E7@NOSPAMhome.com> <822ah5$1gc$1@nntp5.atl.mindspring.net> <3ex14.6774$Ic5.79616@news3.mia> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia>`

```
Judson McClendon wrote in message ...
> [among much else...]
>One of the things in C/C++ and many other languages that contribute most
>to broken code and horrible debugging problems is the use of pointers.


When I first read your message, I realized I had entered the realm of one of
my hot buttons and decided to let that button cool down for a few days
before responding.

And a good thing I did.

As subsequent posters have stated, "pointers" and "dynamic memory
allocation" are not, of and by themselves, problems; rather, it is the
improper or sloppy use of these tools which cause problems - regardless of
language platform (C/C++ mentioned as an example). My real point is, to
paraphrase Churchill's requests to the US for military aid at the onset of
the Second World War, is, "Give us the tools and we'll finish the job."

I just don't see any problem ADDING capabilities to a programming language;
I consider it highly unlikely dynamic allocation or enhanced pointer usage
would supplant 'traditional' COBOL programming techniques. But for those
tough lies behind a tree, it would be nice to have in the bag a tree-iron
and not be forced to use a three-iron.

Michael Mattias
Racine WI USA
```

#### ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nT874.11689$DC6.169673@news2.mia>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <822ah5$1gc$1@nntp5.atl.mindspring.net> <3ex14.6774$Ic5.79616@news3.mia> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
>Judson McClendon wrote:
>> [among much else...]
…[8 more quoted lines elided]…
>the Second World War, is, "Give us the tools and we'll finish the job."


Okay, are you saying then that C/C++ programs are much more 'bug prone'
and difficult to debug because C/C++ programmers are less capable?  If
you are, quickly put on your asbestos pants. ;-)  But the disparity does
exist.  Since both C/C++ and COBOL programs are frequently written in
the same environments, that disparity is caused by either the C/C++
language being more bug prone, or C/C++ programmers being more bug
prone, or both.  Take your pick, I won't argue with either. ;-)

The fact is that you are *partially* correct in your reasoning.  What
you are not taking into account is that not every feature that can be
implemented in a language is equally easy to learn and use correctly.
You can not claim, for example, that C/C++ programmers never make the
mistake of typing or reading '=' for '==', and vice-versa.  This
confusion simply does not exist in COBOL, because any place you can
use '=', a '==' would be a syntax error, and vice versa.  Two of the
subtlest, arcane and difficult to master features of C are pointers,
indirection, and all the subtle variations of their possible uses.
Anyone who says they mastered this with no difficulty, that they do
not make errors using it, is not being honest.  Up to now COBOL has
avoided this completely.  Adding these features will provide similar
opportunities in COBOL, and it is not logically defensible to insist
otherwise.  The question is not 'if it will', but 'is it worth it'.
This is a matter of opinion, but considering where COBOL works best,
I don't think so.  Leave those features to languages frequently used
for tasks for which they are necessary.  A Big Mistake for any tool
is to try and make it a 'be-all, end-all' solution for every problem.
A frequent error being made these days is 'over enhancement'.  It
only complicates use of the tool and makes it less convenient and
reliable for tasks it is best suited for.  Since COBOL is the very
best, most economical and reliable tool we have for core business
applications, why compromise COBOL's strengths by adding bug-prone,
little needed features, when there are other languages available for
the tasks that need them?  My $.02. :-)
```

##### ↳ ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83jfca$g16$1@nntp2.atl.mindspring.net>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <3ex14.6774$Ic5.79616@news3.mia> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia>`

```
<snippage of much PROs and CONs on POINTERS and DYNAMIC MEMORY allocation>

Judson,
  Are you aware that many (most?) COBOL's that I know of have supported USAGE
POINTER for over 10 years now - and some are close to that on USAGE
PROCEDURE-POINTER.  Add to that the fact that CICS (with COBOL on IBM
mainframes) has required you to use POINTERS (previously BLL-cells, but that
is what they really were) since LONG before that?

Yes, some of those programs have bugs - but I don't think any more or less
than "similar" applications written using other techniques. Personally, I
would guess that there are more errors (at least in the development stage)
using COBOL STRING, UNSTRING, and INSPECT than there are with USAGE POINTER,
SET ADDRESS OF, EXEC CICS GETMAIN, etc.

I think that the bottom-line is that "more complex" language features require
better training, more testing, and maintenance by those who UNDERSTAND the
same features as those who coded them in the first place.

Personally, I am HAPPY that these are being added to the Standard so that
"portable" coding techniques can be used - thereby INCREASING the chance of
proper maintenance.  I also, just don't see how anyone can want COBOL be
"eliminated" as a viable language in today's world of multi-language APIs -
which all (or almost all) seem to assume that your programming language has
these features.
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OsLgtSxS$GA.222@cpmsnbbsa02>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:83jfca$g16$1@nntp2.atl.mindspring.net...
> <snippage of much PROs and CONs on POINTERS and DYNAMIC MEMORY allocation>

<snip>

I can see both sides of the story as having valid points here (a:add
pointers and dynamic memory allocation; b:don't add them).  It seems, on the
face of it, that both sides are right.


Sincerely,
      Chris Osborne
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FBx74.847$Fc6.8352@news4.mia>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net>`

```
William M. Klein wrote:
>Judson,
>  Are you aware that many (most?) COBOL's that I know of have supported
>USAGE POINTER for over 10 years now ...?


Yes, mainly from posts in this newsgroup.  But I have little information
on how wide the usage is, or how successful.

>Yes, some of those programs have bugs - but I don't think any more or less
>than "similar" applications written using other techniques. Personally, I
>would guess that there are more errors (at least in the development stage)
>using COBOL STRING, UNSTRING, and INSPECT than there are with USAGE POINTER,
>SET ADDRESS OF, EXEC CICS GETMAIN, etc.


Without actual data, that is hard to determine.  I suggest that the
manner of implementation (syntax and semantics) has a great deal to
do with the difficulty.

>I think that the bottom-line is that "more complex" language features require
>better training, more testing, and maintenance by those who UNDERSTAND the
>same features as those who coded them in the first place.


Bill, it is a well established and easily demonstrated fact that the
more complex the operation, the more likely an error, other factors
being equal.  We humans are simply built that way.  In fact, even a
machine is more likely to make an error on a long operation than a
short one.  That same better training and testing would provide
similar improvements in quality without the extra features.  All the
training would cost a great deal of money and time.  If that extra
cost is necessary to achieve parity in quality with current (COBOL 85)
methods, then that is a liability.  You and I come down on different
sides because we view the issue with different perspectives on the
benefits vs costs. :-)
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RbB74.2227$i05.31993@dfiatx1-snr1.gtei.net>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia>`

```
Judson McClendon wrote in message ...
>
>...the more complex the operation, the more likely an error, other factors
>being equal.  We humans are simply built that way.

Well, if you had migrated here from the planet Krypton, as did I, ....

MCM
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385f0501.84403950@news1.attglobal.net>`
- **References:** `<826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia>`

```
On Mon, 20 Dec 1999 15:55:48 -0600, "Judson McClendon"
<judmc@bellsouth.net> wrote:

>William M. Klein wrote:
>>Judson,
…[6 more quoted lines elided]…
>

I have only used it for interfacing with C routines, or the Windows
API.  
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 5)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf4cb5$2e08e670$0100007f@vaagshaugen>`
- **References:** `<826dpi$fpk$1@nntp3.atl.mindspring.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net>`

```
Thane Hubbell <thaneH@softwaresimple.com> wrote in article
<385f0501.84403950@news1.attglobal.net>...
> On Mon, 20 Dec 1999 15:55:48 -0600, "Judson McClendon"
> <judmc@bellsouth.net> wrote:
…[12 more quoted lines elided]…
> API.  

CICS programmers have been using pointers for a long time.  Though it were
only called BLL cells before, and were moved around in PIC 9(8) COMP
fields.  You had to remember to use SERVICE RELOAD before referencing the
structure again.  To the traditional batch programmer it was a mystery, to
those with assembler (or PL/I, or C) background it was a piece of cake.  VS
COBOL II was a relief.

Gunnar.
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38622de8.291514320@news.freewwweb.com>`
- **References:** `<826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen>`

```
On 22 Dec 1999 20:16:09 GMT, "Gunnar Opheim" <gunnar.opheim@eunet.no>
wrote:

>Thane Hubbell <thaneH@softwaresimple.com> wrote in article
><385f0501.84403950@news1.attglobal.net>...
…[23 more quoted lines elided]…
>Gunnar.

Maybe I am the exception - I am a CICS programmer, and I have never
had occasion (in 15 years) to use BLL cells.  I started on 1.5 and
have worked through 4.1.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83ton4$pgf$1@nntp8.atl.mindspring.net>`
- **References:** `<826slb$peq$1@aklobs.kc.net.nz> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com>`

```
Thane Hubbell <thaneH@softwaresimple.com> wrote in message
  <snip>
> >
> >CICS programmers have been using pointers for a long time.  Though it were
…[3 more quoted lines elided]…
> >those with assembler (or PL/I, or C) background it was a piece of cake.
VS
> >COBOL II was a relief.
> >
…[7 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/

What COBOL product have you used (OS/VS COBOL - or a newer one)?  If it is
anything POST-OS/VS, then you are correct that you haven't used (needed to
use) BLL-cells.  If you ever used OS/VS COBOL and EVER used anything in
LINKAGE SECTION, then you DID use BLL-cells, whether you knew about it or
not.

Of course, if you used CICS on Non-S/370-S/390 environments (OS/2, Windows,
HP, etc) then you wouldn't have used them there either - but MVS (OS/390) and
kVSE did use them.
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 7)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf4da0$f830b130$0100007f@vaagshaugen>`
- **References:** `<826slb$peq$1@aklobs.kc.net.nz> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com>`

```
Thane Hubbell <thaneH@softwaresimple.com> wrote in article
<38622de8.291514320@news.freewwweb.com>...
> Maybe I am the exception - I am a CICS programmer, and I have never
> had occasion (in 15 years) to use BLL cells.  I started on 1.5 and
> have worked through 4.1.

OK, I was referring to CICS on MVS with OS/VS COBOL.  I've been a CICS
systems programmer since CICS/VS was introduced and it was macro-level
those days.  It was no way to avoid the fiddling with BLL cells in COBOL. 
I was not a COBOL programmer, I just supported the guys that had to cope
with it.

I think the way CICS (mis)used the BLL cells in COBOL is an interesting
story.  These are the base locators for the Linkage Section.  Each 01-level
was addressed by a BLL cell (more than one if the structure was more than
4K).  The content was meant to be set at entry to a subroutine and remain
constant until GOBACK.  OS/VS CICS required a first structure that
described the very collection of BLL cells and set the content of this
first BLL, so the program was able to manipulate the BLL cells.  Thus we
got support for dynamic storage.

The code generated by the compiler generally assumed that BLL cell content
was constant.  So to ensure that an updated BLL cell was used when
referencing a Linkage Section structure, you had to code the SERVICE RELOAD
compiler directive.

It is not difficult to understand that this was a mess to a traditional
COBOL batch programmer.  It had to be done in a similar way in assembler,
but this was everyday life to an assembler programmer.  PL/I already had
facilities to support based structures, so the PL/I CICS programs were
cleaner than with COBOL.  C was not supported by CICS in those days.

The introduction of pointers with VS COBOL II changed all this.  COBOL
programs can now be written in PL/I style (though the syntax is different).

Gunnar.
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 1999-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com>`

```
On Thu, 23 Dec 1999 14:24:17 GMT, thaneH@softwaresimple.com (Thane
Hubbell) enlightened us:

>On 22 Dec 1999 20:16:09 GMT, "Gunnar Opheim" <gunnar.opheim@eunet.no>
>wrote:
…[33 more quoted lines elided]…
>My personal web site: http://www.geocities.com/Eureka/2006/

Thane, how is that possible?  In those releases you noted (which I've
also worked with), in order to gain addressability to items in the
Linkage section, you had to do at least one SERVICE RELOAD on entry to
the program.  On top of that, if you read records into an area defined
in the Linkage Section, you had to issue a SERVICE RELOAD to gain
addressability to it.  Just curious.

Happy Holidays.

          ////
         (o o)
-oOO--(_)--OOo-

Two wrongs don't make a right, but two Wrights made an airplane.


Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3862d4a2.334202275@news.freewwweb.com>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net>`

```
On Thu, 23 Dec 1999 11:48:01 -0500, SkippyPB
<swiegand@neo.rr.com.nospam> wrote:

>Thane, how is that possible?  In those releases you noted (which I've
>also worked with), in order to gain addressability to items in the
…[4 more quoted lines elided]…
>

Well - I think I can solve this mystery.  I never have coded a SERVICE
RELOAD.  My 1.5 and 1.6 experience was under Software Pursuits
MVT/VSE, and IBM's DOS/SP 2.1.  My later CICS experience (mostly
maint) is with 3.3 and 4.1 under MVS 5.22 and OS/390. 

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83uqth$ukk$1@nntp5.atl.mindspring.net>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net> <3862d4a2.334202275@news.freewwweb.com>`

```
One issue about "SERVICE RELOAD" and OS/VS COBOL (or DOS/VS COBOL) that may
be missed by some is that IF you used "CAPEX" (later CA-Optimizer), you did
NOT need to code the SERVICE RELOAD statement because that "add-on" to the
IBM compiler handled these linkage pointers "better" than IBM's own compiler.
Other than that, I still can't figure out how Thane avoided them.
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 10)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-12-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3866274f.552008712@news.freewwweb.com>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net> <3862d4a2.334202275@news.freewwweb.com> <83uqth$ukk$1@nntp5.atl.mindspring.net>`

```
On Thu, 23 Dec 1999 21:56:00 -0600, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>One issue about "SERVICE RELOAD" and OS/VS COBOL (or DOS/VS COBOL) that may
>be missed by some is that IF you used "CAPEX" (later CA-Optimizer), you did
…[3 more quoted lines elided]…
>

Well, I can see a couple of ways <G>.  

I rarely used EXEC CICS LINK.  Instead we used XCTL or RETURN with
different transaction ID's.  We made use of the communications section
quite often.  

However, I did have some subroutines executed via EXEC CICS LINK - and
I know I didn't use SERVICE RELOAD.  I think the modified translator
provided by Software Pursuits handled that.  

The DOS/SP 2.1 shop never used EXEC CICS LINK, and in fact never used
RETURN with a transaction ID.  Their code was very simplistic, but
suited their needs.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<845lva$qe3$1@nntp6.atl.mindspring.net>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net> <3862d4a2.334202275@news.freewwweb.com> <83uqth$ukk$1@nntp5.atl.mindspring.net> <3866274f.552008712@news.freewwweb.com>`

```
Somewhere we changed subjects.  I started saying (or meant to say) that I
couldn't believe that you hadn't used BLL-cells.  Others started talking
about the SERVICE RELOAD statement.  If you had any "items" in your linkage
section, then I think you were using BLL-cells -even if you didn't use
SERVICE RELOAD.  This had (has) nothing to do with EXEC CICS LINK
statements - but does happen when you use CICS "locate" rather than "move"
mode.  (I.e. when you use the "name of a bll-cell" in *any* EXEC CICS
statement - rather than the name of a working-storage section.  The were also
used whenever you use EXEC CICS GETMAIN.)
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 12)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-12-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-WdTI3zkJD9pM@localhost>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net> <3862d4a2.334202275@news.freewwweb.com> <83uqth$ukk$1@nntp5.atl.mindspring.net> <3866274f.552008712@news.freewwweb.com> <845lva$qe3$1@nntp6.atl.mindspring.net>`

```
On Sun, 26 Dec 1999 18:10:17, "William M. Klein" 
<wmklein@nospam.netcom.com> wrote:

> Somewhere we changed subjects.  I started saying (or meant to say) that I
> couldn't believe that you hadn't used BLL-cells.  Others started talking
…[7 more quoted lines elided]…
> 

I have avoided GETMAIN like the plague. <G>  Thinking about this 
further, I think I might have had occasion to modify a program that 
used BLL cells, but I never created one.  

Let me give you a little history.  When I started we were using a 
really terrible third party tool called Accolade to create our CICS 
programs.  When moving from 1.5 to 1.6, Accolade would not make the 
transition.  I went to CICS school at IBM so I could port these 
programs.  Based on there extensive use of SWA and TWA, I decided it 
best to just scrap and rewrite them.  We needed some method of 
duplicating the Accolade menus and security features (No RACF with 
MVT/VSE).  I designed and coded a security and menuing system that 
made use of the communications section and XCTL.  In addition, IBM was
hot on the SAA and CUA bandwagon at that time.  I made all the 
applications CUA compliant.  We had some fairly complex applications, 
but none of them were heavy "Transaction serving" systems.  They were 
really interactive file maint systems.  Our user base was around 100 
or so most of the time.  I may have never gotten into the performance 
areas where using memory internally, or sharing memory areas would 
have helped me much.  Looks like I missed out! <G>
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 13)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf510d$cf54f760$0100007f@vaagshaugen>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net> <3862d4a2.334202275@news.freewwweb.com> <83uqth$ukk$1@nntp5.atl.mindspring.net> <3866274f.552008712@news.freewwweb.com> <845lva$qe3$1@nntp6.atl.mindspring.net> <Jl0PnHJ5PvPd-pn2-WdTI3zkJD9pM@localhost>`

```
Thane Hubbell <redsky@ibm.net> wrote in article
<Jl0PnHJ5PvPd-pn2-WdTI3zkJD9pM@localhost>...
> I have avoided GETMAIN like the plague. <G>  Thinking about this 
> further, I think I might have had occasion to modify a program that 
> used BLL cells, but I never created one.  

Disclaimer: I only know Cobol on IBM mainframe.

All Cobol programs that use Linkage Section use BLL cells.  Each 01 level
has a corresponding BLL cell.

The BLL cells are initialized from the parameter list (procedure division
using parm1 parm2 ...) when the program starts.  After that the content of
the BLL cell is not supposed to change in a batch program.  CICS introduced
a new way of using Linkage Section, dynamic storage areas required change
of base locators (BLL).  The point is that the compiled code must recognize
when a BLL has changed, so that it addresses the correct data area.  The
purpose of SERVICE RELOAD is to inform the compiler that it must now reload
the base register from the BLL cell before using it to address data.

This has nothing to do with the operating system (as one other poster
indicated), it is a property of the compiler.  In VS COBOL II, using
pointers and SET ADDRESS statements, this is not an issue; the compiler
will know when to reload base registers.

Maybe I can shed some light on why you didn't have to use SERVICE RELOAD
with OS/VS COBOL (or was it OS COBOL Version 4).  There was a compiler
option for OPTIMIZE.  I think that when not using that compiler option the
compiler would always reload the base registers before using them, so
SERVICE RELOAD was not neccesary.  But this was a long time ago, so I am
not sure.

Gunnar.
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 14)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3868CA5D.F5176BA4@NOSPAMwebaccess.net>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net> <3862d4a2.334202275@news.freewwweb.com> <83uqth$ukk$1@nntp5.atl.mindspring.net> <3866274f.552008712@news.freewwweb.com> <845lva$qe3$1@nntp6.atl.mindspring.net> <Jl0PnHJ5PvPd-pn2-WdTI3zkJD9pM@localhost> <01bf510d$cf54f760$0100007f@vaagshaugen>`

```
Gunnar Opheim wrote:

> Disclaimer: I only know Cobol on IBM mainframe.
> 
> All Cobol programs that use Linkage Section use BLL cells.  Each 01 level
> has a corresponding BLL cell.

I have used COBOL in many environments, but half of my experience has
been with IBM mainframes.  Only a couple of months were CICS.  From your
post, I guess I have been using BLL cells, but outside of this thread I
have never heard of them.  Is there some reason I should have heard of
them?  Should they mean anything for me?
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 15)_

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf518e$6c22d050$0100007f@vaagshaugen>`
- **References:** `<832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net> <3862d4a2.334202275@news.freewwweb.com> <83uqth$ukk$1@nntp5.atl.mindspring.net> <3866274f.552008712@news.freewwweb.com> <845lva$qe3$1@nntp6.atl.mindspring.net> <Jl0PnHJ5PvPd-pn2-WdTI3zkJD9pM@localhost> <01bf510d$cf54f760$0100007f@vaagshaugen> <3868CA5D.F5176BA4@NOSPAMwebaccess.net>`

```
Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in article
<3868CA5D.F5176BA4@NOSPAMwebaccess.net>...
> I have used COBOL in many environments, but half of my experience has
> been with IBM mainframes.  Only a couple of months were CICS.  From your
> post, I guess I have been using BLL cells, but outside of this thread I
> have never heard of them.  Is there some reason I should have heard of
> them?  Should they mean anything for me?

If you were a CICS programmer in the pre-VS COBOL II era: yes, otherwise:
no.   Unless you are involved in tricky debugging.  It is an internal
thing.
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 9)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 1999-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<248FCF01F8E473AF.4333EB6C78D454DF.8EE671F2D085DC90@lp.airnews.net>`
- **References:** `<9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <83jfca$g16$1@nntp2.atl.mindspring.net> <FBx74.847$Fc6.8352@news4.mia> <385f0501.84403950@news1.attglobal.net> <01bf4cb5$2e08e670$0100007f@vaagshaugen> <38622de8.291514320@news.freewwweb.com> <3E8CB67BF5FCBF3E.76466B2A492809DE.E12DAEFB266FFD19@lp.airnews.net> <3862d4a2.334202275@news.freewwweb.com>`

```
On Fri, 24 Dec 1999 02:04:45 GMT, thaneH@softwaresimple.com (Thane
Hubbell) enlightened us:

>On Thu, 23 Dec 1999 11:48:01 -0500, SkippyPB
><swiegand@neo.rr.com.nospam> wrote:
…[16 more quoted lines elided]…
>My personal web site: http://www.geocities.com/Eureka/2006/

That explains it.  I worked with MVT/VSE very briefly in the mid 80's
also and now that I think about it, I do remember that you didn't have
to issue SERVICE RELOAD in CICS programs running under that OS.

Regards and Happy Holidays to all.

          ////
         (o o)
-oOO--(_)--OOo-

Two wrongs don't make a right, but two Wrights made an airplane.


Remove nospam to email me.

 Steve
```

##### ↳ ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2De74.6977$_f.66805@dfiatx1-snr1.gtei.net>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <3ex14.6774$Ic5.79616@news3.mia> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia>`

```
Judson McClendon wrote in message ...
>Michael Mattias wrote:
>>Judson McClendon wrote:
…[3 more quoted lines elided]…
>you are, quickly put on your asbestos pants. ;-)...

No, not at all. Programmers are capable or incapable regardless of race,
creed, color, sex, national origin, Vietnam-era veteran status,
left-handedness, whether or not they are transvestites who have had sex with
their pets OR choice of programming language.

MCM
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ocx74.818$Fc6.7974@news4.mia>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <nT874.11689$DC6.169673@news2.mia> <2De74.6977$_f.66805@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
>Judson McClendon wrote:
>>Okay, are you saying then that C/C++ programs are much more 'bug prone'
…[6 more quoted lines elided]…
>with their pets OR choice of programming language.

You left out 'food preference'.  Remember, 'real programmers' don't eat
quiche.  Unfortunately, I like quiche.  Does that make me a 'pseudo
programmer'. ;-)
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 4)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991222005127.23435.00001234@ng-fx1.aol.com>`
- **References:** `<Ocx74.818$Fc6.7974@news4.mia>`

```
>You left out 'food preference'.  Remember, 'real programmers' don't eat
>quiche.  Unfortunately, I like quiche.  Does that make me a 'pseudo
>programmer'. ;-)

well, if its really good quiche.... :))
Asimov, Heinlein, and Zappa
Still the best
```

#### ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83h03k$83m$1@hermes.enternet.co.nz>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <822ah5$1gc$1@nntp5.atl.mindspring.net> <3ex14.6774$Ic5.79616@news3.mia> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net>`

```

Michael Mattias wrote in message ...
>My real point is, to
>paraphrase Churchill's requests to the US for military aid at the onset of
>the Second World War, is, "Give us the tools and we'll finish the job."
>
Of course, in many Programming shops this gets misquoted as: "Give us the
job and we'll finish the tools"....

Pete.

















>
>
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mrT64.3033$_f.20516@dfiatx1-snr1.gtei.net>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <3ex14.6774$Ic5.79616@news3.mia> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <WdM64.1146$_f.3759@dfiatx1-snr1.gtei.net> <83h03k$83m$1@hermes.enternet.co.nz>`

```
So, you ARE still alive and kicking, Pete. So which part of Gaia's garden
are you in these days? Back upon the pastoral plain of New Zealand? In merry
olde merry olde England? Or for a change of pace, sampling the pleasures of
the Republic of Togo?


Michael Mattias
Racine WI USA


Peter E. C. Dashwood wrote in message
<83h03k$83m$1@hermes.enternet.co.nz>...
>
>Michael Mattias wrote in message ...
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
