[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# List dataset names on a Fujitsu Mainframe

_5 messages · 5 participants · 2001-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### List dataset names on a Fujitsu Mainframe

- **From:** liptakj@hotmail.com (John Liptak)
- **Date:** 2001-07-12T01:32:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9db5eaf6.0107120032.6eed3d03@posting.google.com>`

```
Does anyone know how I can automate a process to get a list of
sequential dataset names.  I want to be able to process hundreds of
sequential files whose names are in the following format;

PROD.XXXXXXXX.DATA (Where I dont know the value of XXXXXXXX).

ie;

PROD.ABCDEFG.DATA
PROD.TEST1.DATA
etc.

These datasets are basically cobol compile listings & I want to create
a JCL that will somehow process every one of these sequential datasets
but I dont know how to allocate the dataset names as I dont know part
of their name.

As I process each one of these sequential files, I will be writing
details about them to another file and part of the output needs to be
the middle portion of the dataset name.  So not only do I need to be
able to allocate the dataset but I also need its name passed to a
program so that I can write its name to another output file.

Any ideas?
```

#### ↳ Re: List dataset names on a Fujitsu Mainframe

- **From:** Bill <wfsent@optonline.net>
- **Date:** 2001-07-12T11:40:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4D8C96.B5DC4B69@optonline.net>`
- **References:** `<9db5eaf6.0107120032.6eed3d03@posting.google.com>`

```
Assuming an IBM MVS machine,

    You could use the IDCAMS utility with the LISTC command.

    Something like

                LISTC PROD.*.DATA

    (I don't have any manuals at hand, so the command may be a bit wrong)

The output can be directed to a file for subsequent processing by a COBOL
pgm or REXX proc

Bill


John Liptak wrote:

> Does anyone know how I can automate a process to get a list of
> sequential dataset names.  I want to be able to process hundreds of
…[21 more quoted lines elided]…
> Any ideas?
```

##### ↳ ↳ Re: List dataset names on a Fujitsu Mainframe

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2001-07-15T19:10:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t6X1wYAoydU7Ewin@ld50macca.demon.co.uk>`
- **References:** `<9db5eaf6.0107120032.6eed3d03@posting.google.com> <3B4D8C96.B5DC4B69@optonline.net>`

```
Try FILEAID in batch.

In article <3B4D8C96.B5DC4B69@optonline.net>, Bill
<wfsent@optonline.net> writes
>Assuming an IBM MVS machine,
>
…[40 more quoted lines elided]…
>
```

#### ↳ Re: List dataset names on a Fujitsu Mainframe

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-07-12T15:34:28+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f5rkt0ekporcdhg4pae6gqeh8cogguc5d@4ax.com>`
- **References:** `<9db5eaf6.0107120032.6eed3d03@posting.google.com>`

```
On 12 Jul 2001 01:32:19 -0700 liptakj@hotmail.com (John Liptak) wrote:

:>Does anyone know how I can automate a process to get a list of
:>sequential dataset names.  I want to be able to process hundreds of
:>sequential files whose names are in the following format;

:>PROD.XXXXXXXX.DATA (Where I dont know the value of XXXXXXXX).

:>ie;

:>PROD.ABCDEFG.DATA
:>PROD.TEST1.DATA
:>etc.

:>These datasets are basically cobol compile listings & I want to create
:>a JCL that will somehow process every one of these sequential datasets
:>but I dont know how to allocate the dataset names as I dont know part
:>of their name.

:>As I process each one of these sequential files, I will be writing
:>details about them to another file and part of the output needs to be
:>the middle portion of the dataset name.  So not only do I need to be
:>able to allocate the dataset but I also need its name passed to a
:>program so that I can write its name to another output file.

:>Any ideas?

Easiest approach is to parse the output of a LISTC LEV(PROD.*.DATA) command.
```

#### ↳ Re: List dataset names on a Fujitsu Mainframe

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-07-12T08:32:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0107120732.1ed863b9@posting.google.com>`
- **References:** `<9db5eaf6.0107120032.6eed3d03@posting.google.com>`

```
Reply at end

liptakj@hotmail.com (John Liptak) wrote in message news:<9db5eaf6.0107120032.6eed3d03@posting.google.com>...
> Does anyone know how I can automate a process to get a list of
> sequential dataset names.  I want to be able to process hundreds of
…[21 more quoted lines elided]…
> Any ideas?


STEP1
Do a LISTCAT with the NAME option, put the output to disk

STEP2
Read the output.  Skip records until you get to the data, I thnk PROD
will be in column 15, but I haven't done it in a while, and do not
have access to a mainframe now.  Look at a sample output to see
exactly where  everything is.  You will have to parse the data names,
because the second node is of varying size. UNSTRING will work for
this.    I do not think you can use a wildcard for the middle of a
dataname, so you will have to discard those that do not end in DATA. 
Write your list to disk, so you can read it back in the next step...
unless you want to do other processing as you go along.

COBOL/390 will allow you to allocate datasets dynamically, so you
don't need the names in advance, nor will you have to submit JCL from
your batch program.


Stephen J Spiro
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
