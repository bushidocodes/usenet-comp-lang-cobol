[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Dialog System Error messages support website? HELP please!!!

_4 messages · 3 participants · 2002-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus Dialog System Error messages support website? HELP please!!!

- **From:** rudyten@yahoo.com (Rudy)
- **Date:** 2002-11-04T15:02:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9be6b58.0211041502.7db7343a@posting.google.com>`

```
Can some direct me to a website where I can get detailed information
on Microfocus Dialog System Error messages? (Net Express 3.1)
I am getting this error 
"DSRUN error 17, 14001,3
A Panels V2 error occurred
Panels v2 funtion PF-Execute-Method returned error
P2ERR-BAD-PARAMETER"

Thanks For any help

Rudy
```

#### ↳ Re: Microfocus Dialog System Error messages support website? HELP please!!!

- **From:** "H-B.Diers" <h-b.diers@web.de>
- **Date:** 2002-11-05T10:08:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aq7sqh$mt0$00$1@news.t-online.com>`
- **References:** `<b9be6b58.0211041502.7db7343a@posting.google.com>`

```
Hi Rudy,
enclosed find a copy of MicroFocus DialogSystem error Codes:
--------------
  07  DS-ERROR-CODE            PIC 9(4) COMP-5.
           88  DS-SCREEN-MANAGER-ERROR   VALUE 17.

17 There was a screen manager error. ds-error-details-1 contains the Panels
V2 function code and ds-error-details-2 contains the Panels V2 return code.

Common errors are listed:

815 16 Sidefile not found.
 920 3 Bitmap not found.
 3203 6 Too many items in list box.
 3260 6 Too many items in selection box.
 All other 6 Out of memory.
 All 13000 Color not found. These codes can be found in pan2link.cpy and
pan2err.cpy, respectively.
-------------

I passed the files pan2link.cpy and pan2err.cpy, the error  14001 could not
be found

H-B. Diers
```

##### ↳ ↳ Re: Microfocus Dialog System Error messages support website? HELP please!!!

- **From:** rudyten@yahoo.com (Rudy)
- **Date:** 2002-11-05T15:24:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9be6b58.0211051524.52ab2ee7@posting.google.com>`
- **References:** `<b9be6b58.0211041502.7db7343a@posting.google.com> <aq7sqh$mt0$00$1@news.t-online.com>`

```
I have looked everywhere for that 14001....no luck too :(

The microfocus site has nothing on it that I can find.....this stuff i
am working with is old...very old dialog code.....

Thanks...for try...hehehe

I am gonna keep checking....am stuck for now...i might get lucky....
```

#### ↳ Re: Microfocus Dialog System Error messages support website? HELP please!!!

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2002-11-05T15:09:08
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aq8n2n$vl7$1@hyperion.microfocus.com>`
- **References:** `<b9be6b58.0211041502.7db7343a@posting.google.com>`

```
Hi Rudy,

Go here http://supportline.microfocus.com/

Select Self Service then Documentation and there you will find a HTML link
to all of the Net Express manuals.

Paul
www.microfocus.com
The Future of COBOL

"Rudy" <rudyten@yahoo.com> wrote in message
news:b9be6b58.0211041502.7db7343a@posting.google.com...
> Can some direct me to a website where I can get detailed information
> on Microfocus Dialog System Error messages? (Net Express 3.1)
…[8 more quoted lines elided]…
> Rudy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
