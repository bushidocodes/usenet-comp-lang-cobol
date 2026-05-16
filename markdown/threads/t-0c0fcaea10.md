[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO COBOL using Fujitsu 4.0

_9 messages · 7 participants · 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Object-oriented COBOL`](../topics.md#oo)

---

### OO COBOL using Fujitsu 4.0

- **From:** Floyd Johnson <floydj@worf.netins.net>
- **Date:** 1999-09-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37D3E77B.A739FE0E@worf.netins.net>`

```
Can anybody verify that parameter passing is only by
reference when invoking a method in Fujitsu's brand of OO
COBOL.  The general information I have (and the new
standard, if I am reading it correctly) specify that
parameters can be passed BY CONTENT or BY VALUE.  It appears
that Fujitsu has not implemented these options.

The following statement (forgive the application - it is a
demonstration for a programming language class that required
a common problem for a number of languages)

     invoke self "calculate-gcd" using by value u v 
                                          returning result

returns an error indicating that the "BY VALUE" is not
valid.  The help files indicate that the BY VALUE class is
not available when invoking a method.

Am I missing something?  Thanks for any help.
```

#### ↳ Re: OO COBOL using Fujitsu 4.0

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37d4861f.37068334@news1.ibm.net>`
- **References:** `<37D3E77B.A739FE0E@worf.netins.net>`

```
On Mon, 06 Sep 1999 12:10:35 -0400, Floyd Johnson
<floydj@worf.netins.net> wrote:

>Can anybody verify that parameter passing is only by
>reference when invoking a method in Fujitsu's brand of OO
…[4 more quoted lines elided]…
>

I can't speak to "INVOKE" but I do know that regular "CALL" statements
allow by value, and by reference.
```

#### ↳ Re: OO COBOL using Fujitsu 4.0

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bef8d7$0dbb7a40$1cf0abc3@default>`
- **References:** `<37D3E77B.A739FE0E@worf.netins.net>`

```


Floyd Johnson <floydj@worf.netins.net> wrote in article
<37D3E77B.A739FE0E@worf.netins.net>...
> Can anybody verify that parameter passing is only by
> reference when invoking a method in Fujitsu's brand of OO
…[16 more quoted lines elided]…
> Am I missing something?  Thanks for any help.


Floyd,

This just sucks man, not even being able to execute that statement.
Sorry, I dont have a solution for you but I will tell you to use Micro
Focus
OO Cobol, in my experience, Micro Focus handles it best, and it has'nt
got the dreaded RAD concepts, so you know whats going on 100% of the
time.

Simon R Hart
Eaton.
```

##### ↳ ↳ Re: OO COBOL using Fujitsu 4.0

- **From:** ENOJON <enojon@delphi.com>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37E693DC.5F86C26A@delphi.com>`
- **References:** `<37D3E77B.A739FE0E@worf.netins.net> <01bef8d7$0dbb7a40$1cf0abc3@default>`

```


Simon R Hart wrote:

> Floyd Johnson <floydj@worf.netins.net> wrote in article
> <37D3E77B.A739FE0E@worf.netins.net>...
…[18 more quoted lines elided]…
> > Am I missing something?  Thanks for any help.

INVOKE <object-ptr>"calculate-gcd" USING u v
                                              BY VALUE
                                              RETURNING result

always works for me in Fj OOCobol.

It's basic A-B-C's of invoking a CALL statement where
the qualifying BY REF, BY VAL, or BY CONT *follows*
the variables passed.
```

###### ↳ ↳ ↳ Re: OO COBOL using Fujitsu 4.0

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf03f9$784b3d00$e4cbac3e@default>`
- **References:** `<37D3E77B.A739FE0E@worf.netins.net> <01bef8d7$0dbb7a40$1cf0abc3@default> <37E693DC.5F86C26A@delphi.com>`

```


ENOJON <enojon@delphi.com> wrote in article
<37E693DC.5F86C26A@delphi.com>...
> 
> 
…[32 more quoted lines elided]…
> the variables passed.
 
Why?, this is a strange method of programming using OO constructs.
This is unnessary using MF, "BY VALUE" is optional, but this
is placed *before* the varibles as it should.

Simon R Hart
Eaton.
```

###### ↳ ↳ ↳ Re: OO COBOL using Fujitsu 4.0

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37E6F0F2.666B4387@home.com>`
- **References:** `<37D3E77B.A739FE0E@worf.netins.net> <01bef8d7$0dbb7a40$1cf0abc3@default> <37E693DC.5F86C26A@delphi.com>`

```
ENOJON wrote:
> 
> Simon R Hart wrote:
…[9 more quoted lines elided]…
> > >

I don't know how Simon does his, but programming purely in OO using
NetExpress I use only the following syntax :-

 01 textstring			pic x(30).
 01 numvalue			pic x(4) comp-5  (could be comp-3 etc..)
 01 anObject		        object reference.

 01 ls-values.
    05 newtext			pic x(12).
    05 newnumber		pic x(4) comp-5 (could be comp-3 etc..)
    05 newObject		object reference.

 invoke MyClass "mymethod" using textstring
		                 numvalue
			         anObject
			   returning ls-values.

I haven't as yet found any need to use 'by reference', 'by value' etc...
Probably same applies with Fujitsu - DON'T make sending and receiving
fields the same, ie 'using x returning x' gives you problems in
NetExpress.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: OO COBOL using Fujitsu 4.0

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s72dc$akl@dfw-ixnews3.ix.netcom.com>`
- **References:** `<37D3E77B.A739FE0E@worf.netins.net> <01bef8d7$0dbb7a40$1cf0abc3@default> <37E693DC.5F86C26A@delphi.com> <37E6F0F2.666B4387@home.com>`

```
James J. Gavan <jjgavan@home.com> wrote in message
  <snip>
>
> I don't know how Simon does his, but programming purely in OO using
…[21 more quoted lines elided]…
> Jimmy, Calgary AB

OK - it's "philosophy" time.  I think that there is definitely a reason to
use BY CONTENT (in both INVOKE and CALL statements).  If (and this is an
"if") you believe in "encapsulation," using BY CONTENT guarantees that your
invoked/called method/program canNOT "play" with your program's data.  I
think that the only time data should be passed to a subprogram or method "by
reference" (which is the default) is IF you want to have that program modify
your invoking/calling program's data.  With the CALL statement, I think that
the "mindset" of COBOL programmers is that the subprogram can (and often
will) change anything it can get its hands (i.e pointers) on.  ON THE OTHER
HAND, when it comes to NEW methods, I really do think that they should be
"designed" NOT to play with the invoking program's data - but to "return"
data for use in the outside program.

As for BY VALUE - there are two issues here.  First, there MAY (depending
upon implementation) be performance advantages for doing this.  Second (and
I think more prevalent), the method (or even called subprogram) may be a
NON-COBOL program that is expecting data "on the stack" as BY VALUE does it.
For that matter, if you are writing your own method and expecting it to be
invoked by non-COBOL programs, you may well want to program for BY VALUE
arguments coming in.

All of this does boil down to the fact that doing everything BY REFERENCE
(explicit or implicit) probably will work - but may not be the best design
decision (IMHO).
```

###### ↳ ↳ ↳ Re: OO COBOL using Fujitsu 4.0

_(reply depth: 5)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990921133154.06411.00000275@ngol07.aol.com>`
- **References:** `<7s72dc$akl@dfw-ixnews3.ix.netcom.com>`

```
In article <7s72dc$akl@dfw-ixnews3.ix.netcom.com>, "William M. Klein"
<wmklein@nospam.netcom.com> writes:

>
>All of this does boil down to the fact that doing everything BY REFERENCE
>(explicit or implicit) probably will work - but may not be the best design
>decision (IMHO).
>

I would think that using BY REFERENCE also limits the amount of physical 
data that has to be passed, making runtime more efficient.
In my particular case, I have to be able to get access to a record area that
could vary from 450 to 8000 bytes.  My sub-program is using BY REFERENCE
on the record area and BY CONTENT on a RecordSize parameter to prevent
data overrun situations in the sub-program.   Currently the plan is for this
action
to operate on 1% of a program's data.   Ultimately, I hope to have procedures 
in place for the sub-program to 'see' 100% of the records passing thru the 
Main program.
```

###### ↳ ↳ ↳ Re: OO COBOL using Fujitsu 4.0

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37E7E465.A0ECBA0@home.com>`
- **References:** `<7s72dc$akl@dfw-ixnews3.ix.netcom.com> <19990921133154.06411.00000275@ngol07.aol.com>`

```
Sff5ky wrote:
> 
> In article <7s72dc$akl@dfw-ixnews3.ix.netcom.com>, "William M. Klein"
…[17 more quoted lines elided]…
> Main program.

I think I'm correct in saying the same problem doesn't prevail with
NetExpress - your table handling problem can be covered by creating
either a variable length collection or dictionary, (its size is
determined by ' invoke MyCollection "size" returning ws-size'), and it
is merely the object reference handle which is passed. If you're getting
really interested in OO - take a look at Adele Goldberg's Smalltalk-80
which neatly describes the structure of collections/dictionaries, and
how you can apply them. 

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
