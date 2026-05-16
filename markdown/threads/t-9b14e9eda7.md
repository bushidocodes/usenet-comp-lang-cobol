[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Utilities in Mainframe

_5 messages · 2 participants · 1999-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Utilities in Mainframe

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37134A78.3D372E5A@NOSPAMhome.com>`
- **References:** `<19990412222831.12527.00002187@ng-fa1.aol.com> <3712C5F5.2D79E6DF@worldnet.att.net>`

```
> I had to scratch my head over this.  In my shop we use H&W's SYSD editor
> instead of TSO/ISPF, and there's a screen that will give you the DCB
> info directly (RECFM, LRECL, BLKSIZE, et cetera).

We have SYSD & ISPF, but SYSD is going away as it is our only
application which uses CICS, and we can save lots of money by dropping
CICS.  (We're an IDMS shop).  Old timers all use SYSD, and only
outsiders had used TSO.  The big difference as far as I can see is that
they have to kludge to get the functionality of MODID to comment changes
in columns 3-80.
```

#### ↳ Re: Utilities in Mainframe

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371439DB.A8DB33D0@worldnet.att.net>`
- **References:** `<19990412222831.12527.00002187@ng-fa1.aol.com> <3712C5F5.2D79E6DF@worldnet.att.net> <37134A78.3D372E5A@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> > I had to scratch my head over this.  In my shop we use H&W's SYSD editor
…[8 more quoted lines elided]…
> in columns 3-80.

We *are* a CICS shop, more than 90 regions.  While I haven't used ISPF
as much as SYSD, I definitely like SYSD better.  Sadly, the sysprogs
have announced they're going to drop SYSD and force us to use ISPF,
which is a major step backwards in my opinion.  The story given out is
that SYSD is not Y2K-compliant, but that's just not true.  We've been
running SYSD in our Time Machine LPAR for over a year and it has no
problems whatsover.

I'm not familiar with MODID.  Is that an ISPF feature or a SYSD feature?
```

##### ↳ ↳ Re: Utilities in Mainframe

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3714979C.C93A27B9@NOSPAMhome.com>`
- **References:** `<19990412222831.12527.00002187@ng-fa1.aol.com> <3712C5F5.2D79E6DF@worldnet.att.net> <37134A78.3D372E5A@NOSPAMhome.com> <371439DB.A8DB33D0@worldnet.att.net>`

```
> We *are* a CICS shop, more than 90 regions.  While I haven't used ISPF
> as much as SYSD, I definitely like SYSD better.  Sadly, the sysprogs
…[6 more quoted lines elided]…
> I'm not familiar with MODID.  Is that an ISPF feature or a SYSD feature?

It's a SYSD feature, and not having it is the biggest complaint people
have about moving to TSO/ISPF/SPF/PDF/whatever.  The recommended way of
duplicating this feature in TSO is to change PF4 to c p'========'
'xxxxxxxx' 73 80 (where xxxxxx is the modid), and hiting F4 after
changing a line.   MODID (modifiy-id) is used to force documentation of
changed source in particular columns of the source code.

Actually, everything else people here want to do from SYSD is easy to do
in SPF.  Except that to get 8 full screen sessions, we have to re-map
our F2 to START and F9 to SWAP NEXT.  Since SPF stores the keymaps a
bunch of different places, this has to be changed a bunch of different
places as SWAP and SWAP NEXT together can get confusing.
```

###### ↳ ↳ ↳ SYSD versus ISPF

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37157DA9.BF345CB3@worldnet.att.net>`
- **References:** `<19990412222831.12527.00002187@ng-fa1.aol.com> <3712C5F5.2D79E6DF@worldnet.att.net> <37134A78.3D372E5A@NOSPAMhome.com> <371439DB.A8DB33D0@worldnet.att.net> <3714979C.C93A27B9@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
> > I'm not familiar with MODID.  Is that an ISPF feature or a SYSD feature?
…[6 more quoted lines elided]…
> changed source in particular columns of the source code.

Thanks for the explanation.  I may find it useful someday, but we let
Endevor handle version control, so this issue doesn't come up for us.

> 
> Actually, everything else people here want to do from SYSD is easy to do
…[3 more quoted lines elided]…
> places as SWAP and SWAP NEXT together can get confusing.

I will definitely save this tip.  My pet peeves over the differences
between SYSD and ISPF include the fact that SYSD allows '/' in the
prefix area (like XEDIT on VM/VMS) to position the current line, and
ISPF does not.  I detest the CSR option because my screen doesn't scroll
predictably, and always use PAGE instead.  This makes it less convenient
to reposition the current line.
  
I also got really attached to the XALL option in SYSD.  I think it's a
royal pain to have to type 'X ALL; F [string] ALL' to get the same
effect.  I begged for months to get the sysprogs to install the ISPF
'ONLY' macro, and it's supplied in a sample library by IBM!  And I'm not
sure if they will allow lowly 'apples' to write their own ISPF macros.

Maybe it's the our mainframe is tuned, but I find it to be much quicker
to edit COBOL source with SYSD in CICS than with TSO/ISPF.

Thanks again.
```

###### ↳ ↳ ↳ Re: SYSD versus ISPF

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3715F3A9.C13AF289@NOSPAMhome.com>`
- **References:** `<19990412222831.12527.00002187@ng-fa1.aol.com> <3712C5F5.2D79E6DF@worldnet.att.net> <37134A78.3D372E5A@NOSPAMhome.com> <371439DB.A8DB33D0@worldnet.att.net> <3714979C.C93A27B9@NOSPAMhome.com> <37157DA9.BF345CB3@worldnet.att.net>`

```
Arnold Trembley wrote:
> 
> Howard Brazee wrote:
…[11 more quoted lines elided]…
> Endevor handle version control, so this issue doesn't come up for us.

We use Endevor also, but it's nice when browsing code to look at the
maintenance code id listed in the change log of REMARKS, then find which
lines were changed by doing a find on that id (which MODID put in
columns 73-80).
 
> >
> > Actually, everything else people here want to do from SYSD is easy to do
…[10 more quoted lines elided]…
> to reposition the current line.

I used an editor which had that feature in an Amdahl operating system
called ASPEN, which never made it past beta.  I agree, that was better
than the CSR option.  But the CSR option always has scrolled predictably
for me - the trouble is that the cursor has to be on the line I want to
scroll to, where the slash didn't require this.
 
> I also got really attached to the XALL option in SYSD.  I think it's a
> royal pain to have to type 'X ALL; F [string] ALL' to get the same
> effect.  I begged for months to get the sysprogs to install the ISPF
> 'ONLY' macro, and it's supplied in a sample library by IBM!  And I'm not
> sure if they will allow lowly 'apples' to write their own ISPF macros.

I'm a fast typer and already learned the TSO.  The keyword ALL can be
before [string] if you like.  Someone wrote a macro to do XALL in tso,
but I don't bother with it.
 
> Maybe it's the our mainframe is tuned, but I find it to be much quicker
> to edit COBOL source with SYSD in CICS than with TSO/ISPF.
> 
> Thanks again.

But there are some commands which work better with the TSO editor.  It
works quickly to type M and press F8 instead of BOT.  I love being able
to type EDIT filename, VIEW filename, or BROWSE filename from within an
edit session.  I like the fact that I don't have to type SAVE before
exiting.  ZOOM & SHOWPROC have no equivalent.  I use 3.12 & 3.14
extensively.  The flip command is useful.  Bounds command is sometimes
necessary.  I used it the other day to add a space in column 12 of some
test data, using "))" to push everything from 12 on to the right.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
