[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Indexed sequential file read question

_15 messages · 12 participants · 1999-06_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Indexed sequential file read question

- **From:** jonathan.vaughan@nocack.bigfoot.com (Jonathan Vaughan)
- **Date:** 1999-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk>`

```
I have an indexed sequential file in the format

01 rec-key
  03 pr-ref	pic 9(8).
  03 end-date   pic 9(6).  (this is in format ddmmyy)
01 blah
01 blah

Where the key field is rec-key.

How can I read through this file in ascending order of pr-ref but descending
order of end-date (there are several end-dates for each pr-ref)?

Thanks

Jon
```

#### ↳ Re: Indexed sequential file read question

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376d2ad8@news3.us.ibm.net>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk>`

```

Jonathan Vaughan <jonathan.vaughan@nocack.bigfoot.com> wrote in message
> I have an indexed sequential file in the format
>
…[8 more quoted lines elided]…
> How can I read through this file in ascending order of pr-ref but
descending
> order of end-date (there are several end-dates for each pr-ref)?

assuming that the file is created in ascending order on rec-key, consider
the
following end-dates for given pr-ref:

010100   Jan 1 2000
010199   Jan 1 1999
010499   April 1 1999
020299   Feb 2 1999

These are in the order given (ascending within rec-key).
You want to read them in this order?:

020299  Feb 2 1999
010499  April 1 1999
010199  Jan 1 1999
010100  Jan 1 2000

which is descending on end-date (and is what you asked for)

or in this one?:

010100  Jan 1 2000
010499  April 4 1999
020299  Feb 2 1999
010199  Jan 1 1999

which is what I think you want.
```

#### ↳ Re: Indexed sequential file read question

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<J7fb3.3110$T25.83260@dfiatx1-snr1.gtei.net>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk>`

```
You can't read this file in this program, using this SELECT and FD, in any
order other than current key order.

You'll have to sort the file again, on your new key. You can read each
record, RELEASE it to a SORT, then RETURN all the records in the new order;
or SORT the file
USING..GIVING.. and then process the GIVING file sequentially.
```

##### ↳ ↳ Re: Indexed sequential file read question

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kjv4i$48f@dfw-ixnews6.ix.netcom.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk> <J7fb3.3110$T25.83260@dfiatx1-snr1.gtei.net>`

```
I didn't see the SELECT/ASSIGN for this file.  My GUESS is that Michael is
correct that you can't do it.  HOWEVER, if your SELECT/Assign has
   "pr-ref" as the primary key and
   "end-date" as an alternate key

and does NOT define "rec-key" as the primary key (as stated in the original
note - but without the Select/Assign, that may not be true),

then I think you can do what you want.
```

##### ↳ ↳ Re: Indexed sequential file read question

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376dab83@news3.us.ibm.net>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk> <J7fb3.3110$T25.83260@dfiatx1-snr1.gtei.net>`

```
Even though there might be several end-dates there probably is not VERY many
(say less than a hundred) in which case you just read them all and sort them
internally in any order you want.

Michael Mattias <michael.mattias@gte.net> wrote in message
news:J7fb3.3110$T25.83260@dfiatx1-snr1.gtei.net...
> You can't read this file in this program, using this SELECT and FD, in any
> order other than current key order.
>
> You'll have to sort the file again, on your new key. You can read each
> record, RELEASE it to a SORT, then RETURN all the records in the new
order;
> or SORT the file
> USING..GIVING.. and then process the GIVING file sequentially.
…[25 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Indexed sequential file read question

- **From:** Bob Berman <bberman@netbox.com>
- **Date:** 1999-06-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<377184C6.26CB@netbox.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk> <J7fb3.3110$T25.83260@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> You can't read this file in this program, using this SELECT and FD, in any
…[26 more quoted lines elided]…
> >

With end-date in format ddmmyy, you will never be able to sort by date.
May 30,1999 (300599) would be greater than june 1, 1999 (010699).  Try
format yymmdd...works much better.  I know it is awkward for British
people, but what isn't ?

Bob
```

#### ↳ Re: Indexed sequential file read question

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7WBb3.2209$6Q3.857@news3.mco>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk>`

```
The keys must be in that order, or you must sort them into the order you
want
and write out the key fields, then read that (or return) and randomly read
the ISAM file.

Jonathan Vaughan wrote in message ...
>I have an indexed sequential file in the format
>
…[8 more quoted lines elided]…
>How can I read through this file in ascending order of pr-ref but
descending
>order of end-date (there are several end-dates for each pr-ref)?
>
…[7 more quoted lines elided]…
>Please remove nocack. to reply
```

#### ↳ Re: Indexed sequential file read question

- **From:** Alex Romaniuk <ales.romaniuk@zag.si>
- **Date:** 1999-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376DD238.720A@zag.si>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk>`

```
Jonathan Vaughan wrote:
> 
> I have an indexed sequential file in the format
…[19 more quoted lines elided]…
> Please remove nocack. to reply
You can solve this using two methods:
1. Sorting before reading

SELECT SORTFILE ASSIGN TO "SORTFILE.SOR".
...
...
SD SORTFILE.
01 SORT-Rec.
   03 SORT-Pr-Ref 	PIC 9(8).
   03 SORT-End-Date 	PIC 9(6).

SORT SORTSD ON DESCENDING KEY SORT-Rec
               ----------



2. Using secondary reverse-key

01 rec-key
   03 pr-ref     pic 9(8).
   03 end-date   pic 9(6).
01 end-date-reverse PIC 9(6).


then
   move this-date to end-date
   compute end-date-reverse = 999999 - this-date


then
   START MYFILE KEY NOT < END-DATE-REVERSE
```

#### ↳ Re: Indexed sequential file read question

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376fc0d4.835257@news.enteract.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk>`

```
Assuming you have access to all programs that use this file, you could
change the way the date is stored so that it will be in the order you
want.  IOW, use an algorithm to change a high date into a low date,
and vice versa when writing records to the file.  Then just convert
the date before you print/use it after reading.

For example, change the date field to be pic 9(8).  Then when writing
records to the file, subtract your date from 99999999 and store the
result in the date field.  Then after you read the records, add
99999999 to the date field.  

Kinda wacky but it would work if the main use of this file is
accessing it in Descending date order. 

Paul

On Sun, 20 Jun 1999 17:00:11 GMT, jonathan.vaughan@nocack.bigfoot.com
(Jonathan Vaughan) wrote:

>I have an indexed sequential file in the format
>
…[13 more quoted lines elided]…
>Jon

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

##### ↳ ↳ Re: Indexed sequential file read question

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<376FCD48.52DCDB2B@home.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk> <376fc0d4.835257@news.enteract.com>`

```
PAL3000 wrote:
> 
> Assuming you have access to all programs that use this file, you could
…[37 more quoted lines elided]…
> words REMOVETHIS from my email address

No, your suggestion isn't the least bit wacky - I do exactly that.
Producing calculations and writing them to an indexed file with
alternate keys, I then have to produce a standard summary report by
various criteria :-

	a) Life expectancy (ascending) - the date this item is likely
	   to expire - so you get those that are 'forecast' to expire
	   in the current year, first
	b) Losses greater than     40 mils per year
	   Losses	..	   25 mils per year
	   Total Loss greater than 25 mils etc......

For Group (b) I create a "negative key descending" - losses being shown
in descending sequence for each sub-title - it works fine.
```

##### ↳ ↳ Re: Indexed sequential file read question

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FaQb3.2490$LI5.228335@axe.netdoor.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk> <376fc0d4.835257@news.enteract.com>`

```
PAL3000 wrote in message <376fc0d4.835257@news.enteract.com>...
>Assuming you have access to all programs that use this file, you could
>change the way the date is stored so that it will be in the order you
…[7 more quoted lines elided]…
>99999999 to the date field.


Close, but no cigar.  Subtract the result from 99999999 again to undo a
nine's complement date.

Our shop has a file of rate records in which the last field in the key is a
nine's complement date representing when the rate went/goes into effect.
Before issuing a START statement we create a nine's complement of the date a
customer used our client's service.  The READ NEXT will pick up the rate
record with the most recent change but not a rate change going into effect
in the future.

Warren Porter -- Remove numbers to reply.
Chessplayers make better mates.
```

###### ↳ ↳ ↳ Re: Indexed sequential file read question

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3770ddfa.5228212@news.enteract.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk> <376fc0d4.835257@news.enteract.com> <FaQb3.2490$LI5.228335@axe.netdoor.com>`

```
On Tue, 22 Jun 1999 13:00:02 -0500, "Warren Porter"
<warrenp123@netdoor123.com> wrote:


>
>Close, but no cigar.  Subtract the result from 99999999 again to undo a
>nine's complement date.
>


What a coincidence!  I was lighting my cigar when I typed my message,
and that is what caused me to type ADD instead of subtract. : )_


--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

##### ↳ ↳ Re: Indexed sequential file read question

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-ZmdcJbw3zv5V@Dwight_Miller.iix.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk> <376fc0d4.835257@news.enteract.com>`

```
On Tue, 22 Jun 1999 17:01:51, pduboisREMOVETHIS@enteract.com (PAL3000)
wrote:

> For example, change the date field to be pic 9(8).  Then when writing
> records to the file, subtract your date from 99999999 and store the
> result in the date field.  Then after you read the records, add
> 99999999 to the date field.  
>

I know what you mean, but you didn't say it! <G>

Read that again slowly.  

take 19990201 for example.  

99999999 - 19990201 = 80009798
80009898 + 99999999 = 180009797

What I think you mean was subtract the "date" read from the file from 
99999999

99999999 - 80009798 = 19990201 

No addition required <G>. 

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Indexed sequential file read question

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-06-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-GqrBsKCVJRPE@Dwight_Miller.iix.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk> <376fc0d4.835257@news.enteract.com> <Jl0PnHJ5PvPd-pn2-ZmdcJbw3zv5V@Dwight_Miller.iix.com>`

```
On Tue, 22 Jun 1999 18:29:57, redsky@ibm.net (Thane Hubbell) wrote:

> On Tue, 22 Jun 1999 17:01:51, pduboisREMOVETHIS@enteract.com (PAL3000)
> wrote:
…[14 more quoted lines elided]…
> 80009898 + 99999999 = 180009797

I typoed that 8000979 + 99999999 = 180009797


> 
> What I think you mean was subtract the "date" read from the file from 
…[14 more quoted lines elided]…
> http://www.geocities.com/Eureka/2006/

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Indexed sequential file read question

- **From:** scottp4-remove-this-to-reply@mindspring.com (Scott Peterson)
- **Date:** 1999-06-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37735a1d.27043867@news.mindspring.com>`
- **References:** `<slrn7mq7cs.tq.jonathan.vaughan@turnip.clara.co.uk>`

```
jonathan.vaughan@nocack.bigfoot.com (Jonathan Vaughan) wrote:

>I have an indexed sequential file in the format
>
…[10 more quoted lines elided]…
>

Jon,

Even if you could make this work this would be pretty ugly. You'd be
bouncing all over the file for each sequential read on pr-ref. to find
the correct sequence on the date.

I've had to handle this in two different ways.  The better way was
sort the file and the process the whole thing sequentially.  

In another situation where that was not possible, I've read the file
sequentially and for each pr-ref, loaded all the records into a
two-dimensional table and then processed the records out of the table
in the correct sequence. 

Then go back and read the next pr-ref series. This actually proved to
be quite quick where the number of records for each ref was not too
large. 


                         
                         		Scott Peterson


Follow your dream! Unless it's the one where you're 
at work in your underwear during a fire drill, or the 
one where you're naked and in the supermarket.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
