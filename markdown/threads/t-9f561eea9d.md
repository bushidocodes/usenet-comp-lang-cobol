[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP: Micro Focus Runtime error.....

_3 messages · 3 participants · 1997-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### HELP: Micro Focus Runtime error.....

- **From:** "scha..." <ua-author-17072361@usenetarchives.gap>
- **Date:** 1997-02-06T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5dfc5c$j0c@simba.cnsnet.com>`

```

We are running Micro Focus, 3.0/3.1, and have run into a runtime error
but I can't seem to find the runtime error book that can hopefully give me
the answer to this error.

The error is : Runtime error R6009
Out of Enviroment Space.

Does anyone have then answer as to what I need to change on this PC
to stop this error? The system is running DOS ver. 6.22.

Thanks,
Paul
```

#### ↳ Re: HELP: Micro Focus Runtime error.....

- **From:** "ads" <ua-author-17072050@usenetarchives.gap>
- **Date:** 1997-02-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9f561eea9d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5dfc5c$j0c@simba.cnsnet.com>`
- **References:** `<5dfc5c$j0c@simba.cnsnet.com>`

```

sch··.@ri··s.com (Paul Schaller) wrote:


› The error is : Runtime error R6009
› Out of Enviroment Space.

add this to your config.sys file:
shell=c:\command.com /p /e:2048
to give 2048 bytes for environment
If your command.com is not in C:\ make sure to point to it.
Broken config.sys can stop your pc booting, so be sure to have a boot
floppy in case.

Al
```

#### ↳ Re: HELP: Micro Focus Runtime error.....

- **From:** "steve burns" <ua-author-645539@usenetarchives.gap>
- **Date:** 1997-02-06T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9f561eea9d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5dfc5c$j0c@simba.cnsnet.com>`
- **References:** `<5dfc5c$j0c@simba.cnsnet.com>`

```

Paul Schaller wrote:
› 
› We are running Micro Focus, 3.0/3.1, and have run into a runtime error
…[10 more quoted lines elided]…
› Paul

I don't have a book that shows that error number, but environment space
is the area of an operating system that is used to hold system
variables. Things like the path and all the Micro Focus variables go
into that area. You don't say which operating system you are using, so
the answer to your problem cant be stated. If you are using DOS and
windows 3.x, you need to increase the environment on the puters where
the application is running.

I no longer have any information about the specific fix, but you can
find it you documents with examples for the autoexec.bat and config.sys.
This is a good reason to upgrade to Micro Focus version 4.0....

*****************************************************************
* Steve Burns    The Boeing Co.    I'm not sure if I subscribe  *
* PO Box 3707    Mail Stop 2L-14   to these opinions, I'm sure  *
* (206) 544-8264 Seattle, WA 98124    that Boeing doesn't.      *
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
