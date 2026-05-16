[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynamic memory allocation in Microfocus cobol

_6 messages · 3 participants · 2000-08 → 2000-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Dynamic memory allocation in Microfocus cobol

- **From:** quazhi@my-deja.com
- **Date:** 2000-08-31T15:11:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8olsii$ki3$1@nnrp1.deja.com>`

```
Does anyone know whether the HP microfocus cobol version B.13.35
compatible with the version of microfocus 4.1 has the feature of the
dynamic memory allocation (uses in calls to routine written in C++)?
Thanks in advance!


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Dynamic memory allocation in Microfocus cobol

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-08-31T15:32:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zUur5.145680$c5.3912692@news2.rdc1.on.home.com>`
- **References:** `<8olsii$ki3$1@nnrp1.deja.com>`

```
Sorry but I don't understand the question. Do you want to know if COBOL can
allocate memory or whether it can exchange addressable memory with other
routines. The answer to both is yes. The details are documented in the
"Object COBOL Programmer's Guide to Writing Programs - Chapter 10:
Interfacing and Mixed-language Programming"

<quazhi@my-deja.com> wrote in message news:8olsii$ki3$1@nnrp1.deja.com...
> Does anyone know whether the HP microfocus cobol version B.13.35
> compatible with the version of microfocus 4.1 has the feature of the
…[5 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Dynamic memory allocation in Microfocus cobol

- **From:** quazhi@my-deja.com
- **Date:** 2000-08-31T17:48:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8om5ou$mb$1@nnrp1.deja.com>`
- **References:** `<8olsii$ki3$1@nnrp1.deja.com> <zUur5.145680$c5.3912692@news2.rdc1.on.home.com>`

```
Thanks Oscar! But I want more details. I mean the dynamic allocation of
memory during calls of the routine C++, not addressable memory
exchange. I learned that the early versions of the standards  before
ANSI X3.23b-1993 don't support the feature of the dynamic memory
allocation (see
http://directory.google.com/Top/Computers/Prgramming/Languages/Cobol/Sta
ndards/). So I want to know whether our current version of the
Microfocus Cobol uses the early ANSI standard of Year1993 or later.

Currently, our cobol programe calls a routine C++ to process XML
documents and return the results back. The problem is that the system
is often deadly locked due to lack of the memory when several big XML
documents are processed. We doubt it is caused by our cobol environment
can not allocate new memory to the routines written in other languages
like C++ to process big document. Is it right?

By the way, where can I find the document "Object Cobol Programmer's
Guide to Writing Programs"? I only find "Object Cobol Programmer's
Guide" in the MicroFocus Cobol document folder.

Waiting your answer. Thanks!

In article <zUur5.145680$c5.3912692@news2.rdc1.on.home.com>,
  "Oscar T. Grouch" <dustbin@home.com> wrote:
> Sorry but I don't understand the question. Do you want to know if
COBOL can
> allocate memory or whether it can exchange addressable memory with
other
> routines. The answer to both is yes. The details are documented in the
> "Object COBOL Programmer's Guide to Writing Programs - Chapter 10:
> Interfacing and Mixed-language Programming"
>
> <quazhi@my-deja.com> wrote in message news:8olsii$ki3
$1@nnrp1.deja.com...
> > Does anyone know whether the HP microfocus cobol version B.13.35
> > compatible with the version of microfocus 4.1 has the feature of the
…[7 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Dynamic memory allocation in Microfocus cobol

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-31T13:18:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8om7h2$li8$1@slb3.atl.mindspring.net>`
- **References:** `<8olsii$ki3$1@nnrp1.deja.com> <zUur5.145680$c5.3912692@news2.rdc1.on.home.com> <8om5ou$mb$1@nnrp1.deja.com>`

```
There is something VERY wrong in this post.  Dynamic Memory allocation is
*not* a part of *any* existing COBOL Standard (before or after 1993).  It
*is* a part of the PROPOSED (draft) Standard - but is very definitely NOT a
part of ANSI X3.23b-1993.

MERANT (previously Micro Focus) does provide some callable cbl_ routines for
dynamic memory allocation, if that is what you are asking about. (BUT these
are very definitely "extensions" - not Standard).

Many existing compilers (MERANT among them) also include "USAGE POINTER" data
items - AGAIN as an extension to the current Standard.  These too will be
part of the NEXT Standard (when/if it is approved).

Finally, as I understand your REAL problem, you are finding that your
application "fails" because of memory allocations - and you don't know who
*is* getting this memory.  If that is the real problem, then it is true (and
always has been) that the COBOL run-time system may WELL "acquire" storage to
accomplish some tasks.  Among other things, if your COBOL program calls other
COBOL programs - without canceling them when done, then such storage is
acquired via the first DYNAMIC access to the subprogram and never released.
```

###### ↳ ↳ ↳ Re: Dynamic memory allocation in Microfocus cobol

_(reply depth: 4)_

- **From:** quazhi@my-deja.com
- **Date:** 2000-09-01T18:21:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8oos30$5b4$1@nnrp1.deja.com>`
- **References:** `<8olsii$ki3$1@nnrp1.deja.com> <zUur5.145680$c5.3912692@news2.rdc1.on.home.com> <8om5ou$mb$1@nnrp1.deja.com> <8om7h2$li8$1@slb3.atl.mindspring.net>`

```
Thanks William,

But in our case, my understanding tells me that the routine C++ called
by the main program Cobol uses "memory allocation" to meet its private
usage. So the question is where the memory pool comes from for this
allocation and who manage this allocation (Cobol library or C library).
Plus, we don't use any "extensions" feature such as cbl_routines for
this purpose.

In article <8om7h2$li8$1@slb3.atl.mindspring.net>,
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> There is something VERY wrong in this post.  Dynamic Memory
allocation is
> *not* a part of *any* existing COBOL Standard (before or after
1993).  It
> *is* a part of the PROPOSED (draft) Standard - but is very definitely
NOT a
> part of ANSI X3.23b-1993.
>
> MERANT (previously Micro Focus) does provide some callable cbl_
routines for
> dynamic memory allocation, if that is what you are asking about. (BUT
these
> are very definitely "extensions" - not Standard).
>
> Many existing compilers (MERANT among them) also include "USAGE
POINTER" data
> items - AGAIN as an extension to the current Standard.  These too
will be
> part of the NEXT Standard (when/if it is approved).
>
> Finally, as I understand your REAL problem, you are finding that your
> application "fails" because of memory allocations - and you don't
know who
> *is* getting this memory.  If that is the real problem, then it is
true (and
> always has been) that the COBOL run-time system may WELL "acquire"
storage to
> accomplish some tasks.  Among other things, if your COBOL program
calls other
> COBOL programs - without canceling them when done, then such storage
is
> acquired via the first DYNAMIC access to the subprogram and never
released.
>
> --
> Bill Klein
>     wmklein <at> ix dot netcom dot com
> <quazhi@my-deja.com> wrote in message
news:8om5ou$mb$1@nnrp1.deja.com...
> > Thanks Oscar! But I want more details. I mean the dynamic
allocation of
> > memory during calls of the routine C++, not addressable memory
> > exchange. I learned that the early versions of the standards  before
> > ANSI X3.23b-1993 don't support the feature of the dynamic memory
> > allocation (see
> >
http://directory.google.com/Top/Computers/Prgramming/Languages/Cobol/Sta
> > ndards/). So I want to know whether our current version of the
> > Microfocus Cobol uses the early ANSI standard of Year1993 or later.
> >
> > Currently, our cobol programe calls a routine C++ to process XML
> > documents and return the results back. The problem is that the
system
> > is often deadly locked due to lack of the memory when several big
XML
> > documents are processed. We doubt it is caused by our cobol
environment
> > can not allocate new memory to the routines written in other
languages
> > like C++ to process big document. Is it right?
> >
…[12 more quoted lines elided]…
> > > routines. The answer to both is yes. The details are documented
in the
> > > "Object COBOL Programmer's Guide to Writing Programs - Chapter 10:
> > > Interfacing and Mixed-language Programming"
…[4 more quoted lines elided]…
> > > > compatible with the version of microfocus 4.1 has the feature
of the
> > > > dynamic memory allocation (uses in calls to routine written in
C++)?
> > > > Thanks in advance!
> > > >
…[10 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Dynamic memory allocation in Microfocus cobol

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-08-31T18:52:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Qxr5.146888$c5.3923245@news2.rdc1.on.home.com>`
- **References:** `<8olsii$ki3$1@nnrp1.deja.com> <zUur5.145680$c5.3912692@news2.rdc1.on.home.com> <8om5ou$mb$1@nnrp1.deja.com>`

```
http://support.merant.com/websupport/docs/microfocus/books/oc41books/prpubb.
htm

<quazhi@my-deja.com> wrote in message news:8om5ou$mb$1@nnrp1.deja.com...
> Thanks Oscar! But I want more details. I mean the dynamic allocation of
> memory during calls of the routine C++, not addressable memory
…[45 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
