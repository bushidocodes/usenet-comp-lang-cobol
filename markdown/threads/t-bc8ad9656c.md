[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sending a program via e-Mail

_10 messages · 6 participants · 2000-06 → 2000-07_

---

### Sending a program via e-Mail

- **From:** "Billy" <mcduffie95@earthlink.net>
- **Date:** 2000-06-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net>`

```
How do I attach my Proj3.cbl from DOS to an email or is it possible? So far
I have not been able to copy and paste to neither WORD nor NotePad nor just
as a plain e-mail. Any help would be appreciated as I am a first time COBOL
programmer. Thanks in advance.
```

#### ↳ Re: Sending a program via e-Mail

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-06-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KQz65.367$Tp.85920@nnrp3.sbc.net>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net>`

```
Check the Help File for your e-mail program. It's usually as simple as
clicking on the paper-clip and specifying the file name to attach.


Billy <mcduffie95@earthlink.net> wrote in message
news:7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net...
> How do I attach my Proj3.cbl from DOS to an email or is it possible?
So far
> I have not been able to copy and paste to neither WORD nor NotePad
nor just
> as a plain e-mail. Any help would be appreciated as I am a first
time COBOL
> programmer. Thanks in advance.
>
>
>
```

##### ↳ ↳ Cutting and Pasting my COBOL code

- **From:** "Billy" <mcduffie95@earthlink.net>
- **Date:** 2000-06-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net> <KQz65.367$Tp.85920@nnrp3.sbc.net>`

```
Jerry,

I do know how to send an attachment in an E-mail without looking at the HELP
menu. Do you know how to cut and paste the COBOL code to a regular document?
So if I just wanted to send the code to someone who did not have the tools
to open it up using a COBOL compiler in the EDIT mode, then that person
could still look at my code anyway.


"Jerry P" <jerryp@bisusa.com> wrote in message
news:KQz65.367$Tp.85920@nnrp3.sbc.net...
> Check the Help File for your e-mail program. It's usually as simple as
> clicking on the paper-clip and specifying the file name to attach.
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cutting and Pasting my COBOL code

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2000-06-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395B74B4.F6E5C67A@dced.state.ak.us>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net> <KQz65.367$Tp.85920@nnrp3.sbc.net> <TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net>`

```
AFAIK a COBOL source code file is simply a text file (usually with a COB or CBL
extension) and can be opened in any text editor. You would need a COBOL
compiler/editor to apply syntax coloring, find & insert copy files, etc. but the
basic source code should be readable.

Billy wrote:

> Jerry,
>
…[26 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Cutting and Pasting my COBOL code

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-06-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FlT65.75$gB5.65962@nnrp2.sbc.net>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net> <KQz65.367$Tp.85920@nnrp3.sbc.net> <TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net>`

```

Billy <mcduffie95@earthlink.net> wrote in message
news:TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net...
> Jerry,
>
> I do know how to send an attachment in an E-mail without looking at
the HELP
> menu. Do you know how to cut and paste the COBOL code to a regular
document?

Yes, I do. I can think of probably half a dozen. Just for starters:

1. The source code is almost assuredly an ASCII text file (in your
words, "a regular document" it just has a funny extension). Use Word,
Notepad, Wordpad, etc., click Open, click on the file. You may have to
change the browse mask to "*.*"
2. Direct the compiler output listing to a file. That FOR SURE is an
ASCII text file.
3. In the unhappy event that the original is not a uniform text file
(has tabs or other strange characters), the editor has a provision -
almost always - to produce source that is straight ASCII (Realia
editor, for example).
4. Open the editor in a DOS window. Tap [Ctrl]-[PrtScreen]. That puts
the whole thing on the Windows clipboard. From there it may be pasted
virtually anywhere.
5. Write a COBOL program to convert the (assumed bizzare) CBL file to
ASCII text and use that.

I suspect you did not know you can move something from a DOS window
(not full screen) to the Windows clipboard. In which case, your
first-time status with COBOL was not the issue and your question would
be better directed to a Windows (or Unix, or whatever) newsgroup.
```

###### ↳ ↳ ↳ Re: Cutting and Pasting my COBOL code

_(reply depth: 4)_

- **From:** "Billy" <mcduffie95@earthlink.net>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Of175.21780$_b3.462090@newsread1.prod.itd.earthlink.net>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net> <KQz65.367$Tp.85920@nnrp3.sbc.net> <TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net> <FlT65.75$gB5.65962@nnrp2.sbc.net>`

```
Jerry,

This is my first time working and programming with MS-DOS. My first computer
class CIS 2243 did not cover this DOS material as was supposed to. So when
you wrote this:
>
> I suspect you did not know you can move something from a DOS window
…[3 more quoted lines elided]…
>
I suspect that you really don't know who you are talking to and you know
nothing else about me except that I had a question stated in my post. So my
advice to you is to keep your lame insults to yourself. If this wasn't an
insult, I would suggest you think first and type second.

Amy

"Jerry P" <jerryp@bisusa.com> wrote in message
news:FlT65.75$gB5.65962@nnrp2.sbc.net...
>
> Billy <mcduffie95@earthlink.net> wrote in message
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cutting and Pasting my COBOL code

_(reply depth: 5)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jjpid08p7@enews1.newsguy.com>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net> <KQz65.367$Tp.85920@nnrp3.sbc.net> <TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net> <FlT65.75$gB5.65962@nnrp2.sbc.net> <Of175.21780$_b3.462090@newsread1.prod.itd.earthlink.net>`

```
IF (AMY = BILLY)
   THEN
      CALL 'ABORT'.


----------
In article <Of175.21780$_b3.462090@newsread1.prod.itd.earthlink.net>,
"Billy" <mcduffie95@earthlink.net> wrote:


> Jerry,
>
…[55 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cutting and Pasting my COBOL code

_(reply depth: 6)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AKx75.77$g54.86566@nnrp2.sbc.net>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net> <KQz65.367$Tp.85920@nnrp3.sbc.net> <TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net> <FlT65.75$gB5.65962@nnrp2.sbc.net> <Of175.21780$_b3.462090@newsread1.prod.itd.earthlink.net> <8jjpid08p7@enews1.newsguy.com>`

```
You don't think my response was THAT emasculating, do you?

Jeff Baynard <union27@macconnect.com> wrote in message
news:8jjpid08p7@enews1.newsguy.com...
> IF (AMY = BILLY)
>    THEN
>       CALL 'ABORT'.
>
>
```

###### ↳ ↳ ↳ Re: Cutting and Pasting my COBOL code

_(reply depth: 6)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jjv01$nnu$1@sshuraac-i-1.production.compuserve.com>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net> <KQz65.367$Tp.85920@nnrp3.sbc.net> <TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net> <FlT65.75$gB5.65962@nnrp2.sbc.net> <Of175.21780$_b3.462090@newsread1.prod.itd.earthlink.net> <8jjpid08p7@enews1.newsguy.com>`

```
    Let's all add this "Billy" to our twit list.  If you ask a
simple minded
question, you get a simple minded answer.  Don't get upset so
easily.
Many people are unaware that you can cut and paste from a dos
window.



Jeff Baynard <union27@macconnect.com> wrote in message
news:8jjpid08p7@enews1.newsguy.com...
> IF (AMY = BILLY)
>    THEN
…[4 more quoted lines elided]…
> In article
<Of175.21780$_b3.462090@newsread1.prod.itd.earthlink.net>,
> "Billy" <mcduffie95@earthlink.net> wrote:
>
…[3 more quoted lines elided]…
> > This is my first time working and programming with MS-DOS. My
first computer
> > class CIS 2243 did not cover this DOS material as was
supposed to. So when
> > you wrote this:
> >>
> >> I suspect you did not know you can move something from a DOS
window
> >> (not full screen) to the Windows clipboard. In which case,
your
> >> first-time status with COBOL was not the issue and your
question would
> >> be better directed to a Windows (or Unix, or whatever)
newsgroup.
> >>
> > I suspect that you really don't know who you are talking to
and you know
> > nothing else about me except that I had a question stated in
my post. So my
> > advice to you is to keep your lame insults to yourself. If
this wasn't an
> > insult, I would suggest you think first and type second.
> >
…[6 more quoted lines elided]…
> >>
news:TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net...
> >> > Jerry,
> >> >
> >> > I do know how to send an attachment in an E-mail without
looking at
> >> the HELP
> >> > menu. Do you know how to cut and paste the COBOL code to a
regular
> >> document?
> >>
> >> Yes, I do. I can think of probably half a dozen. Just for
starters:
> >>
> >> 1. The source code is almost assuredly an ASCII text file
(in your
> >> words, "a regular document" it just has a funny extension).
Use Word,
> >> Notepad, Wordpad, etc., click Open, click on the file. You
may have to
> >> change the browse mask to "*.*"
> >> 2. Direct the compiler output listing to a file. That FOR
SURE is an
> >> ASCII text file.
> >> 3. In the unhappy event that the original is not a uniform
text file
> >> (has tabs or other strange characters), the editor has a
provision -
> >> almost always - to produce source that is straight ASCII
(Realia
> >> editor, for example).
> >> 4. Open the editor in a DOS window. Tap [Ctrl]-[PrtScreen].
That puts
> >> the whole thing on the Windows clipboard. From there it may
be pasted
> >> virtually anywhere.
> >> 5. Write a COBOL program to convert the (assumed bizzare)
CBL file to
> >> ASCII text and use that.
> >>
> >> I suspect you did not know you can move something from a DOS
window
> >> (not full screen) to the Windows clipboard. In which case,
your
> >> first-time status with COBOL was not the issue and your
question would
> >> be better directed to a Windows (or Unix, or whatever)
newsgroup.
> >>
> >>
…[3 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Cutting and Pasting my COBOL code

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395BE3F4.F6334294@zip.com.au>`
- **References:** `<7_s65.11869$_b3.286417@newsread1.prod.itd.earthlink.net> <KQz65.367$Tp.85920@nnrp3.sbc.net> <TrI65.15384$NP5.361728@newsread2.prod.itd.earthlink.net>`

```
Billy wrote:
> 
> Jerry,
…[5 more quoted lines elided]…
> could still look at my code anyway.

What tools and operating platform are you using.  We can help if we
have more detail.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
