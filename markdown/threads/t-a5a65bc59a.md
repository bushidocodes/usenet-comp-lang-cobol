[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A rather odd question

_7 messages · 7 participants · 2000-07_

---

### A rather odd question

- **From:** "Tom Wright" <twright@larimore.net>
- **Date:** 2000-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nIq95.17$g62.245183@news1.i1.net>`

```
I would like to write a cobol program that will open any of our databases
and get info from them.  Since each database is different in size I don't
want to write FD and Select statments for all 300 databases.  This cobol
program will be called by a VB program.  Can I enter file names and select
statments in on the fly in MF cobol 4.032?

Does anyone have any other suggestions short of going with a third party
type middleware.....I'm trying to avoid the middleware thing.

Thanks for any info

Tom Wright
twright@larimore.net
```

#### ↳ Re: A rather odd question

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 2000-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0S22e2AoLlZ5Iw6s@rcav8r.demon.co.uk>`
- **References:** `<nIq95.17$g62.245183@news1.i1.net>`

```
In article <nIq95.17$g62.245183@news1.i1.net>, Tom Wright 
<twright@larimore.net> writes
>program will be called by a VB program.  Can I enter file names and
>select
…[4 more quoted lines elided]…
>

Hi Tom,

I think you need to look into the 'EXTFH' routines in MF-COBOL. No doubt 
someone with more experience of that product line will be able to offer 
more detailed assistance.....   :^)

Cheers

Nigel
```

##### ↳ ↳ Re: A rather odd question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k5kfs$qfr$1@nntp9.atl.mindspring.net>`
- **References:** `<nIq95.17$g62.245183@news1.i1.net> <0S22e2AoLlZ5Iw6s@rcav8r.demon.co.uk>`

```
You might also want to look at the FCD-- compiler directives.  I believe that
these will give you "access" to the file control blocks - that you could
"modify" or build on the fly.  I don't really recommend this, but it might
give you what you want.
```

#### ↳ Re: A rather odd question

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5nE95.72$HD.16281@dfiatx1-snr1.gtei.net>`
- **References:** `<nIq95.17$g62.245183@news1.i1.net>`

```
Tom Wright <twright@larimore.net> wrote in message
news:nIq95.17$g62.245183@news1.i1.net...
> I would like to write a cobol program that will open any of our databases
> and get info from them.  Since each database is different in size I don't
…[3 more quoted lines elided]…
>

Why not open the files from the VB program? If there are ODBC drivers for
the databases, the SQL is portable; and, you can use ODBC calls to get the
available table names, descriptions, etc.

If a third-party DLL is not total anathema to you, there is a pretty good
product for simplified ODBC access available from Perfect Sync at
www.perfectsync.com to eliminate much of the 'low-level' ODBC calls.


MCM
```

#### ↳ Re: A rather odd question

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kcbgl$pec$1@hyperion.mfltd.co.uk>`
- **References:** `<nIq95.17$g62.245183@news1.i1.net>`

```

Tom Wright wrote in message ...
>I would like to write a cobol program that will open any of our databases
>and get info from them.  Since each database is different in size I don't
…[7 more quoted lines elided]…
>Thanks for any info

Hi Tom,

It is possible to use the same SELECT statement to open multiple files,
we have an application which does this. One can access the 'file control
description' and save that away, then reuse the same SELECT statement.
The FCDREG directive sets up a special data item FH--FCD for each
file, and one can use this to access the FCD.

However this only works if you want to open lots of files which have the
same style SELECT statement. So if all your index files have the same
structure, then this is okay. However if they are all different, then
this won't work. Well you might be able to get it to work, but you
will have to store key definition blocks away somewhere as well.

Here is a skeleton program I hope you can make use of:

      $set FCDREG
123456 select db-file assign to db-file-name
           file status is file-status.
       data division.
       file section.
       fd db-file.
       01 db-rec pic x(80).
       working-storage section.

       01 file-status.
          03 db-stat-1  pic 9(2) comp-x.
          03 db-stat-2  pic 9(2) comp-x.

       01 ws-fcd occurs 300.
           *> should be in %COBDIR%\sources
           copy "xfhfcd.cpy".

       01 file-number pic x comp-x.
       procedure division.

           move "filename-1" to db-file-name
           move 1 to file-number
           perform open-file

           move "filename-2" to db-file-name
           move 2 to file-number
           perform open-file

           *> rest of files here

           move 2 to file-number
           perform access-file
           *> file i-o here
           perform save-file

           *> next file

           *> close all files
           perform close-all-files
           stop run
           .

123456 open-file section.
           open i-o db-file
           move fh--fcd of db-file to ws-fcd(file-number)
          *> fast close , posn 8 = fcd-open-mode
          *> needed so can use open statement again
           move x"80" to fh--fcd of db-file(8:1)
           .

       save-file section.
           move fh--fcd of db-file to ws-fcd(file-number)
           .

       access-file.
           move ws-fcd(file-number) to fh--fcd of db-file
           .

       close-all-files section.
           move 0 to file-number
           perform 300 times
               add 1 to file-number
               move ws-fcd(file-number) to fh--fcd of db-file
               close db-file
           end-perform
           .



Regards,
Steven Lalewicz.

>
>Tom Wright
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: A rather odd question

- **From:** Scott Williamson <syw@cdvdc.demon.co.uk>
- **Date:** 2000-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rXR2OCAWBia5EwIm@cdvdc.demon.co.uk>`
- **References:** `<nIq95.17$g62.245183@news1.i1.net> <8kcbgl$pec$1@hyperion.mfltd.co.uk>`

```
>Tom Wright wrote in message ...
>>I would like to write a cobol program that will open any of our databases
…[9 more quoted lines elided]…
>
Some years ago I wrote a standard file access routine that used either a
data dictionary or copybook files to access COBOL datafiles.  The basic
idea was that the setup program generated and compiled a skeleton file
access program for a specific file, and this was then called by the main
(generic) program.  I used it for ad-hoc reporting and problem-solving.

I've still got the code somewhere. if anyone's interested.  It was
written in RM-COBOL, but should be portable to most other compilers.
```

###### ↳ ↳ ↳ Re: A rather odd question

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396B591C.213EE25A@home.com>`
- **References:** `<nIq95.17$g62.245183@news1.i1.net> <8kcbgl$pec$1@hyperion.mfltd.co.uk> <rXR2OCAWBia5EwIm@cdvdc.demon.co.uk>`

```


Scott Williamson wrote:
> 
> Some years ago I wrote a standard file access routine that used either a
…[6 more quoted lines elided]…
> written in RM-COBOL, but should be portable to most other compilers.

Scott,

I'd be interested in seeing a copy - might be able to do something
useful with it in OO. And before DD jumps in - saves me doing a bit of
homework <G>.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
