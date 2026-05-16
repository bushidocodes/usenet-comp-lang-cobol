[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sample for testing "backwards" perform thru

_15 messages · 10 participants · 2008-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Sample for testing "backwards" perform thru

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-11-13T22:10:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`

```
There were some comments about testing support for and behavior of
  Perform procedure-name-1 thru procedure-name-2
where Procedure-name-2 actually appears BEFORE procedure-name-1 in the source 
code.

The following is a sample program to test whether "your" compiler supports this 
(compiles it) and what happens.  I *think* (but won't swear to it) that all 
(most?) compilers will compile this and display "In para4" and then terminate.
 (I don't think that such compiler options as "perform-type" (MF) or OPT (IBM) 
will impact this, but I won't swear to that).

  * * *

       Identification Division.
        Program-ID. PERFTHRU.
       Procedure Division.
        Mainline.
           Display "In Mainline"
           Perform Para3 Thru Para1
           Display "After Perform"
           Stop Run
            .
       Para1.
           Display "In para1"
             .
       Para2.
           Display "In Para2"
              .
       Para3.
           Display "In para3"
             .
       Para4.
           Display "In para4"
             .
       Alternate-End.
           Stop Run
             .
```

#### ↳ Re: Sample for testing "backwards" perform thru

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2008-11-13T17:05:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1226620771_997@isp.n>`
- **In-Reply-To:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`

```
William M. Klein wrote:
> There were some comments about testing support for and behavior of
>   Perform procedure-name-1 thru procedure-name-2
…[9 more quoted lines elided]…
>   * * *
[snipped]
> 
Compaq COBOL V2.8-1286
------------------------
$ date
OpenVMS V8.3 on node PWS600 13-NOV-2008 16:57:07.34 Uptime 13 20:11:34

$ type x.cob
Identification Division.
Program-ID. PERFTHRU.
Procedure Division.
Mainline.
      Display "In Mainline"
      Perform Para3 Thru Para1
      Display "After Perform"
      Stop Run
      .
Para1.
      Display "In para1"
      .
Para2.
      Display "In Para2"
      .
Para3.
      Display "In para3"
      .
Para4.
      Display "In para4"
      .
Alternate-End.
      Stop Run
      .
$ cobo/list=x x
$ link x
$ run x
In Mainline
In para3
In para4
$
---------------------

Jeff


----== Posted via Pronews.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.pronews.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= - Total Privacy via Encryption =---
```

#### ↳ Re: Sample for testing "backwards" perform thru

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2008-11-14T08:39:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gfja07$i32$1@nntp.fujitsu-siemens.com>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:PB1Tk.165855$f64.161933@fe05.news.easynews.com...
> There were some comments about testing support for and behavior of
>  Perform procedure-name-1 thru procedure-name-2
…[38 more quoted lines elided]…
> Bill Klein

Fujitsu Siemens COBOL Compiler COBOL2000 V1.4A issues a warning during 
compilation:
     00005            DISPLAY "IN MAINLINE"
     00006            PERFORM PARA3 THRU PARA1
    >>>>>  BB044 >>>>> 0    IN THE STATEMENT "PERFORM <P1> THRU <P2> 
......." IS THE PARAGRAPH <P2> DEFINED IN FRONT OF PARAGRAPH <P1>.
     00007            DISPLAY "AFTER PERFORM"

the running program displays:
IN MAINLINE
IN PARA3
IN PARA4

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

#### ↳ Re: Sample for testing "backwards" perform thru

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-11-14T14:26:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o5g5jF1ul34U1@mid.individual.net>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`

```
In article <PB1Tk.165855$f64.161933@fe05.news.easynews.com>,
	"William M. Klein" <wmklein@nospam.netcom.com> writes:
> There were some comments about testing support for and behavior of
>   Perform procedure-name-1 thru procedure-name-2
…[5 more quoted lines elided]…
> (most?) compilers will compile this and display "In para4" and then terminate.

Boy are you in for a surprise!!

>  (I don't think that such compiler options as "perform-type" (MF) or OPT (IBM) 
> will impact this, but I won't swear to that).
…[27 more quoted lines elided]…
> 

I tried it with both OpenCOBOL and TinyCOBOL.  Both compiled the code without
comment or complaint.  Here are the results:

OpenCOBOL:

In Mainline
In para3
In para4

TinyCOBOL:

In Mainline
In para3
After Perform


But then, isn't that what "Undefined" means?  :-)

I can't make any promises but it would be fun to try it with things like
some of my old Ryan-McFarland compilers and maybe the one from OpenVMS
or one of the old PDP-11 COBOL's. Could be interesting to see just how
many different ways there are to nterpret the concept. 

bill
```

##### ↳ ↳ Re: Sample for testing "backwards" perform thru

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2008-11-14T10:24:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6a83b60-3b56-4cb6-afbb-2dacb622c609@s1g2000prg.googlegroups.com>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com> <6o5g5jF1ul34U1@mid.individual.net>`

```
On Nov 15, 3:26 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <PB1Tk.165855$f64.161...@fe05.news.easynews.com>,
>         "William M. Klein" <wmkl...@nospam.netcom.com> writes:
…[59 more quoted lines elided]…
> But then, isn't that what "Undefined" means?  :-)

TinyCobol is very broken then. It has made an arbitrary decision to
not execute the code in Para4. For example it may have been that in
Para4 there was a GO TO Para1 that completed the PERFORM.

What _is_ clearly defined is that with a PERFORM THRU the path should
'drop through' until the end point is reached (granted it never could
be in this test).

Cobol also states what happens when a STOP RUN is reached (in
Alternate end) or if the path falls off the end of the code (ie if the
Alternate-end paragraph was removed).

The other compilers get it right.


> I can't make any promises but it would be fun to try it with things like
> some of my old Ryan-McFarland compilers and maybe the one from OpenVMS
> or one of the old PDP-11 COBOL's. Could be interesting to see just how
> many different ways there are to nterpret the concept.

There is only one way to correctly interpret what happens with the
code. There is nothing to direct the path of execution back to Para1
before the STOP RUN or 'falling off the end'. Neither of which will
cause an error message.

Would you hope to find a compiler that did it differently ?

Do you think that TinyCobol is better ?

I certainly don't want arbitrary decisions made that make programs do
something different from what the source code indicates will happen.
```

###### ↳ ↳ ↳ Re: Sample for testing "backwards" perform thru

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-11-14T18:40:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o5v1jF20pffU3@mid.individual.net>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com> <6o5g5jF1ul34U1@mid.individual.net> <b6a83b60-3b56-4cb6-afbb-2dacb622c609@s1g2000prg.googlegroups.com>`

```
In article <b6a83b60-3b56-4cb6-afbb-2dacb622c609@s1g2000prg.googlegroups.com>,
	Richard <riplin@Azonic.co.nz> writes:
> On Nov 15, 3:26ï¿½am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>> In article <PB1Tk.165855$f64.161...@fe05.news.easynews.com>,
…[61 more quoted lines elided]…
> TinyCobol is very broken then. 

Not sure I would agree with that.  Undefined is undefined.  Seems that
grants rather a wide latitude for interpretation.

>                                  It has made an arbitrary decision to
> not execute the code in Para4. For example it may have been that in
> Para4 there was a GO TO Para1 that completed the PERFORM.

Ah!!  Now I see what you mean.  Interesting point and, I would have to agree.
They probably don't care, but I will likely forward this on to them.

> What _is_ clearly defined is that with a PERFORM THRU the path should
> 'drop through' until the end point is reached (granted it never could
…[4 more quoted lines elided]…
> The other compilers get it right.

Yeah, in light of the standard.  But I think the compiler should have done
like the Fuji-Siemens and at least told the programmer his code was crap
and give him a chance to fix it.  :-)  I am also glad (even though I really
don't get to do COBOL for a living anymore) that I never worked ina shop
that would have allowed something like this anywhere near a compiler.

>> I can't make any promises but it would be fun to try it with things like
>> some of my old Ryan-McFarland compilers and maybe the one from OpenVMS
…[6 more quoted lines elided]…
> Would you hope to find a compiler that did it differently ?

As I said, I would hope to never see code like this and I think, given the
availability of resources today, that all compilers should point out the
folly of this kind of code.

> Do you think that TinyCobol is better ?

Didn't say anything was better or worse.  I just ran it thru the two
compilers I have close at hand and posted the results.  When I have
time I will run it thru other (usually much older) compilers just to
see what happens.

> I certainly don't want arbitrary decisions made that make programs do
> something different from what the source code indicates will happen.

And, of course, the real solution to this is don't write arbitrary code.
Write you programs to do what you want and only what you want and you
will never have to worry about the compiler making arbitrary decisions.

bill
```

##### ↳ ↳ Re: Sample for testing "backwards" perform thru

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2008-11-15T06:34:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H3uTk.223740$Xn4.114220@fe09.news.easynews.com>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com> <6o5g5jF1ul34U1@mid.individual.net>`

```
So far, it looks like TinyCOBOL is the only NON-conforming compiler tested and 
reported on here.

Although I misread the Standard originally, this is NOT an "undefined" 
situation.  What OpenCobol (and the other compilers) do, is what the Standard 
(current and past) requires.

<JOKE>
  However, good programming would "require" that no one ever do this - and 
certainly that no one "rely" on the Standard-conforming behavior.
```

###### ↳ ↳ ↳ Re: Sample for testing "backwards" perform thru

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-11-15T17:04:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o8doaF2cr59U1@mid.individual.net>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com> <6o5g5jF1ul34U1@mid.individual.net> <H3uTk.223740$Xn4.114220@fe09.news.easynews.com>`

```
In article <H3uTk.223740$Xn4.114220@fe09.news.easynews.com>,
	"William M. Klein" <wmklein@nospam.ix.netcom.com> writes:
> So far, it looks like TinyCOBOL is the only NON-conforming compiler tested and 
> reported on here.
…[7 more quoted lines elided]…
> certainly that no one "rely" on the Standard-conforming behavior.
 
And just to tie the last ribbon on it, I have been in touch with the
TinyCOBOL folks and the last full-time maintainer has been forced by
other facets of  his life to bow out so while they admit this is a
bug in TinyCOBOL it is unlikely to be fixed in the foreseeable future.

bill
```

###### ↳ ↳ ↳ Re: Sample for testing "backwards" perform thru

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-11-20T13:41:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ol7ndF46bs2U1@mid.individual.net>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com> <6o5g5jF1ul34U1@mid.individual.net> <H3uTk.223740$Xn4.114220@fe09.news.easynews.com> <6o8doaF2cr59U1@mid.individual.net>`

```
In article <6o8doaF2cr59U1@mid.individual.net>,
	billg999@cs.uofs.edu (Bill Gunshannon) writes:
> In article <H3uTk.223740$Xn4.114220@fe09.news.easynews.com>,
> 	"William M. Klein" <wmklein@nospam.ix.netcom.com> writes:
…[14 more quoted lines elided]…
> bug in TinyCOBOL it is unlikely to be fixed in the foreseeable future.


And one more update.  I received an email todcay stating that the problem
has been fixed and the fixed code posted to CVS as version 0.64.3.

Pretty fast response considering I didn't expect it to be fixed at all.

bill
```

#### ↳ Re: Sample for testing "backwards" perform thru

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-11-14T08:54:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<em7rh4drc8in7l5c88osb218tbm0n8lrrj@4ax.com>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`

```
On Thu, 13 Nov 2008 22:10:55 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:


>       Identification Division.
>        Program-ID. PERFTHRU.
…[21 more quoted lines elided]…
>             .

An alternate to test would be to have Para3 go to or perform Para 1.
(at least for the compilers that do not return to display "After
perform").
```

##### ↳ ↳ Re: Sample for testing "backwards" perform thru

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2008-11-14T10:36:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e15e0a39-666d-453f-99b8-74f0e783b154@o4g2000pra.googlegroups.com>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com> <em7rh4drc8in7l5c88osb218tbm0n8lrrj@4ax.com>`

```
On Nov 15, 4:54 am, Howard Brazee <how...@brazee.net> wrote:
> On Thu, 13 Nov 2008 22:10:55 GMT, "William M. Klein"
>
…[28 more quoted lines elided]…
> An alternate to test would be to have Para3 go to or perform Para 1.

A goto Para1 in Para3 or Para4, or at any chosen point afterwards (but
before the stop run), will complete the PERFORM correctly. However, it
may be that the broken TinyCobol may not get to the goto before
deciding that is what will be done.

'Perform Para1' will not, or should not, complete the original
perform. Overlapping performs have an undefined result. In most modern
compilers the perform stack will ensure that only the current return
is seen and the previous one is restored. You should see 'Para1'
before the program continues as before to 'alternate-end'.

For a few ancient compilers that use self-modifying code, such as XE13
on 1900 series, the return point in Para1 will be overwritten by the
new perform and a subsequent 'go to Para1' will find that there is no
longer a return at the end of Para1 and that the original perform will
not complete, the path dropping through all again and finding the 'go
to Para1' each time.

> (at least for the compilers that do not return to display "After
> perform").



> --
> "In no part of the constitution is more wisdom to be found,
…[3 more quoted lines elided]…
> - James Madison
```

#### ↳ Re: Sample for testing "backwards" perform thru

- **From:** Blondie <gordcrawshaw@hotmail.com>
- **Date:** 2008-11-14T08:06:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68780b56-a9b1-4b0b-ba6b-6d759fc15ac2@u29g2000pro.googlegroups.com>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`

```
On Nov 13, 5:10 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> There were some comments about testing support for and behavior of
>   Perform procedure-name-1 thru procedure-name-2
…[38 more quoted lines elided]…
>  wmklein <at> ix.netcom.com

Compiled clean with MF NetExpress 3.1 on Windows XP.

Output:

In Mainline
In para3
In para4
```

#### ↳ Re: Sample for testing "backwards" perform thru

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-11-14T12:29:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<trjTk.5569$Dw1.5379@newsfe09.iad>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:PB1Tk.165855$f64.161933@fe05.news.easynews.com...
> There were some comments about testing support for and behavior of
>   Perform procedure-name-1 thru procedure-name-2
> where Procedure-name-2 actually appears BEFORE procedure-name-1 in the
source
> code.
>
>

Visual Cobol ver 2.10 copyright 1989

- compiles clean
- Displays

In Mainline
In para3
In para4

For compilers of this era and maybe lots of others, probably the "correct"
return code would be generated at the end of para1, but since the program
flow never gets there it never gets executed.

It's an interesting question but I can't imagine any programming problem
that would require this way of doing things.  If performing paragraphs out
of order is needed then seperate performs would be used, almost intuitively,
I'd think.

PL
```

##### ↳ ↳ Re: Sample for testing "backwards" perform thru

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-11-14T18:44:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o5v92F20pffU4@mid.individual.net>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com> <trjTk.5569$Dw1.5379@newsfe09.iad>`

```
In article <trjTk.5569$Dw1.5379@newsfe09.iad>,
	"tlmfru" <lacey@mts.net> writes:
> 
> William M. Klein <wmklein@nospam.netcom.com> wrote in message
…[20 more quoted lines elided]…
> flow never gets there it never gets executed.

Would be interesting to look at the generated output of some compilers to
see if there is dangling code there to handle the return even though it will
never be reached.  The place I can see this causing even more problems is
if other PERFORM THRU's call the Paragraphs in yet different orders.

> 
> It's an interesting question but I can't imagine any programming problem
> that would require this way of doing things.  If performing paragraphs out
> of order is needed then seperate performs would be used, almost intuitively,
> I'd think.

Exactly!!  Separate PERFORM's would remove all ambiguity and keep the
compiler from making those dreaded "arbitrary decisions".

bill
```

#### ↳ Re: Sample for testing "backwards" perform thru

- **From:** Duh_OZ <ozzy.kopec@gmail.com>
- **Date:** 2008-11-19T11:58:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5bf9d819-f527-496c-9280-3e03e2df84c8@r40g2000yqj.googlegroups.com>`
- **References:** `<PB1Tk.165855$f64.161933@fe05.news.easynews.com>`

```
MF 3.2.20 (DOS Shell in W2K):

IN MAINLINE
IN PARA3
IN PARA4

Realia 4.209 run under straight DOS on a w95 computer

IN MAINLINE
IN PARA3
IN PARA4
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
