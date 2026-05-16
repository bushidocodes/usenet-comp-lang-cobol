[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to do GO TO in ANSI85 COBOL

_2 messages · 2 participants · 1994-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`Help requests and how-to`](../topics.md#help)

---

### Re: How to do GO TO in ANSI85 COBOL

- **From:** brucea@atlas.com (Bruce Arbuckle)
- **Date:** 1994-12-02T16:31:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1994Dec2.163115.17069@atlas.com>`
- **References:** `<3b882g$9qk@ixnews1.ix.netcom.com>`

```
In article <3b882g$9qk@ixnews1.ix.netcom.com> kurtmisc@ix.netcom.com (Kurt Miscovich) writes:
>>In article <3b0c3v$l7r@charles.cdec.polymtl.ca>
>		or
…[9 more quoted lines elided]…
>simpler.

Let me give you an example:
 perform p-100 thru p-200
 .
 .
 .
 p-100.
      do what ever.
	do what ever.
	go to p-200.
p-101.

	do what ever.
	go to p-200
p-102.
.
.
.
p-200.	
	exit 
```

#### ↳ Re: Avoiding GO TO

- **From:** Richard_Plinston@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1994-12-03T18:47:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3294336.67668.14675@kcbbs.gen.nz>`
- **References:** `<1994Dec2.163115.17069@atlas.com>`

```
>> 
>>Although you can use GO TO the use of GO TO in a COBOL program is 
…[18 more quoted lines elided]…
> exit 

In what way is this supposed to be simpler than alternate code that
is equivalent ?  

I presume that there should be some IFs preceeding the GO TOs so that
this is a selection block.  Try it as an evaluate.

     EVALUATE Control-Value
     WHEN 100
           do whatever
     WHEN 101
           do 101 whatever
     .....
     END-EVALUATE

In my view this may be 'simpler' because it is very much clearer
what the code is actually doing, wheras someone searching the code may
come across p-102 and not realise that it is part of the block being
PERFORMed.

hope this helps
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
