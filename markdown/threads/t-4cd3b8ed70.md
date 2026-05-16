[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# redefines is giving me hard times newbie help

_2 messages · 2 participants · 2001-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Tutorials, books, learning`](../topics.md#learning)

---

### redefines is giving me hard times newbie help

- **From:** "MadG" <patrick4133@hotmail.com>
- **Date:** 2001-02-18T17:28:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QCTj6.174637$KP3.44143582@news3.rdc1.on.home.com>`

```
and a headache!

 I have in my detail-line a REDEFINES statement that redefines a
group.
 The program ignores the redefined part because I
don't know how to code it.  It looks like this:

01 DETAIL-LINE.
   05 DL-EMP-ID   PIC X(5).
   05 DL-PAY-DETAILS.
       10 DL-HOURLY-RATE  PIC ZZ.99.
   05 DL-PAY-DETAILS-ALT REDEFINES DL-PAY-DETAILS.
       10 DL-DAILY-RATE  PIC ZZ.99.

   My move and print statements:

MOVE DETAIL-LINE TO PRINT-DETAIL-LINE
WRITE PRINT-DETAIL-LINE

   So it ignores the DL-DAILY-RATE all together.  It puts
in whatever was in the buffer from the last read.

Thanks in advance!

AND a SPECIAL Thank-you to Kevin and Jeff.

I was a total klutz!  I have an identifier field, but my head
was up my ...
```

#### ↳ Re: redefines is giving me hard times newbie help

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-18T12:37:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96p4pb$thq$1@slb4.atl.mindspring.net>`
- **References:** `<QCTj6.174637$KP3.44143582@news3.rdc1.on.home.com>`

```
Do you understand that REDEFINES means that you have only ONE copy of the
indicated storage?  This means that DL-HOURLY-RATE and DL-DAILY-RATE  point
to the same 5 bytes of storage?  If you understand that, the next question
is HOW to you get data into the two fields?

If your code looks something like,

  Move send-field to DL-DAILY-RATE
  Move other-field to DL-HOURLY-RATE
  MOVE DETAIL-LINE TO PRINT-DETAIL-LINE
  WRITE PRINT-DETAIL-LINE

Then it is always true that you will only see DL-HOURLY-RATE in your
output - because that is the last thing that you put into those 5 byes of
storage.  If on the other hand, your code looks like:

  Move send-field to DL-DAILY-RATE
  MOVE DETAIL-LINE TO PRINT-DETAIL-LINE
  WRITE PRINT-DETAIL-LINE
  Move other-field to DL-HOURLY-RATE
  MOVE DETAIL-LINE TO PRINT-DETAIL-LINE
  WRITE PRINT-DETAIL-LINE

then you should see alternating lines of daily-rate and hourly-rate.

Finally, if you want to see BOTH daily and hourly rates in the same
print-line, then they must not redefine each other.

Does this help?  If not, show us how you "populate" your print-detail-lines
and we might be able to help more/better.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
