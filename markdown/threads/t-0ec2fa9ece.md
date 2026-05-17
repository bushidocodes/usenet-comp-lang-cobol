[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Creating standalone exe-files

_4 messages · 4 participants · 1997-06_

---

### Creating standalone exe-files

- **From:** "cobol..." <ua-author-17071858@usenetarchives.gap>
- **Date:** 1997-06-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<339d54d0.8981631@news.calypso.net>`

```

i would like to have some more infoemation on how to create standalone
executables from MicroFocus cobol

i got a tip to use "obj" in the compiler directives, but i cant get it
to work.

so please give me a helping hand


/Stefan

email: cob··.@hot··l.com
```

#### ↳ Re: Creating standalone exe-files

- **From:** "chief..." <ua-author-647491@usenetarchives.gap>
- **Date:** 1997-06-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ec2fa9ece-p2@usenetarchives.gap>`
- **In-Reply-To:** `<339d54d0.8981631@news.calypso.net>`
- **References:** `<339d54d0.8981631@news.calypso.net>`

```

Use the compiler directive:
$SET OMF(OBJ)

This should give you an OBJ file that you can link to an EXE

COB -X:options programfile.obj

This will link the OBJ to an EXE file based on the options you chose.
```

#### ↳ Re: Creating standalone exe-files

- **From:** "ifb" <ua-author-4214812@usenetarchives.gap>
- **Date:** 1997-06-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ec2fa9ece-p3@usenetarchives.gap>`
- **In-Reply-To:** `<339d54d0.8981631@news.calypso.net>`
- **References:** `<339d54d0.8981631@news.calypso.net>`

```

you need just to link it to create a exe file
don't forget the extfh,adis,externl or other

bye
```

##### ↳ ↳ Re: Creating standalone exe-files

- **From:** "ronald young" <ua-author-982296@usenetarchives.gap>
- **Date:** 1997-06-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0ec2fa9ece-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0ec2fa9ece-p3@usenetarchives.gap>`
- **References:** `<339d54d0.8981631@news.calypso.net> <gap-0ec2fa9ece-p3@usenetarchives.gap>`

```

This is a multi-part message in MIME format.

--------------697872002E95
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit

IFB wrote:
›
› you need just to link it to create a exe file
› don't forget the extfh,adis,externl or other
›
› bye


Here's a little batch file I use to compile and
link directly into simple EXE files.

--------------697872002E95
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Content-Disposition: inline; filename="COB.BAT"

echo off
if not exist %1.CBL goto exit
set cobdir=\cobol30
COBOL %1;
if errorlevel 1 goto exit
LINK %1+%COBDIR%\ADIS+%COBDIR%\ADISKEY+%COBDIR%\ADISINIT;
if errorlevel 1 goto exit
echo Compile and Link complete with no errors.
:exit

--------------697872002E95--
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
