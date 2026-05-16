[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Program to Convert copybook to C structure

_7 messages · 7 participants · 2005-10 → 2005-12_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Program to Convert copybook to C structure

- **From:** "Karen Monkres" <Gypsy3515@ev1.net>
- **Date:** 2005-10-21T12:46:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11liacffvpjli77@corp.supernews.com>`

```
Is there a program that will convert a copybook record layout to a C 
structure?  Thanks

Ron
```

#### ↳ Re: Program to Convert copybook to C structure

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-10-21T22:29:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hZd6f.1220$Y61.1182@newssvr33.news.prodigy.com>`
- **References:** `<11liacffvpjli77@corp.supernews.com>`

```
> Is there a program that will convert a copybook record layout to a C
> structure?  Thanks

I've never seen one.

Then again, you can probably convert a 100-member COBOL record to C format
in about 30 minutes and it's 'by definition' a one-time job, so I'm not
surprised no one has ever tried to create a 'utility' to do it

But if you don't know the COBOL datatypes, it would be pretty hard. So
download this...
http://www.flexus.com/ftp/cobdata.zip
.. for a tutorial on COBOL datatypes. (The included software is VERY old and
not much fun to use, but the text is still good)

If you have a COBOL source or copyboook, this might be useful:
http://www.flexus.com/ftp/cobfd.zip
That's some MS-DOS (you heard me, MS-DOS) software which will parse your
file and create a report of offsets and data lengths for every variable in
the copybook.
```

##### ↳ ↳ Re: Program to Convert copybook to C structure

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-10-21T23:44:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m3f6f.32767$cw3.6517@fe01.news.easynews.com>`
- **References:** `<11liacffvpjli77@corp.supernews.com> <hZd6f.1220$Y61.1182@newssvr33.news.prodigy.com>`

```
Micro Focus used to have a utility that created COPY members out of header files 
(if I recall correctly) - but I don't recall anything that did the opposite.  (I 
could be wrong on this and I don't know if it is still available)
```

###### ↳ ↳ ↳ Re: Program to Convert copybook to C structure

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2005-10-24T09:00:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hltpl1d20c25f8aorh0va46ked1hjjvlt4@4ax.com>`
- **References:** `<11liacffvpjli77@corp.supernews.com> <hZd6f.1220$Y61.1182@newssvr33.news.prodigy.com> <m3f6f.32767$cw3.6517@fe01.news.easynews.com>`

```
On Fri, 21 Oct 2005 23:44:18 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Micro Focus used to have a utility that created COPY members out of header files 
>(if I recall correctly) - but I don't recall anything that did the opposite.  (I 
>could be wrong on this and I don't know if it is still available)

Some IDDs allow us to have working data structures that are read by
multiple languages.

Of course a procedure division copy member doesn't work this way.
```

###### ↳ ↳ ↳ Re: Program to Convert copybook to C structure

- **From:** Wiggy <wignomore@btopenworld.com>
- **Date:** 2005-10-25T23:28:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<djmf31$hvt$1@nwrdmz02.dmz.ncs.ea.ibs-infra.bt.com>`
- **In-Reply-To:** `<m3f6f.32767$cw3.6517@fe01.news.easynews.com>`
- **References:** `<11liacffvpjli77@corp.supernews.com> <hZd6f.1220$Y61.1182@newssvr33.news.prodigy.com> <m3f6f.32767$cw3.6517@fe01.news.easynews.com>`

```
William M. Klein wrote:
> Micro Focus used to have a utility that created COPY members out of header files 
> (if I recall correctly) - but I don't recall anything that did the opposite.  (I 
> could be wrong on this and I don't know if it is still available)

The h2cpy utility still ships with both Net Express and Server Express, 
though unfortunately (for the o.p.) it only converts C headers to COBOL 
copybooks, and not the reverse.

SimonT.
```

#### ↳ Re: Program to Convert copybook to C structure

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-10-25T16:59:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130284781.271392.5140@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<11liacffvpjli77@corp.supernews.com>`
- **References:** `<11liacffvpjli77@corp.supernews.com>`

```
> Is there a program that will convert a copybook record
> layout to a C structure?

It is unlikely to be useful to do that.  Cobol has types of data that
aren't implemented in C so you cannot just map a struct over a Cobol
record and then expect to use the data items.

For example a Cobol alphanumeric data item may be PIC X(24) and this is
space filled 24 characters. C would usually require a null terminator
to make this a string and so would need to be char name[25] with null
moved to name[24].

Numeric items may be display format with implied decimal point, or
packed decimal or binary.

The data items will need extracting and converting into a C structure
of your own devicing.
```

##### ↳ ↳ Re: Program to Convert copybook to C structure

- **From:** Last Boy Scout <eggbtr@ezl.com>
- **Date:** 2005-12-27T01:56:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jp6sf.2788$Z95.2766@fe04.lga>`
- **In-Reply-To:** `<1130284781.271392.5140@z14g2000cwz.googlegroups.com>`
- **References:** `<11liacffvpjli77@corp.supernews.com> <1130284781.271392.5140@z14g2000cwz.googlegroups.com>`

```
Richard wrote:

>>Is there a program that will convert a copybook record
>>layout to a C structure?
…[16 more quoted lines elided]…
> 
These conversion type programs never work very well.  You may need some 
kind of program in the middle to convert it or that can access it to 
convert things like packed fields and convert them to unpacked fields 
that can be accessed. Fortran reads packed numeric fields quite well.

You could write a program to convert the copybook, but when you run into 
  things like a Redefine statement how do you handle that?  COBOL takes 
the same space and can address it differently under different 
conditions.  For instance Fortran can do this because it uses the 
distance from the beginning of a record to describe a field.  It also 
can access the right and left nibble in a packed field.

I never really studied Fortran, but I use a program that can read 
indexed VSAM Files and access them like TABLES.  Not exactly SQL but 
pretty close.  You will need to think about a conversion program 
in-between COBOL Files and ASCII Files.  COBOL Can be used to unpack 
numeric fields and make them more readable.  The program we use we 
sometimes use a COBOL program we can call that parses one record at a time.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
