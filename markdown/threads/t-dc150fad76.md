[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Kobol and Linux

_5 messages · 3 participants · 2003-03_

---

### Kobol and Linux

- **From:** Scott Brady <bradys_cc@yahoo.com.au>
- **Date:** 2003-03-26T17:36:09+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QAcga.89$1s1.531@newsfeeds.bigpond.com>`

```
Hello all,

I am a student in an Australian University.

I have only just started studying COBOL.

As Linux is my operating system of choice I have recently
purchased a Kobol.

I am used to using Microfocus Personal Compiler under windows.

I am having problems getting Kobol to open a file on the disk.

Please note the following code.

ENVIRONMENT DIVISION
...
...
FILE CONTROL
SELECT Input-File ASSIGN TO DISK "C:\report.dat"
     ORGANISATION IS LINE SEQUENTIAL.
....
...

My Question is how do I reference a file through Linux such that it
recognises the file I want to input.

Any help would be greatly appreciated.

Thanks in Advance.

Scott Brady.
```

#### ↳ Re: Kobol and Linux

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-27T07:47:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5rluo$sh0$1@aklobs.kc.net.nz>`
- **References:** `<QAcga.89$1s1.531@newsfeeds.bigpond.com>`

```
Scott Brady wrote:

> FILE CONTROL
> SELECT Input-File ASSIGN TO DISK "C:\report.dat"
…[3 more quoted lines elided]…
> recognises the file I want to input.

You must use a Unix/Linux name.

         C:  -> this is CP/M, DOS, Windows drive specifier
                Linux does not use these.
         \   -> this is DOS, Windows separator
                Linux uses /
         name   DOS, Windows is case insentive.
                report.dat, RePorT.dAt are the same.
                Unix/Linux is case sensitive you must
                specify _exactly_ whet the name is.

Typically, the file might be:  "/home/scott/data/report.dat"

You also need to worry about 'permissions' where a file or directory may or 
may not be accessible by a program.  If you own the file then there should 
be no problems.
```

##### ↳ ↳ Re: Kobol and Linux

- **From:** Scott Brady <bradys_cc@yahoo.com.au>
- **Date:** 2003-03-26T18:21:27+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ifdga.108$1s1.549@newsfeeds.bigpond.com>`
- **In-Reply-To:** `<b5rluo$sh0$1@aklobs.kc.net.nz>`
- **References:** `<QAcga.89$1s1.531@newsfeeds.bigpond.com> <b5rluo$sh0$1@aklobs.kc.net.nz>`

```
I am aware of the linux naming conventions and have already tried this.

The program runs perfectly under in Windows (Microfocus Personal Compiler)

In the linux Kobol compiler. The program runs but it enters a never 
ending loop.

It is supposed to display the contents of the file to the screen in the 
form of a table. The table headers are displayed but the detail lines 
contain nothing. The report.dat file was written on windows. Would this 
have anything to do with it? Would it not be correctly recognizing the EOF.

It just seems as though the file is not being read properly

Thanks in Advance

Scott Brady
bradys_cc@yahoo.com.au

Richard Plinston wrote:
> Scott Brady wrote:
> 
…[26 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Kobol and Linux

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-26T02:49:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5rpjh$gc7$1@slb9.atl.mindspring.net>`
- **References:** `<QAcga.89$1s1.531@newsfeeds.bigpond.com> <b5rluo$sh0$1@aklobs.kc.net.nz> <ifdga.108$1s1.549@newsfeeds.bigpond.com>`

```
What is the file status code after the OPEN?  (I don't think your
Select/Assign shows you checking file status codes)

Also, my guess is that you do NOT need the "disk" word, i.e you may have
better luck with:

FILE CONTROL
SELECT Input-File ASSIGN TO "C:/report.dat"
     ORGANISATION IS LINE SEQUENTIAL
        File Status working-storage-fs.

Finally, it is possible that your line sequential file DOES have different
"record delimiters" on Linux and Windows.  How did you get it from one to
the other?

P.S. Did you get a clean compile with "ORGANISATION"?  I didn't know that
Kobol supported this Micro Focus extension (rather than "ORGANIZATION")
```

###### ↳ ↳ ↳ Re: Kobol and Linux

_(reply depth: 4)_

- **From:** Scott Brady <bradys_cc@yahoo.com.au>
- **Date:** 2003-03-26T21:00:19+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dAfga.219$1s1.1598@newsfeeds.bigpond.com>`
- **In-Reply-To:** `<b5rpjh$gc7$1@slb9.atl.mindspring.net>`
- **References:** `<QAcga.89$1s1.531@newsfeeds.bigpond.com> <b5rluo$sh0$1@aklobs.kc.net.nz> <ifdga.108$1s1.549@newsfeeds.bigpond.com> <b5rpjh$gc7$1@slb9.atl.mindspring.net>`

```
Many Thanks William.

All it took was to remove the DISK and it compiled perfectly.

ORGANISATION was supposed to be ORGANIZATION. That was a typo error on 
my part.

The Kobol compiler as far as I can ascertain has very little 
Documentation. For a comercial product I find this strange.

Anyway problem solved.

Thanks again.

William M. Klein wrote:
> What is the file status code after the OPEN?  (I don't think your
> Select/Assign shows you checking file status codes)
…[83 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
