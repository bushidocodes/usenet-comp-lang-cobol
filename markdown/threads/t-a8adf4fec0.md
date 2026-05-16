[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# open vendor question

_17 messages · 7 participants · 2000-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### open vendor question

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3986CAF4.1CC673EB@zip.com.au>`

```

I have been working out how to implement a generic feature in Cobol
for handling various length strings without many code changes.

I understand that there is a "PIC X ANY" feature in linkage section
for the standard.

Can the major vendors indicate when they intend to support this
feature.  If so when?

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

PS:  The definition of a major vendor is up to you.  If you think you
are small then you probably are!
```

#### ↳ Re: open vendor question

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3986fac3.14835615@207.126.101.100>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au>`

```
On Tue, 01 Aug 2000 23:04:52 +1000, Ken Foskey <waratah@zip.com.au>
wrote:


>Can the major vendors indicate when they intend to support this
>feature.  If so when?
>

Fujitsu does with v5.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: open vendor question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8m785i$ndu$1@slb1.atl.mindspring.net>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au>`

```
From one of my "usually reliable" sources at MERANT, (concerning Net Express)

"I'm allowed to give an <UN>official position... (well my view as I see
it)...

This feature in my opinion would require runtime and generator changes and
is not isolated to our checker technology so is not on the cards in the
short term. Any implementation would have be part of our strategy for
implementing the whole ISO200x standard."
```

#### ↳ Re: open vendor question

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39875efa.33009776@nntp.sprynet.com>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au>`

```
On Tue, 01 Aug 2000 23:04:52 +1000, Ken Foskey <waratah@zip.com.au>
wrote:

>
>I have been working out how to implement a generic feature in Cobol
…[6 more quoted lines elided]…
>feature.  If so when?

Give me an example of how you would use this, because I think you can
do something similar without this feature.  (Or not -- but I'll let
you give the example before I make a fool of myself.)

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

##### ↳ ↳ Re: open vendor question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8m7s7v$q0a$1@nntp9.atl.mindspring.net>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com>`

```
To use this feature (in a function or method - I am not certain if it is or
is not in the current draft for called subprograms) what you code is:

Linkage Section.
01 SomeParm Pic X Any Length.
Procedure Division Using SomeParm.
   ...

The length of SomeParm is determined by the "run-time" system.  It is *not*
required that the invoking program (or program using this reference) "fill
in" any field with the length of this particular SomeParm. It is also
perfectly legal for "SomeParm" to have different lengths each time the
function/method is invoked.

Does this help explain how it is used?
```

###### ↳ ↳ ↳ Re: open vendor question

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3988d2a1.9303676@nntp.sprynet.com>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net>`

```
On Tue, 1 Aug 2000 20:07:41 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>To use this feature (in a function or method - I am not certain if it is or
>is not in the current draft for called subprograms) what you code is:
…[12 more quoted lines elided]…
>Does this help explain how it is used?

So are you saying that at this point if you used FUNCTION
LENGTH(SomeParm) it would return the actual length?  I guess all I'm
saying is that, even right now, you can define a linkage a linkage 01
level as PIC X but you can still reference past just one byte by using
reference modification or whatever.  Of course you'd have to pass the
length as a second 01 level or have some other way of determining it,
so if PIC X ANY gets past that it would be great.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mala2$c8a$1@slb1.atl.mindspring.net>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com>`

```
Yes,
  I am saying that if you use Function LENGTH  - that you will get the "real"
length of the passed item.

No,
  You may not *LEGALLY* define any Linkage Section items as PIC X - and then
address any amount  of storage that you want.  Although this WORKS some
(most?) of the time, the results are explicitly undefined.  What is more,
there are (historical) examples of where using this "undefined" situation
causes problems.  Just ask any IBM CICS programmer who accidentally tried to
address beyond a 4K boundary with older IBM COBOL products.

Furthermore, with "conformance" checking that will be introduced with the
next Standard - this may even cause a compile-time error - if the lengths of
your passed and received items don't match.
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 5)_

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<398a0c05.22019712@nntp.sprynet.com>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com> <8mala2$c8a$1@slb1.atl.mindspring.net>`

```
On Wed, 2 Aug 2000 21:27:41 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>Yes,
>  I am saying that if you use Function LENGTH  - that you will get the "real"
…[12 more quoted lines elided]…
>your passed and received items don't match.

OK, here's my thing....   Take the following code,

ID DIVISION.
PROGRAM-ID.  NUMTEST.

WORKING-STORAGE SECTION.
01  MY-MESSAGE                           PIC X(10) VALUE '1234567A''.
01  MY-RESULT                               PIC X.

PROCEDURE DIVISION.
    CALL 'CHKNUMR' USING 
                                    BY MY-MESSAGE
                                    BY CONTENT LENGTH OF MY-MESSAGE
                                    BY REFERENCE MY-RESULT
     IF MY-RESULT = 'Y' 
         DISPLAY 'MY-MESSAGE HAS NUMERICS'
     ELSE
         DISPLAY 'MY-MESSAGE HAS NO NUMERICS'
     END-IF
     GOBACK.

ID DIVISION.
PROGRAM-ID. CHMNUMR.

WORKING-STORAGE SECTION.
     01  SUB                                           PIC S9(9) COMP.

LINKAGE SECTION.
     01  SCAN-AREA                                 PIC X(80).
     01  SCAN-SIZE                                    PIC S9(9) COMP.
     01  SCAN-RESULT                            PIC X..
PROCEDURE DIVISION USING SCAN-AREA

SCAN-SIZE

SCAN-RESULT.
     MOVE 'N'  TO  SCAN-RESULT
     PERFORM VARYING SUB FROM 1 BY 1
                                 UNTIL SUB > SCAN-SIZE
                                       OR SCAN-RESULT = 'Y'
          IF SCAN-AREA (SUB:1) NUMERIC
              MOVE 'Y'  TO  SCAN-RESULT
          END-IF
     END-PERFORM.

     EXIT PROGRAM.
END-PROGRAM CHMNUMR.
END-PROGRAM. NUMTEST.

First of all, yes I realize you could simply check MY-MESSAGE for
NUMERIC.  This is only an example!  :-)

In any case, here I defined SCAN-AREA as PIC X(80).  But does it
really matter what size I define it as?  It's only a pointer to the
working-storage in the calling program.  As long as SCAN-SIZE is set
properly it doesn't matter what size SCAN-AREA is defined as.  I'm not
assember expert, but I'm fairly certain this is done all the time in
assember.

Now as for conformance checking, yeah I bet that would be caught at
compile time.  And certainly having a PIC X ANY would be beneficial,
there's no denying that.  But why pretend we can't do something now
when we really can?

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8md4v5$mi0$1@slb6.atl.mindspring.net>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com> <8mala2$c8a$1@slb1.atl.mindspring.net> <398a0c05.22019712@nntp.sprynet.com>`

```
Again, this example PROBABLY will work on MOST systems with MOST compilers -
but it still isn't supported.

Try accessing a 64K item in the linkage section of a subprogram - when you
have only defined it as 1K.  This may WELL cause you problems (in some
operating systems).

The point is that COBOL behavior is only defined to the extent that the
CALLing and CALLed program define the parameters the same (or smaller in the
CALLed program).
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 7)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65rkos0nq7mtrr55obue2i1sfrv9so12e3@4ax.com>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com> <8mala2$c8a$1@slb1.atl.mindspring.net> <398a0c05.22019712@nntp.sprynet.com> <8md4v5$mi0$1@slb6.atl.mindspring.net>`

```
On Thu, 3 Aug 2000 20:07:31 -0500, "William M. Klein" <wmklein@nospam.ix.netcom.com>
wrote:

>Again, this example PROBABLY will work on MOST systems with MOST compilers -
>but it still isn't supported.
…[7 more quoted lines elided]…
>CALLed program).
Making a small change in Frank program should take care of this

ID DIVISION.
PROGRAM-ID.  NUMTEST.
<snipped>

ID DIVISION.
PROGRAM-ID. CHMNUMR.

WORKING-STORAGE SECTION.
     01  SUB                                           PIC S9(9) COMP.

LINKAGE SECTION.
     01  SCAN-AREA.
         02 Scan-area-char                            PIC X
                        OCCURS 1 TO max-number-allowed-by-compiler
                        DEPENDING ON SCAN-SIZE.
     01  SCAN-SIZE                                    PIC S9(9) COMP.
     01  SCAN-RESULT                            PIC X..
PROCEDURE DIVISION USING SCAN-AREA
<snipped>

Then the called program has legally access to all the data it has been passed by the
caller.  



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      I'm still chasing girls.  I don't remember what for, but I'm still chasing them.  - Joe E. Lewis
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 8)_

- **From:** infocat@sprynet.com (Frank Swarbrick)
- **Date:** 2000-08-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<398b6069.43340700@nntp.sprynet.com>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com> <8mala2$c8a$1@slb1.atl.mindspring.net> <398a0c05.22019712@nntp.sprynet.com> <8md4v5$mi0$1@slb6.atl.mindspring.net> <65rkos0nq7mtrr55obue2i1sfrv9so12e3@4ax.com>`

```
On Fri, 04 Aug 2000 09:15:37 +0200, Volker Bandke
<vbandke@bsp-gmbh.com> wrote:

>On Thu, 3 Aug 2000 20:07:31 -0500, "William M. Klein" <wmklein@nospam.ix.netcom.com>
>wrote:
…[34 more quoted lines elided]…
>caller.  

Now there is an excellant idea!  I'll have to try that out.

Frank Swarbrick
home: infocat@sprynet.com / work: frank.swarbrick@efirstbank.com
"I'm very seldom naughty." --Willow Rosenberg "Buffy the Vampire Slayer"
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39891292.95FC253B@home.com>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com>`

```


Frank Swarbrick wrote:
> 
> On Tue, 1 Aug 2000 20:07:41 -0500, "William M. Klein"
…[19 more quoted lines elided]…
> LENGTH(SomeParm) it would return the actual length? 

Frank,

It all depends upon what you mean by 'actual'. Wont bother to post here,
but because of this topic I already had tried it in NetExpress. Given a
field of length pic x(80, stuff it with what you like, including x'00'
positioned somewhere - Function Length ALWAYS returns 80.

> I guess all I'm
> saying is that, even right now, you can define a linkage a linkage 01
> level as PIC X but you can still reference past just one byte by using
> reference modification or whatever.

Right on - that's what Thane said. Ref-mod is the trick.

>  Of course you'd have to pass the
> length as a second 01 level or have some other way of determining it,
> so if PIC X ANY gets past that it would be great.

As you indicate you could have  :-

	call xyz(or invoke MyClass "xyz') using myLenth MyText

Jimmy
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mbue9$a19$1@news.cerf.net>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com> <39891292.95FC253B@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:39891292.95FC253B@home.com...
> It all depends upon what you mean by 'actual'. Wont bother to post here,
> but because of this topic I already had tried it in NetExpress. Given a
> field of length pic x(80, stuff it with what you like, including x'00'
> positioned somewhere - Function Length ALWAYS returns 80.

Well, the way I interpret the ANY LENGHT issue, the function Length actually
should return the correct size.

If I was to compare ANY LENGTH to anything in other languages, it would be
like the open arrays you have in C and Pascal. That is, an array with an
undefined length at implementation time, so, at runtime, the receiving
function will dynamically define the length.

This is not to be mixed with the more commonly known ascii 0 terminated
strings, which basically is a block of memory, that somewhere has a
terminating ascii 0. Also known as char pointers. (in C: char *) (in pascal:
PChar);

Acucobol does for instance, have functionality to provide character pointers
if one uses good will (which we do, don't we :-) ). But, their presence is
not dealt with automatically by the runtime, which would have been a real
scoop.

What Cobol needs is a datatype PCHAR, and embedded knowledge in the runtimes
that handles these differently from conventional PIC X declarations, yet
allows standard operations on them.

What I would like to see is:

    77 DYNAMIC-STRING                    USAGE CHAR POINTER.
    77 STATIC-STRING                         PIC X(100).

as such, a:
    MOVE STATIC-STRING                TO DYNAMIC-STRING

should establish the needed memory for DYNAMIC-STRING automatically and copy
all the 100 elements from STATIC-STRING to DYNAMIC-STRING.

The other way around however, say that DYNAMIC-STRING contained: "Hello
world"X"00" and we did the following:

    MOVE DYNAMIC-STRING          TO STATIC-STRING

Which should move "Hello world" to STATIC-STRING not including the
terminating ascii 0.

Cheesle
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3989B55F.68E2457E@home.com>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com> <39891292.95FC253B@home.com> <8mbue9$a19$1@news.cerf.net>`

```


Cheesle wrote:
> 
> "James J. Gavan" <jjgavan@home.com> wrote in message
…[7 more quoted lines elided]…
> should return the correct size.

Just to clarify this one :-
-------------------------------------------------------------
Program-id. TestLength.                             
Working-Storage section.                            
01 MyText                       pic x(80).          
01 LengthCount                  pic 9(02).          
Procedure Division.                                 
Initialize MyText                                   
compute LengthCount = function length(MyText)       
move "Hello World" to MyText                        
compute LengthCount = function length(MyText)       
move x"00" to MyText(12:1)                          
compute LengthCount = function length(MyText)       
compute LengthCount = function length(MyText(1:12)).
----------------------------------------------------------------------

First three tests = 80 and the last = 12 - but you knew that already.

This thread or elsewhere - Bill was ADAMANT you will get correct length
- so can he please clarify. (He's usually right <G>).

Must confess, I was disappointed first time I used function length and
got the 'max' characters. If above coding sample is correct, then it's a
pity we didn't have :-

compute LengthCount = function MaxLength(MyText)    *> = 80
compute LengthCount = function ActualLength(MyText) *> = 12

Both serve a use as a short-cut to 'manipulating'       	 .

(BTW : Not standard but can a Micro Focus/Merant user explain to me
difference between function Length and function Length-AN. I don't know
how many times I've read the on-line help, comparing both, word by word
- could it be that Length-AN would give me what I was really after = 12
and not 80 ?)

-----------------------
> 
> If I was to compare ANY LENGTH to anything in other languages, it would be
…[35 more quoted lines elided]…
> terminating ascii 0.

I take your points above. Currently this is what I'm doing :-

Class - EditCustomer
--------------------
method-id "do-some-stuff"
*>------------------------

  move length of CUSTOMER-name to Mylength   *> Non-standard but I think
					     *> Bill said it wil be in
					     *> COBOL 200X - otherwise:-
  compute MyLength = function length(CUSTOMER-name)

  invoke os-MyDialog "set-up-field" using MyLenth
					  CUSTOMER-name

Class : MyDialog
*>----------------
method-id. "set-up-field".
*>-----------------------
Linkage seciton.
01 lnk-length		pic x(4) comp-5. *> could be 9(03).
01 lnk-Text.
   05  pic x occurs 1 to x depending on lnk-Length.
Procedure Division using lnk-length lnk-Text.
	etc.... do "funnies" to turn into displayable object

----------------------------------------------------------------------

Jimmy
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8mcgmc$err$1@slb7.atl.mindspring.net>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com> <39891292.95FC253B@home.com> <8mbue9$a19$1@news.cerf.net> <3989B55F.68E2457E@home.com>`

```
Bill is (was) adamant that you get the "correct" length *if* you use the ANY
LENGTH for a data item - and it is defined in Linkage Section (the only place
that ANY LENGTH is valid).

FYI,
  The difference between LENGTH and LENGTH-AN (or BYTE-LENGTH in the draft
Standard) ONLY shows up if you have DBCS (MOCS or National) data.

LENGTH returns the number of characters. Therefore, if you have
    05 Nat  Pic NN.

FUNCTION LENGTH (Nat) will return a value of "2" because Nat is two NATIONAL
characters long.

However, Function Byte-Length (NAT) or
                 Function Length-AN (Nat)

will return a value of *4* - if you are in a system that uses 2 bytes for
each national character.
```

###### ↳ ↳ ↳ Re: open vendor question

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-08-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<398AA050.A9C1A204@zip.com.au>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au> <39875efa.33009776@nntp.sprynet.com> <8m7s7v$q0a$1@nntp9.atl.mindspring.net> <3988d2a1.9303676@nntp.sprynet.com> <39891292.95FC253B@home.com> <8mbue9$a19$1@news.cerf.net> <3989B55F.68E2457E@home.com>`

```
"James J. Gavan" wrote:

> Just to clarify this one :-
> -------------------------------------------------------------
…[32 more quoted lines elided]…
> and not 80 ?)

The length should always be 80.  Low values is only special for C
programming,  hex 00 is just another byte.

The difference with pic x 'any' is only on linkage.  When a string is
passed to the calling routine the size is magically passed.

If I pass PIC x(12) to a routine using 'pic x any' then the function
length in the routine will (should) return 12.

If I pass PIC x(80) to the same routine then the function length in
the routine will (should) return 80.

This is my understanding of the feature and exactly what I need.

An extension to this is if I pass a value "using  'some text'."  I
would expect function length to return 9.

I strongly disagree with cobol following the C route of ending a
string with a Null.   There are some advantages but it is actually
against what I perceive as the general thread of the language, fix
length fields are easy in cobol hard in C.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

#### ↳ Re: open vendor question

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-08-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8md52b$nmu$1@slb0.atl.mindspring.net>`
- **References:** `<3986CAF4.1CC673EB@zip.com.au>`

```
From one of my "usually reliable sources,"

"Bill,

IBM has no plans for the near future to support PIC X ANY, at least on
INTEL/AIX/390 platforms."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
