[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Passing EXTERNAL Data to AMODE(24) Assembler Sub-Program

_6 messages · 5 participants · 2003-08_

---

### Passing EXTERNAL Data to AMODE(24) Assembler Sub-Program

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2003-08-13T10:15:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhdgo2$dnv$1@slb4.atl.mindspring.net>`

```
Greetings,

        I have a COBOL/Batch "Main" program, compiled with DATA(31) and
linked as AMODE(31) RMODE(ANY) and have defined a WS "01" area as EXTERNAL,
which from what I gather, is allocated BELOW THE LINE.

        With this in mind, I need to Dynamically CALL an ASSEMBLER
sub-program, which was linked as AMODE(24) and RMODE(24) and must remain as
such, passing the 24-bit EXTERNAL data as a parameter.

        However, when the PARMLIST is created by the compiler as an
"intermediate field" in the "Main" program prior to the actual CALL(BALR),
the address of the EXTERNAL data is stored into the PARMLIST field (which is
fine) and then R1 is loaded with the address of the PARMLIST, which is above
the line (and is the problem), causing the ASSEMBLER sub-program to choke
when it attempts to establish parameter addressability using R1.

        Does anyone have a resolution or any thought on this, other than
monkeying around with the addressing-mode of the sub-program (BASSM, BSM,
GETMAIN, etc) to attain R1 addressability?

Thanks,

Bill
```

#### ↳ Re: Passing EXTERNAL Data to AMODE(24) Assembler Sub-Program

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-08-13T15:14:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f3a5160.28205062@news.central.cox.net>`
- **References:** `<bhdgo2$dnv$1@slb4.atl.mindspring.net>`

```
"WOB" <wobconsult@sprynet.com> wrote:

>        I have a COBOL/Batch "Main" program, compiled with DATA(31) and
>linked as AMODE(31) RMODE(ANY) and have defined a WS "01" area as EXTERNAL,
…[15 more quoted lines elided]…
>GETMAIN, etc) to attain R1 addressability?

Put a 31-bit wrapper around it. Do a STORAGE OBTAIN,LENGTH=(?),LOC=BELOW and
copy the parmlist below the line.

Sample code:
http://www.urz.uni-heidelberg.de/ADSM/ibmdoc.tsm52/mvs/html/guide/anrmgd51198.htm
```

#### ↳ "Must remain as such" - why?

- **From:** Colin Campbell <cmcampb@attgloabl.net>
- **Date:** 2003-08-13T11:10:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F3A7F30.336A52DE@attgloabl.net>`
- **References:** `<bhdgo2$dnv$1@slb4.atl.mindspring.net>`

```
Why "must" your Assmebler routine remain 24-bit?  Your COBOL routine didn't
"have to" remain 24-bit.  Any program would be able to call a 31-bit Assembler
routine, whether the caller is 24-bit or 31-bit.  So, 31-bit code is the "lowest
common denominator".  It's time to upgrade the Assembler rather than trying to
work around it.

WOB wrote:

> Greetings,
>
…[21 more quoted lines elided]…
> Bill
```

##### ↳ ↳ Re: "Must remain as such" - why?

- **From:** wobconsult@sprynet.com (WOB Consulting)
- **Date:** 2003-08-13T18:58:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<173f80ae.0308131758.6025c60f@posting.google.com>`
- **References:** `<bhdgo2$dnv$1@slb4.atl.mindspring.net> <3F3A7F30.336A52DE@attgloabl.net>`

```
Colin Campbell <cmcampb@attgloabl.net> wrote in message news:<3F3A7F30.336A52DE@attgloabl.net>...
> Why "must" your Assmebler routine remain 24-bit?  Your COBOL routine didn't
> "have to" remain 24-bit.  Any program would be able to call a 31-bit Assembler
> routine, whether the caller is 24-bit or 31-bit.  So, 31-bit code is the "lowest
> common denominator".  It's time to upgrade the Assembler rather than trying to
> work around it.

Unfortunately, it's a proprietary sub-program that reads a sequential
file and subsequently, addresses a DCB. The vendor has been real slow
in making the appropriate changes for 31-bit. Hence, my hands are
tied.

<Rest Snipped>
```

#### ↳ Re: Passing EXTERNAL Data to AMODE(24) Assembler Sub-Program

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-13T19:30:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<plw_a.17581$vo2.9431@newsread1.news.atl.earthlink.net>`
- **References:** `<bhdgo2$dnv$1@slb4.atl.mindspring.net>`

```
The detailed (and somewhat complex) rules on when EXTERNAL data is above the
line and when it is below is discussed at:


http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/1.2.6.4

There was BUG in some earlier release of COBOL or LE that always caused
EXTERNAL data to be below the line.  I can't remember when this was "fixed"
but it is implied in the information at:

    http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igymg202/1.2.4
```

#### ↳ Re: Passing EXTERNAL Data to AMODE(24) Assembler Sub-Program

- **From:** "Don Higgins" <don.higgins@microfocus.com>
- **Date:** 2003-08-14T05:28:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhfl0q$4v0$1@hyperion.microfocus.com>`
- **References:** `<bhdgo2$dnv$1@slb4.atl.mindspring.net>`

```
You can add the Micro Focus COBOL directive:
DATA(24) to the calling COBOL program which will force the data division to
be placed below the 16 MB line so the data can be passed to other 24 bit
application programs.

Don Higgins
don.higgins@microfocus.com

"WOB" <wobconsult@sprynet.com> wrote in message
news:bhdgo2$dnv$1@slb4.atl.mindspring.net...
> Greetings,
>
>         I have a COBOL/Batch "Main" program, compiled with DATA(31) and
> linked as AMODE(31) RMODE(ANY) and have defined a WS "01" area as
EXTERNAL,
> which from what I gather, is allocated BELOW THE LINE.
>
>         With this in mind, I need to Dynamically CALL an ASSEMBLER
> sub-program, which was linked as AMODE(24) and RMODE(24) and must remain
as
> such, passing the 24-bit EXTERNAL data as a parameter.
>
>         However, when the PARMLIST is created by the compiler as an
> "intermediate field" in the "Main" program prior to the actual CALL(BALR),
> the address of the EXTERNAL data is stored into the PARMLIST field (which
is
> fine) and then R1 is loaded with the address of the PARMLIST, which is
above
> the line (and is the problem), causing the ASSEMBLER sub-program to choke
> when it attempts to establish parameter addressability using R1.
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
