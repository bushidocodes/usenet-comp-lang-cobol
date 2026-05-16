[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading Excel from within a COBOL program

_5 messages · 4 participants · 2007-09_

---

### Reading Excel from within a COBOL program

- **From:** razor <iruddock@blueyonder.co.uk>
- **Date:** 2007-09-14T07:00:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189778424.722848.126610@57g2000hsv.googlegroups.com>`

```
Hi

I am trying to read in data from an Excel spreadsheet using SQL. I
have tried creating an ODBC link and then getting the ESQL assistant
to generate all the 'bits' that I need. It keeps telling me there are
no columns within the Excel file.

Has anyone done this and what does the SELECT statement look like. I
have managed to perform a successful connect within the program
without an error.

Even if I get the SELECT statement right I will need to generate host
variables.

I'm sick of generating a CSV file and then reading that, plus if I
have any commas within an addresses it goes out of step. I tried
telling excel that these address columns were text, hoping it would
enclose the contents in quotes, but no luck.

Any help appreciated.

Regards

Ian
```

#### ↳ Re: Reading Excel from within a COBOL program

- **From:** razor <iruddock@blueyonder.co.uk>
- **Date:** 2007-09-14T09:06:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189786016.145186.40960@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<1189778424.722848.126610@57g2000hsv.googlegroups.com>`
- **References:** `<1189778424.722848.126610@57g2000hsv.googlegroups.com>`

```
Aha

Solved it.

I had to define a named area in Excel with teh range I wanted to
access as a table. I'm only on N/E 3.1 so I would assume this is fixed
in the latest versions.

Thats the problem working on your own, no one to ask.
```

##### ↳ ↳ Re: Reading Excel from within a COBOL program

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-14T22:18:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2kjme35p2alvppdo5rpm1va7tfah4te7sq@4ax.com>`
- **References:** `<1189778424.722848.126610@57g2000hsv.googlegroups.com> <1189786016.145186.40960@22g2000hsm.googlegroups.com>`

```
On Fri, 14 Sep 2007 09:06:56 -0700, razor <iruddock@blueyonder.co.uk> wrote:

>Aha
>
…[4 more quoted lines elided]…
>in the latest versions.

That's the answer. No, it hasn't been fixed. The named range must have exactly one row of
column names. If the first row is data, you'll lose it.
```

#### ↳ Re: Reading Excel from within a COBOL program

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-14T13:30:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189801837.877343.289280@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<1189778424.722848.126610@57g2000hsv.googlegroups.com>`
- **References:** `<1189778424.722848.126610@57g2000hsv.googlegroups.com>`

```
On Sep 15, 2:00 am, razor <irudd...@blueyonder.co.uk> wrote:
> Hi
>
…[15 more quoted lines elided]…
> enclose the contents in quotes, but no luck.

I presume by 'generating a CSV' you are doing it by loading it into
Excel manually.  There are several tools that will extract from a
spreadsheet reliably. I use xlhtml which is free. It was for creating
html page but will create a CSV correctly.

Of course when you process the CSV file you have to recognise that the
text fields are quoted and that an embedded comma is not a field
terminator, but that is not hard. It is probably best not to use
uunstring but to process character by character.

Gnumeric also has a free xls to csv batch converter.

I have programs that fetch email, extract attachments, convert
the .xls and then process the data to produce sales orders and other
documents fed into business systems, all without any manual
intervention. It also sends an email back saying what had been done to
confirm. These use free tools such as xlhtml and munpack.
```

#### ↳ Re: Reading Excel from within a COBOL program

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-14T14:46:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ijsle3laasr7on0ocg2oo2i4bi1e4rg9b0@4ax.com>`
- **References:** `<1189778424.722848.126610@57g2000hsv.googlegroups.com>`

```
On Fri, 14 Sep 2007 07:00:24 -0700, razor <iruddock@blueyonder.co.uk>
wrote:

>I'm sick of generating a CSV file and then reading that, plus if I
>have any commas within an addresses it goes out of step. I tried
>telling excel that these address columns were text, hoping it would
>enclose the contents in quotes, but no luck.

I use tab delimited files here:
05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.       
05  RO-INST             PIC X(03).                     
05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.       
05  RO-EXT              PIC X(05).                     
05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.       
05  RO-SID              PIC X(09).                     
05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.       


Before each write, I compress leading and trailing spaces with a small
routine.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
