[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# compile+link Fujitsu Linux (by charles.goodman@bell.ca)

_16 messages · 4 participants · 2008-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** "SeaSideSam" <SeaSideSam@TheBeach>
- **Date:** 2008-02-09T20:02:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET>`

```
charlie.
i don't see where anyone has responded to your posting, so i'll give it a shot.  hopefully you have figured out the problem by now, but just in case...  btw.  i've been programming since 1969 (machine code), and cobol since 1973.  i haven't worked as a programmer in 10+ years (health), but keep up a bit with a rm/cobol package that i use at home.

the first thing i noticed was the absence of a linkage section in both your programs.  some compilers require this.  you don't have this section so i will assume that your compile does not have this requirement.

your compile command strings:
  cobol -M -dy -WC,"BINARY(BYTE),DLOAD" -o MYMAIN MYMAIN.CBL
  cobol -dy -shared -WC,"BINARY(BYTE)" -o libMYSUB1.so MYSUB1.CBL
i'm not familiar with this compiler, thus the question what is the file type of the object generated?

from MYMAIN:
  CALL 'MYSUB1'.
no file type is specified, thus using a default file type.  i will assume that your compile command strings imply the default file type for an object file.

from your runtime log:
  cobol-rts:: HALT: JMP0015I-U [PID:0000763D TID:002516C0] CANNOT CALL PROGRAM 'MYSUB1'.
  MYMAIN: undefined symbol: MYSUB1
my assumption is that JMP0015I-U is a runtime error message that doesn't give much in the way of workable info.  the 'undefined symbol' from MYMAIN is interesting.  my assumption is that this message means that when MYMAIN made it's call to MYMAIN1 the operating system could not find MYMAIN1.  here again file type is not specified thus the default file type is used.

i would be interested in the actual cause of your problem, so i'll continue to monitor usenet.

i am not a fan of linux, and i cuss microsucks with every keystroke.  my past relationship with big blue was mixed (they created all the dirty tricks that microsucks is now using), but they did make one decent operating system:  vm.  i just wish they had ported it to run on pcs.

good luck.  best wishes.





--------------=  Posted using GrabIt  =----------------
------=  Binary Usenet downloading made easy =---------
-=  Get GrabIt for free from http://www.shemes.com/  =-
```

#### ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-10T00:40:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET>`

```
On Sat, 9 Feb 2008 20:02:50 -0600, "SeaSideSam" <SeaSideSam@TheBeach> wrote:

>i am not a fan of linux, and i cuss microsucks with every keystroke.  my past relationship with big blue was mixed (they created all the dirty tricks that microsucks is now using), 
>but they did make one decent operating system:  vm.  i just wish they had ported it to run on pcs.

You sound like you're 17 years old.

Check out VMWare, which is free and does run on PCs.
```

##### ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-11T04:56:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BzQrj.143007$ST4.88822@fe07.news.easynews.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com>`

```
Speaking totally from ignorance,
   Does "VMWare" have anything to do with IBM's VM operating system?  Other than 
the letters in the name, I didn't think so (and a quick online search didn't 
seem to show any relationship).

     ***

FYI,
  IBM actually did port "VM" to PC's - and sold it (and a COBOL for it) for 
several years.  To give you an idea of when this happened, it ran on "PC AT/370" 
and "PC XT/370" machines.  (Some references are still available online).
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-10T22:11:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3f97224-0247-4801-a872-b0219ba23484@q77g2000hsh.googlegroups.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com>`

```
On Feb 11, 5:56 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> Speaking totally from ignorance,
>    Does "VMWare" have anything to do with IBM's VM operating system?  Other than
…[8 more quoted lines elided]…
> and "PC XT/370" machines.  (Some references are still available online).

The Byte Guide to the IBM PC of 'Fall 1984' contained details of the
IBM XT/370.

It had an additional 3 plug in cards. The first, the processor card,
had 2 68000 and an 8087 to run the System/370 instruction set. The 2nd
card has 512Kb RAM, the 3rd is a 3277 emulator with a coax connector
to a mainframe. It runs VM/PC, a 'skinny' version of CM/CMS. It will
also run some actual 370 programs at 0.2 MIPS (approx 4331-1 speed).
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-11T00:56:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r2svq35u5vh8pu2591oc0qghepg0d39jat@4ax.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com>`

```
On Mon, 11 Feb 2008 04:56:02 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Speaking totally from ignorance,
>   Does "VMWare" have anything to do with IBM's VM operating system?  Other than 
>the letters in the name, I didn't think so (and a quick online search didn't 
>seem to show any relationship).

There is no connection between IBM's VM and VMWare, except both create vitrual machines. 
There are quite a few other virtualization products, as shown in this comparison:
http://en.wikipedia.org/wiki/Comparison_of_virtual_machines

>FYI,
>  IBM actually did port "VM" to PC's - and sold it (and a COBOL for it) for 
>several years.  To give you an idea of when this happened, it ran on "PC AT/370" 
>and "PC XT/370" machines.  (Some references are still available online).

Hosting Windows is more difficult than hosting MS-DOS.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-11T11:51:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<REWrj.175276$rl3.35781@fe02.news.easynews.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com> <r2svq35u5vh8pu2591oc0qghepg0d39jat@4ax.com>`

```
OK,
  Now you have me totally confused.  It was you , Robert, (in a previous note) 
who said
    "Check out VMWare, which is free and does run on PCs."

to someone who said
 "my past relationship with big blue was mixed ...,  but they did make one 
decent operating system:  vm"

so was your note just an unrelated comment?
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-11T20:51:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ogt1r398ij6v1uuop5pq1rf4jqi5q4jj9e@4ax.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com> <r2svq35u5vh8pu2591oc0qghepg0d39jat@4ax.com> <REWrj.175276$rl3.35781@fe02.news.easynews.com>`

```
On Mon, 11 Feb 2008 11:51:14 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>OK,
>  Now you have me totally confused.  It was you , Robert, (in a previous note) 
…[7 more quoted lines elided]…
>so was your note just an unrelated comment?

z/VM and VMWare both create virtual machines. Neither is an operating system in the usual
sense, because they run operating systems rather than application programs.

z/VM runs on IBM mainframes, where it hosts IBM branded operating systems. VMWare runs on
Intel, Apple and most servers, where it hosts Windows and most Unixes. 

VMWare is actually several products. The free one runs on top of Windows; the paid ones
run on bare metal, use hardware assists (Intel changed its instruction set for VMWare),
and have low overhead. They 'cross compile' machine language in the OS they're hosting.
z/VM doesn't do that.




>-- 
>Bill Klein
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-12T05:40:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Tiasj.156513$X76.86146@fe08.news.easynews.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com> <r2svq35u5vh8pu2591oc0qghepg0d39jat@4ax.com> <REWrj.175276$rl3.35781@fe02.news.easynews.com> <ogt1r398ij6v1uuop5pq1rf4jqi5q4jj9e@4ax.com>`

```
z/VM can (and does) quite happily run "native"? is the same true for VMware.

Even if this weren't true for VM on IBM mainframes, I still don't understand how 
your original post was responsive to the actual text that it was responding to.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-12T08:03:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e293r31815ur3d4gtf154i7ldlg1et39fg@4ax.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com> <r2svq35u5vh8pu2591oc0qghepg0d39jat@4ax.com> <REWrj.175276$rl3.35781@fe02.news.easynews.com> <ogt1r398ij6v1uuop5pq1rf4jqi5q4jj9e@4ax.com> <Tiasj.156513$X76.86146@fe08.news.easynews.com>`

```
On Tue, 12 Feb 2008 05:40:03 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>z/VM can (and does) quite happily run "native"? is the same true for VMware.

I said VMWare runs on bare metal. If that's not what you mean by "native", please
clariify.

>Even if this weren't true for VM on IBM mainframes, I still don't understand how 
>your original post was responsive to the actual text that it was responding to.

I was responding to, "vm.  i just wish they had ported it to run on pcs." 

VMWare runs on PCs.

> wmklein <at> ix.netcom.com
>"Robert" <no@e.mail> wrote in message 
…[64 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

_(reply depth: 8)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-12T10:07:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6e2d07a-ceae-48e8-821d-a52cbeb4e1d5@y5g2000hsf.googlegroups.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com> <r2svq35u5vh8pu2591oc0qghepg0d39jat@4ax.com> <REWrj.175276$rl3.35781@fe02.news.easynews.com> <ogt1r398ij6v1uuop5pq1rf4jqi5q4jj9e@4ax.com> <Tiasj.156513$X76.86146@fe08.news.easynews.com> <e293r31815ur3d4gtf154i7ldlg1et39fg@4ax.com>`

```
On Feb 13, 3:03 am, Robert <n...@e.mail> wrote:
> On Tue, 12 Feb 2008 05:40:03 GMT, "William M. Klein" <wmkl...@nospam.netcom.com> wrote:
>
…[10 more quoted lines elided]…
> VMWare runs on PCs.


VMWare is not IBM's VM ported to PCs.

IBM's VM runs CMS, VMWare does not.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-13T00:21:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n135r3diiacuigd8vfrj4jbk4uhhk2jbku@4ax.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com> <r2svq35u5vh8pu2591oc0qghepg0d39jat@4ax.com> <REWrj.175276$rl3.35781@fe02.news.easynews.com> <ogt1r398ij6v1uuop5pq1rf4jqi5q4jj9e@4ax.com> <Tiasj.156513$X76.86146@fe08.news.easynews.com> <e293r31815ur3d4gtf154i7ldlg1et39fg@4ax.com> <c6e2d07a-ceae-48e8-821d-a52cbeb4e1d5@y5g2000hsf.googlegroups.com>`

```
On Tue, 12 Feb 2008 10:07:05 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 13, 3:03 am, Robert <n...@e.mail> wrote:
>> On Tue, 12 Feb 2008 05:40:03 GMT, "William M. Klein" <wmkl...@nospam.netcom.com> wrote:
…[16 more quoted lines elided]…
>IBM's VM runs CMS, VMWare does not.

He didn't say he wished they had ported CMS to PCs. 

If they had, VMWare could run it.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-13T17:43:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a%Fsj.159541$kw6.88788@fe10.news.easynews.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com> <BzQrj.143007$ST4.88822@fe07.news.easynews.com> <r2svq35u5vh8pu2591oc0qghepg0d39jat@4ax.com> <REWrj.175276$rl3.35781@fe02.news.easynews.com> <ogt1r398ij6v1uuop5pq1rf4jqi5q4jj9e@4ax.com> <Tiasj.156513$X76.86146@fe08.news.easynews.com> <e293r31815ur3d4gtf154i7ldlg1et39fg@4ax.com> <c6e2d07a-ceae-48e8-821d-a52cbeb4e1d5@y5g2000hsf.googlegroups.com> <n135r3diiacuigd8vfrj4jbk4uhhk2jbku@4ax.com>`

```
Robert,
  It is times like this that it would be RALLY nice if you just admitted that 
your original post was totally irrelevant to the comment to which you were 
replying, rather than continually trying to justify what could have been 
accepted as an "honest mistake".

Other than the letters "VM" and the fact that they each may "host" other things, 
there really is nothing similar between these topics and if one is replying to a 
specific comment about IBM's operating system of "VM", any mention of VMWare in 
the reply may be nice to do but is simply not relevant.
```

##### ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-02-12T11:42:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<06f7040a-7559-4daf-bb4d-00b645e197f7@e25g2000prg.googlegroups.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <ms6tq3p2jejspmek6t639dqsmjfce17dnp@4ax.com>`

```
On 10 Feb, 06:40, Robert <n...@e.mail> wrote:
> On Sat, 9 Feb 2008 20:02:50 -0600, "SeaSideSam" <SeaSideSam@TheBeach> wrote:
> >i am not a fan of linux, and i cuss microsucks with every keystroke.  my past relationship with big blue was mixed (they created all the dirty tricks that microsucks is now using),
…[4 more quoted lines elided]…
> Check out VMWare, which is free and does run on PCs.

You can run VM on a pc. Look for the HERCULES project on Google and
follow the links where people detail how they have loaded VM, MVS,
Cobol, etc., on to their pcs.
```

#### ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-02-13T11:18:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d5145183-5d14-4be3-afeb-1a0a2ec7da29@z17g2000hsg.googlegroups.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET>`

```
On 10 Feb, 02:02, "SeaSideSam" <SeaSideSam@TheBeach> wrote:
> charlie.
> i don't see where anyone has responded to your posting, so i'll give it a shot.  hopefully you have figured out the problem by now, but just in case...  btw.  i've been programming since 1969 (machine code), and cobol since 1973.  i haven't worked as a programmer in 10+ years (health), but keep up a bit with a rm/cobol package that i use at home.
…[15 more quoted lines elided]…
> my assumption is that JMP0015I-U is a runtime error message that >doesn't give much in the way of workable info.  the 'undefined >symbol' from MYMAIN is interesting.  my assumption is that this >message means that when MYMAIN made it's call to MYMAIN1 the >operating system could not find MYMAIN1.  here again file type is


JMP 151-U is a failure in the attempt to call the program named
MYSUB1. There is a second code with the message which relates to more
information available in the online and CD based manuals.

You are probably right about the lack of a linkage section.
```

##### ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-13T21:26:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ic7r3hjj5uea1mvov25h491ab6ir1b75v@4ax.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <d5145183-5d14-4be3-afeb-1a0a2ec7da29@z17g2000hsg.googlegroups.com>`

```
On Wed, 13 Feb 2008 11:18:33 -0800 (PST), Alistair <alistair@ld50macca.demon.co.uk> wrote:

>On 10 Feb, 02:02, "SeaSideSam" <SeaSideSam@TheBeach> wrote:
>> charlie.
…[21 more quoted lines elided]…
>information available in the online and CD based manuals.

The Process ID and Thread ID were assigned by Linux. They are not in the Fujitsu manual.

>You are probably right about the lack of a linkage section.

Linkage Section defines parameters (and a returning item).  Since the caller did not pass
parameters, there is no reason to have an empty linkage section.
```

##### ↳ ↳ Re: compile+link Fujitsu Linux (by charles.goodman@bell.ca)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-14T05:48:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SCQsj.204211$KG4.34230@fe09.news.easynews.com>`
- **References:** `<a84ce$47ae5af5$6214dca7$28171@ALLTEL.NET> <d5145183-5d14-4be3-afeb-1a0a2ec7da29@z17g2000hsg.googlegroups.com>`

```
Just out of curiosity, does anyone know of a current compiler that actually 
requires a Linkage Section in order to be a "subprogram"?  Obviously, if you 
want to PASS data via CALL, you need one, but there is certainly nothing in the 
COBOL Standard that requires such. In fact, with EXTERNAL data, such would be a 
"silly" (to me) restriction.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
