[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help Needed displaying binary (COMP-3) numbers

_10 messages · 7 participants · 2002-03 → 2002-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### Help Needed displaying binary (COMP-3) numbers

- **From:** "Mark Miles" <milesfam@idirect.com>
- **Date:** 2002-03-18T19:18:46-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<u9d0vesaoho968@corp.supernews.com>`

```
I have a file and the first four bytes is a segment length (this is what it
looks like in hex 6CBF0000 00500000 00000000 00000000), 6CBF in hex is 27839
in decimal.  I have tried defining a PIC clause of 9999 BINARY and the value
displayed is 7839.  How do I correctly display the number?

Mark
```

#### ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** "Paul Raulerson" <praulerson@NOSPAM-hot.rr.com>
- **Date:** 2002-03-19T01:52:17+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<lRwl8.29470$Dv6.1023682@typhoon.austin.rr.com>`
- **References:** `<u9d0vesaoho968@corp.supernews.com>`

```
You don't say what machine this is on, but on a mainframe, this would wind
up being in a fullword.
Pic 9(4) is not large enough. So you need to do something like this:

In your FD, put in a

    05 FOUR-BYTE-BINARY-VALUE               PIC X(4).

Then down in Working-Storage, do something like:

    01 BINARY-VALUE                                      USAGE IS BINARY.

finally in the procedure division, do something like:

    MOVE FOUR-BYTE-BINARY-VALUE TO BINARY-VALUE
    DISPLAY BINARY-VALUE

You should get the correct answer. You might have to add a PIC s9(9) before
the usage is binary
clause to force a fullword, but I don't think so, and I unfortunately cannot
test this till tomorrow, at least
on a mainframe.

Yours,
-Paul


"Mark Miles" <milesfam@idirect.com> wrote in message
news:u9d0vesaoho968@corp.supernews.com...
> I have a file and the first four bytes is a segment length (this is what
it
> looks like in hex 6CBF0000 00500000 00000000 00000000), 6CBF in hex is
27839
> in decimal.  I have tried defining a PIC clause of 9999 BINARY and the
value
> displayed is 7839.  How do I correctly display the number?
>
> Mark
>
>
```

#### ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-03-19T03:45:35+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<zvyl8.15257$4I.1690408@bin4.nnrp.aus1.giganews.com>`
- **References:** `<u9d0vesaoho968@corp.supernews.com>`

```

"Mark Miles" <milesfam@idirect.com> wrote in message
news:u9d0vesaoho968@corp.supernews.com...
> I have a file and the first four bytes is a segment length (this is what
it
> looks like in hex 6CBF0000 00500000 00000000 00000000), 6CBF in hex is
27839
> in decimal.  I have tried defining a PIC clause of 9999 BINARY and the
value
> displayed is 7839.  How do I correctly display the number?
>
> Mark

For sure it's not COMP-3.

COBOL (generally) assigns storage depending on the PIC size and the format.

For binary numbers (BINARY or COMP-4):

PIC 9 to PIC 9999 COBOL assigns two bytes.
PIC 9(5) to PIC 9(9) COBOL assigns 4 bytes.

So, your job is now to get the first 2 bytes of your record to the
right-most two-bytes of a 4-byte field.  You want 6CBF to look like 00006CBF
(defined as PIC9(9) COMP-4). Note that if the field begins with "8" or more,
you're dealing with a negative number.

Here's one way:

01  MYRECORD.
   02  MY2BYTE-FIELD    PIC X(2). *>The 6CBF value

WORKING-STORAGE SECTION.


01  WORK-BYTES.
   02  WORK-BYTES-A   PIC X(2) VALUE LOW-VALUES.
   02  WORK-BYTES-B   PIC X(2).
01  FILLER REDEFINES WORK-BYTES.
   02  BIG-COMP    PIC 9(9) COMP-4.

MOVE MY2BYTE-FIELD TO WORK-BYTES-B.

*> At this point, WORK-BYTES (and BIG-COMP) contains: 00 00 6C BF.

DISPLAY BIG-COMP.
```

##### ↳ ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** jnjsle@aol.com (Jnjsle)
- **Date:** 2002-03-19T23:21:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020319182122.00701.00001815@mb-ft.aol.com>`
- **References:** `<zvyl8.15257$4I.1690408@bin4.nnrp.aus1.giganews.com>`

```
Hi Mark,

In a mainframe environment the key to the solution of your problem is the
compiler option TRUNC(BIN).
This could be put in a PROCESS card before the 1st COBOL stmt, e.g.:

PROCESS TRUNC(BIN)

Then the definition below:
 
01 YOUR-FLD PIC 9(004) USAGE BINARY. 

will accept a the maximum value allowable. One caveat though, if the
installation default is specified as other than BIN, you may have to use
Paul’s solution or a variation.

HTH, Jack.
```

###### ↳ ↳ ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** jnjsle@aol.com (Jnjsle)
- **Date:** 2002-03-20T06:29:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020320012902.13417.00001833@mb-fn.aol.com>`
- **References:** `<20020319182122.00701.00001815@mb-ft.aol.com>`

```
Sorry Mark,

I thought you wrote "2 bytes". The field s/b defined as follows for 4 bytes:

01 YOUR-FLD PIC 9(009)  BINARY.
```

##### ↳ ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** "Mark Miles" <milesfam@idirect.com>
- **Date:** 2002-03-19T19:32:09-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<u9fm4e2216r60a@corp.supernews.com>`
- **References:** `<u9d0vesaoho968@corp.supernews.com> <zvyl8.15257$4I.1690408@bin4.nnrp.aus1.giganews.com>`

```
Thanks

I'll give it a go.

Mark

"JerryMouse" <nospam@invalid.com> wrote in message
news:zvyl8.15257$4I.1690408@bin4.nnrp.aus1.giganews.com...
>
> "Mark Miles" <milesfam@idirect.com> wrote in message
…[13 more quoted lines elided]…
> COBOL (generally) assigns storage depending on the PIC size and the
format.
>
> For binary numbers (BINARY or COMP-4):
…[5 more quoted lines elided]…
> right-most two-bytes of a 4-byte field.  You want 6CBF to look like
00006CBF
> (defined as PIC9(9) COMP-4). Note that if the field begins with "8" or
more,
> you're dealing with a negative number.
>
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** "Last Boy Scout" <Crazy-Joe@whitehouse.gov>
- **Date:** 2002-05-03T23:55:46-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aavpil02ub1@enews2.newsguy.com>`
- **References:** `<u9d0vesaoho968@corp.supernews.com> <zvyl8.15257$4I.1690408@bin4.nnrp.aus1.giganews.com> <u9fm4e2216r60a@corp.supernews.com>`

```
Maybe it is a signed comp-3 number.

Mark Miles <milesfam@idirect.com> wrote in message
news:u9fm4e2216r60a@corp.supernews.com...
> Thanks
>
…[9 more quoted lines elided]…
> > > I have a file and the first four bytes is a segment length (this is
what
> > it
> > > looks like in hex 6CBF0000 00500000 00000000 00000000), 6CBF in hex is
…[47 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** "Mark Miles" <milesfam@idirect.com>
- **Date:** 2002-03-19T20:37:10-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<u9fpub39hit534@corp.supernews.com>`
- **References:** `<u9d0vesaoho968@corp.supernews.com> <zvyl8.15257$4I.1690408@bin4.nnrp.aus1.giganews.com>`

```
Tried it and thanks it works fine.

I haven't programmed Cobol for 13 years when I switched to Basic then VB but
it's fun relearning Cobol and I'm finding it a lot faster than VB could ever
be.

Mark

"JerryMouse" <nospam@invalid.com> wrote in message
news:zvyl8.15257$4I.1690408@bin4.nnrp.aus1.giganews.com...
>
> "Mark Miles" <milesfam@idirect.com> wrote in message
…[13 more quoted lines elided]…
> COBOL (generally) assigns storage depending on the PIC size and the
format.
>
> For binary numbers (BINARY or COMP-4):
…[5 more quoted lines elided]…
> right-most two-bytes of a 4-byte field.  You want 6CBF to look like
00006CBF
> (defined as PIC9(9) COMP-4). Note that if the field begins with "8" or
more,
> you're dealing with a negative number.
>
…[21 more quoted lines elided]…
>
```

#### ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-03-19T22:34:54-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8a2d426e.0203192234.38919548@posting.google.com>`
- **References:** `<u9d0vesaoho968@corp.supernews.com>`

```
Hi Mark,

In a mainframe environment the key to the solution of your problem is the
compiler option TRUNC(BIN).
This could be put in a PROCESS card before the 1st COBOL stmt, e.g.:

PROCESS TRUNC(BIN)

Then the definition below:
 
01 YOUR-FLD PIC 9(009) BINARY. 

will accept a the maximum value allowable. One caveat though, if the
installation default is specified as other than BIN, you may have to use
Paul's solution or a variation.

HTH, Jack.





"Mark Miles" <milesfam@idirect.com> wrote in message news:<u9d0vesaoho968@corp.supernews.com>...
> I have a file and the first four bytes is a segment length (this is what it
> looks like in hex 6CBF0000 00500000 00000000 00000000), 6CBF in hex is 27839
…[3 more quoted lines elided]…
> Mark
```

#### ↳ Re: Help Needed displaying binary (COMP-3) numbers

- **From:** Jim Reinhart <jreinhart1@cox.net>
- **Date:** 2002-03-21T02:05:36+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<B8BE8EFF.143F%jreinhart1@cox.net>`
- **References:** `<u9d0vesaoho968@corp.supernews.com>`

```
in article u9d0vesaoho968@corp.supernews.com, Mark Miles at
milesfam@idirect.com wrote on 3/18/02 5:18 PM:

> I have a file and the first four bytes is a segment length (this is what it
> looks like in hex 6CBF0000 00500000 00000000 00000000), 6CBF in hex is 27839
…[5 more quoted lines elided]…
> 
The problem you are having is that using BINARY items, 9999 BINARY is a half
word (i.e. 2 BYTES), Truncating the first 2 bytes.

For binary use this as a reference
Half Word = 2 Bytes uses PIC 9(4) BINARY or less.
Full Word = 4 Bytes uses PIC 9(5) through 9(9) BINARY.
Double Word = 8 Bytes uses PIC 9(10) through 9(18) BINARY.

For your purposes, use at least PIC 9(5) BINARY or 99999 BINARY.  Don't go
higher than 9(9) BINARY.

Good COBOL programming uses only PIC 9(9) BINARY for full word definitions.

To display just move the variable to a display variable.

COMP = BINARY
COMP-3 = PACKED DECIMAL

Don't use a COMP-3.

Regards,

Jim Reinhart
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
