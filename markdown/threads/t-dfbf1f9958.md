[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Runtime Problem about RM/COBOL 85

_3 messages · 3 participants · 2000-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Runtime Problem about RM/COBOL 85

- **From:** "True Yang" <dbc888@gcn.net.tw>
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kt3tq$1kaq$1@member.gcn.net.tw>`

```
Hi,

    I have a problem. When I run an COBOL Program
"runc.exe". It appears an error

"COBOL procedure error 223. Error loading main program."

How can I fix this problem ?

Thanks for your help


True Yang
trueyang@gcn.net.tw
```

#### ↳ Re: Runtime Problem about RM/COBOL 85

- **From:** lsunley@mb.sympatico.ca (Lorne Sunley)
- **Date:** 2000-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqdYs1NR7tmZ-pn2-iEmsLoqrqOGd@tcpserver>`
- **References:** `<8kt3tq$1kaq$1@member.gcn.net.tw>`

```
On Sun, 16 Jul 2000 19:52:20, "True Yang" <dbc888@gcn.net.tw> wrote:

> Hi,
> 
…[9 more quoted lines elided]…
> 

If this is a program compiled by the Microfocus
or the Netexpress COBOL compilers that error
is a problem with a temporary sort work file.

You may have a TMP or TEMP variable that
is pointing to a non-existent directory.
```

#### ↳ Re: Runtime Problem about RM/COBOL 85

- **From:** maxomtech@wiscasset.net
- **Date:** 2000-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kvnt1$8ni$1@nnrp1.deja.com>`
- **References:** `<8kt3tq$1kaq$1@member.gcn.net.tw>`

```


According to my manual, a 223 in error in RM/COBOL indicates:
          "...an error occured while loading a DLL file....This error
generally indicates that the DLL was found, but has an invalid format
for the operating system being used.  Some 'system out of memory'
conditions may cause an error 223, since Windows returns an ambiguous
error status in some low memory situations."

Based on that message, it sounds like either a memory problem or a
problem with a call to a DLL.  Many times these messages will return a
"Line number" that the 'call' failed on.

Hope it helps.

Chris Loy


In article <8kt3tq$1kaq$1@member.gcn.net.tw>,
  "True Yang" <dbc888@gcn.net.tw> wrote:
> Hi,
>
…[12 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
