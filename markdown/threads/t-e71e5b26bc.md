[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Console Colors in MF Personal Cobol

_14 messages · 6 participants · 1998-09 → 1998-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Console Colors in MF Personal Cobol

- **From:** heidegger@my-dejanews.com
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uo747$ct5$1@nnrp1.dejanews.com>`

```
A thousand pardons if this is off-topic and/or a FAQ, but MF Personal Cobol
running on my Win95 box displays barely legible colors in the output console
window. I can't seem to find any way to configure this.

TIA for any light shed on this subject!

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: Console Colors in MF Personal Cobol

- **From:** "Jay Moseley" <jay^_^moseley@ibm-dot-net>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com>`

```
I use Microsoft COBOL 5.0 (which is really repackaged MicroFocus COBOL) and I
have experienced what you describe. Often I write quick&dirty programs to
test code fragments and I finally got annoyed enough with the barely legible
dark red on black information DISPLAYed that I looked into the problem. I
discovered that when I was linking the programs I was not including the 2
libraries LCOBOL and COBAPI. The programs linked and ran fine without them,
but when I put these 2 libraries into the link command the text DISPLAYed
became white on black, which is much more readible.

Hope this helps.

Jay Moseley, CCP


On Mon, 28 Sep 1998 14:40:07 GMT, heidegger@my-dejanews.com wrote:

:>A thousand pardons if this is off-topic and/or a FAQ, but MF Personal Cobol
:>running on my Win95 box displays barely legible colors in the output console
:>window. I can't seem to find any way to configure this.
:>
:>TIA for any light shed on this subject!
:>
:>-----== Posted via Deja News, The Leader in Internet Discussion ==-----
:>http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: Console Colors in MF Personal Cobol

- **From:** heidegger@my-dejanews.com
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6upmvv$2rl$1@nnrp1.dejanews.com>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net>`

```
In article <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net>,
  "Jay Moseley" <jay^_^moseley@ibm-dot-net> wrote:

> I use Microsoft COBOL 5.0 (which is really repackaged MicroFocus COBOL) and I
> have experienced what you describe.

Unfortunately, this is "Personal Cobol," an academic product that MF puts out
for hapless beginning CS students such as myself. Although there is an option
to add compiler directives, a) I don't know what they would look like, and b)
I don't see anything resembling the libs you linked in to improve your
console display. Since Personal Cobol is crippled in that it cannot produce
executable files, I wonder how much flexibility is possible when it comes to
link arguments.

Sorry if this sounds fairly brainless but I'm about three weeks into a first
Cobol course and am in fact brainless at this stage of the game where Cobol is
concerned.

> Hope this helps.

Thanks for replying! It's all uphill from here, yes? <g>

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uq521$995$1@news.igs.net>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com>`

```

heidegger@my-dejanews.com wrote in message
<6upmvv$2rl$1@nnrp1.dejanews.com>...
>In article <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net>,
>  "Jay Moseley" <jay^_^moseley@ibm-dot-net> wrote:
>
>Unfortunately, this is "Personal Cobol," an academic product that MF puts
out


The problem is that it is a DOS product.  Just hit the full screen
icon in the DOS box (you might have to enable the toolbar to do
it) and the screens will become quite readable. You can also play
with the palettes to improve it in a window, but it takes more
screwing about.
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

_(reply depth: 4)_

- **From:** heidegger@my-dejanews.com
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ur64c$l59$1@nnrp1.dejanews.com>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com> <6uq521$995$1@news.igs.net>`

```
In article <6uq521$995$1@news.igs.net>,
  "Donald Tees" <donald@willmack.com> wrote:

> The problem is that it is a DOS product.

AYE, there's the rub: I'm using the Windoze version! So the console in
question is a Win95 text console window.

NOW, call me paranoid, but I suspect MF set up this academic product with
an almost unreadable DISPLAY output so that the chance would be almost
zero that it might be put to actual use. Yes, no, punt?

(OR, finally get off my butt and grab the Linux Cobol package I saw
t'other night while browsing the 'Net?)
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-ddqpMQ5Jq28U@Dwight_Miller.iix.com>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com> <6uq521$995$1@news.igs.net> <6ur64c$l59$1@nnrp1.dejanews.com>`

```
On Tue, 29 Sep 1998 17:41:32, heidegger@my-dejanews.com wrote:

> (OR, finally get off my butt and grab the Linux Cobol package I saw
> t'other night while browsing the 'Net?)
>

Hmmm... Id be interested in a Linux COBOL.
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

_(reply depth: 6)_

- **From:** heidegger@my-dejanews.com
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6utiqt$k80$1@nnrp1.dejanews.com>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com> <6uq521$995$1@news.igs.net> <6ur64c$l59$1@nnrp1.dejanews.com> <Jl0PnHJ5PvPd-pn2-ddqpMQ5Jq28U@Dwight_Miller.iix.com>`

```
In article <Jl0PnHJ5PvPd-pn2-ddqpMQ5Jq28U@Dwight_Miller.iix.com>,
  redsky@ibm.net (Thane Hubbell) wrote:

> Hmmm... Id be interested in a Linux COBOL.

http://www.deskware.com/cobol/cobol.htm

I haven't tried it yet, so I'd be curious to get the impressions of someone
more knowledgeable about Cobol than meeself.
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6urf2l$npg$1@news.igs.net>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com> <6uq521$995$1@news.igs.net> <6ur64c$l59$1@nnrp1.dejanews.com>`

```
heidegger@my-dejanews.com wrote in message
<6ur64c$l59$1@nnrp1.dejanews.com>...
>AYE, there's the rub: I'm using the Windoze version! So the console in
>question is a Win95 text console window.
>NOW, call me paranoid, but I suspect MF set up this academic product with
>an almost unreadable DISPLAY output so that the chance would be almost
>zero that it might be put to actual use. Yes, no, punt?

I'd call you paranoid <g>. In fact, it is common to give away the
last version cheap to students.  Problem is, there are no *old*
Windows95 versions,  so the final of the last version happens
to be a DOS version, written and sold before the Windows95
"console" even existed.  That is when I bought it, and as I recall
I paid in the $600 dollars Canadian range for it.  That is about
a grand in U.S.A. dollars.  The current upgrade is about $6000
in our money, so you got a good deal.  I would not complain ...
it is good enough to learn on.  Like I said, you can get a fairly
good picture by going DOS mode fully, or playing with the
Windows95 palettes.

As I recall, that is a pretty solid compiler.  While I have switched
companies (I find the new product grossly overpriced), I earned
in the one million range using it for five or six years.
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

_(reply depth: 6)_

- **From:** heidegger@my-dejanews.com
- **Date:** 1998-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6utii6$k3q$1@nnrp1.dejanews.com>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com> <6uq521$995$1@news.igs.net> <6ur64c$l59$1@nnrp1.dejanews.com> <6urf2l$npg$1@news.igs.net>`

```
In article <6urf2l$npg$1@news.igs.net>,
  "Donald Tees" <donald@willmack.com> wrote:

> I'd call you paranoid <g>.

Agreed. It must've been a slow news, or a bad hair, day when I pounded out
that mini-rant.

> In fact, it is common to give away the
> last version cheap to students.  Problem is, there are no *old*
> Windows95 versions,  so the final of the last version happens
> to be a DOS version, written and sold before the Windows95
> "console" even existed.

Nope. Apparently there's a Win 3.1 version because that's what it says on the
cover of the manual that came with mine: "Personal Cobol for Windows 3.1".
Cost me about $60 in the school bookstore. Doesn't produce executables.

> As I recall, that is a pretty solid compiler.  While I have switched
> companies (I find the new product grossly overpriced), I earned
> in the one million range using it for five or six years.

Not too shabby. I guess I should lighten up and focus on learning the stuff,
huh? <g>
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

_(reply depth: 6)_

- **From:** as999@torfree.net (Adrian Boldan)
- **Date:** 1998-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F07nI5.EzA.0.bloor@torfree.net>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com> <6uq521$995$1@news.igs.net> <6ur64c$l59$1@nnrp1.dejanews.com> <6urf2l$npg$1@news.igs.net>`

```
Donald Tees (donald@willmack.com) wrote:
: I paid in the $600 dollars Canadian range for it.  That is about
: a grand in U.S.A. dollars.  The current upgrade is about $6000

Oh, tempora! :-) 25 years ago 600CDN may have been $1000 US. Now it's the 
other way around :-(
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6v3or4$eob$1@news.igs.net>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com> <6uq521$995$1@news.igs.net> <6ur64c$l59$1@nnrp1.dejanews.com> <6urf2l$npg$1@news.igs.net> <F07nI5.EzA.0.bloor@torfree.net>`

```

Adrian Boldan wrote in message ...
>Donald Tees (donald@willmack.com) wrote:
>: I paid in the $600 dollars Canadian range for it.  That is about
…[4 more quoted lines elided]…
>
Huh?  You got it the exact opposite.  Today, the Canadian Dollar
is pegged at 69 cents US.  I used the 600 to 1000 ratio because
you also have to add in tax when it crosses the border.  I buy
stateside constantly, and have a US dollar account at my bank
in addition to a couple of Canadian accounts.
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

_(reply depth: 5)_

- **From:** "Thomas Rowe" <trowe@greenville.infi.net>
- **Date:** 1998-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdeda4$b3ff14a0$8e0785d0@default>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com> <6uq521$995$1@news.igs.net> <6ur64c$l59$1@nnrp1.dejanews.com>`

```
Sorry the full scale version displays uses the same awful colors by
default.

heidegger@my-dejanews.com wrote in article
<6ur64c$l59$1@nnrp1.dejanews.com>...
> In article <6uq521$995$1@news.igs.net>,
>   "Donald Tees" <donald@willmack.com> wrote:
…[5 more quoted lines elided]…
> zero that it might be put to actual use.?
```

###### ↳ ↳ ↳ Re: Console Colors in MF Personal Cobol

- **From:** "Thomas Rowe" <trowe@greenville.infi.net>
- **Date:** 1998-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdeda4$1348cec0$8e0785d0@default>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com> <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net> <6upmvv$2rl$1@nnrp1.dejanews.com>`

```
Go into MicroFocus COBOL help;
Click on STANDARD COBOL REFERENCE;
  COBOL SOURCE SYNTAX;
  COBOL VERBS;
  DISPLAY;
  Full Screen.

This shows extended options that you can use with the DISPLAY command.
 

heidegger@my-dejanews.com wrote in article
<6upmvv$2rl$1@nnrp1.dejanews.com>...
> In article <wnlzbfryrlvozarg.f007pv0.pminews@news1.ibm.net>,
>   "Jay Moseley" <jay^_^moseley@ibm-dot-net> wrote:
> 
> > I use Microsoft COBOL 5.0 (which is really repackaged MicroFocus COBOL)
and I
> > have experienced what you describe.
> 
> Unfortunately, this is "Personal Cobol," an academic product that MF puts
out
> for hapless beginning CS students such as myself. Although there is an
option
> to add compiler directives, a) I don't know what they would look like,
and b)
> I don't see anything resembling the libs you linked in to improve your
> console display. Since Personal Cobol is crippled in that it cannot
produce
> executable files, I wonder how much flexibility is possible when it comes
to
> link arguments.
> 
> Sorry if this sounds fairly brainless but I'm about three weeks into a
first
> Cobol course and am in fact brainless at this stage of the game where
Cobol is
> concerned.
> 
…[6 more quoted lines elided]…
>
```

#### ↳ Re: Console Colors in MF Personal Cobol

- **From:** "Dick McMullen" <dmcmulle@exicorp.com>
- **Date:** 1998-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3614eb95.0@207.226.241.101>`
- **References:** `<6uo747$ct5$1@nnrp1.dejanews.com>`

```
Try setting the run-time switch +a1

This changes the stdout device so it is redirectable via command line
redirection (program > display.out) and changes the color from brown to
white.  At least it did for me on an older release of MF COBOL.

Dick McMullen


heidegger@my-dejanews.com wrote in message
<6uo747$ct5$1@nnrp1.dejanews.com>...
>A thousand pardons if this is off-topic and/or a FAQ, but MF Personal Cobol
>running on my Win95 box displays barely legible colors in the output
console
>window. I can't seem to find any way to configure this.
>
…[3 more quoted lines elided]…
>http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
