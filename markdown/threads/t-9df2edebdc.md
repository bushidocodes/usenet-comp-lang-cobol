[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Taking direct input from the keyboard using TinyCobol

_4 messages · 2 participants · 2002-10_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source)

---

### Taking direct input from the keyboard using TinyCobol

- **From:** "Davebondl" <davebondl@mindspring.com>
- **Date:** 2002-10-07T11:28:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ansjp8$l7p$1@slb3.atl.mindspring.net>`

```

All,

Can anyone let me know how to take direct input from the keyboard using
TinyCobol.
I know how to do it using MicroFocus Cobol call X"AF" however this approach
does not work with TinyCobol.
Any help please.

Dave
```

#### ↳ Re: Taking direct input from the keyboard using TinyCobol

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-10-07T22:52:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-Y8cN6nTTHzp8@h24-82-204-17.wp.shawcable.net>`
- **References:** `<ansjp8$l7p$1@slb3.atl.mindspring.net>`

```
On Mon, 7 Oct 2002 19:28:54 UTC, "Davebondl" 
<davebondl@mindspring.com> wrote:

> 
> All,
…[9 more quoted lines elided]…
> 

Have you tried "accept data-name"
```

##### ↳ ↳ Re: Taking direct input from the keyboard using TinyCobol

- **From:** "Davebondl" <davebondl@mindspring.com>
- **Date:** 2002-10-07T16:21:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ant4t4$rpt$1@slb2.atl.mindspring.net>`
- **References:** `<ansjp8$l7p$1@slb3.atl.mindspring.net> <ZpzG4UNLyRNq-pn2-Y8cN6nTTHzp8@h24-82-204-17.wp.shawcable.net>`

```
Yes I know that.. however it will not register F keys etc. I want the direct
keyboard poll.

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-Y8cN6nTTHzp8@h24-82-204-17.wp.shawcable.net...
> On Mon, 7 Oct 2002 19:28:54 UTC, "Davebondl"
> <davebondl@mindspring.com> wrote:
…[6 more quoted lines elided]…
> > I know how to do it using MicroFocus Cobol call X"AF" however this
approach
> > does not work with TinyCobol.
> > Any help please.
…[9 more quoted lines elided]…
> Lorne Sunley
```

###### ↳ ↳ ↳ Re: Taking direct input from the keyboard using TinyCobol

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-10-08T00:23:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-IeC4qk0doPSd@h24-82-204-17.wp.shawcable.net>`
- **References:** `<ansjp8$l7p$1@slb3.atl.mindspring.net> <ZpzG4UNLyRNq-pn2-Y8cN6nTTHzp8@h24-82-204-17.wp.shawcable.net> <ant4t4$rpt$1@slb2.atl.mindspring.net>`

```
You could always use the  OS API to snoop the keyboard.

Lorne

On Tue, 8 Oct 2002 00:21:06 UTC, "Davebondl" 
<davebondl@mindspring.com> wrote:

> Yes I know that.. however it will not register F keys etc. I want the direct
> keyboard poll.
…[26 more quoted lines elided]…
> 
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
