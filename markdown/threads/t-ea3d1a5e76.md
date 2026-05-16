[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBSW

_16 messages · 10 participants · 2002-12_

---

### COBSW

- **From:** dcantua@co.la.ca.us (Daniel G. Cantua)
- **Date:** 2002-12-05T14:38:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6cca870b.0212051438.630564cc@posting.google.com>`

```
Can anyone help me? I have Some OS/2 workstations using MicroFocus
Cobol v3.4 and Windows2000 workstations using MicroFocus NetExpress
3.1.  The program open one of the files with lock.  Sometimes this
cause the system to hang.  We think this is a locking problem and we
are going to tried to set the COBSW to '+R+L1+B'.  We are hoping that
this will solve our problem.  if this does not work can anyone suggest
what else we can try?
```

#### ↳ Re: COBSW

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-12-06T01:28:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com>`

```
On Thu, 5 Dec 2002 22:38:18 UTC, dcantua@co.la.ca.us (Daniel G. 
Cantua) wrote:

> Can anyone help me? I have Some OS/2 workstations using MicroFocus
> Cobol v3.4 and Windows2000 workstations using MicroFocus NetExpress
…[4 more quoted lines elided]…
> what else we can try?

Are you using a "no timeout wait" for a lock, that will cause a hang 
if the lock is not released. You might also want to check to see if 
the Windows "escalated locking" is causing problems between the two 
types of machines.

Are the files resident on the OS/2 box or the Windows box?
```

##### ↳ ↳ Re: COBSW

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-12-06T06:01:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net>`

```

<lsunley@mb.sympatico.ca> wrote in message
news:ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net...
> On Thu, 5 Dec 2002 22:38:18 UTC, dcantua@co.la.ca.us (Daniel G.
> Cantua) wrote:
…[17 more quoted lines elided]…
> Lorne Sunley

    In Net Express there is a lock_mode tuneable, with 3 choices.

0 = compatable with MicroFocus v3.1 and earlier  (Older 16 bit product)

1 (default) = compatable with dos and os2

2 = interlanguage.  Locks physical record.

    I have no idea if 0 or 2 would improve matters.  Perhaps
someone out there knows?
```

###### ↳ ↳ ↳ Re: COBSW

- **From:** dcantua@co.la.ca.us (Daniel G. Cantua)
- **Date:** 2002-12-06T06:13:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6cca870b.0212060613.f802357@posting.google.com>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net>`

```
"Russell Styles" <RWSTYLES@worldnet.att.net> wrote in message news:<T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net>...
> <lsunley@mb.sympatico.ca> wrote in message
> news:ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net...
…[30 more quoted lines elided]…
> someone out there knows?

When we read the file we are only reading it with Lock.  How would you
change the time-out wait?  And the files resident on a Novell File
Server 5.1.  All the files are marked as Sharable.

How do you set the lock_mode tuneables?  Do you use COBSW to set them?

Thank you for your help so far.
```

###### ↳ ↳ ↳ Re: COBSW

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-07T09:01:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF1B903.D7A3AFE@Azonic.co.nz>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com>`

```
Daniel G. Cantua wrote:
> 
> > > > 3.1.  The program open one of the files with lock. 

> >     In Net Express there is a lock_mode tuneable, with 3 choices.
> 
> When we read the file we are only reading it with Lock.  How would you
> change the time-out wait?  And the files resident on a Novell File
> Server 5.1.  All the files are marked as Sharable.

Originally you stated you were 'open .. with lock'.  This is equivalent
to 'lock mode exclusive' and makes the file available to one user at a
time.

I suspect that the lock_mode is inappropriate to exclusive access.

A 'read with lock' is incompatible (or at least unrequired) with 'open
with lock'.

You probably need to be a little more explicit about the actual file
operations:

   Have you specified a file status ?
   Do you use the RM compiler directive ?
   Is run time switch +R on ?
   What are the settings of B and B1 switches ?
```

###### ↳ ↳ ↳ Re: COBSW

_(reply depth: 5)_

- **From:** dcantua@co.la.ca.us (Daniel G. Cantua)
- **Date:** 2002-12-10T11:57:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6cca870b.0212101157.6d78a206@posting.google.com>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<3DF1B903.D7A3AFE@Azonic.co.nz>...
> Daniel G. Cantua wrote:
> > 
…[23 more quoted lines elided]…
>    What are the settings of B and B1 switches ?

We do not use 'open with lock' but we do use 'read with lock'.  While
we are update a particular record we do not want anyone else to access
that record.  They can still access the rest of the file.

In our program, when we hit a file status of record lock it is
skipped.

I do not know what you mead by 'Do you use the RM compiler directive
?'  We compile with the command line command.

We are now trying 'SET COBSW=+R+L1+B'.  We are hoping that the this
setting will stop the system from halting.

Daniel G. Cantua
Los Angeles County - ISD
```

###### ↳ ↳ ↳ Re: COBSW

_(reply depth: 6)_

- **From:** t.goepfert@web.de (Torsten)
- **Date:** 2002-12-13T03:07:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a01384d.0212130307.7dae440b@posting.google.com>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com>`

```
Hi Daniel,

you said '...system hangs...' Perhaps it's a simple mistake in your
code. But for myself i can give you only tips with 'manual locking'
not 'automatic locking'. I don't use any COBSW parameters.

Sounds like a program wants to read an already locked record and is
going into a loop until the file status is zero. So if the reading
program is the problem, it depends on the type of reading. If it's
reading sequential there's no chance to get the locked record, but you
can skip it with a 'start greater' statement. If the program is NOT
reading sequential and NOT with lock you can ignore the file status,
you will get the locked record anyway.

Look at the 'update program': If you 'read with lock' and update the
record, after that you have to release it with 'unlock file'.

Regards, Torsten
```

###### ↳ ↳ ↳ Re: COBSW

_(reply depth: 7)_

- **From:** dcantua@co.la.ca.us (Daniel G. Cantua)
- **Date:** 2002-12-13T15:08:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6cca870b.0212131508.52f0b234@posting.google.com>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com>`

```
t.goepfert@web.de (Torsten) wrote in message news:<7a01384d.0212130307.7dae440b@posting.google.com>...
> Hi Daniel,
> 
…[15 more quoted lines elided]…
> Regards, Torsten

Thanks Torsten for your response.  But when ever the program detects
that the record is locked, it display a message on the screen saying
that the record is locked, and goes to the next record.  This is the
way we coded the programs.  On a strictly OS/2 environment this is
what happens.  We only have the problem when we have a mix of OS/2 and
WindowsNt/2000.

Daniel G. Cantua
Los Angeles County - ISD
```

###### ↳ ↳ ↳ Get rid of those Windows machines and users!

_(reply depth: 8)_

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2002-12-13T15:53:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFA730D.A09F78F7@attglobal.net>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com> <6cca870b.0212131508.52f0b234@posting.google.com>`

```
OS/2 is what everyone should be using.

(Actually, it is what I use, as much as possible.)

Hope you find your answer.
```

###### ↳ ↳ ↳ Re: Get rid of those Windows machines and users!

_(reply depth: 9)_

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2002-12-13T18:46:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DFA9B87.2C4@paralynx.com>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com> <6cca870b.0212131508.52f0b234@posting.google.com> <3DFA730D.A09F78F7@attglobal.net>`

```
Colin Campbell wrote:
> 
> OS/2 is what everyone should be using.
> 

My calendar must have gone wrong.  Is it 1992 again?  I'll have to look for the little 
black OS/2 pin that IBM gave me.  

Wait ...  I think I put it with my "VM Bigot" pin.
```

###### ↳ ↳ ↳ Re: Get rid of those Windows machines and users!

_(reply depth: 9)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-12-14T04:08:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-nSyMViNMOzNZ@h24-82-204-17.wp.shawcable.net>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com> <6cca870b.0212131508.52f0b234@posting.google.com> <3DFA730D.A09F78F7@attglobal.net>`

```
On Fri, 13 Dec 2002 23:53:49 UTC, Colin Campbell 
<cmcampb@attglobal.net> wrote:

> OS/2 is what everyone should be using.
> 
…[3 more quoted lines elided]…
> 

I'll second that - OS/2 is the OS I use 95% of the time

Far more stable for shared files using products like MF COBOL
```

###### ↳ ↳ ↳ Re: Get rid of those Windows machines and users!

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-12-16T15:27:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atkrct$94c$1@peabody.colorado.edu>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com> <6cca870b.0212131508.52f0b234@posting.google.com> <3DFA730D.A09F78F7@attglobal.net>`

```

On 13-Dec-2002, Colin Campbell <cmcampb@attglobal.net> wrote:

> OS/2 is what everyone should be using.
>
> (Actually, it is what I use, as much as possible.)
>
> Hope you find your answer.

Too bad it's on IBM's list of products it will drop support for this Spring.
```

###### ↳ ↳ ↳ Re: Get rid of those Windows machines and users!

_(reply depth: 10)_

- **From:** "Walter Willis" <wwillis1@qwest.net>
- **Date:** 2002-12-16T11:47:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dfe1143$0$221$45beb828@newscene.com>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com> <6cca870b.0212131508.52f0b234@posting.google.com> <3DFA730D.A09F78F7@attglobal.net> <atkrct$94c$1@peabody.colorado.edu>`

```
I'm surprised it's still around.  If there had been adequate software
products for the platform it might have had a chance.  But it never had the
reasonably priced or generally useful software that Windows has.  Most
software for OS/2 was rather specialized.  The last job I had prior to this
one used OS/2 for only two reasons - we were using MF Cobol and Intersolv's
APS (Intersolv has been purchased by MF and then by whomever purchased MF).
The pain was switching between windows and OS/2 all the time because we had
software that only ran in windows.

Walter
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:atkrct$94c$1@peabody.colorado.edu...
>
> On 13-Dec-2002, Colin Campbell <cmcampb@attglobal.net> wrote:
…[7 more quoted lines elided]…
> Too bad it's on IBM's list of products it will drop support for this
Spring.
```

###### ↳ ↳ ↳ Re: Get rid of those Windows machines and users!

_(reply depth: 10)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-12-17T01:53:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-uKoq1zdvtokd@h24-82-204-17.wp.shawcable.net>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com> <6cca870b.0212131508.52f0b234@posting.google.com> <3DFA730D.A09F78F7@attglobal.net> <atkrct$94c$1@peabody.colorado.edu>`

```
On Mon, 16 Dec 2002 15:27:13 UTC, "Howard Brazee" 
<howard.brazee@cusys.edu> wrote:

> 
> On 13-Dec-2002, Colin Campbell <cmcampb@attglobal.net> wrote:
…[7 more quoted lines elided]…
> Too bad it's on IBM's list of products it will drop support for this Spring.

There is a replacement product for OS/2. Serenity Systems has an OEM 
packaging of the OS/2 OS with additional applications and 
enhancements. Their package is not affected by IBM's withdrawal of the
OS/2 shrink wrap products.

See <http://www.ecomstation.com> The 1.1 version of the package will 
probably be released sometime in the next month or two... I have a 
machine running the eComStation OS and it works very well. If you have
a need to run Windows apps you can buy Connectix from Innotek 
<http://www.innotek.de> or a special packaging of Connectix from 
eComStation that will allow you to run a virtual machine for Linux 
and/or Windows etc.
```

###### ↳ ↳ ↳ Re: Get rid of those Windows machines and users!

_(reply depth: 10)_

- **From:** madodel@ptdprolog.net (Mark Dodel)
- **Date:** 2002-12-17T20:57:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yRNWO1cJ1gUw-pn2-CeCKoUlsg2eH@localhost>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com> <6cca870b.0212131508.52f0b234@posting.google.com> <3DFA730D.A09F78F7@attglobal.net> <atkrct$94c$1@peabody.colorado.edu>`

```
On Mon, 16 Dec 2002 15:27:13 UTC, "Howard Brazee" 
<howard.brazee@cusys.edu> wrote the following: 2000 

-)
-)On 13-Dec-2002, Colin Campbell <cmcampb@attglobal.net> wrote:
-)
-)> OS/2 is what everyone should be using.
-)>
-)> (Actually, it is what I use, as much as possible.)
-)>
-)> Hope you find your answer.
-)
-)Too bad it's on IBM's list of products it will drop support for this Spring.

IBM is not dropping support for OS/2.  They announced the withdraw 
from marketing  as of March 12, 2003, all retail packages of OS/2 Warp
4 and Warp Server eBusiness.  These products will be supported through
December 31, 2004.

Because so many large customers can't find a usable replacement for 
OS/2, many have signed TCO (Total Contant Ownership) contracts that 
extend support for over a decade more.  Serenity Systems has an OEM 
version of OS/2 called eComStation - http://www.ecomstation.com  IBM's
deadending the retail OS/2 has no effect on any of these.



Mark
```

###### ↳ ↳ ↳ Re: COBSW

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-16T12:02:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212161202.6889f68f@posting.google.com>`
- **References:** `<6cca870b.0212051438.630564cc@posting.google.com> <ZpzG4UNLyRNq-pn2-4BRfF73Qi4sb@h24-82-204-17.wp.shawcable.net> <T2XH9.40334$vM1.3175035@bgtnsc04-news.ops.worldnet.att.net> <6cca870b.0212060613.f802357@posting.google.com> <3DF1B903.D7A3AFE@Azonic.co.nz> <6cca870b.0212101157.6d78a206@posting.google.com> <7a01384d.0212130307.7dae440b@posting.google.com> <6cca870b.0212131508.52f0b234@posting.google.com>`

```
dcantua@co.la.ca.us (Daniel G. Cantua) wrote

> We only have the problem when we have a mix of OS/2 and
> WindowsNt/2000.

The solution is obvious.  Alternately have you tried it on Linux ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
