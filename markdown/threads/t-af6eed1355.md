[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable length variable

_4 messages · 3 participants · 1998-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Variable length variable

- **From:** "a..." <ua-author-17071896@usenetarchives.gap>
- **Date:** 1998-04-10T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6gmub1$vpg@pellew.ntu.edu.au>`

```

G'day,


I'm not sure what you call this technique, but it allows me to move/display variable length variable.

eg

77 Start-posi pic 99 value 01.
77 var-length pic 99 value 06.

77 test-var pic x(80) value "My pink elephant".


DISPLAY test-var(start-posi : var-length)

output >> My pink



I like to know is this facility is available in newer compilers ?
```

#### ↳ Re: Variable length variable

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-af6eed1355-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6gmub1$vpg@pellew.ntu.edu.au>`
- **References:** `<6gmub1$vpg@pellew.ntu.edu.au>`

```



Alvin Teo wrote in message <6gmub1$v.··.@pel··u.au>...
› G'day,
› 
…[20 more quoted lines elided]…
› 

The technique is called "reference modification". It was introduced via the
'85 ANSI Standard and is available in all ANSI'85 conforming compilers.
```

#### ↳ Re: Variable length variable

- **From:** "mickey ben-tovim" <ua-author-17074116@usenetarchives.gap>
- **Date:** 1998-04-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-af6eed1355-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6gmub1$vpg@pellew.ntu.edu.au>`
- **References:** `<6gmub1$vpg@pellew.ntu.edu.au>`

```

IBM calls it "Refernce Modification". The rest of us call it a
substring.

mickey

Alvin Teo wrote:
› 
› G'day,
…[14 more quoted lines elided]…
› I like to know is this facility is available in newer compilers ?
```

##### ↳ ↳ Re: Variable length variable

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-af6eed1355-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-af6eed1355-p3@usenetarchives.gap>`
- **References:** `<6gmub1$vpg@pellew.ntu.edu.au> <gap-af6eed1355-p3@usenetarchives.gap>`

```



Mickey Ben-Tovim wrote in message <352··.@ho··e.com>...
› IBM calls it "Refernce Modification". The rest of us call it a
› substring.


The ANSI Standard for COBOL and all documentation that conforms to the
ANSI Standard calls it "reference modification". Those who are used to other
languages or tools call it whatever they are used to.

› mickey
› 
…[18 more quoted lines elided]…
›› I like to know is this facility is available in newer compilers ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
