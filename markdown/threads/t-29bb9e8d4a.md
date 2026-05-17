[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Packed-decimal problem!

_4 messages · 4 participants · 1997-10_

---

### Packed-decimal problem!

- **From:** "calvin" <ua-author-104981@usenetarchives.gap>
- **Date:** 1997-10-07T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bcd3e6$ae600b40$0f02000a@calvin>`

```

e.g. 01 amount-1 pic s9(5)v99 usage packed-decimal.

e.g. 01 amount-2 pic s9(5)v99 usage packed-decimal

I would like to ask that why I can't move amount-1 to amount-2?


Calvin
```

#### ↳ Re: Packed-decimal problem!

- **From:** "andrew j. jackson" <ua-author-6589078@usenetarchives.gap>
- **Date:** 1997-10-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-29bb9e8d4a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bcd3e6$ae600b40$0f02000a@calvin>`
- **References:** `<01bcd3e6$ae600b40$0f02000a@calvin>`

```

Calvin wrote:

› e.g. 01 amount-1      pic s9(5)v99      usage packed-decimal.
› 
…[4 more quoted lines elided]…
› Calvin


I don't know about other shops, but in IBM mainframe environmnet
you may not move packed fields a t the group level.

You got SOC7 didn't you?

Richard Jackson
Houston, Tx
```

#### ↳ Re: Packed-decimal problem!

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-10-07T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-29bb9e8d4a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bcd3e6$ae600b40$0f02000a@calvin>`
- **References:** `<01bcd3e6$ae600b40$0f02000a@calvin>`

```

Calvin wrote:
›
› e.g. 01 amount-1 pic s9(5)v99 usage packed-decimal.
…[4 more quoted lines elided]…
›
Calvin,

You *should* be able to do this. What result are you getting?

If you're getting an S0C7 abend it's because 'amount-1' does not contain a valid
numeric value; if you're not sure if you *will* have moved anything to
'amount-1' before moving it to 'amount-2', either MOVE ZERO TO AMOUNT-1 in the
beginning of your program or add a VALUE clause.

If you're getting an S0C4 abend it's possible 'amount-2' is in your LINKAGE
SECTION and you don't have addressability to it.

There--I did your homework for you.

***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

#### ↳ Re: Packed-decimal problem!

- **From:** "gvwm..." <ua-author-9831@usenetarchives.gap>
- **Date:** 1997-10-08T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-29bb9e8d4a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bcd3e6$ae600b40$0f02000a@calvin>`
- **References:** `<01bcd3e6$ae600b40$0f02000a@calvin>`

```

On 8 Oct 1997 12:37:38 GMT, "Calvin" wrote:

› e.g. 01 amount-1 pic s9(5)v99 usage packed-decimal.
›
› e.g. 01 amount-2 pic s9(5)v99 usage packed-decimal
›
› I would like to ask that why I can't move amount-1 to amount-2?

post the procedure division's previous and post 5 lines...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
