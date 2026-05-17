[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can anybody help a COBOL novice?

_5 messages · 5 participants · 1997-01_

---

### Can anybody help a COBOL novice?

- **From:** "s. saalfield" <ua-author-17071900@usenetarchives.gap>
- **Date:** 1997-01-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`

```

I am currently trying to write what is probably a fairly simply program,
but have run across two obstacles:

1) I need to compute and print a percentage (example 200/12000). How would
I do this with moving rules involving decimals?
2) I need to continually print districts, within states, that have
information in the array/table. What I have looks like this:

Perform varying state from 1 by 1 until > 50
after district from 1 by 1 until = 99 (how would I print district 99?) my
pic is 99.

IF T1-KIDS-PER-DISTRICT (IM-STATE-NUMBER,
IM-DISTRICT-NUMBER)> 0
OR T1-TOTAL-IMMUNIZED (IM-STATE-NUMBER,
IM-DISTRICT-NUMBER)> 0
MOVE ZEROS TO W-PERCENT
MOVE IM-DISTRICT-NUMBER TO P-DL-DISTRICT
MOVE T1-KIDS-PER-DISTRICT (IM-STATE-NUMBER,
IM-DISTRICT-NUMBER)
TO P-DL-TOTAL-NUMBER
MOVE T1-TOTAL-IMMUNIZED (IM-STATE-NUMBER,
IM-DISTRICT-NUMBER)
TO P-DL-TOTAL-IMMUNIZED
COMPUTE W-PERCENT =
T1-TOTAL-IMMUNIZED (IM-STATE-NUMBER,
IM-DISTRICT-NUMBER)/
T1-KIDS-PER-DISTRICT (IM-STATE-NUMBER,
IM-DISTRICT-NUMBER)
END-COMPUTE
MOVE W-PERCENT TO P-DL-PERCENT
WRITE PRINT-RECORD FROM P-DETAIL-LINE1
AFTER ADVANCING 1 LINE
ADD 1 TO A-LINE-CT
END-IF.


My problem is that it will only print out one district within one state.
Any brilliant people out there to help?
```

#### ↳ Re: Can anybody help a COBOL novice?

- **From:** "ggr..." <ua-author-1091801@usenetarchives.gap>
- **Date:** 1997-01-16T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eaf04d993a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`
- **References:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`

```

On 18 Jan 1997 22:04:40 GMT, "S. Saalfield"
wrote:

› 1) I need to compute and print a percentage (example 200/12000). How would
› I do this with moving rules involving decimals?

You need to use edited fields here. Make like this...not to scale,
and may not even be compilable, but it ought to show the general idea.

DATA DIVISION
01 percentage-whole pic 999v99.
01 percentage-write pic zz9.99.

Percentage-write floats the first two digits...like if I moved 83.33
there it would show up as 83.33 as you were probably trying to
(were you getting 083.33?) The Z represents a floatable position..(if
it's 0, it doesn't print). The extra . prints exactly as is. As a
note you'll see by some code below, you can't compute directly into an
edited field (which is what percentage-write represents). You have to
be very judicious about where you put the Z's. If you put all Z's and
the value was 0, you'd get nothing but spaces...and if you put a zero
after the decimal point, you'd get incorrect output.

COMPUTE PERCENTAGE-WHOLE = (200/12000)*100.
MOVE PERCENTAGE-WHOLE TO PERCENTAGE-WRITE.

› 2) I need to continually print districts, within states, that have
› information in the array/table.  What I have looks like this:
› My problem is that it will only print out one district within one state. 
› Any brilliant people out there to help?

You need to use a perform until/varying loop. To make it easier on
you, you might rewrite the code you showed us (I don't know what it
SHOULD accomplish, so don't quote me) to use the SEARCH verb (if this
is a class assignment, that may not be an option). Your-table = exact
thing with the occurs clause.

SET YOUR-INDEX TO 1.
SEARCH YOUR-TABLE
AT END DISPLAY 'NOT IN TABLE'
WHEN YOUR-TABLE (YOUR-INDEX) = 14
DISPLAY '14 is in the table'
END-SEARCH.

At end or when performed statements are generally only ONE statement,
so if multiple statements are required, you need to set them off in a
separate paragraph/section.

Glenn Grotzinger
Web Page: http://www.geocities.com/Paris/3537
Writer of the Excellent Training Manual known as the TP Tutorial.
To email, if you hit the reply button, delete the {remove_this}
out of the replied message. Just some protection from SPAM. :(
```

#### ↳ Re: Can anybody help a COBOL novice?

- **From:** "virtua..." <ua-author-649846@usenetarchives.gap>
- **Date:** 1997-01-18T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eaf04d993a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`
- **References:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`

```

1) first-no pic 9(9) value 200.
second-no pic 9(9) value 12000.
per-cent pic 999v99 value 0.

compute per-cent rounded = first-no / second-no.

2) you cant.
why is your pic 99? (heck its stored as pic 9(4) comp anyway?)
at end, you have 100, not 99. (which is really 0, same like the
year 2000). so change your district to pic 9(4) minimum.
besides good buddy,
unless you are trying to create a maintenance job for the future,
districts have been known to increase, and its bad form to limit
growth and increase maintenance fees!



› after district from 1 by 1 until = 99 (how would I print district 99?)  my
› pic is 99.
 
› "S. Saalfield"  wrote:
 
› I am currently trying to write what is probably a fairly simply program,
› but have run across two obstacles:
 
› 1) I need to compute and print a percentage (example 200/12000).  How would
› I do this with moving rules involving decimals?
› 2) I need to continually print districts, within states, that have
› information in the array/table.  What I have looks like this:
 
› Perform varying state from 1 by 1 until > 50
› after district from 1 by 1 until = 99 (how would I print district 99?)  my
› pic is 99.
 
›  IF T1-KIDS-PER-DISTRICT (IM-STATE-NUMBER,
›                                       IM-DISTRICT-NUMBER)> 0
…[20 more quoted lines elided]…
›           END-IF.
 
 
› My problem is that it will only print out one district within one state. 
› Any brilliant people out there to help?


*************************************************************************
Visit my webpage at (new address, please bookmark)
http://www.front.net/virtual.virgin/virtual.html-ssi
*************************************************************************
Link to EXPRESS TYPING SERVICES
http://www3.sympatico.ca/typing.shane/express.htm
*************************************************************************
```

#### ↳ Re: Can anybody help a COBOL novice?

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-01-19T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eaf04d993a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`
- **References:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`

```

In article <01bc058d$58b7cf20$4e0e35cf@saalfield>,
"S. Saalfield" wrote:
›
› 1) I need to compute and print a percentage (example 200/12000). How
› would I do this with moving rules involving decimals?

The most common way is something like this:

COMPUTE P-DL-PERCENT = 100 *
T1-TOTAL-IMMUNIZED (IM-STATE-NUMBER, IM-DISTRICT-NUMBER) /
T1-KIDS-PER-DISTRICT(IM-STATE-NUMBER, IM-DISTRICT-NUMBER)


› 2) I need to continually print districts, within states, that have
› information in the array/table. What I have looks like this:
›
› Perform varying state from 1 by 1 until > 50

Unfortunately, an inline PERFORM with an AFTER clause is not standard,
and your UNTIL clause is not standard either:

PERFORM procedure-name
VARYING IM-STATE-NUMBER FROM 1 BY 1
UNTIL IM-STATE-NUMBER > 50


› after district from 1 by 1 until = 99 (how would I print district 99?)

Same as you print state 50:

UNTIL IN-DISTRICT-NUMBER > 99


› pic is 99.

Always define subscripts computational, for example:

05 IM-STATE-NUMBER PIC S9(4) COMP.
05 IM-DISTRICT-NUMBER PIC S9(4) COMP.


› IF T1-KIDS-PER-DISTRICT(IM-STATE-NUMBER, IM-DISTRICT-NUMBER) > 0
› OR T1-TOTAL-IMMUNIZED (IM-STATE-NUMBER, IM-DISTRICT-NUMBER) > 0

This conditional expression is overspecified. Drop the second relation
condition. If it should happen that kids per district is not set but
total immunized is set, the second relation condition will cause a divide
by zero.


› [...]
› My problem is that it will only print out one district within one
› state.

Almost certainly the part of your program that loads the table has set
only one district within one state.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

#### ↳ Re: Can anybody help a COBOL novice?

- **From:** "7200..." <ua-author-7076740@usenetarchives.gap>
- **Date:** 1997-01-20T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-eaf04d993a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`
- **References:** `<01bc058d$58b7cf20$4e0e35cf@saalfield>`

```

Try this:

Make STATE and DISTRICT PIC 9(3) instead of PIC 9(2). If you're set on
printing a 2-digit DISTRICT, then lop off the high order zero. I.e. make
P-DL-DISTRICT PIC 9(2). You'll probably get a compiler warning but
that's not a problem. PERFORM VARYING STATE FROM 1 BY 1 UNTIL STATE
> 50 AFTER DISTRICT FROM 1 BY 1 UNTIL DISTRICT > 99
IF T1-KIDS-PER-DISTRICT (STATE, DISTRICT) > 0
OR T1-TOTAL-IMMUNIZED (STATE, DISTRICT) > 0
MOVE DISTRICT TO P-DL-DISTRICT
MOVE T1-KIDS-PER-DISTRICT (STATE, DISTRICT)
TO P-DL-TOTAL-NUMBER
MOVE T1-TOTAL-IMMUNIZED (STATE, DISTRICT)
TO P-DL-TOTAL-IMMUNIZED
COMPUTE W-PERCENT ROUNDED =
T1-TOTAL-IMMUNIZED (STATE, DISTRICT) /
T1-KIDS-PER-DISTRICT (STATE, DISTRICT)
END-COMPUTE
COMPUTE P-DL-PERCENT ROUNDED = W-PERCENT * 100
WRITE PRINT-RECORD FROM P-DETAIL-LINE1
AFTER ADVANCING 1 LINE
ADD 1 TO A-LINE-CT
END-IF
END-PERFORM.

Define W-PERCENT as PIC S99V9999 and P-DL-PERCENT as PIC ZZ9.9-, or
something similar depending on the range of possible values. Then
200/12000 would calculate to 00.0167 in W-PERCENT, and P-DL-PERCENT
would print as 1.7 percent. You could also combine the two COMPUTE
statements without any harm.

Hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
