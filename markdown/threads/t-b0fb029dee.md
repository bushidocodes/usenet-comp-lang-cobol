[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need a Little help

_8 messages · 6 participants · 2003-04_

---

### Need a Little help

- **From:** Lee Itson <litson@columbus.rr.com>
- **Date:** 2003-04-13T15:10:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu>`

```
Ok guys, I am just starting with COBOL in a class I'm taking and I'm 
sure these questions are SOOOOO elementary that it isnt funny, but i 
wanted to make sure I'm doing it right.

1.  The report I need to make has page headings and column headings.  Do 
I need to defined those in the File Definitions of the Data Division?

2. On the topic of headings, the column headings need to be underlined. 
  I havent been able to pick up the book we are using yet, and out prof 
hasn't spoken about it, so was wondering what the command for underline was.

Thanks in Advance Guys.

Lee Itson
```

#### ↳ Re: Need a Little help

- **From:** "Lorne Sunley" <lsunley@mb.sympatico.ca>
- **Date:** 2003-04-13T19:27:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JMPlV5b5VFnN-pn2-008qOR1KtHp3@h24-82-204-17.wp.shawcable.net>`
- **References:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu>`

```
On Sun, 13 Apr 2003 19:10:13 UTC, Lee Itson <litson@columbus.rr.com> 
wrote:

> Ok guys, I am just starting with COBOL in a class I'm taking and I'm 
> sure these questions are SOOOOO elementary that it isnt funny, but i 
…[4 more quoted lines elided]…
> 

No, those would usually be defined in working storage, where you can 
assign a literal value to the headings.

> 2. On the topic of headings, the column headings need to be underlined. 
>   I havent been able to pick up the book we are using yet, and out prof 
> hasn't spoken about it, so was wondering what the command for underline was.
> 

You can issue printer control commands to select a font with 
"underline" or you can print another line with "-" characters in the 
appropriate spots.

> Thanks in Advance Guys.
> 
> Lee Itson
> 
```

##### ↳ ↳ Re: Need a Little help

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-04-16T14:17:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99ucncKeZOwdgAOjXTWcrg@comcast.com>`
- **References:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu> <JMPlV5b5VFnN-pn2-008qOR1KtHp3@h24-82-204-17.wp.shawcable.net>`

```

"Lorne Sunley" <lsunley@mb.sympatico.ca> wrote in message
news:JMPlV5b5VFnN-pn2-008qOR1KtHp3@h24-82-204-17.wp.shawcable.net...
> On Sun, 13 Apr 2003 19:10:13 UTC, Lee Itson <litson@columbus.rr.com>
> wrote:
…[14 more quoted lines elided]…
> > hasn't spoken about it, so was wondering what the command for underline
was.
> >
>
…[11 more quoted lines elided]…
> Lorne Sunley

     I know of no reliable way to underline something.  Printing a line
of underlines on top of the first line does not work on laser printers,
and using printer control commands does not normally
work on line printers.
```

#### ↳ Re: Need a Little help

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-13T16:41:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E99D982.70009@Knology.net>`
- **References:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu>`

```
Lee Itson wrote:
> 2. On the topic of headings, the column headings need to be underlined. 
>  I havent been able to pick up the book we are using yet, and out prof 
> hasn't spoken about it, so was wondering what the command for underline 
> was.

You might want to investigate the WRITE ... BEFORE ADVANCING syntax. 
Using it, you can define two records in working-storage - one with text, 
and one with underscores.  Then, you can "overprint" the underscores on 
the text.  It's tricky, but your textbook or COBOL Language Reference 
Manual will detail it for you.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

##### ↳ ↳ Re: Need a Little help

- **From:** yankee_p@interpuntonet.it (Pino)
- **Date:** 2003-04-13T23:33:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2d1c2f2e.0304132233.9163b0a@posting.google.com>`
- **References:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu> <3E99D982.70009@Knology.net>`

```
With Acucobol version >5 you can define with win$printer routine rows
and columns on a print page.



LX-i <DanielJS@Knology.net> wrote in message news:<3E99D982.70009@Knology.net>...
> Lee Itson wrote:
> > 2. On the topic of headings, the column headings need to be underlined. 
…[16 more quoted lines elided]…
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

#### ↳ Re: Need a Little help

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-17T07:00:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dsmdneRum8rvCgOjXTWJiw@giganews.com>`
- **References:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu>`

```

"Lee Itson" <litson@columbus.rr.com> wrote in message
news:b7ccmm$cfi$1@news.cis.ohio-state.edu...
> Ok guys, I am just starting with COBOL in a class I'm taking and I'm
> sure these questions are SOOOOO elementary that it isnt funny, but i
…[7 more quoted lines elided]…
> hasn't spoken about it, so was wondering what the command for underline
was.

Look at the purpose, not the symptom.

Underlining is an artifact left from the days of the typewriter to emphasise
a word or phrase. By so doing, the typist was trying to emulate the printed
world with the tools she had available.

You can now use the same visual tools as the typographer - bold, italic,
even a different font. Go back to the concept of printing and use bold.
Don't try to emulate a typewriter that's compensating as it trys to emulate
a printing press.
```

##### ↳ ↳ Re: Need a Little help

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-17T20:41:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E9F57DA.1050808@Knology.net>`
- **References:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu> <dsmdneRum8rvCgOjXTWJiw@giganews.com>`

```
JerryMouse wrote:
> "Lee Itson" <litson@columbus.rr.com> wrote in message
> news:b7ccmm$cfi$1@news.cis.ohio-state.edu...
…[8 more quoted lines elided]…
> a printing press.

However, he would probably fail if the prof wanted it underlined...  :)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

#### ↳ Re: Need a Little help

- **From:** Lee Itson <litson@columbus.rr.com>
- **Date:** 2003-04-17T13:31:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7moe9$k1v$1@news.cis.ohio-state.edu>`
- **In-Reply-To:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu>`
- **References:** `<b7ccmm$cfi$1@news.cis.ohio-state.edu>`

```
Lee Itson wrote:
> Ok guys, I am just starting with COBOL in a class I'm taking and I'm 
> sure these questions are SOOOOO elementary that it isnt funny, but i 
…[13 more quoted lines elided]…
> 

Thanks all for your help, got it all figured out.

Lee
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
