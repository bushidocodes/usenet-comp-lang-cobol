[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Acucobol printing with VISTA

_5 messages · 4 participants · 2009-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Acucobol printing with VISTA

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2009-05-02T11:37:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52659c1b-cdd1-433d-be93-bf85823afd14@s28g2000vbp.googlegroups.com>`

```
Hi,
in my ACUCOBOL (4.3) programs I use to print my reports using the
configuration option
PRINTER -P SPOOLER-DIRECT

I normally open a file using the port name or the netwoork address of
the printer

open output LPT1
or
open output \\server\hplj4200

All this worked fine with WindowsXP and Server2003 but I'm facing a
big problem using Windows Vista.
I cannot print on networked printers.
I tried
net use LPT1 \\comp_name\Printer_name
without any success.

The software works only if I have a printer fisically connected to the
port.

Did someone have any suggestion ?

Thanks

Giovanni.
```

#### ↳ Re: Acucobol printing with VISTA

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-03T12:56:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7648d3F1aqgj7U1@mid.individual.net>`
- **References:** `<52659c1b-cdd1-433d-be93-bf85823afd14@s28g2000vbp.googlegroups.com>`

```
Gio wrote:
> Hi,
> in my ACUCOBOL (4.3) programs I use to print my reports using the
…[21 more quoted lines elided]…
>

One way to solve this is to install a "print-to-file" printer driver, then 
select that as the printer.

Install the driver for the printer you currently use, using add a printer in 
Control Panel.  When the wizard asks what port to use say: "FILE:"

Give this copy of the driver a different printer name in your printer 
selection options and then just use that "printer" when you want to print to 
file, and the real printer when you want hard copy.

HTH,

Pete.
```

##### ↳ ↳ Re: Acucobol printing with VISTA

- **From:** Gio <giovanni_dimaio@virgilio.it>
- **Date:** 2009-05-03T17:08:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20742563-7661-4141-9105-3c20afda7043@b1g2000vbc.googlegroups.com>`
- **References:** `<52659c1b-cdd1-433d-be93-bf85823afd14@s28g2000vbp.googlegroups.com> <7648d3F1aqgj7U1@mid.individual.net>`

```
On May 3, 2:56 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Gio wrote:
> > Hi,
…[37 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

Thanks Pete,
this will work fine for standard reports but my main concern is for
some invoices that for some reasons have to go directly to the
prenumbered folios.

G
```

###### ↳ ↳ ↳ Re: Acucobol printing with VISTA

- **From:** rtwolfe <rtwolfe@flexus.com>
- **Date:** 2009-05-03T17:24:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d59347a9-9c61-44f9-b220-a78878fd0c47@n4g2000vba.googlegroups.com>`
- **References:** `<52659c1b-cdd1-433d-be93-bf85823afd14@s28g2000vbp.googlegroups.com> <7648d3F1aqgj7U1@mid.individual.net> <20742563-7661-4141-9105-3c20afda7043@b1g2000vbc.googlegroups.com>`

```
On May 3, 8:08 pm, Gio <giovanni_dim...@virgilio.it> wrote:
>
> Thanks Pete,
…[6 more quoted lines elided]…
> - Show quoted text -

Gio:

Take a look at our FormPrint product.  It will not only help you
resolve your printing problems, it is also 100% COBOL compiler
independent and we also offer add-on products which support printing
documents to PDF format and automatically sending electronic documents
via e-mail attachment.

http://www.flexus.com/formprint.html

I'll also be happy to answer any of your questions on the product.
```

#### ↳ Re: Acucobol printing with VISTA

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-05-04T09:20:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gtmv1n0252k@news7.newsguy.com>`
- **In-Reply-To:** `<52659c1b-cdd1-433d-be93-bf85823afd14@s28g2000vbp.googlegroups.com>`
- **References:** `<52659c1b-cdd1-433d-be93-bf85823afd14@s28g2000vbp.googlegroups.com>`

```
Gio wrote:
> 
> All this worked fine with WindowsXP and Server2003 but I'm facing a
> big problem using Windows Vista.
> I cannot print on networked printers.

I see you've already received some suggestions which may resolve this
for you, but if not:

- Are you running your applications normally, from the desktop?
They're not running as Windows services or anything like that, are
they? Vista (and Server 2008) did significantly improve the separation
between processes running in different contexts, and this has broken a
number of programs that worked (but were security holes) in earlier
versions of Windows.

- Vista apparently includes several mysterious changes to printing
support. I've seen a handful of customer printing issues with AcuCOBOL
on Vista, and they're often in code that's entirely outside Acu - in
the Windows printing API, system dialogs, drivers, etc. (For example,
configuring multiple copies in the Windows printer driver dialog
apparently no longer works on Vista; the option is there, but setting
it has no effect.) These are Windows bugs, and there's nothing we can
do about them. This doesn't sound like that sort of problem, but it's
difficult to tell.

- Have you tried printing to the network printer from another program?
That seems obvious, but you didn't say so in your original note, so I
thought I should ask.

- Have you contacted MF support with this issue?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
