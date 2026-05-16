[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VS COBOL II VSAM retcode 93

_3 messages · 3 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### VS COBOL II VSAM retcode 93

- **From:** valrik@aol.com (Valrik)
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991116113048.01104.00000095@ng-cg1.aol.com>`

```
Hi Y'all,

Anyone out there in COBOL-land have any tips on debugging a VSAM retcode 93
(the IBM COBOL manual refers to a resource shortage)?

The programmer has tried a variety of things, including increasing the region
size as well as ensuring that the data set in question is closed to CICS.

The application is CA's SAAvi payroll system, running under OS/390 V2.4. 
Alternate indices are also in use with this data set.  CA doesn't have any
reported hits like this one.

Thanks in advance!

Rick J. Valles
```

#### ↳ Re: VS COBOL II VSAM retcode 93

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8166fv$du5$1@nnrp1.deja.com>`
- **References:** `<19991116113048.01104.00000095@ng-cg1.aol.com>`

```
In article <19991116113048.01104.00000095@ng-cg1.aol.com>,
  valrik@aol.com (Valrik) wrote:
> Hi Y'all,
>
> Anyone out there in COBOL-land have any tips on debugging a VSAM
retcode 93
> (the IBM COBOL manual refers to a resource shortage)?
>
> The programmer has tried a variety of things, including increasing
the region
> size as well as ensuring that the data set in question is closed to
CICS.
>
> The application is CA's SAAvi payroll system, running under OS/390
V2.4.
> Alternate indices are also in use with this data set.  CA doesn't
have any
> reported hits like this one.
>
…[4 more quoted lines elided]…
>

Rick,

Go to the following ===> http://knowledge.storage.ibm.com

WOB,
Atlanta



Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: VS COBOL II VSAM retcode 93

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3836AA26.981BFC2F@nbnet.nb.ca>`
- **References:** `<19991116113048.01104.00000095@ng-cg1.aol.com> <8166fv$du5$1@nnrp1.deja.com>`

```
The record size for your alternate index may not be big enough to handle
all of the keys if the alternate keys are not unique.

Clark Morris, CFM Technical Programming Services, morrisc@nbnet.nb.ca

WOB Consulting wrote:
> 
> In article <19991116113048.01104.00000095@ng-cg1.aol.com>,
…[32 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
