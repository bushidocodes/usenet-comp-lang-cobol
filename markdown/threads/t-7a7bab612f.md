[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "low-values"

_2 messages · 2 participants · 1999-10_

---

### Re: "low-values"

- **From:** roadraat@aol.com (RoadRaat)
- **Date:** 1999-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991002125941.02146.00000036@ng-fm1.aol.com>`
- **References:** `<37f3c25b.15328200@news.mindspring.com>`

```
>You might try defining a working storage field with low-values as:
>
>    01  W-LOW-VALUES           PIC (2)   VALUE X'0000'.

That won't work, will it?  The default USAGE in this case will be DISPLAY. 
Therefore, assigning '0000' will leave in storage the hex values of 'F0F0F0F0'.

Wouldn't you want to use the actual figurative constant, LOW-VALUES?

RoadRaat
```

#### ↳ Re: "low-values"

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-10-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F6C91D.ABF7E0EA@att.net>`
- **References:** `<37f3c25b.15328200@news.mindspring.com> <19991002125941.02146.00000036@ng-fm1.aol.com>`

```
RoadRaat wrote:
> 
> >You might try defining a working storage field with low-values as:
> >
> >    01  W-LOW-VALUES           PIC (2)   VALUE X'0000'.

The PIC is in error, if you make it "X(2) ..." it'll be fine. The VALUE
clause is invalid for any PIC 9...

> That won't work, will it?  The default USAGE in this case will be DISPLAY.
> Therefore, assigning '0000' will leave in storage the hex values of 'F0F0F0F0'.

He didn't assign a value of '0000'; but X'0000', which is LOW-VALUES in
the IBM mainframe world.

Bill Lynch
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
