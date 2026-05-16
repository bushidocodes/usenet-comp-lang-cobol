[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question regarding WIN32 API PrintDlg

_11 messages · 6 participants · 2000-01_

---

### Question regarding WIN32 API PrintDlg

- **From:** Chris T. <ctaliercio@my-deja.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85i7io$4qd$1@nnrp1.deja.com>`

```
I am using the WIN32 "PrintDlg" API call to display a print dialog box
for the user. The structure that is passed to this routine is:

01  PRINT-DLG.
    05  lStructSize             PIC  X(04)  COMP-5.
    05  hwndOwner               PIC  X(04)  COMP-5.
    05  hDevMode                PIC  X(04)  COMP-5.
    05  hDevNames               PIC  X(04)  COMP-5.
    05  hDC                     PIC  X(04)  COMP-5.
    05  Flags                   PIC  X(04)  COMP-5.
    05  nFromPage               PIC  X(02)  COMP-5.
    05  nToPage                 PIC  X(02)  COMP-5.
    05  nMinPage                PIC  X(02)  COMP-5.
    05  nMaxPage                PIC  X(02)  COMP-5.
    05  nCopies                 PIC  X(02)  COMP-5.
    05  hInstance               PIC  X(04)  COMP-5.
    05  lCustData               PIC  X(04)  COMP-5.
    05  lpfnPrintHook           POINTER.
    05  lpfnSetupHook           POINTER.
    05  lpPrintTemplateName     POINTER.
    05  lpSetupTemplateName     POINTER.
    05  hPrintTemplate          PIC  X(04)  COMP-5.
    05  hSetupTemplate          PIC  X(04)  COMP-5.

On return from the API call, the hDevMode and hDevNames contain handles
to other structures which contain all of the information the user
selected in the Print Dailog box.

I am NOT using object COBOL, so my question is this:

Is there a way to set the address of the DEVMODE and DEVNAME structures
I have defined in my program based upon the returned handle?

Any help would be greatly appreciated.

Thanks! - Chris


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Question regarding WIN32 API PrintDlg

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85ifuc$hkh$1@hyperion.mfltd.co.uk>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com>`

```
Chris,

Yes, you can do this. You need to define the DEVMODE and DEVNAMES structures
in LINKAGE SECTION and then SET ADDRESS OF DEVMODE to <pointer>. I can't
remember offhand whether you can define hDevNames as a pointer and do it
directly or whether you need to call the GlobalLock API and get a pointer
back (the latter would be safer though), but that should be all you will
need to do.

The same principle can be used for any API that returns a pointer to a
structure.

Chris T. wrote in message <85i7io$4qd$1@nnrp1.deja.com>...
>I am using the WIN32 "PrintDlg" API call to display a print dialog box
>for the user. The structure that is passed to this routine is:
…[37 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: Question regarding WIN32 API PrintDlg

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85j5fd$a71$1@nntp8.atl.mindspring.net>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com> <85ifuc$hkh$1@hyperion.mfltd.co.uk>`

```
> The same principle can be used for any API that returns a pointer to a
structure.>

This is not always the case....

Ensure that you know the length of the data returned and globally allocated
by an api call...If not defined properly, you will abend...For example
getting data from the clipboard returns such a pointer to a null terminated
string...But since you do not know the length, you can only reference it one
byte at a time...treat it as an array of one byte elements, bumping the
index until you get to the null...MF cobol will abend with a 114 if it
thinks the length is more than what is actually there...

kenmullins
```

###### ↳ ↳ ↳ Re: Question regarding WIN32 API PrintDlg

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iyaf4.32756$g12.975855@news2.rdc1.on.home.com>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com> <85ifuc$hkh$1@hyperion.mfltd.co.uk> <85j5fd$a71$1@nntp8.atl.mindspring.net>`

```

"Ken Mullins" <KenMullins@mindspring.com> wrote in message
news:85j5fd$a71$1@nntp8.atl.mindspring.net...
> > The same principle can be used for any API that returns a pointer to a
> structure.>
…[3 more quoted lines elided]…
> Ensure that you know the length of the data returned and globally
allocated
> by an api call...If not defined properly, you will abend...For example
> getting data from the clipboard returns such a pointer to a null
terminated
> string...But since you do not know the length, you can only reference it
one
> byte at a time...treat it as an array of one byte elements, bumping the
> index until you get to the null...MF cobol will abend with a 114 if it
> thinks the length is more than what is actually there...
>
> kenmullins

There are easier ways to deal with it than coding a loop. Try:

1) INSPECT my-var TALLYING x FOR ALL CHARACTERS BEFORE INITIAL LOW-VALUE
then using a reference modified move.

2) UNSTRING my-var DELIMITED LOW-VALUE. INTO ...

- Karl Wagner
```

###### ↳ ↳ ↳ Re: Question regarding WIN32 API PrintDlg

_(reply depth: 4)_

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85jl3f$e3s$1@nntp2.atl.mindspring.net>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com> <85ifuc$hkh$1@hyperion.mfltd.co.uk> <85j5fd$a71$1@nntp8.atl.mindspring.net> <iyaf4.32756$g12.975855@news2.rdc1.on.home.com>`

```
How big do you define my-var to be when you don't know how big of an area
the API is going to return???...Seems like I remember defining an area that
would be more than enough for what I was concerned with...Problem is, MF
abended with a 114 when referencing my-var if it was bigger than the actual
data returned...Even though my-var was in the linkage section...The only way
I could do it was to code it as a one byte element in an array, and
reference it one byte at a time...

kenmullins


Oscar T. Grouch <dustbin@home.com> wrote in message
news:iyaf4.32756$g12.975855@news2.rdc1.on.home.com...
>
> "Ken Mullins" <KenMullins@mindspring.com> wrote in message
…[28 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Question regarding WIN32 API PrintDlg

_(reply depth: 5)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vinf4.34352$g12.1035820@news2.rdc1.on.home.com>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com> <85ifuc$hkh$1@hyperion.mfltd.co.uk> <85j5fd$a71$1@nntp8.atl.mindspring.net> <iyaf4.32756$g12.975855@news2.rdc1.on.home.com> <85jl3f$e3s$1@nntp2.atl.mindspring.net>`

```
Don't reference my-var. Reference my-var(1:len), where 'len' is determined
using either an INSPECT or by length information returned by the API. When
you reference my-var there is a risk of a 114 when you get beyond the
low-value.

Another trick is to use an 'OCCURS DEPENDING ON len' in the linkage
definition. It's not too different from what you're probably already doing
byte-at-a-time but once you've established the value of 'len' you can
reference my-var safely.

Karl Wagner

"Ken Mullins" <KenMullins@mindspring.com> wrote in message
news:85jl3f$e3s$1@nntp2.atl.mindspring.net...
> How big do you define my-var to be when you don't know how big of an area
> the API is going to return???...Seems like I remember defining an area
that
> would be more than enough for what I was concerned with...Problem is, MF
> abended with a 114 when referencing my-var if it was bigger than the
actual
> data returned...Even though my-var was in the linkage section...The only
way
> I could do it was to code it as a one byte element in an array, and
> reference it one byte at a time...
…[9 more quoted lines elided]…
> > > > The same principle can be used for any API that returns a pointer to
a
> > > structure.>
> > >
…[7 more quoted lines elided]…
> > > string...But since you do not know the length, you can only reference
it
> > one
> > > byte at a time...treat it as an array of one byte elements, bumping
the
> > > index until you get to the null...MF cobol will abend with a 114 if it
> > > thinks the length is more than what is actually there...
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Question regarding WIN32 API PrintDlg

_(reply depth: 6)_

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85oe27$tof$1@nntp9.atl.mindspring.net>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com> <85ifuc$hkh$1@hyperion.mfltd.co.uk> <85j5fd$a71$1@nntp8.atl.mindspring.net> <iyaf4.32756$g12.975855@news2.rdc1.on.home.com> <85jl3f$e3s$1@nntp2.atl.mindspring.net> <vinf4.34352$g12.1035820@news2.rdc1.on.home.com>`

```
you have to reference my-var for the inspect verb, right? and it would need
an implied length (i.e., the length of the pic clause)??? I  will try and go
back and see if this works, but if the defined length of my-var is greater
than the actual data returned (since the api call does not return a length),
it will probably 114 also...But I will check it out and see...

thanks

kenmullins

Oscar T. Grouch <dustbin@home.com> wrote in message
news:vinf4.34352$g12.1035820@news2.rdc1.on.home.com...
> Don't reference my-var. Reference my-var(1:len), where 'len' is determined
> using either an INSPECT or by length information returned by the API. When
…[12 more quoted lines elided]…
> > How big do you define my-var to be when you don't know how big of an
area
> > the API is going to return???...Seems like I remember defining an area
> that
…[16 more quoted lines elided]…
> > > > > The same principle can be used for any API that returns a pointer
to
> a
> > > > structure.>
…[5 more quoted lines elided]…
> > > > by an api call...If not defined properly, you will abend...For
example
> > > > getting data from the clipboard returns such a pointer to a null
> > > terminated
> > > > string...But since you do not know the length, you can only
reference
> it
> > > one
> > > > byte at a time...treat it as an array of one byte elements, bumping
> the
> > > > index until you get to the null...MF cobol will abend with a 114 if
it
> > > > thinks the length is more than what is actually there...
> > > >
…[4 more quoted lines elided]…
> > > 1) INSPECT my-var TALLYING x FOR ALL CHARACTERS BEFORE INITIAL
LOW-VALUE
> > > then using a reference modified move.
> > >
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Question regarding WIN32 API PrintDlg

_(reply depth: 7)_

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85oet4$aib$1@nntp9.atl.mindspring.net>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com> <85ifuc$hkh$1@hyperion.mfltd.co.uk> <85j5fd$a71$1@nntp8.atl.mindspring.net> <iyaf4.32756$g12.975855@news2.rdc1.on.home.com> <85jl3f$e3s$1@nntp2.atl.mindspring.net> <vinf4.34352$g12.1035820@news2.rdc1.on.home.com> <85oe27$tof$1@nntp9.atl.mindspring.net>`

```
Tried it, and you ARE CORRECT sir...worked fine...Much appreciated...much
better than referencing one byte at a time...

Thanks again

kenmullins

Ken Mullins <KenMullins@mindspring.com> wrote in message
news:85oe27$tof$1@nntp9.atl.mindspring.net...
> you have to reference my-var for the inspect verb, right? and it would
need
> an implied length (i.e., the length of the pic clause)??? I  will try and
go
> back and see if this works, but if the defined length of my-var is greater
> than the actual data returned (since the api call does not return a
length),
> it will probably 114 also...But I will check it out and see...
>
…[6 more quoted lines elided]…
> > Don't reference my-var. Reference my-var(1:len), where 'len' is
determined
> > using either an INSPECT or by length information returned by the API.
When
> > you reference my-var there is a risk of a 114 when you get beyond the
> > low-value.
> >
> > Another trick is to use an 'OCCURS DEPENDING ON len' in the linkage
> > definition. It's not too different from what you're probably already
doing
> > byte-at-a-time but once you've established the value of 'len' you can
> > reference my-var safely.
…[9 more quoted lines elided]…
> > > would be more than enough for what I was concerned with...Problem is,
MF
> > > abended with a 114 when referencing my-var if it was bigger than the
> > actual
> > > data returned...Even though my-var was in the linkage section...The
only
> > way
> > > I could do it was to code it as a one byte element in an array, and
…[10 more quoted lines elided]…
> > > > > > The same principle can be used for any API that returns a
pointer
> to
> > a
…[14 more quoted lines elided]…
> > > > > byte at a time...treat it as an array of one byte elements,
bumping
> > the
> > > > > index until you get to the null...MF cobol will abend with a 114
if
> it
> > > > > thinks the length is more than what is actually there...
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Question regarding WIN32 API PrintDlg

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3882536E.CB50F6D5@home.com>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com> <85ifuc$hkh$1@hyperion.mfltd.co.uk> <85j5fd$a71$1@nntp8.atl.mindspring.net> <iyaf4.32756$g12.975855@news2.rdc1.on.home.com> <85jl3f$e3s$1@nntp2.atl.mindspring.net> <vinf4.34352$g12.1035820@news2.rdc1.on.home.com> <85oe27$tof$1@nntp9.atl.mindspring.net> <85oet4$aib$1@nntp9.atl.mindspring.net>`

```


Ken Mullins wrote:
> 
> Tried it, and you ARE CORRECT sir...worked fine...Much appreciated...much
…[3 more quoted lines elided]…
> 
Ken,

Just for info - you know APIs aren't my bag - but what was your code to 
establish the length ?

Jimmy
```

#### ↳ Re: Question regarding WIN32 API PrintDlg

- **From:** Stephen.Biggs@merant.com (Steve Biggs)
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85ifqt$hf6$1@hyperion.mfltd.co.uk>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com>`

```
Chris T. <ctaliercio@my-deja.com> wrote:
>I am using the WIN32 "PrintDlg" API call to display a print dialog box
>for the user. The structure that is passed to this routine is:
[snip]
>
>On return from the API call, the hDevMode and hDevNames contain handles
…[4 more quoted lines elided]…
>I have defined in my program based upon the returned handle?

Chris,
Try this:
Use the API "GlobalLock" to get the addresses of each structure as 
a POINTER then use SET ADDRESS of the DEVMODE/DEVNAME structures you have 
defined in _linkage_ section to those POINTERs.
When you've finished, use "GlobalUnlock"

Steve.
```

#### ↳ Re: Question regarding WIN32 API PrintDlg

- **From:** Chris T. <ctaliercio@my-deja.com>
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85nupu$cqj$1@nnrp1.deja.com>`
- **References:** `<85i7io$4qd$1@nnrp1.deja.com>`

```
My thanks to everyone who submitted answers to this issue. The
functions GlobalLock and GlobalUnlock worked perfectly.

Thanks!
Chris


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
