[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can I access COM1 or COM2 from RMCOBOL85?

_8 messages · 6 participants · 1997-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Can I access COM1 or COM2 from RMCOBOL85?

- **From:** "joao b." <ua-author-5850388@usenetarchives.gap>
- **Date:** 1997-03-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<331BDCDE.5C8E@mail.telepac.pt>`

```

I would like to know if there is any chance I can
read data from COM1 or COM2 which is connected to
an external device such as a digital thermometer or
a weigh machine.

Thank you.

John.
```

#### ↳ Re: Can I access COM1 or COM2 from RMCOBOL85?

- **From:** "jason" <ua-author-11075@usenetarchives.gap>
- **Date:** 1997-03-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6ef6859ed-p2@usenetarchives.gap>`
- **In-Reply-To:** `<331BDCDE.5C8E@mail.telepac.pt>`
- **References:** `<331BDCDE.5C8E@mail.telepac.pt>`

```

Joao B. wrote:
› 
› I would like to know if there is any chance I can
…[6 more quoted lines elided]…
› John.

John,
Sure can, your COM ports are send and recieve bud. Now finding a device
such as you mentioned that has a connection to a serial device, now that
is another story. I see some electronics classes in your future... Oh
yeah, dude, why are you posting this to this newsgroup?

Good luck
```

##### ↳ ↳ Re: Can I access COM1 or COM2 from RMCOBOL85?

- **From:** "joao b." <ua-author-5850388@usenetarchives.gap>
- **Date:** 1997-03-04T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6ef6859ed-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6ef6859ed-p2@usenetarchives.gap>`
- **References:** `<331BDCDE.5C8E@mail.telepac.pt> <gap-a6ef6859ed-p2@usenetarchives.gap>`

```

Jason wrote:
› 
› Joao B. wrote:
…[16 more quoted lines elided]…
› Good luck
Well, Jason, I do have to connect a peripheral to an RS232 but
the only problem I have is how to get that data from the RS232 inside
the RMCOBOL 85 program. I work with RM as long as 15 years, but I reaaly
can't find the necessary info in the manuals.

In another hand I do not want to use a C external program to get the
data. All I would like to do is to get it just using RMCOBOL and nothing
else.

Thank you

John.
```

###### ↳ ↳ ↳ Re: Can I access COM1 or COM2 from RMCOBOL85?

- **From:** "jaime rezola clemente" <ua-author-6589443@usenetarchives.gap>
- **Date:** 1997-03-04T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6ef6859ed-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6ef6859ed-p3@usenetarchives.gap>`
- **References:** `<331BDCDE.5C8E@mail.telepac.pt> <gap-a6ef6859ed-p2@usenetarchives.gap> <gap-a6ef6859ed-p3@usenetarchives.gap>`

```

Joao B. wrote:
› 
› Jason wrote:
…[30 more quoted lines elided]…
› John.

Vai ser em ingles por atencao para o resto dos leitores...

I had to make a similar program some time ago. The best solution I found
was to make a small program writen in C to handle the communication with
the external device. That program dealt with the protocol of the device
(the device sent blocks of data with a header specifying its length and
type). The C program wrote the data in files in a directory which the
COBOL program would read. To send instructions the COBOL program wrote
other files in the same or another directory.

The files had a structure to ease the reading by COBOL.

I did not program directly with COBOL because I couldn't garantee the
speed of the program was enough to react to the communication port.

Hope this helps.

Cumprimentos


Jaime Rezola Clemente
rez··.@mai··c.pt
```

###### ↳ ↳ ↳ Re: Can I access COM1 or COM2 from RMCOBOL85?

- **From:** "jon richardson" <ua-author-718469@usenetarchives.gap>
- **Date:** 1997-03-04T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6ef6859ed-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6ef6859ed-p3@usenetarchives.gap>`
- **References:** `<331BDCDE.5C8E@mail.telepac.pt> <gap-a6ef6859ed-p2@usenetarchives.gap> <gap-a6ef6859ed-p3@usenetarchives.gap>`

```

Joao B. wrote:
› 
› Jason wrote:
…[30 more quoted lines elided]…
› John.


Your program should simply be able to treat COMn as another file.
```

###### ↳ ↳ ↳ Re: Can I access COM1 or COM2 from RMCOBOL85?

- **From:** "jason" <ua-author-11075@usenetarchives.gap>
- **Date:** 1997-03-05T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6ef6859ed-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6ef6859ed-p3@usenetarchives.gap>`
- **References:** `<331BDCDE.5C8E@mail.telepac.pt> <gap-a6ef6859ed-p2@usenetarchives.gap> <gap-a6ef6859ed-p3@usenetarchives.gap>`

```

Joao B. wrote:
› 
› Jason wrote:
…[30 more quoted lines elided]…
› John.

John,

You have me beat on the experience side of RM (I have been working with
it for 3 months). But allow me to share something useful (maybe) to
you. I posted to this group wanting docs on RM-COBOL and a friendly
chap responded to my inquiry with the company that currently owns the RM
compiler (Liant software) and thier 800 # 1-800-RMCOBOL maybe they
have something that would help you.

Have a day, Jason
```

###### ↳ ↳ ↳ Re: Can I access COM1 or COM2 from RMCOBOL85?

_(reply depth: 4)_

- **From:** "rbryan" <ua-author-6596844@usenetarchives.gap>
- **Date:** 1997-03-05T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6ef6859ed-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6ef6859ed-p6@usenetarchives.gap>`
- **References:** `<331BDCDE.5C8E@mail.telepac.pt> <gap-a6ef6859ed-p2@usenetarchives.gap> <gap-a6ef6859ed-p3@usenetarchives.gap> <gap-a6ef6859ed-p6@usenetarchives.gap>`

```

On Thu, 6 Mar in the year of the ox, Jason wrote:

› Joao B. wrote:
›› 
…[44 more quoted lines elided]…
› 

I'm not too sure about RMCOBOL but try the following:

SELECT IN-FILE
ASSIGN TO COM1
FILE STATUS IS FILE-STATUS.

or

SELECT IN-FILE
ASSIGN TO "COM1"
FILE STATUS IS FILE-STATUS.

Then use it just like any other sequential file. What the hey
it only costs a compile.
```

#### ↳ Re: Can I access COM1 or COM2 from RMCOBOL85?

- **From:** "tod reinheimer" <ua-author-2792466@usenetarchives.gap>
- **Date:** 1997-03-09T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6ef6859ed-p8@usenetarchives.gap>`
- **In-Reply-To:** `<331BDCDE.5C8E@mail.telepac.pt>`
- **References:** `<331BDCDE.5C8E@mail.telepac.pt>`

```

There is a utility that started shipping with RM/Cobol85 version 5.1 (the
name escapes me completely) that allows you to execute any command line
statement and get values back. So, if you have a routine that you would
like to have access your com ports and check the status of the call, that
would work. If you're looking to get complete control just with RM/Cobol I
don't think you can do so.

Joao B. wrote in article
<331··.@mai··c.pt>...
› I would like to know if there is any chance I can
› read data from COM1 or COM2 which is connected to
…[6 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
