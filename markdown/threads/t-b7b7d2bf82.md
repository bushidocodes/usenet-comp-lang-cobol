[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Is MF COBOL unable to run large applications?

_7 messages · 5 participants · 1996-05 → 1996-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Is MF COBOL unable to run large applications?

- **From:** "rey..." <ua-author-17087329@usenetarchives.gap>
- **Date:** 1996-05-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4mv81s$4s1@bulldns.bull.fr>`

```


We have a large application running under AIX 4.1 and compiled with
the MicroFocus COBOL compiler 3.2.31.
This application is very modular with a lot of procedures (4000) and all of
these procedures are statically linked.
Each of them is compiled with the INITIAL attribute.
So, after running our program a couple of minutes, it aborts with the following
message: Load error file 'XXXX'
error code: 55, pc=0, call=255,seg=0
55 routine table overflow
The abort occurs at the line containing the instruction: CALL "XXXX" USING ...
and XXXX is a statically linked procedure.
Our technical support says: "No solution, try to simplify your application".
But, of course, it is a lot of work to redesign completly our application
which is running without any problem on other system that does not use the
MicroFocus COBOL compiler.
So is there another solution?
A magic option for the compiler or the linker?
Or, in other terms, does it exist a real professional compiler COBOL for AIX?

Jean-Max Reymond
  
============================================================================
 Email  : rey··.@ct0··l.fr
 Phone  : (33) 93 14 23 19                Bulltel:  22-32319
 Fax    : (33) 93 14 23 11                Bullfax:  22-32311 
  
 Address:  BULL SLDV (Saint Laurent du Var)
============================================================================
```

#### ↳ Re: Is MF COBOL unable to run large applications?

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-05-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b7b7d2bf82-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4mv81s$4s1@bulldns.bull.fr>`
- **References:** `<4mv81s$4s1@bulldns.bull.fr>`

```

rey··.@ct0··l.fr wrote:
› 
›        We have a large application running under AIX 4.1 and compiled with 
…[6 more quoted lines elided]…
›         55 routine table overflow
 
› So is there another solution? [to redesigning the application]

Yes. This limitation is due to the architecture of a part of the RTS. However,
a tuneable exists to allow you to change the active-COBOL-module limit to
anything from 10 to 65535 modules. To change this limit, edit (or create) the
file "$COBDIR/cobconfig". Somewhere in that file, include a line which reads:

set routine_table_size=4000

.. or whatever maximum you want. Don't forget that using certain syntax
causes the RTS to implicitly load COBOL support modules which will also use
up routine table slots (eg CODESET, CLASS, ADIS, mFFH, PANELS etc). The default
is, I think, just 255 (hence the "call=255" in the error message).

FYI. There is newer technology being developed on Unix at the moment which,
among LOTS of other things, removes this (historical) artificial limit.

› Or, in other terms, does it exist a real professional compiler COBOL for AIX?

Yes. Try Micro Focus COBOL 3.2 (it's yours absolutely free, considering what
you have now :)) - I do think that was a little uncalled for until you'd waited
to see if there was a solution.
Having said that, there's obviously a problem with one of our Technical Support
offices not knowing this information. Can you tell me which Technical Support
site you contacted, please ? I'll make sure this information gets disseminated.

Cheers, Kevin.

Kevin. Advancing all electric at Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own. I doubt that anyone else would want them.
STUFF FOR SALE: Here!
```

##### ↳ ↳ Re: Is MF COBOL unable to run large applications?

- **From:** "sh..." <ua-author-6886694@usenetarchives.gap>
- **Date:** 1996-05-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b7b7d2bf82-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b7b7d2bf82-p2@usenetarchives.gap>`
- **References:** `<4mv81s$4s1@bulldns.bull.fr> <gap-b7b7d2bf82-p2@usenetarchives.gap>`

```

While stranded on information super highway Kevin Digweed wrote:
->rey··.@ct0··l.fr wrote:
->>

stuff deleted...

->>Or, in other terms, does it exist a real professional compiler COBOL for AIX?


We are right now evaluating IBM COBOL set for AIX on AIX 4.1.4. We have been
using MF COBOL until now. Right now it looks very promising. IBM COBOL
set supports shared library, no more int code :-), and I can use a any
Unix debugger I like (no more animator :-)).

Since we do cross development, we like IBM compiler because it is built
from same code that is used for MVS and OS/2. We get same errors we
get on mainframe. With MF COBOL there were some errors which MF COBOL
ignored, but Main Frame COBOL complained.


->Yes. Try Micro Focus COBOL 3.2 (it's yours absolutely free, considering what
->you have now :)) - I do think that was a little uncalled for until you'd waited

It is very nice compiler, but there are few things that were carried over
from DOS world, which Micro FOCUS has not fixed. We have asked them
several times.

e.g.: They do not add symbol information in the object files so I cannot
use other Unix debugger to debug the COBOL program. Our application
contains mixture of C and COBOL programs and it is hard to debug.

Constraints on file name length:
e.g. cob -C DIR=/some/file/name
file name cannot be more than certain character, I forgot the exact
size, we ended up naming file like "./conf/cp.ol.gn.dir"

Instead of "compile_online_general.directives"

These are to name a few.

->to see if there was a solution.
->Having said that, there's obviously a problem with one of our Technical Support
->offices not knowing this information. Can you tell me which Technical Support
->site you contacted, please ? I'll make sure this information gets disseminated.

->Cheers, Kevin.

->--
->Kevin. Advancing all electric at Micro Focus, Newbury, UK. (k.··.@mfl··o.uk)
->These views are strictly my own. I doubt that anyone else would want them.
->STUFF FOR SALE: Here!



                                      /-------------------¥    ^‾‾‾‾^
                                      |TECHNOLOGY         |    |    |
                                      |No place for wimps |   o|-OO-|o
                                      |          -Dilbert |--- | () |
                                      ¥-------------------/    |    |
---------------------------------------------------------------------------
Hemant Shah                      | I haven't lost my mind,
LIDP, Inc.                       | it's backed up on tape somewhere.
Voice: (708) 960 0133 Ext: 64    |
Fax: (708) 960 0717              | Above opinions are mine only. Others can
E-mail: Personal - sh··.@xn··t.com | have their own.
        Work - sha··.@li··p.com   | 
WWW: http://www.xnet.com/‾shah   | DO NOT SEND UNSOLICITED E-MAIL
--------------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Is MF COBOL unable to run large applications?

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-05-13T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b7b7d2bf82-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b7b7d2bf82-p3@usenetarchives.gap>`
- **References:** `<4mv81s$4s1@bulldns.bull.fr> <gap-b7b7d2bf82-p2@usenetarchives.gap> <gap-b7b7d2bf82-p3@usenetarchives.gap>`

```

sh··.@flo··t.com (Hemant Shah) wrote:
› IBM COBOL
› set supports shared library, no more int code :-),

FYI. Micro Focus products have supported native code generation for many many
years now.


› and I can use a any
› Unix debugger I like (no more animator :-)).

You *don't* like animator ? OK. Well, FYI, you can also use 'dbx' with Micro
Focus COBOL programs on AIX. Try:

$ cob -xg file.cbl
$ dbx file

(dbx) stop in file
(dbx) r

› With MF COBOL there were some errors which MF COBOL
›   ignored, but Main Frame COBOL complained.
 
› Did you report these problems to Technical Support ?
 
 
›  e.g.: They do not add symbol information in the object files so I cannot
›        use other Unix debugger to debug the COBOL program. Our application
›        contains mixture of C and COBOL programs and it is hard to debug.

Not sure what you mean. See the above comment about using dbx with MF COBOL.
Also, if you linked your C functions into a RTS and executed your COBOL code
with that RTS and include the +A switch in the $COBSW environment variable,
the animator is automatically entered when an animatable program is executed,
*even* if the RTS is running under a C debugger - you have two debuggers
coexisting - the Unix debugger for your C code and static linked MF COBOL and
the animator (which knows about COBOL) for your COBOL code. It's actually a
very powerful system (I sometimes use it when debugging our COBOL RTS itself).

›        Constraints on file name length:
›        e.g. cob -C DIR=/some/file/name
…[3 more quoted lines elided]…
›        Instead of "compile_online_general.directives"

Long filename support has also been in our AIX product for quite a while now
(years, I believe - I can't give you an exact time/version).

Cheers, Kev.
```

###### ↳ ↳ ↳ Re: Is MF COBOL unable to run large applications?

_(reply depth: 4)_

- **From:** "sh..." <ua-author-6886694@usenetarchives.gap>
- **Date:** 1996-05-14T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b7b7d2bf82-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b7b7d2bf82-p4@usenetarchives.gap>`
- **References:** `<4mv81s$4s1@bulldns.bull.fr> <gap-b7b7d2bf82-p2@usenetarchives.gap> <gap-b7b7d2bf82-p3@usenetarchives.gap> <gap-b7b7d2bf82-p4@usenetarchives.gap>`

```

While stranded on information super highway Kevin Digweed wrote:
->sh··.@flo··t.com (Hemant Shah) wrote:
->> IBM COBOL
->> set supports shared library, no more int code :-),

->FYI. Micro Focus products have supported native code generation for many many
->years now.

We use MF COBOL on HP-UX, AIX, Unixware, and MF tech support has always
told me that you cannot create shared library of COBOL modules
using MF COBOL.


->> and I can use a any
->> Unix debugger I like (no more animator :-)).

->You *don't* like animator ? OK. Well, FYI, you can also use 'dbx' with Micro
->Focus COBOL programs on AIX. Try:

->$ cob -xg file.cbl
->$ dbx file

->(dbx) stop in file
->(dbx) r

I have tried using dbx on AIX, but I cannot query/edit variables, I can
only step through it, I also found that many times dbx would highlight
wrong COBOL source line.

I still cannot use dbx/gdb/adb etc in HP-UX and Unixware.


->> With MF COBOL there were some errors which MF COBOL
->> ignored, but Main Frame COBOL complained.

->Did you report these problems to Technical Support ?

Yes we have (I personaly have not, but other programmers have).


->> e.g.: They do not add symbol information in the object files so I cannot
->> use other Unix debugger to debug the COBOL program. Our application
->> contains mixture of C and COBOL programs and it is hard to debug.

->Not sure what you mean. See the above comment about using dbx with MF COBOL.
->Also, if you linked your C functions into a RTS and executed your COBOL code
->with that RTS and include the +A switch in the $COBSW environment variable,
->the animator is automatically entered when an animatable program is executed,
->*even* if the RTS is running under a C debugger - you have two debuggers
->coexisting - the Unix debugger for your C code and static linked MF COBOL and
->the animator (which knows about COBOL) for your COBOL code. It's actually a
->very powerful system (I sometimes use it when debugging our COBOL RTS itself).

As I mentioned earlier, I do not like animator, unlike other Unix debugger
animator does not run as a seperate process, and many times we have found
that if the COBOL programs have bug, then while animating the program
animator walks over COBOL code and crashes. Many times we have found that
the program would execute O.K., but while animating it it would crash.

I have also talked with MF tech support about supporting Unix debuggers
and their response was that most of the users love animator and they have
no plan to support other debuggers.


->> Constraints on file name length:
->> e.g. cob -C DIR=/some/file/name
->> file name cannot be more than certain character, I forgot the exact
->> size, we ended up naming file like "./conf/cp.ol.gn.dir"
->>
->> Instead of "compile_online_general.directives"

->Long filename support has also been in our AIX product for quite a while now
->(years, I believe - I can't give you an exact time/version).

But not on other Unix platforms. Why doesn't MF write all Unix versions
of COBOL compiler from same soource code.

IBM's compiler (according to IBM) for MVS, AIX, OS/2 is built from same
source code. So far IBM has been very receptive to our comments.
Hopefully IBM will port their compiler to other Unix versions soon.


->Cheers, Kev.

->--
->Kevin. Advancing all electric at Micro Focus, Newbury, UK. (k.··.@mfl··o.uk)
->These views are strictly my own. I doubt that anyone else would want them.
->STUFF FOR SALE: Here!



                                      /-------------------¥    ^‾‾‾‾^
                                      |TECHNOLOGY         |    |    |
                                      |No place for wimps |   o|-OO-|o
                                      |          -Dilbert |--- | () |
                                      ¥-------------------/    |    |
---------------------------------------------------------------------------
Hemant Shah                      | I haven't lost my mind,
LIDP, Inc.                       | it's backed up on tape somewhere.
Voice: (708) 960 0133 Ext: 64    |
Fax: (708) 960 0717              | Above opinions are mine only. Others can
E-mail: Personal - sh··.@xn··t.com | have their own.
        Work - sha··.@li··p.com   | 
WWW: http://www.xnet.com/‾shah   | DO NOT SEND UNSOLICITED E-MAIL
--------------------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: Is MF COBOL unable to run large applications?

_(reply depth: 5)_

- **From:** "gary r. hook" <ua-author-8937134@usenetarchives.gap>
- **Date:** 1996-05-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b7b7d2bf82-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b7b7d2bf82-p5@usenetarchives.gap>`
- **References:** `<4mv81s$4s1@bulldns.bull.fr> <gap-b7b7d2bf82-p2@usenetarchives.gap> <gap-b7b7d2bf82-p3@usenetarchives.gap> <gap-b7b7d2bf82-p4@usenetarchives.gap> <gap-b7b7d2bf82-p5@usenetarchives.gap>`

```

Hemant Shah wrote:
› 
› While stranded on information super highway Kevin Digweed wrote:
…[9 more quoted lines elided]…
›    using MF COBOL.

Then MF Tech Support doesn't know what it's talking about, because
MF 3.2 added this capability on AIX. I've done it, it _is_
possible.


________________________________________________________________________
Gary R. Hook                       | I don't want you to think of art as
AIX Kernel Development             | a little whipped cream on the cake
IBM Corporation, Austin, Texas     | of life.  It's more like steak and
The above opinions are all mine.   | potatoes.         -- Dallas Willard
```

###### ↳ ↳ ↳ Re: Is MF COBOL unable to run large applications?

_(reply depth: 6)_

- **From:** "veeru mehta" <ua-author-13876829@usenetarchives.gap>
- **Date:** 1996-06-11T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b7b7d2bf82-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b7b7d2bf82-p6@usenetarchives.gap>`
- **References:** `<4mv81s$4s1@bulldns.bull.fr> <gap-b7b7d2bf82-p2@usenetarchives.gap> <gap-b7b7d2bf82-p3@usenetarchives.gap> <gap-b7b7d2bf82-p4@usenetarchives.gap> <gap-b7b7d2bf82-p5@usenetarchives.gap> <gap-b7b7d2bf82-p6@usenetarchives.gap>`

```

Gary R. Hook wrote:
› 
› Hemant Shah wrote:
…[15 more quoted lines elided]…
› possible.

Same goes for HP UX.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
