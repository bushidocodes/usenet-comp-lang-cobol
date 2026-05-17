[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL and C: Do they mesh?

_5 messages · 5 participants · 1995-09 → 1995-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL and C: Do they mesh?

- **From:** "dlei..." <ua-author-16068968@usenetarchives.gap>
- **Date:** 1995-09-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44fj6c$c14@news2.delphi.com>`

```
Yes, it's me again... I seem to be posting a lot of questions on this
newsgroup.

We are porting a monstrous system from MVS to HP-UX. Some modules
are in assembler. Two opposing schools of thought have broken out
in our porting team. One team wants to use C whenever possible, and
they claim MF COBOL 3.1 will cheerfully cooperate with C modules.
THe other team says the COBOL-to-C overhead will be significant and
that it will be a shotgun marriage.

Any comments from anyone who has done this? Our MF sales rep has told
us that it's easy, but we are somewhat skeptical of his comments.

Thanks.
Dan Leifker
dle··.@del··i.com
```

#### ↳ Re: MF COBOL and C: Do they mesh?

- **From:** "mobu..." <ua-author-15667290@usenetarchives.gap>
- **Date:** 1995-09-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3ff9b5eb3d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<44fj6c$c14@news2.delphi.com>`
- **References:** `<44fj6c$c14@news2.delphi.com>`

```
dle··.@del··i.com
says:
› We are porting a monstrous system from MVS to HP-UX.  Some modules
› are in assembler.  Two opposing schools of thought have broken out
…[3 more quoted lines elided]…
› that it will be a shotgun marriage.
 
› Any comments from anyone who has done this?  Our MF sales rep has told
› us that it's easy, but we are somewhat skeptical of his comments.

I wrote a Query/Report system that used COBOL for the front end (screens)
and
C for the file handling to allow English based queries on Micro-Focus and
AcuCOBOL files.

Micro Focus allows the marriage in two ways.

C can be directly called from COBOL if the final package is compiled down
to
an executable. There are some things to consider in the C such as the fact
that passed parameters are always received as pointers, and passed
strings are not NUL terminated. Since COBOL forces a known size on all
data
types, this isn't a real problem. The C code just processes the passed
parameter for a known length.

The other method is used when compiling MicroFocus to intermediate code.

The runtime that will execute the code has to be modified and relinked to
include the C runtime routines. This is a bit more complicated. The first
solution is easy, just compile and link. The second requires a C module
with table entries that identify the name of the C routine, parameters
and some other over head. The table, C code and original runtime library
are
linked together and the new executable is used as a replacement runtime.

Both methods work, but debugging is a big headache. If your problem is
in C then use the system debugger, if it's in COBOL then use the Animator.

Micro Focus Animator debugging really only works with the second method
(compiled to .INT files with a modified runtime), and I have experienced
problems trying to debug a linked executable. After converting to .INT
to use Animator, the bug disappears, but it's still there in the
executable.

Anyway, it's pretty easy, and a lot less painful than other cross language
marriages that I have been involved in.

mob··.@a··.com
```

##### ↳ ↳ Re: MF COBOL and C: Do they mesh?

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-10-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3ff9b5eb3d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3ff9b5eb3d-p2@usenetarchives.gap>`
- **References:** `<44fj6c$c14@news2.delphi.com> <gap-3ff9b5eb3d-p2@usenetarchives.gap>`

```

Sorry. I realise I've already replied to this thread, but I've a couple of
other comments now I've seen one of the earlier articles (they didn't arrive
here in order).

In article <44gb3q$p.··.@new··l.com>, mob··.@a··.com (MoBudlong) writes:
› dle··.@del··i.com
› says:
…[6 more quoted lines elided]…
› [snip]
 
› Micro Focus allows the marriage in two ways.
› 
…[13 more quoted lines elided]…
› linked together and the new executable is used as a replacement runtime.

This comment is the one that is confusing me. The original question was with
regard to porting to HP-UX. On all of our Unix products, calling C from COBOL
is exactly the same at source code level whether the COBOL is in .int .gnt or
.o (*).

ie:

cprog.c:
int
cprog(int x)
{
return x;
}

prog.cbl:
procedure division.
main section.
para.
call "cprog" using by value 54 size 4
exhibit named return-code
stop run.

1. .int (or .gnt) calling the C :
----------------------------------

$ cob -i prog.cbl cprog.c
(or cob -u prog.cbl cprog.c)

This will leave you with an RTS (./cprog) with your C program to linked in, so:

$ ./cprog prog.int
(or ./cprog prog.gnt)

... will run it.

2. statically linked calling the C :
-------------------------------------

$ cob -x prog.cbl cprog.c
$ ./prog

There are no "tables" to build, or parameter lists to define.

(*) The exception here is if a CALL is made to an ENTRY point within a program
before the main program is called. This will work fine when statically
linked (as all the entry points are visible initially), but not in the
dynamic environment (as they are only visible when the program is loaded
by the RTS from disk).


Cheers,
Kev.

Kevin. Advancing all electric at Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

#### ↳ Re: MF COBOL and C: Do they mesh?

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1995-09-28T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3ff9b5eb3d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<44fj6c$c14@news2.delphi.com>`
- **References:** `<44fj6c$c14@news2.delphi.com>`

```
I don't think the overhead will be any more significant than on MVS.
Perhaps it is time to consider doing those assembler things in COBOL.
The language has had quite a few significant advances sinces your system
was most likely coded.

Tom Morrison, T.M··.@li··t.com
Relativity (div. Liant Software)
512-719-7019  FAX:512-719-7070  WWW: http://www.liant.com/
```

#### ↳ Re: MF COBOL and C: Do they mesh?

- **From:** "a..." <ua-author-512315@usenetarchives.gap>
- **Date:** 1995-09-29T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3ff9b5eb3d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<44fj6c$c14@news2.delphi.com>`
- **References:** `<44fj6c$c14@news2.delphi.com>`

```
DLE··.@new··i.com (DLE··.@DEL··I.COM) wrote:


› THe other team says the COBOL-to-C overhead will be significant and
› that it will be a shotgun marriage.
› Any comments from anyone who has done this?  Our MF sales rep has told
› us that it's easy, but we are somewhat skeptical of his comments.

Hi,
this is my first attempt at using Newsgroups so if this goes
wrong....

Your MF sales rep is actually telling the truth. Using MF 32bit
technology COBOL has the same stack model as C and so they comunicate
v. easily. Infact if you configure the ANIMATOR correctly you should
even be able to do end-to-end debugging.

It gets a little harder with there 16bit stuff but it can still be
done.

MF ALWAYS recomend that you code the business part of your app. in
COBOL and if you wish to use other tools for the data or interface
then they will do everything in their power to intergrate.

Sales Support Consultant
MICRO FOCUS Ltd.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
