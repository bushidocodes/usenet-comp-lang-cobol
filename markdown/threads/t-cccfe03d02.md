[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using Learn Cobol 24 Hours by Thane Hubbell

_9 messages · 6 participants · 1999-09_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** "COLLINSJ" <COLLINSJ@xtra.co.nz>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sescl$8a5k2$1@titan.xtra.co.nz>`

```
I am new to Cobol and struck a problem in Chapter 17 of this book,the only
one to date.  Both Chapt 17a and d have the same error code as follows :
JMP0613-U SORT MERGE LIBARY CANNOT BE LOADED .
FB3BESORT,DLL  CODE = 1157 = CHAPT17A  ADR=00401233.

If any one has any idea please let me know
Regards John
collinsj@xtra.co.nz
```

#### ↳ Re: Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990924193147.09493.00000300@ngol06.aol.com>`
- **References:** `<7sescl$8a5k2$1@titan.xtra.co.nz>`

```
In article <7sescl$8a5k2$1@titan.xtra.co.nz>, "COLLINSJ" <COLLINSJ@xtra.co.nz>
writes:

>
>I am new to Cobol and struck a problem in Chapter 17 of this book,the only
…[3 more quoted lines elided]…
>

My first thought is that the PowerBSORT and PowerBSORT OCX components
were not loaded/installed from the CD.  Or the location of the BSort utilities
does not exist on the search path.
```

#### ↳ Re: Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EB1387.7056B79A@home.com>`
- **References:** `<7sescl$8a5k2$1@titan.xtra.co.nz>`

```
COLLINSJ wrote:
> 
> I am new to Cobol and struck a problem in Chapter 17 of this book,the only
…[6 more quoted lines elided]…
> collinsj@xtra.co.nz

Thane,

Take off your marketing hat and put on your teacher's hat <G>

Jimmy, Calgary AB
```

#### ↳ Re: Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ed3456.77841526@news1.ibm.net>`
- **References:** `<7sescl$8a5k2$1@titan.xtra.co.nz>`

```
On Sat, 25 Sep 1999 15:47:43 +1200, "COLLINSJ" <COLLINSJ@xtra.co.nz>
wrote:

>I am new to Cobol and struck a problem in Chapter 17 of this book,the only
>one to date.  Both Chapt 17a and d have the same error code as follows :
>JMP0613-U SORT MERGE LIBARY CANNOT BE LOADED .
>FB3BESORT,DLL  CODE = 1157 = CHAPT17A  ADR=00401233.

We are talking in e-mal now about this problem - but no solution yet.
Anyone have any ideas?  This might be just a v4 over v3 install
problem.  He is now using v4.
```

#### ↳ Re: Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ed36d3.78478852@news1.ibm.net>`
- **References:** `<7sescl$8a5k2$1@titan.xtra.co.nz>`

```
On Sat, 25 Sep 1999 15:47:43 +1200, "COLLINSJ" <COLLINSJ@xtra.co.nz>
wrote:

>I am new to Cobol and struck a problem in Chapter 17 of this book,the only
>one to date.  Both Chapt 17a and d have the same error code as follows :
>JMP0613-U SORT MERGE LIBARY CANNOT BE LOADED .
>FB3BESORT,DLL  CODE = 1157 = CHAPT17A  ADR=00401233.

Problem Solved!

It was a version over version install problem that had it confused.

Solution: Uninstall all Fujitsu products from the Add/Remove programs.
DELETE the \FSC directory and all subdirectories.
Run REGEDIT and search for Fujitsu removing all entries.
Re-install v4.  Everything works!
```

##### ↳ ↳ Re: Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ED5848.51F88783@home.com>`
- **References:** `<7sescl$8a5k2$1@titan.xtra.co.nz> <37ed36d3.78478852@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> On Sat, 25 Sep 1999 15:47:43 +1200, "COLLINSJ" <COLLINSJ@xtra.co.nz>
…[14 more quoted lines elided]…
> Re-install v4.  Everything works!

I think this is a real bloody pain. Mr. Microsoft again. Same headache
occurs when playing around with NetExpress reinstalls - that Registry
junk really screws things up. By comparison the old DOS RM/COBOL V2
re-installs just over-writing what exists - but even there, thanks to
Windows again, a slight problem. It comes up "Incompatible DOS Version
#". So you have to do SETVER - but Windows 98 no longer gives you SETVER
automatically - you now have to search for it.

Hhha ! And Windows was supposed to make life easier.

PS. You can put your marketing hat back on <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sklfb$2j8$4@ssauraac-i-1.production.compuserve.com>`
- **References:** `<7sescl$8a5k2$1@titan.xtra.co.nz> <37ed36d3.78478852@news1.ibm.net> <37ED5848.51F88783@home.com>`

```
simple and obvious for programmers - but what about other products.  I have
seen this with networks and other stuff that non-techys deal with.  Major
disaster for them.


James J. Gavan <jjgavan@home.com> wrote in message
news:37ED5848.51F88783@home.com...
> Thane Hubbell wrote:
> >
…[3 more quoted lines elided]…
> > >I am new to Cobol and struck a problem in Chapter 17 of this book,the
only
> > >one to date.  Both Chapt 17a and d have the same error code as follows
:
> > >JMP0613-U SORT MERGE LIBARY CANNOT BE LOADED .
> > >FB3BESORT,DLL  CODE = 1157 = CHAPT17A  ADR=00401233.
…[22 more quoted lines elided]…
> Jimmy, Calgary AB
```

#### ↳ Re: Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ed9891.103504927@news1.ibm.net>`
- **References:** `<7sescl$8a5k2$1@titan.xtra.co.nz>`

```
Hope I'm taggin on the proper thread.  It was pointed out to me that I
implied (said) AT&T bought IBM.  AT&T bought IBM Global services, also
known as Advantis, also know as IBM Internet services etc.  They did
this last year and promised no e-mail changes (to me when I asked) but
I guess they just could not keep IBM.NET so they will become
ATTGLOBAL.NET.  Alas, my e-mail address is published in over 15,000
books and I'm not really happy about the whole thing.  So I have
registered a domain name (that I will use for my independant software
sales efforts), and I'm looking for web hosting and e-mail forwarding
that has the features I want.  Once I find it, I'll become someone
else. AT&T is nice enough to forward ibm.net traffic for a year, but
that's it.
```

##### ↳ ↳ Re: Using Learn Cobol 24 Hours by Thane Hubbell

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EF54D6.106ECED3@zip.com.au>`
- **References:** `<7sescl$8a5k2$1@titan.xtra.co.nz> <37ed9891.103504927@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> Hope I'm taggin on the proper thread.  It was pointed out to me that I
…[10 more quoted lines elided]…
> that's it.

This is a lesson to all internet companies and individuals.

This is discussed in the web development book on photo.net, a
worthwhile read for anyone interesting in developing applications for
the web.

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
