[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RENT vs. RENT

_4 messages · 4 participants · 2001-07_

---

### RENT vs. RENT

- **From:** dimbriale@bear.com (Don Imbriale)
- **Date:** 2001-07-12T11:18:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<340ff33e.0107121018.741db0db@posting.google.com>`

```
If I compile using IBM's COBOL for OS/390 and specify compile option
RENT, the load module is not automatically marked RENT.  Is it
recommended to specify linkage editor (or binder) parameter RENT if
compile option RENT has been used?
```

#### ↳ Re: RENT vs. RENT

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-07-12T22:09:57+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63trktc6i7b85a5h3lpmgccb0lv7qv22bn@4ax.com>`
- **References:** `<340ff33e.0107121018.741db0db@posting.google.com>`

```
On 12 Jul 2001 11:18:46 -0700 dimbriale@bear.com (Don Imbriale) wrote:

:>If I compile using IBM's COBOL for OS/390 and specify compile option
:>RENT, the load module is not automatically marked RENT.  

True.

:>                                                         Is it
:>recommended to specify linkage editor (or binder) parameter RENT if
:>compile option RENT has been used?

You may as well.

Of course, unless the load library is APF authorized it won't make a
difference.
```

##### ↳ ↳ Re: RENT vs. RENT

- **From:** Steve Thompson <sthompson_2@neo.rr.com>
- **Date:** 2001-07-16T02:50:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B5255F6.75CD89F2@neo.rr.com>`
- **References:** `<340ff33e.0107121018.741db0db@posting.google.com> <63trktc6i7b85a5h3lpmgccb0lv7qv22bn@4ax.com>`

```
Binyamin Dissen wrote:
<snip>

> :>recommended to specify linkage editor (or binder) parameter RENT if
> :>compile option RENT has been used?
…[4 more quoted lines elided]…
> difference.

<snip>

Well, not entirely true. For every LOAD (or equivalent) a new copy of that
module will be fetched. If this is not the desired result, then one needs
to provide either the REUS or RENT option to the Binder/Linkage editor.

Granted, most COBOL programmers do not understand the requirements for
actual RE-Entrant coding. But assuming that this was done correctly, then
obtaining one copy of the code and entering it multiple times without
having to check to see if it is already loaded (by running the CDE chain
unless some other method is used)... Well you get my drift.

Regards,
Steve Thompson
OSP Consulting
330/335-9907 office
```

#### ↳ Re: RENT vs. RENT

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-12T14:26:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9iktm2$7l8$1@slb0.atl.mindspring.net>`
- **References:** `<340ff33e.0107121018.741db0db@posting.google.com>`

```
If you compile with the RENT compiler option and do NOT do anything to
override the linkage-editor (binder) attributes, I thought it did default to
RENT (assuming you aren't link-editing in a non-RENT module).  I would check
out the IBM documentation to see if you are doing something else to "turn
off" this default.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
