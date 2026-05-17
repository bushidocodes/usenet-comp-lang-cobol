[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ibm thinkpad & micro focus cobol

_3 messages · 2 participants · 1995-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Ibm thinkpad & micro focus cobol

- **From:** "kim..." <ua-author-3680929@usenetarchives.gap>
- **Date:** 1995-01-16T20:27:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff6da$iqm@ns>`

```

vesa.exe conflicts with mf rts if it is placed in config.sys. I moved it to autoexec
after setting all rts env's, then it works ok.

Similar (related ?) problem: carbon copy (terminal mode - other modes work fine) and
procomm locks both valuepoint and thinkpad - if emm has noems switch.

Another problem: some mf intrinsic functions lock these machines as well.

Does anyone have solutions for these?
```

#### ↳ Re: Ibm thinkpad & micro focus cobol

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-01-18T13:46:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b2b5fcd4fb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3ff6da$iqm@ns>`
- **References:** `<3ff6da$iqm@ns>`

```

In article <3ff6da$iqm@ns>, kim··.@bro··l.com (kimsoft) writes:
›
› Another problem: some mf intrinsic functions lock these machines as well.
› Does anyone have solutions for these?

Please post example code for each intrinsic function that fails, or contact
Micro Focus technical support.

Kev.

Kevin.			 Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

#### ↳ Re: Ibm thinkpad & micro focus cobol

- **From:** "kim..." <ua-author-3680929@usenetarchives.gap>
- **Date:** 1995-01-20T10:13:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b2b5fcd4fb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3ff6da$iqm@ns>`
- **References:** `<3ff6da$iqm@ns>`

```
In article <3fjhbp$o.··.@ice··o.uk>, s.··.@mfl··o.uk says...
› 
› kim··.@bro··l.com (kimsoft) wrote:
…[23 more quoted lines elided]…
› 
Thanks for the info. I am using a pre-relase version of MF V 3.2.20 and have a
number of odds and ends attached to my thinkpad. May be one (or more) of the
attached is causing the conflict? I use MS DOS 6.2, Novell 4.x, FTP winsock,
Netscape, NCSA httpd server and APEX fax/modem.

Perhaps, you can spot my problem(s). My autoexec and config are given below (much of
which was 'pre-loaded' by IBM):

LH c:¥dos¥smartdrv.exe

SET READIBM=C:¥READIBM¥READIBM.PRO

set TZ=EST5EDT

PATH=C:¥;C:¥DOS;C:¥WINDOWS;C:¥THINKPAD;¥f:¥public
path=%PATH%;c:¥CCMOBILE;C:¥MONOLOGW;C:¥READIBM

SET TEMP=C:¥TEMP
SET IBMAV=C:¥DOS
SET WIN$=C:¥WINDOWS
lh C:¥DOS¥MOUSE.COM /Y
LH C:¥DOS¥DOSKEY.COM
LH C:¥DOS¥SHARE.EXE

set pctcp=c:¥explore¥pctcp.ini
c:¥explore¥vxdinit.exe

lh c:¥dos¥mode con: rate=32 delay=1

set path=c:¥explore;%path%

set K=c:
set M=c:
set USER=MAS
set KCOMP=0001
set CARBON=c:

if exist %K%¥prnsav.doc del %K%¥prnsav.doc
lh %K%¥kimdos¥prn2file %K%¥prnsav.doc

call %K%¥kim¥mfrun¥setpath
rem
rem Moved from config.sys
rem
C:¥IBMVESA¥VESA.EXE
-------------------------------------
rem config.sys

DEVICE=C:¥DOS¥HIMEM.SYS
DEVICE=C:¥DOS¥EMM386.EXE NOEMS X=C800-CFFF I=E000-E5FF

shell=c:¥dos¥command.com c:¥dos¥ /e:1526 /p
DOS=HIGH,UMB

FILES=99
BUFFERS=20
STACKS=9,256

DEVICE=C:¥DOS¥POWER.EXE
DEVICEHIGH=C:¥THINKPAD¥IBMDSS01.SYS
DEVICEHIGH=C:¥THINKPAD¥IBMDOSCS.SYS
DEVICEHIGH=C:¥THINKPAD¥DICRMU01.SYS /MA=C800-CFFF
DEVICEHIGH=C:¥THINKPAD¥$ICPMDOS.SYS
DEVICEHIGH=C:¥THINKPAD¥AUTODRV.SYS C:¥THINKPAD¥AUTODRV.INI
REM DEVICEHIGH=C:¥IBMVESA¥VESA.EXE ===> moved to autoexec.bat

LASTDRIVE=Z

Thanks for your help.

I use more or less the same setup on compaq, compadd and toshiba with no problem with
carbon copy, procomm, cobol, etc.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
