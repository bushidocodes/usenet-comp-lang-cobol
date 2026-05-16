[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SOURCEFORMAT AND COPY LIBRARY

_10 messages · 6 participants · 2005-03_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### SOURCEFORMAT AND COPY LIBRARY

- **From:** apknight@gmail.com (apknight)
- **Date:** 2005-03-07T00:12:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95895e6d.0503070012.13599100@posting.google.com>`

```
sorry.  my english is very poor. so my text is not proof reading -_-a


If SOURCEFORMAT was FREE, Copy text was Fixed?


example:


      $ SET SOURCEFORMAT "FREE"

IDENTIFICATION DIVISION.

PROGRAM-ID.  Aroma96exam.



*STUDENT NAME .................................................

*STUDENT ID   .....................................................



ENVIRONMENT DIVISION.

INPUT-OUTPUT SECTION.

FILE-CONTROL.



DATA DIVISION.

COPY "abc.txt".

.............



abc.txt was fixed or free?



01 dat1 pic x(10).    <-?



         01 data pic x(10) <-?
```

#### ↳ Re: SOURCEFORMAT AND COPY LIBRARY

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-03-07T06:51:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<afdb7$422c4e68$45491f85$25530@KNOLOGY.NET>`
- **In-Reply-To:** `<95895e6d.0503070012.13599100@posting.google.com>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com>`

```
apknight wrote:
> sorry.  my english is very poor. so my text is not proof reading -_-a
> 
…[11 more quoted lines elided]…
> PROGRAM-ID.  Aroma96exam.

I'm not sure what compiler you're using, but the one I have (Fujitsu) 
has settings for "Source Format" for both the program, and the copy 
texts.  Check the compiler's manual and see if SOURCEFORMAT can take two 
arguments.  :)
```

##### ↳ ↳ Re: SOURCEFORMAT AND COPY LIBRARY

- **From:** Russell <rws0203nospam@comcast.net>
- **Date:** 2005-03-07T11:16:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns96127CE1F176Arws0203comcastnet@216.196.97.131>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com> <afdb7$422c4e68$45491f85$25530@KNOLOGY.NET>`

```
LX-i <lxi0007@netscape.net> wrote in news:afdb7$422c4e68$45491f85$25530
@KNOLOGY.NET:

> apknight wrote:
>> sorry.  my english is very poor. so my text is not proof reading -_-a
…[16 more quoted lines elided]…
> texts.  Check the compiler's manual and see if SOURCEFORMAT can take 
two 
> arguments.  :)
> 
> 

    	Another option would be use a format in cpy files that works
with both free and normal.  Eg, columns 01-06 are blank (only), never go 
past column 72, comments are marked by an "*" in column 07, and a ">" in 
column 08.  You are not allowed to put "-" in column 07 (or anything else 
but spaces as well).

    	Start paragraph names in column 08, all else in column 12.

    	Have I missed anything?

    	This should work whether or not you are in "free" mode or not.
```

###### ↳ ↳ ↳ Re: SOURCEFORMAT AND COPY LIBRARY

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-03-07T19:20:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IP1Xd.4391408$f47.787549@news.easynews.com>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com> <afdb7$422c4e68$45491f85$25530@KNOLOGY.NET> <Xns96127CE1F176Arws0203comcastnet@216.196.97.131>`

```
Actually, you don't need to put the "*" in column 7 and the ">" in column 8.

If you start a line with "*>" anywhere after column 6, it will work.

You don't talk about the "/" for page eject - but I don't see that in very 
common usage anymore.  The '02 Standard allows fixed and free format to have a
    >>PAGE
statement.

You also don't talk about debugging lines. In the '02 Standard, both fixed and 
free format support
    >>D
```

###### ↳ ↳ ↳ Re: SOURCEFORMAT AND COPY LIBRARY

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-03-07T11:25:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1110223527.220749.297420@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<IP1Xd.4391408$f47.787549@news.easynews.com>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com> <afdb7$422c4e68$45491f85$25530@KNOLOGY.NET> <Xns96127CE1F176Arws0203comcastnet@216.196.97.131> <IP1Xd.4391408$f47.787549@news.easynews.com>`

```
> 1) Actually, you don't need to put the "*" in column 7 and the ">" in
column 8.

> 2) If you start a line with "*>" anywhere after column 6, it will
work.

2) is compiler dependent.  1) should work with _any_ compiler, even
'74.
```

###### ↳ ↳ ↳ Re: SOURCEFORMAT AND COPY LIBRARY

_(reply depth: 4)_

- **From:** Russell <rws0203nospam@comcast.net>
- **Date:** 2005-03-07T14:54:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns9612A1D3AADD0rws0203comcastnet@216.196.97.131>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com> <afdb7$422c4e68$45491f85$25530@KNOLOGY.NET> <Xns96127CE1F176Arws0203comcastnet@216.196.97.131> <IP1Xd.4391408$f47.787549@news.easynews.com>`

```
    	I don't know how widespread the "*>" comment is.  A "*>" in
col 7 would work on any compiler.  However, since we are talking
about compilers that support freeform, I suppose that the
distinction is pointless.

    	I have no idea what to do about "/" and "D", other than
do not use.

    	


"William M. Klein" <wmklein@nospam.netcom.com> wrote in
news:IP1Xd.4391408$f47.787549@news.easynews.com: 

> Actually, you don't need to put the "*" in column 7 and the ">" in
> column 8. 
…[12 more quoted lines elided]…
> 

> LX-i <lxi0007@netscape.net> wrote in news:afdb7$422c4e68$45491f85$25530
> @KNOLOGY.NET:
…[26 more quoted lines elided]…
> with both free and normal.  Eg, columns 01-06 are blank (only), never 
go
> past column 72, comments are marked by an "*" in column 07, and a ">" 
in
> column 08.  You are not allowed to put "-" in column 07 (or anything 
else
> but spaces as well).
>
…[4 more quoted lines elided]…
>    This should work whether or not you are in "free" mode or not.
```

###### ↳ ↳ ↳ Re: SOURCEFORMAT AND COPY LIBRARY

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-03-07T15:11:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4642e$422cc399$45491f85$7817@KNOLOGY.NET>`
- **In-Reply-To:** `<IP1Xd.4391408$f47.787549@news.easynews.com>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com> <afdb7$422c4e68$45491f85$25530@KNOLOGY.NET> <Xns96127CE1F176Arws0203comcastnet@216.196.97.131> <IP1Xd.4391408$f47.787549@news.easynews.com>`

```
William M. Klein wrote:
> Actually, you don't need to put the "*" in column 7 and the ">" in column 8.

You do if you want it to work with fixed format as well...  :)
```

##### ↳ ↳ Re: SOURCEFORMAT AND COPY LIBRARY

- **From:** apknight@gmail.com
- **Date:** 2005-03-07T16:34:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1110242077.686639.137820@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<afdb7$422c4e68$45491f85$25530@KNOLOGY.NET>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com> <afdb7$422c4e68$45491f85$25530@KNOLOGY.NET>`

```
If I has not setting "SOURCE FORMAT" the copy texts, was occured error?
( only setting original source marked "free" )
```

#### ↳ Re: SOURCEFORMAT AND COPY LIBRARY

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-03-07T18:41:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pf1Xd.597407$6l.477586@pd7tw2no>`
- **In-Reply-To:** `<95895e6d.0503070012.13599100@posting.google.com>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com>`

```
apknight wrote:
> sorry.  my english is very poor. so my text is not proof reading -_-a
> 
…[45 more quoted lines elided]…
>          01 data pic x(10) <-?

I assume you are using a Micro Focus compiler. I think, (but could be 
wrong), that they are the only ones who use $set to indicate Directives.

Whether or not you use fixed or free format I think is just a personal 
preference. I prefer fixed giving me a margin around my text, which I 
find more 'pleasing' - and using 'portrait' (8.5 x 11), there is room to 
use a three-hole punch so that you can put source into a binder. (Not 
that I do that - but the facility is there).

Back through the 60's-80's on mainframes with print barrels that gave 
only Uppercase then free format would have been useful. The 80 column 
maximum meant that printing on continuous 11 x 14 there was a fair 
amount of paper wastage on the right side of each sheet.

You can (assuming Micro Focus again), use free format with a maximum 
line of 250 characters. Now try and print it out - you would have to 
select 'landscape' and chances are you will finish up with a fair amount 
of wastage on the right, yet again.

Never tried it - but do you have to put that very first $set 
sourceformat "free", starting in Column 7. Presumably all subsequent 
lines can be coded to the extreme left starting at Column 1. Again no 
knowledge of it, but I would have thought copy 'abc.txt' also starts in 
Column 1 - although if using free format, aren't the rules relaxed about 
column positioning, with a compiler ignoring preceding spaces in any one 
line ????

The real practical use I have seen for free format is reducing the 
amount of space taken up in a text book, where the author has the source 
as a table of two columns. (Yes of course using laser printers you can 
even get more than one page of source on a sheet - so one sheet of paper 
  can, front and back contain four lots of source. Trouble with that, 
unless your eyesight is very good - you can't read it easily).

A possible tip if you are using Net Express. There are many occasions 
where utilties, copyfiles can be used with more than one applicaion. My 
approach I put the 'originals' in an application 'copylib' - within 
individual projects I will then have say DateRoutines.cbl - within the 
current project there is a three-liner :-

*>------------ DateRoutines.cbl--------------
copy "\coplylib\DateRoutines.cbl".
*>--------------------------------------------

I have to compile the above within the current project - but it is at 
least referencing the original source which can also be used by other 
applicatons. If I have applications using common copyfiles, then you 
will see an entry in the appropriate source :-

copy "\copylib\dates2.cpy".

One immediate reaction from others here might be, the approach is 
half-assed - produce a copylib DLL - but I don't necessarily want a DLL 
covering ALL that is in the copylib - the current application may only 
use 10% of the \copylib.

Jimmy
```

#### ↳ Re: SOURCEFORMAT AND COPY LIBRARY

- **From:** apknight@gmail.com
- **Date:** 2005-03-07T16:29:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1110241774.016573.24150@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<95895e6d.0503070012.13599100@posting.google.com>`
- **References:** `<95895e6d.0503070012.13599100@posting.google.com>`

```

apknight wrote:
> sorry.  my english is very poor. so my text is not proof reading -_-a
>
…[45 more quoted lines elided]…
>          01 data pic x(10) <-?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
