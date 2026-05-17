[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need help on decimals, DISPLAY

_3 messages · 3 participants · 1997-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Need help on decimals, DISPLAY

- **From:** "jamie" <ua-author-32585@usenetarchives.gap>
- **Date:** 1997-03-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fnf2c$ap1@news.istar.ca>`

```

Hello

1: Which is better form:

05 record-out pic 9(6) DISPLAY "999.99"
or
05 record-out pic 999.99

These are output fields recieving processed fields to be edited and
printed. I was told that the first is the proper way to edit a field
for printer output, but I have never seen DISPLAY used in this context.

2. If I send the data 1123v45(v indicating the implicit decimal) to an
edited field Pic 999.99 will COBOL align the data on the implied
decimal point or simply fill from left to right? That is, would the
output be 123.45, or 112.34?

Regards


=======================33=======================
James Simpson	'I hear the turnin' of the page
		and the comin of a new age
		and the grooms' still standing at the 			altar."
```

#### ↳ Re: Need help on decimals, DISPLAY

- **From:** "chai..." <ua-author-2228828@usenetarchives.gap>
- **Date:** 1997-03-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-20a74e0bcb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5fnf2c$ap1@news.istar.ca>`
- **References:** `<5fnf2c$ap1@news.istar.ca>`

```

COBOL will align the implied decimal to the implicit decimal just fine.
```

#### ↳ Re: Need help on decimals, DISPLAY

- **From:** "dbret..." <ua-author-6588809@usenetarchives.gap>
- **Date:** 1997-03-07T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-20a74e0bcb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5fnf2c$ap1@news.istar.ca>`
- **References:** `<5fnf2c$ap1@news.istar.ca>`

```

COBOL will align your decimals for you if you send something to the PIC
999.99 field. I prefer choice two anyway. I've never used "usage" in
any program, nor have I ever seen it used. (I know that's going to spark
some comment).

Dave
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
