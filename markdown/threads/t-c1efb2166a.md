[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microsoft XML, Version 2 (msxml.dll) using NetExpress.

_3 messages · 3 participants · 2000-02_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Microsoft XML, Version 2 (msxml.dll) using NetExpress.

- **From:** "Neil Hayes" <NeilH@syspro.co.za>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38997be8$0$35291@helios.is.co.za>`

```
Hi,

I want to be able to use this dll in order to create and xml documents and
to parse xml documents via various cobol and VB COM components, but
somewhere the light bulb went out.  I struggle to find any good examples or
any examples of using Object cobol(MF) and automataion with other languages
and looking at converting vb to cobol is sometimes not fully explained.

In theory this should be just 5 or 6 lines of code:-

$set ooctrl(+p)

class-control.
myserver is class  "$OLE$Microsoft.FreeThreadedXM LDOM".

01 theServer object reference.

invoke myserver "new" returning theServer.

......etc:

Somewhere I'm going wrong or I'm using the wrong concept.

Has anyone done this ?.....

Neil
NeilH@syspro.co.za
```

#### ↳ Re: Microsoft XML, Version 2 (msxml.dll) using NetExpress.

- **From:** Stephen.Biggs@merant.com (Steve Biggs)
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87c6rq$h0b$1@hyperion.mfltd.co.uk>`
- **References:** `<38997be8$0$35291@helios.is.co.za>`

```
"Neil Hayes" <NeilH@syspro.co.za> wrote:
>$set ooctrl(+p)
>
>class-control.
>myserver is class  "$OLE$Microsoft.FreeThreadedXMLDOM".

The above should work (I just removed a space)...
You *do* have to have version 2.0 installed (I first tried this on one 
that didn't, and did get an error!). :)

>01 theServer object reference.
>
>invoke myserver "new" returning theServer.

This, from looking at the type library in the Type Library Wizard, should 
return an object reference (theServer) representing an instance of 
the automation interface IXMLDOMDocument. 
From there, you should be able to call the methods from that interface 
(remembering that things like BSTRs translate to PIC X(N) and other 
automation interfaces/objects as object references).

>Somewhere I'm going wrong or I'm using the wrong concept.

It seems to be a reasonable approach. What was the problem you got?

Steve.
```

#### ↳ Re: Microsoft XML, Version 2 (msxml.dll) using NetExpress.

- **From:** "David Sands" <davs@mfltd.co.uk>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87cht8$i89$1@hyperion.mfltd.co.uk>`
- **References:** `<38997be8$0$35291@helios.is.co.za>`

```
Hi Neil,

I have had some success using the Microsoft XML support using code along the
lines of:-

       CLASS-CONTROL.

           XMLDoc              is class "$OLE$MSXML.DOMDocument"
           OLEVariant          is class "olevar"
           XMLErr              is class "$OLE$MSXML.IXMLDOMParseError"
           olesup              is class "olesup"
           CharArray           is class "chararry"
           mfoleapi            is class "mfoleapi"


and in the procedure division:-

      ***** Create the XML DOM Object

           invoke XMLDoc "New" returning  XMLDocument

      ***** Load the document syncronously

           move OLEFALSE to async

           invoke XMLDocument "setasync" using by value async
                                         returning ws-result

           invoke OLEVariant "New" returning ws-OLEVariant

           move length of thestring to theStringLength
           invoke ws-OLEVariant "setStringAsBytes" using
                               by value     theStringLength
                               by reference theString
                   returning ws-result

      ***** Now load the document

           invoke XMLDocument "load" using by reference thestring
                                              returning ws-result

           if ws-result = OLEFALSE
               perform XML-Load-Error
           end-if

You can then access the information thats loaded.

You can use the Type Library Assistant in Net Express to generate a CPY that
shows the info you need to call the various methods.

Hope this helps.
David.

           .


Neil Hayes <NeilH@syspro.co.za> wrote in message
news:38997be8$0$35291@helios.is.co.za...
> Hi,
>
> I want to be able to use this dll in order to create and xml documents and
> to parse xml documents via various cobol and VB COM components, but
> somewhere the light bulb went out.  I struggle to find any good examples
or
> any examples of using Object cobol(MF) and automataion with other
languages
> and looking at converting vb to cobol is sometimes not fully explained.
>
…[21 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
