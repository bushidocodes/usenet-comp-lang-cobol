[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus COBOL index file structure

_4 messages · 4 participants · 1997-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus COBOL index file structure

- **From:** "jonathan jay" <ua-author-17071272@usenetarchives.gap>
- **Date:** 1997-06-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc81a4$5f9a5220$5638989e@jons-pc>`

```

Does anybody know the byte structure of a Micro Focus COBOL index file ??

We run an Accounts Program which is written in Micro Focus COBOL on UNIX
(Sequent DYNIX). There is a requirement to write a C program which can
access some of the accounts databases. The database files are indexed and
also have an alternate index. I want to be able to read the datafile by key
but haven't managed to work out exactly what information is stored in it -
anybody know ?? I know that for each record added to the data file 54 bytes
are added to the index, but there seems to be 'extra' information held in
the index file.



Thanks,

Jon
```

#### ↳ Re: Microfocus COBOL index file structure

- **From:** "grj..." <ua-author-14608199@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-14b4cfab06-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81a4$5f9a5220$5638989e@jons-pc>`
- **References:** `<01bc81a4$5f9a5220$5638989e@jons-pc>`

```

Jonathan Jay (j.··.@bat··o.uk) wrote:
: Does anybody know the byte structure of a Micro Focus COBOL index file ??

Yes.

: We run an Accounts Program which is written in Micro Focus COBOL on UNIX
: (Sequent DYNIX). There is a requirement to write a C program which can
: access some of the accounts databases. The database files are indexed and
: also have an alternate index. I want to be able to read the datafile by key
: but haven't managed to work out exactly what information is stored in it -
: anybody know ?? I know that for each record added to the data file 54 bytes
: are added to the index, but there seems to be 'extra' information held in
: the index file.

You don't need to know the structure to do what you want. Use
the EXTFH interface provided by MF to access the files. If you
were on HP. AIX. or SCO (unless Sequent DYNIX is SCO compliant)
you could use our isamedit program to do what you want.

Glen Johnson
CSI
```

##### ↳ ↳ Re: Microfocus COBOL index file structure

- **From:** "tyo..." <ua-author-12381974@usenetarchives.gap>
- **Date:** 1997-06-26T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-14b4cfab06-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-14b4cfab06-p2@usenetarchives.gap>`
- **References:** `<01bc81a4$5f9a5220$5638989e@jons-pc> <gap-14b4cfab06-p2@usenetarchives.gap>`

```

Or you might want to interface the M/F Cobol program with the C code.
Pretty straight forward on the HPUX - don't know about your platform.
There may be several data types (e.g. COMP-3) which are difficult to
handle in C.

Tom Young

Glen Johnson
(grj··.@b··.com) wrote: : Jonathan Jay (j.··.@bat··o.uk) wrote:
: : Does anybody know the byte structure of a Micro Focus COBOL index file ??

: Yes.

: : We run an Accounts Program which is written in Micro Focus COBOL on UNIX
: : (Sequent DYNIX). There is a requirement to write a C program which can
: : access some of the accounts databases. The database files are indexed and
: : also have an alternate index. I want to be able to read the datafile by key
: : but haven't managed to work out exactly what information is stored in it -
: : anybody know ?? I know that for each record added to the data file 54 bytes
: : are added to the index, but there seems to be 'extra' information held in
: : the index file.

: You don't need to know the structure to do what you want. Use
: the EXTFH interface provided by MF to access the files. If you
: were on HP. AIX. or SCO (unless Sequent DYNIX is SCO compliant)
: you could use our isamedit program to do what you want.

: Glen Johnson
: CSI
```

#### ↳ Re: Microfocus COBOL index file structure

- **From:** "10025..." <ua-author-17071258@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-14b4cfab06-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc81a4$5f9a5220$5638989e@jons-pc>`
- **References:** `<01bc81a4$5f9a5220$5638989e@jons-pc>`

```

Jonathan Jay wrote:
›› There is a requirement to write a C program which can
access some of the accounts databases. The database files are
indexed and also have an alternate index. I want to be able to
read the datafile by key but haven't managed to work out exactly
what information is stored in it - anybody know ?
<<

Bite the bullet and buy from Microfocus their own library
routines. That is by far the safest option.

John Allman
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
