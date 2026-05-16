[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# os/vs cobol to cobol II for mvs

_5 messages · 4 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### os/vs cobol to cobol II for mvs

- **From:** "Larry Vervynckt" <lawrence.vervynckt@eds.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bde195$be772d20$b95efa90@kopc1157.delcoelect.com>`

```
I am interested in information regarding the conversion to cobol II. 
Hints, available guides, resources of any type.  We are in the beginnings
of a mass conversion and need some help from all of you gurus out there. 
Any help would be appreciated.
```

#### ↳ Re: os/vs cobol to cobol II for mvs

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tpem9$23q@dfw-ixnews10.ix.netcom.com>`
- **References:** `<01bde195$be772d20$b95efa90@kopc1157.delcoelect.com>`

```
Hint number 1
   Do not even THINK about converting to "COBOL II".  The product VS COBOL
II is quite old and has been superceded.  Although IBM will support it thru
2000, it is not the way to solve Y2K problems.  The compiler that you want
to look at (assuming your MVS or OS/390 - and not VSE) is
    IBM COBOL for OS/390 & VM
    (you could also use COBOL for MVS & VM - but that too is semi-old. If
you hear about COBOL/370 - support for that has already been dropped!)

Once you have figured out the compiler to go to, the first book that you
should read is IBM's "Migration Guide".  There are separate versions for VS
COBOL II, COBOL for MVS & VM, and COBOL for OS/390 & VM.  Get the one for
the compiler that you are moving to.  (If you are going to one of the COBOL
for this-and-that compilers, you will also want to get a copy of the LE
(Language Environment) "Migration Guides".

There are courses that you can take on utilizing the new products and/or
migrating from the old ones.  There are also courses on analyzing your own
shop's situation and how difficult the conversion will be.  Some of these
have already been discussed in this newsgroup.  I suggest you look at
DejaNews for some of the old threads.  If you need more hints, please let us
know.

Larry Vervynckt wrote in message
<01bde195$be772d20$b95efa90@kopc1157.delcoelect.com>...
>I am interested in information regarding the conversion to cobol II.
>Hints, available guides, resources of any type.  We are in the beginnings
>of a mass conversion and need some help from all of you gurus out there.
>Any help would be appreciated.
>
```

##### ↳ ↳ Re: os/vs cobol to cobol II for mvs

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980916201328.29931.00000323@ng86.aol.com>`
- **References:** `<6tpem9$23q@dfw-ixnews10.ix.netcom.com>`

```

The recommended Migration Guide is  indispensable.

Your conversion will take a lot of resources if  you have many programs. In the
vendor's documentation the least emphasized aspect of the switch-over is the
ending of support for non-standard IBM extensions to COBOL.

Beware of ODOs (occurs depending on clauses) in your time estimates, there are
surprises there. The need to change programs from EXAMINE to INSPECT can
require much work too, especially in testing.

As a previous responder has pointed out, you eventually need to be hussling
your puppies into COBOL 390 (again assuming this is not VSE).  But you could
face the problem that many shops do, you may not be ready to go to OS/390 until
later.

I am not sure that COBOL 390 will fly in MVS/ESA etc.

Beware that the LE/390 world is slightly different that the LE/370 world. 
LE/390 is required with COBOL 390.  LE/370 is optional.  I have been in
environments where features of LE/370 are turned on and off in MVS contexts
just to see how much code is still not ready for OS 390.

Your main concern now is to get to COBOL-85 syntax.  COBOL II, and other
compilers  prior to the COBOL 390 can get you there. The surprising list of
recent names and name changes for the mainframe COBOL compiler is confusing. 
Most of the names have the name of an operation system in it. 

Do not be misled by the product names.  You are NOT primarily involved in an
operating system change. Instead, you are involved in a major source code
syntax change (from the COBOL 74 standard to the COBOL 85 standard), and the
dropping of certain vendor extensions to the language.

Your issue is the source code.  Much of it needs attention.

It is best to start discussion early on about rebuilding entire systems, (as an
option), rather than tweaking parts and relinking.
IBM, an extremely talented group of people, has established ways to combine old
code and new code (code compiled under prior compilers, and code compiled under
newer compilers). 

This defintiely can allow delay in source code conversion.   But the new code /
old code mix links become rather more abstract than application programmers
might be used to.
Also note that certain strategies offered (like MIXRES) in intermediate COBOL
85 products have disappered in the later COBOL (for OS/390).

IBM definitely should be admired for what they have accomplished with the COBOL
technologies.  But the mix approach runs a real risk of generating a Tower of
Babel effect. It involves concepts and terminology alien to the application
technicians and managers.

This is an opinion, but you may be in the  best  position later on if you regen
entire applications from the source code out.

For some organizations, the conversion to the new syntax can be truely major.
Obviously, a divide and concur approach becomes necessary.  It is, perhaps,
best to divide way up at the application level, and do not mix old code and new
code in a single run unit.

Any divide strategy that stages portions of code into production over time does
run into the dificulty of having programs on either side of an interface (file
or online I/O area) compiled with different language standards.

Here you must distinguish syntax (COBOL 74/ versus COBOL 85) from semantics,
which is the menaing of code.

The BINary data items are one focal point here, and an enumeration of such
items in interfaces may be a portion of the estimate process.  Generally, you
are looking at TRUNC(BIN) for the new world.  The places  where this could
cause problems between old code and new code are usually rare, (this is because
the old code is already operating with a TRUNC(STD) domain of data.

None the less, program conversion may bring about changes that increase length,
the new code may be able to see it, the old code may not.

The list goes on.  It is a major undertaking if you have lots of programs. 
Many of the language changes involve details which will necessitate substantial
testing. Resources of a large order may be required from user groups.

Also note that the migration guide also describes hardware resource
implications.
The new world is much fatter than the old. But the resource hog is the
transition period, where many application components exist in duplicate.

Less emphasized in the COB(OL migration guide is the hardware resources needed
to support major system testing during the transition.  Data review can be
lengthy, and the need for reruns can slow things also.  The amount of DASD and
printer time to support the users during system verification, will require
major commitments.













Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: os/vs cobol to cobol II for mvs

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980919103614.11915.00001824@ng123.aol.com>`
- **References:** `<19980916201328.29931.00000323@ng86.aol.com>`

```

RKRayhawk writes ...

[snip it all]

Very nicely put, RK.

-Cheers

Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: os/vs cobol to cobol II for mvs

- **From:** "Larry Vervynckt" <lawrence.vervynckt@eds.com>
- **Date:** 1998-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bde301$266270e0$b95efa90@kopc1157.delcoelect.com>`
- **References:** `<01bde195$be772d20$b95efa90@kopc1157.delcoelect.com>`

```
I have received some good suggestions.  But I have also received emails
from companys offering their services for the conversion.  My team will be
making the conversion,  all I want is suggestions for making it go
smoothly(if possible).

thanks 

Larry Vervynckt <lawrence.vervynckt@eds.com> wrote in article
<01bde195$be772d20$b95efa90@kopc1157.delcoelect.com>...
> I am interested in information regarding the conversion to cobol II. 
> Hints, available guides, resources of any type.  We are in the beginnings
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
