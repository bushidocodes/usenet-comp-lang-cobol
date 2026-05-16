[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable length Params in Linkage section

_16 messages · 10 participants · 2002-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`VSAM, files, sorting`](../topics.md#files)

---

### Variable length Params in Linkage section

- **From:** marydegallo@yahoo.com (Mary Degallo)
- **Date:** 2002-04-24T12:05:15-07:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<f0bf00c.0204241105.4467dc29@posting.google.com>`

```
Hi !

   LINKAGE SECTION. 
   01 PARAM1     PIC X(48). 
   01 PARAM2     PIC X(48). 

   PROCEDURE DIVISION USING PARAM1, PARAM2. 


   I have this above Code; 
   on AS400 each PARAM is being given as 48 characters. 

   Fixed length parameters. 

   I donot want to do it like that. 
   I want to have a single string. Length is immaterieal. 
   Variable length. 

   And I will parse the parameter(s) in my Code. 

   Is it possible? 
   How do I do that?

   I will appreciate the help forwarded. 

    (Pls send a copy of the response to my eMail address: MaryDeGallo@yahoo.com)
   thanx,
-Mary
```

#### ↳ Re: Variable length Params in Linkage section

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-04-24T15:34:16-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aa74sg$5p0$1@nntp9.atl.mindspring.net>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com>`

```
    LINKAGE SECTION.
    01 PARAM1.
         05 Each-Byte1 occurs 1 to 48 times     PIC X.
    01 PARAM2.
        05 Each-Byte2 occurs 1 to 48 times     PIC X.

    PROCEDURE DIVISION USING PARAM1, PARAM2.

If you KNOW the length when you PASS the parameter, then add an Occurs
Depending On phrase.
```

#### ↳ Re: Variable length Params in Linkage section

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-04-24T21:45:18+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<i56ecu034qis327uu4mpidsm3crvvlv1lq@4ax.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com>`

```
On 24 Apr 2002 12:05:15 -0700, marydegallo@yahoo.com (Mary Degallo)
wrote:

>Hi !
>
…[5 more quoted lines elided]…
>
do 
linkage...
01 param-size pic 9(4).
01 param-all pic x(5000).

procedure using param-size param-all.

aaa.
move param-all(1:param-size) to working-storage-variable.

then only work with this working-storage-variable.


Note: the program that calls the COBOL program MUST pass
the size of the string (param-all).

FF


PS. No email responses. only news groups.
```

##### ↳ ↳ Re: Variable length Params in Linkage section

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-04-25T10:17:17+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3CC7C99D.5CCAFB15@Azonic.co.nz>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <i56ecu034qis327uu4mpidsm3crvvlv1lq@4ax.com>`

```
Frederico Fonseca wrote:

> do
> linkage...
…[11 more quoted lines elided]…
> the size of the string (param-all).

Only because you have designed it that way.  It can be done without a
specific size being passed as long as there is some mechanism for
stopping the subroutine accessing data outside the actual data area of
the caller.

For example a null (x"00") could be used as a string terminator to
indicate not to access beyond that.  As long as the string parameter is
read-only then there should be no problem being passed various data
lengths.

However if the routine is to be written to be the subroutine then (as in
all languages) you had beeter be certain that the caller has created an
actual data area large enough to take whatever the subroutine will
write.

eg routine:
       LINKAGE SECTION.
       01  Param                PIC X(5000).
       PROCEDURE DIVISION USING Param.
           UNSTRING Param
               DELIMITED BY x"00"
               INTO WS-Area
           ...

caller:
       01  Small-string         PIC X(10) VALUE "Small" & x"00".
           CALL "routine" USING Small-String

This should be no problem (YMMV depending on hardware checking).

If, however, the routine does:

        MOVE "X"       TO Param

Then the program will overwrite the 10 byte Small-String (with 'X' and 9
spaces) and then overwite the next 4990 bytes in the calling program
with spaces causing severe disruption.
```

###### ↳ ↳ ↳ Re: Variable length Params in Linkage section

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-04-25T09:20:25+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<q0ffcuoe27jf49jo9r2hrmkdhbru7u5io2@4ax.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <i56ecu034qis327uu4mpidsm3crvvlv1lq@4ax.com> <3CC7C99D.5CCAFB15@Azonic.co.nz>`

```
On Thu, 25 Apr 2002 10:17:17 +0100, Richard Plinston
<riplin@Azonic.co.nz> wrote:


>
>However if the routine is to be written to be the subroutine then (as in
…[15 more quoted lines elided]…
>           CALL "routine" USING Small-String
Have you tried this code.
Do so if not and then came back.


FF
```

###### ↳ ↳ ↳ Re: Variable length Params in Linkage section

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-04-26T07:37:15+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3CC8F59A.B0AC34E2@Azonic.co.nz>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <i56ecu034qis327uu4mpidsm3crvvlv1lq@4ax.com> <3CC7C99D.5CCAFB15@Azonic.co.nz> <q0ffcuoe27jf49jo9r2hrmkdhbru7u5io2@4ax.com>`

```
Frederico Fonseca wrote:
> >caller:
> >       01  Small-string         PIC X(10) VALUE "Small" & x"00".
> >           CALL "routine" USING Small-String

> Have you tried this code.
> Do so if not and then came back.
 
Yes I have tried it - what is your point ?
```

#### ↳ Re: Variable length Params in Linkage section

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2002-04-24T22:11:13+01:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000001cf.08b88155@ieee.org>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com>`

```
Mary,

> Fixed length parameters. 
> 
…[4 more quoted lines elided]…
>    And I will parse the parameter(s) in my Code.

Don't be silly. This costs CPU time. The point about developing in Cobol 
is that it runs extremely fast. If you spend your time decoding messages 
rather than acting upon them, you'll begin to achieve MS execution times, 
and that's no good for your users.

Sigh. But if you insist, you could define a single string, length 96, 
redefined as 96 bytes (PIC X(96)) and do your own thing.

---

Doug

dwscott@ieee.org
```

##### ↳ ↳ Re: Variable length Params in Linkage section

- **From:** Edward Reid <edward@paleo.org>
- **Date:** 2002-04-25T09:53:53-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<01HW.B8ED82B100C36C130DB3DC60@news-east.usenetserver.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <VA.000001cf.08b88155@ieee.org>`

```
On Wed, 24 Apr 2002 17:11:13 -0400, Doug Scott wrote
> Don't be silly. This costs CPU time. The point about developing in Cobol 
> is that it runs extremely fast.

It's possible to develop COBOL programs that run extremely fast, but 
the language is certainly *not* very helpful in this respect. There are 
all kinds of constructs in COBOL that allow you to waste a lot of CPU 
time, and you won't have any idea what's happening if you have no 
background in assembler (on at least some system). I've seen many quite 
competent COBOL programmers who can't figure out where the CPU time is 
going if their lives depend on it.

What saves them -- and why I call them quite competent nonetheless -- 
are two things. One is that the applications they are developing don't 
often lead them to do severely CPU-expensive things and don't generally 
require much algorithmic analysis. The other is that CPUs have become 
so powerful that large organizations find it easier to throw a lot of 
CPU at the problem than to find programmers who can optimize for CPU 
time.

> If you spend your time decoding messages 
> rather than acting upon them, you'll begin to achieve MS execution times, 
> and that's no good for your users.

If the code executes a thousand times per second, then by all means use 
code which optimizes the CPU time.

If the code executes once a day, then by all means use code which 
optimizes the programmer's time.

Somewhere in between lies the break-even point. Most of the time, 
nowadays, the answer is to optimize programmer time, design programs 
well to avoid inefficiencies that are hard to fix, and then consider 
CPU time when and where necessary.

Efficiency means various things, but on an average day it's the 
programmer efficiency that's most important.

Edward Reid
```

###### ↳ ↳ ↳ Re: Variable length Params in Linkage section

- **From:** docdwarf@panix.com
- **Date:** 2002-04-25T10:43:48-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aa94n4$pm$1@panix1.panix.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <VA.000001cf.08b88155@ieee.org> <01HW.B8ED82B100C36C130DB3DC60@news-east.usenetserver.com>`

```
In article <01HW.B8ED82B100C36C130DB3DC60@news-east.usenetserver.com>,
Edward Reid  <edward@paleo.org> wrote:

[snip]

>Efficiency means various things, but on an average day it's the 
>programmer efficiency that's most important.

This is the point I was trying to reach... in an email I sent on this 
subject I stated it thusly:

--begin quoted text:


 Exactly... for the comfort and ease of all involved (especially the one
 who gets the 3:am Prod Support call) the code should read:

 LINKAGE SECTION.
      COPY LINKPARM.
 ...
 WORKING-STORAGE SECTION.
 ...
      COPY WSLKPARM.
 ...
 PROCEDURE DIVISION USING SYSTEMWIDE-LINKPARMS.
 ...
      MOVE SYSTEMWIDE-LINKPARMS  TO  WS-SYSTEMWIDE-LINKPARMS.

 ... or so I was taught that The Professionals do it.

--end quoted text

DD
```

#### ↳ Re: Variable length Params in Linkage section

- **From:** docdwarf@panix.com
- **Date:** 2002-04-24T20:19:45-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aa7i31$3tm$1@panix1.panix.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com>`

```
In article <f0bf00c.0204241105.4467dc29@posting.google.com>,
Mary Degallo <marydegallo@yahoo.com> wrote:
>Hi !
>
…[16 more quoted lines elided]…
>   And I will parse the parameter(s) in my Code. 


Outside of amusing yourself - essentially writing 'Look, Ma, I'm a
Programmer!' code, *always* a dangerous thing - would you be so kind as to
state some of the advantages of doing it the way you want to?

>    (Pls send a copy of the response to my eMail address: MaryDeGallo@yahoo.com)
>   thanx,

Post it here, read it here.

DD
```

##### ↳ ↳ Re: Variable length Params in Linkage section

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-25T01:18:24+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<APIx8.9198$d17.390006@typhoon.austin.rr.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <aa7i31$3tm$1@panix1.panix.com>`

```
Actually, I do some of that here, though in a slightly more sophisticated
way.
I simply pass the address in with the Linkage section though.

I often have to deal with an unknown number (to the called program) of
arguments.
In a most un-COBOLish way, I simply pass one argument, and do some 'pointer
arithmetic'
till I find a null, and then I have the end of my list. It is much simpler
to code and understand than
the alternative of passing in several hundred arguments, and copying them in
till I
hit a NULL. Then copying them back to the linkage section when it is time to
return.


-Paul

<docdwarf@panix.com> wrote in message news:aa7i31$3tm$1@panix1.panix.com...
> In article <f0bf00c.0204241105.4467dc29@posting.google.com>,
> Mary Degallo <marydegallo@yahoo.com> wrote:
…[25 more quoted lines elided]…
> >    (Pls send a copy of the response to my eMail address:
MaryDeGallo@yahoo.com)
> >   thanx,
>
> Post it here, read it here.
>
> DD
```

###### ↳ ↳ ↳ Re: Variable length Params in Linkage section

- **From:** docdwarf@panix.com
- **Date:** 2002-04-24T22:06:21-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aa7oat$ik5$1@panix1.panix.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <aa7i31$3tm$1@panix1.panix.com> <APIx8.9198$d17.390006@typhoon.austin.rr.com>`

```
In article <APIx8.9198$d17.390006@typhoon.austin.rr.com>,
Paul Raulerson <praulerson@NO-SPAM.hot.rr.com> wrote:

[snippage]

>I often have to deal with an unknown number (to the called program) of
>arguments.

'Have to' catches my eye here... Mr Raulerson, did you design it this way?  
If so, for what reason... if no then, given the alternative, would you do 
so again?

DD

><docdwarf@panix.com> wrote in message news:aa7i31$3tm$1@panix1.panix.com...
>> In article <f0bf00c.0204241105.4467dc29@posting.google.com>,
…[34 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Variable length Params in Linkage section

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-04-25T11:50:21+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<14Sx8.9690$d96.4374@nwrddc04.gnilink.net>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <aa7i31$3tm$1@panix1.panix.com> <APIx8.9198$d17.390006@typhoon.austin.rr.com> <aa7oat$ik5$1@panix1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:aa7oat$ik5$1@panix1.panix.com...
> In article <APIx8.9198$d17.390006@typhoon.austin.rr.com>,
> Paul Raulerson <praulerson@NO-SPAM.hot.rr.com> wrote:
…[8 more quoted lines elided]…
> so again?

I do not find this weird at all; I do it all the time.

If you want a library call or "internal utility" usable by many many
programs or jobs,  it only stands to reason that some programs may need
extra or other options than needed by some other programs.

Look at a simple example: such a utility program may have a "purge" or
"update" option in addition to a report option. You might run the job ...

EXEC PGM=FOO, PARM='REPORT'      << report only
or
EXEC PGM=FOO,PARM='REPORT,UPDATE'  << report and update

Variable number of options: Reasonable, yes?

We might be getting into semantics here about what is an 'argument' versus
what is an 'option' ... I see no reason for a variable number of 'arguments'
mostly because it's darn near impossible (for me) to set up the calls and
handle the parameter chain. (This refers to CALLs rather than EXECs. But as
I understand it, walking the argumment chain in linkage is possible).

MCM
```

###### ↳ ↳ ↳ Re: Variable length Params in Linkage section

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2002-04-25T09:29:21-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aa90bh$gab$1@panix1.panix.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <APIx8.9198$d17.390006@typhoon.austin.rr.com> <aa7oat$ik5$1@panix1.panix.com> <14Sx8.9690$d96.4374@nwrddc04.gnilink.net>`

```
In article <14Sx8.9690$d96.4374@nwrddc04.gnilink.net>,
Michael Mattias <michael.mattias@gte.net> wrote:
><docdwarf@panix.com> wrote in message news:aa7oat$ik5$1@panix1.panix.com...
>> In article <APIx8.9198$d17.390006@typhoon.austin.rr.com>,
…[24 more quoted lines elided]…
>Variable number of options: Reasonable, yes?

The picayune rebuttal would be 'Reasonable, no; it violates the dictum of 
'Thou Shalt Not Have A Report That Updates'... but such things aside your 
program can perform only (m) functions, each of which is related to a parm 
of (n) characters.  Variable, yes... unknown, no.

>
>We might be getting into semantics here about what is an 'argument' versus
>what is an 'option'

Perhaps there might be a confusion between 'variable' and 'unknown'.

DD
k
```

###### ↳ ↳ ↳ Re: Variable length Params in Linkage section

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-04-25T02:30:33+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3CC769C0.97188600@shaw.ca>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <aa7i31$3tm$1@panix1.panix.com> <APIx8.9198$d17.390006@typhoon.austin.rr.com>`

```


Paul Raulerson wrote:

> Actually, I do some of that here, though in a slightly more sophisticated
> way.
…[12 more quoted lines elided]…
>

If only <G>. Extending your description and using OO COBOL -

Sending Class :
- create a collection, CollectionA, containing the individual arguments as
separate elements. Invoke  the receiver :-

 invoke ReceivingClass "thismethodX" using CollectionA

Receiving Class:
Working-storage section.
01 os-CollectionC                                object reference.

method-id. "thisMethodX".
   Linkage section.
    01 lnk-CollectionB                object reference.
    Procedure Division using lnk-CollectionB

    set os-CollectionC to lnk-CollectionB
    invoke lnk-CollectionB/os-CollectionC "getsize" returning thisSize
            (it automatically knows its own size)

.........then you go on from there ..........

Actually if I'm only going to action the recipient collection in the one method,
I don't even bother to set up the reference for os-CollectionC - the latter is
only necessary globally if it is referenced in several different methods.

Now unlike what you are doing there is no need to return the list of changed
arguments back through linkage. CollectionA, lnk-CollectionB or os-CollectionC
are all references to the same object, each referencing the one object in its
current state..

'Course you knew this, 'cos you use other OO languages. <G>

Jimmy
```

###### ↳ ↳ ↳ Re: Variable length Params in Linkage section

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praulerson@NO-SPAM.hot.rr.com>
- **Date:** 2002-04-25T03:09:34+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<OrKx8.9451$d17.412691@typhoon.austin.rr.com>`
- **References:** `<f0bf00c.0204241105.4467dc29@posting.google.com> <aa7i31$3tm$1@panix1.panix.com> <APIx8.9198$d17.390006@typhoon.austin.rr.com> <3CC769C0.97188600@shaw.ca>`

```
<grin> And given the choice I would have done it exactly that way. (nice
code Jimmy... :)
Unfortunately, the inbound argument list is from two other languages, PERL,
and C.
What comes in is just a set of pointers.

In fact, that is exactly what you get with the copying thing, except you
cannot use normal
operations like ADD on a linkage section variable. What a nuisance.

-Paul

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3CC769C0.97188600@shaw.ca...
>
>
> Paul Raulerson wrote:
>
> > Actually, I do some of that here, though in a slightly more
sophisticated
> > way.
> > I simply pass the address in with the Linkage section though.
…[3 more quoted lines elided]…
> > In a most un-COBOLish way, I simply pass one argument, and do some
'pointer
> > arithmetic'
> > till I find a null, and then I have the end of my list. It is much
simpler
> > to code and understand than
> > the alternative of passing in several hundred arguments, and copying
them in
> > till I
> > hit a NULL. Then copying them back to the linkage section when it is
time to
> > return.
> >
…[24 more quoted lines elided]…
> Actually if I'm only going to action the recipient collection in the one
method,
> I don't even bother to set up the reference for os-CollectionC - the
latter is
> only necessary globally if it is referenced in several different methods.
>
> Now unlike what you are doing there is no need to return the list of
changed
> arguments back through linkage. CollectionA, lnk-CollectionB or
os-CollectionC
> are all references to the same object, each referencing the one object in
its
> current state..
>
…[4 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
