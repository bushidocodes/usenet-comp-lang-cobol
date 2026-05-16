[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New user on Fujitsu COBOL V3 help me

_7 messages · 7 participants · 1999-03 → 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### New user on Fujitsu COBOL V3 help me

- **From:** Alain Chappuis <Alain.Chappuis@medecine.unige.ch>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F8A59F.4AEFF02@medecine.unige.ch>`

```
Hello
I'm a new user on Fujitsu COBOL V3 and I need some help.

After I installed the compilator under NT4 SP4, and I reading
the manual "Getting Started with Fujitsu COBOL". In the
application "Programming Staff" I open my file .COB no problem.
But when I trying to use Tools and any option in, in particular
WINCOB[Compile...] it does not occur anything at all! 

No box open for asking me for the file to compile.
Did I forget parameter something? 

Thank you in advance for your help.

Ps: my compiler is installed on c:\Program File\Cobol3 not in
the default proposed by Fujitsu!

Alain
```

#### ↳ Re: New user on Fujitsu COBOL V3 help me

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F9A09B.2A08@netbox.com>`
- **References:** `<36F8A59F.4AEFF02@medecine.unige.ch>`

```
Alain Chappuis wrote:
> But when I trying to use Tools and any option in, in particular
> WINCOB[Compile...] it does not occur anything at all!
> 
> Ps: my compiler is installed on c:\Program File\Cobol3 not in
> the default proposed by Fujitsu!

I made the same mistake the first time I installed it.  V3 will not
handle directory names longer than 8 characters.  If you search the
registry carefully, and change the paths to c:\Progra~1\...you can get
it to work, but I found that it was much easier to reinstall using their
defaults.

Bob
```

##### ↳ ↳ Re: New user on Fujitsu COBOL V3 help me

- **From:** "Hajo Schepker" <schepker@geocities.com>
- **Date:** 1999-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7dgea9$aqn$1@namib.north.de>`
- **References:** `<36F8A59F.4AEFF02@medecine.unige.ch> <36F9A09B.2A08@netbox.com>`

```
V3 can handle directories with more than 8 characters, only watch, if threre
is no space in the directory-name.
```

#### ↳ Re: New user on Fujitsu COBOL V3 help me

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7damg1$o1$1@news.igs.net>`
- **References:** `<36F8A59F.4AEFF02@medecine.unige.ch>`

```
You have to set up a project ... the pstaff program is a full project
manager with projects, editor, etc. all built in.  Try opening a project
(use one of the samples), then compiling.  Once you see that, you should
have no problem setting up a project, and sticking your own Cobol into it.

Alain Chappuis wrote in message <36F8A59F.4AEFF02@medecine.unige.ch>...
>Hello
>I'm a new user on Fujitsu COBOL V3 and I need some help.
…[25 more quoted lines elided]…
>+----------------------+-------------------------------------------+
```

#### ↳ Re: New user on Fujitsu COBOL V3 help me

- **From:** "Ian Stoddart" <Ian@stoddart60.freeserve.co.uk>
- **Date:** 1999-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be7cdd$9722a7c0$da1e883e@stodfamily.u-net.com>`
- **References:** `<36F8A59F.4AEFF02@medecine.unige.ch>`

```
Alain Chappuis <Alain.Chappuis@medecine.unige.ch> wrote in article
<36F8A59F.4AEFF02@medecine.unige.ch>...
> Hello
> I'm a new user on Fujitsu COBOL V3 and I need some help.
…[26 more quoted lines elided]…
> 


Alain,
I think your problem is in the directory name "program files".  See Support
FAQ COBOL V3 on the Fujitsu web site.

Point 3 says "Fujitsu COBOL does not work correctly if a directory contains
a blank".
Point 4 says "Fujitsu COBOL does not compile correctly if a directory in
the path or the file name contains a blank".

So Fujitsu, why make the default install directory C:\Program
Files\...........?
Regards,
Ian.
```

##### ↳ ↳ Re: New user on Fujitsu COBOL V3 help me

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3704e746.404508249@news1.ibm.net>`
- **References:** `<36F8A59F.4AEFF02@medecine.unige.ch> <01be7cdd$9722a7c0$da1e883e@stodfamily.u-net.com>`

```
On 2 Apr 1999 07:54:33 GMT, "Ian Stoddart"
<Ian@stoddart60.freeserve.co.uk> wrote:

>
>So Fujitsu, why make the default install directory C:\Program
>Files\...........?
>Regards,
>Ian.

In their defense, the default install is \FSC
```

##### ↳ ↳ Re: New user on Fujitsu COBOL V3 help me

- **From:** "Gary Roush" <gkr@adtools.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XShO2.248$Bs3.33588@news20.ispnews.com>`
- **References:** `<36F8A59F.4AEFF02@medecine.unige.ch> <01be7cdd$9722a7c0$da1e883e@stodfamily.u-net.com>`

```
Ian,

The default directory is C:\FSC    and has been for a long time.
Unfortunately the user can change it and if they don't follow instructions
according to the book regarding spaces in the folder, there will be
problems. To anyone that has done this, I would recommend uninstalling the
Fujitsu COBOL program completely and install it again and be sure to accept
the defaults as <drive>:\FSC and go from there. Then what the programmer
wants to do will start working.

Regards,
Gary Roush
Fujitsu COBOL Support



Ian Stoddart wrote in message
<01be7cdd$9722a7c0$da1e883e@stodfamily.u-net.com>...
>Alain Chappuis <Alain.Chappuis@medecine.unige.ch> wrote in article
><36F8A59F.4AEFF02@medecine.unige.ch>...
…[32 more quoted lines elided]…
>I think your problem is in the directory name "program files".  See
Support
>FAQ COBOL V3 on the Fujitsu web site.
>
>Point 3 says "Fujitsu COBOL does not work correctly if a directory
contains
>a blank".
>Point 4 says "Fujitsu COBOL does not compile correctly if a directory in
…[5 more quoted lines elided]…
>Ian.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
