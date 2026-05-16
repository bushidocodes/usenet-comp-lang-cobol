[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ok, heres one...

_13 messages · 10 participants · 1998-08 → 1998-09_

---

### ok, heres one...

- **From:** Mike Ganas <skidmike@mindspring.com>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EA0537.9A5E33D5@mindspring.com>`

```
back to the muffler shop system.  we want to keep estimates on file in
hopes that the customer comes back.  but the estimates need to be
deleted after 15 days.  i can deal with the date-handling myself, how do
you delete a file totally from cobol?  i can open output it and then
close it, but that leaves the filename in the directory.
well?
```

#### ↳ Re: ok, heres one...

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35E9FFC6.614F@erols.com>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com>`

```
Mike Ganas wrote:
> 
> back to the muffler shop system.  we want to keep estimates on file in
…[4 more quoted lines elided]…
> well?

I fail to see what benefit would be gained from complete deletion... but
why not just toss off an IEFBR14 with a DISP=(OLD,DELETE,DELETE)?

DD
```

#### ↳ Re: ok, heres one...

- **From:** gchomuk@my-dejanews.com
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sf631$e9b$1@nnrp1.dejanews.com>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com>`

```
In article <35EA0537.9A5E33D5@mindspring.com>,
  Mike Ganas <skidmike@mindspring.com> wrote:
> back to the muffler shop system.  we want to keep estimates on file in
> hopes that the customer comes back.  but the estimates need to be
…[4 more quoted lines elided]…
>
Sounds suspiciously like MS-Cobol.  There must be a way to issue a DOS delete
of the file. C, C++ has the SYSTEM("DELETE"), or SHELLEXT("DELETE") function.

MS-COBOL should have something similar.  Opening the Closing the file, as you
indicated, leaves a directory entry of zero length.  You need to issue a
system call to issue the delete.  You'll have to close the file, of course,
prior to deleting.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: ok, heres one...

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Zyitn3r2DSE1@Dwight_Miller.iix.com>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com> <6sf631$e9b$1@nnrp1.dejanews.com>`

```
On Mon, 31 Aug 1998 21:54:41, gchomuk@my-dejanews.com wrote:

> In article <35EA0537.9A5E33D5@mindspring.com>,
>   Mike Ganas <skidmike@mindspring.com> wrote:
…[6 more quoted lines elided]…
> >

He's running Fujitsu COBOL 3.0 and it does support the Delete File of 
the next standard.
```

#### ↳ Re: ok, heres one...

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EB1257.225DA5E2@IMN.nl>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com>`

```
Mike Ganas wrote:

> back to the muffler shop system.  we want to keep estimates on file in
> hopes that the customer comes back.  but the estimates need to be
…[3 more quoted lines elided]…
> well?

COBOL does not have external file handling capacities, like delete, rename,
move, copy etc. the only way to do is  calling some system utility or a
program written in another language that has those capabilities.

But it is platform dependent how and what to call.
On IBM mainframe, invoke some JCL, f.e. the IEFBR14 that The Goobers
mentioned in his reply post.
On PC's with DOS/WinX you could call (via command.com f.e.) some batch file.
From Micro Focus I know that they have some special routines provided, like
CBL_CHECK_FILE_EXIT, CBL_DELETE_FILE, CBL_RENAME_FILE (and for DIR's as
well). Probably fujitsu, acuCOBOL and others have some stuff too...

Does this help?

You could also redesign to one big file containing all customer's records,
preferably ordered by customer/date and precess that with OPEN I-O and the
DELETE record statements.

The COBOL Frog
```

##### ↳ ↳ Re: ok, heres one...

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sf50k$6n8@dfw-ixnews10.ix.netcom.com>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com> <35EB1257.225DA5E2@IMN.nl>`

```
This seems to be my month to plug the new (draft) Standard.

COBOL Frog (Huib Klink) wrote in message <35EB1257.225DA5E2@IMN.nl>...
>Mike Ganas wrote:
>
…[10 more quoted lines elided]…
>


The new (draft) Standard does include a DELETE FILE option to do exactly
what you want.
```

###### ↳ ↳ ↳ Re: ok, heres one...

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-VbDrjolcc5HK@Dwight_Miller.iix.com>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com> <35EB1257.225DA5E2@IMN.nl> <6sf50k$6n8@dfw-ixnews10.ix.netcom.com>`

```
On Mon, 31 Aug 1998 21:33:29, "William M. Klein" 
<wmklein@ix.netcom.com> wrote:

> This seems to be my month to plug the new (draft) Standard.
>> 
…[3 more quoted lines elided]…
>

Are you sure that wasn't  in the last standard?  I've used this on a 
lot of compilers compliant with the '85 standard.  Even some not 
updated since 1991.
```

###### ↳ ↳ ↳ Re: ok, heres one...

_(reply depth: 4)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ef255f.0@news3.uswest.net>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com> <35EB1257.225DA5E2@IMN.nl> <6sf50k$6n8@dfw-ixnews10.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-VbDrjolcc5HK@Dwight_Miller.iix.com>`

```
Thane,

Vendors, anxious to improve their products, often put into their compiler
anything they think might make it into the next standard.


Thane Hubbell wrote in message ...
>On Mon, 31 Aug 1998 21:33:29, "William M. Klein"
><wmklein@ix.netcom.com> wrote:
…[12 more quoted lines elided]…
>
```

##### ↳ ↳ Re: ok, heres one...

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EB6FF0.71A3E4B1@att.net>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com> <35EB1257.225DA5E2@IMN.nl>`

```
COBOL Frog (Huib Klink) wrote:
> 
> Mike Ganas wrote:
…[14 more quoted lines elided]…
> mentioned in his reply post.

Now that I'm thinking about this, one could delete files from a COBOL by
building IDCAMS control statements & CALLing IDCAMS (pointing to the
control statements, of course). CALLing IEFBR14 would *not* have the
same effect <g>

Bill Lynch
```

##### ↳ ↳ Re: ok, heres one...

- **From:** "Dennis J. Minette" <dennis_minette@email.msn.com>
- **Date:** 1998-09-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ulN6twh39GA.277@upnetnews03>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com> <35EB1257.225DA5E2@IMN.nl>`

```

COBOL Frog (Huib Klink) wrote in message <35EB1257.225DA5E2@IMN.nl>...
>Mike Ganas wrote:
>
…[14 more quoted lines elided]…
>On PC's with DOS/WinX you could call (via command.com f.e.) some batch
file.
>From Micro Focus I know that they have some special routines provided, like
>CBL_CHECK_FILE_EXIT, CBL_DELETE_FILE, CBL_RENAME_FILE (and for DIR's as
…[6 more quoted lines elided]…
>DELETE record statements.


A redesign to use an ISAM file to hold the estimate records, using entry
date as an alternate key, sounds like a more efficient way to go.  The
original proposition sounds like the process would require a daily deletion
of "estimates" files, namely those 15 (business?) days old, whose names
incorporate a date reference (or whose names are maintained in another file
keyed by date.)
```

#### ↳ Re: ok, heres one...

- **From:** Paul_Knudsen@ibm.net (Paul Knudsen)
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ea00e1.29451084@news-s01.ny.us.ibm.net>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com>`

```
Why have all those little files?  Keep all the estimates in one
master.  At the end of each day process the whole file deleting the
records more than 15 days old.  Then back it up.

On Sun, 30 Aug 1998 19:06:47 -0700, Mike Ganas
<skidmike@mindspring.com> wrote:

>back to the muffler shop system.  we want to keep estimates on file in
>hopes that the customer comes back.  but the estimates need to be
…[3 more quoted lines elided]…
>well?
```

##### ↳ ↳ Re: ok, heres one...

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-3p7XTWN69lGz@Dwight_Miller.iix.com>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com> <35ea00e1.29451084@news-s01.ny.us.ibm.net>`

```
On Mon, 31 Aug 1998 01:51:22, Paul_Knudsen@ibm.net (Paul Knudsen) 
wrote:

> 
> >back to the muffler shop system.  we want to keep estimates on file in
…[4 more quoted lines elided]…
> >well?

I missed the original post, 

But you can do a 

DELETE FILE File-Name 

where File-Name is the name of the file defined in the FD.
```

#### ↳ Re: ok, heres one...

- **From:** Lookin'@You.2 (WDS)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35f872b9.6016704@news1.frb.gov>`
- **References:** `<35EA0537.9A5E33D5@mindspring.com>`

```
On Sun, 30 Aug 1998 19:06:47 -0700, Mike Ganas
<skidmike@mindspring.com> wrote:

>[...]how do
>you delete a file totally from cobol?  i can open output it and then
>close it, but that leaves the filename in the directory.
>well?

This is implementation specific.  I have seen such things as:
    CLOSE file-name WITH PURGE,
    CLOSE file-name WITH DELETE, and
    CLOSE file-name FOR REMOVAL,
all of which either violate the standard or are extensions.  Check
your COBOL manual to see what feature, if any, is implemented for your
compiler.  Also see if you can send a command to the operating system
(such as a DEL command in DOS) from your COBOL program.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
