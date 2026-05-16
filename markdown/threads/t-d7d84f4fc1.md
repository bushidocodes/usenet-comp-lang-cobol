[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus "PC_WIN..." routines, any experience of these?

_6 messages · 3 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus "PC_WIN..." routines, any experience of these?

- **From:** grahamr@cix.compulink.co.uk ("Graham Ranson")
- **Date:** 1999-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FBL1zK.Gqt@cix.compulink.co.uk>`

```
Does anyone have experience of using the call-by-name "PC_WIN..." 
routines. We're using COBOL 3.2 (and no support contract at the moment!); 
we've had no problems with using the "CBL_..." routines but when we've 
tried to use any of the "PC_WIN..." routines the system comes up with run 
time error 198, "load failure - usually because of insufficient memory". I 
do not believe that there is any problem with memory!

We are using a built WINDOWS .EXE with called INTs running in WINDOWS 95 
and while we have had no problems with the other "CBL_..." routines all of 
the "PC_WIN..." routines fail in the same way. I cannot really believe 
that it's anything to do with memory but I cam worried about either some 
undocumented environmental consideration or simply a bug in the RTS or 
compiler. It seems more than a coincidence that none of these routines 
seem to work while the others ("CBL_..." ) are fine.

We want to use these routines for proper WINDOWs  printer access, so the 
other approach is some alternative method of accessing WINDOWS printers; 
has anyone tried such an approach?

Graham Ranson
```

#### ↳ Re: MicroFocus "PC_WIN..." routines, any experience of these?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-1tERfVrpoOvd@Dwight_Miller.iix.com>`
- **References:** `<FBL1zK.Gqt@cix.compulink.co.uk>`

```
On Tue, 11 May 1999 19:26:08, grahamr@cix.compulink.co.uk ("Graham 
Ranson") wrote:
> We want to use these routines for proper WINDOWs  printer access, so the 
> other approach is some alternative method of accessing WINDOWS printers; 
> has anyone tried such an approach?
> 

Send me an e-mail - I have just the template you need.  You are 
missing the piece of code where you set the entry point I think.

Also, there are better solutions for Windows printing.  See COBOL Form
Print at http://www.flexus.com.

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: MicroFocus "PC_WIN..." routines, any experience of these?

- **From:** grahamr@cix.compulink.co.uk ("Graham Ranson")
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FBoMpo.G5z@cix.compulink.co.uk>`
- **References:** `<Jl0PnHJ5PvPd-pn2-1tERfVrpoOvd@Dwight_Miller.iix.com>`

```
In article <Jl0PnHJ5PvPd-pn2-1tERfVrpoOvd@Dwight_Miller.iix.com>, 
redsky@ibm.net (Thane Hubbell) wrote:
> Send me an e-mail - I have just the template you need.  You are 
> missing the piece of code where you set the entry point I think.
> 

Thanks ... that worked fine...

Graham Ranson
```

###### ↳ ↳ ↳ Re: MicroFocus "PC_WIN..." routines, any experience of these?

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373B3747.DD21B2AC@IMN.nl>`
- **References:** `<Jl0PnHJ5PvPd-pn2-1tERfVrpoOvd@Dwight_Miller.iix.com> <FBoMpo.G5z@cix.compulink.co.uk>`

```
Graham Ranson wrote:

> In article <Jl0PnHJ5PvPd-pn2-1tERfVrpoOvd@Dwight_Miller.iix.com>,
> redsky@ibm.net (Thane Hubbell) wrote:
…[6 more quoted lines elided]…
> Graham Ranson

Please share this solution in the group, as you did the original
questioning here. I would like to know it too.

The Frog
```

###### ↳ ↳ ↳ Re: MicroFocus "PC_WIN..." routines, any experience of these?

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373e2563.179420002@news1.ibm.net>`
- **References:** `<Jl0PnHJ5PvPd-pn2-1tERfVrpoOvd@Dwight_Miller.iix.com> <FBoMpo.G5z@cix.compulink.co.uk> <373B3747.DD21B2AC@IMN.nl>`

```
On Thu, 13 May 1999 22:34:15 +0200, The COBOL Frog <H.Klink@IMN.nl>
wrote:

>Graham Ranson wrote:
>
…[13 more quoted lines elided]…
>The Frog

       01  Mfprn-Ptr Procedure-Pointer.

       Set Mfprn-Ptr To Entry "mfprnt16"

The the PC_WIN_PRINTER calls work fine with MF 3.2-3.4
```

###### ↳ ↳ ↳ Re: MicroFocus "PC_WIN..." routines, any experience of these?

_(reply depth: 5)_

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37448D24.55EF75D2@IMN.nl>`
- **References:** `<Jl0PnHJ5PvPd-pn2-1tERfVrpoOvd@Dwight_Miller.iix.com> <FBoMpo.G5z@cix.compulink.co.uk> <373B3747.DD21B2AC@IMN.nl> <373e2563.179420002@news1.ibm.net>`

```
Thanks, Thane

Thane Hubbell wrote:

>        01  Mfprn-Ptr Procedure-Pointer.
>
>        Set Mfprn-Ptr To Entry "mfprnt16"
>
> The the PC_WIN_PRINTER calls work fine with MF 3.2-3.4
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
