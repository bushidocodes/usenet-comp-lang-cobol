[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need Help with Microfocus cobol...!

_4 messages · 4 participants · 1998-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Need Help with Microfocus cobol...!

- **From:** "lap..." <ua-author-904956@usenetarchives.gap>
- **Date:** 1998-01-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34ceb33e.577656@news.pcpros.net>`

```

I am currently takeing Cobol as a required course for my CIS
major in College. Would someone mind helping me out with answering
a few beginner questions...?

1. I am using Micorofocus Cobol on my Pent100 system, with a
HP660c printer. I have been trying to get a page to eject (by using
the books recomendataion) of ' / ' on line 7. This does not work, and
my Prof has no idea how to get it to work. Can anyone tell me how to
eject a page using cobol with a pc and HP printer.

P.S. Were using 'Stern & Stern' Structured COBOL programming.

Any help would be greatly appreaciated..?

Dave LaPorte

lap··.@pcp··s.net
```

#### ↳ Re: Need Help with Microfocus cobol...!

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-01-26T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8c1a1faf9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34ceb33e.577656@news.pcpros.net>`
- **References:** `<34ceb33e.577656@news.pcpros.net>`

```


Dave LaPorte wrote in message <34c··.@new··s.net>...
›
› 1. I am using Micorofocus Cobol on my Pent100 system, with a
› HP660c printer. I have been trying to get a page to eject (by using
› the books recomendataion) of ' / ' on line 7.

Are you trying to get a page eject for your compiler listing or in an output
file? The '/' ONLY works for compiler listings - not for output files. ( I
have used this with Micro /focus COBOL so I know that it works - but I
haven't tried it with your printer.)

If what you want is a page eject in your printed output, there are lots of
solutions possible (depending on where you are in the class). Some
possibilities are

1) Find the HP printer manual and put an ejection character (defined by
them) in a record and write it out.

2) Use a LINAGE clause in your file definition

3) Use the Report Writer facility

I hope this helps
```

#### ↳ Re: Need Help with Microfocus cobol...!

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-01-27T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8c1a1faf9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34ceb33e.577656@news.pcpros.net>`
- **References:** `<34ceb33e.577656@news.pcpros.net>`

```

In article <34c··.@new··s.net>,
Dave LaPorte wrote:
› I am currently takeing Cobol as a required course for my CIS
› major in College.    Would someone mind helping me out with answering
…[6 more quoted lines elided]…
› eject a page using cobol with a pc and HP printer.

Putting a '/' in col 7 will force an eject for the compiler's output
listing on most mainframe printers (as will the old standby of EJECT); it
will not force a page if one is just printing the file. If my memory
holds the standard ASCII formfeed character is CHR$(12); I do not know if
MicroFocus translates a '/' or an EJECT in a source listing into this
during a compile. Check your options when you check (PF3) the program and
see if you can dump the listing to a file on disk for further examination.

›
› P.S. Were using 'Stern & Stern' Structured COBOL programming.

Not a bad text, as I recall... that and McCracken were standards Way Back
When.

DD
```

#### ↳ Re: Need Help with Microfocus cobol...!

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-01-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8c1a1faf9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34ceb33e.577656@news.pcpros.net>`
- **References:** `<34ceb33e.577656@news.pcpros.net>`

```

Dave LaPorte wrote:
›         1.  I am using Micorofocus Cobol on my Pent100 system, with a
› HP660c printer.  I have been trying to get a page to eject (by using
› the books recomendataion) of ' / ' on line 7.  This does not work, and
› my Prof has no idea how to get it to work.  Can anyone tell me how to
› eject a page using cobol with a pc and HP printer.

Hi Dave.

It's difficult to tell from your post whether you are trying to print
the source of a COBOL program, or running a COBOL program which
produces a file to be sent to a printer.

The usage of the '/' in *COLUMN* 7 is a COBOL source thing - when you
compile your program with the LIST(file.lst) directive, the listing
file produced will include pagethrows (control-L characters) wherever
there is a slash in column 7 (followed by a compiler-inserted page
header). You would then send the listing file to the printer. I just
tested this on the latest NetExpress compiler and it works fine.

If you want to get a page eject on a file being created by a COBOL
program, use WRITE rec AFTER ADVANCING PAGE (or BEFORE ADVANCING ....).

If neither of these suggestions gets you anywhere, please post example
source, a description of the erroneous output, and the version of
Micro Focus COBOL that you are using.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
