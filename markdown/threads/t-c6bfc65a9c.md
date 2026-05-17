[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# I need some utilities that makes screens works at 60x80 or similar, in COBOL

_11 messages · 8 participants · 1998-01 → 1998-02_

---

### I need some utilities that makes screens works at 60x80 or similar, in COBOL

- **From:** "ram..." <ua-author-17075243@usenetarchives.gap>
- **Date:** 1998-01-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34ccfec9.2082604@diana.ibernet.es>`

```

Is that possible?

Do you know any util or lib that can do it?

I'am to do my final project at school and I want to do my program like
it shows in graphic mode in PASCAL or as similar as possible...

If you know anything that can do it, I will thank you if you
send me an e-mail about how to get it..

Thx and Bye.
```

#### ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

- **From:** "ram..." <ua-author-17075243@usenetarchives.gap>
- **Date:** 1998-01-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34ccfec9.2082604@diana.ibernet.es>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es>`

```

I must use MF-COBOL 4.5
```

##### ↳ ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

- **From:** "la..." <ua-author-93577@usenetarchives.gap>
- **Date:** 1998-01-25T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6bfc65a9c-p2@usenetarchives.gap>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es> <gap-c6bfc65a9c-p2@usenetarchives.gap>`

```

Hello there,

Does anyone know the minimum qualifications for an "entry-level"
programmer in COBOL?

I'm an older college grad (Eng.Lit. major--don't laugh, and a Phil.
minor) living in the San Fran area. I've been reading "Cobol for
Dummies" and "Teach Yourself Cobol in 21 Days". Book theory and lessons
on a compiler are OK, but I imagine it doesn't come anywhere close to
the practical experience gained in an actual programming job.

It would be most appreciated if anyone can please tell me what I need
from here to get entry-level work . Thanks.
```

#### ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-25T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34ccfec9.2082604@diana.ibernet.es>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es>`

```


Luis wrote in message <34c··.@dia··t.es>...
› Is that possible?
› 
…[8 more quoted lines elided]…
› Thx and Bye.

Having seen your other note indicating that you are using Micro Focus
COBOL, have you looked at the Screen Section and ACCEPT/DISPLAY syntax? I
am not clear what you mean by 80x60 or like PASCAL graphics - but that is
probably just my ignorance of those terms. However, if you are doing simple
character mode "data-entry" type screens, those can easily be done in MF
COBOL. If you are looking to do GUI (graphical) screens, this can be done in
MF COBOL too - but it takes calls to various APIs (for example Windows).
```

##### ↳ ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6bfc65a9c-p4@usenetarchives.gap>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es> <gap-c6bfc65a9c-p4@usenetarchives.gap>`

```

"William M. Klein" wrote:

› Luis wrote in message <34c··.@dia··t.es>...
› [snip]
…[7 more quoted lines elided]…
› 

William:

When he says 80 x 60, I believe that he's talking about 800 x 600
screen display resolution. Typical VGA resolution is 640 horizontal
pixel density by 480 vertical pixel density. 800 by 600 resolution is
on the low end of the super VGA resolution modes.

....for an even easier way to implement GUI screens than the event
driven API, take a look at COBOL sp2......(sorry William, I plead
guilty to slipping in my P.T. Barnum-like company propaganda ;-)

You can download an evaluation version from the flexus website at:

http://www.flexus.com



Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

- **From:** "charles w. hall" <ua-author-6588798@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6bfc65a9c-p5@usenetarchives.gap>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es> <gap-c6bfc65a9c-p4@usenetarchives.gap> <gap-c6bfc65a9c-p5@usenetarchives.gap>`

```

When someone says 80X60 that usually means 80 columns across with
screen, with 60 rows on the screen. This is common for text screens
displaying a whole page of text at once, as opposed to 80x24 or 80x25
that most CRTs would display. How times have changed (mostly for the
better) that people are no longer certain what these terms mean. Where I
work we constantly run across this kind of confusion, as people who grew
up on PCs never had to deal with these kinds of display restrictions and
have no way to relate to these older concepts.

Charles Hall

Bob Wolfe wrote:

›   I
›› am not clear what you mean by 80x60 or like PASCAL graphics - but
› that is
›› probably just my ignorance of those terms.
›
```

###### ↳ ↳ ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

- **From:** "ram..." <ua-author-17075243@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6bfc65a9c-p5@usenetarchives.gap>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es> <gap-c6bfc65a9c-p4@usenetarchives.gap> <gap-c6bfc65a9c-p5@usenetarchives.gap>`

```

On Tue, 27 Jan 1998 13:41:14 GMT, rtw··.@fle··s.com (Bob Wolfe)
wrote:

› "William M. Klein"  wrote:
› 
…[4 more quoted lines elided]…
›› am not clear what you mean by 80x60 or like PASCAL graphics - but that is
 
› When he says 80 x 60, I believe that he's talking about 800 x 600

First, Thanks for your interest.

I'm sorry, but my English is not as good as I should want...
When I said 'work by 80x60' I mean 80 columns by 60 lines or something
like that, in text-mode.

Is it possible to do it by means of any Standard lib or CALL
statement? If it is not, then how can I do it?

I have read all messages about Flexus, but if they are for
Windows or trial version, I think I may not use them... I'm sorry
again.

My project must be run on MS-DOS, or maybe in Linux if I could
(but I think it will not be possible, I am the only one that knows
Linux in my work-group, and not a lot).
```

###### ↳ ↳ ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

_(reply depth: 4)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6bfc65a9c-p7@usenetarchives.gap>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es> <gap-c6bfc65a9c-p4@usenetarchives.gap> <gap-c6bfc65a9c-p5@usenetarchives.gap> <gap-c6bfc65a9c-p7@usenetarchives.gap>`

```

If you have the Micro Focus compiler and you are interested in text-mode
only screens, then using the Screen Section and the ACCEPT/DISPLAY verbs
should work fine.

As I recall, Micro Focus still defaults to running 80x25 - but does have a
run-time switch that supports more lines per screen.

The ACCEPT/DISPLAY and Screen Section syntax should be in your Language
Reference manual; the run-time switch should be in your user guide.

(If you don't have access to the Micro Focus documentation, then you should
ask your teacher or lab assistant how to get a hold of it.)

Luis wrote in message <34c··.@dia··t.es>...
› On Tue, 27 Jan 1998 13:41:14 GMT, rtw··.@fle··s.com (Bob Wolfe)
› wrote:
…[29 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

_(reply depth: 4)_

- **From:** "john m. saxton, jr." <ua-author-789954@usenetarchives.gap>
- **Date:** 1998-02-01T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6bfc65a9c-p7@usenetarchives.gap>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es> <gap-c6bfc65a9c-p4@usenetarchives.gap> <gap-c6bfc65a9c-p5@usenetarchives.gap> <gap-c6bfc65a9c-p7@usenetarchives.gap>`

```

I used Flexus' tool under DOS. I suspect it is still available. And I thought
they supported UNIX. Don't know about Linux. You would have to check with
Flexus.

Luis wrote:

› On Tue, 27 Jan 1998 13:41:14 GMT, rtw··.@fle··s.com (Bob Wolfe)
› wrote:
…[26 more quoted lines elided]…
› Linux in my work-group, and not  a lot).
```

###### ↳ ↳ ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

_(reply depth: 4)_

- **From:** "red..." <ua-author-9624@usenetarchives.gap>
- **Date:** 1998-02-01T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c6bfc65a9c-p7@usenetarchives.gap>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es> <gap-c6bfc65a9c-p4@usenetarchives.gap> <gap-c6bfc65a9c-p5@usenetarchives.gap> <gap-c6bfc65a9c-p7@usenetarchives.gap>`

```

On Tue, 27 Jan 1998 15:28:16 GMT, ram··.@tel··e.es (Luis) wrote:

› On Tue, 27 Jan 1998 13:41:14 GMT, rtw··.@fle··s.com (Bob Wolfe)
› wrote:
…[19 more quoted lines elided]…
› 

You must use the +C runtime switch with micro focus cobol, and
"somehow" get the screen into the 80x60 mode. Then normal screen
sections will work.

The way to get the screen into 80x60 requires a call to an interrupt -
interrupt 10, with differing modes. I do not know the mode for 80x60,
but you can perhaps find it in the 'standard' interrupt list that
floats around the internet.

A secondary way is to use the MODE command to set the display size.
```

#### ↳ Re: I need some utilities that makes screens works at 60x80 or similar, in COBOL

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-02-02T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c6bfc65a9c-p11@usenetarchives.gap>`
- **In-Reply-To:** `<34ccfec9.2082604@diana.ibernet.es>`
- **References:** `<34ccfec9.2082604@diana.ibernet.es>`

```

Micro Focus COBOL supports 80x50 mode with run-time switch C5. But I
do not know of a switch to invoke 80x60 mode.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)

Luis  wrote:
> Is that possible?
> 
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
