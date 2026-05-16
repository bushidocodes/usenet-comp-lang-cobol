[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microsoft Cobol 5.0 Help Needed

_5 messages · 2 participants · 2006-06_

---

### Microsoft Cobol 5.0 Help Needed

- **From:** "John Simpson" <jasimp@earthlink.net>
- **Date:** 2006-06-21T15:32:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s9hmg.49366$ZW3.12954@dukeread04>`

```
Yes, I know it's old. I have to deal with it because my client doesn't want 
to spend the money for a new compiler. In case someone doesn't recognize it, 
it's an older version of MicroFocus Cobol with the Microshaft name on it.

I'm working on a program that is giving me a 'subscript out of range' run 
time error at (PC 1A3F). The program is wall to wall subscripts, so there's 
no way I can locate the problem without seeing the line of code. I've 
searched the manuals and cannot find the compiler switch (or directive) that 
will give me a listing showing  the Program Counter references. Google 
didn't help a bit. I know it can be done, because I've done it (way) in the 
past. At 68+, I've come to the conclusion that the mind *may* be the first 
thing to go!

Any help will be greatly appreciated.

Thanks in advance.

John
```

#### ↳ Re: Microsoft Cobol 5.0 Help Needed

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-06-21T13:45:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1150922725.187086.11660@b68g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<s9hmg.49366$ZW3.12954@dukeread04>`
- **References:** `<s9hmg.49366$ZW3.12954@dukeread04>`

```

John Simpson wrote:

> I'm working on a program that is giving me a 'subscript out of range' run
> time error at (PC 1A3F). The program is wall to wall subscripts, so there's
> no way I can locate the problem without seeing the line of code. I've
> searched the manuals and cannot find the compiler switch (or directive) that
> will give me a listing showing  the Program Counter references.

NOERRLIST COPYLIST REF ASMLIST"progname.ASM" SOURCEASM STATS

If you use OPT"0" you will get the equivalent of an .INT and the
reference numbers will be on the copylist.  If you have OPT"1", which
is the default I think, then the reference is different and you need to
have the ASMLIST.
```

##### ↳ ↳ Re: Microsoft Cobol 5.0 Help Needed

- **From:** "John Simpson" <jasimp@earthlink.net>
- **Date:** 2006-06-22T15:37:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9kCmg.49425$ZW3.47379@dukeread04>`
- **References:** `<s9hmg.49366$ZW3.12954@dukeread04> <1150922725.187086.11660@b68g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1150922725.187086.11660@b68g2000cwa.googlegroups.com...
>
> John Simpson wrote:
…[15 more quoted lines elided]…
>

Richard,

I don't understand opt "1" and opt "0", but I'll play with the above 
directives.
Thanks for the response.

John
```

###### ↳ ↳ ↳ Re: Microsoft Cobol 5.0 Help Needed

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-06-22T15:18:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151014737.799369.161650@b68g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<9kCmg.49425$ZW3.47379@dukeread04>`
- **References:** `<s9hmg.49366$ZW3.12954@dukeread04> <1150922725.187086.11660@b68g2000cwa.googlegroups.com> <9kCmg.49425$ZW3.47379@dukeread04>`

```

John Simpson wrote:

> I don't understand opt "1" and opt "0", but I'll play with the above
> directives.

OPT is 'optimize'.

Original MF Cobol compilers (CIS Cobol of 1978 and its predecessor
Dataskill 1500 Cobol) produced 'interemediate code', 'byte code'
similar to pcode of some Pascals, or Java byte code today.  This is
portable to different machine architectures only requiring a run-time
interpreter that runs on the target machine. The MF files are of type
.int.

Later with Level II Cobol MF added a Generator to turn 'int' into
machine code for a specific architecture. This was less portable and
the code was about 3 times the size but ran 3 times faster (approx).
The files are of type .gnt.  The speed difference is usually irrelevant
for file and screen processing systems.

MF Cobol/2 for DOS, Windows 3.0 and OS/2 2.x, on which MS Cobol 4.x and
5.0 is based, allowed these .int and .gnt files to be buried in .EXEs
so hiding the nature of the files. But it is still possible to have
.EXEs that contain intermediate byte code and these will run as long as
the runtime byte code interpreter (COBLIB.DLE for DOS or COBLIB.DLW for
Win3.x) can be found.

OPT"0" gives byte code objects, OPT"1" generates machine code, OPT"2"
optimizes the code.  The problem is that the reference given on a 153
error is the byte offset of the failure, not a source code line number.
 With OPT"0" the COPYLIST REF directives will give the offsets of the
int code _before_ the generator has turned this into machine code. With
OPT"1" or "2" (one of these is the default) you need to get a listing
after the generator has turned it into machine code thus
ASMLIST"name.ASM" and SOURCEASM will list the machine code and add the
source code as comments so that the offset can be found and related to
the source directly.
```

###### ↳ ↳ ↳ Re: Microsoft Cobol 5.0 Help Needed

_(reply depth: 4)_

- **From:** "John Simpson" <jasimp@earthlink.net>
- **Date:** 2006-06-23T16:29:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%aYmg.49476$ZW3.27975@dukeread04>`
- **References:** `<s9hmg.49366$ZW3.12954@dukeread04> <1150922725.187086.11660@b68g2000cwa.googlegroups.com> <9kCmg.49425$ZW3.47379@dukeread04> <1151014737.799369.161650@b68g2000cwa.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1151014737.799369.161650@b68g2000cwa.googlegroups.com...
>
> John Simpson wrote:
…[36 more quoted lines elided]…
>

Thanks. This answers some old questions.

John
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
