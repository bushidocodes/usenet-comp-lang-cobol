[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP !!! I want to translate Microfocus COBOL files in ASCII plain text

_2 messages · 2 participants · 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### HELP !!! I want to translate Microfocus COBOL files in ASCII plain text

- **From:** paoreffo@tin.it (Paolo REFFO)
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3710535b.631370@news.tin.it>`

```
I have got many files in Microfocus Cobol which I must import in other
environments, suche as ACCESS, EXCEL, OS/400.
The operating system is UNIX.
With an FTP I can download it on a PC.
Then I can see what's inside the files.
The only problems come with numeric fields which - they told me - are
in "COMP-3" format.
I'd like to have a tool which (giving it an input a file with the
positions, the length and the types of these non-character fields)
TRANSLATES THIS RECORD FORMAT IN ALL ASCII PLAIN TEXT.

Consider I don't know anything about Cobol, Microfocus and COMP-3
format, but I have quite good programming experiences in other
programming environments, so that I can send and share many other
tools (written by me) for importing and exporting files in commercial
environments.

However many thanks to anybody who will give me a help.

PAOLO
paoreffo@tin.it
```

#### ↳ Re: HELP !!! I want to translate Microfocus COBOL files in ASCII plain text

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fA5Q2.724$lq5.63885@dfiatx1-snr1>`
- **References:** `<3710535b.631370@news.tin.it>`

```
Did you download the COBDATA.ZIP tutorial from
http://www.flexus.com/softwaredownload.html ???  That tells you what the
data looks like so you could write your own conversion in any programming
language.

As far as a "generic" tool, I know of no such item, although I speculated
here in response to your original post about writing one. (Hint: it would
not be free).

However, if you have a record layout (the "COBOL FD") and a COBOL compiler
(or even Microfocus' Personal COBOL interpreter), any COBOL programmer
should be able to write a program to read your file as input and write ASCII
output. If it takes longer than fifteen minutes, (add ten minutes for each
file after the first one) you have the wrong programmer.

Just to prove my point: consider this a firm quotation.

MCM


Paolo REFFO wrote in message <3710535b.631370@news.tin.it>...
>I have got many files in Microfocus Cobol which I must import in other
>I'd like to have a tool which (giving it an input a file with the
…[7 more quoted lines elided]…
>paoreffo@tin.it
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
