[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help requested ... need direction

_4 messages · 3 participants · 2000-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help requested ... need direction

- **From:** Steve Burg <webmaster@fortbendweb.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DFAD93.7E0B387E@fortbendweb.com>`

```
Greetings,

I have a client that lost their hard drive.  This was an old SCO Unix
3.2v4.x system with 2 MFM drives.  Yes...MFM.  Since they have recently
upgraded to a new system and software, they want to printout all of
their old data.  So I am trying to run the application on my SCO OSR5
box, and I see the following error...

COBOL procedure error 204. Error loading main program.

The COBOL Info is as follows:

RM/COBOL-85 Runtime  (Ver 2.02.05)  for XENIX. Configured for 016 users.

(c) Copyright 1985, 1986 by Ryan-McFarland Corp.  All rights reserved.

I did notice that it states XENIX, but it was running fine on SCO Unix
3.2v4.x.......

Any suggestions...

Thanks,
Steve Burg
```

#### ↳ Re: Help requested ... need direction

- **From:** jgill_1@my-deja.com
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bod8r$m60$1@nnrp1.deja.com>`
- **References:** `<38DFAD93.7E0B387E@fortbendweb.com>`

```


> COBOL procedure error 204. Error loading main program.

Steve:

I have run RM-Cobol (Ver 2.01) on a DOS system and the error 204
means that the Run-Time program could not locate the program
to load it into memory. On DOS, there is an environment variable
called RUNPATH that points to a directory that should be searched
when the called program is not in the current directory.
Example: SET RUNPATH=C:\COBOL


I don't know if XENIX/UNIX uses the same procedure.

Are the programs in the current directory when the RUN command
is executed ?

John Gill   (jdgill@juno.com)




Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Help requested ... need direction

- **From:** Steve Burg <webmaster@fortbendweb.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DFCD21.55214873@fortbendweb.com>`
- **References:** `<38DFAD93.7E0B387E@fortbendweb.com> <8bod8r$m60$1@nnrp1.deja.com>`

```
I will check the script and verify path and environment variables.  I'll
get back to you.

Thanks.


jgill_1@my-deja.com wrote:

> > COBOL procedure error 204. Error loading main program.
>
…[17 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Help requested ... need direction

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4uk2esgn98it5afh8jd0nukvlh697ggpbu@4ax.com>`
- **References:** `<38DFAD93.7E0B387E@fortbendweb.com> <8bod8r$m60$1@nnrp1.deja.com>`

```
jgill_1@my-deja.com wrote:

>Example: SET RUNPATH=C:\COBOL


>I don't know if XENIX/UNIX uses the same procedure.

>Are the programs in the current directory when the RUN command
>is executed ?

if you don't know, it's best to write a file existance test as well in
the code. nothing like 20 years later when a programmer moves the
file, and a month later a user runs it and it crashes.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
