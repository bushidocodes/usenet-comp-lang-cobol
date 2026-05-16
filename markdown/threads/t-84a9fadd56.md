[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynalloc return code from Cobol

_2 messages · 2 participants · 1998-12_

---

### Dynalloc return code from Cobol

- **From:** spalmeri@my-dejanews.com
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<758nuj$mdo$1@nnrp1.dejanews.com>`

```
I have a cobol II program with the following statement:

CALL 'DYNALLOC' USING JCL-CARD

It calls the assembler exit named DYNALLOC and passes a jcl card (containing
the datasetname to dynamically create and various file attributes).

How do I retrieve the return code, after DYNALLOC is called, from within my
Cobol program ?

Thank you in advance for your help.
```

#### ↳ Re: Dynalloc return code from Cobol

- **From:** WOB@my-dejanews.com
- **Date:** 1998-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<759aie$7ji$1@nnrp1.dejanews.com>`
- **References:** `<758nuj$mdo$1@nnrp1.dejanews.com>`

```
In article <758nuj$mdo$1@nnrp1.dejanews.com>,
  spalmeri@my-dejanews.com wrote:
> I have a cobol II program with the following statement:
>
…[10 more quoted lines elided]…
> --

Hopefully, the Sub-Program sets a value in Register 15. Subsequently, you can
query the COBOL RETURN-CODE Special-Register for this value. A normal value is
ZERO.

HTH....

WOB



-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
