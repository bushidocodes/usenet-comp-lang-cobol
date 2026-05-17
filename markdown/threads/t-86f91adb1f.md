[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Libsocket.a not found...

_9 messages · 3 participants · 1998-01 → 1998-02_

---

### Libsocket.a not found...

- **From:** "ron gladski" <ua-author-17074598@usenetarchives.gap>
- **Date:** 1998-01-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34cfbf84.0@news3.paonline.com>`

```

I'm trying to gen a generic runtime with MicroFocus Cobol V4.0.

I receive the following error:

i386ld libosx.a: can't find library libsocket.a

My system is ScoUnix 5.0.4 box with supplement rs504c installed.
The TCP/IP Development system is installed.

The libsocket.a file is located in the /usr/lib directory, and also in
/usr/lib/libp.

These directories are linked to:

/var/opt/K/SCO/tcpdev/2.1.0Eb/usr/lib/libsocket.a
and
/var/opt/K/SCO/tcpdev/2.1.0Eb/usr/lib/libp/libsocket.a
respectively

MicroFocus says it SHOULD work. SCO's web site doesn't have anything about
this issue.


Appreciate any help...

Ron Gladski
IS Mgr.
RGl··.@RIc··T.com
```

#### ↳ Re: Libsocket.a not found...

- **From:** "ron gladski" <ua-author-17074598@usenetarchives.gap>
- **Date:** 1998-01-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86f91adb1f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34cfbf84.0@news3.paonline.com>`
- **References:** `<34cfbf84.0@news3.paonline.com>`

```

My command line is:

cob -xe ""

The /usr/lib/cobol/coblib/liblist file:

/*
@(#)liblist 4.6
*/
/* This file specifies which libraries to use for different passes of the
* system linker.
* The first character of each line is treated as a selector, the selectors
* supported at present are:
* 'i' - initialization routines
* 'p' - profiler initialization routines
* 'c' - cobol libraries
* 's' - system libraries
* '1' - pass 1 linker specials
* '2' - pass 2 linker specials
* 'F' - cob -F linker specials
*/
i/lib/crt1.o
p/lib/mcrt1.o
c-L$COBDIR/coblib
c-lfhutil
c-lcobol
c-lasmcrtn
c-lcrtn
c-lsupp
c-lscreen
c-losx
s-lsocket
s-lintl
s-lc
s/lib/crtn.o


The libsocket.a is probably called from s-lsocket. If I comment out
s-lsocket, I get a list of undefined symbols (_DYNAMIC,
htons,bind,send,gethostname,etc...)


*---------------------------------------------------------------------------
-------------------
Ron Gladski wrote in message <34c··.@new··e.com>...
› I'm trying to gen a generic runtime with MicroFocus Cobol V4.0.
› 
…[26 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Libsocket.a not found...

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-01-28T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86f91adb1f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-86f91adb1f-p2@usenetarchives.gap>`
- **References:** `<34cfbf84.0@news3.paonline.com> <gap-86f91adb1f-p2@usenetarchives.gap>`

```

Ron Gladski wrote:
› 
› My command line is:
› 
›     cob -xe ""
 
› OK. Can't get much simpler than that :)
 
› The /usr/lib/cobol/coblib/liblist file:
› 
…[16 more quoted lines elided]…
› The libsocket.a is probably called from s-lsocket.

Correct - That line is causing cob to give "-lsocket" to the linker
*after* the COBOL/app archives (as it should be).

› If I comment out
› s-lsocket, I get a list of undefined symbols (_DYNAMIC,
› htons,bind,send,gethostname,etc...)

OK. This means that libsocket.a *was* being picked up (I recognise
at least one of those symbols as being from libsocket.a).
That brings me back to your original question:

› Ron Gladski wrote in message <34c··.@new··e.com>...
›› I'm trying to gen a generic runtime with MicroFocus Cobol V4.0.
…[3 more quoted lines elided]…
››        i386ld libosx.a:  can't find library libsocket.a

Do you have any SCO manuals which say exactly what that error means ?
It obviously doesn't mean what I thought, as your liblist file seems
to be correct (and removing the s-lsocket entry does what I would
expect on a correctly functioning installation).

It's strange that it's mentioning archive names rather than symbol
names (for static linking, archives don't reference other archives,
only symbols). It's possible that you are seeing a problem mixing
COFF and ELF objects.

Micro Focus COBOL V4.0 was built on SCO V3 (and is therefore COFF),
however SCO V5 uses the ELF format.

It might be possible to get around this (if it is indeed your problem)
by forcing the linker to use ELF format (It can convert COFF objects to
ELF on the fly, but not the other way around).
By default, it will use whichever format the first objects/archives it
sees are in (in this case, the COBOL archives are first, so that is
COFF). Maybe this error message means "I am working in COFF mode, but I
have now seen ELF objects" ? Coincidentally, according to your liblist
file, the last COBOL (COFF) archive supplied is libosx.a and the first
system (ELF) one is libsocket.a.

Two things to try:

Add a line "s-lc" between "c-losx" and "s-lsocket" (leave the old
"s-lc" line there - it's still needed). Does the error now report
against libc.a ?

Also, try the following command:

cob -xe "" -Q "-b ELF"

This tells "cob" to tell the linker to override it's default of
choosing COFF mode when it sees the first COBOL system archive, so
it won't choke when it eventually sees an ELF object. You might want to
check the native "ld" option (given to "cob" with -Q) using "man ld"
first (I don't have a machine handy to try any of this on).

FYI: I believe Micro Focus COBOL V4.1, was built natively on SCO V5 and
will therefore be ELF. You might feel more confident in the long run by
upgrading.

Cheers,
Kev.
```

###### ↳ ↳ ↳ Re: Libsocket.a not found...

- **From:** "ron gladski" <ua-author-17074598@usenetarchives.gap>
- **Date:** 1998-01-29T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86f91adb1f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-86f91adb1f-p3@usenetarchives.gap>`
- **References:** `<34cfbf84.0@news3.paonline.com> <gap-86f91adb1f-p2@usenetarchives.gap> <gap-86f91adb1f-p3@usenetarchives.gap>`

```


Kevin Digweed wrote in message <34D··.@mfl··o.uk>...
› Do you have any SCO manuals which say exactly what that error means ?
 
 
› No Kev, Nothing from the SCO side...
 
› Two things to try:
› 
› Add a line "s-lc" between "c-losx" and "s-lsocket" (leave the old
› "s-lc" line there - it's still needed). Does the error now report
› against libc.a ?
 
› Yes, the error comes from libc.a vs, libosx.a
 
› 
› Also, try the following command:
› 
› cob -xe "" -Q "-b ELF"


cob returns the following:
i386ld crt1.o: unknown flag: b ELF
i386ld libosx.a: can't find library libsocket.a

Ron Gladski
```

###### ↳ ↳ ↳ Re: Libsocket.a not found...

_(reply depth: 4)_

- **From:** "ron gladski" <ua-author-17074598@usenetarchives.gap>
- **Date:** 1998-02-01T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86f91adb1f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-86f91adb1f-p4@usenetarchives.gap>`
- **References:** `<34cfbf84.0@news3.paonline.com> <gap-86f91adb1f-p2@usenetarchives.gap> <gap-86f91adb1f-p3@usenetarchives.gap> <gap-86f91adb1f-p4@usenetarchives.gap>`

```


› Kevin Digweed wrote in message <34D··.@mfl··o.uk>...
› Do you have any SCO manuals which say exactly what that error means ?
 
› No Kev, Nothing from the SCO side...
 
› Two things to try:
 
› Add a line "s-lc" between "c-losx" and "s-lsocket" (leave the old
› "s-lc" line there - it's still needed). Does the error now report
› against libc.a ?
 
 
› Yes, the error comes from libc.a vs, libosx.a
 
 
› Also, try the following command:
 
› cob -xe "" -Q "-b ELF"


cob returns the following:
i386ld crt1.o: unknown flag: b ELF
i386ld libosx.a: can't find library libsocket.a

Ron Gladski
```

###### ↳ ↳ ↳ Re: Libsocket.a not found...

_(reply depth: 5)_

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-02-02T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86f91adb1f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-86f91adb1f-p5@usenetarchives.gap>`
- **References:** `<34cfbf84.0@news3.paonline.com> <gap-86f91adb1f-p2@usenetarchives.gap> <gap-86f91adb1f-p3@usenetarchives.gap> <gap-86f91adb1f-p4@usenetarchives.gap> <gap-86f91adb1f-p5@usenetarchives.gap>`

```

Hi Ron.

›› Add a line "s-lc" between "c-losx" and "s-lsocket" (leave the old
›› "s-lc" line there - it's still needed). Does the error now report
›› against libc.a ?
› 
› Yes, the error comes from libc.a vs, libosx.a

This is good (believe it or not). It lends a bit of weight to the
COFF vs ELF theory.

›› Also, try the following command:
› 
…[4 more quoted lines elided]…
›     i386ld libosx.a:  can't find library libsocket.a

OK. These are actually error messages from the linker. It looks like
cob is passing through the -Q "parameters" as a single option. They
need to be separate. Therefore, try:

cob -xe "" -Q -b -Q ELF

This should pass "-b" and "ELF" through to the linker as separate
parameters. I'm still assuming that "-b ELF" is the correct way of
telling the linker that it should work in ELF mode. Does the output of
"man ld" confirm this ? If you're not sure, email me the output of
"man ld" and I'll take a look.

Cheers,
Kev.
```

###### ↳ ↳ ↳ Re: Libsocket.a not found...

_(reply depth: 5)_

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-02-02T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86f91adb1f-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-86f91adb1f-p5@usenetarchives.gap>`
- **References:** `<34cfbf84.0@news3.paonline.com> <gap-86f91adb1f-p2@usenetarchives.gap> <gap-86f91adb1f-p3@usenetarchives.gap> <gap-86f91adb1f-p4@usenetarchives.gap> <gap-86f91adb1f-p5@usenetarchives.gap>`

```

On Mon, 2 Feb 1998 17:35:22 -0500, "Ron Gladski"
wrote:
›
› No Kev, Nothing from the SCO side...

please do read the following and try to install the "OSS459A" patch
as stated.

I think it will solve the problem but I can not try it.
the file is in " http://www5.sco.com/cgi-bin/ssl_getsupplement?OSS459
"

Best regards

Frederico Fonseca

idld(M) ld(CP) oracle7 coff can't find library libraries
libsocket.a libnsl_s.a missing error
install linker fails editor openserver host desktop faststart oses
504 5.0.4 i386ld ENGREF
SCO-244-396 ERGREF 710241 OSS459A oss459a oracle

Release

SCO OpenServer Enterprise System Release 5.0.4
SCO OpenServer Host System Release 5.0.4
SCO OpenServer Desktop System Release 5.0.4
SCO OpenServer Internet FastStart Release 5.0.4

Problem

The COFF linker fails to search the second default directory for
required libraries.

Solution

Support Level Supplement (SLS) OSS459A, the COFF Linker
Supplement, corrects this
problem. This SLS was created for Oracle7.

See the attached cover letter that accompanies this SLS for more
information, including
installation instructions.

Dear SCO Customer,

The enclosed Support Level Supplement (SLS) OSS459A, the COFF Linker
Supplement, resolves a problem found in the COFF Linker which ships
in the OpenServer 5.0.4 link kit. The linker failed to search the
second
default directory for required libraries. This SLS was created for
Oracle7.

Note: After installing OSS459A, this problem will still exist in the
COFF Linker included in the OpenServer 5.0.4 development
system;
a fix for all copies of the COFF linker will ship in a later
Release Supplement.


RELEASE INFORMATION

SLS OSS459A is intended for use on these products:

SCO OpenServer Host System Release 5.0.4
SCO OpenServer Desktop System Release 5.0.4
SCO OpenServer Enterprise System Release 5.0.4
SCO OpenServer Internet FastStart Release 5.0.4
```

###### ↳ ↳ ↳ Re: Libsocket.a not found...

_(reply depth: 4)_

- **From:** "ron gladski" <ua-author-17074598@usenetarchives.gap>
- **Date:** 1998-02-01T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86f91adb1f-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-86f91adb1f-p4@usenetarchives.gap>`
- **References:** `<34cfbf84.0@news3.paonline.com> <gap-86f91adb1f-p2@usenetarchives.gap> <gap-86f91adb1f-p3@usenetarchives.gap> <gap-86f91adb1f-p4@usenetarchives.gap>`

```


› Kevin Digweed wrote in message <34D··.@mfl··o.uk>...
› Do you have any SCO manuals which say exactly what that error means ?
…[17 more quoted lines elided]…
› 
cob returns the following:
i386ld crt1.o: unknown flag: b ELF
i386ld libosx.a: can't find library libsocket.a


Ron Gladski
```

#### ↳ Re: Libsocket.a not found...

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-01-28T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86f91adb1f-p9@usenetarchives.gap>`
- **In-Reply-To:** `<34cfbf84.0@news3.paonline.com>`
- **References:** `<34cfbf84.0@news3.paonline.com>`

```

Ron Gladski wrote:
› 
› I'm trying to gen a generic runtime with MicroFocus Cobol V4.0.
…[9 more quoted lines elided]…
› /usr/lib/libp.

Hi Ron.

I assume you're using the "cob" utility to build the RTS. It would help
if you could give the full "cob" command line, and also the contents
of the file $COBDIR/coblib/liblist (the "cob" linker options config
file).

In the meantime, I'll try to assist without that information.

In general, there are two "sets" of archive files which cob uses to
build the RTS - Application/COBOL system archives and OS archives.
As a general rule, the OS archives MUST come last on the linker command
line (the linker will only look at each archive once, in the order
they appear on the command line. Usually it's the COBOL system and
application archives which reference symbols in the OS archives, hence
they must come first).

libsocket.a is an OS archive, so must be on the linker command line
AFTER all COBOL system and application archives have been listed.

In the file $COBDIR/coblib/liblist, the "-lsocket" entry (if there is
one) must be preceeded by a 's' character, to tell the system that it
is a system archive. This means it will be placed after any 'c'
entries in the file, and after any "-larchive" entries on the "cob"
command line.

If you are using the "cob" command line to specify "-lsocket", then
you must similarly tell "cob" that it's an OS archive by replacing
the minus sign with a plus (ie, +lsocket). The same goes if you are
giving any "system" -L directories (ie, -L/usr/lib should be specified
to "cob" as +L/usr/lib).
"cob" ensures that any "-L/-l" arguments appear on the linker command
line before any "+L/+l" arguments (though of course, the "+" versions
are changed to "-" by the time the linker sees them).

If none of that helps, please post (to the newsgroup) the command line
and liblist file contents.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
