[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL SCREEN Questions!

_3 messages · 3 participants · 1997-09_

---

### COBOL SCREEN Questions!

- **From:** "calvin" <ua-author-104981@usenetarchives.gap>
- **Date:** 1997-09-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bcc907$f32259c0$0f02000a@calvin>`

```

what are differences among FROM, TO, USING while using PICTURE in SCREEN
SECTION?

Calvin
```

#### ↳ Re: COBOL SCREEN Questions!

- **From:** "daniel g. cantua" <ua-author-17073049@usenetarchives.gap>
- **Date:** 1997-09-23T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe534d2dec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bcc907$f32259c0$0f02000a@calvin>`
- **References:** `<01bcc907$f32259c0$0f02000a@calvin>`

```

Calvin wrote:

› what are differences among FROM, TO, USING while using PICTURE in
› SCREEN
› SECTION?
› 
› Calvin

When you use the FROM with the PICTURE clause of the SCREEN SECTION,
it is getting the data from another variable, and when you accept the
screen the orginal variable will be unchanged. When using the TO, you
must also use the FROM, and after the accept of the screen, the variable
after the FROM is unchanged and the variable after the TO hold the
results of the accept. In the case of the USING, the variable is
displayed and can be change after the accept. This is according to
MicroFocus COBOL's Language Reference Manual

Daniel G. Cantua
Los Angeles County - ISD
```

#### ↳ Re: COBOL SCREEN Questions!

- **From:** "byrd house" <ua-author-15568987@usenetarchives.gap>
- **Date:** 1997-09-25T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe534d2dec-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bcc907$f32259c0$0f02000a@calvin>`
- **References:** `<01bcc907$f32259c0$0f02000a@calvin>`

```

Calvin wrote in article
<01bcc907$f32259c0$0f02000a@calvin>...
› what are differences among FROM, TO, USING while using PICTURE in SCREEN
› SECTION?
›
› Calvin

Now to show that a little knowledge is a bad thing :)

We could say that the picture clause is simply an data location within the
"record" of the screen.

I don't know about other versions of COBOL but on MFCOBOL:

If one uses say FROM PREV-REC-NUM then when the screen is DISPLAYed any
data that is held in the PREV-REC-NUM field will be inserted into the
picture and will be truncated if too long or produce an error if they are
the wrong type (alpha from numeric). Basically the same for ACCEPT but one
may modify the "inserted" information.

TO is the same as FROM accept that no info is taken from the PREV-REC-NUM
field but when an accept is excecuted any info entered in that area will
then be inserted into that field.

USING basically does both, taking the data from the field, allows you to
change it, and then put it back.

Sorry for the rough explanation, I've had to learn this on my own.

If I'm wrong, tell me, but don't tell me if you don't know what the correct
answer is :)

EMAIL: by··.@ra··x.com subject "Bryce personal"

thanks for your time

Bryce Byrd-LaBove
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
