[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Strange print problem in DOS

_12 messages · 12 participants · 1998-03_

---

### Strange print problem in DOS

- **From:** "jcj..." <ua-author-1139539@usenetarchives.gap>
- **Date:** 1998-03-09T19:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e21fb$ege$1@nnrp1.dejanews.com>`

```

I have moved a simple end of month summary report off of our
mid-range to a PC for feasibility testing. The program works
fine when re-compiled with Micro Focus COBOL with the following
exception:

In the main frame / mid range world, I would not expect a print file
to be sent to the printer until either the print file were closed or
the program reached a STOP RUN statement. On the PC, if there is
no activity to the printer for approx 20 seconds, the file begins
printing. Since this is a summary report, it digs through thousands
of transactions for the month before writing a summary line. This can
take far longer than 20 seconds.

Hence I get the three heading lines, then a forced eject from the
printer, then the summary lines begin to print. Dohhhhhh ??

I have called Micro Focus support (what an oxymoron) and dug through
what I believe to be the appropriate manuals (there were about 12
supplied with Micro Focus Tool Set) but I still haven't a clue.

This is especially frustrating

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Strange print problem in DOS

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6e21fb$ege$1@nnrp1.dejanews.com>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com>`

```

I think he following is a pretty AWFUL solution, but it might do as a
temporary circumvention. If you changed the output of the report to be a
file instead of a printer and when you were done you could just read the
file and send it to a printer - all at once.

There should be a better way than this and I have asked some of sources for
suggestions, but this should be a work-around.
```

##### ↳ ↳ Re: Strange print problem in DOS

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e584b4deb1-p2@usenetarchives.gap>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com> <gap-e584b4deb1-p2@usenetarchives.gap>`

```

For a month summary report on a PC, I would agree with Bill Klein. If the
first report lines aren't ready immediately after the header is printed, use
a different method. Write the output to a temporary file, then loop thru the
records reading & writing to the printer.
David M.
```

##### ↳ ↳ Re: Strange print problem in DOS

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e584b4deb1-p2@usenetarchives.gap>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com> <gap-e584b4deb1-p2@usenetarchives.gap>`

```

On Mon, 9 Mar 1998 18:25:18 -0800, "William M. Klein"
wrote:

› I think he following is a pretty AWFUL solution, but it might do as a
› temporary circumvention.  If you changed the output of the report to be a
…[16 more quoted lines elided]…
›› 
This has nothing to do with the PC.
This will depend on :
1-the printer you are using (Laser; dot matrix; deskjet)
2-If you are using a spooler (Eg . Novell capture)
3-Other things (specific to the operating system)

If you can post all the operating system configuration
stating operating system, operating system printer configuration
printer used, printer configuration and other that can help us.
I am sure that we can give you more information.

Best regards

Frederico Fonseca
```

#### ↳ Re: Strange print problem in DOS

- **From:** "binyami..." <ua-author-932190@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6e21fb$ege$1@nnrp1.dejanews.com>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com>`

```

On Mon, 09 Mar 1998 18:29:31 -0600 JCJ··.@a··.com wrote:

:>I have moved a simple end of month summary report off of our
:>mid-range to a PC for feasibility testing. The program works
:>fine when re-compiled with Micro Focus COBOL with the following
:>exception:

:>In the main frame / mid range world, I would not expect a print file
:>to be sent to the printer until either the print file were closed or
:>the program reached a STOP RUN statement.

Try

//filename DD UNIT=00E

on MVS and you will get the same results.

The reason the print is delayed is because you use something like

//filename DD SYSOUT=A

which goes to a spooler which waits for the job to complete before printing.

:> On the PC, if there is
:>no activity to the printer for approx 20 seconds, the file begins
:>printing. Since this is a summary report, it digs through thousands
:>of transactions for the month before writing a summary line. This can
:>take far longer than 20 seconds.

:>Hence I get the three heading lines, then a forced eject from the
:>printer, then the summary lines begin to print. Dohhhhhh ??

You have to discover if this is hardware or software.

:>I have called Micro Focus support (what an oxymoron) and dug through
:>what I believe to be the appropriate manuals (there were about 12
:>supplied with Micro Focus Tool Set) but I still haven't a clue.

Why not use a print spooler? They are available.
```

#### ↳ Re: Strange print problem in DOS

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6e21fb$ege$1@nnrp1.dejanews.com>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com>`

```

JCJ··.@a··.com wrote:

› Hence I get the three heading lines, then a forced eject from the
› printer, then the summary lines begin to print.  Dohhhhhh ??
…[6 more quoted lines elided]…
› 

I had a similar problem printing to an HP laser printer. I was using
thier horizontal and vertical scaling codes, which scales a page after
the entire page is sent to the printer. Well, it was re-scaling if there
was a long (more than a few seconds) pause.

My solution.

I wrote the print output to a file with a carriage control character.

Where I had "print after 1" I would put a 1 in column 1 of the report
line and the restof the line after that.

For after Page I used "P" (what you use for each carriage control
character does not matter).

Then I wrote a callable program to read this file and send it to the
printer using the carriage control characters to determine printing
pages, double spaces, etc. Then the file could be created first, and
when complete, sent as a continous stream to the printer with no pauses.
```

#### ↳ Re: Strange print problem in DOS

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p7@usenetarchives.gap>`
- **In-Reply-To:** `<6e21fb$ege$1@nnrp1.dejanews.com>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com>`

```

All of a sudden, JCJ··.@a··.com wrote:

› I have moved a simple end of month summary report off of our
› mid-range to a PC for feasibility testing.  The program works
…[17 more quoted lines elided]…
› 
I don't know the cause of the problem, but can think of two solutions:

a) write your report to a disk file, then copy the file to the
printer

b) change the program to table up your information, then do all your
printing at once

Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

#### ↳ Re: Strange print problem in DOS

- **From:** "keld laksh��j-hansen" <ua-author-17075488@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p8@usenetarchives.gap>`
- **In-Reply-To:** `<6e21fb$ege$1@nnrp1.dejanews.com>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com>`

```

It may be because you're using a laser-printer, which may have a 20-second
time-out limit. Many laser-printers have as an option an automatic
form-feed when they haven't received data for at specific period of time.If
this is indeed your problem, then the cure is simpel - disable the
automatic time-out form-feed.

JCJ··.@a··.com wrote:

› I have moved a simple end of month summary report off of our
› mid-range to a PC for feasibility testing.  The program works
…[21 more quoted lines elided]…
› http://www.dejanews.com/   Now offering spam-free web-based newsreading
```

##### ↳ ↳ Re: Strange print problem in DOS

- **From:** "page-cray" <ua-author-17075349@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e584b4deb1-p8@usenetarchives.gap>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com> <gap-e584b4deb1-p8@usenetarchives.gap>`

```

Write it to a file then print it.


Keld Lakshï¿½j-Hansen wrote in message <351··.@mai··s.dk>...
› It may be because you're using a laser-printer, which may have a 20-second
› time-out limit. Many laser-printers have as an option an automatic
…[32 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Strange print problem in DOS

- **From:** "richard bolin" <ua-author-17074528@usenetarchives.gap>
- **Date:** 1998-03-21T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e584b4deb1-p8@usenetarchives.gap>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com> <gap-e584b4deb1-p8@usenetarchives.gap>`

```
How about not printing the heading lines (if they are needed) until ready to
print a summary line?

Keld LakshÃ¸j-Hansen wrote:

› It may be because you're using a laser-printer, which may have a 20-second
› time-out limit. Many laser-printers have as an option an automatic
…[29 more quoted lines elided]…
›› http://www.dejanews.com/   Now offering spam-free web-based newsreading
```

###### ↳ ↳ ↳ Re: Strange print problem in DOS

- **From:** "alex flinsch" <ua-author-12480541@usenetarchives.gap>
- **Date:** 1998-03-22T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e584b4deb1-p10@usenetarchives.gap>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com> <gap-e584b4deb1-p8@usenetarchives.gap> <gap-e584b4deb1-p10@usenetarchives.gap>`

```

richard bolin wrote:
›
› How about not printing the heading lines (if they are needed) until ready to
› print a summary line?
›

Or
redirect the output to a disk file, then print it later. This will also
allow easier reprints fo the report.
```

###### ↳ ↳ ↳ Re: Strange print problem in DOS

_(reply depth: 4)_

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-03-22T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e584b4deb1-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e584b4deb1-p11@usenetarchives.gap>`
- **References:** `<6e21fb$ege$1@nnrp1.dejanews.com> <gap-e584b4deb1-p8@usenetarchives.gap> <gap-e584b4deb1-p10@usenetarchives.gap> <gap-e584b4deb1-p11@usenetarchives.gap>`

```

Alex Flinsch wrote:
› 
› richard bolin wrote:
…[7 more quoted lines elided]…
› allow easier reprints fo the report.

Mr Flinsch, I agree with you here... but you would be surprised at how
many sites I've worked at where the old 'DASD is too expensive!'
argument still holds sway... strangely enough it is also at such sites
that they violate the commandment of 'Thou Shalt Not Have A Program
Which Updates Files *And* Generates A Report (Unless Said Report Is
*Only* Of Update Activity)'... so, of course, when someone spills coffee
on the distribution-cart and the VP's BFR (Large Copulating Report) is
ruined one not only has to re-run all 14 jobs which create the tempfiles
which go into making this stack o' greenbar... but one has to restore
the old files from the tapes, as well... oh, and did I mention reloading
indexed files from those tapes, too?

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
