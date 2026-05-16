[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FTPing COMP-3 data from mainframe to UNIX

_6 messages · 4 participants · 2007-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### FTPing COMP-3 data from mainframe to UNIX

- **From:** kimi <mraghu83@gmail.com>
- **Date:** 2007-05-23T23:09:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179986957.656932.312050@b40g2000prd.googlegroups.com>`

```
hi,

    I am actually trying to ftp a PS file from mainframe to UNIX.

    The contents of the PS file are data declared as S9(8) COMP-3 and
9(2).

     When i ftp this file to UNIX in ASCII mode , i am able to read
the data declared as 9(2) as it
     is but there is a  erroneuos read as far as the COMP-3 data is
concerned.

     When i ftp this file to UNIX in BINARY mode , i am able to read
the data declared as COMP-
     3 as it is but  there is a erroneuos read as far as the 9(2) data
is concerned.

     The ftped data in UNIX is being read using a cobol program.
     The cobol program is being compiled using the command "cob -iaPV
filename.cbl".
     The cobol program is being run using the command "cobrun
filename.int".

     The above commands are provided by microfocus.ie. the cobol
program is being executed
     on  a UNIX environment using MICRO FOCUS  SERVER EXPRESS 4.0 SP2.

     Pls let me know how i can read both the types of data
successfully.
```

#### ↳ Re: FTPing COMP-3 data from mainframe to UNIX

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-05-24T07:11:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Aif5i.2708$u56.2645@newssvr22.news.prodigy.net>`
- **References:** `<1179986957.656932.312050@b40g2000prd.googlegroups.com>`

```
>    I am actually trying to ftp a PS file from mainframe to UNIX.
>
…[11 more quoted lines elided]…
> is concerned.

The BINARY mode transfer is the correct mode to use, and it should be 
working.   I do this all the time.

I will guess you are running into EBCDIC/ASCII issues. When you transfer 
ASCII, *all* the data in each record are converted to ASCII, but that should 
not be done with COMP-3 data, explaining your problem with those fields. 
When you transfer BINARY, *none* of the data are converted to ASCII, which 
means the COMP-3 data are still readable but the DISPLAY data are not (still 
use EBCDIC) ; meaning you can read COMP-3 but not the display.

What you need to due is EITHER
- Make all the data in the record DISPLAY format and transfer ASCII
OR
- Convert all display data to ASCII on the mainframe (leaving the COMP-3 
fields alone) and transfer BINARY.

And, you should probably confirm with your system administrators that the 
system is configured to do as I suspect: convert EBCDIC to ASCII when mode 
is ASCII and 'do nothing' when the mode is BINARY. I'm pretty sure this is 
the case, but it never hurts to check.
```

##### ↳ ↳ Re: FTPing COMP-3 data from mainframe to UNIX

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-05-24T12:43:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180035835.599403.255630@q66g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<Aif5i.2708$u56.2645@newssvr22.news.prodigy.net>`
- **References:** `<1179986957.656932.312050@b40g2000prd.googlegroups.com> <Aif5i.2708$u56.2645@newssvr22.news.prodigy.net>`

```
On 24 May, 13:11, "Michael Mattias" <mmatt...@talsystems.com> wrote:
> >    I am actually trying to ftp a PS file from mainframe to UNIX.
>
…[67 more quoted lines elided]…
> - Show quoted text -

I recall that when receiving files with packed fields on to a
mainframe (IBM) the system programmers had to set up a version of
XBPBATCH which would treat the records as fixed length rather than
allowing the system to treat packed numerics as premature end-of-
record codes. Does FTP and Unix suffer from the same problem (ie
seeing packed fields as control codes)?
```

###### ↳ ↳ ↳ Re: FTPing COMP-3 data from mainframe to UNIX

- **From:** kimi <mraghu83@gmail.com>
- **Date:** 2007-05-25T00:50:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1180079444.121734.174410@x18g2000prd.googlegroups.com>`
- **In-Reply-To:** `<1180035835.599403.255630@q66g2000hsg.googlegroups.com>`
- **References:** `<1179986957.656932.312050@b40g2000prd.googlegroups.com> <Aif5i.2708$u56.2645@newssvr22.news.prodigy.net> <1180035835.599403.255630@q66g2000hsg.googlegroups.com>`

```
On May 25, 12:43 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
> On 24 May, 13:11, "Michael Mattias" <mmatt...@talsystems.com> wrote:
>
…[78 more quoted lines elided]…
> - Show quoted text -
Tnx for ur suggestions guys...
Michael , your solution seems to be a logical one to the situation.But
it seems there is a need for a intermediate tool which can convert all
the non COMP data into ASCII before FTPing it in binary.

The tool should be able to do a fieldwise translation from EBCDIC to
ASCII so that i can exclude the COMP data from this process.Do u know
any tool which can do this job??

Another direction in which i can think of is in terms of any
manipulations that can be done with the
commands or options that is provided by microfocus in microfocus
server express..
Is there any way in which the Microfocus compiler can handle this
issue intelligently.. ???  Pls provide me some inputs on this..
```

###### ↳ ↳ ↳ Re: FTPing COMP-3 data from mainframe to UNIX

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-05-25T07:47:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PVA5i.6757$4Y.3666@newssvr19.news.prodigy.net>`
- **References:** `<1179986957.656932.312050@b40g2000prd.googlegroups.com> <Aif5i.2708$u56.2645@newssvr22.news.prodigy.net> <1180035835.599403.255630@q66g2000hsg.googlegroups.com> <1180079444.121734.174410@x18g2000prd.googlegroups.com>`

```
"kimi" <mraghu83@gmail.com> wrote in message 
news:1180079444.121734.174410@x18g2000prd.googlegroups.com...
> On May 25, 12:43 am, Alistair <alist...@ld50macca.demon.co.uk> wrote:
>> On 24 May, 13:11, "Michael Mattias" <mmatt...@talsystems.com> wrote:
…[7 more quoted lines elided]…
>>

> Michael , your solution seems to be a logical one to the situation.But
> it seems there is a need for a intermediate tool which can convert all
…[4 more quoted lines elided]…
> any tool which can do this job??

I could write one (to run on the Windows side) but...

> Is there any way in which the Microfocus compiler can handle this
> issue intelligently.. ???  Pls provide me some inputs on this..

If 'compiler' here refers to the human being, then yes. Re-designing the 
file would do that job. There are some tips on mixing packed/binary data 
with display data in the character-set conversion scenario (EBCDIC<==>ASCII) 
in this article on my web site:
http://www.talsystems.com/tsihome_html/downloads/C2IEEE.htm
```

###### ↳ ↳ ↳ Re: FTPing COMP-3 data from mainframe to UNIX

_(reply depth: 5)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-05-26T12:15:23+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f391c4$4mc$03$1@news.t-online.com>`
- **References:** `<1179986957.656932.312050@b40g2000prd.googlegroups.com> <Aif5i.2708$u56.2645@newssvr22.news.prodigy.net> <1180035835.599403.255630@q66g2000hsg.googlegroups.com> <1180079444.121734.174410@x18g2000prd.googlegroups.com> <PVA5i.6757$4Y.3666@newssvr19.news.prodigy.net>`

```
Top post (as Bill and I do)
My company has provided a thing callled DCP
(Data Conversion Processor) since the late 80's.
It's written in Cobol (including the conversion file
parsing as below).
Example for an instruction file that is
read by DCP -
TRANSLATE INPUT EBCDIC-TO-ASCII.
IF-CHARACTER POSITION=5 LENGTH=4 NOT-EQUAL=0000 GOTO=WEITER.
CONVBB POSITION=1 TO=1 ILENGTH=2 OLENGTH=2.
MOVE POSITION=3 TO=3 LENGTH=20.
*Insert different BGDB number
MOVE CHARACTER-VALUE=01 TO=23 LENGTH=2.
MOVE POSITION=25 TO=25 LENGTH=2.
MOVE BINARY-VALUE=1 TO=27 LENGTH=2.
TRANSLATE INPUT EBCDIC-TO-ASCII.
IF-CHARACTER POSITION=5 LENGTH=4 NOT-EQUAL=0000 GOTO=WEITER.
CONVBB POSITION=1 TO=1 ILENGTH=2 OLENGTH=2.
MOVE POSITION=3 TO=3 LENGTH=20.
*Insert different BGDB number
MOVE CHARACTER-VALUE=01 TO=23 LENGTH=2.
MOVE POSITION=25 TO=25 LENGTH=2.
MOVE BINARY-VALUE=1 TO=27 LENGTH=2.
MOVE POSITION=29 TO=29 LENGTH=17.
*Insert different BGDB number
MOVE CHARACTER-VALUE=01 TO=46 LENGTH=2.
*Insert different Katasteramtsschluessel
MOVE CHARACTER-VALUE=4380 TO=48 LENGTH=4.
MOVE POSITION=52 TO=52 LENGTH=17.
CONVBB POSITION=69 TO=69 ILENGTH=4 OLENGTH=4.
MOVE POSITION=73 TO=73 LENGTH=12.
CONVBB POSITION=85 TO=85 ILENGTH=4 OLENGTH=4.
MOVE POSITION=89 TO=89 LENGTH=2.
*Insert 3 fuer Kennzeichen Eroeffnungsbilanz
MOVE CHARACTER-VALUE=1 TO=91 LENGTH=1.
MOVE POSITION=92 TO=92 LENGTH=3.
CONVBB POSITION=95 TO=95 ILENGTH=4 OLENGTH=4.
MOVE POSITION=99 TO=99 LENGTH=500.
GOTO=SCHREIB.
LABEL=WEITER.
CONVBB POSITION=1 TO=1 ILENGTH=2 OLENGTH=2.
MOVE POSITION=3 TO=3 LENGTH=24.
CONVBB POSITION=27 TO=27 ILENGTH=2 OLENGTH=2.
MOVE POSITION=29 TO=29 LENGTH=540.
GOTO=SCHREIB.
LABEL=SCHREIB.
WRITE Datensatz.

With this "pseudo-language", you can manipulate conversions
as required.
Some  "psuedo" commands -
      *
      * MOVE-TYPE = RS MOVE RECORD SEPARATOR "TO"
      *             FS MOVE FIELD SEPARATOR "TO"
      *
      *             DT MOVE DATA "FROM" "TO" "LENGTH"
      *             LV MOVE LOW-VALUES "TO" "LENGTH"
      *             HV MOVE HIGH-VALUES "TO" "LENGTH"
      *             MS MOVE SPACES "TO" "LENGTH"
      *
      *             ML MOVE CHARACTER "CHARACTER-STRING" "TO" "LENGTH"
      *             MB MOVE BINARY VALUE "TO" "LENGTH"
      *             MP MOVE PACKED VALUE "TO" "LENGTH"
      *             MD MOVE DECIMAL VALUE "TO" "LENGTH"
      *
      * CONV-TYPES  C1 CONVERT BINARY > DECIMAL "FROM" "TO" "ILENGTH"
      *                                       "OLENGTH" "SIGN-TO"
      *             C2 CONVERT DECIMAL > BINARY "FROM" "TO" "ILENGTH"
      *                                       "OLENGTH"
      *             C3 CONVERT PACKED > DECIMAL "FROM" "TO" "ILENGTH"
      *                                       "OLENGTH" "SIGN-TO"
      *             C4 CONVERT DECIMAL > PACKED "FROM" "TO" "ILENGTH"
      *                                       "OLENGTH"
      *             C5 CONVERT PACKED > BINARY "FROM" "TO" "ILENGTH"
      *                                       "OLENGTH"
      *             C6 CONVERT BINARY > PACKED "FROM" "TO" "ILENGTH"
      *                                       "OLENGTH"
      *             C7 CONVERT DECIMAL > DECIMAL "FROM" "TO" "ILENGTH"
      *                                       "OLENGTH" "SIGN-TO"
      *             C8 CONVERT BINARY > BINARY "FROM" "TO" "ILENGTH"
      *                                       "OLENGTH"
      *             C9 CONVERT PACKED > PACKED "FROM" "TO" "ILENGTH"
      *                                        "OLENGTH"
      * IF-TYPES    IC IF-CHARACTER "FROM" "LITERAL" "LENGTH" "LABEL-TAG
      *             IB IF-BINARY "FROM" "VALUE" "LENGTH" "LABEL-TAG"
      *             IP IF-PACKED "FROM" "VALUE" "LENGTH" "LABEL-TAG"
      *             ID IF-DECIMAL "FROM" "VALUE" "LENGTH" "LABEL-TAG"
      *
      * MISC-TYPES  GT GOTO "MOVE-LABEL-NO" "LABEL-TAG"
      *             LB LABEL "LABEL-TAG"
      *             WR WRITE OUTPUT RECORD

Any proficient Cobol programmer should be able to knock
that up overnight :-)

Yes, the main prog has an EBCDIC->ASCII and ASCII->EBCDIC table that
may need to be adjusted depending on source (eg. In Germany,
differences on mainframe represantion of Umlauts)
Yes, the main prog (and parser prog)  depend on the ability to
access/define ONE-byte binary fileds.

And, no, unfortunately, it's not free.

Roger

"Michael Mattias" <mmattias@talsystems.com> schrieb im Newsbeitrag 
news:PVA5i.6757$4Y.3666@newssvr19.news.prodigy.net...
> "kimi" <mraghu83@gmail.com> wrote in message 
> news:1180079444.121734.174410@x18g2000prd.googlegroups.com...
…[52 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
