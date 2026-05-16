[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem w/ Fujitsu COBOL

_5 messages · 2 participants · 2003-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Problem w/ Fujitsu COBOL

- **From:** Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com>
- **Date:** 2003-01-29T17:56:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E385C05.8A4DE9BC@ix.netcom.com>`

```
I am attempting to use WINEXEC's HELP function. It is
complaining about being missing f3biprhj.hlp. I haven't been
able to find it on the CD. Anyone got any clues about this,
or have the sucker?
```

#### ↳ Re: Problem w/ Fujitsu COBOL

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-01-29T18:59:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E389505.4000800@Sympatico.ca>`
- **References:** `<3E385C05.8A4DE9BC@ix.netcom.com>`

```
 From the file name, I would guess that it is actually a fujitsu runtime 
routine that you are using for the first time, and it has nothing to do 
at all with help.  Could you be looking on the wrong CD?

Donald


Steve Thompson wrote:
> I am attempting to use WINEXEC's HELP function. It is
> complaining about being missing f3biprhj.hlp. I haven't been
…[12 more quoted lines elided]…
> attorney's fees) for collecting this fee.
```

##### ↳ ↳ Re: Problem w/ Fujitsu COBOL

- **From:** Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com>
- **Date:** 2003-01-29T21:47:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E38922A.41578289@ix.netcom.com>`
- **References:** `<3E385C05.8A4DE9BC@ix.netcom.com> <3E389505.4000800@Sympatico.ca>`

```
Donald Tees wrote:
> 
>  From the file name, I would guess that it is actually a fujitsu runtime
> routine that you are using for the first time, and it has nothing to do
> at all with help.  Could you be looking on the wrong CD?
> 
<snip>

With an extension of "hlp" I would have thought it a help
file. And what makes me really think that is I had just hit
the <HELP> key on the WINEXEC panel. At this point, I'm not
trying to execute one of my programs, but testing to see if
I can build the CBR file using a panel (rather than by hand
as I've been doing all along).

Meanwhile, I have 1 CD. And I also have V5's CD and can't
find a similarly named HELP file there either.
```

###### ↳ ↳ ↳ Re: Problem w/ Fujitsu COBOL

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-01-29T22:10:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E38C1DF.8060908@Sympatico.ca>`
- **References:** `<3E385C05.8A4DE9BC@ix.netcom.com> <3E389505.4000800@Sympatico.ca> <3E38922A.41578289@ix.netcom.com>`

```
Steve Thompson wrote:
> Donald Tees wrote:
> 
…[16 more quoted lines elided]…
> 

Well, ok, but the version of fuijitsu that I have installed has a file 
named F3BIPRHE.hlp. A one letter difference seems somewhat suspicious, 
and you may be running a different version than me. Perhaps I was not 
clear.  Did you look on your Fujitsu CD?
```

###### ↳ ↳ ↳ Re: Problem w/ Fujitsu COBOL

_(reply depth: 4)_

- **From:** Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com>
- **Date:** 2003-01-30T10:53:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E394A64.199BBDF4@ix.netcom.com>`
- **References:** `<3E385C05.8A4DE9BC@ix.netcom.com> <3E389505.4000800@Sympatico.ca> <3E38922A.41578289@ix.netcom.com> <3E38C1DF.8060908@Sympatico.ca>`

```
Donald Tees wrote:
<snip>
> Well, ok, but the version of fuijitsu that I have installed has a file
> named F3BIPRHE.hlp. A one letter difference seems somewhat suspicious,
> and you may be running a different version than me. Perhaps I was not
> clear.  Did you look on your Fujitsu CD?

Yes, I've looked on the CD. And what you have observed is
exactly my observation, and in fact, that particular help
file contains *EXACTLY* what I was looking for, so there
appears to be a bug in the install (someone finger checked
when they built this).

If only I knew enough about the Wintel architecture, I'd
write a version of AMASPZAP for it and fix the sucker
myself.... (grumble grumble).

Well, back to writing more of my code generator...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
