[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# >>>>> HELP !

_7 messages · 5 participants · 1998-10_

---

### >>>>> HELP !

- **From:** "Luc Mertes" <luc.mertes@ibsr.be>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vl6ip$7o7$1@news3.Belgium.EU.net>`

```
I know this could seem elementary to you ...

I work with a PC / Windows NT 4.0 / Fujitsu COBOL 85.

In a COBOL program, I would like to test some bytes, in order for me to
check their binary value (hexa '0D' or dec '013' for instance).
I read the bytes with a MOVE TO ELEM (with ELEM defined as 01  ELEM
PIC X)

... Then, what do I have to do to be able to read the real value of ELEM (0
to 255 Decimal) ?

Thanks to all of you !

Luc
luc.mertes@village.uunet.be
luc.mertes@ibsr.be
```

#### ↳ Re: >>>>> HELP !

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vlemb$166$1@news.igs.net>`
- **References:** `<6vl6ip$7o7$1@news3.Belgium.EU.net>`

```
COMP-5 is a 16 bit number, so the easiest way is to redefine
your base field as that, then look at it. The code would be as follows:

    01 dumy-name-one.
        02 filler                        picture x.
        02 ascii-character      picture x.
    01 dumy-name-two redefines dumy-name-one.
        02 binary-number        picture s9(5) comp-5.

    move zero to binary-number.   (make sure high order is hex zero)
    move character-data to ascii-character.
    move binary-number to numeric-value-of-character.

I think I might have the order of the filler and ascii character
in the above example reversed, I always end up doing it wrong
once and fixing it on the debug<g>, but that should get you there.
There is also an intrinsic function to do the same job. That is
in the manual under "intrinsic functions".

Luc Mertes wrote in message <6vl6ip$7o7$1@news3.Belgium.EU.net>...
>I know this could seem elementary to you ...
>
…[17 more quoted lines elided]…
>
```

##### ↳ ↳ Re: >>>>> HELP !

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rfuT1.107$ce.312564@news4.mia.bellsouth.net>`
- **References:** `<6vl6ip$7o7$1@news3.Belgium.EU.net> <6vlemb$166$1@news.igs.net>`

```
Donald Tees wrote:
>COMP-5 is a 16 bit number, so the easiest way is to redefine
>your base field as that, then look at it. The code would be as follows:
…[5 more quoted lines elided]…
>        02 binary-number        picture s9(5) comp-5.

I think you want to make that s9(4) Donald, because -99999 to -32769
and 32768 to 99999 can't be stored in 2 bytes. :-)
```

###### ↳ ↳ ↳ Re: >>>>> HELP !

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vmbmb$pu6$1@news.igs.net>`
- **References:** `<6vl6ip$7o7$1@news3.Belgium.EU.net> <6vlemb$166$1@news.igs.net> <rfuT1.107$ce.312564@news4.mia.bellsouth.net>`

```

Judson McClendon wrote in message ...
>
>I think you want to make that s9(4) Donald, because -99999 to -32769
>and 32768 to 99999 can't be stored in 2 bytes. :-)


That is correct, though from the Fujitsu docs, it appears that
comp-5 is a 16 bit regardless. Perhaps though, I am mistaken
and it is actually 32 bit.  That is the usage that they use internally
for indices, etc.  I'll test it in the morning, and get back to you.
```

#### ↳ Re: >>>>> HELP !

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981009131311.14582.00008398@ng-fa2.aol.com>`
- **References:** `<6vl6ip$7o7$1@news3.Belgium.EU.net>`

```


Luc Mertes <luc.mertes@ibsr.be>
On Fri, 9 Oct 1998 16:29:05 0200


Asked about
>>I work with a PC / Windows NT 4.0 / Fujitsu COBOL 85.

In a COBOL program, I would like to test some bytes, in order for me to
check their binary value (hexa '0D' or dec '013' for instance).
I read the bytes with a MOVE TO ELEM (with ELEM defined as 01  ELEM
PIC X)

... Then, what do I have to do to be able to read the real value of ELEM (0
to 255 Decimal) ?
<<

I can tell you how to do what you want to do then comment about what you
specifically asked.

1) Hex
COBOL 85 permits hexadecimal literals, like
X'0D' and X'0A'. (The Following examples are in ASCII, not EBCDIC).

So having populated your data item
 01  ELEM PIC X.

you can code test like

   IF ELEM = X'0D'
      PERFORM 013-CARRIAGE-RETURN
   END-IF.

or perhaps
   EVALUATE ELEM
      WHEN X'0D'
          PERFORM 013-CARRIAGE-RETURN
      WHEN X'0A'
          PERFORM 010-LINE-FEED
      WHEN X'09'
          PERFORM 009-DETAB-TEXT
      WHEN X'0B'
          PERFORM 012-FORM-FEED
      WHEN OTHER
          PERFORM 099-PROCESS-IT
    END-EVALUATE.
      
the hex literals can go into other relationals, like

* You know you cold do the following
* with a test for a blank, but just for illustration
   IF ELEM < X'20'
      PERFORM 013-SKIP-PROTOCOL-CIPHER
   ELSE
      PERFORM 099-PROCESS-IT
   END-IF.


Incidentally you can code hexadecimal literals longer than one byte.  You can
put them in VALUE clauses of data items.

Or you could do something like

    INSPECT item-bigger-than-elem-say-x256
       CONVERTING x'0A0D'
       INTO ALL SPACES.
* I am a little unsure of the above syntax.    

using a literal or a fixed data item for the CONVERTING clause or the INTO
CLAUSE.

2) Decimal

But there is noway I know of to do this with decimal literals exactly as you
have layed oout your plan, COBOL does not have an ASCII function, like some
other languages.

However, the typical recommendation is to move the cipher to the lower byte of
a binary and then test the binary item,  as in

01 WORK-GROUP. 
     05 F       PIC X.
     05 ELEM PIC X.
01 ASCII-GROUP REDEFINES 
     WORK-GROUP. 
     05 ELEM-ASCII PIC S9(4) BINARY.

 
 PROCEDURE DIVISION.
* initialize it atleast once in procedure div,
* or initialize it repeatedly in a loop,
* or transpose the redefintion above, and 
*    init it in WS.
    INTIALIZE ELEM-ASCII.

    PERFORM LOOP-LOGIC
      VARYING NNN....
.......


 LOOP-LOGIC.
    MOVE SOURCE-DATA(NNN:1)
        to ELEM.
   IF ELEM-ASCII = 13
      PERFORM 013-CARRIAGE-RETURN
   END-IF.
   
or
   EVALUATE ELEM-ASCII
      WHEN 13
          PERFORM 013-CARRIAGE-RETURN
      WHEN 010
          PERFORM 010-LINE-FEED
      WHEN OTHER
          PERFORM 099-PROCESS-IT
    END-EVALUATE.
or

* note value and relational operator varied
* from earlier example just for fun
* but should have same effect
   IF ELEM-ASCII <= 31 
     PERFORM 013-SKIP-PROTOCOL-CIPHER
   ELSE
      PERFORM 099-PROCESS-IT
   END-IF.


Best Wishes,




Robert Rayhawk
RKRayhawk@aol.com
```

##### ↳ ↳ Re: >>>>> HELP !

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uuzT1.640$q3.4810597@news1.atlantic.net>`
- **References:** `<6vl6ip$7o7$1@news3.Belgium.EU.net> <19981009131311.14582.00008398@ng-fa2.aol.com>`

```

RKRayhawk wrote in message <19981009131311.14582.00008398@ng-fa2.aol.com>...
>
>But there is noway I know of to do this with decimal literals exactly as
you
>have layed oout your plan, COBOL does not have an ASCII function, like some
>other languages.
>

Actually, it does! Use the ORD intrinsic function. As in,

    01 ELEM PIC X.
    01 REAL-VALUE PIC 999.

    COMPUTE REAL-VALUE = FUNCTION ORD ( ELEM ) - 1

The adjustment of -1 is required to match the ordinal value of the character
(within the COBOL character set) to its numeric value. The complementary
intrinsic function is CHAR. As in,

    01 ELEM PIC X.
    01 DECIMAL-VALUE PIC 999.

    MOVE FUNCTION CHAR ( DECIMAL-VALUE + 1 ) TO ELEM.

The adjustment of +1 is required to map the numeric value to the position
within the character set.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: >>>>> HELP !

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ueFT1.232$ce.601478@news4.mia.bellsouth.net>`
- **References:** `<6vl6ip$7o7$1@news3.Belgium.EU.net> <19981009131311.14582.00008398@ng-fa2.aol.com> <uuzT1.640$q3.4810597@news1.atlantic.net>`

```
Rick Smith wrote:
>
>RKRayhawk wrote:
…[24 more quoted lines elided]…
>within the character set.

Rick, that is a clever approach which should work for standard COBOL.
However, I would expect FUNCTION ORD to be affected by the ALPHABET
clause in the SPECIAL-NAMES paragraph of the CONFIGURATION SECTION.
The FUNCTION ORD description in the Intrinsic Function Module standard
refers to the collating sequence 'for the program' not 'for the system'.
This might be a problem for applications using ALPHABET.  Probably a
small number of programs, but a potential 'Oops!' to remember. :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
