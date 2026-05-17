[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol's doing my head in again...

_6 messages · 5 participants · 1998-05_

---

### Cobol's doing my head in again...

- **From:** "patrick herring" <ua-author-6588874@usenetarchives.gap>
- **Date:** 1998-05-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35607159.16FC@bt.com>`

```

Has anybody ever seen & solved this:

000051
000052 DCOPY DISPLIST.
000053C D
000054C D01 DIS-PLIST.
000055C D 02 DIS-TYPE PIC X.
000056C D 88 DIS-VARS VALUE '1'.
000057C D 88 DIS-LISTS VALUE '3'.
000058C D 88 DIS-PAGES VALUE '2'.
000059C D 88 DIS-PTR VALUE '4'.
000060C D 02 DIS-PTR-VALUE PIC 9(8)
COMP. 000061C D 02 DIS-PTR-VALUE-DIS PIC
X(8).

==000061==> IGYDS1089-S ". " WAS INVALID. SCANNING WAS RESUMED AT THE
NEXT AREA LEVEL-NUMBER, OR THE START OF THE NEXT CLAUSE.

000062C D
000063C D

I can't find any message manuals, and I bet they'd just say 'correct the
error and re-run' anyway. The same copybook compiles fine in another
program. I've taken out a bit of whitespace for this post, so it's not
that. Maybe I'm working too hard...


________________________________________________________
Patrick Herring at work (clearly not - Ed.)
Disclaimer: The appearance is BT but the essence is me.

"Ockham's razor is so sharp, I bought the whole argument"
```

#### ↳ Re: Cobol's doing my head in again...

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1998-05-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db6e5ebb2b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35607159.16FC@bt.com>`
- **References:** `<35607159.16FC@bt.com>`

```

Patrick, I can't see any problems. Ii would suggest moving the COPY
statement to another place in Working storage and see if the error
moves with it, or a different one pops up.

Good luck,

Paul
```

#### ↳ Re: Cobol's doing my head in again...

- **From:** "len lewandowski" <ua-author-17073393@usenetarchives.gap>
- **Date:** 1998-05-17T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db6e5ebb2b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<35607159.16FC@bt.com>`
- **References:** `<35607159.16FC@bt.com>`

```

Have you tried viewing your source in hex? Sometimes strange things can
creep in.

Patrick Herring wrote:

› Has anybody ever seen & solved this:
› 
…[29 more quoted lines elided]…
› "Ockham's razor is so sharp, I bought the whole argument"
```

#### ↳ Re: Cobol's doing my head in again...

- **From:** "patrick herring" <ua-author-6588874@usenetarchives.gap>
- **Date:** 1998-05-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db6e5ebb2b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<35607159.16FC@bt.com>`
- **References:** `<35607159.16FC@bt.com>`

```

Dennis J. Minette wrote:
› 
› Looks to me like the input source had a LF/CR sequence positioned 
…[3 more quoted lines elided]…
› line breakup by some enroute internet e-mail server?)

That was just my newsreader's line-length.

Thanks for all the replies. I tried them all with no luck. However I
think I've got somewhere: the problem goes if I take out the blank line
at the end of the copybook, and reappears if I put it back in (so it's
not some funny hex char that crept in - not difficult since I'm using
KEDIT & yes I tried SET EOFOUT EOL). There's another copybook in the
same program that has a trailing blank line & the compiler fails to barf
on that. Also the first copybook is in another program, albeit in
linkage instead of ws, and it's OK in that compilation.

The compiler is MVS bog-standard VS COBOL II rel 4, which is worrying.
However, it's possible the machine's in the middle of an MVS upgrade,
also possibly a compiler upgrade (I thought I was using rel
3.something).

Anyway, thanks a lot.
________________________________________________________
Patrick Herring at work (clearly not - Ed.)
Disclaimer: The appearance is BT but the essence is me.

"Ockham's razor is so sharp, I bought the whole argument"
```

#### ↳ Re: Cobol's doing my head in again...

- **From:** "in..." <ua-author-17074430@usenetarchives.gap>
- **Date:** 1998-05-20T13:10:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db6e5ebb2b-p5@usenetarchives.gap>`
- **In-Reply-To:** `<35607159.16FC@bt.com>`
- **References:** `<35607159.16FC@bt.com>`

```

On Tue, 19 May 1998 17:02:21 -0700, supercalifragilisticexpialidocious
wrote:
› Does the version of Cobol you are using allow "COMP." or does it require
› something like "COMP-3."? I am new to Cobol, but I seem to recall that
› some Cobol compilers choke on "COMP." even if only one value is allowed
› for "COMP-n." 

COMP is usually a binary field and COMP-3 is a packed field.

I seem to recall that these two were swopped around on the old
Burroughs machines of the early eighty's.
Johan Potgieter
www.choicetraining.com
in··.@cho··g.com
```

##### ↳ ↳ Re: Cobol's doing my head in again...

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db6e5ebb2b-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-db6e5ebb2b-p5@usenetarchives.gap>`
- **References:** `<35607159.16FC@bt.com> <gap-db6e5ebb2b-p5@usenetarchives.gap>`

```

Johan Potgieter wrote:
› 
› On Tue, 19 May 1998 17:02:21 -0700, supercalifragilisticexpialidocious
…[4 more quoted lines elided]…
›› for "COMP-n."
 
› COMP is ANSI Cobol.  COMP-n is an extension.
 
› COMP is usually a binary field and COMP-3 is a packed field.
› 
› I seem to recall that these two were swopped around on the old
› Burroughs machines of the early eighty's.

COMP is the prefered numeric format for the given platform. By all
rights it *should* be the most efficient numeric format the platform
supports, but the standard doesn't require it. Burroughs had a
corporate standard for Cobol-74 which said that COMP is packed decimal
(like it is on IBM AS/400). In Unisys A Series Cobol-85, COMP is still
packed decimal, even though BINARY is a more efficient format. (There's
a compile option $BINARYCOMP to make COMP binary instead packed.)

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net             Bar··.@att··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \  
e    |\ Californians:  Vote June 2nd         Dennis PERON for Governor
Y    |/ John PINKERTON For Senator   Bill LOCKYER for Attorney General
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
