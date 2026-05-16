[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need for 64 bit addressing in COBOL was Re: New COBOL announced.

_2 messages · 2 participants · 2001-11 → 2001-12_

---

### Need for 64 bit addressing in COBOL was Re: New COBOL announced.

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2001-11-29T01:27:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C058F49.765D27A2@istar.ca>`
- **References:** `<200111281824.fASIOKW137488@westrelay01.boulder.ibm.com>`

```
If the AIX and AS400 COBOL products support 64 bit addressing and there
are shops taking advantage of the capability, then lack of that
capability on the mainframe would be a barrier to migrating those
workloads to the z/OS environment.  If the z/OS C/C++ and Java programs
are supporting and using 64 bit addressing especially in the Websphere
environment, COBOL needs it for interoperability.  If there are COBOL
programs in other environments (DEC Alpha, SUN?, and HP-UX?) that take
advantage of 64-bit, then lack of the capability would be a hindrance to
migration to z/OS.  Windows will be supporting 64-bit with Itanium. 
Linux is supporting 64 bit in some environments.  64 bits may become
desirable for large CICS regions where the invidual transaction doesn't
need 64 bits worth of space but the concurrent transactions collectively
do.  Also handling of BLOBs (Binary Large OBjects) in CICS may force the
issue.  As COBOL starts handling non-traditional data the addressing
requirement increases because the size of the individual data aggregate
increases.  For example, your payroll record may include a picture of
the employee and their fingerprint.  Indeed we probably have to look at
what people are doing on other platforms in order to better understand
future needs.  

When data management gets its act together with a universal access
method and control block that will handle all of the currently supported
data formats (CKD sequential, ESDS, KSDS, RRDS, HFS, PDSE etc. plus
VTAM, etc.) in the 64 bit environment, COBOL will need 64 bit addressing
to take advantage of the capability. 

Tom Ross wrote:
> 
>  Does anyone in IBMMAIN know of 'real-world' (no retirees please) reqirements
…[12 more quoted lines elided]…
> Search the archives at http://bama.ua.edu/archives/ibm-main.html


Tom Ross wrote:
> 
>  Does anyone in IBMMAIN know of 'real-world' (no retirees please) reqirements
…[12 more quoted lines elided]…
> Search the archives at http://bama.ua.edu/archives/ibm-main.html
```

#### ↳ Re: Need for 64 bit addressing in COBOL was Re: New COBOL announced.

- **From:** "James" <mangogrower@telocity.com>
- **Date:** 2001-12-02T18:48:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E2zO7.30$f4.121600@newsrump.sjc.telocity.net>`
- **References:** `<200111281824.fASIOKW137488@westrelay01.boulder.ibm.com> <3C058F49.765D27A2@istar.ca>`

```
You get around the 16MB limit by compiling with 'RENT' - even for non-CICS
batch
programs.

"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message
news:3C058F49.765D27A2@istar.ca...
> If the AIX and AS400 COBOL products support 64 bit addressing and there
> are shops taking advantage of the capability, then lack of that
…[26 more quoted lines elided]…
> >  Does anyone in IBMMAIN know of 'real-world' (no retirees please)
reqirements
> > for 64-bit addressing in COBOL?  We DO know that people want to be able
to
> > code COBOL data items that are bigger than 16M (our current limit) but
we
> > could go much larger and still be AMODE 31.  Larger data items is in the
> > list of things to do, but we are looking for input on 64 bit
requirements.
> > Specifically, any COBOL programs that address 2MB of data and need more?
> >
…[11 more quoted lines elided]…
> >  Does anyone in IBMMAIN know of 'real-world' (no retirees please)
reqirements
> > for 64-bit addressing in COBOL?  We DO know that people want to be able
to
> > code COBOL data items that are bigger than 16M (our current limit) but
we
> > could go much larger and still be AMODE 31.  Larger data items is in the
> > list of things to do, but we are looking for input on 64 bit
requirements.
> > Specifically, any COBOL programs that address 2MB of data and need more?
> >
…[6 more quoted lines elided]…
> > Search the archives at http://bama.ua.edu/archives/ibm-main.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
