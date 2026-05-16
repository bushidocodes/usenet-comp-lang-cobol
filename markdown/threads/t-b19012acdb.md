[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error 114 installing MF COBOL 4.0.32... Help!

_34 messages · 11 participants · 2012-06 → 2012-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Error 114 installing MF COBOL 4.0.32... Help!

- **From:** Lori Hornidge <lhornidge@gmail.com>
- **Date:** 2012-06-18T07:14:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com>`

```
Has anyone encountered an error when trying to install the Microfocus/
Merant COBOL 4.0.32 update on a Windows machine?

The actual error is "Execution error:  File 'Update', error code: 114,
pc=0;call=1,seg=0 (Signal 11).

I am able to install 4.0.07 and the WinSDK, but cannot load the 4.0.32
update and I'm getting desperate!  My old desktop died a couple of
weeks ago - it was almost as old as the COBOL :)  I have successfully
installed it several times in the past, but it's been a while...

I've tried setting FILES, BUFFERS, STACK.  I've tried installing it on
WinXP Pro SP3 & SP2 and on a Win98 VM.  I've tried installing it from
DOS and I've even set the Date back to 2009.  Nothing has worked.

I'd appreciate any thoughts or suggestions.

Thanks!
Lori
```

#### ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2012-06-18T11:27:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nnhut7ha3hfl8eda83v9h8f844ujtekk2p@4ax.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com>`

```
On Mon, 18 Jun 2012 07:14:45 -0700 (PDT), Lori Hornidge
<lhornidge@gmail.com> wrote:

>Has anyone encountered an error when trying to install the Microfocus/
>Merant COBOL 4.0.32 update on a Windows machine?
…[16 more quoted lines elided]…
>Lori

According to MF's support website, error 114 is telling you that you
do not have enough memory.

"114 Attempt to access item beyond bounds of memory (Fatal)

Memory access violation has been detected by your operating system.

Good luck.
```

##### ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** lhornidge@gmail.com
- **Date:** 2012-06-18T12:02:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0b73287-c35e-4aa1-8fe5-fcadd5bd1acf@googlegroups.com>`
- **In-Reply-To:** `<nnhut7ha3hfl8eda83v9h8f844ujtekk2p@4ax.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <nnhut7ha3hfl8eda83v9h8f844ujtekk2p@4ax.com>`

```
On Monday, June 18, 2012 8:27:45 AM UTC-7, SkippyPB wrote:
> On Mon, 18 Jun 2012 07:14:45 -0700 (PDT), Lori Hornidge
>  wrote:
…[43 more quoted lines elided]…
> Steve

Thanks for replying so quickly, Steve.  That doesn't seem to be it, not that I can actually prove or disprove it :), but this is a clean XP SP2 desktop with 1GB RAM, nothing running to speak of, firewall & NAV both turned off.  Also had a colleague try installing it on an older desktop and she got the exact same error. I even tried pulling out one of the RAM chips just in case it didn't like having all that memory...  

It's funny - if anything, I would've thought I'd have trouble running the initial 4.0.07 Setup...

Is anyone out there running Object COBOL v4.0.32?
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2012-06-18T20:25:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l9CdnfHNrLtuSULSnZ2dnUVZ_tKdnZ2d@earthlink.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <nnhut7ha3hfl8eda83v9h8f844ujtekk2p@4ax.com> <f0b73287-c35e-4aa1-8fe5-fcadd5bd1acf@googlegroups.com>`

```
lhornidge@gmail.com wrote:
> On Monday, June 18, 2012 8:27:45 AM UTC-7, SkippyPB wrote:
>> On Mon, 18 Jun 2012 07:14:45 -0700 (PDT), Lori Hornidge
…[55 more quoted lines elided]…
>

Remove the cushions from your sofa. Collect the coins. Buy 3 Gigabytes more 
of RAM for your machine.

Try again. Report back.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 4)_

- **From:** lhornidge@gmail.com
- **Date:** 2012-06-19T10:45:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90d7ceb2-3553-40b2-b439-c0e8a90a362a@googlegroups.com>`
- **In-Reply-To:** `<l9CdnfHNrLtuSULSnZ2dnUVZ_tKdnZ2d@earthlink.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <nnhut7ha3hfl8eda83v9h8f844ujtekk2p@4ax.com> <f0b73287-c35e-4aa1-8fe5-fcadd5bd1acf@googlegroups.com> <l9CdnfHNrLtuSULSnZ2dnUVZ_tKdnZ2d@earthlink.com>`

```
On Monday, June 18, 2012 6:25:04 PM UTC-7, HeyBub wrote:
> lhornidge@gmail.com wrote:
> > On Monday, June 18, 2012 8:27:45 AM UTC-7, SkippyPB wrote:
…[61 more quoted lines elided]…
> Try again. Report back.

Haha, thanks - don't think it's the RAM.  Last time I installed it on XP Home (I know, but it was all I had at hand), the machine only had 512MB...
```

##### ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2012-06-19T00:47:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9dd13990-b224-4748-897c-f51827de779c@googlegroups.com>`
- **In-Reply-To:** `<nnhut7ha3hfl8eda83v9h8f844ujtekk2p@4ax.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <nnhut7ha3hfl8eda83v9h8f844ujtekk2p@4ax.com>`

```
On Tuesday, June 19, 2012 3:27:45 AM UTC+12, SkippyPB wrote:
> On Mon, 18 Jun 2012 07:14:45 -0700 (PDT), Lori Hornidge
> <lhornidge@gmail.com> wrote:
…[26 more quoted lines elided]…
> Memory access violation has been detected by your operating system.

It is unlikely to be cured by additional system memory. It is not that it can't allocate memory, it would just use virtual memory if it used up all the RAM, it has had a protection error by trying to access outside a block of the memory that has been allocated to it.

http://supportline.microfocus.com/documentation/books/sx20books/prxept.htm
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** lhornidge@gmail.com
- **Date:** 2012-06-19T10:49:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64701101-6ba7-40dd-859d-6b59d23818b1@googlegroups.com>`
- **In-Reply-To:** `<9dd13990-b224-4748-897c-f51827de779c@googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <nnhut7ha3hfl8eda83v9h8f844ujtekk2p@4ax.com> <9dd13990-b224-4748-897c-f51827de779c@googlegroups.com>`

```
On Tuesday, June 19, 2012 12:47:31 AM UTC-7, Richard wrote:
> On Tuesday, June 19, 2012 3:27:45 AM UTC+12, SkippyPB wrote:
> > On Mon, 18 Jun 2012 07:14:45 -0700 (PDT), Lori Hornidge
…[31 more quoted lines elided]…
> http://supportline.microfocus.com/documentation/books/sx20books/prxept.htm

Exactly!  But since it's the Update executable from MF, I can't really debug it, can I?  I've looked into the logs on the machine and didn't find anything useful.
```

#### ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-06-19T12:08:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<df4fcb32-549e-487b-896e-e8b9a2de10d0@googlegroups.com>`
- **In-Reply-To:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com>`

```
On Monday, 18 June 2012 15:14:45 UTC+1, Lori  wrote:
> Has anyone encountered an error when trying to install the Microfocus/
> Merant COBOL 4.0.32 update on a Windows machine?
…[16 more quoted lines elided]…
> Lori

You won't find much info on this eror on the net but if you google:

"pc=0;call=1,seg=0 (Signal 11)"

there is some info about setting permissions. There is other stuff about Macola but that I think is irrelevant.

The 114 error mentioned by others is a Cobol runtime error message and probably does not apply to an update of the executable.
```

##### ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** Lori <lhornidge@gmail.com>
- **Date:** 2012-06-20T09:20:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7d592e73-bf42-4512-b04e-654d5d0ae6b1@googlegroups.com>`
- **In-Reply-To:** `<df4fcb32-549e-487b-896e-e8b9a2de10d0@googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <df4fcb32-549e-487b-896e-e8b9a2de10d0@googlegroups.com>`

```
On Tuesday, June 19, 2012 12:08:12 PM UTC-7, Alistair Maclean wrote:
> On Monday, 18 June 2012 15:14:45 UTC+1, Lori  wrote:
> > Has anyone encountered an error when trying to install the Microfocus/
…[25 more quoted lines elided]…
> The 114 error mentioned by others is a Cobol runtime error message and probably does not apply to an update of the executable.

Thanks Alistar - I think you're right, it's looking to be permission-based and I'll keep bashing away at that end if no one else has already solved it...?

Rick - thanks for the link.  That's a known issue with the Setup of 4.0.07.  I'd used the fix and didn't get any errors installing it.  The problem I'm currently having is loading the 4.0.32 update.  It's just truly bizarre and very persistent.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** Lori <lhornidge@gmail.com>
- **Date:** 2012-06-20T12:00:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<568cb629-3baf-4169-a9ff-730e4ecc303f@googlegroups.com>`
- **In-Reply-To:** `<7d592e73-bf42-4512-b04e-654d5d0ae6b1@googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <df4fcb32-549e-487b-896e-e8b9a2de10d0@googlegroups.com> <7d592e73-bf42-4512-b04e-654d5d0ae6b1@googlegroups.com>`

```
On Wednesday, June 20, 2012 9:20:45 AM UTC-7, Lori wrote:
> On Tuesday, June 19, 2012 12:08:12 PM UTC-7, Alistair Maclean wrote:
> > On Monday, 18 June 2012 15:14:45 UTC+1, Lori  wrote:
…[30 more quoted lines elided]…
> Rick - thanks for the link.  That's a known issue with the Setup of 4.0.07.  I'd used the fix and didn't get any errors installing it.  The problem I'm currently having is loading the 4.0.32 update.  It's just truly bizarre and very persistent.

Meanwhile, back at the ranch... I was able to get the COBOL folders off the old hard-drive (local chop shop retrieved them for me).  Once I copied the one with the 4.0.32 version on to the new machine and installed the Sentinel driver (so it would recognize the dongle, good times), I was able to compile.  I don't know if I've ever been this happy to see a COBOL program compiling... LOL  

Thanks again for everyone's suggestions!
```

#### ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-06-19T13:35:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<941e7bbc-f6f5-407b-af23-8d97d52ce686@googlegroups.com>`
- **In-Reply-To:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com>`

```
On Monday, June 18, 2012 10:14:45 AM UTC-4, Lori wrote:
> Has anyone encountered an error when trying to install the Microfocus/
> Merant COBOL 4.0.32 update on a Windows machine?
…[16 more quoted lines elided]…
> Lori

< https://groups.google.com/d/topic/comp.lang.cobol/ukwz_eSgIQY/discussion >
Subject: Problems installing MF Workbench 4.0 on WinXP
```

#### ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** M Kippels <mkippels@ignorethis-comcast.net>
- **Date:** 2012-06-22T09:51:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4FE48673.4892@ignorethis-comcast.net>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com>`

```
Lori Hornidge wrote:
> 
> Has anyone encountered an error when trying to install the Microfocus/
…[17 more quoted lines elided]…
> Lori

This is was a Y2K install problem.  Microfocus (Merant in those days) 
released a patch, fix2kset.zip.  I have a copy of the patch.  If you 
search for "fix2kset.zip", you will find a couple of references to the
problem and the patch.  Here's MF's (Merant's) info:

Year 2000 fix for MF 32bit setups

General

The following file contains a year 2000 fix for products that are using
the
Micro Focus GUI Setup technology on Win32 platforms e.g. WB4.0

Problem Fixed

When Setup is run in the year 2000, fatal errors are encountered e.g.
114
on 'log'

RPIs fixed

   * 502236

Download the fix

Download the fix. It is a zip file containing four files. You may use
this
in either of two ways as given below.

Down load the fix

Method 1

Unzip the file into it's own directory and then type

     Enter setup -from x:

     where x: is the location of the original setup files.

Method 2

Unzip the file into a directory containing the installation for the
product, replacing files already present.

     Enter setup

This will allow the MF setup to run in the year 2000.
```

##### ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** "Stephen" <noacndo@anon.com>
- **Date:** 2012-12-10T14:22:49
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net>`

```
"M Kippels" <mkippels@ignorethis-comcast.net> wrote in message 
news:4FE48673.4892@ignorethis-comcast.net...
>
> This is was a Y2K install problem.  Microfocus (Merant in those days)
…[3 more quoted lines elided]…
>
Anyone know how to get hold of that fix.  I was trying to install 32 bit 
COBOL the other day and ran into this issue.  Unfortunately my maintenance 
ran out years ago so I can't go direct to MF for the fix as you need a 
support contract to logon to their support web site to download anything. 
Does anyone have it or could point me to where I could download it for free? 
The old MF ftp site used to have all the old updates but it doesn't anymore, 
alas.

Many thanks

Stephen
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2012-12-10T10:20:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ka4uk8029o3@news1.newsguy.com>`
- **In-Reply-To:** `<2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com>`

```
Stephen wrote:
> "M Kippels" <mkippels@ignorethis-comcast.net> wrote in message 
> news:4FE48673.4892@ignorethis-comcast.net...
…[8 more quoted lines elided]…
> support contract to logon to their support web site to download anything. 

Irrelevant - I couldn't find it on the MF Supportline site anyway. 
Even in the "fix archives" area, the oldest materials I could find are 
for Net Express 1.0.

> Does anyone have it or could point me to where I could download it for free? 

Afraid not.

Why are you trying to install MF COBOL 4.0.32? (I don't appear to have 
your original message in my feed.) If it's just for personal use, you 
could try the now-free Enterprise Developer Personal Edition:

http://online.microfocus.com/Enterprise-Developer-PE

Otherwise, your best option may be a virtual machine running an old 
version of Windows with the date set to something before 2000-01-01.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 4)_

- **From:** "Stephen" <noacndo@anon.com>
- **Date:** 2012-12-10T15:43:28
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Fqnxs.81840$oT2.60506@en-nntp-06.am2.easynews.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com>`

```
"Michael Wojcik" <mwojcik@newsguy.com> wrote in message 
news:ka4uk8029o3@news1.newsguy.com...
>>>
>
…[5 more quoted lines elided]…
>
Thanks for your response.  To be honest, it was mostly for old time's sake. 
I have't developed seriously in COBOL since the late 1990s but I still have 
all my old developer tools.  I had an old WinNT box that I had working 
copies of 4.0.32 COBOL on but junked it a couple of months ago.  Now I have 
remorse and wanted to get it working again in a NT4 WM on Windows 7.  I 
though that it might be fun to revisit some of my old programs.

Perhaps the Enterprise Personal Developer might be my best bet, but was 
pining for the old Workbench interface !

> Otherwise, your best option may be a virtual machine running an old 
> version of Windows with the date set to something before 2000-01-01.
>
I've already tried that but still doesn't work
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 4)_

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-12-11T02:05:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com>`

```
Michael Wojcik wrote:

> Stephen wrote:
> >"M Kippels" <mkippels@ignorethis-comcast.net> wrote in message
…[29 more quoted lines elided]…
> version of Windows with the date set to something before 2000-01-01.

Michael: what exactly does the Enterprise Developer PE give its user?
Is it just an IDE for COBOL programs? I have MF COBOL 4.0.32 which runs
fine in an XP Command prompt.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 5)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2012-12-11T08:18:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ka7bsl06fs@news3.newsguy.com>`
- **In-Reply-To:** `<rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au>`

```
Paul Richards wrote:
> Michael Wojcik wrote:
> 
…[9 more quoted lines elided]…
> fine in an XP Command prompt.

To be honest, I'm not sure exactly what's included with EDPE - I don't 
have it installed myself (since I end up installing the latest builds 
of at least two different versions of our products every couple of 
weeks as it is).

ED is the COBOL compiler and integration for the Visual Studio and 
Eclipse IDEs, so you can use it with either of those IDEs. (Eclipse is 
also free, and there's a free version of Visual Studio available from 
Microsoft.) You can also compile from the command line.

ED includes things like syntax checking in the editor, traditional and 
OO COBOL (including both ISO and MF simplified OO syntax), native and 
managed (.NET and JVM) code, etc.

The IDEs are pretty resource-hungry - you'll need a fairly recent 
machine with ample memory and disk space to run either of them. On the 
other hand, the simplified-syntax managed-code COBOL is pretty slick 
and lets you use the .NET Framework or Java class libraries, plus 
anything else that supports those environments.

I think PE has some limit on how big source files can be, and I don't 
think it contains the mainframe emulation environments (CICS, JES, and 
IMS support).
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 6)_

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-12-11T18:28:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h5ednemBt_4yUlrNnZ2dnUVZ_hOdnZ2d@westnet.com.au>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <ka7bsl06fs@news3.newsguy.com>`

```
Michael Wojcik wrote:


> > Michael: what exactly does the Enterprise Developer PE give its
> > user?  Is it just an IDE for COBOL programs? I have MF COBOL 4.0.32
…[13 more quoted lines elided]…
><snip>

Michael: does this mean that I could use ED as an IDE for MF COBOL
4.0.32 (if I wanted to) and run its compiler i.e. 4.0.32's and other
tools e.g. Animator, from the IDE?
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2012-12-12T10:13:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kaa7rb026fk@news3.newsguy.com>`
- **In-Reply-To:** `<h5ednemBt_4yUlrNnZ2dnUVZ_hOdnZ2d@westnet.com.au>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <ka7bsl06fs@news3.newsguy.com> <h5ednemBt_4yUlrNnZ2dnUVZ_hOdnZ2d@westnet.com.au>`

```
Paul Richards wrote:
> 
> Michael: does this mean that I could use ED as an IDE for MF COBOL
> 4.0.32 (if I wanted to) and run its compiler i.e. 4.0.32's and other
> tools e.g. Animator, from the IDE?

No, I'm afraid not. ED is the compiler, debugger, and other tools, and 
it runs under either the Visual Studio or Eclipse IDE. It replaces 
earlier versions of MF COBOL.

However, any correct, standard COBOL program that worked under MF 
COBOL 4 should work under ED, and most programs that use non-standard 
extensions will too.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 8)_

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-12-13T18:03:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l5adndr0is4j8VfNnZ2dnUVZ_uednZ2d@westnet.com.au>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <ka7bsl06fs@news3.newsguy.com> <h5ednemBt_4yUlrNnZ2dnUVZ_hOdnZ2d@westnet.com.au> <kaa7rb026fk@news3.newsguy.com>`

```
Michael Wojcik wrote:

> Paul Richards wrote:
> > 
…[10 more quoted lines elided]…
> extensions will too.

Michael: I realised after I had posted my message that I had a basic
misunderstanding of ED. So I downloaded it (the Personal Edition) and
installed it. As far as I can make out you can syntax check COBOL code
but if you want to run, debug and,I suppose, compile it you have to
take out a trial version licence. I didn't investigate this but I
assumed it would not be free to get ED PE to do anything 'useful' ;-).
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 9)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2012-12-14T10:28:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kan6i5030do@news6.newsguy.com>`
- **In-Reply-To:** `<l5adndr0is4j8VfNnZ2dnUVZ_uednZ2d@westnet.com.au>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <ka7bsl06fs@news3.newsguy.com> <h5ednemBt_4yUlrNnZ2dnUVZ_hOdnZ2d@westnet.com.au> <kaa7rb026fk@news3.newsguy.com> <l5adndr0is4j8VfNnZ2dnUVZ_uednZ2d@westnet.com.au>`

```
Paul Richards wrote:
> 
> Michael: I realised after I had posted my message that I had a basic
…[4 more quoted lines elided]…
> assumed it would not be free to get ED PE to do anything 'useful' ;-).

Hmm. I didn't realize that's what ED PE did (I've never installed it 
myself). I thought it was more like the Academic Edition we had a 
while back. Sorry to waste your time!
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 5)_

- **From:** "Stephen" <noacndo@anon.com>
- **Date:** 2012-12-11T15:03:01
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HWHxs.57118$U23.18135@en-nntp-08.am2.easynews.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au>`

```
"Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au> wrote in message 
news:rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au...
> Michael Wojcik wrote:
>
…[36 more quoted lines elided]…
>
Paul - You are running what I want to run 4.0.32 on NT 4 or XP.  Do you have 
this fix that is referred to above?  If so would you be able to send it to a 
(throwaway) email address I could nominate?

Thanks
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 6)_

- **From:** "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au>
- **Date:** 2012-12-11T18:31:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dMKdnYj5h-TSTVrNnZ2dnUVZ_oudnZ2d@westnet.com.au>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <HWHxs.57118$U23.18135@en-nntp-08.am2.easynews.com>`

```
Stephen wrote:

> "Paul Richards" <paulrichards@XXXNOSPAMiinet.net.au> wrote in message
> news:rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au...
…[45 more quoted lines elided]…
> Thanks

Stephen: I've replied to your email.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-12-18T08:49:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com>`
- **In-Reply-To:** `<rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au>`

```
On Tuesday, December 11, 2012 8:05:46 AM UTC, Paul Richards wrote:
> If it's just for personal > use, you could try the now-free Enterprise Developer Personal Edition: > > http://online.microfocus.com/Enterprise-Developer-PE > > Otherwise, your best option may be a virtual machine running an old > version of Windows with the date set to something before 2000-01-01. 
> Michael: what exactly does the Enterprise Developer PE give its user? Is it just an IDE for COBOL programs? I have MF COBOL 4.0.32 which runs fine in an XP Command prompt. 

I've checked out the MF link for Enterprise Developer Personal Edition and was impressed with it's capabilities until I got to the last paragraph which states that it runs under Windows 7 only. I have yet to try it on Windows XP. 

The link https://www.microfocus.com/assets/enterprise-developer_tcm6-205109.pdf 
gives an overview of what it does but doen't compare it with Net Express or earlier versions of MF Cobol but if you are heavily in to mainframe environments it should be good for you.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 6)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-12-18T09:02:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com>`
- **In-Reply-To:** `<b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com>`

```
The MF Community indicates that MFEDPE will install on older Windows systems:

Enterprise Developer Personal and Team Edition are officially supported on Windows 7.0 and Windows Server 2008 and available as both a 32 and 64 bit application. Enterprise Developer will install successfully on earlier versions of Windows but this is not officially supported.

The pre-requisite software required (and installed as part of the software setup) varies depending on the product being installed. For Enterprise Developer for Eclipse the following will be installed

• Java JRE 1.6.27
•.NET Framework v4.0
•Eclipse 3.7.1 (incorporated into the EDTE MSI).
•Micro Focus License Manager
 For Enterprise Developer Team Edition for Visual Studio

•Visual Studio 2010 Integrated Shell (incorporates  .NET Framework v4.0)
•Micro Focus License Manager
The installation process will drive you through the install and add all the necessary components, if not already installed and compatible.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-12-19T05:30:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<839d5751-22c7-4faa-9302-352832509d43@googlegroups.com>`
- **In-Reply-To:** `<fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com> <fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com>`

```
The quote about working on XP may be inaccurate. I tried installing the MF package yesterday with the message "Cabinet file 'data1.cab'....is corrupt and can not be used". I tried this three times via the web installer option and once via the alternative installation route with the same result.

Apart from giving up does anybody have any suggestions?
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 8)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2012-12-19T09:15:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kasi7n020id@news1.newsguy.com>`
- **In-Reply-To:** `<839d5751-22c7-4faa-9302-352832509d43@googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com> <fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com> <839d5751-22c7-4faa-9302-352832509d43@googlegroups.com>`

```
Alistair Maclean wrote:
> The quote about working on XP may be inaccurate.

Well, it mentioned "earlier" versions - that might just mean Windows 
Vista.

 > I tried installing
> the MF package yesterday with the message "Cabinet file
…[4 more quoted lines elided]…
> Apart from giving up does anybody have any suggestions?

You could check that you have the latest version of MSI (Microsoft's 
demonic software installer). It looks like version 4.5 might be the 
latest:

http://www.microsoft.com/en-us/download/details.aspx?id=8483

It requires XP Service Pack 2.

Is the full installer (as opposed to the web installer) available on 
the MF site for EDPE? That might also work better.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 9)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-12-20T12:00:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8f757d8-66ed-42b1-a7b7-a6341361f7b3@googlegroups.com>`
- **In-Reply-To:** `<kasi7n020id@news1.newsguy.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com> <fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com> <839d5751-22c7-4faa-9302-352832509d43@googlegroups.com> <kasi7n020id@news1.newsguy.com>`

```
Thanks to Pete and Michael. I will follow instructions for the various suggestions and post back here when I've done that (don't hold your breath as I'm notoriously slow).
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2012-12-20T11:12:45+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajesetFs1vnU1@mid.individual.net>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com> <fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com> <839d5751-22c7-4faa-9302-352832509d43@googlegroups.com>`

```
"Alistair Maclean" <alistair.j.l.maclean@gmail.com> wrote in message 
news:839d5751-22c7-4faa-9302-352832509d43@googlegroups.com...
The quote about working on XP may be inaccurate. I tried installing the MF 
package yesterday with the message "Cabinet file 'data1.cab'....is corrupt 
and can not be used". I tried this three times via the web installer option 
and once via the alternative installation route with the same result.

Apart from giving up does anybody have any suggestions?
---------------------------------------------------
Pete commented thus...

Giving up is not usually an attractive option and, for some of us, can only 
be implemented when there is definite proof that what is being attempted 
cannot be done. (That is an EXTREMELY rare scenario...)

The problem of "corrupted CAB files" can stem from many causes and Michael 
is right to suggest checking the MSI installer.

Here are some possible actions:

1. Re-register the msiexec program. (Run "msiexec /unregister"  then 
"msiexec /register".

(I believe this one has the best chance of success... When you do it, it may 
look as if nothing happened. Don't be deterred... complete the two steps.)

2. Quoting from Adobe.... (where I once experienced this)
"The message "Corrupt cabinet file" appears if the downloaded file you're 
trying to open is damaged. Downloaded files are more susceptible to damage 
when downloaded during peak periods or over an unstable Internet connection. 
The message also appears if your Internet connection was broken while the 
file was downloading. Your Internet service provider (ISP) maintains the 
connection when it detects activity, such as when you visit Web sites or 
send e-mail. The ISP doesn't detect activity when you are only downloading a 
file."

Note that under some circumstances, even if the file ISN'T damaged it may 
report as being so...
3. Check the RAM on your system. If you have flawed memory it will cause 
this.

http://windows.microsoft.com/en-US/windows-vista/How-do-I-know-if-my-computer-has-a-memory-problem

4. Check the integrity of your main disk drive. (Checkdisk or similar...)

5. Use a quality repair program.

http://www.datanumen.com/acr/

(No, it ISN'T free, but believe it or not, software developers have to eat 
too...)

6. Try extracting the CAB file with 7z or a RAR utility. Then repackage it 
as a CAB. (This one is not for amateurs...)

HTH,

Pete.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 8)_

- **From:** Mike Fleming <{mike}@tauzero.co.uk>
- **Date:** 2012-12-21T17:32:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fr69d8tloeogq25ffnqhd22o8nstgo413j@4ax.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com> <fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com> <839d5751-22c7-4faa-9302-352832509d43@googlegroups.com>`

```
In article <839d5751-22c7-4faa-9302-352832509d43@googlegroups.com>,
Alistair Maclean <alistair.j.l.maclean@gmail.com> writes:

> The quote about working on XP may be inaccurate. I tried installing
> the MF package yesterday with the message "Cabinet file
…[4 more quoted lines elided]…
> Apart from giving up does anybody have any suggestions?

I can tell you that it (the Eclipse version, anyway) will install and
run on XP (SP3 anyway). I've got EDTE for Eclipse on a work laptop and
desktop, both of which are on XP SP3, and EDPE for Eclipse on my own
XP SP3 machine. The installers for EDPE, EDTE, and Visual COBOL for
SOA are identical.

However, I did have to install EDTE for Visual Studio on a Win 7
machine (I don't think we've got any Vista machines at work, so at
least someone has made one correct decision, although OTOH someone
decided that McAffee was a good choice for AV).

I haven't applied for a trial EDPE licence - not sure whether it would
be time limited.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 9)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2012-12-21T11:48:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ef9392f-2475-4ceb-be33-d26eaf09264e@googlegroups.com>`
- **In-Reply-To:** `<fr69d8tloeogq25ffnqhd22o8nstgo413j@4ax.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com> <fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com> <839d5751-22c7-4faa-9302-352832509d43@googlegroups.com> <fr69d8tloeogq25ffnqhd22o8nstgo413j@4ax.com>`

```
On Friday, December 21, 2012 5:32:34 PM UTC, Mike Fleming wrote:
> I haven't applied for a trial EDPE licence - not sure whether it would be time limited. -- Mike Fleming

I spent a lot of time going through the licence, etc., for EDPE but could find no time delimitation nor any source limits. I believe there are limits to what it does (ie it isn't the mainstream full package).
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 10)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2012-12-21T13:31:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<158703a5-f999-4204-a3c9-5422976590da@googlegroups.com>`
- **In-Reply-To:** `<5ef9392f-2475-4ceb-be33-d26eaf09264e@googlegroups.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <ka4uk8029o3@news1.newsguy.com> <rLSdnVJZ1oHHdFvNnZ2dnUVZ_r-dnZ2d@westnet.com.au> <b9d37319-aa12-4536-ab6d-c905d508a972@googlegroups.com> <fc88f1cc-c1dd-4265-a827-6f774f54efad@googlegroups.com> <839d5751-22c7-4faa-9302-352832509d43@googlegroups.com> <fr69d8tloeogq25ffnqhd22o8nstgo413j@4ax.com> <5ef9392f-2475-4ceb-be33-d26eaf09264e@googlegroups.com>`

```
On Friday, December 21, 2012 2:48:43 PM UTC-5, Alistair Maclean wrote:
> On Friday, December 21, 2012 5:32:34 PM UTC, Mike Fleming wrote:
> 
…[8 more quoted lines elided]…
> package).

Micro Focus Enterprise Developer 2.1 for Visual Studio
Release Notes, page 21.
=====
Enterprise Developer Personal Edition is a single-user
entry-level version that allows developers to edit
mainframe applications off the host. Enterprise Developer
Personal Edition checks syntax as you type code. You
can compile applications, and view compilation errors,
but not access built artifacts. Personal Edition does
not support producing build artifacts at build time,
debugging, unit testing mainframe applications, or
developing PL/I applications.

The Personal Edition of this product is free.

Enterprise Developer Team Edition is a full-function
team-enabled version that allows developers to edit,
compile, debug and unit-test mainframe applications
within the Visual Studio IDE.

You can request a 30-days trial license for the Team
Edition of the product or contact a Micro Focus sales
representative to obtain a full unlimited license.
=====

What I understand is that one may code and syntax check
a substantial application for an IBM mainframe; however,
one cannot execute any part of that code without a Team
Edition license.

From other sources at www.microfocus.com it appears that
the Team Edition may be used to develop applications
that run on servers and workstations, as well as IBM
mainframes.

While the product may be of interest for those who work
with IBM mainframes, it appears to provide little benefit
to those who don't.
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2012-12-10T10:23:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p8vbc8tljm5lctlvjiatucuigv8nku9ir0@4ax.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com>`

```
On Mon, 10 Dec 2012 14:22:49 -0000, "Stephen" <noacndo@anon.com>
wrote:

>"M Kippels" <mkippels@ignorethis-comcast.net> wrote in message 
>news:4FE48673.4892@ignorethis-comcast.net...
…[17 more quoted lines elided]…
>

Found this information using Google:

This is was a Y2K install problem. Microfocus (Merant in those days)
released a patch, fix2kset.zip. I have a copy of the patch. If you
search for "fix2kset.zip", you will find a couple of references to the
problem and the patch. Here's MF's (Merant's) info:

Year 2000 fix for MF 32bit setups

General

The following file contains a year 2000 fix for products that are
using
the
Micro Focus GUI Setup technology on Win32 platforms e.g. WB4.0

Problem Fixed

When Setup is run in the year 2000, fatal errors are encountered e.g.
114
on 'log'

RPIs fixed

* 502236

Download the fix

Download the fix. It is a zip file containing four files. You may use
this
in either of two ways as given below.

Down load the fix

Method 1

Unzip the file into it's own directory and then type

Enter setup -from x:

where x: is the location of the original setup files.

Method 2

Unzip the file into a directory containing the installation for the
product, replacing files already present.

Enter setup

This will allow the MF setup to run in the year 2000.
.
---------------------------

Also found this (using Google):

One or more GNT missing from engine

Product: 	 Dialog System 	KB Number: 	 15413
Product Family: 	 Workbench 	Date Published: 2003-05-05
00:00:00.000

Problem
This is the error the users will get when they attempt to install
Dialog System, Workbench, and OSX on a Windows 2000 machine. This is
due to the fact that the base installation for 32-bit Dialog System
v2.5 is not Y2K compliant.

Resolution
The patch for the setup program can be found at:
ftp://ftp.microfocus.com/updates/cobol-workbench-v4.0/non-security-keyed/windows-nt-95/,
and it is the same patch that can be used to install Workbench and
OSX. The name of the patch is fix2kset.zip. Here are the instructions:
To install: 1. Make sure the TEMP and TMP environment variables point
to a non-spacey named directory, such has C:\TEMP 2. Extract the files
from the attached ZIP file (fix2kset.zip) to a temporary directory
that does not exceed 8 characters and does not contain any spaces (eg.
D:\DSFIX2K) 3. Insert the Dialog System CD into the CD-ROM (eg. E:\)
4. Click Start > Run 5. Run the following command:
D:\DSFIX2K\setup.exe -FROM E: ***where E:\ points to the old version
of setup.exe on the CD To update; Downloading 2.5.64 update from
ftp://ftp.microfocus.com/updates/dialog-system/ds-2.5/windows-nt-95/
1. Download ALL zip files to the Same directory (drive:\FTPupd) 2.
Start by unzipping the DS2564win1.zip through DS2564win3.zip (should
be 3 zip files) 3. Unzip the supplied Win32.zip to the drive:\FTPupd
directory replace the existing one. 4. Go to Start\Run 5. Type the
following: drive:\FTPupd\Update.exe

------------------------------------

HTH

Regards,
```

###### ↳ ↳ ↳ Re: Error 114 installing MF COBOL 4.0.32... Help!

_(reply depth: 4)_

- **From:** "Stephen" <noacndo@anon.com>
- **Date:** 2012-12-10T15:44:37
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jrnxs.32596$Wg6.9720@en-nntp-07.am2.easynews.com>`
- **References:** `<1aa3f3c6-015c-4492-8865-bcdc2e75695b@n9g2000pbi.googlegroups.com> <4FE48673.4892@ignorethis-comcast.net> <2fmxs.86581$Qv2.78091@en-nntp-03.am2.easynews.com> <p8vbc8tljm5lctlvjiatucuigv8nku9ir0@4ax.com>`

```
"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
news:p8vbc8tljm5lctlvjiatucuigv8nku9ir0@4ax.com...
>
> Resolution
…[5 more quoted lines elided]…
>
Unfortunately those directories no longer exist on the ftp site :(
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
