[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Net Express v5.- personal edition

_6 messages · 6 participants · 2007-06_

---

### Net Express v5.- personal edition

- **From:** "Vince Coen" <VBCoenDespawn@btconnect.com>
- **Date:** 2007-06-02T14:07:36
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180789656@f609.n257.z2.fidonet.ftn>`

```
Hello All!

I'm having a problem converting some old Workbench programs to NE.

The biggest problem is just to print out reports.

Original assign clause is Select print-rep assign "PRN:".
This doesn't work and have also tried assign printer as well as assign printer 
"print.txt".
This last one does work to some point but I have to manually spool out the 
print.txt file.   How do you set printing up in NE to auto go to spool say to 
an HP laserjet 4000 ?

Any suggestions please, but don't forget there is a 2200 line limit on 
compiler.

Vince
```

#### ↳ Re: Net Express v5.- personal edition

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-06-02T08:57:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eIe8i.5423$u56.324@newssvr22.news.prodigy.net>`
- **References:** `<1180789656@f609.n257.z2.fidonet.ftn>`

```
"Vince Coen" <VBCoenDespawn@btconnect.com> wrote in message 
news:1180789656@f609.n257.z2.fidonet.ftn...

> I'm having a problem converting some old Workbench programs to NE.
>
> Original assign clause is Select print-rep assign "PRN:".

Boy, I'll say it's old. I haven't seen the "PRN:"  device used since MS-DOS.

> This doesn't work and have also tried assign printer as well as assign 
> printer
…[4 more quoted lines elided]…
> an HP laserjet 4000 ?

You don't say what your O/S is, but if it's Windows, there simply must be an 
official method of "Windows printing" in the compiler.

You may need to just send output to a file (should be simply 'ASSIGN 
filename' but check the manual) then either "ShellExecute  "print" 
"filename" . rest of params"  or shellexecute another program which does 
allow for some control over the device (ShellExecute always uses the default 
printer.)  ADVANCING is not going to work here, but ADVANCING 1  will be the 
result of doing exactly nothing; ADVANCING >1 [LINES] or  ADVANCING PAGE 
you'll have to do by outputting additional blank lines

 > Any suggestions please, but don't forget there is a 2200 line limit on
> compiler.

? What's this a demo version?

MCM
```

#### ↳ Re: Net Express v5.- personal edition

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-06-02T10:40:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13633qjp47vj268@news.supernews.com>`
- **References:** `<1180789656@f609.n257.z2.fidonet.ftn>`

```
Vince Coen wrote:
> Hello All!
>
…[12 more quoted lines elided]…
> compiler.

Try:
http://www.syntax.gr/departments/CobolSolutions/files/downloads/demos.htm#printing
```

#### ↳ Re: Net Express v5.- personal edition

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-06-02T11:51:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68KdnU9S5beeD_zbnZ2dnUVZ_jOdnZ2d@golden.net>`
- **In-Reply-To:** `<1180789656@f609.n257.z2.fidonet.ftn>`
- **References:** `<1180789656@f609.n257.z2.fidonet.ftn>`

```
Vince Coen wrote:
> Hello All!
> 
…[16 more quoted lines elided]…
> 

"PRN:" to my knowledge, has been obsolete since DOS 3.1.

Try assign to "LPT1:" or assign to "LPT2:".  You may also want to try 
"assign to printer.", as that is the standard way for selecting the 
default printer.

Donald
```

##### ↳ ↳ Re: Net Express v5.- personal edition

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-06-02T16:29:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180826941.553510.152330@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<68KdnU9S5beeD_zbnZ2dnUVZ_jOdnZ2d@golden.net>`
- **References:** `<1180789656@f609.n257.z2.fidonet.ftn> <68KdnU9S5beeD_zbnZ2dnUVZ_jOdnZ2d@golden.net>`

```
On Jun 2, 8:51 am, donald tees <don...@execulink.com> wrote:
> Vince Coen wrote:
> > Hello All!
…[5 more quoted lines elided]…
> > Original assign clause is Select print-rep assign "PRN:".

Hi Vince,

Some of HP printers uses USB port instead of LPT1/2, so I guess the
link below will instead instruct you to use the general format for
printer "redirection".

http://supportline.microfocus.com/mf_kb_display.asp?kbnumber=21320
```

#### ↳ Re: Net Express v5.- personal edition

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2007-06-11T19:05:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32hbi.13954$NV3.643@pd7urf2no>`
- **In-Reply-To:** `<1180789656@f609.n257.z2.fidonet.ftn>`
- **References:** `<1180789656@f609.n257.z2.fidonet.ftn>`

```
Vince Coen wrote:
> Hello All!
> 
…[16 more quoted lines elided]…
> 
The question has already been partially answered but you simply can't 
mix and match the old DOS OS syntax with Windows OS.

Possibilities are :-

- assign print file to disk - see some examples at University of 
Limerick - http://www.csis.ul.ie/COBOL/. Then of course you subsequently 
print the disk file.

- use PC_PRINT routines - plenty of M/F examples - think of setting up 
your common print lines in W/S rather like laying out Screen Section or 
Report Writer lines

- third party 'Windows' printer software like - 
http://www.sanface.com/txt2pdf.html

If you want to try the PC_PRINT e-mail me, (editing my address). I can 
give you an OO class, while not containing all the printer routines, 
would certainly  get you off the ground. (It's a while since I did it, 
so it can be improved upon).

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
