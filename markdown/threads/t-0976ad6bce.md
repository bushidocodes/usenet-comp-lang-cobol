[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# REDEFINES confusion

_24 messages · 12 participants · 2003-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### REDEFINES confusion

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-09-12T12:50:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca>`

```
I'm a little confused on the uses of REDEFINES.  I think I have a handle 
on what it does, but I'm unclear on where one would use it.  I know I 
have some code that might benefit it, as I have a record made up of 
aggregate similar information.

I've gone through Murach's and done a few web searches without finding 
an example that speaks to me.  Does anyone have a good reference or 
starting point for more typical uses of the REDEFINES clause, and how it 
might better my life?
```

#### ↳ Re: REDEFINES confusion

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-12T14:59:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mJo8b.6840$fC5.1362045@news20.bellglobal.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca>`

```
"clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
news:BPm8b.69623$PD3.4724069@nnrp1.uunet.ca...
> I'm a little confused on the uses of REDEFINES.  I think I have a handle
> on what it does, but I'm unclear on where one would use it.  I know I
…[7 more quoted lines elided]…
>

It is really quite simple ... it allows you to define the same data in two
different layouts.

example .. I have two record layouts, completely differnt, that depend on
the first character of the record.  I describe it as so:

    01 record-layout.
        02 record-type            picture x.
            88 type-one            value 1.
            88 type-two            value 2.
        02 rest-of-record.
            03 data-name-one    picture x.
            03 data-name-two    picture x(50).
            03 data-name-three   picture x(10).
        02 second-definition redefines rest-of-record.
            03 data-name-four    picture x(25).
            03 data-name-five     picture x(25).
            03 data-name-six      picture x(11).

You will notice both definitions are the same size, though the second *may*
be shorter, it cannot be any longer.

You would place a record into "record-layout", then reference either the
first set of data names or the second, depending on the value of
record-type.

Donald
```

##### ↳ ↳ Re: REDEFINES confusion

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-09-12T16:53:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1nq8b.69721$PD3.4725069@nnrp1.uunet.ca>`
- **In-Reply-To:** `<mJo8b.6840$fC5.1362045@news20.bellglobal.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <mJo8b.6840$fC5.1362045@news20.bellglobal.com>`

```
Donald Tees wrote:

> "clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
> news:BPm8b.69623$PD3.4724069@nnrp1.uunet.ca...
…[18 more quoted lines elided]…
> 
[example snipped]

I think I have a handle on the syntax, but so far all I've seen are 
contrived examples, except for one that shows a date stored as a long 
string, or redefined as month/day/year strings.

My main query is that I'm just not sure where I would use such a device 
in my own code.  I think I have a few likely candidates, but was hoping 
for further examples.  That is, not how, but why.
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-12T21:04:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wxq8b.2831$NM1.522@newsread2.news.atl.earthlink.net>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <mJo8b.6840$fC5.1362045@news20.bellglobal.com> <1nq8b.69721$PD3.4725069@nnrp1.uunet.ca>`

```
The WHY is when you want to "look at" storage in multiple ways.  Some
examples (that you may or may not think of as "contrived" - but which are
fairly COMMON in real-world "business" applications).

Example 1:
  Same field may be alphanumeric or numeric

  05  Alpha-Field   Pic X(5).
  05 Num-field redefines Alpha-Field   Pic 999V99.

Example 2
   Some "monetary" field is looked at as number of cents or dollars

  05 Dollar-field   Pic  9999V99.
  05 Cents-Field redefines Dollar-Field  Pic  9(6).

Example 3:
  You want to look at one-byte of a binary field

 05  Full-Binary   Pic S9(04) Binary.
 05  Filler redefines Full-Binary.
     10  Byte-One   Pic X.
     10  Byte-Two  Pic X.
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

_(reply depth: 4)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-12T22:36:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MTr8b.139460$3o3.9933188@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <mJo8b.6840$fC5.1362045@news20.bellglobal.com> <1nq8b.69721$PD3.4725069@nnrp1.uunet.ca> <Wxq8b.2831$NM1.522@newsread2.news.atl.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:Wxq8b.2831$NM1.522@newsread2.news.atl.earthlink.net...
| The WHY is when you want to "look at" storage in multiple ways.  Some
| examples (that you may or may not think of as "contrived" - but which are
…[6 more quoted lines elided]…
|   05 Num-field redefines Alpha-Field   Pic 999V99.

This could also be coded:

   05  Alpha-Field.
     10 Num-field  Pic 999V99.

I run across quite a few unnecessary REDEFINES, but they are acceptable as
written, and you are correct that this construction is common..

I think REDEFINES usage is dropping because we don't have the same storage
constraints we had in the past.
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-09-13T10:57:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7KC8b.1986$ev2.1320952@newssrv26.news.prodigy.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <mJo8b.6840$fC5.1362045@news20.bellglobal.com> <1nq8b.69721$PD3.4725069@nnrp1.uunet.ca> <Wxq8b.2831$NM1.522@newsread2.news.atl.earthlink.net> <MTr8b.139460$3o3.9933188@bgtnsc05-news.ops.worldnet.att.net>`

```
"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:MTr8b.139460$3o3.9933188@bgtnsc05-news.ops.worldnet.att.net...
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
…[5 more quoted lines elided]…
> |   05 Num-field redefines Alpha-Field   Pic 999V99.


> This could also be coded:
>
…[4 more quoted lines elided]…
> written, and you are correct that this construction is common..

Since there is precisely zero difference in the generated code, one might
equally well suggest that manufacturing a group item with its implied
superior-subordinate relationships is unnecessary, since REDEFINES is
available...making this a question far more of style than of substance. (Not
to mention the possible source of a 200+ messages newsgroup thread ending
only when the name of  a certain personage associated with the National
Socialist Party of 1930's-1940's Germany is introduced).

MCM
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

_(reply depth: 6)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-13T11:43:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpD8b.137283$0v4.10066873@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <mJo8b.6840$fC5.1362045@news20.bellglobal.com> <1nq8b.69721$PD3.4725069@nnrp1.uunet.ca> <Wxq8b.2831$NM1.522@newsread2.news.atl.earthlink.net> <MTr8b.139460$3o3.9933188@bgtnsc05-news.ops.worldnet.att.net> <7KC8b.1986$ev2.1320952@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:7KC8b.1986$ev2.1320952@newssrv26.news.prodigy.com...
| "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
| news:MTr8b.139460$3o3.9933188@bgtnsc05-news.ops.worldnet.att.net...
…[15 more quoted lines elided]…
| > I run across quite a few unnecessary REDEFINES, but they are acceptable
as
| > written, and you are correct that this construction is common..
|
…[3 more quoted lines elided]…
| available...making this a question far more of style than of substance.

True, but it also makes the group item length dynamic, and you avoid having
to calculate the length when the numeric item is packed decimal.

|(Not
| to mention the possible source of a 200+ messages newsgroup thread ending
…[8 more quoted lines elided]…
|
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-13T04:20:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xWw8b.53335$Mb2.1738541@twister.tampabay.rr.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <mJo8b.6840$fC5.1362045@news20.bellglobal.com> <1nq8b.69721$PD3.4725069@nnrp1.uunet.ca>`

```
Just a few examples where I have seen it.  After writing these out it came
down to two things IMHO.
I didn't get this from code so syntax may be wrong.

1) You don't use more storage then necessary.  Example 5 shows this; granted
you could declare multiple tables (if the data types were different sizes
such as 100 characters and a Fixed Decimal 15,5) and then use the
appropriate table and save even more storage; however single tables are more
simple to share across programs and easier to follow.

2) The main point is that you can take a field that has disparate types and
move them into fields more appropriate to their natural view.  See Example
3.

I guess the simple thing is that there is no instance I can think of where a
REDEFINES is *REQUIRED*.  However, it can be used to allow a
function/procedure to treat a piece of data in a generic way in spite of the
fact that the underlying data is not the same without another allocated
storage and a move. Big whoop I hear you say...but I think that no one reads
storage first and then the code....they read the code then the storage if
they cannot figure it out.....remove unecessary moves make the code
easier...that's my argument and I's sticking to it.

Example 1
=======
We have a key field that for some records is a numeric field and for some
records is a text field where it drops into a common leg which uses that
value.

01  KEY.
    05 TEXT-KEY PIC X(10).
    05 NUM-KEY REDEFINES TEXT-KEY.
        05 NUMBER-KEY PIC  9(05).
        05 SPACE-FILLER PIC X(05).  <----Prevents a compiler Warning

NUMERIC-PROCESS-LEG.
        MOVE NUMBER TO NUMBER-KEY
        PERFORM COMMON-LEG

TEXT-PROCESS-LEG
        MOVE NUMBER TO TEXT-KEY
        PERFORM COMMON-LEG

COMMON-LEG.
        LOG KEY.

Example 2
=======
Often it used in reports just to keep alignment - this was discussed as an
option in the thread that started with an example that some people didn't
like and went into report writer pros/cons.
You can align headers/underlines using a redefines.

Example 3
=======
01 SHORT-INT PIC S9(04) USAGE IS BINARY.
01 CHAR-INT    REDEFINES SHORT-INT PIC X(02).
This can be used in a data field that includes binary values.  This is
common in non xml data transmission to insert offsets etc.  This is the most
common use where I am at.

So for example a record that has a int for the overall length in a PIC
X(1000).

01 MSG  PIC X(1000) USAGE IS BINARY.
01 MSG-LEN REDEFINES MSG PIC S9(04) USAGE IS BINARY.

You could then do either of these without a move (big whoop I hear you say)

READ MSG-SOURCE INTO MSG
COMPUTE TOTAL-BYTES = TOTAL-BYTES + MSG-LEN

Example 4
=======
01 DATA-FIELD.
    05 DATA-TYPE  PIC 9.
    05 DATA-TYPE-1.
         10 COPY DATA-TYPE-1.
    05 DATA-TYPE-2 REDEFINES DATA-TYPE-1.
         10 COPY DATA-TYPE-2.
    ...etc etc...
.
Read data field into DATA-FIELD.

IF DATA-TYPE = 1 THEN
    Do Stuff using fields of DATA-TYPE-1
END-IF
IF DATA-TYPE = 2 THEN PERFORM MSG-2 PROCESSING.
    Do Stuff using fields of DATA-TYPE-2
END-IF

Doesn't do anything except save you a MOVE and storage.  You've said you
understood this and needed an example...Maybe you just don't value the use
of it and are happy doing it the other way.

Example 5
=======

In C, the equivalend is the union operator that you can use to build a table
of different types of different lengths.  The same is true of cobol -

01 TABLE-DATA OCCURS 1 TO 1000 TIMES DEPENDING ON TABLE-ROWS,
      10 TABLE-DATA-TYPE PIC 99.
      10 CHAR-FIELD                      PIC X(04).
      10 SHORT-INT                         PIC S9(04) REDEFINES CHAR-FIELD
Nothing to stop you from
01 TEXT-DATA OCCURS 1 TO 1000 TIMES DEPENDING ON TEXT-ROWS,
.....
01 SHORT-INT-DATA OCCURS 1 TO 1000 TIMES DEPENDING ON SI-ROWS,
.....

JCE

"clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
news:1nq8b.69721$PD3.4725069@nnrp1.uunet.ca...
> Donald Tees wrote:
>
…[15 more quoted lines elided]…
> > It is really quite simple ... it allows you to define the same data in
two
> > different layouts.
> >
> > example .. I have two record layouts, completely differnt, that depend
on
> > the first character of the record.  I describe it as so:
> >
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-13T04:26:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_%w8b.53343$Mb2.1739131@twister.tampabay.rr.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <mJo8b.6840$fC5.1362045@news20.bellglobal.com> <1nq8b.69721$PD3.4725069@nnrp1.uunet.ca>`

```
From: "jce" <defaultuser@hotmail.com>
Subject: Re: REDEFINES confusion
Date: Saturday, September 13, 2003 12:20 AM

Just a few examples where I have seen it.  After writing these out it came
down to two things IMHO.
I didn't get this from code so syntax may be wrong.

1) You don't use more storage then necessary.  Example 5. Yyou could declare
multiple tables (if the data types were different sizes such as 100
characters and a Fixed Decimal 15,5) and then use the
appropriate table and save even more storage; however single tables are more
simple to share across programs and easier to follow.

2) The main point is that you can take a field that has disparate types and
move them into fields more appropriate to their natural view.  See Example
3.

I guess the simple thing is that there is no instance I can think of where a
REDEFINES is *REQUIRED*.  However, it can be used to allow a
function/procedure to treat a piece of data in a generic way in spite of the
fact that the underlying data is not the same.  You could do the same with
another storage allocation and a move so I hear you say "Big whoop"...I
think that no one reads
storage first and then the code....they read the code then the storage if
they cannot figure it out from the name what the storage likely
is.....removing unecessary moves make the code easier to read...that's my
argument and I'm sticking to it.

Example 1
=======
We have a key field that for some records is a numeric field and for some
records is a text field where it drops into a common leg which uses that
value.

01  KEY.
    05 TEXT-KEY PIC X(10).
    05 NUM-KEY REDEFINES TEXT-KEY.
        05 NUMBER-KEY PIC  9(05).
        05 SPACE-FILLER PIC X(05).  <----Prevents a compiler Warning

NUMERIC-PROCESS-LEG.
        MOVE NUMBER TO NUMBER-KEY
        PERFORM COMMON-LEG

TEXT-PROCESS-LEG
        MOVE NUMBER TO TEXT-KEY
        PERFORM COMMON-LEG

COMMON-LEG.
        LOG KEY.

Example 2
=======
Often it used in reports just to keep alignment - this was discussed as an
option in the thread that started with an example that some people didn't
like and went into report writer pros/cons.
You can align headers/underlines using a redefines.

Example 3
=======
01 SHORT-INT PIC S9(04) USAGE IS BINARY.
01 CHAR-INT    REDEFINES SHORT-INT PIC X(02).
This can be used in a data field that includes binary values.  This is
common in non xml data transmission to insert offsets etc.  This is the most
common use where I am.

So for example a record that has a int for the overall length in a PIC
X(1000).

01 MSG  PIC X(1000) USAGE IS BINARY.
01 MSG-LEN REDEFINES MSG PIC S9(04) USAGE IS BINARY.

You could then do either of these without a move (big whoop I hear you say)

READ MSG-SOURCE INTO MSG
COMPUTE TOTAL-BYTES = TOTAL-BYTES + MSG-LEN

Example 4
=======
01 DATA-FIELD.
    05 DATA-TYPE  PIC 9.
    05 DATA-TYPE-1.
         10 COPY DATA-TYPE-1.
    05 DATA-TYPE-2 REDEFINES DATA-TYPE-1.
         10 COPY DATA-TYPE-2.
    ...etc etc...
.
Read data field into DATA-FIELD.

IF DATA-TYPE = 1 THEN
    Do Stuff using fields of DATA-TYPE-1
END-IF
IF DATA-TYPE = 2 THEN PERFORM MSG-2 PROCESSING.
    Do Stuff using fields of DATA-TYPE-2
END-IF

Doesn't do anything except save you a MOVE and storage.  You've said you
understood this and needed an example...Maybe you just don't value the use
of it and are happy doing it the other way.

Example 5
=======

In C, the equivalend is the union operator that you can use to build a table
of different types of different lengths.  The same is true of cobol -

01 TABLE-DATA OCCURS 1 TO 1000 TIMES DEPENDING ON TABLE-ROWS,
      10 TABLE-DATA-TYPE PIC 99.
      10 CHAR-FIELD                      PIC X(04).
      10 SHORT-INT                         PIC S9(04) REDEFINES CHAR-FIELD
Nothing to stop you from the following; however, if you have 100 types you
have 100 tables....YUK!

01 TEXT-DATA OCCURS 1 TO 1000 TIMES DEPENDING ON TEXT-ROWS,
.....
01 SHORT-INT-DATA OCCURS 1 TO 1000 TIMES DEPENDING ON SI-ROWS,
.....

JCE

"clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
news:1nq8b.69721$PD3.4725069@nnrp1.uunet.ca...
> Donald Tees wrote:
>
…[15 more quoted lines elided]…
> > It is really quite simple ... it allows you to define the same data in
two
> > different layouts.
> >
> > example .. I have two record layouts, completely differnt, that depend
on
> > the first character of the record.  I describe it as so:
> >
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

_(reply depth: 4)_

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-09-15T11:24:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oQk9b.70587$PD3.4736715@nnrp1.uunet.ca>`
- **In-Reply-To:** `<_%w8b.53343$Mb2.1739131@twister.tampabay.rr.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <mJo8b.6840$fC5.1362045@news20.bellglobal.com> <1nq8b.69721$PD3.4725069@nnrp1.uunet.ca> <_%w8b.53343$Mb2.1739131@twister.tampabay.rr.com>`

```
jce wrote:

> From: "jce" <defaultuser@hotmail.com>
> Subject: Re: REDEFINES confusion
…[5 more quoted lines elided]…
> 
[good examples snipped]

Thanks a lot.  There's a lot for me to review here, when I have more 
coffee in me.  I'm saving this to a local store for my future reference.

Thanks again.

-- cm
```

#### ↳ Re: REDEFINES confusion

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-09-12T22:37:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F624BAC.E0D0D375@shaw.ca>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca>`

```


clvrmnky wrote:

> I'm a little confused on the uses of REDEFINES.  I think I have a handle
> on what it does, but I'm unclear on where one would use it.  I know I
…[6 more quoted lines elided]…
> might better my life?

I haven't got Murach's book, but go through his text looking for use of
Tables :-

01 D1
    05 pic x(36) value "JanFebMartAprMayJunJulAugSepOctNovDec".
01 D2 redefines D1.
     05 D-Month occurs 12 pic x(03).

01 In-Date.
     05 In-ccyy                pic 9(04).
     05 In-month              pic 9(02).
     05 In-Day                 pic 9(02).

01 Out-Date.
     05 Out-ccyy            pic x(04).
     05 Out-Month         pic x(03).
     05 Out-Day             pic z9.

move In-ccyy to Out-ccyy
move D-Month(In-Month) to Out-Month
move In-Day  to Out-Day
- - - - - - - - - - - - - - - - - - - - - -

Note: Just for readability of tables like above - it is 'preferable' if you
put commas in between where they might have a mx of alpha and numeric values
:-

01 D3
    05 pic x(12) value "01,NWT,04,005,6,70".
01 D4 redefines D3.
     05 D5-record.
         10 D-CustomerType          pic 9(02).
         10                                      pic x.
         10 D-Division                    pic x(03).
         10                                      pic x.
         10 D-?????                       pic 9(02).
         10                                      pic x.
         10 D-?????                       pic 9(03).
         10                                      pic x.
         10 D-????                         pic 9(01).
         10                                      pic x.
         10 D-?????                       pic 9(02).

- - - - - - - - - - - - - - - - - - - - - - - - - -

01 ErrorCode                        pic 99.
    88 ErrorNoKey                value 1.
    88 ErrorBlankName          value 2.
    88 Error.........

01 E1.
   05 pic x(50) value "No Key for this record".
   05 pic x(50) value "Name can't be blank".
   05 pic x(50) value "This message is closer to fifty characters"..
01 E2 redefines E1.
     05 E-text occurs "n" pic x(50).

Note : You don't have to "flesh out" the individual error messages to 50
characters
with spaces, (they are "all" 50 characters in length).

Accept Namefield
if NameField = spaces
   set ErrorBlankName to true
   perform DISPLAY-ERROR
End-if
.

DISPLAY-ERROR.

display E-Text(ErrorCode).

...............................
```

#### ↳ Re: REDEFINES confusion

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-09-13T17:08:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vm75c0ndqs3rd9@corp.supernews.com>`
- **In-Reply-To:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca>`

```
clvrmnky wrote:

> I'm a little confused on the uses of REDEFINES.  I think I have a handle 
> on what it does, but I'm unclear on where one would use it.  I know I 
…[6 more quoted lines elided]…
> might better my life?

REDEFINES is very handy.  Most things that REDEFINES does you can also 
do with reference modification, but redefining something into a 
meaningful name makes code more readable.  Here one way you can use 
redefines - we have the following in our code.  A key for a record can 
be either 6 positions (equipment ID and unit ID) or 25 positions 
(part/serial number).  We have a field layout like this...

01  Eqpp-Key                    Pic X(25).
01  Eqpp-Key-X             Redefines Eqpp-Key.
     05  Eqpp-Key-Equip-ID       Pic X(05).
     05  Eqpp-Key-Equip-Unit-ID  Pic X(01).
     05  Filler                  Pic X(19).
01  Eqpp-Key-X2            Redefines Eqpp-Key.
     05  Eqpp-Key-Part-Number    Pic X(15).
     05  Eqpp-Key-Serial-Number  Pic X(10).

This way, you can refer to the generic "Key" if you don't know what kind 
of equipment you have, or you can refer to the specific type if you know 
what you've got.  Another use is splitting stuff out - say you have have 
the following...

01  My-String               Pic X(80).
01  My-Characters      Redefines My-String.
     05  My-Character   Occurs 80 Times  Pic X(01).

...then you can step through the string, character by character, in a 
Perform Varying Loop (for example).  Sometimes, you'll see something 
like this...

01  Months    Pic X(36) Value "JANFEBMARAPRMAYJUNJULAUGSEPOCTNOVDEC".
01  Months-Table  Redefines Months.
     03  Month     Occurs 12 Times  Pic X(03).

This allows you to get a 3-character abbreviation by a month number. 
Month (1) is "JAN", Month (2) is "FEB", etc.

One of the most useful things REDEFINES does is force the data type of a 
particular item.  We have dates that we store as CCYYDDDHHMMSS (4-digit 
year, 3-digit ordinal day, 6-digit time).  The definition of this is Pic 
9(13).  Any group item is alphanumeric, so to force each subset of these 
items to be numeric, we have definitions such as...

01  My-Dt-J7-Tm-6                Pic 9(13).
01  My-Dt-J7-Tm-6-X          Redefines My-Dt-J7-Tm-6.
     05  My-Date-J7               Pic 9(07).
     05  My-Date-J7-X         Redefines My-Date-J7.
         10  My-Date-J-CC         Pic 9(02).
         10  My-Date-J5           Pic 9(03).
         10  My-Date-J5-X     Redefines My-Date-J5.
             15  My-Date-J-YY     Pic 9(02).
             15  My-Date-J-DDD    Pic 9(03).
     05  My-Time-6                Pic 9(06).
     05  My-Time-6-X          Redefines My-Time-6.
         10  My-Time-4            Pic 9(04).
         10  My-Time-4-X      Redefines My-Time-4.
             15  My-Time-HH       Pic 9(02).
             15  My-Time-MM       Pic 9(02).
         10  My-Time-SS           Pic 9(02).
01  My-Dt-J7-Tm-6-X2         Redefines My-Dt-J7-Tm-6.
     05  My-Dt-J7-Tm-4            Pic 9(11).
     05  Filler                   Pic X(02).

By using this definition, we can access any part of the date as a 
numeric item.  These suffixes are also part of our naming standards (J = 
"Julian" - not exactly Julian, more ordinal, but whatever...).  That 
way, you know exactly what type of date or time item you're comparing.

There's more than you can do with it, but I've hit the biggest uses with 
my examples here - meaningful names for multi-use fields, breaking out 
long fields in to even repetitions of fixed characters, and forcing data 
types on fields.
```

##### ↳ ↳ Re: REDEFINES confusion

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-09-14T06:53:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_4-dneJVnplMy_miU-KYgw@giganews.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <vm75c0ndqs3rd9@corp.supernews.com>`

```
LX-i wrote:
> Sometimes, you'll see something
> like this...
…[6 more quoted lines elided]…
> Month (1) is "JAN", Month (2) is "FEB", etc.

You could also code the above as:
01  Months Value "JanFebMarAprMayJunJulAugSepOctNovDec".
   02  Month occurs 12 Pic X(3).
```

#### ↳ Re: REDEFINES confusion

- **From:** "Mudd Bug" <muddbug@cox.net>
- **Date:** 2003-09-14T01:50:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BPP8b.5188$3Y2.4012@news2.central.cox.net>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca>`

```



01  ws-date-yyyymmdd         pic 9(8).
01  ws-date-yyyymmdd-red redefines ws-date-yyyymmdd.
      05  ws-yyyy    pic 9(4).
      05  ws-mmdd pic 9(4).

01  wk-date-mmddyyyy        pic 9(8).
01  wk-date-mmddyy-red redefines wk-date-mmddyy.
      05  wk-mmdd                    pic 9(4).
      05  wk-yyyy                       pic 9(4).
....

 flip-date.
    move ws-yyyy to wk-yyyy.
    move ws-mmdd to wk-mmdd.


"clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
news:BPm8b.69623$PD3.4724069@nnrp1.uunet.ca...
> I'm a little confused on the uses of REDEFINES.  I think I have a handle
> on what it does, but I'm unclear on where one would use it.  I know I
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: REDEFINES confusion

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-15T10:06:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f64e776_3@news.athenanews.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <BPP8b.5188$3Y2.4012@news2.central.cox.net>`

```

"Mudd Bug" <muddbug@cox.net> wrote in message
news:BPP8b.5188$3Y2.4012@news2.central.cox.net...
>
>
…[15 more quoted lines elided]…
>

I would use...

 01  ws-date-yyyymmdd         pic x(8).
 01  wk-date-mmddyyyy        pic x(8).
...
flip-date.
      move  ws-date-yyyymmdd (5:4) to wk-date-mmddyyyy
      move  ws-date-yyyymmdd (1:4) to wk-date-mmddyyyy (5:)

...which is 50% less  source code, and much better object code because there
is no arithmetic conversion required.

I see no point in holding dates as numeric unless you intend to do some form
of arithmetic on them.

Doing the two moves in Mudd Buggs example MAY require conversion because
they are moves to display numeric fields. As both source and target are
display numeric and they are the same length, we would hope that compiler
optimization will generate a straight move, but this is by no means
GUARANTEED (it will depend on the compiler...).

Pete.

>
> "clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

- **From:** "Mudd Bug" <muddbug@cox.net>
- **Date:** 2003-09-15T01:14:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5o89b.6798$3Y2.4632@news2.central.cox.net>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <BPP8b.5188$3Y2.4012@news2.central.cox.net> <3f64e776_3@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f64e776_3@news.athenanews.com...
>
> "Mudd Bug" <muddbug@cox.net> wrote in message
…[27 more quoted lines elided]…
>       move  ws-date-yyyymmdd (1:4) to wk-date-mmddyyyy (5:)

Not all compilers support the above syntax.

>
> ...which is 50% less  source code, and much better object code because
there
> is no arithmetic conversion required.
>
> I see no point in holding dates as numeric unless you intend to do some
form
> of arithmetic on them.
>
…[11 more quoted lines elided]…
> > > I'm a little confused on the uses of REDEFINES.  I think I have a
handle
> > > on what it does, but I'm unclear on where one would use it.  I know I
> > > have some code that might benefit it, as I have a record made up of
…[4 more quoted lines elided]…
> > > starting point for more typical uses of the REDEFINES clause, and how
it
> > > might better my life?
> > >
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-15T13:46:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f651aed_5@news.athenanews.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <BPP8b.5188$3Y2.4012@news2.central.cox.net> <3f64e776_3@news.athenanews.com> <5o89b.6798$3Y2.4632@news2.central.cox.net>`

```

"Mudd Bug" <muddbug@cox.net> wrote in message
news:5o89b.6798$3Y2.4632@news2.central.cox.net...
>
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
…[33 more quoted lines elided]…
>

No, certainly not if they aren't COBOL compilers...<G>

A reasonable point.

I believe anything that calls itself COBOL and was released after 1985 will
support it,  but Bill Klein will know for sure what the status of reference
modding is, in regard to the COBOL Standard.

Can you comment please, Bill?

[MY compiler supports it ;-). My comment was about what I would use...]

Pete.
<snip>
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-17T00:55:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8iO9b.22900$Aq2.1805@newsread1.news.atl.earthlink.net>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <BPP8b.5188$3Y2.4012@news2.central.cox.net> <3f64e776_3@news.athenanews.com> <5o89b.6798$3Y2.4632@news2.central.cox.net> <3f651aed_5@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f651aed_5@news.athenanews.com...
>
> "Mudd Bug" <muddbug@cox.net> wrote in message
…[6 more quoted lines elided]…
> > > news:BPP8b.5188$3Y2.4012@news2.central.cox.net...
<snip>
> > >       move  ws-date-yyyymmdd (5:4) to wk-date-mmddyyyy
> > >       move  ws-date-yyyymmdd (1:4) to wk-date-mmddyyyy (5:)
…[8 more quoted lines elided]…
> I believe anything that calls itself COBOL and was released after 1985
will
> support it,  but Bill Klein will know for sure what the status of
reference
> modding is, in regard to the COBOL Standard.
>
…[5 more quoted lines elided]…
> <snip>

Reference modification was added to the ANSI/ISO COBOL Standard in the '85
Standard.  Having said that, it is part of "Nucleus 2" - not "Nucleus 1".
This means that a "fully conforming" '85 Standard compiler need NOT include
support for reference modification UNLESS it claims conformance to the "HIGH
subset". (No compiler claiming support for the '74 or '68 Standard need
include this feature - although they could as an EXTENSION.)

Does this answer the question to me?
```

###### ↳ ↳ ↳ Re: REDEFINES confusion

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-17T14:14:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f67c475_1@news.athenanews.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <BPP8b.5188$3Y2.4012@news2.central.cox.net> <3f64e776_3@news.athenanews.com> <5o89b.6798$3Y2.4632@news2.central.cox.net> <3f651aed_5@news.athenanews.com> <8iO9b.22900$Aq2.1805@newsread1.news.atl.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:8iO9b.22900$Aq2.1805@newsread1.news.atl.earthlink.net...
<snip>
> > >
> > > Not all compilers support the above syntax.
…[21 more quoted lines elided]…
> This means that a "fully conforming" '85 Standard compiler need NOT
include
> support for reference modification UNLESS it claims conformance to the
"HIGH
> subset". (No compiler claiming support for the '74 or '68 Standard need
> include this feature - although they could as an EXTENSION.)
>
> Does this answer the question to me?
>
Eloquently. Thank you Bill.
(I honestly don't know how you do it...<G> I am reminded of Oliver
Goldsmith's Village Schoolteacher...

"While words of learned length and thundering sound
 Amazed the gaping rustics ranged around.
 And still they gazed
 And still their wonder grew
 That one small head could carry
 All he knew."

-The Deserted Village-  )

So Mudd Bugg's point has some substance in fact.

I'd be interested to know of any COBOL compilers in current use that DON'T
support the "HIGH subset"...

Pete.
```

###### ↳ ↳ ↳ Obscue but, ... (was: REDEFINES confusion

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-17T03:44:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LMQ9b.24013$Aq2.21571@newsread1.news.atl.earthlink.net>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <BPP8b.5188$3Y2.4012@news2.central.cox.net> <3f64e776_3@news.athenanews.com> <5o89b.6798$3Y2.4632@news2.central.cox.net> <3f651aed_5@news.athenanews.com> <8iO9b.22900$Aq2.1805@newsread1.news.atl.earthlink.net> <3f67c475_1@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f67c475_1@news.athenanews.com...
>
> "William M. Klein" <wmklein@nospam.netcom.com> wrote in message
> news:8iO9b.22900$Aq2.1805@newsread1.news.atl.earthlink.net...
> <snip>
> > > >
<snip>
> I'd be interested to know of any COBOL compilers in current use that DON'T
> support the "HIGH subset"...
>
> Pete.
>

This gets into anothe "obscure" difference.  Since 1989 (in the US) the
intrinsic function module has been a required part of the FIPS "high subset"
but is an OPTIONAL module in the ANSI/ISO Standard.  Therefore, RM/COBOL
(for example) conforms to the high subset of the ANSI/ISO Standard - but is
only an "intermediate level" compiler when it comes to the FIPS (Federal)
Standard.

IBM's "ILE COBOL" (COBOL on OS/400) does NOT include High level suport (but
includes PARTS of intrinsic functions - but not even ALL of Nucleus level 2)
```

#### ↳ Re: REDEFINES confusion

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-09-15T10:44:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f64f101_2@news.athenanews.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca>`

```

"clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
news:BPm8b.69623$PD3.4724069@nnrp1.uunet.ca...
> I'm a little confused on the uses of REDEFINES.  I think I have a handle
> on what it does, but I'm unclear on where one would use it.  I know I
…[7 more quoted lines elided]…
>

REDEFINES is one of the most powerful things in COBOL. Combined with 66
level RENAMES (which allows "redefinition" across group boundaries, in
effect, "regrouping" data structures, and which nobody ever uses...<G>) you
can achieve effects that are not possible with any combination of COBOL
verbs.

Like all powerful tools it gets "misused" a lot. (I unclude "unnecessary
use" as "misuse"...but it really comes down to style in the end. People get
used to writing code a certain way, when faced with a certain problem, and
then they continue doing that.  For example, I would use REDEFINES whenever
I need to define a table. I don't even think about it... When I define
tables, they use REDEFINES, OCCURS, and INDEXED BY. Even though this is not
always necessary. (See JerryMouse's post...). How seriously bad is that? To
me it is acceptable...)

This thread has posted good examples (and a few "not so good" ones) but I
understand it is not the mechanics that bothers you, it is the conceptual
use.

You will have realised that there are two fundamental reasons why the
language has this facility:

1. To save on storage space (which, many years ago, was precious and
expensive).
2. To provide alternative paths of attack on data.

Those two reasons alone justify its inclusion.

But there are cases where REDEFINES is "the only way"... (Not really, when
programmers say: "It's the only way..." what they really mean is: "It's the
most desirable way I can think of..." <G>.)

So, here's an example from live code where I couldn't think of any other way
than using REDEFINES...

SITUATION:  A component method is talking to a COM server. When things go
pants, the server returns a hex code as a pointer in the general direction
of what was wrong. All the documentation shows this code in Hex so I want it
to print on my system log in Hex. (To facilitate looking it up...)

The following "sub-routine" (whatever that means...<G>) converts bytes into
their Hex equivalent.

WORKING-STORAGE.
...

 01  COM-server-error-data.
     12 COM-error-type     pic x.
     12 COM-SCODE          pic x(4).
     12 COM-SCODE-Hex      pic x(10).
     12 COM-SCODE-Text     pic x(20).
     12 COM-Desc           Pic x(256).
     12 COM-Desc-Len       pic s9(9) comp-5.
     12 COM-count          pic 9 value zero.

 01  Hex-work.
     12 hex-1             pic 1(4).
     12 hex-2             pic 1(4).

 01  Hex-bin              pic s9(4) binary.
*
* Some smoke and mirrors to manipulate bits...
*
 01  Hex-smoke redefines  Hex-bin.
     12 filler            pic x.
     12 filler            pic 1(4).
     12 hex-bits          pic 1(4).

 01  Hex-value-table.
     12 filler            pic x value zero.
     12 filler            pic x value '1'.
     12 filler            pic x value '2'.
     12 filler            pic x value '3'.
     12 filler            pic x value '4'.
     12 filler            pic x value '5'.
     12 filler            pic x value '6'.
     12 filler            pic x value '7'.
     12 filler            pic x value '8'.
     12 filler            pic x value '9'.
     12 filler            pic x value 'A'.
     12 filler            pic x value 'B'.
     12 filler            pic x value 'C'.
     12 filler            pic x value 'D'.
     12 filler            pic x value 'E'.
     12 filler            pic x value 'F'.
 01  hex-vals redefines hex-value-table.
     12 hex-val           pic x occurs 16
                          indexed by hex-x1.

PROCEDURE DIVISION.
...
*
* Try to establish WHICH COM Server screwed up...
*
         invoke EXCEPTION-OBJECT "GET-ERROR-TYPE"          returning
COM-error-type
         invoke EXCEPTION-OBJECT "GET-SCODE"               returning
COM-SCODE
*
* Convert SCODE to Hex...
*
         move '0x' to COM-SCODE-Hex (1:2)
         move 3 to K
         perform
            varying J
               from 1
                 by 1
              until J > 4
            move COM-SCODE (J:1) to hex-work
            move zero to hex-bin
            move hex-1 to hex-bits
            add 1 to hex-bin
            set hex-x1 to hex-bin
            move hex-val (hex-x1) to COM-SCODE-Hex (K:1)
            add 1 to K
            move zero to hex-bin
            move hex-2 to hex-bits
            add 1 to hex-bin
            set hex-x1 to hex-bin
            move hex-val (hex-x1) to COM-SCODE-Hex (K:1)
            add 1 to K
         end-perform

         invoke EXCEPTION-OBJECT "GET-SCODE-TEXT"          returning
COM-SCODE-Text
         invoke EXCEPTION-OBJECT "GET-DESCRIPTION"         returning
COM-Desc
         if COM-Desc = spaces or low-values
            move zero to COM-Desc-Len
         else
            invoke EXCEPTION-OBJECT "GET-DESCRIPTION-LENGTH"
                                                           returning
COM-Desc-Len
         end-if
         set S2NObj    to NULL
         set WBRSvrObj to NULL
         display "Objects were NULLified from exception process." upon
syserr
         display "COM-error-type="  COM-error-type  upon syserr
         display "COM-SCODE     ="  COM-SCODE-Hex   upon syserr

...

The inline perform above converts 4 bytes to hex and formats it as:
0xFFFFFFFF

You could easily modify it to take any number of bytes and build your own
internal "Hex dump" of records or buffers or whatever, but most environments
provide such a facility that can be called (NOT the PC, as far as I know...)

The point is that I don't know how the above could be achieved in COBOL
WITHOUT using REDEFINES... (although I'm reasonably sure that given some
time and thought, it probably COULD be). I leave this as an exercise for
readers with more time than I currently have available <G>.

Pete.
```

##### ↳ ↳ Re: REDEFINES confusion

- **From:** clvrmnky <clvrmnky@coldmail.com.invalid>
- **Date:** 2003-09-15T11:27:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iTk9b.70591$PD3.4736713@nnrp1.uunet.ca>`
- **In-Reply-To:** `<3f64f101_2@news.athenanews.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <3f64f101_2@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:

> "clvrmnky" <clvrmnky@coldmail.com.invalid> wrote in message
> news:BPm8b.69623$PD3.4724069@nnrp1.uunet.ca...
…[31 more quoted lines elided]…
>
[examples snipped]

Thanks for your help.  I've saved a copy of this posting for careful 
review.  This is exactly the kind of stuff I need to get my teeth into 
the project I've been thrown into.

-- cm
```

##### ↳ ↳ Re: REDEFINES confusion

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-09-15T22:36:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vmctvn1mtnaa1@corp.supernews.com>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <3f64f101_2@news.athenanews.com>`

```

Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in message
news:3f64f101_2@news.athenanews.com...
[snip]

> The point is that I don't know how the above could be achieved in COBOL
> WITHOUT using REDEFINES... (although I'm reasonably sure that given some
> time and thought, it probably COULD be). I leave this as an exercise for
> readers with more time than I currently have available <G>.

[Just taking a break from re-reading Federalist 78.]

The following has not been tested.

WORKING-STORAGE.
...

 01  COM-server-error-data.
     12 COM-error-type     pic x.
     12 COM-SCODE          pic x(4).
     12 COM-SCODE-Hex      pic x(10).
     12 COM-SCODE-Text     pic x(20).
     12 COM-Desc           Pic x(256).
     12 COM-Desc-Len       pic s9(9) comp-5.
     12 COM-count          pic 9 value zero.

 01  Hex-bin              pic s9(4) binary.
 01  Hex-left              pic s9(4) binary.
 01  Hex-right           pic s9(4) binary.

 01  Hex-val pic x(16) value '0123456789ABCDEF'.

PROCEDURE DIVISION.
...
[code snipped]
*
* Convert SCODE to Hex...
*
         move '0x' to COM-SCODE-Hex (1:2)
         move 3 to K
         perform
            varying J
               from 1
                 by 1
              until J > 4
            compute hex-bin = function ord (COM-SCODE (J:1)) - 1
            divide hex-bin by 16 giving hex-left remainder hex-right
            move hex-val (hex-left + 1:1) to COM-SCODE-Hex (K:1)
            add 1 to K
            move hex-val (hex-right + 1:1) to COM-SCODE-Hex (K:1)
            add 1 to K
         end-perform

[code snipped]
```

##### ↳ ↳ Re: REDEFINES confusion

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-20T11:37:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CZWab.146262$0v4.10810576@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<BPm8b.69623$PD3.4724069@nnrp1.uunet.ca> <3f64f101_2@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f64f101_2@news.athenanews.com...
|

I snipped the post, Pete's comments were on the money.

Here's another convert hex to character program.
You'll see redefines etc.

       IDENTIFICATION DIVISION.
       PROGRAM-ID.  'HEXCHAR-CONVER-HEX-TO-CHAR'.

      *AUTHOR.  D HARLEY.
      *
      *    ==========================================================
      *    THIS IS A NESTED PROGRAM
      *    ==========================================================

       ENVIRONMENT DIVISION.

       DATA DIVISION.

       WORKING-STORAGE SECTION.

       01  IND-INDICATORS.

           05                        PIC X   VALUE  'Y'.
             88  IND-FIRST-CALL      VALUE  'Y'.
             88  IND-NOT-FIRST-CALL  VALUE  'N'.

       01  T-CHAR-HEX-CHARACTERS.

           05  T-CHAR-VALUES    PIC X(16)  VALUE '0123456789ABCDEF'.

           05  REDEFINES         T-CHAR-VALUES.

             10  T-CHAR          PIC X
                                 OCCURS  16  TIMES
                                 INDEXED  BY  I-CHAR-1 I-CHAR-2.

       01  T-HEX-CHARACTERS.

           05 T-HEX-CHARS        OCCURS  256  TIMES
                                 INDEXED  BY  I-HEX.
             10 T-HEX-CHAR-1     PIC X.
             10 T-HEX-CHAR-2     PIC X.

       01  WK-WORK.

           05  WK-HEX-NUM        PIC 9(4)  BINARY.
           05         REDEFINES  WK-HEX-NUM.
             10                  PIC X.
             10  WK-HEX-NUM-LOW  PIC X.

       LINKAGE  SECTION.

       01  IN-HEX-BYTE           PIC X.

       01  OUT-HEX-CHARS         PIC  XX.

       PROCEDURE DIVISION  USING  IN-HEX-BYTE
                                  OUT-HEX-CHARS.

           IF  IND-FIRST-CALL
               SET  IND-NOT-FIRST-CALL  TO  TRUE
               PERFORM  INIT-CONVERSION-TBL
           END-IF.

           MOVE  0            TO  WK-HEX-NUM
           MOVE  IN-HEX-BYTE  TO  WK-HEX-NUM-LOW
           ADD   1            TO  WK-HEX-NUM
           MOVE  T-HEX-CHARS (WK-HEX-NUM)  TO   OUT-HEX-CHARS

           GOBACK.

       INIT-CONVERSION-TBL.

           SET  I-HEX  TO  1.
           PERFORM  VARYING  I-CHAR-1  FROM  1  BY  1
                      UNTIL  I-CHAR-1  >  16
             PERFORM  VARYING  I-CHAR-2  FROM  1  BY  1
                        UNTIL  I-CHAR-2  >  16
                MOVE  T-CHAR (I-CHAR-1)  TO  T-HEX-CHAR-1 (I-HEX)
                MOVE  T-CHAR (I-CHAR-2)  TO  T-HEX-CHAR-2 (I-HEX)
                SET  I-HEX  UP  BY  1
             END-PERFORM
           END-PERFORM.

       END PROGRAM  'HEXCHAR-CONVER-HEX-TO-CHAR'.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
