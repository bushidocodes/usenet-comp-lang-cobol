[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# pass tables of data in Cobol to any other format

_4 messages · 4 participants · 2003-12_

---

### pass tables of data in Cobol to any other format

- **From:** "Elite" <alvaro.herbecon@terra.es>
- **Date:** 2003-12-10T11:27:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AqDBb.1792962$uj6.4327531@telenews.teleline.es>`

```
Hello!
 It would please me to know as I can pass tables of data in Cobol to any
other format (DBase, Paradox, Acces, etc..)
  I thank for your aid.
 A greeting.
```

#### ↳ Re: pass tables of data in Cobol to any other format

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-12-10T12:46:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HAEBb.10692$aw2.5424475@newssrv26.news.prodigy.com>`
- **References:** `<AqDBb.1792962$uj6.4327531@telenews.teleline.es>`

```
"Elite" <alvaro.herbecon@terra.es> wrote in message
news:AqDBb.1792962$uj6.4327531@telenews.teleline.es...
> Hello!
>  It would please me to know as I can pass tables of data in Cobol to any
> other format (DBase, Paradox, Acces, etc..)
>   I thank for your aid.

If you are talking specifically about dBase, Paradox(r), Access(r) and other
RDBMS products, you'd probably want to look at using embedded SQL. Consult
your compiler manual for implementation details for your brand and version
of the compiler.

If you are speaking generically, the COBOL CALL verb can pass the address of
the start of a COBOL table, which surely can be interpreted by the CALLed
program or module. Details and mechanics vary by operating system and in
some cases by compiler.

MCM
```

#### ↳ Re: pass tables of data in Cobol to any other format

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-10T19:35:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br7shi$2fg$1@peabody.colorado.edu>`
- **References:** `<AqDBb.1792962$uj6.4327531@telenews.teleline.es>`

```

On 10-Dec-2003, "Elite" <alvaro.herbecon@terra.es> wrote:

> Hello!
>  It would please me to know as I can pass tables of data in Cobol to any
> other format (DBase, Paradox, Acces, etc..)
>   I thank for your aid.
>  A greeting.

CoBOL doesn't have a native format.   To pass data so that some other program
can access it, what you need to do is learn exactly what your other program
needs.

The easiest way to move data so that a spreadsheet can read it is to write it
out so that the spreadsheet can import it.   Sometimes this will be in tab
delimited files with numbers the way you see it in the spreadsheet.    I have
written programs that create files with tab delimited fields, making sure to
write all numbers with signs.

The following is the beginning of a record format I used on my EBCDIC mainframe
to produce a file that was FTP'd to a PC and imported into an Excel spreadsheet:

 01  SPREAD-REC.
     05  FILLER              PIC X(01)   VALUE '"'.
     05  SPREAD-BUCKET       PIC X(06)   VALUE 'BUCKET'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.

     05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.
     05  SPREAD-ID           PIC X(09)   VALUE 'ID'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.

     05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.
     05  SPREAD-NAME         PIC X(32)   VALUE 'NAME'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.

     05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.
     05  SPREAD-EXT          PIC X(03)   VALUE 'EXT'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.


     05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.
     05  FILLER-TRANS-AMT                VALUE 'TRANS-AMT'.
         10  SPREAD-TRANS-AMT PIC -(7).99.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.

     05  FILLER-DELIMITER    PIC X(01)   VALUE X'05'.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.
     05  FILLER-PAID-AMT                 VALUE 'PAID-AMT'.
         10  SPREAD-PAID-AMT PIC -(7).99.
     05  FILLER-QUOTES       PIC X(01)   VALUE '"'.


Some people will recommend SIGN SEPARATE, but this worked for me.    Binary and
packed do not work.
```

#### ↳ Re: pass tables of data in Cobol to any other format

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2003-12-12T19:23:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EAoCb.1693$NNW1.45@news04.bloor.is.net.cable.rogers.com>`
- **References:** `<AqDBb.1792962$uj6.4327531@telenews.teleline.es>`

```
There are two ways:
    programmatically, using SQL
    No programming, dump your table out as text file delimited and import it
into DB


"Elite" <alvaro.herbecon@terra.es> wrote in message
news:AqDBb.1792962$uj6.4327531@telenews.teleline.es...
> Hello!
>  It would please me to know as I can pass tables of data in Cobol to any
…[4 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
