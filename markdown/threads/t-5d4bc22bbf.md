[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SORTs ...

_5 messages · 5 participants · 1998-04_

---

### SORTs ...

- **From:** "r.m. de blouw" <ua-author-17084313@usenetarchives.gap>
- **Date:** 1998-04-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35293733.2B4080E1@pi.net>`

```

Hi there,

I'm currently working part-time with a company dealing with (of course)
da millenium shit using Oscar 2000. Oscar is smart, but it isn't so
smart as to convert SORTs.

My question:

Suppose I've go this record and want to sort using a field
999.Date(6)YMD.99 as a key, how can I do this. I mean how do I
temporarily expand the date from 6 to 8 digits determine the position in
a list and shrink it again to 6 digits...

-- Ronald
```

#### ↳ Re: SORTs ...

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1998-04-05T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d4bc22bbf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35293733.2B4080E1@pi.net>`
- **References:** `<35293733.2B4080E1@pi.net>`

```

I'm not entirely sure what '999.Date(6)YMD.99' is suppose to represent, but,
if you want to do an expand on the date field so it'll sort correctly, one
way would be to define the field as PIC 9(08) in the SD, then, before your
RELEASE, expand the input date into the sort entry, and shrink it back after
your RETURN.
```

#### ↳ Re: SORTs ...

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-04-05T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d4bc22bbf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<35293733.2B4080E1@pi.net>`
- **References:** `<35293733.2B4080E1@pi.net>`

```

R.M. de Blouw wrote:
› 
› Hi there,
…[11 more quoted lines elided]…
› 

Do Oscar know de syncsort? If he Do, or even if he don't, Syncsort know
de window.

I hear, that DFSORT know the same window.
```

##### ↳ ↳ Re: SORTs ...

- **From:** "fyae..." <ua-author-17074334@usenetarchives.gap>
- **Date:** 1998-04-07T14:05:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d4bc22bbf-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5d4bc22bbf-p3@usenetarchives.gap>`
- **References:** `<35293733.2B4080E1@pi.net> <gap-5d4bc22bbf-p3@usenetarchives.gap>`

```

In article <352··.@i··.net>,
red··.@i··.net wrote:
› 
› R.M. de Blouw wrote:
…[25 more quoted lines elided]…
› 

I don't know anything about Oscar 2000, but you can
find complete details about DFSORT's Year 2000
features for sorting and transforming two-digit
year dates by reading my SORT2000 paper on the
DFSORT home page at URL:

http://www.ibm.com/storage/dfsort/

or downloading text/Postscript versions from the
DFSORT FTP site at:

ftp://index.storsys.ibm.com/dfsort/mvs/

The SORT2000 paper has a section that discusses how
you can use DFSORT's Year 2000 features from COBOL.

Frank Yaeger - DFSORT Team (Specialties: Y2K,
ICETOOL, OUTFIL)

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: SORTs ...

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-06T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d4bc22bbf-p5@usenetarchives.gap>`
- **In-Reply-To:** `<35293733.2B4080E1@pi.net>`
- **References:** `<35293733.2B4080E1@pi.net>`

```

In article <352··.@p··.net>, R.M. de Blouw wrote:
› Hi there,
› 
…[9 more quoted lines elided]…
› a list and shrink it again to 6 digits...

Is this an IBM mainframe shop using SyncSort? If so then an internal SORT
can be overridden using a $ORTPARM card in the JCL step EXECuting the
program.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
