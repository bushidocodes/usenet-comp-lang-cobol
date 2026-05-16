[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# graphical printing from cobol

_6 messages · 4 participants · 2001-01_

---

### graphical printing from cobol

- **From:** fiuka@my-deja.com
- **Date:** 2001-01-29T12:34:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<953o0r$k6b$1@nnrp1.deja.com>`

```
I want to print graphical (jpg e.g.) from a cobol-program. Does anybody
know how I can do that? Could it be possible to change the printer-
language to PJL then to postscript and then print the file?
Mainly it will be used to print a little symbol for our firm-symbol
in graphical form and the remainder of the printjob is in ascii.

Compiler: MF-Object-Cobol V4.1.06 on IBM-AIX (RS/6000)
the printer: HP-Laserjet 4


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: graphical printing from cobol

- **From:** flexus@epix.net (Bob Wolfe)
- **Date:** 2001-01-29T20:31:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a75d21c.26625789@news.epix.net>`
- **References:** `<953o0r$k6b$1@nnrp1.deja.com>`

```
fiuka@my-deja.com wrote:

>I want to print graphical (jpg e.g.) from a cobol-program. Does anybody
>know how I can do that? Could it be possible to change the printer-
…[9 more quoted lines elided]…
>http://www.deja.com/


Fiuka:

If you have PC's also connected to the laser printer, our Thin Client
and COBOL FormPrint combination will do this for you very easily.

The Thin Client server software can run on Windows 32 bit servers or
UNIX servers (including IBM AIX based RS6000 boxes).  The FormPrint
components run on Windows PC's and print directly to the Windows Print
Manager.

The only additional requirement is that there is a TCP/IP connection
between the RS6000 and any PC which is connected to the laser jet.

Visit http://www.flexus.com for more details.


Bob Wolfe, flexus
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: graphical printing from cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-30T07:45:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A767103.461F0BAA@Azonic.co.nz>`
- **References:** `<953o0r$k6b$1@nnrp1.deja.com>`

```
fiuka@my-deja.com wrote:
> 
> I want to print graphical (jpg e.g.) from a cobol-program. Does anybody

I don't think that you would want to hand code .jpg handling code in
Cobol, or in fact in any language.  

> know how I can do that? Could it be possible to change the printer-
> language to PJL then to postscript and then print the file?

Were you wanting to reprogram the Laserjet so that it could handle
postscript ?  If the printer does actually have postscript handling
capability then you can send codes to it to change to postscript, and
then send all your output as postscript.

> Mainly it will be used to print a little symbol for our firm-symbol
> in graphical form and the remainder of the printjob is in ascii.
> 
> Compiler: MF-Object-Cobol V4.1.06 on IBM-AIX (RS/6000)
> the printer: HP-Laserjet 4

I have programmed in Cobol to send .BMPs to various dot matrix
printers.  This wasn't too hard as they are only bitmaps with no
compression, no trick stuff.  It just takes transformations to print it
backwards inverting each 7 bits taken from 7 lines at a time and sending
to the printer.

I haven't done it for Laserjets though.
```

##### ↳ ↳ Re: graphical printing from cobol

- **From:** fiuka@my-deja.com
- **Date:** 2001-01-30T07:22:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<955q4a$el8$1@nnrp1.deja.com>`
- **References:** `<953o0r$k6b$1@nnrp1.deja.com> <3A767103.461F0BAA@Azonic.co.nz>`

```
In article <3A767103.461F0BAA@Azonic.co.nz>,
  Richard Plinston <riplin@Azonic.co.nz> wrote:
> >
> I don't think that you would want to hand code .jpg handling code in
> Cobol, or in fact in any language.

No, my problem is, that I have to use an existing jpg-file, which comes
from MS-Windows. I tried to print this file on UNIX with different
methodes. My first test was: I printed the jpg-file on Windows into a
file instead to a printer. This file I could print on UNIX with
different commands linke qprt or so. That's why I think, it MUST be
possible to do this from a COBOL-Program (maybe with call "SYSTEM"),
but then the printer prints the picture and ejects the paper and the
remainder of my program-output is printed on the next sheet.

> Were you wanting to reprogram the Laserjet so that it could handle
> postscript ?  If the printer does actually have postscript handling
> capability then you can send codes to it to change to postscript, and
> then send all your output as postscript.
I dont't have any knowlidge in postscript. I send all my print-output
from COBOL with PCL-commands. But I found a command to change the
printer-language to postscript. I thougt, with this I would be able to
print a jpg file and change then the printer-language back to pcl for
the other printing.


Sent via Deja.com
http://www.deja.com/
```

###### ↳ ↳ ↳ Re: graphical printing from cobol

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-31T08:25:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A77CBED.B081C877@Azonic.co.nz>`
- **References:** `<953o0r$k6b$1@nnrp1.deja.com> <3A767103.461F0BAA@Azonic.co.nz> <955q4a$el8$1@nnrp1.deja.com>`

```
fiuka@my-deja.com wrote:
> 
> No, my problem is, that I have to use an existing jpg-file, which comes

You could process it to a .BMP using Paint-Shop or similar.  

> I dont't have any knowlidge in postscript. I send all my print-output
> from COBOL with PCL-commands. But I found a command to change the
> printer-language to postscript. I thougt, with this I would be able to
> print a jpg file and change then the printer-language back to pcl for
> the other printing.

Postscript is a different language.  I suspect that changing to
postscript or back would reset the printer page.  One way to print
postsscript is to create a template file using a drawing program that
will output postscript and to include 'fields' by, say, putting specific
markers like <!%FIELDNAME%> over the page where output is to go.  Then
this can be read into your program with the <!%...%> markers substituted
with actual data.  Al the fonts and fixed data is in the template.

This does take some fiddling to get the right paint program (eg
StarOffice isn't) and getting the merge right, but then if the template
printing is in a called routine it can be reused for other reports.

Or buy a program that does this.
```

#### ↳ Re: graphical printing from cobol

- **From:** "Paulo Vieira" <pvieira@emporsoft.pt>
- **Date:** 2001-01-30T10:57:43
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9566t2$mcg$1@venus.telepac.pt>`
- **References:** `<953o0r$k6b$1@nnrp1.deja.com>`

```
I used to do that a few years ago, sending to the PCL printer a .bmp and an
escape sequence instructing the printer to treat it as a permanent overlay
image. That way, the image was kept in the printer's memory until
specificaly cleaned, and I was free to send my character listing which would
overprint the image.
I can't remember what the escape sequence was, but it should be documented
in your printer's manual.
By the way, don't forget to discard the image after printing your report,
otherwise every body else gets the same image in every listing.

best regards
Paulo Vieira, emporsoft

<fiuka@my-deja.com> wrote in message news:953o0r$k6b$1@nnrp1.deja.com...
> I want to print graphical (jpg e.g.) from a cobol-program. Does anybody
> know how I can do that? Could it be possible to change the printer-
…[9 more quoted lines elided]…
> http://www.deja.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
