[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol 11 ver4 SEARCH ALL

_4 messages · 4 participants · 1996-03_

---

### Cobol 11 ver4 SEARCH ALL

- **From:** "ric..." <ua-author-17087309@usenetarchives.gap>
- **Date:** 1996-03-19T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<827363016.973@ricfox.demon.co.uk>`

```
Is there a limit to the size of table that can be searched?
If so what is it?
(I have heard that its 32K, but can't find it in the manuals).

Thanks,
Richard Fox.
```

#### ↳ Re: Cobol 11 ver4 SEARCH ALL

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-03-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6d7dcab11f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<827363016.973@ricfox.demon.co.uk>`
- **References:** `<827363016.973@ricfox.demon.co.uk>`

```
If you are referring to IBM's VS COBOL II Release 4 product (MVS, VM and
VSE) the answer is 16MB - the maximum size of a 01 level data item. There
is also a limit of 4M for OCCURS, but with a 4M OCCURS, you would hit the
table size limit at a 4 byte table element. Yup, could hit this but not
very likely. BTW to reach these limits you would need to insure that the
program in running with the DATA(31),RENT,RES compile time options (puts
working storage avbove the 16MB line).

32K and 128K limits were in effect with earlier IBM mainframe COBOL
products such as OS/VS COBOL, ANS V2, ANS V3, ANS V4, etc, etc.



Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: Cobol 11 ver4 SEARCH ALL

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-03-20T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6d7dcab11f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<827363016.973@ricfox.demon.co.uk>`
- **References:** `<827363016.973@ricfox.demon.co.uk>`

```
In <827··.@ric··o.uk>, ric··.@ric··o.uk writes:
› Is there a limit to the size of table that can be searched?
› If so what is it?
…[4 more quoted lines elided]…
› 

There is a general limit of 32k of the size of a table,
so implicitly that limits the size of any table that can
be searched.

Leif Svalgaard
```

#### ↳ Re: Cobol 11 ver4 SEARCH ALL

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1996-03-22T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6d7dcab11f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<827363016.973@ricfox.demon.co.uk>`
- **References:** `<827363016.973@ricfox.demon.co.uk>`

```
ric··.@ric··o.uk wrote:
› 
› Is there a limit to the size of table that can be searched?
…[4 more quoted lines elided]…
› Richard Fox.

Using the old OS/VS Cobol, 32K is the maximum table size limit for
a fixed-occurace table. I believe the limit was at least 64k for
a variable-occurs table. Whatever the maximum, the IBM OS/VS
Cobol limits are small.

With the introduction of the IBM VS Cobol/II compiler, IBM lists
the following as compiler limits for table handling:

OCCURS integer 16mb
Total number of ODO's 4mb
Table size 16mb <---- Answer to your question
Table element 8mb
ASC/DES KEY... 12
Total length (keys) 256 bytes
Indexed by (names) 12
Total num of index names 64k
Size of relative index 32k-2

Even though you could have a table 16mb in size, you need to make
sure your system will allow an executable of that size. Check with
your systems people. Systems' will generally impose a maximum Region
size.

P.S. If you are using IBM's Cobol/II or Cobol/370, all of the
compiler limits information can be found in the 'Application
Programm Language Reference' and 'Application Programming
Reference Summary'.

Hope this helps . . .
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
