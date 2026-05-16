[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable length records

_9 messages · 8 participants · 1999-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Variable length records

- **From:** Roberto Barsallo <robertobarsallo@hotmail.com>
- **Date:** 1999-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<80jspd$j9h$1@nnrp1.deja.com>`

```
   Dear all:

   I am newbie to COBOL. I am using DEC COBOL on OpenVMS in an Alpha
Server. What I am intending to do is opening an 8-field record file
delimited by tabs, searching for certain field's condition and, if met,
move that record into another record file.
   My main problems are two: first, the input file record's length is
variable, i.e, one record can have 50 characters and the next one could
have 75 characters, but always 8 fields; this is because of a couple of
fields having variable length. I would like to move every record into a
temporary record, padding each field with spaces when needed, and then
moving this fixed-length record to the final record file; but, how do I
declare the input file length? Can I go further the average length?,
like:

01   Input-Record   PIX X(100)

or am I enable to not declare the input record's length?, like:

01   Input-Record

   Secondly, when sorted out the declaration, how do I search for tabs
delimeters?  I am trying to unstring the record using:

UNSTRING Input-Record DELIMITED BY X'09'

but to no avail.  If this is the right way, then can someone say for
sure which is the exact syntax for the Tab character in COBOL and how
to represent it - say it is hexadecimal or EBDC? Otherwise, how do I
search for Tabs?

   I will definitely praise your help and support.  Thanks, guys.

                  Bar.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Variable length records

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<382E9591.8FC1CE8F@zip.com.au>`
- **References:** `<80jspd$j9h$1@nnrp1.deja.com>`

```
Roberto Barsallo wrote:
> 
>    Secondly, when sorted out the declaration, how do I search for tabs
…[3 more quoted lines elided]…
> 

The tab character is X'08' in ascii and x'05' in Ebcdic.

Ken
```

##### ↳ ↳ Re: Variable length records

- **From:** pgraham@dynasty.net
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b2AX3.1316$I73.10911@newsfeed.slurp.net>`
- **References:** `<80jspd$j9h$1@nnrp1.deja.com> <382E9591.8FC1CE8F@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

|Roberto Barsallo wrote:
|> 
…[4 more quoted lines elided]…
|> 

|The tab character is X'08' in ascii and x'05' in Ebcdic.

It's been so long ago (or not long enough), I don't know about EBCDIC,
but ASCII tab is X'09'

Phil
```

##### ↳ ↳ Re: Variable length records

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-11-14T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<80msru$tps$1@aklobs.kc.net.nz>`
- **References:** `<80jspd$j9h$1@nnrp1.deja.com> <382E9591.8FC1CE8F@zip.com.au>`

```
In comp.lang.cobol Ken Foskey <waratah@zip.com.au> wrote:
:> 
:> UNSTRING Input-Record DELIMITED BY X'09'

: The tab character is X'08' in ascii and x'05' in Ebcdic.

No, x"08" is BS (Backspace), x"09" is HT (Horizontal Tab).
```

#### ↳ Re: Variable length records

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<SIVX3.12720$YI2.611763@typ11.nn.bcandid.com>`
- **References:** `<80jspd$j9h$1@nnrp1.deja.com>`

```

Roberto Barsallo <robertobarsallo@hotmail.com> wrote in message
news:80jspd$j9h$1@nnrp1.deja.com...
> I am using DEC COBOL on OpenVMS in an Alpha
> Server. What I am intending to do is opening an 8-field record file
…[8 more quoted lines elided]…
> declare the input file length?

One option might be to define your file as having a record length of 1 and
then build your record into an array from a loop, counting (looking for) tab
stops or other delimiters.  If your file has a Block Descriptor Word (BDW)
or Record Descriptor Word (RDW) you could read the word to know how many
bytes to expect.  We do this all the time reading files created by telephone
switches.
```

##### ↳ ↳ Re: Variable length records

- **From:** Nige <nige@wg.zicl.co.zuk>
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<38302CBC.9EAE26D5@wg.zicl.co.zuk>`
- **References:** `<80jspd$j9h$1@nnrp1.deja.com> <SIVX3.12720$YI2.611763@typ11.nn.bcandid.com>`

```
Warren Porter wrote:
> One option might be to define your file as having a record length of 1 and
> then build your record into an array from a loop, counting (looking for) tab
…[3 more quoted lines elided]…
> switches.

I still think UNSTRING is the best way to separate the fields.  I'm 
not sure how to read variable length records though.  (Do the records
have a terminating TAB?)

   Cheers
      Nige
```

###### ↳ ↳ ↳ Re: Variable length records

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<TOWX3.12780$YI2.622484@typ11.nn.bcandid.com>`
- **References:** `<80jspd$j9h$1@nnrp1.deja.com> <SIVX3.12720$YI2.611763@typ11.nn.bcandid.com> <38302CBC.9EAE26D5@wg.zicl.co.zuk>`

```

Nige <nige@wg.zicl.co.zuk> wrote in message
news:38302CBC.9EAE26D5@wg.zicl.co.zuk...
> Warren Porter wrote:
> > One option might be to define your file as having a record length of 1
and
> > then build your record into an array from a loop, counting (looking for)
tab
> > stops or other delimiters.  If your file has a Block Descriptor Word
(BDW)
> > or Record Descriptor Word (RDW) you could read the word to know how many
> > bytes to expect.  We do this all the time reading files created by
telephone
> > switches.
>
> I still think UNSTRING is the best way to separate the fields.  I'm
> not sure how to read variable length records though.  (Do the records
> have a terminating TAB?)

Others had already mentioned the UNSTRING statement as a way to separate the
fields, but no one at that time discussed reading variable length records--a
prerequisite to reading the fields.  If the records are separated by a line
feed and/or carriage return, defining the file as LINE SEQUENTIAL would
work.  If the file is all data separated by tab stops, reading in one byte
at a time until the right number of tab stops were found would be the way to
go.  With a RDW present, read in the number of bytes promised in that field.
Without knowing the exact format of the data, all I can do is suggest
options.  Once a record has been identified and read in, I have no problem
using UNSTRING.
```

###### ↳ ↳ ↳ Re: Variable length records

_(reply depth: 4)_

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 1999-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<sQ+PiAAnkWM4EwdS@ld50macca.demon.co.uk>`
- **References:** `<80jspd$j9h$1@nnrp1.deja.com> <SIVX3.12720$YI2.611763@typ11.nn.bcandid.com> <38302CBC.9EAE26D5@wg.zicl.co.zuk> <TOWX3.12780$YI2.622484@typ11.nn.bcandid.com>`

```
If the records are always either 50 bytes or 75 bytes long, and if there
is no record descriptor word, then the file could be defined as a 25
byte record length and then either two or three records could be read
(depending upon the number of tabs found) to reconstitute the 50 or 75
byte records respectively.

In article <TOWX3.12780$YI2.622484@typ11.nn.bcandid.com>, Warren Porter
<warrenp123@netdoor123.com> writes
>
>Nige <nige@wg.zicl.co.zuk> wrote in message
…[28 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Variable length records

- **From:** Alex <ales.romaniuk@zag.si>
- **Date:** 1999-11-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<MPG.129c879eaaf1e5e1989691@news.siol.net>`
- **References:** `<80jspd$j9h$1@nnrp1.deja.com> <SIVX3.12720$YI2.611763@typ11.nn.bcandid.com>`

```
In article <SIVX3.12720$YI2.611763@typ11.nn.bcandid.com>, 
warrenp123@netdoor123.com says...
> 
> Roberto Barsallo <robertobarsallo@hotmail.com> wrote in message
…[21 more quoted lines elided]…
> 
I am doing this using my PARSE function. I put parse in my home page, but 
only MF Cobol. If you're interested in source for VMS, please contact me.

Url to that page is http://www.zag.si/~romaniuk/download/cobol.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
