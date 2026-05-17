[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL HELP

_8 messages · 6 participants · 2016-01_

---

### COBOL HELP

- **From:** "aleksandar.zubic" <ua-author-14501789@usenetarchives.gap>
- **Date:** 2016-01-18T04:55:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com>`

```
Hi all

I need help

Im using COBOL-85 on work (version 2.10 R2.1A)
Work fine with dos machines, win95, win98 and we manage to make it run on winxp.

I need something to convert my files to work on win7 and upper version cuz i can find any old machines anymore. If anyone have any info or tip in right direction pls post.

And what do you all think about Fujitsu Netcobol can he do what i asked or i need to adjust whole program?

I have search i bit and found something but i cant download to see what it is, always or broken link or page not found or virus malware.

Does Fujitsu COBOL85 version 3.0 can do this and what id COBOL-IT?
```

#### ↳ Re: COBOL HELP

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2016-01-18T10:39:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9a6e19fd1f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com>`
- **References:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com>`

```
In article <80d96265-eeae-4cc0-8574-d89··f@goo··s.com>,
wrote:
› Hi all
› 
…[7 more quoted lines elided]…
› in right direction pls post.

First tip: tell what methods you have tried that failed.

DD
```

#### ↳ Re: COBOL HELP

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-01-18T22:15:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9a6e19fd1f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com>`
- **References:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com>`

```
ale··c@gm··l.com wrote:
› Hi all
›
› I need help
›
› Im using COBOL-85 on work (version 2.10 R2.1A)

>From which vendor? (COBOL-85 is a STANDARD. It is implemented by a number of
compiler vendors...)

› Work fine with dos machines, win95, win98 and we manage to make it
› run on winxp.
› 
› I need something to convert my files to work on win7 and upper
› version cuz i can find any old machines anymore.

Do you really mean "files" or are you talking about data and programs?

If your compiler won't run on Win 7 + it is a fair bet that the code it
generates and the file structures it creates are not going to be very
successful in that environmnet either.

It sounds like you may have a very old 16 bit implementation of COBOL.

You need to upgrade your compiler and environment, then recompile your
existing source. You will need utilities (provided by some vendors) to load
the data on the old files into the new ones. If you don't have such
utilities you will need to write them yourself, or pay someone else to do it
for you.

(Personally, I'd take this opportunity to convert all your old indexed files
to a modern RDBMS, but that's another story...)

The first step is to decide on which COBOL vendor you are going to go with.

There is also a version of "Open COBOL" available (GNU COBOL) which is
free, and reports are very positive about it. It will take you through the
Win 7+ barrier.

› If anyone have any
› info or tip in right direction pls post.
› 
› And what do you all think about Fujitsu Netcobol can he do what i
› asked or i need to adjust whole program?

Fujitsu NetCOBOL for Windows is an excellent (native code generating)
product (it supports COBOL-85 and should be able to re-compile your existing
source without major changes.) I use it myself, and have done so for over 20
years. Micro Focus is also good, but I believe they charge a Run Time
Licence fee, so anything you do cannot be distrbuted without paying
them.Both these companies also sell COBOL for .NET (CIL generating)
compilers, but these are very expensive and you can get C# (also CIL
generating) for free.

›
› I have search i bit and found something but i cant download to see
› what it is, always or broken link or page not found or virus malware.
›
› Does Fujitsu COBOL85 version 3.0 can do this and what id COBOL-IT?

Fujitsu COBOL85 version 3 was an early 16 bit version which was available
for free. It is now obsolete and no longer supported.

COBOL-IT is a French produced COBOL system which claims to be Open Source
(similar to GNU COBOL, above; they both produce C code.). It is marketed in
the USA through ESI and runs on most platforms. If you go with this, please
let us know your opinions about it.

Hope this helps,

Pete.

"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: COBOL HELP

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2016-01-18T23:49:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9a6e19fd1f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9a6e19fd1f-p3@usenetarchives.gap>`
- **References:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com> <gap-9a6e19fd1f-p3@usenetarchives.gap>`

```
On 1/18/2016 9:15 PM, Pete Dashwood wrote:
› ale··c@gm··l.com wrote:
›› Hi all
…[3 more quoted lines elided]…
›› Im using COBOL-85 on work (version 2.10 R2.1A)


This sounds like the old IBM PC-DOS COBOL compiler, or possibly the old
MicroFocus COBOL compiler for DOS re-badged as Microsoft COBOL for MS-DOS.


› 
›  From which vendor? (COBOL-85 is a STANDARD. It is implemented by a number of
…[29 more quoted lines elided]…
› Win 7+ barrier.


The older COBOL might work on on a 32-bit version of Win7, Win8.1, or
Win10. Most new PC's (since Win7) come pre-installed with 64-bit
versions of Windows.

GnuCOBOL 1.1 will work in 32-bit or 64-bit windows. I have built a
installed for windows using the package on Sourceforge.net:

http://www.arnoldtrembley.com/GnuCOBOL-MinGw-Installer.zip

I'm still working on building a GnuCOBOL 2.0 installer for Windows. GC
2.0 is not quite feature complete yet.

GnuCOBOL does not yet include a debugger.

There are manuals available at:
https://sourceforge.net/projects/open-cobol/
http://open-cobol.sourceforge.net/

And a very large FAQ:
http://open-cobol.sourceforge.net/faq/index.html

There's also a free Python based Interactive Development Environment for
OpenCOBOL/GnuCOBOL, for Linux, Mac, or Windows - opencobolide:

https://pypi.python.org/pypi/OpenCobolIDE
http://opencobolide.readthedocs.org/en/latest/download.html
https://launchpad.net/cobcide/+download


› 
›› If anyone have any
…[26 more quoted lines elided]…
› let us know your opinions about it.


I could be wrong, but I believe COBOL-IT is built from
OpenCOBOL/GnuCOBOL source files, and is available for free download
(registration required) from their website. COBOL-IT makes money
selling service and support for their compiler.

http://www.cobol-it.com/
http://www.cobol-it.com/index.php?page=compiler-suite
http://www.cobol-it.com/contact.php?request_type=cs


›
› Hope this helps,
›
› Pete.
›

Ditto!


http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: COBOL HELP

- **From:** "aleksandar.zubic" <ua-author-14501790@usenetarchives.gap>
- **Date:** 2016-01-19T01:36:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9a6e19fd1f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9a6e19fd1f-p4@usenetarchives.gap>`
- **References:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com> <gap-9a6e19fd1f-p3@usenetarchives.gap> <gap-9a6e19fd1f-p4@usenetarchives.gap>`

```
› The older COBOL might work on on a 32-bit version of Win7, Win8.1, or 
› Win10.  Most new PC's (since Win7) come pre-installed with 64-bit 
…[24 more quoted lines elided]…
› https://launchpad.net/cobcide/+download

10x for this i will check it and if have any question i will ask
mainly i need to convert my old program and maybe make "exe" file from it so can work on any machine
```

##### ↳ ↳ Re: COBOL HELP

- **From:** "aleksandar.zubic" <ua-author-14501790@usenetarchives.gap>
- **Date:** 2016-01-19T01:31:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9a6e19fd1f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9a6e19fd1f-p3@usenetarchives.gap>`
- **References:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com> <gap-9a6e19fd1f-p3@usenetarchives.gap>`

```
› From which vendor? (COBOL-85 is a STANDARD. It is implemented by a number of 
› compiler vendors...)
 
› its MS oliveti quite old i must say
 
› Do you really mean "files" or are you talking about data and programs?
 
› We create software and mainly we have issues with data cuz it 16bit and rebuild dont work in windows 7 and higher that is main problem and that why i want to change it to something else without bigger adjustments
 
› If your compiler won't run on Win 7 + it is a fair bet that the code it 
› generates and the file structures it creates are not going to be very 
…[17 more quoted lines elided]…
› Win 7+ barrier.

that is why we want to change from index files to something new
my question is open cobol can convert this without major correction in code?

› Fujitsu NetCOBOL for Windows is an excellent (native code generating) 
› product (it supports COBOL-85 and should be able to re-compile your existing 
…[5 more quoted lines elided]…
› generating) for free.

Have this i think maybe version 7.0 but i never tried it but now i will have to
now

thanks for information and i will check all this i post for additional question and help if needed
```

###### ↳ ↳ ↳ Re: COBOL HELP

- **From:** "riplin" <ua-author-6588701@usenetarchives.gap>
- **Date:** 2016-01-20T14:47:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9a6e19fd1f-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9a6e19fd1f-p6@usenetarchives.gap>`
- **References:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com> <gap-9a6e19fd1f-p3@usenetarchives.gap> <gap-9a6e19fd1f-p6@usenetarchives.gap>`

```
On Tuesday, January 19, 2016 at 7:31:57 PM UTC+13, Aleksandar Zubic wrote:
›› From which vendor? (COBOL-85 is a STANDARD. It is implemented by a number of
›› compiler vendors...)
›
› its MS oliveti quite old i must say

It is the COBOL Vendor that was being asked for: MicroFocus, Ryan-MacFarland, Microsoft, Fujitsu, Accu, ... ?

>From the 'COBOL-85' and '2.10' I would guess Microfocus from 1990 or so for MS-DOS, Windows 3.x and OS/2. It may be that Olivetti resold it. RM did call their compiler 'COBOL-85' so it could be that.

›› Do you really mean "files" or are you talking about data and programs?
› 
› We create software and mainly we have issues with data cuz it 16bit and rebuild dont work in windows 7 and higher that is main problem and that why i want to change it to something else without bigger adjustments
› 
 
› 'Rebuild' also may indicate Microfocus.
 
 
› that is why we want to change from index files to something new 
› my question is open cobol can convert this without major correction in code?

Converting data files between different vendors can be a problem. If you have COMP fields in the files then the data may need to be copied by your cobol system to sequential files with display fields only with sign separate.

You would then need to rebuild the ISAM files (or other) in the new version's cobol.

If you programs use Accept/Display for data entry using X-Open or other extensions, such as DISPLAY AT nnnn, then expect much program rewriting if you change vendors.
```

###### ↳ ↳ ↳ Re: COBOL HELP

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2016-01-25T06:02:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9a6e19fd1f-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9a6e19fd1f-p6@usenetarchives.gap>`
- **References:** `<80d96265-eeae-4cc0-8574-d89e0187074f@googlegroups.com> <gap-9a6e19fd1f-p3@usenetarchives.gap> <gap-9a6e19fd1f-p6@usenetarchives.gap>`

```
Aleksandar Zubic wrote:
›› From which vendor? (COBOL-85 is a STANDARD. It is implemented by a
›› number of compiler vendors...)
…[52 more quoted lines elided]…
› additional question and help if needed

If you have Fujitsu NetCOBOL version 7 it will almost certainly compile your
existing source to 32 bit. You can then re-run the programs that create your
data and you will get proper 32 bit indexed files. Existing indexed data
files may still need conversion.

Pete.
"I used to write COBOL...now I can do anything."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
