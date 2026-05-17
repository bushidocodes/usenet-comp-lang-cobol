[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CORBA support in COBOL

_4 messages · 4 participants · 1997-12_

---

### CORBA support in COBOL

- **From:** "giora katz-lichtenstein" <ua-author-17073123@usenetarchives.gap>
- **Date:** 1997-12-13T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<349470FD.25594446@us.oracle.com>`

```
Hi.

I'm looking to find information about COBOL products supporting OMG
CORBA.
Are there any COBOL commercial products supporting CORBA?
Where can I buy them?
What is the estimated price?

Regards,

Giora Katz-Lichtenstein
```

#### ↳ Re: CORBA support in COBOL

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1997-12-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ab65e77b0e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<349470FD.25594446@us.oracle.com>`
- **References:** `<349470FD.25594446@us.oracle.com>`

```

I know that Micro Focus, Fujitsu, and IBM all offer compilers which they
(not I) claim are CORBA compliant. I suspect others do as well. You should
be aware, however, that the actual standard (ANSI/ISO) language for handling
OO is:
A) still in flux
B) a superset of CORBA requirements
You might also be interested in the language binding that is still "under
development" at OMG for accessing CORBA.

Giora Katz-Lichtenstein wrote in message
<349··.@us.··e.com>...
› Hi.
› 
…[9 more quoted lines elided]…
›
```

#### ↳ Re: CORBA support in COBOL

- **From:** "einar clementz" <ua-author-6588781@usenetarchives.gap>
- **Date:** 1997-12-21T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ab65e77b0e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<349470FD.25594446@us.oracle.com>`
- **References:** `<349470FD.25594446@us.oracle.com>`

```

Hi

Yes there is a product called DIAS from a ICL company.

see http://www.iclsoft.com/sbs/daismenu.html

and http://www.cs.wustl.edu/~schmidt/corba.html
for a more broad view of this issue.

Best regards
Einar Clementz, Oslo, Norway


Giora Katz-Lichtenstein wrote:

› Hi.
› 
…[24 more quoted lines elided]…
›   Version   2.1
```

##### ↳ ↳ Re: CORBA support in COBOL

- **From:** "bvk" <ua-author-936803@usenetarchives.gap>
- **Date:** 1997-12-22T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ab65e77b0e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ab65e77b0e-p3@usenetarchives.gap>`
- **References:** `<349470FD.25594446@us.oracle.com> <gap-ab65e77b0e-p3@usenetarchives.gap>`

```



Einar Clementz wrote in article
<349··.@onl··e.no>...
› Hi
›
› Yes there is a product called DIAS from a ICL company.
›

I Did a research project using DIAS and object cobol. At the time of doing
this it was only possible to
generate IDL for procedural cobol and not for object cobol for use with
CORBA. This was a severe blow
to us which, along with the "THEN" immaturity of DIAS a caused the project
to be put on hold.
I am led to believe that MicroFocus now has support for ORBIX.

If you have a IDL generator for ORBIX, it should be a relatively simple
matter to implement distributed objects.

Cheers
Bruce...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
