[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# read disk using mf cobol by \\\\.\\physicaldrivex

_14 messages · 5 participants · 2010-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** Ronald Draper <ronald.draper@gmail.com>
- **Date:** 2010-02-22T14:55:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com>`

```
I want to access an unmountable drive using mf cobol and the physical
drive path.  It seems like I should be able to treat the disk as a
single relative record file.  Is this doable or just a pipe dream for
some other language?
Thanks
Ron
```

#### ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-02-22T16:07:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf4cddcb-4baa-4d56-bbf0-d6e493ef5b4c@o16g2000prh.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com>`

```
On Feb 23, 11:55 am, Ronald Draper <ronald.dra...@gmail.com> wrote:
> I want to access an unmountable drive using mf cobol and the physical
> drive path.  It seems like I should be able to treat the disk as a
> single relative record file.  Is this doable or just a pipe dream for
> some other language?

You certainly will not be able to do it as a relative file.

Fixed length relative files may be implemented as fixed size records
but these have a record terminator that indicates whether the record
is valid or deleted.

Variable length relative files (if possible) may be implemented by
having record headers.

Neither of these are useful for looking at disk level sectors.

You are more likely to be able to access the disk by booting into a
Linux Live CD, especially one that is designed for the purpose, such
as SystemRescueCD

http://www.sysresccd.org/Main_Page
```

#### ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-22T17:17:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y7Fgn.3146$BD2.2620@newsfe14.iad>`
- **In-Reply-To:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com>`

```
Ronald Draper wrote:
> I want to access an unmountable drive using mf cobol and the physical
> drive path.  It seems like I should be able to treat the disk as a
…[3 more quoted lines elided]…
> Ron

Much too generalized a question for you to anticipate getting helpful 
answers. If I had written, "I use mf and can I do this with a DB ?". 
What is your answer ?

So which version of M/F for appropriate compiler, hardware configuration 
and does that unmountable have a 'driver' that the OS recognizes. It 
*may* just be possible - I really don't know. One factor is you should 
look at hard copy or on-line manuals from M/F. Search on the word 
'Limitations', covering various topics which include access to disks, 
i.e. max disk sizes. You might be screwed before you start.

Jimmy, Calgary AB
```

#### ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2010-02-22T16:53:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ab82f0b0-cb6b-409e-84aa-2b9e899779ea@k36g2000prb.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com>`

```
On Feb 23, 6:55 am, Ronald Draper <ronald.dra...@gmail.com> wrote:
> I want to access an unmountable drive using mf cobol and the physical
> drive path.  It seems like I should be able to treat the disk as a
…[3 more quoted lines elided]…
> Ron

You could always do it, IF you are asking about the physical drive
path. Code below;

    SELECT theFile ASSIGN TO theDrive

               :
               :

    MOVE spaces TO theDrive
    STRING "\\theDrive\physicaldrivex" delimited by size
           "\myFile.DAT" delimited by size
      INTO theDrive

    OPEN INPUT theFile

You could always manipulate the drive path using your own style
(variables). What I'm guessing is that you are using the usual Cobol
data structures. You could also change the path size into an IP
address (ie. \\192.168.1.20\physicaldrivex ).
```

##### ↳ ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2010-02-22T17:14:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ebab65df-02a2-404c-a331-d504022859d0@s36g2000prf.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com> <ab82f0b0-cb6b-409e-84aa-2b9e899779ea@k36g2000prb.googlegroups.com>`

```
Take note however, that SOME devices if it is attached externally
(mobile) are basically opened as a 'read-only' devices... so you would
not able to do some WRITE/REWRITE or OPEN I-O.

Always look at your user privileges on such (mobile) devices before
doing some processing, or else it will fail.
```

#### ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** Ronald Draper <ronald.draper@gmail.com>
- **Date:** 2010-02-22T18:07:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a8242a8-5639-4554-849f-865a5d276618@e19g2000prn.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com>`

```
On Feb 22, 4:55 pm, Ronald Draper <ronald.dra...@gmail.com> wrote:
> I want to access an unmountable drive using mfcoboland thephysical
> drive path.  It seems like I should be able to treat the disk as a
…[3 more quoted lines elided]…
> Ron
I have searched all the resources I can find including m$ and I find
many mixed ways to define the path including a new one here.

I have tried just a drive letter "I:", "\\.\physicaldisk2", "\\?
\physicaldisk2", "\\.\physicaldisk2\I:", "\\.\I:".

I have yet to find a c or c++ example but I will continue searching.

I am sure there are limits as to what Cobol can do especially with
this being a 250 gb drive and the compiler I have has a 4 gb limit on
file size.  I have done thing like this on older computers (not
windooze) since the sectors were 512 bytes - if I wanted sector 255 I
used a relative key of 256 with no problems but that as I said has
been a while ago on and using a another compiler brand.

Ron
```

#### ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-02-22T19:42:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29597804-0660-4888-ba5e-19521b5c2adf@s36g2000prf.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com>`

```
On Feb 23, 11:55 am, Ronald Draper <ronald.dra...@gmail.com> wrote:
> I want to access an unmountable drive using mf cobol and the physical
> drive path.  It seems like I should be able to treat the disk as a
> single relative record file.  Is this doable or just a pipe dream for
> some other language?
>

What makes it "unmountable" ?
```

##### ↳ ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** Ronald Draper <ronald.draper@gmail.com>
- **Date:** 2010-02-23T10:53:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b0e2e4af-ba6d-4be8-bec3-db55b3d98f25@k2g2000pro.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com> <29597804-0660-4888-ba5e-19521b5c2adf@s36g2000prf.googlegroups.com>`

```
On Feb 22, 9:42 pm, Richard <rip...@Azonic.co.nz> wrote:
> On Feb 23, 11:55 am, Ronald Draper <ronald.dra...@gmail.com> wrote:
>
…[5 more quoted lines elided]…
> What makes it "unmountable" ?

With out starting a "war", a "windooze" crash has left it in a screwed
up state that will require reformating to resolve the problem.  The
"windooze" utilities fail and like all of Mr. Gates junk, fails to
provide any meaninful info other than the file or directory is bad and
will not mount it.

There is a lot of "recovery" software out there and some of it is
almost useful.  I have tried several "demo" programs and all run for
hours and then then fail without a message - the programs just
disappear which tells me that there may be a real problem with the
disk but there is still no excuse for their programs just
disappearing.  I would not recommend any of their programs to even a
hard core recovery service let alone a novice user.

So I thought why not create a really solid search and recovery program
that is built on a solid foundation and is generally more portable
than even a "c" program.
There is nothing I really need from the disk but I will keep it and
use it as the source for my "new" tool.

I have have found a "c" program to do low level io and I will rewrite
it in Cobol to experiment with but I still would rather have a total
Cobol program without calling a system service.  I have used Cobol for
over 30 years to do everything I needed without resorting to assembler
and they all allowed you access to a device.  I will post a message on
the MF forum and see what show up there.

Ron
```

###### ↳ ↳ ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-02-23T12:23:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4e2a1f4-a0a4-492a-9e8a-6fa7c5678b8c@t17g2000prg.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com> <29597804-0660-4888-ba5e-19521b5c2adf@s36g2000prf.googlegroups.com> <b0e2e4af-ba6d-4be8-bec3-db55b3d98f25@k2g2000pro.googlegroups.com>`

```
On Feb 24, 7:53 am, Ronald Draper <ronald.dra...@gmail.com> wrote:
> On Feb 22, 9:42 pm, Richard <rip...@Azonic.co.nz> wrote:
>
…[13 more quoted lines elided]…
> will not mount it.

The best advice that I can give is to _NOT_ run any Windows recovery
programs at all (probably too late) and certainly do not get Windows
to scandisk if it has failing sectors, that will completely bork the
disk.

Use SystemRescueCD which can actually do a better job of accessing a
broken VFAT or NTFS drive and is designed to recover data from the
disk and not to try to 'fix' it.

The other advantage of SystemRescueCD is that it boots from CD so it
can be used if the system won't boot off the disk. That at least
allows recovering files that are readable to USB or network.

> There is a lot of "recovery" software out there and some of it is
> almost useful.  I have tried several "demo" programs and all run for
…[8 more quoted lines elided]…
> than even a "c" program.

I do not know why you think that it would be 'more portable' than a C
program, or why this is necessary or even desirable. To access the raw
drive will require tricks that are OS dependent. You will be working
with VFAT or NTFS partitions (if you can actually find out how they
work), there is no point in having this run on an IBM mainframe or an
iPhone.

And MF COBOL is probably not the most useful for this type of job. It
requires run-times an who will pay for that ?

Maybe if you used OpenCOBOL it would at least be freely usable.


> There is nothing I really need from the disk but I will keep it and
> use it as the source for my "new" tool.
…[6 more quoted lines elided]…
> the MF forum and see what show up there.

You certainly cannot use a MF relative file for this. I doubt that you
would be able to open a physical disk as a file in MF COBOL.

I have done stuff on a raw drive many years ago on MS-DOS (actually DR-
DOS) with C. Zortech C provided functions to do this so it was easy. I
was just cloning the drive and not trying to figure out the structure
or deal with bad sectors and corrupt clusters.
```

###### ↳ ↳ ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-24T11:42:17+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7uj3ubF2t6U1@mid.individual.net>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com> <29597804-0660-4888-ba5e-19521b5c2adf@s36g2000prf.googlegroups.com> <b0e2e4af-ba6d-4be8-bec3-db55b3d98f25@k2g2000pro.googlegroups.com> <d4e2a1f4-a0a4-492a-9e8a-6fa7c5678b8c@t17g2000prg.googlegroups.com>`

```
Richard wrote:
> On Feb 24, 7:53 am, Ronald Draper <ronald.dra...@gmail.com> wrote:
>> On Feb 22, 9:42 pm, Richard <rip...@Azonic.co.nz> wrote:
…[70 more quoted lines elided]…
> structure or deal with bad sectors and corrupt clusters.

I think this is very sound advice. :-)

Certainly writing your utility in Open COBOL (you're intending to call C 
routines for the "hard stuff" anyway) makes sound sense, and is a perfect 
chance to use Open COBOL for something useful.

Fujitsu COBOL has no runtime fees and it does offer byte streamed IO 
(assuming you can read the sectors), but I agree with Richard here that you 
might as well right the whole thing in C or use Open COBOL (which generates 
C anyway) if you really want a COBOL wrapper round it.

Pete.
```

###### ↳ ↳ ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2010-02-23T20:48:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Mj1hn.32648$K81.3371@newsfe18.iad>`
- **In-Reply-To:** `<b0e2e4af-ba6d-4be8-bec3-db55b3d98f25@k2g2000pro.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com> <29597804-0660-4888-ba5e-19521b5c2adf@s36g2000prf.googlegroups.com> <b0e2e4af-ba6d-4be8-bec3-db55b3d98f25@k2g2000pro.googlegroups.com>`

```
Ronald Draper wrote:

> There is a lot of "recovery" software out there and some of it is
> almost useful.  I have tried several "demo" programs and all run for
…[16 more quoted lines elided]…
> and they all allowed you access to a device.  

I can understand where you are coming from and sympathize. I hold the
same view. I put a lot of sweat into getting a handle on OO COBOL with
Net Express and I am loathe to drop that experience for the newer stuff,
specifically .Net. And frankly, being 80 in September 2011, if I
make it, I don't need the challenge of switching. A former M/F employee,
(got lost in one phase of M/F's "rationalizations", wrote to me ten
years ago, 'Any COBOL compiler that claims to be OO will not succeed
without supporting classes". I couldn't agree more. But M/F OO DOES have
those supporting classes, (utilities). I haven't had the need to write a
single line in Java or any of the 'C' family.

Your correspondents wrote based on their personal experiences. Richard
has been at it for some decades and writes in numerous languages or
scripts as he sees fit to arrive at a solution. I don't recall he ever
gave OO any blessing; he does very nicely and successfully with his
approach.

Pete uses Fujitsu but his emphasis has been on 'components'; if that
represents a new term to you, think of, as an example, very small
sub-routines being called, (Invoked in OO parlance). Yes he did things
in Fujitsu but his main emphasis is .Net and components. He came to
realize that Fujitsu OO was lacking. It doesn't have the rich set of
support classes that Net Express has, nor those available via .Net.

Neither of the above approaches is wrong, neither is yours nor mine.

I will post a message on
> the MF forum and see what show up there.

Back to your compiler. You might just be lucky but I'm thinking you
could be SOL depending upon how up-to-date you are and any money
required from M/F.

The following message was posted in the M/F Forum, (primarily covers
their 'Express' compilers :-

----------------------------------------------------------------
Topic:	 Where are you MF-guys (dolls)? (1 of 2), Read 28 times
Conf:	 Net Express (NetX)
From:	 Lars Aune
Date:	 Sunday, February 07, 2010 11:23 PM
More than 50% of the posts are unanswered on the 1st page. We wish you
to participate more actively. In other words - we miss you.
-------------------------------------------------------------------

Dated February 7th above as you can see. Not a response to date. And the
reason, did some digging. Extract from M/F's blurb on N/E V 5.1 :-

You need to go here for full version :-

http://www.microfocus.com/000/DS-Upgrading-to-NET-Express-v4_tcm21-28067.pdf

Now that really explains it, and introduction to the newly coined
marketing word "sundown". Quick extract, but not the full piece :-

------------------------------------------------------------------------------
As announced in June 2008 with the release of the v5.1 product family,
Net Express v5.0 and the related COBOL Server products enter the
ï¿½sundownï¿½ state at the end in July 2009 and then ï¿½end of serviceï¿½ in
July 2010. All versions prior to v5.0 have already reached end of
service. (** this 'sundown'; excuse me please, when did you tell us
N/E V 3.1 users ? ***).

Products in the end of service state are subject to limited support
services and restrictions on new corrective fixes and it is recommended
that all users upgrade to the latest version. (*** Sure and pay you
lotsa, lotsa, more money **** I know of somebody in the States being
asked to pay $120,000 for the file handling facilities. He has taken
some 2 million lines of COBOL code and re-written it in Basic ***).

For users of Net Express, perhaps the most important new feature of v5.1
is that it is fully supported and no sundown or end of service date has
been published. It will be fully supported for at least 12 months (i.e.
at least until July 2010) and regular maintenance releases are planned
going beyond that date. Where Micro Focus COBOL products and
applications built using them are in everyday use, this commitment
provides the reassurance users need that their systems will continue to
be supported by the award-winning, 24x7 support provided by Micro Focus.
At least 12 months notice will be provided before the sundown or end of
service.
---------------------------------------------------------------------------------

They have most certainly pulled the plug on us N/E V 3.1 users, and for
starters they aren't making new money out of us - hence the
non-response to the 'Guys and Dolls' Message. Yes M/F are solely in the
software business, not hardware, and yes it's problematic supporting old
stuff, because with staff changes you may well lose those with the
experience of the various old versions. Also, from their point of view
they are not a charity. They need to encourage people to upgrade to make
more money. It would have been nice though, within the Forum being used
if ages ago they had posted a 'Sundown' message to forewarn. They
didn't. (There has to be a term for it in politics - "Don't defend. 
Don't Agree. Don't say anything and the problem will just go away").

So subject to what you are using you might get lucky with a response for
your particular compiler; but you might score a zero.

Jimmy, Calgary AB.
```

###### ↳ ↳ ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

_(reply depth: 4)_

- **From:** Ronald Draper <ronald.draper@gmail.com>
- **Date:** 2010-02-23T21:42:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<56928020-dfc6-42ad-bda5-ac75830a97b9@k5g2000pra.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com> <29597804-0660-4888-ba5e-19521b5c2adf@s36g2000prf.googlegroups.com> <b0e2e4af-ba6d-4be8-bec3-db55b3d98f25@k2g2000pro.googlegroups.com> <Mj1hn.32648$K81.3371@newsfe18.iad>`

```
On Feb 23, 9:48 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
> Ronald Draper wrote:
> > There is a lot of "recovery" software out there and some of it is
…[119 more quoted lines elided]…
> - Show quoted text -

I will use the MF cobol to "update" my 15 year old VMS disk dumper
program.  I have pondered the open cobol and except for its lack of
debugging interactively it looks like the compiler I will use to get
this program into the peoples hands.

But the question remains, how to access an unmounted disk and it could
and should be treated like a tape (I do not actually need the random
access just yet) so sequential reads are fine like I said at the
moment.

If MF chooses not to respond, that is okay too.  There are a lot of
companies that can not afford to maintain the older products and they
tend to fade into the sunset with their products as well.

I guess from looking at the c code, that I need is an example of
coding the "createfile" api as I do not see it listed in the MF docs.

While this is not really the group or time, I am looking for old
(sunset) retired RPG II and III programs for study.  I have read that
there are some 99,999 line programs out there and I would love to get
my hands on one.

Thanks one and all for your comments and suggestions.

If I get the problem solved, I will post the results here for all to
enjoy.

Ron
```

###### ↳ ↳ ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2010-02-23T22:56:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65e8c947-8bcc-4689-b7a1-d75eef3a4bf6@g28g2000prb.googlegroups.com>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com> <29597804-0660-4888-ba5e-19521b5c2adf@s36g2000prf.googlegroups.com> <b0e2e4af-ba6d-4be8-bec3-db55b3d98f25@k2g2000pro.googlegroups.com> <Mj1hn.32648$K81.3371@newsfe18.iad> <56928020-dfc6-42ad-bda5-ac75830a97b9@k5g2000pra.googlegroups.com>`

```
On Feb 24, 6:42 pm, Ronald Draper <ronald.dra...@gmail.com> wrote:
> On Feb 23, 9:48 pm, "James J. Gavan" <jgavandeletet...@shaw.ca> wrote:
>
…[133 more quoted lines elided]…
> moment.

I doubt that you will be able to access a disk as any form of file
when running under Windows. see:

http://www.codeproject.com/KB/system/rawsectorio.aspx

While a disk dumper may simply read blocks sequential from the device,
or write them for restoring, a 'recovery' program will need to
understand what the sector contents are. This was not easy for a
simple file system such as MS-DOS, it required bit shifting and bit
masking, things that are not portable in COBOL.

COBOL gains its 'portability' by defining a virtual machine that is
not necessarily the architecture of the underlying machine. Dealing
with raw disks _requires_ that the program work exactly like the
machine it is running on. For the purpose that you want, COBOL is not
portable, and probably not useful at all.

Interestingly on Unix/Linux one can open "/dev/sdb" if one is
superuser and can read it (or write if you must). For example 'cat /
dev/sda | less' (less is a better more) will display the raw drive
contents (less converts x00 to ^@ etc).

But Windows requires using the API that is nothing like file access.

Once you have accessed the blocks you will need to decode the
partition table, then each partition will have a file system that will
need decoding. With VFAT and NTFS there is no freely available
definitive documentation that will allow you to code your way reliably
around the system. For example Windows symlinks seem to be
undocumented.

When developers wrote the Linux NTFS driver they had to reverse
engineer the disk contents.

> If MF chooses not to respond, that is okay too.  There are a lot of
> companies that can not afford to maintain the older products and they
…[15 more quoted lines elided]…
> Ron
```

###### ↳ ↳ ↳ Re: read disk using mf cobol by \\\\.\\physicaldrivex

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-02-25T01:33:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ukkk8FcboU1@mid.individual.net>`
- **References:** `<68d89984-63e3-49b8-9241-c46e0728e4f4@k5g2000pra.googlegroups.com> <29597804-0660-4888-ba5e-19521b5c2adf@s36g2000prf.googlegroups.com> <b0e2e4af-ba6d-4be8-bec3-db55b3d98f25@k2g2000pro.googlegroups.com> <Mj1hn.32648$K81.3371@newsfe18.iad>`

```
James J. Gavan wrote:
> Ronald Draper wrote:
>
…[39 more quoted lines elided]…
> sub-routines being called, (Invoked in OO parlance).

Components are not sub-routines and neither are they necessarily small. You 
have a wrong conception of exactly what they are, and that is fine because 
it doesn't matter. As long as you don't go propagating it....

Is Excel a subroutine, or Outlook? Yet both are accessible via the Component 
Object Model.


> Yes he did things
> in Fujitsu but his main emphasis is .Net and components.

Ok, you got that right... :-)

>He came to
> realize that Fujitsu OO was lacking. It doesn't have the rich set of
> support classes that Net Express has, nor those available via .Net.

Jimmy this is outrageous.

You are not privy to the realizations which occur in my head so you make it 
up.

I did not come to realize that Fujitsu COBOL was "lacking", on the contrary, 
it is an excellent product and implementation of OO COBOL and I have said 
that here repeatedly. Neither does it lack the "rich set of support classes" 
which NE allegedly enjoys. You obviously don't know much about Fujitsu. 
Again, that is fine too, but now you are expounding this ignorance and 
attributing it to me. Have I ever posted something about you based purely on 
my assumptions and perceptions, rather than on quoted passages of what you 
have actually said? Can you not see how offensive and unnecessary that is?

It ISN'T chatty or friendly to make stuff up about people and post it is 
being true (any more than it is OK to reveal information from personal mail 
that people may not want made public, as you did recently.)

You have as much right to be here as anyone else (more than some :-)) but if 
you will persist in this pretence that you are privy to what I think and 
feel, and put words in my mouth that I not only never said , but never WOULD 
say...then you really can't expect me to respond to your posts.

We've had this discussion before and this is the last time I ever want to 
have it with you. DON'T attribute attitudes, feelings, opinions, or anything 
else to me, unless you can back it with a quote. In fact, I'd really be very 
happy if you simply left me out of your posts.

I'm perfectly happy to discuss things (on and off topic) in the usual way 
and have no problem doing that, but leave the personal assessments out of it 
please.

It isn't personal and I bear you no malice; I just don't want people 
thinking something you said that I said or thought, is the actual truth, 
when it isn't.

If you want to know what I think, (and it probably isn't half as much fun as 
making up your own take on it :-)), just ask me, or read my posts here. I 
try to make them clear and precise.

Getting back to Fujitsu COBOL...

My reasons for moving off COBOL were nothing to do with Fujitsu software, it 
DID have something to do with Fujitsu personnel. There is no point in 
picking at old wounds and I have posted here what drove me to download C# 
and Visual Studio. As it turned out, they did me a favour and I only wish I 
had had the balls to make the move much sooner, without being pushed by the 
incompetence and rudeness of salespeople, (but I didn't :-) - I was stuck in 
a comfortable little COBOL rut...) The distance between what I knew when I 
"left" and what I have learned since is huge, and the 4 years or so that 
have ensued have been enriching for me personally, professionally, and 
economically. So I wouldn't sit and fester about what went down.(Besides, it 
is not my nature to carry grudges...:-))

I honestly can't see COBOL lasting, but that also doesn't really matter. It 
is an opinion and it is arguable. I believe both Micro Focus and Fujitsu 
have excellent products, but they are products that are COBOL and that is a 
fading star.

As for collection classes, that is just one very tiny part of the whole OO 
landscape. Neither MF nor Fujitsu OO COBOL can support (in their unmanaged 
code products) the true richness of the .NET framework (over 90,000 classes 
in the latest release) so it is silly to say that one of them is better than 
the other; you might as well say that one of two horses is a donkey, as you 
get into your Ferrari...

>
> Neither of the above approaches is wrong, neither is yours nor mine.
…[68 more quoted lines elided]…
> problem will just go away").

Is it me, or do you get a creepy feeling of "deja vu" from the above?

I'm thinking VISOC, but in that case the notice period was not 12 months...

So, if support is being withdrawn and these versions are no longer 
maintained, does that mean the runtime fees no longer apply?

I think you are right about them not being a charity and now that Stephen 
Kelly has hopped it they may be lacking vision and direction. (No offence to 
the current management; it takes a while to get a feel for it.) The fact is 
they are in the business of selling a product that has a declining demand. 
From a business perspective that isn't a good place to be. It would make 
sense to start cutting costs as hard as possible and that probably does mean 
withdrawing support for old versions, just as you outlined.

I am currently supporting two versions of my software but I plan to close it 
to one. Fortunately I can afford to give people a free upgrade so it 
shouldn't be a problem. :-)

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
