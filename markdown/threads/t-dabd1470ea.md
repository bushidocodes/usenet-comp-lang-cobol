[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL

_19 messages · 10 participants · 2004-12 → 2005-01_

---

### COBOL

- **From:** "TammyBain" <baint@cityofrochester.gov>
- **Date:** 2004-12-22T17:09:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com>`

```
I can't find any documentation on assign statements with 
-UT- in them.    Does the 'UT' stand for Unit Tape or Utility Tape?
```

#### ↳ Re: COBOL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-12-22T22:39:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vImyd.1331040$SM5.104426@news.easynews.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com>`

```
You don't tell us

 - COMPILER (release, version, and vendor)

- Operating system (e.g. VSE, MVS, z/OS, Windows, whatever)

- What YOUR compiler vendor's documentation (LRM) says for the "Select/Assign 
clause).

  ***

However, for IBM mainframes the bottom-line is that UT-xxxx is a feature from 
VERY old (long unsupported) compilers that is IGNORED (treated as a comment) in 
all currently supported compilers.
```

#### ↳ Re: COBOL

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-12-23T01:22:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com>`

```
On Wed, 22 Dec 2004 17:09:25 -0500, "TammyBain"
<baint@cityofrochester.gov> wrote:

>I can't find any documentation on assign statements with 
>-UT- in them.    Does the 'UT' stand for Unit Tape or Utility Tape?  

Device-specific assignments are obsolete. Nowadays,  ASSIGN statements
take three forms:

1.  SELECT file ASSIGN TO '/path/file'

2.  SELECT file ASSIGN TO data-name (which contains /path/file)

3. SELECT file ASSIGN TO ddname (environment variable or JCL
containing /path/file)
```

##### ↳ ↳ Re: COBOL

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-12-22T21:12:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JSpyd.27730$GK5.1338462@news20.bellglobal.com>`
- **In-Reply-To:** `<137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com>`

```
Robert Wagner wrote:
> On Wed, 22 Dec 2004 17:09:25 -0500, "TammyBain"
> <baint@cityofrochester.gov> wrote:
…[14 more quoted lines elided]…
> containing /path/file)

"PRN".

Donald
```

###### ↳ ↳ ↳ Re: COBOL

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-12-22T21:18:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XXpyd.27800$GK5.1340484@news20.bellglobal.com>`
- **In-Reply-To:** `<JSpyd.27730$GK5.1338462@news20.bellglobal.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com> <JSpyd.27730$GK5.1338462@news20.bellglobal.com>`

```
Donald Tees wrote:
> Robert Wagner wrote:
> 
…[24 more quoted lines elided]…
> 

Not to mention standard-in and standard-out, though I suppose they are 
really "JCL names".  Maybe printers are as well. Depends on how you look 
at it. What is the context TamyBain? Platform and compiler?

Donald
```

##### ↳ ↳ Re: COBOL

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-12-23T08:53:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqet70$1v83$1@si05.rsvl.unisys.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com>`

```

"Robert Wagner" <spamblocker-robert@wagner.net> wrote in message
news:137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com...

> Device-specific assignments are obsolete. Nowadays,  ASSIGN statements
> take three forms:
…[6 more quoted lines elided]…
> containing /path/file)

Ummm.... In what context?   Although exactly *what* a file may be assigned
to is still defined by the implementor, ISO/IEC 1989:2002 specifically
changed the terminology for the non-literal case from "implementor-name-1"
to "device-name".

While IBM may have favored such intutively-clear device-names as
"SYS00C-UR-2540R-S" at one time, Unisys MCP-based systems have gone more
toward such unfathomable mnemonics as "READER" and "DISK" in this context,
believing that more specific assignation than that is rightly more the
purview of the operating environment than of the COBOL program itself.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-12-23T19:41:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9NP2iZw9flB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com> <cqet70$1v83$1@si05.rsvl.unisys.com>`

```
.    On  23.12.04
  wrote  charles.stevens@unisys.com (Chuck Stevens)
     on  /COMP/LANG/COBOL
     in  cqet70$1v83$1@si05.rsvl.unisys.com
  about  Re: COBOL


CS> While IBM may have favored such intutively-clear device-names as
CS> "SYS00C-UR-2540R-S" at one time, Unisys MCP-based systems have gone
CS> more toward such unfathomable mnemonics as "READER" and "DISK" in
CS> this context, believing that more specific assignation than that is
CS> rightly more the purview of the operating environment than of the
CS> COBOL program itself.


    Similar on the OS/2200 side -- there were three standard devices:  
CARDREADER, CARDPUNCH and PRINTER, similar to UNIX' so popular SYSIN,  
SYSOUT and SYSERR. Then of course, DISC and TAPE, with a second name  
referring to the name actually used in the runstream, i.e. job.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Es gibt eine wahre und eine fï¿½rmliche Orthographie. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: COBOL

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2004-12-23T16:14:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqfn26$2g3i$1@si05.rsvl.unisys.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com> <cqet70$1v83$1@si05.rsvl.unisys.com> <9NP2iZw9flB@jpberlin-l.willms.jpberlin.de>`

```
On the MCP side, you'd do something like "SELECT BLIVET ASSIGN TO READER" in
the program.

In the WFL job running the program you ccan do something like
    "RUN <object-program-name>; FILE BLIVET (KIND=DISK)".
You can use the ancient VALUE OF in the FD of the program like
    "VALUE OF KIND IS VALUE (DISK)".
In the Procedure Division, you can do
    "CHANGE ATTRIBUTE KIND OF BLIVET TO VALUE (DISK)"
In the compilation of the program, this permanently overrides the device
assignment:
    "COMPILE <object-program-name> .... FILE BLIVET (KIND=DISK); ..."
    (to modify the *compiler's* file you precede the keyword FILE with
COMPILER)
After the program's compiled you can also change it permanently by:
    "WFL MODIFY <object-program-name> FILE BLIVET (KIND=DISK);"

The "handle" by which the file is known to the system is the name by which
it was declared in the program -- in this instance "BLIVET".  That "handle"
is itself a file attribute, INTNAME, subject to the same set of mechanisms;
the externally-visible name can thus be changed to be different from what's
used in the program, to no particular ill effect.

    -Chuck Stevens

"Lueko Willms" <l.willms@jpberlin.de> wrote in message
news:9NP2iZw9flB@jpberlin-l.willms.jpberlin.de...
> .    On  23.12.04
>   wrote  charles.stevens@unisys.com (Chuck Stevens)
…[23 more quoted lines elided]…
> Es gibt eine wahre und eine f�rmliche Orthographie. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: COBOL

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-12-24T18:47:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<331orsF3sn49mU1@individual.net>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com> <cqet70$1v83$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:cqet70$1v83$1@si05.rsvl.unisys.com...
>
> "Robert Wagner" <spamblocker-robert@wagner.net> wrote in message
…[22 more quoted lines elided]…
>
"SYS00C-UR-2540R-S"...  I recognize immediately as an IBM unit record
device, 2540 80 column card reader without punch capability, assigned to
slot 12 on the "slow peripherals" bus.

"READER"  ...Now what the Hell does THAT mean? Paper tape, punched cards,
OCR, guy in the Library? What?! <G>

Pete.
```

###### ↳ ↳ ↳ Re: COBOL

_(reply depth: 4)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-12-24T06:08:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9NT5F9LPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <cqet70$1v83$1@si05.rsvl.unisys.com> <331orsF3sn49mU1@individual.net>`

```
.    On  24.12.04
  wrote  dashwood@enternet.co.nz (Pete Dashwood)
     on  /COMP/LANG/COBOL
     in  331orsF3sn49mU1@individual.net
  about  Re: COBOL


PD> "READER"  ...Now what the Hell does THAT mean? Paper tape, punched
PD> cards, OCR, guy in the Library? What?! <G>

   Translate it to SYSIN.

   Usable in the good olde dayse both for punched cards as well as  
punched tape.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Das Buch, das in der Welt am ehesten verboten zu werden verdiente, wï¿½re ein Katalogus von verbotenen Bï¿½chern. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: COBOL

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-01-04T11:04:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<crepc1$1tc5$1@si05.rsvl.unisys.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <cqet70$1v83$1@si05.rsvl.unisys.com> <331orsF3sn49mU1@individual.net> <9NT5F9LPflB@jpberlin-l.willms.jpberlin.de>`

```

"Lueko Willms" <l.willms@jpberlin.de> wrote in message
news:9NT5F9LPflB@jpberlin-l.willms.jpberlin.de...
> .    On  24.12.04
>   wrote  dashwood@enternet.co.nz (Pete Dashwood)
…[11 more quoted lines elided]…
> punched tape.

Actually, B6500 COBOL(60) had CARD-READER with READER as a synonym; it also
had PAPER-TAPE-READER.  Paper tape devices were apparently dropped very
early in the history of the B6700; COBOL(68) has no SELECT syntax for them,
though it continued to allow CARD-READER and CARD-PUNCH.  By the time
COBOL74 rolled around the SELECTable devices had been pared down to just
seven (DISK, TAPE, READER, PUNCH, PRINTER, REMOTE and PORT)  with any and
all refinements beyond that handled programmatically either by VALUE OF
extensions in the FD or CHANGE ATTRIBUTE statements in the Procedure
DIVISION, or externally by WFL file equations, at compile time, at execution
time, or through WFL MODIFY statements against the object code file itself.

For sequential files, there are only a few edge cases in which the object
code for the I/O statements differs anyway; the system's had almost entirely
device-independent I/O for a very, very long time.  A program with a READER
file will operate just fine if you reassign it to an extant file on TAPE or
DISK, or even an available REMOTE or PORT file.  If you try something
inappropriate like attempt to OPEN a file INPUT when it's actually assigned
to a printer or printer-backup device, or OUTPUT when it's actually assigned
to READER (which these days is actually a file in the WFL stream; we no
longer support physical card devices), most likely you'll get your knuckles
rapped at execution time.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: COBOL

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-12-24T03:11:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqgivp$5iv$1@panix5.panix.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com> <cqet70$1v83$1@si05.rsvl.unisys.com> <331orsF3sn49mU1@individual.net>`

```
In article <331orsF3sn49mU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>
>"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
>news:cqet70$1v83$1@si05.rsvl.unisys.com...

[snip]

>> While IBM may have favored such intutively-clear device-names as
>> "SYS00C-UR-2540R-S" at one time, Unisys MCP-based systems have gone more
…[9 more quoted lines elided]…
>OCR, guy in the Library? What?! <G>

Meaning is the result of interpretation, Mr Dashwood... but it might help 
to demonstrate that 'obvious is in the mind of the beholder'.

DD
```

###### ↳ ↳ ↳ Re: COBOL

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-12-24T23:22:46+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3328vsF3svptkU1@individual.net>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <137ks05k9jnticqq4qihfq5obkmlri1lam@4ax.com> <cqet70$1v83$1@si05.rsvl.unisys.com> <331orsF3sn49mU1@individual.net> <cqgivp$5iv$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:cqgivp$5iv$1@panix5.panix.com...
> In article <331orsF3sn49mU1@individual.net>,
> Pete Dashwood <dashwood@enternet.co.nz> wrote:
…[7 more quoted lines elided]…
> >> "SYS00C-UR-2540R-S" at one time, Unisys MCP-based systems have gone
more
> >> toward such unfathomable mnemonics as "READER" and "DISK" in this
context,
> >> believing that more specific assignation than that is rightly more the
> >> purview of the operating environment than of the COBOL program itself.
…[10 more quoted lines elided]…
>
(Precisely my point, Your Majesty <G>. Though when spelled out it kinda
loses subtlety...<G>)

No idea what I'm doing here on Xmas Eve. Stopped to collect some mail and
sudde
nly I'm in CLC... I need another drink... Best wishes to all - Oh...and
confusion to your enemies, Sire....

Pete (or someone very like him....)
```

#### ↳ Re: COBOL

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-12-23T22:00:38+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32vfppF3pmhk0U1@individual.net>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com>`

```

"TammyBain" <baint@cityofrochester.gov> wrote in message
news:781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com...
> I can't find any documentation on assign statements with
> -UT- in them.    Does the 'UT' stand for Unit Tape or Utility Tape?
>
>
The UT stands for "Utility". In the very olden days, before disks were
invented and freely available, this was tape. Later, replaced by disk
drives, these "utility" devices were available for any kind of storage
requirement. The UT was not about a physical device, it was about the
logical use of a physical device, i.e. as a "Utility".

Other posts have covered the implications for COBOL; I just thought your
actual question needed an answer.

Pete.
```

##### ↳ ↳ Re: COBOL

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2004-12-23T14:56:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g8ms0hc7eahork2f468m4p1qp6nm05np1@4ax.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <32vfppF3pmhk0U1@individual.net>`

```
On Thu, 23 Dec 2004 22:00:38 +1300 "Pete Dashwood" <dashwood@enternet.co.nz>
wrote:

:>"TammyBain" <baint@cityofrochester.gov> wrote in message
:>news:781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com...
:>> I can't find any documentation on assign statements with
:>> -UT- in them.    Does the 'UT' stand for Unit Tape or Utility Tape?

:>The UT stands for "Utility". In the very olden days, before disks were
:>invented and freely available, this was tape. Later, replaced by disk
:>drives, these "utility" devices were available for any kind of storage
:>requirement. The UT was not about a physical device, it was about the
:>logical use of a physical device, i.e. as a "Utility".

More precisely it defined a device that could be "rewound" and reprocessed,
but could not be processed by block number.

UR defined a device that could not be re-processed.

DA added the ability to randomly access blocks.

In Ye Olde Days the DCB (file descriptor) for a device will less capability
used less memory.
```

###### ↳ ↳ ↳ Re: COBOL

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-12-23T21:40:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqfe1n$5cn$1@peabody.colorado.edu>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <32vfppF3pmhk0U1@individual.net> <8g8ms0hc7eahork2f468m4p1qp6nm05np1@4ax.com>`

```
I liked the first time I worked on a VAX, discovering that I could either put
the file name in the ASSIGN clause, or have it redirected by DCL.   The COBOL
didn't care what the file looked like anyway, that was the operating system's
business.

This was before PCs.
```

###### ↳ ↳ ↳ Re: COBOL

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-12-24T18:51:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<331p3pF3sfnklU1@individual.net>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <32vfppF3pmhk0U1@individual.net> <8g8ms0hc7eahork2f468m4p1qp6nm05np1@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com> wrote in message
news:8g8ms0hc7eahork2f468m4p1qp6nm05np1@4ax.com...
> On Thu, 23 Dec 2004 22:00:38 +1300 "Pete Dashwood"
<dashwood@enternet.co.nz>
> wrote:
>
> :>"TammyBain" <baint@cityofrochester.gov> wrote in message
>
:>news:781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com..
.
> :>> I can't find any documentation on assign statements with
> :>> -UT- in them.    Does the 'UT' stand for Unit Tape or Utility Tape?
…[7 more quoted lines elided]…
> More precisely it defined a device that could be "rewound" and
reprocessed,
> but could not be processed by block number.
>
Thanks for that, Binyamin. I never made that connection before. I remember
an engineer explaining the meaning of "utility" to me (I was always ahanging
round them trying to borrow manuals). I'm sure you're right. Where did you
come across this, or did you just recognise that that's how it is/was?

Pete.

> UR defined a device that could not be re-processed.
>
> DA added the ability to randomly access blocks.
>
> In Ye Olde Days the DCB (file descriptor) for a device will less
capability
> used less memory.
>
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL

_(reply depth: 4)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2004-12-24T09:23:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d6os0lfh1p5lao5s6it3kr81jso926med@4ax.com>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com> <32vfppF3pmhk0U1@individual.net> <8g8ms0hc7eahork2f468m4p1qp6nm05np1@4ax.com> <331p3pF3sfnklU1@individual.net>`

```
On Fri, 24 Dec 2004 18:51:48 +1300 "Pete Dashwood" <dashwood@enternet.co.nz>
wrote:

:>"Binyamin Dissen" <postingid@dissensoftware.com> wrote in message
:>news:8g8ms0hc7eahork2f468m4p1qp6nm05np1@4ax.com...
:>> On Thu, 23 Dec 2004 22:00:38 +1300 "Pete Dashwood"
:><dashwood@enternet.co.nz>
:>> wrote:

:>> :>"TammyBain" <baint@cityofrochester.gov> wrote in message

:>:>news:781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com..
:>.
:>> :>> I can't find any documentation on assign statements with
:>> :>> -UT- in them.    Does the 'UT' stand for Unit Tape or Utility Tape?

:>> :>The UT stands for "Utility". In the very olden days, before disks were
:>> :>invented and freely available, this was tape. Later, replaced by disk
:>> :>drives, these "utility" devices were available for any kind of storage
:>> :>requirement. The UT was not about a physical device, it was about the
:>> :>logical use of a physical device, i.e. as a "Utility".

:>> More precisely it defined a device that could be "rewound" and
:>reprocessed,
:>> but could not be processed by block number.

:>Thanks for that, Binyamin. I never made that connection before. I remember
:>an engineer explaining the meaning of "utility" to me (I was always ahanging
:>round them trying to borrow manuals). I'm sure you're right. Where did you
:>come across this, or did you just recognise that that's how it is/was?

Being mumble years old, I recognized it.

:>> UR defined a device that could not be re-processed.

:>> DA added the ability to randomly access blocks.

:>> In Ye Olde Days the DCB (file descriptor) for a device will less
:>capability
:>> used less memory.
```

#### ↳ Re: COBOL

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-12-23T14:26:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqekjp$av9$1@peabody.colorado.edu>`
- **References:** `<781a5bf97064111bb1fb057deb0cb1a0@localhost.talkaboutprogramming.com>`

```

On 22-Dec-2004, "TammyBain" <baint@cityofrochester.gov> wrote:

> I can't find any documentation on assign statements with
> -UT- in them.    Does the 'UT' stand for Unit Tape or Utility Tape?

Is this for historical interest?

Back in the days when this actually meant something, I used to keep clone of the
various assign statements I wanted to use, and then copied them in to the new
programs.   I'm glad that this is no longer necessary.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
