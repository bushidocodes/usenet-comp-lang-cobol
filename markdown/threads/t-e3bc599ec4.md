[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol on Solaris "AFTER POSITIONING" feature

_8 messages · 6 participants · 1998-04 → 1998-05_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol on Solaris "AFTER POSITIONING" feature

- **From:** "clement ng" <ua-author-4833818@usenetarchives.gap>
- **Date:** 1998-04-30T00:21:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3547E01D.86AC2506@shaw.wave.ca>`

```

Hi all,

I have problem using the "AFTER POSITIONING" feature
with MicroFocus Cobol V4.1 on Solaris. I have a short test
program which uses this feature to print multiple 132 bytes long
lines. When I compile the cobol source, I have specified the
OSVS option already and the code compiles ok. However,
when I run it, I got one long line instead of multiple lines in
the output file.

I need this "AFTER POSITIONING" feature because there
are lots of these in the source and it is not feasible to change
them to "AFTER ADVANCING".

Thanks for the help.

cng
```

#### ↳ Re: MF Cobol on Solaris "AFTER POSITIONING" feature

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-04-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e3bc599ec4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3547E01D.86AC2506@shaw.wave.ca>`
- **References:** `<3547E01D.86AC2506@shaw.wave.ca>`

```

In article <354··.@sha··e.ca>, Clement Ng
writes:

› I have problem using the "AFTER POSITIONING" feature
› with MicroFocus Cobol V4.1 on Solaris.

Just as a wild guess: did you declare the file as LINE SEQUENTIAL? When we did
some preliminary testing under Windows95 we had to identify "printer" files as
LINE SEQUENTIAL.

Mark A. Young
```

#### ↳ Re: MF Cobol on Solaris "AFTER POSITIONING" feature

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e3bc599ec4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3547E01D.86AC2506@shaw.wave.ca>`
- **References:** `<3547E01D.86AC2506@shaw.wave.ca>`

```

In article <354··.@sha··e.ca>,
Clement Ng wrote:
› Hi all,
› 
 
› [snippage]
 
› 
› I need this "AFTER POSITIONING" feature because there
› are lots of these in the source and it is not feasible to change
› them to "AFTER ADVANCING".

Perhaps your problem will be taken care of by changing your file's
ORGANIZATION to LINE SEQUENTIAL... but the statement I retained for a
quote is the one which disturbs me. You are retaining an unsupported
feature in the language because 'lots of (POSITIONINGs)' make it 'not
feasible' to change the code?

How is this different from saying 'too much work to do it right so let's
retain obsolete language usages'?

You wouldn't happen to be bucking for a Manager's Slot, would you?

DD
```

#### ↳ Re: MF Cobol on Solaris "AFTER POSITIONING" feature

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1998-04-30T02:10:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e3bc599ec4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3547E01D.86AC2506@shaw.wave.ca>`
- **References:** `<3547E01D.86AC2506@shaw.wave.ca>`

```

I assume when you say 'one long line', you mean that your output file
displays a single record, and that this was a print file. Did your output
file specify a file type which includes delimiters (something you need in
Solaris, like on PC's, but which are not there for MF sequential output
files by default).

If, as I suspect, that is your problem, then your solution is to add
'ORGANIZATION LINE SEQUENTIAL' to your SELECT statement for your print
output file. That will instruct the compiler to put code in to add LF
delimiters to the end of each output line. On a PC they would be CRLF, but
Solaris uses the simpler form. That adds extra confusion, since if you are
using a PC editor (e.g., Notepad) to look at the output then it will still
look like one long line even if it does have the correct delimiters for
Solaris. If you want to look at a Solaris delimited ASCII file on a
Windows machine, use Wordpad (which seems to know about various delimiter
forms). The carriage control for an AFTER ADVANCING would not be in a lead
character, but would come from inserting blank lines where necessary.

BTW, this option (LINE SEQUENTIAL) also instructs the compiler to override
a CHARSET EBCDIC program directive for the particular file, so it is a
quick and dirty way to force an EBCDIC to ASCII conversion with almost no
code. This can be useful.

Gary Lee gl··.@nsp··m.com (Remove the spam filter, etc.)

Clement Ng wrote in article
<354··.@sha··e.ca>...
› Hi all,
› 
…[16 more quoted lines elided]…
›
```

##### ↳ ↳ Re: MF Cobol on Solaris "AFTER POSITIONING" feature

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e3bc599ec4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e3bc599ec4-p4@usenetarchives.gap>`
- **References:** `<3547E01D.86AC2506@shaw.wave.ca> <gap-e3bc599ec4-p4@usenetarchives.gap>`

```

You don't tell us how the compile fails with LINE SEQUENTIAL. However,
earlier you said you were using the OSVS directive. I have a couple of
suggestions.

1) Check your FLAGAS directive - if it is set to "S" - you may be getting an
error on LINE SEQUENTIAL just because that wasn't part of OS/VS COBOL (on an
IBM mainframe). Change this to FLAGAS(W) and see if your "error message"
becomes a warning.

2) Look at the SEQUENTIAL directive and see if you can change the type of
file without changing the source code. This will ONLY work if you have no
files (input particularly) that really ARE "record sequential"

3) Look at the FILE-TYPE directive. One MF person (off-line) suggested to
me that FILETYPE(3) for this file, *might* solve your problem.

4) Check your directive listing (using the SETTING directive). Do you have
both OSVS *and* MF turned on? If not, I think you should (unless you think
this program will ever be put back on an IBM mainframe using OS/VS COBOL)

5) Are you aware that the minute you specify the "OSVS" directive, you will
be limited in your use of "reference modification"? This is documented in
the MF material - but lots of people miss it.

6) I know you aren't doing a "real mainframe migration" but you may want to
look at the following web location on information on how to convert AFTER
POSITIONING to AFTER ADVANCING. In the long run, this should be your "goal"
to get away from the OSVS directive.

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/IGYMG200/4.1.7

(and do a find on "WRITE AFTER" when you get to this page.)
```

###### ↳ ↳ ↳ Re: MF Cobol on Solaris "AFTER POSITIONING" feature

- **From:** "clement ng" <ua-author-4833818@usenetarchives.gap>
- **Date:** 1998-05-05T00:32:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e3bc599ec4-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e3bc599ec4-p5@usenetarchives.gap>`
- **References:** `<3547E01D.86AC2506@shaw.wave.ca> <gap-e3bc599ec4-p4@usenetarchives.gap> <gap-e3bc599ec4-p5@usenetarchives.gap>`

```

Thanks William, I have tried FILETYPE(3) compilation directive. It works.
However,
what does FILETYPE(3) mean?

cng

William M. Klein wrote:

› You don't tell us how the compile fails with LINE SEQUENTIAL. However,
› earlier you said you were using the OSVS directive.  I have a couple of
…[108 more quoted lines elided]…
››
```

##### ↳ ↳ Re: MF Cobol on Solaris "AFTER POSITIONING" feature

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-30T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e3bc599ec4-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e3bc599ec4-p4@usenetarchives.gap>`
- **References:** `<3547E01D.86AC2506@shaw.wave.ca> <gap-e3bc599ec4-p4@usenetarchives.gap>`

```

In article <354··.@sha··e.ca>,
Clement Ng wrote:
› Hi,
› 
…[3 more quoted lines elided]…
› WRITE ... AFTER POSITIONING ... LINES

One does not POSITION a number of lines, one POSITIONs a control-character
for spacing.

DD
```

#### ↳ Re: MF Cobol on Solaris "AFTER POSITIONING" feature

- **From:** "johan" <ua-author-21418@usenetarchives.gap>
- **Date:** 1998-04-30T14:33:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e3bc599ec4-p8@usenetarchives.gap>`
- **In-Reply-To:** `<3547E01D.86AC2506@shaw.wave.ca>`
- **References:** `<3547E01D.86AC2506@shaw.wave.ca>`

```

› I need this "AFTER POSITIONING" feature because there
› are lots of these in the source and it is not feasible to change
…[4 more quoted lines elided]…
› cng

Just use a search and replace in your editor - AFTER ADVANCING is the more
logical one to use ...

Johan
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
