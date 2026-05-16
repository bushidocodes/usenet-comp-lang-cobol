[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# GETMAIN ACROSS LINKAGE IN COBOL

_5 messages · 5 participants · 2000-05_

---

### GETMAIN ACROSS LINKAGE IN COBOL

- **From:** kittu234@my-deja.com
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g07sn$d2e$1@nnrp1.deja.com>`

```
What happens when i have a field like this

PROGRAM1.

01 field-1   PIC  X(1000000).


i GETMAIN  1000 bytes for the field-1 in this program and pass it
across linkage to program-2




program-2


inside of program-2 i do a FREEMAIN on this field and i do a getmain
again say with 2000 bytes this time.

at
GOBACK in program2 will program-1 get back the 2000 bytes ??

or will it lose addressability to field-1 as program-2 has FREEMAINed

it??

**

Question-2

what happens when this field is used with COBOL  verbs like

INITIALIZE , INSPECT ??

will I get a S0C-4  ??

krishna.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: GETMAIN ACROSS LINKAGE IN COBOL

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ng7isc9bi91m5uhl905h05032sg8dus20@4ax.com>`
- **References:** `<8g07sn$d2e$1@nnrp1.deja.com>`

```
On Thu, 18 May 2000 07:59:27 GMT, kittu234@my-deja.com wrote:

>What happens when i have a field like this
>
…[18 more quoted lines elided]…
>GOBACK in program2 will program-1 get back the 2000 bytes ??

No
>
>or will it lose addressability to field-1 as program-2 has FREEMAINed
>
>it??
>
No, it is worse.  Program-1 still has addressability to the previous area, even though it
is freemained.  Actually, it may now be GETMAIN for some other area used by this task, and
program-1 might now destroy some of its own controlblocks etc
>**
>
…[7 more quoted lines elided]…
>
Most probably, yes.




     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



         Strike while the iron is hot.
```

#### ↳ Re: GETMAIN ACROSS LINKAGE IN COBOL

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7YQU4.565$pE3.17541@dfiatx1-snr1.gtei.net>`
- **References:** `<8g07sn$d2e$1@nnrp1.deja.com>`

```
Same question, different values, you asked in another thread...but

<kittu234@my-deja.com> wrote in message news:8g07sn$d2e$1@nnrp1.deja.com...
> [Second]  Question-2
>
…[5 more quoted lines elided]…
>

In the other thread, someone suggested you pass an item of USAGE POINTER to
GETMAIN. Once you have the pointer, you can SET ADDRESS OF (item in linkage
section to which you do have addressability) TO (valid pointer obtained by
GETMAIN) and use COBOL verbs on that item.

(I think).

But of course, then why bother with GETMAIN, as COBOL will allocate the
space for the COBOL dataname? Well, if you were trying to create a large
table of  items, you could work on them one at a time in COBOL defining only
one element in LINKAGE, SET ADDRESS as above, then SET ADDRESS OF (this
item) UP BY FUNCTION LENGTH(this item) to "walk the table."

(Also a guess).

Probably worth a try?

I don't know squat about how this stuff might work/not work under CICS,
which I have gathered uses some of its own rules for allocations and
addressing, but this might be worth tinkering with.

(Doesn't CICS have its own callable functions for allocations?)

MCM
```

#### ↳ Re: GETMAIN ACROSS LINKAGE IN COBOL

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g2k1i$sjr$1@sshuraaa-i-1.production.compuserve.com>`
- **References:** `<8g07sn$d2e$1@nnrp1.deja.com>`

```
    One of my pet peeves.  Initialize can NOT be used with a
variable length (ODO) array.
Not certain  about inspect.

    You would need to pass the pointer if you expect try this.
Even so, I am
not sure what would happen when you cancel program-2.  Some
cobol's
would automatically free the memory.

<kittu234@my-deja.com> wrote in message
news:8g07sn$d2e$1@nnrp1.deja.com...
> What happens when i have a field like this
>
…[5 more quoted lines elided]…
> i GETMAIN  1000 bytes for the field-1 in this program and pass
it
> across linkage to program-2
>
…[6 more quoted lines elided]…
> inside of program-2 i do a FREEMAIN on this field and i do a
getmain
> again say with 2000 bytes this time.
>
…[3 more quoted lines elided]…
> or will it lose addressability to field-1 as program-2 has
FREEMAINed
>
> it??
…[15 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: GETMAIN ACROSS LINKAGE IN COBOL

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gturc$i0b$1@nntp9.atl.mindspring.net>`
- **References:** `<8g07sn$d2e$1@nnrp1.deja.com> <8g2k1i$sjr$1@sshuraaa-i-1.production.compuserve.com>`

```
FYI,
  The rule on INITIALIZE and ODO's is "fixed" in the next Standard.  You
might want to do a "requirement" (enhancement request) to your vendor of
choice to fix this NOW.  FYI, many vendors do already support this (as an
extension).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
