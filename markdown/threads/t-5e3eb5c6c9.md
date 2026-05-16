[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to read files in subprogram [URGENT]

_14 messages · 9 participants · 2009-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to read files in subprogram [URGENT]

- **From:** tiyinyin <progsystem@gmail.com>
- **Date:** 2009-07-18T05:45:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com>`

```
At work,i develop on mainframe (IBM MVS Z9, cobol 3.4).
I've created a main program [MP] wich calls (dynamic call) a subprogram
[B].

Subprogram B will have to read a sequential file that should be define
in the JCL which execute MP.

In MP i have done all the thing necessary for calling program
dynamically
In Subprogram B, i have declare a normal file read procedure.

The problem is that i don't know if it's possible to do thing like
that and if the subprogram could open the file declare in the JCL for
the main program .

I've not found reference in my manuals that could help me understand i
to read write file in subprogram

So, if somebody have the solution, it will be very usefull.
Thanks a lot
```

#### ↳ Re: How to read files in subprogram [URGENT]

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2009-07-18T15:55:10+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h3sk7v$nj6$1@news.dmz.bit.nl>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com>`

```
tiyinyin wrote:

> At work,i develop on mainframe (IBM MVS Z9, cobol 3.4).
> I've created a main program [MP] wich calls (dynamic call) a
…[15 more quoted lines elided]…
> to read write file in subprogram

IIRC you failed until now by compiling, linking and testing the MP in
combination with the subprogram.

Not being comfortable with IBM mainframes, but on other mainframes such
software solutions will run without problems. Don't get me started on
that, but even in a UNIX / Linux or DOS environment this will work.
```

#### ↳ Re: How to read files in subprogram [URGENT]

- **From:** Joel C Ewing <jREMOVEcCAPSewing@acm.org>
- **Date:** 2009-07-18T09:55:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wnl8m.8933$O23.8567@newsfe11.iad>`
- **In-Reply-To:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com>`

```
tiyinyin wrote:
> At work,i develop on mainframe (IBM MVS Z9, cobol 3.4).
> I've created a main program [MP] wich calls (dynamic call) a subprogram
…[17 more quoted lines elided]…
> Thanks a lot

z/OS JCL defines the run time execution environment for the job step, 
seen by both the main program and any called subprograms. If the file is 
only read within Subprogram B and read in its entirety by a single call, 
no problem.  Define the file in subprogram B, and do OPEN , READ, CLOSE 
operations all within Subprogram B.

If B will be called multiple times with a need to get subsequent records 
on each call things are a little trickier.  Even though you are calling 
the subprogram dynamically multiple times, the COBOL/LE runtime 
environment will only load the subroutine on the first call so that the 
file control blocks (DCB in z/OS parlance) containing the file status 
(implicitly created by the COBOL file definition) will be preserved 
between calls of B. You would need some internal "flag" so that on the 
first call you would OPEN the file, and also provide some mechanism for 
closing the file on the last call to B.  z/OS will normally do an 
auto-CLOSE of any open files at end of job step, but there are 
circumstances (e.g., execution of DB2 programs via "DSN" under batch 
TSO) where this is impossible, so doing an explicit CLOSE is a better 
practice.

If the file will be read by multiple program units in addition to B 
things get still more complex.  You can have multiple COBOL file 
definitions in different program units referencing the same JCL DDNAME, 
but only one may be OPEN at any given time.  It used to be possible to 
declare a file in one program unit and pass it as a parameter to a lower 
program unit, but it has been many years since I have had occasion to do 
this.  If only read access is involved, another possibility is to have 
multiple JCL DD statements pointing to the same physical file and have 
different file definition statements pointing to those unique DDNAMES in 
the various program units needing to read the file.
   JC Ewing
```

##### ↳ ↳ Re: How to read files in subprogram [URGENT]

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-07-18T10:22:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0Nl8m.425603$6p1.406812@en-nntp-02.dc1.easynews.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <Wnl8m.8933$O23.8567@newsfe11.iad>`

```
I agree with Joel on what to do if the only processing of the file is in the 
subprogram.  Just define it there and OPEN, REAL, CLOSE it there (in the 
subprogram) making certain that you only OPEN and CLOSE it once.

If, however, you want to share the file with multiple programs, you have (at 
least) two options.

Define the file as EXTERNAL in all programs.  Only OPEN and CLOSE it once (in 
one program) but you can then access the file in any program.
   OR
If the file is QSAM, you can still pass it (as an extension) via the CALL 
statement (and this will make the DCB available in all CALLed subprograms).  It 
is only VSAM files that may (no longer) be passed BY REFERENCE in a CALL 
statement.
```

#### ↳ Re: How to read files in subprogram [URGENT]

- **From:** Jessica Colman <jessica.colman@augustakom.net>
- **Date:** 2009-07-18T17:52:24+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h3sr3o$gug$1@svr7.m-online.net>`
- **In-Reply-To:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com>`

```
I'm much more familiar with PL/I than with COBOL, but what you like to 
do should be no problem. In PL/I, the limitations on writing files in 
dynamically called subroutines were removed with version 3 (Enterprise 
PL/I) and I think the same is true for COBOL.

Jessica


tiyinyin schrieb:
> At work,i develop on mainframe (IBM MVS Z9, cobol 3.4).
> I've created a main program [MP] wich calls (dynamic call) a subprogram
…[17 more quoted lines elided]…
> Thanks a lot
```

#### ↳ Re: How to read files in subprogram [URGENT]

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-07-18T11:54:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ftr3655de69najchoh837n3csa8dis1jul@4ax.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com>`

```
On Sat, 18 Jul 2009 05:45:43 -0700 (PDT), tiyinyin
<progsystem@gmail.com> wrote:

>At work,i develop on mainframe (IBM MVS Z9, cobol 3.4).
>I've created a main program [MP] wich calls (dynamic call) a subprogram
…[17 more quoted lines elided]…
>Thanks a lot

This is so very basic.  In the MP you send a code to B to tell it to
OPEN the file.  In the MP you send a code to B to tell it to READ the
file.  In the MP you send a code to B to tell it to CLOSE the file.
Your LINKAGE section in B contains a 1 byte command field and the
record layout.  These are what you pass from MP.  In B you READ the
file into the layout defined in Linkage.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"I am free of all prejudices. I hate everyone equally."
-- W.C.Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: How to read files in subprogram [URGENT]

- **From:** docdwarf@panix.com ()
- **Date:** 2009-07-20T13:34:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h41rpm$1a3$4@reader1.panix.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <ftr3655de69najchoh837n3csa8dis1jul@4ax.com>`

```
In article <ftr3655de69najchoh837n3csa8dis1jul@4ax.com>,
SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:

[snip]

>This is so very basic.  In the MP you send a code to B to tell it to
>OPEN the file.  In the MP you send a code to B to tell it to READ the
…[3 more quoted lines elided]…
>file into the layout defined in Linkage.

This is starting to sound like the I-O module I wrote a few decades back, 
when (company) wanted to avoid the work of cleaning out Dead Data and was 
approaching the 4-GB limit on a VSAM KSDS.

As the Germans say, 'plus ca change, plus c'est la meme chose'... so 
here's Free Advice: instead of a 1-byte command field you use a binary 
halfword (COMP 9(4)) and have B use it as identifier-1 for a GO TO 
DEPENDING ON... because if you manage this trick 'just this once' you will 
have to do it forever, for this program and this one file and for other 
programs with multiple files.

DD
```

###### ↳ ↳ ↳ Re: How to read files in subprogram [URGENT]

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-07-20T11:46:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t74965p63n1nu7l7afvimk3oigus9h0t81@4ax.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <ftr3655de69najchoh837n3csa8dis1jul@4ax.com> <h41rpm$1a3$4@reader1.panix.com>`

```
On Mon, 20 Jul 2009 13:34:46 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <ftr3655de69najchoh837n3csa8dis1jul@4ax.com>,
>SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:
…[21 more quoted lines elided]…
>DD

Good advice.  However, with the ability to now use the EVALUATE verb,
a 1 byte character field would work just as well and be just as easily
maintained.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Nice perfume.  Must you marinate in it?"
-- Unknown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: How to read files in subprogram [URGENT]

_(reply depth: 4)_

- **From:** "Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com>
- **Date:** 2009-07-20T13:09:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h428cg$mie$1@news.eternal-september.org>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <ftr3655de69najchoh837n3csa8dis1jul@4ax.com> <h41rpm$1a3$4@reader1.panix.com> <t74965p63n1nu7l7afvimk3oigus9h0t81@4ax.com>`

```
"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
news:t74965p63n1nu7l7afvimk3oigus9h0t81@4ax.com...
> On Mon, 20 Jul 2009 13:34:46 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[28 more quoted lines elided]…
>

Something that has always been fascinating to me is that people who decry 
"GO TO DEPENDING ON" to be evil (and avoided like the plague) are at the 
same time quite happy with using EVALUATE to do the same thing.
```

###### ↳ ↳ ↳ Re: How to read files in subprogram [URGENT]

_(reply depth: 5)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-07-20T12:02:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9a9c31a-9a60-4d45-adcb-06f2549cd518@y4g2000prf.googlegroups.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <ftr3655de69najchoh837n3csa8dis1jul@4ax.com> <h41rpm$1a3$4@reader1.panix.com> <t74965p63n1nu7l7afvimk3oigus9h0t81@4ax.com> <h428cg$mie$1@news.eternal-september.org>`

```
On Jul 21, 5:09 am, "Kerry Liles"
<kerry.removethisandoneperiod.li...@gmail.com> wrote:
> "SkippyPB" <swieg...@Nospam.neo.rr.com> wrote in message
>
…[37 more quoted lines elided]…
> same time quite happy with using EVALUATE to do the same thing.

Do you not understand the difference ?
```

###### ↳ ↳ ↳ Re: How to read files in subprogram [URGENT]

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-07-20T14:15:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<On39m.361940$Lo1.130215@en-nntp-04.dc1.easynews.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <ftr3655de69najchoh837n3csa8dis1jul@4ax.com> <h41rpm$1a3$4@reader1.panix.com> <t74965p63n1nu7l7afvimk3oigus9h0t81@4ax.com> <h428cg$mie$1@news.eternal-september.org> <a9a9c31a-9a60-4d45-adcb-06f2549cd518@y4g2000prf.googlegroups.com>`

```

"riplin" <riplin@Azonic.co.nz> wrote in message 
news:a9a9c31a-9a60-4d45-adcb-06f2549cd518@y4g2000prf.googlegroups.com...
On Jul 21, 5:09 am, "Kerry Liles"
<kerry.removethisandoneperiod.li...@gmail.com> wrote:
> "SkippyPB" <swieg...@Nospam.neo.rr.com> wrote in message
>
…[37 more quoted lines elided]…
> same time quite happy with using EVALUATE to do the same thing.

> Do you not understand the difference ?

I understand the difference when the EVALUATE uses "PERFORM" in its WHEN 
clauses.  I don't, however, understand the difference when EVALUATE uses GO TO 
in the WHEN clause - which is something that I have seem (semi-)often in the 
case where an eVALUATE appears in a subprogram's mainline as the first thing tto 
do.  (Often in a program that was rewritten from one that used the non-Standard 
ENTRY statement)
```

###### ↳ ↳ ↳ Re: How to read files in subprogram [URGENT]

_(reply depth: 7)_

- **From:** "Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com>
- **Date:** 2009-07-20T15:51:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h42hrp$2bh$1@news.eternal-september.org>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <ftr3655de69najchoh837n3csa8dis1jul@4ax.com> <h41rpm$1a3$4@reader1.panix.com> <t74965p63n1nu7l7afvimk3oigus9h0t81@4ax.com> <h428cg$mie$1@news.eternal-september.org> <a9a9c31a-9a60-4d45-adcb-06f2549cd518@y4g2000prf.googlegroups.com> <On39m.361940$Lo1.130215@en-nntp-04.dc1.easynews.com>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message 
news:On39m.361940$Lo1.130215@en-nntp-04.dc1.easynews.com...
>
> "riplin" <riplin@Azonic.co.nz> wrote in message 
…[55 more quoted lines elided]…
>


I understand the main useful difference would be to take the opportunity in 
the WHEN clause to do some other work (and not just issue a GO TO) but using 
the EVALUATE to (merely) avoid using GO TO DEPENDING ON is laughable.  Note 
that I did not advocate bringing back ALTER (but that is another religious 
war I suppose).
```

###### ↳ ↳ ↳ Re: How to read files in subprogram [URGENT]

_(reply depth: 8)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-07-20T15:57:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c826a2c7-7a2d-458f-8290-e620983571ee@j9g2000prh.googlegroups.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <ftr3655de69najchoh837n3csa8dis1jul@4ax.com> <h41rpm$1a3$4@reader1.panix.com> <t74965p63n1nu7l7afvimk3oigus9h0t81@4ax.com> <h428cg$mie$1@news.eternal-september.org> <a9a9c31a-9a60-4d45-adcb-06f2549cd518@y4g2000prf.googlegroups.com> <On39m.361940$Lo1.130215@en-nntp-04.dc1.easynews.com> <h42hrp$2bh$1@news.eternal-september.org>`

```
On Jul 21, 7:51 am, "Kerry Liles"
<kerry.removethisandoneperiod.li...@gmail.com> wrote:
> "William M. Klein" <wmkl...@nospam.ix.netcom.com> wrote in messagenews:On39m.361940$Lo1.130215@en-nntp-04.dc1.easynews.com...
>
…[63 more quoted lines elided]…
> war I suppose).

A 'GO TO' is not, in itself, a problem. The statement is very clear in
what the intention of the code is.

Where the problem lies when various control constructs are used is at
the point a label. In a reasonable program that one has been given it
should be possible to examine a part of the program that is used for a
particular purpose and to understand that part and modify it to remove
a bug or update its functionality.

If the program has been written in some particular ways then the logic
can be isolated and encapsulated so that changing one part in this way
does not affect other parts.

When looking at a part of the code and there is a label it is
necessary to determine the logic flow around and through that label.
At one extreme if the program has no procedure division sections, no
use of THRU, and no GO TO (ie the only control is PERFORM paragraph)
then the flow of control is easy to determine: it can only be that the
paragraph above returns to the PERFORM at this label and PERFORMs of
this label terminate at the next label. There is no drop through.

If there are any of SECTION, THRU, or GO TO in the program then it is
possible that other paths can be taken and drop-throughs may occur.
This makes the task of determining the logic an order of magnitude
more difficult. While it still may be that the code is isolated and
encapsulated it is not possible to be assured of this without a
complete examination of the whole program.

Other languages deal with this problem by having specific types of
labels. For example in C a function or procedure can only be used by a
call reference, you cannot goto or drop-into a procedure as one can in
COBOL.

So the problem is not the GO TO itself, but the fact that any GO TO
(or THRU or PD SECTION) increases the complexity of the program, or
the potential to be more complex.

You may not notice this in the programs that you write, or even in
programs that others write following identical standards to those that
you must obey. These may be arbitrarily complex but in a way that is
constrained by site standards to a fixed set of complexities. If there
is a guarantee of conformance then the area that needs to be
understood can be reduced.

EVALUATE falls within the scope of reduced complexity. GO TO DEPENDING
ON does not.
```

###### ↳ ↳ ↳ Re: How to read files in subprogram [URGENT]

_(reply depth: 7)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-07-20T15:28:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d4cbcd2f-a2af-4b46-aafa-9aef8f715e1d@p10g2000prm.googlegroups.com>`
- **References:** `<3f0a1104-9a37-4757-abb8-224ed86a995e@y17g2000yqn.googlegroups.com> <ftr3655de69najchoh837n3csa8dis1jul@4ax.com> <h41rpm$1a3$4@reader1.panix.com> <t74965p63n1nu7l7afvimk3oigus9h0t81@4ax.com> <h428cg$mie$1@news.eternal-september.org> <a9a9c31a-9a60-4d45-adcb-06f2549cd518@y4g2000prf.googlegroups.com> <On39m.361940$Lo1.130215@en-nntp-04.dc1.easynews.com>`

```
On Jul 21, 7:15 am, "William M. Klein" <wmkl...@nospam.ix.netcom.com>
wrote:
> "riplin" <rip...@Azonic.co.nz> wrote in message
>
…[47 more quoted lines elided]…
> clauses.

Good.

> I don't, however, understand the difference when EVALUATE uses GO TO
> in the WHEN clause

Nor, it seems, did the author of those lines.

> - which is something that I have seem (semi-)often in the
> case where an eVALUATE appears in a subprogram's mainline as the first thing tto
…[5 more quoted lines elided]…
>  wmklein <at> ix.netcom.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
