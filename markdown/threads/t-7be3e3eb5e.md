[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Missing Output

_1 message · 1 participant · 1999-08_

---

### RE: Missing Output

- **From:** "Thompson, William" <wthompson@okc.disa.mil>
- **Date:** 1999-08-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90491CB93918D21189BD00805FBE300B015769D9@voyager.okc.disa.mil>`

```
When did this start, upon compiler/runtime change?
Did it ever print correctly?
FWIW, the header line on the compile listing will tell you what compiler is
currently in use...
By "getting no header lines, no continuation line, and no total line" do you
mean that the program is printing thme but they are not appearing on the
output?  Or the program is neven getting to the output statements at all?

Bill
wthompson at okc dot disa dot mil

-----Original Message-----
From: Eileen Preston [mailto:epreston@lear.com]
Sent: Wednesday, August 18, 1999 2:26 PM
To: comp.lang.cobol@list.deja.com
Subject: Missing Output


 Message from the Deja.com forum: 
 comp.lang.cobol
 Your subscription is set to individual email delivery

I have gone thru my entire list of 'dumb things programmers do to mess
up their programs' and cannot find the cause of this bug.  I have had
several people look at this and they can't find anything either.  What
makes this worse is this program worked just last week (I know, I know,
you've heard that before :)  ) Ok - here goes:

This is a COBOL/MVS program (we're running LE etc etc).  At one time is
was VS/Cobol then COBOL II, and now whatever version we're currently
running (compiler).  This program prints invoices.  The invoice is
output to 2 output files.  It consists of 17 header lines, 6 detail
lines per line item, a continuation line if more than one page, and a
total line on the last page.  All lines are defined in Working-Storage
as 01 levels.

What is happening is I'm getting no header lines, no continuation line,
and no total line.  I only get the 6 detail lines / line item.  Not
blank lines - NO lines on either file.

I have put displays into the program and yes there is data in the W/S
definitions and in the FD right after the WRITE statement was executed.

I have changed the program to do an explicit move of the W/S to the FD
and then perform a single WRITE statement (WRITE PRINT-REC AFTER 1) for
both the headers and the detail - I still get only the detail lines.

I can't see anything in the definition of the header lines or the ending
lines that would cause this but I'm leaning in that direction but don't
have a clue what to look for.  I will ask that if the name of the line
could have anything to do with the problem.  Headers are named HEADER-1
thru HEADER-17, the details are named DETAIL-1 thru DETAIL-6, and the
ending line used (depending on last page or not), are REFERENCE-LINE,
TOTAL-LINE, SHIPPER-LINE.

Anyone got any ideas?

Thanks all
Eileen


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.



 _____________________________________________________________
 Deja.com: Share what you know. Learn what you don't.
 http://www.deja.com/
 * To modify or remove your subscription, go to
 http://www.deja.com/edit_sub.xp?group=comp.lang.cobol
 * Read this thread at
 http://www.deja.com/thread/%3C7pf1bb%24e0n%241%40nnrp1.deja.com%3E


 Sent via Deja.com http://www.deja.com/
 Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
