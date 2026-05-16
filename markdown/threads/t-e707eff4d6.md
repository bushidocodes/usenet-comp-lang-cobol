[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# help Looking for some code to do a Bubble sort in Cobol/Fortran

_6 messages · 6 participants · 1999-03_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### help Looking for some code to do a Bubble sort in Cobol/Fortran

- **From:** "spacesspaces" <spacesspaces@email.msn.com>
- **Date:** 1999-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<eQ3QQm4d#GA.333@upnetnews02.moswest.msn.net>`

```
help       Looking for some code to do a "Bubble" sort in Cobol/Fortran


have a need to sort some internal tables, multikey.


thanks in advance
ed
.
.
.
Got Lotto ?
Brighton Computer Group
http://www.geocities.com/Eureka/Boardroom/7821/lgames.htm
.
.
```

#### ↳ Re: help Looking for some code to do a Bubble sort in Cobol/Fortran

- **From:** twymer@aol.com (Twymer)
- **Date:** 1999-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990326083844.23496.00000484@ng-ch1.aol.com>`
- **References:** `<eQ3QQm4d#GA.333@upnetnews02.moswest.msn.net>`

```
here is some pseudocode:

set table pointers to 1 and 2.
set the "switched" switch to no.
compare the first 2 keys.
Is the first key less than the second key?
If yes increment both pointers by 1
else
   move the second key into a temp area
   move the first key into the second key
   move the temp area into the first key
   set the "switched" to yes
   increment both pointers by 1
endif

If the second table pointer points to end of table,  and the "switched" switch
is Yes...reset the switch to No and set the table pointers to 1 and 2. 

keep reading the table until the second table pointer points to end of table
and the "switched" switch is no

Good luck.

TW
```

#### ↳ Re: help Looking for some code to do a Bubble sort in Cobol/Fortran

- **From:** "Jay Siegel" <ka2csh@nospam.nowhere>
- **Date:** 1999-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<Q1.D1.412IAo9yMtq4soqs4.NR@nospam.nowhere>`
- **References:** `<eQ3QQm4d#GA.333@upnetnews02.moswest.msn.net>`

```
"space" == "spacesspaces" writes:

space> help       Looking for some code to do a "Bubble" sort in
space> Cobol/Fortran
space> 
space> 
space> have a need to sort some internal tables, multikey.
space> 
space> 
space> thanks in advance
space> ed
space> .

    Bubble sort?  I'd recommend at least a Shell sort algorythm,
    while the Fast sort algorythm is even faster.  The Bubble sort
    algorythm is one of the slowest algorythms for sorting.

Jay
```

##### ↳ ↳ Re: help Looking for some code to do a Bubble sort in Cobol/Fortran

- **From:** jeff@jakfield.xu-netx.com (Jeff York)
- **Date:** 1999-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<36fbd570.64531942@news.u-net.com>`
- **References:** `<eQ3QQm4d#GA.333@upnetnews02.moswest.msn.net> <Q1.D1.412IAo9yMtq4soqs4.NR@nospam.nowhere>`

```
"Jay Siegel" <ka2csh@nospam.nowhere> wrote:

>"space" == "spacesspaces" writes:
>
…[14 more quoted lines elided]…
>
Except,  of course,  in the case where the data is already in
sequence..    I've seen sorts in the past where the first pass is a
bubble,  just to cope with that possibility..    :-)
```

##### ↳ ↳ Re: help Looking for some code to do a Bubble sort in Cobol/Fortran

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<36FF8FFC.FE03B90D@NOSPAMhome.com>`
- **References:** `<eQ3QQm4d#GA.333@upnetnews02.moswest.msn.net> <Q1.D1.412IAo9yMtq4soqs4.NR@nospam.nowhere>`

```
Jay Siegel wrote:
> 
> "space" == "spacesspaces" writes:
…[16 more quoted lines elided]…
> Jay

True.  But I am guessing about why a COBOL program needs to code a sort
at all.  I suspect it is for a very small amount of data, maybe to order
some data on a screen.  In that case, who cares which sort is faster. 
Just code which is easier (to maintain and avoid bugs).

Otherwise use a sort utility (external sort, COBOL sort, or SQL ordered
input).
```

#### ↳ Re: help Looking for some code to do a Bubble sort in Cobol/Fortran

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol,fj.comp.lang.cobol,fj.lang.cobol
- **Message-ID:** `<36FE2AD6.38C2C7D5@IMN.nl>`
- **References:** `<eQ3QQm4d#GA.333@upnetnews02.moswest.msn.net>`

```
spacesspaces wrote:

> help       Looking for some code to do a "Bubble" sort in Cobol/Fortran

Your not the only one. Some ather class with homework perhaps?
Look at the other answers given to you and to the other thread about
"Bubble sort" in c.l.c.
Then do your (home)work/job

The Frog
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
