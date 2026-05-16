[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tandem

_6 messages · 6 participants · 2005-11 → 2005-12_

---

### Tandem

- **From:** "R.Freitag" <rfr-mailbox@gmx.de>
- **Date:** 2005-11-30T17:25:39+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dmkip2$4lq$1@newsreader3.netcologne.de>`

```
Hi

I would like to know the differences between usual Cobol and Tandem Cobol. 
Thanks for any help

Robert
```

#### ↳ Re: Tandem

- **From:** "Mike" <MPBrede@gmail.com>
- **Date:** 2005-11-30T08:53:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1133369622.802318.54550@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<dmkip2$4lq$1@newsreader3.netcologne.de>`
- **References:** `<dmkip2$4lq$1@newsreader3.netcologne.de>`

```

R.Freitag wrote:
> I would like to know the differences between usual Cobol and Tandem Cobol.

It comes with a second rider to help out over the steep bits.
```

##### ↳ ↳ Re: Tandem

- **From:** Bob Iles <bobi@mikal.com>
- **Date:** 2005-11-30T12:02:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6780$438dda97$42a1ca14$24039@FUSE.NET>`
- **In-Reply-To:** `<1133369622.802318.54550@o13g2000cwo.googlegroups.com>`
- **References:** `<dmkip2$4lq$1@newsreader3.netcologne.de> <1133369622.802318.54550@o13g2000cwo.googlegroups.com>`

```
Mike wrote:
> R.Freitag wrote:
> 
…[4 more quoted lines elided]…
> 
nice :)
```

##### ↳ ↳ Re: Tandem

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2005-11-30T10:26:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j4oro15fmfs3oapnmk9mgtpff76fcs1pc1@4ax.com>`
- **References:** `<dmkip2$4lq$1@newsreader3.netcologne.de> <1133369622.802318.54550@o13g2000cwo.googlegroups.com>`

```
On 30 Nov 2005 08:53:42 -0800, "Mike" <MPBrede@gmail.com> wrote:

>> I would like to know the differences between usual Cobol and Tandem Cobol.
>
>It comes with a second rider to help out over the steep bits.

I always wanted one of those two handled mugs that Tandem computer
salesmen used to give out to prospective customers.
```

#### ↳ Re: Tandem

- **From:** Jeff Lanam <jeff-dot-lanam@hp-dot-com-not.net>
- **Date:** 2005-12-01T18:36:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39euo1lf0nkjdsnk4t807gvq94s8lcd596@4ax.com>`
- **References:** `<dmkip2$4lq$1@newsreader3.netcologne.de>`

```
On Wed, 30 Nov 2005 17:25:39 +0100, "R.Freitag" <rfr-mailbox@gmx.de>
wrote:

>Hi
>
…[3 more quoted lines elided]…
>Robert

I am not sure what you mean by "usual Cobol".  HP NonStop COBOL
(formerly Tandem COBOL) conforms to the 1985 COBOL standard, with the
1989 Intrinsic Functions amendment.  There are numerous extension.
Some are from the 2002 Standard, although none of the "big" ones such
as OO or exceptions. Off the top of my head, I can think of:
Free-format source, not identical to the 2002 free-format.
USAGE NATIVE-n, to define binary numbers in the same ranges as C.
The RECEIVE-CONTROL paragraph, for client-server communication.
The ability to create NonStop process pairs.
File ORGANIZATION IS LINE-SEQUENTIAL, for LF terminated text files.
Embedded SQL
Several relating to the file formats supported on NSK.

You can access the COBOL manual, or any HP NonStop manual, from the
NonStop Technical Library, http://h30163.www3.hp.com/ntl/ First,
select the release series you are interested in, then the specific
release, then Publications, then the letter C.
```

#### ↳ Re: Tandem

- **From:** "Sergey Kashyrin" <ska@resqnet.com>
- **Date:** 2005-12-01T14:44:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2pIjf.969$Is2.235576@news.sisna.com>`
- **References:** `<dmkip2$4lq$1@newsreader3.netcologne.de>`

```
Robert,

For documentation you can try to look at http://h30163.www3.hp.com/ntl/
Regarding the differences,  it depends on what you mean by "usual".
Some of them:

does not support OS-VS perform type

does not have a real "dynamic" CALLs (you have to link all modules together, even you can have some of them as a separate DLLs), i.e. you can't "add" program to existing system without relinking.

does not allow to assign filename dynamically (even thru external assignmant like DD on mainframe)
 
accepts only quotes (does not have "apost" option)

syntax checking is more strict than "ususally" (i.e. ZEROS vs ZERO, etc...)

"R.Freitag" <rfr-mailbox@gmx.de> wrote in message news:dmkip2$4lq$1@newsreader3.netcologne.de...
> Hi
> 
…[3 more quoted lines elided]…
> Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
