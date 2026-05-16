[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL COPYBOOK CONVERTER

_27 messages · 14 participants · 2004-11_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### COBOL COPYBOOK CONVERTER

- **From:** FrOsTbYtE <frostbyte@arctic.net>
- **Date:** 2004-11-18T15:59:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com>`

```
OK. I have been doing this through SAS. But the maintenace has become
to great. We have flat files on mainframes that have copybooks defined
for them. 

Most records have hundreds of fields. I am only interested in 20 or
so. I would like to create the output copybook layout using the same
field names as the input copybook. 

Does anyone have a COBOL program that does nothing more than this?

Moreover, I would prefer to have something where I could compile the
program and pass the copybooks as PARMS in my JCL or as DD statements.
Basically something that I can reuse as long as I have an input and
output copybook layout that uses the same field names.

Any suggestions?

FYI I know JCL, SAS and SYNCSORT pretty well. Used COBOL in school
years ago so I understand just can't write from scratch.

Thanks.
```

#### ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-18T21:10:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ud8nd.3220451$yk.502624@news.easynews.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com>`

```
I am not clear on exactly what you are asking for the program to do.  If you 
have (COBOL) copybooks that describe the input file - do you want to MANUALLY 
create the output copybook (telling which files to keep) and then have a COBOL 
program create the output file for you?

If so, this is a pretty simple COBOL program (and could be done quite easily). 
Providing JCL to (semi-)randomly take various input/output copybooks and compile 
the COBOL program and then run it would also be easy.

If, however, you want a COBOL program to CREATE the output copybook, then  how 
will you tell it which fields you want to keep and which you don't?
```

#### ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-11-18T21:28:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9L4jKGleflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com>`

```
.    On  18.11.04
  wrote  frostbyte@arctic.net (FrOsTbYtE)
     on  /COMP/LANG/COBOL
     in  3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com
  about  COBOL COPYBOOK CONVERTER


f> Most records have hundreds of fields. I am only interested in 20 or
f> so. I would like to create the output copybook layout using the same
f> field names as the input copybook.
f>
f> Does anyone have a COBOL program that does nothing more than this?

   You mean using the same COPY element for two files? Sure, why not?  
You can use MOVE CORRESPONDING, or qualify the fields with the file  
names.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Es gibt manche Leute die nicht eher hï¿½ren bis man ihnen die Ohren abschneidet. -G.C.Lichtenberg
```

#### ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** FrOsTbYtE <frostbyte@arctic.net>
- **Date:** 2004-11-18T22:59:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o8rqp0lmeol119orc7evo6g5io8ptcid9d@4ax.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com>`

```
Thanks to all that have responded thus far. Actually what I am looking
for is quite simple. I want an example of COBOL code that would:

Read in a dataset (name provided in JCL)
Read in a copybook (name provided in JCL)
Write the dataset (name provided in JCL)
Using a different copybook (name provided in JCL)

Usually reading in just one DSN per instance of the job. If more than
one dataset is specified, I could concatenate them on DD statement in
the JCL as they will always use the same copybook and be the same
format. 

The output will always be just one dataset. 

The output dataset will only contain the fields specified in the
output copybook layout. Most of the time, just character or numeric
data. 

The idea is if the input copybook changes (i.e. a new field gets
added). No modification would need to be made unless the field is
going to be newly added to the output copybook. In short, no having to
recalculate field positions for the output.

That's it. Nothing fancy.

Does anybody have a working sample?



On Thu, 18 Nov 2004 15:59:21 -0500, FrOsTbYtE <frostbyte@arctic.net>
wrote:

>OK. I have been doing this through SAS. But the maintenace has become
>to great. We have flat files on mainframes that have copybooks defined
…[18 more quoted lines elided]…
>Thanks.
```

##### ↳ ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-19T04:25:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nBend.3235102$yk.501138@news.easynews.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <o8rqp0lmeol119orc7evo6g5io8ptcid9d@4ax.com>`

```
From your references to "DSN, JCL, SAS" - I am assuming that you are on an IBM 
mainframe.

With the COBOL there, there is no EASY way to "dynamically" read in a copybook 
(at run-time) and determine what fields to copy to an output file.

  ***

The way that I would (probably) solve your problem would be to set up a JCL 
stream.

1) Step 1
  Copy input and output copybooks from "individual" names to some common name 
(in a PDS) such as
    INPCPY
    OUTPCPY

2) Step 2
  Compile (probably also Step2a - link)  a simple program (using these standard 
copybook names) for the input and output files

3) Step 3
   Run the job specified above (with the designated input and output files)

***

Creating such JCL is a "piece of cake"  - Creating the COBOL program for Step 2 
is ALMOST as easy but does require someone knowing COBOL.
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2004-11-19T11:28:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0411191128.33f7eada@posting.google.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <o8rqp0lmeol119orc7evo6g5io8ptcid9d@4ax.com> <nBend.3235102$yk.501138@news.easynews.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<nBend.3235102$yk.501138@news.easynews.com>...
> From your references to "DSN, JCL, SAS" - I am assuming that you are on an IBM 
> mainframe.
…[46 more quoted lines elided]…
> >

1. Why can't you use existing system utilities to extract fields from
one dataset to create another? Read both copybooks, parse them, match
fields, calculate character positions and write a file containing the
needed JCL?

2. Or, read both copybooks as data files, parse them, match fields,
then write a COBOL program to be compiled as output?

3. Why supply an output copybook at all? How about (for example)
prefixing each line in the input copybook with an extra column. If the
character in that column is blank, then do nothing, otherwise append
that line to the output copybook and add a MOVE statement. Again, let
one COBOL program write another.

(Sorry if these suggestions do not make sense in a mainframe
environment. I do all of my work on PCs these days.)
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-11-19T19:40:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cnli75$a4p$1@peabody.colorado.edu>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <o8rqp0lmeol119orc7evo6g5io8ptcid9d@4ax.com> <nBend.3235102$yk.501138@news.easynews.com> <7f64e2ff.0411191128.33f7eada@posting.google.com>`

```
What's the advantage of having one program handle a bunch of copybooks pulled in
at run time?

Why not have a bunch of programs?   Either have the JCL select the program, or
have one program call the sub-program that matches the parms?
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** FrOsTbYtE <frostbyte@arctic.net>
- **Date:** 2004-11-19T19:57:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <o8rqp0lmeol119orc7evo6g5io8ptcid9d@4ax.com> <nBend.3235102$yk.501138@news.easynews.com>`

```
On Fri, 19 Nov 2004 04:25:55 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>From your references to "DSN, JCL, SAS" - I am assuming that you are on an IBM 
>mainframe.
…[25 more quoted lines elided]…
>is ALMOST as easy but does require someone knowing COBOL.

Bill K:

That is so simple it is almost eloquent. You are a genius. 

The reason for this program is:

1) I do not own the input copybook and cannot make changes to it.
2) The copybooks change in position too frequently to use SYNCSORT
3) Fields get added and reformatted all the time but seldom renamed or
deleted.
4) Reusability of code. 

I may have to compile and link. But it should work in theory.

Thanks to all for the help.
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 4)_

- **From:** epc8@juno.com (E P Chandler)
- **Date:** 2004-11-20T07:47:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f64e2ff.0411200747.4b192897@posting.google.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <o8rqp0lmeol119orc7evo6g5io8ptcid9d@4ax.com> <nBend.3235102$yk.501138@news.easynews.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com>`

```
FrOsTbYtE <frostbyte@arctic.net> wrote:
 
> Bill K:
> 
> That is so simple it is almost eloquent. You are a genius. 
> 

He certainly is! For some reason I did not think about using MOVE
CORRESPONDING inrec TO outrec. Other than stupidity, is there some
reason that I should avoid this construct?
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 5)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-11-20T15:58:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9LCvZiquflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com>`

```
.    On  20.11.04
  wrote  epc8@juno.com (E P Chandler)
     on  /COMP/LANG/COBOL
     in  7f64e2ff.0411200747.4b192897@posting.google.com
  about  Re: COBOL COPYBOOK CONVERTER


EPC> He certainly is! For some reason I did not think about using MOVE
EPC> CORRESPONDING inrec TO outrec. Other than stupidity, is there some
EPC> reason that I should avoid this construct?

   No.


Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Gerade das Gegenteil tun heiï¿½t auch nachahmen, es heiï¿½t nï¿½mlich das Gegenteil nachahmen. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 6)_

- **From:** alistair@ld50macca.demon.co.uk (Alistair Maclean)
- **Date:** 2004-11-21T11:27:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d487f04c.0411211127.5beb9c7e@posting.google.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de>`

```
l.willms@jpberlin.de (Lueko Willms) wrote in message news:<9LCvZiquflB@jpberlin-l.willms.jpberlin.de>...
> .    On  20.11.04
>   wrote  epc8@juno.com (E P Chandler)
…[10 more quoted lines elided]…
> 
Actually, YES. I worked at First Data Europe, in Basildon, England,
where we used an in-house developed cross-reference facility which
x-refed all data items. A move corresponding would miss a vital move.
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 7)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-11-21T20:43:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9LH2WGCeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com>`

```
.    On  21.11.04
  wrote  alistair@ld50macca.demon.co.uk (Alistair Maclean)
     on  /COMP/LANG/COBOL
     in  d487f04c.0411211127.5beb9c7e@posting.google.com
  about  Re: COBOL COPYBOOK CONVERTER


   on the CORRESPONDING clause in MOVE, ADD and SUBTRACT:


AM> where we used an in-house developed cross-reference facility which
AM> x-refed all data items. A move corresponding would miss a vital move.

   in other words, because this cross-reference tool could not cope  
with the COBOL syntax, the COBOL programs had to be crippled?

   BTW, it is the compiler which should provide the cross-reference  
listing.



Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Das Buch muï¿½ erst ausgedroschen werden. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 8)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-11-22T00:18:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hfaod.31854$hc5.19260383@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<9LH2WGCeflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com> <9LH2WGCeflB@jpberlin-l.willms.jpberlin.de>`

```
In reply to the question at the end,
does the compiler have all the information?

Warren simmons

Lueko Willms wrote:
> .    On  21.11.04
>   wrote  alistair@ld50macca.demon.co.uk (Alistair Maclean)
…[23 more quoted lines elided]…
> Das Buch muï¿½ erst ausgedroschen werden. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Cross-Referencing CORRESPONDING (was: COBOL COPYBOOK CONVERTER)

_(reply depth: 9)_

- **From:** l.willms@jpberlin.de (Lueko Willms)
- **Date:** 2004-11-22T08:45:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9LL49UtuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <9LH2WGCeflB@jpberlin-l.willms.jpberlin.de> <Hfaod.31854$hc5.19260383@news4.srv.hcvlny.cv.net>`

```
.    On  22.11.04
  wrote  wsimmons5@optonline.net (Warren Simmons)
     on  /COMP/LANG/COBOL
     in  Hfaod.31854$hc5.19260383@news4.srv.hcvlny.cv.net
  about  Re: COBOL COPYBOOK CONVERTER


WS> In reply to the question at the end,

   moved up here:

LW>>    BTW, it is the compiler which should provide the cross-
LW>> reference listing.

WS> does the compiler have all the information?

    For the compilation unit which it is working on, it should have.  
Otherwise the compiler could not generate correct code.

    On the other hand, a cross-reference generator for a whole set of  
COBOL programs should be able to parse COBOL syntax _completely._



   Quoted from previous messages:

>>    on the CORRESPONDING clause in MOVE, ADD and SUBTRACT:
>>
…[7 more quoted lines elided]…
>>




Yours,
Lï¿½ko Willms                                     http://www.willms-edv.de
/--------- L.WILLMS@jpberlin.de -- Alle Rechte vorbehalten --

Der Satz muï¿½ noch mit einem Bruch multipliziert werden. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: Cross-Referencing CORRESPONDING

_(reply depth: 10)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-11-22T13:29:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41A2301D.2020603@optonline.net>`
- **In-Reply-To:** `<9LL49UtuflB@jpberlin-l.willms.jpberlin.de>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <9LH2WGCeflB@jpberlin-l.willms.jpberlin.de> <Hfaod.31854$hc5.19260383@news4.srv.hcvlny.cv.net> <9LL49UtuflB@jpberlin-l.willms.jpberlin.de>`

```
I thought so, Lueko. But hesitate to commit myself
here on things so "new". <G>

Warren

Lueko Willms wrote:
> .    On  22.11.04
>   wrote  wsimmons5@optonline.net (Warren Simmons)
…[44 more quoted lines elided]…
> Der Satz muï¿½ noch mit einem Bruch multipliziert werden. -G.C.Lichtenberg
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-11-22T15:39:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cnt179$5at$1@peabody.colorado.edu>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com>`

```

On 21-Nov-2004, alistair@ld50macca.demon.co.uk (Alistair Maclean) wrote:

> Actually, YES. I worked at First Data Europe, in Basildon, England,
> where we used an in-house developed cross-reference facility which
> x-refed all data items. A move corresponding would miss a vital move.

I don't understand.   Why would a move corresponding miss any move because of a
cross-reference facility?
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 8)_

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-11-22T10:54:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B0ood.8052$Ro.556818@news20.bellglobal.com>`
- **In-Reply-To:** `<cnt179$5at$1@peabody.colorado.edu>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com> <cnt179$5at$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On 21-Nov-2004, alistair@ld50macca.demon.co.uk (Alistair Maclean) wrote:
> 
…[7 more quoted lines elided]…
> cross-reference facility?

Exactly. A move of record to record uses data names the same as any other.

Donald
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 8)_

- **From:** alistair@ld50macca.demon.co.uk (Alistair Maclean)
- **Date:** 2004-11-22T16:46:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d487f04c.0411221646.41f3c3a0@posting.google.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com> <cnt179$5at$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<cnt179$5at$1@peabody.colorado.edu>...
> On 21-Nov-2004, alistair@ld50macca.demon.co.uk (Alistair Maclean) wrote:
> 
…[5 more quoted lines elided]…
> cross-reference facility?

Move corresponding does not explicitly reference the subject fields
and therefore a program suite which parses the code and extracts
fields referenced by line will not explicitly pick up on the
implicitly referenced fields.
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 9)_

- **From:** Esmond Pitt <esmond.pitt@not.bigpond.com>
- **Date:** 2004-11-23T01:54:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3Lwod.45341$K7.43168@news-server.bigpond.net.au>`
- **In-Reply-To:** `<d487f04c.0411221646.41f3c3a0@posting.google.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com> <cnt179$5at$1@peabody.colorado.edu> <d487f04c.0411221646.41f3c3a0@posting.google.com>`

```
Alistair Maclean wrote:
> Move corresponding does not explicitly reference the subject fields
> and therefore a program suite which parses the code and extracts
> fields referenced by line will not explicitly pick up on the
> implicitly referenced fields.

That would appear to indicate a shortcoming in the program suite ...
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-11-23T14:30:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cnvhhg$pv4$1@peabody.colorado.edu>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com> <cnt179$5at$1@peabody.colorado.edu> <d487f04c.0411221646.41f3c3a0@posting.google.com>`

```

On 22-Nov-2004, alistair@ld50macca.demon.co.uk (Alistair Maclean) wrote:

> > I don't understand.   Why would a move corresponding miss any move because
> > of a
…[5 more quoted lines elided]…
> implicitly referenced fields.

So the move corresponding works fine.   The cross-referencing fails.
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-11-23T10:11:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0411231011.6c432c15@posting.google.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com> <cnt179$5at$1@peabody.colorado.edu> <d487f04c.0411221646.41f3c3a0@posting.google.com>`

```
alistair@ld50macca.demon.co.uk (Alistair Maclean) wrote

> Move corresponding does not explicitly reference the subject fields
> and therefore a program suite which parses the code and extracts
> fields referenced by line will not explicitly pick up on the
> implicitly referenced fields.

Nor would a group move.
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-11-24T13:33:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_l5pd.2486$_6.701@fe40.usenetserver.com>`
- **In-Reply-To:** `<d487f04c.0411221646.41f3c3a0@posting.google.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com> <9LCvZiquflB@jpberlin-l.willms.jpberlin.de> <d487f04c.0411211127.5beb9c7e@posting.google.com> <cnt179$5at$1@peabody.colorado.edu> <d487f04c.0411221646.41f3c3a0@posting.google.com>`

```
Alistair Maclean wrote:
> "Howard Brazee" <howard@brazee.net> wrote in message news:<cnt179$5at$1@peabody.colorado.edu>...
> 
…[14 more quoted lines elided]…
> implicitly referenced fields.

Wouldn't you have the same problem with other group-level items?  i.e.,

01  var1.
     12  var1-a  pic x.
     12  var1-b  pic x.

01  var2    pic xx.

move var1 to var2.
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2004-11-20T12:50:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cno05l$o3r$1@panix5.panix.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <nBend.3235102$yk.501138@news.easynews.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com>`

```
In article <7f64e2ff.0411200747.4b192897@posting.google.com>,
E P Chandler <epc8@juno.com> wrote:
>FrOsTbYtE <frostbyte@arctic.net> wrote:
> 
…[7 more quoted lines elided]…
>reason that I should avoid this construct?

Other than the fact that some folks seem to be religiously opposed to 
it... maybe.

DD
```

###### ↳ ↳ ↳ Re: COBOL COPYBOOK CONVERTER

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-11-23T22:50:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uqUod.2116$_6.707@fe40.usenetserver.com>`
- **In-Reply-To:** `<7f64e2ff.0411200747.4b192897@posting.google.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <o8rqp0lmeol119orc7evo6g5io8ptcid9d@4ax.com> <nBend.3235102$yk.501138@news.easynews.com> <j65tp01iot54d4rng5kolfv3b11mdje7kc@4ax.com> <7f64e2ff.0411200747.4b192897@posting.google.com>`

```
E P Chandler wrote:
> FrOsTbYtE <frostbyte@arctic.net> wrote:
>  
…[9 more quoted lines elided]…
> reason that I should avoid this construct?

For this, no.  For a large program, qualification can get to be a bit 
tedious, but it still works.  If "variable not uniquely qualified" is 
not at least a minor error on your compiler, and you don't check for it 
in your compiles, you can really get yourself messed up.
```

##### ↳ ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-11-19T06:18:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ju3rp0p4967ffkermboahude5krrq011tv@4ax.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com> <o8rqp0lmeol119orc7evo6g5io8ptcid9d@4ax.com>`

```
On Thu, 18 Nov 2004 22:59:13 -0500, FrOsTbYtE <frostbyte@arctic.net>
wrote:

>Thanks to all that have responded thus far. Actually what I am looking
>for is quite simple. I want an example of COBOL code that would:
…[22 more quoted lines elided]…
>That's it. Nothing fancy.

I posted here a program that does half of what you want. It reads and
interprets an input copybook, reads the data file and writes a CSV.
Look for COB2CSV. Logic to parse an output copybook would be the same
as input. Flagging matching fields would be easy.
```

#### ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-11-19T09:15:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-EF7A6E.09152319112004@knology.usenetserver.com>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com>`

```
In article <3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com>,
 FrOsTbYtE <frostbyte@arctic.net> wrote:

> OK. I have been doing this through SAS. But the maintenace has become
> to great. We have flat files on mainframes that have copybooks defined
…[18 more quoted lines elided]…
> Thanks.

If you are on a mainframe and have IBMs compiler there is an easy 
solution.  

Write out a simple template program that has nothing but the 
ID-division, et al, working storage section with your COPY statement and 
a procedure division with a goback.

Invoke the compiler on this simple program with the ADATA option.  The 
ADATA records for the program will be written to the SYSADATA dd.  You 
can then read them in and convert them to whatever you want.  The record 
layouts are described at the end of the IBM Cobol Language Reference for 
the latest version, but I dont remember which appendix.

No Cobol required for this, you could use SAS or Rexx or C or whatever 
you feel comfortable with.
```

#### ↳ Re: COBOL COPYBOOK CONVERTER

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-11-19T14:17:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cnkv9i$r58$1@peabody.colorado.edu>`
- **References:** `<3o2qp0dsqdn9g4tgn7u5a136q64l3b18k3@4ax.com>`

```
I have a program that copies a file that was FTPd to me, and reformats it to
match the tape that we have been getting.

The difference between the two files is that the tape has some packed decimal
fields, and the FTP file obviously doesn't.

This is the applicable part of the code:

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   67 Line(s) not Displayed
     COPY LAMMASTP REPLACING ==EDUSERV-RECORD==
                          BY ==TAPEOUT-REC==.
/
     COPY LAMMASTP REPLACING ==COMP-3== BY ==DISPLAY==.
-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   70 Line(s) not Displayed
         MOVE CORRESPONDING EDUSERV-RECORD TO TAPEOUT-REC
-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -   21 Line(s) not Displayed


The copy member starts off like this:

01  EDUSERV-RECORD.
    05  LN-DETAIL-RECORD.
        10  LN-BORROWER-NAME              PIC X(30).
        10  LN-SOC-SEC-NUMBER             PIC S9(09)      COMP-3.
        10  LN-P-ADDR-LINE-1              PIC X(25).
        10  LN-P-ADDR-LINE-2              PIC X(25).
        10  LN-P-ADDR-LINE-3              PIC X(25).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
