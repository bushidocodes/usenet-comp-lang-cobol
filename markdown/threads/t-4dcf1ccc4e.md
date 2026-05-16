[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Interface directly with OCX from NetExpress

_3 messages · 2 participants · 2000-06_

---

### Interface directly with OCX from NetExpress

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000630115708.01769.00000706@ng-cq1.aol.com>`

```
Good Afternoon,

I have an OCX that I would like to be able to communicate with.  I have used
the "Type Library Assistant" to create a copy file.  But I am confused how to
interface that to my COBOL program.  I do not use Object COBOL and would prefer
to stay with the plain old COBOL that I am used to.  Does anyone have samples
or advice on how to interface with OCX's ?

Thanks,
Bob Hennessey
```

#### ↳ Re: Interface directly with OCX from NetExpress

- **From:** Stephen.Biggs@merant.com (Steve Biggs)
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jiov2$qsf$1@hyperion.mfltd.co.uk>`
- **References:** `<20000630115708.01769.00000706@ng-cq1.aol.com>`

```
bob7536@aol.com (Bob7536) wrote:
>Good Afternoon,
>
>I have an OCX that I would like to be able to communicate with.  I have used
>the "Type Library Assistant" to create a copy file.  But I am confused how to
>interface that to my COBOL program.  

The Type Library Assistant has two uses:
1) To generate details about OLE Automation interfaces found in a type 
library in COBOL format, such as enumerations, ids and so forth, including 
commented out method descriptions. These can then be used when talking to 
Automation servers using the Object COBOL OLE domain support - most 
documentation etc. gives these values and details in C or VB, so the 
Assistant provides a valuable COBOL utility for this.

2) To generate OLE class library-like skeleton classes which can be edited 
to provide access to "raw" (non-Automation) interfaces that the type 
library describes. See the OLE class library sources, shipped with Net 
Express, for examples of how "raw" COM interfaces can be used/called from 
COBOL.

>I do not use Object COBOL and would prefer
>to stay with the plain old COBOL that I am used to.  Does anyone have samples
>or advice on how to interface with OCX's ?

Using Object COBOL is much easier for any COM work, as COM maps much 
better to instances of interfaces than "normal" (non-OO) COBOL. 
If you don't want to use the Object COBOL support, you need a decent 
understanding of COM - such as "interfaces are pointers to pointers to a 
table of procedure pointers (functions)" - and using such pointers in 
COBOL.

There is an example of using OCXs (which is an ActiveX control - ie 
usually has a GUI interface) in
\netexpress\base\demo\oledemos\contain\ocx
and
\netexpress\dialogsystem\demo\ocxds

Most of the other demos in \oledemos just use OLE automation servers, such 
as Word or Excel. If what you want to use is just an automation server, 
these would be a better bet.

Steve.
```

##### ↳ ↳ Re: Interface directly with OCX from NetExpress

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000630133623.04085.00000840@ng-fe1.aol.com>`
- **References:** `<8jiov2$qsf$1@hyperion.mfltd.co.uk>`

```
Hi Steve,

Thanks I will give it a look.

Bob
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
