[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sort record

_15 messages · 11 participants · 1999-02 → 1999-03_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Sort record

- **From:** jlmeyer@rmi.net (John Meyer)
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36d4deea.8592302@news.rmi.net>`

```
	Hi, I have a sort file taking input from a file and giving
output to a procedure.  Where do I put the sort description for the
sort file?  (Note:  the file only exists in memory).
```

#### ↳ Re: Sort record

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b3941$bnc@sjx-ixn10.ix.netcom.com>`
- **References:** `<36d4deea.8592302@news.rmi.net>`

```
Probably "homework" but I'll give the answer any way; it is under the SD.
```

##### ↳ ↳ Re: Sort record

- **From:** john_meyer@my-dejanews.com
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b4ktp$pe0$1@nnrp1.dejanews.com>`
- **References:** `<36d4deea.8592302@news.rmi.net> <7b3941$bnc@sjx-ixn10.ix.netcom.com>`

```
In article <7b3941$bnc@sjx-ixn10.ix.netcom.com>,
  "William M. Klein" <wmklein@inospam.netcom.com> wrote:
> Probably "homework" but I'll give the answer any way; it is under the SD.


It is, and I'll get you the code I've done so far, but then I have to select
the sort-file and assign it to something, and it's a file in memory (the file
is destroyed after the program files).

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: Sort record

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b4pk6$m2b@dfw-ixnews7.ix.netcom.com>`
- **References:** `<36d4deea.8592302@news.rmi.net> <7b3941$bnc@sjx-ixn10.ix.netcom.com> <7b4ktp$pe0$1@nnrp1.dejanews.com>`

```
Yes, you do need a SELECT/ASSIGN statement for your SD.
  NO, the chances are whatever you put in the ASSIGN statement *will* not be
used by the compiler

If you are using Fujitsu COBOL (and no other compiler), you need to make
certain you use the filename format of the Assign and not the "literal"
format.

Show the whole NG what you have, and we should be able to help you.
```

###### ↳ ↳ ↳ Re: Sort record

_(reply depth: 4)_

- **From:** john_meyer@geocities.com
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b9ai5$ml9$1@nnrp1.dejanews.com>`
- **References:** `<36d4deea.8592302@news.rmi.net> <7b3941$bnc@sjx-ixn10.ix.netcom.com> <7b4ktp$pe0$1@nnrp1.dejanews.com> <7b4pk6$m2b@dfw-ixnews7.ix.netcom.com>`

```
In article <7b4pk6$m2b@dfw-ixnews7.ix.netcom.com>,
  "William M. Klein" <wmklein@inospam.netcom.com> wrote:
> Yes, you do need a SELECT/ASSIGN statement for your SD.
>   NO, the chances are whatever you put in the ASSIGN statement *will* not be
…[4 more quoted lines elided]…
> format.


Forget it.  I found out the answer on my own.  Thanks for the help.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Sort record

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D55C1D.D03D6750@ASPMnetdoor.com>`
- **References:** `<36d4deea.8592302@news.rmi.net>`

```
Put your SD(s) (Sort Description) after your FD's.  Good luck on your
next exam.

John Meyer wrote:

>         Hi, I have a sort file taking input from a file and giving
> output to a procedure.  Where do I put the sort description for the
> sort file?  (Note:  the file only exists in memory).
```

##### ↳ ↳ Re: Sort record

- **From:** john_meyer@geocities.com
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b4krb$p6e$1@nnrp1.dejanews.com>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com>`

```
In article <36D55C1D.D03D6750@ASPMnetdoor.com>,
  Warren Porter <warrenp@ASPMnetdoor.com> wrote:
> Put your SD(s) (Sort Description) after your FD's.  Good luck on your
> next exam.

I tried that, but it chokes on the code.  Essentially telling me operation
SORT-FILE is undefined.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: Sort record

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N7oB2.320$bk.136225@storm.twcol.com>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com> <7b4krb$p6e$1@nnrp1.dejanews.com>`

```
>> Put your SD(s) (Sort Description) after your FD's.  Good luck on your
>> next exam.
>
>I tried that, but it chokes on the code.  Essentially telling me operation
>SORT-FILE is undefined.


Some versions of COBOL allow for dynamic allocation of temporary files.
Check the DYNAM compiler option. Assuming you are working under MVS, you may
need to define a temporary DSN in the JCL associated with the sort file
DDNAME for the NODYNAM compiler option:

//SORTFILE DD DSN=&&SORTFILE,DISP=(NEW,DELETE,DELETE)

Your SD should look something like:

       SD  SORT-FILE.
       01  SORT-FILE-RECORD.
           05 SORT-KEY ........
```

###### ↳ ↳ ↳ Re: Sort record

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b777c$35h@dfw-ixnews11.ix.netcom.com>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com> <7b4krb$p6e$1@nnrp1.dejanews.com> <N7oB2.320$bk.136225@storm.twcol.com>`

```
Just to "correct" something in the attached note (or at least as I read it).
If you are talking MVS (or OS/390), the DYNAM compiler option has absolutely
NOTHING to do with "dynamic file allocation".  There may be some compiler
somewhere where this is true, but certainly not from IBM.

FYI,
  The file specified in the ASSIGN clause for an SD (for most but NOT ALL
compilers) has little or nothing to do with where you physical "sort work"
files are allocated.  There is nothing in the Standard that says that these
shouldn't be related, but neither is there anything that says they should.
Therefore, (as I have stated in other posts) most compilers basically just
ignore the information in the Select/Assign clause for an SD.

Out of curiosity, does anyone know a compiler that DOES pay attention to the
Select/Assign clause for an SD?  I am certain that there are some, so I am
genuinely interested in hearing the answer.
```

###### ↳ ↳ ↳ Re: Sort record

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-02-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D936A5.1417E8C3@zip.com.au>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com> <7b4krb$p6e$1@nnrp1.dejanews.com> <N7oB2.320$bk.136225@storm.twcol.com> <7b777c$35h@dfw-ixnews11.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Just to "correct" something in the attached note (or at least as I read it).
…[3 more quoted lines elided]…
> 

There is a parameter that says this in the compiler set up.  I cannot
remember the name but it does exist.  I had a problem with an empty
dataset after Fujitsu to MVS conversion, the DDname was supposed to be
XYZO1 (XYZ output 1) instead it was defined as XYZ01 (XYZ zero 1). 
After some hunting we found the parameter and turned it off and a lot of
interesting features appeared in our conversion.  I prefer it to be OFF
for this reason, I consider dynamic allocation a bad thing for everyone.

I never use internal sort so I cannot say that flipping the flag will or
will not affect it.

Happy hunting
Ken
```

###### ↳ ↳ ↳ Re: Sort record

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7bcfcv$t08@sjx-ixn6.ix.netcom.com>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com> <7b4krb$p6e$1@nnrp1.dejanews.com> <N7oB2.320$bk.136225@storm.twcol.com> <7b777c$35h@dfw-ixnews11.ix.netcom.com> <36D936A5.1417E8C3@zip.com.au>`

```
The option is NOT a compiler option but is the LE
   CBLQDA
run-time option.   If you take what USED to be the LE default, it would
create a file - that would not get cataloged and would disappear at the end
of the job step.

With the latest release of LE (OS/390 2.6), the default has now been changed
to the not-ANSI conforming but what most MVSers want of
  NOCBLQDA

Note:  IBM compilers on VM, OS/2, and NT (I am not certain about OS/400) all
create "usable" files in conformance with the ANSI/ISO Standard - and you
can use them without any difficulty.  It is only OS/390 and MVS where IBM
implemented this in an unusable manner.
```

###### ↳ ↳ ↳ Re: Sort record

_(reply depth: 5)_

- **From:** WDS.WDS@WDS.WDS (WDS)
- **Date:** 1999-03-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36dde23a.13515834@news1.frb.gov>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com> <7b4krb$p6e$1@nnrp1.dejanews.com> <N7oB2.320$bk.136225@storm.twcol.com> <7b777c$35h@dfw-ixnews11.ix.netcom.com>`

```
On Fri, 26 Feb 1999 14:26:09 -0800, "William M. Klein" wrote:

[snippage]

>Out of curiosity, does anyone know a compiler that DOES pay attention to the
>Select/Assign clause for an SD?  I am certain that there are some, so I am
>genuinely interested in hearing the answer.
>

I know most of this thread has been IBM MVS-oriented, but some other
compilers do (did) use some of the SELECT/ASSIGN information for an SD
(other than the file name in the SELECT statement, which I would
think, all must use).

Unisys V-Series COBOL compilers, both 68 and 74, use the ASSIGN
information to determine what media (disk, diskpack, tape) will hold
the sort work file.

I seem to remember that at least one of the compilers (68 or 74) on
the DECSystem 20 used at least some of this information, but I do not
remember which information or for what; it has been quite a while
since I have even seen a DECSystem 20.
```

###### ↳ ↳ ↳ Re: Sort record

_(reply depth: 4)_

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1999-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D761DF.72091F53@ix.netcom.com>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com> <7b4krb$p6e$1@nnrp1.dejanews.com> <N7oB2.320$bk.136225@storm.twcol.com>`

```
Under MVS, there is no need to define an //SORTFILE. The compiler requires the
SD's SELECT/ASSIGN clause only to satisfy syntax but never uses the the
assigned_name at all. All sorting occurs in the //SORTWKxx files as required.
Rather than define a slew of  //SORTWKxx's in your JCL, it would be better to
tell SORT to dynamically allocate  sort space as needed. This can be done with:
//$ORTPARM DD *     << syncsort
    OPTION DYNALLOC

//IGZSRTCD  DD * << dfsort
     OPTION DYNALLOC

These parameters are not related to the compiler DYNAM option.


Jeff wrote:

> >> Put your SD(s) (Sort Description) after your FD's.  Good luck on your
> >> next exam.
…[15 more quoted lines elided]…
>            05 SORT-KEY ........
```

###### ↳ ↳ ↳ Re: Sort record

_(reply depth: 5)_

- **From:** Frank Yaeger <fyaeger@ibm.net>
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36D8084D.93C7F2A8@ibm.net>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com> <7b4krb$p6e$1@nnrp1.dejanews.com> <N7oB2.320$bk.136225@storm.twcol.com> <36D761DF.72091F53@ix.netcom.com>`

```


John Trifon wrote:

> Rather than define a slew of  //SORTWKxx's in your JCL, it would be better to
> tell SORT to dynamically allocate  sort space as needed. This can be done with:
…[5 more quoted lines elided]…
>

 Actually, the DFSORT equivalent of Syncsort's //$ORTPARM DD would be:

 //DFSPARM DD *
    OPTION DYNALLOC
 /*

 Or you can even use //$ORTPARM if you set DFSORT's PARMDDN installation option
 to PARMDDN=$ORTPARM (the shipped default is PARMDDN=DFSPARM).

 However, OPTION DYNALLOC is not normally required since DFSORT will
 automatically use dynamically allocated work data sets by default if you don't
 have any JCL SORTWKs (set DFSORT's DYNAUTO=IGNWKDD installation option if you
 want DFSORT to use dynamically allocated work data sets INSTEAD of JCL SORTWKs).

Frank Yaeger - DFSORT Team (Specialties: Y2K, Symbols, ICETOOL, OUTFIL :-)
fyaeger@vnet.ibm.com
DFSORT/MVS is on the World Wide Web at URL:
     http://www.ibm.com/storage/dfsort/
```

###### ↳ ↳ ↳ Re: Sort record

_(reply depth: 6)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36d84660.895875@news1.ibm.net>`
- **References:** `<36d4deea.8592302@news.rmi.net> <36D55C1D.D03D6750@ASPMnetdoor.com> <7b4krb$p6e$1@nnrp1.dejanews.com> <N7oB2.320$bk.136225@storm.twcol.com> <36D761DF.72091F53@ix.netcom.com> <36D8084D.93C7F2A8@ibm.net>`

```
On Sat, 27 Feb 1999 06:59:25 -0800, Frank Yaeger <fyaeger@ibm.net>
wrote:

> However, OPTION DYNALLOC is not normally required since DFSORT will
> automatically use dynamically allocated work data sets by default if you don't
> have any JCL SORTWKs (set DFSORT's DYNAUTO=IGNWKDD installation option if you
> want DFSORT to use dynamically allocated work data sets INSTEAD of JCL SORTWKs).
>

And if you have a lot of memory in your machine DFsort uses that.  And
it's FAST.  I'm very impressed with DFSORT in it's present
incarnation.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
