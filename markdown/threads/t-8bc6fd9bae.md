[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# compiler options for COBOL under os390

_13 messages · 10 participants · 2001-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### compiler options for COBOL under os390

- **From:** "G���nther Ruf" <guenther.ruf@aon.at>
- **Date:** 2001-04-09T10:56:03+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at>`

```
Hi!

Is there a way to write the COBOL options into a member and read it from
there instead of the
//     PARM='....' parameter in the JCL?

Thank you very much!

Greetings from Austria!

G�nther
```

#### ↳ Re: compiler options for COBOL under os390

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2001-04-09T20:57:36+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<josephk-289767.20573609042001@echo-01.iinet.net.au>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at>`

```
In article <3ad17920$0$18874@SSP1NO25.highway.telekom.at>,
 "Gï¿½nther Ruf" <guenther.ruf@aon.at> wrote:

> Hi!
> 
…[5 more quoted lines elided]…
> 
At the very beginning of your program (before IDENTIFICATION DIVISION) 
put

PROCESS option,option,....
```

#### ↳ Re: compiler options for COBOL under os390

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-04-09T13:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010409090006.22493.00003858@ng-xc1.aol.com>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at>`

```
Gï¿½nther writes...

>Hi!
>
…[4 more quoted lines elided]…
>Thank you very much!

Well, you can have the options as part of the source code itself: PROCESS lines
at the beginning of the source module ensure the compiler options go with the
code and are not dependent on various procs, JCL, or workbenches.

Don't think there's a way to put them in a separate file to be merged at
compile time, unless you write your own pre-process step (which wouldn't be too
hard; could use Dialog Manager file tailoring, for example).

Hope this helps,

Regards,

Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: compiler options for COBOL under os390

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-04-09T14:06:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BljA6.512$y32.61858@paloalto-snr1.gtei.net>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at>`

```
G�nther Ruf <guenther.ruf@aon.at> wrote in message
news:3ad17920$0$18874@SSP1NO25.highway.telekom.at...
> Hi!
>
…[3 more quoted lines elided]…
>

Assuming your options are a bunch of PROCESS statements, it be easier in
your compile JCL to just concatenate the options member to precede the real
source...


SYSIN DD  DSN=PDS.PROCESS.STATEMENTS(FAVORITE),DISP=SHR
           DD  DSN=THE.REAL.SOURCE.CODE,DISP=OLD

result to compiler...

  PROCESS TRUNC(BIN)
  PROCESS NOSSRANGE
  etc
  ID DIVISION.
  PROGRAM-ID. GREAT.
....
```

##### ↳ ↳ Re: compiler options for COBOL under os390

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-04-09T15:39:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QIkA6.872$FY5.51368@www.newsranger.com>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at> <BljA6.512$y32.61858@paloalto-snr1.gtei.net>`

```
Hi Gunther,

You didn't say why you wanted to do this. It could eliminate some of the
possibilities. Well, anyway:

You could use the JCL INCLUDE statement and code your EXEC statement in 
an INCLUDE member.

Jack 

In article <BljA6.512$y32.61858@paloalto-snr1.gtei.net>, Michael Mattias says...
>
>G�nther Ruf <guenther.ruf@aon.at> wrote in message
…[26 more quoted lines elided]…
>
```

#### ↳ Re: compiler options for COBOL under os390

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-04-09T10:35:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD1E4C7.A2348E91@brazee.net>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at>`

```
"Gï¿½nther Ruf" wrote:

> Hi!
>
…[4 more quoted lines elided]…
> Thank you very much!

You can put them in the front of your CoBOL source, which means you can
concatenate it to your source.   But I can't because Endeavor will cough
when it tries to migrate them to production.

Of course, you can have your JCL call a proc which has these parameters in
the proc.

It might help if we knew why you want to do this.
```

##### ↳ ↳ Re: compiler options for COBOL under os390

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2001-04-10T06:06:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD2A2B7.643846E2@worldnet.att.net>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at> <3AD1E4C7.A2348E91@brazee.net>`

```
Howard Brazee wrote:
> 
> "Gï¿½nther Ruf" wrote:
…[11 more quoted lines elided]…
> when it tries to migrate them to production.

If I recall correctly, you have mentioned this before as a
customization of Endevor (tm) at your site.  My shop uses Endevor and
we have no problems embedding PROCESS or CBL statements in our
programs.  I tend to do it because it will always be saved with the
source code.

> 
> Of course, you can have your JCL call a proc which has these parameters in
> the proc.
> 
> It might help if we knew why you want to do this.

I can think of several reasons why one would want to do this.  I once
had an large and ancient program blow up with a S0C7 after conversion
to COBOL II.  It wouldn't work with the NUMPROC(MIG) option which was
then our default, but would produce correct results with PROCESS
NUMPROC(NOPFD).

Recently, I was working with a large group of older programs that were
being converted to COBOL for MVS & VM solely to make them 31-bit
compatible.  A couple of those programs called ancient assembler
subprograms that were AMODE(24),RMODE(24) and could not be changed
(political reasons).  So, I needed to add RMODE(24) in the PROCESS
statement to keep them from blowing up.

Your default options probably include NORENT for batch COBOL.  In the
unlikely event that one might need to build a re-entrant batch COBOL
program, it would be better if the RENT option could be embedded in
the source code.

DYNAM is the default option for batch CONOL in my shop.  I might need
NODYNAM for batch EXCI programs.

I like the idea of concatenating a PROCESS member in front of the
source code, as suggested by Michael Mattias, but it probably would
cause problems for my Endevor administrators.
```

###### ↳ ↳ ↳ Re: compiler options for COBOL under os390

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-04-10T08:21:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD316D6.E56F2036@brazee.net>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at> <3AD1E4C7.A2348E91@brazee.net> <3AD2A2B7.643846E2@worldnet.att.net>`

```


Arnold Trembley wrote:

> Howard Brazee wrote:
> >
…[18 more quoted lines elided]…
> source code.

yep.


> > Of course, you can have your JCL call a proc which has these parameters in
> > the proc.
…[7 more quoted lines elided]…
> NUMPROC(NOPFD).

...

The thing which wasn't clear to me was in his original question:

> Is there a way to write the COBOL options into a
> member and read it from
> there instead of the
> //     PARM='....' parameter in the JCL?
>

It sounds as though this is a standard member which all programs use.  I don't
quite get why this would be desirable though.  If it was a program by program
basis, why use a member?  I don't understand his needs, and without such
understanding, I can answer his question but it may be the wrong question.   I'm
sure we have all seen this in applications development - sure I can do what you
asked, but is what you asked really the problem?
```

###### ↳ ↳ ↳ Re: compiler options for COBOL under os390

_(reply depth: 4)_

- **From:** JD <dragonslayer@bigfoot.com>
- **Date:** 2001-04-10T22:05:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD3BBFD.C673D93@bigfoot.com>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at> <3AD1E4C7.A2348E91@brazee.net> <3AD2A2B7.643846E2@worldnet.att.net> <3AD316D6.E56F2036@brazee.net>`

```
One reason is that the systems programmers do not have the compiler
installed with all the appropriate defaults, so having a common member
with all the appropriate options would simplify standardization.

Another is they may simply have a specific system which needs to be
compiled with specialized options, etc., etc.

Howard Brazee wrote:

>
>
…[62 more quoted lines elided]…
> you asked really the problem?
```

###### ↳ ↳ ↳ Re: compiler options for COBOL under os390

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-04-10T22:12:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b0i3t$cel$1@slb1.atl.mindspring.net>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at> <3AD1E4C7.A2348E91@brazee.net> <3AD2A2B7.643846E2@worldnet.att.net> <3AD316D6.E56F2036@brazee.net> <3AD3BBFD.C673D93@bigfoot.com>`

```
The method of creating a "customized" default compiler option module is
documented in the IBM COBOL for OS/390 & VM "customization" manual.  It is
entirely possible for an application group to create their own "default"
compiler module - place it in a load module and put that in the "steplib"
for their compile PROC.

My guess is that this is "fairly obscure" for most of the readers of this
NG, but I would be willing to explain the "details" - if others are
interested (and haven't read the customization guide for themselves)
```

###### ↳ ↳ ↳ Re: compiler options for COBOL under os390

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-04-11T07:28:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AD45C01.DE550721@brazee.net>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at> <3AD1E4C7.A2348E91@brazee.net> <3AD2A2B7.643846E2@worldnet.att.net> <3AD316D6.E56F2036@brazee.net> <3AD3BBFD.C673D93@bigfoot.com>`

```
In that case, my solution is to create a proc with the standard defaults, and
have everybody run JCL which calls the proc.  They can still do JCL
overrides.   I think this would work better and easier than having the
defaults in a member.

I do this with my JCL:
//SGPF       EXEC SGPF,PARM.SGPF#2=(MAP,XREF,
//     SSRANGE,FLAGSTD(H),OUTDD(SYSOUX),DYNAM,BUFSIZE(69900)),

The Proc doesn't have MAP, XREF, nor SSRANGE, but I like them in testing, so
I override it.

JD wrote:

> One reason is that the systems programmers do not have the compiler
> installed with all the appropriate defaults, so having a common member
…[71 more quoted lines elided]…
> > you asked really the problem?
```

#### ↳ Re: compiler options for COBOL under os390

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-04-11T04:11:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NPQA6.2818$FY5.200311@www.newsranger.com>`
- **References:** `<3ad17920$0$18874@SSP1NO25.highway.telekom.at>`

```
A plea to Gunther REf: PLEASE! Tell us, what problem were you trying to solve by
asking this question? Why was parm= not meeting your needs?

Jack


In article <3ad17920$0$18874@SSP1NO25.highway.telekom.at>, G�nther Ruf says...
>
>Hi!
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: compiler options for COBOL under os390

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-04-11T13:29:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010411092927.00621.00001032@nso-fe.aol.com>`
- **References:** `<NPQA6.2818$FY5.200311@www.newsranger.com>`

```
In article <NPQA6.2818$FY5.200311@www.newsranger.com>, John H Sleight Jr
<John_member@newsranger.com> writes:

>
>A plea to Gunther REf: PLEASE! Tell us, what problem were you trying to solve
…[4 more quoted lines elided]…
>

I would venture to guess that PARM= does not work as there is a 100-char
limit to what can be passed via PARM=.
I ran into the same situation when experimenting with enhancing our LE 
implementation and doing some 'tuning' tests.
Both options of 1) include PROCESS records in the source file and 
2)  DD concatenation were used in my case.  Initial testing used a 
single source with the PROCESS records embedded in the source.
When the options were defined, I copied the records into a separate 
PDS member to be included as the first SYSIN DD for the source to compile.
Later, when the Systems Programmer found the time to set the options
as defaults, we were able to phase out use of the Options Pds Member.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
