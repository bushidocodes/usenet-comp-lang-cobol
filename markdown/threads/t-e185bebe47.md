[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Fileshare - best platform?

_9 messages · 7 participants · 2000-03_

---

### MF Fileshare - best platform?

- **From:** "Charles Goodman" <cgoodman@mbnet.mb.ca>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com>`

```
We are about to implement a system with 30 ISAM files and 100 concurrent
users.  Netexpress, character interface is being used with Win98 PC's.
Should I use Fileshare on an NT server or on a UNIX server or simply on
WIN98 PC?  What are the advantages/disadvantages of each?
```

#### ↳ Re: MF Fileshare - best platform?

- **From:** "Costas Giannoulis" <diavasi@otenet.gr>
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aqbtc$ahe$1@newssrv.otenet.gr>`
- **References:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com>`

```
Hi Charlie,

I am using fileshare for some time and i can tell you the following :

*> DO NOT USE FileShare under Novell NetWare (ver 4.11 or previous),
especially with SFT-III, if the speed is critical for you.

*> Under NT works fine. I have not tested under UNIX.

*> FileShare provides an efficient transaction mechanism (commit, rollback)
and if you write some clever code (i suggest you use some oocobol) you can
write your own database rules. Example : when you want to delete a customer
then delete automatically his detail records and if something goes wrong
upon a delete then rollback the whole transaction.

*> If you  use FS  on a stand alone  Win98 PC, you will not see any
improvement on the file access speed.

*> You cannot use at the same time FileShare and ExtFH.

*> Read carefully the instructions about recovery. There are some
limitations.

Have a nice R&D (research and development)

Costas Giannoulis (diavasi@otenet.gr)


Charles Goodman <cgoodman@mbnet.mb.ca> wrote in message
news:mBCz4.16668$a27.264141@news1.rdc1.mb.home.com...
> We are about to implement a system with 30 ISAM files and 100 concurrent
> users.  Netexpress, character interface is being used with Win98 PC's.
…[8 more quoted lines elided]…
>
```

#### ↳ Re: MF Fileshare - best platform?

- **From:** "Projetos Especiais - Gilberto Junior" <projrev2@osite.com.br>
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aqent$qtj$1@news.mandic.com.br>`
- **References:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com>`

```
Hi Goodman,

don't use fileshare of the microfocus. He has many bug.

Think of using a RDMS SQL

Example SQL Server or Oracle.


Regards

Gilberto Junior





Charles Goodman <cgoodman@mbnet.mb.ca> wrote in message
news:mBCz4.16668$a27.264141@news1.rdc1.mb.home.com...
> We are about to implement a system with 30 ISAM files and 100 concurrent
> users.  Netexpress, character interface is being used with Win98 PC's.
…[8 more quoted lines elided]…
>
```

#### ↳ Re: MF Fileshare - best platform?

- **From:** "Greg Condon" <nospam@me.thanks>
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IgbA4.3981$eh.507991@news.bc.tac.net>`
- **References:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com>`

```
Hi Charles -

It sounds like you have already decided on your architecture, i.e. ISAM
files on a DOS filesystem.

In this environment, ISAM files are prone to being corrupted.

The very first thing I would recommend you do is create some COBOL test
programs to exercise your ISAM files, network and file server.  While these
simulations are running on about a dozen or so PCs see if your files hang
together.  Next try rebooting or crashing one or two PCs running the
simulation and see what happens.  If you start getting file corruption then
you know in your heart this ain't gonna cut it in a production environment.
Wtih 100 users I can guarantee at least one crash/reboot a day, especially
on Win9x systems.

_If_ you agree with my line of thinking so far, now you have more options...

You could try going with Fileshare, but I haven't heard of any successful
large-scale Fileshare installations.  Someone feel free to pipe in here.
The downside with Fileshare is that it is slower that normal ISAM I-O up to
a certain number of users.  I don't know where the threshold is.  Please
note that I am not bashing Fileshare.  I don't have direct experience with
it.  It may work perfectly in your situation but I would make sure I heard
from at least one or two users who said they have it working 100% in an
environment similar to yours.

If you don't want to use Fileshare, then my next suggestion would be to look
at using a UNIX server to host your application completely and run ANSI
terminal emulation over the network.  I think there is even support in
NetExpress to port your product over to UNIX.  You would have to purchase a
UNIX compiler as well.  In this situation you would expect to see your file
I/O be easily 10 to 100 times faster, and general application performance
would improve greatly.  This assumes you have some sort of UNIX expertise.
SCO OpenServer works just fine in this environment.  You could go with
UnixWare 7, it's newer, but it depends how bleeding-edge you want to be.  I
am currently working with a client that has over 150 concurrent users no
problem on SCO OpenServer.  This is on an old Compaq Pentium Pro MP server.

The most radical option would be to skip ISAM altogether and go with an NT
database instead of using ISAM.  The bonus here is that you can use a lot of
third-party tools via ODBC/OLE DB/ADO to get at your data, let users do
custom reports, etc...

So there ya go, one user's perspective on file I/O.  FYI I have been dealing
with MF COBOL on DOS/Novell/NT/UNIX for over 10 years.  Flame away...  :^)


 - Greg (wearing asbestos suit)




"Charles Goodman" <cgoodman@mbnet.mb.ca> wrote in message
news:mBCz4.16668$a27.264141@news1.rdc1.mb.home.com...
> We are about to implement a system with 30 ISAM files and 100 concurrent
> users.  Netexpress, character interface is being used with Win98 PC's.
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: MF Fileshare - best platform?

- **From:** "Charles Goodman" <cgoodman@mbnet.mb.ca>
- **Date:** 2000-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g5nA4.17771$a27.272665@news1.rdc1.mb.home.com>`
- **References:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com> <IgbA4.3981$eh.507991@news.bc.tac.net>`

```
Greg,

I fully agree that native ISAM will NOT work.  My real question is about
Fileshare.  Is it better to have the Fileshare server hosted under NT or
UNIX?

If I was to stay with 100% character interface then UNIX with terminal
emulation is probably the 'best' solution.  I will need to be able to have
some GUI programs and must eventually integrate with PC based CTI.

"Greg Condon" <nospam@me.thanks> wrote in message
news:IgbA4.3981$eh.507991@news.bc.tac.net...
> Hi Charles -
>
…[6 more quoted lines elided]…
> programs to exercise your ISAM files, network and file server.  While
these
> simulations are running on about a dozen or so PCs see if your files hang
> together.  Next try rebooting or crashing one or two PCs running the
> simulation and see what happens.  If you start getting file corruption
then
> you know in your heart this ain't gonna cut it in a production
environment.
> Wtih 100 users I can guarantee at least one crash/reboot a day, especially
> on Win9x systems.
>
> _If_ you agree with my line of thinking so far, now you have more
options...
>
> You could try going with Fileshare, but I haven't heard of any successful
> large-scale Fileshare installations.  Someone feel free to pipe in here.
> The downside with Fileshare is that it is slower that normal ISAM I-O up
to
> a certain number of users.  I don't know where the threshold is.  Please
> note that I am not bashing Fileshare.  I don't have direct experience with
…[4 more quoted lines elided]…
> If you don't want to use Fileshare, then my next suggestion would be to
look
> at using a UNIX server to host your application completely and run ANSI
> terminal emulation over the network.  I think there is even support in
> NetExpress to port your product over to UNIX.  You would have to purchase
a
> UNIX compiler as well.  In this situation you would expect to see your
file
> I/O be easily 10 to 100 times faster, and general application performance
> would improve greatly.  This assumes you have some sort of UNIX expertise.
> SCO OpenServer works just fine in this environment.  You could go with
> UnixWare 7, it's newer, but it depends how bleeding-edge you want to be.
I
> am currently working with a client that has over 150 concurrent users no
> problem on SCO OpenServer.  This is on an old Compaq Pentium Pro MP
server.
>
> The most radical option would be to skip ISAM altogether and go with an NT
> database instead of using ISAM.  The bonus here is that you can use a lot
of
> third-party tools via ODBC/OLE DB/ADO to get at your data, let users do
> custom reports, etc...
>
> So there ya go, one user's perspective on file I/O.  FYI I have been
dealing
> with MF COBOL on DOS/Novell/NT/UNIX for over 10 years.  Flame away...  :^)
>
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MF Fileshare - best platform?

- **From:** "RUSSELL STYLES" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b11m0$ah8$2@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com> <IgbA4.3981$eh.507991@news.bc.tac.net> <g5nA4.17771$a27.272665@news1.rdc1.mb.home.com>`

```
    Have you considered something other than Fileshare?

    Betreive can be used with no changes to the source code, just a
compiler option.  The engine is available on Netware and NT.  I have no idea
about Unix, and can not advise you on speed.

    The current version of Betrieve also supports SQL.


Charles Goodman <cgoodman@mbnet.mb.ca> wrote in message
news:g5nA4.17771$a27.272665@news1.rdc1.mb.home.com...
> Greg,
>
…[6 more quoted lines elided]…
> some GUI programs and must eventually integrate with PC based CTI.

<snip>
```

###### ↳ ↳ ↳ Re: MF Fileshare - best platform?

- **From:** "Greg Condon" <nospam@me.thanks>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ad%A4.4334$eh.556873@news.bc.tac.net>`
- **References:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com> <IgbA4.3981$eh.507991@news.bc.tac.net> <g5nA4.17771$a27.272665@news1.rdc1.mb.home.com>`

```
Hi again!

If you are thinking of going GUI sometime in the future, then perhaps you
should consider going with a client/server implementation NOW.  If you do
this, you can keep all your ISAM file I/O on one server.  MF has tools to
allow you to put Dialog on a client and the rest of the your application on
a server.

For grins, try running a file i/o bound process on a PC (such as an
invoicing run) with the files on an NT server, and the same process directly
on the NT server.  Notice a difference?  This is one of the bonuses of a
client/server setup.  It keeps the file i/o off the network.

I have seen client/server implementations on both NT and UNIX.  At my
largest client we have a custom-developed client/server system, all in MF
COBOL.  Thin GUI clients on Windows, server on UNIX.  On the same hardware a
UNIX server would be faster than NT, but if you don't have the UNIX
experience you can always throw extra $$ at the NT server - fast hardware
getting cheap these days!!

I would recommend sticking with well-travelled pieces of the MF product
line.  When you start going into Fileshare land or Btrieve land, you are
going into areas that I think only a small percentage of MF customers are
using.  Can you can't afford to be this gutsy?


Regards,

Greg


"Charles Goodman" <cgoodman@mbnet.mb.ca> wrote in message
news:g5nA4.17771$a27.272665@news1.rdc1.mb.home.com...
> Greg,
>
…[20 more quoted lines elided]…
> > simulations are running on about a dozen or so PCs see if your files
hang
> > together.  Next try rebooting or crashing one or two PCs running the
> > simulation and see what happens.  If you start getting file corruption
…[3 more quoted lines elided]…
> > Wtih 100 users I can guarantee at least one crash/reboot a day,
especially
> > on Win9x systems.
> >
…[3 more quoted lines elided]…
> > You could try going with Fileshare, but I haven't heard of any
successful
> > large-scale Fileshare installations.  Someone feel free to pipe in here.
> > The downside with Fileshare is that it is slower that normal ISAM I-O up
> to
> > a certain number of users.  I don't know where the threshold is.  Please
> > note that I am not bashing Fileshare.  I don't have direct experience
with
> > it.  It may work perfectly in your situation but I would make sure I
heard
> > from at least one or two users who said they have it working 100% in an
> > environment similar to yours.
…[5 more quoted lines elided]…
> > NetExpress to port your product over to UNIX.  You would have to
purchase
> a
> > UNIX compiler as well.  In this situation you would expect to see your
> file
> > I/O be easily 10 to 100 times faster, and general application
performance
> > would improve greatly.  This assumes you have some sort of UNIX
expertise.
> > SCO OpenServer works just fine in this environment.  You could go with
> > UnixWare 7, it's newer, but it depends how bleeding-edge you want to be.
…[5 more quoted lines elided]…
> > The most radical option would be to skip ISAM altogether and go with an
NT
> > database instead of using ISAM.  The bonus here is that you can use a
lot
> of
> > third-party tools via ODBC/OLE DB/ADO to get at your data, let users do
…[4 more quoted lines elided]…
> > with MF COBOL on DOS/Novell/NT/UNIX for over 10 years.  Flame away...
:^)
> >
> >
…[7 more quoted lines elided]…
> > > We are about to implement a system with 30 ISAM files and 100
concurrent
> > > users.  Netexpress, character interface is being used with Win98 PC's.
> > > Should I use Fileshare on an NT server or on a UNIX server or simply
on
> > > WIN98 PC?  What are the advantages/disadvantages of each?
> > >
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: MF Fileshare - best platform?

- **From:** "Joshua Seltzer" <jseltzer@larich.com>
- **Date:** 2000-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8D73F90F4ABEC59E.D4AFC20A712CB82A.5DF04E2AE8EB9F56@lp.airnews.net>`
- **References:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com> <IgbA4.3981$eh.507991@news.bc.tac.net> <g5nA4.17771$a27.272665@news1.rdc1.mb.home.com>`

```

We have been using Fileshare since last November in a multi site Point Of
Sale System.  The main application runs on a centrally located SCO UNIX
application Server with Fileshare running on another SCO UNIX server.  There
are about 50 thin clients in our stores running SCO Embedded UNIX  connected
over a 64K WAN.  The Clients use Telnet to run the main application and also
run several opening and closing programs locally and access their files via
Fileshare over the WAN.

Compared to Windows NT apps we use in out main office the MF COBOL /
Fileshare combination have been fairly reliable and effective.  Our old
pre-y2k POS used MF and Btrieve as ISAM was not so reliable on DOS.  On UNIX
the  C-ISAM file system is fast and fairly reliable.  This is helped by SCO
UNIX (and AIX used in put back office system) have journaled file systems
which tend to protect files in case of a system crash.

We have had 4 crashes on our Fileshare Server since November.  Three of the
crashes were Fileshare failing on TCP/IP issues.  MF Support pointed out we
that we were running on a version 2 rev levels back and suggested an
upgrade.  When the Fileshare server program dies files are not properly
closed and we had to run the rebuild utility to fix them. (It only took a
few min). I believe we hung TCP/IP port 86 as we were using client server
bindings to facilitate remote printing and the crashes coincided with the
port slowing down trying to print to a dead terminal.  Since we moved to a
different method or print control and no longer use client server bindings
the Fileshare Server itself has not crashed.  We did have the SCO server
itself crash last month, but after a reboot all was well, no files needed a
rebuild.

If I were to consider using Fileshare on a larger mission critical project I
would recommend using an IBM RS/6000 or SUN server simply because of
stability/speed issues vs. SCO (or LINUX) on an x86 based system.  We run
our back office MF COBOL apps on an RS/6000 59H which is an older slower
system and uses C-ISAM files and does NOT use Fileshare locally (but does
use Fileshare to access shared POS files on the SCO Server - you can mix
access).  Programs seem to run just about as fast as on a 450mz SCO box!

I hope this info helps.

Joshua Seltzer
Larich Distributors, Inc.
jseltzer@larich.com
```

###### ↳ ↳ ↳ Re: MF Fileshare - best platform?

_(reply depth: 4)_

- **From:** "Gerald Moull" <gerald@moull.freeserve.co.uk>
- **Date:** 2000-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b46m3$41v$1@newsg1.svr.pol.co.uk>`
- **References:** `<mBCz4.16668$a27.264141@news1.rdc1.mb.home.com> <IgbA4.3981$eh.507991@news.bc.tac.net> <g5nA4.17771$a27.272665@news1.rdc1.mb.home.com> <8D73F90F4ABEC59E.D4AFC20A712CB82A.5DF04E2AE8EB9F56@lp.airnews.net>`

```
From my experiences supporting RM/COBOL users with the RM/InfoExpress
product (Liant's equivalent of FileShare) the results have been fairly good.
The best example I found was a company in South Africa who started life
small on a SCO Unix bix and grew dramatically ending up with 100's of users.
Continually throwing more memory at the poor old Intel processor didn't help
much, nore did throwing in another processor (or 2).  In the end they
distributed the users over 3 SCO boxes and kept all the files on a central
SCO box with an RM/InfoExpress server installed.  This did the trick and
they were up and running again.  I think they have in the region of 400
users on SCO!

The DOS/Novell LAN environment can never be 100% secure (eliminate data
coruptions) and a Win98/WinNT situation appears to compond this (did anybody
on CLC suffer hours of headaches until the VRDUPDT patch from Microsoft for
Win95!!!!).  Although it won't improve performance a great deal on a LAN a
C/S filehandler such as FileShare or RM/InfoExpress (so long as it works)
will improve performance - if it goes down 4 times a year how many file
corruptions would you have had without it?  They also have other hidden
benefits such as the file system does not need to be visible to the users,
only the server process - they can't therefore go deleting those files!

Our experiences of BTrieve on Novell are that it is very stable and if you
used the hooks provides Transaction support.  We've just updated a system in
London that has been running since the dawn of life on BTrieve.  The system
was running on kit ranging from 486/33s downwards!  The server was
originally Novell 2 but had at some point been updated to 3 and was the type
that was completely clogged up with dust!  The only thing that they knew how
to do was turn the PCs on and use their system - which it did well enough
for them.  The only thing was the Tape drive broke about 6 milleniums ago
and they didn't take backups.  It was only through hardware luck and BTrieve
they didn't end up in big cacky!  We haven't had so much experience of
BTrieve on WinNT (Pervasive SQL), but it does appear to be a lot more
complicated and difficult to get going.

However if you stick to Unix you don't need to worry about these things
hardly at all.  Thankfully the industry is moving back to server centric
apps and there's great products in the COBOL industry which mean that that
server can just as easily be Unix even if you want the connectivity 'bells
and whistles' of WinNT (OK Win2000 if anybody is brave enough to put a
mission critical app of it yet!).

Gerald

PS As an aside to the BTrieve site - they've just installed all new Compaq
machines.  They were delivered with no power switch - now they can't turn
their PCs off at night because when Windows hangs on the 'windows is closing
down' message, the only way they can restart the PC is by physically pulling
the plug from the wall or the back of the PC and waiting for the loud bangs
and crackle!


Joshua Seltzer <jseltzer@larich.com> wrote in message
news:8D73F90F4ABEC59E.D4AFC20A712CB82A.5DF04E2AE8EB9F56@lp.airnews.net...
>
> We have been using Fileshare since last November in a multi site Point Of
> Sale System.  The main application runs on a centrally located SCO UNIX
> application Server with Fileshare running on another SCO UNIX server.
There
> are about 50 thin clients in our stores running SCO Embedded UNIX
connected
> over a 64K WAN.  The Clients use Telnet to run the main application and
also
> run several opening and closing programs locally and access their files
via
> Fileshare over the WAN.
>
> Compared to Windows NT apps we use in out main office the MF COBOL /
> Fileshare combination have been fairly reliable and effective.  Our old
> pre-y2k POS used MF and Btrieve as ISAM was not so reliable on DOS.  On
UNIX
> the  C-ISAM file system is fast and fairly reliable.  This is helped by
SCO
> UNIX (and AIX used in put back office system) have journaled file systems
> which tend to protect files in case of a system crash.
>
> We have had 4 crashes on our Fileshare Server since November.  Three of
the
> crashes were Fileshare failing on TCP/IP issues.  MF Support pointed out
we
> that we were running on a version 2 rev levels back and suggested an
> upgrade.  When the Fileshare server program dies files are not properly
…[6 more quoted lines elided]…
> itself crash last month, but after a reboot all was well, no files needed
a
> rebuild.
>
> If I were to consider using Fileshare on a larger mission critical project
I
> would recommend using an IBM RS/6000 or SUN server simply because of
> stability/speed issues vs. SCO (or LINUX) on an x86 based system.  We run
…[11 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
