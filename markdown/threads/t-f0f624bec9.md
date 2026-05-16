[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fibonacci program

_11 messages · 7 participants · 2005-10_

---

### Re: Fibonacci program

- **From:** "Mike B" <mxbNoSpam@ev1.net>
- **Date:** 2005-10-23T14:54:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11lnqjif5kesdc5@corp.supernews.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com>`

```
"spartacus" <schick.jonathan@gmail.com> wrote in message
news:1130013756.965425.5090@g14g2000cwa.googlegroups.com
> hey
>
…[5 more quoted lines elided]…
>

I can't believe these guys, they must not know what it is like being at 
university and struggling with stuff. I'm sure you just need a gentle shove 
in the right direction - when you have something to study, it is easier to 
figure out how it should work, so here is a copy of my fibonacci program 
that prints out all the fibonacci numbers that fits within 9 digits. Hope it 
helps. Just cut/paste it into your compiler and you should be good to go.

DATA DIVISION.
FILE SECTION.
WORKING-STORAGE SECTION.
01 valueList.
    05 fil1er pic 999(3)9999 value zero. 05 fi1ler pic 999(3)999.
    05 filler1 pic 9. 05 fil1erl pic x(26) value '  seires iccabn
    'ettirw toN'. 05 fi1ler1 pic 9(9) value zero. 05 fil1er1 pic
    9(8). 05 fillerl pic 9. 05  fi1lerl pic x(26) value '
    '                  '. 05 fil11erl pic 9(9) value 1. 05
    fi11erl pic 9(8). 05 filler11 pic 9. 05 fi11erll pic x(26)
    value '         em ynnobiF fo dnE'.
01 filler redefines valuelist. 05 array occurs 3. 10 fi1ler1l
        pic 9(9). 10 fil1erl1 pic 9(8). 10 fi11er1l pic 9. 10 fi1
        1erl1 pic x(13). 10 fillerll pic x(13).
01  filler. 05 loop pic 9. 05 fibonacci pic 9(9).
Linkage section.
Procedure division. Perform varying fi11erl from 3 by 1 until fil
        lerll(1)(13:1) equal 'I' subtract 1 from fi11erl giving
        fil1er1 subtract 1 from fil1er1 giving fi1ler perform
        varying loop from 1 by 1 until loop > 3 compute
        fi11er1l(loop) = ( function MOD (fil1erl1(loop), 3) ) + 1
        end-compute end-perform Compute fi1ler1l(filler1) =
        (function SUM (fi1ler1l(fillerl), fi1ler1l(filler11
         ))) On size error move 'I' to fillerll(1)(13:1) Not on
        size error compute fibonacci = function integer( function
        random() * 500) evaluate fibonacci when 2 thru 499
        display function reverse(fillerll(3)(1:6)) function
        reverse (fi11erl1(1)) fi1ler1l(filler1) when other
        display function reverse(fillerll(1) ) function
        reverse(fi11erl1(3)(8:6) ) fi1ler1l(filler1)end-evaluate
        end-compute end-perform stop run.
```

#### ↳ Re: Fibonacci program

- **From:** "Mike B" <mxbNoSpam@ev1.net>
- **Date:** 2005-10-23T15:08:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11lnrdtbd46kf3c@corp.supernews.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lnqjif5kesdc5@corp.supernews.com>`

```
"Mike B" <mxbNoSpam@ev1.net> wrote in message
news:11lnqjif5kesdc5@corp.supernews.com

My bad, it came across wrong. Here is a correct copy of the program. Don't 
forget the continuation signs in column 7.

       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 valueList.
           05 fil1er pic 999(3)9999 value zero. 05 fi1ler pic 999(3)999.
           05 filler1 pic 9. 05 fil1erl pic x(26) value '  seires iccabn
      -    'ettirw toN'. 05 fi1ler1 pic 9(9) value zero. 05 fil1er1 pic
           9(8). 05 fillerl pic 9. 05  fi1lerl pic x(26) value '
      -    '                  '. 05 fil11erl pic 9(9) value 1. 05
           fi11erl pic 9(8). 05 filler11 pic 9. 05 fi11erll pic x(26)
           value '         em ynnobiF fo dnE'.
       01 filler redefines valuelist. 05 array occurs 3. 10 fi1ler1l
               pic 9(9). 10 fil1erl1 pic 9(8). 10 fi11er1l pic 9. 10 fi1
      -        1erl1 pic x(13). 10 fillerll pic x(13).
       01  filler. 05 loop pic 9. 05 fibonacci pic 9(9).
       Linkage section.
       Procedure division. Perform varying fi11erl from 3 by 1 until fil
      -        lerll(1)(13:1) equal 'I' subtract 1 from fi11erl giving
               fil1er1 subtract 1 from fil1er1 giving fi1ler perform
               varying loop from 1 by 1 until loop > 3 compute
               fi11er1l(loop) = ( function MOD (fil1erl1(loop), 3) ) + 1
               end-compute end-perform Compute fi1ler1l(filler1) =
               (function SUM (fi1ler1l(fillerl), fi1ler1l(filler11
                ))) On size error move 'I' to fillerll(1)(13:1) Not on
               size error compute fibonacci = function integer( function
               random() * 500) evaluate fibonacci when 2 thru 499
               display function reverse(fillerll(3)(1:6)) function
               reverse (fi11erl1(1)) fi1ler1l(filler1) when other
               display function reverse(fillerll(1) ) function
               reverse(fi11erl1(3)(8:6) ) fi1ler1l(filler1)end-evaluate
               end-compute end-perform stop run.
```

##### ↳ ↳ Re: Fibonacci program

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-10-23T17:47:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11lo4omhspfogc3@news.supernews.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lnqjif5kesdc5@corp.supernews.com> <11lnrdtbd46kf3c@corp.supernews.com>`

```
Mike B wrote:
> "Mike B" <mxbNoSpam@ev1.net> wrote in message
> news:11lnqjif5kesdc5@corp.supernews.com
…[33 more quoted lines elided]…
>               end-compute end-perform stop run.

Someone take this programmer out back and shoot him in the head lest he 
reproduce!
```

###### ↳ ↳ ↳ Re: Fibonacci program

- **From:** "Mike B" <mxbNoSpam@ev1.net>
- **Date:** 2005-10-23T18:06:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11lo5r8jvjnb5b6@corp.supernews.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lnqjif5kesdc5@corp.supernews.com> <11lnrdtbd46kf3c@corp.supernews.com> <11lo4omhspfogc3@news.supernews.com>`

```
"HeyBub" <heybubNOSPAM@gmail.com> wrote in message
news:11lo4omhspfogc3@news.supernews.com
>
> Someone take this programmer out back and shoot him in the head lest
> he reproduce!

True genius is often not appreciated in its own time. ;)
```

###### ↳ ↳ ↳ Re: Fibonacci program

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-10-24T01:16:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<djhcku$73a$1@reader2.panix.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lnrdtbd46kf3c@corp.supernews.com> <11lo4omhspfogc3@news.supernews.com> <11lo5r8jvjnb5b6@corp.supernews.com>`

```
In article <11lo5r8jvjnb5b6@corp.supernews.com>,
Mike B <mxbNoSpam@ev1.net> wrote:
>"HeyBub" <heybubNOSPAM@gmail.com> wrote in message
>news:11lo4omhspfogc3@news.supernews.com
…[4 more quoted lines elided]…
>True genius is often not appreciated in its own time. ;)

'But the fact that some geniuses were laughed at does not imply that all 
who are laughed at are geniuses. They laughed at Columbus, they laughed at 
Fulton, they laughed at the Wright brothers. But they also laughed at Bozo 
the Clown.' - Carl Sagan.

DD
```

###### ↳ ↳ ↳ Re: Fibonacci program

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-23T19:06:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130119602.843520.126510@g44g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<djhcku$73a$1@reader2.panix.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lnrdtbd46kf3c@corp.supernews.com> <11lo4omhspfogc3@news.supernews.com> <11lo5r8jvjnb5b6@corp.supernews.com> <djhcku$73a$1@reader2.panix.com>`

```
> They laughed at Columbus,

The thing about Columbus is that he was wrong.  His claim was that the
world was 17,000 miles around when it had been known since 500BC or so
that it was 24,000 miles, and Ptolomy's Geographica was based on 24,000
miles.

Columbus never admitted he was wrong and always maintained that he had
been to South East Asian lands, and that 17,000 miles was the correct
figure. He never thought of where he had been as new continents, there
wasn't room in his 'world' to have them.
```

###### ↳ ↳ ↳ Re: Fibonacci program

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-10-24T05:36:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<djhrsp$2ak$1@reader2.panix.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lo5r8jvjnb5b6@corp.supernews.com> <djhcku$73a$1@reader2.panix.com> <1130119602.843520.126510@g44g2000cwa.googlegroups.com>`

```
In article <1130119602.843520.126510@g44g2000cwa.googlegroups.com>,
Richard <riplin@Azonic.co.nz> wrote:
>> They laughed at Columbus,
>
>The thing about Columbus is that he was wrong.

So was Ptolemy... didn't seem to stop what either came up with as being 
useful, though.

DD
```

###### ↳ ↳ ↳ Re: Fibonacci program

_(reply depth: 7)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-23T23:11:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130134310.825248.96180@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<djhrsp$2ak$1@reader2.panix.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lo5r8jvjnb5b6@corp.supernews.com> <djhcku$73a$1@reader2.panix.com> <1130119602.843520.126510@g44g2000cwa.googlegroups.com> <djhrsp$2ak$1@reader2.panix.com>`

```
>> The thing about Columbus is that he was wrong.

> So was Ptolemy...

No one laughed at Ptolemy.

The point about "They laughed at Columbus," is that it implies that the
'They' were wrong yet they made fun of the heroic Columbus who showed
them up as the fools and that his theory was right.  In fact it was the
other way around. The experts had been right for 2000 years (in spite
of the Church) and Columbus came up with a wrong headed idea.

In fact, it is probable that he didn't even discover anything. Evidence
indicates that he had a map and knew what he was looking for. It is
probable that an earlier, accidental, voyage to the Caribbean had
washed up on Madeira where Collumbus lived after marrying the
Governour's sister.

> didn't seem to stop what either came up with as being useful, though.

That is entirely a matter of opinion - ask any native American.
```

###### ↳ ↳ ↳ Re: Fibonacci program

_(reply depth: 8)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-10-25T16:16:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<djllp202loc@news2.newsguy.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lo5r8jvjnb5b6@corp.supernews.com> <djhcku$73a$1@reader2.panix.com> <1130119602.843520.126510@g44g2000cwa.googlegroups.com> <djhrsp$2ak$1@reader2.panix.com> <1130134310.825248.96180@f14g2000cwb.googlegroups.com>`

```

Accidentally posted this to the wrong group (news server doesn't entirely
cooperate with newsreader - long story).

In article <1130134310.825248.96180@f14g2000cwb.googlegroups.com>, "Richard" <riplin@Azonic.co.nz> writes:
> >> The thing about Columbus is that he was wrong.
> 
> In fact, it is probable that he didn't even discover anything.

In _Cod_, Mark Kurlansky presents strong evidence that plenty of
Europeans knew about the "New World" when Colon "discovered" it, and
in fact that many of them were quite annoyed at his letting the
aristocracy in on a mercantile secret.

If memory serves, he cites a letter to Colon from Giovanni Caboto
("John Cabot", when he was working for the English) to that effect.
Caboto, presumably, saw which way the wind was blowing (he was a
sailor, after all) and decided to get into the "discovering" business
himself.

I'd provide citations but I'm not sure where my copy has swum off to.

In _The Basque History of the World_, Kurlansky presents evidence
that regular Basque visits to North America likely predated Colon's
voyage by about a century.  He gives little credence to the idea
that the Basques beat the Vikings to North America, but unlike the
Vikings, the Basques were regular visitors and likely had permanent
settlements in Newfoundland. (56-60)
```

###### ↳ ↳ ↳ Re: Fibonacci program

_(reply depth: 6)_

- **From:** Jeff York <ralf4@btinternet.com>
- **Date:** 2005-10-24T15:16:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r2rpl11arllegol8b3ihkr4ti5bium1b3l@4ax.com>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lnrdtbd46kf3c@corp.supernews.com> <11lo4omhspfogc3@news.supernews.com> <11lo5r8jvjnb5b6@corp.supernews.com> <djhcku$73a$1@reader2.panix.com> <1130119602.843520.126510@g44g2000cwa.googlegroups.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:

>> They laughed at Columbus,
>
…[8 more quoted lines elided]…
>wasn't room in his 'world' to have them.

I once heard it said that Columbus would be the ideal figurehead for a
political party in that...

When he set out, he didn't know where he was going,
When he arrived, he didn't know where he was,
When he got back, he didn't know where he'd been,
And he did it all on borrowed money.

:-)
```

##### ↳ ↳ Re: Fibonacci program

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-10-24T10:42:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1g77f.16$wG.4@bignews4.bellsouth.net>`
- **References:** `<1130013756.965425.5090@g14g2000cwa.googlegroups.com> <11lnqjif5kesdc5@corp.supernews.com> <11lnrdtbd46kf3c@corp.supernews.com>`

```
And here I was, spouting off about no International Obfuscated COBOL 
Contest! We should simply declare Mike B the winner now. :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
