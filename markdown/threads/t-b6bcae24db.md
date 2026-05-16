[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comp-3 data or not?

_5 messages · 4 participants · 1999-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Comp-3 data or not?

- **From:** "Tony" <triordan@_ame.ie>
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hs3hr$664$1@news2.news.iol.ie>`

```
I am an engineer with no experience of Cobol. I have a cobol data file that
I have successfully read into a Visual Basic application except for a couple
of fields that have me stumped. I have read through Michael Mattias's
excellent data type descriptions without resolving my problem.
The problem is a field defined as "PIC S9(06) COMP-3". Now this seems fine
and should hold a packed decimal field in 4 bytes, least sig. nibble a sign,
C,D or F. The fields are supposed to hold dates, what dates I don't know.

The four bytes in each field are as follows:
00 20 19 E6 . . . This is the date on which this report was generated
00 90 89 E6 . . . This is the FROM date
00 20 19 E6 . . . This is the TO date.

If anyone would like to comment or tell me I'm an idiot, please do.

Tony Riordan
AME Ltd.,
Ireland
```

#### ↳ Re: Comp-3 data or not?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-dOGmvWhCl5bU@Dwight_Miller.iix.com>`
- **References:** `<7hs3hr$664$1@news2.news.iol.ie>`

```
On Tue, 18 May 1999 16:16:06, "Tony" <triordan@_ame.ie> wrote:

> I am an engineer with no experience of Cobol. I have a cobol data file that
> I have successfully read into a Visual Basic application except for a couple
…[9 more quoted lines elided]…
> 00 20 19 E6 . . . This is the TO date.


It looks to me like the fields were corrupted in an EBCDIC to ASCII 
transfer.  Possible?

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Comp-3 data or not?

- **From:** MKS <m_k_s@hotmail.com>
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3741B6A8.D2FC3822@hotmail.com>`
- **References:** `<7hs3hr$664$1@news2.news.iol.ie>`

```
Tony,

What is the actual appearance of the data on the mainframe?

0096    021E
021E or 0096 the first could be 97083 (9 complement of julian)

0096    098E
098E or 0096 the first could be 90013 (9 complement of julian)

0096    021E
021E or 0096 the first could be 97083 (9 complement of julian)

Matt
```

#### ↳ Re: Comp-3 data or not?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hsrf7$p78@sjx-ixn6.ix.netcom.com>`
- **References:** `<7hs3hr$664$1@news2.news.iol.ie>`

```
On IBM mainframes, there is an "odd" (and little used) option which does
allow sign-nibbles of "B" and "E". Check out the NUMCLS(ALT) compiler option
described in any current COBOL manual.  Online, you can read a little about
it at:

 http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYMG201/4%2e2%2e1

(or in the Programmers or Installation Guides).

As far as I know, COBOL will never produce (output) a field with a "B" or
"E" sign-nibble, but there assembler instructions that can do this.
```

#### ↳ Re: Comp-3 data or not?

- **From:** Alex Romaniuk <ales.romaniuk@zag.si>
- **Date:** 1999-05-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37424D11.3296@zag.si>`
- **References:** `<7hs3hr$664$1@news2.news.iol.ie>`

```
Tony wrote:
> 
> I am an engineer with no experience of Cobol. I have a cobol data file that
…[16 more quoted lines elided]…
> Ireland

First of all, you should know, what to do with dates. If you want only
to hold an information, than any 9(6) ??? works fine. If you need
something
more (e.g.sorting etc.), it would probably be better to use ordinary
numerical
data type  9(6). You should also think about y2k problem when sorting.
I always am using PIC 9(8) for all dates. It can be easily viewed thru
any editor,
can be manually changed, or sorted without any problems. I use COMP
fields only
for amounts or counters or similiary (they really increase
performances).
If you want to spare some memory, or disk space with using COMP instead
normal
numeric field, then think about:
- Is it worth to complicate, if I plan to have max. of 1000 records/file
with date field
- I want to review date values many times thru any viewer possible
- I need certain performances (complex calculation etc..)
etc..


Regards
Alex
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
