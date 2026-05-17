[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Has anyone Migrated from Wang to MFC

_2 messages · 2 participants · 1998-06_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Has anyone Migrated from Wang to MFC

- **From:** "john..." <ua-author-3781614@usenetarchives.gap>
- **Date:** 1998-06-08T21:25:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6li2to$nn6$1@nnrp1.dejanews.com>`

```

Has anyone out there migrated from Wang Cobol to Microfocus Cobol? We have a
Wang VS 85 and we are thinking of moving to Microfocus Cobol. The Wang is not
Y2K nor can it be without buying new hardware.
Is MFC a good idea or are there easier solutions?

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Has anyone Migrated from Wang to MFC

- **From:** "david furin" <ua-author-6588918@usenetarchives.gap>
- **Date:** 1998-06-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c03aa35df1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6li2to$nn6$1@nnrp1.dejanews.com>`
- **References:** `<6li2to$nn6$1@nnrp1.dejanews.com>`

```

joh··.@ho··e.com wrote:
›
› Has anyone out there migrated from Wang Cobol to Microfocus Cobol?

Yes. There are several options depending on your desired outcome.

There are tools to convert your Wang code into 'native' COBOL (i.e., all
Wang syntax removed and replaced with functionally equivalent code).
This provides you the cleanest break from the VS, but involves a high
degree of modification to your source (IMO). The nice thing is that
your code becomes more 'standard' and does not rely on Wang-specific
extensions, file/library/volume conventions, etc. The conversion tools
most likely provide callable subroutines to replace many of the VS
functions.

The other side of the VS migration issue is to use your Wang code
essentially 'as is' by using a pre-compiler to interpret your Wang
syntax. This approach gets you off the VS faster and with fewer
modifications to your code, but leaves you tied strongly to the
conversion vendor.

Either choice is valid and has advantages and disadvantages. We chose
the second approach for various reasons--migrating off our ancient
VS-100 in 1995. We used the VUPort product from San Soft, Inc. Looking
back, it wasn't as painful as I thought it would be, but we are still on
the learning curve regarding system administration in the 'open' world.

Of course, you can simply buy a new VS. These days Wang seems to be
viable again--they are building ever-bigger VS machines. Certainly your
ancient VS-85 can be duplicated in the smallest new(er) VS. Keep in
mind that you will NOT see another platform as easy to use and
administer as the VS (IMHO).

David Furin                   |
                              | email:  dan··.@wor··t.net
Information Systems Manager   | smail:  2600 St. Clair Ave. NE
LaRich Distributors, Inc.     |         Cleveland, OH  44114  USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
