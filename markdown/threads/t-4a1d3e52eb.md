[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# short step towards re-engineering

_6 messages · 6 participants · 2000-08_

---

### short step towards re-engineering

- **From:** "kiran" <slsup@bom6.vsnl.net.in>
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8mvf85$jhn$1@news.vsnl.net.in>`

```
Hello!
         As we know that there is no fixed file format for the COBOL
Databases. Now, what I am doing is, I am analyzing the source code, scan the
data division for the record structure of the file. I am preparing a *Data
Dictionary * that will contain the basic structure of the records such as
Table name corresponding to the Record Name; Fields and its different
attributes such as type, size etc. Now, a query arrives and demands some
data which is in COBOL format.
        My question is how to *map* this data dictionary with the actual
data files which are in COBOL format. Any suggestions???
```

#### ↳ Re: short step towards re-engineering

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<ZgCk5.393$FD4.50752@paloalto-snr1.gtei.net>`
- **References:** `<8mvf85$jhn$1@news.vsnl.net.in>`

```
Let me suggest some materials for you to use in your research.

Courtesy of Flexus, there are some materials on their website for download:

at www.flexus.com/softwaredownload.html you can get file COBDATA.ZIP, a text
and graphics tutorial on COBOL datatypes, and COBFD.ZIP, a record analyzer
which works the same as your proposed scanner.

at www.flexus.com/ebd2asc.html

you can read about data conversion issues, both COBOL to IEEE datatypes and
EBCDIC - ASCII issues.

As far as constructing a "query tool" which would work by mapping the
data-division record types against full records... I have a 32-bit Windows
DLL and some BASIC-language source code which shows how to do that. For
those you'll have to write me.

(No, I don't have it in COBOL.)

-
Michael Mattias
Tal Systems
Racine WI USA
michael.mattias@gte.net
(Author of the stuff on the Flexus web site).

kiran <slsup@bom6.vsnl.net.in> wrote in message
news:8mvf85$jhn$1@news.vsnl.net.in...
> Hello!
>          As we know that there is no fixed file format for the COBOL
> Databases. Now, what I am doing is, I am analyzing the source code, scan
the
> data division for the record structure of the file. I am preparing a *Data
> Dictionary * that will contain the basic structure of the records such as
…[5 more quoted lines elided]…
>
```

#### ↳ Re: short step towards re-engineering

- **From:** lcccpiasabird@my-deja.com
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8mv6gg$9ak$1@nnrp1.deja.com>`
- **References:** `<8mvf85$jhn$1@news.vsnl.net.in>`

```
In article <8mvf85$jhn$1@news.vsnl.net.in>,
  "kiran" <slsup@bom6.vsnl.net.in> wrote:

Try using some sql to determine the longest element in the fields maybe
putting the length of the variable out and then taking the max of all
of those values.  Then use that for the fixed length for each given
field.  Maybe sql can do that.

Or
If you just ran the sql on the fields you want it would make a report
wide enough for the widest element.  If you do it in a fixed length
font you can determine the length.  Make the database do the work.
Imagine them asking why you need all the cycle time, Hee Hee.

Or you could just make a utility program to determine the length of all
the fields as you read each one and store the maximum and print it out
at the end then hard code the field length.  Tallying would be good for
text and just the highest number could be used to determing the numeric
length.  Boy would that be a pain!

sql sounds a lot better.
> Hello!
>          As we know that there is no fixed file format for the COBOL
> Databases. Now, what I am doing is, I am analyzing the source code,
scan the
> data division for the record structure of the file. I am preparing a
*Data
> Dictionary * that will contain the basic structure of the records
such as
> Table name corresponding to the Record Name; Fields and its different
> attributes such as type, size etc. Now, a query arrives and demands
some
> data which is in COBOL format.
>         My question is how to *map* this data dictionary with the
actual
> data files which are in COBOL format. Any suggestions???
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: short step towards re-engineering

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hqt8pso87aevg6a07lvoesjstmp5h7kfh3@4ax.com>`
- **References:** `<8mvf85$jhn$1@news.vsnl.net.in> <8mv6gg$9ak$1@nnrp1.deja.com>`

```
>>          As we know that there is no fixed file format for the COBOL
>> Databases. Now, what I am doing is, I am analyzing the source code,
…[11 more quoted lines elided]…
>> data files which are in COBOL format. Any suggestions???

i think what you are doing suggests some product i saw years ago
called relativity, which connects to cobol data files. to me you are
doing overkill, if you use two languages to get the job done.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: short step towards re-engineering

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 2000-08-10T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<399336A9.B7FA1E4E@siber.com>`
- **References:** `<8mvf85$jhn$1@news.vsnl.net.in>`

```
kiran wrote:
> 
> Hello!
…[8 more quoted lines elided]…
> data files which are in COBOL format. Any suggestions???

The easiest way is to license our DataAccess library.
It will take file and record description (FDD and RDD files)
and it will be able to read Cobol data records in several
formats (MF, FSC, RM, ACU) and present them in a way
understood by C++ programs.

More details on it at http://www.siber.com/sct/datafile/

If you ask me: is it cheaper to write such library myself,
then the answer would be No. We are doing this datafile 
reading stuff for the 3rd year now and we still have bugs 
to fix in the new data formats.

The problem with Cobol data files formats is that 
they are not really documented anywhere and 
there's a lot of them (we are aware of at least 20).
So a lot of investigative work is required when 
trying to read (shall we say, unencrypt -) a Cobol data file.

Look for our new release 3.8.1 (to come out in 2-3 days),
it will add 3 new data file formats. But probably you can
read your format with the existing library.

We have Evaluation Package available.

Regards,
Vadim Maslov
Siber Systems
```

#### ↳ Re: short step towards re-engineering

- **From:** g_t_g@my-deja.com
- **Date:** 2000-08-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8nhk9j$puh$1@nnrp1.deja.com>`
- **References:** `<8mvf85$jhn$1@news.vsnl.net.in>`

```
Try an ODBC product. It will make your project much much easier.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
