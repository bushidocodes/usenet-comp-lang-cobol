[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reusability

_26 messages · 9 participants · 2008-06_

---

### Reusability

- **From:** amir <ahsharif@gmail.com>
- **Date:** 2008-06-01T00:31:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com>`

```
In the other languages we have many things for reusability:
1- Common Reusability:
  a. include other files in source code
...
2- Data Reusability:
  a. type, subtype and class definition
  b. template class and type definition
...
3- Source Code Reusability:
  a. procedure and function and sub-routines.
  b. template procedure and function
  c. exception handling, aspect oriented programming and new
technologies...
...


I am looking for reusability strategies, methods and tricks in the
COBOL language and found:
1- Common Reusability:
a. using Copy-Book files and COPY ... REPLACING ... BY ... statement

2- Data Reusability:
a. TYPEDEF is available but not recommended for main-frame development

3- Code Reusability:
a. subprogram (static or dynamic link):
b. section and paragraph

I think all new technology and thought's root is in the before
problems and solved by ancestors and in the new languages and
technologies there is not anything but encapsulated concepts of
before.

Any help to complete this list, is very useful to developers migrating
from other languages to COBOL, like me.
```

#### ↳ Re: Reusability

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-01T12:36:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nsk5441svai249fkmeov981qctpf046hod@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com>`

```
On Sun, 1 Jun 2008 00:31:37 -0700 (PDT), amir <ahsharif@gmail.com> wrote:

>I am looking for reusability strategies, methods and tricks in the
>COBOL language and found:
>1- Common Reusability:
>a. using Copy-Book files and COPY ... REPLACING ... BY ... statement

You should never copy procedure division code. Instead, make it a callable program.

REPLACING is not very useful for data division code. If you need two copies of the same
structure, use OCCURS or qualification. 

>2- Data Reusability:
>a. TYPEDEF is available but not recommended for main-frame development

It is not available in Enterprise Cobol V4. The same can be accomplished with COPY.

>3- Code Reusability:
>a. subprogram (static or dynamic link):

Dynamic is the norm. Static has been obsolete so long that Micro Focus is dropping
support.

>b. section and paragraph

c. Nested programs.

d. Object oriented.

>I think all new technology and thought's root is in the before
>problems and solved by ancestors and in the new languages and
>technologies there is not anything but encapsulated concepts of
>before.

Innovators hate that kind of talk. They think their ideas are new.
```

##### ↳ ↳ Static, Dynamic, etc (was: Reusability

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-01T18:37:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h%B0k.908221$Gl5.93236@fe02.news.easynews.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:nsk5441svai249fkmeov981qctpf046hod@4ax.com...
> On Sun, 1 Jun 2008 00:31:37 -0700 (PDT), amir <ahsharif@gmail.com> wrote:
<snip>
>>3- Code Reusability:
>>a. subprogram (static or dynamic link):
…[4 more quoted lines elided]…
>
<snip>
Robert,
  I am not saying that you are wrong about what Micro Focus "is doing" but can 
you point me to where the document that they are "dropping support for static 
linking" (and in which product and environments or O/S)?

FYI,
  Among *some* COBOL users the terms "static" and "dynamic" linking are 
SOMETIMES used to distinguish between
    CALL "literal" *> subprogram name known at compile-time
        versus
    CALL data-name  *>subprogram name NOT *usually* known at compile-time

(The latter can be done with a data-name that is never changed within the 
program logic).

This COBOL feature also relate to "early" versus "late" binding.

It is my impression (and I could be mistaken on this) that in the non-COBOL 
programming world, "static" vs "dynamic" binding is ONLY used to distinguish 
between "single object code module" vs "run-time access to subroutines in 
separate object code".

Historically, for IBM mainframe COBOL users, there was actually a 2nd 
distinction (no longer supported)

1) Did you "link-edit" in user created subroutines or not (dynamic vs static 
CALLs)
        vs
2) Did you "link-edit" in IBM supplied COBOL support routines or not (RES vs 
NORES)

It is the latter option that is no longer supported on IBM mainframe.  All 
IBM-supplied COBOL support routines are accessed "dynamically" at run-time (i.e. 
older RES behavior).

From an "historical" point-of view, the IBM mainframe COBOL "joke" was always

 "The good news about RES and DYNAM was that you always got  "new" behavior if 
the subroutines changed
        but
"  The BAD news about RES and DYNAM was that you always got  "new" behavior if 
the subroutines changed "

In other words, if the subroutine made a "good change" you would get it 
automatically without needing to re-link-edit your "load module".  However, if 
it turned out that there was a "bad" or "incomplete" change in the subroutine, 
then it would IMMEDIATELY impact all "main" programs that used it.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc (was: Reusability

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-01T18:28:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<alG0k.3385$xZ.2861@nlpi070.nbdc.sbc.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:h%B0k.908221
> It is my impression (and I could be mistaken on this) that in the 
> non-COBOL programming world, "static" vs "dynamic" binding is ONLY used to 
> distinguish between "single object code module" vs "run-time access to 
> subroutines in separate object code".

That's actually pretty close..

But if you want to get ultra-geeky, in world of Windows' systems, there are 
actually three (count 'em , 3) different times object code from 
separately-compiled modules can be link-edited.... or at least the moral 
equivalent of link-editing.....

1. At compile time .. or more accurately, 'pre-execution'
2. At program load time. This happens when the PE header defines "imports" 
in which case addresses of the imported routines are resolved 
("link-edited")  by the operating system when the primary executable file is 
first loaded. (A failure in tis step is what causes the error message 
"Program X or one of its components is missing" or "Windows cannot find 
procedure <X> in library <filename>,"  depending the  version of Windows  in 
use.
3. On demand during execution. This one is a little different, in that the 
operating does not resolve the call-addresses, the programmer must request 
the address of the 'procedure of interest' and from the additional module 
use his source language's "call by address" mechanism to actually call that 
procedure.

(Since I haven't written a line of COBOL since 2001, I no longer feel 
qualified to comment on the various COBOL implementations of these three 
different methods of "link editing.")

MCM
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc (was: Reusability

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-01T22:01:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com>`

```
On Sun, 01 Jun 2008 18:37:02 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>"Robert" <no@e.mail> wrote in message 
>news:nsk5441svai249fkmeov981qctpf046hod@4ax.com...
…[13 more quoted lines elided]…
>linking" (and in which product and environments or O/S)?

Server Express 5.0 Migration Guide

You can no longer create statically linked executables. The -B option has, therefore, been
removed. 

http://supportline.microfocus.com/Documentation/books/sx50/sx50indx.htm

>  Among *some* COBOL users the terms "static" and "dynamic" linking are 
>SOMETIMES used to distinguish between
…[5 more quoted lines elided]…
>program logic).

That's a bad idea. On Unix, normal practice is to store the names,  and optionally
directories, of called programs in the (ELF format) executable header. At program load
time, the loader insures they are accessible and actually loads them. If it cannot find
one, the executable does not start. The search is recursive; a called program can call
others. There are tools that use the executable headers to create dependency trees and
where-used lists, which are useful for impact assessment and finding deadwood. 

There is a way, dlopen, to load a program during execution. It should not be used for
ordinary linkage because you lose the benefits described above. The names of callable
programs are almost almost knowable at link time. If the program name is typed in, the
feature becomes a security risk. 

There is another feature called Lazy Load, which lists program names in the header and
verifies their accessibility but does not load then until the first call. It is intended
for large programs that may never be called. For example, the Micro Focus file system is
loaded that way. Lazy Load sounded like a good idea 20 years ago, but is not used much any
longer. 

>This COBOL feature also relate to "early" versus "late" binding.

The language shouldn't be involved with how programs are linked. That's an OS function.

>It is my impression (and I could be mistaken on this) that in the non-COBOL 
>programming world, "static" vs "dynamic" binding is ONLY used to distinguish 
>between "single object code module" vs "run-time access to subroutines in 
>separate object code".

That's right.

>Historically, for IBM mainframe COBOL users, there was actually a 2nd 
>distinction (no longer supported)
…[22 more quoted lines elided]…
>then it would IMMEDIATELY impact all "main" programs that used it.

On Unix, you can optionally specify at link time a directory and/or a version. If you say
you want version 3.1.2, you won't get any other version. If you don't trust the user's
library path, you can point to your own directory and it won't look anywhere else. 

If you're really paranoid, you can tell it to lock all versions at link time. The linker
stores a hash in the executable header; the loader will not another, even with the same
version number.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 4)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2008-06-02T10:48:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2127u02vh@news2.newsguy.com>`
- **In-Reply-To:** `<grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com>`

```
Robert wrote:
> On Sun, 01 Jun 2008 18:37:02 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:
>>  I am not saying that you are wrong about what Micro Focus "is doing" but can 
…[6 more quoted lines elided]…
> removed. 

That does not mean that static linking is no longer supported. Server 
Express still supports the static linking of multiple object files.

What's not supported is the creation of pure-static executables with 
no shared-object dependencies, which is what the -B flag could be used 
for in the past.

You can still compile a bunch of COBOL sources to object code, and 
then statically link those objects together. If you create a 
standalone executable, though, it will have dynamic dependencies on 
shared objects, including the shared objects for the COBOL runtime, 
the C runtime, and so on.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-02T19:06:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com>`

```
On Mon, 02 Jun 2008 10:48:49 -0400, Michael Wojcik <mwojcik@newsguy.com> wrote:

>Robert wrote:
>> On Sun, 01 Jun 2008 18:37:02 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:
…[20 more quoted lines elided]…
>the C runtime, and so on.

Which makes it similar to Bill's account of mainframe Cobol with the RES option. 

For those unfamilar with Unix, a library distributed in Shared Object (.so)  format must
be linked dynamically; it cannot be linked statically. If it's in the old object format
(.o and .a) it is expected to be linked statically, although it CAN be linked dynamically
(this is oddball) or packaged into an .so. An .so typically contains multiple called
programs. Thus, if a third party such as Micro Focus provides only .so, which is normal
nowadays, you must link that library dynamically. 

For late-bound objects intended to be loaded with dlopen, unusual outside Cobol, there is
no reason why you cannot list them as dynamically called, which puts their names in the
ELF header (EXTRN list) and checks for their availability at program load time. When you
make the first call, dlopen checks whether the program is already known to the loader. If
yes, it simply returns the entry point address. The only gotcha is that CANCEL won't do
anything. 

Doing that is easy on projects build by 'make', which is the norm in real world Unix
shops. The make file must know the names of child programs so it can check whether they
need to be recompiled (it compares timestamps of source to object). It can easily bundle
all of them into a single .so and put the name of that .so as a linker parameter when it
builds the main executable. By doing that, dynamic Cobol objects can be version
controlled, inventoried and deployed the same way as called programs written in other
languages. 

Advocates of static linking cite the simplicity of one file to deploy. This is almost as
simple. You have two files: an executable and an .so.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 6)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2008-06-03T10:05:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g23kpv0t3j@news3.newsguy.com>`
- **In-Reply-To:** `<u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com>`

```
Robert wrote:
> 
 > [rewrapped to a sensible line length]
…[7 more quoted lines elided]…
> must link that library dynamically.

This is more or less true, though there are platform-specific variations.

AIX's XCOFF object format permits various kinds of rebinding. On AIX, 
there's less of a distinction between shared and static object code 
than on most other Unix platforms.

The .a (archive) file format is not exclusively for "old" (static) 
objects. On AIX in particular, archive libraries often contain shared 
objects or a mix of sharable and static objects. In earlier versions 
of AIX, the .so extension (for a sharable object) was rarely used; 
sharable object was usually packaged in an archive library (.a extension).

For a long time, most shared object on AIX was delivered as an archive 
library containing at least one shared object member, which would 
typically have been produced by binding a number of regular static 
objects together.

The ELF object format (which historically was used by Solaris 2 and 
other SVR4 derivatives and Linux since the 1.2 release, and today by 
just about everyone except AIX and HP-UX) distinguishes between 
position-dependent and position-independent (PIC) object code. Only 
the latter can be included in a shared object.

Consequently, on ELF platforms, it's often the case that third-party 
static objects can't be incorporated into shared object, because it 
wasn't generated as PIC.

> For late-bound objects intended to be loaded with dlopen, unusual outside Cobol, 

Dynamic loading is quite common outside COBOL. Many programs use it 
for "plugins" or other configurable extension mechanisms, for example.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-03T18:24:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com>`

```
On Tue, 03 Jun 2008 10:05:47 -0400, Michael Wojcik <mwojcik@newsguy.com> wrote:

>The ELF object format (which historically was used by Solaris 2 and 
>other SVR4 derivatives and Linux since the 1.2 release, and today by 
>just about everyone except AIX and HP-UX) 

A Wikipedia article incorrectly says HP retained the old format on PA. I've not seen it.
Every HP-UX I've worked on in the last five years has used ELF exclusively.I'm guessing
the change occurred in the first release of HP-UX 11 in 1997 or the i1 version in 2000. 

FWIW, ELF is used on some non-Unix platforms such as games, handheld and cell phone. 

>> For late-bound objects intended to be loaded with dlopen, unusual outside Cobol, 
>
>Dynamic loading is quite common outside COBOL. Many programs use it 
>for "plugins" or other configurable extension mechanisms, for example.

I stand corrected. I forgot about plugins.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 8)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2008-06-04T09:56:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2694b01uts@news1.newsguy.com>`
- **In-Reply-To:** `<dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com>`

```
Robert wrote:
> On Tue, 03 Jun 2008 10:05:47 -0400, Michael Wojcik <mwojcik@newsguy.com> wrote:
> 
…[4 more quoted lines elided]…
> A Wikipedia article incorrectly says HP retained the old format on PA.

No, that article is correct. HP-UX *9* ran on PA-RISC, after all.

HP-UX 11.23 for ia64 is ELF-only. But PA-RISC systems still support 
the SOM format for 32-bit executables, at least through HP-UX 11.11. 
Look at the man pages for ld and chatr, for example; only SOM binaries 
have the option of using EXEC_MAGIC, DEMAND_MAGIC, or SHMEM_MAGIC.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 9)_

- **From:** amir <ahsharif@gmail.com>
- **Date:** 2008-06-09T06:44:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b36ba3d-04cf-461a-a9b1-497fe04ad468@25g2000hsx.googlegroups.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com>`

```
Some one told me about using INCLUDE as COPY statement.
I could not find any sample about it, but using INCLUDE in Embedded-
SQL.

Is there anyone help me?
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-09T21:40:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pqh3k.145781$RG7.49472@fe09.news.easynews.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <7b36ba3d-04cf-461a-a9b1-497fe04ad468@25g2000hsx.googlegroups.com>`

```
If you are talking about either IBM mainframes (with 3rd party add-on products) 
or Micro Focus (when running with IBM emulation, you should check out the 
"Panvalet" (or was it Librarian) feature of

  ++INCLUCE

It's in the MF LRM.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 11)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-09T17:06:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rPh3k.4468$N87.1844@nlpi068.nbdc.sbc.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <7b36ba3d-04cf-461a-a9b1-497fe04ad468@25g2000hsx.googlegroups.com> <Pqh3k.145781$RG7.49472@fe09.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:Pqh3k.145781$RG7.49472@fe09.news.easynews.com...
> If you are talking about either IBM mainframes (with 3rd party add-on 
> products) or Micro Focus (when running with IBM emulation, you should 
> check out the "Panvalet" (or was it Librarian) feature...

Woo, Panvalet. Now there's a word I haven't heard in a while. (OK, so I 
haven't worked mainframes in a while, either).

But I do recall that nearly every mainframe shop I worked in had Panvalet 
installed. However, only one such shop (Allstate Insurance) actually USED it 
in any way close to its designers' intentions. All the other places it may 
as well have been "just another Partioned Dataset"

MCM
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-09T22:19:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0i3k.1009834$Gl5.170089@fe02.news.easynews.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <7b36ba3d-04cf-461a-a9b1-497fe04ad468@25g2000hsx.googlegroups.com> <Pqh3k.145781$RG7.49472@fe09.news.easynews.com> <rPh3k.4468$N87.1844@nlpi068.nbdc.sbc.com>`

```
I stopped being personally active in mainframes about the time that Panvalet and 
Librarian were both being "replaced" by Endevor.  (SCLM never really caught on).

The Panvalet and Librarian uses as an IEBUDTE surrogate weren't very popular - 
once people stopped using punched cards, but the did still exist (and Micro 
Focus supports them - just as they do the INSERT, DELETE, etc) statements.

Now, WHY anyone doing "new" work would care, I can't imagine - but they do 
exist.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 12)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2008-06-10T11:23:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d07t44d2c33olehlrgtipm0b6amd8567hk@4ax.com>`
- **References:** `<nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <7b36ba3d-04cf-461a-a9b1-497fe04ad468@25g2000hsx.googlegroups.com> <Pqh3k.145781$RG7.49472@fe09.news.easynews.com> <rPh3k.4468$N87.1844@nlpi068.nbdc.sbc.com>`

```
On Mon, 9 Jun 2008 17:06:03 -0500, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
>news:Pqh3k.145781$RG7.49472@fe09.news.easynews.com...
…[13 more quoted lines elided]…
>

I've used Panvalet for years in my client's shops and it was used as a
source library and audit facility to track changes.  Now days Endevor
is the preferred tool for that sort of thing in my client's shops.
Some also use Changeman.  

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"You've got the brain of a four-year-old boy, and
I'll bet he was glad to get rid of it."
-- Groucho Marx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-09T21:44:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wuh3k.968992$us.160720@fe04.news.easynews.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <7b36ba3d-04cf-461a-a9b1-497fe04ad468@25g2000hsx.googlegroups.com>`

```
Have you (yet) looked at the IBM LRM (for the current Enterprise COBOL).  If 
not, check out:

  http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/IGY3LR40/CCONTENTS

If syntax is NOT described there, then this isn't a matter of "opinion" it is 
what is and is not supported with that compiler.

You never got back with answers to a bunch of earlier questions, but if you are 
still using the *OLD* (very old) Microsoft (not Micro Focus) compiler and want 
to develop code for IBM mainframes, then please compile with the following 
compiler directives:

  NOMF,COBOL370,FLAG(COBOL370),FLAGAS(E)

I think if you use that and try putting in a TYPEDEF, you will get a compiler 
error.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 9)_

- **From:** amir <ahsharif@gmail.com>
- **Date:** 2008-06-09T06:45:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e80567b3-5abf-4898-baea-5f84fa033f57@59g2000hsb.googlegroups.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com>`

```
Some people believe in do not use TYPEDEF in mainframe COBOL.
Can anyone more comment on?
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-06-09T14:15:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2jdu6$pnl$1@reader2.panix.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <e80567b3-5abf-4898-baea-5f84fa033f57@59g2000hsb.googlegroups.com>`

```
In article <e80567b3-5abf-4898-baea-5f84fa033f57@59g2000hsb.googlegroups.com>,
amir  <ahsharif@gmail.com> wrote:
>Some people believe in do not use TYPEDEF in mainframe COBOL.
>Can anyone more comment on?

Sure.

Different people have different beliefs.

DD
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 10)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-09T12:39:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<flqq44t0sf02d82vn2ijqsk6chbouana0p@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <e80567b3-5abf-4898-baea-5f84fa033f57@59g2000hsb.googlegroups.com>`

```
On Mon, 9 Jun 2008 06:45:12 -0700 (PDT), amir <ahsharif@gmail.com> wrote:

>Some people believe in do not use TYPEDEF in mainframe COBOL.
>Can anyone more comment on?

IBM does not support TYPEDEF, at least through Enterprise Cobol version 4.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-06-09T19:07:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adGdncpimscFKtDVnZ2dnUVZ_sninZ2d@posted.mid-floridainternet>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <e80567b3-5abf-4898-baea-5f84fa033f57@59g2000hsb.googlegroups.com>`

```

"amir" <ahsharif@gmail.com> wrote in message
news:e80567b3-5abf-4898-baea-5f84fa033f57@59g2000hsb.googlegroups.com...
> Some people believe in do not use TYPEDEF in mainframe COBOL.
> Can anyone more comment on?

According to the following source, if TYPEDEF is used in
Enterprise COBOL, "it is flagged with an informational message."

From <
http://publib.boulder.ibm.com/infocenter/pdthelp/v1r1/index.jsp?topic=/com.ibm.entcobol.doc_4.1/MG/igymapxb001.htm >
-----
Enterprise COBOL for z/OS, Version 4.1, Compiler and Runtime
Migration Guide

--------------------------------------------------

COBOL reserved word comparison
Key:

[snip]

RFD
The word is reserved for future development. If used, it is
flagged with an informational message.

[snip]

Table 1. Reserved word comparison

Reserved word Enterprise COBOL

[snip]

TYPEDEF       RFD
-----
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-10T00:41:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85k3k.438170$qg2.338247@fe08.news.easynews.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <dkjb44l2ljamags7oft2gl0um6qe8776uf@4ax.com> <g2694b01uts@news1.newsguy.com> <e80567b3-5abf-4898-baea-5f84fa033f57@59g2000hsb.googlegroups.com> <adGdncpimscFKtDVnZ2dnUVZ_sninZ2d@posted.mid-floridainternet>`

```
What gets an informational message is using "TYPEDEF" as a user-defined word. 
Any attempt to use it to actually define a TYPE won't work.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-04T03:45:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wdo1k.926241$Gl5.882561@fe02.news.easynews.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com>`

```
(Not posted to the newsgroup)

Do you have an "appropriate" contact in Newbury for documentation issues? (In 
the old days, I would have sent something to Alan Cocker, but I don't know if 
that would be "good" any more.)   I think this whole thing could be clearer. 
However, I went to the online dox at:
   http://supportline.microfocus.com/Documentation/books/es50sx03/espubb.htm

for the latest ServerExpress documentation.  Under "running" it says

"
a.. You can create a linked system executable file, which can be run directly 
from the command line.
See the chapter Packaging Applications for an introduction to executable file 
types.

"



However, the "link" to "Packaging Applications" is bad - and I couldn't find 
that or "linked system executable" elsewhere in the Dox.
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-06-04T04:53:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tcp1k.383648$qg2.244812@fe08.news.easynews.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <Wdo1k.926241$Gl5.882561@fe02.news.easynews.com>`

```
OOPS !!!
  I meant to do a "reply" rather than  a "reply group"  on this.

Sorry about sending it publicly ):
```

###### ↳ ↳ ↳ Re: Static, Dynamic, etc

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-06-04T00:13:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s95c441u64ghqdb6makr8u129qai3484u3@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <h%B0k.908221$Gl5.93236@fe02.news.easynews.com> <grl64455er9df1egj0lm6dht9gefdcetqq@4ax.com> <g2127u02vh@news2.newsguy.com> <u30944pdjona4c70j6n1llt48j7a24a3gk@4ax.com> <g23kpv0t3j@news3.newsguy.com> <Wdo1k.926241$Gl5.882561@fe02.news.easynews.com>`

```
On Wed, 04 Jun 2008 03:45:58 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>(Not posted to the newsgroup)

Whoops.

>Do you have an "appropriate" contact in Newbury for documentation issues? (In 
>the old days, I would have sent something to Alan Cocker, but I don't know if 
…[10 more quoted lines elided]…
>types.

You could ALWAYS make the main program an executable, by using the -x option. 
The issue we're discussing is how you link called programs. 

On Unix, the linker is usually not run separately (it can be). Linker options are placed
on the compiler line and the compiler calls the linker under the covers. 

A static link looks like this (assuming subprogs were already compiled to .o)
cob -x mainprog.cbl subprog1.o subprog2.o 
To also statically link the cobol runtime, add -Q Bstatic. The default is dynamic.

A dynamic link looks like this:
cob -Z subprog1.cbl subprog2.cbl -o libmylib.so  # create .so containing 2 programs
cob -x mainprog.cbl -l mylib

Michael is correct when he says both still work. What doesn't work is statically linking
the Cobol runtime. The migration guide says you cannot use linker option -Bstatic. The
option is written they way when running the linker (ld) separately, but MF has no control
over that. On the cob command line it is written -Q Bstatic, where -Q means 'put a dash in
front of the next word and pass it to the linker.' The migration guide contains a slight
error.

The page you are looking for is in Part 1.1 and 1.3. The cob flags you should be looking
for are in Part 3.
http://supportline.microfocus.com/Documentation/books/sx50/sx50indx.htm
```

##### ↳ ↳ Re: Reusability

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-06-02T07:32:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cbt744hr9g9svik0e5t33tanpa94e6jgf2@4ax.com>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com>`

```
On Sun, 01 Jun 2008 12:36:14 -0500, Robert <no@e.mail> wrote:

>>1- Common Reusability:
>>a. using Copy-Book files and COPY ... REPLACING ... BY ... statement
>
>You should never copy procedure division code. Instead, make it a callable program.

Why never?    

Procedure division copy code is often used to perform standard error
handling routines.

>REPLACING is not very useful for data division code. If you need two copies of the same
>structure, use OCCURS or qualification. 

I have used REPLACING to create unique names from a standard copybook.
It is not obvious to me how OCCURS or qualification would help me do
this.
```

###### ↳ ↳ ↳ Re: Reusability

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-06-02T10:09:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v8qdnb47h5a6Yt7VnZ2dnUVZ_oSunZ2d@mid-floridainternet>`
- **References:** `<9902dc52-5258-469b-957a-8c31dd5e8905@p25g2000hsf.googlegroups.com> <nsk5441svai249fkmeov981qctpf046hod@4ax.com> <cbt744hr9g9svik0e5t33tanpa94e6jgf2@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:cbt744hr9g9svik0e5t33tanpa94e6jgf2@4ax.com...
> On Sun, 01 Jun 2008 12:36:14 -0500, Robert <no@e.mail> wrote:
[snip]
> >REPLACING is not very useful for data division code. If you need two
copies of the same
> >structure, use OCCURS or qualification.
>
> I have used REPLACING to create unique names from a standard copybook.
> It is not obvious to me how OCCURS or qualification would help me do
> this.

It doesn't make the name unique; it makes the reference
(to the structure) unique!

FDIS, ISO/IEC 1989:2002, page 83, 8.4.1 Uniqueness
of reference,
"Every user-defined name in a source element is assigned,
by the user, to name a resource that is to be used in solving
a data processing problem. (See 8.3.1.1.1, User-defined
words.) In order to use a resource, a statement shall contain
a reference that uniquely identifies that resource. In order to
ensure uniqueness of reference, a user-defined name may be
qualified, subscripted, or reference modified as described in
the following paragraphs."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
