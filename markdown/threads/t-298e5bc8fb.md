[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Mainframe JCL Conversion Tools

_10 messages · 7 participants · 2004-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Re: IBM Mainframe JCL Conversion Tools

- **From:** james8049 <james8049.1bm5tr@mail.codecomments.com>
- **Date:** 2004-08-24T12:10:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<james8049.1bm5tr@mail.codecomments.com>`

```

In defense of JCL!
For its time JCL was quite advanced: 
It give you device independence long before UNIX did. The target of a
DD statement could be a printer, cardreader, disk file, tape drive, a
collection of files. As long as it was readable for "OPEN INPUT" or
writeable for "OPEN OUTPUT" and some basic record size and blocking
matched your program did not care.


And if you think JCL is bad try UNIX CSH.

Having said that though the only JCL I ever use is:-
//TSO      EXEC PGM=IKJEFT1B,.......

:-)
```

#### ↳ Re: Re: IBM Mainframe JCL Conversion Tools

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-08-26T20:29:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cglh7h$4vg$1@peabody.colorado.edu>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com>`

```

On 24-Aug-2004, james8049 <james8049.1bm5tr@mail.codecomments.com> wrote:

> In defense of JCL!
> For its time JCL was quite advanced:
…[4 more quoted lines elided]…
> matched your program did not care.

How do you compare JCL with what the other mainframe computer manufacturers
offered?

Let's pick a date - say 1980 and rank the various mainframe operating systems.
Or 1970.
```

##### ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-26T23:14:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-3103C4.23140726082004@knology.usenetserver.com>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com> <cglh7h$4vg$1@peabody.colorado.edu>`

```
In article <cglh7h$4vg$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:

> On 24-Aug-2004, james8049 <james8049.1bm5tr@mail.codecomments.com> wrote:
> 
…[12 more quoted lines elided]…
> Or 1970.

The only date that matters is 2004 -- no other mainframe OS/hardware 
combos exist.  It is JCL compared to bash or cmd.

My only complaint is that IBM has failed to realized that the tiny 
computers are taking over its turf.  If it does not update its tools to 
be competitive it will go the way of ______________ (Rayovac, Spery, GE, 
Univac, RCA, fill in the blank with the name of a dead electronics 
manufacturer here, etc, etc)...
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** rsteiner@visi.com (Richard Steiner)
- **Date:** 2004-08-27T02:43:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4YuLBpHpvKRQ092yn@visi.com>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com> <cglh7h$4vg$1@peabody.colorado.edu> <joe_zitzelberger-3103C4.23140726082004@knology.usenetserver.com>`

```
Here in comp.lang.cobol,
Joe Zitzelberger <joe_zitzelberger@nospam.com> spake unto us, saying:

>The only date that matters is 2004 -- no other mainframe OS/hardware 
>combos exist.  It is JCL compared to bash or cmd.

As a 2200 programmer who has at least an academic interest in IBM's
JCL, how does it compare to the current incarnation of Unisys' ECL?

Does anyone here know both?

>My only complaint is that IBM has failed to realized that the tiny 
>computers are taking over its turf.  If it does not update its tools to 
>be competitive it will go the way of ______________ (Rayovac, Spery, GE, 
>Univac, RCA, fill in the blank with the name of a dead electronics 
>manufacturer here, etc, etc)...

You might want to note that at least two members of the BUNCH (Sperry
and Burroughs) are still very much alive in their limited markets under
the guise of Unisys "Clearpath" hardware (which run either OS2200/EXEC8
or MCP in most cases).  :-)
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-27T14:47:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408271347.24228ea3@posting.google.com>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com> <cglh7h$4vg$1@peabody.colorado.edu> <joe_zitzelberger-3103C4.23140726082004@knology.usenetserver.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote 

> My only complaint is that IBM has failed to realized that the tiny 
> computers are taking over its turf.  

How odd that you think this.  The number of z series machines being
sold is greater than ever before.

> If it does not update its tools to 
> be competitive it will go the way of ______________ (Rayovac, Spery, GE, 
> Univac, RCA, fill in the blank with the name of a dead electronics 
> manufacturer here, etc, etc)...

Well it has 'updated'.  Now most z series seem to be running Linux.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 4)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-28T19:52:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ae1j0hf3306j7g6bamu05b1si06fasdo0@4ax.com>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com> <cglh7h$4vg$1@peabody.colorado.edu> <joe_zitzelberger-3103C4.23140726082004@knology.usenetserver.com> <217e491a.0408271347.24228ea3@posting.google.com>`

```
>> 27 Aug 2004 14:47:17 -0700, riplin@Azonic.co.nz (Richard) wrote:

>Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote 
>
…[4 more quoted lines elided]…
>sold is greater than ever before.

Not ever before, since the late '80s. During the '90s IBM was selling
about 30 _new_ shops per year in the US. After they introduced Linux,
the number shot up to 200.

>> If it does not update its tools to 
>> be competitive it will go the way of ______________ (Rayovac, Spery, GE, 
>> Univac, RCA, fill in the blank with the name of a dead electronics 
>> manufacturer here, etc, etc)...

Don't forget Amdahl and Cray, which are now sinking ships.

>Well it has 'updated'.  Now most z series seem to be running Linux.

Make that most NEW installations. There are many more zOS shops in the
US. I've been told that in the world, VSE is still IBM's most popular
operating system.

FWIW, 70% of IBM's Net Profit still comes from mainframes. Not Revenue
but net profit. Most of it comes from non-hardware functions such as
Services (outsourcing, body-shop backfill) and Software licenses. 

I've worked with their Services people quite a lot. I wasn't impressed
with their screening standards. Other contracting companies cultivate
long-term relationships. With IBM, workers are a commodity to be
herded in and out. Some of their people, mostly managers,  are
talented, but 90% are cordwood. Clients could hire better talent from
other contractors for less than half IBM's $200/hr bill rate. For some
reason, the IBM imprimatur continues to have cachet and command
respect from executives. 

Not because it's Good but because it's Safe. If a project fails, it's
finger-pointing time. Nobody can criticize the decision to go with the
Gold Standard IBM. Similarly, networking contracts go to AT&T, not
because they have the best talent,  but because they're The Phone
Company.

We've developed a mentality that reveres Brand Names as safe havens,
fulfilling the function religion used to perform. Then you were
Protestant, Catholic or Jewish; later you were GM, Ford or Chrysler;
now you are IBM, Sun or Mac.  Human nature doesn't change.  IBM found
a way to exploit that and it continues to pay dividends 25 years
later.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-28T20:35:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgr8c4$o77$1@panix5.panix.com>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com> <joe_zitzelberger-3103C4.23140726082004@knology.usenetserver.com> <217e491a.0408271347.24228ea3@posting.google.com> <4ae1j0hf3306j7g6bamu05b1si06fasdo0@4ax.com>`

```
In article <4ae1j0hf3306j7g6bamu05b1si06fasdo0@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:

[snip]

>For some
>reason, the IBM imprimatur continues to have cachet and command
…[4 more quoted lines elided]…
>Gold Standard IBM.

As my first programming instructor taught us, lo, those many years ago, 
'Nobody ever got fired for recommending IBM'.

As the Germans say, 'plus ca change, plus c'est la meme chose'.

DD
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-29T02:20:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nbf2j05npjrum65hkr3i77tktrksvd6oma@4ax.com>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com> <joe_zitzelberger-3103C4.23140726082004@knology.usenetserver.com> <217e491a.0408271347.24228ea3@posting.google.com> <4ae1j0hf3306j7g6bamu05b1si06fasdo0@4ax.com> <cgr8c4$o77$1@panix5.panix.com>`

```
On 28 Aug 2004 20:35:16 -0400, docdwarf@panix.com wrote:

>As the Germans say, 'plus ca change, plus c'est la meme chose'.

Germans wouldn't phrase their aphorisms in French. Too close to home.
Maybe Brazilian Portuguese or Spanish .. to show how worldly they are.
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-28T22:25:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgrera$shd$1@panix5.panix.com>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com> <4ae1j0hf3306j7g6bamu05b1si06fasdo0@4ax.com> <cgr8c4$o77$1@panix5.panix.com> <nbf2j05npjrum65hkr3i77tktrksvd6oma@4ax.com>`

```
In article <nbf2j05npjrum65hkr3i77tktrksvd6oma@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On 28 Aug 2004 20:35:16 -0400, docdwarf@panix.com wrote:
>
…[3 more quoted lines elided]…
>Maybe Brazilian Portuguese or Spanish .. to show how worldly they are.

Mr Wagner, I've worked with Germans... and my experience is different than 
what you describe here.

DD
```

###### ↳ ↳ ↳ Re: IBM Mainframe JCL Conversion Tools

_(reply depth: 7)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-29T09:43:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-104C84.09435629082004@knology.usenetserver.com>`
- **References:** `<james8049.1bm5tr@mail.codecomments.com> <joe_zitzelberger-3103C4.23140726082004@knology.usenetserver.com> <217e491a.0408271347.24228ea3@posting.google.com> <4ae1j0hf3306j7g6bamu05b1si06fasdo0@4ax.com> <cgr8c4$o77$1@panix5.panix.com> <nbf2j05npjrum65hkr3i77tktrksvd6oma@4ax.com>`

```
In article <nbf2j05npjrum65hkr3i77tktrksvd6oma@4ax.com>,
 Robert Wagner <robert@wagner.net.yourmammaharvests> wrote:

> On 28 Aug 2004 20:35:16 -0400, docdwarf@panix.com wrote:
> 
…[3 more quoted lines elided]…
> Maybe Brazilian Portuguese or Spanish .. to show how worldly they are.

Perhaps it was said by an ex-collaborator with an original native French 
language.

;-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
