[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NT CICS Gurus - 3 questions?

_5 messages · 5 participants · 2000-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### NT CICS Gurus - 3 questions?

- **From:** ghobbs@sympatico.ca (G.Hobbs)
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396cc59b.21142901@news1.sympatico.ca>`

```
PC CICS Gurus - 3 questions - answers to any would be appreciated. 

At home, retired, no access to any skilled folk, cant afford IBM tech
support, on a Thinkpad, am running CICS for Windows NT V3.1, VisualAge
Cobol V2.2 (3.0 is too expensive) and DB2 V6.1 and trying to develop a
software package. The questions are...

-----------------
Question 1) 
-----------------
Using the PRINT function in EXEC CICS SEND MAP works fine but the
screen prints everytime which is not what I want. When I used to work
on a mainframe there was an independent 'screen print' key - can I set
up such on my platform? Can I print to my hard drive 
(consecutively if possible)? 
Recompiling pgm with/without PRINT is not an option. I read that
without the PRINT the data is sent to the printer buffer so is there a
way to tap this buffer (is this what the mainframe does)?  

------------------
Question 2) 
------------------
When I tran/comp/link with CICS down pgms always tran/comp/link
without problem. 
Doing the same with CICS up doesn't work and means I have to bring
CICS down everytime I make a change. Very painful. With CICS up, even
with no transactions running, i.e. screen is blank, gives the
following link error: 

E:\conrad\dovs>CALL XTCLH DOVSP11 

E:\conrad\dovs>set tempmem=on 

E:\conrad\dovs>CICSTCL DOVSP11.CCP EBCDIC BINARY(S370) ( -HOST 

-QLIB,SSRANGE,NOSEQUENCE,MAP,TEST -G 
-----------------------------------------------------------------------
  CICSTCL - Processing DOVSP11.CCP EBCDIC BINARY(S370) ( -HOST 

-QLIB,SSRANGE,NOSEQUENCE,MAP,TEST -G
-----------------------------------------------------------------------
-----------------------------------------------------------------------
  CICSTRAN - Translate E:\CONRAD\DOVS\DOVSP11.CCP
-----------------------------------------------------------------------
CICS for Windows NT API COBOL Translator
CICS for Windows NT Version 3.1
(C) Copyright International Business Machines 1988,1997. All Rights
Reserved.   
FAA0199I CICS COBOL translation ended with 0 error(s), RC = 0000

-----------------------------------------------------------------------
    CICSCOMP -  Compile DOVSP11.cbl
-----------------------------------------------------------------------
COB2 -c -comprc_ok=4 DOVSP11.cbl -qnosequence -qlib -qtrunc(bin)
-HOST 

-QLIB,SSRANGE,NOSEQUENCE,MAP,TEST -G
PP 5639-B92 IBM VisualAge for COBOL (Windows)  2.2 in progress ...
End of compilation 1,  program DOVSP11,  no statements flagged.
-----------------------------------------------------------------------
    CICSLINK -  Link DOVSP11.obj
-----------------------------------------------------------------------
ILIB /geni DOVSP11.def
IBM Librarian for Windows (TM) Version 0.00.04 cc_WTC354e (C)
Copyright IBM Corporation, 

1991, 1996.(C) Copyright Microsoft Corp., 1988, 1989.Licensed
Materials - Property of IBM - 

All Rights Reserved.ILINK /dll DOVSP11.obj
/out:F:\CNT310\RUNTIME\DOVSP11 /map:DOVSP11.map 

DOVSP11.exp /DEBUG  faacbid.lib faaotscb.lib faasr32.lib pa2clock.lib
iwzrwin3.obj 

db2api.lib

BM(R) Linker for Windows(R), ersion 02.01.private
opyright (C) IBM Corporation 

1988, 1998.
Copyright (C) Microsoft Corp. 1988, 1989.
All rights reserved.
ILink : atal error he system cannot find message for message number
0x13din message file for 

lnkwtx10.dll.

Link errors discovered

------------------
Question 3)
------------------
A CICS pgm obviously has many paths needing testing. How does one
automate such testing in CICS and I haven't got a lot of money (e.g.
not Winrunner)! Anybody ever tried to write something themselves?


- any takers and my sincere thanks in advance???

Graham Hobbs, ghobbs@sympatico.ca
```

#### ↳ Re: NT CICS Gurus - 3 questions?

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396CC9AA.53093596@yahoo.com>`
- **References:** `<396cc59b.21142901@news1.sympatico.ca>`

```


"G.Hobbs" wrote:
> 
> PC CICS Gurus - 3 questions - answers to any would be appreciated.
…[17 more quoted lines elided]…
> 
Try using the ALT-PrintScrn key -- this copies the active desktop screen
into the clipboard.  You can then paste it somewhere or print it.
Sorry, but can't help with the next two.

Joe
> ------------------
> Question 2)
…[78 more quoted lines elided]…
> Graham Hobbs, ghobbs@sympatico.ca
```

##### ↳ ↳ Re: NT CICS Gurus - 3 questions?

- **From:** Jason Edmeades <edmeades@uk.ibm.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396D8442.97399A0@uk.ibm.com>`
- **References:** `<396cc59b.21142901@news1.sympatico.ca> <396CC9AA.53093596@yahoo.com>`

```
AS per update on bit.listserv.cics-l:
2) This is problably because the program is currently loaded and stored
in memory.
If you link a program and the destination .dll is loaded, I think you
will get this error.
When you run a transaction, VA CICS loads its dll file in that
application server. When you run a different transaction, it unloads
that dll and reloads another (unless you have defined PPT entries to
make them permanently resident). To relink your app, ensure it is not in
use on any application server (including the background ones) - This is
'easy' if you are only running them from a terminal (run something else,
eg.CECI), slightly harder if you e.c.start them or run them from a
client. A use of cedf then cedf,off may help in this situation.

1) When a terminal receives a datastream containing the WCC Print bit
on, then it does a print screen. VA CICS shouldnt be doing anything
different in this case, although it is possible that on a mainframe the
sends buffer up more than on VA CICS (we only buffer one send).
You could come in from a CICS Universal Client/CTG and use the cicsterm
/f to send the info to a file (and you might want to try /j to buffer
all sends into one print job). Incidentally the client has an alt-P to
do a print screen, I think VA CICS may have as well.
I dont see how this is working differently to a mainframe, though.

Regards,
Jason Edmeades

Joseph Kohler wrote:
> 
> "G.Hobbs" wrote:
…[105 more quoted lines elided]…
> > Graham Hobbs, ghobbs@sympatico.ca
```

#### ↳ Re: NT CICS Gurus - 3 questions?

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 2000-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kk43l$m5t$1@hyperion.mfltd.co.uk>`
- **References:** `<396cc59b.21142901@news1.sympatico.ca>`

```
Graham,

I have asked one of my CICS Chaps to get on to this group and
answer your questions.  Watch this space...

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT International.

G.Hobbs <ghobbs@sympatico.ca> wrote in message
news:396cc59b.21142901@news1.sympatico.ca...
> PC CICS Gurus - 3 questions - answers to any would be appreciated.
>
…[99 more quoted lines elided]…
>
```

#### ↳ Re: NT CICS Gurus - 3 questions?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<825ums09t30ul8al4e9gis0ptlhccj5hcc@4ax.com>`
- **References:** `<396cc59b.21142901@news1.sympatico.ca>`

```
On Wed, 12 Jul 2000 19:28:17 GMT, ghobbs@sympatico.ca (G.Hobbs) wrote:


>Using the PRINT function in EXEC CICS SEND MAP works fine but the
<rest snipped>

I believe the EXEC CICS SEND MAP .... PRINT works as designed, with no difference to the
mainfrasme.  To have a "Print Screen" key, try to EXEC CICS ISSUE PRINT whenever a certain
function key is pressed
>
>------------------
…[3 more quoted lines elided]…
>without problem. 
<rest snipped again>
This looks like alinkage editor problem, or several of them.  The message path seems not
to be set up correctly, and also the module to be linked seems to be in use.
Try running another transaction in CICS (like CEMT) before recompiling the old one, that
should help the second problem.  Or, if the program is running an background, do a CEMT
SET PROG(xxx) new BEFORE trying to recompile (I know, it sounds counterintuitive, but it
might just do the trick)

As for the Linker message not showing up - try putting the IBMCOBW\BIN directory into
DPATH
>------------------
>Question 3)
…[6 more quoted lines elided]…
>- any takers and my sincere thanks in advance???

Nope, I do every testing with CEDF and the COBOL Debugger




     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      He who weeps when sowing shall laugh when reaping.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
