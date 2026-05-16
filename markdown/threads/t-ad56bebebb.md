[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF use skeletons

_7 messages · 4 participants · 2003-09_

---

### MF use skeletons

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-25T21:20:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030925172026.27155.00000170@mb-m03.aol.com>`

```

I am reading a 1998 copy of "COBOL Unleashed,"
by Jon Wessler, et al.; a good book, and useful
for keeping furniture in place during high winds, as well.

He refers to Micro-Focus use skeletons.

I am interested in knowing if such things are still in their (MF's)
current product. And would like to know how much of that thinking
has made it into COBOL 2002. 

Citations to technical material online from _any_vendor_ would be 
helpful to my further studies.  Online examples would also be useful.

If there is alternative vocabulary from other vendors, please guide me 
to their terms, and any terms that have become the norm in the standard
that might relate to use skeletons.

Thanking you in advance for your troubles, ...

Bob Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: MF use skeletons

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-09-26T16:23:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F746922.EDB5A194@shaw.ca>`
- **References:** `<20030925172026.27155.00000170@mb-m03.aol.com>`

```


RKRayhawk wrote:

> I am reading a 1998 copy of "COBOL Unleashed,"
> by Jon Wessler, et al.; a good book, and useful
…[3 more quoted lines elided]…
>

Sorry don't understand the question. I have a copy of 'COBOL Unleashed' and
I use Net Express - point me to what you are referring to.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: MF use skeletons

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-26T16:30:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2RZcb.5119$NX3.1670@newsread3.news.pas.earthlink.net>`
- **References:** `<20030925172026.27155.00000170@mb-m03.aol.com> <3F746922.EDB5A194@shaw.ca>`

```
Look at the chapter

   "Chapter 13: Requirements-based Vocabulary"

in
http://supportline.microfocus.com/supportline/documentation/books/nx40/nx40indx.htm

For an example, they have

method-id. credit is method
    ...
procedure division using lnkAmount
    INVOKED AS ==Credit <self> [with] <lnkAmount> ==
    OR AS ==deposit <lnkAmount> [in] <self> ==

which allows your program to "use" CREDIT as a COBOL "verb".

(I assume this is what RKRayhawk was referring to)
```

###### ↳ ↳ ↳ Re: MF use skeletons

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-09-26T17:40:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F747B24.2D8247B5@shaw.ca>`
- **References:** `<20030925172026.27155.00000170@mb-m03.aol.com> <3F746922.EDB5A194@shaw.ca> <2RZcb.5119$NX3.1670@newsread3.news.pas.earthlink.net>`

```


"William M. Klein" wrote:

> Look at the chapter
>
…[16 more quoted lines elided]…
>

If your assumption is correct, about 'Vocabulary', then it's probably a fair guess that
this is a feature that J4 wont pick up on. I'm not aware of any N/E people using this
OO feature extensively. (Nobody has publicly 'enthused' about it).

For Ray's info there is a Vocabulary class, (included under the 'Base' set), which lets
you make the kind of change BIll illustrated.

In contradiction of what I've written above, a GUI vocabulary file, 'guibase.if', is
used extensively by people creating GUIs :-

copy "guibase.if".
*>-------------------------------------------------
$set hidemessage(731)
 class-id. guibase is external.
  object section.
  class-control.
     Dependent is class "dependnt"
     guibase is class "guibase".
 object.
 method-id. "setEvent".
 linkage section.
 01 lnkeventindex          pic s9(9) comp-5.
 01 lnkeventhandler        usage object reference.
 procedure division using lnkeventindex lnkeventhandler
*> vocabulary
 INVOKED as
 == setEvent
   [using] ([<self>] ,
             <lnkeventindex> ,
             <lnkeventhandler> )
 ==.
 end method "setEvent".
 method-id. "translateEvent".
 linkage section.
 01 lnkeventindex          pic s9(9) comp-5.
 01 lnkTranslatedEvent     pic s9(9) comp-5.
 01 lnkReceiver            usage object reference.
 01 lnkmethodName          usage object reference.
 procedure division using lnkeventindex lnkReceiver
                          lnkTranslatedEvent
*> vocabulary
 INVOKED as
 == map event <lnkeventindex> upon <self>
        to logical event <lnkTranslatedEvent> upon <lnkReceiver>
 ==.
 end method "translateEvent".
 method-id. "setEventTo".
 linkage section.
 01 lnkeventindex        pic s9(9) comp-5.
 01 lnkReceiver          usage object reference.
 01 lnkmethodName        pic x.
 01 lnkParam1            pic x(4).
 01 lnkParam2            pic x(4).
 procedure division using lnkeventindex lnkReceiver lnkMethodName
                          lnkParam1 lnkParam2
*> vocabulary
 INVOKED as
 == map event <lnkeventindex> upon <self>
        to method <lnkMethodName> upon  <lnkReceiver>
             [<lnkParam1>] [<lnkParam2>]
 ==.
 end method "setEventTo".
 end object.
 end class guibase.
*>--------------------------------------------------------------

As yet I haven't found a need to create my own 'Vocabularies' - but I'll keep my
options open - the penny might drop some time in the future.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: MF use skeletons

_(reply depth: 4)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-27T00:43:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030926204358.12504.00000188@mb-m04.aol.com>`
- **References:** `<3F747B24.2D8247B5@shaw.ca>`

```
Thanks to "James J. Gavan" and "William M. Klein" for the detailed replies and
citation.

This is much more than I found in "COBOL Unleashed,"  Chapter 28, Object
Oriented COBOL - Implementation,  under the heading
'Retaining Readability."
```

###### ↳ ↳ ↳ Re: MF use skeletons

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-27T12:17:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309271117.1b9c821e@posting.google.com>`
- **References:** `<20030925172026.27155.00000170@mb-m03.aol.com> <3F746922.EDB5A194@shaw.ca> <2RZcb.5119$NX3.1670@newsread3.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote

> procedure division using lnkAmount
>     INVOKED AS ==Credit <self> [with] <lnkAmount> ==
>     OR AS ==deposit <lnkAmount> [in] <self> ==
> 
> which allows your program to "use" CREDIT as a COBOL "verb".

This caters for those OO programmers who want to use it to write their
own personal language.  While it adds readability to the _writer_, it
reduces readability to everyone else.

(see other discusion on 'all manner of searching').
```

###### ↳ ↳ ↳ Re: MF use skeletons

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-09-27T20:21:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F75F27C.634EC8BD@shaw.ca>`
- **References:** `<20030925172026.27155.00000170@mb-m03.aol.com> <3F746922.EDB5A194@shaw.ca> <2RZcb.5119$NX3.1670@newsread3.news.pas.earthlink.net> <217e491a.0309271117.1b9c821e@posting.google.com>`

```


Richard wrote:

> "William M. Klein" <wmklein@nospam.netcom.com> wrote
>
…[10 more quoted lines elided]…
> (see other discusion on 'all manner of searching').

Basically the reason that I don't use vocabularies. However, following up
on your comments I had a look at the on-line manual for N/E V4.0.  (V.3.1
is 'poor' on OO in the LRMs). - this piqued my interest :-
---------------------------------------------------------
User-defined Functions

You can also create new functions with user vocabularies. The new
functions look like
COBOL intrinsic functions when used in a program.

For example, you could code:

compute interest = .06 * function balance (thisBankAccount)

You can omit the keyword function, so you could also write:

compute interest = .06 * balance (thisBankAccount)

The definition of function balance looks like this:

 method-id. "getBalance".
 linkage section.
 01 lsAmount pic S9(10)v99.

 procedure division returning lsAmount
    INVOKED AS FUNCTION == Balance ( <self> ) ==.
 end method "getbalance".
-----------------------------------------------------------------------------

Now I'm not about to rush off and start coding that way - but it does have
possibilities.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
