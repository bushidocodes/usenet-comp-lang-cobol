[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS START command

_4 messages · 4 participants · 2004-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS START command

- **From:** andre.queiroz@netcabo.pt (Andr? Queiroz)
- **Date:** 2004-01-02T09:56:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e571c199.0401020956.139cce5d@posting.google.com>`

```
Hello,
 Can anyone tell me if it is possible to run a "background"
transaction with the CICS START command, releasing my own terminal
while doing the background process.
 I tried a START without the TERMINAL parameter but still my own
terminal was busy until the background transaction ended.
 Thanks in advance,

  Andre Queiroz
```

#### ↳ Re: CICS START command

- **From:** robertwessel2@yahoo.com (Robert Wessel)
- **Date:** 2004-01-02T14:48:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bea2590e.0401021448.238af4@posting.google.com>`
- **References:** `<e571c199.0401020956.139cce5d@posting.google.com>`

```
andre.queiroz@netcabo.pt (Andr? Queiroz) wrote in message news:<e571c199.0401020956.139cce5d@posting.google.com>...
> Hello,
>  Can anyone tell me if it is possible to run a "background"
…[4 more quoted lines elided]…
>  Thanks in advance,


That should be all you need.  If you do a "CEMT I TAS" from another
terminal while your background task is running, does it show it
attached to a terminal ("Fac()")?  What does the background task do? 
If it's strictly computational it'll never relinquish control to CICS,
and no other tasks will run.
```

#### ↳ Re: CICS START command

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2004-01-03T07:44:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ApuJb.586988$0v4.23293326@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<e571c199.0401020956.139cce5d@posting.google.com>`
- **References:** `<e571c199.0401020956.139cce5d@posting.google.com>`

```


Andr? Queiroz wrote:

> Hello,
>  Can anyone tell me if it is possible to run a "background"
…[6 more quoted lines elided]…
>   Andre Queiroz

If you want your STARTed transaction to execuate asynchronously from 
your current CICS transaction, then I believe it will be necessary for 
you to START it to a terminal (or facility) that is different from 
your current terminal/facility.

I have used started tasks in CICS to perform file I/O asynchronously 
from network message processing.

I hope that helps.
```

#### ↳ Re: CICS START command

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2004-01-03T10:43:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kodvvsn6dpijn1hr11377g8eiui7g5qef@4ax.com>`
- **References:** `<e571c199.0401020956.139cce5d@posting.google.com>`

```
On 2 Jan 2004 09:56:00 -0800, andre.queiroz@netcabo.pt (Andr? Queiroz)
enlightened us:

>Hello,
> Can anyone tell me if it is possible to run a "background"
…[6 more quoted lines elided]…
>  Andre Queiroz

Unless you use the TERMID parameter of the START command, it is not
attached to any terminal.  Check your CICS manual.  It will state that
if the TERMID option is not used, the task is not attached to any
terminal and, as a result, can't do any terminal I/O.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-


Real Tombstone Epitaphs:

In a Uniontown, Pennsylvania, cemetery:
Here lies the body of Jonathan Blake.
Stepped on the gas
Instead of the brake.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
