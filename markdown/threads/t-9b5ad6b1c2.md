[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microsoft Cobol Workbench 3.2.50 & Fujitsu Cobol 4

_6 messages · 3 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microsoft Cobol Workbench 3.2.50 & Fujitsu Cobol 4

- **From:** "Alms" <alms@a1plus.at>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<925822252.69351@proxy.styria.com>`

```
Hi there!

Is there any chance to move from MFC Workbench 3.250 (16Bit) and Dialog
System
to Fujitsu Cobol 4.

The Destination-Environment is Win95/98 and WinNT ... the Application should
run in 32Bit ... not in the lame 16Bit-Cobol who nearly frezzes WinNT & Co.

My special Questions:

 - Can i convert the Dialog System-Screens from MF to Fujitsu ?

 - Does any one know why MFC Runtime takes so much advantage on the
   CPU-Power on Win95/98 and specialy on WinNT??

 - Is there a possibility of changing Dialog System-Screens to Visual Basic
or
   to run it from Visual Basic (Version 5 or 6) ??


Thanx for all your help

:-)
A. Ledineg
```

#### ↳ Re: Microsoft Cobol Workbench 3.2.50 & Fujitsu Cobol 4

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-JodhVcnkeJ67@Dwight_Miller.iix.com>`
- **References:** `<925822252.69351@proxy.styria.com>`

```
On Tue, 4 May 1999 12:44:05, "Alms" <alms@a1plus.at> wrote:

> Hi there!
> 
…[10 more quoted lines elided]…
> 

Total rewrite.  MF panels and Fujitsu Forms are incompatible.  "Dialog
code" behind objects will have to be converted to COBOL - which is the
scripting language used by Fujitsu.  Also, your "separate" application
program goes away.

This is the DANGER involved with using any vendor specific tools or 
extensions.  It makes it virtually impossible to make an economic move
to another compiler.  If you had used a third party tool, such as 
COBOL sp2 you would be able to change compilers easily - including 
moving from 16 to 32 bit.

>  - Does any one know why MFC Runtime takes so much advantage on the
>    CPU-Power on Win95/98 and specialy on WinNT??
> 

Dunno.

>  - Is there a possibility of changing Dialog System-Screens to Visual Basic
> or
>    to run it from Visual Basic (Version 5 or 6) ??
> 

Same issues as moving to PowerCOBOL


-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Microsoft Cobol Workbench 3.2.50 & Fujitsu Cobol 4

- **From:** "Alms" <alms@a1plus.at>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<925828363.160317@proxy.styria.com>`
- **References:** `<925822252.69351@proxy.styria.com> <Jl0PnHJ5PvPd-pn2-JodhVcnkeJ67@Dwight_Miller.iix.com>`

```
> This is the DANGER involved with using any vendor specific tools or
> extensions.  It makes it virtually impossible to make an economic move
> to another compiler.  If you had used a third party tool, such as
> COBOL sp2 you would be able to change compilers easily - including
> moving from 16 to 32 bit.

What is Cobol sp2 ... is it from Fujitsu, if it is, how good is Fujitsu
Cobol 4


> Same issues as moving to PowerCOBOL

PowerCOBOL (from which Vendor?)

:)
A. Ledineg
```

###### ↳ ↳ ↳ Re: Microsoft Cobol Workbench 3.2.50 & Fujitsu Cobol 4

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<372f244a.1784795@news.enter.net>`
- **References:** `<925822252.69351@proxy.styria.com> <Jl0PnHJ5PvPd-pn2-JodhVcnkeJ67@Dwight_Miller.iix.com> <925828363.160317@proxy.styria.com>`

```
"Alms" <alms@a1plus.at> wrote:

>> This is the DANGER involved with using any vendor specific tools or
>> extensions.  It makes it virtually impossible to make an economic move
…[5 more quoted lines elided]…
>Cobol 4

Alms:

No.  COBOL sp2 is from flexus.  Visit www.flexus.com.

>> Same issues as moving to PowerCOBOL
>
>PowerCOBOL (from which Vendor?)

PowerCOBOL is the Fujitsu COBOL GUI development tool.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Microsoft Cobol Workbench 3.2.50 & Fujitsu Cobol 4

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-F4dUVsbKff2q@Dwight_Miller.iix.com>`
- **References:** `<925822252.69351@proxy.styria.com> <Jl0PnHJ5PvPd-pn2-JodhVcnkeJ67@Dwight_Miller.iix.com> <925828363.160317@proxy.styria.com>`

```
On Tue, 4 May 1999 14:32:17, "Alms" <alms@a1plus.at> wrote:

> > This is the DANGER involved with using any vendor specific tools or
> > extensions.  It makes it virtually impossible to make an economic move
…[6 more quoted lines elided]…
> 

Sp2 is from Flexus - http://www.flexus.com and is independant of the 
compiler - it works with virtually any PC or UNIX COBOL.

Fujitsu v4.2 is a great compiler.

> 
> > Same issues as moving to PowerCOBOL
> 
> PowerCOBOL (from which Vendor?)
> 

PowerCOBOL is a Fujitsu product.

> :)
> A. Ledineg
> 
> 
> 

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Microsoft Cobol Workbench 3.2.50 & Fujitsu Cobol 4

- **From:** "Alms" <alms@a1plus.at>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<925827913.227683@proxy.styria.com>`
- **References:** `<925822252.69351@proxy.styria.com>`

```
Ups!

Sorry ... I mean Microfocus Cobol Workbench 3.2.50
and not Microsoft .

:-)
A. Ledineg
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
