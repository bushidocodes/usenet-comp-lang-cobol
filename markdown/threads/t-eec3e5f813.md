[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

_8 messages · 3 participants · 2009-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

- **From:** Mel_3 <myemaillist@gmail.com>
- **Date:** 2009-07-04T11:54:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<207e1839-3d68-41ab-8b79-2c97c4544414@j32g2000yqh.googlegroups.com>`

```
THE SITUATION:
- I'm trying to resurrect an old custom COBOL ap that ran on an old
DOS PC.
- The program used a DOS GUI App HI-SCREEN Pro II by PC Soft as the
interface to the Ao.,
- I'm having trouble getting HI-SCREEN Pro II to work...
- and want to search for the actual compiled COBOL file(s) to get the
darn'd thing to work.

But I'm not a COBOL programmer.

The QUESTION:
What file extension is used for a compiled Micro Focus COBOL program
that was running on an old DOS 6.2 PC ? Would I look for a .COM
or .EXE file type? or what?

Thanks for any help.
```

#### ↳ Re: What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-07-04T14:00:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33782f77-a97b-443b-95a8-c6e059616d31@v15g2000prn.googlegroups.com>`
- **References:** `<207e1839-3d68-41ab-8b79-2c97c4544414@j32g2000yqh.googlegroups.com>`

```
On Jul 5, 6:54 am, Mel_3 <myemaill...@gmail.com> wrote:
> THE SITUATION:
> - I'm trying to resurrect an old custom COBOL ap that ran on an old
> DOS PC.
> - The program used a DOS GUI App HI-SCREEN Pro II by PC Soft as the
> interface to the Ao.,

I used that (well I played with it) and have a copy here.

> - I'm having trouble getting HI-SCREEN Pro II to work...
> - and want to search for the actual compiled COBOL file(s) to get the
…[7 more quoted lines elided]…
> or .EXE file type? or what?

Most binary executables are .EXE but the compiler can output .INT
'intermediate' code which is a byte code that is executed by the run-
time or .GNT which is 'generated' and has much machine code in it.
These are equivalent to Java byte code and the output from a Java JIT
respectively.

Or the .int and/or .gnt can be linked and encapsulated into a .EXE
which is what I usually did.
```

##### ↳ ↳ Re: What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

- **From:** Mel_3 <myemaillist@gmail.com>
- **Date:** 2009-07-04T14:22:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c1b91c64-ed22-4dad-b189-99ffc920936b@q11g2000yqi.googlegroups.com>`
- **References:** `<207e1839-3d68-41ab-8b79-2c97c4544414@j32g2000yqh.googlegroups.com> <33782f77-a97b-443b-95a8-c6e059616d31@v15g2000prn.googlegroups.com>`

```
Ah Ha... you have a copy of HI-Screen Pro II ???

Maybe you can answer a question then... here is the last part of the
DOS 6.2 Batch file that should launch the old COBOL app...

hs-beg
DISPLAY
CLS
RUN MSTRMENU
hs-end

I is how I think this works...

hs-beg init's HI=Screen Pro II which is a DOS GUI (I think)

DISPLAY runs display.com in the HSPRO2 dir & in my case it displays HI-
Screen Pro & the copyright holder PC Soft

RUN MSTRMENU should, I think, run the HI-Screen Pro II file
MstrMenu.MNU which I think is the menu for this app as compiled by HI-
Screen PRO II... but I get this error message...

"Cannot find application SHELL"

But, I'm stumped... and may have all of this wrong... that is why I
was trying to bypass HI=Screen Pro II and just attempt to run the
COBOL files directly...

but if you know anything about Hi-Screen Pro II... please let me
know... I need a little help on this.

Thanks
```

###### ↳ ↳ ↳ Re: What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-07-05T01:39:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f837b4af-57b2-41c7-b978-4c807bca11d0@o18g2000pra.googlegroups.com>`
- **References:** `<207e1839-3d68-41ab-8b79-2c97c4544414@j32g2000yqh.googlegroups.com> <33782f77-a97b-443b-95a8-c6e059616d31@v15g2000prn.googlegroups.com> <c1b91c64-ed22-4dad-b189-99ffc920936b@q11g2000yqi.googlegroups.com>`

```
On Jul 5, 9:22 am, Mel_3 <myemaill...@gmail.com> wrote:
> Ah Ha... you have a copy of HI-Screen Pro II ???

I played with it, mostly the Windows version, in 1993 or so. The
machine that was on died in 2001. Its replacement does still have some
files recovered from the dead one, but not the DOS HS programs that I
played with.

> Maybe you can answer a question then... here is the last part of the
> DOS 6.2 Batch file that should launch the old COBOL app...
…[12 more quoted lines elided]…
> Screen Pro & the copyright holder PC Soft

DISPLAY.COM loads as a TSR

The hs_beg or hs_end would be .COM files that set up and tear down the
TSR environment.

RUN is the Cobol runtime environment. I would have expected MSTRMENU
to be a .INT or a .GNT file and the .MNU to be a data file perhaps or
perhaps a HS screen definition file.

>
> RUN MSTRMENU should, I think, run the HI-Screen Pro II file
…[3 more quoted lines elided]…
> "Cannot find application SHELL"

> But, I'm stumped... and may have all of this wrong... that is why I
> was trying to bypass HI=Screen Pro II and just attempt to run the
…[3 more quoted lines elided]…
> know... I need a little help on this.

Do you not have manuals ?

Are you running this on a real MS-DOS or similar. Note that NT/XP/
Vista console is not MS-DOS and probably won't run the DISPLAY.COM
TSR.
```

###### ↳ ↳ ↳ Re: What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

_(reply depth: 4)_

- **From:** Mel_3 <myemaillist@gmail.com>
- **Date:** 2009-07-05T06:39:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e64ec78f-eea7-42a7-b5c3-3cae021b076b@p29g2000yqh.googlegroups.com>`
- **References:** `<207e1839-3d68-41ab-8b79-2c97c4544414@j32g2000yqh.googlegroups.com> <33782f77-a97b-443b-95a8-c6e059616d31@v15g2000prn.googlegroups.com> <c1b91c64-ed22-4dad-b189-99ffc920936b@q11g2000yqi.googlegroups.com> <f837b4af-57b2-41c7-b978-4c807bca11d0@o18g2000pra.googlegroups.com>`

```
Thanks for the great help !

I have these MstrMenu.xxx files in the folder...

MstrMenu.BAT
MstrMenu.CBL
MstrMenu.GNT
MstrMenu.IDY
MstrMenu.INT

To review... the last few lines of MstrMenu.BAT are...

hs-beg
DISPLAY
CLS
RUN MSTRMENU
hs-end

- I "guess" it is working OK until it attempts to execute the line RUN
MSTRMENU
- Then I get this ERROR... "Cannot find application SHELL"

Do you know what this error message means?

FYI I think hs-beg and Display.com are executing correctly because...
..Once MstrMenu.bat aborts with the error message
..I manually type Display at the DOS prompt
..I get prompted that Display is already loaded...
..so I'm guessing the TSR environment got setup OK
.. and Display.com got installed as it should... right?

I'm running a DOS 6.2 as a Virtual Machine - on an Windows XP machine
- under Sun Micro's VirtualBox
And DOS seems to be working fine as a virtual machine... I've ran a
number of other app's no problem.
Hopefully I can get this one to work as well.

No manuals at all. This was a custom Ap and the developer can not be
found.

Thanks again for your kind assistance on this.
```

###### ↳ ↳ ↳ Re: What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

_(reply depth: 5)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-07-05T12:52:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<827b23a7-49e1-426b-92d0-ec763d0c87a8@d7g2000prl.googlegroups.com>`
- **References:** `<207e1839-3d68-41ab-8b79-2c97c4544414@j32g2000yqh.googlegroups.com> <33782f77-a97b-443b-95a8-c6e059616d31@v15g2000prn.googlegroups.com> <c1b91c64-ed22-4dad-b189-99ffc920936b@q11g2000yqi.googlegroups.com> <f837b4af-57b2-41c7-b978-4c807bca11d0@o18g2000pra.googlegroups.com> <e64ec78f-eea7-42a7-b5c3-3cae021b076b@p29g2000yqh.googlegroups.com>`

```
On Jul 6, 1:39 am, Mel_3 <myemaill...@gmail.com> wrote:
> Thanks for the great help !
>
…[6 more quoted lines elided]…
> MstrMenu.INT

.CBL is the Cobol source file.  .INT is the byte coded compiler
output. .IDY is the debug references. .GNT is the generated program
(ie JIT compiled). It is the .GNT that will be run.


> To review... the last few lines of MstrMenu.BAT are...
>
…[10 more quoted lines elided]…
> Do you know what this error message means?

I don't have your version of MS Cobol but it looks like a message from
Cobol because it can't find the run-time libraries. These would be
similar to COBENV.DLE and should be on the COBLIB= environment.

> FYI I think hs-beg and Display.com are executing correctly because...
> ..Once MstrMenu.bat aborts with the error message
…[3 more quoted lines elided]…
> .. and Display.com got installed as it should... right?

After running hs-end the DISPLAY.COM TSR should _no_longer_ be
loaded.  'begin' puts a marker in memory, 'end' restores the free
memory back to that marker and resets the interrupt vectors.


> I'm running a DOS 6.2 as a Virtual Machine - on an Windows XP machine
> - under Sun Micro's VirtualBox
> And DOS seems to be working fine as a virtual machine... I've ran a
> number of other app's no problem.
> Hopefully I can get this one to work as well.


> No manuals at all. This was a custom Ap and the developer can not be
> found.
>
> Thanks again for your kind assistance on this.
```

###### ↳ ↳ ↳ Re: What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

_(reply depth: 6)_

- **From:** Mel_3 <myemaillist@gmail.com>
- **Date:** 2009-07-06T06:49:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1a41e50-4283-4d22-a964-449133a22516@d9g2000prh.googlegroups.com>`
- **References:** `<207e1839-3d68-41ab-8b79-2c97c4544414@j32g2000yqh.googlegroups.com> <33782f77-a97b-443b-95a8-c6e059616d31@v15g2000prn.googlegroups.com> <c1b91c64-ed22-4dad-b189-99ffc920936b@q11g2000yqi.googlegroups.com> <f837b4af-57b2-41c7-b978-4c807bca11d0@o18g2000pra.googlegroups.com> <e64ec78f-eea7-42a7-b5c3-3cae021b076b@p29g2000yqh.googlegroups.com> <827b23a7-49e1-426b-92d0-ec763d0c87a8@d7g2000prl.googlegroups.com>`

```
Got it working!
Somehow when files were copied... file names that contained a dash
changed to an under bar so...

my-file.abc became my_file.abc

But in the batch files that setup and launch the system... the dash
remained in the file name...

So nothing worked.

One of your comments led me to very carefully review the batch
files... and find each file they referenced... including the files
referenced with the SET command... finally, just like finding a syntax
error when debugging code... I saw it and the light went off... I
fixed all the file names and da da... the darn thing worked.

Now I have DOS 6.2 running as a virtual machine on a Windows XP box
using Sun's VirtualBox application... and I have the very old Micro
Focus COBOL application up and running... just like it was on the old
486 PC... only now it is on modern hardware... very cool indeed !

Thanks again for all the fine help!

Best.

Mel_3
```

###### ↳ ↳ ↳ Re: What is executable file ext for Micro Focus COBOL/2 Ver 1.2.29 L2.2 rev 003 on old DOS PC ?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-06T14:49:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h2t2u1$5t9$1@reader1.panix.com>`
- **References:** `<207e1839-3d68-41ab-8b79-2c97c4544414@j32g2000yqh.googlegroups.com> <e64ec78f-eea7-42a7-b5c3-3cae021b076b@p29g2000yqh.googlegroups.com> <827b23a7-49e1-426b-92d0-ec763d0c87a8@d7g2000prl.googlegroups.com> <a1a41e50-4283-4d22-a964-449133a22516@d9g2000prh.googlegroups.com>`

```
In article <a1a41e50-4283-4d22-a964-449133a22516@d9g2000prh.googlegroups.com>,
Mel_3  <myemaillist@gmail.com> wrote:

[snip]

>One of your comments led me to very carefully review the batch
>files... and find each file they referenced... including the files
>referenced with the SET command... finally, just like finding a syntax
>error when debugging code... I saw it and the light went off... I
>fixed all the file names and da da... the darn thing worked.

Congratulations on your situation... whether it was your own find or The 
Muse descending upon you it is one of the things that makes coding the 
most fun I've had making a buck yet.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
