[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM85 Indexed files

_6 messages · 4 participants · 1998-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### RM85 Indexed files

- **From:** "oam" <ua-author-3431686@usenetarchives.gap>
- **Date:** 1998-04-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6h0a11$468$1@diana.bcn.ibernet.es>`

```

I've received a new client from other software house with an RM85
aplication. This client does not have the source code of this application,
and wants to migrate data to other platform.
I can see the data but I can't interpretate the numerics fields (comp-3,
etc) of the data files nor the structure of the data-record. The
compression-algorithm of these fields is too complex to guess. I need help
for migrate information from these files. Maybe there is a tool that does
it or information about the format of the numerics fields in RM85 v6.
Thanks you all.
```

#### ↳ Re: RM85 Indexed files

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1998-04-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f4c3fed1d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6h0a11$468$1@diana.bcn.ibernet.es>`
- **References:** `<6h0a11$468$1@diana.bcn.ibernet.es>`

```

My company used to use RM85 so we still have the file utilities that
will help you. They run on Unix.. One is rmmapinx which will print
the index structure of any file. We also have two recover programs
that will dump all the records in an index file to an ascii file.

Send me some email so we can talk.

Paul


"oam" wrote:

› I've received a new client from other software house with an RM85
› aplication. This client does not have the source code of this application,
…[9 more quoted lines elided]…
›
```

##### ↳ ↳ Re: RM85 Indexed files

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1998-04-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f4c3fed1d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3f4c3fed1d-p2@usenetarchives.gap>`
- **References:** `<6h0a11$468$1@diana.bcn.ibernet.es> <gap-3f4c3fed1d-p2@usenetarchives.gap>`

```

Paul DuBois wrote:
› 
› My company used to use RM85 so we still have the file utilities that
…[6 more quoted lines elided]…
› Paul

I have refrained from responding so far but...

Paul, please remember to conform to the license provisions regarding
distribution rights.

Sr. Oskar M. can also _license_ these from his _local_ Liant
distributor. Then he would be in possession of _licensed_ software.
Liant has an excellent distributor in Spain.

› 
› "oam"  wrote:
…[16 more quoted lines elided]…
›› 

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

###### ↳ ↳ ↳ Re: RM85 Indexed files

- **From:** "pa..." <ua-author-6589140@usenetarchives.gap>
- **Date:** 1998-04-15T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f4c3fed1d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3f4c3fed1d-p3@usenetarchives.gap>`
- **References:** `<6h0a11$468$1@diana.bcn.ibernet.es> <gap-3f4c3fed1d-p2@usenetarchives.gap> <gap-3f4c3fed1d-p3@usenetarchives.gap>`

```

Tom Morrison (t.m··.@li··t.com) wrote:

: I have refrained from responding so far but...

: Paul, please remember to conform to the license provisions regarding
: distribution rights.

: Sr. Oskar M. can also _license_ these from his _local_ Liant
: distributor. Then he would be in possession of _licensed_ software.
: Liant has an excellent distributor in Spain.


Tom -
I'm not the Paul that started this (I think) but I have an exactly
similar problem. I have some RM Data I have to convert out to another
platform, and in my case, some of the data is so old that it is
not convertable with the utitlies I have.


Besides which, I had a really horrible experience with your sales
people. Sure, I could go out and buy a copy of RM/COBOL, and
send you over $1K for a product I'm not going to use, but it is
perfectly legal for me to ask an owner of an ancient copy of
RM/COBOL to just convert them out for me.



-Paul Raulerson
```

###### ↳ ↳ ↳ Re: RM85 Indexed files

_(reply depth: 4)_

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1998-04-15T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f4c3fed1d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3f4c3fed1d-p4@usenetarchives.gap>`
- **References:** `<6h0a11$468$1@diana.bcn.ibernet.es> <gap-3f4c3fed1d-p2@usenetarchives.gap> <gap-3f4c3fed1d-p3@usenetarchives.gap> <gap-3f4c3fed1d-p4@usenetarchives.gap>`

```

paulr wrote:
›  Besides which, I had a really horrible experience with your sales
› people. Sure, I could go out and buy a copy of RM/COBOL, and
…[4 more quoted lines elided]…
› -Paul Raulerson

Yes, that is quite legal, and, in a private email "the other Paul"
indicated that, indeed, that was his intent. If my posting was too
pointed, I publicly apologize to Paul DuBois.

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

###### ↳ ↳ ↳ Re: RM85 Indexed files

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1998-04-15T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f4c3fed1d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3f4c3fed1d-p3@usenetarchives.gap>`
- **References:** `<6h0a11$468$1@diana.bcn.ibernet.es> <gap-3f4c3fed1d-p2@usenetarchives.gap> <gap-3f4c3fed1d-p3@usenetarchives.gap>`

```

Tom Morrison wrote:

› I have refrained from responding so far but...
› 
…[7 more quoted lines elided]…
›› 
Tom,

Thanks for your concern, but I would not be violating anything. My
aim is to have him send me the data, then I would create an ascii
file(s) for him, then send the converted data back. I resolutely
believe in copyrights, and would never violate them because I know
what it takes to produce software. OTOH, if it was a Microsoft
product........

As a side note, I haven't heard from the original poster yet anyway.

Paul
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
