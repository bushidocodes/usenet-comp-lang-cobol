[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AIX, Acucobol data conversion

_4 messages · 4 participants · 2001-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### AIX, Acucobol data conversion

- **From:** "Milton Bradley" <nospam@nospam.com>
- **Date:** 2001-01-22T14:27:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94i5em$nlr$1@news.chorus.net>`

```
Hello,

We have the need to convert data from an application running on an RS6000
(old AIX v4.1.5). The programs were written by a vendor so there appears to
be no access to source code. We did find a directory that contains the data
files and the program executables. Some of the AIX scripts on the machine
refer to acucobol so we are assuming it is a COBOL application with
proprietary indexed data files. The programs appear to have been written
around 1992 if that helps.

What we are looking for is advice on whether these data files could be
converted to ASCII text or some other common format. Does acucobol provide
some sort of utility for exporting data? Maybe we could pay someone to
convert it for us. Any advice appreciated.

- Linda
```

#### ↳ Re: AIX, Acucobol data conversion

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-01-23T01:39:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a6ce08f.175765335@news1.attglobal.net>`
- **References:** `<94i5em$nlr$1@news.chorus.net>`

```
Without the source code, at least for the data descriptions, you
basically out of luck.  You would be better served capturing any
reports the system is capable of generating and using these to
reproduce the data.


On Mon, 22 Jan 2001 14:27:52 -0600, "Milton Bradley"
<nospam@nospam.com> wrote:

>Hello,
>
…[15 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: AIX, Acucobol data conversion

- **From:** Vadim Maslov <vadik-nws@siber.com>
- **Date:** 2001-01-23T02:35:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A6CEE04.57497B44@siber.com>`
- **References:** `<94i5em$nlr$1@news.chorus.net>`

```
Siber Systems has developed DataReader technology 
that allows to read Cobol data files when you have
source for FD and SELECT and when you have NO source 
of the Cobol program.

DataGuess tool from our family of tools performs
statistical analysis of records in your data file
and comes up with a record layout that fits the pattern 
that we discover in the file.

Then a technician would manually refine the record layout
(or you can do it yourself, if you also get Data2Flat tool
for testing different data layouts).

The service is not cheap, but if you really *really* need it, 
then we can create reader of any Cobol data file for you.

A trial version of the DataGuess tool and 
more info on DataReader technology is available 
from http://www.siber.com/sct/datafile/

Regards,
Vadim Maslov


Milton Bradley wrote:
> 
> Hello,
…[14 more quoted lines elided]…
> - Linda
```

#### ↳ Re: AIX, Acucobol data conversion

- **From:** <fred@basset.com>
- **Date:** 2001-01-25T15:43:05+11:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94oaps$cv@newshost.fujitsu.com.au>`
- **References:** `<94i5em$nlr$1@news.chorus.net>`

```
We use ACUCOBOL (version 4.3.1) on SCO and HP Unix, so don't know if the
following will help.
First, try issuing the command                                    runcbl -v
This should show if the ACUCOBOL runtime is loaded, and what version it is.
Always a good starting point.

Our versions of ACUCOBOL come with a tool called vutil.
If you issue the command
                                         vutil -info data_file_name
you get such info as number of records, record size and number of keys.
Using the command
                                                  vutil -info -x -k
data_file_name
provides more data on the keys in the file.
Then try issuing the command
                                   vutil -unload -t data_file_name
new_data_file_name
this should extract the data and put it in the new_data_file_name in an
ASCII format.
Vutil has many other options so it might pay to get a copy of the doco
(available on CD).

ACUCOBOL also comes with Alfred, an Indexed File Record Editor. Alfred is a
menu-driven, record-level editor. Alfred allows you to view, modify, add, or
delete individual records stored in an indexed file.

Hope this is of help,

Glenn Wood

xsys@hotpop.com


Milton Bradley <nospam@nospam.com> wrote in message
news:94i5em$nlr$1@news.chorus.net...
> Hello,
>
> We have the need to convert data from an application running on an RS6000
> (old AIX v4.1.5). The programs were written by a vendor so there appears
to
> be no access to source code. We did find a directory that contains the
data
> files and the program executables. Some of the AIX scripts on the machine
> refer to acucobol so we are assuming it is a COBOL application with
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
