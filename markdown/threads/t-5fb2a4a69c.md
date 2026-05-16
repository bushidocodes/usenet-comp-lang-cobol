[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ASSIGN TO PRINTER, Internal SORTing and .NET

_7 messages · 3 participants · 2003-06_

---

### ASSIGN TO PRINTER, Internal SORTing and .NET

- **From:** richardson@eclecticsoftwaresolutions.com (Chris Richardson)
- **Date:** 2003-06-14T15:11:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b11feff.0306141411.3023c537@posting.google.com>`

```
I'd like to share the content from a converation that I had...

I friend asked me the other day:
 
"Is it true that Fujitsu's NetCOBOL for .NET does not support basic
features like ASSIGN TO PRINTER and Internal SORTing?"

My reply sounded something like this:

"Yes, this is true AND not true. 

True, IF you are trying to print or sort internally - WHILE using the
Legacy COBOL syntax approach, - those features are not supported in
pure COBOL .NET (managed) code.

Not True, however, IF you leverage the .NET Framework class library
for your printing and for internal sorting needs. Since Fujitsu's
NetCOBOL for .NET fully supports the .NET Framework class library, you
can use the .NET classes to accomplish your task."

I continued:

"The .NET "ARRAY" class - which is part of the "System"
namespace/class library - can be filled with data - conceptually much
like you would fill a traditional COBOL table. Then, you can use the
SORT method that is exposed by the ARRAY class.

Then, there is the .NET ARRAYLIST class - which is part of the
"System.Collections" namespace/class library. This class also exposes
a SORT method and can be filled with data (that you want to sort).

Both the ARRAY class and the ARRAYLIST classes offer many other
features (in addition to SORTing). Additonally, there are other
similiar feature-rich classes in the "System.Collections"
namespace/class library that can also be used for
"loading/retrieving/manipulating" table data and value/pair data.

As for printing, using pure .NET code, in COBOL or any other .NET
enabled language...you have the .NET PrintDocument class found in the
"System.Drawing.Printing" namespace/class library. Using the public
methods and properties exposed by this class, you can certainly
accomplish your printing - in your .NET Windows Application.

If you happen to be using a .NET Web Application, you can even add two
or three lines of DHTML (or even Javascript) code to invoke the Print
method from the Windows object - to accomplish your printing. Of
course, you can even leverage the Print button that is freely exposed
on your Browser window to print your Printer-Ready HTML display.

Lastly, for your advanced Printing/Reporting needs, with either
Windows or Web, you could take advantage of the .NET Crystal Reports
components - yet another .NET Class Library - that are bundled with
VS.NET.

So, using COBOL (or any other .NET enabled language) and the .NET
Framework classes, you can easily print and/or SORT internally.

- well, that is about it.

---------------------------------

<Marketing>

For those interested, I have authored a book that uses this .NET
centric view towards using COBOL (or VB.NET) to build Windows and Web
applications.

To find out more please visit either of the following 3 links:

http://www.amazon.com/exec/obidos/ASIN/1590590481/eclecticsoftw-20

http://www.eclecticsoftwaresolutions.com

http://apress.com/book/bookDisplay.html?bID=112

Alternate link page:
http://www.eclecticsoftwaresolutions.com/HTMLPage3.html

</Marketing>
```

#### ↳ Re: ASSIGN TO PRINTER, Internal SORTing and .NET

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-14T17:26:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcg7fh$t6n$1@slb4.atl.mindspring.net>`
- **References:** `<b11feff.0306141411.3023c537@posting.google.com>`

```
And the "general" answer is,

 No, Fujitsu's NetCOBOL for  .NET is *not* an ANSI/ISO '85 much less 2002
conforming compiler (either as far as OO or non-OO features go).  They don't
claim that it is - and they certainly do not claim that code developed for
this compiler is portable to any other ANSI/ISO conforming COBOL compiler
(unless you use a VERY limited sub-set of code).

If, on the other hand, your "goal" or design requirement is to create a .NET
*only* solution, then this is certainly a viable solution.  Of course, it is
ALSO possible to create (using Fujitsu COBOL NetCOBOL for Windows - or ANY
of the other Windows compiler) object code that can run as "not managed"
within the .NET environment.  Such code would have the advantage of being
more portable but the disadvantage of having no "native" access to anything
that makes .NET really language-independent and Windows-exploiting
(including no access to the *extensive* .NET class libraries)

P.S. Chris - do you know whether V2 of NetCOBOL for .NET still has all (or
many) of the native COBOL language restrictions that V1 did? (e.g. no
internal SORT statement, no direct output to printers, etc)
```

##### ↳ ↳ Re: ASSIGN TO PRINTER, Internal SORTing and .NET

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-14T17:28:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcg7kj$omh$1@slb5.atl.mindspring.net>`
- **References:** `<b11feff.0306141411.3023c537@posting.google.com> <bcg7fh$t6n$1@slb4.atl.mindspring.net>`

```
P.P.S.  It will be HIGHLY interesting to see whether or not when (expected
later this year) Micro Focus provides its "full .NET" product they provide
*both* .NET "managed" program solution *and* ANSI/ISO conforming compiler.
```

###### ↳ ↳ ↳ Re: ASSIGN TO PRINTER, Internal SORTing and .NET

- **From:** richardson@eclecticsoftwaresolutions.com (Chris Richardson)
- **Date:** 2003-06-15T10:45:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b11feff.0306150945.6031451a@posting.google.com>`
- **References:** `<b11feff.0306141411.3023c537@posting.google.com> <bcg7fh$t6n$1@slb4.atl.mindspring.net> <bcg7kj$omh$1@slb5.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<bcg7kj$omh$1@slb5.atl.mindspring.net>...
> P.P.S.  It will be HIGHLY interesting to see whether or not when (expected
> later this year) Micro Focus provides its "full .NET" product they provide
> *both* .NET "managed" program solution *and* ANSI/ISO conforming compiler.
> 

Certainly, I agree. When it becomes possible, I'm looking forward to
being able to the .NET implementation of Micro Focus with that of
Fujitsu.

> --
> Bill Klein
…[113 more quoted lines elided]…
> >
```

##### ↳ ↳ Re: ASSIGN TO PRINTER, Internal SORTing and .NET

- **From:** richardson@eclecticsoftwaresolutions.com (Chris Richardson)
- **Date:** 2003-06-15T10:43:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b11feff.0306150943.28723387@posting.google.com>`
- **References:** `<b11feff.0306141411.3023c537@posting.google.com> <bcg7fh$t6n$1@slb4.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<bcg7fh$t6n$1@slb4.atl.mindspring.net>...
> And the "general" answer is,
> 
…[17 more quoted lines elided]…
> internal SORT statement, no direct output to printers, etc)

I'm currently checking with Fujitsu to see what information - beyond
what was originally stated in their V2 press release
(http://www.adtools.com/news/prelease/pr20030424.htm) - they may care
to "publicly" disclose.

> 
> --
…[82 more quoted lines elided]…
> > </Marketing>
```

#### ↳ Re: ASSIGN TO PRINTER, Internal SORTing and .NET

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-06-15T05:37:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c33300$1dbf51c0$de8bf243@chottel>`
- **References:** `<b11feff.0306141411.3023c537@posting.google.com>`

```
Thanks, I was hoping that something like this was possible.  By the way I
bought your book and it arrived today.

<nothing more from me follows>

Chris Richardson <richardson@eclecticsoftwaresolutions.com> wrote in
article <b11feff.0306141411.3023c537@posting.google.com>...
> I'd like to share the content from a converation that I had...
> 
…[77 more quoted lines elided]…
>
```

##### ↳ ↳ Re: ASSIGN TO PRINTER, Internal SORTing and .NET

- **From:** richardson@eclecticsoftwaresolutions.com (Chris Richardson)
- **Date:** 2003-06-16T20:51:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b11feff.0306161951.48d94862@posting.google.com>`
- **References:** `<b11feff.0306141411.3023c537@posting.google.com> <01c33300$1dbf51c0$de8bf243@chottel>`

```
"Charles Hottel" <chottel@cpcug.org> wrote in message news:<01c33300$1dbf51c0$de8bf243@chottel>...
> Thanks, I was hoping that something like this was possible.  By the way I
> bought your book and it arrived today.

Thank you. I welcome any feedback (both positive and negative <g>). 

> 
> <nothing more from me follows>
…[82 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
