[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read comma-delimited

_27 messages · 11 participants · 2004-11_

---

### Read comma-delimited

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-11-11T15:12:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cmvvhm$l35$1@peabody.colorado.edu>`

```
Anybody have some CoBOL source that will read in a comma-delimited Excel file?
 The part I would like to avoid coding is figuring out whether a comma is a
delimiter or within a string.

(what are the string delimiters that can have a comma in them?)

(Actually, it is another programmer who asked if I have such a program)
```

#### ↳ Re: Read comma-delimited

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-11-11T16:00:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9KgoJr3PflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu>`

```
.    On  11.11.04
  wrote  howard@brazee.net (Howard Brazee)
     on  /COMP/LANG/COBOL
     in  cmvvhm$l35$1@peabody.colorado.edu
  about  Read comma-delimited


HB> Anybody have some CoBOL source that will read in a comma-delimited
HB> Excel file?  The part I would like to avoid coding is figuring out
HB> whether a comma is a delimiter or within a string.

   Quite recently there has been discussion of this together with code  
examples. You may search for UNSTRING and CSV


HB> (what are the string delimiters that can have a comma in them?)

   rather the delimited strings do have them

   E.g. the city line of a US-american address, like this:

   New York, NY 10014

   or a the street line of a french address:

   33, rue Verollot




Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Er kann die Tinte nicht halten, und wenn es ihm ankommt, jemand zu besudeln, so besudelt er sich gemeiniglich am meisten. -G.C.Lichtenberg
```

##### ↳ ↳ Re: Read comma-delimited

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-11-11T18:41:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cn0bpe$smd$1@peabody.colorado.edu>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <9KgoJr3PflB@jpberlin-l.willms.jpberlin.de>`

```

On 11-Nov-2004, l.willms@jpberlin.de (Lueko Willms) wrote:

> HB> Anybody have some CoBOL source that will read in a comma-delimited
> HB> Excel file?  The part I would like to avoid coding is figuring out
…[3 more quoted lines elided]…
> examples. You may search for UNSTRING and CSV

Unstring works nicely if we had a consistent delimiter.   It fails when we have
that delimiter as part of the data.   What does CSV stand for?

> HB> (what are the string delimiters that can have a comma in them?)
>
…[8 more quoted lines elided]…
>    33, rue Verollot

I understand this.   But what are the acceptable string delimiters?   Are there
alternatives to double quotes?
The following needs to be parsed into 4 fields.
My name is Joe,-3.4,"105 South Reed Court, Lakewood",6.2
"Hi ""Henry""",3.4,Smith,4


I'm thinking I need to do reference modification and check to see if a comma is
followed by a single double-quote.
```

###### ↳ ↳ ↳ Re: Read comma-delimited

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-11-11T19:28:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Kgq4LAPflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <9KgoJr3PflB@jpberlin-l.willms.jpberlin.de> <cn0bpe$smd$1@peabody.colorado.edu>`

```
.    On  11.11.04
  wrote  howard@brazee.net (Howard Brazee)
     on  /COMP/LANG/COBOL
     in  cn0bpe$smd$1@peabody.colorado.edu
  about  Re: Read comma-delimited


HB> I understand this.   But what are the acceptable string delimiters?
HB> Are there alternatives to double quotes?

  My recipe is to go back to ASCII and use the US (Unit Separator)  
character as the unit separator. One would not get into conflict with  
any character normally to be expeced in a text file.  But that is just  
MY idea.

HB> The following needs to be parsed into 4 fields.
HB> My name is Joe,-3.4,"105 South Reed Court, Lakewood",6.2
HB> "Hi ""Henry""",3.4,Smith,4
HB>
HB>
HB> I'm thinking I need to do reference modification and check to see if
HB> a comma is followed by a single double-quote.

  Yes, I just recommended UNSTRING and CSV as keywords to search for.  
Robert Wagner had presented some good ideas on how to proceed.

   "Veni, vidi, vici" was, I believe, in his example.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Nach einem dreiï¿½igjï¿½hrigen Krieg mit sich selbst kam es endlich zu einem Vergleich, aber die Zeit war verloren. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Read comma-delimited

_(reply depth: 4)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-12T08:47:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qtt8p01plfck86hnpvdcfqdkkitecmtae3@4ax.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <9KgoJr3PflB@jpberlin-l.willms.jpberlin.de> <cn0bpe$smd$1@peabody.colorado.edu> <9Kgq4LAPflB@jpberlin-l.willms.jpberlin.de>`

```
On 11 Nov 2004 19:28:00 GMT, l.willms@jpberlin.de (Lueko Willms)
wrote:


>  Yes, I just recommended UNSTRING and CSV as keywords to search for.  
>Robert Wagner had presented some good ideas on how to proceed.
>
>   "Veni, vidi, vici" was, I believe, in his example.

Emend that to  'veni, vidi .. capta feri'.  I came, I saw, I lost my
head.
```

###### ↳ ↳ ↳ Re: Read comma-delimited

- **From:** Louis Krupp <lkrupp@pssw.NOSPAM.com.INVALID>
- **Date:** 2004-11-11T13:28:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10p7irf3st6e27b@corp.supernews.com>`
- **In-Reply-To:** `<cn0bpe$smd$1@peabody.colorado.edu>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <9KgoJr3PflB@jpberlin-l.willms.jpberlin.de> <cn0bpe$smd$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
<snip>
> But what are the acceptable string delimiters?   Are there
> alternatives to double quotes?
> The following needs to be parsed into 4 fields.

CSV stands for "comma separated values."

I would try stepping through the input record one character at a time, 
and toggling a string flag when you see a quote.  When you see a comma 
outside of a quote, start a new field (you might use an array of fields 
and then move them to the eventual destination record when you're done 
parsing).

I would try looking for double quotes unless an inspection of some 
sample data turns up single quotes.  If those show up, remember which 
one started the string and look for one of the same flavor to terminate it.

This one looks pretty civilized:
> My name is Joe,-3.4,"105 South Reed Court, Lakewood",6.2

This one is more complicated;  qoutes within strings have been replaced 
by pairs of quotes (a common way of doing things).  Assuming there are 
no empty values (..., "", ...), when you see a quote, you could look 
ahead one character and if the next one is also a quote, you could put 
one quote character in the destination field, not toggle the string 
flag, and skip both input quotes.
> "Hi ""Henry""",3.4,Smith,4
<snip>

Have fun.

Louis Krupp
```

###### ↳ ↳ ↳ Re: Read comma-delimited

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-11T23:52:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85q7p05jgs4uc8ln780v3bd1bhaq06vhoa@4ax.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <9KgoJr3PflB@jpberlin-l.willms.jpberlin.de> <cn0bpe$smd$1@peabody.colorado.edu>`

```
On Thu, 11 Nov 2004 18:41:50 GMT, "Howard Brazee" <howard@brazee.net>
wrote:


>I'm thinking I need to do reference modification and check to see if a comma is
>followed by a single double-quote.

There can be any number of spaces and/or tabs between fields.
```

#### ↳ Re: Read comma-delimited

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-11-11T13:46:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0411111346.17ab4318@posting.google.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> Anybody have some CoBOL source that will read in a comma-delimited Excel file?
>  The part I would like to avoid coding is figuring out whether a comma is a
> delimiter or within a string.
> 
> (what are the string delimiters that can have a comma in them?)

Sometimes tab-delimited files are used, but they are difficult to read
because the tabs may get expanded to spaces on reading as LINE
SEQUENTIAL.

BTW: there is a free program xlhtml which will convert .xls files to
html or csv which I use with success.
```

#### ↳ Re: Read comma-delimited [Long]

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-11-12T09:20:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<er-dnfNVWcEhSQncRVn-2g@giganews.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> Anybody have some CoBOL source that will read in a comma-delimited
> Excel file? The part I would like to avoid coding is figuring out
…[5 more quoted lines elided]…
> program)

Try this:

----- begin
000001 IDENTIFICATION DIVISION.
000002 PROGRAM-ID. DECOMMA.
000003*====================================================DECOMMA======
000004* NAME:      DECOMMA - Remove commas in CSV file
000005*
000006* PURPOSE:   Converts delimiting commas in CSV record to low-value
000007*            to facilitate UNSTRING command.
000008*
000009*
000010* USAGE:
000011*            CALL 'DECOMMA' USING LINK-LEN LINK-RECORD
000012*
000013*                LINK-LEN [S9(7)C-5)] - Length in bytes of RECORD
000014*                LINK-RECORD [X(...)] - The record to attack
000015*
000016*
000017*            CALL 'DECSV' USING LINK-LEN LINK-RECORD
000018*
000019*                LINK-LEN [S9(7)C-5] - length of record
000020*                LINK-RECORD [X(nnn)] - Record to fix
000021*
000022*
000023*            Routine converts:
000024*              "AB,CD","123","XYZ123"bbbbb
000025*
000026*              AB,CD^123^XYZ123^bbbbbbbbbb
000027*
000028*                where ^ is low-values, b=blank
000029*
000030*            CALL 'DECOMMA-COMMASP' USING LINK-LEN LINK-RECORD
000031*
000032*                Converts ', ' to ',' if it occurs outside
000033*                a double quote:
000034*
000035*                0, 123,"a, b", 5
000036*                0,123,"a, b",5
000037
000038* DATE WRITTEN: 03/09/01
000039*
000040* SIZE: CODE
000041*       DATA
000042*       TOTAL
000043*
000044* REVISIONS:
000045*
000046*=================================================================
000047 COPY '..\CB\NSBIS.COB'.
000048
000049 DATA DIVISION.
000050 FILE SECTION.
000051
000052
000053 WORKING-STORAGE SECTION.
000054
000055 01  FILLER.
000056     COPY '..\CB\FAKESIG.COB'.
000057 01  FIRST-QUOTE                 PIC X.
000058 01  I                           PIC S9(7) COMP-5.
000059 01  J                           PIC S9(4) COMP-5.
000060 01  SW                          PIC S9(4) COMP-5.
000061
000062 LINKAGE SECTION.
000063
000064 01  LINK-LEN                    PIC S9(7) COMP-5.
000065 01  LINK-RECORD                 PIC X(1024).
000066
000067 PROCEDURE DIVISION USING LINK-LEN LINK-RECORD.
000068     MOVE 'N' TO FIRST-QUOTE.
000069     PERFORM VARYING I FROM 1 BY 1 UNTIL I > LINK-LEN
000070         EVALUATE TRUE
000071             WHEN LINK-RECORD(I:1) = '"'
000072                 IF FIRST-QUOTE = 'Y'
000073                     MOVE 'N' TO FIRST-QUOTE
000074                 ELSE
000075                     MOVE 'Y' TO FIRST-QUOTE
000076                     END-IF
000077                 MOVE ' ' TO LINK-RECORD(I:1)
000078             WHEN LINK-RECORD(I:1) = ','
000079                 IF FIRST-QUOTE = 'Y'
000080                     MOVE ' ' TO LINK-RECORD(I:1)
000081                     END-IF
000082             END-EVALUATE
000083         END-PERFORM.
000084     GO TO QUIT.
000085
000086 P100-CSV.
000087     ENTRY 'DECSV' USING LINK-LEN LINK-RECORD.
000088
000089     MOVE 1 TO SW    *>Looking for quote 1 or 2
000090     MOVE 0 TO J.
000091     PERFORM VARYING I FROM 1 BY 1 UNTIL I > LINK-LEN
000092         EVALUATE LINK-RECORD(I:1) ALSO SW
000093             WHEN '"' ALSO 1
000094                 COMPUTE SW = 3 - SW   *>Found 1st quote
000095             WHEN '"' ALSO 2
000096                 COMPUTE SW = 3 - SW   *>Found 2nd quote, new
000097             WHEN ',' ALSO 1           *>delimit external comma
000098                 ADD 1 TO J
000099                 MOVE LOW-VALUES TO LINK-RECORD(J:1)
000100             WHEN ',' ALSO 2           *>Copy internal comma
000101                 ADD 1 TO J
000102                 MOVE LINK-RECORD(I:1) TO LINK-RECORD(J:1)
000103             WHEN OTHER                *>Copy all else
000104                 ADD 1 TO J
000105                 MOVE LINK-RECORD(I:1) TO LINK-RECORD(J:1)
000106             END-EVALUATE
000107         END-PERFORM.
000108     PERFORM VARYING I FROM J BY 1 UNTIL I > LINK-LEN
000109         MOVE SPACE TO LINK-RECORD(I:1)
000110         END-PERFORM.
000111     GO TO QUIT.
000112
000113 P200-DECOMMA-COMMASP.
000114     ENTRY 'DECOMMA-COMMASP' USING LINK-LEN LINK-RECORD.
000115     MOVE 1 TO SW.
000116     PERFORM VARYING I FROM 1 BY 1 UNTIL I > LINK-LEN - 1
000117         EVALUATE LINK-RECORD(I:1) ALSO SW
000118             WHEN '"' ALSO 1
000119                 COMPUTE SW = 3 - SW
000120             WHEN '"' ALSO 2
000121                 COMPUTE SW = 3 - SW
000122             WHEN ',' ALSO 1
000123                 COMPUTE J = I + 1
000124                 IF LINK-RECORD(J:1) = ' '
000125                     MOVE LOW-VALUES TO LINK-RECORD(J:1)
000126                     END-IF
000127             END-EVALUATE
000128         END-PERFORM.
000129     CALL 'JUSTL' USING LINK-LEN LINK-RECORD.
000130     GO TO QUIT.
000131
000132 QUIT.
000133
000134     GOBACK.
000135

-------
Notes: You should be able to concoct the copy-book NSBIS. You may ignore the 
copy-book FAKESIG (actually contains "C++ Copyright(c) 1997 Microsoft" just 
to put the reverse-engineering geeks in the fetal position).

"JUSTL" is another routine to justify-left - you can probably construct your 
own.
```

##### ↳ ↳ Re: Read comma-delimited [Long]

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-11-12T18:35:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eo7ld.205423$nl.87373@pd7tw3no>`
- **In-Reply-To:** `<er-dnfNVWcEhSQncRVn-2g@giganews.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com>`

```
JerryMouse wrote:

>Howard Brazee wrote:
>  
…[19 more quoted lines elided]…
>
<snip>

Can't help wondering are we making a dog's breakfast of this ? I do use 
ACCESS but as yet not EXCEL, (although OO-wise the latter will give me 
the opportunity of simple charting - using OLE class support).

I just pulled up EXCEL giving it a 'foreign' file and it prompted for 
how records were delimited.

1) Delimiter -  Tab, Semi-colon, Comma, Space and Other ( you specify 
what you want)
2) Text qualifier (a) " or (b) ' or (c) <none>

If you are the recipient of a CSV from another source, it doesn't seem 
unreasonable to me that you should be able to request the delimiting 
character you want to overcome the comma problem.
Me - I'd go for Tilde (~) using 'Other' in # 1 ??????

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-11-12T18:57:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cn312c$9b$1@peabody.colorado.edu>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <eo7ld.205423$nl.87373@pd7tw3no>`

```

On 12-Nov-2004, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> Can't help wondering are we making a dog's breakfast of this ? I do use
> ACCESS but as yet not EXCEL, (although OO-wise the latter will give me
…[12 more quoted lines elided]…
> Me - I'd go for Tilde (~) using 'Other' in # 1 ??????

The person who asked me if we had an existing program for this task says that
she's not willing to go to the work of persuading the vendor to change.   It is
sometimes *much* easier and cheaper to write a dozen programs than to persuade a
vendor to be reasonable.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-11-12T22:59:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jfbld.209149$%k.131423@pd7tw2no>`
- **In-Reply-To:** `<cn312c$9b$1@peabody.colorado.edu>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <eo7ld.205423$nl.87373@pd7tw3no> <cn312c$9b$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

>On 12-Nov-2004, "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
…[25 more quoted lines elided]…
>
Interesting reply, but a cop out. 'Easier and cheaper to write a dozen 
programs' ? What could be easier and cheaper than requesting the 
delimiter be a Tilde(~). As an academic institution I would have thought 
you would have some clout with your so-called 'vendors'. No wonder 
there's so much outsourcing going on in the States.

Now the other side of the coin - DOS days. Given a series of CSVs where 
the record layouts were unimaginable, (basically that was because the 
third-party wanted to be in control - didn't want user, (Oil/Gas 
company) to know I "existed" - so he was interpreting for me what he 
*thought* it was we needed from their table layouts - after six months 
we gave it up !).

Then of  course the oil/gas companies got into DBs - and natch - 
realized they could use data from the DOS COBOL system - but of course 
each company wanted the data presented differently to *fit* their 
existing DB. And of course what they got was a freebie.

The *one* rare occasion I did get to talk to an oil company employee, he 
was a Systems Analyst. I told him I could send a zipfile via modem, 
(back then). Note that the phone connection between the two of us in 
Calgary was a freebie. His solution - send him a diskette via Courier. 
Some analyst ! (To my mind he was *begging* for his job to be outsourced).

Fast forward to current - OO COBOL and MS Access. The portability of 
data - the *major* reason I switched to MS Access.  So oil company has 
MS Access as part of the application - they have two choices, (1) Read 
my Tables and extract as they see fit to import into their corporate DB, 
or (2) They don't want to bother and rather I did it - Yes please, but I 
now want $$$$s for doing it.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

- **From:** docdwarf@panix.com
- **Date:** 2004-11-12T14:04:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cn31f0$aeq$1@panix5.panix.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <eo7ld.205423$nl.87373@pd7tw3no>`

```
In article <eo7ld.205423$nl.87373@pd7tw3no>,
James J. Gavan <jjgavan@shaw.ca> wrote:

[snip]

>Can't help wondering are we making a dog's breakfast of this ?

Well, puppies gotta eat, too, y'know.

DD
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-11-12T18:12:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0pKdnSTuYtTizAjcRVn-1w@giganews.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <eo7ld.205423$nl.87373@pd7tw3no>`

```
James J. Gavan wrote:
>
> Can't help wondering are we making a dog's breakfast of this ? I do
…[8 more quoted lines elided]…
> 2) Text qualifier (a) " or (b) ' or (c) <none>

Which may not work if the delimiter is a combination of quotes and commas, 
especially if the comma is contained within a quote-delimited field.

>
> If you are the recipient of a CSV from another source, it doesn't seem
…[4 more quoted lines elided]…
> Jimmy, Calgary AB

Why? CSV is a "semi-standard" and any shop should be able to handle it 
straightaway. Good luck on convincing a government agency to provide you 
with a unique file.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-11-13T00:42:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zLcld.207466$nl.204731@pd7tw3no>`
- **In-Reply-To:** `<0pKdnSTuYtTizAjcRVn-1w@giganews.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <eo7ld.205423$nl.87373@pd7tw3no> <0pKdnSTuYtTizAjcRVn-1w@giganews.com>`

```
JerryMouse wrote:

>James J. Gavan wrote:
>  
…[17 more quoted lines elided]…
>
How do you figure that out Mr. MS shareholder ? The specific question 
was addressed to using Excel. Where in the above, (from an Excel 
dialog)  do you  see that you can use either/or for a field delimiter, 
in one export ? Generating the export, #'s 1 and 2 above are distinct 
and separate parameters. (Now of course if the originator of the CSV was 
stupid enough to choose the comma for #1 and #2 .........).

>Why? CSV is a "semi-standard" and any shop should be able to handle it 
>straightaway. Good luck on convincing a government agency to provide you 
…[3 more quoted lines elided]…
>
It isn't a question of being able to handle it, the answer is already 
coded within Excel as a choice - given somebody makes the effort to 
negotiate. Government or no, what's unique about passing you an Excel 
CSV - hitting one checkbox to give the recipient what they want.?

Yes - if it is not controllable, with CSVs coming from a variety of 
applications, then you are *forced* into a COBOL solution as you suggest.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-11-14T15:29:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xuSdnTmP4byCUwrcRVn-sA@giganews.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <eo7ld.205423$nl.87373@pd7tw3no> <0pKdnSTuYtTizAjcRVn-1w@giganews.com> <zLcld.207466$nl.204731@pd7tw3no>`

```
James J. Gavan wrote:
> JerryMouse wrote:
>
…[24 more quoted lines elided]…
> was stupid enough to choose the comma for #1 and #2 .........).

No, the original question was dealing with a file CREATED by Excel - not 
USING Excel. Secondly, there is no such thing as an "Excel CSV" file. A file 
created by Excel is either an Excel file (.XLS) or a CSV file (.CSV). If you 
want to buy Micros~1 Office so you can read a CSV file, as a Micros~1 
stockholder, I say: "Good for you!"

The following cells in an Excel book:
1     Paris, France     1.23

are saved, by Excel, in CSV format as:
1,"Paris, France",1.23

Now go use a comma-delimiter on that.



>
>> Why? CSV is a "semi-standard" and any shop should be able to handle
…[8 more quoted lines elided]…
> CSV - hitting one checkbox to give the recipient what they want.?

Because there's no such thing as an "Excel CSV." The file is either an Excel 
file or a CSV file (that may or may not have been created by Excel). Now 
Excel can certainly scarf up a standard CSV file - if you HAVE Excel. But 
then what do you do with the data? You can't feed it, directly, to a COBOL 
program.

I read the original request as:

"Somebody sent us a CSV-formatted file. We need to be able to read this file 
into our COBOL-language system (the file is list of price updates from our 
vendor, hours worked by our contract employees at the customer's site, rents 
collected, or something else)."

How Excel got into this discussion is beyond me.

>
> Yes - if it is not controllable, with CSVs coming from a variety of
> applications, then you are *forced* into a COBOL solution as you
> suggest.

Bingo.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-13T20:22:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c4rcp0h3gbgukehp4dge4k23fpcdm5eg78@4ax.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <eo7ld.205423$nl.87373@pd7tw3no>`

```
On Fri, 12 Nov 2004 18:35:54 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:


>If you are the recipient of a CSV from another source, it doesn't seem 
>unreasonable to me that you should be able to request the delimiting 
>character you want to overcome the comma problem.
>Me - I'd go for Tilde (~) using 'Other' in # 1 ??????

The second most common delimiter is Tab. Using tab avoids the need for
quotes around alpha fields that may contain commas. 

The solution I favor is to discard commas in text fields.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-11-14T10:13:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0411141013.269f7066@posting.google.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <eo7ld.205423$nl.87373@pd7tw3no> <c4rcp0h3gbgukehp4dge4k23fpcdm5eg78@4ax.com>`

```
Robert Wagner <spamblocker-robert@wagner.net> wrote 

> The solution I favor is to discard commas in text fields.

That would be modifying user data.  You would probaly blame it on the
database again, but in most systems the users expect to be able to
control their data and not have programs make arbitrary changes that
corrupt it.
```

##### ↳ ↳ Re: Read comma-delimited [Long]

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-11-13T12:20:59+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2vkur2F2m2fcrU1@uni-berlin.de>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com>`

```
The real problem here is that the field delimiter can appear inside a
literal string. When it does, it must be left intact. It doesn't matter
whether the delimiter is comma, tilde, TAB or whatever.

Jerry's approach addresses this and therefore (in my book), is a good one.

If I were doing it, I'd generalise it to work for ANY delimiter.

Somewhere amongst my archives I have such a solution I wrote many years ago.
If I can find it, I'll post it.

Pete.

(Top post, nothing below the signature.)

"JerryMouse" <nospam@bisusa.com> wrote in message
news:er-dnfNVWcEhSQncRVn-2g@giganews.com...
> Howard Brazee wrote:
> > Anybody have some CoBOL source that will read in a comma-delimited
…[148 more quoted lines elided]…
> Notes: You should be able to concoct the copy-book NSBIS. You may ignore
the
> copy-book FAKESIG (actually contains "C++ Copyright(c) 1997 Microsoft"
just
> to put the reverse-engineering geeks in the fetal position).
>
> "JUSTL" is another routine to justify-left - you can probably construct
your
> own.
>
>
>
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-13T20:26:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kdrcp05gegsfclc4ams34k6ss23u7u4fs9@4ax.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <2vkur2F2m2fcrU1@uni-berlin.de>`

```
On Sat, 13 Nov 2004 12:20:59 +1300, "Pete Dashwood"
<dashwood@enternet.co.nz> wrote:

>The real problem here is that the field delimiter can appear inside a
>literal string. When it does, it must be left intact. It doesn't matter
>whether the delimiter is comma, tilde, TAB or whatever.

On most platforms, TAB will never appear in a text field, which makes
it a good choice for delimiter.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-11-13T20:08:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0411132008.bd6452c@posting.google.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <2vkur2F2m2fcrU1@uni-berlin.de> <kdrcp05gegsfclc4ams34k6ss23u7u4fs9@4ax.com>`

```
Robert Wagner <spamblocker-robert@wagner.net> wrote 

> On most platforms, TAB will never appear in a text field, which makes
> it a good choice for delimiter.

But it makes a very poor choice for reading into line sequential files
(on many Cobol systems) because the tabs are expanded to spaces and
the resulting fields rarely line up.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-11-14T22:32:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2von2cF2n1065U1@uni-berlin.de>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <2vkur2F2m2fcrU1@uni-berlin.de> <kdrcp05gegsfclc4ams34k6ss23u7u4fs9@4ax.com>`

```

"Robert Wagner" <spamblocker-robert@wagner.net> wrote in message
news:kdrcp05gegsfclc4ams34k6ss23u7u4fs9@4ax.com...
> On Sat, 13 Nov 2004 12:20:59 +1300, "Pete Dashwood"
> <dashwood@enternet.co.nz> wrote:
…[7 more quoted lines elided]…
>

I have used TAB delimited files, and agree it is fine. But so is any other
character if you apply the rules stated above.

The TAB character can still appear in a quoted string; I know this because I
have seen it. (To be fair, it was not in a TAB delimited file...)

Pete.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 5)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2004-11-14T17:56:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pu6fp094cevj7125bg5tq6tc10rpueui5u@4ax.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <2vkur2F2m2fcrU1@uni-berlin.de> <kdrcp05gegsfclc4ams34k6ss23u7u4fs9@4ax.com> <2von2cF2n1065U1@uni-berlin.de>`

```
On Sun, 14 Nov 2004 22:32:53 +1300, "Pete Dashwood"
<dashwood@enternet.co.nz> wrote:

>
>"Robert Wagner" <spamblocker-robert@wagner.net> wrote in message
…[16 more quoted lines elided]…
>have seen it. (To be fair, it was not in a TAB delimited file...)

The problem isn't the field delimiter appearing in a quoted string -
that's what the quotes are for! It's a quote, or whatever you're using
to delimit text, appearing in a quoted string.

Ian
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-11-15T13:09:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2vqadrF2os6saU1@uni-berlin.de>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <2vkur2F2m2fcrU1@uni-berlin.de> <kdrcp05gegsfclc4ams34k6ss23u7u4fs9@4ax.com> <2von2cF2n1065U1@uni-berlin.de> <pu6fp094cevj7125bg5tq6tc10rpueui5u@4ax.com>`

```

"Ian Dalziel" <iandalziel@lineone.net> wrote in message
news:pu6fp094cevj7125bg5tq6tc10rpueui5u@4ax.com...
> On Sun, 14 Nov 2004 22:32:53 +1300, "Pete Dashwood"
> <dashwood@enternet.co.nz> wrote:
…[8 more quoted lines elided]…
> >> >literal string. When it does, it must be left intact. It doesn't
matter
> >> >whether the delimiter is comma, tilde, TAB or whatever.
> >>
<snip>
>
> The problem isn't the field delimiter appearing in a quoted string -
> that's what the quotes are for! It's a quote, or whatever you're using
> to delimit text, appearing in a quoted string.
>
Let's look at it again...

I have dealt with "CSV" files where text was not delimited by anything.
example:  1234,some text field,another text field,789, ... It was the job of
the decoding program to decide what was numeric and what was text. (and it
did).

The quotes on text were introduced so that commas (or whatever field
delimiters are being used) could be included in a string: 1234,"some text
field","another text field",789,"field that has, an included comma"...
(You pointed this out)

I believe your point was: 1234,"some text field","another text
field",789,"field that has " an included quote",...
...is not covered by my rules above, and, on reflection, I believe you are
right. I was looking at the field delimiter and not the text delimiter
(always assuming that one is present).

Thanks for pointing it out. As penance, I shall now write a generalised
solution to all of the above... <G> (The component I use currently would not
handle a quote in a quoted string, but it has never had to...)

Pete.
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 7)_

- **From:** Louis Krupp <lkrupp@pssw.NOSPAM.com.INVALID>
- **Date:** 2004-11-14T17:44:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10pfuvvloeh5jbb@corp.supernews.com>`
- **In-Reply-To:** `<2vqadrF2os6saU1@uni-berlin.de>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <2vkur2F2m2fcrU1@uni-berlin.de> <kdrcp05gegsfclc4ams34k6ss23u7u4fs9@4ax.com> <2von2cF2n1065U1@uni-berlin.de> <pu6fp094cevj7125bg5tq6tc10rpueui5u@4ax.com> <2vqadrF2os6saU1@uni-berlin.de>`

```
Pete Dashwood wrote:
<snip>
> I believe your point was: 1234,"some text field","another text
> field",789,"field that has " an included quote",...
…[6 more quoted lines elided]…
> handle a quote in a quoted string, but it has never had to...)

Note that in the example given by the OP, embedded quotes are doubled 
("this is a quote ("") in the middle of a qouted string").

This could be a finite state machine application...

Louis
```

###### ↳ ↳ ↳ Re: Read comma-delimited [Long]

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-11-14T21:19:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0411142119.7928d821@posting.google.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu> <er-dnfNVWcEhSQncRVn-2g@giganews.com> <2vkur2F2m2fcrU1@uni-berlin.de> <kdrcp05gegsfclc4ams34k6ss23u7u4fs9@4ax.com> <2von2cF2n1065U1@uni-berlin.de> <pu6fp094cevj7125bg5tq6tc10rpueui5u@4ax.com>`

```
Ian Dalziel <iandalziel@lineone.net> wrote 

> The problem isn't the field delimiter appearing in a quoted string -
> that's what the quotes are for! It's a quote, or whatever you're using
> to delimit text, appearing in a quoted string.

That is not a problem to sensible program code (such as I have
supplied to Howard by EMail).  Most spreadsheets that I care about
will output double quotes for embedded quote characters.

  [  1][This is text with a , and a " in it][34]

gives:

1,"This is text with a , and a "" in it",34
```

#### ↳ Re: Read comma-delimited

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2004-11-16T14:56:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Cyomd.33947$Al3.21262@newssvr30.news.prodigy.com>`
- **References:** `<cmvvhm$l35$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:cmvvhm$l35$1@peabody.colorado.edu...
> Anybody have some CoBOL source that will read in a comma-delimited Excel 
> file?
> The part I would like to avoid coding is figuring out whether a comma is a
> delimiter or within a string.

Howard, have a look at this thread on Tek-Tips COBOL discussion:
http://www.tek-tips.com/viewthread.cfm?qid=888552

(registration might be required.  Tek-Tips is worth it, though.)

There are some programs there that deal with the issues you are facing.

Best regards,
Tom Morrison
Liant Software Corporation
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
