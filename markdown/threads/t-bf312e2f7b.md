[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus VISOC / IIS / NT 4.0

_2 messages · 2 participants · 1997-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus VISOC / IIS / NT 4.0

- **From:** "john reynaert" <ua-author-7876551@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc9128$0262ccc0$0a00a8c0@kjsserver>`

```

First the setup.

NT4.0 Server running IIS 3.0.

Application 1.
A VISOC CGI application, Static linked called from
web page... works fine....(has worked for months.)

Application 2.
A VISOC DLL (shared runtime) called from VB5 works fine

Application 3.
The same VISOC DLL called from ActiveX DLL which
in turn runs from a ASP webpage as an object.. Works fine...

Applications 1 and (Applications 2 and 3) are not related.
Not in the same directory, not the same data, not the same
users...

Now the problem..
Application 2 and 3 can run at same time.
Multiple copies of App 2 can run at same time.
multiple copies of App 3 can run ....
App 1 and 2 can run .....

Anytime App 3 runs, App 1 goes dead.
Apps 2 and 3 are still fine.
To bring App 1 back, I have to shutdown IIS, and restart it.
As soon as App 3 runs App 1 goes dead again..

(Sorry for all the APPS :-)

Any ideas ?
John
```

#### ↳ Re: Microfocus VISOC / IIS / NT 4.0

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-07-15T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bf312e2f7b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc9128$0262ccc0$0a00a8c0@kjsserver>`
- **References:** `<01bc9128$0262ccc0$0a00a8c0@kjsserver>`

```

John Reynaert wrote:
› 
› First the setup.
…[31 more quoted lines elided]…
› Any ideas  ?

Hi John.

I've had a chat with some of the guys around here, and it seems that
a similar known problem exists. The problem originates from the fact
that CGI applications will usually run under a user-account with a
restricted set of permissions, as a security measure. This causes a
problem when the VISOC runtime system is attempting to get access to
a system-wide mutex object which is already being accessed by a user
with a different privilege (sp?) set.
This would not usually occur, as you would not normally be developing
and/or running interactive apps on the same machine as a web server.
However, if this is a development environment (or you know your CGI
apps are secure) you may be able to get around this problem by altering
the user-account which the CGI apps are being executed under. It's all
there in the IIS Properties page, I believe.

Note that the newest Micro Focus product, NetExpress, comes with a
standalone web server (Solo) which is integrated into the development
environment and removes the need to set up and run the IIS software in
the development environment.

Cheers,
Kev.

PS. Sorry for being vague in places - I don't have the s/w in front
of me. It should give you an idea of what things to try changing,
anyway.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
