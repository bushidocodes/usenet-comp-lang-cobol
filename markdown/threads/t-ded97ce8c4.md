[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol-mode for emacs

_8 messages · 5 participants · 2003-09_

---

### cobol-mode for emacs

- **From:** Benoit Dejean <bnet@ifrance.com>
- **Date:** 2003-09-09T20:41:57+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2003.09.09.18.41.57.562489@ifrance.com>`

```
i am looking for a cobol mode for emacs or a cobol editor for GNU/Linux.
thanks
```

#### ↳ Re: cobol-mode for emacs

- **From:** "Simeon Nevel" <snevel@sonic.net>
- **Date:** 2003-09-09T19:02:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Osp7b.20166$dk4.630351@typhoon.sonic.net>`
- **References:** `<pan.2003.09.09.18.41.57.562489@ifrance.com>`

```

"Benoit Dejean" <bnet@ifrance.com> wrote:

> i am looking for a cobol mode for emacs or a cobol editor for GNU/Linux.

Google is your friend.

The first & third link returned from a Google search for

    emacs cobol-mode

found 2 different cobol.el files.

http://www.geocrawler.com/archives/3/338/1993/3/0/1879063/

http://tiny-cobol.sourceforge.net/docs/tiny-cobol-introduction-0.2/firstprogram.html

The other links look useful as well.

Simeon
```

##### ↳ ↳ Re: cobol-mode for emacs

- **From:** Benoit Dejean <bnet@ifrance.com>
- **Date:** 2003-09-09T21:27:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2003.09.09.19.27.13.22903@ifrance.com>`
- **References:** `<pan.2003.09.09.18.41.57.562489@ifrance.com> <Osp7b.20166$dk4.630351@typhoon.sonic.net>`

```
Le Tue, 09 Sep 2003 19:02:06 +0000, Simeon Nevel a ï¿œcritï¿œ:


> "Benoit Dejean" <bnet@ifrance.com> wrote:
> 
…[3 more quoted lines elided]…
> Google is your friend.

(i meant in console mode)

> The first & third link returned from a Google search for
> 
…[4 more quoted lines elided]…
> http://www.geocrawler.com/archives/3/338/1993/3/0/1879063/

seems to be incomplete

> http://tiny-cobol.sourceforge.net/docs/tiny-cobol-introduction-0.2/firstprogram.html

is broken

> The other links look useful as well.

i have a found byte-compiled .elc but i am not able to make it work
(doesn't load)

that's why i am here :oD

> Simeon

thank you
```

#### ↳ Re: cobol-mode for emacs

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-09T15:15:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vlsd7n8hqlu532@corp.supernews.com>`
- **In-Reply-To:** `<pan.2003.09.09.18.41.57.562489@ifrance.com>`
- **References:** `<pan.2003.09.09.18.41.57.562489@ifrance.com>`

```
Benoit Dejean wrote:

> i am looking for a cobol mode for emacs or a cobol editor for GNU/Linux.
> thanks

I don't know if there's a console-mode GVIM or not, but it works pretty 
well.  It flags lines with footprints past column 72 as errors, even if 
they're commented with *>, but other than that, it does highlight syntax 
and such.
```

##### ↳ ↳ Re: cobol-mode for emacs

- **From:** Sven Brueggemann <SBrueggemann@gmx.net>
- **Date:** 2003-09-09T22:29:56+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vsdslvgdl2okulcrnra1h5rk3tuvu30uuf@4ax.com>`
- **References:** `<pan.2003.09.09.18.41.57.562489@ifrance.com> <vlsd7n8hqlu532@corp.supernews.com>`

```
LX-i <LXi0007@Netscape.net> wrote:

>> i am looking for a cobol mode for emacs or a cobol editor for GNU/Linux.
>> thanks
…[3 more quoted lines elided]…
>and such.

The console-mode "gvim" is called "vim" and is available for every OS
you will find a COBOL compiler for.

Regarding column 72: That never occured to me but it should be easy to
fix that in cobol.vim.

Kind regards

Sven
```

##### ↳ ↳ Re: cobol-mode for emacs

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-09T18:53:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309091753.7efa300@posting.google.com>`
- **References:** `<pan.2003.09.09.18.41.57.562489@ifrance.com> <vlsd7n8hqlu532@corp.supernews.com>`

```
LX-i <LXi0007@Netscape.net> wrote 

> > i am looking for a cobol mode for emacs or a cobol editor for GNU/Linux.
> > thanks
…[4 more quoted lines elided]…
> and such.

Isn't suggesting that an emacs user look at a vi clone like offering a
ham and cheese sandwich to a Rabbi ?
```

###### ↳ ↳ ↳ Re: cobol-mode for emacs

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-10T11:18:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vlujmaislnhe36@corp.supernews.com>`
- **In-Reply-To:** `<217e491a.0309091753.7efa300@posting.google.com>`
- **References:** `<pan.2003.09.09.18.41.57.562489@ifrance.com> <vlsd7n8hqlu532@corp.supernews.com> <217e491a.0309091753.7efa300@posting.google.com>`

```
Richard wrote:
> LX-i <LXi0007@Netscape.net> wrote 
> 
…[11 more quoted lines elided]…
> ham and cheese sandwich to a Rabbi ?

I don't know - I'm not too familiar with Linux (though I'm learning). 
He said "or", so I thought it might be what he wanted.  Is vi vs. emacs 
a big unix rivalry (like Word vs. WordPerfect used to be)?
```

#### ↳ Re: cobol-mode for emacs

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-09T18:50:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309091750.e2c25fe@posting.google.com>`
- **References:** `<pan.2003.09.09.18.41.57.562489@ifrance.com>`

```
Benoit Dejean <bnet@ifrance.com> wrote 

> i am looking for a cobol mode for emacs or a cobol editor for GNU/Linux.
> thanks

I quite like setedit (setedit.sourceforge.net) for Linux.  I wrote my
own 'Cobol mode' which involved a list of all keywords (plus a couple
of other things) for colour highlighting and some setup for keystroke
macros to output keywords from a couple of keystrokes.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
