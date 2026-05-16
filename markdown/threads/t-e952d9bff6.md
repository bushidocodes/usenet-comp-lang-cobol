[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PC_PRINTER_OPEN Routine

_5 messages · 5 participants · 2002-06_

---

### PC_PRINTER_OPEN Routine

- **From:** "Ralph Leiherr" <leiherr@vwda.de>
- **Date:** 2002-06-27T17:08:12+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aff9nu$fhg$00$1@news.t-online.com>`

```
Hi all,

my Cobol-Compiler is MicroFocus NetExpress 3.1, my operating-system is
Windows-NT 4.0 Sp6a.

So, I use the "'PC_PRINTER_OPEN" - Routine zu select the Printer that the
client need to print. I have a programm who use this routine. I wrote this
programm about 1 year - and never change the code but this code is tested
only by the operation-system WIN-NT 4.0.

We must change the operation-system of the clientï¿½s to Windows 2000
Professional. Now my routine donï¿½t work.

Has anybody one idee ??

Thanks

Ralph
```

#### ↳ Re: PC_PRINTER_OPEN Routine

- **From:** "Mike Kinasz" <mkinasz@cbspayroll.com>
- **Date:** 2002-06-28T04:18:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<asRS8.18625$Uu2.2880@sccrnsc03>`
- **References:** `<aff9nu$fhg$00$1@news.t-online.com>`

```
If it were me in that particular situation and using NE3.1 then i'd convert
your print routines to use Windows API (i only say this because we use these
routines and they work quite well.  i'm sorry i can't post sample source for
this particular item...)

Here's a list of calls you'd need

OpenPrinterA
StartDocPrinterA
StartPagePrinter
WritePrinter
EndPagePrinter
EndDocPrinter
ClosePrinter

GetLastError helps too if you have a problem.  (TIP:  Also pass a null
termed "RAW" string as the datatype for your StartDocPrinterA call in the
Datatype field.)   I'm pretty sure MF has some examples in their
knowledgebase.......

Maybe someone else has some better advice...... who knows..

Good Luck,
Mike


"Ralph Leiherr" <leiherr@vwda.de> wrote in message
news:aff9nu$fhg$00$1@news.t-online.com...
> Hi all,
>
…[18 more quoted lines elided]…
>
```

##### ↳ ↳ Re: PC_PRINTER_OPEN Routine

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-06-28T05:58:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D1BFBAC.ED2FDE81@shaw.ca>`
- **References:** `<aff9nu$fhg$00$1@news.t-online.com> <asRS8.18625$Uu2.2880@sccrnsc03>`

```


Mike Kinasz wrote:

> If it were me in that particular situation and using NE3.1 then i'd convert
> your print routines to use Windows API (i only say this because we use these
…[18 more quoted lines elided]…
> Maybe someone else has some better advice...... who knows..

If it's only semi broke then  fix it <G>. He's probably got a lot of working
code using PC_PRINT. Ralph go ask you question at the new Answer Exchange, (used
to be Answerlab) :-

The following from Calin should get you there :-

> > Try this: http://supportline.microfocus.com/
> > From here go to "Self service" on the left menu bar and then choose
"answer
> > exchange".  You can safely disregard the user-name and password up to
here, as
> > this link will take you (as Alan said) to the cobol portal site.
There's a bit
> > more to this: at the bottom of the page you're in (some "I agree"
message),
> > there's an "Answer Exchange" link
> >
…[3 more quoted lines elided]…
> > Calin, TORONTO

when you've "joined" the following bookmark should take you direct to Answer
Exchange :-

http://forum.microfocus.com/~Micro_Focus_Products/login

Jimmy, Calgary AB
```

#### ↳ Re: PC_PRINTER_OPEN Routine

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-06-28T07:50:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D1C0752.1A34D210@Azonic.co.nz>`
- **References:** `<aff9nu$fhg$00$1@news.t-online.com>`

```
Ralph Leiherr wrote:
> 
> We must change the operation-system of the client's to Windows 2000
> Professional. Now my routine don't work.

Thank you Microsoft.

As they say: "The job ain't done 'til Lotus won't run."

;-)
```

#### ↳ Re: PC_PRINTER_OPEN Routine

- **From:** jean.villemaire@microfocus.com (Jean Villemaire)
- **Date:** 2002-06-28T12:00:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b9b30ab.0206281100.395b22a5@posting.google.com>`
- **References:** `<aff9nu$fhg$00$1@news.t-online.com>`

```
"Ralph Leiherr" <leiherr@vwda.de> wrote in message news:<aff9nu$fhg$00$1@news.t-online.com>...
> Hi all,
> 
…[15 more quoted lines elided]…
> Ralph

Ralph,

Make sure that the printer-handle and windows-handle parameters of
your PC_PRINTER_OPEN call are initialzed properly;

           move 0 to Window-Handle
           move 0 to Printer-Handle

           call "PC_PRINTER_OPEN" using
               by reference Printer-Handle
               by reference Document-Title
               by value     Printer-Flags
               by value     Window-Handle
           end-call


You can find examples of the PC_PRINTER calls at
http://supportline.microfocus.com under Self Services click on Net
Express examples & Utilities and go on the samples page and choose the
printing category.  A zip file called pcprintercalls.zip will have
several demo programs.

Hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
