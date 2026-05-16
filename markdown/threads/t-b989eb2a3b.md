[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus PC_WIN_SET_PDEFAULT Runtime Abort

_7 messages · 4 participants · 1999-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus PC_WIN_SET_PDEFAULT Runtime Abort

- **From:** dblaze@merchants-fla.com (Doug Blaze)
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376a4fcf.4256059@news.icix.net>`

```
Hello all,

I'm running MF 4.0.32 and using the PC_WIN_SET_PDEFAULT to set the
default printer.  I have the name of the printer in an INI file.  I'm
checking the return code on the call to detect if there is a problem.
However, if the user changes printers and the name in the INI file no
longer exists, the program aborts with: 

error code: 114, pc=0, call=1, seg=0
114 Attempt to access item beyond bounds of memory (Signal 11)

In other words, I don't a chance to detect the problem before the
program aborts.  Is there a compiler option or something else I need
to specify in order to trap runtime errors so I can deal with them
programmatically?

Thanks,
Doug Blaze
```

#### ↳ Re: MicroFocus PC_WIN_SET_PDEFAULT Runtime Abort

- **From:** "David Sands" <davs@mfltd.co.uk>
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kdt39$9f1$1@hyperion.mfltd.co.uk>`
- **References:** `<376a4fcf.4256059@news.icix.net>`

```
Hi Doug,

There is a Win32 api call "EnumPrinters" that will return details on the
printers defined to the system. You check the INI file definitions against
the details from the API call and deal with it according.

You could also look at CBL_ERROR_PROC which allows you to trap the RTS
Errors.

Hope this helps.
David.


Doug Blaze wrote in message <376a4fcf.4256059@news.icix.net>...
>Hello all,
>
…[15 more quoted lines elided]…
>Doug Blaze
```

#### ↳ Re: MicroFocus PC_WIN_SET_PDEFAULT Runtime Abort

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-tnH8zM8Ld8Hn@Dwight_Miller.iix.com>`
- **References:** `<376a4fcf.4256059@news.icix.net>`

```
Doug,

You are missing the entry point in working storage that is necessary 
along with the SET to set the addres of "mfwinp32" (that might be 
wrong, but it's cose) to that entry point.  Get those in there and 
it'll work.  Read PRINT.DOC in the docs directory and it'll explain 
it.

On Fri, 18 Jun 1999 14:07:53, dblaze@merchants-fla.com (Doug Blaze) 
wrote:

> Hello all,
> 
…[15 more quoted lines elided]…
> Doug Blaze

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: MicroFocus PC_WIN_SET_PDEFAULT Runtime Abort

- **From:** dblaze@merchants-fla.com (Doug Blaze)
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376a933b.21515898@news.icix.net>`
- **References:** `<376a4fcf.4256059@news.icix.net> <Jl0PnHJ5PvPd-pn2-tnH8zM8Ld8Hn@Dwight_Miller.iix.com>`

```
Hi Thane,

Sorry, but no joy.  The only PRINT.TXT file I can find is in 16-bit
version, not the 32-bit that I'm using.  However, I followed the
sample in the PRINT.TXT file and still get the 114 RTS.  It made no
difference if I did the SET MFPRN-PTR TO ENTRY "MFPRNT32" as the first
statement in the Procedure Division or just before I tried to use the
PC_WIN_SET_PDEFAULT call.

Any other ideas?

Doug

>Doug,
>
…[36 more quoted lines elided]…
>http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MicroFocus PC_WIN_SET_PDEFAULT Runtime Abort

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-XkihYkdMzwyg@Dwight_Miller.iix.com>`
- **References:** `<376a4fcf.4256059@news.icix.net> <Jl0PnHJ5PvPd-pn2-tnH8zM8Ld8Hn@Dwight_Miller.iix.com> <376a933b.21515898@news.icix.net>`

```
On Fri, 18 Jun 1999 18:52:58, dblaze@merchants-fla.com (Doug Blaze) 
wrote:

> Hi Thane,
> 
…[5 more quoted lines elided]…
> PC_WIN_SET_PDEFAULT call.

Make sure MFPRN-PTR is usage pointer. (I'm sure it is) The Entry point
is the only thing I know of for sure that causes the 114 right away.  
If it's not that, I'm at a loss as to the cause.

Sorry :(
-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: MicroFocus PC_WIN_SET_PDEFAULT Runtime Abort

_(reply depth: 4)_

- **From:** "Simon Hart" <hart1@technologist.com>
- **Date:** 1999-06-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ziya3.1193$BS6.570@wards>`
- **References:** `<376a4fcf.4256059@news.icix.net> <Jl0PnHJ5PvPd-pn2-tnH8zM8Ld8Hn@Dwight_Miller.iix.com> <376a933b.21515898@news.icix.net> <Jl0PnHJ5PvPd-pn2-XkihYkdMzwyg@Dwight_Miller.iix.com>`

```

Thane Hubbell <redsky@ibm.net> wrote in message
news:Jl0PnHJ5PvPd-pn2-XkihYkdMzwyg@Dwight_Miller.iix.com...
> On Fri, 18 Jun 1999 18:52:58, dblaze@merchants-fla.com (Doug Blaze)
> wrote:
…[12 more quoted lines elided]…
> If it's not that, I'm at a loss as to the cause.

I've had this problem only with the PC_PRINT_FILE lib routine, and it drove
me nuts,
post your code, for the whole module call.

Simon Hart.
```

#### ↳ Re: MicroFocus PC_WIN_SET_PDEFAULT Runtime Abort

- **From:** dblaze@merchants-fla.com (Doug Blaze)
- **Date:** 1999-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37722c3b.519027792@news.icix.net>`
- **References:** `<376a4fcf.4256059@news.icix.net>`

```
Hello All,

Sorry to be so late posting the code for my problem, but fires will
burn!

Here's the code:

    move spaces to prt-printer-name.
    String IF-PrinterNameValue delimited by "  ", x"00"
        delimited by size into prt-printer-name.
    Call "PC_WIN_SET_PDEFAULT" using
        by reference prt-printer-name
        returning return-code
    End-Call.
    If return-code not = 0
        Perform Printer-Error
        go to print-reports-exit
    End-If.

I'm getting the 114 RTS abort and never getting a chance to check the
return-code value.  If you want to try to replicate the situation,
provide a name in 'prt-printer-name' that doesn't exist on your system
(ie:  'My Printer').  Then try the same call with a valid printer name
(ie: the EXACT name that appears when the printer dialog is invoked in
Windows).  It will work. I don't want the program to abort with the
RTS but allow me to handle my error routine.  I have to assume I don't
have a compiler option/directive set that would allow me to do this.

Thanks,
Doug Blaze






dblaze@merchants-fla.com (Doug Blaze) wrote:

>Hello all,
>
…[15 more quoted lines elided]…
>Doug Blaze
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
