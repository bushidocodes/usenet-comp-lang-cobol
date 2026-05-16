[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie question

_3 messages · 3 participants · 1999-04_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Newbie question

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7evpde$lbk$1@client2.news.psi.net>`
- **References:** `<_yrQ2.785$Ws1.273625@news3.mia>`

```
lucero@mail.mia.bellsouth.net wrote in message
<_yrQ2.785$Ws1.273625@news3.mia>...
>I called the instructor and he told me that there was an error in the
>code. He is probably right although I've read the code forwards and
>backwards but can't find the error. I'll keep looking for it.

Send me a copy of the code.  If you can, please send me a binary copy
(perhaps by sending it as a ZIPed attachment).  This will help me diagnose
what might be going wrong.

>
>My question is: isn't the compiler supposed to compile the programs as
>they are and then show you how many errors you've made? That's how this
>one used to work.

Yes, this is what should be happening.

>I asked this question to the instructor three times,
>but he never explained this. Any replies you can give me will be
>greately aprecciated.

Sorry that your instructor is not more helpful.

Other possibilities:

The RM/COBOL-85 compiler loads overlays from the A: drive as the program is
being compiled.  This happens when the compiler goes from one DIVISION to
the next, as well as some other, less easily described, times.  Are you sure
that you have not corrupted any of the files named RMCOBOL.* on the
diskette?  Could you compare the files to those of a fellow student to make
sure they are unchanged?  Will the compiler still compile the programs it
previously compiled successfully?

How do you know it is a specific line?  Are you compiling with the listing
going to the screen, or to a file?  If a file, be aware that the compiler
buffers more than one line, so the last line you are seeing in a listing
file merely reflects the last line that was written, not the last line
compiled.

>
>Anna

Tom Morrison
Liant Software Corporation
(and one of the authors of RM/COBOL-85)
```

#### ↳ Re: Newbie question

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3714A057.DE3D0D66@zip.com.au>`
- **References:** `<_yrQ2.785$Ws1.273625@news3.mia> <7evpde$lbk$1@client2.news.psi.net>`

```
Tom Morrison wrote:
> 
> 
…[3 more quoted lines elided]…
> 

I found SYSET on the ETK site which is a minimal precompiler for
COBOL.

Haven't used it but it looks the goods from the examples.

Ken
```

##### ↳ ↳ Re: Newbie question

- **From:** lucero@bellsouthNOSPAM.net
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37156E3E.6F8B@bellsouthNOSPAM.net>`
- **References:** `<_yrQ2.785$Ws1.273625@news3.mia> <7evpde$lbk$1@client2.news.psi.net> <3714A057.DE3D0D66@zip.com.au>`

```
Some newsgroups frown on thank you notes. I hope
I'm not breaking any rules with this post.

Thanks to everyone who replied. I had a chance to read your messages,
but unfortunately I couldn't reply until today.

I found this newsgroup about a week ago and I must say it is very
interesting and informative. A great find for any newbie struggling to
learn without anyone to compare notes with or just talk
about COBOL.

Thank you for sharing your knowdlege and guiding those of us who
have just stated to test the programming waters :)

Anna
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
