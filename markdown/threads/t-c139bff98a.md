[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Having trouble declaring/fetching in Pro*Cobol

_9 messages · 4 participants · 2010-03_

---

### Having trouble declaring/fetching in Pro*Cobol

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2010-03-10T16:17:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com>`

```
If I run the query in sql developer it works fine, but when I declare
it as a cursor it is not retrieving but 1 record.

          SELECT SubStr(mbrsep,1,8), Count(*)
          FROM mbrsepmstr
          GROUP BY SubStr(mbrsep,1,8)
          HAVING Count(*) > 01

Returns 1915 rows.  Below is the code. If anyone can help I would
really appreciate it!

4000-SECOND-PASS.
    PERFORM 4000-DECLARE-CURSOR
       THRU 4000-DECLARE-CURSOR-EXIT.

    PERFORM 4000-FETCH-CURSOR
       THRU 4000-FETCH-CURSOR-EXIT.
    MOVE SQLERRD(3) to SQL-ARG-CNT.
    IF SQL-ARG-CNT = 0
        GO TO 4000-SECOND-PASS-EXIT.

    DISPLAY "SQL " SQL-ARG-CNT
    PERFORM VARYING DTL-SUB FROM 1 BY 1
      UNTIL DTL-SUB > sql-arg-cnt
        MOVE D-SQL-ARG-NO(dtl-sub) to SQL-ARG-NO
        PERFORM 4000-UPDATE-MBRSEPMSTR
           THRU 4000-UPDATE-MBRSEPMSTR-EXIT
           IF UPD-ERR-RESULT = 1
              GO TO 4000-SECOND-PASS-EXIT
           END-IF
        END-PERFORM.

4000-SECOND-PASS-EXIT. EXIT.

4000-DECLARE-CURSOR.
    MOVE ZEROES TO LCOUNT.
    EXEC SQL
     DECLARE  MBR_C CURSOR FOR
         SELECT SubStr(mbrsep,1,8), Count(*) as COUNT
         FROM mbrsepmstr
         GROUP BY SubStr(mbrsep,1,8)
         HAVING Count(*) > 01
    END-EXEC.

    EXEC SQL
      OPEN MBR_C
    END-EXEC.

    IF (SQLCODE NOT = 0)
      DISPLAY "ERR IN 4000-DECLARE-CURSOR"
         PERFORM SQL-ERROR-PARA
            THRU SQL-ERROR-PARA-EXIT
    END-IF.
4000-DECLARE-CURSOR-EXIT.

4000-FETCH-CURSOR.
    EXEC SQL
       FETCH  MBR_C
         INTO :D-SQL-ARG-NO
             ,:D-SQL-ARG-CouNT
    end-exec.

    IF SQLCODE <> 0 AND 1403
      DISPLAY "ERR IN 4000-FETCH-CURSOR"
         PERFORM SQL-ERROR-PARA
            THRU SQL-ERROR-PARA-EXIT
    END-IF.

4000-FETCH-CURSOR-EXIT. EXIT.

4000-UPDATE-MBRSEPMSTR.
    exec sql
       update mbrsepmstr
       set CODE4 = '1000'
       where SubStr(mbrsep,1,8) = :SQL-ARG-NO
    end-exec.

    IF SQLCODE <> 0 AND 1403
      DISPLAY "ERR IN 4000-UPDATE-MBRSEPMSTR"
         PERFORM SQL-ERROR-PARA
            THRU SQL-ERROR-PARA-EXIT
    END-IF.
```

#### ↳ Re: Having trouble declaring/fetching in Pro*Cobol

- **From:** dashwood@enternet.co.nz
- **Date:** 2010-03-10T19:26:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63a05385-3ebd-4a46-a5a2-738bfe39d9f0@a16g2000pre.googlegroups.com>`
- **References:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com>`

```
On Mar 11, 1:17 pm, jmoore <jmoore...@gmail.com> wrote:
> If I run the query in sql developer it works fine, but when I declare
> it as a cursor it is not retrieving but 1 record.
…[7 more quoted lines elided]…
> really appreciate it!

It can only retrieve 1 row because the host variables have not been
defined with OCCURS on them.

SQLERRD(3) will have a count of the number of rows actually loaded by
the FETCH. (Or the same for a SELECT...)

If there is no OCCURS ON the Host Variables, it can only ever load 1
row.

If you want more rows, keep fetching (with a loop) until you get a non-
zero SQLCODE (taking care to save the host variables into something
else on each FETCH, because they will obviously be overwritten by the
next FETCH), OR, don't use a CURSOR and simply SELECT ...INTO an array
of Host Variables. (SQLERRD(3) will tell you how many it loaded).

HTH,

Pete.
<snipped>
```

##### ↳ ↳ Re: Having trouble declaring/fetching in Pro*Cobol

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2010-03-11T04:20:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<189d9d58-d35b-49d3-b29e-682edc6877a0@u9g2000yqb.googlegroups.com>`
- **References:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com> <63a05385-3ebd-4a46-a5a2-738bfe39d9f0@a16g2000pre.googlegroups.com>`

```
On Mar 10, 10:26 pm, dashw...@enternet.co.nz wrote:
> On Mar 11, 1:17 pm, jmoore <jmoore...@gmail.com> wrote:
>
…[29 more quoted lines elided]…
> <snipped>

Can you give me some pseudocode for the example I gave. I am fetching
into 2 variables for count and mbrsep that occurs 4000 times.
```

###### ↳ ↳ ↳ Re: Having trouble declaring/fetching in Pro*Cobol

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2010-03-12T11:54:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vtakeF9kpU1@mid.individual.net>`
- **References:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com> <63a05385-3ebd-4a46-a5a2-738bfe39d9f0@a16g2000pre.googlegroups.com> <189d9d58-d35b-49d3-b29e-682edc6877a0@u9g2000yqb.googlegroups.com>`

```
jmoore wrote:
> On Mar 10, 10:26 pm, dashw...@enternet.co.nz wrote:
>> On Mar 11, 1:17 pm, jmoore <jmoore...@gmail.com> wrote:
…[34 more quoted lines elided]…
> into 2 variables for count and mbrsep that occurs 4000 times.

Here is ONE way to do it (It isn't the ONLY way and may not even be the BEST 
way, but it is a good way for Embedded SQL)

declare host variables (You only need each variable defined once without 
OCCURS on it.)
declare cursor

move zero to SQLSTATE
set stored array index/subscript to 1

Perform until SQLSTATE is not = zero
      exec SQL
            fetch...into the defined host variables
      end-exec
      move host variables fetched into to the sorage array or whatever
      increment the storage array index/subscript
end-perform

The storage array index/subscript tells you how many there were.

ALTERNATIVELY:

declare host variables with OCCURS 4000

DON'T declare a cursor.

exec SQL
      SELECT  blah blah INTO  (occurring host variables without subscript on 
their names)
end-exec

Check SQLSTATE/SQLCODE    (I prefer SQLSTATE; it tells me more...)

SQLERRD(3) contains the number of rows loaded to HV array.

If you find this helpful, please return the favour and go and visit 
http://primacomputing.co.nz/cobol21

(Seeing the visit count going up makes my day :-))

Cheers,

Pete.
```

###### ↳ ↳ ↳ Re: Having trouble declaring/fetching in Pro*Cobol

_(reply depth: 4)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2010-03-12T08:09:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<304d6278-0354-48ca-a11a-e4e15b62d4ea@g4g2000yqa.googlegroups.com>`
- **References:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com> <63a05385-3ebd-4a46-a5a2-738bfe39d9f0@a16g2000pre.googlegroups.com> <189d9d58-d35b-49d3-b29e-682edc6877a0@u9g2000yqb.googlegroups.com> <7vtakeF9kpU1@mid.individual.net>`

```
On Mar 11, 5:54 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> jmoore wrote:
> > On Mar 10, 10:26 pm, dashw...@enternet.co.nz wrote:
…[82 more quoted lines elided]…
> - Show quoted text -

Thanks everyone for your responses, I decided to handle it a different
way.

               update mbrsepmstr set
code4='1000'
               where substr(mbrsep,1,8) in (select substr(mbrsep,
1,8)
               from
mbrsepmstr
               group by substr(mbrsep,
1,8)
               having count(*) >
01)
```

#### ↳ Re: Having trouble declaring/fetching in Pro*Cobol

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2010-03-11T11:33:02+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<24ehp55rej59ea96rhfklkdm2fdebm4de0@4ax.com>`
- **References:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com>`

```
On Wed, 10 Mar 2010 16:17:04 -0800 (PST) jmoore <jmoore207@gmail.com> wrote:

:>If I run the query in sql developer it works fine, but when I declare
:>it as a cursor it is not retrieving but 1 record.

:>          SELECT SubStr(mbrsep,1,8), Count(*)
:>          FROM mbrsepmstr
:>          GROUP BY SubStr(mbrsep,1,8)
:>          HAVING Count(*) > 01

:>Returns 1915 rows.  Below is the code. If anyone can help I would
:>really appreciate it!

You only fetched one row. If you want more rows, FETCH more rows.
```

##### ↳ ↳ Re: Having trouble declaring/fetching in Pro*Cobol

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2010-03-11T04:18:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46408a2d-2d66-4a91-bec9-4dfbb85bcc13@z4g2000yqa.googlegroups.com>`
- **References:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com> <24ehp55rej59ea96rhfklkdm2fdebm4de0@4ax.com>`

```
On Mar 11, 4:33 am, Binyamin Dissen <postin...@dissensoftware.com>
wrote:
> On Wed, 10 Mar 2010 16:17:04 -0800 (PST) jmoore <jmoore...@gmail.com> wrote:
>
…[22 more quoted lines elided]…
> especially those from irresponsible companies.

My fetch is going into variables that occur 4000 times.
000000 01  D-SQL-ARG-COUNT          PIC S9(04) OCCURS 4000 times.
000000 01  D-SQL-ARG-NO             pic 9(08) OCCURS 4000 times.
```

###### ↳ ↳ ↳ Re: Having trouble declaring/fetching in Pro*Cobol

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2010-03-11T15:45:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8sshp5p8ncvnftvqm5k9svrprr862b0io1@4ax.com>`
- **References:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com> <24ehp55rej59ea96rhfklkdm2fdebm4de0@4ax.com> <46408a2d-2d66-4a91-bec9-4dfbb85bcc13@z4g2000yqa.googlegroups.com>`

```
On Thu, 11 Mar 2010 04:18:48 -0800 (PST) jmoore <jmoore207@gmail.com> wrote:

:>On Mar 11, 4:33ï¿½am, Binyamin Dissen <postin...@dissensoftware.com>
:>wrote:

:>> On Wed, 10 Mar 2010 16:17:04 -0800 (PST) jmoore <jmoore...@gmail.com> wrote:

:>> :>If I run the query in sql developer it works fine, but when I declare
:>> :>it as a cursor it is not retrieving but 1 record.
:>>
:>> :> ï¿½ ï¿½ ï¿½ ï¿½ ï¿½SELECT SubStr(mbrsep,1,8), Count(*)
:>> :> ï¿½ ï¿½ ï¿½ ï¿½ ï¿½FROM mbrsepmstr
:>> :> ï¿½ ï¿½ ï¿½ ï¿½ ï¿½GROUP BY SubStr(mbrsep,1,8)
:>> :> ï¿½ ï¿½ ï¿½ ï¿½ ï¿½HAVING Count(*) > 01

:>> :>Returns 1915 rows. ï¿½Below is the code. If anyone can help I would
:>> :>really appreciate it!

:>> You only fetched one row. If you want more rows, FETCH more rows.

:>My fetch is going into variables that occur 4000 times.
:>000000 01  D-SQL-ARG-COUNT          PIC S9(04) OCCURS 4000 times.
:>000000 01  D-SQL-ARG-NO             pic 9(08) OCCURS 4000 times.

That don't matter.

You can use the 

         FOR :host ROWS

clause if your database supports it.
```

###### ↳ ↳ ↳ Re: Having trouble declaring/fetching in Pro*Cobol

_(reply depth: 4)_

- **From:** jmoore <jmoore207@gmail.com>
- **Date:** 2010-03-11T05:54:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71f7d8be-845a-4563-af3e-f24ca45c4bc8@z35g2000yqd.googlegroups.com>`
- **References:** `<c9b97518-b502-4ce3-9249-b1b06021b5b4@t41g2000yqt.googlegroups.com> <24ehp55rej59ea96rhfklkdm2fdebm4de0@4ax.com> <46408a2d-2d66-4a91-bec9-4dfbb85bcc13@z4g2000yqa.googlegroups.com> <8sshp5p8ncvnftvqm5k9svrprr862b0io1@4ax.com>`

```
On Mar 11, 8:45 am, Binyamin Dissen <postin...@dissensoftware.com>
wrote:
> On Thu, 11 Mar 2010 04:18:48 -0800 (PST) jmoore <jmoore...@gmail.com> wrote:
>
…[39 more quoted lines elided]…
> especially those from irresponsible companies.

Oracle database
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
