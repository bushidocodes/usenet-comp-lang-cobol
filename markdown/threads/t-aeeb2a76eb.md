[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Novice: All about COMP-3 fields

_14 messages · 12 participants · 2004-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Novice: All about COMP-3 fields

- **From:** mkbobba@yahoo.com (Bob)
- **Date:** 2004-01-09T03:51:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64713ce9.0401090351.6dd85003@posting.google.com>`

```
Hi,

We have MF cobol running on Sun Solaris server. Our's is a
Datawarehouse setup. We get EBCDIC files from mainframe. We transform
those files and load them in to a SYBASE datawarehouse. We use COBOL
to transform and Shell scripts to load the data.

My today's first question is concerning some input fields defined as

01 INPUT-FIELD3  PIC S9(03) COMP-3.

What is a comp-3 definition?. Some cobol books gave me an idea that
this type of definitions are for space saving.
Does that mean this field will not occupy 4 character spaces in memory
and less. If this is correct, how much space they will occupy?

Can somebody point to some documentation where I can learn all about
COMP-3 fields?.

Second question:

Scenario

We are moving a PIC S9(03) COMP-3. field to a PIC X(03).

If the value in the input field is '100' will it be moved as '10 ' or
'100' in the receiving field?.

One of the senior developers in our shop says that it will be received
as '10 ' with a space in the 3rd position.

Can somebody clarify this and give me some examples of move?.

I can post the piece of code if somebody wants to look further and
help me.

Thank you,

Murali
```

#### ↳ Re: Novice: All about COMP-3 fields

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-01-09T07:37:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rsydnZLh5qQ-M2Oi4p2dnA@giganews.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com>`

```
Bob wrote:
> Hi,
>
…[12 more quoted lines elided]…
> and less. If this is correct, how much space they will occupy?

Correct. COMP-3 fields occupy from 1 to 10 bytes.

>
> Can somebody point to some documentation where I can learn all about
> COMP-3 fields?.

You really don't need any. See below.

>
> Second question:
…[3 more quoted lines elided]…
> We are moving a PIC S9(03) COMP-3. field to a PIC X(03).

No known compiler will let you do that (or at least it shouldn't).

>
> If the value in the input field is '100' will it be moved as '10 ' or
> '100' in the receiving field?.

The move you've described above is not allowed or, at the least, will
generated a truncated value (plus, where does the sign go or how is it
represented in the "X(3)" destination. You should move the C-3 field to a
numeric display field first.

>
> One of the senior developers in our shop says that it will be received
> as '10 ' with a space in the 3rd position.
>
> Can somebody clarify this and give me some examples of move?.

COMP-3 is both a space-saver and optimizer. Space saving is obvious, but
many computers have base-10 logic boards which process C-3 fields directly.

C-3 fields look like this (each character is a half-byte or nibble)

NN NN NN ... NS

where "N" is a digit (note: a DIGIT, 1-9). The "..." means as many bytes as
necessary to satisfy the length definition of the field. "S" is the
algebraic sign of the field: F,A,C,E are all considered positive; B,D imply
negative.

So, then, examples, decimal to C-3 (bytes of storage needed):
1 = 1F (1)
10 = 01 0F (2)
100 = 10 0F (2)
1000 = 01 00 0F (3)
-1 = 1D (1)
-1234 = 01 23 4D (3)
-12.34 = 01 23 4D (3) [decimal positioning is defined by the data defintion
and is not carried with the data]

In your example, PIC 9(3) COMP-3, occupies 2 bytes of memory and can contain
99 9D through 99 9F (-999 thru 999+).

You can move a C-3 field to a numeric display field:

MOVE [C-3] TO [S9(3)],

but don't move a C-3 field to an "X" field.

I'm sure someone will post a link to a grand exposition of COMP-3 fields; I
just don't happen to know one off-hand (although I suspect Google is your
friend).
```

##### ↳ ↳ Re: Novice: All about COMP-3 fields

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-01-09T13:46:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mhyLb.23554$P%1.22048348@newssvr28.news.prodigy.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com> <rsydnZLh5qQ-M2Oi4p2dnA@giganews.com>`

```
> Bob wrote:
> > Hi,
…[4 more quoted lines elided]…
> > to transform and Shell scripts to load the data.


Converting cobol-created data for use with other systems...

http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm
```

#### ↳ Re: Novice: All about COMP-3 fields

- **From:** "Simon Tobias" <Simon.Tobias@nospam.MicroFocus.com>
- **Date:** 2004-01-09T14:48:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<btmgm5$8d2$1@hyperion.microfocus.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com>`

```
You can access the Micro Focus documentation from
http://supportline.microfocus.com/. Click on Self-Service in the left-hand
pane, and then Documentation. You should find the Server Express
documentation there.

The Language Reference Manual, section 2.6.4.4 details how COMP-3 items are
represented.

Hope this helps.

Simon.
```

#### ↳ Re: Novice: All about COMP-3 fields

- **From:** nagiscool@yahoo.co.in (Nagaraj Reddy)
- **Date:** 2004-01-09T12:21:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f078b180.0401091221.7c00b9ec@posting.google.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com>`

```
mkbobba@yahoo.com (Bob) wrote in message news:<64713ce9.0401090351.6dd85003@posting.google.com>...
> Hi,
> 
…[13 more quoted lines elided]…
> 
This field will not occupy 4 character spaces instead it saves the
data in Hexa Decimal in 2 bytes. Sign uses 1/2 byte and 3 digits are
stored in 1 1/2 bytes.
It is stored in Hexa Decimal to make faster computing and save space.

> Can somebody point to some documentation where I can learn all about
> COMP-3 fields?.
> 

I cannot correctly point out to documentation but I can confidently
say it.
If you need verification you can refer to IBM COBOL lang reference
manuals.

> Second question:
> 
…[11 more quoted lines elided]…
>

After making the above move the results cannot be predicted easily
because comp-3 fields are stored in HEX for pure calculating purposes
whereas the other data item with PIC X(03) is purely for display.
If you still need it's internal storege here it is:
In comp-3 field value '+100' will be stored as C1 00
In display i.e with PIC X(03) value '100' will be internally stored as
F1 F0 F0

My suggetion to get the desired results would be to declare another
data item with PIC 9(03) and then use COMPUTE statement to transfer
the value.
for example.

77 A PIC S9(03) COMP-3.
77 B PIC S9(03).
..............

COMPUTE B=A.

If you use MOVE statment then you cannot get the expected results for
sure b'coz it just transfers the internal storage values from one data
item to other. In this case since internal storage is different it is
always better and preferred to use COMPUTE statement.

If you still need the value to transferred to the dataitem with PIC
x(03) , then you can only move the contents from data item with PIC
9(03).
You cannot direwctly move from comp-3 field. you should definitely use
the intermediate field like B PIC s9(03).

 
  
> I can post the piece of code if somebody wants to look further and
> help me.
…[3 more quoted lines elided]…
> Murali
```

##### ↳ ↳ Re: Novice: All about COMP-3 fields

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-01-09T16:52:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6c-dnWgU3tszrWKiRVn-jw@giganews.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com> <f078b180.0401091221.7c00b9ec@posting.google.com>`

```
Nagaraj Reddy wrote:


I hope you will permit a few corrections.

>>
> This field will not occupy 4 character spaces instead it saves the
> data in Hexa Decimal in 2 bytes. Sign uses 1/2 byte and 3 digits are
> stored in 1 1/2 bytes.
> It is stored in Hexa Decimal to make faster computing and save space.

No. There is no hexadecimal notation involved in COMP-3 data.

>> Second question:
>>
…[15 more quoted lines elided]…
> In comp-3 field value '+100' will be stored as C1 00

Not on any machine I've ever seen. 00 1C on IBM. Maybe C1 00 on some Intel
representations.

> In display i.e with PIC X(03) value '100' will be internally stored as
> F1 F0 F0

On EBCDIC. Different for ASCII.

>
> My suggetion to get the desired results would be to declare another
…[13 more quoted lines elided]…
> always better and preferred to use COMPUTE statement.

No. The compiler will generate the necessary conversions when you use MOVE A
TO B.

ADD, COMPUTE, and (where permissable) MOVE generate identical results. You
can take that to the bank.
```

###### ↳ ↳ ↳ Re: Novice: All about COMP-3 fields

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2004-01-10T02:32:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fvJLb.131905$JW3.24790@twister.nyroc.rr.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com> <f078b180.0401091221.7c00b9ec@posting.google.com> <6c-dnWgU3tszrWKiRVn-jw@giganews.com>`

```
snip
> > If you still need it's internal storege here it is:
> > In comp-3 field value '+100' will be stored as C1 00
…[3 more quoted lines elided]…
>
Are you sure it's not 100C on IBM?
```

#### ↳ Re: Novice: All about COMP-3 fields

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-01-10T01:19:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XqILb.977$1e.543@newsread2.news.pas.earthlink.net>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com>`

```
"Bob" <mkbobba@yahoo.com> wrote in message
news:64713ce9.0401090351.6dd85003@posting.google.com...
<snip>
> Scenario
>
> We are moving a PIC S9(03) COMP-3. field to a PIC X(03).
>
<snip>

Can you tell us what you WANT to happen?  If the "sending" field has the value
of "-123" (regardless of how it is stored), exactly what do you WANT to be in
the "3 byte" receiving field?

My *guess* is that you want to have an application that stores the value "-123"
or possibly "123-" in a 4 (not 3) byte receiving field.  If this is the case,
then what you want to do is something like (and there are a number of ways to do
this).

01  Sending-Comp-3   Pic S9(3)  Comp-3.
01  4-byte-alphanumeric.
     05   Display-Numeric   Pic +9(3).
   ...
Move Sending-Comp-3  to Display-Numeric

display "4 byte field:" 4-byte-alphanumeric
```

##### ↳ ↳ Re: Novice: All about COMP-3 fields

- **From:** mkbobba@yahoo.com (Bob)
- **Date:** 2004-01-15T07:26:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64713ce9.0401150726.38690c9c@posting.google.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com> <XqILb.977$1e.543@newsread2.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<XqILb.977$1e.543@newsread2.news.pas.earthlink.net>...
> "Bob" <mkbobba@yahoo.com> wrote in message
> news:64713ce9.0401090351.6dd85003@posting.google.com...
…[22 more quoted lines elided]…
> display "4 byte field:" 4-byte-alphanumeric



Sending field is an input record of
the County Code numbers storing numbers 1 to 100.
           05  CNG-COUNTY                       PIC S9(03) COMP-3.
Receving field is 

01  WS-LOOKUP-SEARCH-CR-CTY-NUM   PIC X(03) VALUE SPACES

       01  COUNTY-REGION-TABLE.
           05  CR-TABLE OCCURS 500 TIMES
               INDEXED BY CR-IDX
               ASCENDING KEY CR-COUNTY-NUMBER.
               10  CR-COUNTY-NUMBER         PIC X(03).
               10  CR-COUNTY-NAME           PIC X(30).
               10  CR-REGION-FOR-COUNTY     PIC X(01).
               10  CR-TERRITORY-FOR-COUNTY  PIC X(01).
               10  CR-FEDERAL-FIPS-CODE     PIC 9(03).
               10  CR-TIMESTAMP-OF-LAST-CHG PIC X(26).
               10  CR-USER-WHO-CHANGED-BY   PIC X(08).

       01  WS-CR-MAX                        PIC 9(04) COMP-5 VALUE 500.
       01  WS-LOOKUP-SEARCH-CR-CTY-NUM      PIC X(03) VALUE SPACES.
       01  WS-FOUND-CR-COUNTY-NUMBER        PIC X(01) VALUE SPACES.

Moving this input field into the receiving field and
performing binary search.

           IF  CNG-COUNTY                    OF WFINPUT-REC
               NUMERIC
->             MOVE CNG-COUNTY               OF WFINPUT-REC
                   TO WS-LOOKUP-SEARCH-CR-CTY-NUM
               PERFORM S610-000-COUNTY-BINARY-SEARCH
               IF  WS-FOUND-CR-COUNTY-NUMBER = 'N'
                   ADD +1                   TO
                       FIELD-BAD            OF FILE-I(FILE-NO FLD-NO)
                   SET FLD-NO               TO
                       I-FIPS-COUNTY-CODE   OF SSFAC100-INFO
                   ADD +1                   TO
                       FIELD-BAD            OF FILE-I(FILE-NO FLD-NO)
               ELSE  

So far as per the posts I have read, this search should not work
and strangely it is working. We wonder how it is working.

For ex: It should work only if 34 stored in the COMP-3 field
is received as 34 by the receiving field and matched.


Thanks.

Bob
```

###### ↳ ↳ ↳ Re: Novice: All about COMP-3 fields

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2004-01-15T11:32:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0401151132.245c0b6a@posting.google.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com> <XqILb.977$1e.543@newsread2.news.pas.earthlink.net> <64713ce9.0401150726.38690c9c@posting.google.com>`

```
you really have to give us more to go on, for example what is the code
for the S610 procedure and some more of the code surrounding the
snippet you have given us.  It is possible that the search never
executed and just returned a previous value, but you don't show us
enough code to know what could have happened.

Robert 
> 
> 
…[49 more quoted lines elided]…
> Bob
```

###### ↳ ↳ ↳ Re: Novice: All about COMP-3 fields

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2004-01-17T18:25:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0401171825.76bb32b6@posting.google.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com> <XqILb.977$1e.543@newsread2.news.pas.earthlink.net> <64713ce9.0401150726.38690c9c@posting.google.com>`

```
Hi Bob,

According to my COBOL II manual (admittedly somewhat dated) numeric
INTEGER moves to A/N fields is permitted. Non-integer moves are not.

If the sending field is signed (as in your ex.) an unsigned value is
used in the MOVE. Since you expect values 1 thru 100 this presents no
problem.

In addition, the max value possible in the COMP-3 field is 999;
therefore a 3 byte receiving field [pic X(03)] is sufficient for your
needs and no spaces will be inserted into the receiving field. I'd
restate your ex. as follows: "It should work only if 034 stored in the
COMP-3 field is received as 034 by the receiving field and matched."
It will be.

The code you posted should (and does) work fine. I'm curious though
about how the search is conducted.

Regards, Jack.




mkbobba@yahoo.com (Bob) wrote in message news:<64713ce9.0401150726.38690c9c@posting.google.com>...
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<XqILb.977$1e.543@newsread2.news.pas.earthlink.net>...
> > "Bob" <mkbobba@yahoo.com> wrote in message
…[76 more quoted lines elided]…
> Bob
```

#### ↳ Re: Novice: All about COMP-3 fields

- **From:** "Easton Beymer" <eastonbeymer@hotmail.com>
- **Date:** 2004-01-11T02:12:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kk9Mb.50785$gN.32869@fed1read05>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com>`

```
> 01 INPUT-FIELD3  PIC S9(03) COMP-3.
>
> What is a comp-3 definition?. Some cobol books gave me an idea that
> this type of definitions are for space saving.

Comp-3 is a signed packed decimal field.

> Does that mean this field will not occupy 4 character spaces in memory
> and less. If this is correct, how much space they will occupy?

It will occupy 2 bytes in your example.  The right most half nibble contains
the sign, typically 'c' = positive, 'd' = negative, and 'f' = unsigned.

> Scenario
>
…[3 more quoted lines elided]…
> '100' in the receiving field?.

The field will contain hexadecimal '100f' in two bytes. The X(03) receiving
field will contain hex '100f20' in three bytes which is pretty worthless.
No conversion occurs because the move was to a display field.  The hex '20'
in the third byte is a space which is the default padding character when a
receiving display field is longer than the sending field.

If the move was to a 9(3) field instead, this field would then contain hex
'f1f0f0' (ascii assumed) in three bytes which would display as '100', which
obviously is useful.

The length of a comp-3 field is the number of digits in the field divided by
2 (remainder is dropped) plus 1.  For example a s9(7)v99 comp-3 field would
be 5 bytes long (9 / 2 = 4 + 1 = 5).  Also, a s9(6)v99 comp-3 field would
be 5 bytes long (8 / 2 = 4 + 1 = 5).  .  If either field contained the
number '-123456.78', the hex string for that number would be '012345678d' in
the 5 bytes.
```

##### ↳ ↳ Re: Novice: All about COMP-3 fields

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-13T21:42:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401132142.195afac2@posting.google.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com> <Kk9Mb.50785$gN.32869@fed1read05>`

```
"Easton Beymer" <eastonbeymer@hotmail.com> wrote

> If the move was to a 9(3) field instead, this field would then contain hex
> 'f1f0f0' (ascii assumed) in three bytes which would display as '100', which
> obviously is useful.

On an ASCII machine it will be x'313030' which is characters '100'. 
You must be thinking of EBCDIC.
```

#### ↳ Re: Novice: All about COMP-3 fields

- **From:** Wiggy <wignomore@nospam.btopenworld.com>
- **Date:** 2004-01-13T21:54:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bu1pe8$334$1@sparta.btinternet.com>`
- **In-Reply-To:** `<64713ce9.0401090351.6dd85003@posting.google.com>`
- **References:** `<64713ce9.0401090351.6dd85003@posting.google.com>`

```
I'm not sure my post from the other day got through, but the
Server Express docs are accessible from
http://supportline.microfocus.com/ . This includes details
of how COMP-3 (and other) items are represented.

Wiggy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
