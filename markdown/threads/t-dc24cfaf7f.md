[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# They took away COMPAREX!!!

_3 messages · 3 participants · 2003-10_

---

### They took away COMPAREX!!!

- **From:** studlow1@hotmail.com (The Mean Farmer)
- **Date:** 2003-10-27T07:51:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e0465864.0310270751.328232c1@posting.google.com>`

```
I am feeling pretty tied up because they decided to get rid of the
COMPAREX utility and are going to force us to use SuperC and FILE-AID
to do all of our compares.

Personally I don't like this much but I get to deal with the problem.

First off, all of our code is held in librarian (ELIPS).  And SuperC
won't access librarian modules.  I really don't want to go thru the
next XX years of my life copying down librarian source code modules to
a PDS just so I can do a comparex on them.  Is there a
IEBGENER/SORT/UDACS equivalent to copy librarian members to a PDS?? 
Or a way to get SuperC to compare a librarian file???

I would perfer to run these in batch mode so any JCL would be a
godsend as well.


And I don't think I will every understand why they would take away a
utiiity that is used so much.

blah blah blah
```

#### ↳ Re: They took away COMPAREX!!!

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-27T16:37:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lRbnb.3884$Px2.2197@newsread4.news.pas.earthlink.net>`
- **References:** `<e0465864.0310270751.328232c1@posting.google.com>`

```
I won't comment on why this change would be good or bad, but there are two
facilities of (current) Librarian software that MIGHT make your conversion
easier:

 Comparator (and Comparator II) which is a "built-in" comparison utility

 Lib/AM - which provides the ability for other software to read Librarian
files AS IF they were PDS (thus SuperC) should work with them.

 Check with your Librarian support person to determine if you can use either
or both of these - and if so get the correct "training" on how to use them
to do what you want.

P.S. For those reading this thread, these are all IBM mainframe products:

  Comparex - from Serena
    http://www.serena.com/product/aa_comparex.html

   File-Aid - from Compuware
     http://www.compuware.com/products/fileaid/

  Librarian - from Computer Associates
    http://www3.ca.com/Solutions/Collateral.asp?CID=33827&ID=1347

 SuperC - from IBM

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ISPZU210/APPENDIX1.1
```

#### ↳ Re: They took away COMPAREX!!!

- **From:** docdwarf@panix.com
- **Date:** 2003-10-27T12:16:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bnjjtm$78c$1@panix1.panix.com>`
- **References:** `<e0465864.0310270751.328232c1@posting.google.com>`

```
In article <e0465864.0310270751.328232c1@posting.google.com>,
The Mean Farmer <studlow1@hotmail.com> wrote:
>I am feeling pretty tied up because they decided to get rid of the
>COMPAREX utility and are going to force us to use SuperC and FILE-AID
>to do all of our compares.

Who is 'they'?

>
>Personally I don't like this much but I get to deal with the problem.
>
>First off, all of our code is held in librarian (ELIPS).  And SuperC
>won't access librarian modules.

Not even when you specify SUBSYS=LAM?

>I really don't want to go thru the
>next XX years of my life copying down librarian source code modules to
>a PDS just so I can do a comparex on them.

You may not have to.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
