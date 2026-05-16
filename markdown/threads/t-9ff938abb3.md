[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# comunications

_10 messages · 7 participants · 1999-02 → 1999-03_

---

### comunications

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b6d6f$mir$1@news.igs.net>`

```
This is not a Cobol problem, but maybe some people in here can
help anyway.

I have a flat ASCII file, (Cobol produced, no binary) that I have to
move from one PC to another.  The existing system does it using
ProComm scripts under DOS, then shells, and runs a program (also
Cobol) that merges it with a master input file.  Data is received from
several locations.  This is very low volume stuff, and only done once
per day, but it has to be done over a modem, and it must be completely
automatic.

It will not work under windows, even in a DOS box.  I would like to
replace it in the simplest way possible.  I thought of using dial in
networking, and a batch file, but I cannot seem to find any way for
windows95 to answer the phone.  Does anybody have a simple
solution?
```

#### ↳ Re: comunications

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HEzB2.3$gY4.9@news19.ispnews.com>`
- **References:** `<7b6d6f$mir$1@news.igs.net>`

```

Donald Tees wrote in message <7b6d6f$mir$1@news.igs.net>...
>This is not a Cobol problem, but maybe some people in here can
>help anyway.
…[9 more quoted lines elided]…
>It will not work under windows, even in a DOS box.

I assume you mean the ProComm scripts will not work.

>  I would like to
>replace it in the simplest way possible.  I thought of using dial in
…[3 more quoted lines elided]…
>
Use VB 5 (or 6). Communications is fairly straight forward (no API
calls necessary) and it can launch the COBOL program (DOS or
Windows) when the file(s) have been successfully transferred.

Place the program in the StartUp folder.

The downside is that the Com Port will not be available for any
other applications.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

#### ↳ Re: comunications

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b6gvt$5nn@lotho.delphi.com>`
- **References:** `<7b6d6f$mir$1@news.igs.net>`

```

Well, you have several options actually. The simplest option 
may be to simply use NT at your central site, and let all the 
remote machines dial into it. (The NT machine supports remote
dial in very easily.)  

You can then just have a batch file on the remote systems that
copies the datafiles to a 'hot folder' on the NT system. 
(literraly - 
  copy c:\mylocalfile //name-of-nt-server/shared-folder/filename)
)

Or you can get sophisticated and use something like NDm (Connect
Direct), or you can get slick and write a C or VB program that
opens a socket and accepts the information directly. 

I recommend *against* doing this out of COBOL, though there 
are many PC COBOL implementations that can do this. The reason is
that I don' trust PC COBOL's to keep up in the Windows / NT world,
but almost all the C compilers will, and VB is very good for 
doing things like this. (Gee- it comes out to something like 
15 or 20 lines of code... just the right size for a BASIC program. :) 

But the key to all of that working very simply is just to use NT
as your server. (You could use OS/2, but probably not politically
viable. :) Heck, you can even use secure / non secure internet 
connections with the NT machine at that point. Just make sure it
has a nice stable internet address...

-Paul


Donald Tees (donald@willmack.com) wrote:
: This is not a Cobol problem, but maybe some people in here can
: help anyway.

: I have a flat ASCII file, (Cobol produced, no binary) that I have to
: move from one PC to another.  The existing system does it using
: ProComm scripts under DOS, then shells, and runs a program (also
: Cobol) that merges it with a master input file.  Data is received from
: several locations.  This is very low volume stuff, and only done once
: per day, but it has to be done over a modem, and it must be completely
: automatic.

: It will not work under windows, even in a DOS box.  I would like to
: replace it in the simplest way possible.  I thought of using dial in
: networking, and a batch file, but I cannot seem to find any way for
: windows95 to answer the phone.  Does anybody have a simple
: solution?
```

##### ↳ ↳ Re: comunications

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b6p80$s4m@lotho.delphi.com>`
- **References:** `<7b6d6f$mir$1@news.igs.net> <7b6gvt$5nn@lotho.delphi.com>`

```
Oh, and I forgot, you can do dial in networking with Windows 95,
but the software to do it is on the Microsoft PLUS disk for Windows
95. Again, NT Workstation is probably your best bet here....

paulr (paulr@bix.com) wrote:

: Well, you have several options actually. The simplest option 
: may be to simply use NT at your central site, and let all the 
: remote machines dial into it. (The NT machine supports remote
: dial in very easily.)  

: You can then just have a batch file on the remote systems that
: copies the datafiles to a 'hot folder' on the NT system. 
: (literraly - 
:   copy c:\mylocalfile //name-of-nt-server/shared-folder/filename)
: )

: Or you can get sophisticated and use something like NDm (Connect
: Direct), or you can get slick and write a C or VB program that
: opens a socket and accepts the information directly. 

: I recommend *against* doing this out of COBOL, though there 
: are many PC COBOL implementations that can do this. The reason is
: that I don' trust PC COBOL's to keep up in the Windows / NT world,
: but almost all the C compilers will, and VB is very good for 
: doing things like this. (Gee- it comes out to something like 
: 15 or 20 lines of code... just the right size for a BASIC program. :) 

: But the key to all of that working very simply is just to use NT
: as your server. (You could use OS/2, but probably not politically
: viable. :) Heck, you can even use secure / non secure internet 
: connections with the NT machine at that point. Just make sure it
: has a nice stable internet address...

: -Paul


: Donald Tees (donald@willmack.com) wrote:
: : This is not a Cobol problem, but maybe some people in here can
: : help anyway.

: : I have a flat ASCII file, (Cobol produced, no binary) that I have to
: : move from one PC to another.  The existing system does it using
: : ProComm scripts under DOS, then shells, and runs a program (also
: : Cobol) that merges it with a master input file.  Data is received from
: : several locations.  This is very low volume stuff, and only done once
: : per day, but it has to be done over a modem, and it must be completely
: : automatic.

: : It will not work under windows, even in a DOS box.  I would like to
: : replace it in the simplest way possible.  I thought of using dial in
: : networking, and a batch file, but I cannot seem to find any way for
: : windows95 to answer the phone.  Does anybody have a simple
: : solution?
```

##### ↳ ↳ Re: comunications

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-02-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bd7nm$1dq$1@birch.prod.itd.earthlink.net>`
- **References:** `<7b6d6f$mir$1@news.igs.net> <7b6gvt$5nn@lotho.delphi.com>`

```

paulr wrote in message <7b6gvt$5nn@lotho.delphi.com>...
>

>I recommend *against* doing this out of COBOL, though there
>are many PC COBOL implementations that can do this. The reason is
…[4 more quoted lines elided]…
>

I just attended a class where one of the topics was Converting
Legacy C++ Programs to Cobol.

"Don't trust PC COBOL's to keep up ..." indeed. Sniff.
```

#### ↳ Re: comunications

- **From:** "Ramon Gonzalez" <kp4tr@leading.net>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b86hr$t4p@news2.southeast.net>`
- **References:** `<7b6d6f$mir$1@news.igs.net>`

```
I can suggest innumerable methods of capturing this file, but Ill suggest
this:

1. Disable the MODEM/COM port from Win 95 and let PROCOMM for DOS talk
directly to the MODEM/COM port. Procomm for DOS wants to talk directly to
the MODEM/COM port, not thru Win 95 drivers.
2. Get Procomm Plus for Windows and migrate your ASPECT scripts.
3. Get a cheap 486 PC, install DOS, and dedicate this PC for this job. Have
this PC connect thru a newtork card (Novell or LAN Manager) to the PC where
you will do your file crunching.

A more sophisticated way is to install Linux and use (PPP) to establish a
TCP/IP connection, then FTP your files to Linux, and use SAMBA between Linux
and Win 95 over a network.


Donald Tees wrote in message <7b6d6f$mir$1@news.igs.net>...
>This is not a Cobol problem, but maybe some people in here can
>help anyway.
…[16 more quoted lines elided]…
>
```

#### ↳ Re: comunications

- **From:** "Ramon Gonzalez" <kp4tr@leading.net>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b86ki$t4s@news2.southeast.net>`
- **References:** `<7b6d6f$mir$1@news.igs.net>`

```
I can suggest innumerable methods of capturing this file, but Ill suggest
this:

1. Disable the MODEM/COM port from Win 95 and let PROCOMM for DOS talk
directly to the MODEM/COM port. Procomm for DOS wants to talk directly to
the MODEM/COM port, not thru Win 95 drivers.
2. Get Procomm Plus for Windows and migrate your ASPECT scripts.
3. Get a cheap 486 PC, install DOS, and dedicate this PC for this job. Have
this PC connect thru a newtork card (Novell or LAN Manager) to the PC where
you will do your file crunching.

A more sophisticated way is to install Linux and use (PPP) to establish a
TCP/IP connection, then FTP your files to Linux, and use SAMBA between Linux
and Win 95 over a network.


Donald Tees wrote in message <7b6d6f$mir$1@news.igs.net>...
>This is not a Cobol problem, but maybe some people in here can
>help anyway.
…[16 more quoted lines elided]…
>
```

#### ↳ Re: comunications

- **From:** "Ramon Gonzalez" <kp4tr@leading.net>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b86m2$t7o@news2.southeast.net>`
- **References:** `<7b6d6f$mir$1@news.igs.net>`

```
I can suggest innumerable methods of capturing this file, but Ill suggest
this:

1. Disable the MODEM/COM port from Win 95 and let PROCOMM for DOS talk
directly to the MODEM/COM port. Procomm for DOS wants to talk directly to
the MODEM/COM port, not thru Win 95 drivers.
2. Get Procomm Plus for Windows and migrate your ASPECT scripts.
3. Get a cheap 486 PC, install DOS, and dedicate this PC for this job. Have
this PC connect thru a newtork card (Novell or LAN Manager) to the PC where
you will do your file crunching.

A more sophisticated way is to install Linux and use (PPP) to establish a
TCP/IP connection, then FTP your files to Linux, and use SAMBA between Linux
and Win 95 over a network.


Donald Tees wrote in message <7b6d6f$mir$1@news.igs.net>...
>This is not a Cobol problem, but maybe some people in here can
>help anyway.
…[16 more quoted lines elided]…
>
```

#### ↳ Re: comunications

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 1999-03-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bedru$6t6g$1@newssvr03-int.news.prodigy.com>`
- **References:** `<7b6d6f$mir$1@news.igs.net>`

```
Don,

If you can get ahold of the Win95 Plus! pack, you can install dial up server
software from there.

Good Luck!

Denny
```

##### ↳ ↳ Re: comunications

- **From:** NoLonger@ix.netcom.com (OldUncleMe)
- **Date:** 1999-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36db31ea.34806268@news>`
- **References:** `<7b6d6f$mir$1@news.igs.net> <7bedru$6t6g$1@newssvr03-int.news.prodigy.com>`

```
It was: Mon, 1 Mar 1999 11:05:39 -0500 and with STARTLING insight,  ""Denny Brouse"
<denden@prodigy.net>" posted "Re: comunications" to "comp.lang.cobol" :

-->Don,
-->
-->If you can get ahold of the Win95 Plus! pack, you can install dial up server
-->software from there.

-->Good Luck!

-->Denny

I seem to recall that one of the DUN upgrades, probably to 1.2?, includes this functionality,
and it's free.  Assuming this is true, and that with some consistancy M$ has included all
previous upgrades in the newest version, could it be true then that DUN --> 1.3 upgrade would
have it too?  Info on this should be found at www.microsoft.com/blah. 


              tenox  @  home  dat   com
                                                                             /ts
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
