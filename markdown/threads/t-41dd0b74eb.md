[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wrong e-mail address above.

_3 messages · 3 participants · 1997-11_

---

### Wrong e-mail address above.

- **From:** "desperate programmer" <ua-author-17072939@usenetarchives.gap>
- **Date:** 1997-11-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3481B5D8.D48BDCBD@mail.com>`

```

Do not respond to the above request for "How do you open two records".
The address is wrong.

How do I read two records and put them into two separate tables. I know

that I must connect the O/S to the records with a "sysin=". Do I
connect them with a command such as "sysin=abc, xyz" or what. When I
connect it to the O/S I then bring the records into the program in by an

OPEN INVENT-FILE, INVENT-FILE-2.

Am I close? Just a little guidance would help a great deal.

Thanks
```

#### ↳ Re: Wrong e-mail address above.

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1997-11-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-41dd0b74eb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3481B5D8.D48BDCBD@mail.com>`
- **References:** `<3481B5D8.D48BDCBD@mail.com>`

```

Desperate Programmer wrote:
› 
› Do not respond to the above request for "How do you open two records".
…[12 more quoted lines elided]…
› Thanks

I don't think you know enough about Cobol -- or your operating system
(MVS?) -- for us to be helpful. Are you familiar with the READ verb?
That sounds like a silly question, but I get the impression you're
trying to read with the OPEN verb.
I  |\   Randall Bart                      mailto:Bar··.@usa··m.net
L  |/   
o  |\        Bar··.@wor··m.net  Bar··.@hot··m.com
v  | \  1-818-985-3259                       Please reply without spam
e    |\ 
Y    |/ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
o    |\ 
u    |/ Have you solved http://members.aol.com/PanicYr00/Sequence.html
```

#### ↳ Re: Wrong e-mail address above.

- **From:** "byrd house" <ua-author-15568987@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-41dd0b74eb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3481B5D8.D48BDCBD@mail.com>`
- **References:** `<3481B5D8.D48BDCBD@mail.com>`

```

I am not quite sure what you said, but if your using COBOL, and you want to
open two
records you just define their FD's and open them

my typical open statement:

OPEN FOR INPUT INVENT-FILE
INVENT-FILE-2

*shrug*

Bryce


Desperate Programmer wrote in message <348··.@ma··l.com>...
› Do not respond to the above request for "How do you open two records".
› The address is wrong.
…[14 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
