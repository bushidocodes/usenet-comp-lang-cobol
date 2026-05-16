[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How set window title in Win32 console app Need help

_4 messages · 3 participants · 1999-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How set window title in Win32 console app Need help

- **From:** "J���rgen Ibelgaufts" <ibelgaufts@gfc-net.de>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369DEA44.751A9573@gfc-net.de>`

```
Hi,

I have the following problem. When I start a new Windows NT console window I can
do this with the windows command "start". This command allows me to set the title
of the window (for example type 

  start "ABC"

in your console window and a new window will open which has the title "ABC" on the
title bar and the button down there in the start menu bar.

But as soon I invoke a Cobol program (for example XYZ.EXE), the title will first
change to "ABC - XYZ) and then to "XYZ".

Does anybody have a workaround or a method to set the window title from cobol?

Thanks in advance

Juergen Ibelgaufts
```

#### ↳ Re: How set window title in Win32 console app Need help

- **From:** "Gary Roush" <support@adtools.com>
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77ovhh$3lc$1@remarQ.com>`
- **References:** `<369DEA44.751A9573@gfc-net.de>`

```
Which COBOL compiler are you using?

Gary

J�rgen Ibelgaufts wrote in message <369DEA44.751A9573@gfc-net.de>...
>Hi,
>
>I have the following problem. When I start a new Windows NT console window
I can
>do this with the windows command "start". This command allows me to set the
title
>of the window (for example type
>
>  start "ABC"
>
>in your console window and a new window will open which has the title "ABC"
on the
>title bar and the button down there in the start menu bar.
>
>But as soon I invoke a Cobol program (for example XYZ.EXE), the title will
first
>change to "ABC - XYZ) and then to "XYZ".
>
>Does anybody have a workaround or a method to set the window title from
cobol?
>
>Thanks in advance
>
>Juergen Ibelgaufts
```

##### ↳ ↳ Re: How set window title in Win32 console app Need help

- **From:** "J���rgen Ibelgaufts" <ibelgaufts@gfc-net.de>
- **Date:** 1999-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A2E15D.D887F13F@gfc-net.de>`
- **References:** `<369DEA44.751A9573@gfc-net.de> <77ovhh$3lc$1@remarQ.com>`

```
Hi altogether,

I use Microfocus Object Cobol 4.0 on Windows NT.

In the meantime, I found a solution myself by finding that the Microfocus 
COB32API.DLL provides access to the windows api by simply calling its functions
like SetConsoleTitleA.

Juergen Ibelgaufts

------------------------------------------------------------------------

Gary Roush schrieb:
> 
> Which COBOL compiler are you using?
…[27 more quoted lines elided]…
> >Juergen Ibelgaufts
```

#### ↳ Re: How set window title in Win32 console app Need help

- **From:** "David Sands" <davs@mfltd.co.uk>
- **Date:** 1999-01-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77uusl$cb2@hyperion.mfltd.co.uk>`
- **References:** `<369DEA44.751A9573@gfc-net.de>`

```
Hi Jurgen,

You can do this using a standard Resource File and the Resource compiler.

The Resource file should be something like:-

#include "DISPLAY.H"
#define _MFRES_INC_
/* Micro Focus Resource File. */
/* Version 4.00.017 */
STRINGTABLE LOADONCALL DISCARDABLE
BEGIN
   100 "This is the Title"
END
#include <mfrcwin.h>
/*MF_BITMAP*/
/*MF_CURSOR*/
/*MF_DIALOG*/
/*MF_ICON*/
ID_DPS  ICON PRELOAD DISCARDABLE "dps.ico"
/*MF_MENU*/
/*MF_RCDATA_END*/

This sets the standard title text and also associates an ICON with the
application.

Hope this help.
David.


J�rgen Ibelgaufts wrote in message <369DEA44.751A9573@gfc-net.de>...
>Hi,
>
>I have the following problem. When I start a new Windows NT console window
I can
>do this with the windows command "start". This command allows me to set the
title
>of the window (for example type
>
>  start "ABC"
>
>in your console window and a new window will open which has the title "ABC"
on the
>title bar and the button down there in the start menu bar.
>
>But as soon I invoke a Cobol program (for example XYZ.EXE), the title will
first
>change to "ABC - XYZ) and then to "XYZ".
>
>Does anybody have a workaround or a method to set the window title from
cobol?
>
>Thanks in advance
>
>Juergen Ibelgaufts
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
