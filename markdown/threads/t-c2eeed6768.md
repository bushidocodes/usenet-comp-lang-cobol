[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Menus in dos cobol

_4 messages · 4 participants · 1997-12_

---

### Menus in dos cobol

- **From:** "shai levy" <ua-author-16993123@usenetarchives.gap>
- **Date:** 1997-12-15T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3496E37E.CF532A08@rock.com>`

```

let me rephrase my last question :
is the in any easy way to make scroll bar menus or other friendly gui in
microsoft cobol (dos) - (i know its and old complier... )
sh··.@ro··k.com
```

#### ↳ Re: Menus in dos cobol

- **From:** "g.k.g. van de bovenkamp" <ua-author-6588938@usenetarchives.gap>
- **Date:** 1997-12-15T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2eeed6768-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3496E37E.CF532A08@rock.com>`
- **References:** `<3496E37E.CF532A08@rock.com>`

```

Shai Levy wrote:

› let me rephrase my last question :
› is the in any easy way to make scroll bar menus or other friendly gui in
› microsoft cobol (dos) - (i know its and old complier... )
› sh··.@ro··k.com

Ofcourse that's possible.

Everything can be programmed in COBOL (almost)
As far as I know the only way to do this, is to program it yourself.
It's a lot of work but it's fun to make.

I made a menuprogram with scrollbars and stuff for RM/COBOL-85 and it worked
and still does.

Success

Bert.
( REMOVE 'NOSPAM' BEFORE REPLYING )
\\\---///
\\ ~ ~ //
(| @ _ @ |)
____________oOOo__|__(_)__|__oOOo___________
____| Whatever you do, Just Hang On |_____
\ | | /
\ | http://www1.tip.nl/~t178377/index.htm | /
] | Oooo. | [
/ |________________.oooO___( )_______________| \
/_______) ( ) | / (________\
\ | (__)
(__)
```

#### ↳ Re: Menus in dos cobol

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1997-12-16T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2eeed6768-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3496E37E.CF532A08@rock.com>`
- **References:** `<3496E37E.CF532A08@rock.com>`

```

Shai Levy wrote:

› let me rephrase my last question :
› is the in any easy way to make scroll bar menus or other friendly gui in
…[4 more quoted lines elided]…
› 

Shai:

You should distinguish between "scroll bars" which are those bars at
the right side and bottom which allow you to view a screen which is
larger than the displayable area and "menu bars" which is the row of
textual options at the top of a screen allowing you to navigate
through an application by selecting from the various options.

When you say "friendly GUI" in Microsoft COBOL (DOS) do you mean
native MS-DOS without Windows running at all? If that's the case,
then the only way to accomplish this is to either write low level
graphic display routines to display bitmap based screens in native DOS
or buy some 3rd party tool that accomplishes this.

There used to be a COBOL screen handler called Hi Screen XL which did
allow you to build graphical screens in regular DOS. I believe that
the product is no longer sold.

But, if you mean "Windows (dos)" then you have a few options, but you
have to check the version of your compiler first. I believe that
Microsoft COBOL version 3, 4, 4.5 and 5 all support the ability to
build GUI screens (menus included) in 16 bit Windows (Windows
3.1/3.11). This is an older version of the Micro Focus COBOL compiler
which was licensed to Microsoft. If you have the older Microsoft
COBOL compiler (version 2.x), then you are out of luck if you want to
run in Windows. It only supported DOS and XENIX.

1. You can buy the Microsoft SDK (Software Developer's Kit) and embed
native Windows API CALLs in your COBOL.

2. You can obtain a 3rd party GUI screen tool which supports
Microsoft COBOL version 3 through version 5.

If you want to discuss this with me off line, I would be happy to
assist you. Just send an e-mail to my e-mail address below and we can
sort out the details instead of clogging up the newsgroup. Please
make sure that you correct my e-mail address before sending the
mailing out. Our COBOL sp2 product does support the ability to run
character mode DOS screens (with menu bars and pull down menus) as
well as 16 bit and 32 bit Windows GUI screens (with menu bars and pull
down menus) using the same source program and the same screen
definitions.


Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: Menus in dos cobol

- **From:** "john m. saxton, jr." <ua-author-789954@usenetarchives.gap>
- **Date:** 1997-12-16T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2eeed6768-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3496E37E.CF532A08@rock.com>`
- **References:** `<3496E37E.CF532A08@rock.com>`

```

You might check out http://www.flexus.com. They have a tool that is more or
less a screen painter. You use it to create a screen image and standard
COBOL CALLS to call a Flexus runtime to display the screen.

Regards... John Saxton

Shai Levy wrote:

› let me rephrase my last question :
› is the in any easy way to make scroll bar menus or other friendly gui in
› microsoft cobol (dos) - (i know its and old complier... )
› sh··.@ro··k.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
