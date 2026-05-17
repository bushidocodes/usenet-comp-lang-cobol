[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable Length records

_6 messages · 5 participants · 1997-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Variable Length records

- **From:** "steven hughes" <ua-author-794783@usenetarchives.gap>
- **Date:** 1997-04-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33454C8B.197F@netcomuk.co.uk>`

```

Hi,
What's the best way to write out a lot of differing length records?

I've usually had to deal with up to maybe half a dozen different
lengths so I defined six 01 levels in the FD.

I now have the following structure in W-S.

01 WS-Variable-Record.
03 Key-Part-1 PIC X(08).
03 Key-Part-2 PIC X(08).
03 Key-Part-3 PIC X(10).
03 Occurs-Number PIC S9(04) COMP-4.
03 Data-Part Occurs 1 To 70 Times Depending On Occurs-Number
PIC X(133).

This means up to 70 different length records and 70 write statements.
I'm not writing the program, just trying to help out a junior
programmer.

My understanding is the record length is not available to COBOL.

Any and all responses appreciated; unfortunately it's not my design.

Thanks in advance,
Steven.
```

#### ↳ Re: Variable Length records

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-04-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-474b1ab4ed-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33454C8B.197F@netcomuk.co.uk>`
- **References:** `<33454C8B.197F@netcomuk.co.uk>`

```

Steve, make your 01 level in working storage, the O1 level in the data
description of your FD for the file. COBOL handles variable length records
like this automatically. Unless I am dense this afternoon (Quite possible)
I don't see what the problem is.

Steven Hughes wrote in article
<334··.@net··o.uk>...
› Hi,
›    What's the best way to write out a lot of differing length records?
…[25 more quoted lines elided]…
›
```

#### ↳ Re: Variable Length records

- **From:** "alan russell" <ua-author-1025782@usenetarchives.gap>
- **Date:** 1997-04-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-474b1ab4ed-p3@usenetarchives.gap>`
- **In-Reply-To:** `<33454C8B.197F@netcomuk.co.uk>`
- **References:** `<33454C8B.197F@netcomuk.co.uk>`

```

You can simply move that record definition into the FILE SECTION, and COBOL
will recognize the definition as being a variable length record and write
the appropriate size based on the 'DEPENDING ON' variable. It's that easy
:)
```

#### ↳ Re: Variable Length records

- **From:** "wbbla..." <ua-author-17071433@usenetarchives.gap>
- **Date:** 1997-04-04T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-474b1ab4ed-p4@usenetarchives.gap>`
- **In-Reply-To:** `<33454C8B.197F@netcomuk.co.uk>`
- **References:** `<33454C8B.197F@netcomuk.co.uk>`

```

On Fri, 04 Apr 1997 19:46:35 +0100, Steven Hughes
wrote:

› Hi,
›   What's the best way to write out a lot of differing length records?
…[21 more quoted lines elided]…
› 

Steven, I agree with the other respondents ... COBOL should be able to
handle this, although there are a few caveats if you're running this
in an IBM mainframe environment.

If you do a group move to the output record (e.g., WRITE ... FROM),
be sure to move the counter field value first, as the MOVE statement
will figure the length of the receiving field from the value of the
occurs count, before the MOVE. If you forget this, and the occurs
count in the record area is less than the occurs count in the sending
area, the group moved will be truncated.

Also, I'd recommend that you use "RECORD CONTAINS 0 CHARACTERS"
in your FD.



Regards,
Bill

------------------------ Address Notice ------------------------
Since there are automated programs which mine Usenet posts
for e-mail addresses for junk mail, I have a dummy address
given in the "From:" message field. My actual address is
given in the "Reply-to:" field - if you reply to any message
I send, it will be addressed correctly, to wbb··.@po··x.com
-----------------------------------------------------------------
```

##### ↳ ↳ Re: Variable Length records

- **From:** "steven hughes" <ua-author-794783@usenetarchives.gap>
- **Date:** 1997-04-04T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-474b1ab4ed-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-474b1ab4ed-p4@usenetarchives.gap>`
- **References:** `<33454C8B.197F@netcomuk.co.uk> <gap-474b1ab4ed-p4@usenetarchives.gap>`

```

Thanks for all replies but the problem is the bloody inflexible
standards clowns I have to put up with!

The FD *must* be:

FD file-name
RECORD IS VARYING FROM 167 TO 9344.

01 short-record PIC X(167).
01 long-record PIC X(9344).

The definition must be in W-S; its a copybook!

I'm not allowed to write the program, a junior programmer must do
that.

I can write pseudo-code that say "WRITE RECORD", but, as the
definition is in W-S, a maximum length record is going to be written.
Am I right? Is the standards twit a twit?

Regards,
Steven.

William B. Blakemore wrote:
› 
› On Fri, 04 Apr 1997 19:46:35 +0100, Steven Hughes
…[50 more quoted lines elided]…
› -----------------------------------------------------------------
```

#### ↳ Re: Variable Length records

- **From:** "rsi..." <ua-author-17071488@usenetarchives.gap>
- **Date:** 1997-04-05T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-474b1ab4ed-p6@usenetarchives.gap>`
- **In-Reply-To:** `<33454C8B.197F@netcomuk.co.uk>`
- **References:** `<33454C8B.197F@netcomuk.co.uk>`

```

On Fri, 04 Apr 1997 19:46:35 +0100, Steven Hughes
wrote:

› Hi,
›   What's the best way to write out a lot of differing length records?
…[24 more quoted lines elided]…
› 


The variable record length is part of ANSI COBOL.

You must define the file with the correct FD sintax:

FD file-name
RECORDS CONTAINS XXX TO YYY CHARACTERS DEPENDING ON
LENGTH-COUNTER.
01 VARIABLE-RECORD PIC X(ZZZZ).

(where XXX is the minimum record lenght and YYY is the maximum record
lenght; LENGTH-COUNTER (or another name you prefer..) is a
WORKING-STORAGE numeric field like this:
01 LENGTH-COUNTER PIC 9(004).
ZZZZ is the MAXIMUM record length.

When you write a record BEFORE the WRITE statement you MUST move the
lenght of your record in LENGTH-COUNTER for example:

COMPUTE LENGTH-COUNTER = 28 + (OCCURS-NUMBER * 133).
MOVE WS-VARIABLE-RECORD TO VARIABLE-RECORD.
WRITE VARIABLE-RECORD.

If you read the file, the update of LENGTH-COUNTER is done in
automatic by system.

bye ROBERTO SILVA
email: rsi··.@stu··s.it

Sorry for my bad english ...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
