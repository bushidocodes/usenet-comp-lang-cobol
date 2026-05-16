[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help request: Realia 16bit to 32bit conversion problem

_5 messages · 5 participants · 2002-08 → 2003-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help request: Realia 16bit to 32bit conversion problem

- **From:** maurice.northey@team.telstra.com (Maurice Northey)
- **Date:** 2002-08-25T23:43:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<697c3488.0208252243.3b3dcbbd@posting.google.com>`

```
I am converting a batch app from Realia Cobol v3 (DOS) to Realia
Workbench 3.1 (NT).
One program won't behave the same upon recompilation.
I have tried every trick in the book to find out why. 

I don't have any doco on what language-level Cobol version v3 is, so I
have tried recompiling in Realia4, Realia, ANSI74, 85, error checking
on/off etc without success.

So (1) does anyone know what options should be used with Workbench to
do the recompilation?

(2) Is it possible to trace a v3 program?

I reckon the problem is related to COMP SYNC usage.
(3) Does anyone know what COMP in v3 equates to in Workbench
(comp-3,4,5 etc)?

Any sggestions appreciated.
Maurice
```

#### ↳ Re: Help request: Realia 16bit to 32bit conversion problem

- **From:** charles.godwin@ca.com (Charles Godwin)
- **Date:** 2002-08-26T06:33:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8035ce7.0208260533.4a4829db@posting.google.com>`
- **References:** `<697c3488.0208252243.3b3dcbbd@posting.google.com>`

```
1) Have you spoken to Computer Associates technical support? They will
gladly help if oyu are are the lciensed owner of a  version of
workbench 3.1.

2)What exactly is the problem? can you stil compile with 16 bit? If so
check the compiled options list at the end of the listing and see if
there's a difference.

Charles Godwin
Computer Associates
Development Manager
Advantage CA-Realia II Workbench

maurice.northey@team.telstra.com (Maurice Northey) wrote in message news:<697c3488.0208252243.3b3dcbbd@posting.google.com>...
> I am converting a batch app from Realia Cobol v3 (DOS) to Realia
> Workbench 3.1 (NT).
…[17 more quoted lines elided]…
> Maurice
```

##### ↳ ↳ Re: Help request: Realia 16bit to 32bit conversion problem

- **From:** maurice.northey@bigpond.com (Maurice Northey)
- **Date:** 2002-09-24T22:06:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c825e98d.0209242106.42e2c455@posting.google.com>`
- **References:** `<697c3488.0208252243.3b3dcbbd@posting.google.com> <c8035ce7.0208260533.4a4829db@posting.google.com>`

```
> maurice.northey@team.telstra.com (Maurice Northey) wrote in message news:<697c3488.0208252243.3b3dcbbd@posting.google.com>...
> > I am converting a batch app from Realia Cobol v3 (DOS) to Realia
> > Workbench 3.1 (NT).
> > One program won't behave the same upon recompilation.
> > I have tried every trick in the book to find out why. 

For the benefit of anyone searching this message in the future, the
problem was that the following structure compiles OK but the program
appeared not to be able to access the elements of ABC-REC correctly.

01  ABC-REC.
  03  IN-CHAR OCCURS 1 TO 512
            DEPENDING ON REC-LEN
            INDEXED BY XIN
            PIC X.

The fix was to change ABC-REC to X(512).
```

#### ↳ Re: Help request: Realia 16bit to 32bit conversion problem

- **From:** bsambartolo <member24915@dbforums.com>
- **Date:** 2003-02-13T19:52:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2526464.1045165935@dbforums.com>`
- **References:** `<697c3488.0208252243.3b3dcbbd@posting.google.com>`

```

do you still have that realia v3, i assume its 16-bit, if so and you
have the manual would you be interested in selling it?
```

##### ↳ ↳ Re: Help request: Realia 16bit to 32bit conversion problem

- **From:** "Stephen Plotnick" <thepla@attglobal.net>
- **Date:** 2003-02-15T17:54:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e4ed335_3@news3.prserv.net>`
- **References:** `<697c3488.0208252243.3b3dcbbd@posting.google.com> <2526464.1045165935@dbforums.com>`

```
The current version is Workbench 3.?. The older version is Relia COBOL 4.?

"bsambartolo" <member24915@dbforums.com> wrote in message
news:2526464.1045165935@dbforums.com...
>
> do you still have that realia v3, i assume its 16-bit, if so and you
…[3 more quoted lines elided]…
> Posted via http://dbforums.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
