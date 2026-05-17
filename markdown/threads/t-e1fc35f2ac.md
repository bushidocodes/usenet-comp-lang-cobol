[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A question from the curious

_7 messages · 5 participants · 1998-04_

---

### A question from the curious

- **From:** "jbrook" <ua-author-17074308@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6gtu1d$ms8@corn.cso.niu.edu>`

```

I am a student and taking a beggining course in COBOL. I have seen in this
newsgroup people using statements such as.

77 INDEX-1 PIC S9999 VALUE +0 COMP.

Im just wondering what the COMP statement does. We are at the end of our
course and i know we will not use that.

Thanks
JBrook
```

#### ↳ Re: A question from the curious

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1fc35f2ac-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6gtu1d$ms8@corn.cso.niu.edu>`
- **References:** `<6gtu1d$ms8@corn.cso.niu.edu>`

```



Jbrook wrote in message <6gtu1d$m.··.@cor··u.edu>...
› I am a student and taking a beggining course in COBOL.  I have seen in this
› newsgroup people using  statements such as.
…[9 more quoted lines elided]…
› 

I am a little surprised that a full course never got to USAGE COMPUTATIONAL,
but it is possible. If your course was trying to teach you a version of
COBOL that would work the same on ALL platforms and with all compilers, this
is a feature that syntactically is defined as Standard, but has platform
specific semantics.

The bottom-line is that in most (probably all?) platforms, using USAGE
COMPUTATIONAL is the most efficient way to define a subscript. This lets
your compiler compute the offset of a specific table entry using the least
possible number of machine instructions.

If your subscript is actually based on a value that comes in with another
USAGE, then it is usually (but not quite always) the best coding technique
to set up a separate data item to use as a subscript and then move the input
field to this before using it as a subscript. If the value that you will
want to use as a subscript is totally under your control (never coming in
from an outside file nor going out in a printed format) then you should set
it up as computational to start with.

Note: In many (actually most - but not quite all) environments USAGE
COMPUTATIONAL and USAGE BINARY are identical (and both are ANSI Standard
USAGEs). Therefore, if your course already covered USAGE BINARY, then you
really know almost everything you need to know about USAGE COMPUTATIONAL.
```

##### ↳ ↳ Re: A question from the curious

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1998-04-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1fc35f2ac-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1fc35f2ac-p2@usenetarchives.gap>`
- **References:** `<6gtu1d$ms8@corn.cso.niu.edu> <gap-e1fc35f2ac-p2@usenetarchives.gap>`

```

William M. Klein wrote:
[snip]
› 
› The bottom-line is that in most (probably all?) platforms, using USAGE
› COMPUTATIONAL is the most efficient way to define a subscript.  This
› lets your compiler compute the offset of a specific table entry using the
› least possible number of machine instructions.

Bill, you are normally dead-on accurate, but this time you missed!

While you can claim a technicality here (subscript vs. index), the 'most
efficient' way to describe a 'subscript' is to use INDEXED BY (but not
USAGE INDEX). COBOL standard semantics force the compiler writer to
store an occurrence number in a subscript, whereas an index (defined by
an INDEXED BY) may contain any value that is convenient to the
subscripting of a table. Such conveniences include being zero-relative
(occurrences are defined as one-relative) and adding and subtracting the
span (length of a single table item) rather than one, thus obviating the
need for a multiply (by the span) when it is time to compute the address
of the desired table item. Alas, the syntax for index items is
different ('SET index UP BY 1' rather than 'ADD 1 TO index'), making it
seem obscure.

[snip]
› Note: In many (actually most - but not quite all) environments USAGE
› COMPUTATIONAL and USAGE BINARY are identical (and both are ANSI
› Standard USAGEs). [snip]

N.B. for those folks who are still clinging to the old RM/COBOL (1974)
or are using an RM/COBOL-74 compatibility mode: you are included in the
'not quite all' group Bill mentions. COMP in RM/COBOL (1974) is
unpacked BCD, now a quite antiquated notion, but a good choice then.

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation   http://www.liant.com/
512-343-1010  FAX:512-343-9487
```

###### ↳ ↳ ↳ Re: A question from the curious

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-04-13T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1fc35f2ac-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1fc35f2ac-p3@usenetarchives.gap>`
- **References:** `<6gtu1d$ms8@corn.cso.niu.edu> <gap-e1fc35f2ac-p2@usenetarchives.gap> <gap-e1fc35f2ac-p3@usenetarchives.gap>`

```

I agree that indexing is usually (but as with the rest of this post - not
always) more efficient than using a subscript. In fact, the Standard allows
(and some compilers do) store an index as a "subscript" (i.e. as an
occurrence number). For those environments, indexing is no more efficient
than subscripting. A few related notes (mostly "trivia" for the pedantic):

1) In the '85 Standard, the term subscripting was expanded to include
indexing. Personally, I find this confusing at times, but it does support
Tom's assertion that the most efficient way to do subscripting is with an
index (i.e. an INDEXED BY item).

2) Related to item 1, both relative indexing and relative subscripting are
supported with the current Standard. In the draft of the next Standard, any
"arithmetic expression" can be used as a subscript (including -as I recall -
a reference to a subscripted data item). I think this will be a useful
enhancement, but it does scare me a bit. (I think - but am not positive -
that some compilers already allow this as an extension).

3) The most common (as far as I know today) place where COMP does not equate
to BINARY is COBOL/400 where COMP is equal to Packed-Decimal.
```

##### ↳ ↳ Re: A question from the curious

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-14T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1fc35f2ac-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1fc35f2ac-p2@usenetarchives.gap>`
- **References:** `<6gtu1d$ms8@corn.cso.niu.edu> <gap-e1fc35f2ac-p2@usenetarchives.gap>`

```

William M. Klein wrote:

› The bottom-line is that in most (probably all?) platforms, using USAGE
› COMPUTATIONAL is the most efficient way to define a subscript.  This lets
› your compiler compute the offset of a specific table entry using the least
› possible number of machine instructions.

Not all platforms. Back around 1979, Burroughs developed corporate
standards for Cobol-74, to enhance portablity between the various
Burroughs families. They decided that COMP should mean packed decimal,
which was the most efficient representation on Medium Systems, but not
Large. Unisys A Series is still living with this decision, so COMP is
generally not as efficient as BINARY. However there is a compile time
option BINARYCOMP which makes COMP the same as BINARY.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \      Todd McCormick released after 12 day illegal incarceration
e    |\ for using Marinol w/ prescription: http://www.freecannabis.org
Y    |/     http://www.marijuanamagazine.com/toc/articles/toddfree.htm
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

#### ↳ Re: A question from the curious

- **From:** "jbrook" <ua-author-17074308@usenetarchives.gap>
- **Date:** 1998-04-13T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1fc35f2ac-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6gtu1d$ms8@corn.cso.niu.edu>`
- **References:** `<6gtu1d$ms8@corn.cso.niu.edu>`

```

Well I did look in my book "COBOL From Micro to Mainframe" by Robert T.
Grauer and Carol Vazquez Villar and there is NO reference to the COMP
statement. Reading some of the other responses, we have done subscripted
tables, and indexed tables. So im still not really sure where COMP comes
in. Oh well.

thanks for the info
JBrook
Renegade wrote in message <353··.@new··x.com>...
› All of a sudden, "Jbrook"  wrote:
› 
…[24 more quoted lines elided]…
›
```

##### ↳ ↳ Re: A question from the curious

- **From:** "gary lee" <ua-author-1751270@usenetarchives.gap>
- **Date:** 1998-04-16T06:19:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1fc35f2ac-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1fc35f2ac-p6@usenetarchives.gap>`
- **References:** `<6gtu1d$ms8@corn.cso.niu.edu> <gap-e1fc35f2ac-p6@usenetarchives.gap>`

```

Some of your confusion may be in looking for a 'statement' COMP. COMP is a
possible value in the USAGE 'clause' (as others have pointed out). A
'statement' is another thing entirely. Look under the USAGE clause in the
chapter on the DATA division.

Gary Lee gl··.@nsp··m.com (Remove the spam filter, etc.)

Jbrook wrote in article
<6h0j2r$n.··.@cor··u.edu>...
› Well I did look in my book "COBOL From Micro to Mainframe" by Robert T.
› Grauer and Carol Vazquez Villar and there is NO reference to the COMP
…[3 more quoted lines elided]…
› in.  Oh well.
------------ snip ---------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
