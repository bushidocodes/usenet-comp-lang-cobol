[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# X Occurs 1 To 10 Times Depending On Y ??

_5 messages · 5 participants · 2004-09 → 2004-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### X Occurs 1 To 10 Times Depending On Y ??

- **From:** cctj_82 <cctj_82.1ddidn@mail.codecomments.com>
- **Date:** 2004-09-29T20:13:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1096713992.zXGPew9W5jNUhJqxzLYpNw@tng>`

```

how can we explain the statement ?
X OCCURS 1 TO 10 TIMES DEPENDING ON Y

what's the meaning of 'DEPENDING ON'

thanks, it's better to give a example.
```

#### ↳ Re: X Occurs 1 To 10 Times Depending On Y ??

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-10-02T15:33:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9I73mrXeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<1096713992.zXGPew9W5jNUhJqxzLYpNw@tng>`

```
.    Am  29.09.04
schrieb  cctj_82.1ddidn@mail.codecomments.com (cctj_82)
    auf  /COMP/LANG/COBOL
     in  1096713992.zXGPew9W5jNUhJqxzLYpNw@tng
  ueber  X Occurs 1 To 10 Times Depending On Y ??

c81> X OCCURS 1 TO 10 TIMES DEPENDING ON Y
c81>
c81> what's the meaning of 'DEPENDING ON'

   an example would be like this:

--------- schnipp -----------------------------------------

   identification division.
   program-id.
       occurs-example.

   data division.
   working-storage section.

   01  a-string-record.
       02  its-length  PIC 9(4) comp.
       02  the-string.
           03 filler pix x occurs 1 to 80 times
                             depending on its-length.


   procedure division.
   the-only section.
   its-beginning.
       move 80 to its-length
       move all '8' to the-string
       move 20 to its-length
       move all 'twenty' to the-string
       display the-string
       move 80 to its-length
       display the-string
       perform with test after
            varying its-length from 5 by 5
            until its-length >= 80
         display the-string
       end-perform
       .
    the-end.
       stop run.

------------------ schnapp --------------------------------


    When you compile and run that program, you will see that the  
variable "the-string" is treated as an item of varying length,  
depending on the value in "its-length". In this example, "the-string"  
is treated as an item of 80 or 20 characters in length, then in the  
PERFORM-loop as an item of 5, 10, 15, ... upto 80 characters in  
length.

    In case you didn't know, the clause (option) "all" in the MOVE  
statement makes it a repeated MOVE of the sending item, until the  
receiving item is filled to its length.



Yours,
Lï¿½ko Willms
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --
```

#### ↳ Re: X Occurs 1 To 10 Times Depending On Y ??

- **From:** rjones0@hotmail.com (Robert Jones)
- **Date:** 2004-10-02T12:50:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dd8322.0410021150.b7fce2f@posting.google.com>`
- **References:** `<1096713992.zXGPew9W5jNUhJqxzLYpNw@tng>`

```
cctj_82 <cctj_82.1ddidn@mail.codecomments.com> wrote in message news:<1096713992.zXGPew9W5jNUhJqxzLYpNw@tng>...
> how can we explain the statement ?
> X OCCURS 1 TO 10 TIMES DEPENDING ON Y
…[3 more quoted lines elided]…
> thanks, it's better to give a example.

Hello,

The "DEPENDING ON" phrase of the OCCURS clause of a data description
specifies the current logical number of occurrences that the table
contains.  It is a standard construct of COBOL and is explained in the
language reference manuals and application programmer guides of all
the main compilers.  The value of "Y" is a numeric value specifying
the current number of occurrences of the the table elements.  However,
despite it implying that the table takes less space when the value of
"Y" is less than "10", this is not true, the table always uses
physical space for ten occurrences.  The difference from an OCCURS
clause without the DEPENDING ON phrase is applicable when
moving/comparing the table to other data items or reading and writing
to a file, when only the logical number of occurrences are moved,
compared, read or written.

Robert
```

##### ↳ ↳ Re: X Occurs 1 To 10 Times Depending On Y ??

- **From:** "Russell Styles" <rws0203@comcast.net>
- **Date:** 2004-10-03T02:21:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9I6dna75c-HtB8LcRVn-tg@giganews.com>`
- **References:** `<1096713992.zXGPew9W5jNUhJqxzLYpNw@tng> <6dd8322.0410021150.b7fce2f@posting.google.com>`

```

"Robert Jones" <rjones0@hotmail.com> wrote in message
news:6dd8322.0410021150.b7fce2f@posting.google.com...
> cctj_82 <cctj_82.1ddidn@mail.codecomments.com> wrote in message
news:<1096713992.zXGPew9W5jNUhJqxzLYpNw@tng>...
> > how can we explain the statement ?
> > X OCCURS 1 TO 10 TIMES DEPENDING ON Y
…[21 more quoted lines elided]…
> Robert

    The bit about how much space the array takes up can differ
depending on implementation and compiler options.

    If your compiler does allow variable length arrays (eg Microfocus and
ODOSLIDE), be careful.  Some verbs might not work as you expect.  I
think that I remember that the initialize verb was not useable, at least
with
the old 16 bit compiler.  I have not tried it with NetExpress.

    To make an array truly variable length, you had to use memory
allocation,
not working storage.

    But it could be made to work.
```

###### ↳ ↳ ↳ Re: X Occurs 1 To 10 Times Depending On Y ??

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-10-03T13:26:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6T7d.479671$yk.77262@news.easynews.com>`
- **References:** `<1096713992.zXGPew9W5jNUhJqxzLYpNw@tng> <6dd8322.0410021150.b7fce2f@posting.google.com> <9I6dna75c-HtB8LcRVn-tg@giganews.com>`

```
As far as I know, an ODO *never* (at least in any standard conforming) compiler 
impacts the amount of storage allocated - only the amount "currently 
accessible".

The Micro Focus ODOSLIDE directive attempts to emulate an IBM mainframe 
*extension* to the Standard that allows an ODO to be nested within another ODO 
and/or to have "fixed" data following an ODO item, e.g

01  Full-Item-type1.
    05  ODO1.
          10  Elem1  occurs  1 to 10 times depending on Some-Counter
                 15  Elem2  occurs 1 to 100 times depending on Other-Counter
                        Pic X.

01 Full-Item-type2.
     05  ODO2.
           10 Elem3  Occurs 1 to 10 times depending on Counter3
                Pic X.
      05  Post-ODO-Fixed   Pic X(10).

***

From reading the "Substantive Change Potentially effecting" section of the '85 
Standard, one or both of these were "allowed" in the '74 Standard, but not well 
defined there (or at least the rules prohibiting them wasn't clear).

In both cases, the amount of storage "required" for Full-item-type1 and 
Full-item-type2 is (still - just like standard conforming ODO's) "fixed" - but 
the amount of storage accessible is dependent upon the current values of the 
various counters.   Also, whether the item is used as a "sending" or "receiving" 
item can impact what is accessible - but not the amount of storage allocated.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
