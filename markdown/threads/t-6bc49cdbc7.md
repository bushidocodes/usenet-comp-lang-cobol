[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading MF Files from Powercobol7

_27 messages · 10 participants · 2003-02 → 2003-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Reading MF Files from Powercobol7

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-02-25T23:23:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2573793.1046215399@dbforums.com>`

```

I am trying to install Power 7 ( i have already use 6.1)
In documetatios fujtisu says that  its possible
to read, write etc  a Microfocus cobol File, just
doing this  C:\xxx\nameoffile.dat,EXFH(inf,xxx.dll)
where xxx.dll its  a .DLL thar reads Microfocus files.
the question is:
does anybody here knows how its wokrs?
does anybody here has tested It ?
This .DLL only reads files from NetExpress or Reads
Microfocus Vrs 5.0  (character Mode) ?
and finally , where can i get this  .DLL and what his name
because Fujtisu dont name it.

Tks
Carlos Lages
```

#### ↳ Re: Reading MF Files from Powercobol7

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-26T13:22:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5cbe97.18507712@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com>`

```
If you are converting to Fujitsu, you may not need that .dll. Ordinary Micro
Focus indexed files store the data as ASCII text delimited by cr-lf. You can
sort them with a utility and load into Fujitsu files. However, if they use
EXTFH, they are in a proprietary format. MOST Micro Focus files are ordinary.

Robert


Carlos lages <member129@dbforums.com> wrote:

>
>I am trying to install Power 7 ( i have already use 6.1)
…[16 more quoted lines elided]…
>Posted via http://dbforums.com
```

##### ↳ ↳ Re: Reading MF Files from Powercobol7

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-26T11:42:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302261142.3a10eded@posting.google.com>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> If you are converting to Fujitsu, you may not need that .dll. Ordinary Micro
> Focus indexed files store the data as ASCII text delimited by cr-lf. 

Is this also something you 'learnt' decades ago and never updated ?

MF Level II Cobol (circa early 80s) indexed files used a fixed record
size file for the data. This was roughly based on C-ISAM format.

However it had no restrictions on containing binary, packed, or any
other data and _cannot_ be treated as if it were ASCII text.  Valid
records were terminated by cr/lf but deleted records were marked with
a null byte over the cr.  The file was extended by clusters and there
may also be slack space at the end where records have not been written
yet.

In the mid-late 80s MF Cobol 2 introduced a better indexed file
format, but also could use old Level II files.  The new format catered
for variable length, compression, and various other improvements. 
This file structure had a file header and a header for each record
that gave the length.

> You can sort them with a utility 

Extremely poor advice.  Simply wrong in most cases.

> and load into Fujitsu files. 

There was no indication that he even _wanted_ to load into Fujitsu
files, he may well want to share files with a MF system.

> However, if they use EXTFH, they are in a proprietary format. 

No. Wrong. Misleading.  Cobol/2 (mid 80s) uses EXTFH for all access to
MF indexed files regardless of whether they are Level II format or
Cobol/2 format.

> MOST Micro Focus files are ordinary.

They may have all been Level II format two decades ago, but even these
weren't 'ordinary' in any way due to binary or packed data, deleted
records, slack space.
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-28T02:55:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e5ead7e.97103717@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[3 more quoted lines elided]…
>Is this also something you 'learnt' decades ago and never updated ?

It is something I work with every day on my (almost) current Micro Focus
compiler. A plain vanilla indexed file uses this format. One must specify EXTFH
to get the External File Handler. Only one file in this shop uses EXTFH.

>MF Level II Cobol (circa early 80s) indexed files used a fixed record
>size file for the data. This was roughly based on C-ISAM format.
>
>However it had no restrictions on containing binary, packed, or any
>other data and _cannot_ be treated as if it were ASCII text.

Which is why my Best Practices says to store numbers in files in display format.


>  Valid
>records were terminated by cr/lf but deleted records were marked with
>a null byte over the cr.  

Any editor worth its salt will interpret 0A as a line terminator. 

>In the mid-late 80s MF Cobol 2 introduced a better indexed file
>format, but also could use old Level II files.  The new format catered
>for variable length, compression, and various other improvements. 
>This file structure had a file header and a header for each record
>that gave the length.

Probably so, but it did not become the default format. 

>There was no indication that he even _wanted_ to load into Fujitsu
>files, he may well want to share files with a MF system.

That's why I began "If you are converting..". It sounded to me like he was.

>> MOST Micro Focus files are ordinary.
>
>They may have all been Level II format two decades ago, but even these
>weren't 'ordinary' in any way due to binary or packed data, deleted
>records, slack space.

Most Micro Focus files are what you call Level II TODAY. What does slack space
have to do with anything?
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-28T03:41:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5ED99F.F42D96B0@shaw.ca>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net>`

```


Robert Wagner wrote:

> >> If you are converting to Fujitsu, you may not need that .dll. Ordinary Micro
> >> Focus indexed files store the data as ASCII text delimited by cr-lf.
> >
> >Is this also something you 'learnt' decades ago and never updated ?
>

Richard originally jumped in on this one with historical background. Exactly which
is your 'almost current' M/F compiler. I just didn't understand your reference to '
indexed files store the data as ASCII text delimited by cr-lf'.

Back to the DOS V 3.0 and then VISOC and Net Express - if I use an old PC Magazine
routine 'DR', (in a DOS Window), I can look at any file, (COBOL or otherwise). But
any ISAM, Sequential or Relative that has comp fields just shows up as a series of
gobbledegook characters - not dissimilar to the Rosetta stone. Naturally text fields
are readable.

When displaying the above three types they just display across the screen with
wrap-around - no intervening space indicating CR/LF. It is only Line Sequential that
'jumps' to a newline triggered by the CR/LF.

And so far as using that Fujitsu support DLL, the original enquirer must have been
referring to very current M/F formats. Sure, I have used the M/F Convert3 tool to
move RM/COBOL ISAMs to M/F - but that was the old RM/COBOL '74 V 2.0. Not worth
tiddly squat with the latest RM file formats.

> >However it had no restrictions on containing binary, packed, or any
> >other data and _cannot_ be treated as if it were ASCII text.
>
> Which is why my Best Practices says to store numbers in files in display format.
>

Now - there's a statement a couple of old hands here will agree with you on. Not me,
I'm much more interested in design than programming and bits and bytes. But based on
what they have previously written, I go along with the advantages that they
highlighted.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-27T22:27:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3mofi$3a$1@slb9.atl.mindspring.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca>`

```
Let me jump into this thread and give you the information that when EXTFH is
and is not used - and what the "default" file handling facility is depends
(or at least did when I last checked) VERY MUCH on whether you are using a
Micro Focus "Unix-type" or "DOS/Windows-type" compiler.  For further
information on "Object COBOL 4.1.40 for UNIX" usage, see:

http://supportline.microfocus.com/documentation/books/ocds4140/oc41indx.htm

and look (for example) at:

"10.2 Using the Callable File Handler"

  which says in part,

"Your programs may already be using the Callable File Handler. If your COBOL
program uses Micro Focus COBOL syntax for all its file handling, the
Callable File Handler is used in the following cases:

 - If the CALLFH Compiler directive is used, all COBOL I/O statements are
compiled into calls to ExtFH, or to a file handler of your own, if
specified.

 - 32-bit:
On 32-bit systems, all COBOL I/O statements are compiled into calls to
ExtFH.

 - 16-bit:
On 16-bit systems, if you do not set the CALLFH Compiler directive, ExtFH is
used as follows:
 - ExtFH is called by the run-time system to handle I/O operations on all
indexed files.
 -The Compiler puts direct calls to ExtFH in your compiled code to handle
I/O operations on files of all organizations that have the ANSI'85 attribute
of EXTERNAL. "

and also of "interest" is

"10.1.3 Supported Files"

which says,

"In addition to the standard COBOL organizations, the following file types
are also supported:
 - LEVEL II COBOL
 - IDXFORMAT"4"
 - Btrieve format with ANSI emulation
 - Btrieve format without ANSI emulation
- C-ISAM (UNIX and 32-bit OS/2)"

    ***

Therefore, to understand which "file system" is being used when one says
"Micro Focus" - one needs to know

  - the platform (operating system)
 - the release of the compiler
 - what directives were used
 - whether "standard" COBOl syntax or other mechanism were used to access
the files.
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-02-28T04:46:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E5EE87D.F4479A0E@shaw.ca>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net>`

```


"William M. Klein" wrote:

> Let me jump into this thread and give you the information that when EXTFH is
> and is not used - and what the "default" file handling facility is depends
…[5 more quoted lines elided]…
>

Well you know me 'Sir William' - I avoid using Directives like the plague - so
I'm using the Default whatever the hell that is <G>

Jimmy
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 6)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-01T01:47:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e600256.184372586@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>"In addition to the standard COBOL organizations, the following file types
>are also supported:
…[4 more quoted lines elided]…
>- C-ISAM (UNIX and 32-bit OS/2)"

IDXFORMAT"4" is what I meant to say, rather than EXTFH. 

Whether a file is accessed via EXTFH vs. run-time code doesn't change its
format. 

Vanilla, default Micro Focus indexed files are formatted like ASCII text. They
can be read by utilities such as sort and text editors. Only files designated
IDXFORMAT"4" are in an ISAM-like format.

The other formats referenced above are foreign to MF. If a shop has 'MF format
files', they are either vanilla or IDXFORMAT"4".  In a typical Micro Focus shop,
all or a vast majority of indexed files will be the former, which means you
don't need conversion software, you can process them as flat or 'line
sequential' files. 

Robert
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-01T03:45:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E602B0E.5A36DE21@shaw.ca>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net>`

```


Robert Wagner wrote:

> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
…[23 more quoted lines elided]…
> Robert

Robert,

Here you go again. I have always used the D-E-F-A-U-L-T format without any prior
knowledge of what that is - and checking the Net Express on-line help - this tells
me that the Default *IS* :-

The IDXFORMAT parameter specifies the format to use when creating indexed files.

IDXFORMAT=integer

Default: 3

0 Default format for the operating system (same as 3 on Windows)
1 C-ISAM
3 Micro Focus default indexed file format
4 Optimized format for fast duplicate key handling
5 Btrieve with ANSI conformance
6 Btrieve without ANSI conformance
8 Large indexed file format

And that being the case - there is no way I can view ISAMs as Ascii Text !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-01T18:32:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3pgo7$g1r$1@aklobs.kc.net.nz>`
- **References:** `<2573793.1046215399@dbforums.com> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca>`

```
Robert Wagner wrote:
 
> "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
…[11 more quoted lines elided]…
> format.

You have already been told, and you can confirm it by reading the manual, 
that _ALL_ _indexed_ files on DOS, Windows and OS/2 whether 16 or 32 bit 
since Cobol/2 have used EXTFH to access the files of the above type. If you 
read the manual, or even WMKs extract, you will that it tells you that code 
is generated by the compiler to call the EXTFH module.

For example in the archaic version 2.5 Toolset Reference manual (p 3-2):

"The file handler [EXTFH] is called by the run-time system to handle I/O 
operations on all files with organization indexed."

There are a few cases where sequential and relative files may use the 'run 
time', but indexed files use EXTFH.

As you have been told the IDXFORMAT controls the format that files are 
_created_.  The EXTFH module is able to create and use all the above 
formats (in all versions in the last decade).

> Vanilla, default Micro Focus indexed files are formatted like ASCII text.

No. WRONG. You have been told this before.

The default is IDXFORMAT'3'.  These are structured files with binary file 
and record headers and are nothing like 'ASCII text'. Go and read what it 
tells you in the manual.

If you have Level II (IDXFORMAT'2') files (by accident or design), while 
yours may superficially look like ASCII files, it has been explained to you 
why they cannot be treated as such, even if the design avoids binary or 
packed data, which it need not.

It may be that your compiling environment has a .DIR directives file that 
has IDXFORMAT'2' in it, go and ask someone in your site that has two clues 
to rub together to explain this to you.

> They can be read by utilities such as sort and text editors. 

Not in any useful way in the general case.

> Only files designated IDXFORMAT"4" are in an ISAM-like format.

No that is simply not true, it is a lie, it is false.  In fact it 
specifically states in the manual that IDXFORMAT'4' is "an optimised form 
of [IDXFORMAT'3'].  And IDXFORMAT'3' is the default (read the manual).

The actual differences between '3' and '4' are in the index file and not in 
the data file, in both cases this has headers with binary data for the file 
and for each record.

Older versions of MF (eg version 2.5 of 1991) did require that for the use 
of IDXFORMAT'4' an additional package be bought, but this was rolled into 
the normal EXTFH, probably around version 3.0.

What actual version are you using, how out of date are you ?

> The other formats referenced above are foreign to MF. If a shop has 'MF
> format files', they are either vanilla or IDXFORMAT"4".  

No The formats above are the ones that MF will create and maintain (in 
recent versions, certainly since 1994).  It is only necessary to specify 
the appropriate IDXFORMAT and this will be used when the file is created.

_NONE_ of them are 'vanilla'.

> In a typical Micro
> Focus shop, all or a vast majority of indexed files will be the former,

You have absolutely no idea about what 'typical MF shops' do.  Many of 
them, for example, will be using versions that are less than a dozen years 
old.

The default is _not_ Level II, it is a format that is a 'non-optimised' 
form of IDXFORMAT'4'.  
 
> which means you don't need conversion software, you can process them as
> flat .. files.

No you cannot, unless you are prepared to lose data and have junk:

          The file may have binary or packed data.
          Deleted records are left in the file and may 'reappear',
                or worse.
          Slack space at end of file will give junk.

And this is only if they are specifically Level II which is the closest to 
'ordinary' (though C-ISAM is much the same).

> or 'line sequential' files.

And that is possibly your worst piece of advice ever.  Even if they are 
Level II format any binary or packed data will cause records to be junked.
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 9)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-03-01T01:55:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Zg2dnau0rLnBxP2jXTWc3Q@comcast.com>`
- **References:** `<2573793.1046215399@dbforums.com> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <b3pgo7$g1r$1@aklobs.kc.net.nz>`

```
> No that is simply not true, it is a lie, it is false.  In fact it
> specifically states in the manual that IDXFORMAT'4' is "an optimised form
> of [IDXFORMAT'3'].  And IDXFORMAT'3' is the default (read the manual).
>
> The actual differences between '3' and '4' are in the index file and not
in
> the data file, in both cases this has headers with binary data for the
file
> and for each record.
>

    Actually, the type 4 data files are slightly different from the
type 3 data files.  They have some extra information in the data
file.  The major difference is that the type 4 allows more than
65,535 records with the same exact value in an alternate key
that allows duplicate values.  It also is much faster when this
is true (Example - a phone number is placed in a key field, but
many people do not give you their phone number.

    Most of the data files in microfocus indexed files can be accessed
without using the index, but it is finicky work.  Use rebuild if you
can.
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-01T11:41:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6096ac.222352547@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <b3pgo7$g1r$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:

>You have already been told, and you can confirm it by reading the manual, 

I wish you'd stop talking down to me, as though I'm a child. Doing so doesn't
make you seem more knowledgable, just more unmannerly. 

>> Vanilla, default Micro Focus indexed files are formatted like ASCII text.
>
…[4 more quoted lines elided]…
>tells you in the manual.

I don't have to read about it. I work with these files every day. 

>It may be that your compiling environment has a .DIR directives file that 
>has IDXFORMAT'2' in it, go and ask someone in your site that has two clues 
>to rub together to explain this to you.

I know what the compiling environment is because I set it up. There isn't anyone
else here to ask. If you want to talk to the 'systems guy', that's me.

>> Only files designated IDXFORMAT"4" are in an ISAM-like format.
>
…[6 more quoted lines elided]…
>and for each record.

This statement shows the weakness of relying on (misinterpreted) manuals rather
than hands-on field experience. 

The knowledge that they are ASCII files (after purging deleted records via
reorg) is _useful_ to someone doing a conversion. Your hand-waving obfuscates
the issue rather than illuminating it. 

>What actual version are you using, how out of date are you ?

I'm using Micro Focus for Solaris dated 1999.

>> or 'line sequential' files.
>
>And that is possibly your worst piece of advice ever.  Even if they are 
>Level II format any binary or packed data will cause records to be junked.

More hand-waving. I would never store binary or packed data in a file. In this
financial services industry, all files are assumed to be portable.
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-02T09:15:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3r4fp$b01$1@aklobs.kc.net.nz>`
- **References:** `<2573793.1046215399@dbforums.com> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <b3pgo7$g1r$1@aklobs.kc.net.nz> <3e6096ac.222352547@news.optonline.net>`

```
Robert Wagner wrote:

> I wish you'd stop talking down to me, as though I'm a child.

I talk down to you because you act like a child who has never been out of 
his playpen and thinks that the whole world is like that.
 
> I'm using Micro Focus for Solaris dated 1999.

That is atypical.  The default for that is C-ISAM.  You obviously didn't 
notice that we were being specific in saying 'DOS Windows and OS/2'.  You 
never noticed that Solaris isn't DOS Windows or OS/2 ?

> This statement shows the weakness of relying on (misinterpreted) manuals
> rather than hands-on field experience. 

Quite the reverse.  If you had read any manuala you would know that Solaris 
is _NOT_ Net Express, is _NOT_ the specified 'DOS, Windows and OS/2'.

Even when WMK was quite specific with "depends VERY MUCH on whether you are 
using a Micro Focus "Unix-type" or "DOS/Windows-type" compiler." it simply 
didn't register with you.

Do most of these posts pass through without triggering a brain cell ? 

But no, you _insisted_ that you were right, all MicroFocus _must_ be like 
yours, the manual quotes and personal experience being sent to you _must_ 
be completely wrong simply because it was from outside your experience.

> I don't have to read about it. I work with these files every day.

You obviously feel that you don't have to read anything, all can be learnt 
from studying your navel.

> I know what the compiling environment is because I set it up. There isn't
> anyone else here to ask. If you want to talk to the 'systems guy', that's
> me.

<<<shudder>>>.  Did you say this 'here' deals with the IRS ?

> The knowledge that they are ASCII files (after purging deleted records via
> reorg) is _useful_ to someone doing a conversion. Your hand-waving
> obfuscates the issue rather than illuminating it.

No. Entirely the opposite.  Your 'knowledge' that Solaris does it a way 
that is different to the majority is _only_ useful for Solaris users, and 
only those who do not have binary or packed data, (or index data items).

My 'hand waving' is useful to the other 99.99% of the world.

But as you haven't yet come to terms with the fact that the 'rest of the 
world' is not just like a bigger version of your desk, you probably won't 
understand that.

>>And that is possibly your worst piece of advice ever.  Even if they are
>>Level II format any binary or packed data will cause records to be junked.
> 
> More hand-waving. I would never store binary or packed data in a file. In
> this financial services industry, all files are assumed to be portable.

While >>>> _YOU_ <<<< may "never store binary data", this is nota 
automatically a restriction on the rest of the world.  For >>>> _THEM_ <<<< 
it is particulaly bad advice.

As an aside, and as a serious question, not just a put down: have you been 
tested for Autism ?
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-01T18:40:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ph7b$g94$1@aklobs.kc.net.nz>`
- **References:** `<2573793.1046215399@dbforums.com> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca>`

```
James J. Gavan wrote:

> 0 Default format for the operating system (same as 3 on Windows)
> 1 C-ISAM
…[4 more quoted lines elided]…
> 8 Large indexed file format

Interesting that '2' - Level II format has finally been dropped.  I still 
have some systems that started on Level II Cobol and moved to more recent 
versions while retaining their existing files.

There have been some restritions on Level II format files, though nothing 
serious to me, I can understand why they would drop it.
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 8)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-01T11:41:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6088e0.218819360@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:

>
>
…[17 more quoted lines elided]…
>> Vanilla, default Micro Focus indexed files are formatted like ASCII text.
They
>> can be read by utilities such as sort and text editors. Only files designated
>> IDXFORMAT"4" are in an ISAM-like format.
>>
>> The other formats referenced above are foreign to MF. If a shop has 'MF
format
>> files', they are either vanilla or IDXFORMAT"4".  In a typical Micro Focus
shop,
>> all or a vast majority of indexed files will be the former, which means you
>> don't need conversion software, you can process them as flat or 'line
…[6 more quoted lines elided]…
>Here you go again. I have always used the D-E-F-A-U-L-T format without any
prior
>knowledge of what that is - and checking the Net Express on-line help - this
tells
>me that the Default *IS* :-
>
>The IDXFORMAT parameter specifies the format to use when creating indexed
files.
>
>IDXFORMAT=integer
…[11 more quoted lines elided]…
>And that being the case - there is no way I can view ISAMs as Ascii Text !

Nothing here contradicts what I said. Format 3, Micro Focus default, is ASCII
text. The deleted records problem can be solved by reorganizing the file before
conversion.
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-02T08:53:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3r380$ae3$1@aklobs.kc.net.nz>`
- **References:** `<2573793.1046215399@dbforums.com> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <3e6088e0.218819360@news.optonline.net>`

```
Robert Wagner wrote:


>> and checking the Net Express 
                    ^^^^^^^^^^^
>>Default: 3
>>
…[12 more quoted lines elided]…
> file before conversion.

Now that you have revealed that you are talking about a different product 
entirely we can see the difficulty you are having.

This specifically states 'Net Express', others have stated 'DOS, Windows, 
OS/2'.  

Solaris has a default of C-ISAM (which is much the same as Level II).

MF Solaris is not Net Express. Solaris is not 'DOS, Windows or OS/2'. 

IDXFORMAT'3' files are _NOT_ 'ASCII text', they are very much like 
IDXFORMAT'4' - which you should know 

C-ISAM are not 'ASCII text' (though superficially they may look like it).

Indexed files have no restriction on having binary or packed data, and thus 
may not be at all like ASCII files.

At least you finally have noticed that deleted records are a problem, that 
is one clue you have grown.

You really can't understand that the world outside your office maight be 
different.  You had advised some one that they could just read the file 
into a sort or as a flat file.  You completely failed to notice that some 
conditions needed to be added:

     _IF_ you want to convert (not even implied)
     _IF_ you use Solaris (0.01% chance)
     _IF_ you use only DISPLAY ASCCI text in records.
     _IF_ you have reorganised
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-01T23:28:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e613944.3185692@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <3e6088e0.218819360@news.optonline.net> <b3r380$ae3$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:

>>> and checking the Net Express 
>                    ^^^^^^^^^^^
…[17 more quoted lines elided]…
>OS/2'. 

The Micro Focus Solaris manual contains the same language. I thought my files
were format 3. 

>Solaris has a default of C-ISAM (which is much the same as Level II).

I did not know that. Thanks for the education. 

>C-ISAM are not 'ASCII text' (though superficially they may look like it).

If a file contains no packed/binary fields, the only difference is deleted
records. When viewed with a text editor, they look like non-deleted records. 

>At least you finally have noticed that deleted records are a problem, that 
>is one clue you have grown.

I said to reorganize the file to get rid of them before conversion.

>     _IF_ you use Solaris (0.01% chance)

It's very likely to be the same on other brands of Unix. Make that 3%. 

I spent a year writing MF COBOL on HP-UX, but didn't use indexed files there. It
was all database. 

<mention of database causes light bulb to come on>

ODBC! Why didn't I think of it first? Why didn't anyone else? That's the answer
to the original question, which was how to access MF files from Fujitsu. Micro
Focus offers an ODBC driver called Correlate. A Web search found at least six
other sources, such as:

http://www.parkway-software.com/sql/funktion_1.html

Another solution requires no additional software. Write an access program in
Micro Focus and 'call' it from Fujitsu. Trying to do this with a COBOL CALL
would be asking for trouble because Micro Focus requires an extensive run-time,
and Fujitsu has a small run-time as well. I'd run them as two tasks
communicating through a pipe. See API functions CreateNamedPipe and CreateFile
to get started. Two other unattractive approaches come to mind: shared memory
(high overhead) and passing the data through a dll, which is amateurish but does
have the attraction of an all-COBOL solution. IMO, pipe is the way to go .. if
you are comfortable talking to the Windows API. 

Richard (and others): don't ask me to post code samples showing how to call
Windows from MF and Fujitsu. It can be done with a little 'glue'.

Robert
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-01T23:19:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E61406C.FAB129CC@shaw.ca>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <3e6088e0.218819360@news.optonline.net>`

```


Robert Wagner wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
…[61 more quoted lines elided]…
> conversion.

Well I give up - don't expect any more comment from me !. And as regards your paper
'Best Practices...", I suggest you re-title it "The Shitiest Practices you can use".

I have to stop here - like the other ex-Brit, Richard, I might get into some salty
epithets - and with 12 years in the RAF - you can take for granted my repertoire
will be more versatile than Richard's.

Jimmy
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 10)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-02T01:41:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e61602d.13147988@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <3e6088e0.218819360@news.optonline.net> <3E61406C.FAB129CC@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote:

>I have to stop here - like the other ex-Brit, Richard, I might get into some
salty
>epithets - and with 12 years in the RAF - you can take for granted my
repertoire
>will be more versatile than Richard's.

I was in US Marine Corps Reconnaissance, commonly called "animals". We worked
behind Pathet Lao and Khymer Rouge lines, and ran POW camps in SE Asia. I'm very
familar with brow beating and psychological pressure. We were also at Bay of
Pigs a week before the landing. 

RAF conjures pictures of guys in white ascots. If you had said SAS or SBS, we'd
be talking on the same level.  If you think you're saltier than Americans,
consider this email I recently received:

>An actual letter home from a marine with the multinational force in 
>Bosnia:
…[13 more quoted lines elided]…
>I additionally told him that America, being a nation of deeds and action,
not words, 
>would do whatever it had to do, and France's support, if it ever came, was
only 
>for show anyway.  Just like in ALL NATO exercises, the US would shoulder 85% 
>of the burden, and provide 85% of the support, as evidenced by the fact that
…[15 more quoted lines elided]…
>LtCol., USMC

In parting, go fuck yourself. 

Robert
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 11)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-03-02T05:17:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ltg8a.77032$zF6.5487269@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <3e6088e0.218819360@news.optonline.net> <3E61406C.FAB129CC@shaw.ca> <3e61602d.13147988@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message news:3e61602d.13147988@news.optonline.net...
> 
> RAF conjures pictures of guys in white ascots.

I was actually crediting you with intelligence until this point.

I thought that your arrogance and a burning desire 
to be the center of attention were the barrier between us.

Do you harbor the same disrespect for all who serve their country?
Excluding yourself, of course?
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-02T19:18:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e625869.76705494@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <3e6088e0.218819360@news.optonline.net> <3E61406C.FAB129CC@shaw.ca> <3e61602d.13147988@news.optonline.net> <ltg8a.77032$zF6.5487269@bgtnsc04-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote:

>Robert Wagner <robert@wagner.net> wrote in message
news:3e61602d.13147988@news.optonline.net...
>> 
>> RAF conjures pictures of guys in white ascots.
…[7 more quoted lines elided]…
>Excluding yourself, of course?

Touched a nerve, did I? I disrespect flag-wavers who get their patriotism from
tabloid newspapers. How ignoble. How unsophisticated. I respect guys like you,
who actually did something. 

FWIW, the failure at Bay of Pigs was blamed on "bad intelligence". I know the
intelligence was correct because I wrote the 'bad' report. What did them in was
someone from our side leaked the plan to the bad guys (published it in Stern)
and the CIA's amateur 'air force' kept getting lost. But we (Recon) got blamed
for screwing up. Reading this newgroup caused me to recall other bum raps.  

Robert
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 11)_

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-02T11:17:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1FFD3FFC522EBA71.B34540BCE6FFDC02.77C37F13502FAAEB@lp.airnews.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <3e6088e0.218819360@news.optonline.net> <3E61406C.FAB129CC@shaw.ca> <3e61602d.13147988@news.optonline.net>`

```
On Sun, 02 Mar 2003 01:41:38 GMT, robert@wagner.net (Robert Wagner)
enlightened us:

>
>"James J. Gavan" <jjgavan@shaw.ca> wrote:
…[30 more quoted lines elided]…
>>

I've seen this on the internet somewhere, but can't recall where.  Has
your daughter (real or imagined) posted this elsewhere?

Another thing, she'd better learn her history.  The United States did
not help France in Vietnam.  Fact of the matter is France was trying
to take Vietnam over and Vietnam asked the U.S. to intervene.
President Truman not wanting to annoy a fellow Nato partner did
nothing and the Vietnamese forces went on to kick France's butt all by
themselves.  However, Ho Chi Minh did not forget the U.S. snub.  Also
remember that Ho Chi Minh and Vietnam provided much more intelligence
against Japan during WWII than almost anyone else in Southeast Asia.

So I guess your grasp of history is about as accurate as your "Best
Practices".

>>I additionally told him that America, being a nation of deeds and action,
>not words, 
…[14 more quoted lines elided]…
>>

A you wonder why they think Americans are "cowboys" .

>>Dad, tell Mom I love her,
>>
…[6 more quoted lines elided]…
>Robert

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Going to war without France is like going deer hunting 
without your accordian."  - Donald Rumsfeld / US Secretary of Defense
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-03-02T12:09:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3tds9$lch$1@panix1.panix.com>`
- **References:** `<2573793.1046215399@dbforums.com> <3E61406C.FAB129CC@shaw.ca> <3e61602d.13147988@news.optonline.net> <1FFD3FFC522EBA71.B34540BCE6FFDC02.77C37F13502FAAEB@lp.airnews.net>`

```
In article <1FFD3FFC522EBA71.B34540BCE6FFDC02.77C37F13502FAAEB@lp.airnews.net>,
SkippyPB  <swiegand@neo.NOSPAM.rr.com> wrote:
>On Sun, 02 Mar 2003 01:41:38 GMT, robert@wagner.net (Robert Wagner)
>enlightened us:
…[24 more quoted lines elided]…
>>>A funny thing happened to me yesterday at CampBondsteel (Bosnia). A French

[snip]

>I've seen this on the internet somewhere, but can't recall where.  Has
>your daughter (real or imagined) posted this elsewhere?
>
>Another thing, she'd better learn her history.

... and geography.  From http://www.snopes.com/military/marine.htm :

--begin quoted text:

A real soldier -- especially one serving in the Balkans -- would know Camp 
Bondsteel is in Kosovo, not Bosnia. 

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 12)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-02T22:07:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e626180.79033436@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net> <3E5ED99F.F42D96B0@shaw.ca> <b3mofi$3a$1@slb9.atl.mindspring.net> <3e600256.184372586@news.optonline.net> <3E602B0E.5A36DE21@shaw.ca> <3e6088e0.218819360@news.optonline.net> <3E61406C.FAB129CC@shaw.ca> <3e61602d.13147988@news.optonline.net> <1FFD3FFC522EBA71.B34540BCE6FFDC02.77C37F13502FAAEB@lp.airnews.net>`

```
SkippyPB <swiegand@neo.NOSPAM.rr.com> wrote:

>On Sun, 02 Mar 2003 01:41:38 GMT, robert@wagner.net (Robert Wagner)
>enlightened us:

>>>An actual letter home from a marine with the multinational force in 
>>>Bosnia:

>I've seen this on the internet somewhere, but can't recall where.  Has
>your daughter (real or imagined) posted this elsewhere?

I didn't claim she was _my_ daughter. Someone forwarded it to me. As you say,
the letter is going around the internet. It doesn't rign true to my ear as an
actual letter, but does accurately portray the attitude of Marines. 

>A you wonder why they think Americans are "cowboys" .

Real cowboys in West Texas, where I lived for 20 years, are paragons of modesty
and civility .. 180 degrees opposite from the cocky, reckless image assigned to
the word. 

Robert
```

###### ↳ ↳ ↳ Re: Reading MF Files from Powercobol7

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-28T12:39:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302281239.39e3ccd9@posting.google.com>`
- **References:** `<2573793.1046215399@dbforums.com> <3e5cbe97.18507712@news.optonline.net> <217e491a.0302261142.3a10eded@posting.google.com> <3e5ead7e.97103717@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> It is something I work with every day on my (almost) current Micro Focus
> compiler. A plain vanilla indexed file uses this format. One must specify EXTFH
> to get the External File Handler. Only one file in this shop uses EXTFH.

No. That is wrong. There is _NO_ compiler option 'EXTFH'. If the
system is DOS or Windows or OS/2 and is MF Cobol later than the
mid-80s the it _WILL_ be using EXTFH for indexed files.

Ypou may be confused by the CALLFH compiler option which allows you to
specify a _different_ external file handler. If you do not use a
non-MF file handler, such as B-Trieve, then you _will_ be using EXTFH
whether you know it or not, whether the CALLFH is specified or not.

> Which is why my Best Practices says to store numbers in files in display format.

It may well be that you self impose this restriction on yourself, but
you advised others that the indexed file _WILL_ be ASCII characters
and you have no means of knowing whether this is true or not.

> Any editor worth its salt will interpret 0A as a line terminator. 

Exactly.  And deleted records will be brought back to life again.  If,
however, the delete marker is _not_ treated as a line terminator the
record after the deleted record will be appended to the deleted record
and if this is trimmed the deleted record becomes live and a valid
record is lost.

If the record contains binary or packed data (on which there is no
actual restriction) the data may cause many problems.

> Probably so, but it did not become the default format. 

Yes it did.  See the IDXFORMAT compiler option.  The default has been
'current system' since mid-late-80s.  It requires IDXFORMAT'2' to
create Level II format files, which are the closest to your
'ordinary', though still unusable in the way you suggested.

The IDXFORMAT applies when a file is created, so the program will
still use files created by earlier systems in the format they have.
 
> That's why I began "If you are converting..". It sounded to me like he was.

Do you think so ?  It didn't sound like he wanted to convert to me, he
was quite specific that he wanted "to read, write etc  a Microfocus
cobol File,"

> >> MOST Micro Focus files are ordinary.
> 
> Most Micro Focus files are what you call Level II TODAY. 

What surveys have you done to determine this ?  Given that it has been
the default for nearly two decades to _not_ use Level II then your
assertion is simply bogus.

> What does slack space have to do with anything?

You are supposed to understand these things before giving advice to
others.

When a new record is to be written and there is no space for it an
arbitrary amount of disk space is added to the file, sufficient for
several records and the one record is written somewhere in there.

When the file is read as record sequential then the unwritten parts of
that extended space are read as junk records.  Even if they get
ignored they may affect the alignment of any good records there.

MF indexed files are _not_ ordinary files and cannot be treated as
such even when they are the old Level II and even if they are only
ASCII data.
I think that you have excelled even your own best in this thread in
that _every_ point that you made was factually wrong, misleading, bad
advice or indicated that you had a complete lack of understanding of
the issues.
```

#### ↳ Re: Reading MF Files from Powercobol7

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-02-26T21:36:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0302262136.604a8d58@posting.google.com>`
- **References:** `<2573793.1046215399@dbforums.com>`

```
Carlos - chapter 7 of the Windows users guide tells how to do this.

You really only need do this:

assign..... "C:\xxxxx\nameoffile.dat,EXFH"

Then in your COBOL85.CBR add these lines:

@CBR_EXFH_API=MFFH
@CBR_EXFH_LOAD=MFFH.DLL

You might have to change the API to EXTFHSUB - I've not got it working
yet because I don't have the NetExpress runtime properly installed on
the machine I first tested on.  I'll check another - but this might
get you started.  Please report your progress here!


Carlos lages <member129@dbforums.com> wrote in message news:<2573793.1046215399@dbforums.com>...
> I am trying to install Power 7 ( i have already use 6.1)
> In documetatios fujtisu says that  its possible
…[12 more quoted lines elided]…
> Carlos Lages
```

#### ↳ Re: Reading MF Files from Powercobol7

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-01T23:28:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6140b0.5086282@news.optonline.net>`
- **References:** `<2573793.1046215399@dbforums.com>`

```
Carlos lages <member129@dbforums.com> wrote:

>
>I am trying to install Power 7 ( i have already use 6.1)
…[10 more quoted lines elided]…
>because Fujtisu dont name it.

Use an ODBC driver. You can get one from Micro Focus, where it is called
Correlate, or at least six other sources. The access language will be SQL.

Call an access module written in Micro Focus. See my posting to Richard for more
on this. 

Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
