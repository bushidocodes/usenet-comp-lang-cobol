[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and APPC

_3 messages · 3 participants · 1997-06_

---

### COBOL and APPC

- **From:** "steve burns" <ua-author-645539@usenetarchives.gap>
- **Date:** 1997-06-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<339828F4.3BBF@PSS.Boeing.com>`

```

Has anyone any experience in writing COBOL code for APPC (Advanced
Program to Program Communication). If possible I need to see some
example code. I have some examples I can look at written in C, but I
would rather learn Greek than C.

I haven't decided yet if my code will run on a desktop or on a server.
Most likely I will start with a desktop version and rebuild it as server
code later...

*****************************************************************
* Steve Burns    The Boeing Co.    I'm not sure if I subscribe  *
* PO Box 3707    Mail Stop 2L-14   to these opinions, I'm sure  *
* (206) 544-8264 Seattle, WA 98124    that Boeing doesn't.      *
```

#### ↳ Re: COBOL and APPC

- **From:** "bob england" <ua-author-2566067@usenetarchives.gap>
- **Date:** 1997-06-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-da4ce1a3c5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<339828F4.3BBF@PSS.Boeing.com>`
- **References:** `<339828F4.3BBF@PSS.Boeing.com>`

```

› Steve Burns wrote:
› 
…[7 more quoted lines elided]…
› code later...

Steve, if you are looking for a simpler way to create applications with
distributed logic, check out Cobol-RPC on our website:
http://www.netins.net/showcase/etsinc. Cobol-RPC makes building
distributed applications as simple as standalone applications by
allowing the COBOL call statement to work between separate machines.

Bob England
England Technical Services, Inc.
```

##### ↳ ↳ Re: COBOL and APPC

- **From:** "j.s." <ua-author-88615@usenetarchives.gap>
- **Date:** 1997-06-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-da4ce1a3c5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-da4ce1a3c5-p2@usenetarchives.gap>`
- **References:** `<339828F4.3BBF@PSS.Boeing.com> <gap-da4ce1a3c5-p2@usenetarchives.gap>`

```

APPC is not that hard in COBOL. CHeck out a tool called NETRON.
http://www.netron.com. They can do APPC, IPXSPX, TCPIP, and several others
within COBOL, and it not a runtime like RPC. It is straight COBOL. I have
several apps using APPC to communication directrly to CICS on the
mainframe. It works like a champ....
Bob England wrote in article <339··.@net··s.net>...
›› Steve Burns wrote:
›› 
…[18 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
