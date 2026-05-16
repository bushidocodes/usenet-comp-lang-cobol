[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# debug VS release

_2 messages · 2 participants · 2003-10_

---

### debug VS release

- **From:** Donald Tees <Donald_Tees@sympatico.ca>
- **Date:** 2003-10-15T12:44:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1Rejb.7418$cT6.345836@news20.bellglobal.com>`

```
I am working with an older project in MS NetExpress, biult with lots of 
modules, calls, cancels, etc.  I am able to build and execute the 
program with no problems in debug mode, and as INTS it runs just fine. 
When I re-compile it as a large executable or DLL, however, I get file 
lock errors that do not appear with the INTS.

The situation is that both a main module and a sub-module are using the 
same file, and both open with locks automatic. The main module opens a 
file, closes it, then calls the submodule.  The submodule does the same.

With INTS, this works fine.  With the EXE the second module barfs, and 
jumps to the lock exception in the declaratives.

Any ideas on why anyone?

Donald
```

#### ↳ Re: debug VS release

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-10-15T14:44:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3485518.1066243476@dbforums.com>`
- **References:** `<1Rejb.7418$cT6.345836@news20.bellglobal.com>`

```

Dear Sir,



I had many problems with EXE. Today my EXE count only the menu selector.

An operation of more select calculations generated mistakes.

I recommend to do the same.



respectfully
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
