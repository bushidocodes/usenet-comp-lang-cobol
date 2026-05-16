[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Information about direct cobol abort codes

_6 messages · 5 participants · 2006-12_

---

### Information about direct cobol abort codes

- **From:** "E-mailID:" <ajai.47@gmail.com>
- **Date:** 2006-12-11T22:31:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com>`

```
hi

i need to use direct abort codes in cobol for aborting my job..
i.e if i have soem fields with non-numeric values then i need to set an
abort code and stop the pgm there itself and return the abort codes..
this should not be done with SOC7 or return codes..
i heard that there are direct abort codes in cobol through which one
can implement this..
if anyone knows about this pls help me..
```

#### ↳ Re: Information about direct cobol abort codes

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-12T10:01:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ellumm$fq$1@reader2.panix.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com>`

```
In article <1165905109.388489.104690@n67g2000cwd.googlegroups.com>,
E-mailID: <ajai.47@gmail.com> wrote:
>hi
>
>i need to use direct abort codes in cobol for aborting my job..

Please do your own homework.

DD
```

##### ↳ ↳ Re: Information about direct cobol abort codes

- **From:** "Kevin M" <kmills44@bellsouth.net>
- **Date:** 2006-12-16T17:01:47-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<X%Zgh.104$2Y2.99@newsfe03.lga>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com> <ellumm$fq$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:ellumm$fq$1@reader2.panix.com...
> In article <1165905109.388489.104690@n67g2000cwd.googlegroups.com>,
> E-mailID: <ajai.47@gmail.com> wrote:
…[6 more quoted lines elided]…
> DD

In other words, DD has no frigging clue!
```

###### ↳ ↳ ↳ Re: Information about direct cobol abort codes

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-17T00:26:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<em22rd$h68$1@reader2.panix.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com> <ellumm$fq$1@reader2.panix.com> <X%Zgh.104$2Y2.99@newsfe03.lga>`

```
In article <X%Zgh.104$2Y2.99@newsfe03.lga>,
Kevin M <kmills44@bellsouth.net> wrote:
>
><docdwarf@panix.com> wrote in message news:ellumm$fq$1@reader2.panix.com...
…[8 more quoted lines elided]…
>In other words, DD has no frigging clue! 

I think I have enough of a clue as to what constitutes homework, aye.

DD
```

#### ↳ Re: Information about direct cobol abort codes

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-12T15:00:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<duzfh.450289$kz6.292512@fe08.news.easynews.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com>`

```
You don't tell us compiler or operating system, but from the mention of "S0C7", 
I am *guessing* it is IBM mainframe (probably z/OS).  Check out the LE callable 
services described at:

  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3170/2.2.5.1
    and
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/CEEA3170/2.2.5.2

This (of course) assumes that YOU are testing for numeric fields and don't let 
the system find them for you.
```

#### ↳ Re: Information about direct cobol abort codes

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-12T09:04:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0iktn2d29ddg9qq5h7rbbhv219dd4hvvrq@4ax.com>`
- **References:** `<1165905109.388489.104690@n67g2000cwd.googlegroups.com>`

```
On 11 Dec 2006 22:31:49 -0800, "E-mailID:" <ajai.47@gmail.com> wrote:

>i need to use direct abort codes in cobol for aborting my job..
>i.e if i have soem fields with non-numeric values then i need to set an
…[4 more quoted lines elided]…
>if anyone knows about this pls help me..

First, why not exit cleanly with a chosen return code that your JCL
can evaluate?

Look up 'CEE3ABC'.

05  MY-ABORT            PIC X(08)  VALUE 'CEE3ABC'.    
 -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 3 Line(s) 
05  MY-ERROR            PIC S9(9)    BINARY VALUE 24.  
05  CLEAN-UP            PIC S9(9)    BINARY VALUE 1.   
 -  -  -  -  -  -  -  -  -  -  -  -  -  - 3341 Line(s) 
CALL MY-ABORT      USING MY-ERROR, CLEAN-UP.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
