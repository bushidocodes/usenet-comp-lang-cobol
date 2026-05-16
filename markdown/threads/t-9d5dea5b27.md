[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question on JCL DD statement for EXPDT.

_4 messages · 4 participants · 1998-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Question on JCL DD statement for EXPDT.

- **From:** lcy <lcy@interlog.com>
- **Date:** 1998-10-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362E9F6D.8E7EBB09@interlog.com>`

```
Folks,

When we need to create a dataset, we can use the parameter EXPDT to set
the expiry date for the Dataset in DD statement. According to the manual
if EXPDT can be YY/DDD or YYYY/DDD, DDD is 000 to 366, if it is equal to
99365 or 99366, the dataset will never be expired. However, is there any
special meaning for 99000? Thanks.

Regards,
lcy
```

#### ↳ Re: Question on JCL DD statement for EXPDT.

- **From:** "Vincent DiGioia" <vmdigioia@digioia.com>
- **Date:** 1998-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iVHX1.170$K4.3474767@news.abs.net>`
- **References:** `<362E9F6D.8E7EBB09@interlog.com>`

```
The expiration date defaults to the system default (30, 60, 90 or whatever
your system folks set the parameter at).

Vincent
```

#### ↳ Re: Question on JCL DD statement for EXPDT.

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362f550c.84207343@news3.ibm.net>`
- **References:** `<362E9F6D.8E7EBB09@interlog.com>`

```
On Wed, 21 Oct 1998 22:58:53 -0400, lcy <lcy@interlog.com> wrote:

>Folks,
>
…[7 more quoted lines elided]…
>lcy


Yes, there is.  The UCC-1 (oops, my age is showing) with CA-1 the EXPDT=98000 and 99000
had special meaning for tape datasets, like EXPDT=98000 means tape comes from outside the
datacenter's tape library


with kind regards

Volker Bandke
(BSP GmbH)
```

##### ↳ ↳ Re: Question on JCL DD statement for EXPDT.

- **From:** Clifton Ivy <clif@purdue.edu>
- **Date:** 1998-10-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362F9F73.55427D23@purdue.edu>`
- **References:** `<362E9F6D.8E7EBB09@interlog.com> <362f550c.84207343@news3.ibm.net>`

```
I expect any special meaning would depend on the system you are using to
keep track of datasets -- in Volker's example below, these are tape
datasets.

We also have UCC-1 with CA-1, and the 99000 means keep the dataset as
long as it is cataloged.  Daily a job runs that checks to see what tape
datasets are past their expiration date; if the expiration date is 99000
and the dataset is still cataloged, then it is kept; if the dataset is
not cataloged, the tape (in the tape management system) is marked as
"scratch", available to be written on.

There are other special values, all of which are probably going to be
problems between now and 12/31/1999.  Ah, well, it probably seemed such
a good idea at the time!  For instance, 99365 means the tape is to be
kept forever (or maybe just until 1/1/2000!!!).

Volker Bandke wrote:
> 
> On Wed, 21 Oct 1998 22:58:53 -0400, lcy <lcy@interlog.com> wrote:
…[19 more quoted lines elided]…
> (BSP GmbH)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
