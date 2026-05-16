[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reverse Engineering Cobol Apps

_22 messages · 16 participants · 2001-05_

---

### Reverse Engineering Cobol Apps

- **From:** steven_jones@nas.adp.com (Steve Jones)
- **Date:** 2001-05-23T12:09:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
We have a Cobol application that will be rewritten in Java ... be this
good, bad, or ugly ... the decision has been made and there is no
talking us out of it !
  
Our first step is to reverse engineer the Cobol application such that
the Java engineers can use the output of this effort as the input to
their endeavor.  Our application is currently in Micro Focus Cobol v4
... on Win95, NT, and Unix.

Is anyone aware of a good (or half-way descent) tool that we can use
to run against this application and produce some sort of output ...
diagrams, functional decomps, whatever ... that might be either
useable as specs for the Java guys or that we could use as the first
step toward producing something that they can work from.

Much Thanks !

-Dr. Jones
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-05-23T14:30:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9eh33q$npd$1@nntp9.atl.mindspring.net>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
I have heard of some "medium poor"products that attempt to do this for IBM
mainframe COBOL programs - but none for PC products. If your program (which
is pretty unusual for a production Micro Focus program) actually sticks to
"ANSI" COBOL or IBM compatible COBOL, then you COULD try porting it to that
environment and use one of those tools.

As others will probably respond to this, the only semi-reliable "tool" for
doing this (usually) is a knowledgeable COBOL programmer.
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-05-23T22:44:44+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sv3ogt80cc10boksdpktiil2v69aegon1u@4ax.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
On 23 May 2001 12:09:09 -0700 steven_jones@nas.adp.com (Steve Jones) wrote:

:>We have a Cobol application that will be rewritten in Java ... be this
:>good, bad, or ugly ... the decision has been made and there is no
:>talking us out of it !
  
:>Our first step is to reverse engineer the Cobol application such that
:>the Java engineers can use the output of this effort as the input to
:>their endeavor.  Our application is currently in Micro Focus Cobol v4
:>... on Win95, NT, and Unix.

Why would you take that approach?

Why not determine the business function that the application performs and then
have the Java coders write the application?

As COBOL and Java are quite different, merely translating the code will create
a program that neither COBOL nor Java programmers will be able to reasonably
maintain. 

:>Is anyone aware of a good (or half-way descent) tool that we can use
:>to run against this application and produce some sort of output ...
:>diagrams, functional decomps, whatever ... that might be either
:>useable as specs for the Java guys or that we could use as the first
:>step toward producing something that they can work from.

Determine the business function and start from scratch.
```

##### ↳ ↳ Re: Reverse Engineering Cobol Apps

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-05-24T10:07:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0CCF56.FA53BE9B@Azonic.co.nz>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <sv3ogt80cc10boksdpktiil2v69aegon1u@4ax.com>`

```
Binyamin Dissen wrote:
> 
> Why not determine the business function that the application performs and then
…[6 more quoted lines elided]…
> Determine the business function and start from scratch.

Exactly.  How did it go ?

   '_Real_ programmers can write FORTRAN programs in _any_ language.'
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-05-23T21:43:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9eh3jp$n9p$1@newsg3.svr.pol.co.uk>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
Have you considered writing a cobol emulator in java ? Not so daft
when you consider I was playing Jet Set Willy using a ZX Spectrum
emulator written in java.

"Steve Jones" <steven_jones@nas.adp.com> wrote in message
news:f2b3dd25.0105231109.6d1b6ec@posting.google.com...
> We have a Cobol application that will be rewritten in Java ... be this
> good, bad, or ugly ... the decision has been made and there is no
…[15 more quoted lines elided]…
> -Dr. Jones
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-05-23T21:42:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q9WO6.17155$425.4449571@news3.rdc1.on.home.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
You could look into Netron's HotRod product http://www.netron.com/products/HotRod. It includes Merant's Revolve product so it should be able to handle Micro Focus COBOL.

Karl

"Steve Jones" <steven_jones@nas.adp.com> wrote in message news:f2b3dd25.0105231109.6d1b6ec@posting.google.com...
> We have a Cobol application that will be rewritten in Java ... be this
> good, bad, or ugly ... the decision has been made and there is no
…[15 more quoted lines elided]…
> -Dr. Jones
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-05-23T21:58:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UnWO6.43671$T7.3531222@bin1.nnrp.aus1.giganews.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```

"Steve Jones" <steven_jones@nas.adp.com> wrote in message
news:f2b3dd25.0105231109.6d1b6ec@posting.google.com...
> We have a Cobol application that will be rewritten in Java ... be
this
> good, bad, or ugly ... the decision has been made and there is no
> talking us out of it !
>

(zero stars)

WOW! I've heard of several instances of rewriting JAVA applications in
COBOL, but not this direction.

Will wonders never cease.

You might also check to see if there's an assembly-to-Java converter.
Then you could translate a COBOL object listing.
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 2001-05-23T23:12:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OlQspHBfXDD7IwHB@rcav8r.demon.co.uk>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
In article <f2b3dd25.0105231109.6d1b6ec@posting.google.com>, Steve Jones 
<steven_jones@nas.adp.com> writes
>We have a Cobol application that will be rewritten in Java ... be this
>good, bad, or ugly ... the decision has been made and there is no
>talking us out of it !

Interesting........ I'd love to hear the reasoning behind this if you 
have the time.

>
>Our first step is to reverse engineer the Cobol application such that
>the Java engineers can use the output of this effort as the input to
>their endeavor.  Our application is currently in Micro Focus Cobol v4
>... on Win95, NT, and Unix.

Probably a poor strategy. If you're going to throw away the investment 
you have in your business logic, you need to do it 'properly'.......

>
>Is anyone aware of a good (or half-way descent) tool that we can use
…[3 more quoted lines elided]…
>step toward producing something that they can work from.

In this context "something they can work from" is a functional 
specification. Don't be too surprised if a "Java guy" doesn't recognise 
one. Even if it does bite him / her in the ass. ;^)

I really can't offer much help (or indeed, hope!). I'd really like to 
hear how the project works out though. Really.

Regards

Nigel
```

##### ↳ ↳ Re: Reverse Engineering Cobol Apps

- **From:** test <mbs@labyrinth.net.au>
- **Date:** 2001-05-24T09:07:01+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0C4295.2ABB67EE@labyrinth.net.au>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <OlQspHBfXDD7IwHB@rcav8r.demon.co.uk>`

```
Hi,

Isn't there an application that converts COBOL to Java called PerCOBOL
and BlueJ?



Nigel Eaton wrote:

> In article <f2b3dd25.0105231109.6d1b6ec@posting.google.com>, Steve Jones
> <steven_jones@nas.adp.com> writes
…[40 more quoted lines elided]…
> the bit about otters)
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-05-24T04:49:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b0c92ca.5476205@news1.attglobal.net>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
Another suggestion - go to http://www.legacyj.com and just recompile
the program and get a .java file out of it.

On 23 May 2001 12:09:09 -0700, steven_jones@nas.adp.com (Steve Jones)
wrote:

>We have a Cobol application that will be rewritten in Java ... be this
>good, bad, or ugly ... the decision has been made and there is no
…[15 more quoted lines elided]…
>-Dr. Jones
```

##### ↳ ↳ Re: Reverse Engineering Cobol Apps

- **From:** gary drummond <gdrumm@ont.com>
- **Date:** 2001-05-24T14:37:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0D7F1D.1AC7CCD0@ont.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <3b0c92ca.5476205@news1.attglobal.net>`

```
Thane Hubbell wrote:
> 
> Another suggestion - go to http://www.legacyj.com and just recompile
> the program and get a .java file out of it.
> 

Thane, 
I did that, just to see what would happen. It worked, but it's not 
native JAVA (I think). There is a run-time fee, but much less than 
some COBOL. I thought it would be easier to port to java, and 
distribute, but the run-time looks about like COBOL in size.

I wrote a cross-reference program for an 8051 assembler and it did 
work. It ran a little slower than the MF Personal COBOL, comparing 
it to compiled code didn't seem to be fair...


Here is some of the generated code-just in case anyone is interested.
You don't have to touch it, but I thought COBOL was the "long-winded"
language. (Well, the new breed of "software engineers" say that!)
----------------------------------------
// Import Java Packages

import com.synkronix.cobol.*; // main import
import java.util.*;
import java.sql.*;
import java.awt.*;
import java.applet.*;

// Data Division
    static // initializer
    {
        Variable.validate("9JJALL0KYXJL7VCP5Z","PERCobol(TM) COBOL
runtimes Copyright 1996-2001 LegacyJ Corp.");
    }
    public class Fil implements Section
    {
        // Create Variables
        public final Variable in_line_OF_input_record_OF_input_file=new
Variable();
        public final Variable in_chars_OF_input_record_OF_input_file=new
Variable();
        public final Variable input_record_OF_input_file=new Variable();
        public final Variable in_symbol_OF_sort_record_OF_sort_file=new
Variable();
        public final Display in_num_OF_sort_record_OF_sort_file=new
Display();
        public final Variable type_flag_OF_sort_record_OF_sort_file=new
Variable();
        public final Variable sort_record_OF_sort_file=new Variable();
        public final Variable p_line_OF_giving_record_OF_giving_file=new
Variable();
----------------------------------------

The procedure code is not that hard to walk though, but I'm glad I
don't have to try to "maintain" code like this. Again, you don't have
to touch the generated code, it does work, and the run-time is 
cheaper than the COBOL ones being *bitched* about in this group.

So, it does work as advertised. Like any generated language, names are
llllllloooooooonnnnnnnggggggg, and I would pity anyone who tryed to 
keep them! However, even changing the names to shorter ones would still
leave the problem of the run-times hiding much of the COBOL 
built-in capabilities, and would not be *pure* java programming. 

Anyone trying to convert COBOL to java would be better off using
PERCobol as it is, because it will stil be COBOL. I talked to the
Sales Manager, and BlueJ is what they say to use for new, or 
graphical type development, but again-still COBOL...

Gary

By the way, I know enough about java to spell it ;^)

cases
```

###### ↳ ↳ ↳ Re: Reverse Engineering Cobol Apps

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-05-24T21:53:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LpfP6.60410$T7.4978549@bin1.nnrp.aus1.giganews.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <3b0c92ca.5476205@news1.attglobal.net> <3B0D7F1D.1AC7CCD0@ont.com>`

```

"gary drummond" <gdrumm@ont.com

> Anyone trying to convert COBOL to java would be better off using
> PERCobol as it is, because it will stil be COBOL. I talked to the
> Sales Manager, and BlueJ is what they say to use for new, or
> graphical type development, but again-still COBOL...
>

So you're saying: Keep and maintain the COBOL source but instead of
compiling it, PerCOBOL it?

Well, why the hell not?

After all, a COBOL compiler simply converts COBOL source into cryptic
assembly/object which virtually nobody looks at anyway. Same could be
true for the java output of PerCOBOL. Just gotta keep the Java
programmers away from the 'executable(?)' code. Better still, don't
have any Java programmers in the building.

Get the best of both worlds: Business logic and investment in
experience with the COBOL and the latest/greatest fad with Java. Works
for me.

P.S.,

I made a similar suggestion to George McGovern many years ago on
school busing. My plan was to send children to the school closest to
their home. BUT the kids would have to take a two-hour bus trip
through a neighborhood of differing ethnic makeup to and from school.

McGovern never acknowledged my suggestion.
```

###### ↳ ↳ ↳ Re: Reverse Engineering Cobol Apps

_(reply depth: 4)_

- **From:** gary drummond <gdrumm@ont.com>
- **Date:** 2001-05-24T20:09:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0DCCFC.62CB3AA1@ont.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <3b0c92ca.5476205@news1.attglobal.net> <3B0D7F1D.1AC7CCD0@ont.com> <LpfP6.60410$T7.4978549@bin1.nnrp.aus1.giganews.com>`

```
Jerry P wrote:
> 
> "gary drummond" <gdrumm@ont.com
…[16 more quoted lines elided]…
> have any Java programmers in the building.

But the original thread was about developing/converting to java. Leaving
it in COBOL is not the answer he wanted. A large RT for java is not what
they wanted, IMHO, and I see no advantage in that-except for the
management-types who want someone to say "Yep, it's a JAVA app now!".
Now-the BlueJ environment sounds OK. A graphical screen, a buzz word
enjoyed by many a manager, but supported in COBOL code, THAT sounds like
something worth following up on, because you're not hiding the fact that
it's all in COBOL. Flexus' SP2, which I'll get to test when I get my new
CD, sounds just as good, if not better.

See my earlier post on "Internet Enabled COBOL - NO! You can't because
it works!", because it (tongue-in-cheek?) states the "real" reasons
COBOL is "BAD", at least in the opinion of the current
software-engineer/CTO/PM/Acadamia-nut  people. For some reason they
don't understand the world of data processing, which I thought was to
develop applications to do your business, following the business rules
required, by designing/coding something that can be maintained over a
long period of time.

Sorry about that, but that little third-party viewpoint summed up my
feeling for the last 5-6 years. There are times to use the newer
technology, but just "because it's there" is not a good reason. There
are a LOT of dot.com's who "could" have told you why...
> 
> Get the best of both worlds: Business logic and investment in
> experience with the COBOL and the latest/greatest fad with Java. Works
> for me.

Yes, for me too-until they find out that they still need a COBOL
programmer.

> 
> P.S.,
…[6 more quoted lines elided]…
> McGovern never acknowledged my suggestion.

I believe I said something similar when mine began busing. I wanted them
to close ALL the schools in the "wrong areas", and bus the ones that
needed to get to school. I am not embarrassed to admit that it worked
out much better when they let the kids pick their high school. They
created "magnet" schools, with special funding and teachers. My sons
picked the engineering/math schools, and did *much* better than I did.
So-I've been wrong, and I will be again... (BUT NOT NOW! ;^)

Gary
```

###### ↳ ↳ ↳ Re: Reverse Engineering Cobol Apps

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-05-25T07:01:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0E579F.45877D70@brazee.net>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <3b0c92ca.5476205@news1.attglobal.net> <3B0D7F1D.1AC7CCD0@ont.com> <LpfP6.60410$T7.4978549@bin1.nnrp.aus1.giganews.com>`

```


Jerry P wrote:

> "gary drummond" <gdrumm@ont.com
>
…[9 more quoted lines elided]…
> Well, why the hell not?

It depends upon why the company is switching to Java.  It may be because
they don't want to have to keep programmers who know Java and CoBOL.
```

###### ↳ ↳ ↳ Re: Reverse Engineering Cobol Apps

_(reply depth: 5)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-05-25T22:21:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OVAP6.696$NK4.121624@news2.aus1.giganews.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <3b0c92ca.5476205@news1.attglobal.net> <3B0D7F1D.1AC7CCD0@ont.com> <LpfP6.60410$T7.4978549@bin1.nnrp.aus1.giganews.com> <3B0E579F.45877D70@brazee.net>`

```

"Howard Brazee" <howard@brazee.net>

> > So you're saying: Keep and maintain the COBOL source but instead
of
> > compiling it, PerCOBOL it?
> >
> > Well, why the hell not?
>
> It depends upon why the company is switching to Java.  It may be
because
> they don't want to have to keep programmers who know Java and CoBOL.

I agree your question ("why the company is switching to Java") is at
the heart of the plan.

With my plan they'd have Java but  wouldn't NEED any Java programmers!
```

###### ↳ ↳ ↳ Re: Reverse Engineering Cobol Apps

_(reply depth: 6)_

- **From:** gary drummond <gdrumm@ont.com>
- **Date:** 2001-05-27T00:46:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B10B0DC.524356E5@ont.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <3b0c92ca.5476205@news1.attglobal.net> <3B0D7F1D.1AC7CCD0@ont.com> <LpfP6.60410$T7.4978549@bin1.nnrp.aus1.giganews.com> <3B0E579F.45877D70@brazee.net> <OVAP6.696$NK4.121624@news2.aus1.giganews.com>`

```
Jerry P wrote:
> 
> "Howard Brazee" <howard@brazee.net>
…[14 more quoted lines elided]…
> With my plan they'd have Java but  wouldn't NEED any Java programmers!

The bottom line is that they probably wanted to get rid of the COBOL
programming/programmers. Using PERcobol would result in JAVA running,
but it wouldn't be native JAVA, because everything written does go 
through the run-time. They could SELL a JAVA-to-COBOL-run-time interface 
manual I guess...


Gary
```

##### ↳ ↳ Re: Reverse Engineering Cobol Apps

- **From:** "Charles F. Townsend" <ctowns@ix.netcom.com>
- **Date:** 2001-05-29T08:08:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B13BB68.88C2A241@ix.netcom.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <3b0c92ca.5476205@news1.attglobal.net>`

```
Thane,
Actually, LegacyJ PERCobol currently allows the user to see the
"intermediate" .java but the executable .class file is the generated result
of the compile.  PERCobol runtimes permit the executables to continue to
perform or behave as a COBOL including and will reading and writing COBOL
files.  LegacyJ has spent some time thinking about deploying extensive
runtime libraries with individual applications and determined that COBOL
programmers needed a way to "deploy" only those runtime elements that are
needed by the COBOL program.  Now we include with PERCobol on all graphical
platforms a graphical deploy tool that creates and executable .jar file
containing the application, runtime and other program elements necessary
for program execution.

The PERCobol COBOL Language manuals are available with the product or
viewed from the LegacyJ website at http://www.legacyj.com/perc_doc.html

Charles Townsend
LegacyJ
http://www.legacyj.com

Thane Hubbell wrote:

> Another suggestion - go to http://www.legacyj.com and just recompile
> the program and get a .java file out of it.
…[21 more quoted lines elided]…
> >-Dr. Jones
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** Bob Reeves <theOrcas@worldnet.att.net>
- **Date:** 2001-05-24T14:59:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0D2156.65D1@worldnet.att.net>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
Steve Jones wrote:
> 
> We have a Cobol application that will be rewritten in Java ... be this
…[16 more quoted lines elided]…
> -Dr. Jones

Try PowerStructure for COBOL. It automatically generates structure charts 
of COBOL source. I think they are at www.usflowchart.com

Bobby
```

##### ↳ ↳ Re: Reverse Engineering Cobol Apps

- **From:** gary drummond <gdrumm@ont.com>
- **Date:** 2001-05-24T20:21:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0DCFC1.690C5BAF@ont.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <3B0D2156.65D1@worldnet.att.net>`

```
Bob Reeves wrote:
> 
> Steve Jones wrote:
…[23 more quoted lines elided]…
> Bobby

Nice pictures. It would be nice to use something that tells me I went
off into the wrong procedures. I've done that many times, and STILL
can't read my own printing...

The price is nice for a tool like that (OK, for me it is!).

Gary
```

#### ↳ Re: Reverse Engineering Cobol Apps

- **From:** merhottin@aol.com (Merhottin)
- **Date:** 2001-05-25T02:06:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010524220609.00603.00001124@ng-fr1.aol.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com>`

```
Hi Steve,

     I work in a COBOL Shop, and we outsourced our web development, and werent
very happy with it. (was written in Java)   We found some software out there
that allowed us to "web enable" or "internet enable" our COBOL programs.
     We are using Fujitsu 5.0 (32 bit compiler) , Flexus SP2 (screen drivers),
and Flexus Thin Client.  
    We waited a year for the web company to deliver our web site, and it really
sucked wind to put it nicely.  We had our cobol program up and running in under
2 months.  If you are a COBOL shop, it is definatly the way to go.  We are very
very excited about it.  check out www.Flexus.com & read up on it.  
     They offer a demo version (intact), and full support during demo.  They
always responded within an hour or 2.
     Java is not meant for business applications, we had a ton of problems with
our relative simple program.  Any questions feel free to ask. but again, Flexus
offers full support, and they are more then happy to help.  

John
```

##### ↳ ↳ Re: Reverse Engineering Cobol Apps

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-05-25T03:26:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0DD14D.96BC7885@home.com>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <20010524220609.00603.00001124@ng-fr1.aol.com>`

```


Merhottin wrote:

> Hi Steve,
>
…[15 more quoted lines elided]…
> John

Well Bob,

Another glowing recommendation. You should be easy to spot at CW2001 - the one with
the BIG HEAD and wearing glasses <G> Just in case I have difficulty, to draw
attention, make sure you wave a fireman's spanner around <G>

Jimmy
```

##### ↳ ↳ Re: Reverse Engineering Cobol Apps

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-05-25T07:02:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B0E5801.AC0E32DA@brazee.net>`
- **References:** `<f2b3dd25.0105231109.6d1b6ec@posting.google.com> <20010524220609.00603.00001124@ng-fr1.aol.com>`

```
http://www.computerworld.com/cwi/story/0,1199,NAV47_STO60683,00.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
