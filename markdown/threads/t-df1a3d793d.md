[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Netexpress

_2 messages · 2 participants · 1998-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus Netexpress

- **From:** vgibson@westga.edu (Vince Gibson)
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35916116.31571006@news.westga.edu>`

```

I have been asked to develop an application for personal use. This
program is a standard GUI PC based application which needs to be a
stand alone executable to run on a win95 machine. This application
collects information on a screen, saves it to a database(Access) table
and prints a form. I have the program written and debugged and it runs
fine on my NT machine with the development system. Now comes the part
where I make it stand alone.

I read through all the available documentation and did the following:

1. Set the build type to "Generic release build"
2. Highlighted the .exe and right clicked the mouse
3. Selected the build settings and then clicked the "Link" tab
4. Clicked "Static", "Single threaded", "Graphical", and "Link
animate"
5. Clicked "Advanced" and set the link level to "Full"

According to what the documentation says, that should link the runtime
system to the program and make it a stand alone .exe which can be
shipped to, and run on any PC. Unfortunately, I get the following
errors:

Starting rebuild
Rebuilding                RELEASE\VOUCAPRN1.EXE
TBSDI.OBJ : error LNK2001: unresolved external symbol _oops
SBAR.OBJ : error LNK2001: unresolved external symbol _oops
TBSDI.OBJ : error LNK2001: unresolved external symbol
_oopsgetclassobject
SBAR.OBJ : error LNK2001: unresolved external symbol
_oopsgetclassobject
TBSDI.OBJ : error LNK2001: unresolved external symbol _oopsresolve
SBAR.OBJ : error LNK2001: unresolved external symbol _oopsresolve
RELEASE\VOUCAPRN1.EXE : fatal error LNK1120: 3 unresolved externals
Rebuild complete with errors

I am at a loss as to what I am doing wrong. Is there some trick that
is not in the documentation? The entire development system is
installed on my machine, so all the necessary files should be there. I
also have the Microsoft Development kit installed from the second CD
on this machine. Calls to the win32api fail as well. The doc says that
if you have the MDK installed, API calls will work. 

So, I have managed to get two of the three types of available programs
to work. I desperately need to get this program to work. It is for one
of the big bosses and I have been working on it for three weeks. I
can't get it to compile. This is all I lack, to deploy it. I can't
install the runtime on every machine, and this application is going on
a laptop, so I can't put it on a server.

I have to make it a static stand alone executable.

HELP!!!!

Vince
Atlanta, GA
```

#### ↳ Re: Microfocus Netexpress

- **From:** <kenmullins@mindspring.com>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mrteq$lin$1@camel21.mindspring.com>`
- **References:** `<35916116.31571006@news.westga.edu>`

```

Try linking using the shared runtime system...You can deploy the app with
the cblrtss.dll (single threaded) and the msvcrt.dll...This should
work...Seems to me I remember reading somewhere that the MF OO stuff
requires the shared runtime, and doesn't work with a static linked
program...Hence the unresolved references...

You should not need all of the redist files from the cd on each
machine...You just need to pick the ones your app needs...

KenMullins
Atlanta, GA

Vince Gibson wrote in message <35916116.31571006@news.westga.edu>...
>I have been asked to develop an application for personal use. This
>program is a standard GUI PC based application which needs to be a
…[53 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
