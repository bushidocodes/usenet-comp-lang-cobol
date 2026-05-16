[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# use compression in an application program

_5 messages · 5 participants · 1999-11_

---

### use compression in an application program

- **From:** clastname@nospam.com (Charles Haatvedt Jr.)
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<MPG.1297a76aea89adb19896c2@news>`

```
I am looking for information on using compression within a application 
module. If this is not the appropriate forum I appologize.

backround...   

we have an application system which passes very large volumes of data, 
700 byte records at ~ 100,000,000 records per file. We have jobs which 
manipulate and sort this data. 

I am considering using a compression routine to reformat the output 
record before writing it. What I would like to attempt is to compress the 
record in the application and then format the output record as the record 
key used in sorting followed by the compressed record. I realize that I 
would have to include at the minimum a length of the compressed area as 
well as perhaps a key of some sort to be used by the compression routine.

What I am interested in is if IBM supplies any compression modules as 
part of OS/390 which could be used to accomplish this...

I would also be interested in the results if anyone has experience of a 
similiar nature...

				Thanks,
```

#### ↳ Re: use compression in an application program

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<382E968B.F9A671AE@zip.com.au>`
- **References:** `<MPG.1297a76aea89adb19896c2@news>`

```
"Charles Haatvedt Jr." wrote:
> 
> I am looking for information on using compression within a application
…[20 more quoted lines elided]…
> a similiar nature...

Compression is now done in two ways by MVS:

1.  The disk drives themselves are compressed.  No overhead, no
changes.

2.  SMS has compression built in.  You define a compressed data class
and everything looks uncompressed because the operating system is
doing the work.

Compression by the program is generally unnecessary and just adds
bugs.

Ken
```

#### ↳ Re: use compression in an application program

- **From:** Jim Keohane <jimkeo@multi-platforms.com>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<80mvq3$j0k$1@nnrp1.deja.com>`
- **References:** `<MPG.1297a76aea89adb19896c2@news>`

```
In article <MPG.1297a76aea89adb19896c2@news>,
  clastname@nospam.com (Charles Haatvedt Jr.) wrote:
> I am looking for information on using compression within a
application
> module.

Chuck,

   Most S/390's have hardware assisted compression that can be invoked
in an assembler routine. I will try to be more specific when I'm back
in the office with my CD's.

   The nature of your data is important. If your data is report-like
data or readable data then simpler compression like RLE might be less
of a CPU burden. RLE (run length encoding) compresses repetitive blanks
and other characters. Even if you do not have that kind of data and you
do not have hardware support there is also freely available compression
code (in C) that operates like ZIP/WINZIP/etc.

   You have a huge amount of data to compress. Keep in mind that a C
program that runs fine on a small Intel box can bring a mainframe to
its knees. Different instrction sets. Different architectures.
Different runtimes, etc. I have had to "tailor" C compression code
(using SAS/C optimization and inline assembler) to drastically reduce
the S/390 CPU impact.
Cheers,  - Jim Keohane
```

##### ↳ ↳ Re: use compression in an application program

- **From:** Kurt Quackenbush <kurtq@us.ibm.com>
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<383079F3.5AA893B5@us.ibm.com>`
- **References:** `<MPG.1297a76aea89adb19896c2@news> <80mvq3$j0k$1@nnrp1.deja.com>`

```
Do a search on CMPSC and CSRCMPSC in the literature.  CMPSC is the
Compression Call hardware instruction, and CSRCMPSC is the assembler macro
(provided by OS/390) used to invoke the CMPSC instruction.  I think both
the Assembler Services Guide and Reference provide some useful information,
also, "Enterprise Systems Architecture/390 Data Compression" if you can
find it.

As mentioned in a previous append, the nature of your data is VERY
important.  The service encodes data by replacing strings of characters
with shorter fixed-length symbols.  The key component is a symbol table, or
dictionary, which you must construct yourself and provide to the service.
Compressed data contains symbols which correspond to entries in the
dictionary.  Therefore, if your data is well behaved, you may be able to
construct a dictionary which provides excellent levels of compression.  If
on the other hand, your data is quite unpredictable, then your dictionary
will be less specific, and hence you will achieve less spectacular levels
of compression.

There are also a couple of REXX execs in SYS1.SAMPLIB which you can use to
help construct and test compression dictionaries: CSRBDICT and CSRCMPEX.

As far as experience in using this service, SMP/E does use the service
successfully to compress data within PTFs in the SMPPTFIN data set.  The
only real trouble we had was in creating good compression dictionaries.
Also, if my memory serves me, DFSMS uses the CMPSC service for compressed
data sets; DFSMS creates a specific dictionary for the data set and stores
it along with the data in the data set.

Kurt Quackenbush - - IBM, SMP/E Development
```

#### ↳ Re: use compression in an application program

- **From:** far@mobilixnet.dk (Frank Allan Rasmussen)
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<382ffeeb.8459966@news.inet.tele.dk>`
- **References:** `<MPG.1297a76aea89adb19896c2@news>`

```
On Sat, 13 Nov 1999 22:51:20 GMT, clastname@nospam.com (Charles
Haatvedt Jr.) wrote:

>I am looking for information on using compression within a application 
>module. If this is not the appropriate forum I appologize.
>
>What I am interested in is if IBM supplies any compression modules as 
>part of OS/390 which could be used to accomplish this...

IBM have some assembler macro's (CSRCESRV and CSRCMPSC) that does
compression. It should not be a large task to write a small program
you can call to do the compression you need (if you need it).

CSRCESRV use a method of reduction of repeated bytes and is very good
when you use on output listings with lots of blank strings.

CSRCMPSC use hoffmann compression (I think) and is described in detail
in 'Assembler Services Guide'. There is a REXX mentioned that should
give you a number on how much you will gain using this macro.

I do not think that there is a module you can call with input and
output areas, but check SYS1.PARMLIB.

I think I can remember that BMC had a compression module in some
software in relation to DB2?


Frank Allan Rasmussen
Systemsprogrammer
Fyns Amts EDB-central
FAR@OES.FYNS-AMT.DK
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
