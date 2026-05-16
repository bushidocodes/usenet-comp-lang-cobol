[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sorting Tables with sort-merge ??

_10 messages · 9 participants · 2001-02_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### Sorting Tables with sort-merge ??

- **From:** "R.Freitag" <r.freitag@netcologne.de>
- **Date:** 2001-02-11T16:11:28+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A86ABA0.20923005@netcologne.de>`

```
Hi,

it is possible to sort files with the
sort-merge-modul.
Can this be used to sort tables ?

Thx

RFr
```

#### ↳ Re: Sorting Tables with sort-merge ??

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-11T10:11:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<966dhc$7at$1@slb3.atl.mindspring.net>`
- **References:** `<3A86ABA0.20923005@netcologne.de>`

```
The ability to SORT a table is in the draft of the next Standard - but is
not currently ANSI/ISO conforming.  Micro Focus (MERANT) has had this
capability for several years - I do not know which other vendors already
support it as an extension.

Which compiler are you using?
```

##### ↳ ↳ Re: Sorting Tables with sort-merge ??

- **From:** "R.Freitag" <r.freitag@netcologne.de>
- **Date:** 2001-02-11T18:45:17+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A86CFAD.658F6E0@netcologne.de>`
- **References:** `<3A86ABA0.20923005@netcologne.de> <966dhc$7at$1@slb3.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> The ability to SORT a table is in the draft of the next Standard - but is
…[4 more quoted lines elided]…
> Which compiler are you using?

I use the Fujutsu student version ( Sams
Book's CD)


> 
> --
> Bill Klein
>  wmklein <at> ix.netcom.com
>
```

#### ↳ Re: Sorting Tables with sort-merge ??

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-02-11T16:29:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-kCgz1g6WYLEt@tcpserver>`
- **References:** `<3A86ABA0.20923005@netcologne.de>`

```
On Sun, 11 Feb 2001 15:11:28, "R.Freitag" <r.freitag@netcologne.de> 
wrote:

> Hi,
> 
…[3 more quoted lines elided]…
> 

Yes, this is possible with compilers that support it
```

#### ↳ Re: Sorting Tables with sort-merge ??

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-02-11T19:14:14+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cvhd8tsq7ndd1opj5igm5mueqmihdrpcge@4ax.com>`
- **References:** `<3A86ABA0.20923005@netcologne.de>`

```
On Sun, 11 Feb 2001 16:11:28 +0100 "R.Freitag" <r.freitag@netcologne.de>
wrote:

:>it is possible to sort files with the
:>sort-merge-modul.
:>Can this be used to sort tables ?

Certainly.

Use an INPUT and OUTPUT procedure.
```

##### ↳ ↳ Re: Sorting Tables with sort-merge ??

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-02-11T23:05:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9VEh6.6481$vd7.860016@dfiatx1-snr1.gtei.net>`
- **References:** `<3A86ABA0.20923005@netcologne.de> <cvhd8tsq7ndd1opj5igm5mueqmihdrpcge@4ax.com>`

```
Thanks. For as long as I've been writing, using the SORT verb to sort tables
that way (with INPUT/OUTPUT procedures) never occured to me. (Duh).

Kinda easier than writing your own bubble/insertion/shell/quick sort every
time, isn't it?
```

##### ↳ ↳ Re: Sorting Tables with sort-merge ??

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-12T07:29:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A87F352.4370127A@brazee.net>`
- **References:** `<3A86ABA0.20923005@netcologne.de> <cvhd8tsq7ndd1opj5igm5mueqmihdrpcge@4ax.com>`

```
I rarely have need to sort a table that can't be handled by an external sort
nor a standard CoBOL sort.

Real small tables can be accessed just as fast with a linear search than a
sorted search -  where "real small" means in one page of memory.

But last year I did have such an occasion and coded in a simple comb sort.
A simple perform worked.    If you want to code your own sort, look at comb
sort in the following web page.


http://www.etk.com/papers/sorting/sorting.htm#comparisons
```

###### ↳ ↳ ↳ Re: Sorting Tables with sort-merge ??

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2001-02-13T06:54:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A88DA0E.D0727BDF@worldnet.att.net>`
- **References:** `<3A86ABA0.20923005@netcologne.de> <cvhd8tsq7ndd1opj5igm5mueqmihdrpcge@4ax.com> <3A87F352.4370127A@brazee.net>`

```
Howard Brazee wrote:
> 
> I rarely have need to sort a table that can't be handled by an external sort
…[9 more quoted lines elided]…
> http://www.etk.com/papers/sorting/sorting.htm#comparisons

A couple of years ago we had a performance problem in a CICS
application, where a large table of time dependent values had to be
sorted before it could be redisplayed.  The nature of the application
was that the sequence of values changed frequently (but not the sort
key).  And since it was CICS, we could not use the SORT verb.  We used
the comb sort from the ETK web page, and we were very pleased with the
results.
```

###### ↳ ↳ ↳ Re: Sorting Tables with sort-merge ??

_(reply depth: 4)_

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-02-13T09:02:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g8p8bi0.pminews@news.wanadoo.es>`
- **References:** `<3A86ABA0.20923005@netcologne.de> <cvhd8tsq7ndd1opj5igm5mueqmihdrpcge@4ax.com> <3A87F352.4370127A@brazee.net> <3A88DA0E.D0727BDF@worldnet.att.net>`

```
On Tue, 13 Feb 2001 06:54:58 GMT, Arnold Trembley wrote:

>Howard Brazee wrote:
>> 
…[21 more quoted lines elided]…
>http://arnold.trembley.home.att.net/prog.htm

A few years ago I wrote an article in XEPHON VSE Update on the ose of tables
in COBOL. In that article I included both SHELL sort and QUICKSORT routines
implemented in COBOL. 
If anyone is interested, you can find it at

http://www.bimoyle.com/biminfo/june_97.pdf
Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

#### ↳ Re: Sorting Tables with sort-merge ??

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-02-12T21:46:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hcig8toiq6qtnft6o80lhcr4nqg61c5ak7@4ax.com>`
- **References:** `<3A86ABA0.20923005@netcologne.de>`

```
On Sun, 11 Feb 2001 16:11:28 +0100, "R.Freitag" <r.freitag@netcologne.de> wrote:

>Hi,
>
…[6 more quoted lines elided]…
>RFr

Sure,

and your compiler doesn't even have to know the new syntax of sorting tables.  Try
something like

SORT Sortfile INPUT PROCEDURE read-table OUTPUT PROCEDURE write-table

Read-Table.

    PERFORM VARYING Row-number FROM 1 BY 1 UNTIL Row-number > Max-rows
       RELEASE Myrow(row-number)
    END-PERFORM
    .

Write-table
    MOVE 0 TO Row-number
    PERFORM UNTIL End-of-table
       RETURN Sort-file
          AT END
             Set End-of-table TO TRUE
          NOT AT END
             ADD 1 TO Row-number 
             MOVE Sort-rec TO Myrow(row-number
       END-RETURN
    END-PERFORM
    .




     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         What does CICS mean? - Crash IBM Computer Swiftly
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
