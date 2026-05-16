[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PCL codes

_7 messages · 4 participants · 2001-05_

---

### PCL codes

- **From:** Stefan Schneck <Schneck_Stefan@Poerringer.de>
- **Date:** 2001-05-17T08:45:18+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B03737E.236BFED9@Poerringer.de>`

```
Hello !

Thankyou very much for your help with the PCL codes.

It is a little bit difficult for me, because these are my first
steps in that kind of "printer-programming".

I just tried to do it that way:

STRING x'1B28733342' "Test" DELIMITED BY SIZE INTO LINE
WRITE LINE AFTER 1

But that does not work :-(((

Maybe your code for parsing print lines could help me ?

Any other / better ;-))) ideas ?

Thanks a lot
Stefan
```

#### ↳ Re: PCL codes

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-05-17T15:30:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010517113043.21890.00000818@nso-cq.aol.com>`
- **References:** `<3B03737E.236BFED9@Poerringer.de>`

```
In article <3B03737E.236BFED9@Poerringer.de>, Stefan Schneck
<Schneck_Stefan@Poerringer.de> writes:

>
>I just tried to do it that way:
…[5 more quoted lines elided]…
>

Are you doing this is a Windows environment or DOS?
For some reason, I vaguely recall that in the Windows environment
Escape Sequences have a tendency to be stripped from whatever 
messaging is sent to the printer.
I may be entirely off-base on this, but it might be worth scanning the 
old messages about sending ESC codes to the printer.
```

##### ↳ ↳ Re: PCL codes

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-05-18T02:21:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e1pkp$jo0$1@news8.svr.pol.co.uk>`
- **References:** `<3B03737E.236BFED9@Poerringer.de> <20010517113043.21890.00000818@nso-cq.aol.com>`

```
I don't have any problems printing from my dos program under
windows-whatever
using raw or emf. I could be wrong (probably am) but isnt this how windows
internally
handles the print job with the end result being the same for raw/emf ?

"Sff5ky" <sff5ky@aol.comxxx123> wrote in message
news:20010517113043.21890.00000818@nso-cq.aol.com...
> In article <3B03737E.236BFED9@Poerringer.de>, Stefan Schneck
> <Schneck_Stefan@Poerringer.de> writes:
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: PCL codes

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2001-05-18T09:09:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8vl9gtc633ivd3vdo35id31ed7r9kdiuqt@4ax.com>`
- **References:** `<3B03737E.236BFED9@Poerringer.de> <20010517113043.21890.00000818@nso-cq.aol.com> <9e1pkp$jo0$1@news8.svr.pol.co.uk>`

```
If you use the Windows Spooler then it matters (and if you are using
networked printers in a Windows network you will most probably be
using it).
If you are printing directly to LPTx then it doesn't.

Best

FF

On Fri, 18 May 2001 02:21:24 +0100, "Alister Munro"
<alister@specsoft.freeserve.co.uk> wrote:

>I don't have any problems printing from my dos program under
>windows-whatever
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: PCL codes

_(reply depth: 4)_

- **From:** Stefan Schneck <Schneck_Stefan@Poerringer.de>
- **Date:** 2001-05-18T11:15:07+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B04E81B.9BE55C70@Poerringer.de>`
- **References:** `<3B03737E.236BFED9@Poerringer.de> <20010517113043.21890.00000818@nso-cq.aol.com> <9e1pkp$jo0$1@news8.svr.pol.co.uk> <8vl9gtc633ivd3vdo35id31ed7r9kdiuqt@4ax.com>`

```
Hello,

my "environment" is:

COBOL 85 on BULL GCOS 7 (hardware and operating system),
platform workstation is MS Windows 98, novell network 4.11.

Editing a file in DOS-mode and printing is OK, but ...

Any suggestions ? 

PLEASE HELP ME - WEEKEND IS COMING AND I AM GETTING NERVOUS OF MY
PROBLEM ;-)))))

Greetings and a nice weekend to everybody 
Stefan

PS. I have tried the UEL-Commands, ESC%-12345X and ESCE and ....
it does not work :-((


Frederico Fonseca schrieb:
> 
> If you use the Windows Spooler then it matters (and if you are using
…[38 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: PCL codes

_(reply depth: 5)_

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-05-18T21:52:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e3u7v$o0p$1@newsg1.svr.pol.co.uk>`
- **References:** `<3B03737E.236BFED9@Poerringer.de> <20010517113043.21890.00000818@nso-cq.aol.com> <9e1pkp$jo0$1@news8.svr.pol.co.uk> <8vl9gtc633ivd3vdo35id31ed7r9kdiuqt@4ax.com> <3B04E81B.9BE55C70@Poerringer.de>`

```
Why not try printing to a disk file rather than to the printer and then
check
the output against what you coded. Could be that Cobol is converting
some of the control sequences. Post one of your test programs and I'll
see what I get on my MF WB / HP combo.

"Stefan Schneck" <Schneck_Stefan@Poerringer.de> wrote in message
news:3B04E81B.9BE55C70@Poerringer.de...
> Hello,
>
…[35 more quoted lines elided]…
> > >using raw or emf. I could be wrong (probably am) but isnt this how
windows
> > >internally
> > >handles the print job with the end result being the same for raw/emf ?
…[19 more quoted lines elided]…
> > >> I may be entirely off-base on this, but it might be worth scanning
the
> > >> old messages about sending ESC codes to the printer.
> > >>
> > >
```

#### ↳ Re: PCL codes

- **From:** Stefan Schneck <Schneck_Stefan@Poerringer.de>
- **Date:** 2001-05-22T16:10:48+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0A7368.1F2C1024@Poerringer.de>`
- **References:** `<3B03737E.236BFED9@Poerringer.de>`

```
Hello,

sun is shining in germany ;-)))

I just want to say THANKYOU - for all your advices and help !!

I am still working on it, but I will find the solution.

Seems like the way "pc -> host (BULL) -> pc (windows)" does not work
as it should. I will write when I am OK with that.

Very much greetings
Stefan

PS. It is really fantastic - all your help !!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
