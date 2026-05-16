[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Structure Chart for cobol program

_11 messages · 7 participants · 2001-10_

---

### Structure Chart for cobol program

- **From:** tc_yohannan@hotmail.com (Chuck Leviton)
- **Date:** 2001-10-12T14:21:16+00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<3bc6fbb9.263235532@News.CIS.DFN.DE>`

```
Is there a compiler option or some other means when working on MVS
COBOL to generate a structure chart of the way in which paragraphs are
PERFORMed?

I am looking for essentially a list of para names with indentations to
show which para PERFORMs which other para
```

#### ↳ Re: Structure Chart for cobol program

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-10-14T04:50:40+00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<AQ8y7.28263$ev2.35704@www.newsranger.com>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE>`

```
Hi TC,

You're using MVS COBOL so I assume that you also use ISPF. If so, you can get
into edit for the source of the module you're interested in and do the
following:

On the cmd line enter: x all;f proc 8;f all p'^' 8;del all nx
next cmd           : create yrname;can

The member "yrname" will contain all the pnames in the pgm. You'll have to
indent them manually or you could add another "f all perform" and collect all
the "perform pgraph" stmts.

It's not fancy, but the price is right.

Regards, Jack



In article <3bc6fbb9.263235532@News.CIS.DFN.DE>, Chuck Leviton says...
>
>Is there a compiler option or some other means when working on MVS
…[4 more quoted lines elided]…
>show which para PERFORMs which other para
```

##### ↳ ↳ Re: Structure Chart for cobol program

- **From:** "Rufio" <davecawdell@home.com>
- **Date:** 2001-10-14T16:43:54+00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<ehjy7.140894$aZ6.33136889@news1.rdc1.az.home.com>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE> <AQ8y7.28263$ev2.35704@www.newsranger.com>`

```

"John H Sleight Jr" <nospam@newsranger.com> wrote in message
news:AQ8y7.28263$ev2.35704@www.newsranger.com...
> Hi TC,
>
> You're using MVS COBOL so I assume that you also use ISPF. If so, you can
get
> into edit for the source of the module you're interested in and do the
> following:
…[5 more quoted lines elided]…
> indent them manually or you could add another "f all perform" and collect
all
> the "perform pgraph" stmts.
>
…[3 more quoted lines elided]…
>

I like this - nice simple lo-tech solution. Q. I don't have my ISPF command
chart with me - how does the ^ differ from # ? Also, will this get messy if
the program performs sections, with a section exit paragraph in each
section?


>
>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Structure Chart for cobol program

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-18T16:22:09+00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<9qmvfo$rb6$1@peabody.colorado.edu>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE> <AQ8y7.28263$ev2.35704@www.newsranger.com> <ehjy7.140894$aZ6.33136889@news1.rdc1.az.home.com>`

```

On 14-Oct-2001, "Rufio" <davecawdell@home.com> wrote:

> I like this - nice simple lo-tech solution. Q. I don't have my ISPF
> command
…[3 more quoted lines elided]…
> section?

If you have a standard naming convention that says all paragraphs start with
a numeric value p'#' 8 works better because it skips all of the comments.  
p"^" 8 looks for non blanks.
```

###### ↳ ↳ ↳ Re: Structure Chart for cobol program

_(reply depth: 4)_

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-10-19T04:09:28+00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<YHNz7.34998$ev2.42611@www.newsranger.com>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE> <AQ8y7.28263$ev2.35704@www.newsranger.com> <ehjy7.140894$aZ6.33136889@news1.rdc1.az.home.com> <9qmvfo$rb6$1@peabody.colorado.edu>`

```
I don't think f all p'#' 8 will skip comments lines. f all p' #' 7 or p' ^' 7
will.  


In article <9qmvfo$rb6$1@peabody.colorado.edu>, Howard Brazee says...
>
>
…[11 more quoted lines elided]…
>p"^" 8 looks for non blanks.
```

#### ↳ Re: Structure Chart for cobol program

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-10-14T20:23:43+00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<jvmy7.28793$ev2.35729@www.newsranger.com>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE>`

```
Hi Rufio,

The P'^' means any non-blank chars.

I guess you could code "f all ' exit'" to identify the exit pgraphs.
BTW, I forgot to mention that you can create a PF key to do this stuff if you
use it often. As a mater of fact, I created a PDS member (PFKEYS) to keep all
this kind of stuff. Then I can cut & paste it into the PF keys when I need it. I
include comments, because I always forget which one I used for what. Sometimes,
even w/the comments I don't remember what I used them for. 

A sample is below. Regards, Jack

Sorry Chuck, for the salutation of my prev post. Didn't see your name till it
was too late.

***********************************************************************
***************  USE TO DELETE one of 2 paired lines    ***************
***************  saves the line w/"cont" in it and del  ***************
***************  etes the previous line.                ***************
***********************************************************************
f cont; f ' ' 1 prev;f ' ' 1 prev;:d;f p'=' 72
*********************************************************************   
***************  USE TO FIRE UP 8 ISPF WINDOWS AFTER    *************   
***************  ISPF STARTUP                           *************   
*********************************************************************   
SCRNAME SDSF1 PERM;SPLIT NEW;SCRNAME COMPILE PERM                       
SPLIT NEW;SCRNAME JOBJCL PERM;SPLIT NEW;SCRNAME PGMSRC PERM;            
SPLIT NEW;SCRNAME CPYBKS PERM;SPLIT NEW;SCRNAME MISC1 PERM              
SPLIT NEW;SCRNAME MISC2 PERM;SPLIT NEW;SCRNAME MISC3 PERM;;;            

*********************************************************************   
***************        USE TO FIRE UP A NEW WINDOW      *************   
*********************************************************************   
SPLIT NEW;SCRNAME                                                       
*********************************************************************   
***************      USE TO LIST ALL ACTIVE WINDOWS     *************   
*********************************************************************   
SWAP LIST
********************************************************************* 
***************   USE TO EXIT A WINDOW. ENTER REPEATEDLY   ********** 
***************   AT EOD UNTIL DELETE LOG DS PANEL APPEARS ********** 
********************************************************************* 
;=X
***************  USE TO bracket cobol paragraph names   ***************
***************  with '*****'                           ***************
***********************************************************************
Manually: x all;f all p'a####' 8 then use the following pf keys for 
Each paragraph name.
x all -exit;top;f p'a####' 8 nx;:r2;:.a;f nx a 8;f a 8;:.b
c all .a .a p'�' '*';c all .b .b p'�' '*';x all .a .b




In article <3bc6fbb9.263235532@News.CIS.DFN.DE>, Chuck Leviton says...
>
>Is there a compiler option or some other means when working on MVS
…[4 more quoted lines elided]…
>show which para PERFORMs which other para
```

##### ↳ ↳ Re: Structure Chart for cobol program

- **From:** tc_yohannan@hotmail.com (Chuck Leviton)
- **Date:** 2001-10-15T09:56:14-07:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<82bca2a3.0110150856.53231cfd@posting.google.com>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE> <jvmy7.28793$ev2.35729@www.newsranger.com>`

```
John, 
Thanks for the useful input.  It takes me a step in the right
direction. But what I really need is a way to know which para Performs
which other para w/ appropriate indentations.

Couple of other things...
- The non blank character is different on different emulators.  On
mine I have to enter the [ key and it shows up as the non blank ï¿½ .  I
have copied and pasted it here in my posting but am not sure if it
will show up in everbody's newsreader/browser.  I guess it is ASCII
150 or something like that and so you can get it by depressing the ALT
key and some 3 digit number!

- By doing an "x all '*' 7", we can eliminate the comment lines too if
we find they clutter up the output.

I like your idea of storing PF Key settings in a PDS member.  If you
know you will be working in one shop for a long while, you can also
explore the keyboard macros that most emulators provide and can be
used most effectively (in case you are not doing so already!)

Thanks again

John H Sleight Jr <nospam@newsranger.com> wrote in message news:<jvmy7.28793$ev2.35729@www.newsranger.com>...
> Hi Rufio,
> 
…[60 more quoted lines elided]…
> >show which para PERFORMs which other para
```

#### ↳ Re: Structure Chart for cobol program

- **From:** cmcgann@connect.ie (ClemMcGann)
- **Date:** 2001-10-16T07:53:39-07:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<2a0a162d.0110160653.6516d94b@posting.google.com>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE>`

```
Did you check 'application understanding'
which used to be part of ibm's visual age cobol
now they market websphere studio asset analyser
(you wouldn't think it from the name, but it will scan cobol)
however, I understand that 'application understanding'
is now a free download from their site
-----------------------------------------------------------------
tc_yohannan@hotmail.com (Chuck Leviton) wrote in message news:<3bc6fbb9.263235532@News.CIS.DFN.DE>...
> Is there a compiler option or some other means when working on MVS
> COBOL to generate a structure chart of the way in which paragraphs are
…[3 more quoted lines elided]…
> show which para PERFORMs which other para
```

##### ↳ ↳ Re: Structure Chart for cobol program

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 2001-10-17T09:26:24-05:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<3bcd9818$1_1@feed1.realtime.net>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE> <2a0a162d.0110160653.6516d94b@posting.google.com>`

```
Do you need a real structure chart,
or would you be happy with simply
knowing for a particular paragraph who calls it?

If the latter is useful, you might be interested
in our tools for generating HTMLized COBOL
program cross references.  The result
is an HTML page equivalent of the source
code with hot links for each name
leading to to its  definitions and uses.

You can download a sample at
http://www.semdesigns.com/Products/Formatters/index.html;
see COBOL example ZIP file.
```

#### ↳ Re: Structure Chart for cobol program

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-16T17:09:02+00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<OQZy7.31496$ev2.38016@www.newsranger.com>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE>`

```
On Fri, 12 Oct 2001 14:21:16 GMT, in article
<3bc6fbb9.263235532@News.CIS.DFN.DE>, Chuck Leviton stated 
>
>Is there a compiler option or some other means when working on MVS
…[4 more quoted lines elided]…
>show which para PERFORMs which other para
There is a Compiler option that shows everywhere a reference is in the program
for a paragraph or procedure name whether it is a go to or perform statement in
the reference section of the compile.
I use IBM COMPILER FOR VSE/ESA 1.1.1 (COBOL LE) WITH MAP AND CROSS REFERENCE
(FULL).

You could possible create a program that gave all of the perform statements a
level and make some sort of tree diagram, simply by reading the program and
listing every perform executed in each perform and then list everywhere each
perform was executed from.  In some cases certain papagraphs could be referenced
from multiple levels in a program.

The Problem is when dealing with external calls what would you want to do then?
CICS and on-line, interactive programs would be completely differrent if they
can call each other.
```

#### ↳ Re: Structure Chart for cobol program

- **From:** tal_rosenberger@hotmail.com (Tal Rosenberger)
- **Date:** 2001-10-21T22:51:13-07:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<4151cf5b.0110212151.328d1266@posting.google.com>`
- **References:** `<3bc6fbb9.263235532@News.CIS.DFN.DE>`

```
tc_yohannan@hotmail.com (Chuck Leviton) wrote in message news:<3bc6fbb9.263235532@News.CIS.DFN.DE>...
> Is there a compiler option or some other means when working on MVS
> COBOL to generate a structure chart of the way in which paragraphs are
…[3 more quoted lines elided]…
> show which para PERFORMs which other para

We have a solution to show graphical and interative structure charts,
flow diagrams, UML from MVS Cobol programs.

If you are interested please send me your contact details.

Regards,
Tal Rosenberger
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
