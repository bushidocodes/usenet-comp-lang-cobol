[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Clearing Register 15

_11 messages · 8 participants · 2000-07_

---

### Clearing Register 15

- **From:** "Eileen Preston" <epreston@lear.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s96e031e.008@UTAEMAIL.UTA.COM>`

```
Maybe some of you can shed some light on this situation.

Environment:  Mainframe OS/390 with LE
Compiler:       Cobol OS/390 (or whatever the latest mainframe is)

If you are familiar with CICS and EXCI (or DPL calls) it would definately help.

For those not familiar this is a way for batch programs to call a CICS program to do I/O on vsam file owned by CICS and not have to close the files and allows data integrety.

This program takes in a sequential input file, does several calls to DB2 databases and formats a record which is then sent via DPL calls to a CICS program to update our shipper file.

All the calls, init_user, allocate_pipe, open_pipe are fine.  The updates work just fine, the close and deallocate work just fine.  I've put in a display of every response code and return code I can think of and everything is zero but the program ends with a return code of 12.

I've been told that IBM assembler code (which is what I'm calling with the DPL calls) are notorious for not clearing register 15 and that is what I'm seeing.  IBM of course says that my COBOL program isn't clearing register 15 and I'm saying 'huh?'.  

The very last thing I want to code into the program is MOVE +0 TO RETURN-CODE before I do my GOBACK as this is considered a really bad programming habit around here (we've been bit in the posterier many a time with old programs issuing comments via displays and then moving a +0 to the return-code, ending, and the job going on it's merry way with lousy data - the statements were yanked as fast as we could find them).

Let the debates begin!

Eileen


 Sent via Deja.com http://www.deja.com/
 Before you buy.
```

#### ↳ Re: Clearing Register 15

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8klh57$2lhon$1@ID-39920.news.cis.dfn.de>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM>`

```

Eileen Preston <epreston@lear.com> wrote in
message news:s96e031e.008@UTAEMAIL.UTA.COM...
> Maybe some of you can shed some light on this
situation.
>
> Environment:  Mainframe OS/390 with LE
> Compiler:       Cobol OS/390 (or whatever the
latest mainframe is)
>
> If you are familiar with CICS and EXCI (or DPL
calls) it would definately help.
>
> For those not familiar this is a way for batch
programs to call a CICS program to do I/O on vsam
file owned by CICS and not have to close the files
and allows data integrety.
>
> This program takes in a sequential input file,
does several calls to DB2 databases and formats a
record which is then sent via DPL calls to a CICS
program to update our shipper file.
>
> All the calls, init_user, allocate_pipe,
open_pipe are fine.  The updates work just fine,
the close and deallocate work just fine.  I've put
in a display of every response code and return
code I can think of and everything is zero but the
program ends with a return code of 12.
>
> I've been told that IBM assembler code (which is
what I'm calling with the DPL calls) are notorious
for not clearing register 15 and that is what I'm
seeing.  IBM of course says that my COBOL program
isn't clearing register 15 and I'm saying 'huh?'.
>

An easy way to find out is to display return-code
immediately after the call.

> The very last thing I want to code into the
program is MOVE +0 TO RETURN-CODE before I do my
GOBACK as this is considered a really bad
programming habit around here (we've been bit in
the posterier many a time with old programs
issuing comments via displays and then moving a +0
to the return-code, ending, and the job going on
it's merry way with lousy data - the statements
were yanked as fast as we could find them).
>
> Let the debates begin!
…[5 more quoted lines elided]…
>  Before you buy.
```

#### ↳ Re: Clearing Register 15

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396e492e.23231334@news.transport.com>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM>`

```
We took a slightly different approach here.
We stole an EXCI assembler subroutine from the web, and we perform our
EXCI calls via this subroutine so our application code is sheltered
from EXCI complications.

Heres the web site we stole the code from.  It also includes a sample
COBOL application program so you can see how to call it;
http://www.xephon.com/cgi-bin/xephon2/tdisplay?/c145a01.txt

It helped that I had a very good CICS and Assembler coder here to help
whip this code into shape for our shop.  Now calling CICS programs
from batch is a real SNAP!

Pete Wirfs





On Thu, 13 Jul 2000 17:57:31 -0400, "Eileen Preston"
<epreston@lear.com> wrote:

>Maybe some of you can shed some light on this situation.
>
…[21 more quoted lines elided]…
> Before you buy.
```

#### ↳ Re: Clearing Register 15

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8klm94$9i3$1@slb6.atl.mindspring.net>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM>`

```
Eileen,
  Tell who ever from IBM is telling you that it isn't THEIR fault to "RTFM" -
please see

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYPG204/4%2e10%2e3%2e1

which says (in part),

"Note that (with the exception listed below) DB2 passes the return code back
in the SQLCA, not in Register 15. Therefore, the COBOL RETURN-CODE special
register might contain an invalid value. Because a COBOL program stores its
RETURN-CODE special register into Register 15 before it returns to its
caller, your COBOL program should set the RETURN-CODE special register to a
meaningful value before returning to its caller. "

Note: DB2 is NOTORIOUS for this problem and anyone at IBM who doesn't know
about it, should check again.
```

##### ↳ ↳ Re: Clearing Register 15

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gC7d5.4385$h77.2477203@news2.mia>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM> <8klm94$9i3$1@slb6.atl.mindspring.net>`

```
I can tell you for a FACT that COBOL OS/390 does NOT automatically clear the
RETURN-CODE.  If you call a subroutine, upon return whatever is in R15 is
LEFT there.
Previous versions of IBMCOBOL did clear R15, but no more!

You will HAVE to 'MOVE ZERO TO RETURN-CODE'.

We had an assembler routine someelse wrote that returns the Job Number and a
couple
of other Job items to the caller.  The cleanup code was REALLY STUPID and
all of a sudden,
after 2 years on previous releases, on OS/390 it started giving us COND
CODE=7000
or COND CODE =3963 (not exact, but as close as I can remember).

I had to modify the caller to clear RETURN-CODE ASAP, until I had time to
determine
just why the assembler sub was whacking R15. (the sub was called by over a
dozen
programs in more than 200 jobs that ran at various times of the day!).

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8klm94$9i3$1@slb6.atl.mindspring.net...
> Eileen,
>   Tell who ever from IBM is telling you that it isn't THEIR fault to
"RTFM" -
> please see
>
>
http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYPG204/4%2e10%2e3%2e
1
>
> which says (in part),
>
> "Note that (with the exception listed below) DB2 passes the return code
back
> in the SQLCA, not in Register 15. Therefore, the COBOL RETURN-CODE special
> register might contain an invalid value. Because a COBOL program stores
its
> RETURN-CODE special register into Register 15 before it returns to its
> caller, your COBOL program should set the RETURN-CODE special register to
a
> meaningful value before returning to its caller. "
>
…[13 more quoted lines elided]…
> > If you are familiar with CICS and EXCI (or DPL calls) it would
definately
> help.
> >
> > For those not familiar this is a way for batch programs to call a CICS
> program to do I/O on vsam file owned by CICS and not have to close the
files
> and allows data integrety.
> >
…[4 more quoted lines elided]…
> > All the calls, init_user, allocate_pipe, open_pipe are fine.  The
updates
> work just fine, the close and deallocate work just fine.  I've put in a
> display of every response code and return code I can think of and
everything
> is zero but the program ends with a return code of 12.
> >
> > I've been told that IBM assembler code (which is what I'm calling with
the
> DPL calls) are notorious for not clearing register 15 and that is what I'm
> seeing.  IBM of course says that my COBOL program isn't clearing register
15
> and I'm saying 'huh?'.
> >
…[3 more quoted lines elided]…
> with old programs issuing comments via displays and then moving a +0 to
the
> return-code, ending, and the job going on it's merry way with lousy data -
> the statements were yanked as fast as we could find them).
…[9 more quoted lines elided]…
>
```

#### ↳ Re: Clearing Register 15

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m26ums86midi17vp1t999c21l7b5qqep0p@4ax.com>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM>`

```
On Thu, 13 Jul 2000 17:57:31 -0400, "Eileen Preston" <epreston@lear.com> wrote:

>If you are familiar with CICS and EXCI (or DPL calls) it would definately help.
<rest snipped>

Eileen,  
I do NOT believe that IBM clobbers R15 on a regular (or even irregular) basis. At least I
haven't seen in in my environment when playing around with EXCI. I would display the
return code after each and every CALL in the program to find out who really is the one
with the black hat.

Alternatively, you could set up a debugging section at the beginning of your program 

DECLARATIVES
Debuuging Section
      USE FOR DEBUGGING ON ALL PROCEDURES
      .
Bebug-para.
      DISPLAY RETURNCODE
      DISPLAY DEBUG-ITEM
      .
END DECLARATIVES



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      Hell is for children. - Pat Benatar
```

##### ↳ ↳ Re: Clearing Register 15

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39705813.2EE5E6A1@zip.com.au>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM> <m26ums86midi17vp1t999c21l7b5qqep0p@4ax.com>`

```
Volker Bandke wrote:

> I do NOT believe that IBM clobbers R15 on a regular (or even irregular) basis.
> At least I haven't seen in in my environment when playing around with EXCI. I
> would display the return code after each and every CALL in the program to find
> out who really is the one with the black hat.

Now this does not quite make sense to me.  R15 is THE place to return
a 'condition code' in MVS.  Why would any routine not routinely trash
it's contents with it's own values.

I was tripped up by a call to a clean up routine after I set
return-code,  could not figure out why it did not work until ages
afterwards.  I of course worked around it by using a work variable for
MY return value and moving this as the last thing before returning to
the caller (whatever this may be).  This would solve the original
problem as well at a small overhead.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

For fast secure document delivery on the Net
http://www.themailxchange.com.au/
```

###### ↳ ↳ ↳ Re: Clearing Register 15

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<18q0nsgkcfc4i8md6ei28butpojdofoeje@4ax.com>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM> <m26ums86midi17vp1t999c21l7b5qqep0p@4ax.com> <39705813.2EE5E6A1@zip.com.au>`

```
On Sat, 15 Jul 2000 22:24:51 +1000, Ken Foskey <waratah@zip.com.au> wrote:

>Volker Bandke wrote:
>
…[7 more quoted lines elided]…
>it's contents with it's own values.
The reason I suggested to check the RETURN-CODE variable was exactly that - Eileen
suspected that some CALLed routine did NOT set R15 to 0, even though the routine was
successfull.  NAd this was just to find out WHERE the R15 was (incorrectly) nor cleared.

She found out, in the meantime, that here EXCI calls returned with a R15 = 12, and is
investigating now WHY this is the case (here EXCI calls seem to work perfectly, though)


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      The solution to a problem changes the nature of the problem.
```

###### ↳ ↳ ↳ Re: Clearing Register 15

_(reply depth: 4)_

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4F7d5.4387$h77.2477325@news2.mia>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM> <m26ums86midi17vp1t999c21l7b5qqep0p@4ax.com> <39705813.2EE5E6A1@zip.com.au> <18q0nsgkcfc4i8md6ei28butpojdofoeje@4ax.com>`

```
I've written and test an EXCI / DPL server and I can state for the record,
that a correctly
installed DPL config AND an UNMODIFIED DFHEXCI module clears R15.
I tested more than 50 functions and my COND CODE was always correct
upon exit.

Volker Bandke <vbandke@bsp-gmbh.com> wrote in message
news:18q0nsgkcfc4i8md6ei28butpojdofoeje@4ax.com...
> On Sat, 15 Jul 2000 22:24:51 +1000, Ken Foskey <waratah@zip.com.au> wrote:
>
> >Volker Bandke wrote:
> >
> >> I do NOT believe that IBM clobbers R15 on a regular (or even irregular)
basis.
> >> At least I haven't seen in in my environment when playing around with
EXCI. I
> >> would display the return code after each and every CALL in the program
to find
> >> out who really is the one with the black hat.
> >
…[3 more quoted lines elided]…
> The reason I suggested to check the RETURN-CODE variable was exactly
that - Eileen
> suspected that some CALLed routine did NOT set R15 to 0, even though the
routine was
> successfull.  NAd this was just to find out WHERE the R15 was
(incorrectly) nor cleared.
>
> She found out, in the meantime, that here EXCI calls returned with a R15 =
12, and is
> investigating now WHY this is the case (here EXCI calls seem to work
perfectly, though)
>
>
…[7 more quoted lines elided]…
>       The solution to a problem changes the nature of the problem.
```

###### ↳ ↳ ↳ Re: Clearing Register 15

_(reply depth: 5)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e7hans8935nm5o8nf3k8kpjn1gd2p49iki@4ax.com>`
- **References:** `<s96e031e.008@UTAEMAIL.UTA.COM> <m26ums86midi17vp1t999c21l7b5qqep0p@4ax.com> <39705813.2EE5E6A1@zip.com.au> <18q0nsgkcfc4i8md6ei28butpojdofoeje@4ax.com> <4F7d5.4387$h77.2477325@news2.mia>`

```
On Tue, 18 Jul 2000 21:34:33 -0700, "mangogwr" <mangogwr@bellsouth.net> wrote:

>I've written and test an EXCI / DPL server and I can state for the record,
>that a correctly
>installed DPL config AND an UNMODIFIED DFHEXCI module clears R15.
>I tested more than 50 functions and my COND CODE was always correct
>upon exit.
That was my experience also.  Therefore I assume that there must be some problem in the
call that Eileen has coded somewhere.  But she doesn'r seem to have found it, yet



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      How does a project get to be a year late? ... One day at a time.
```

###### ↳ ↳ ↳ Re: Clearing Register 15

_(reply depth: 6)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-07-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000723183840.08288.00000299@ng-ft1.aol.com>`
- **References:** `<e7hans8935nm5o8nf3k8kpjn1gd2p49iki@4ax.com>`

```
>From: Volker Bandke vbandke@bsp-gmbh.com 
>Date: 7/19/00 2:06 AM Eastern Daylight Time
…[14 more quoted lines elided]…
>

Well gentlemen - I wish I knew how you did it because I'm still stuck -
however....

Since I can get to the IBM manuals on the web at home I did some digging and
found this:

From:

Title: CICS/ESA V4R1 External CICS Interface
Document Number: SC33-1390-01
Build Date: 04/21/98 09:59:40 Build Version: 1.3.0
Topic: 7.3.3
# The external CICS interface does not clear register 15 at termination, 
# regardless of whether your client program executes normally or not. 
# Therefore, even if your MVS client program terminates normally after 
# successfully using the external CICS interface, the job step could end 
# with an undefined return code. 

# To ensure a meaningful return code is given at termination, set the job 
# step return code before terminating your program. The sample client 
# programs illustrate how you can do this, using the saved response code 
# from last call to the external CICS interface. For example, the COBOL 
# sample DFH0CXCC program moves SAVED-RESPONSE to special register 
# RETURN-CODE before terminating. 

I have SC33-1390-00 at work and I'm not sure this is in it.  If it is I sure
missed it :(

Anyway guess I'll be putting in that dreaded MOVE +0 TO RETURN-CODE come Monday
morning.

Eileen

PS - Volker - the message was garbage, and for those of you curious the display
of the return-code gave 4616 or if I moved it to a PIC S9(8) field prior to
display I got 14616.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
