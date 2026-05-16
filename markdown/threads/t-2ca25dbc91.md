[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# fix for RTS load failure error

_1 message · 1 participant · 2002-01_

---

### fix for RTS load failure error

- **From:** ant_eater_98@yahoo.com (somthing)
- **Date:** 2002-01-31T09:31:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95ace044.0201310931.5df29917@posting.google.com>`

```
What Operating System are you using?
If it is Windows 2000 or Windows XP then use the following procedures:

To install Personal COBOL under Windows XP and Windows 2000 do the
following:

1. Place the Personal COBOL CD-ROM into the drive.
2. Select Start Menu and Run.
3. Select Browse from the Run menu and select the CD-ROM drive (D on my
system) and select D:\SETUP.EXE,
4. Run Setup.
5. The Setup Welcome screen is displayed - Press OK to continue.
6. Enter your name and company at the next screen and Press OK.
7. Press Yes at the next screen when prompted to check your name.
8. At the next screen accept the default installation directory name of
C:\PCOBWIN and press OK.
9. You will then be prompted to select the programs to install. Check 
both
Personal COBOL for Windows and Personal Dialog System and Press OK.
10. You will be prompted for the name of the Program Group. Accept the
default of Personal COBOL.
11. A screen will then be displayed allowing you to select if you would 
like
to modify your autoexec.bat file.

Select "Leave" so that it will not modify your settings.

12. Personal COBOL will then be installed. You will get a message that 
your
environment variables need to set. Click OK and Exit out of the 
Personal
COBOL group.

To modify your system settings do the following:

1. From the Start Menu select Control Panel. Then select Performance 
and
Maintenance and then the System icon at the bottom.
2. From the System Properties menu select the Advanced Tab and press 
the
Environment Variables button.
3. Under the User Variables selection highlight PATH and select Edit. 
To the
end of the current PATH add the following:
;C:\PCOBWIN and press OK.
4. Select New for each of the remaining options to create a new 
environment
variable and setting.

Name Settings

COBDIR C:\PCOBWIN
COBCPY C:\PCOBWIN\CLASSLIB
COBHNF C:\PCOBWIN
DSGDIR C:\PCOBWIN
COBSW +p3/s14000

When you are done Press OK and then OK again to exit.

Then download the patch for Windows 2000 at:
http://www.merant.com/services/aprograms/aprograms_support.asp
Personal COBOL should then start.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
