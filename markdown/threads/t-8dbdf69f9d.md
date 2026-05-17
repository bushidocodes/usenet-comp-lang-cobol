[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL with Visual Basic Interface How can this be done?

_9 messages · 8 participants · 1997-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL with Visual Basic Interface How can this be done?

- **From:** "alf" <ua-author-29335@usenetarchives.gap>
- **Date:** 1997-10-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bccf4d$b338b240$0100a8c6@alf>`

```

I was currently assigned a project which uses MicroFocus COBOL, but
requires
a visual basic front end for data input and validation. The COBOL program
does the crunching. My teacher thinks there is a way for this to be done.
But with requirment that the COBOL program be the driving program, How can
a procedural app control the Visual Basic app which is message driven.
Essentialy from what i have done, the cobol program seems to compile to be
no more than a DOS executable. Anyone ever link cobol programs with visual
basic programs, with the cobol program being the driving program. I can see
how this could be done if i were to use the VB front end to drive the cobol
programs to process the data, but is there a way to actually use the
linkage section to transfer data between the cobol and vb front end.
Any Ideas would be greatly appreciated.
Rafael F. Richard
rfr··.@m··.net
```

#### ↳ Re: MF COBOL with Visual Basic Interface How can this be done?

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1997-10-01T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8dbdf69f9d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bccf4d$b338b240$0100a8c6@alf>`
- **References:** `<01bccf4d$b338b240$0100a8c6@alf>`

```

"alf" wrote:

› I was currently assigned a project which uses MicroFocus COBOL, but
› requires 
› a visual basic front end for data input and validation. The COBOL program
› does the crunching. My teacher thinks there is a way for this to be done.

Your teacher is right, it can be done, but now you have two different
programs in two different languages to maintain. One program is
written using procedurally based programming methods and the other
uses event driven methodology. Could get messy in maintenance.

› But with requirment that the COBOL program be the driving program, How can
› a procedural app control the Visual Basic app which is message driven.

Scrap the VB and use COBOL sp2 instead. sp2 allows the COBOL
programmer to write the entire program in 100% COBOL. That eliminates
the procedural versus event driven headache.

› Essentialy from what i have done, the cobol program seems to compile to be
› no more than a DOS executable. Anyone ever link cobol programs with visual
…[3 more quoted lines elided]…
› linkage section to transfer data between the cobol and vb front end.

sp2 simply passes the data from the GUI screen directly into a COBOL
copybook. You don't have to worry about how to get the data into
COBOL, because it's already there.

› Any Ideas would be greatly appreciated.
› Rafael F. Richard
› rfr··.@m··.net

Bob Wolfe, flexus, rtw··.@FIL··s.com
Delete FILTER from my e-mail address to reply
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: MF COBOL with Visual Basic Interface How can this be done?

- **From:** "mark" <ua-author-10783@usenetarchives.gap>
- **Date:** 1997-10-01T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8dbdf69f9d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bccf4d$b338b240$0100a8c6@alf>`
- **References:** `<01bccf4d$b338b240$0100a8c6@alf>`

```


Rafael,

I have spent over a year working on a Microfocus Cobol / Visual Basic 4.0
project. I am afraid we did it the other way around. The Cobol .DLL's were
merely called to do the file i-o and data to be written/data read is passed
in the linkage section. I know of no way to have Cobol drive the
application and we are now rewriting the system to use access instead. I
must say though that we have Microfocus Cobol 3.2 and I know nothing about
Microfocus's Visual Cobol or whatever their 32-bit Windows version is
called, perhaps this is a better option. Our problem was compounded by the
fact that we had to stay on a 16-bit platform which ruled out Visual Cobol.

I would be happy to help with any other questions you may have - sorry this
is not quite what you were looking for but something may be helpful.

Mark Farr
Analyst Programmer
South Africa

Constant's aren't, variables don't





alf wrote in article <01bccf4d$b338b240$0100a8c6@alf>...
› I was currently assigned a project which uses MicroFocus COBOL, but
› requires 
…[18 more quoted lines elided]…
›
```

#### ↳ Re: MF COBOL with Visual Basic Interface How can this be done?

- **From:** "jim morcombe" <ua-author-1974021@usenetarchives.gap>
- **Date:** 1997-10-01T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8dbdf69f9d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bccf4d$b338b240$0100a8c6@alf>`
- **References:** `<01bccf4d$b338b240$0100a8c6@alf>`

```

Alf,

We have done this by writing a C++ program which we compiled into the Microfocus
run time system. The Cobol program calls the C program which uses TCP/IP to
comunicate with a Visual Basic program sitting on a Windows 95 PC. This approach
means that the Cobol program can sit on the same PC or can reside on a remote host.

It took a while to write the programs but now we can drive VB data entry as well as
display graphics and images - all driven by a Cobol Program. The end result was
pretty mind blowing.

Jim Morcombe.

PS - You wouldn't believe what we're doing in our next generation of software.

alf wrote:

› I was currently assigned a project which uses MicroFocus COBOL, but
› requires
…[12 more quoted lines elided]…
›                                                         rfr··.@m··.net
```

##### ↳ ↳ Re: MF COBOL with Visual Basic Interface How can this be done?

- **From:** "pri..." <ua-author-17072105@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8dbdf69f9d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8dbdf69f9d-p4@usenetarchives.gap>`
- **References:** `<01bccf4d$b338b240$0100a8c6@alf> <gap-8dbdf69f9d-p4@usenetarchives.gap>`

```

Jim Morcombe wrote:

hello,
you can create a DLL with inside the cobol routine ad call them from
VB. The application have the Windows interface from VB3 with the
Cobol code.

Hope This Help :-)
```

##### ↳ ↳ Re: MF COBOL with Visual Basic Interface How can this be done?

- **From:** "pri..." <ua-author-17072105@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8dbdf69f9d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8dbdf69f9d-p4@usenetarchives.gap>`
- **References:** `<01bccf4d$b338b240$0100a8c6@alf> <gap-8dbdf69f9d-p4@usenetarchives.gap>`

```

Jim Morcombe wrote:

hello,
you can create a DLL with inside the cobol routine ad call them from
VB. The application have the Windows interface from VB3 with the
Cobol code.

Hope This Help :-)
Ugo
```

#### ↳ Re: MF COBOL with Visual Basic Interface How can this be done?

- **From:** "michael vanbrocklin" <ua-author-17073255@usenetarchives.gap>
- **Date:** 1997-10-01T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8dbdf69f9d-p7@usenetarchives.gap>`
- **In-Reply-To:** `<01bccf4d$b338b240$0100a8c6@alf>`
- **References:** `<01bccf4d$b338b240$0100a8c6@alf>`

```

in the mf cobol directory under samples you should find a subdirectory
called vbdemo with just the code you need. it is a simple vb data collector
that passed the data to cobol for writing to an isam file.

If you do not find these files respond as such and we will figure out a way
to get them to you.
```

#### ↳ Re: MF COBOL with Visual Basic Interface How can this be done?

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8dbdf69f9d-p8@usenetarchives.gap>`
- **In-Reply-To:** `<01bccf4d$b338b240$0100a8c6@alf>`
- **References:** `<01bccf4d$b338b240$0100a8c6@alf>`

```

On 2 Oct 1997 04:17:12 GMT, "alf" wrote:

› I was currently assigned a project which uses MicroFocus COBOL, but
› requires 
…[5 more quoted lines elided]…
› no more than a DOS executable.

your teacher is stupid. MFCobol for DOS does not link with visual
basic for windows, unless you want to make calls from cobol to
assembly, or write a data file, run the cobol, and return. in ANY
case, this out-of-language call takes many processing cycles.

however, you could call visual C or visual Cobol from visual basic
easier, but that requires that you look up the linking to other
languages section, and get a different compiler.

also, as another poster said, maintaining two languages is harder than
one (unless this is only a graduate project which can run extremely
slow and has no real-world application). choose one language and go
with it.
```

#### ↳ Re: MF COBOL with Visual Basic Interface How can this be done?

- **From:** "john the hedgehog" <ua-author-17071484@usenetarchives.gap>
- **Date:** 1997-10-11T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8dbdf69f9d-p9@usenetarchives.gap>`
- **In-Reply-To:** `<01bccf4d$b338b240$0100a8c6@alf>`
- **References:** `<01bccf4d$b338b240$0100a8c6@alf>`

```

alf wrote:
› 
› I was currently assigned a project which uses MicroFocus COBOL, but
…[13 more quoted lines elided]…
›                                                         rfr··.@m··.net

I've used Visual Object Cobol to provide a GUI interface to an old Cobol
suite and it works beautifully. Of course VOC has been superseded by
NetExpress at $3,650 dollars in the US and $5,840 in the UK, but the
principle's the same (see http://www.microfocus.com for more details).
Where do drawing-board designers go when their products fail?
-------------------------------------------------------------------
John Rogers, Aizoon Computing Limited, Bristol, England
Remove .spamless to e-mail.
See also http://wkweb4.cableinet.co.uk/JohnRogers/pond.htm
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
