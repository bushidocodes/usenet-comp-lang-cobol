[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can someone help me please?

_8 messages · 7 participants · 2000-01_

---

### Can someone help me please?

- **From:** "Gerda Beerda" <g.beerda@wanadoo.nl>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<858lo5$2j95$1@buty.wanadoo.nl>`

```
Who can help me with the following problem:

Ihave 2 files: PERSONS.SEQ en BANK.SEQ.

Contents of PERSONEN.SEQ (I will type one line, there are many more):
7114AUWEMA      ENNE       KLEINE ROZENSTRAAT  0   LEEK    13687
first 4 numbers = PERSNUMBER
then 21 karakters = PERSNAME
then 11 karakters = PERSFIRSTN
then 22 karakters = PERSSTREET
then 20 karakters = CITY
then 7 cijfers = ABNNUM

Contents of BANK.SEQ (I will type one line, there are many more):
6380405100
first 4 numbers = PERSNUMBER
then 6 numbers = AMOUNT

Now I need to make a list of all PERSONS (PERSNUMBER + PERSNAME) with an
amount higher than 500000.
This list must be written to OPG18-2.SEQ

Who can help me? I don't get it.
I can send you the files PERSONS.SEQ and BANK.SEQ.

I hope someone can help me.

Cheers,
Gerda Beerda.
```

#### ↳ Re: Can someone help me please?

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eh6qdwtW$GA.272@cpmsnbbsa04>`
- **References:** `<858lo5$2j95$1@buty.wanadoo.nl>`

```

Gerda Beerda <g.beerda@wanadoo.nl> wrote in message
news:858lo5$2j95$1@buty.wanadoo.nl...
> Who can help me with the following problem:
>
…[20 more quoted lines elided]…
> Who can help me? I don't get it.


Could you please explain what part of this you don't understand?  Honestly,
it seems like you explained it enough for me to create the program you want
from the small amount of information you presented (although I'd have to
come up with more test data).

As has already been mentioned, providing your source code plus platform, OS,
and compiler would be appreciated.



> I can send you the files PERSONS.SEQ and BANK.SEQ.
>
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Can someone help me please?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38787E9F.46617F92@zip.com.au>`
- **References:** `<858lo5$2j95$1@buty.wanadoo.nl>`

```
Gerda Beerda wrote:
> 
> 
…[6 more quoted lines elided]…
> Gerda Beerda.

Show me yours and I will show you mine.

If you would like help please let us know what you have tried already
and we will be glad to help.  Without that you are fishing for a free
ride and will get short shift.

Code, platform, and compiler would be very helpful.  WE are totally
unclear on what you do not get.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: Can someone help me please?

- **From:** "Steven Kalemkiewicz" <senseisk@flash.net>
- **Date:** 2000-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c30e4.18579$r6.1054052@news.flash.net>`
- **References:** `<858lo5$2j95$1@buty.wanadoo.nl>`

```
Look up the topic Select-Extract Reporting

-Steve Kalemkiewicz
```

#### ↳ Re: Can someone help me please?

- **From:** Charles Hammond <ceh1@ritz.cec.wustl.edu>
- **Date:** 2000-01-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000110105303.5437A-100000@ritz.cec.wustl.edu>`
- **References:** `<858lo5$2j95$1@buty.wanadoo.nl>`

```
Generally this can be done a couple different ways.

One way is to read one file and search the other file.  This requires that
the file you are searching to have a different access say random and use
an index/record key.

Another way would be to read the file you want to search into a table and
search the table (Table must have an index to search it).  Normally the
table is loaded in the housekeeping or initialization section of the
program.  Since you are reading till end of file, the EOJ switch would
have to be switched back and reused for the other file.

If you don't understand any of this maybe you should have gone to class.

However searching files and tables requires you to read your book and find
out how to do it.  Most people will not do it for you in this newsgroup.

I will give you this hint:

select filea
 assign to file1-database
  organization is indexed
   access is random
    record key is emp-nbr

This will only work for a flat file.  Access of a VSAM file on a mainframe
is a little different.  Better read your book a little about searching a
file with an index or a record key.

A lot depends on how your instructor wants it done.  Just start writing
the program and get all the file descriptions written out and maybe you
will get a little more help.  You have to make an effort to figure it out.

Good Luck.

 Charles Hammond, BSIM Undergraduate Program

On Sun, 9 Jan 2000, Gerda Beerda wrote:

> Who can help me with the following problem:
> 
…[32 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Can someone help me please?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387B18C4.B8A17298@zip.com.au>`
- **References:** `<858lo5$2j95$1@buty.wanadoo.nl> <Pine.SOL.3.96.1000110105303.5437A-100000@ritz.cec.wustl.edu>`

```
Received from Gerda, can't see it on the news group:

I'm trying to sort a file
I get the error:
C:\Sortpers 50: JMN2896I-S  SORT-MERGE FILE CAN ONLY SPECIFY
FILE-IDENTIFIER
IN ASSIGN CLAUSE.

I included the code and the SEQ file.
Can someone help me with this problem?

Cheers,
Gerda
```

###### ↳ ↳ ↳ Re: Can someone help me please?

- **From:** "Paulo Vieira" <pvieira@emporsoft.pt>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85ic1g$eoe$1@duke.telepac.pt>`
- **References:** `<858lo5$2j95$1@buty.wanadoo.nl> <Pine.SOL.3.96.1000110105303.5437A-100000@ritz.cec.wustl.edu> <387B18C4.B8A17298@zip.com.au>`

```
By the error message, it seems Fujitsu.
I can't recall the details, but I remember a thread a few months ago, on the
same topic. May be it's in DejaNews.
It seems that the only valid reference is to "file.dat", not to a WS field
containing the name of the file, or to an equivalent in the parameter file
(cobol85.cbr?).
Ken Foskey <waratah@zip.com.au> wrote in message
news:387B18C4.B8A17298@zip.com.au...
> Received from Gerda, can't see it on the news group:
>
…[10 more quoted lines elided]…
> Gerda
```

##### ↳ ↳ Re: Can someone help me please?

- **From:** slarsen22@aol.com (SLarsen22)
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000129152753.28337.00000318@ng-cd1.aol.com>`
- **References:** `<Pine.SOL.3.96.1000110105303.5437A-100000@ritz.cec.wustl.edu>`

```
A flat file does not have a key, and thus an index either.  That is why it is
called a flat file.  To rephrase, a keyed file must have an index and is not a
flat file.  You can still search any flat file on any bytes, but then you don't
have the advantage of the index.  If you are talking databases - different
subject. 
.Pray to God but row the boat for shore....
 >http://members.aol.com/SLarsen22>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
