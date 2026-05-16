[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help in Realia Classroom Cobol Compiler

_17 messages · 8 participants · 1999-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help in Realia Classroom Cobol Compiler

- **From:** "Norman Leach" <norlea@anson-industries.com>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ou0V2.167$J73.11252@news.ntr.net>`

```
Hello all,
    I am working on a project for my second semester COBOL class which
involves subprograms and indexed files and all the fun stuff!  Anyway,
programs work fine but now I am trying to spruce things up a little by
activating the F1 key for help.  I already asked my instructor and he's not
sure what I'm doing incorrectly so thought I would try here.
I got it to work correctly in MicroFocus COBOL by using the
                    call x"af" using......     line
and defining everything in working storage.

However, when I try the same call in Realia COBOL the subprogram compiles
correctly but upon linking i get "Error 37: Symbol Undefined >>"  anyone
have any ideas?
I can't just use MF COBOL for this project because our student version won't
create an executable.  I would be happy to send my code to anyone who would
be willing to help.  Thanks.

Norman Leach
norlea@anson-industries.com
```

#### ↳ Re: Help in Realia Classroom Cobol Compiler

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7g2eji$mg0@dfw-ixnews10.ix.netcom.com>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net>`

```
Unfortunately, there is NO (currently) PORTABLE screen/function-key
interface in COBOL.  What works in Micro Focus may or not work in CA-Realia
which may or may not work in Fujitsu which probably WON'T work with any
mainframe (IBM, UNISYS, TANDEM) implementation.

The next Standard provides a "character based" interface (no GUI) which is
based on (but not identical to) the existing X/Open COBOL definition.

Bottom-Line:
  Today if you want to use "F1" to do something, you will need to modify  it
for the compiler or run-time you are using.  (This is an EXCELLENT example
of where using a called sub-routine can be used to "isolate" operating
system specific code.)

Note: You may see responses to this thread that mention Flexus or other
PORTABLE 3rd party products. This is another way that you could go in the
"real world" - but I doubt is what you want for a school assignment.
```

##### ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7g2n73$bmi$1@news.cerf.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com>`

```
William M. Klein wrote in message <7g2eji$mg0@dfw-ixnews10.ix.netcom.com>...
>Unfortunately, there is NO (currently) PORTABLE screen/function-key
>interface in COBOL.  What works in Micro Focus may or not work in CA-Realia
>which may or may not work in Fujitsu which probably WON'T work with any
>mainframe (IBM, UNISYS, TANDEM) implementation.

Not quite so, with Acucobol you may configure the keyboard to behave the way
you like it, you could for instance make an input terminate when pressing Y
and let the enter key add an Y...

Cheesle
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3725b702.3959884@news.enter.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <7g2n73$bmi$1@news.cerf.net>`

```
"Cheesle" <cheesle@online.NoSpamPlease.no> wrote:

>William M. Klein wrote in message <7g2eji$mg0@dfw-ixnews10.ix.netcom.com>...
>>Unfortunately, there is NO (currently) PORTABLE screen/function-key
…[10 more quoted lines elided]…
>

Cheesle...

I think that Bill's original statement was correct.  You mention an
Acucobol specific feature and he is saying "what works in one compiler
may or may not in another."  I believe that he was referring to cross
compiler portability.

As far as machine and operating system portability goes....I don't
know of anything which is truly 100% portable.  Acucobol may indeed be
portable across a wide variety of machines and operating systems, but
if you re-read Bill's comment, he also mentions mainframe systems.

I am not aware of any recent developments, but as far as I know,
Acucobol and Fujitsu COBOL have not yet been ported to run under
DOS/VSE or MVS.



Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-PtOtgpCs9dyS@Dwight_Miller.iix.com>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <7g2n73$bmi$1@news.cerf.net> <3725b702.3959884@news.enter.net>`

```
On Tue, 27 Apr 1999 13:15:58, rtwolfe@flexus.com (Bob Wolfe) wrote:
> I am not aware of any recent developments, but as far as I know,
> Acucobol and Fujitsu COBOL have not yet been ported to run under
> DOS/VSE or MVS.
>

AFAIK - Fujitsu DOES offer an MVS COBOL compiler - but I've never seen
it used in the US.

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

_(reply depth: 5)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37260569.24034343@news.enter.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <7g2n73$bmi$1@news.cerf.net> <3725b702.3959884@news.enter.net> <Jl0PnHJ5PvPd-pn2-PtOtgpCs9dyS@Dwight_Miller.iix.com>`

```
redsky@ibm.net (Thane Hubbell) wrote:

>On Tue, 27 Apr 1999 13:15:58, rtwolfe@flexus.com (Bob Wolfe) wrote:
>> I am not aware of any recent developments, but as far as I know,
…[6 more quoted lines elided]…
>

Thane:

But in order to offer cross platform portability, the same source
program must be able to be compiled in either compiler and run in the
appropriate target environment.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7g4ipk$13b$1@news.cerf.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <7g2n73$bmi$1@news.cerf.net> <3725b702.3959884@news.enter.net>`

```
Bob Wolfe wrote in message <3725b702.3959884@news.enter.net>...
>I think that Bill's original statement was correct.  You mention an
>Acucobol specific feature and he is saying "what works in one compiler
>may or may not in another."  I believe that he was referring to cross
>compiler portability.

I see, I thought he ment that the keystroke testing in itself was not
portable, in the sense of being a part of the ANSI Cobol definition, that is
correct.

>if you re-read Bill's comment, he also mentions mainframe systems.

That is correct, I have never been working on mainframes, so for me, it is
something heard of, but never seen :-)

>I am not aware of any recent developments, but as far as I know,
>Acucobol and Fujitsu COBOL have not yet been ported to run under
>DOS/VSE or MVS.

For Acucobol I believe that is true.

Isn't mainframes dying as application servers, becoming more like file
servers? (No hate please, this is an honest question, no statement!)

Cheesle
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3725E37F.865B9EE7@NOSPAMhome.com>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <7g2n73$bmi$1@news.cerf.net> <3725b702.3959884@news.enter.net> <7g4ipk$13b$1@news.cerf.net>`

```
> Isn't mainframes dying as application servers, becoming more like file
> servers? (No hate please, this is an honest question, no statement!)

They were, but big iron is selling better than ever as we cram more and
more data in our information systems.  High volume and high security
demand the attributes which make mainframes cost effective.

The company which sold more new databases than Oracle is the same one
which lost a billion dollars in its PC business last year.  IBM made
lots of money selling big iron and big systems.  It's also making a big
iron Virtual Java Machine for high volume internet servers.

Meanwhile Unix machines are growing.  Nowadays many computer rooms in
large organizations have two or more plain boxes hidden away between all
of the peripherals.   One box is the mainframe, one is the Unix
machine.  It's getting hard to tell them apart by looking at them or by
looking at what they do.

And really, the difference between application servers and file servers
is getting blurry.   Java has objects which are half on a server and
half on a terminal (actually, often parts are somewhere in between!).  
A Web page may be connected to a database which is getting updated
currently.   Certainly E-commerce works much better if your purchase of
a whatzit marks it as sold so that I can't buy it a second later.

Data warehouses are certainly applications, and people are cramming more
and more data in them.
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

_(reply depth: 6)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7g549o$6oe$1@news.cerf.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <7g2n73$bmi$1@news.cerf.net> <3725b702.3959884@news.enter.net> <7g4ipk$13b$1@news.cerf.net> <3725E37F.865B9EE7@NOSPAMhome.com>`

```
Howard Brazee wrote in message <3725E37F.865B9EE7@NOSPAMhome.com>...
>> Isn't mainframes dying as application servers, becoming more like file
>> servers? (No hate please, this is an honest question, no statement!)
>
>They were, but big iron is selling better than ever as we cram more and

Thank you for thoroughly information!

Cheesle
```

##### ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

- **From:** "Norman Leach" <norlea@anson-industries.com>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8Z3V2.170$J73.12219@news.ntr.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com>`

```
>Bottom-Line:
>  Today if you want to use "F1" to do something, you will need to modify
it
>for the compiler or run-time you are using.  (This is an EXCELLENT example
>of where using a called sub-routine can be used to "isolate" operating
>system specific code.)


exactly...now my question is.....does anyone know the syntax for getting F1
(or any function key) to work in Realia COBOL?

norm
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

- **From:** "Norman Leach" <norlea@anson-industries.com>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B34V2.171$J73.12239@news.ntr.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <8Z3V2.170$J73.12219@news.ntr.net>`

```
just realized that may have sounded like i didn't appreciate the feedback
(which i did very much) sorry if it didn't come across in my message!

norm
Norman Leach wrote in message <8Z3V2.170$J73.12219@news.ntr.net>...
>>Bottom-Line:
>>  Today if you want to use "F1" to do something, you will need to modify
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3724ecfa@news3.us.ibm.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <8Z3V2.170$J73.12219@news.ntr.net> <B34V2.171$J73.12239@news.ntr.net>`

```
01  KBD-DATA-VAL              VALUE +0  PIC S9(4) COMP-5.
01  FILLER REDEFINES KBD-DATA-VAL.
      02  KBD-DATA-CHAR    PIC X.
      02  FILLER                        PIC X.

....


CALL "DOS_READ_KBD" USING KBD-DATA-VAL         (or DOS-READ-KBD)

This function reads the next character from the keyboard. For a graphic or
control key, the value transferred is the std ASCII code. For a function
key,
the key value is transferred as two separate characters. The first one is
zero
(low-values). The second byte (call the function again) returns a value as
follows:

15 shift tab
16-25 alt-Q,W,E,R,T,Y,U,I,O,P
30-38 alt-A,S,D,F,GF,H,I,J,K,L
44-50 alt-Z,X,C,V,B,N,M
59-68 F1 thru F10
71 home
72 cursor up
73 pgup
75 cursor left
77 cursor right
79 end
80 cursor down
81 pgdn
82 ins
83 del
84-93 shift F1 thru F10
94-103 ctrl F1 thru F10
104-113 alt-F1 thru F10
115 ctrl-cursor left
116 ctrl-cursor right
117 ctrl-emd
119 ctrl-pgdn
132 ctrl-pgup

.171$J73.12239@news.ntr.net...
> just realized that may have sounded like i didn't appreciate the feedback
> (which i did very much) sorry if it didn't come across in my message!
…[6 more quoted lines elided]…
> >>for the compiler or run-time you are using.  (This is an EXCELLENT
example
> >>of where using a called sub-routine can be used to "isolate" operating
> >>system specific code.)
> >
> >
> >exactly...now my question is.....does anyone know the syntax for getting
F1
> >(or any function key) to work in Realia COBOL?
> >
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3724f103.109598742@news1.ibm.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <8Z3V2.170$J73.12219@news.ntr.net> <B34V2.171$J73.12239@news.ntr.net>`

```
On Mon, 26 Apr 1999 16:23:17 -0400, "Norman Leach"
<norlea@anson-industries.com> wrote:

>just realized that may have sounded like i didn't appreciate the feedback
>(which i did very much) sorry if it didn't come across in my message!
>
>norm

Leif posted the call I was looking for.  However, if you are using a
Screen Section, or want to find out the key that terminates an accept
you can use the following:

Declare in special names:

 Environment Division.
 Configuration Section.
 Special-Names.
     Crt Status is Keyboard-Status.

Then define Keyboard-Status in Working Storage as:

 01  Keyboard-Status.
       03  Accept-Status Pic 9.
       03  System-Use    Pic X.
       03  Function-Key  Pic X.
             88  F1-Pressed Value X"3B".
             88  F2-Pressed Value X"3C".
             88  F3-Pressed Value X"3D".
             88  F4-Pressed Value X"3E".
             88  F5-Pressed Value X"3F".

After the accept you can use the 88 level test to determine which key
was  pressed.
```

##### ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-mTb2PyjuYbuB@Dwight_Miller.iix.com>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com>`

```
On Mon, 26 Apr 1999 19:23:31, "William M. Klein" 
<wmklein@nospam.netcom.com> wrote:
> Note: You may see responses to this thread that mention Flexus or other
> PORTABLE 3rd party products. This is another way that you could go in the
> "real world" - but I doubt is what you want for a school assignment.

I'm going to e-mail Norman when I get home with the Realia solution.  
While MF uses X"AF", Realia uses a different call.  I just can't 
remember it, but it's at home in the manual.
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

- **From:** Jeffrey Friedman <jfriedm@ibm.net>
- **Date:** 1999-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3724F2E6.AD4F0A62@ibm.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-mTb2PyjuYbuB@Dwight_Miller.iix.com>`

```
The predefined FIELD-TERMINATOR special register is set to indicate which
function key (if any) terminated the ACCEPT.

Thane Hubbell wrote:

> On Mon, 26 Apr 1999 19:23:31, "William M. Klein"
> <wmklein@nospam.netcom.com> wrote:
…[6 more quoted lines elided]…
> remember it, but it's at home in the manual.
```

###### ↳ ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3725ae34.158039167@news1.ibm.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com> <Jl0PnHJ5PvPd-pn2-mTb2PyjuYbuB@Dwight_Miller.iix.com> <3724F2E6.AD4F0A62@ibm.net>`

```
On Mon, 26 Apr 1999 19:12:38 -0400, Jeffrey Friedman <jfriedm@ibm.net>
wrote:

>The predefined FIELD-TERMINATOR special register is set to indicate which
>function key (if any) terminated the ACCEPT.

Forgot about that.  Virtually all of my DOS Realia used Screenio - the
only reason I knew about the Special-Names and Screen section method
is that I ported some of the code examples in my book to Realia, just
in case someone asked me how to perform them with Realia!
```

##### ↳ ↳ Re: Help in Realia Classroom Cobol Compiler

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3725b4cb.3393313@news.enter.net>`
- **References:** `<ou0V2.167$J73.11252@news.ntr.net> <7g2eji$mg0@dfw-ixnews10.ix.netcom.com>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote:

>Unfortunately, there is NO (currently) PORTABLE screen/function-key
>interface in COBOL.  What works in Micro Focus may or not work in CA-Realia
…[10 more quoted lines elided]…
>system specific code.)

Bill:

Called subroutines can also allow you to avoid compiler specific
extensions so that your code is much more portable across all of the
COBOL compilers.

>Note: You may see responses to this thread that mention Flexus or other
>PORTABLE 3rd party products. This is another way that you could go in the
>"real world" - but I doubt is what you want for a school assignment.

I agree.  If a professor saw a "called" commercial dynamic link
library or executable to perform some program function, I think that
the student would be asked to explain what it is and why it was used.


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
