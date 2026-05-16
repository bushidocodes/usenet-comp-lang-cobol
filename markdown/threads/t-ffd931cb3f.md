[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Associating an icon with an executable

_1 message · 1 participant · 1998-12_

---

### Associating an icon with an executable

- **From:** dblaze@merchants-fla.com
- **Date:** 1998-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3687d26d.18162576@news.icix.net>`

```
I have a program written in MicroFocus 4.0.32 and want to add an icon
to the executable so that in InstallShield, I can create the a desktop
shortcut with the icon.  I checked the MF documentation and I found
information on the Resource Compiler.  My application is called
msepc.exe and the icon I want to add to the exe is msepc.ico.  The MF
instructions said to make a .rc file with the following line:
    msepc.exe icon msepc.ico
then run the Resource Compiler:
    rc -r msepc.rc
the output of which is msepc.res (this is created).
After compiling and linking the app, use this command to attach the
.res file to .exe:
    rc msepc.res
I get the following error:
    RC: fatal error RC1208: input file has .RES extension

Any ideas?

Thanks,
Doug
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
