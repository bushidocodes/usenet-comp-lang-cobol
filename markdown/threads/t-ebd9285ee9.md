[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Clients not seeing FileShare NLM

_2 messages · 1 participant · 1997-08_

---

### Clients not seeing FileShare NLM

- **From:** "greg coles" <ua-author-17071942@usenetarchives.gap>
- **Date:** 1997-08-10T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bca690$0ad0f8a0$8464a8c0@greg>`

```

If I start Microfocus' FileShare on a PC, then execute programs designed to
use FileShare on another PC, everything works fine, the programs are able
to go through FileShare to access the files on the server. However, if I
load the FileShare NLM on the server and execute the same programs, they
act as if the FileShare is not running... I get a 124 error message. Any
ideas what I'm doing wrong? Command line I'm using to load is...
LOAD FS /S DRB /CM CCIIPX.
Gregory L. Coles
Yakima Hardware Company
509-453-3181
har··.@y··.com
```

#### ↳ Re: Clients not seeing FileShare NLM

- **From:** "greg coles" <ua-author-17071942@usenetarchives.gap>
- **Date:** 1997-08-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebd9285ee9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bca690$0ad0f8a0$8464a8c0@greg>`
- **References:** `<01bca690$0ad0f8a0$8464a8c0@greg>`

```

Thought I would add my own update to this problem. Microfocus responded to
my original posting with the following and it worked.
-------------------------------------------
Greg,
You need to specify the machine address when contacting a Fileshare
Server that is running on the NetWare machine (you should find docs on
this with Fileshare NLM).

To briefly summarise:
run slist on the workstation (or: nlist server /b) and add the address
of the server that Fileshare NLM is running on to an fhredir.cfg file as
follows:

/ma 10102.1 /s nlmsrv1

where nlmsrv1 is the name you've given to the Fileshare server.
For example, if your current fhredir.cfg says:

/s nlmsrv1

to tell FHREDIR to redirect everything to nlmsrv1, then it needs to be
changed to read:

/s nlmsrv1
/ma 10102.1 /s nlmsrv1

to tell it to use machine address 10102.1 (or whatever is relevant to
you) when conatcting nlmsrv1.

Hope this helps,

D. Gwyn Jones.
Fileshare Delvelopment, Micro Focus UK.
› ----------
Gregory L. Coles
Yakima Hardware Company
509-453-3181
har··.@y··.com

Greg Coles  wrote in article
<01bca690$0ad0f8a0$8464a8c0@greg>...
> If I start Microfocus' FileShare on a PC, then execute programs designed
to
> use FileShare on another PC, everything works fine, the programs are able
> to go through FileShare to access the files on the server.  However, if I
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
