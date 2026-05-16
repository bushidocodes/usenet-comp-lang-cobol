[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MS/MF Cobol 16bit and Windows NT 4.0

_4 messages · 3 participants · 2001-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MS/MF Cobol 16bit and Windows NT 4.0

- **From:** "Frank.Saur" <Frank.Saur@t-online.de>
- **Date:** 2001-02-02T11:44:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95e2s7$gbd$07$1@news.t-online.com>`

```
Hi,

i have installed the Microsoft / Micro Focus V 4.5 Cobol Software (16-bit)
on Windows NT 4.0. If I start the compiler i get an error message:

Cobol run time library not installed

If i boot good old DOS (same environment-variables set as in nt) it works.

Can anyone tell me what I should try?

Thanks

Frank
```

#### ↳ Re: MS/MF Cobol 16bit and Windows NT 4.0

- **From:** "Tom Wright" <twright@@larimore.net>
- **Date:** 2001-02-02T10:39:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqBe6.1338$9r5.214917@news1.primary.net>`
- **References:** `<95e2s7$gbd$07$1@news.t-online.com>`

```
Are you sure that your environment variables are getting set int NT.
Microfocus sets the variables according to the user profile.  If you
installed MF under one user and try to run it under another it may not work.
Try moving the environment variables to the system variables that way
they'll be loaded no matter who logs in.  You can check to see if the
environment variables are being set in both by going to a DOS prompt in NT
and typing SET.  If the info scrolls off the screen the type SET |(<--also
known as a pipe)MORE that should list a page at a time.  Look to see that
the variables are being set.

Hope this helps
Tom
"Frank.Saur" <Frank.Saur@t-online.de> wrote in message
news:95e2s7$gbd$07$1@news.t-online.com...
> Hi,
>
…[13 more quoted lines elided]…
>
```

#### ↳ Re: MS/MF Cobol 16bit and Windows NT 4.0

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-03T09:05:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A7BC9EC.2A07E039@Azonic.co.nz>`
- **References:** `<95e2s7$gbd$07$1@news.t-online.com>`

```
Frank.Saur wrote:
> i have installed the Microsoft / Micro Focus V 4.5 Cobol Software (16-bit)
> on Windows NT 4.0. If I start the compiler i get an error message:
> 
> Cobol run time library not installed

MS Cobol 4.5 has real mode (DOS) and protected mode (OS/2) run times. 
When started it finds protected mode available and tries to load the
OS/2 version.  This is failing.  One way around this is to use FORCEDOS
to start it ensuring only the real mode is detected.

Isn't this in the FAQ ?
```

##### ↳ ↳ Re: MS/MF Cobol 16bit and Windows NT 4.0

- **From:** juergen_ibelgaufts <juergen.ibelgaufts@copewithcytokines.de>
- **Date:** 2001-02-03T12:54:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A7BF187.A5FCF1E4@copewithcytokines.de>`
- **References:** `<95e2s7$gbd$07$1@news.t-online.com> <3A7BC9EC.2A07E039@Azonic.co.nz>`

```
Hello,

the OS/2 protected mode runs very well on winnt and win2k. You simply
have to add the path to the binp directory inside your cobol
installation for example on the command line (set
os2libpath=%os2libpath%c:\cobol\binp or whatever your directory name
is). Running the OS2 runtime is much faster and more convenient than the
DOS runtime because you will not run into these memory limitations.

Greetings
Juergen Ibelgaufts

---------------------------------

Richard Plinston wrote:
> 
> Frank.Saur wrote:
…[10 more quoted lines elided]…
> Isn't this in the FAQ ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
