[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Laser Printing from MFCOBOL 4.5

_13 messages · 9 participants · 2008-09_

---

### Laser Printing from MFCOBOL 4.5

- **From:** Nitin Kothari <nitkot@gmail.com>
- **Date:** 2008-09-11T05:26:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com>`

```
Hi,

I am using MFCOBOL 4.5 (DOS/Novell Version) to develop commercial
application from last 18 years. I have done lot of development during
this tenure. Around 40 large softwares has been developed by me
individually. I am heading community of users in India. It works fine
on all windows operating system upto from 98 to VISTA.

I came to know about this group recently and happy to know that people
are actively contributing to keep COBOL alive. I always call myself as
"Its not COBOL Over.... but I am COBO Lover.....

Many of my customer has now bought laser printer, They would like to
print output on laser printer instead of DOT Matrix printer.

There may be print out of large sheet paper of 132 column, which needs
to be condensed from software to print correctly on laser printer,
which we can easily do on dot matrix printer.

Can any one share their knowledge on same?

Awaiting your response to the earliest.

Nitin Kothari
Mumbai, India
9867696515
```

#### ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-11T07:52:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hw8yk.22771$89.9322@nlpi069.nbdc.sbc.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com>`

```
"Nitin Kothari" <nitkot@gmail.com> wrote in message 
news:8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com...

> am using MFCOBOL 4.5 (DOS/Novell Version) ....
> Many of my customer has now bought laser printer, They would like to
…[6 more quoted lines elided]…
> Can any one share their knowledge on same?

There should be an escape sequence you can send to the printer to throw it 
into "condensed" mode. This will be documented in the printer's owner's 
manual or reference manual. (Just like it works on your dot matrix).

That is, assuming this printer is NOT a 'Windows only' printer, in which 
case it will print only thru the Windows' driver. If a printer connects via 
USB port, good chance it's a "Windows-only" printer. Excellent chance 
actually. Um, make that  a virtual "lock."

If you can 'copy filename LPT1:'   from a command prompt and it prints (you 
may have to manually hit the 'form feed' button to eject the sheet), you are 
OK.

If this is a Windows'-only printer, you should be able to find a utilty 
which prints text files thru Windows facilities ....and you could call that 
as an external program from your COBOL program after generating your report 
to a disk file.  (I know such utilities exist.... eg in my "other language' 
group someone posted one for free use for others to use.  These utilities 
should offer an option for you to specify the font to be used, and selecting 
the correct font size/characteristics will handle the 'condensed' 
requirement.
```

##### ↳ ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-09-11T08:01:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v49ic4ls626o6fci1gqh32l1r75upltugb@4ax.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com> <Hw8yk.22771$89.9322@nlpi069.nbdc.sbc.com>`

```
On Thu, 11 Sep 2008 07:52:41 -0500, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>That is, assuming this printer is NOT a 'Windows only' printer, in which 
>case it will print only thru the Windows' driver. If a printer connects via 
>USB port, good chance it's a "Windows-only" printer. Excellent chance 
>actually. Um, make that  a virtual "lock."

My wife's USB printer works similarly with Mac drivers.  I don't know
how it works with Linux.   I suppose the driver accepts the same
commands.
```

##### ↳ ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-11T11:36:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e3e2ef02-ebf5-4da4-8af8-5721fa699bfe@q5g2000prf.googlegroups.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com> <Hw8yk.22771$89.9322@nlpi069.nbdc.sbc.com>`

```
On Sep 12, 12:52 am, "Michael Mattias" <mmatt...@talsystems.com>
wrote:
> "Nitin Kothari" <nit...@gmail.com> wrote in message
>
…[19 more quoted lines elided]…
> actually. Um, make that  a virtual "lock."

Not true. There is no relationship between the printer being a 'GDI'
device and the interface used. GDI may be parallel port, USB or
network, but full PCL or PS printers will also use these.

In fact just yesterday I installed a new OKI B4600 PCL page printer
using USB.

> If you can 'copy filename LPT1:'   from a command prompt and it prints (you
> may have to manually hit the 'form feed' button to eject the sheet), you are
> OK.

It is unlikely that this will work without first setting the printer
to 'capture' LPT1.


> If this is a Windows'-only printer, you should be able to find a utilty
> which prints text files thru Windows facilities ....and you could call that
…[11 more quoted lines elided]…
> mmatt...@talsystems.com
```

#### ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-09-11T12:02:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f354996-ee8b-4a55-82d1-a7efebc5cd8a@n33g2000pri.googlegroups.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com>`

```
On Sep 12, 12:26 am, Nitin Kothari <nit...@gmail.com> wrote:
> Hi,
>
> I am using MFCOBOL 4.5 (DOS/Novell Version) to develop commercial

That is probably MicroSoft COBOL 4.5 which is a version of Microfocus
(MF) 3.x.

> application from last 18 years. I have done lot of development during
> this tenure. Around 40 large softwares has been developed by me
…[8 more quoted lines elided]…
> print output on laser printer instead of DOT Matrix printer.

If it is an HP or emulates it and supports PCL then the hex codes that
I would use are:

0x1B451B266C314F
0x1B2838551B2873307031362E363668382E3576307330623054
0x1B266C3844
0x1B266131354C

Note that 1B is escape and starts a string that ends with an upper
case letter that is the actual command. Lower case letters are also
commands but don't end the string. Escape indicated by @:

@E                      reset
@&l1O                   orientation landscape
@(8U                    can't remember
@(s0p16.66h8.5v0s0b0T   16.66 cpi 8.5 lpi fixed font
@&l8D                   top margin ??
@&a15L                  left margin 15

I have these strings in a control file that has different settings
depending on what the user requires.

If the printer is not PCL then it may have emulations that could be
used instead, such as IBM Proprinter.

The printer will need to be set to 'capture' a port that the program
can access, such as 'LPT1'. Some GDI drivers can, some will not. Most
real printer (non GDI) drivers can, after setting them to share, with

net use LPT1 \\server\sharename

(may not work on XP Home or other limited version, with Vista: don't
know, don't care, don't want to know)

You may need to ensure that the print driver has a 'raw' setting for
these to pass through.


> There may be print out of large sheet paper of 132 column, which needs
> to be condensed from software to print correctly on laser printer,
…[8 more quoted lines elided]…
> 9867696515
```

##### ↳ ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2008-09-11T19:01:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a609effa-1f92-4417-9cc6-8d8aca25fd15@n33g2000pri.googlegroups.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com> <5f354996-ee8b-4a55-82d1-a7efebc5cd8a@n33g2000pri.googlegroups.com>`

```
>
> > I am using MFCOBOL 4.5 (DOS/Novell Version) to develop commercial
…[3 more quoted lines elided]…
>

If you are using MF NetExpress devtool, then you can use several
options (refer to URL link) from their sample applications.

http://supportline.microfocus.com/examplesandutilities/nesamp.asp#Printing

For Microfocus support, the above site is a great help.


Rene
```

#### ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2008-09-12T10:18:41+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48ca2636$0$2865$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com>`

```
Nitin,

An interessant alternative might be RPV Report from RPVSoftware.
Otherwise, you will have to deal with PCL codes.

Regards

Alain

Nitin Kothari a ï¿½crit :
> Hi,
>
…[25 more quoted lines elided]…
>
```

#### ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-16T10:41:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rrednS2ah6RYTlLVnZ2dnUVZ_umdnZ2d@earthlink.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com>`

```
Nitin Kothari wrote:
> Hi,
>
…[23 more quoted lines elided]…
> 9867696515

You have two problems. Laser (page) printers have lots of additional 
commands that are necessary: Font, font size, margins, page length, stroke 
weight, lines-per-inch, characters-per-inch, paper size, tray, etc. About 
100 bytes. Fortunately, these commands can be stored in a file which you 
must send to the printer every time you open the print file.

Your second problem is printing to a port other than LPT1(2), especially XP, 
2000, and Vista which do not allow "Capture Printer Port."

There are techniques for so doing on Windows machines involving pooling the 
printer port. One can be found here:

http://members.shaw.ca/bsanders/printfromdos.htm

Possibly the easiest is the program RPV (Report Program Viewer) already 
mentioned if you can still find the free version. RPV works as follows: You 
must direct all your printing to a file at a specific location, instead of 
the printer. RPV (running in the background) continually monitors this 
location and, when it finds a file in the folder, grabs the file and sends 
it to the Windows print spooler.

Of course this presumes you were foresighted enough to put all your printing 
commands in a sub-program so you don't have to make thousands of changes to 
hundreds of programs...
```

##### ↳ ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** epc8@juno.com
- **Date:** 2008-09-16T12:54:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4639e8e3-f841-467c-87f6-7fe277d980fb@x41g2000hsb.googlegroups.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com> <rrednS2ah6RYTlLVnZ2dnUVZ_umdnZ2d@earthlink.com>`

```
On Sep 16, 11:41 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Nitin Kothari wrote:
> > Hi,
>
> > I am using MFCOBOL 4.5 (DOS/Novell Version) to develop commercial
> > application from last 18 years.

> > Many of my customer has now bought laser printer, They would like to
> > print output on laser printer instead of DOT Matrix printer.
>

> You have two problems. Laser (page) printers have lots of additional
> commands that are necessary: Font, font size, margins, page length, stroke
…[21 more quoted lines elided]…
> hundreds of programs

A Google search does not find RPV. But this might work. See

http://www.lerup.com/printfile/

The online docs say that PrintFile also acts as a printer spooler for
files in a particular directory. It also list command line options for
input. YMMV. I have NOT tried or installed this program.

- e
```

###### ↳ ↳ ↳ Re: Laser Printing from MFCOBOL 4.5

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-18T10:19:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6LmdnZhwvp_r7E_VnZ2dnUVZ_jqdnZ2d@earthlink.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com> <rrednS2ah6RYTlLVnZ2dnUVZ_umdnZ2d@earthlink.com> <4639e8e3-f841-467c-87f6-7fe277d980fb@x41g2000hsb.googlegroups.com>`

```
epc8@juno.com wrote:
> On Sep 16, 11:41 am, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
>> Nitin Kothari wrote:
…[44 more quoted lines elided]…
>

I think I found the old RPV here:

http://www.rpvsoftware.com/downloads.php

We used and distributed Version 2.00; maybe the available V2.2 will work.

Still, the concept is reasonable. A program that, once started, polls a 
specific folder for any new files every ten or thirty seconds. If a file is 
found, grab the file an send it to a printer defined at startup (or via 
command line variables).

Meanwhile, other ad hoc programs are diverting their print jobs to a file in 
the specified folder.

If someone wants to try RPV 2.0, email me privately and I'll send along the 
copy I have (orginally marked 'freely distributable').

As an aside, this illustrates the wonderfulness of putting I/O in a 
sub-program. In our case, it was a, maybe, ten-line change to optionally 
divert printing to a file instead of LPT1. Re-link of 80 programs and we 
were good to go.
```

###### ↳ ↳ ↳ Re: Laser Printing from MFCOBOL 4.5

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-09-18T14:17:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PRxAk.506$pr6.63@flpi149.ffdc.sbc.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com> <rrednS2ah6RYTlLVnZ2dnUVZ_umdnZ2d@earthlink.com> <4639e8e3-f841-467c-87f6-7fe277d980fb@x41g2000hsb.googlegroups.com> <6LmdnZhwvp_r7E_VnZ2dnUVZ_jqdnZ2d@earthlink.com>`

```
"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:6LmdnZhwvp_r7E_VnZ2dnUVZ_jqdnZ2d@earthlink.com...
> As an aside, this illustrates the wonderfulness of putting I/O in a 
> sub-program. In our case, it was a, maybe, ten-line change to optionally 
> divert printing to a file instead of LPT1. Re-link of 80 programs and we 
> were good to go.

So near, yet so far....

Wouldn't have had to re-link anything if you had called the I-O module 
dynamically.

MCM
```

###### ↳ ↳ ↳ Re: Laser Printing from MFCOBOL 4.5

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-09-18T18:06:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s42dnX89HsNrQ0_VnZ2dnUVZ_rmdnZ2d@earthlink.com>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com> <rrednS2ah6RYTlLVnZ2dnUVZ_umdnZ2d@earthlink.com> <4639e8e3-f841-467c-87f6-7fe277d980fb@x41g2000hsb.googlegroups.com> <6LmdnZhwvp_r7E_VnZ2dnUVZ_jqdnZ2d@earthlink.com> <PRxAk.506$pr6.63@flpi149.ffdc.sbc.com>`

```
Michael Mattias wrote:
> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
> news:6LmdnZhwvp_r7E_VnZ2dnUVZ_jqdnZ2d@earthlink.com...
…[9 more quoted lines elided]…
>

Well, yeah. But in an old DOS suite, it seemed easier...
```

###### ↳ ↳ ↳ Re: Laser Printing from MFCOBOL 4.5

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-09-20T03:49:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ji002F3eet9U1@mid.individual.net>`
- **References:** `<8a8711d3-2898-4129-90a1-695c8818b1e4@b2g2000prf.googlegroups.com> <rrednS2ah6RYTlLVnZ2dnUVZ_umdnZ2d@earthlink.com> <4639e8e3-f841-467c-87f6-7fe277d980fb@x41g2000hsb.googlegroups.com> <6LmdnZhwvp_r7E_VnZ2dnUVZ_jqdnZ2d@earthlink.com> <PRxAk.506$pr6.63@flpi149.ffdc.sbc.com> <s42dnX89HsNrQ0_VnZ2dnUVZ_rmdnZ2d@earthlink.com>`

```


"HeyBub" <heybub@NOSPAMgmail.com> wrote in message 
news:s42dnX89HsNrQ0_VnZ2dnUVZ_rmdnZ2d@earthlink.com...
> Michael Mattias wrote:
>> "HeyBub" <heybub@NOSPAMgmail.com> wrote in message
…[13 more quoted lines elided]…
>
I am an ardent supporter of tiered architecture, with separation layers 
(interfaces).

There are SO many benefits in doing this which are simply not apparent when 
you first do it. After you implement a few systems using this architecture, 
and some years go by, you suddenly find benefits which you couldn't envision 
crawling out of the woodwork. Swap the data resource to the latest 
technology (maybe even a new technology...), but don't change the business 
logic...? Easy. Want to move from green screens to GUI? Easy. The list goes 
on.

I'm sold.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
