[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol IMS Update Name Over-write

_4 messages · 4 participants · 2003-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Cobol IMS Update Name Over-write

- **From:** denkenlamb <member46674@dbforums.com>
- **Date:** 2003-11-02T00:41:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3549913.1067751713@dbforums.com>`

```

I am working with code that is not Structrured Cobol.  I need help in
determining where new code is being overwritten by a IMS Database
update.  A code change is being undone when the database is updated.
For example, a change is made online to a name, when the database is
updated, then the change is overwritten.  Does anyone know of any tips
about IMS that would help me solve this problem?
```

#### ↳ Re: Cobol IMS Update Name Over-write

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-03T04:55:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dlpb.4301$qh2.1306@newsread4.news.pas.earthlink.net>`
- **References:** `<3549913.1067751713@dbforums.com>`

```
What type of "interactive" debugging tools do you have for IMS programs?

  Xpediter?
  BTS?
  IBM debug tool?

Depending on what tools are available, you SHOULD be able to "trace" when
such changes are taking place in your application logic (or <G> mis-logic)
```

##### ↳ ↳ Re: Cobol IMS Update Name Over-write

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-11-03T05:32:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PLlpb.203780$0v4.15993636@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3549913.1067751713@dbforums.com> <3dlpb.4301$qh2.1306@newsread4.news.pas.earthlink.net>`

```

 "denkenlamb" <member46674@dbforums.com> wrote in message
 news:3549913.1067751713@dbforums.com...

> I am working with code that is not Structrured Cobol.  I need help in
> determining where new code is being overwritten by a IMS Database
…[3 more quoted lines elided]…
> about IMS that would help me solve this problem?

The most likely cause of this is a logic error
whereby the program to issue an unwarranted rollback call
after the update call has been executed.
```

#### ↳ Re: Cobol IMS Update Name Over-write

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-11-03T17:41:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bo6416$o64$1@peabody.colorado.edu>`
- **References:** `<3549913.1067751713@dbforums.com>`

```

On  1-Nov-2003, denkenlamb <member46674@dbforums.com> wrote:

> I am working with code that is not Structrured Cobol.  I need help in
> determining where new code is being overwritten by a IMS Database
…[3 more quoted lines elided]…
> about IMS that would help me solve this problem?

Does IMS have a pre-compiler that sticks in code?   Does your compiler have an
option to see this listing that is normally turned off?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
