[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indexed file searching

_3 messages · 3 participants · 1999-09_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Indexed file searching

- **From:** Cameron McAllister <s369539@student.uq.edu.au>
- **Date:** 1999-09-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.OSF.4.10.9909061211340.21170-100000@student.uq.edu.au>`

```
Does anyone know of a good example for searching for an entry in an
indexed file when you only have part of the key?

key is a string, but a partial string should match, but I cannot get it to
this.

ta

cameron mcallister
```

#### ↳ Re: Indexed file searching

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37D339EF.A79715F3@home.com>`
- **References:** `<Pine.OSF.4.10.9909061211340.21170-100000@student.uq.edu.au>`

```
Cameron McAllister wrote:
> 
> Does anyone know of a good example for searching for an entry in an
…[7 more quoted lines elided]…
> cameron mcallister

Assuming :  01 Myrecord.
	       05 MyPrimeKey	pic x(06).
	       05 .......

and you only know the PrimeKey starts "JAC   "

	set FileNotFinished to true
	move "JAC" to MyPrimeKey
	Start Myfile key is > MyPrimeKey
 	    invalid key set FileFinished to true
	End-start

	if  FileNotFinished
	    read MyFile next record
		at end set FileFinished to true
	    end-read
	End-if

	if  FileNotFinished and
	    MyPrimeKey(1:3) = "JAC"
            display "Strewth Mate - I've found it !"
	End-if

Jimmy, Calgary AB
```

#### ↳ Re: Indexed file searching

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-09-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37d3bb23.42615957@news1.ibm.net>`
- **References:** `<Pine.OSF.4.10.9909061211340.21170-100000@student.uq.edu.au>`

```
On Mon, 6 Sep 1999 12:12:56 +1000, Cameron McAllister
<s369539@student.uq.edu.au> wrote:

>Does anyone know of a good example for searching for an entry in an
>indexed file when you only have part of the key?
…[3 more quoted lines elided]…
>

Well that all depends.   Is it the first part of the key field you
want to match or any old part?  If under CICS there is a feature
called "Generic Keys" that you can use for this that I discussed in my
portion of the book COBOL Unleashed.  What is your platform and what
portion of the key are you trying to match?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
