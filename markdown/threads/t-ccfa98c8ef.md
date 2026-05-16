[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and C/C++

_7 messages · 7 participants · 2001-11_

---

### COBOL and C/C++

- **From:** "Matthias Philipp" <wrongmail@web.de>
- **Date:** 2001-11-06T12:10:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9s8g7h$11cei2$1@ID-109843.news.dfncis.de>`

```
Hello out there!
I'm a COBOL-Newbie and I have to read a COBOL-Data-File with C/C++. Are
there any includes for C for that job?
I wonder if there is any possibility to read a cobol-structure into a
c-struct.
thanks for any help!

Matthias
```

#### ↳ Re: COBOL and C/C++

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-11-06T13:06:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AfRF7.75165$tb2.6004396@bin2.nnrp.aus1.giganews.com>`
- **References:** `<9s8g7h$11cei2$1@ID-109843.news.dfncis.de>`

```
There is no such thing as a "COBOL-Data-File."

1. COBOL can write standard sequential text files.
2. COBOL can write files in organizational formats proprietary (=secret) to
the compiler in use.
3. COBOL can access standard database formats (BTrieve, Access, Excel,
etc.).

If #1 or #3, you're golden.

If #2, you still have two choices: A) Write a COBOL program to read the file
under investigation and output the file in some (text?) format you can
access, or B) Use - with varying degrees of effort and success - third party
conversion routines.

If, for example, you have a production COBOL ISAM file that you want to
fiddle with using C, (keeping the original file and file structure), you
have a career.

I could be out of date on the above, but I firmly believe it's turtles all
the way down.


"Matthias Philipp" <wrongmail@web.de> wrote in message
news:9s8g7h$11cei2$1@ID-109843.news.dfncis.de...
> Hello out there!
> I'm a COBOL-Newbie and I have to read a COBOL-Data-File with C/C++. Are
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL and C/C++

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-11-09T06:53:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BEB7D66.7FBA2CC3@Azonic.co.nz>`
- **References:** `<9s8g7h$11cei2$1@ID-109843.news.dfncis.de> <AfRF7.75165$tb2.6004396@bin2.nnrp.aus1.giganews.com>`

```
JerryP wrote:
> 
> If, for example, you have a production COBOL ISAM file that you want to
> fiddle with using C, (keeping the original file and file structure), you
> have a career.

Microfocus provided a callable routine for its file handler and this can
be called by C programs.  As it is the actual file handler it maintains
the integrity of the Cobol file even when concurrently accessing with
Cobol or other C programs.

Of course you still need to know the format of the data and ensure that
the record fields are not corrupted.
```

#### ↳ Re: COBOL and C/C++

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-11-06T13:19:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ArRF7.289$ea5.74175@paloalto-snr1.gtei.net>`
- **References:** `<9s8g7h$11cei2$1@ID-109843.news.dfncis.de>`

```
http://www.flexus.com/downloads.html
Get file COBDATA.ZIP; this is a tutorial on COBOL data types.

You will also find http://www.flexus.com/ebd2asc.html useful; it addresses
the question, "How can I convert COBOL-created data for use in my BASIC,
C/C++ or other non-COBOL programs, and what about EBCDIC-ASCII
considerations?"

If you are looking for something where you can just call a DLL to convert
data on the fly, I have a freeware DLL you may use for non-commercial
purposes (I explain what that means). You will get a questionnaire to
answer; but that you are a programmer, but not a COBOL programmer (well, a
"newbie" by your own standards) means you are exactly the target audience
for whom I developed this conversion software.
```

#### ↳ Re: COBOL and C/C++

- **From:** Daniel Jacot<daniel.jacot@winterthur.ch>
- **Date:** 2001-11-07T15:55:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_PcG7.16072$xS6.23680@www.newsranger.com>`
- **References:** `<9s8g7h$11cei2$1@ID-109843.news.dfncis.de>`

```

On Tue, 6 Nov 2001 12:10:08 +0100, in article
<9s8g7h$11cei2$1@ID-109843.news.dfncis.de>, Matthias Philipp stated...
>
>Hello out there!
…[7 more quoted lines elided]…
>

As usual, the best answer is 'it depends '.

It depends on the operating system, the file-organisation and the code page of
the file  (ASCII, EBCDIC).
It depends on the COBOL datatypes you use. There is no direct equivalent to the
COBOL COMP-3 (packed-decimal), nor to numeric picture items in C. Strings are
not '\0' terminated but either fixed or variable in length.
It depends on the COBOL compiler you used to produce the file.
It depends on the C/C++ compiler you want to use to read the file.

Please post the COBOL structure and give us  the  informations  mentioned above.
Post the C/C++ code you have written so far. Post the problems you encountered
so far.  Maybe we are willing to help you then. Maybe we will ask you to RTFM.

-------------------------------------------------
With kind regards
Daniel Jacot
-------------------------------------------------
visit us at: http://www.winterthur.com
```

#### ↳ Re: COBOL and C/C++

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-11-07T19:34:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9scp17017r7@enews2.newsguy.com>`
- **References:** `<9s8g7h$11cei2$1@ID-109843.news.dfncis.de>`

```
There's a hilariously named product out there--COBjects--that
purports to give you a COM-based interface to a wide variety of
data formats used by common cobol systems.  I can't vouch for
it, but it sounds applicable.

"Matthias Philipp" <wrongmail@web.de> wrote in message
news:9s8g7h$11cei2$1@ID-109843.news.dfncis.de...
> Hello out there!
> I'm a COBOL-Newbie and I have to read a COBOL-Data-File with
C/C++. Are
> there any includes for C for that job?
> I wonder if there is any possibility to read a cobol-structure
into a
> c-struct.
> thanks for any help!
…[3 more quoted lines elided]…
>
```

#### ↳ Re: COBOL and C/C++

- **From:** Vadim Maslov <vadik@siber.com>
- **Date:** 2001-11-16T07:46:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BF4C4F8.A89E9BD8@siber.com>`
- **References:** `<9s8g7h$11cei2$1@ID-109843.news.dfncis.de>`

```
You can use DataAccess COM component from Siber Systems.

It can read Cobol data files straight into your program
for MF, FSC, RM and Acu Cobol data files.

It does not use ODBC, so it is fast.

http://www.siber.com/sct/datafile/

Vadim Maslov
Siber Systems


Matthias Philipp wrote:
> 
> Hello out there!
…[6 more quoted lines elided]…
> Matthias
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
