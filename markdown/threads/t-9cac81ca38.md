[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol .exe file

_2 messages · 2 participants · 1999-09_

---

### cobol .exe file

- **From:** CrazedHope <rkowalc@my-deja.com>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sdsg9$jl0$1@nnrp1.deja.com>`

```
 I'm trying to make an .exe file using microfocus cobol.  Does anyone
know how to do that or give a reference for it?
```

#### ↳ Re: cobol .exe file

- **From:** JohndeV <johndevNOhwSPAM@yahoo.com>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<026faffc.190c4409@usw-ex0108-057.remarq.com>`
- **References:** `<7sdsg9$jl0$1@nnrp1.deja.com>`

```
You did not say what version you have of Micro Focus.and on
what platform you were running.

But anyway, here goes.

First compile your program;

COBOL programname.CBL omf"obj";

If you use an old 16bit version just do

XM COBOL programname.CBL omf"obj";

Then link your program.  With recent versions of Micro Focus
you can do the following;

For a Static linked EXE; CBLLINK -T programname
For a Shared runtime EXE; CBLLINK programname

If you want to know what other parameters you can use with
CBLLINK, just type CBLLINK at a command prompt and press 
ENTER.

For linking with older versions of MF I suggest that you
have a look at your documentation.

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
