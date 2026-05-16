[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus File corrupt

_4 messages · 4 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus File corrupt

- **From:** "EUROMERCANTE" <euromercante@mail.telepac.pt>
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7he5pk$2hq$1@duke.telepac.pt>`

```
Hi,

Could any body inform us if it�s normal and correct when a indexed file is
open for Input or I-O , and at same time we run Rebuild utility with /F
switch, it�s return the message "the file is corrupt".
For exemple:
 REBUILD  /V  file  /F

And if we stop the aplication  (closing the file) , doing rebuild again it
display the message "file is ok".
(This occurs with Netexpress V2).

Thanks
jm
```

#### ↳ Re: Micro Focus File corrupt

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373fbb6a.106569797@news.netvision.net.il>`
- **References:** `<7he5pk$2hq$1@duke.telepac.pt>`

```
On Wed, 12 May 1999 20:23:05 +0100 "EUROMERCANTE"
<euromercante@mail.telepac.pt> wrote:

:>Could any body inform us if itï¿½s normal and correct when a indexed file is
:>open for Input or I-O , and at same time we run Rebuild utility with /F
:>switch, itï¿½s return the message "the file is corrupt".
:>For exemple:
:> REBUILD  /V  file  /F

:>And if we stop the aplication  (closing the file) , doing rebuild again it
:>display the message "file is ok".
:>(This occurs with Netexpress V2).

Stating right away that I do not know Micro Focus, but I would doubt that any
verification program would provide useable results when another application
has the target file open in update mode.  
```

#### ↳ Re: Micro Focus File corrupt

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qJz_2.9185$gy1.2181390@news3.mia>`
- **References:** `<7he5pk$2hq$1@duke.telepac.pt>`

```
EUROMERCANTE wrote:
>
>Could any body inform us if it�s normal and correct when a indexed file is
…[7 more quoted lines elided]…
>(This occurs with Netexpress V2).


Expecting REBUILD to work with a file opened by another program is not
logical, unless the documentation expressly tells you to do it.  Does it?
```

#### ↳ Re: Micro Focus File corrupt

- **From:** mark.warren@merant.com (Mark Warren)
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<373b0f28.121023813@news.mfltd.co.uk>`
- **References:** `<7he5pk$2hq$1@duke.telepac.pt>`

```
As others have pointed out it is not recommended to try to rebuild a
file while it is in use.

If you have any particular questions about file handling or Rebuild,
please contact your local Support Representatives.

Mark Warren
MERANT International, Newbury, Berks. UK



On Wed, 12 May 1999 20:23:05 +0100, "EUROMERCANTE"
<euromercante@mail.telepac.pt> wrote:

>Hi,
>
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
