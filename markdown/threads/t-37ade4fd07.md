[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# compile cobol on mvs

_4 messages · 3 participants · 1998-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### compile cobol on mvs

- **From:** "Eyal Rond" <eyal@isg.co.il>
- **Date:** 1998-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75tigu$6le$1@news.netvision.net.il>`

```
hello to u all
i need to compile a simple cobol program on the mainframe

can u please send me an jcl example

thanks in advance
```

#### ↳ Re: compile cobol on mvs

- **From:** docdwarf@clark.net ()
- **Date:** 1998-12-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<75tl6a$acu$1@clarknet.clark.net>`
- **References:** `<75tigu$6le$1@news.netvision.net.il>`

```
In article <75tigu$6le$1@news.netvision.net.il>,
Eyal Rond <eyal@isg.co.il> wrote:
>hello to u all
>i need to compile a simple cobol program on the mainframe
…[3 more quoted lines elided]…
>thanks in advance

Please do your own homework

DD
```

##### ↳ ↳ Re: compile cobol on mvs

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1998-12-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36845343.69F036DD@acm.org>`
- **References:** `<75tigu$6le$1@news.netvision.net.il> <75tl6a$acu$1@clarknet.clark.net>`

```
docdwarf@clark.net wrote:
> 
> In article <75tigu$6le$1@news.netvision.net.il>,
…[10 more quoted lines elided]…
> DD

More to the point, this can be highly installation dependent.  You need
to know what COBOL compiler your installation uses, what standard JCL
PROC's they have customized and made available for general use, any
special library names you need to use, etc.  You need to get this
information from someone knowledgable with your specific installation or
from documentation created by your specific installation.  The
appropriate COBOL Programming Guide will show how to do this with the
"standard" IBM JCL PROC's, but this still may not be directly compatible
with your specific installation.  (for example, we use ISPF dialogs to
generate all compile JCL and for the most part don't bother to customize
the IBM PROC's to make them functional).
```

###### ↳ ↳ ↳ Re: compile cobol on mvs

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 1998-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-Cyh2K8Xddbfk@dsm4merlin.iix.com>`
- **References:** `<75tigu$6le$1@news.netvision.net.il> <75tl6a$acu$1@clarknet.clark.net> <36845343.69F036DD@acm.org>`

```
On Sat, 26 Dec 1998 03:08:51, "Joel C. Ewing" <jcewing@acm.org> wrote:

> More to the point, this can be highly installation dependent.  You need
> to know what COBOL compiler your installation uses, what standard JCL
> PROC's they have customized and made available for general use, any
> special library names you need to use, etc

Yep, right on - fer inst'nce - for me this will work fine:


//D JOB 7000,DWIGHT
//  EXEC  COBLNK,MODULE=STRAWN

but I'd be willing to bet that nobody else here except Thane could use
it without doing a bit of background work!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
