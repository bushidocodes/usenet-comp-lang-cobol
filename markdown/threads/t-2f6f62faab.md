[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

_14 messages · 13 participants · 1999-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** docdwarf@clark.net ()
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```

To all who addressed the difficulty I had with the override I wish to
express my thanks and gratitude.  To the group at large I wish to express
my apologies; the override, as written, *was* corrrect and I was
mis-reading the SCAN results.  I am sorry that I wasted your time with my
error; I am an idiot, a simpleton, a fraud and a charlatan... a janitor,
masquerading as a Programmer.

That being said the next difficulty will, I am sure, raise many giggles...
S0C7 under LE/370.  The job's sysout reads (slight truncation):

IEA995I SYMPTOM DUMP OUTPUT                                           
  USER COMPLETION CODE=4039 REASON CODE=00000000                      
 TIME=14.18.14  SEQ=04888  CPU=0000  ASID=0045                        
 PSW AT TIME OF ERROR  078D1000   88B77CFA  ILC 2  INTC 0D            
   ACTIVE LOAD MODULE           ADDRESS=08B335E8  OFFSET=00044712     
   NAME=CEEPLPKA                                                      
   DATA AT PSW  08B77CF4 - 00181610  0A0D58D0  D00498EC               
   GPR  0-3  84000000  84000FC7  00025488  08B77CFA                   
   GPR  4-7  00000003  000253D0  00025488  00000000                   
   GPR  8-11 00026017  08B3D5A6  000253D0  08B77C30                   
   GPR 12-15 00019898  00027018  88B3D7D2  00000000                   
 END OF SYMPTOM DUMP                                                  
IEF450I FRRGHAUE FRMTHAUD FRMTHAUD - ABEND=S0C7 U0000 REASON=00000007 

... and this 'smells', to me, like something in a system 'packing'
subroutine (CEEPLPKA) went 'kerflooie'.  At the head of the dump is:

Original Condition:                                                    
  CEE3207S The system detected a data exception.                       
Location:                                                              
  Program Unit: FRMTHAUD Entry: FRMTHAUD Statement:  Offset: +00009CD6 

Relying on the paltry skills which I've publicly shamed myself by showing
here I checked the compile, made with the LIST option, and found:

011700  PERFORM                                                
    019CD0  D203 D9C0 D47C          MVC  2496(4,13),1148(13)   
    019CD6  4120 B29E               LA   2,670(0,11)           
    019CDA  5020 D47C               ST   2,1148(0,13)          
    019CDE  58B0 C094               L    11,148(0,12)          
    019CE2  47F0 B02A               BC   15,42(0,11)           
    019CE6                 GN=1504  EQU  *                     
    019CE6  D203 D47C D9C0          MVC  1148(4,13),2496(13)   

... and got confused.  The statement at 9CD0 is an MVC, not one prone
towards blowing up... and the COBOL statement at 11700 is:

PERFORM 8980-INT-MONEY-STRD THRU 8980-EXIT

... without even a subscript which might be uninitialised.

Has the Universe changed so much that a search for the PSW will no longer
yield the ABENDing statement?

DD
```

#### ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** john_mindock@my-deja.com
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84d7t1$s4j$1@nnrp1.deja.com>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```

> Has the Universe changed so much that a search for the PSW will no
longer
> yield the ABENDing statement?

Th PSW is usually the NEXT statement to execute, not the one causing
the abend. Check what's before the PERFORM

John


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386A1B0B.79C526B6@NOSPAMwebaccess.net>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```
To non IBM programmers - SOC7 is IBMese for Data exception.  (trying to
do arithmetic with non numeric data)  This discussion may still be of
interest to you as much as for IBM programmers.  At least my reply/guess
is very general in nature.



docdwarf@clark.net wrote:

> That being said the next difficulty will, I am sure, raise many giggles...
> S0C7 under LE/370.  The job's sysout reads (slight truncation):
...
> The statement at 9CD0 is an MVC, not one prone
> towards blowing up... and the COBOL statement at 11700 is:
…[3 more quoted lines elided]…
> ... without even a subscript which might be uninitialised.


I remember about 15 years ago, a coworker was giving a class on abends
and dump reading.  He decided to create an error by overflowing
subscript bounds.  To his delight, he got a SOC7, which he gave to his
class.

If your abend points to a line for which the error doesn't make sense,
there are a couple of things to look at:
1.  Lines above and below - maybe put in a period or two to isolate the
line.
2.  Data overflow.  Occasionally you can move data so far outside of a
table, that it actually overwrites the program.  When the program tries
to execute data, it may by chance have a real command which it tries to
execute.  That's what happened 15 years ago.  
3.  Memory limits.  Some systems have different memory limits than
others.  Sometimes you have a choice which allows one to compile with
one memory model or another.  C programmers know what I mean.  And COBOL
II programmers know what I mean.  Occasionally a program can work OK
with one compile option - usually.  That "usually" is the killer.

What other general advice do you all have for abends pointing towards
statements which don't make sense to be wrong?  (all environments)
```

##### ↳ ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84f35p$8qr$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net> <386A1B0B.79C526B6@NOSPAMwebaccess.net>`

```
RE option 3, although I have never programmed on this particular OS,
I heard that one particular version of OS/2 prior to 2.0 (1.2 or 1.3 I
think)
was prized because it trimmed segments, etc exactly.  Almost any
wrong doing if this sort would trigger an error.

    Probably annoying as heck to the users.



>
> If your abend points to a line for which the error doesn't make sense,
…[14 more quoted lines elided]…
> statements which don't make sense to be wrong?  (all environments)
```

#### ↳ S0C7 (was Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84d6id$kks$1@nntp1.atl.mindspring.net>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```
Any chance that the original program's offset was for a version compiled with
OPT and the LIST output is from one with NOOPT?   Don't mean to be going back
to basics, but it does happen sometimes that you only have OPT code when you
get a S0C7.
```

#### ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C2CD88E50C38016E.C24FB2E9C715A888.DC89B4FA884D189A@lp.airnews.net>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```
On Wed, 29 Dec 1999 13:34:22 GMT, docdwarf@clark.net () enlightened
us:

>
>To all who addressed the difficulty I had with the override I wish to
…[53 more quoted lines elided]…
>DD

Doc,

I don't know if this still happens or not, but I remember many moons
and beers ago that program offsets could change depending on if the
original program had been compiled and linked with the PMAP option or
not.  So you might recompile and link the program with the PMAP option
(or LIST as I guess it is now known) and run the program again to see
if the SOC7 happens at the same PSW.   And you are correct in your
analysis that nothing in the Assembler code you showed should cause a
data exception.  You might also increase the size of the region you
are running in as well (Region= on EXEC statement) if you are running
in MVS.  

Good Luck.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Don't sweat the petty things and Don't pet the sweaty things.


Remove nospam to email me.

 Steve
```

#### ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** ThaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-bhyGMol3xph1@localhost>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```
On Wed, 29 Dec 1999 13:34:22, docdwarf@clark.net () wrote:
> Has the Universe changed so much that a search for the PSW will no longer
> yield the ABENDing statement?
> 

Personally I use the verb list from my last compile to find the 
statement in error.  Seems to work.

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Try a better search engine: http://www.google.com

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf524f$c0c60480$0100007f@vaagshaugen>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote in article
<y5oa4.20475$W2.185701@iad-read.news.verio.net>...
>   Program Unit: FRMTHAUD Entry: FRMTHAUD Statement:  Offset: +00009CD6 
...
> 011700  PERFORM                                                
>     019CD0  D203 D9C0 D47C          MVC  2496(4,13),1148(13)   
>     019CD6  4120 B29E               LA   2,670(0,11)           

Care to show the program list at the correct offset?

Sure your list corresponds to the load module executed?

Gunnar.
```

#### ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<psxa4.310$zp.4650@news3.mia>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```
The 'OFFSET' is +0009CD6 which is nowhere  near where you're looking.
'Statement:  Offset: +00009CD6 '   this means the stmt (machine ins) located
at that
offset from the load point.  Look thru your listing  for the CLOSEST address
to 9CD6.


<docdwarf@clark.net> wrote in message
news:y5oa4.20475$W2.185701@iad-read.news.verio.net...
>
> To all who addressed the difficulty I had with the override I wish to
…[54 more quoted lines elided]…
>
```

#### ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** Volker Bandke <vbandke@ibm.net>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pbin6sghs14iqrofr9olaud0930bns8g1o@4ax.com>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net>`

```
On Wed, 29 Dec 1999 13:34:22 GMT, docdwarf@clark.net () wrote:

>
>To all who addressed the difficulty I had with the override I wish to
…[24 more quoted lines elided]…
>subroutine (CEEPLPKA) went 'kerflooie'.

Nope.  This is just LE/370 way of telling you something is wrong.  Regs and PSW are just
the values inside of SCV D (at time of original abend)
>  At the head of the dump is:
>
…[4 more quoted lines elided]…
>
USE THE TEST(SYM) compile time option to get the real statement that failed
Also, it would be helpfull if you looked at offset 09CD6, not at offset 19Cd6.  But this
could be just the case of incorrect cut and paste, isn't it?
>
>Has the Universe changed so much that a search for the PSW will no longer
>yield the ABENDing statement?
Yes.  Somewhere I have a PDF file on debugging in the LE/370 environment.  Would you like
me to send you a copy of it?

May you have a happy and successful New Year
```

##### ↳ ↳ Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** "john doe" <someone@microsoft.com>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84hg6f$pmv$1@news.smartworld.net>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net> <pbin6sghs14iqrofr9olaud0930bns8g1o@4ax.com>`

```
I could use that PDF file this is exactly what I need!

tom@melee.net and thanks!

Volker Bandke wrote in message ...

>Yes.  Somewhere I have a PDF file on debugging in the LE/370 environment.
Would you like
>me to send you a copy of it?
>

>

>Nope.  This is just LE/370 way of telling you something is wrong.  Regs and
PSW are just
>the values inside of SCV D (at time of original abend)


>USE THE TEST(SYM) compile time option to get the real statement that failed
>Also, it would be helpfull if you looked at offset 09CD6, not at offset
19Cd6.  But this
>could be just the case of incorrect cut and paste, isn't it?
```

###### ↳ ↳ ↳ LE "Debugging" PDF (was Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84hhet$vso$1@nntp4.atl.mindspring.net>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net> <pbin6sghs14iqrofr9olaud0930bns8g1o@4ax.com> <84hg6f$pmv$1@news.smartworld.net>`

```
The LE debugging PDFs (and there are a couple of interest) can be downloaded
from:

"How to Solve Abends using Language Environment Dumps"
    http://www.s390.ibm.com/le/conference/s8209.pdf

"Solving LE ABENDs using the CEEDUMP"
    http://www.s390.ibm.com/le/conference/sh6209.pdf

Generally, if you are interested in LE "stuff" for which PDF "slide-shows"
can be downloaded, I suggest you look at:

    http://www.s390.ibm.com/le/conference/share.html

Then, again, I can also suggest that you look in deja.com and get information
on some of the classes that Steve Comstock has previously mentioned in
comp.lang.cobol.
```

###### ↳ ↳ ↳ Re: LE "Debugging" PDF (was Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84im6s$lte$1@news.igs.net>`
- **References:** `<y5oa4.20475$W2.185701@iad-read.news.verio.net> <pbin6sghs14iqrofr9olaud0930bns8g1o@4ax.com> <84hg6f$pmv$1@news.smartworld.net> <84hhet$vso$1@nntp4.atl.mindspring.net>`

```
William M. Klein wrote in message
>
>"How to Solve Abends using Language Environment Dumps"
>    http://www.s390.ibm.com/le/conference/s8209.pdf
>
Bill, I read this and started laughing.  Are you sure it is not about old
fart bowel problems?
```

###### ↳ ↳ ↳ Re: LE "Debugging" PDF (was Re: [OT] JCL Override Not... Overriding? - Solved, Thanks, Now S0C7?

_(reply depth: 5)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991231164433.21984.00000129@ng-xa1.aol.com>`
- **References:** `<84im6s$lte$1@news.igs.net>`

```
donald tees writes...

>William M. Klein wrote in message
>>
…[4 more quoted lines elided]…
>fart bowel problems?

Don, remember, the audience for that material is for people debugging LE. If
you want information on using LE dumps for debugging application programs, we
would be happy to come teach a class or two.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
