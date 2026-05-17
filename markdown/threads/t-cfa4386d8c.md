[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Linkage strangeness

_8 messages · 6 participants · 1997-02_

---

### Linkage strangeness

- **From:** "patrick herring" <ua-author-6588874@usenetarchives.gap>
- **Date:** 1997-02-24T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33137449.7619@rlsclare.agw.bt.co.uk>`

```

Just discovered a compiler 'bug' in VS COBOL II...



Has anyone else used Linkage Section areas in a top-level program? If

you USING (so to speak) the 01 on the PROCEDURE DIVISION header then it

gets addressability, else it doesn't. This 'feature' is implied by the

manual (p150) more or less, and has always worked for me til now. You

need to use only Linkage areas in SET ADDRESS which is something I'm

trying to understand in my spare moments. However strange things happen

when you have more than 2 Linkage areas. The code:



*-----------------------------------------------------------------

LINKAGE SECTION.



01 L1 PIC X.

01 L2 PIC X.

01 L3 PIC X.

01 L4 PIC X.

01 L5 PIC X.

01 L6 PIC X.

01 L7 PIC X.

01 L8 PIC X.

01 L9 PIC X.

01 LA PIC X.

01 LB PIC X.

EJECT

*-----------------------------------------------------------------

PROCEDURE DIVISION USING L1 L2 L3 L4 L5 L6 L7 L8 L9 LA LB.



DISPLAY 'L1'; MOVE '1' TO L1

DISPLAY 'L2'; MOVE '2' TO L2

* DISPLAY 'L3'; MOVE '3' TO L3

DISPLAY 'L4'; MOVE '4' TO L4

DISPLAY 'L5'; MOVE '5' TO L5

* DISPLAY 'L6'; MOVE '6' TO L6

* DISPLAY 'L7'; MOVE '7' TO L7

* DISPLAY 'L8'; MOVE '8' TO L8

* DISPLAY 'L9'; MOVE '9' TO L9

* DISPLAY 'LA'; MOVE 'A' TO LA

* DISPLAY 'LB'; MOVE 'B' TO LB



GOBACK

.



is OK but uncomment any of L3, L6-B and you get an 0C4. Also there's

something wrong with L4 in that although I can move a value to it I get

an OC1 SETting an unUSINGd Linkage area's ADDRESS to its ADDRESS. In

short the BLL cells are stuffed beyond #2.



If the above code is in a called program every Ln is fine. Whether or
not there is a PARM on the EXEC (to provide an address) makes no
difference (and if it did it's only one 01 - where's BLL 2 coming
from?). So I'm wondering whether I'm using a non-feature. Anyone know
whether I

can rely on BLLs 1 & 2, and/or whether there's a PTF for the rest?



yours, Patrick

________________________________________________________

Patrick Herring at work, her··.@rls··o.uk

Disclaimer: The form is BT but the essence is me.



"Occam's razor is so sharp, I bought the whole argument"
```

#### ↳ Re: Linkage strangeness

- **From:** "mi..." <ua-author-6589463@usenetarchives.gap>
- **Date:** 1997-02-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfa4386d8c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33137449.7619@rlsclare.agw.bt.co.uk>`
- **References:** `<33137449.7619@rlsclare.agw.bt.co.uk>`

```

.In article <331··.@rls··o.uk>,
.he··.@rls··o.uk says...
.>
.>Just discovered a compiler 'bug' in VS COBOL II...
.>
.>
.>
.>Has anyone else used Linkage Section areas in a top-level program? If
.>
.>you USING (so to speak) the 01 on the PROCEDURE DIVISION header then i
.>t
.>
.>gets addressability, else it doesn't. This 'feature' is implied by the
.>
.>manual (p150) more or less, and has always worked for me til now. You
.>
.>need to use only Linkage areas in SET ADDRESS which is something I'm
.>
.>trying to understand in my spare moments. However strange things happe
.>n
.>
.>when you have more than 2 Linkage areas. The code:
.>
.>
.>
.> *---------------------------------------------------------------
.>--
.>
.> LINKAGE SECTION.
.>
.>
.>
.> 01 L1 PIC X.
.>
.> 01 L2 PIC X.
.>
.> 01 L3 PIC X.
.>
.> 01 L4 PIC X.
.>
.> 01 L5 PIC X.
.>
.> 01 L6 PIC X.
.>
.> 01 L7 PIC X.
.>
.> 01 L8 PIC X.
.>
.> 01 L9 PIC X.
.>
.> 01 LA PIC X.
.>
.> 01 LB PIC X.
.>
.> EJE
.>CT
.>
.> *---------------------------------------------------------------
.>--
.>
.> PROCEDURE DIVISION USING L1 L2 L3 L4 L5 L6 L7 L8 L9 LA LB.
.>
.>
.>
.> DISPLAY 'L1'; MOVE '1' TO L1
.>
.> DISPLAY 'L2'; MOVE '2' TO L2
.>
.> * DISPLAY 'L3'; MOVE '3' TO L3
.>
.> DISPLAY 'L4'; MOVE '4' TO L4
.>
.> DISPLAY 'L5'; MOVE '5' TO L5
.>
.> * DISPLAY 'L6'; MOVE '6' TO L6
.>
.> * DISPLAY 'L7'; MOVE '7' TO L7
.>
.> * DISPLAY 'L8'; MOVE '8' TO L8
.>
.> * DISPLAY 'L9'; MOVE '9' TO L9
.>
.> * DISPLAY 'LA'; MOVE 'A' TO LA
.>
.> * DISPLAY 'LB'; MOVE 'B' TO LB
.>
.>
.>
.> GOBACK
.>
.> .
.>
.>
.>
.>is OK but uncomment any of L3, L6-B and you get an 0C4. Also there's
.>
.>something wrong with L4 in that although I can move a value to it I ge
.>t
.>
.>an OC1 SETting an unUSINGd Linkage area's ADDRESS to its ADDRESS. In
.>
.>short the BLL cells are stuffed beyond #2.
.>
.>
.>
.>If the above code is in a called program every Ln is fine. Whether or
.>not there is a PARM on the EXEC (to provide an address) makes no
.>difference (and if it did it's only one 01 - where's BLL 2 coming
.>from?). So I'm wondering whether I'm using a non-feature. Anyone know
.>whether I
.>
.>can rely on BLLs 1 & 2, and/or whether there's a PTF for the rest?
.>
.>
.>
.>yours, Patrick
.>
.>________________________________________________________
.>


I don't know about the use of multiple Linkage Sections, but when you use
a Linkage Section in the main program, you need to specify the first data
name for parm length. This indicates the length of the string passed on
the JCL's Parm=. I believe this IBM's implementation. For example:

LINKAGE SECTION

01 PARM-LENGTH PIC S9(4) COMP.
01 L1 PIC X.
01 L2 PIC X.

PROCEDURE DIVISION USING PARM-LENGTH L1 L2.


Hope this helps.

Mike Dodas
```

##### ↳ ↳ Re: Linkage strangeness

- **From:** "patrick herring" <ua-author-6588874@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfa4386d8c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cfa4386d8c-p2@usenetarchives.gap>`
- **References:** `<33137449.7619@rlsclare.agw.bt.co.uk> <gap-cfa4386d8c-p2@usenetarchives.gap>`

```

Michael Dodas wrote:
...
› I don't know about the use of multiple Linkage Sections, but when you use
› a Linkage Section in the main program, you need to specify the first data
…[9 more quoted lines elided]…
› PROCEDURE DIVISION USING PARM-LENGTH  L1 L2.

Certainly VS COBOL II on MVS doesn't do it this way. The length comes
through as the first half-word of the one-and-only Linkage 01 area. I
haven't been able to make PARM= generate more than one 01 area, probably
because I'm not meant to.

yours, Patrick
________________________________________________________
Patrick Herring at work, her··.@rls··o.uk
Disclaimer: The form is BT but the essence is me.

"Occam's razor is so sharp, I bought the whole argument"
```

##### ↳ ↳ Re: Linkage strangeness

- **From:** "kevin p corkery" <ua-author-17071571@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfa4386d8c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cfa4386d8c-p2@usenetarchives.gap>`
- **References:** `<33137449.7619@rlsclare.agw.bt.co.uk> <gap-cfa4386d8c-p2@usenetarchives.gap>`

```



Michael Dodas wrote in article
<5evp13$m.··.@tig··w.com>...
› I don't know about the use of multiple Linkage Sections, but when you use
 
› a Linkage Section in the main program, you need to specify the first data
 
› name for parm length.  This indicates the length of the string passed on 
› the JCL's Parm=.  I believe this IBM's implementation. For example:
…[8 more quoted lines elided]…
› 
Actually, the implementation is as follows....

In JCL ... // EXEC PGM=YOURPGM,PARM='SOMETHING,ELSE'

In COBOL ... LINKAGE SECTION.
01 PARM-PASSED.
03 PARM-LENGTH PIC S9(4) COMP.
03 PARM-STRING.
05 PARM-BYTE OCCURS 100 TIMES PIC X(1).
PROCEDURE DIVISION USING PARM-PASSED.
The pointer to the parm is established by a single 01 area in linkage
section. This area is preceded by a half-word binary value representing
the length of the string passed. It is up to the programmer to parse the
associated values from the string and manage its length

Multiple 01s in linakge can be used when invoked as a subroutine of other
programs and addressability is established only by expressing the list in
the associated USING statement.
```

#### ↳ Re: Linkage strangeness

- **From:** "steven hughes" <ua-author-794783@usenetarchives.gap>
- **Date:** 1997-02-24T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfa4386d8c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<33137449.7619@rlsclare.agw.bt.co.uk>`
- **References:** `<33137449.7619@rlsclare.agw.bt.co.uk>`

```

Patrick Herring wrote:
› 
› Just discovered a compiler 'bug' in VS COBOL II...
…[97 more quoted lines elided]…
› "Occam's razor is so sharp, I bought the whole argument"

Hello Patrick,
How, exactly, are you executing this program?

If you're running it via JCL (EXEC PGM=program,PARM='xxx'), you'll
need to define a signed halfword before the 01 level, as:

LINKAGE SECTION.

01 L1.
03 FILLER PIC S9(04) COMP-4.
03 L1-VALUE-FROM-PARM PIC X(nn).

What you do with multiple 01's I don't know 'cos I've never had to do
it.

When you call a module from a program, you don't need this halfword,
which backs up what you've said in your last paragraph.

Does this help?


Regards,
Steven
```

##### ↳ ↳ Re: Linkage strangeness

- **From:** "patrick herring" <ua-author-6588874@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfa4386d8c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cfa4386d8c-p5@usenetarchives.gap>`
- **References:** `<33137449.7619@rlsclare.agw.bt.co.uk> <gap-cfa4386d8c-p5@usenetarchives.gap>`

```

Steven Hughes wrote:
...
›     If you're running it via JCL (EXEC PGM=program,PARM='xxx'), you'll
› need to define a signed halfword before the 01 level, as:
…[11 more quoted lines elided]…
› which backs up what you've said in your last paragraph.

Yes I'm EXECing just like you write. But I'm not interested in the PARM
value just in getting BLL1 to get a valid address, so I don't need the
address. I'm sure it's the PARM that's doing it for BLL1 but that leaves
the question of why BLL2 is also valid. I suspect that's a side-effect
of the way IBM happens to have implemented it.

yours, Patrick
________________________________________________________
Patrick Herring at work, her··.@rls··o.uk
Disclaimer: The form is BT but the essence is me.

"Occam's razor is so sharp, I bought the whole argument"
```

#### ↳ Re: Linkage strangeness

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1997-02-26T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfa4386d8c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<33137449.7619@rlsclare.agw.bt.co.uk>`
- **References:** `<33137449.7619@rlsclare.agw.bt.co.uk>`

```

The problem with the Linkage Division and Procedure Division is that they
assume that the program was called with a
CALL 'your-program' USING L1 L2 L3 L4 L5 L6 L7 L8 L9 LA LB.
On IBM MVS and IBM VM the system in effect loads the program using a
CALL 'your-program' USING PARM-VALUE where Parm-Value is defined as follows.
01 PARM-VALUE.
05 PARM-LENGTH PIC S9999 BINARY.
05 PARM-DATA.
10 PARM-CHAR PIC X OCCURS 0 to 144 DEPENDING ON PARM-LENGTH.

Since there are no other addresses passed your program is picking up random
data for the addresses of L2 thru LB. I'm not certain why any of them work.
›  
› Patrick Herring wrote: 
…[124 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at mor··.@nbn··b.ca
```

#### ↳ Re: Linkage strangeness

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-02-28T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cfa4386d8c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<33137449.7619@rlsclare.agw.bt.co.uk>`
- **References:** `<33137449.7619@rlsclare.agw.bt.co.uk>`

```

In article <331··.@rls··o.uk>,
Patrick Herring wrote:
› 
› Has anyone else used Linkage Section areas in a top-level program?  If
…[7 more quoted lines elided]…
› If the above code is in a called program every Ln is fine.

It might help to think of each 01-level in the linkage section as a
pointer. Obviously, you have to load this pointer by some means before
you use it. If you try to use any pointer before you load it, you get
undefined behaviour. It won't necessarily abend; there's a good chance
of hitting a valid address.

How do these pointers get loaded? Well, the official method is to
specify the 01-level in a USING phrase in the PROCEDURE DIVISION header.
The caller then specifies a real area of the appropriate type in a USING
phrase in the CALL statement. This causes your pointer to be set to the
real area that was passed to you by your caller.

You can still get into mysterious trouble if your LINKAGE SECTION
description doesn't match the real area passed by the caller, or the
USING phrase expects more arguments than the caller passed, etc.

So, as you say, when you CALL your program with the appropriate real
areas, "every Ln is fine".

It was an obvious extension to let you use the mechanism that is already
there by allowing you to SET a pointer yourself. Generally, an 01-level
in the LINKAGE SECTION that does not appear in the USING phrase is
intended to be SET by you, while an 01-level that does appear in the
USING phrase is intended to be set by your caller.

Now, when you execute your program as a top-level program, it is actually
being CALLed by the operating system. Like any other caller, the real
areas that are passed you you are determined by the caller. The calling
program does not go into your LINKAGE SECTION and match it. It is up to
you to make your LINKAGE SECTION match what the caller will pass.

As it happens, your particular operating system always passes you one
parameter in LL format. If you execute the program you posted as a main
program, you have broken the promise you made to CoBOL in your USING
phrase. _None_ of the 01-levels except the first has addressability, and
whether one of those 01-level abends or not is random.

Even though your first 01-level does have addressability, it's still up
to you to make your LINKAGE SECTION match what was passed to you. For
example, if you attempt to write beyond the length pased to you in the
LL, you are asking for trouble.

If you want to use the code you posted as a main program under your
operating system, take out all but one 01-level from the USING phrase.

[Digression: Although I think it's clearer if the LINKAGE SECTION is in
the same order as the USING phrase, it doesn't have to be. You could
have all of your SETs first and then USING LB, if you wanted to, or any
other order.]

Then you have to make the 01-level match what the operating system is
passing to you, something like this:

01 PARM-LS.
05 PARM-LEN-LS PIC S9(4) COMP.
05 PARM-X-LS PIC X
OCCURS 0 TO 32767
DEPENDING ON PARM-LEN-LS.

The problem is that not all compilers accept this. It works on the
latest IBM CoBOL but I don't have an IBM CoBOL 2 to test with today. If
it doesn't work on CoBOL 2, you can use the "traditional" method, dating
back to OS/VS CoBOL, that goes something like this:

01 PARM-LS.
05 PARM-LEN-LS PIC S9(4) COMP.
05 PARM-X-LS PIC X OCCURS 1.

Then you have to code a SET ADDRESS for each of the other pointers that
you want to use, to make up for the fact that they were not loaded by a
calling program. Using SET ADDRESS is like passing a parameter to
yourself.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
