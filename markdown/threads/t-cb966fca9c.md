[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sorting

_17 messages · 11 participants · 1999-10 → 1999-11_

---

### Sorting

- **From:** ladybug44@my-deja.com
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v7l33$ek6$1@nnrp1.deja.com>`

```
Hi...  I was wondering if there was a SORT command for sorting tables.
If there is, could anyone point me in the right direction?  My book only
details how to sort files, but also mentions that there are other uses
of SORT.  I cannot find anything on it, however, in other books or on
the web.
Thanks in advance,
~e


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Sorting

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sDJR3.641$23.44910@typ11.nn.bcandid.com>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com>`

```
<ladybug44@my-deja.com> wrote in message news:7v7l33$ek6$1@nnrp1.deja.com...
> Hi...  I was wondering if there was a SORT command for sorting tables.
> If there is, could anyone point me in the right direction?  My book only
> details how to sort files, but also mentions that there are other uses
> of SORT.

In your sort input procedure, release every item in your table from within a
loop.  Your output procedure would move each returned sort record to the
next entry in your original table.  The table would be ready for a SEARCH
ALL or other use requiring sorted entries.
```

#### ↳ Re: Sorting

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38176FCA.8AE1979A@home.com>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com>`

```


ladybug44@my-deja.com wrote:
> 
> Hi...  I was wondering if there was a SORT command for sorting tables.
…[4 more quoted lines elided]…
> Thanks in advance,

There is a Sort Table in MicroFocus(Merant) compilers - but I don't know
if it is available in others. Bill Klein would tell us, (he's still in
UK), that it is included in the new Standards.

Don't suppose it will help much, (if your compiler doesn't have sort
table), but here's an example of how I'm using it :-

       *>-------------------------------------------------------------
       Method-id. "d2-capacity-sort".
       *>-------------------------------------------------------------
       Local-storage section.
       01 c                                     pic x(4) comp-5.
       01 n                                     pic x(4) comp-5.
       01 ls-count                              pic x(4) comp-5.
       01 ls-table.
          05 ls-line occurs 1 to MaxCapacityLine depending on c
                            ascending  ls-Capacity-key
                            ascending  ls-capacity-value.

             15 ls-capacity-key          pic x(04).
             15 ls-capacity-value        pic 9(03)v9(03) comp-3.

       Procedure Division.

       move zeroes to c
       perform varying n from 1 by 1 until n > MaxCapacityLine

          if  VESSEL-Capacity-key(n) <> spaces
              add 1 to c
              move VESSEL-Capacity-line(n) to ls-line(c)
          End-if
       End-perform

       sort ls-line

       initialize VESSEL-Capacity-table
       perform varying n from 1 by 1 until n > c
           move ls-line(n) to VESSEL-Capacity-line(n)
       End-perform

       End Method "d2-capacity-sort".
       *>-------------------------------------------------------------

To briefly explain the above - assume a sort-table of 9 lines and I've
only got 3 lines of 'actual' data. I'm rearranging them so they appear
as the first 3 lines in the final record written to file.

Jimmy, Calgary AB
```

#### ↳ Re: Sorting

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38177290.14442994@news1.attglobal.net>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com>`

```
On Wed, 27 Oct 1999 19:51:00 GMT, ladybug44@my-deja.com wrote:

>Hi...  I was wondering if there was a SORT command for sorting tables.
>If there is, could anyone point me in the right direction?  My book only
…[5 more quoted lines elided]…
>

Sorting of tables is supported in the next standard - but not the
present one.  However, many compiler vendors do allow you to sort
tables.  With recent versions of Microfocus the syntax is:

Sort Ascending Table-Name

Where Table-Name is the level that has the occurs clause.
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Sorting

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3817765D.B4527B87@NOSPAMhome.com>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com>`

```
ladybug44@my-deja.com wrote:
> 
> Hi...  I was wondering if there was a SORT command for sorting tables.
…[5 more quoted lines elided]…
> ~e

Soon.   But for now, I either sort by hand, or read the table in as a
sorted file.
```

##### ↳ ↳ Re: Sorting

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iBiS3.8892$qy6.121888@news2.mia>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <3817765D.B4527B87@NOSPAMhome.com>`

```
Howard Brazee wrote:
>ladybug44@my-deja.com wrote:
>>
…[9 more quoted lines elided]…
>sorted file.

Sorting tables in memory is not difficult.  If your compiler doesn't
support a table sort option, then you can download SHELSRT.ZIP from my
web page below.
```

###### ↳ ↳ ↳ Re: Sorting

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D2tS3.1219$jD2.33721@typhoon01.swbell.net>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <3817765D.B4527B87@NOSPAMhome.com> <iBiS3.8892$qy6.121888@news2.mia>`

```

Judson McClendon <judmc123@bellsouth.net
>
> Sorting tables in memory is not difficult.  If your compiler doesn't
> support a table sort option, then you can download SHELSRT.ZIP from
my
> web page below.
> --
Or you could write your own
EXCHANGE SORT
BUBBLE SORT
RADIX SORT
or others, depending on the nature of the data.
```

###### ↳ ↳ ↳ Re: Sorting

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381a6a9e_4@news3.prserv.net>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <3817765D.B4527B87@NOSPAMhome.com> <iBiS3.8892$qy6.121888@news2.mia> <D2tS3.1219$jD2.33721@typhoon01.swbell.net>`

```

Jerry P <bismail@bisusa.com> wrote in message
news:D2tS3.1219$jD2.33721@typhoon01.swbell.net...
>
> Judson McClendon <judmc123@bellsouth.net
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sorting

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381a6abc_1@news3.prserv.net>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <3817765D.B4527B87@NOSPAMhome.com> <iBiS3.8892$qy6.121888@news2.mia> <D2tS3.1219$jD2.33721@typhoon01.swbell.net>`

```
try
http://www.etk.com/papers/sorting/sorting.htm

Jerry P <bismail@bisusa.com> wrote in message
news:D2tS3.1219$jD2.33721@typhoon01.swbell.net...
>
> Judson McClendon <judmc123@bellsouth.net
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Sorting

_(reply depth: 4)_

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jw5T3.1886$iS.87064@viper>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <3817765D.B4527B87@NOSPAMhome.com> <iBiS3.8892$qy6.121888@news2.mia> <D2tS3.1219$jD2.33721@typhoon01.swbell.net>`

```
>EXCHANGE SORT
>BUBBLE SORT
>RADIX SORT
Is any one of these the INDEX sort? Where a table is used to store the data
and an index. The index is stored in yet another array which is simply a
list of pointers to the appropriate table entry. Sorting is then don on the
index array and no table data has to be moved, save the index values. The
first entry in the table would be refereced as:

TABLE_DATA(TABLE_INDEX(1))

Where TABLE_INDEX(1) can refer to any entry in the table, but actually
refers to the ENTRY which has the lowest key value.
```

###### ↳ ↳ ↳ Re: Sorting

_(reply depth: 5)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sr7T3.744$td2.30144@typhoon01.swbell.net>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <3817765D.B4527B87@NOSPAMhome.com> <iBiS3.8892$qy6.121888@news2.mia> <D2tS3.1219$jD2.33721@typhoon01.swbell.net> <Jw5T3.1886$iS.87064@viper>`

```

Gumbo <a@a.com> wrote in message news:Jw5T3.1886$iS.87064@viper...
> >EXCHANGE SORT
> >BUBBLE SORT
> >RADIX SORT
> Is any one of these the INDEX sort? Where a table is used to store
the data
> and an index. The index is stored in yet another array which is
simply a
> list of pointers to the appropriate table entry. Sorting is then
done on the
> index array and no table data has to be moved, save the index
values. The
> first entry in the table would be refereced as:
>
> TABLE_DATA(TABLE_INDEX(1))
>
> Where TABLE_INDEX(1) can refer to any entry in the table, but
actually
> refers to the ENTRY which has the lowest key value.

No. An INDEX SORT is yet another animal. As I understand an
index sort, the data value is mapped to an entry in another array,
the mapping operator dependent on the data in the table. Suppose
you had a table of employees and wanted to sort them by employee
number. You have another table of size MAX EMPLOYEE NUMBER.
The original table might look like:
1 ADAMS            4
2 BROWN          1
3 CLARK            3
4 DOE                 2

After looping through the employee table and mapping table
entries, the INDEX table looks like
2
4
3
1
So the first pointer in the INDEX table points to smallest
customer number in the original table.

Logic in an INDEX sort gets complicated when two (or more)
data elements map to the same location in the INDEX table
(such as a sort by ZIP code). In that case, the already-present
entries in the INDEX table have to be shuffled around to
accommodate the new guy.
```

###### ↳ ↳ ↳ Re: Sorting

_(reply depth: 6)_

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mW9U3.570$GH5.20943@viper>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <3817765D.B4527B87@NOSPAMhome.com> <iBiS3.8892$qy6.121888@news2.mia> <D2tS3.1219$jD2.33721@typhoon01.swbell.net> <Jw5T3.1886$iS.87064@viper> <sr7T3.744$td2.30144@typhoon01.swbell.net>`

```
I know my terminology is off. I haven't had to think about this stuff in a
long time, but here it goes....
>1 ADAMS            4
>2 BROWN          1
>3 CLARK            3
>4 DOE                 2


using your example the sort I am thinking about would be,,,,

Adding the names in some random order would have the table look like:

BROWN
CLARK
DOE
ADAMS

The index array would hold values:
4
1
2
3
Given Arrays NAME and NAME-INDEX, to refer to the first NAME you would:
PERFORM VARYING CTR FROM 1 BY 1 UNTIL END-OF-TABLE
    DISPLAY NAME(NAME-INDEX(CTR))
END-PERFORM

Thus if you were to apply a SORT to the NAME table, no values would have to
be moved, just the NAME-INDEX values would be moved around. With small data
fields this would be inappropriate, but if each table entry is quite large
the actual moves would be significantly less than moving all the data in the
table entry.

Obviously I don't know the correct terminology for this type of sort, but it
always seemed like a good way to speed up any table sort.

Oh yeah...the actual sort I was thinking of, a modified BUBBLE SORT, I think
it is actually called a SHELL sort

PERFORM VARYING CTR1 FROM 1 BY 1 UNTIL CTR1 > MAX-TABLE-ENTRY
    PERFORM VARYING CTR2 FROM CTR1+1 BY 1 UNTIL CTR2 > MAX-TABLE-ENTRY
        IF NAME(NAME-INDEX(CTR1)) > NAME(NAME-INDEX(CTR2))
            TEMP = NAME-INDEX(CTR1)
            NAME-INDEX(CTR1) = NAME-INDEX(CTR2)
            NAME-INDEX(CTR2) = TEMP
        END-IF
    END-PERFORM
END-PERFORM
```

#### ↳ Re: Sorting

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qSOR3.712$jn3.32239@typhoon01.swbell.net>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com>`

```

<ladybug44@my-deja.com> wrote in message
news:7v7l33$ek6$1@nnrp1.deja.com...
> Hi...  I was wondering if there was a SORT command for sorting
tables.
> If there is, could anyone point me in the right direction?  My book
only
> details how to sort files, but also mentions that there are other
uses
> of SORT.

If you book shows only files, it uses the syntax

SORT SORT-WORK ON ASCENDING KEY SORT-KEY
        USING INPUT-FILE
         GIVING OUTPUT-FILE.

The other form of the syntax is:

 SORT SORT-WORK ON ASCENDING KEY SORT-KEY
        INPUT PROCEDURE IS procedure-name (thru procedure-name2)
        OUTPUT PROCEDURE IS procedure-name (thru procedure-name2)..

So, to sort a table:

SORT SORT-WORK ON ASCENDING KEY SORT-KEY
    INPUT PROCEDURE IS WAFFLE-IRON
    OUTPUT PROCEDURE IS DIABETES.

    EXIT PROGRAM.

WAFFLE-IRON.
    PERFORM VARYING MINNOW FROM 1 BY 1 UNTIL MINNOW > TABLE-LENGTH
        MOVE TABLE-ITEM(MINNOW) TO SORT-REC
        RELEASE SORT-REC
    END-PERFORM.

DIABETES.
    MOVE 0 TO MINNOW
    RETURN SORT-FILE NOT AT END
        ADD 1 TO MINNOW
        MOVE SORT-REC TO TABLE-ITEM(MINNOW)
        GO TO DIABETES.

NEXT-PARAGRAPH.

Advanced users only:
You can mix-and-match

SORT SORT-WORK ON ASCENDING KEY SORT-KEY
     USING INPUT-FILE
     OUTPUT PROCEDURE IS (procedure-name).
or vice-versa.
```

##### ↳ ↳ Re: Sorting

- **From:** "Gumbo" <a@a.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CC3S3.345$iS.19137@viper>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <qSOR3.712$jn3.32239@typhoon01.swbell.net>`

```
>So, to sort a table:
>
…[5 more quoted lines elided]…
>


You are still sorting a file. You are simply moving the table to a file one
at a time then back into the table again.
However that is a valid answer to the question.

Along the same lines, the table could be stored in an indexed file. Then
sorting would only be reading the table back in again after an update
occurs, otherwise the table would remain in memory. Inserts into the table
would be writes to the file and reading the table back in. With a small
number of updates this could be practical. If the table is small enough it
would remain in the disk buffer and not hold up the program when IO's are
actually executed.
```

###### ↳ ↳ ↳ Re: Sorting

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<as5S3.597$%D6.20129@typhoon01.swbell.net>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <qSOR3.712$jn3.32239@typhoon01.swbell.net> <CC3S3.345$iS.19137@viper>`

```

Gumbo <a@a.com> wrote in message news:CC3S3.345$iS.19137@viper...
> >So, to sort a table:
> >
…[8 more quoted lines elided]…
> You are still sorting a file. You are simply moving the table to a
file one
> at a time then back into the table again.
> However that is a valid answer to the question.

Not necessarily. It only looks like you are sorting a file
to conform to COBOL syntax.

Realia (for one) and probably any other good compiler
will sort the records in memory if at all possible. I imagine sorting
a 100-element table of 50 bytes each would generate zero disk
accesses.
```

###### ↳ ↳ ↳ Re: Sorting

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vrv8k$tm1$1@nntp4.atl.mindspring.net>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com> <qSOR3.712$jn3.32239@typhoon01.swbell.net> <CC3S3.345$iS.19137@viper>`

```
In the draft Standard (and in several existing implementations - including
MERANT), a TABLE SORT is valid, i.e.

01 Whatever.
    05 Sort-Work  occurs 10 times.
          10 Sort-Key Pic XX
           10 OtherStuf  Pic XXX.

   ....

SORT SORT-WORK ON ASCENDING KEY SORT-KEY.

(I can't remember but I think that
    INPUT PROCEDURE IS WAFFLE-IRON
    OUTPUT PROCEDURE IS DIABETES.
would even be allowed).

If you have your table defined with an ASCENDING/DESCENDING key, you don't
even need to tell it what to sort on - unless you want to sort on some other
field (which is allowed).
```

#### ↳ Re: Sorting

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FW6S3.692$DM3.10344@news4.mia>`
- **References:** `<7v7l33$ek6$1@nnrp1.deja.com>`

```
No, if you are on IBM or Wang or Honeywell, you can call a 'table-sort' /
memory sort.
Otherwise you have to order it yourself.  (You can write it to a seq-file,
then sort USING / GIVING
and reload the table.


ladybug44@my-deja.com wrote in message <7v7l33$ek6$1@nnrp1.deja.com>...
>Hi...  I was wondering if there was a SORT command for sorting tables.
>If there is, could anyone point me in the right direction?  My book only
…[8 more quoted lines elided]…
>Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
