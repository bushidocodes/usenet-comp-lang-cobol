[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Win32API and file execution?

_6 messages · 6 participants · 2000-07 → 2000-08_

---

### Win32API and file execution?

- **From:** rezeerf@my-deja.com
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8l14qt$9j3$1@nnrp1.deja.com>`

```
Hi!

Hope you can help me:

How can i execute a file i.e. exe-file out of a cobol-source (netexpress
3.0) using the win32api or something similar ?

Thanx in advance

alex


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Win32API and file execution?

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8l1b5v$6ku$1@hyperion.mfltd.co.uk>`
- **References:** `<8l14qt$9j3$1@nnrp1.deja.com>`

```
> How can i execute a file i.e. exe-file out of a cobol-source (netexpress
> 3.0) using the win32api or something similar ?
…[4 more quoted lines elided]…
>

Alex, you can execute an EXE using the CBL_EXEC_RUN_UNIT call. You don't
need to make a Win32 API call to do it.
```

##### ↳ ↳ Re: Win32API and file execution?

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2000-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000719210526.20102.00000108@ng-cq1.aol.com>`
- **References:** `<8l1b5v$6ku$1@hyperion.mfltd.co.uk>`

```
Hi Alex,

If you would like send me an e-mail and I will send you an example of the
CreateProcess API you can use.

Bob Hennessey
```

###### ↳ ↳ ↳ Re: Win32API and file execution?

- **From:** trinh <trinhNOtrSPAM@aol.com.invalid>
- **Date:** 2000-07-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190c8d3.66ffe686@usw-ex0104-025.remarq.com>`
- **References:** `<8l1b5v$6ku$1@hyperion.mfltd.co.uk> <20000719210526.20102.00000108@ng-cq1.aol.com>`

```
hi alex u can use win api creatprocess..to execute your process..
this have the option where u can hide the black screen that will
appear on your monitor.  i think there this an example on
microfocus web


-----------------------------------------------------------

Got questions?  Get answers over the phone at Keen.com.
Up to 100 minutes free!
http://www.keen.com
```

#### ↳ Re: Win32API and file execution?

- **From:** "Tom Wright" <twright@larimore.net>
- **Date:** 2000-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y9%f5.37$Ug.210485@news1.i1.net>`
- **References:** `<8l14qt$9j3$1@nnrp1.deja.com>`

```
You can also use winexec api.  Much simpler to use
Tom
<rezeerf@my-deja.com> wrote in message news:8l14qt$9j3$1@nnrp1.deja.com...
> Hi!
>
…[11 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Win32API and file execution?

- **From:** "Grinder" <no.spam@no.spam.spam.spam.net>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Q0kl5.8839$T73.438147@nntp1.onemain.com>`
- **References:** `<8l14qt$9j3$1@nnrp1.deja.com> <y9%f5.37$Ug.210485@news1.i1.net>`

```
WinExec should only be used if you plan to run on 16-bit systems, the 32-bit
counterparts are ShellExecute or CreateProcess.

ShellExecute gives you the ability to "execute" documents.  The associated
exe will be looked up and used to open the data file.  You can even do other
shell operations like "print" or "send."

CreateProcess is a bit complicated, but gives you buenos control over the
execution.  Google should be able to help you find specific examples.


"Tom Wright" <twright@larimore.net> wrote in message
news:y9%f5.37$Ug.210485@news1.i1.net...
> You can also use winexec api.  Much simpler to use
> Tom
…[16 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
