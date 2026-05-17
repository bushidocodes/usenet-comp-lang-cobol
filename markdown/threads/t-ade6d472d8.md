[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EXTERNAL problem with Microfocus Cobol for Unix

_2 messages · 2 participants · 1997-11 → 1997-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### EXTERNAL problem with Microfocus Cobol for Unix

- **From:** "eyalra" <ua-author-17073645@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65uls5$eeg@speedy.amdocs.com>`

```

Hi everybody :

I'm writing a Cobol program that uses EXTERNAL data and I need some help.
I have a Cobol program that defines an ETERNAL data item. I then call
another Cobol program that defines the same EXTERNAL with the same
structure. This Cobol program calls a C program which in turn calls another
Cobol program that again defines the EXTERNAL (I hope you're following).
All three externals are defined exactly the same (I use a COPY statement to
the same file with all of them). At run-time I get the following message :

304 Access EXTERNAL data items with different sizes. (Symbol
`ext_error_record')

I'm 100% percent sure that all EXTERNAL definitions are the same so I don't
understand the error.
If someone has the explanation for this code please send it to me. And if
someone has seen this happened please give me a hand.
I'm running Unix MicroFocus Cobol on HP-UX.
Thanks a lot,

Alan Vexler
```

#### ↳ Re: EXTERNAL problem with Microfocus Cobol for Unix

- **From:** "ami sayag" <ua-author-17071610@usenetarchives.gap>
- **Date:** 1997-12-01T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ade6d472d8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<65uls5$eeg@speedy.amdocs.com>`
- **References:** `<65uls5$eeg@speedy.amdocs.com>`

```

hi Eyal,
did you check if the same variable name declared in the C also ?

ami sayag.

eyalra wrote:

› Hi everybody :
› 
…[26 more quoted lines elided]…
›                                    Alan Vexler
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
