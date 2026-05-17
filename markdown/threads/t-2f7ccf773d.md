[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help !! Numeric field in COBOL

_8 messages · 8 participants · 1997-07 → 1997-08_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help !! Numeric field in COBOL

- **From:** "su..." <ua-author-17072564@usenetarchives.gap>
- **Date:** 1997-07-29T20:24:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<870222262.31667@dejanews.com>`

```

Hi,

i need immediate help regarding handling of numeric field in COBOL85
on
HP 3000 platform.

I have a field like 9(12)V9(6). I want to check if the field is
numeric or if it has any alphanumeric character. Is there a function
call
i can use to do a quick check ?

I am reading a field from input file as 9(12)V9(6). I am then putting
this field in the database (ingres). Before putting in Ingres database
i want to perform a check to make sure that the field is NUMERIC.

Please let me know if there is a function which can be used. If not,
do
you have a code which does this check ? THanks, Sunil

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: Help !! Numeric field in COBOL

- **From:** "bruce d. sinclair" <ua-author-14902526@usenetarchives.gap>
- **Date:** 1997-07-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f7ccf773d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<870222262.31667@dejanews.com>`
- **References:** `<870222262.31667@dejanews.com>`

```

If it's a DISPLAY usage data item, COBOL has the NUMERIC class
test for determining if the item is a valid numeric data item. For
example,
if the data item's data-name is VALUE01, then

IF VALUE01 IS NUMERIC
{put in database}
ELSE
{display error message}
END-IF

verifies that VALUE01 contains only valid digits. If the data item were
signed, the NUMERIC class test also validates that the item has a
valid sign in the correct position (leading or trailing, combined or
separate).
Some COBOL implementations extend the NUMERIC class test to work
for PACKED-DECIMAL (aka COMP-3) usage data items. If the data item
is BINARY (aka COMP or COMP-4) usage, then there is no way to validate
the item (other than it conforms to the PICTURE restrictions), so few,
if any, implementations allow a NUMERIC class test on such items.

--Bruce Sinclair, Liant Software Corporation

su··.@aq··s.com wrote in article <870··.@dej··s.com>...
› Hi,
› 
…[19 more quoted lines elided]…
›
```

#### ↳ Re: Help !! Numeric field in COBOL

- **From:** "william lynch" <ua-author-97506@usenetarchives.gap>
- **Date:** 1997-07-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f7ccf773d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<870222262.31667@dejanews.com>`
- **References:** `<870222262.31667@dejanews.com>`

```

If the field is WS-DOLLAR-AMOUNT, you can code:

IF WS-DOLLAR-AMOUNT NUMERIC ...

or

IF WS-DOLLAR-AMOUNT NOT NUMERIC ...

It's a good edit check for any numeric field from outside your system.

Bill Lynch
```

#### ↳ Re: Help !! Numeric field in COBOL

- **From:** "bill herron" <ua-author-2540427@usenetarchives.gap>
- **Date:** 1997-07-29T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f7ccf773d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<870222262.31667@dejanews.com>`
- **References:** `<870222262.31667@dejanews.com>`

```

› i need immediate help regarding handling of numeric field in COBOL85 on
› HP 3000 platform.
 
› This problem is general to all COBOL situations.
 
› I have a field like 9(12)V9(6). I want to check if the field is numeric
› or if it has any
› alphanumeric character. Is there a function call i can use to do a quick
check ?

How about using the IS NUMERIC condition on the field:

01 WS-FIELD PIC 9(12)V9(6).

IF WS-FIELD IS NUMERIC
THEN
save to database.

If that doesn't work, you can try a less elegant approach:

01 WS-FIELD PIC 9(12)V9(6).
01 WS-FIELD-CHAR REDEFINES WS-FIELD
PIC 9(01)
OCCURS 18 TIMES.

Then use a loop to see if each WS-FIELD-CHAR is greater than 0 or less than
9. The problem here is that you may get an error if an alphabetic is in
one of these positions.

So use

01 WS-FIELD-CHAR REDEFINES WS-FIELD
PIC X(01)
OCCURS 18 TIMES.

Then check to see if each WS-FIELD-CHAR is greater than '0' and less than
'9'.

There may be other solutions to this (and I'm sure my fellow posters will
have them). This should get you on the right track, though.

Bill


-------------==== Posted via Sexzilla News ====------------------
http://www.sexzilla.com Search, Read, Post to Usenet
-------------==== With A Whole Lot More ====------------------
```

##### ↳ ↳ Re: Help !! Numeric field in COBOL

- **From:** "sabine rother-scholz" <ua-author-17073500@usenetarchives.gap>
- **Date:** 1997-07-29T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f7ccf773d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f7ccf773d-p4@usenetarchives.gap>`
- **References:** `<870222262.31667@dejanews.com> <gap-2f7ccf773d-p4@usenetarchives.gap>`

```

Bill Herron wrote:
› 
›› i need immediate help regarding handling of numeric field in COBOL85 on
…[16 more quoted lines elided]…
› 

(snip)

How about

01 WS-FIELD-X.
05 WS-FIELD PIC 9(12)V9(6).

IF WS-FIELD-X IS NUMERIC ....

Testing a numeric-defined field could be a problem. But group-fields are
always handled as alpha-numeric.

Greetings
Sabine
```

#### ↳ Re: Help !! Numeric field in COBOL

- **From:** "lefew" <ua-author-6590554@usenetarchives.gap>
- **Date:** 1997-07-29T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f7ccf773d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<870222262.31667@dejanews.com>`
- **References:** `<870222262.31667@dejanews.com>`

```

It sounds as if you are answering your own question. Redefine your field
as alphanumeric (some compilers will allow a 'type' trap if the data is
alphanumeric) and simply ask "if field numeric...else...!
```

#### ↳ Re: Help !! Numeric field in COBOL

- **From:** "fred..." <ua-author-28008@usenetarchives.gap>
- **Date:** 1997-07-30T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f7ccf773d-p7@usenetarchives.gap>`
- **In-Reply-To:** `<870222262.31667@dejanews.com>`
- **References:** `<870222262.31667@dejanews.com>`

```

use the expression IS NUMERIC.
example: IF FIELD-NAME IS NUMERIC
MOVE FIELD-NAME TO DATA-BASE.

However, unless the field is in an input record, it should always have a
numeric value, even if it's all zeroes.
```

##### ↳ ↳ Re: Help !! Numeric field in COBOL

- **From:** ""roland schiradin" Roland Schiradin" <ua-author-17071524@usenetarchives.gap>
- **Date:** 1997-08-06T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2f7ccf773d-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2f7ccf773d-p7@usenetarchives.gap>`
- **References:** `<870222262.31667@dejanews.com> <gap-2f7ccf773d-p7@usenetarchives.gap>`

```

FREDPIERZ wrote:

› use the expression IS NUMERIC.
› example:  IF FIELD-NAME IS NUMERIC
…[3 more quoted lines elided]…
› numeric value, even if it's all zeroes.

Sorry but all zeros is numeric!

roland**2
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
