[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL "reserved columns" (was: Philosophical question

_7 messages · 6 participants · 2000-09_

---

### Re: COBOL "reserved columns" (was: Philosophical question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-05T21:08:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p48sj$jdc$1@slb6.atl.mindspring.net>`
- **References:** `<NBBBJPGEPBMHMOJGKPFFEENAEDAA.wmklein@ix.netcom.com>`

```
I am NOT quoting myself - but thought that comp.lang.cobol might be
interested in this post that I sent to IBM-MAIN.
```

#### ↳ Re: COBOL "reserved columns" (was: Philosophical question

- **From:** Charles Hammond <ceh1@cec.wustl.edu>
- **Date:** 2000-09-07T09:34:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000907093216.10279A-100000@hilton.cec.wustl.edu>`
- **In-Reply-To:** `<8p48sj$jdc$1@slb6.atl.mindspring.net>`
- **References:** `<NBBBJPGEPBMHMOJGKPFFEENAEDAA.wmklein@ix.netcom.com> <8p48sj$jdc$1@slb6.atl.mindspring.net>`

```
If you have no numbering system for the lines how do you know where the
error is?  will the error messages be immedately after the line in
question forcing you to hunt for them or is there a hidden line index?
like the index on a sequential file?

Charles Hammond, BSIM Undergraduate Program
```

##### ↳ ↳ Re: COBOL "reserved columns" (was: Philosophical question

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-07T09:31:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39B7B4DE.443D9F63@brazee.net>`
- **References:** `<NBBBJPGEPBMHMOJGKPFFEENAEDAA.wmklein@ix.netcom.com> <8p48sj$jdc$1@slb6.atl.mindspring.net> <Pine.SOL.3.96.1000907093216.10279A-100000@hilton.cec.wustl.edu>`

```


Charles Hammond wrote:

> If you have no numbering system for the lines how do you know where the
> error is?  will the error messages be immedately after the line in
…[3 more quoted lines elided]…
> Charles Hammond, BSIM Undergraduate Program

Mainframe listings still have line numbers when your source code doesn't.
But it is a pain searching for the same line in your source code if it
doesn't have a sequence number as a cross reference.  Maybe PCs could have
some type of hypertext cross reference, moving you to the source code
error.  I would like that, but I have several copy libraries, including
IDMS COPY from the data dictionary which is put in during the pre-compiler
stage.  I don't see compiler software knowing how to get to the IDD.
```

###### ↳ ↳ ↳ Re: COBOL "reserved columns" (was: Philosophical question

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-09-08T02:13:30+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39B7BEAA.4705451A@melbpc.org.au>`
- **References:** `<NBBBJPGEPBMHMOJGKPFFEENAEDAA.wmklein@ix.netcom.com> <8p48sj$jdc$1@slb6.atl.mindspring.net> <Pine.SOL.3.96.1000907093216.10279A-100000@hilton.cec.wustl.edu> <39B7B4DE.443D9F63@brazee.net>`

```
Typically on PC or Unix the development environmetns are set up so that when
you click on the error message it takes you to the source line in question.
The source line number is just the physical sequence number in the file
starting from 1. This also works for included files (like COBOL copy
libraries). You can also go to an arbitrary label with a couple of keystrokes,

Tim Josling

Tim Josling

Howard Brazee wrote:

> Mainframe listings still have line numbers when your source code doesn't.
> But it is a pain searching for the same line in your source code if it
…[4 more quoted lines elided]…
> stage.  I don't see compiler software knowing how to get to the IDD.
```

###### ↳ ↳ ↳ Re: COBOL "reserved columns" (was: Philosophical question

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-09-07T16:34:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39B7C361.D7408F8@home.com>`
- **References:** `<NBBBJPGEPBMHMOJGKPFFEENAEDAA.wmklein@ix.netcom.com> <8p48sj$jdc$1@slb6.atl.mindspring.net> <Pine.SOL.3.96.1000907093216.10279A-100000@hilton.cec.wustl.edu> <39B7B4DE.443D9F63@brazee.net>`

```


Howard Brazee wrote:
> 
> Charles Hammond wrote:
…[14 more quoted lines elided]…
> stage.  I don't see compiler software knowing how to get to the IDD.

I don't know for sure, but I'm guessing Fujitsu is very similar to
NetExpress. Without line numbers being used the compiler does do a
source line count, (but that's really only info). All errors are listed
in a separate window at the bottom of the screen. You click the
appropriate error message and the top window (source) displays the line
marked with a red 'X" in left margin. Alternatively you can page-down
through the source looking for lines marked as errors.

When it comes to copy files, they are treated in sequence as part of
your source.

It really is an excellent feature in the IDE.

Jimmy
```

#### ↳ Re: COBOL "reserved columns" (was: Philosophical question

- **From:** Steve Thompson <sthompson2_@neo.rr.com>
- **Date:** 2000-09-07T22:43:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39B81A17.EAC307FE@neo.rr.com>`
- **References:** `<NBBBJPGEPBMHMOJGKPFFEENAEDAA.wmklein@ix.netcom.com> <8p48sj$jdc$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> I am NOT quoting myself - but thought that comp.lang.cobol might be
…[19 more quoted lines elided]…
> > functionally "compatible" - but not the same syntax)
<snip>

How about some thoughts on this for a bit?  If there are no
sequence numbers in the code, then how does one merge fixes into
the code?

Example:  IBM supplies CPCS (Check Processing Control System) in
source (could be any source maintained product by any vendor). 
When they send out fixes, it is based on the sequence numbers of
the **ORIGINALLY SUPPLIED SOURCE** (not yelling, but trying to
put in emphasis).  Now, going with the new COBOL standards, if we
decide to go to variable length lines, how can we provide
maintenance to our clients?

Mind you, the clients have been doing their own modifications to
the code on the basis of the sequence numbering.  

(Forgive me if this is plainly obvious to most) -- So, here you
are with a product from some vendor, where you are allowed to
make your own modifications.  You do your mods by using a utility
to merge your changes into the base code from the vendor.  The
vendor now sends out a new update.  So, you merge their "deck"
with the original, and then your mod "deck" with the result. 
Immediately prior to this, you ran a check to see if there were
any collisions between your respective changes.

With the new standard, the above will not be possible, if the
COBOL compiler now does not recognize that the first 6 columns
are not actually source.

Am I the only one that sees a problem with this picture?
```

##### ↳ ↳ Re: COBOL "reserved columns" (was: Philosophical question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-07T19:40:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8p9ci5$jep$1@slb3.atl.mindspring.net>`
- **References:** `<NBBBJPGEPBMHMOJGKPFFEENAEDAA.wmklein@ix.netcom.com> <8p48sj$jdc$1@slb6.atl.mindspring.net> <39B81A17.EAC307FE@neo.rr.com>`

```
This is NOT a problem that I think the committee has ever addressed.  I will
say that CURRENTLY the Standard (and IBM COBOLs) do not require you to put
sequence numbers in 1-6, it allows them.  This will be a continued option for
fixed format in the future.

In addition, any "free form" (variable length) line may END with "in-line
comments".  These COULD include sequence numbers or any other "identifier"
that you want.

If this doesn't convince you, then you might want to send your original note
to the J4 chair at
  doncobol <at> mediaone.net

I think this is a "new" issue, so it might be worthwhile for J4 to think
about it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
