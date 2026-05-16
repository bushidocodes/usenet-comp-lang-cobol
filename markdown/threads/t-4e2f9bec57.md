[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help on MF PCW

_10 messages · 6 participants · 1999-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help on MF PCW

- **From:** "zenster" <zenster@zenxsite.net>
- **Date:** 1999-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e1ti3.789$J71.41779@monger.newsread.com>`

```
Somehow I can't seem to execute through this simple move.  This same program
passed with flying colors on my school's MVS mainframe.

It compiled fine on Personal Cobol yet gets jammed only at this move
statement at execution (runtime 163).  Here are some pertinent lines:

01  IN-REC.
      05 NUM-IN            PIC X(4).
      05 NAME-IN          PIC X(10).
      05                            PIC X.
      05 PREV-BAL-IN   PIC 9(3)V99.
      05                            PIC X.
      05 CHARGES-IN OCCURS 10 TIMES  PIC 9(5).

01  OUT-REC.
       05                           PIC X(2).
       05 NAME-OUT     PIC X(10).
       05                           PIC X(2).
       05 NUM-OUT       PIC X(4).
       05                           PIC X(2).
       05 TOT-CHRG-OUT     PIC $$$,$$$.99.
       05                           PIC X(2).
       05 PREV-BAL-OUT     PIC $$$$.99.
--------
100-BEGIN.
           INITIALIZE OUT-REC.
200-LOOP.
       MOVE NAME-IN TO NAME-OUT.
       MOVE NUM-IN TO NUM-OUT.
>err MOVE PREV-BAL-IN TO PREV-BAL-OUT.    >>>  ERROR!!!!!<<<

Pretty straight forward right?  There has to be something I'm missing.  If
someone has any insight I'd be much obliged.

thanks
```

#### ↳ Re: Help on MF PCW

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LNvi3.617$TJ4.32841@dfiatx1-snr1.gtei.net>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com>`

```
If PREV-BAL-IN is not initialized to ZERO or some other value, its contents
are undefined, and may result in the illegal MOVE.
```

##### ↳ ↳ Re: Help on MF PCW

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7me24e$fbu@dfw-ixnews7.ix.netcom.com>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com> <LNvi3.617$TJ4.32841@dfiatx1-snr1.gtei.net>`

```
You may want to add

INITIALIZE IN-REC

in addition to

INITIALIZE OUT-REC

(or you might need to "validate" the data in IN-REC if it is coming to you
in a file or other input medium)
```

#### ↳ Re: Help on MF PCW

- **From:** "Roque Bruno" <roque69@earthlink.net>
- **Date:** 1999-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mjetg$mc$1@ash.prod.itd.earthlink.net>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com>`

```
dont used INITIALIZE ....
INITIALIZE command only applicable to PIC X and PIC 9
when you try to initialized a numeric-edited field or comp or comp-3..etc...
it will give you nothing in compile time, but it will gives you a
unpredictable
message in runtime.


zenster <zenster@zenxsite.net> wrote in message
news:e1ti3.789$J71.41779@monger.newsread.com...
> Somehow I can't seem to execute through this simple move.  This same
program
> passed with flying colors on my school's MVS mainframe.
>
…[45 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Help on MF PCW

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mjhm5$5gh@dfw-ixnews7.ix.netcom.com>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com> <7mjetg$mc$1@ash.prod.itd.earthlink.net>`

```
Roque Bruno <roque69@earthlink.net> wrote in message
news:7mjetg$mc$1@ash.prod.itd.earthlink.net...
> dont used INITIALIZE ....
> INITIALIZE command only applicable to PIC X and PIC 9
> when you try to initialized a numeric-edited field or comp or
comp-3..etc...
> it will give you nothing in compile time, but it will gives you a
> unpredictable
> message in runtime.
>
>

I don't know what makes you say this - it isn't true.  If you use INITIALIZE
record-name (with no other phrases) it will initialize *all* numeric fields
to their "correct" zero values (with or without signs, with or without
packing, etc).

If you have a compiler that doesn't work that way - it has a BUG.

FYI,
   There are methods of using the INITIALIZE verb to get values other than
spaces or zeroes - but the simplest format of the verb is what people
USUALLY want.
```

###### ↳ ↳ ↳ Re: Help on MF PCW

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uZUY7Tqz#GA.364@nih2naad.prod2.compuserve.com>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com> <7mjetg$mc$1@ash.prod.itd.earthlink.net> <7mjhm5$5gh@dfw-ixnews7.ix.netcom.com>`

```
        I have found that the DOS 16bit MF compiler is hopelessly
naive with INITIALIZE.  Judging from the program size, it seems to generate
a move for each item in the group.  In addition, it can be slow when
running INT code, if the group contains a LOT of items.  I have had better
luck with a move spaces followed by initialize xxx replacing numeric by
zero.

    This generates move ONLY for numeric items.  If most of the
group are pic X, this can save a lot.  Of course, if the group is mostly
numeric, do not bother.



>FYI,
>   There are methods of using the INITIALIZE verb to get values other than
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help on MF PCW

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mkpfs$nra@dfw-ixnews3.ix.netcom.com>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com> <7mjetg$mc$1@ash.prod.itd.earthlink.net> <7mjhm5$5gh@dfw-ixnews7.ix.netcom.com> <uZUY7Tqz#GA.364@nih2naad.prod2.compuserve.com>`

```
Russell Styles <RWSTYLES@COMPUSERVE.COM> wrote in message
news:uZUY7Tqz#GA.364@nih2naad.prod2.compuserve.com...
>         I have found that the DOS 16bit MF compiler is hopelessly
> naive with INITIALIZE.  Judging from the program size, it seems to
generate
> a move for each item in the group.  In addition, it can be slow when
> running INT code, if the group contains a LOT of items.  I have had better
…[7 more quoted lines elided]…
>

The 16-bit MF product is fairly old now. l think (but am not positive) that
more recent Micro Focus products *do* optimize the INITIALIZE verb.
However, this may well (again) be a case of comparing run-time performance
vs "maintainability".

In most (not all) cases, you use the INITIALIZE verb once per record (in the
entire program - not per loop).  Therefore, a little run-time performance
degradation is rarely significant in the entire program's run-time.  On the
other hand, having to do explicit MOVEs of ZERO to each of the numeric
sub-fields (elementary items) means that you need to REMEMBER to update this
when you add additional fields.   I am not saying that you shouldn't
consider the performance ramifications of this verb, but I do think that you
need to consider all the ramifications PRO and CON before dismissing it in
general.
```

###### ↳ ↳ ↳ Re: Help on MF PCW

_(reply depth: 5)_

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eaao1tuz#GA.306@nih2naaa.prod2.compuserve.com>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com> <7mjetg$mc$1@ash.prod.itd.earthlink.net> <7mjhm5$5gh@dfw-ixnews7.ix.netcom.com> <uZUY7Tqz#GA.364@nih2naad.prod2.compuserve.com> <7mkpfs$nra@dfw-ixnews3.ix.netcom.com>`

```

William M. Klein wrote in message <7mkpfs$nra@dfw-ixnews3.ix.netcom.com>...
>Russell Styles <RWSTYLES@COMPUSERVE.COM> wrote in message
>news:uZUY7Tqz#GA.364@nih2naad.prod2.compuserve.com...
…[4 more quoted lines elided]…
>> running INT code, if the group contains a LOT of items.  I have had
better
>> luck with a move spaces followed by initialize xxx replacing numeric by
>> zero.
…[12 more quoted lines elided]…
>In most (not all) cases, you use the INITIALIZE verb once per record (in
the
>entire program - not per loop).  Therefore, a little run-time performance
>degradation is rarely significant in the entire program's run-time.  On the
>other hand, having to do explicit MOVEs of ZERO to each of the numeric
>sub-fields (elementary items) means that you need to REMEMBER to update
this
>when you add additional fields.   I am not saying that you shouldn't
>consider the performance ramifications of this verb, but I do think that
you
>need to consider all the ramifications PRO and CON before dismissing it in
>general.
…[6 more quoted lines elided]…
>
    All true.  But when I complained about performance, I was referring to
an "int'd" program when initializing a "large" (will the gentlemen with the
14 Meg array stop laughing please) of 20,000-30,000 numbers in a multi
level array.  And the comment about having a move spaces for each pic x
item is of course a guess (although I could view generated assembler if I
wanted).

    Also many performance issues are much harder to notice now
that we have such fast pc's.  A code segment that took 1/2 second on a 33M
386
is not noticeable on a 400M pentium.

    I agree that doing a manual initialize is out of the guestion, unless
you get lucky
with a move low-values.  That can work with binary (MF COMP or COMP-X or
COMP-5)
data items.

    My orginal complaint concerned group items with a significant number of
pic x fields,
where the naive behavior of INITIALIZE was too glaring.
```

###### ↳ ↳ ↳ Re: Help on MF PCW

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ml8mo$r9r@dfw-ixnews13.ix.netcom.com>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com> <7mjetg$mc$1@ash.prod.itd.earthlink.net> <7mjhm5$5gh@dfw-ixnews7.ix.netcom.com> <uZUY7Tqz#GA.364@nih2naad.prod2.compuserve.com> <7mkpfs$nra@dfw-ixnews3.ix.netcom.com> <eaao1tuz#GA.306@nih2naaa.prod2.compuserve.com>`

```
If you check out DejaNews (or whatever it is called this week), you will see
that over the last year or so (that I know of) there have been performance
discussions about INITIALIZE, STRING, UNSTRING, and almost every COBOL verb
more complicated than CONTINUE :-)

When members of the NG have tried, they have been able to "hand-code" more
efficient versions of EVERY individual task that they took on - on every
platform - with every compiler - when they tried.   In general (semi-gross
generalization), any programmer SHOULD be able to code a "task-specific"
piece of logic that is more efficient than a "generalized" COBOL verb.
HOWEVER, this still doesn't mean that the better performing piece of logic
is the "best" solution.  On the other hand,  cases like yours (where a
"simple" MOVE SPACES to record-name - followed by an INITIALIZE record-name
REPLACING NUMERIC by ZEROES) shows significant performance differences
*does* provide an excellent opportunity for a "paying customer" to ask the
vendor to "improve" their optimization.
```

###### ↳ ↳ ↳ Re: Help on MF PCW

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378DE18F.C392AD5@NOSPAMhome.com>`
- **References:** `<e1ti3.789$J71.41779@monger.newsread.com> <7mjetg$mc$1@ash.prod.itd.earthlink.net> <7mjhm5$5gh@dfw-ixnews7.ix.netcom.com>`

```
William M. Klein wrote:

> I don't know what makes you say this - it isn't true.  If you use INITIALIZE
> record-name (with no other phrases) it will initialize *all* numeric fields
> to their "correct" zero values (with or without signs, with or without
> packing, etc).

Unfortunately, it isn't obvious to somone not in the know what their
"correct" values are.  To me, ANSI defined this verb in a
less-than-useful manner.  Fortunately, in the future we will be able to
replace the naked INITIALIZE command with one more useful.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
