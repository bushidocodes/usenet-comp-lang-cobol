[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ERROR 337

_8 messages · 6 participants · 2001-10_

---

### ERROR 337

- **From:** JONESEY <mrjones_101@hotmail.com>
- **Date:** 2001-10-22T22:37:40+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com>`

```
ANY IDEAS WHAT THE HELL THIS ERROR MEANS??

        Error 337 : number of subscripts used is more than expected

Compiler is throwing at me!!!!

Thanks
```

#### ↳ Re: ERROR 337

- **From:** "Vinylmixer" <bpcmg@SPAMhotmail.com>
- **Date:** 2001-10-22T23:07:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uO0B7.59975$sF.5380130@news2-win.server.ntlworld.com>`
- **References:** `<a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com>`

```
Sounds like a problem with an array i,e u are trying to access a part of an
array that doesnt exist.

v

"JONESEY" <mrjones_101@hotmail.com> wrote in message
news:a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com...
> ANY IDEAS WHAT THE HELL THIS ERROR MEANS??
>
…[5 more quoted lines elided]…
>
```

#### ↳ Re: ERROR 337

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-22T17:43:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r27p8$v60$1@slb4.atl.mindspring.net>`
- **References:** `<a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com>`

```
Have you heard this before?

 SHOW US THE CODE getting the error.

(show us both the Procedure Division statement getting the error AND the
entire 01-level for all the data items referenced in your statement).

P.S.  It also REALLY helps if you tell us which compiler you are using.
```

#### ↳ Re: ERROR 337

- **From:** JONESEY <mrjones_101@hotmail.com>
- **Date:** 2001-10-22T23:52:59+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae89ttgp9phljroceqpo3vq6ab2pv1dg1q@4ax.com>`
- **References:** `<a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com>`

```
Heres the code


       DATA DIVISION. 
       FILE SECTION.
       FD LEAGUE-FILE.
       01 LEAGUE-RECORD.
          02 TEAM-NAME             PIC X(15).
          02 MATCHES-PLAYED        PIC 9(2).
          02 POINTS                PIC 9(3).

       WORKING-STORAGE SECTION.
       01 A-LEAGUE-TABLE.
          02 A-LEAGUE-RECORD OCCURS 10 TIMES.
              03 A-TEAM-NAME       PIC X(15)      VALUE SPACES.
              03 A-MATCHES-PLAYED  PIC 9(2)       VALUE ZERO.
              03 A-POINTS          PIC 9(3)       VALUE ZERO.

       01 EOF                      PIC 9          VALUE ZERO.
       01 I                        PIC 99.
.............

       PROCEDURE DIVISION. 
       MAIN-PARAGRAPH. 
.............
           MOVE 1 TO I.
           PERFORM READ-RECORD.
           PERFORM ARRAY-RECORD UNTIL EOF IS EQUAL TO 1.

       READ-RECORD.
           READ LEAGUE-FILE AT END MOVE 1 TO EOF.
.............
       ARRAY-RECORD.
           MOVE TEAM-NAME TO A-TEAM-NAME(I).
           MOVE MATCHES-PLAYED TO MATCHES-PLAYED(I). ******error at or before this line

           MOVE POINTS TO A-POINTS(I).
              ADD 1 TO I
           PERFORM READ-RECORD.

.............

my compiler is COBOL 85 Level 2 Compiler - Version 5.2 Sanderson Computing  1998

Thanks
```

##### ↳ ↳ Re: ERROR 337

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-10-22T23:59:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Np2B7.38881$ev2.45866@www.newsranger.com>`
- **References:** `<a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com> <ae89ttgp9phljroceqpo3vq6ab2pv1dg1q@4ax.com>`

```
Hi Jonesey,

Relax, take a deep breath. We'll get you thru this. An error msg like that
usually means you miscoded a stmt and it's not connected to the table per se.

Quote:
MOVE MATCHES-PLAYED TO MATCHES-PLAYED(I). 
^

The ^ shows that you misspelled A-MATCHES-PLAYED. I do it all the time.

Regards, Jack.
In article <ae89ttgp9phljroceqpo3vq6ab2pv1dg1q@4ax.com>, JONESEY says...
>
>Heres the code
…[44 more quoted lines elided]…
>
```

##### ↳ ↳ Re: ERROR 337

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-23T13:00:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bd4b58e_5@news.newsgroups.com>`
- **References:** `<a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com> <ae89ttgp9phljroceqpo3vq6ab2pv1dg1q@4ax.com>`

```
You asked what the error means. It means you are trying to subscript a field
which has no OCCURS on it, (or use a table dimension which has never been
defined).

If you think about this and look at your code you will see the error.

Just this once, I'll cut you some slack and give you the solution, but don't
do it again...<G>

Try changing "MATCHES-PLAYED (I)" to "A-MATCHES-PLAYED (I)" on the line
where the error is flagged.

Spend more time thinking and less time screaming...<G>

Pete.


"JONESEY" <mrjones_101@hotmail.com> wrote in message
news:ae89ttgp9phljroceqpo3vq6ab2pv1dg1q@4ax.com...
> Heres the code
>
…[32 more quoted lines elided]…
>            MOVE MATCHES-PLAYED TO MATCHES-PLAYED(I). ******error at or
before this line
>
>            MOVE POINTS TO A-POINTS(I).
…[5 more quoted lines elided]…
> my compiler is COBOL 85 Level 2 Compiler - Version 5.2 Sanderson Computing
1998
>
> Thanks
>



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: ERROR 337

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-23T00:40:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD4BE23.F94F0C0C@home.com>`
- **References:** `<a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com> <ae89ttgp9phljroceqpo3vq6ab2pv1dg1q@4ax.com> <3bd4b58e_5@news.newsgroups.com>`

```


"Peter E. C. Dashwood" wrote:

> You asked what the error means. It means you are trying to subscript a field
> which has no OCCURS on it, (or use a table dimension which has never been
…[10 more quoted lines elided]…
> Spend more time thinking and less time screaming...<G>

Jonesey,

As your use of 'SORTED'  suggests to me you are in the UK - hopefully you've
also now got it 'SUSSED' <G>.

Tip - if you want help from us, show us THE SOURCE - it's bloody frustrating
trying to guess what you may have done wrong, because inevitably you young 'uns
point us at the things that *you* think are wrong - "It aint necessarily so !".
(Gershwin's 'Porgy and Bess').

And remember, remember, like the 5th of November - it is very, very  RARE that
the compiler is wrong - it's us dweebs !

Jimmy, Calgary AB
```

##### ↳ ↳ Re: ERROR 337

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-22T19:04:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r2c5n$l20$1@nntp9.atl.mindspring.net>`
- **References:** `<a849ttsh1snsmqkp2tjd1c0coq90214vem@4ax.com> <ae89ttgp9phljroceqpo3vq6ab2pv1dg1q@4ax.com>`

```
OK - now easy to answer,

the data item
  MATCHES-PLAYED

that you reference as the RECEIVING item in the statement
 MOVE MATCHES-PLAYED TO MATCHES-PLAYED(I)

is not defined under an OCCURS clause.  Therefore, when you try and use
  (I)
to subscript it - the compiler is telling you something is wrong.

Look carefully at the statement that the compiler is telling you is wrong
and try and figure out what you think is wrong.

HINT - it is NOT the fact that you have used a subscript.  Compare it to
your other MOVE statements and see what you have as sending and receiving
items for them.

P.S.  This is your introduction to "the error that you get tells you where
the problem is but NOT necessarily what your mistake really is"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
