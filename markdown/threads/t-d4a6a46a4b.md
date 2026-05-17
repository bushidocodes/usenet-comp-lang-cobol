[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Check Writing

_5 messages · 4 participants · 1997-09_

---

### Check Writing

- **From:** "bo..." <ua-author-585336@usenetarchives.gap>
- **Date:** 1997-09-18T20:24:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<874628659.3509@dejanews.com>`

```

Greeting all, I would appreciate some pointer, for creating a check
writing program using COBOL. Especially setting up a table to print the
wording for the dollar amounts. I admit this is a school project. Our
Professor suggested we contact some more experienced programmers to find
more than one way of doing it.

Thanks in advance

Cedrick

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Check Writing

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-09-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d4a6a46a4b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<874628659.3509@dejanews.com>`
- **References:** `<874628659.3509@dejanews.com>`

```

bo··.@hot··l.com wrote:

› Greeting all, I would appreciate some pointer, for creating a check
› writing program using COBOL. Especially setting up a table to print the
…[9 more quoted lines elided]…
›      http://www.dejanews.com/     Search, Read, Post to Usenet
You can index into tables using the numeric values in the SPECIFIC
places in your numeric field. Then you STRING the words together using
a POINTER to keep track of the current end of string.

Watch out for the irregular forms like TWELVE, THIRTEEN etc.

The rest is just coding your homework.

Piece of cake.

JR
and stir with a Runcible spoon...
```

#### ↳ Re: Check Writing

- **From:** "e jon" <ua-author-17071971@usenetarchives.gap>
- **Date:** 1997-09-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d4a6a46a4b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<874628659.3509@dejanews.com>`
- **References:** `<874628659.3509@dejanews.com>`

```

bo··.@hot··l.com wrote:

› Greeting all, I would appreciate some pointer, for creating a check
› writing program using COBOL. Especially setting up a table to print
…[8 more quoted lines elided]…
› Cedrick

Gosh, I remember that project. You need to convert the dollars and
cents to
zoned-decimal (ie: characters), then use a loop to process from left to
right
each place value, then process the decimal positions.

You want $53,145.35 to read :
"Fifty-three thousand one-hundred fourty-five dollars and thirty-five
cents"

Hint: Use a table for the place values, such as thousand, hundred,
dollars and cents etc.

The trick is knowing when to hyphenate and when to throw out a place
value
which should depend upon where you are in the characters you're scanning

from left to right.
```

#### ↳ Re: Check Writing

- **From:** "bo..." <ua-author-585336@usenetarchives.gap>
- **Date:** 1997-09-23T15:42:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d4a6a46a4b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<874628659.3509@dejanews.com>`
- **References:** `<874628659.3509@dejanews.com>`

```

In article ,
dbr··.@net··m.com (David K. Bryant) wrote:
› 
› bo··.@hot··l.com writes:
…[5 more quoted lines elided]…
› easier to do.  Other than that,  WE DON'T DO HOMEWORK.

LOL, Thanks to everyone for the hints.

Peace

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Check Writing

- **From:** "judson d. mcclendon" <ua-author-19104@usenetarchives.gap>
- **Date:** 1997-09-26T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d4a6a46a4b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<874628659.3509@dejanews.com>`
- **References:** `<874628659.3509@dejanews.com>`

```

bo··.@hot··l.com wrote in article <874··.@dej··s.com>...
› Greeting all, I would appreciate some pointer, for creating a check
› writing program using COBOL. Especially setting up a table to print the
› wording for the dollar amounts. I admit this is a school project. Our
› Professor suggested we contact some more experienced programmers to find
› more than one way of doing it.

Below find a Micro-Focus COBOL program which demonstrates a routine which
formats a numeric dollar amount into several lines of text, delimited by
asterisks, to be placed on a check. The '78' constants may be changed to
specify how many lines of what length are to be output. If your COBOL is
before COBOL85, you can change the 78's to 77's, along with the WS
references.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
