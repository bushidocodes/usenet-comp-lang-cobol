[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problems with MF Workbench 4.0.7 and COMMDLG32.DLL

_7 messages · 5 participants · 1998-02_

---

### Problems with MF Workbench 4.0.7 and COMMDLG32.DLL

- **From:** "mark warner" <ua-author-2311718@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34e0c3a5.0@news2.ibm.net>`

```

Just installed MF Workbench 4.0.7 and am continually getting the message
"cannot find commdlg32.dll". The installation went fine without any errors,
but I'm unable to get past the message. Has anybody seen this, and
hopefully have an answer..

Thanks in advance..
Mark Warner
```

#### ↳ Re: Problems with MF Workbench 4.0.7 and COMMDLG32.DLL

- **From:** "karl wagner" <ua-author-12514286@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be1166b9cf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34e0c3a5.0@news2.ibm.net>`
- **References:** `<34e0c3a5.0@news2.ibm.net>`

```

Did you install the Microsoft Win32 SDK which also ships on the CD but
must be installed separately? comdlg32.dll is in the SDK. The other
thing you should do is wander over to http://www.microfocus.com and
download the updates to 4.0.32.


Karl Wagner


Mark Warner wrote:
› 
› Just installed MF Workbench 4.0.7 and am continually getting the message
…[5 more quoted lines elided]…
› Mark Warner
```

#### ↳ Re: Problems with MF Workbench 4.0.7 and COMMDLG32.DLL

- **From:** "aaron lewis" <ua-author-813170@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be1166b9cf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34e0c3a5.0@news2.ibm.net>`
- **References:** `<34e0c3a5.0@news2.ibm.net>`

```

I've had MF Workbench 4.0.7 for some time now and have just recently
started using it. I too was frustrated by the insistent "cannot find
commdlg32.dll" message. My installation files are on diskette and nowhere
do I find the Win32 SDK mentioned by Karl. Is there another way to get
around this problem? I registed the dll, still no go.

Aaron Lewis
```

##### ↳ ↳ Re: Problems with MF Workbench 4.0.7 and COMMDLG32.DLL

- **From:** "karl wagner" <ua-author-12514286@usenetarchives.gap>
- **Date:** 1998-02-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be1166b9cf-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-be1166b9cf-p3@usenetarchives.gap>`
- **References:** `<34e0c3a5.0@news2.ibm.net> <gap-be1166b9cf-p3@usenetarchives.gap>`

```

Aaron Lewis wrote:
› 
› I've had MF Workbench 4.0.7 for some time now and have just recently
…[5 more quoted lines elided]…
› Aaron Lewis

COMMDLG32.DLL is a Microsoft system DLL which provides support for the
'Common' controls like ListViews, PropertySheets, etc. It should be in
your WINNT\System32 directory (NT) or Windows\System directory (Win95).
It's probably there or your system would be having some serious
problems, so I suspect the problem is with configuration.

Use the 'Find' function on the Windows 'start' menu to confirm the DLLs
are present. If they are, make sure the PATH environment variable
includes the directory (highly likely since they are supposed to be in
the system directory). As a last resort, check if the PATH has any
directories with long filenames which have embedded spaces. I've had
some problems in the past where development tools misbehave.

Karl Wagner
```

###### ↳ ↳ ↳ Re: Problems with MF Workbench 4.0.7 and COMMDLG32.DLL

- **From:** "david mowat" <ua-author-4670319@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be1166b9cf-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-be1166b9cf-p4@usenetarchives.gap>`
- **References:** `<34e0c3a5.0@news2.ibm.net> <gap-be1166b9cf-p3@usenetarchives.gap> <gap-be1166b9cf-p4@usenetarchives.gap>`

```


Karl Wagner wrote in message <34E··.@sym··o.ca>...
› Aaron Lewis wrote:
›› 
…[22 more quoted lines elided]…
› Karl Wagner

Yes I can confirm that long path names (over 66 chars in a path) can produce
the comdlg32.dll error. Scandisk will find this error.
David.
```

##### ↳ ↳ Re: Problems with MF Workbench 4.0.7 and COMMDLG32.DLL

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-02-15T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be1166b9cf-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-be1166b9cf-p3@usenetarchives.gap>`
- **References:** `<34e0c3a5.0@news2.ibm.net> <gap-be1166b9cf-p3@usenetarchives.gap>`

```

Aaron,

Workbench 4.0.07 was released before NT 4. Microsoft changed things in NT 4
and this led to the error you are experiencing. Micro Focus fixed this
problem many months ago and you need to update your product to 4.0.32. This
update can be downloaded from our web site.

ftp://ftp.microfocus.com/pub/updates/cobol-workbench-v4.0/non-security-keyed
/Windows-NT-95/

You need to download the c4032wu?.zip files to your PC. Unzip them in a
directory and run the update program.

Hope this helps.

Paddy Coleman
Team Leader, UK Distributed Computing Support (WinTel)
Micro Focus.

Aaron Lewis wrote in message <01bd38b6$eb61cb20$8351b6cc@MAIN133>...
› I've had MF Workbench 4.0.7 for some time now and have just recently
› started using it.  I too was frustrated by the insistent "cannot find
…[4 more quoted lines elided]…
› Aaron Lewis
```

##### ↳ ↳ Re: Problems with MF Workbench 4.0.7 and COMMDLG32.DLL

- **From:** "paddy coleman" <ua-author-4477990@usenetarchives.gap>
- **Date:** 1998-02-15T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be1166b9cf-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-be1166b9cf-p3@usenetarchives.gap>`
- **References:** `<34e0c3a5.0@news2.ibm.net> <gap-be1166b9cf-p3@usenetarchives.gap>`

```

Aaron,

Workbench 4.0.07 was released before NT 4. Microsoft changed things in NT 4
and this led to the error you are experiencing. Micro Focus fixed this
problem many months ago and you need to update your product to 4.0.32. This
update can be downloaded from our web site.

ftp://ftp.microfocus.com/pub/updates/cobol-workbench-v4.0/non-security-keyed
/Windows-NT-95/

You need to download the c4032wu?.zip files to your PC. Unzip them in a
directory and run the update program.

Hope this helps.

Paddy Coleman
Team Leader, UK Distributed Computing Support (WinTel)
Micro Focus.

Aaron Lewis wrote in message <01bd38b6$eb61cb20$8351b6cc@MAIN133>...
› I've had MF Workbench 4.0.7 for some time now and have just recently
› started using it.  I too was frustrated by the insistent "cannot find
…[4 more quoted lines elided]…
› Aaron Lewis
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
