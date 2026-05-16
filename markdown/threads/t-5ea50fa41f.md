[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Source file compare utility?

_5 messages · 5 participants · 1998-11_

---

### Source file compare utility?

- **From:** Michael Russell <m006s300@mcmail.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365B12FC.8C6FBF5B@mcmail.com>`

```
Working with unix-based Cobol system - there is no
source-file compare available that gives good results.

What is available is the unix diff (or sdiff) command -
which operates on the whole width of a source-line - ie
columns 1-80. Naturally, what is needed is a comaparison
from 8-72, and a difference-report that *does* include the
line-numbers, ie columns 1-6.

Anyone help? Of course, it doesn't have to be particularly
Cobol-oriented; however, I do need to be able to run it
under NT-Dos (Dos shell).

Any help would be appreciated.

Mike Russell
```

#### ↳ Re: Source file compare utility?

- **From:** kownby@humboldt1.com (Kindrick Ownby)
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b17b4.7971539@news2.humboldt1.com>`
- **References:** `<365B12FC.8C6FBF5B@mcmail.com>`

```
On Tue, 24 Nov 1998 20:11:40 +0000, Michael Russell
<m006s300@mcmail.com> wrote:

>Working with unix-based Cobol system - there is no
>source-file compare available that gives good results.

I downloaded one from

http://ourworld.compuserve.com/homepages/Jonathan_Rosenne/jdif.htm

but haven't tried it yet, nor do I know if it can be used on
your platform.

Kindrick
```

#### ↳ Re: Source file compare utility?

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b3207.0@news1.ibm.net>`
- **References:** `<365B12FC.8C6FBF5B@mcmail.com>`

```

Michael Russell wrote in message <365B12FC.8C6FBF5B@mcmail.com>...
>Working with unix-based Cobol system - there is no
>source-file compare available that gives good results.
…[9 more quoted lines elided]…
>under NT-Dos (Dos shell).


Such a utility is part of the ETK toolset. There is a slight
ambiguity in your post (Unix vs NT-Dos ?). E-mail me
if you want a tool that runs in a Dos Box on Windows NT.
It also exists for unix, but you will have to compile it
yourself from the sources.
leif@etk.com
```

#### ↳ Re: Source file compare utility?

- **From:** "Warren Porter" <warrenp@netdoor.com>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NJH62.2308$b53.11703@axe.netdoor.com>`
- **References:** `<365B12FC.8C6FBF5B@mcmail.com>`

```
You might want to run both files through a sed command and compare the
modified files.

Michael Russell wrote in message <365B12FC.8C6FBF5B@mcmail.com>...
>Working with unix-based Cobol system - there is no
>source-file compare available that gives good results.
…[14 more quoted lines elided]…
>
```

#### ↳ Re: Source file compare utility?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365b802e.8221137@news1.ibm.net>`
- **References:** `<365B12FC.8C6FBF5B@mcmail.com>`

```
On Tue, 24 Nov 1998 20:11:40 +0000, Michael Russell
<m006s300@mcmail.com> wrote:

>Working with unix-based Cobol system - there is no
>source-file compare available that gives good results.
…[6 more quoted lines elided]…
>

The MicroFocus workbench Dif is not available under Unix?  It's the
best DIF tool I have used.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
