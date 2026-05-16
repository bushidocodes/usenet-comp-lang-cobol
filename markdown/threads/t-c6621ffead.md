[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Split output

_57 messages · 17 participants · 2000-04 → 2000-05_

---

### Split output

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39073291.2953296B@cusys.edu>`

```
This is an operating system issue, not a programming language issue -
but I sure wish I could point the output of a program to multiple
locations at once.  Maybe have my DISPLAY go to SYSOUT and to a file
simultaneously.
```

#### ↳ Re: Split output

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3907397e_2@news1.prserv.net>`
- **References:** `<39073291.2953296B@cusys.edu>`

```
Are you using Micro Focus Cobol?  If so, then you can.  You will have to
write an external File Handler routine to do it, but it can be done.

TL

Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:39073291.2953296B@cusys.edu...
> This is an operating system issue, not a programming language issue -
> but I sure wish I could point the output of a program to multiple
> locations at once.  Maybe have my DISPLAY go to SYSOUT and to a file
> simultaneously.
```

##### ↳ ↳ Re: Split output

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39073FA3.818E6FC5@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <3907397e_2@news1.prserv.net>`

```
MVS

"Lucas, Todd" wrote:
> 
> Are you using Micro Focus Cobol?  If so, then you can.  You will have to
…[9 more quoted lines elided]…
> > simultaneously.
```

###### ↳ ↳ ↳ Re: Split output

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcufgscm07j6h2680qv3r7f3l5qqqb00bn@4ax.com>`
- **References:** `<39073291.2953296B@cusys.edu> <3907397e_2@news1.prserv.net> <39073FA3.818E6FC5@cusys.edu>`

```
On Wed, 26 Apr 2000 13:12:35 -0600 Howard Brazee <howard.brazee@cusys.edu>
wrote:

:>MVS

:>"Lucas, Todd" wrote:
 
:>> Are you using Micro Focus Cobol?  If so, then you can.  You will have to
:>> write an external File Handler routine to do it, but it can be done.
 
:>> TL
 
:>> Howard Brazee <howard.brazee@cusys.edu> wrote in message
:>> news:39073291.2953296B@cusys.edu...

:>> > This is an operating system issue, not a programming language issue -
:>> > but I sure wish I could point the output of a program to multiple
:>> > locations at once.  Maybe have my DISPLAY go to SYSOUT and to a file
:>> > simultaneously.

If you don't want to (or can't) change the source program you can have your
friendly systems programmer write an SSI routine to do it.

PIPEs or SmartBatch may be able to do it as well.
```

#### ↳ Re: Split output

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e7e4p$j6g$1@slb6.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu>`

```
If you are talking about OS/390, then I believe there are ways to handle this
via JCL.  (Certainly you CAN send the output to a file and spool that to a
printer via IEBGENER in a subsequent step.)
```

##### ↳ ↳ Re: Split output

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39074022.7E99A597@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> If you are talking about OS/390, then I believe there are ways to handle this
> via JCL.  (Certainly you CAN send the output to a file and spool that to a
> printer via IEBGENER in a subsequent step.)

I am.  I noticed this need when I had to create a file to duplicate my
display.  I did a write to a file and a display to sysout - so that I
could go into SYSD and monitor my progress.  Once I got sufficient debug
lines, I could kill my long running job.  A subsequent step won't do it.
```

###### ↳ ↳ ↳ Re: Split output

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e7grf$hhb$1@slb6.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu>`

```
I have never used it, but have you looked at the OUTDISP parameter? Might
this give you what you are looking for (assuming JES2, not JES3).  See

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IEA1B510/5%2e5%2e6%2e2
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 4)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39075165.399488BA@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <8e7grf$hhb$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> I have never used it, but have you looked at the OUTDISP parameter? Might
> this give you what you are looking for (assuming JES2, not JES3).  See
> 
> http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IEA1B510/5%2e5%2e6%2e2

This looks useful, but not for what I want, unless I can convert from
SYSOUT=* to SYSOUT=FILE.NAME,DISP=(NEW,CATLG,DELETE),SPACE=...

Interesting, looking at your link I found the following:
        //ddname  DD  SYSOUT=class 

        //name    OUTPUT CLASS=class 
        //ddname  DD     SYSOUT=(,),OUTPUT=*.name 

        //name    OUTPUT DEFAULT=YES,CLASS=class 
        //ddname  DD     SYSOUT=(,) 

What in the world is *.name?


 
> --
> Bill Klein
…[16 more quoted lines elided]…
> > lines, I could kill my long running job.  A subsequent step won't do it.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9LN4.18480$0o4.137675@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39074022.7E99A597@cusys.edu> <8e7grf$hhb$1@slb6.atl.mindspring.net> <39075165.399488BA@cusys.edu>`

```
In article <39075165.399488BA@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, to, Howard, Brazee, post,
 	them!!> wrote:
>
>
…[19 more quoted lines elided]…
>What in the world is *.name?

Hmmmmmm... smells like referback, Kemo Sabe.

DD
```

###### ↳ ↳ ↳ Re: Split output - BatchPipeWorks ?

_(reply depth: 5)_

- **From:** Jonathan Nash <jnash@qis.net>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.GSO.3.96.1000426230122.1779A-100000@eclipse>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <8e7grf$hhb$1@slb6.atl.mindspring.net> <39075165.399488BA@cusys.edu>`

```
Could BatchPipeWorks be used for something like this ?
```

###### ↳ ↳ ↳ Re: Split output - BatchPipeWorks ?

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e8g6g$afg$1@slb1.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <8e7grf$hhb$1@slb6.atl.mindspring.net> <39075165.399488BA@cusys.edu> <Pine.GSO.3.96.1000426230122.1779A-100000@eclipse>`

```
I don't think so.  Batch pipes lets you send output from one job to another -
before the 1st job finishes.  I don't think that is what Howard was looking
for.
```

###### ↳ ↳ ↳ Re: Split output - BatchPipeWorks ?

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39082DD8.36AD9911@zip.com.au>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <8e7grf$hhb$1@slb6.atl.mindspring.net> <39075165.399488BA@cusys.edu> <Pine.GSO.3.96.1000426230122.1779A-100000@eclipse> <8e8g6g$afg$1@slb1.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> I don't think so.  Batch pipes lets you send output from one job to
> another - before the 1st job finishes.  I don't think that is what
> Howard was looking for.

> "Jonathan Nash" <jnash@qis.net> wrote in message
> > Could BatchPipeWorks be used for something like this ?

You could write the equivalent of Unix 'tee' which copies the output
to console and passes it to the next program in the pipe.

program 1  |  tee  |  program 2

tee would dump the output of program 1 and program 2 would also get
the output.  Sledgehammer to crack a nut, but it would work.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 5)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000427000331.12346.00001241@nso-fc.aol.com>`
- **References:** `<39075165.399488BA@cusys.edu>`

```
In article <39075165.399488BA@cusys.edu>, Howard Brazee
<howard.brazee@cusys.edu> writes:

>
>        //name    OUTPUT CLASS=class 
…[8 more quoted lines elided]…
> 

Wouldn't this be the JCL Referback to the OUTPUT profile 'name'?
```

###### ↳ ↳ ↳ Re: Split output

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y7LN4.18478$0o4.137619@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu>`

```
In article <39074022.7E99A597@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, to, Howard, Brazee, post,
 	them!!> wrote:
>
>
…[9 more quoted lines elided]…
>lines, I could kill my long running job.  A subsequent step won't do it.

Golly... wasn't the ready availability of COBTEST supposed to make such
things unnecessary?

DD
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 4)_

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#5Uct2#r$GA.351@cpmsnbbsa04>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <y7LN4.18478$0o4.137619@iad-read.news.verio.net>`

```
<docdwarf@clark.net> wrote in message
news:y7LN4.18478$0o4.137619@iad-read.news.verio.net...
> In article <39074022.7E99A597@cusys.edu>,
> Howard Brazee  <Please, do, not, e-mail, replies, to, Howard, Brazee,
post,
>   them!!> wrote:
> >
…[3 more quoted lines elided]…
> >> If you are talking about OS/390, then I believe there are ways to
handle this
> >> via JCL.  (Certainly you CAN send the output to a file and spool that
to a
> >> printer via IEBGENER in a subsequent step.)
> >
…[6 more quoted lines elided]…
> things unnecessary?

Don't the local sysprogs have to install COBTEST?  I know it wasn't
installed at all at a former site I worked at; though they had Xpediter to
make up for it.

>
> DD
>
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e885b$saa$1@slb3.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <y7LN4.18478$0o4.137619@iad-read.news.verio.net> <#5Uct2#r$GA.351@cpmsnbbsa04>`

```
"ChrisOsborne" <chris_n_osborne@yahoo.com> wrote in message it.
> >
> > Golly... wasn't the ready availability of COBTEST supposed to make such
…[5 more quoted lines elided]…
>

Bits and pieces of "information"

COBTEST was the VS COBOL II debugger - the current "debugger" is called "The
Debug Tool" - and it works for ALL the LE-enabled languages.  (It DOES also
support debugging of VS COBOL II programs in a COBOL for this-and-that
applications.)

The Debug Tool is a "freebie" (unlike earlier IBM "add-ons") - so if your
site has LE, it has the Debug Tool.

Yes, your systems programmers need to "install" it, but it is actually easier
to install it than to avoid it.  Often it is installed in shops - that don't
even know that it is there.

The original question about viewing output as a "debugging" option, is really
independent of COBTEST vs Debug Tool vs Xpediter vs SmarTest vs whatever.
Any one of those debugging programs SHOULD provide you an "option" that (I
would think) would be better than trying to monitor an output file.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39084D30.2B83B434@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <y7LN4.18478$0o4.137619@iad-read.news.verio.net> <#5Uct2#r$GA.351@cpmsnbbsa04>`

```
ChrisOsborne wrote:
> 
> Don't the local sysprogs have to install COBTEST?  I know it wasn't
> installed at all at a former site I worked at; though they had Xpediter to
> make up for it.

To tell the truth, I don't know.  I have never worked at a place where
anybody used debugger tools to follow what a batch program does - at
least past a bit of playing around.  In this case, the volume of data is
such that I simply want to browse through the building output until I
found interesting data.  This might be a hundred thousand records in,
before I killed the process.  I guess we're too lazy to take the time
and effort to use those tools when we can do displays exactly where we
want and get our debugging out of the way quickly and easily.  On the
other hand, it doesn't mean we have less work to do - by finishing up
quickly we just get handed new work.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e9jl1$d55$1@slb0.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <y7LN4.18478$0o4.137619@iad-read.news.verio.net> <#5Uct2#r$GA.351@cpmsnbbsa04> <39084D30.2B83B434@cusys.edu>`

```
Just FYI,
  All of the debuggers have a method to put a "break point" in a debugging
session when a data-item (such as a record description) has a specific value.
You then "run" the program to that break point.  Several of them (I believe)
even have a method of asking (in advance) for "backtrack" capability.  This
would allow you to "run" to the record in question - and "backtrack" to look
at what happened with the previous record.

FYI-2,
  From my days of working for both Micro Focus *and* ADS (the then vendor of
Xpediter), it is truly remarkable how many shops pay for
debugging/development tools but don't provide the time and resources for
their programmers to actually learn how and when to use them.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 7)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39085AD1.8D5656AA@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <8e7e4p$j6g$1@slb6.atl.mindspring.net> <39074022.7E99A597@cusys.edu> <y7LN4.18478$0o4.137619@iad-read.news.verio.net> <#5Uct2#r$GA.351@cpmsnbbsa04> <39084D30.2B83B434@cusys.edu> <8e9jl1$d55$1@slb0.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Just FYI,
…[5 more quoted lines elided]…
> at what happened with the previous record.

If you know what you're looking for, this would be almost as easy as
putting in a display, and that backtracking ability could possibly be
useful.  If you are simply putting out a lot of data looking for
something weird, that won't work.

I miss the EXHIBIT statement.  I miss the ON statement.

But you may be right - that the reason batch debugging tools are not
widely used in mainframe shops is because of lack of training and
company support, rather than lack of perceived value to programmers in a
hurry.

> FYI-2,
>   From my days of working for both Micro Focus *and* ADS (the then vendor of
…[25 more quoted lines elided]…
> > quickly we just get handed new work.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 7)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D2%N4.18762$0o4.142608@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <#5Uct2#r$GA.351@cpmsnbbsa04> <39084D30.2B83B434@cusys.edu> <8e9jl1$d55$1@slb0.atl.mindspring.net>`

```
In article <8e9jl1$d55$1@slb0.atl.mindspring.net>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:

[snippimente]

>FYI-2,
>  From my days of working for both Micro Focus *and* ADS (the then vendor of
>Xpediter), it is truly remarkable how many shops pay for
>debugging/development tools but don't provide the time and resources for
>their programmers to actually learn how and when to use them.

My experiences are similar to this.

DD
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u1%N4.18761$0o4.142564@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <y7LN4.18478$0o4.137619@iad-read.news.verio.net> <#5Uct2#r$GA.351@cpmsnbbsa04> <39084D30.2B83B434@cusys.edu>`

```
In article <39084D30.2B83B434@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, to, Howard, Brazee, post,
 	them!!> wrote:

[snippage]

>I guess we're too lazy to take the time
>and effort to use those tools when we can do displays exactly where we
>want and get our debugging out of the way quickly and easily.

BLEARGH!  With all due respect, Mr Brazee, what you describe here is not
what I was taught to call 'laziness'.  To be 'lazy' is to put out the
minimal amount of effort necessary to 'get away' with a task... the task
may or may not actually get done but the lazy one 'gets away' with
it.  You seem to be stating here that you are putting in *more* effort
than the task might otherwise require were your efforts directed
differently... this, as I was taught, is not 'laziness' but more akin to
'stupidity'.

A Story:

A gang of carpenters are working on a house; the Foreman (this story is
old enough to have originated in the days when Foremen were Foremen, not
Forefolk), as is the Forman's wont, is wandering about, keeping an eye on
things.  He notices one particular carpenter laboring *mightily* with his
saw and the following dialogue ensues:

F: 'Hey, Joe... what'cha doin'?'

J: 'Sawin' these planks, Boss, just like ya tol' me to.'

F: 'Yup, that ya are... y'know, I can't really tell from this angle but it
looks, to me, like your saw's kinda dull.'

J: 'You sure got a good eye, Boss... I guess that's why you're the
Boss.  Saw sure is dull, duller'n a butterknife.'

F: 'Oh... ummmm, Joe, why don't you sharpen your saw?'

J: 'Sharpen my saw?  I'm too busy cuttin' these planks to sharpen my saw!'

EOS

Now I have told that tale many times, in many places... and many folks
have laughed and nodded while intoning 'Yup, it's *just* that way here,
too'...

... while *my* response, when I first heard it, was to think 'All
right... and now the Foreman says 'Joe, lissen'a me.  I am your
Boss... Direct Order, stop cuttin' the planks and sharpen your saw, *now*,
please?''

DD
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 7)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39088F27.2483B4DD@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <y7LN4.18478$0o4.137619@iad-read.news.verio.net> <#5Uct2#r$GA.351@cpmsnbbsa04> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
> 
> In article <39084D30.2B83B434@cusys.edu>,
…[16 more quoted lines elided]…
> 'stupidity'.

That wasn't my intent.  What I meant to say is that I use displays (in
batch programs) because I don't want to go to the extra work of tracing
through a debugger.
 
> A Story:
> 
…[31 more quoted lines elided]…
> DD

Good story.  I infer then that you believe that if we took the time to
really know the debugger well, we would find it to be less work than
using displays.  You may be correct, but past experience has shown that
debugging batch is similar to debugging on-line.  We have plenty of
experience using debugging tools with on-line - that's because we don't
have much choice.  We do have a choice with batch, so we avoid them.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4S0O4.18780$0o4.143337@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu>`

```
In article <39088F27.2483B4DD@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, to, Howard, Brazee, post,
 	them!!> wrote:
>docdwarf@clark.net wrote:
>> 
…[11 more quoted lines elided]…
>> what I was taught to call 'laziness'. 

[mas snippimente]

>That wasn't my intent.  What I meant to say is that I use displays (in
>batch programs) because I don't want to go to the extra work of tracing
>through a debugger.

... and what was  intended in reply was what you concluded below... so, in
the words of Engineer Scott, 'Let's go see!'

> 
>> A Story:

[a tale docked]

>> EOS
>> 
…[15 more quoted lines elided]…
>have much choice.  We do have a choice with batch, so we avoid them.

I read your reply with sadness, Mr Brazee... see...

'... if we took the time to really know... we would find it to be less
work'.

The conclusion is that your work efforts are not directed by full
knowledge of alternatives... but the 'rut you know best', as it were.

Where, oh where is the Foreman who will tell you to sharpen your saws?

DD
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 9)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3908A68F.69875EFE@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net>`

```
docdwarf@clark.net wrote:
> 

> >Good story.  I infer then that you believe that if we took the time to
> >really know the debugger well, we would find it to be less work than
…[11 more quoted lines elided]…
> knowledge of alternatives... but the 'rut you know best', as it were.


I infer then that you believe that the batch debugger tools you are
familiar with are many orders of magnitude better than the online tools
we are familiar with.  

Either that or your batch programs do a lot of calling of subprograms
(possibly OO).  (That kind of complexity requires stronger tools).  Boy
it would be nice if our online tools were half as useful as batch
displays.  Maybe I have just worked in the wrong shops.   

At any rate, I have worked with lots of programmers in lots of shops. 
Maybe a third of us have tried online tools for batch.  None of us have
kept doing so.  The difference between us and that sawyer is that he
believes he has a tool to sharpen his saw.  Maybe you have a better
"sharpener" than what I have seen at my shops, one that actually doesn't
dull the blades.

I do have to admit that in my current job I have no idea whether we have
any such tool at all.  (Our online programs uses ADS/O and ADS-ALIVE for
debugging).  I have asked around, but the systems person who might know
is on vacation.  Since I have worked here for over two years, my
experience may be out of date.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eaciu$egb$1@slb7.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu>`

```
Again - going back to my Xpediter days (Micro Focus and "porting" testing to
the PC is another story completely), there really should be LESS effort in
invoking an "online debugger" than using DISPLAYs.

Xpediter (and I assume several other online tools) provides a "tool" to
auto-magically convert JCL to TSO CLISTS (or possibly REXX now).  In that
case, all you SHOULD need to do is (one time only) convert your JCL to
CLIST/REXX - and then invoke the debugger (usually under ISPF).

Once the full screen version of your program "comes up" - you can use a
single "line command" (that should look a LOT like and ISPF line command) to
put a break point where you would have put a DISPLAY and then run your
program.  This should then give you a LOT more debugging capabilities than a
"simple display" to resolve your problem.

If this is "difficult," I just don't get it.
   OTOH, there are lots and LOTS more capabilities that online debuggers have
that give you MORE capabilities than "display" statements.  Getting to know
when and how to use those may take some time, but I just don't understand
how/why this is "difficult".

Now, the above DOES assume that your "installer" has installed the debugging
tool "successfully" so that it is easy to reach from your normal ISPF
session.  If that is "missing" then there may be some reasons for never using
it.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 11)_

- **From:** Eddie White <eddiewhite@hotmail.com>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ekqus$4t$1@nnrp1.deja.com>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu> <8eaciu$egb$1@slb7.atl.mindspring.net>`

```
In article <8eaciu$egb$1@slb7.atl.mindspring.net>,
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> Again - going back to my Xpediter days (Micro Focus and "porting"
testing to
> the PC is another story completely), there really should be LESS
effort in
> invoking an "online debugger" than using DISPLAYs.
>
> Xpediter (and I assume several other online tools) provides a "tool"
to
> auto-magically convert JCL to TSO CLISTS (or possibly REXX now).  In
that
> case, all you SHOULD need to do is (one time only) convert your JCL to
> CLIST/REXX - and then invoke the debugger (usually under ISPF).
>
Bill,

In my previous life as a Cobol programmer, I worked in shops that used
both Xpediter and SmarTest.  The gotcha in the JCL to CLIST conversion
method is if you have any files on tape.  OTOH, both of these debugging
tools had the ability to attach from an ISPF session to a batch address
space.  Again, there is a gotcha.  The batch address space identifier
has to be recognizable as a VTAM application for the cross-region
communication to work.  If you have a willing MVS sysprog, no problem.
Otherwise, you have to use Howard's method.

Eddie White, Volvo IT North America


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 12)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390DFEF7.3157C34A@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu> <8eaciu$egb$1@slb7.atl.mindspring.net> <8ekqus$4t$1@nnrp1.deja.com>`

```
Eddie White wrote:
> 
> In my previous life as a Cobol programmer, I worked in shops that used
…[6 more quoted lines elided]…
> Otherwise, you have to use Howard's method.

Has anybody used a batch COBOL debugger in an IDMS environment? 

As I said earlier, I do use ADS-ALIVE to debug ADS programs.  I am
limited to producing snaps of IDMS-DC programs called by on-line.  Batch
IDMS programs, I use displays.  Of the three the hierarchy of ease of
use is very clear:

Displays are much easier.
ADS-ALIVE is pretty much of a pain, but it allows me to change my mind
during the test run.
Snap dumps are at the bottom.

When I have been at shops which had Expediter, nobody used it for more
than getting nicely formatted dumps.  Now that IBM gives us almost as
good dumps, I wouldn't spend money for that limited use.  (It is quite
possible that if they were forced to use it interactively more, they
would eventually gotten used to it enough to choose to use it - but that
didn't happen).

I have used debugging tools with Java, Paradox for Windows, and C++ on
PCs.  I found the switch from Paradox for DOS to Paradox for Windows had
a large effect in making me not want to use Paradox anymore - debugging
was all of a sudden much harder.  But that isn't the fault of the
debugging tool, that was a result of its attempt to be more like OO. 
With a lot of objects, debugging tools are necessary, as everything is
hidden and hard to find.  And with interactive programs, some type of
debugging tool is necessary.

A powerful tool sometimes is necessary to do a tough job.  But a
strength of Cobol is that it can often be designed so that debugging is
an easy job.  Instead of getting out the back hoe and its highly paid
trained operator, I can get out a shovel, dig my small hole, find my
treasure and fill it back in while the back hoe is still being loaded
into the trailer.

I infer that OO shops have much tougher maintenance requirements which
make such tools more appropriate.  I intend on using the right sized
tool for the job.
```

###### ↳ ↳ ↳ Debugging (was: Split output

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8el3p4$fl7$1@nntp9.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu> <8eaciu$egb$1@slb7.atl.mindspring.net> <8ekqus$4t$1@nnrp1.deja.com> <390DFEF7.3157C34A@cusys.edu>`

```
Howard,
  "long ago and far away" - when I worked for ADS (Xpediter's then vendor),
we had LOTS of IDMS sites.  I suspect that Compuware would be more than happy
to provide you with a number of "reference sites" for IDMS (batch) debugging.
```

###### ↳ ↳ ↳ Re: Debugging (was: Split output

_(reply depth: 14)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390ED14C.F1894FD3@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu> <8eaciu$egb$1@slb7.atl.mindspring.net> <8ekqus$4t$1@nnrp1.deja.com> <390DFEF7.3157C34A@cusys.edu> <8el3p4$fl7$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Howard,
…[5 more quoted lines elided]…
> Bill Klein

The last IDMS site I worked at before my current site had Xpediter.  But
nobody used its on-line debugger (we liked the formatted dumps though -
this was before IBM had formatted dumps).  My current probably has
whatever comes with IBM Cobol.  Since this thread started, I have done
some inquiry, but will need to do more research to determine whether we
have anything.  It is not a priority.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 13)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390E1D0B.BAA67C03@home.com>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu> <8eaciu$egb$1@slb7.atl.mindspring.net> <8ekqus$4t$1@nnrp1.deja.com> <390DFEF7.3157C34A@cusys.edu>`

```


Howard Brazee wrote:
> 
 
> I infer that OO shops have much tougher maintenance requirements which
> make such tools more appropriate.  I intend on using the right sized
> tool for the job.

Not PC-wise. The same N/E Animator is used for both structured and OO.
No real difference. For the latter you can open a 'window' to see a lot
of background specific to an OO object.

Regarding using the right tool. I haven't used it, although I was given
a copy. Eric Garrigue Vesely "COBOL Debugging Diagnostic Manual" 1990 -
ISBN 013 140187 4 - Prentice Hall. A quick glance indicates he uses
Declaratives to trap ALL errors for debugging purposes. Are you familiar
with it Howard ?

Jimmy
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 14)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390ED326.79588A79@cusys.edu>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu> <8eaciu$egb$1@slb7.atl.mindspring.net> <8ekqus$4t$1@nnrp1.deja.com> <390DFEF7.3157C34A@cusys.edu> <390E1D0B.BAA67C03@home.com>`

```


"James J. Gavan" wrote:
> 
> Howard Brazee wrote:
…[16 more quoted lines elided]…
> Jimmy

I have used declaratives to do the equivalent of READY TRACE, and showed
it to others who weren't interested.  After playing with a bit, I lost
interest as well.  We set our compiler options so that programs give us
the line number of the abort so it is very easy to tell what the abort
was all about (along with a formatted dump).  What does this procedure
give that would be more useful?
```

###### ↳ ↳ ↳ Debugging (was: Split output

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ektv6$iem$1@nntp9.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu> <8eaciu$egb$1@slb7.atl.mindspring.net> <8ekqus$4t$1@nnrp1.deja.com>`

```
The "test data on tape" issue is one that I understand - but question how
much of your "debugging" stage should be using tape files.

The VTAM session problem ONLY is a problem if you are using a "remote"
debugger, i.e. running your debugging session on the PC while the application
runs on the mainframe.  If, instead, you do your debugging in "TSO
Foreground," this should not be a problem.  (Although some shops still do NOT
like the resources that this takes either)
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 10)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MP4O4.18869$0o4.145114@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu>`

```
In article <3908A68F.69875EFE@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, to, Howard, Brazee, post,
 	them!!> wrote:
>docdwarf@clark.net wrote:
>> 
…[19 more quoted lines elided]…
>we are familiar with.  

My apologies for my obscurity, Mr Brazee; I took your statement of 'if we
took the time to really know' as the equivalent of '... but we have not
taken the time and do not really know'.

If my reading is correct then *either* of us might be right... but More
Learning is in order before a conclusion based on more on data and less on
assumption might be arrived at.

[snip]

>At any rate, I have worked with lots of programmers in lots of shops. 
>Maybe a third of us have tried online tools for batch.  None of us have
…[3 more quoted lines elided]…
>dull the blades.

A sharpening-stone, improperly handled, can dull a blade; first one needs
to learn how to use it.

DD
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 11)_

- **From:** Art Perry <eowynfuzz@my-deja.com>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ecd8a$4qq$1@nnrp1.deja.com>`
- **References:** `<39073291.2953296B@cusys.edu> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <3908A68F.69875EFE@cusys.edu> <MP4O4.18869$0o4.145114@iad-read.news.verio.net>`

```
By now we are pretty much off topic, so I want to jump in with a saw
sharpening comment:

When my project has slow times (which it often does.  Our work load
goes up and down.) I sharpen my saw.  I am sharpening my saw right now
by reading this newsgroup.

Several weeks ago, I got yelled at for sharpening my saw.  My leader
felt that it was not project related work and I should not be doing
it.  I feel that saw sharpening is important, and although it might not
directly support the project, it always indirectly supports the
project, because it supports me.

Unfortunately, many narrow minded people who tell me what to do don't
see it that way, thus my dilemma.  I've noticed several times, DD,
where you justify a given solution you have described by
saying "...Because he who signs my paychecks told me to..."

-Art


In article <MP4O4.18869$0o4.145114@iad-read.news.verio.net>,
  docdwarf@clark.net () wrote:
[snip]
> My apologies for my obscurity, Mr Brazee; I took your statement
of 'if we
> took the time to really know' as the equivalent of '... but we have
not
> taken the time and do not really know'.
>
> If my reading is correct then *either* of us might be right... but
More
> Learning is in order before a conclusion based on more on data and
less on
> assumption might be arrived at.
>
> [snip]
>
> >At any rate, I have worked with lots of programmers in lots of
shops.
> >Maybe a third of us have tried online tools for batch.  None of us
have
> >kept doing so.  The difference between us and that sawyer is that he
> >believes he has a tool to sharpen his saw.  Maybe you have a better
> >"sharpener" than what I have seen at my shops, one that actually
doesn't
> >dull the blades.
>
> A sharpening-stone, improperly handled, can dull a blade; first one
needs
> to learn how to use it.
>
> DD
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 12)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N6rO4.19052$0o4.152409@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <3908A68F.69875EFE@cusys.edu> <MP4O4.18869$0o4.145114@iad-read.news.verio.net> <8ecd8a$4qq$1@nnrp1.deja.com>`

```
In article <8ecd8a$4qq$1@nnrp1.deja.com>,
Art Perry  <eowynfuzz@my-deja.com> wrote:
>By now we are pretty much off topic, so I want to jump in with a saw
>sharpening comment:
…[14 more quoted lines elided]…
>saying "...Because he who signs my paychecks told me to..."

For me it is more than 'several times', Mr Perry; I need to remind myself
of this on a daily basis:

'Why am I working on a proc in a public library where anyone, at any time,
can make mods that might screw up what I am doing?  Because the person who
signs my timesheets tells me to.'

... and suchlike.  You mention that a manager hollered on you for
'sharpening your saw'; this is behavior similar to the anecdote and
directly opposed to my msuing over why the Foreman didn't issue a
saw-sharpening order.

I am reminded of A Story! - perhaps apochryphal, granted, but if it isn't
true it should be.

It was told that Someone Important - Kernigan?  Ritchie? - was working at
Bell Labs in the mid '70's, doing some rather... intricate work on data
dictionaries.  He had A Problem in mind and had assumed the Programmer's
Position... cup of coffee in one hand, cigarette in the other, feet up on
the desk, staring at the ceiling and mapping out memory-locations in the
acoustic tiles.

His Boss walks past and bellows out 'What *ARE* you doing?!?'

He shakes himself, recovers from whatever intricacy is now lost... and, in
a calm, measured manner said 'I'm *thinking*, Boss.'

'Oh... well, can't you do that on your own time?'

This brings to mind a bit of a Benny Hill skit I saw, a few decades
back... I think it was a parody of Kojak... anyhow, Benny Hill, as one
character, engages Benny Hill, as another character, in the following
exchange:

'Where were you?

'Getting a haircut.'

'On company time?'

'It grew on company time.'

... and even more interesting, in the case of some companies - the old EDS
or Disney, say - not only does it grow on company time but it is the
company which demands hair of a certain length, too.

DD

>
>In article <MP4O4.18869$0o4.145114@iad-read.news.verio.net>,
…[20 more quoted lines elided]…
>> to learn how to use it.
```

###### ↳ ↳ ↳ Re: Split output from a COBOL pgm - BatchPipeWorks

_(reply depth: 13)_

- **From:** Jonathan Nash <jnash@qis.net>
- **Date:** 2000-04-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.GSO.3.96.1000429100821.9404B-100000@eclipse>`
- **References:** `<39073291.2953296B@cusys.edu> <3908A68F.69875EFE@cusys.edu> <MP4O4.18869$0o4.145114@iad-read.news.verio.net> <8ecd8a$4qq$1@nnrp1.deja.com> <N6rO4.19052$0o4.152409@iad-read.news.verio.net>`

```
Someone on IBM-MAIN said that this 
can be done with BatchPipeWorks:

>Yes, for the price of (a) JCL changes and (b) BatchPipes.  The advantage
>to your management is that the code is maintained (by IBM, compared to
>Paul's suggestion from yesterday.)
>It would be a half-pipe fitting to do the split.
>Tom S.

I do not know enough about BatchPipeWorks to put together the
JCL that would be needed but here is a snippit from a manual
which shows how BatchPipeWorks can send output to more than
one location:

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
IBM SmartBatch for OS/390: BatchPipeWorks User's Guide
Document Number GC28-1651-01
� Copyright IBM Corp. 1995, 1998
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

5.3.2 The > Stage Function
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

The > (rewrite data set) stage function reads records from its input
stream and writes those records to a physical sequential data set or
member of a partitioned data set.  The physical sequential data set must
already exist.  The member of the partitioned data set may or may not
exist.  The physical sequential data set is replaced.  If the member of
the partitioned data set exists, it is replaced.  If the member does not
exist, it is created.  Specify a data set identifier as the operand.  The
data set identifier can be the name of an existing physical sequential
data set, the name of a partitioned data set and the member that you want
to replace or create, or the ddname of an allocated data set.  A > stage
cannot be the first stage of a pipeline.

Like the TERMINAL stage function, the > stage function copies its input
stream to its output stream for use by any following stage.  All output
device drivers work this way.  In fact, both the following pipelines yield
the same results:

pipe tso listcat � > space.data � terminal

pipe tso listcat � terminal � > space.data

In the example, the order of the > and TERMINAL stage functions is
reversed.  TERMINAL displays the LISTCAT response on your terminal, but
also writes the records to its output stream.  The input stream of the >
stage function is connected to the output stream of TERMINAL.  So, the >
stage reads the response records and writes them to the SPACE.DATA data
set, replacing the contents of the data set.

In Figure 154, the < stage function reads the data set DAY.LIST, writing
the records to its output stream.  Then the > stage function reads those
records from its input stream and writes them to the existing data set
NEWDAY.LIST.

--------------------------------------------------------------------------
[snip]
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390BD473.6B@Azonic.co.nz>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net>`

```
> 
> I read your reply with sadness, Mr Brazee... see...
…[7 more quoted lines elided]…
> Where, oh where is the Foreman who will tell you to sharpen your saws?

"To a hammer all problems look like nails".

You seem to have no idea of the problem area but you are proposing that
your solution is best regardless of any aspects that you are completely
oblivious to.

While interactive debugging is wonderful for certain sets of problems it
is not always the best solution.  I have a system which would be
extremely difficult to interactively debug and would be almost
unmanageable to maintain in a manner that would facilitate this.  It is
a large Windows API system maintaining a dozen or so main windows and a
multitude of dialog boxes that allows completely unstructured user
interaction.

The system has its own built in 'debugging' trace that can be turned on
or off.  This is equivalent to 'Batch Displays' but uses a dialog list
box and write a log file.  Mostly it is only necessary to turn on the
trace - on the users' site if required, and get the trace results to see
where the problem is occuring.

Different mechanisms may be more appropriate to other needs.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8efeiv$84n$1@slb6.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz>`

```
Just from my perspective (going back to my Micro Focus days - not my Xpediter
days), if your interactive debugging tool (that comes with your compiler) is
NOT built to make debugging of exactly that type of application "easy" - then
you should look at another vendor.

Certainly, Micro Focus' Animator has been enhanced (since multi-threading and
Windows APIs became common) to work exactly IN that type of environment.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 11)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qPLO4.1361$%Z2.179283@dfiatx1-snr1.gtei.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz> <8efeiv$84n$1@slb6.atl.mindspring.net>`

```
Not withstanding my high regard for your views, I think I'll weigh in on the
side of Mr Plinston on this one.

Perhaps it's because the first couple of times I tried to use a stepping
debugger it was very difficult to use; or perhaps it's because I rarely need
to maintain old non-structured code, but I have developed the attitude that
a stepping debugger is just not that valuable a tool.

Seems to me other methods - log files or displays for instance - are better
tools.

Of course, there's no substitute for better planning when first developing
the code - that is, planning in advance how you are going to *test* the
code - and building in the appropriate "hook" points.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eg1r2$bd0$1@slb6.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz> <8efeiv$84n$1@slb6.atl.mindspring.net> <qPLO4.1361$%Z2.179283@dfiatx1-snr1.gtei.net>`

```
I agree that a "stepping" debugger is not that useful (well actually even
that depends) - but all the debuggers that I know of, let you put a "break
point" in and to RUN to that point.  Many (but not all) allow you to then
"backtrack" from that point to see how you got there.  Even if you JUST have
the former capability, I am still not convinced of how/why a DISPLAY or
"logging" tool would be easier to use for debugging.

Oh well, the days of my getting a paycheck based on "selling" people on more
efficient debugging techniques is long gone, so I wish you luck with whatever
technique you find easiest/most useful.  (How about always writing and
maintaining "perfect" code - Now debugging that is a "breeze" <G>)
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 13)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000429235314.24686.00002540@nso-fz.aol.com>`
- **References:** `<8eg1r2$bd0$1@slb6.atl.mindspring.net>`

```
In article <8eg1r2$bd0$1@slb6.atl.mindspring.net>, "William M. Klein"
<wmklein@nospam.ix.netcom.com> writes:

>
>I agree that a "stepping" debugger is not that useful (well actually even
…[5 more quoted lines elided]…
>

I have tried using the LE Debug Tool on a batch program and found that
it can be VERY difficult to work with.  Even when using a control break 
on a given line, it seemed to break/stop on EVERY record of the SYSIN 
parms file which happens to be almost 1500 lines.  It usually generates 
about 5000 lines of output in the listings file.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 13)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390CFA09.DE14CB4E@home.com>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz> <8efeiv$84n$1@slb6.atl.mindspring.net> <qPLO4.1361$%Z2.179283@dfiatx1-snr1.gtei.net> <8eg1r2$bd0$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> I agree that a "stepping" debugger is not that useful (well actually even
…[10 more quoted lines elided]…
>
 
Are we differentiating between mainframe and PC debuggers. I see Sff5ky
referring to LE debugger as being difficult to use.

Believe me, just having had to recently do a quick and dirty Y2K on
RM/COBOL(1980) - how I wished for a debugger. To get it right
necessitated me putting in displays and "ACCEPT CHAR-X" to stop the
bloody thing so I could see what was being displayed. Remember - this
was meant to be a quick fix, not something for posterity.

My current debugger is a dream. I set breakpoints to stop at critical
areas then step through until I hit the specific line of code causing
the problem. Being OO, invariably it is a missing linkage parameter or
an incorrect object reference. 

Jimmy
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 14)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390D05EC.6F4B0C40@zip.com.au>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz> <8efeiv$84n$1@slb6.atl.mindspring.net> <qPLO4.1361$%Z2.179283@dfiatx1-snr1.gtei.net> <8eg1r2$bd0$1@slb6.atl.mindspring.net> <390CFA09.DE14CB4E@home.com>`

```
"James J. Gavan" wrote:
> 
> My current debugger is a dream. I set breakpoints to stop at critical
> areas then step through until I hit the specific line of code causing
> the problem. Being OO, invariably it is a missing linkage parameter
> or an incorrect object reference.

For every object and method you should be using the interface
definition.  This will stop the compile dead and no debugging
required.

I saw a statistic that 30% of all coding errors were mismatches in
parameters in writing solid code,  this is the first instance when
this has been supported.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Debuggin (was: Split output

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ej1t4$mkh$1@nntp9.atl.mindspring.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz> <8efeiv$84n$1@slb6.atl.mindspring.net> <qPLO4.1361$%Z2.179283@dfiatx1-snr1.gtei.net> <8eg1r2$bd0$1@slb6.atl.mindspring.net> <390CFA09.DE14CB4E@home.com> <390D05EC.6F4B0C40@zip.com.au>`

```
Ken and Jimmy,
  I know that Jimmy is using MERANT's NetExpress.  Has it yet provided
support for an 'external repository' for interfaces?  If not, and it still
requires you to actually keep the "prototype" in EVERY program that uses it,
I am not so positive that this really is a "good solution" (yet).

Once they do support an external repository for such things, then YES, I
would say that you should make certain that all CALLs and INVOKEs use "early"
binding where possible and late when that is all that is available.
```

###### ↳ ↳ ↳ Re: Debuggin (was: Split output

_(reply depth: 16)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390DBA33.C859C42C@home.com>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz> <8efeiv$84n$1@slb6.atl.mindspring.net> <qPLO4.1361$%Z2.179283@dfiatx1-snr1.gtei.net> <8eg1r2$bd0$1@slb6.atl.mindspring.net> <390CFA09.DE14CB4E@home.com> <390D05EC.6F4B0C40@zip.com.au> <8ej1t4$mkh$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> Ken and Jimmy,
…[8 more quoted lines elided]…
> 
As Thane has already pointed out, it is the linkage/conformance checking
in COBOL 200X which will be a real boon. Given these two features, I
think debugging becomes a matter of merely checking your business
logic/sequencing in a three-tier system approach. Using three-tier and
having gotten "canned" User Interface (Screens) and DBI(File Handling)
right - you can be almost 100% certain that your errors reside in your
business logic.

Jimmy
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 15)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<390dadfc.177992988@news.cox-internet.com>`
- **References:** `<39073291.2953296B@cusys.edu> <39084D30.2B83B434@cusys.edu> <u1%N4.18761$0o4.142564@iad-read.news.verio.net> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz> <8efeiv$84n$1@slb6.atl.mindspring.net> <qPLO4.1361$%Z2.179283@dfiatx1-snr1.gtei.net> <8eg1r2$bd0$1@slb6.atl.mindspring.net> <390CFA09.DE14CB4E@home.com> <390D05EC.6F4B0C40@zip.com.au>`

```
On Mon, 01 May 2000 14:19:56 +1000, Ken Foskey <waratah@zip.com.au>
wrote:

>"James J. Gavan" wrote:
>> 
…[12 more quoted lines elided]…
>

Ken, 

He can't.  Neither Fujitsu or Merant (that I am aware of) have
implementated the "INTERFACE". However, Fujitsu does let you restrict
object references to certain classes - either spcifically or to that
class and anything that inherits from it.  Also using the Repository,
Fujitsu presently does conformance checking.  Interface is defined in
the draft standard, but I know of no compiler vendor that has
implemented it.
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 10)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QWLO4.19411$0o4.158636@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39088F27.2483B4DD@cusys.edu> <4S0O4.18780$0o4.143337@iad-read.news.verio.net> <390BD473.6B@Azonic.co.nz>`

```
In article <390BD473.6B@Azonic.co.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>> 
>> I read your reply with sadness, Mr Brazee... see...
…[13 more quoted lines elided]…
>oblivious to.

Mr Plinston, please re-read what you quoted above and, if you would,
ponder the phrase 'full knowledge of the alternatives'.

What do you interpret this to be?  I intended it to be nothing more than
a reference to the gaining of knowledge, that one should decide on a tool
*after* one has knowledge of tools; limited fellow that I am I have found
that decisions made with knowledge are usually better than ones made in
ignorance.

>
>While interactive debugging is wonderful for certain sets of problems it
>is not always the best solution.

I do not recall suggesting that this might be the case.

>I have a system which would be
>extremely difficult to interactively debug and would be almost
…[11 more quoted lines elided]…
>Different mechanisms may be more appropriate to other needs.

I'm not usre what you intend to be learned from this example, Mr Plinston,
but a conclusion that I do *not* see coming out of it is that Mr Brazee
should remain in ignorance regarding the capabilities of the debugger
available to him... if my vision is correct then we are, I believe, in
agreement.

DD
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 5)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AsON4.18610$0o4.139623@iad-read.news.verio.net>`
- **References:** `<39073291.2953296B@cusys.edu> <39074022.7E99A597@cusys.edu> <y7LN4.18478$0o4.137619@iad-read.news.verio.net> <#5Uct2#r$GA.351@cpmsnbbsa04>`

```
In article <#5Uct2#r$GA.351@cpmsnbbsa04>,
ChrisOsborne <chris_n_osborne@yahoo.com> wrote:
><docdwarf@clark.net> wrote in message
>news:y7LN4.18478$0o4.137619@iad-read.news.verio.net...
…[21 more quoted lines elided]…
>make up for it.

I am not sure into whose lap such things falls... but I can readily
imagine that when the Big Blue Boys are in the taperoom, tossing carts
into the silo to load the OS and someone were to ask them 'Hey, will you
be installing COBTEST?'... that it would get done along with everything
else.

In my experience... not only does it have to be properly installed (and
rarely is) but there needs to be a bit of training in how to use it
(likewise never is).

DD
```

#### ↳ Re: Split output

- **From:** Charles Hammond <ceh1@ritz.cec.wustl.edu>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pine.SOL.3.96.1000426142023.19391B-100000@ritz.cec.wustl.edu>`
- **References:** `<39073291.2953296B@cusys.edu>`

```
This isn't that difficult an issue.  I program on a leagacy IBM 370 and we
often have reports that do multiple tasks.  Sometimes we use an accept so
we can select what we want to do.  

For instance if you want to build a file to sort, sort it and then print
it you can use a switch in your program to decide which task to do.  By
doing this you eliminate wasted space for the 2 programs.

I have a little program that prints sections from my system dictionary, so
I needed to build an SD so I could sort it. I also needed to save the file
for a PC usage of the data so I built a downlod file that I can download
through the network. 

A lot of this is operating system dependent.  I actually just run the
program once for the build and once for the print, because we use a
utility program to do the sort in the middle.  but you could do both
either at the same time with multiple writes or by just using a switch to
go back and start over after the build. You just need an extra file in the
file description, one for the print-file and one to write the file to.
The accepts on a mainframe we handle in the job control language.  So for
one job you can run multiple programs.


Charles Hammond, BSIM Undergraduate Program

On Wed, 26 Apr 2000, Howard Brazee wrote:

> This is an operating system issue, not a programming language issue -
> but I sure wish I could point the output of a program to multiple
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Split output - network output

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000427000335.12346.00001242@nso-fc.aol.com>`
- **References:** `<Pine.SOL.3.96.1000426142023.19391B-100000@ritz.cec.wustl.edu>`

```
In article <Pine.SOL.3.96.1000426142023.19391B-100000@ritz.cec.wustl.edu>,
Charles Hammond <ceh1@ritz.cec.wustl.edu> writes:

>
>I have a little program that prints sections from my system dictionary, so
…[3 more quoted lines elided]…
>

Does anyone know of a method for routing the output of a DDname 
to a network drive?  I am speaking from an IBM OS/390 perspective 
with USS, TCP/IP and FTP capabilities.  Currently we output a DASD 
file and then from the PC initiate an FTP session and download the files
in BINARY mode.   I would like to know if there is anyone with experience
with generating the output directly to a PC/LAN Drive using Mainframe 
JCL syntax.
Any assistance or pointers to specific locations in the Online reference 
manuals would be greatly appreciated.
I have yet to search the manuals as I have never had a great deal of luck
finding what I need without first locating the correct book.  Most times the
book I choose is not the one the documentation wizards decided to use for
explaining what I am looking for.

Thanks for your time.
```

###### ↳ ↳ ↳ Re: Split output - network output

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e8gqa$3gd$1@slb7.atl.mindspring.net>`
- **References:** `<Pine.SOL.3.96.1000426142023.19391B-100000@ritz.cec.wustl.edu> <20000427000335.12346.00001242@nso-fc.aol.com>`

```
Another area that I have never tried myself, but you might want to look at:

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IEA1B510/5%2e7%2e1%2e2

(I sure wouldn't try this without asking my "friendly local SysProg" first)
```

###### ↳ ↳ ↳ Re: Split output - network output

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3908300A.BC942E0E@zip.com.au>`
- **References:** `<Pine.SOL.3.96.1000426142023.19391B-100000@ritz.cec.wustl.edu> <20000427000335.12346.00001242@nso-fc.aol.com>`

```
Sff5ky wrote:

> file and then from the PC initiate an FTP session and download the 

You can execute the FTP client program from the TCPIP suite on the MVS
mainframe to a FTP server installed on your Network PC server (you do
have that set up don't you :-}).

If you need a sample JCL email me at 'waratah at zip dot com dot au'
and I will provide a JCL sample.  (spamcop is broken must RTFM)

We do this to NT servers and Unix servers regularly and reliably.  My
guess is you might not have the FTP server set up on your PC system
and this might be your biggest hurdle.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Split output - network output

- **From:** docdwarf@clark.net ()
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JG_N4.18757$0o4.142391@iad-read.news.verio.net>`
- **References:** `<Pine.SOL.3.96.1000426142023.19391B-100000@ritz.cec.wustl.edu> <20000427000335.12346.00001242@nso-fc.aol.com>`

```
In article <20000427000335.12346.00001242@nso-fc.aol.com>,
Sff5ky <sff5ky@aol.comxxx123> wrote:
>In article <Pine.SOL.3.96.1000426142023.19391B-100000@ritz.cec.wustl.edu>,
>Charles Hammond <ceh1@ritz.cec.wustl.edu> writes:
…[9 more quoted lines elided]…
>to a network drive?

As in using a DDname to point directly to an open ftp session directed to
a network drive?  No.  As in creating a jobstream on the mainframe which
will invoke an ftp session and send the file down?  Yes.

> I am speaking from an IBM OS/390 perspective 
>with USS, TCP/IP and FTP capabilities.  Currently we output a DASD 
…[3 more quoted lines elided]…
>JCL syntax.

See above.

>Any assistance or pointers to specific locations in the Online reference 
>manuals would be greatly appreciated.

See below.

>I have yet to search the manuals as I have never had a great deal of luck
>finding what I need without first locating the correct book.  Most times the
>book I choose is not the one the documentation wizards decided to use for
>explaining what I am looking for.

Ow OW ow ow ow... *this* is what makes it less painful, but still
painful.  Yes, I have designed jobstreams for OS390 systems which will
initiate an ftp session and squirt down a file; depending on how the ftp
logon id is configured the appropriate network drive/directory will be
said id's default.

In fact... I have designed... stuff, a combination of simple .BAT files
and JCL, which, when invoked by a PC user, will submit a batch job to the
mainframe's internal reader, run an extract program and then squirt the
file back down to the PC (via ftp) so that the user has fresh data to use.

Sounds right tasty, doesn't it?  Well, here's the... sticky part: I was
paid for doing this... in fact, I was paid several severals of tens of
thousands of dollars for doing this; the result was a bunch of... stuff
which is now in daily use by a Very Large Company on a daily basis.

In short... I did this and still do this kind of stuff for money; this is
My Job.  When I am asked to do My Job for free. I get kind of... wary.

When I am asked to do My Job for free by someone who admits that he has
'yet to search the manuals' I stifle obscenities.

You have my email address; feel free to pass it along to someone who has
sufficient authority to cut me a check.

DD
```

#### ↳ Re: Split output

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39088F1E.AB85E67C@yahoo.com>`
- **References:** `<39073291.2953296B@cusys.edu>`

```


Howard Brazee wrote:
> 
> This is an operating system issue, not a programming language issue -
> but I sure wish I could point the output of a program to multiple
> locations at once.  Maybe have my DISPLAY go to SYSOUT and to a file
> simultaneously.

Try this JCL method...

//JEPR240      JOB     (EPR240,P),'W-2 PRINT JOB',MSGCLASS=5,      
//             USER=JEPR240,CLASS=A,PRTY=7                         
//*                                                                
//$AVRS        OUTPUT CLASS=*                                      
//SYSLIST      OUTPUT CLASS=M                                      
.
.
.
//STEP01       EXEC ...
.
.
.
//SYSOUD       DD   SYSOUT=(,),OUTPUT=(*.$AVRS,*.SYSLIST) 
.
.
.

This enables us to print the same output file to 2 different classes at
once.  I presume you can also write to a file as well.

Joe Kohler
```

##### ↳ ↳ Re: Split output

- **From:** Eddie White <eddiewhite@hotmail.com>
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8emoki$2p7$1@nnrp1.deja.com>`
- **References:** `<39073291.2953296B@cusys.edu> <39088F1E.AB85E67C@yahoo.com>`

```
In article <39088F1E.AB85E67C@yahoo.com>,
  Joseph Kohler <joe_kohler@yahoo.com> wrote:
>
>
> Howard Brazee wrote:
> >
> > This is an operating system issue, not a programming language issue
-
> > but I sure wish I could point the output of a program to multiple
> > locations at once.  Maybe have my DISPLAY go to SYSOUT and to a file
…[21 more quoted lines elided]…
> This enables us to print the same output file to 2 different classes
at
> once.  I presume you can also write to a file as well.
>
> Joe Kohler
>

The OUTPUT statement was my first thought, as well.  But, a check of my
MVS/ESA JCL user's guide shows that OUTPUT only works for multiple
sysout classes/destinations, not to files.  BTW, you can have send
sysout to an external writer by the OUTPUT statement.

Howard, if you want to have your displays saved in a dataset for
additional analysis after your test run is done, here's a suggestion.
First, I'm making the assumption that since you working on a
TSO/MVS/IDMS system, you have SDSF or something equivalent.  Okay, when
you're ready to end you job, cancel it instead of purging it.  This will
leave your sysout files on the TSO hold queue.  Then, select the sysout
file your display were written to.  Use the SDSF Print D command, which
will display a panel where you specify a dataset to copy the sysout file
to.  Once you press enter, you're returned to the sysout display.  Issue
the Print command, followed by the Print Close command.  Your displays
are now save to the dataset you specified.

HTH,
Eddie White


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Split output

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-05-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000502193038.10669.00001788@nso-cr.aol.com>`
- **References:** `<8emoki$2p7$1@nnrp1.deja.com>`

```
In article <8emoki$2p7$1@nnrp1.deja.com>, Eddie White <eddiewhite@hotmail.com>
writes:

>file your display were written to.  Use the SDSF Print D command, which
>will display a panel where you specify a dataset to copy the sysout file
…[3 more quoted lines elided]…
>

This sounds similar to putting XDC in the NP column of an
output queue display.  This presents the same data set destination
choice and handle the PRINT;PRINT CLOSE as well.

Something new I learned in the last couple of months
```

###### ↳ ↳ ↳ Re: Split output

_(reply depth: 4)_

- **From:** Eddie White <eddiewhite@hotmail.com>
- **Date:** 2000-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8epfkj$4ra$1@nnrp1.deja.com>`
- **References:** `<8emoki$2p7$1@nnrp1.deja.com> <20000502193038.10669.00001788@nso-cr.aol.com>`

```
In article <20000502193038.10669.00001788@nso-cr.aol.com>,
  sff5ky@aol.comxxx123 (Sff5ky) wrote:
> In article <8emoki$2p7$1@nnrp1.deja.com>, Eddie White
<eddiewhite@hotmail.com>
> writes:
>
> >file your display were written to.  Use the SDSF Print D command,
which
> >will display a panel where you specify a dataset to copy the sysout
file
> >to.  Once you press enter, you're returned to the sysout display.
Issue
> >the Print command, followed by the Print Close command.  Your
displays
> >are now save to the dataset you specified.
> >
…[7 more quoted lines elided]…
>

The only difference between the primary command Print Dataset and the
XDC line command is that the primary command gives you the opportunity
to copy only a portion of the sysout file to a dataset.  You do this by
specifying a range of lines on the Print command--Print 150 300, for
examply would copy only lines 150 through 300.  The line command
automatically copies the entire sysout file to a dataset.

Eddie


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
