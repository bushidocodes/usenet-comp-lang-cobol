[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FJ and Win Common Dialog

_10 messages · 4 participants · 2000-07_

---

### FJ and Win Common Dialog

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9iCd5.871$LG.153555@nnrp1.sbc.net>`

```
We recently discovered the wonders of using the MS CommonDialog
control within a FJ PowerCOBOL program. It works pretty much as
advertised. For example,

INVOKE CD1 "ShowPrinter" (where "CD1" is the name of the Common Dialog
control)

brings up the normal Windows Select Printer dialog box.

But, doggone it, how can we tell if the user poked the "Cancel" button
on the dialog box?

Any hints would be appreciated.

Jerry Peacock
```

#### ↳ Re: FJ and Win Common Dialog

- **From:** "Tim O'Brien" <tdo658@earthlink.net>
- **Date:** 2000-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NMJd5.3101$U56.86018@newsread1.prod.itd.earthlink.net>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net>`

```
Jerry,

Good question Jerry - but I'm wondering why you would want to trap the
Cancel
click event from the Printer Dialog.  You might want to try the following:

- Select the MSCommonDialog control and bring up the properties window for
the control.
- Select the print tab and click the "CancelError" check box.
- Save and recompile.

Here is the behavior that you get.  When you click "Cancel", the printer
dialog goes away and a
Dialog box (with an exclamation icon) comes up that says, "Cancel was
selected."

Good luck,

Tim



"Jerry P" <jerryp@bisusa.com> wrote in message
news:9iCd5.871$LG.153555@nnrp1.sbc.net...
> We recently discovered the wonders of using the MS CommonDialog
> control within a FJ PowerCOBOL program. It works pretty much as
…[20 more quoted lines elided]…
>
```

##### ↳ ↳ Re: FJ and Win Common Dialog

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RUNd5.144$_c.69059@nnrp1.sbc.net>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net> <NMJd5.3101$U56.86018@newsread1.prod.itd.earthlink.net>`

```

Tim O'Brien <tdo658@earthlink.net

>
> Good question Jerry - but I'm wondering why you would want to trap
the
> Cancel
> click event from the Printer Dialog.  You might want to try the
following:
>
> - Select the MSCommonDialog control and bring up the properties
window for
> the control.
> - Select the print tab and click the "CancelError" check box.
> - Save and recompile.
>
> Here is the behavior that you get.  When you click "Cancel", the
printer
> dialog goes away and a
> Dialog box (with an exclamation icon) comes up that says, "Cancel
was
> selected."
>

Yeah, I got that far. The dialog box tells the user he poked the
"Cancel" button. But my question is: how does the dialog box tell the
calling program?

Other Win applications (e.g., Word) takes the "Cancel" button in the
printer dialog box to mean: 1) I don't want to select a (different)
printer, AND 2) I don't want to print anyway.

Suppose the user selects "Print." The program pops up the printer
dialog box. The user discovers there are NO printers available. He
selects "Cancel."

If the program can't discover the user attempted to abandon the
printing process.... oh well. I guess I could ask again: "Do you
really want to print now that you've selected a printer."
```

###### ↳ ↳ ↳ Re: FJ and Win Common Dialog

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3977B1C4.B1B919CA@home.com>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net> <NMJd5.3101$U56.86018@newsread1.prod.itd.earthlink.net> <RUNd5.144$_c.69059@nnrp1.sbc.net>`

```


Jerry P wrote:
> 
> Tim O'Brien <tdo658@earthlink.net
…[16 more quoted lines elided]…
> really want to print now that you've selected a printer."

Not quite the same as I'm using PC_PRINT with N/E. It gives me a Dialog
box showing printing in progression - but if I hit the CANCEL this
signals a Cancel event to PC_PRINT from which I can use a return code to
the invoking class. Surely F/J must give you a similar feature ?

Jimmy
```

###### ↳ ↳ ↳ Re: FJ and Win Common Dialog

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qLWd5.274$UI3.188510@nnrp2.sbc.net>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net> <NMJd5.3101$U56.86018@newsread1.prod.itd.earthlink.net> <RUNd5.144$_c.69059@nnrp1.sbc.net> <3977B1C4.B1B919CA@home.com>`

```

James J.
>
> Not quite the same as I'm using PC_PRINT with N/E. It gives me a
Dialog
> box showing printing in progression - but if I hit the CANCEL this
> signals a Cancel event to PC_PRINT from which I can use a return
code to
> the invoking class. Surely F/J must give you a similar feature ?

Yeah, kinda.

I can put my own button on the screen to pause/cancel the printing and
test for the button having been pressed. And we do that.

But that's effective only after the printing gets started.

I want to be able to detect the 'Cancel' button in the "ShowPrinter"
method of the Common Dialog box. If I can't detect the 'Cancel'
button, then (without some other step) the program may well try to
open a non-existent printer before the user gets the chance to poke my
pause/cancel button.
```

#### ↳ Re: FJ and Win Common Dialog

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2000-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8lf2nf$2lms$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net>`

```

Jerry,

We use the Printer Control under PC 5.0, and if we use the "SetPrinter"
Method, the ReturnValue can be interrogated for POW-TRUE which indicates the
OK button was pressed.  Otherwise, POW-FALSE indicates the cancel button was
pressed.  If we see Cancel, we skip the print routines entirely.  There
should be a sample program in the POWERCOBOL sub-directory in a folder named
PRINT that should illustrate this.

Hope this helps.

Denny
```

##### ↳ ↳ Re: FJ and Win Common Dialog

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pwWe5.452$pC5.148193@nnrp1.sbc.net>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net> <8lf2nf$2lms$1@newssvr05-en0.news.prodigy.com>`

```
Yes, we found that. There is, however, a problem:

We use PowerForm. PowerForm uses (always!) the system default printer
(a ghastly oversight). PowerForm has no way to set the system default
printer. The Print Control (that you suggest) has no way to set the
system default printer. The printer selected by the Print Control is
ignored by PowerForm. So it seems we have three alternatives: 1) Hope
the user set the default printer correctly before entering the
application, 2) Finding some way to get PowerForm to use the printer
we want; 3) Find some way to set the default printer for PowerForm's
use.

(There is another way (according to FJ) involving batch files and the
renaming/redirecting of DEFAULT.PRN information files from within the
application, a charitable description of which would be 'inelegant.')

After some experimentation, we opted for solution #3 using the
CommonDialog control (which is pretty nifty for other stuff too, like
"Save" and "SaveAs"). The CommonDialog box has two buttons: "OK" and
"Cancel." But we can't tell which button the user selected, which
brings us to the subject of this inquiry. And no, the content of
RETURN-CODE,  is not dependable .


"Denny Brouse" <denden@prodigy.net> wrote in message
news:8lf2nf$2lms$1@newssvr05-en0.news.prodigy.com...
>
> Jerry,
>
> We use the Printer Control under PC 5.0, and if we use the
"SetPrinter"
> Method, the ReturnValue can be interrogated for POW-TRUE which
indicates the
> OK button was pressed.  Otherwise, POW-FALSE indicates the cancel
button was
> pressed.  If we see Cancel, we skip the print routines entirely.
There
> should be a sample program in the POWERCOBOL sub-directory in a
folder named
> PRINT that should illustrate this.
>
…[5 more quoted lines elided]…
>
```

#### ↳ Re: FJ and Win Common Dialog

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uYIf5.277$Vh7.33782@nnrp2.sbc.net>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net>`

```
Got an answer.

According to FJ support, the MS CommonDialog box posts an error
condition when "Cancel" is selected and this can be tested for only by
using DECLARATIVES.

Further, DECLARATIVES are not supported in PowerCOBOL Version 5 (but
will be in version SEVEN(??!!).


"Jerry P" <jerryp@bisusa.com> wrote in message
news:9iCd5.871$LG.153555@nnrp1.sbc.net...
> We recently discovered the wonders of using the MS CommonDialog
> control within a FJ PowerCOBOL program. It works pretty much as
> advertised. For example,
>
> INVOKE CD1 "ShowPrinter" (where "CD1" is the name of the Common
Dialog
> control)
>
> brings up the normal Windows Select Printer dialog box.
>
> But, doggone it, how can we tell if the user poked the "Cancel"
button
> on the dialog box?
>
…[11 more quoted lines elided]…
>
```

##### ↳ ↳ Re: FJ and Win Common Dialog

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<397F9D43.675A224@home.com>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net> <uYIf5.277$Vh7.33782@nnrp2.sbc.net>`

```


Jerry P wrote:
> 
> Got an answer.
…[6 more quoted lines elided]…
> will be in version SEVEN(??!!).

BUT..... will Version 7 be compliant with COBOL '200?'

Jimmy
```

###### ↳ ↳ ↳ Re: FJ and Win Common Dialog

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dv5g5.464$c86.66312@nnrp2.sbc.net>`
- **References:** `<9iCd5.871$LG.153555@nnrp1.sbc.net> <uYIf5.277$Vh7.33782@nnrp2.sbc.net> <397F9D43.675A224@home.com>`

```
COBOL 2000 is expected circa 2023. FJ version 11 may be COBOL 2000
compliant.


"James J. Gavan" <jjgavan@home.com> wrote in message
news:397F9D43.675A224@home.com...
>
>
…[5 more quoted lines elided]…
> > condition when "Cancel" is selected and this can be tested for
only by
> > using DECLARATIVES.
> >
> > Further, DECLARATIVES are not supported in PowerCOBOL Version 5
(but
> > will be in version SEVEN(??!!).
>
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
