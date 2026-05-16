[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# LE 1.8 wierd COBOL abend dump-longish ( x-posted to IBM-MAIN and COBOL )

_6 messages · 5 participants · 1998-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### LE 1.8 wierd COBOL abend dump-longish ( x-posted to IBM-MAIN and COBOL )

- **From:** "Ian Reid" <reid.ian@pmintl.ch>
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** alt.cobol,bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<01be22cc$b2a4cc50$1c00810a@pmecheew0267>`

```
Good Afternoon Listers

Anyone had this kind of abend before?
We're running OS/390 R5 and LE 1.8, and the program's batch :) .

In addition to the included U2120, we have had one (only one) occ. of a
U2000. 
I can't find anything on DIAL-IBM, the OS/390 Cd's or the net.

Someone throw me a life-bouy !

Dump info :

=================================================================

Condition Information for Active Routines                                  
    
  Condition Information for NLMC1210 (DSA address 0004F370)                
    
    CIB Address: 0002D478                                                  
    
    Current Condition:                                                     
    
      CEE0198S The termination of a thread was signaled due to an unhandled
cond
    Original Condition:                                                    
    
      CEE3250C The system or user abend U2120 R=NULL     was issued.       
    
    Location:                                                              
    
      Program Unit: NLMC1210 Entry: NLMC1210 Statement:  Offset: +000088BA

====================================================================

Also the following identification was found in the dump :


Program NLMC1210 was compiled 03/20/91 11:36:33 AM                         
 
COBOL Version = 1  Release = 3  Modification = 1      User Level = '    '

======================================================================

IEA995I SYMPTOM DUMP OUTPUT                                           
  USER COMPLETION CODE=4039 REASON CODE=00000000                      
 TIME=10.57.49  SEQ=02684  CPU=0000  ASID=0060                        
 PSW AT TIME OF ERROR  078D1000   8AFE33F2  ILC 2  INTC 0D            
   ACTIVE LOAD MODULE           ADDRESS=0AF14678  OFFSET=000CED7A     
   NAME=CEEPLPKA                                                      
   DATA AT PSW  0AFE33EC - 00181610  0A0D58D0  D00498EC               
   GPR  0-3  84000000  84000FC7  0002D478  0AFE33F2                   
   GPR  4-7  0AF128A0  00000000  0002D3D0  0002E017                   
   GPR  8-11 0AF3B175  0AF3A176  0002D3D0  8AFE3328                   
   GPR 12-15 00020910  0002F018  8AF3A81E  00000000                   
 END OF SYMPTOM DUMP                                                  

Regards
:Ian 
```

#### ↳ Re: LE 1.8 wierd COBOL abend dump-longish ( x-posted to IBM-MAIN and COBOL )

- **From:** Roland.Schiradin@t-online.de (Roland Schiradin)
- **Date:** 1998-12-08T00:00:00
- **Newsgroups:** alt.cobol,bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<74jpem$ago$1@news02.btx.dtag.de>`
- **References:** `<01be22cc$b2a4cc50$1c00810a@pmecheew0267>`

```
Ian Reid schrieb in Nachricht <01be22cc$b2a4cc50$1c00810a@pmecheew0267>...
>Anyone had this kind of abend before?
>We're running OS/390 R5 and LE 1.8, and the program's batch :) .

hmmh.. R5 comes with LE 1.9, LE 1.8 is for R4.


>>In addition to the included U2120, we have had one (only one) occ. of a
>U2000.
Looks like a user-abend. Check program NLMC1210

Roland
```

#### ↳ Demystifying LE and LE Abends

- **From:** Colin Campbell <ccampbe2@csc.com>
- **Date:** 1998-12-09T00:00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.asm370
- **Message-ID:** `<366EEFC9.6249@csc.com>`
- **References:** `<01be22cc$b2a4cc50$1c00810a@pmecheew0267>`

```
Ian Reid wrote:
> 
> Good Afternoon Listers
…[40 more quoted lines elided]…
> --

I've learned a bit about understanding LE's actions.  You mention having
OS/390 CD's; the OS/390 Language Environment bookshelf includes the
"Debug & Msgs" manual, which is where you start.  You find the U=40xx
abend explanation in Chapter 16.  (What you learn isn't all that
exciting, just that it is the end result of issuing the CEE0198S
message.)  Chapter 2 tells you that LE uses U4000 thru U4095 abend
codes, while reserving U0000 - U3999 for user programs.  It also
provides the high level information about message id's - CEE means LE,
IGZ means COBOL, etc.

If you have access to it, there is also a Licensed manual for LE, which
goes into depth explaining the ways in which LE works, and how it
changes things for experienced S/390 programmers.  Little things like
taking away one of your Gen. Purpose Regs., extending the Save Area and
calling it a DSA, etc.  In this manual, I was able to read about
CEEPLPKA (where you were at the time of abend).  It is a giant load
module, containing dozens of the CEExxxxx library routines, and residing
in the ELPA (Extended Link Pack Area above the 16M line).  Your
displacement is larger than our whole module, so I would guess that
either your later version of LE is larger, or your Sys Progs have been
tuning your system.

If you can make a module map of your CEEPLPKA, you can find out what
CSECT contains the address X'CDE7A' -- it is probably LE's "abend
routine", CEE3DMP, or something like that.  This sort of thing tends to
take some of the mystery out of the situation.

Another aspect of using LE is the run time options which you can
specify.  One of these is ABPERC(code), where 'code' is either a system
abend code coded as 'Sxxx' or a user abend code, coded as 'Udddd' that
you want LE to keep its hands off of.  If you ran again with
PARM='/ABPERC(U2120)', you could see the U2120 abend as you would have
under MVS, with no 'help' from LE.  Read about them in the LE
Programming Guide.  This manual will also show you how to control LE's
handling of exceptions globally.  For instance, our shop uses an abend
subroutine which issues U0999 abends accompanied by a message, and an
optional dump.  LE grabs the condition and produces a dump we don't
want!  We're going to have to create a table of codes we want LE to
ignore, or learn to live with big increases in the number of output
lines when jobs abend.  The CEEUOPT and CEEVOPT load modules let you
control single programs, or everything LE executes, or (I hope) some
level in between.

However, after all is said and done, I agree with one of your other
respondents, that this is just a program issuing a User Abend, for a
reason that is probably shown by a message somewhere in your output, or
is documented in the program's documentation.  One of your efforts
should be to determine whether this is a program that was written at
your shop or one that is part of a third party product.  No one knows
all of the world's mainframe products, and the program name doesn't look
at all familiar to me.

If you have the SoftAudit One tool (or one like it), you may be able to
tell if this program is identifiable to a product by looking at some of
the reports available from the SoftAudit product.

It looks as if LE is going to be with us on the mainframe for the long
term, so we all will have to get a good understanding of how to live
with it.
Good luck,
Colin Campbell
```

##### ↳ ↳ Re: Demystifying LE and LE Abends

- **From:** "Ian Reid" <reid.ian@pmintl.ch>
- **Date:** 1998-12-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be24dc$c90585e0$1c00810a@pmecheew0267>`
- **References:** `<01be22cc$b2a4cc50$1c00810a@pmecheew0267> <366EEFC9.6249@csc.com>`

```

Colin Campbell <ccampbe2@csc.com> wrote in article
<366EEFC9.6249@csc.com>...
[Large snip]
> It looks as if LE is going to be with us on the mainframe for the long
> term, so we all will have to get a good understanding of how to live
…[3 more quoted lines elided]…
> 
Colin, 
Thanks very much, what a clear and concise explanation.

As most repondents suggested, it was an application driven User Abend.
Security precluded looking at the source - hands tied and all that.

Many thanks to all who replied - I expect we've all learn't something here.

Regards

:Ian 
```

#### ↳ Re: LE 1.8 wierd COBOL abend dump-longish ( x-posted to IBM-MAIN and COBOL )

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-12-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981208204236.07840.00003807@ng20.aol.com>`
- **References:** `<01be22cc$b2a4cc50$1c00810a@pmecheew0267>`

```

I do not have the resources here at home to look this up. Can offer some
guesses that may help you.

The   ACTIVE LOAD MODULE       is      NAME=CEEPLPKA

I think LPKA has to do with Link Pack Area. So you are dealing with an
environmental/ linkage problem, perhpas.  A system module (LE or COBOL) is
expected to be present, by conventions communicated by the invoker (the
compiled program) and it is not there.

You posted message text to the effect 
"COBOL Version = 1  Release = 3  Modification = 1      User Level = '    '
".  Does this mean, do you think, that you are bringing in a pre COBOL II
module?  Have you planned for that, is the vendor telling you the OS/390 LE
environment that you have installed will be able to vector the antiquated
service module calls (ILB modules)? Have you relinked old code, that you did
not recompile (as might be necessary)?

We have had so many rapid changes in compilers that I may be guessing too far
back here.  But what compiler are you using that gets tagged "Version =  1"?

Anyway, I hope this guess is close enough to be useful; it looks like an older
module in a newer environment that is either not complete or not compatible.

Best Wishes,

Robert Rayhawk
RKRayhawk@aol.com
```

#### ↳ Re: LE 1.8 wierd COBOL abend dump-longish ( x-posted to IBM-MAIN and COBOL )

- **From:** slug@fast.co.za (Chris Anderson)
- **Date:** 1998-12-18T00:00:00
- **Newsgroups:** alt.cobol,bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<3679f5b7.23727545@news.netactive.co.za>`
- **References:** `<01be22cc$b2a4cc50$1c00810a@pmecheew0267>`

```
"Ian Reid" <reid.ian@pmintl.ch> wrote:


>Anyone had this kind of abend before?
>We're running OS/390 R5 and LE 1.8, and the program's batch :) .

May I suggest that you change your compiler options. 
There are certain combinations that produce this weird
stuff. Try it with TEST (Debug) options only.
Use the static mode options (e.g. for CICS), they seem
to be the most stable. Also check the order
of your LINKLIB concatenation.
------------------------------------------------------------------------
Chris Anderson		email:	                     slug@fast.co.za  
Y2K Cinderella Project		webmaster@cinderella.co.za
http://www.cinderella.co.za	        Striving for Year 2000 Compliance
------------------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
