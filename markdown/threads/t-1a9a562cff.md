[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Loading Tables

_8 messages · 5 participants · 2001-12_

---

### Loading Tables

- **From:** igal2000@hotmail.com (Igal)
- **Date:** 2001-12-08T09:27:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c124eb5e.0112080927.5a5c0938@posting.google.com>`

```
Hey Guys! I have two problems....
1. could anyone give me an example of loading tables from data-files
and explain to me what is the basic logic behind it?
2. I had this problem in one of my tests and I could not get it...
 an input record consist of 15 group items, each with a 3-digit part
number and an associated 3-digit quantity on hand. Assuming there are
50 input records:
 a. write a working-storage entry to store the data
 b. write a procedure division code to load the records into the
working storage entry you created
 c. write procedure division code to print the quantity on hand for
part number 126
 d. write proc-division code to find the average quantity for all the
parts.

I hope someone can guide me through the process of doing this, because
my book is really bad...so is my teacher....
Thanks!!!
```

#### ↳ Re: Loading Tables

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-12-08T18:22:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YTsQ7.39646$WC1.3937973@newsread2.prod.itd.earthlink.net>`
- **References:** `<c124eb5e.0112080927.5a5c0938@posting.google.com>`

```
Show us (the NG) what you have so far, and the newsgroup will help.  Ask us
a "general question" like this and we will guess (rightly or wrongly) that
you haven't really TRIED it yet.
```

#### ↳ Re: Loading Tables

- **From:** Steve Thompson <sthompsonNOSPAM@ix.netcom.com>
- **Date:** 2001-12-10T04:20:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C1437EB.5B4636FB@ix.netcom.com>`
- **References:** `<c124eb5e.0112080927.5a5c0938@posting.google.com>`

```
I'll try to answer you sometime tomorrow. It's late and I've
got to finish some other stuff (the reason that I'm posting
this is so that I'll find it again tomorrow and remember...)

<snip>
```

#### ↳ Re: Loading Tables

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-12-11T14:38:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fToR7.57408$xS6.92520@www.newsranger.com>`
- **References:** `<c124eb5e.0112080927.5a5c0938@posting.google.com>`

```
On 8 Dec 2001 09:27:01 -0800, in article
<c124eb5e.0112080927.5a5c0938@posting.google.com>, Igal stated 
>
>Hey Guys! I have two problems....
…[16 more quoted lines elided]…
>Thanks!!!
```

#### ↳ Re: Loading Tables

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-12-11T15:15:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DqpR7.57443$xS6.92895@www.newsranger.com>`
- **References:** `<c124eb5e.0112080927.5a5c0938@posting.google.com>`

```
On 8 Dec 2001 09:27:01 -0800, in article
<c124eb5e.0112080927.5a5c0938@posting.google.com>, Igal stated 
>

Oops! hit the wrong button.

This goes back to physics!!!

1.  It is faster to read a table than a file, since it is already in memory.
Reading a file takes longer, but it can be done that way in certain cases.  If
you have to search the table for every record of the main file it even takes
longer.

2.  A table is usually loaded using a sub-script.  If you have a table it
usually has an occurs (table occurs 200 times).  It is normal to read a table by
either using the varying verb or by incrementing an index or a variable you
described in working storage, as you read the file.    

3.  You can add the phrase "indexed by <variable>" to create an index for the
table.  It might be needed later to search the table.

>Hey Guys! I have two problems....
>1. could anyone give me an example of loading tables from data-files
…[15 more quoted lines elided]…
>Thanks!!!

01  MY-TABLE OCCURS 500 TIMES INDEXED BY PART-IDX.
05  T-PART-NO     PIC X(5).
05  T-PART-DESC   PIC X(30).
05  T-QTY-ON-HAND PIC 9(7).




You have a file you have to describe as input.  You just read it in order to
load the data into the file layout you have for the file. You move the data you
want into the table using a subscript.  
EXAMPLE:  "MOVE IN-PART-NO TO T-PART-NO (PART-IDX)".
The logic is the same as making a simple report.  The only difference is you are
moving the input fields to the table fields using PART-IDX as a sub-script.
When you get to the end of the file, you go to the next paragraph in the program
instead of the end of program processing.  You close the file because you no
longer need it.  You can use the same variable for end of file in the next part
of the program by setting it back to its starting value.   

This is really simple stuff.  If you know how to make a table, read a file, and
move a variable into a table you know all you need to know.  You just do this in
the initialization section of your program like setting printlines to zero.  You
can use the varying verb to actually increment the index or subscript, or just
add one to a variable for the subscript.
```

#### ↳ Re: Loading Tables

- **From:** Steve Thompson <sthompsonNOSPAM@ix.netcom.com>
- **Date:** 2001-12-13T17:11:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C18E12D.96B9317B@ix.netcom.com>`
- **References:** `<c124eb5e.0112080927.5a5c0938@posting.google.com>`

```
Igal wrote:
> 
> Hey Guys! I have two problems....
> 1. could anyone give me an example of loading tables from data-files
> and explain to me what is the basic logic behind it?
<snip>
1) You will need to write all of the logic for SELECT, FD,
01, OPEN INPUT and READ for the table. You will want to do
this as part of your house-keeping routines, because it must
be done prior to any other programming that will need to
reference the table.

2) The logic behind this is, the table may be common to many
different programs and/or it may be updated on a fairly
frequent basis. This would then cause you to have to
recompile a program every time the table changed.
<snip>
> 2. I had this problem in one of my tests and I could not get it...
>  an input record consist of 15 group items, each with a 3-digit part
> number and an associated 3-digit quantity on hand. Assuming there are
> 50 input records:
<snip>
The input record would look similar to this:

01 INPUT-TABLE-RECORD.
   02 INV-TABLE-ELEMENT      OCCURS 15 TIMES.
      03 INV-DETAIL.
         05 INV-PART-NO      PIC 9(3).
         05 INV-QUANTITY     PIC 9(3).

It is your job to set this up for indexing or subscripting.

<SNIP>
>  a. write a working-storage entry to store the data
<SNIP>

The table would look something like this:

01 INVENTORY-TABLE.
   03 INVENTORY-RECORDS OCCURS 1000 TIMES.
      05 INVENTORY-PART-NO  PIC 9(3) COMP-3.
      05 INVENTORY-QUANTITY PIC 9(3) COMP-3.

It is your job to set this table up to use index or
subscript.
<snip>
>  b. write a procedure division code to load the records into the
> working storage entry you created
<snip>
As I said before, you must determine the logic for this. It
will require an OPEN INPUT and a READ. Your job is to put
the code in there to handle the end of file, and to
implement subscript or index of the table and input record
table.
<snip>
>  c. write procedure division code to print the quantity on hand for
> part number 126
<snip>
Now, you will have to write the search logic or some
specific verb to do this (depending on how you ultimately
set up the table, indexed or subscripted, and if you paid
attention you would arrange for this to be in ascending
order by part number -- or it would already come to you in
ascending part number order).
<snip>
>  d. write proc-division code to find the average quantity for all the
> parts.
<snip>
Well, if you know math, then you will have to sequentially
read your table and capture the quantities. Then you will
also have to pay attention and capture the number of REAL
table entries (hint - the number 1000 that I used is well
beyond the number of entries you will get from 50 records
each having 15 entries). Only after this will you be able to
write the correct statements to determine the averages.
<snip>
> 
> I hope someone can guide me through the process of doing this, because
> my book is really bad...so is my teacher....
> Thanks!!!

You would have been in really tough shape had you been in my
COBOL class. You would have been expected to write this and
turn it in. And then for the next assignment, you would have
had to exchange this program with someone else in the class
(randomly selected by me), and then you would have been
given new specs that have to be applied to that program.
Your grade would be determined by how well you got your
"new" program to work, and how well your original program
could be modified (YES! It meant for me, having to grade 50
of these to spend about a week just doing the grading).
```

#### ↳ Re: Loading Tables

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-12-16T09:19:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C1C6722.D2ECB9@Azonic.co.nz>`
- **References:** `<c124eb5e.0112080927.5a5c0938@posting.google.com>`

```
Igal wrote:
> 
>  an input record consist of 15 group items, each with a 3-digit part
…[8 more quoted lines elided]…
> parts.

If I were to be marking the results of this test then I would give the
highest marks to the solution that had c. similar to:

        MOVE 126                       TO Printer-Part-No
                                          Part-No
        MOVE Table-Quantity(Part-No)   TO Printer-Quantity
        WRITE Printer-Line

and d. as:

        MOVE ZERO         TO Total-Quantity
        MOVE ZERO         TO Total-Parts
        PERFORM VARYING Part-No FROM 1 BY 1 UNTIL Part-No > 999
            IF ( Table-Part(I) > ZERO )
                ADD 1     TO Total-Parts
                ADD Table-Quantity(Part-No) TO Total-Quantity
            END-IF
        END-PERFORM
        COMPUTE Average-Quantity = Total-Quantity / Total-Parts

This would show that the programmer had read through the whole question
before deciding on a design that will produce the actual required
results of parts c) and d).

It would show that the programmer used the information supplied (that
part-numbers are 3 digit) and had been able to conceptualise the
transformation of arrays from one form on input to another form to solve
the problems that exist in produced the required results.

It would be becessary to increment each subscript by 1 if part number
'000' was valid.

If part c. had been coded similar to:

     MOVE 126      TO Part-Code
     MOVE "N"      TO Found-Flag
     PERFORM VARYING Record-No FROM 1 BY 1 
               UNTIL Record-No > 50
                  OR Found-Flag = "Y"
        PERFORM VARYING Group-No FROM 1 BY 1 
                  UNTIL Group-No > 15
                     OR Found-Flag = "Y"
            IF ( Group-Code(Record-No Group-No) = Part-Code  )
                MOVE Group-Quantity(Record-No Group-No)
                            TO Part-Quantity
                MOVE "Y"    TO Found-Flag
            END-IF
         END-PERFORM
     END-PERFORM

then I would give it very low marks.  This indicates that the solution
had been decided before the problem had been fully read.  The structure
is based on the input and _not_ on the requirements of the problem.  The
indications are that the design of the program had been decided when
reading part b) leading to a part c) (above) that is overly complex and
failing to actually solve the required problem.

An additional point would be given if the found-flag had not been coded
and the 'Part-Quantity' had been added to for each occurance of part-no
126.  However this would still make it impossible to determine the
average quantities of the _parts_, as against the average quantity of
the _groups_, without a further transformation into an array that was
either sorted by part number or used the part number as an index. There
is nothing to say that the part-number won't repeat in the input data.

A solution that only used a single array and stored the data
sequentially would get an intermediate score from me as: the 50 is only
to be assumed, there may be more; and the data would need to be sorted
or accumulated by part number before the average quantity can be
determined as it will be necessary to know not only the total quantity
but the number of _different_ part numbers.

As with _all_ programming, it is necessary to design to solve part d)
not just to solve part c) or (worse) just part b) and then hope that the
rest can be fixed later.

I hope that no one will accuse me of 'missing' something here.
```

##### ↳ ↳ Re: Loading Tables

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-12-19T02:48:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<veTT7.3629$XC5.3916@www.newsranger.com>`
- **References:** `<c124eb5e.0112080927.5a5c0938@posting.google.com> <3C1C6722.D2ECB9@Azonic.co.nz>`

```
If I were to be marking the results of this test I'd give Steve, Chaz, ands Rich
passing grades and fail Igal w/a zero grade. She returned a blank Blue Book.
Didn't even attempt to struggle w/a soution or indicate ANY understanding of the
problem.

Of course, nobody but Bill asked her to.

Jack  


In article <3C1C6722.D2ECB9@Azonic.co.nz>, Richard Plinston says...
>
>Igal wrote:
…[88 more quoted lines elided]…
>I hope that no one will accuse me of 'missing' something here.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
