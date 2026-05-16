[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Enterprise COBOL's XML PARSE

_2 messages · 2 participants · 2002-07_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Enterprise COBOL's XML PARSE

- **From:** "Steve Dearth" <steve@dearth.info>
- **Date:** 2002-07-25T17:01:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M9W%8.2807$XG5.2140@newsread1.prod.itd.earthlink.net>`

```
I'm examining IBM Enterprise COBOL and trying to come to an understanding of
its new XML PARSE facilities.  My basic problem/question is this - it
appears from the fairly limited examples in the documentation that the
command expects an entire XML document as its argument.  This seems weird to
me in a record oriented environment.

Does anyone have any experience with this?  Am I correct in my assumptions?
If so, any suggestions on the best way to get the entire file into memory
and process what could be incredibly variable data?
```

#### ↳ Re: Enterprise COBOL's XML PARSE

- **From:** "Larry Kahm" <lkahm@heliotropicsystems.com>
- **Date:** 2002-07-25T17:26:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NwW%8.11124$ub.8475@nwrddc02.gnilink.net>`
- **References:** `<M9W%8.2807$XG5.2140@newsread1.prod.itd.earthlink.net>`

```
Steve,

Yes, the way the COBOL parser works is the way you read and understood it;
the entire file is read into working storage and is then parsed.

The rules for parsing the file are based on your application's business
logic.  You (the application programmer) have to determine which tags
contain the data required by the application program.  You can then perform
any additional processing once you have the data.

For some additional information about this topic, please take a look at my
recent article in Technical Support magazine: Generation X Meets
Tyrannosaurus Rex: Working with XML on the Mainframe
(http://www.naspa.com/02articlesbymonth.htm#may).

I hope that helps!

Larry Kahm
Heliotropic Systems, Inc.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
