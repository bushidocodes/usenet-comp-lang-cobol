[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Microsoft 4.5 and Win200 Pro

_11 messages · 6 participants · 2003-07_

---

### Cobol Microsoft 4.5 and Win200 Pro

- **From:** "Mauro" <maspa31@hotmail.com>
- **Date:** 2003-07-13T11:18:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ber89n$3s2$1@newsread.albacom.net>`

```
Sorry for my bad english
I have any package write in Microsoft Cobol 4.5 and now I have a computer
with O.S. Win2000 Pro.
When I try to compile the old programs the system return me the message
"Cobol run time library not installed"
I have modifed the files AUTOEXEC.NT and CONFIG.NT with the parameters how I
do under Win98SE but the final result is that error:
"Cobol run time library not installed"
Sombody can help me?
Thanks
Mauro
```

#### ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-07-13T07:45:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rFbQa.19$eP6.18805@news20.bellglobal.com>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net>`

```
You are missing a file called cobol.dle, if my memory is correct.  This is a
*very* old compiler.

Donald

"Mauro" <maspa31@hotmail.com> wrote in message
news:ber89n$3s2$1@newsread.albacom.net...
> Sorry for my bad english
> I have any package write in Microsoft Cobol 4.5 and now I have a computer
…[3 more quoted lines elided]…
> I have modifed the files AUTOEXEC.NT and CONFIG.NT with the parameters how
I
> do under Win98SE but the final result is that error:
> "Cobol run time library not installed"
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

- **From:** "Mauro" <maspa31@hotmail.com>
- **Date:** 2003-07-13T16:21:20+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<berq1p$blb$1@newsread.albacom.net>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net> <rFbQa.19$eP6.18805@news20.bellglobal.com>`

```
The library file is coblib.dle and it is present in the correct path. I know
that this compiler is very old but I have any programs in cobol microsoft
for any customers with old computers.
Under Windows XP the same configuration run but don't run under Win2000 Pro.
Mauro


"Donald Tees" <Donald_Tees@sympatico.ca> ha scritto nel messaggio
news:rFbQa.19$eP6.18805@news20.bellglobal.com...
> You are missing a file called cobol.dle, if my memory is correct.  This is
a
> *very* old compiler.
>
…[5 more quoted lines elided]…
> > I have any package write in Microsoft Cobol 4.5 and now I have a
computer
> > with O.S. Win2000 Pro.
> > When I try to compile the old programs the system return me the message
> > "Cobol run time library not installed"
> > I have modifed the files AUTOEXEC.NT and CONFIG.NT with the parameters
how
> I
> > do under Win98SE but the final result is that error:
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-07-13T10:53:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qpeQa.129$ym.51832@news20.bellglobal.com>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net> <rFbQa.19$eP6.18805@news20.bellglobal.com> <berq1p$blb$1@newsread.albacom.net>`

```
"Mauro" <maspa31@hotmail.com> wrote in message
news:berq1p$blb$1@newsread.albacom.net...
> The library file is coblib.dle and it is present in the correct path. I
know
> that this compiler is very old but I have any programs in cobol microsoft
> for any customers with old computers.
> Under Windows XP the same configuration run but don't run under Win2000
Pro.
> Mauro

Then I'm tapped out ... the many times I've seen that message have always
been related to not finding that file. The code will probably compile under
a MicroFocus cobol compiler, as the MS compiler was really MF.

Donald

>
>
> "Donald Tees" <Donald_Tees@sympatico.ca> ha scritto nel messaggio
> news:rFbQa.19$eP6.18805@news20.bellglobal.com...
> > You are missing a file called cobol.dle, if my memory is correct.  This
is
> a
> > *very* old compiler.
…[9 more quoted lines elided]…
> > > When I try to compile the old programs the system return me the
message
> > > "Cobol run time library not installed"
> > > I have modifed the files AUTOEXEC.NT and CONFIG.NT with the parameters
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-07-13T15:20:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0307131303.77aa5c11@posting.google.com>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net> <rFbQa.19$eP6.18805@news20.bellglobal.com> <berq1p$blb$1@newsread.albacom.net>`

```
You don't do your customers any favors using a discontinued development tool.  

Time to upgrade.


"Mauro" <maspa31@hotmail.com> wrote in message news:<berq1p$blb$1@newsread.albacom.net>...
> The library file is coblib.dle and it is present in the correct path. I know
> that this compiler is very old but I have any programs in cobol microsoft
…[32 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-07-14T17:20:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beterj$e49$1@aklobs.kc.net.nz>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net> <rFbQa.19$eP6.18805@news20.bellglobal.com> <berq1p$blb$1@newsread.albacom.net> <bfdfc3e8.0307131303.77aa5c11@posting.google.com>`

```
Thane Hubbell wrote:

> You don't do your customers any favors using a discontinued development
> tool.

MS Cobol 4.5 is a stable, relatively error free version of '85.  If it 
doesn't have any support issues then why would one need support ?
 
> Time to upgrade.

>> ... for any customers with old computers.

Assuming that the 'old computer' is running, MS-DOS or Win95/98:

You are suggesting that he obtain a recent compiler.  This would probably 
require a more recent version of Windows to run the programs on - XP is the 
only one available, this would require a new computer as it is likely that 
an old computer has inadequate CPU, RAM and HD space.

So, after paying out several thousand dollars, exactly what benefits would 
arise for the customer ?

Perhaps it will spend 99.95% of the time waiting for keystrokes rather than 
the current 97%. 

Businesses are not there to be revenue sources for computer companies. 
Computers are for being tools.  If there is a _business_case_ for upgrading 
then make it.
```

###### ↳ ↳ ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

_(reply depth: 5)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-07-14T15:06:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0307141406.5b14a52d@posting.google.com>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net> <rFbQa.19$eP6.18805@news20.bellglobal.com> <berq1p$blb$1@newsread.albacom.net> <bfdfc3e8.0307131303.77aa5c11@posting.google.com> <beterj$e49$1@aklobs.kc.net.nz>`

```
Richard,

Since he stated he was running on Windows 2000 Professional, I stand
by my advice to acquire a modern and supported compiler.

Were he still on DOS with this customer - of course you would be
correct, but he's not.

Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<beterj$e49$1@aklobs.kc.net.nz>...
> Thane Hubbell wrote:
> 
…[25 more quoted lines elided]…
> then make it.
```

###### ↳ ↳ ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-07-14T18:41:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0307141741.754ebd99@posting.google.com>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net> <rFbQa.19$eP6.18805@news20.bellglobal.com> <berq1p$blb$1@newsread.albacom.net> <bfdfc3e8.0307131303.77aa5c11@posting.google.com> <beterj$e49$1@aklobs.kc.net.nz> <bfdfc3e8.0307141406.5b14a52d@posting.google.com>`

```
thaneh@softwaresimple.com (Thane Hubbell) wrote 

> Since he stated he was running on Windows 2000 Professional, I stand
> by my advice to acquire a modern and supported compiler.

There is a difference between where he is wanting to run the compiler
in order to compile versions of his programs, and the target machines
which are "for any customers with old computers".

> Were he still on DOS with this customer - of course you would be
> correct, but he's not.

We don't know what his customers are running on their old computers,
it may be DOS. It is not necessary to compile on the same machine as
the program is run on, in fact licence agreements for the MS Cobol
compiler will preclude installing it on customer machines.
```

###### ↳ ↳ ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

_(reply depth: 5)_

- **From:** "Russell Styles" <RWS0202@comcast.net>
- **Date:** 2003-07-16T00:30:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8zidnbBWFORLSYmiXTWJkw@comcast.com>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net> <rFbQa.19$eP6.18805@news20.bellglobal.com> <berq1p$blb$1@newsread.albacom.net> <bfdfc3e8.0307131303.77aa5c11@posting.google.com> <beterj$e49$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:beterj$e49$1@aklobs.kc.net.nz...
> Thane Hubbell wrote:
>
…[13 more quoted lines elided]…
> require a more recent version of Windows to run the programs on - XP is
the
> only one available, this would require a new computer as it is likely that
> an old computer has inadequate CPU, RAM and HD space.
…[4 more quoted lines elided]…
> Perhaps it will spend 99.95% of the time waiting for keystrokes rather
than
> the current 97%.
>
> Businesses are not there to be revenue sources for computer companies.
> Computers are for being tools.  If there is a _business_case_ for
upgrading
> then make it.
>

    The major business case for replacing something that works, i.e. MS-DOS
and
a 16 bit compiler, such as MS Cobol 4.5 or Microfocus ver 3.4 (workbench -
no relation
to net express) is Sales.

    Given a choice between a simple, fast, and reliable program on MS-DOS,
and a slow,
less than reliable program on windows, with a 32 bit compiler, buyers will
choose the
2cd choice almost every time.

    Never mind the fact that many a windows pc might need to be reformatted
and have windows
reinstalled every year or so, while a DOS pc can continue to run until the
government depreciation
runs out.  Or beyond.
```

#### ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-13T17:04:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f115d5e.72328442@news.optonline.com>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net>`

```
"Mauro" <maspa31@hotmail.com> wrote:

>I have any package write in Microsoft Cobol 4.5 and now I have a computer
>with O.S. Win2000 Pro.
…[5 more quoted lines elided]…
>Sombody can help me?

The problem is with COBDIR. Does it specify a full path, not just "SET
COBDIR=."?

It sounds like you are running under CMD.EXE. This is a 32-bit app, therefore
does not use AUTOEXEC.NT. 

The simplest solution is to create a shortcut using COMMAND.COM, which is a
16-bit app that does use AUTOEXEC.NT. The command, of course, is "COBRUN
yourprog". 

Alternatively, you could use the PIF editor to modify your PIF to specify
Options = \winnt\system32\AUTOEXEC.NT. 

Another alternative, start regedit, go to
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment,
add an entry for COBDIR.
```

#### ↳ Re: Cobol Microsoft 4.5 and Win200 Pro

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-07-14T07:51:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<besdg3$vm8$1@aklobs.kc.net.nz>`
- **References:** `<ber89n$3s2$1@newsread.albacom.net>`

```
Mauro wrote:

> Sorry for my bad english
> I have any package write in Microsoft Cobol 4.5 and now I have a computer
…[6 more quoted lines elided]…
> Sombody can help me?

The _actual_ problem is that MS Cobol 4.5 can compile and run programs for 
MS-DOS, Windows 3.x and OS/2 2.x.  Windows NT and 2000 (but not XP) has an 
OS/2 'personality'.

When you try to run a program the Cobol notices that there are several 
environments available and tries to use the 'best' one - OS/2 in protected 
mode.  This, however requires a different setup and run-time from DOS.

The best way to fix it is to use FORCEDOS command to ensure that only the 
DOS environment is used:

   FORCEDOS COBOL ......
   
As Windows98 does not have the OS/2 'personality' the compiler works in DOS 
without complaint.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
