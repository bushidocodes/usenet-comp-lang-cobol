[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# trans id and task id incase of CICS xctl and link

_4 messages · 4 participants · 2003-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### trans id and task id incase of CICS xctl and link

- **From:** tarun_bhardwaj <member22201@dbforums.com>
- **Date:** 2003-10-14T05:19:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3478635.1066123173@dbforums.com>`

```

i have 2 doubts :



1. when we "xctl" in cics, does the task-id and trans-id remain the same
   or do they change ?



2. when we "link" in cics, does the task-id and trans-id remain the same
   or do they change ?
```

#### ↳ Re: trans id and task id incase of CICS xctl and link

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-10-14T12:33:06+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i6knovc2n100pousnvba0t647nmhq2ucfn@4ax.com>`
- **References:** `<3478635.1066123173@dbforums.com>`

```
On Tue, 14 Oct 2003 05:19:33 -0400 tarun_bhardwaj <member22201@dbforums.com>
wrote:

:>i have 2 doubts :

:>1. when we "xctl" in cics, does the task-id and trans-id remain the same
:>   or do they change ?

:>2. when we "link" in cics, does the task-id and trans-id remain the same
:>   or do they change ?

Yes.
```

##### ↳ ↳ Re: trans id and task id incase of CICS xctl and link

- **From:** Joseph Katnic <usrr@mac.kat>
- **Date:** 2003-10-14T21:46:09+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<141020032146092167%usrr@mac.kat>`
- **References:** `<3478635.1066123173@dbforums.com> <i6knovc2n100pousnvba0t647nmhq2ucfn@4ax.com>`

```
Well that was useful :)

The answer is they remain the same UNLESS you specify the SYSID()
parameter in which case surrogate transaction will be executed to run
your remote program call.


In article <i6knovc2n100pousnvba0t647nmhq2ucfn@4ax.com>, Binyamin
Dissen <postingid@dissensoftware.com> wrote:

> On Tue, 14 Oct 2003 05:19:33 -0400 tarun_bhardwaj <member22201@dbforums.com>
> wrote:
…[15 more quoted lines elided]…
> Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: trans id and task id incase of CICS xctl and link

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-10-15T00:53:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-744699.00533715102003@corp.supernews.com>`
- **References:** `<3478635.1066123173@dbforums.com> <i6knovc2n100pousnvba0t647nmhq2ucfn@4ax.com> <141020032146092167%usrr@mac.kat>`

```
Some qualifiers are in order.

You can LINK or XCTL to a program that is defined remote to another 
region, in which case a mirror tran will be brought up on the remote 
region and executed.

Also, with some of the newer CICS toys, like dynamic load balancing, 
dynamic regions, CICSPlex/SM you can find things shifting about somewhat 
freely.  A LINK or XCTL is one of those points where such shifting is 
explicitly defined as allowed.

In either case, the LINKing program would retain the original tran and 
task-id.

But if the LINKed program inspects the tran-id or task-id they MIGHT be 
different.  This should be covered in the programmers guide about system 
affinity (it might not be, but it should be).


In article <141020032146092167%usrr@mac.kat>,
 Joseph Katnic <usrr@mac.kat> wrote:

> Well that was useful :)
> 
…[25 more quoted lines elided]…
> > Director, Dissen Software, Bar & Grill - Israel
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
