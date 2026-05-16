[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol set for AIX - secuential files - DDMEA

_3 messages · 3 participants · 2004-10_

---

### Cobol set for AIX - secuential files - DDMEA

- **From:** Daniel Vidal <vidal_dan@gva.es>
- **Date:** 2004-10-22T11:22:23+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4178D14F.A72AC01@gva.es>`

```
Hi all

    I have a problem with Cobol and secuential files when migrating from
MVS to AIX.

    I have many batch processes that do 3 steps:

        1 -  extract data from database and write secuential file
        2 -  sort the secuential file (external tool like syncsort)
        3 -  generate report

    Secuential files in Cobol set for Aix have two real files one like
filename.txt and other hidden file named .filename.ddmea .

    If the sort not have 'INCLUDE' or 'OMIT' options i can copy the
original  .ddmea file with the name of sorted file and all work fine
but.... I have some sort processes with 'INCLUDE' option set...

    Someone know any utilitie for generate .ddmea file from secuential
file?
    Someone know the .ddmea file specification?

NOTES: I can't use 'line secuential' files... i have packed data.
              The migrated application is very very old and big!!!

T.I.A.

Salud y Suerte!!!!!!!!!!
```

#### ↳ Re: Cobol set for AIX - secuential files - DDMEA

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-10-22T16:05:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pi8in0l7ecqbuuuk7ud07hgpuuf5v2ta0b@4ax.com>`
- **References:** `<4178D14F.A72AC01@gva.es>`

```
On Fri, 22 Oct 2004 11:22:23 +0200, Daniel Vidal <vidal_dan@gva.es>
wrote:

>    I have a problem with Cobol and secuential files when migrating from
>MVS to AIX.
…[19 more quoted lines elided]…
>              The migrated application is very very old and big!!!

Pipes are the preferred way to pass data between programs under Unix.
Disk files are for transport through time, not space. Change program 1
to write to STDOUT and program 3 to read from STDIN. Yes, you CAN send
binary data through a pipe. 

Execute the triad this way:

prog1 | syncsort | prog3

As a last resort, you could unpack the packed fields and use a
standardized file format: ASCII.
```

#### ↳ Re: Cobol set for AIX - secuential files - DDMEA

- **From:** pottmi@gmail.com (michael potter)
- **Date:** 2004-10-27T21:30:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2379dacc.0410272030.28d79b3f@posting.google.com>`
- **References:** `<4178D14F.A72AC01@gva.es>`

```
Daniel Vidal <vidal_dan@gva.es> wrote in message news:<4178D14F.A72AC01@gva.es>...
> Hi all
> 
…[25 more quoted lines elided]…
> Salud y Suerte!!!!!!!!!!


Dan,

I had a similar problem.  I suggest that you convert to the
other indexed file system supported by aix cobol 2.0.  the
name slips my mind, but you should be able to find it in
the programmers reference: 
http://www-306.ibm.com/software/awdtools/cobol/aix/library/

this alternate indexed file system does not use the annoying
.ddmea files.  THere are two ways to tell aix cobol to
use the alternate file system: set an environment variable,
or prefix the name of the file in the program.

I dont think this information specifically addresses your
problem, but at least you will not have to deal with .ddmea.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
