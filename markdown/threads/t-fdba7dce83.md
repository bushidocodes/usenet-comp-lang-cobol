[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fillers????

_8 messages · 7 participants · 2001-10_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Fillers????

- **From:** JONESEY <mrjones_101@hotmail.com>
- **Date:** 2001-10-18T20:28:40+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com>`

```
So this is probably a stupid question....but could someone explain fillers to me in sequential files...why do we need them and how do you know how
many to put in??

Thanks
```

#### ↳ Re: Fillers????

- **From:** "Ron" <Ron@NoSpamForMe.Com>
- **Date:** 2001-10-18T15:48:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9qnf77$sef$1@suaar1ac.prod.compuserve.com>`
- **References:** `<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com>`

```
FILLER is any part of the record description that is undefined
or any part of the record description you do not intend to use in
your program. FILLER *DOES NOT* necessarily mean the data
contains SPACES.  RTM.

=================================================================

"JONESEY" <mrjones_101@hotmail.com> wrote in message
news:tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com...
> So this is probably a stupid question....but could someone explain fillers
to me in sequential files...why do we need them and how do you know how
> many to put in??
>
> Thanks
```

##### ↳ ↳ Re: Fillers????

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-18T22:34:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BCF5A70.C995AE0D@home.com>`
- **References:** `<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com> <9qnf77$sef$1@suaar1ac.prod.compuserve.com>`

```


Ron wrote:

> FILLER is any part of the record description that is undefined
> or any part of the record description you do not intend to use in
…[11 more quoted lines elided]…
> > Thanks

Well that tells you what a FILLER is but doesn't answer your 'Why".

Firstly they don't apply JUST to sequential files, but all - Relative, ISAM and
Sequential. You design a system :-

FD Customerfile. (the "Old' file)
01 CustomerRecord.
 05 Cus-PrimeKey                pic x(05).
 05 Cus-Address.
   10 Cus-AddressLine1        pic x....
   10 Cus-Address Line 2 etc.....

Having run the system for say eighteen months, somebody suggests, 'It would be
nice to have the Customer's Current Balance in the record". You are stumped -
you don't have any spare space.

To get over the above you now have to create a "New"file :-

FD OldCustomerfile. (the "Old' file)
01 OldCustomerRecord.
 05 OldCus-PrimeKey                pic x(05).
 05 OldCus-Address.
   10 OldCus-AddressLine1        pic x....
   10 OldCus-Address Line 2 etc.....

FD Customerfile. (the "New' file)
01 CustomerRecord.
 05 Cus-PrimeKey                pic x(05).
 05 Cus-Address.
   10 Cus-AddressLine1        pic x....
   10 Cus-Address Line 2 etc.....
 05 Cus-Balance                    pic s9(06)v9(02).

1. Read in Old file
2. Move fields to "New" record
3. Initialize Cus-Balance
4. write Newfile record

Assuming some 30 programs use this file format - you now have 30 re-compiles.

The other alternative is take the "Old" record and anticipate you "might" be
asked to add information as the system progresses. So your 'Old' record looks
like :-

   10 OldCus-AddressLine1        pic x....
   10 OldCus-Address Line 2 etc.....
    10 filler                                    pic x(20).

and in the "New" record you show :-

   10 Cus-Address Line 2 etc.....
 05 Cus-Balance                     pic 9(06)v9(02)    = 8 chars.
 05 filler                                   pic x(12).

You still have to go through the conversion routine above, ensuring you
initialize Cus-Balance. However, if ONLY two of your programs access that
Cus-Balance field, it is only those two programs that immediately need to be
recompiled. For peace of mind of course, you make sure all get recompiled.

FILLERS are much more likely to be used with "historical" or Master files,
primarily ISAMs, but can occur in sequentials if needed.  How much FILLER space
do you need - depends upon the complexity of the system - you might get away
with pic x(20) or somebody else could allocate pic x(100). But whichever you do,
change the record format and you still have to go through the conversion
routines above.

I assume you are a student - so there are two possibilities.

a) Your instructor has given you a test data file to use as input :-

123456 Smith          John J.            30.00
234679 Brown         Michael, B.    29.00

and in the record format he has included FILLERS so that you can easily see the
fields.

b) You are being asked to display or prepare a print line :-

01 DisplayPrintRecord.
    05 IdNumber                     pic x(06).
    05 filler                               pic x(03).
    05 LastName                     pic x(20).
    05 filler                               pic x(01).
    05 FirstNames                    pic x(10).
    05 filler                               pic x(03).
    05 HourlyRate                    pic zz.99  blank when zero.

Jimmy, Calgary AB
```

#### ↳ Re: Fillers????

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-23T16:06:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RzgB7.39697$ev2.46783@www.newsranger.com>`
- **References:** `<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com>`

```
On Thu, 18 Oct 2001 20:28:40 +0100, in article
<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com>, JONESEY stated 
>
>So this is probably a stupid question....but could someone explain fillers to me in sequential files...why do we need them and how do you know how
>many to put in??
>
>Thanks

In a file you may want a filler to reserve some unused space for future use,
or/and as a work area.  

A second reason for a filler is if you have an area used for more than one thing
and it may have a redfine statement.  

Sometimes a file may have more than one record type and for one or more record
types there may be space that is unused.
```

##### ↳ ↳ Re: Fillers????

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-23T14:16:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bpiB7.11201$v21.1901265@news20.bellglobal.com>`
- **References:** `<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com> <RzgB7.39697$ev2.46783@www.newsranger.com>`

```
Filler is data space that is never referenced by a name.  It may be used by
other programs, it may be reserved for future use, or it may be someone
elses file and you do not have a clue what it is because you were never
told.  Often, it is obsolete data. It could also be referenced by a
different method ... a higher level data name or a redefines clause.

You need them because there is something in the field at that spot, and if
you do not put something in your record description, the data you are using
will not be alligned in the buffer correctly.

Often, with output, you fill a line with spaces, then populate the
non-filler portions of the record with data.  The filler remains as blank,
so that you can read it ... IE-spaces between the data column on successive
lines of output.

"Charles" <nospam@newsranger.com> wrote in message
news:RzgB7.39697$ev2.46783@www.newsranger.com...
> On Thu, 18 Oct 2001 20:28:40 +0100, in article
> <tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com>, JONESEY stated
> >
> >So this is probably a stupid question....but could someone explain
fillers to me in sequential files...why do we need them and how do you know
how
> >many to put in??
> >
> >Thanks
>
> In a file you may want a filler to reserve some unused space for future
use,
> or/and as a work area.
>
> A second reason for a filler is if you have an area used for more than one
thing
> and it may have a redfine statement.
>
> Sometimes a file may have more than one record type and for one or more
record
> types there may be space that is unused.
>
>
```

#### ↳ Re: Fillers????

- **From:** "Editor" <Editor@aboutlegacycoding.com>
- **Date:** 2001-10-23T16:16:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r4j6c$1mi3$1@allbad.news.cais.net>`
- **References:** `<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com>`

```
Way back when I used to do Tech Support, I had a sign on my desk that said:
"There are no stupid questions, only stupid mistakes!"

I think this question and Donald's answer illustrate this point beautifully!
```

##### ↳ ↳ Re: Fillers????

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-10-24T11:52:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dYxB7.52$C45.8935@dfiatx1-snr1.gtei.net>`
- **References:** `<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com> <9r4j6c$1mi3$1@allbad.news.cais.net>`

```
Editor <Editor@aboutlegacycoding.com> wrote in message
news:9r4j6c$1mi3$1@allbad.news.cais.net...
> Way back when I used to do Tech Support, I had a sign on my desk that
said:
> "There are no stupid questions, only stupid mistakes!"

Back when I managed Tech Support,  I had a version of this I used with my
programmers (which earned me no brownie points):

"There is no such thing as user error, there is only a missed edit."

MCM
```

###### ↳ ↳ ↳ Re: Fillers????

- **From:** "Editor" <Editor@aboutlegacycoding.com>
- **Date:** 2001-10-24T09:45:24-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9r6glg$5sn$1@allgood.news.cais.net>`
- **References:** `<tabust8jr54qdntsttce91hlvd4hg6bn5o@4ax.com> <9r4j6c$1mi3$1@allbad.news.cais.net> <dYxB7.52$C45.8935@dfiatx1-snr1.gtei.net>`

```
LOL
I LIKE it, a lot - thanks for sharing!
I may have to make up another sign!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
