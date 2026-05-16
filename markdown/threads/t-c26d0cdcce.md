[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File formatting.

_1 message · 1 participant · 1999-05_

---

### Re: File formatting.

- **From:** warrenp123@netdoor123.com (warrenp123@netdoor123.com)
- **Date:** 1999-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc.1dcede5a849400001dcede5afd953dd0.4018ba6@city.magnet.at>`

```

John wrote in message ...
>I am writing a program in Cobol to convert an ASCII file into a formatted
>file so that I can import the files into a database.
…[4 more quoted lines elided]…
>I want to read a line at a time and then look at each character for
[ and ].
>  Is there a better way?  PLEASE HELP.

Yes.  Try the UNSTRING statement.  First define a numeric field to help
with
this statment:   01  WS-POINT    PIC 999.    I also assume you would define
FIELD-NAME and FIELD-DATA there as well. Then in the procedure division:

MOVE 1 TO WS-POINT.

And within a loop or PERFORM statement:

IF IN-REC(WS-POINT:1) NOT = SPACE
  UNSTRING IN-REC DELIMITED BY "[" INTO FIELD-NAME POINTER WS-POINT
  UNSTRING IN-REC DELIMITED BY "]" INTO FIELD-DATA POINTER WS-POINT
   ... Code to process each field would go here.

>
>Also I will need to search and replace - is it possible to replace end of
>line chars with spaces?  How do I look for end of line chars.

Define your input file ORGANIZATION LINE SEQUENTIAL and you won't have to.
Short lines will be padded out with spaces.  The IF statement checks to see
if you have reached the end.


Warren Porter -- Remove numbers to reply.



Message-ID: <udFZ2.102$r14.11510@axe.netdoor.com>
Path:
magnet.at!newsfeed03.univie.ac.at!newscore.univie.ac.at!howland.erols.net!newsfeed.wli.net!su-news-hub1.bbnplanet.com!atl-news-feed1.bbnplanet.com!news.gtei.net!axe.netdoor.com!not-for-mail
Date: Mon, 10 May 1999 13:05:12 -0500
From: "Warren Porter" <warrenp123@netdoor123.com>
Organization: Internet Doorway, Inc. -- http://www.netdoor.com/
Subject: Re: File formatting.
Lines: 37
Newsgroups: comp.lang.cobol
References: <DoEZ2.3184$%x.2654@wards>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
