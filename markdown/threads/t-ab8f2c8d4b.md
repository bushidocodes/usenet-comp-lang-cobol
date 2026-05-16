[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# InkJet Printer Support anyone?

_9 messages · 7 participants · 2001-01_

---

### InkJet Printer Support anyone?

- **From:** "Sam" <Music98@Mindspring.com>
- **Date:** 2001-01-15T19:47:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<940997$shg$1@slb3.atl.mindspring.net>`

```
Hi All;

I'm working with Micro Focus 3.1 and would like to use my Lexmark InkJet to
produce reports.  So far I've been unsuccessful in getting the printer's
control program to process the output from the PC.

Anyone know the control-codes/escape-sequences necessary to overcome this?

--Sam

__________________________________________________________________________
Stop USFSPA Abuse!  Sign a petition at:

http://www.e-thepeople.com/affiliates/messengerinquirer/index.cfm?PC=PETFV1&
PETID=482614

'Till Death Do Us Part should not apply "ONLY" to Military Retirement Pay!
```

#### ↳ Re: InkJet Printer Support anyone?

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-01-16T02:07:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-Kp3KvSs2i9qI@tcpserver>`
- **References:** `<940997$shg$1@slb3.atl.mindspring.net>`

```
On Tue, 16 Jan 2001 01:47:34, "Sam" <Music98@Mindspring.com> wrote:

> Hi All;
> 
…[6 more quoted lines elided]…
> --Sam

You probably have to use the PC_PRINTER_xxxx routines to use the 
Inkjet printers. A lot of the inkjet printers are "mindless 
win-printers" and must be accessed through the printer driver supplied
by the manufacturer. There is no "printer command language" like PCL 
or Postscript for these things, they depend on the Windows print 
driver to rasterize the output and direct the bits to the printer.
```

##### ↳ ↳ Re: InkJet Printer Support anyone?

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-01-16T07:51:38-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A647C19.AB2474B1@dced.state.ak.us>`
- **References:** `<940997$shg$1@slb3.atl.mindspring.net> <ZpzG4UNLyRNq-pn2-Kp3KvSs2i9qI@tcpserver>`

```
lsunley@mb.sympatico.ca wrote:

> On Tue, 16 Jan 2001 01:47:34, "Sam" <Music98@Mindspring.com> wrote:
>
…[18 more quoted lines elided]…
> Lorne Sunley

Lexmarks might be "mindless win-printers" but I've not found this true of other
inkjets. Are you sure you aren't letting one brand prejudice you against an
entire technology?
```

###### ↳ ↳ ↳ Re: InkJet Printer Support anyone?

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-01-16T19:53:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-dddZdMKj93H4@tcpserver>`
- **References:** `<940997$shg$1@slb3.atl.mindspring.net> <ZpzG4UNLyRNq-pn2-Kp3KvSs2i9qI@tcpserver> <3A647C19.AB2474B1@dced.state.ak.us>`

```
On Tue, 16 Jan 2001 16:51:38, Calvin Crumrine 
<Calvin_Crumrine@dced.state.ak.us> wrote:

> lsunley@mb.sympatico.ca wrote:
> 
…[25 more quoted lines elided]…
> 

Not really, you will notice that I did not name Lexmarks as a 
particular "mindless win-printer" source. Almost all manufacturers 
seem to have several models of inkjet printers that are "host based" 
or "mindless win-printers". You can usually pick them out because they
always require "Windows XX" as an operating system and do not mention 
support of a particular command language (not to mention they are 
usually the "most inexpensive"). HP, Lexmark, Canon all have one or 
models.

One other problem that I forgot to mention - even if the printer is 
not a "mindless win-printer" the driver may require you to select 
"support DOS printing" during installation. Without that support 
Windows will not provide you with the ability to open a line 
sequential file on "LPTx" and write to it.

The PC_PRINTER_xxx library calls allow you to access to basic printer 
functions and font control. If you want to do more complex page 
handling the PC_PRINT_OPEN? call returns the handle to the Windows 
device context and you can use that to call any of the Windows 
graphics drawing APIs to do whatever you want on the printer.
```

###### ↳ ↳ ↳ Re: InkJet Printer Support anyone?

_(reply depth: 4)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-01-16T12:25:26-09:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A64BC46.DE48D9E2@dced.state.ak.us>`
- **References:** `<940997$shg$1@slb3.atl.mindspring.net> <ZpzG4UNLyRNq-pn2-Kp3KvSs2i9qI@tcpserver> <3A647C19.AB2474B1@dced.state.ak.us> <ZpzG4UNLyRNq-pn2-dddZdMKj93H4@tcpserver>`

```


lsunley@mb.sympatico.ca wrote:

> Not really, you will notice that I did not name Lexmarks as a
> particular "mindless win-printer" source. Almost all manufacturers
…[20 more quoted lines elided]…
> Lorne Sunley

Apparently I misunderstood your original posting. I took it as you saying that a lot
of the inkjet printers were 'mindless win-printers' which is incorrect. I won't argue
that all inkjet printer manufacturers have produced at least one model which is a
mindless win-printer. It's true of all *manufacturers* that I know of but it isn't
true of all inkjet *printers* I know of. Several come to mind that *will* print a
text file simply by copying it to LPTx. *Some* of those 'require' Windows because
they only ship with Windows drivers. They also support a 'printer control language'
although it's often expressed as an 'emulation mode' and is for a dot-matrix printer,
usually an Epson. (By the way, I just realized that these are several years old so
maybe they aren't manufactured any more. Maybe you're right about all currently
manufactured inkjet printers.)

Anyway, my comment re: Lexmark was to accept what I understood to be your comment
about *all* inkjet printers as possibly applying to all *Lexmark* inkjet printers.
(This is because I'm not familiar with Lexmark inkjet printers.) This was not meant
to imply that some non-Lexmark inkjet printers don't share the same failings, only
that not all of them do.
```

###### ↳ ↳ ↳ Re: InkJet Printer Support anyone?

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2001-01-17T04:46:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sk8a6t4n8psvg18sc47g7rufmk0ldjp175@4ax.com>`
- **References:** `<940997$shg$1@slb3.atl.mindspring.net> <ZpzG4UNLyRNq-pn2-Kp3KvSs2i9qI@tcpserver> <3A647C19.AB2474B1@dced.state.ak.us>`

```
>> --
>> Lorne Sunley
…[3 more quoted lines elided]…
>entire technology?

Some HP also have the same problem, some Lexmark the same, same OKI
(laser), and there are others.


ff
```

#### ↳ Re: InkJet Printer Support anyone?

- **From:** Warren Porter <wbport4@bellsouth3.net>
- **Date:** 2001-01-16T18:03:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A64E141.99117F02@bellsouth3.net>`
- **References:** `<940997$shg$1@slb3.atl.mindspring.net>`

```
You might want to contact the maker of your printer for this information.  I was
able to "print" an escape sequence for an HP printer a few years ago, but
nothing is available for my Epson at home.  The printer would have to have its
own memory to handle escape sequences.  If the print driver converts text into
Run Length Encoding (fire the ink jet when you get here and for this long), you
might be out of luck trying to go around that.

Sam wrote:

> Hi All;
>
…[4 more quoted lines elided]…
> Anyone know the control-codes/escape-sequences necessary to overcome this?
```

##### ↳ ↳ Re: InkJet Printer Support anyone?

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-01-17T02:18:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Oh796.4093$KE.213456@newsread2.prod.itd.earthlink.net>`
- **References:** `<940997$shg$1@slb3.atl.mindspring.net> <3A64E141.99117F02@bellsouth3.net>`

```

"Warren Porter" <wbport4@bellsouth3.net> wrote in message
news:3A64E141.99117F02@bellsouth3.net...
> You might want to contact the maker of your printer for this
information.  I was
> able to "print" an escape sequence for an HP printer a few years
ago, but
> nothing is available for my Epson at home.  The printer would have
to have its
> own memory to handle escape sequences.  If the print driver converts
text into
> Run Length Encoding (fire the ink jet when you get here and for this
long), you
> might be out of luck trying to go around that.
>

Exactly. Printer manufacturers can save $2.35 per printer by putting
the escape decode logic in Windows software rather than a chip inside
the printer. $2.35 here, $2.35 there. It adds up.
```

#### ↳ Re: InkJet Printer Support anyone?

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-01-18T01:17:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a6643ac.129779204@news1.attglobal.net>`
- **References:** `<940997$shg$1@slb3.atl.mindspring.net>`

```
If you want to create some really nice printouts with pictures,
different fonts, or even if you just want to create simple reports
from your COBOL programs, you should check out COBOL Form Print from
Flexus (http://www.flexus.com).  It's a breeze and makes printing to
ANY windows based printer from your COBOL program easy and fast.

On Mon, 15 Jan 2001 19:47:34 -0600, "Sam" <Music98@Mindspring.com>
wrote:

>Hi All;
>
…[16 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
