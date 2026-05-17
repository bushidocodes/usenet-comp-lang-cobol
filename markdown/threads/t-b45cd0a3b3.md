[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HIMEM Question, Please Help

_3 messages · 3 participants · 1996-01 → 1996-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HIMEM Question, Please Help

- **From:** "msta..." <ua-author-1932963@usenetarchives.gap>
- **Date:** 1996-01-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4emie7$s7b@ixnews7.ix.netcom.com>`

```
In MicroFocus Cobol version 2.3, can you overcome the problem with
having to run within the base 640k of RAM?

Is there a simple way to load and run programs in HIMEM?

Thanks in advance-

Jonathan Mstar
```

#### ↳ Re: HIMEM Question, Please Help

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-01-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b45cd0a3b3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4emie7$s7b@ixnews7.ix.netcom.com>`
- **References:** `<4emie7$s7b@ixnews7.ix.netcom.com>`

```
In <4emie7$s.··.@ixn··m.com>, mst··.@ix.··m.com(Jonathan B. Morningstar ) writes:
› In MicroFocus Cobol version 2.3, can you overcome the problem with
› having to run within the base 640k of RAM?
› Is there a simple way to load and run programs in HIMEM?
› Thanks in advance-
› Jonathan Mstar

No, there really isn't. It works with MF Cobol because the run-time
works as a DOS-Extender. There are other DOS-Extenders, but it is
non-trivial to use these. There is no magic switch you can flip and
then everything runs in extended memory.

Leif Svalgaard 'le··.@i··.net'
```

#### ↳ Re: HIMEM Question, Please Help

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-02-01T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b45cd0a3b3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4emie7$s7b@ixnews7.ix.netcom.com>`
- **References:** `<4emie7$s7b@ixnews7.ix.netcom.com>`

```
In message <<4emie7$s.··.@ixn··m.com>> mst··.@ix.··m.com writes:
› having to run within the base 640k of RAM?
›
› Is there a simple way to load and run programs in HIMEM?

I develop primarily for DOS (though I use Multiuser-DOS) where
the 640Kb limit exists, but I run applications up to several
megabytes in size. The secret is to use dynamic loading.
Each application is made up of many function modules: customer
maintenance, order entry, invoice print, etc. There are also
utility modules: menu, system control, etc.

In general there is one core module which just does a:

MOVE "MENU" TO Program-Name
MOVE "MENU" TO Next-Program
PERFORM Call-Program
UNTIL Next-Program = "FINISH"
STOP RUN.
Call-Program.
CALL Program-Name
USING Linkage-Data
CANCEL Program-Name
MOVE Next-Program TO Program-Name
MOVE "MENU" TO Next-Program
.

Any program can change Next-Program to whatever is to be done
next, for example order entry can set next-program to picking-slip
print. The Linkage-Data is COPYed into Working-Storage in the
core module and into Linkage Section in all other programs.
Only the core does a STOP RUN, all others EXIT PROGRAM.

The CANCEL removes the exiting program from memory leaving room
for the next called program.

Actual systems are actually a lot more complex with utility
routines that are callable from many modules, so it is critical
to get the loading sequence right. With this structure I get
large systems to run in as little as 450Kb mfree memory.

With MF Level-II Cobol on Concurrent-DOS I could run half a
dozen users in a 1 MByte machine. This is because the CDOS
Level-II run-time used the shared memory feature of CDOS so its
code was only resident once and all data areas and called programs
used the OS memory management calls to allocate and release
memory as calls and cancels were issued.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
