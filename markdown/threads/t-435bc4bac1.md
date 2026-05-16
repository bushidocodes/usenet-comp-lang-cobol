[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# STRING help please

_2 messages · 2 participants · 2000-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### STRING help please

- **From:** "M S" <maz@websurf.fsnet.co.uk>
- **Date:** 2000-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8k5qr6$9bt$1@newsg2.svr.pol.co.uk>`

```
Hi
I am using SCREEN SECTION to accept input to make the customer-address field
which is PIC X(60). It has got 4 lines:
  ie line one   maximum input pic x(20)
     line two   maximum input pic x(20)
     line three maximum input pic x(20)
     line four  maximum input pic x(20)
     ** Note total characters should not exceed 57 **(because of 3 DELIMITERS '#')

 The answer required is:- the ADDRESS FIELD should look like:

     line one#line two#line three#line four
     123456789012345678901234567890123456789012345678901234567890>>pic x(60)

 I tried very hard to get this answer but instead I get the following:

     line one            #line two           #line three         #line four
     123456789012345678901234567890123456789012345678901234567890>>pic x(60)

     ....line four truncated...delimiters # fixed on 21 st, 41st positions.

     I tried the following:

SCREEN SECTION...

      ...04  LINE 02 COLUMN 10     VALUE 'CUSTOMER ADDRESS'.
         04          COLUMN 30     PIC X(20) USING W-ADDRESS-A.
         04  LINE 03 COLUMN 30     PIC X(20) USING W-ADDRESS-B.
         04  LINE 04 COLUMN 30     PIC X(20) USING W-ADDRESS-C.
         04  LINE 05 COLUMN 30     PIC X(20) USING W-ADDRESS-D.

PROCEDURE DIVISION...
      ...   STRING W-ADDRESS-A  '#'
                   W-ADDRESS-B  '#'
                   W-ADDRESS-C  '#'
                   W-ADDRESS-D  DELIMITED BY SPACE (also tried DELIMITED BY SIZE)
            INTO CUSTOMER-ADDRESS 

which gives CUSTOMER-ADDRESS FIELD as:
           >>line one            #line two           #line three         <<

      
        I have got some idea, it is using pic x(20) for each field inputted
eventhough it is less than pic x(20),it uses the remaining spaces or tab.

        Please help me what am I doing wrong here? 
        compiler is fujitsu v3.

Regards
M S
```

#### ↳ Re: STRING help please

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39669D21.39D1738F@home.com>`
- **References:** `<8k5qr6$9bt$1@newsg2.svr.pol.co.uk>`

```


> M S wrote:
> 
…[59 more quoted lines elided]…
> M S

I think :-

(A) the first question has to be why do you want it all in one Address
Field ? Assuming you are storing this in a file, then it would make
sense to store each line separately so that they can INDEPENDENTLY be
edited.

(B) Second, I'm no Einstein - but 4 x 20 doth not make 60. <G> You would
need to include ON OVERFLOW for eventuality the four address lines do
exceed your targeted 60 characters !

(C) If what you are trying to achieve is an 'address block' to CURRENTLY
print from the Screen data, then the STRING verb would be valid.

>          PIC X(20) USING W-ADDRESS-A.
>          PIC X(20) USING W-ADDRESS-B.
>          PIC X(20) USING W-ADDRESS-C.
>          PIC X(20) USING W-ADDRESS-D.

You really don't need those '#' markers. NOTE INITIALIZE FIRST for
safety :-

	initialize Customer-Address
	String  w-address-a 	delimited by "  " *> two spaces
		w-address-b	delimited by "  "	..
		w-address-c	delimited by "  "	..
		w-address-c	delimited by "  "	.. 
		into Customer-Address
	End-String

If you wanted the above as four lines for displaying/printing :-

	initialize Customer-Address
	String  w-address-a 	delimited by "  " *> two spaces
		x"odoa"		delimited by size
		w-address-b	delimited by "  "	..
		x"odoa"		delimited by size
		w-address-c	delimited by "  "	..
		x"odoa"		delimited by size
		w-address-c	delimited by "  "	.. 
		x"odoa"		delimited by size
		into Customer-Address
	End-String

And if you were into GUI displays, take the last example and before
'into Customer-Address' add :-

		x"00"		delimited by size

PS: Check on-line help for STRING syntax and use of hex values "od",
"oa" and "00".

Jimmy, Calgary, AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
