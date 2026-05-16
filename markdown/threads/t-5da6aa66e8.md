[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sequential Update

_5 messages · 5 participants · 1999-11_

---

### Sequential Update

- **From:** Bill <dc606@my-deja.com>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81515d$me9$1@nnrp1.deja.com>`

```
I am trying to write a program doing a sequential update.  I only have
an example of a program to do a "non"sequential update and in this
program INVALID KEY and NOT VALID KEY statements are used.  Of course,
my program is not even compiling properly.  I have a feeling a lot of
the errors are due to these statements.  Are these statements used soley
for nonsequential updates?  If so, what statements do I use for
sequential updates?

Thanks


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Sequential Update

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<816fb7$nkk$1@news.igs.net>`
- **References:** `<81515d$me9$1@nnrp1.deja.com>`

```
KEYS are for keyed files.  That is, files with an index.  For a sequential
file, the only input variation is "AT END".   The verbs are READ, WRITE, and
REWRITE.

Bill wrote in message <81515d$me9$1@nnrp1.deja.com>...
>I am trying to write a program doing a sequential update.  I only have
>an example of a program to do a "non"sequential update and in this
…[10 more quoted lines elided]…
>Before you buy.
```

#### ↳ Re: Sequential Update

- **From:** paulr@delphi.com
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38378efa$1$cnhye$mr2ice@news.stonemedia.com>`
- **References:** `<81515d$me9$1@nnrp1.deja.com>`

```
Essentially, for a sequential file, you read, then rewrite. 
It can get a bit tricky depending upon exactly what kind of file it  is
though. Is this on an IBM mainframe with VSAM, or something else? -Paul



In <81515d$me9$1@nnrp1.deja.com>, on 11/20/99 
   at 02:31 AM, Bill <dc606@my-deja.com> said:

>I am trying to write a program doing a sequential update.  I only have an
>example of a program to do a "non"sequential update and in this program
…[4 more quoted lines elided]…
>updates?

>Thanks


>Sent via Deja.com http://www.deja.com/
>Before you buy.
```

##### ↳ ↳ Re: Sequential Update

- **From:** jgwolfe@netcom.ca (Gerry Wolfe)
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38384617.8066923@nntp.netcom.ca>`
- **References:** `<81515d$me9$1@nnrp1.deja.com> <38378efa$1$cnhye$mr2ice@news.stonemedia.com>`

```
The REWRITE implies an update in place.  I wouldn't want to do that
for a couple of reasons:

1. If you run into problems, the original (input) file would be
corrupted and you would have to restore it before re-processing.
Assuming there was a backup done before the update!!!
2. Sequential file maintenance also implies adding new records or
perhaps deleting existing ones.  You can't do this with an
input/output file.

Instead, you probably want logic to match the input master file to an
input transaction file, creating a new master file as output.  This
would allow you to add/delete records, and not have to worry about
recovery if the job abended (ie simply re-run the job).

rgds, G.

On Sun, 21 Nov 1999 00:18:26 -0600, paulr@delphi.com wrote:
>Essentially, for a sequential file, you read, then rewrite. 
>It can get a bit tricky depending upon exactly what kind of file it  is
>though. Is this on an IBM mainframe with VSAM, or something else? -Paul
>
[snips here...]
```

#### ↳ Re: Sequential Update

- **From:** "ChrisOsborne" <chris_n_osborne@msn.com>
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e9qInyIN$GA.281@cpmsnbbsa03>`
- **References:** `<81515d$me9$1@nnrp1.deja.com>`

```
What platform?
What compiler?
What type of source file?
What type of target file?
What does your code look like?
What errors are you getting?
Are you just looking for an algorithm that does sequential updating?
In place updating, or creation of an entirely new file with deletion of the
old (or GDG processing for MVS and related environments)?

What?


Bill <dc606@my-deja.com> wrote in message
news:81515d$me9$1@nnrp1.deja.com...
> I am trying to write a program doing a sequential update.  I only have
> an example of a program to do a "non"sequential update and in this
…[10 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
