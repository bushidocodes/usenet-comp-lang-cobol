[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to use the "AddressOf" of "SetWindowlong" Api call

_5 messages · 3 participants · 2002-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to use the "AddressOf" of "SetWindowlong" Api call

- **From:** gmspano <member@dbforums.com>
- **Date:** 2002-09-02T18:25:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1765940.1030991156@dbforums.com>`

```

Hello to all

Does anyone know how to obtain the "AddressOf" of a procedure?
I will explain better..
I'm "translating" a Vb source project to manage the scrollbar in a form
(i'm using Fujitsu Netcobol for Windows 6.1) and searching in the
Windows api list, i found the "ShowScrollbar" api call.
I'm able to see the scrollbar (horz and vert), but i can't capture their
events.
Here is a little portion of the vb source code:

m_oldWinProc = SetWindowLong (m_hWnd, GWL_WNDPROC, AddressOf
HandleScrollMsg)

The HANDLESCROLLMSG is a routine that checks the scroll type (horz
or vert)...

Could someone help me?

Thanks in advance..

Gianni
```

#### ↳ Re: How to use the "AddressOf" of "SetWindowlong" Api call

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-09-02T14:14:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<al0dj6$e42$1@slb5.atl.mindspring.net>`
- **References:** `<1765940.1030991156@dbforums.com>`

```
What compiler (Vendor and release) are you using.

Some (certainly NOT all) Windows compilers have a

  05 Procedure-Ptr  Usage Procedure-Pointer.
       ....
 Set Procedure-Ptr to Address of  "entry-point-name"

feature.
```

##### ↳ ↳ Re: How to use the "AddressOf" of "SetWindowlong" Api call

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-09-02T20:01:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<osPc9.6355$yt3.2923253@newssrv26.news.prodigy.com>`
- **References:** `<1765940.1030991156@dbforums.com> <al0dj6$e42$1@slb5.atl.mindspring.net>`

```
Even if the compiler supports PROCEDURE POINTER, you will also need to setup
a COBOL ENTRY (or subprogram) for the subclass procedure.

BUT....
If "all"  the subclass procedure is doing  is checking if it's a horizontal
or vertical scrollbar ("The HANDLESCROLLMSG is a routine that checks the
scroll type (horz or vert)...),  it is *not* necessary to set up a subclass
procedure to do that. You will know within the COBOL program which control
is sending the message, and as the designer, you will "know" if that
particular control is a horizontal or vertical bar. You could also figure it
out from GetWindowRect, if you are willing to live with the assumption a
scrollbar which is wider than it is high is 'horizontal.' (Although this is
not a requirement. You can make really short, really fat scrollbars if you
want).

Can you post the VB subclass procedure so we can check? It may be doing
something else. It does not make sense that someone would go to the trouble
of setting up a subclass procedure just to check which control is sending
the message.
```

#### ↳ Re: How to use the "AddressOf" of "SetWindowlong" Api call

- **From:** gmspano <member@dbforums.com>
- **Date:** 2002-09-02T19:53:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1766135.1030996396@dbforums.com>`
- **References:** `<1765940.1030991156@dbforums.com>`

```

Hello William

As i specified in the post, i'm using Netcobol for Windows (old
Powercobol) v6.1 by Fujistu Software Corp.

I'm trying to use some api calls to resolve the troubles, but it seems
that it doesn't working.

Gianni
```

#### ↳ Re: How to use the "AddressOf" of "SetWindowlong" Api call

- **From:** gmspano <member@dbforums.com>
- **Date:** 2002-09-02T21:12:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1766245.1031001141@dbforums.com>`
- **References:** `<1765940.1030991156@dbforums.com>`

```

Hi Bill

Could i send to you the original Vb source code to verify what i mean?
Email me at: softline2000@tin.it

Thanks

Gianni
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
