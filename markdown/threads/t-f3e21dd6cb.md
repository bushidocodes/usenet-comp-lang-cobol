[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Parameter Hand over

_4 messages · 4 participants · 1996-06 → 1996-07_

---

### Parameter Hand over

- **From:** "peni..." <ua-author-6684699@usenetarchives.gap>
- **Date:** 1996-06-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4r5od2$la6@newsbf02.news.aol.com>`

```
Hello CBOL Programmers,

I 'm just at the beginning by learning COBOL during my training for
computer scientist. Now I'm loocking for a possibility to hand over a
parameter by starting a program i.e. "sort C:\adress.dat". Does anybody
know s.th. about it?
I'm working with the Realia compiler and at the moment only for source
and object computer : IBM-PC.
Please, if anybody knows a algorythm send me an E-Mail to
PeN··.@A··.COM.
Thansk a lot

Bye
Peter from Black Forest
```

#### ↳ Re: Parameter Hand over

- **From:** "ande..." <ua-author-17072691@usenetarchives.gap>
- **Date:** 1996-06-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f3e21dd6cb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4r5od2$la6@newsbf02.news.aol.com>`
- **References:** `<4r5od2$la6@newsbf02.news.aol.com>`

```

On 30 Jun 1996 07:28:34 -0400, pen··.@a··.com (PeNiepel) wrote:

>Hello CBOL Programmers,
>
…[11 more quoted lines elided]…
>Peter from Black Forest

I believe reading the command line is in the Realia manual.
>From memory - (I read this newsgroup at home, here is how it is done.
In linkage define a structure like this
01 COMMAND-LINE.
05 COMMAND-LINE-LENGTH PIC S9(4) COMP-5.
05 COMMAND-LINE-TEXT PIC X(128).

Then is procedure division you can access the command line
directly and parse it at will.
______________________________
John Andersen
Juneau, Alaska
```

#### ↳ Re: Parameter Hand over

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1996-06-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f3e21dd6cb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4r5od2$la6@newsbf02.news.aol.com>`
- **References:** `<4r5od2$la6@newsbf02.news.aol.com>`

```

*In article <4r5od2$l.··.@new··l.com>, pen··.@a··.com says...
*>
*>Hello CBOL Programmers,
*>
*>I 'm just at the beginning by learning COBOL during my training for
*>computer scientist. Now I'm loocking for a possibility to hand over a
*>parameter by starting a program i.e. "sort C:\adress.dat". Does anybod
*>y
*>know s.th. about it?
*>I'm working with the Realia compiler and at the moment only for sourc
*>e
*>and object computer : IBM-PC.
*>Please, if anybody knows a algorythm send me an E-Mail to
*>PeN··.@A··.COM.
*>Thansk a lot
*>
*>Bye
*>Peter from Black Forest


I assume by your question you wish to pass parameters from the DOS
command line. This is very easy to do with Realia Cobol. In your
Cobol program:

- Define the Linkage Section:

LINKAGE SECTION

01 Command-Parms.
03 Parm-Count Pic S9(4) COMP.
03 Parm-Data Pic X(120).


PROCEDURE DIVISION Using Command-Parms.

When you invoke your program with data following the program name;
for example, at the DOS command line, SORT C:\address.dat, the
program SORT will be loaded and the value C:\address.dat will passed to
Command-Parms in the LINKAGE SECTION.

Note that Parm-Count must be present. Realia Cobol passes a count of
characters retrieved from the command line. Parm-Data will contain
c:\address.dat. Depending on your needs, the value in Parm-Data may
have to be parsed for unique values, depending on you application.

NOTE: You should always check Parm-Count for a value > 0 before trying
to access the contents of Parm-Data. If Parm-Count is zero, which
indicates no data was entered on the DOS command line, the
compiler does not allocate a segment for it and your program
will abend with an exception.

If you are using Version 4.2 of CA-Realia, this information can be found
in Chapter 6, Page 2, Running a Program.

Hope this helps,

mike dodas
```

##### ↳ ↳ Re: Parameter Hand over

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-07-02T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f3e21dd6cb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f3e21dd6cb-p3@usenetarchives.gap>`
- **References:** `<4r5od2$la6@newsbf02.news.aol.com> <gap-f3e21dd6cb-p3@usenetarchives.gap>`

```

mi··.@u··.com (Michael Dodas) wrote:
› 
› I assume by your question you wish to pass parameters from the DOS
…[12 more quoted lines elided]…
›  PROCEDURE DIVISION Using Command-Parms.

Hi. You will find that what Mike has described works in Micro Focus 32-bit
COBOL products also.
I would suggest, however, that you just declare Parm-Data as a pic X and use
Reference Modification to access the correct number of bytes (ie, "MOVE
Parm-Data(1:Parm-Count) TO Command-Line-Buffer"). Also, be aware that the
MF runtime ($COBDIR/cobconfig) tuneable "command_line_in_linkage" can prevent
this from happening (sometimes, people want a system that can run a program that
can either be called by another COBOL program or direct from the shell - in
that case, they don`t want this behaviour as they want to check ADDRESS OF
the first USING parameter against NULL to see which way they were invoked).

I would reccomend using "ACCEPT Command-Line-Buffer FROM COMMAND-LINE" instead
of the linkage-section method anyway.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
