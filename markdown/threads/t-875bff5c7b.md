[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS COBOL compile JCL

_5 messages · 4 participants · 2004-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS COBOL compile JCL

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-03-25T19:36:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0403251936.3dde683d@posting.google.com>`

```
OS/390 2.7, COBOL for this and that 2.1.  CICS 4.1.  Looking for some
COBOL compile and link JCL with translator step.  Hunted high and low
and can't find any!

If someone has one - I can customize it to my system.  You can either
post here (even if your versions don't match mine - something close
will do) or email me (but not to the address I have posted with) - use
thane at softwaresimple.com.

Thanks.
```

#### ↳ Re: CICS COBOL compile JCL

- **From:** docdwarf@panix.com
- **Date:** 2004-03-26T07:52:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c4192g$qjl$1@panix5.panix.com>`
- **References:** `<bfdfc3e8.0403251936.3dde683d@posting.google.com>`

```
In article <bfdfc3e8.0403251936.3dde683d@posting.google.com>,
Thane Hubbell <thaneh@softwaresimple.com> wrote:
>OS/390 2.7, COBOL for this and that 2.1.  CICS 4.1.  Looking for some
>COBOL compile and link JCL with translator step.  Hunted high and low
>and can't find any!

Got some old stuff that might be of help... sending via email.

DD
```

#### ↳ Re: CICS COBOL compile JCL

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2004-03-26T20:39:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2y09c.45561$PY1.851763@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<bfdfc3e8.0403251936.3dde683d@posting.google.com>`
- **References:** `<bfdfc3e8.0403251936.3dde683d@posting.google.com>`

```


Thane Hubbell wrote:
> OS/390 2.7, COBOL for this and that 2.1.  CICS 4.1.  Looking for some
> COBOL compile and link JCL with translator step.  Hunted high and low
…[7 more quoted lines elided]…
> Thanks.

Thane,

I'm enjoying a day off from work today, so I don't have an example 
close to hand.  But if you still need one on Monday, please let me know.

In my shop we have several procs for compiling, depending on compiler 
version, cics or not, et cetera.  I believe our procs are normally 
modifications from IBM supplied samples.  There may be IBM sample 
procs somewhere on your system.  You might try looking for those.

But if you still need an example on Monday, please let me know.

With kindest regards,
```

#### ↳ Re: CICS COBOL compile JCL

- **From:** rjones0@hotmail.com (Robert Jones)
- **Date:** 2004-03-27T07:33:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dd8322.0403270733.ca40c62@posting.google.com>`
- **References:** `<bfdfc3e8.0403251936.3dde683d@posting.google.com>`

```
Bottom posting

thaneh@softwaresimple.com (Thane Hubbell) wrote in message news:<bfdfc3e8.0403251936.3dde683d@posting.google.com>...
> OS/390 2.7, COBOL for this and that 2.1.  CICS 4.1.  Looking for some
> COBOL compile and link JCL with translator step.  Hunted high and low
…[7 more quoted lines elided]…
> Thanks.

I haven't worked in the field for some time, but if they are available
to you, the CICS and COBOL programmer's guides should contain this
information.  They can be found on IBM website, you would be best
placed to identify the appropriate versions of the manuals to look at.
 The CICS one seems to be in bookmanager format last time I looked so
you would have to install bookmanager, a free download from IBM, to
read it.

http://www-1.ibm.com/servers/eserver/zseries/zos/bkserv/

A quicker way might be to ask on google bit.listserve.ibm-main or join
the CICS-L listserve group which communicates by email.

Bill Klein has recently posted on ibm-main about potential problems
using CICS 4.1 with recent compilers, it provides a link to a manual
that may also be of interest.

Robert
```

##### ↳ ↳ Re: CICS COBOL compile JCL

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-03-28T20:08:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0403282008.6e370826@posting.google.com>`
- **References:** `<bfdfc3e8.0403251936.3dde683d@posting.google.com> <6dd8322.0403270733.ca40c62@posting.google.com>`

```
Thanks Everyone,

Bill's and Doc's private responses were enough to get us going. 
Onward and upward.  Thanks again.

rjones0@hotmail.com (Robert Jones) wrote in message news:<6dd8322.0403270733.ca40c62@posting.google.com>...
> Bottom posting
> 
…[29 more quoted lines elided]…
> Robert
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
