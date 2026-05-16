[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM OS390/MVS CICS COBOL - ISCICS

_10 messages · 9 participants · 1999-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM OS390/MVS CICS COBOL - ISCICS

- **From:** Andre de Jager <ajager@mweb.co.za>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3821D99B.823A3071@mweb.co.za>`

```
In the 'C' environment there is a function to check if you are running under CICS or not
    i = iscics()
that will return 1 if you are running under cics and zero if you are not.

Unfortunately calling 'C' from Cobol has become very hazardous under LE370.

Has any one got an easy way to enquire if you are being called from a main program under 'CICS'
environment or under BATCH environment.

Assembler or COBOL or LE utility will do very nicely.

Thanks
```

#### ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

- **From:** TINLC <agent01413@deja.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7mYiOMtqezl+f8SInZ5sDSvFqvNR@4ax.com>`
- **References:** `<3821D99B.823A3071@mweb.co.za>`

```
On Thu, 04 Nov 1999 21:08:12 +0200, Andre de Jager <ajager@mweb.co.za>
sacrificed an address to the spam gods to say:

>In the 'C' environment there is a function to check if you are running under CICS or not
>    i = iscics()
…[9 more quoted lines elided]…
>Thanks

I've always issued an ASSIGN APPLID or SYSID query to determine which
CICS region I'm executing in, if any.  These are installation defined
values, so you'll need to experiment during testing to see what comes
back in each case, or ask your domain engineer.  In the case of a CICS
environment, APPLID will contain the 8 character region ID (so what
you'll get back during unit testing will vary from acceptence testing
will vary from production).  I dont remember what came back under
batch, but I remember that it was readily capable of differentiation
```

##### ↳ ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<382293CB.E7BE3170@att.net>`
- **References:** `<3821D99B.823A3071@mweb.co.za> <7mYiOMtqezl+f8SInZ5sDSvFqvNR@4ax.com>`

```
TINLC wrote:
> 
(snip)
> >Has any one got an easy way to enquire if you are being called from a main program under 'CICS'
> >environment or under BATCH environment.
…[12 more quoted lines elided]…
> batch, but I remember that it was readily capable of differentiation

I wouldn't expect anything to come back if you invoke a CICS program
with an EXEC statement; rather, I'd expect it to blow up (S0C4).

Bill Lynch
```

#### ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3823e4b3.177440606@news2.ibm.net>`
- **References:** `<3821D99B.823A3071@mweb.co.za>`

```
On Thu, 04 Nov 1999 21:08:12 +0200, Andre de Jager <ajager@mweb.co.za> wrote:

>In the 'C' environment there is a function to check if you are running under CICS or not
>    i = iscics()
…[9 more quoted lines elided]…
>Thanks


Code a little assembler (sub)program which does

	DFHAFCD TYPE=LOCATE,CB=CSA,REG=(5)

	
This will return the address of the CSA if you are running under CICS, or it will return
0.  Thus you can set the programs return code accordingly.



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         Better to understand a little than to misunderstand a lot.
```

#### ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7vuqgp$nj1$1@nnrp1.deja.com>`
- **References:** `<3821D99B.823A3071@mweb.co.za>`

```
In article <3821D99B.823A3071@mweb.co.za>,
  Andre de Jager <ajager@mweb.co.za> wrote:
> In the 'C' environment there is a function to check if you are running
under CICS or not
>     i = iscics()
> that will return 1 if you are running under cics and zero if you are
not.
>
> Unfortunately calling 'C' from Cobol has become very hazardous under
LE370.
>

Oh no, you must do anything wrong. I have absolutly no problems with ILC
under LE. Could you specify the kind of 'hazard' you experience?

> Has any one got an easy way to enquire if you are being called from a
main program under 'CICS'
> environment or under BATCH environment.
>
> Assembler or COBOL or LE utility will do very nicely.

In ASSEMBLER, I would use the CSVQUERY SEARCH=JPA macro with INEPNAME
pointed to 'DFHSIP'. I use the following table:

DC CL8'DFSRRC00',F'0'    IMS MPP, BMP, BATCH, BTS
DC CL8'DFHSIP  ',F'8'    CICS
DC CL8'IKJEFT01',F'4'    TSO NORMAL
DC CL8'IKJEFT25',F'4'    TSO ALIAS OF IKJEFT01
DC CL8'TSOSESS ',F'4'    TSO-PLUS
DC CL8'********',F'16'   END OF LIST

CSVQUERY returns 0 in R15 if the named program is loaded in the current
address space.

There is also a COBOL program originally written by Roland Schiradin and
Gilbert Saint-flour. The essential few lines are:

   Linkage Section.
   01 cb1.
       05 ptr1 Pointer Occurs 256.
   Procedure Division.
 *    PSA
       SET Address of cb1 to null
 *    TCB
       SET Address of cb1 to ptr1(136)
 *    EXT2
       SET Address Of cb1 To ptr1(53)
       if ptr1(6) = NULL
           display 'BATCH'
       else
           display 'CICS '
       end-if

Daniel
------------------------------------------------------------
visit us at:
http://www.winterthur.com


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3823FA06.D0F57C5A@melbpc.org.au>`
- **References:** `<3821D99B.823A3071@mweb.co.za> <7vuqgp$nj1$1@nnrp1.deja.com>`

```
I was researching this a while back. The book says under CICS you
can't call C from COBOL. You have to do EXEC CICS LINK. This is a
catch 22 if you are trying to find out if you are running under
CICS.

As usual on the mainframe, 'write a little assembler routine',

Tim Josling


Daniel Jacot wrote:
> Oh no, you must do anything wrong. I have absolutly no problems with ILC
> under LE. Could you specify the kind of 'hazard' you experience?
```

###### ↳ ↳ ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3825BD97.2DCEDA78@techie.com>`
- **References:** `<3821D99B.823A3071@mweb.co.za> <7vuqgp$nj1$1@nnrp1.deja.com> <3823FA06.D0F57C5A@melbpc.org.au>`

```
Things changed.  Read up on the latest and greatest stuff and I
believe it can be done.  Sorry I can't recall the exact release
levels off the top of my head.  I was browsing the new books one
day and this caught my eye because I had learned that you couldn't
do it either.

Tim Josling wrote:
> 
> I was researching this a while back. The book says under CICS you
…[10 more quoted lines elided]…
> > under LE. Could you specify the kind of 'hazard' you experience?
```

###### ↳ ↳ ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<804ilv$30i$1@nntp4.atl.mindspring.net>`
- **References:** `<3821D99B.823A3071@mweb.co.za> <7vuqgp$nj1$1@nnrp1.deja.com> <3823FA06.D0F57C5A@melbpc.org.au> <3825BD97.2DCEDA78@techie.com>`

```
For the current (most recent) documentation on what is and is not supported
for ILC under LE under CICS - see

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/CEEA406/14%2e1%2e1

Which points to:
  "14.1.1 OS/390 C/C++ and COBOL"

Under
  "14.1 Language Pairs Supported in ILC under CICS"

In:
    Title: OS/390 V2R7.0 Lang Env Writing ILC Application
    Document Number: SC28-1943-06
```

###### ↳ ↳ ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

_(reply depth: 4)_

- **From:** stephen_j_spiro@my-deja.com
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8053e0$tc1$1@nnrp1.deja.com>`
- **References:** `<3821D99B.823A3071@mweb.co.za> <7vuqgp$nj1$1@nnrp1.deja.com> <3823FA06.D0F57C5A@melbpc.org.au> <3825BD97.2DCEDA78@techie.com>`

```
If you are writing a subroutine which can be
called from either batch or on-line programs, AND
IT MAKES A DIFFERENCE, you should set a flag  to
indicate the environment.  Yeah, I know you can
get deep enough into the calls not to have this
information, but this is usually handled by
designing the system before coding it.

Stephen J Spiro
President, Wizard Systems
Member, J4 COBOL Committee
stephenjspiro@hotmail.com



In article <3825BD97.2DCEDA78@techie.com>,
  jared@techie.com wrote:
> Things changed.  Read up on the latest and
greatest stuff and I
> believe it can be done.  Sorry I can't recall
the exact release
> levels off the top of my head.  I was browsing
the new books one
> day and this caught my eye because I had
learned that you couldn't
> do it either.
>
> Tim Josling wrote:
> >
> > I was researching this a while back. The book
says under CICS you
> > can't call C from COBOL. You have to do EXEC
CICS LINK. This is a
> > catch 22 if you are trying to find out if you
are running under
> > CICS.
> >
> > As usual on the mainframe, 'write a little
assembler routine',
> >
> > Tim Josling
> >
> > Daniel Jacot wrote:
> > > Oh no, you must do anything wrong. I have
absolutly no problems with ILC
> > > under LE. Could you specify the kind
of 'hazard' you experience?
>
> --
…[4 more quoted lines elided]…
>



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: IBM OS390/MVS CICS COBOL - ISCICS

_(reply depth: 4)_

- **From:** Andre de Jager <ajager@mweb.co.za>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<38273C9E.136F2C2A@mweb.co.za>`
- **References:** `<3821D99B.823A3071@mweb.co.za> <7vuqgp$nj1$1@nnrp1.deja.com> <3823FA06.D0F57C5A@melbpc.org.au> <3825BD97.2DCEDA78@techie.com>`

```
The Hazards are
In Os390 Release 2.7 a small bug
    Cobol Pgm A Calls C Pgm 1 and returns
    Cobol Pgm A Calls Cobol Pgm B
        Cobol Pgm B Calls C Pgm 2 and returns, Pgm B Returns to A
     Cobol Pgm A Calls C Pgm 1 again.

Unfortunately program 2 has stomped all over program 1's static variables and crunch. Finally got a
fix from IBM.

Under Os390 1.2 watch out for static variables in 'C'.

In fact as soon as you try to implement a black box solution in 'C' you start to get problems from
one release of OS390 to another.

And Yes I have also seen the documentation that says you cannot call 'C' from Cobol although I
believe this does not apply to LeC.

Andre de Jager
Cape Town

Jared Thomas wrote:

> Things changed.  Read up on the latest and greatest stuff and I
> believe it can be done.  Sorry I can't recall the exact release
…[23 more quoted lines elided]…
> http://www.radiks.net/~jmthomas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
