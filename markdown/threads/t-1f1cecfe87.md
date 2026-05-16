[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Urgent help - A implementation question -

_12 messages · 9 participants · 1998-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Urgent help - A implementation question -

- **From:** "Me & Myself" <infoagetech@yahoo.com>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36423b19.0@lightning.ica.net>`

```
To all philosophers out there:

I need to implement a scheme where each record in a DB/2 table contains 6
flags.
Each of these flags can be on or off (i.e. containing 1 or 0 respectively).
 We don't wanna store these 6 flags in 6 different one-byte columns.
Rather we combine them into a single INTEGER field on
the table using a binary translation scheme such that

e.g.   000001  will store as  1
          000010 will store as  2
          000011 will store as  3
          ....
          000111 will store as 7 and so on.

But I find this scheme awkward since we have to constantly convert between
the numeric
representation and the binary representation the flags to see which flag is
set
when retrieving the records.

Any help is greatly appreciated.
M&M.
```

#### ↳ Re: Urgent help - A implementation question -

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71tg9m$kop$1@news.igs.net>`
- **References:** `<36423b19.0@lightning.ica.net>`

```
Me & Myself wrote in message <36423b19.0@lightning.ica.net>...
>To all philosophers out there:


If the method is awkward, why do you want to do it that way? Surely
a difference of five bytes per record is not going to blow your disk
storage budget in this day and age.  Store the data in a format that
is compatible, and just move it back and forth.

>
>I need to implement a scheme where each record in a DB/2 table contains 6
…[22 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Urgent help - A implementation question -

- **From:** JeffreyFarkas@earthlink.net (Jeff Farkas)
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.10ac331199cece27989682@news.earthlink.net>`
- **References:** `<36423b19.0@lightning.ica.net> <71tg9m$kop$1@news.igs.net>`

```
In article <71tg9m$kop$1@news.igs.net>, donald@willmack.com says...
> Me & Myself wrote in message <36423b19.0@lightning.ica.net>...
> >To all philosophers out there:
…[5 more quoted lines elided]…
> is compatible, and just move it back and forth.

From what I see it seems like a solution in search of a problem. 

There two ways of making this work, IMO, are:

1) Set up a small program that will perform the numeric conversions. 

2) Set up the field as a six characters and not integer. The following
logic will work:

  nnnnny = 1 is on
  nnnnnn = 1 is off

  nnnnyn = 2 is on
  nnnnnn = 2 is off
.......

I have seen something like this used and it can be made to work.

> 
> >
…[26 more quoted lines elided]…
> 
```

#### ↳ Re: Urgent help - A implementation question -

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3642747e.0@news1.ibm.net>`
- **References:** `<36423b19.0@lightning.ica.net>`

```

Me & Myself <infoagetech@yahoo.com> wrote in message
news:36423b19.0@lightning.ica.net...
>To all philosophers out there:
>
…[17 more quoted lines elided]…
>when retrieving the records.

Instead of a integer use a text string of 6 digits:
"000001" for 1
"000010" for 2
etc

then it is easy to test if you define the host variable like this:
02  host-flags.
      03  host-flag-bit   pic 9 occurs 6 times.
```

#### ↳ Re: Urgent help - A implementation question -

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36432d1c.0@news2.uswest.net>`
- **References:** `<36423b19.0@lightning.ica.net>`

```
What version of DB2 are you using?


Me & Myself wrote in message <36423b19.0@lightning.ica.net>...
>To all philosophers out there:
>
…[23 more quoted lines elided]…
>
```

#### ↳ Re: Urgent help - A implementation question -

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3644348a.5392975@nntp.ix.netcom.com>`
- **References:** `<36423b19.0@lightning.ica.net>`

```
On Thu, 5 Nov 1998 18:59:03 -0800, "Me & Myself"
<infoagetech@yahoo.com> wrote:

>To all philosophers out there:
>
…[18 more quoted lines elided]…
>

umm, i think the newest cobol standard will have something with
bit format.

gvwmoore@ix.spam.netcom.com to reply remove the spam
```

##### ↳ ↳ Re: Urgent help - A implementation question -

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3643A58E.E0B708C3@ix.netcom.com>`
- **References:** `<36423b19.0@lightning.ica.net> <3644348a.5392975@nntp.ix.netcom.com>`

```
Why is saving 5 bytes per row is so important you want to incur the overhead and
confusion of storing 6 switches in one byte?  This method also guarantees you
can never do anything like SELECT * FROM YOUR_TAB WHERE SWITCH1 = 'Y' ... This
is nothing but a maintainance nightmare.

G Moore wrote:

> On Thu, 5 Nov 1998 18:59:03 -0800, "Me & Myself"
> <infoagetech@yahoo.com> wrote:
…[26 more quoted lines elided]…
> gvwmoore@ix.spam.netcom.com to reply remove the spam
```

#### ↳ Re: Urgent help - A implementation question -

- **From:** "Hugh Candlin" <hugh.candlin@getridofspam.worldnet.att.net>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71u57b$7qn@bgtnsc03.worldnet.att.net>`
- **References:** `<36423b19.0@lightning.ica.net>`

```

Me & Myself wrote in message <36423b19.0@lightning.ica.net>...
>To all philosophers out there:
>
…[17 more quoted lines elided]…
>when retrieving the records.

I  think this is what you are looking for:

01  DB2-RUBE-GOLDBERG-TABLE.
      05  DB2-TABLE-FLAG        PIC 99.
             88  DB2-TABLE-FLAG-1-IS-ON  VALUES ARE
                   1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
31, 33,
                   35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61,
63.
              88  DB2-TABLE-FLAG-2-IS-ON  VALUES ARE
                    2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30,
31,
                    34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59,
62, 63.
              88  DB2-TABLE-FLAG-3-IS-ON  VALUES ARE
                    4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30,
31,
                    36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60,61,
62, 63.
              88  DB2-TABLE-FLAG-4-IS-ON  VALUES ARE
                     8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29,
30, 31,
                     40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61,
62, 63.
              88  DB2-TABLE-FLAG-5-IS-ON  VALUES ARE
                     16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31,
                     48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
62, 63.
              88  DB2-TABLE-FLAG-6-IS-ON  VALUES ARE
                     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,, 44,
45, 46, 47,
                     48, 49, 50, 51, 52, 53, 54, 55. 56, 57, 58, 59, 60, 61,
62, 63.

       (YOUR OTHER TABLE DATA GOES HERE)

*    TO SET FLAG #1 ON ADD   1 TO DB2-TABLE-FLAG
*    TO SET FLAG #2 ON ADD   2 TO DB2-TABLE-FLAG
*    TO SET FLAG #3 ON ADD   4 TO DB2-TABLE-FLAG
*    TO SET FLAG #4 ON ADD   8 TO DB2-TABLE-FLAG
*    TO SET FLAG #5 ON ADD 16 TO DB2-TABLE-FLAG
*    TO SET FLAG #6 ON ADD 32 TO DB2-TABLE-FLAG

*    TO SET FLAG #1 OFF SUBTRACT   1 FROM DB2-TABLE-FLAG
*    TO SET FLAG #2 OFF SUBTRACT   2 FROM DB2-TABLE-FLAG
*    TO SET FLAG #3 OFF SUBTRACT   4 FROM DB2-TABLE-FLAG
*    TO SET FLAG #4 OFF SUBTRACT   8 FROM DB2-TABLE-FLAG
*    TO SET FLAG #5 OFF SUBTRACT 16 FROM DB2-TABLE-FLAG
*    TO SET FLAG #6 OFF SUBTRACT 32 FROM DB2-TABLE-FLAG

I typed all the values to help you see the patterns.  Feel free to modify
the definitions for efficiency.  eg Anything over 31 means #6 is ON,
so you don't really need the level 88 values spelled out.

Don't set a flag OFF unless you know that flag is ON.
Otherwise you will corrupt that table entry's flags.

ie If Flag #3 is ON, and all others are OFF, the DB2-TABLE-FLAG value will
be 4.
    If you set Flag #1 to OFF (by subtracting 1), the new value will be 3,
    which would incorrectly indicate that Flag #1 and Flag #2 were ON.
```

#### ↳ Re: Urgent help - A implementation question -

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3644349F.12C13905@zip.com.au>`
- **References:** `<36423b19.0@lightning.ica.net>`

```
DB2:  Hmmm I know that there is a way to put an exit into the DB2 system
expand details so that the database could contain the bit fields and
return it as a string field.  Not my cup of tea unless there was a huge
space benefit.

It might be a perfect complementary program written in C (it has bit
manipulation) or assembler.  Write it once and call it from all your
programs to expand your field.

Me & Myself wrote:
> 
> To all philosophers out there:
…[21 more quoted lines elided]…
> M&M.
```

#### ↳ A implementation question (redefined)

- **From:** "Me & Myself" <infoagetech@yahoo.com>
- **Date:** 1998-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36465ad3.0@lightning.ica.net>`
- **References:** `<36423b19.0@lightning.ica.net>`

```
Hi group:
First of all, let me say how grateful I am to all of you who have spent time
responding to my posting.
Please allow me response to your postings a bit.

1) The reason why I don't want to implement this as 6 separate flags is
because my SQL will have to read
something like

    select ....
... where FLAG1 = 1
          or FLAG2 = 1
          or FLAG 3 = 1 ....etc.
and with the million-plus-row table that I have I will have to define all
these flags into the primary index, unless I don't care about table scan
which, for my online system, is not even an option.  I guess this is to
address Donald Tees' point.
2) I think implementing my problem using explicit binary scheme as Leif
Svalgaard suggested may be the one heuristic solution.  That is to use FLAG
= 000000 where each digit represent a flag 0/1.  This way I only need to put
this one flag into the primary index.  I thought about this method but never
actually fully materialize my thought.
3) To Chris Osborne, I use version 5 of DB2 on the MVS system
4) To G Moore, I'm dying to have some kind of bit operation in COBOL, but
without much hope.

Having addressed all the major points, I think I am leaning towards solution
#2 above.  Can you please reply this post or send me email directly telling
me if this is the optimum solution or if you have any other suggestions.  If
you agree with me, can you please tell me why my ...intelligent !@$#%$^....
boss kept insisting that representing all flags into an integer as I first
posted was the best solution?

Again, I am indebted to all of you.
M&M


Me & Myself wrote in message <36423b19.0@lightning.ica.net>...
>To all philosophers out there:
>
…[23 more quoted lines elided]…
>
```

##### ↳ ↳ Re: A implementation question (redefined)

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<727e3u$l8r$1@news.igs.net>`
- **References:** `<36423b19.0@lightning.ica.net> <36465ad3.0@lightning.ica.net>`

```
If I understand you correctly, you want to index on *one* variable
in one program, and on several in the other. In order to do that,
you were thinking in terms on an integer which would be a specific
value in one program, thus representing (as a specific integer) one
specific combination of flags in the one index, yet could be split
out into several different flags in a different program.  Is that a
realistic statement of the problem?

If it is, then my comment is still valid.  What I was implying is that
the problem is really only in the fact that you want binary bits as
your flags.  As far as the indexing goes, you could simply use
bytes instead, and not worry about "bit picking".  In the one place,
you index a variable that is an ASCII string looking like "YYNNYNYN",
where in the other you define it as eight separate bytes. The
*only* advantage that I can see of using numbers is that you
save 7 bits per flag. I would suspect that in a spreadsheet, you
would not save anything, as it is going to convert every logic bit into
a number anyway.  I am pretty sure that most databases do not
allocate only a single bit for a logical value.

Me & Myself wrote in message <36465ad3.0@lightning.ica.net>...
>Hi group:
>First of all, let me say how grateful I am to all of you who have spent
time
>responding to my posting.
>Please allow me response to your postings a bit.
…[15 more quoted lines elided]…
>= 000000 where each digit represent a flag 0/1.  This way I only need to
put
>this one flag into the primary index.  I thought about this method but
never
>actually fully materialize my thought.
>3) To Chris Osborne, I use version 5 of DB2 on the MVS system
…[3 more quoted lines elided]…
>Having addressed all the major points, I think I am leaning towards
solution
>#2 above.  Can you please reply this post or send me email directly telling
>me if this is the optimum solution or if you have any other suggestions.
If
>you agree with me, can you please tell me why my ...intelligent !@$#%$^....
>boss kept insisting that representing all flags into an integer as I first
…[11 more quoted lines elided]…
>>Each of these flags can be on or off (i.e. containing 1 or 0
respectively).
>> We don't wanna store these 6 flags in 6 different one-byte columns.
>>Rather we combine them into a single INTEGER field on
…[10 more quoted lines elided]…
>>representation and the binary representation the flags to see which flag
is
>>set
>>when retrieving the records.
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: A implementation question (redefined)

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36474492.0@news1.ibm.net>`
- **References:** `<36423b19.0@lightning.ica.net> <36465ad3.0@lightning.ica.net> <727e3u$l8r$1@news.igs.net>`

```
>Me & Myself wrote in message <36465ad3.0@lightning.ica.net>...

>>Having addressed all the major points, I think I am leaning towards
solution
>>#2 above.  Can you please reply this post or send me email directly
telling
>>me if this is the optimum solution or if you have any other suggestions.
If
>>you agree with me, can you please tell me why my ...intelligent
!@$#%$^....
>>boss kept insisting that representing all flags into an integer as I first
>>posted was the best solution?

This is for your intelligent !@$#%$^ (sic) boss:
There is no need to pack all the flags into an integer.
It is a perfectly good solution to simply store the six flags as
a six-character field. Each flag being either "Y"/"N" or "1"/"0"
or something like that.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
