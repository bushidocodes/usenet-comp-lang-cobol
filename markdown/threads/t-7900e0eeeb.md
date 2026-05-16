[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OO Exception Handling

_35 messages · 7 participants · 2002-08_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### OO Exception Handling

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-10T22:10:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5590B9.B38DF038@shaw.ca>`

```
Donald and Grinder,

Thought we should make this a specific thread. Don, wasn't clear where
you were describing EXIT METHOD to Grinder - so did the following to
clarify that which I believed to happen, in my own mind.

EXIT METHOD is an implied instruction prior to the line 'End Method' if
not explicitly included. Much of the code we see as examples, has as a
'pair',  'Exit Method' and 'End Method" - but in fact the 'Exit Method',
most of the time, is superfluous and can create the condition you see in
Method 4 Para-4A below, (assuming you are using paragraphs). Plus it's
also part of the category 'red tape', if you want to keep the coding
short and clear.

It does have ONE advantage, and I'm guessing this also applies to
Fujitsu. You can't PAUSE the Animator on 'End Method', but you can pause
on 'Exit Method' if it is the preceding line. As the final 'instruction'
line of a method the pause then allows you to query any variables or
objects that you are suspicious about in the Method.

Hopefully following shows all possible permutations - any comments ?

The GOOD NEWS. Bill may recall that I wrote a while back that using
'EXIT PROGRAM' just didn't do anything for me. God knows what I did, and
haven't got the code, but it led me down the wrong path.

EXIT PROGRAM or GOBACK will do EXACTLY the same as Procedural as you can
see in Method 4 below. You'll see I've deliberately commented out the
explict EXIT METHOD in Method 4, to prove it gets back to the 'caller'
DIRECTLY. (Obviously if Paragraph-4A didn't indicate some sort of error,
then Method 4 would function exactly like Method 3).

That's a big step forward in my mind. So if I go back to my original
example of nested Classes and Methods - Method3B WILL  (using GOBACK)
cause an exit from Class 3 - and we are back in Class 2 Method 2C.

With that concept firmly entrenched - now I put on the thinking cap, and
perhaps using the existing Net Express Exception Class, containing
callbacks, exception objects etc. - I can start to figure a way to tell
Class 2, 'You should be doing an automatic  GOBACK to Class 1". (????).

The ideal is to make any Exception Handling 'dual' feature, (and is
available within Net Express). Currently we can't cover fatal errors, (
messages to wrong objects, a field contains non-numerics etc.), and the
Runtime kicks in with a Messgebox and STOPS RUN. However if Exceptions
can be made to operate in two ways :-

1- 'semi-failure' - can't provide records for a list, missing info
invoking other languages etc., then we can signal via a GOBACK 'Get out
of this sub-suite' and let the user select one of the other 19 items
from the Master Menu that we know still work. (Could also be applied to
ISAM crashed indices.)

2- 'success/failure' - when reading a File/Table - did we establish
RecordFound/RecordNotFound - this info needs to be fed back to the
invoking class/method.

BTW - Do you have an Exception Handler in Fujitsu ?

Jimmy

*>----------------------------------------------------------
Program-id. excptn01.
Class-control.              Program02 is class "excptn02"
Procedure Division.
invoke Program02 "begin"
STOP RUN.
*>----------------------------------------------------------
*>-------------------excptn02.cbl-----------------------------

Class-id.        Exception02
                 inherits from Base.

Class-control.   Exception02 is class "excptn02".
*>--------------------------------------------------------------
FACTORY.
*>--------------------------------------------------------------
Method-id. "begin".
*>--------------------------------------------------------------
*> This doesn't have an EXIT METHOD - it's implied

Procedure Division.
 invoke self "Method1"
 invoke self "Method2"
 invoke self "Method3"
 invoke self "Method4"
End Method "begin".
*>--------------------------------------------------------------
Method-id. "Method1".
*>--------------------------------------------------------------
*> This has no EXIT METHOD - it's implied

Procedure Division.
    display "This is Method1 Line 1A"
    display "This is Method1 Line 1B"
End Method "Method1".

*> This Method displays  :-
*> This is Method1 Line 1A
*> This is Method1 Line 1B
*> and then automatically Exits
*>--------------------------------------------------------------
Method-id. "Method2".
*>--------------------------------------------------------------
*> This has an EXPLICIT EXIT after the 'mainline'

Procedure Division.
    perform PARA-2A
    perform PARA-2B
    .
EXIT METHOD.

PARA-2A.
display "This is Method2, Paragraph 2A".

PARA-2B.
display "This is Method2, Paragraph 2B".

End Method "Method2".

*> This Method displays and exits :-
*> This is Method2, Paragraph 2A
*> This is Method2, Paragraph 2B

*>--------------------------------------------------------------
Method-id. "Method3".
*>--------------------------------------------------------------
*> Note the EXIT METHOD, immediately prior to "End Method"

Procedure Division.
    perform PARA-3B *> I've switched the perform paragraphs
    perform PARA-3A
    .
PARA-3A.
display "This is Method3, Paragraph 1".

PARA-3B.
display "This is Method3, Paragraph 3B".
display "I don't do Method3 Paragraph 3A"

EXIT METHOD.
End Method "Method3".

*> This Method displays and exits :-
*> This is Method3, Paragraph 3B
*> I don't do Method3 Paragraph 3A

*>--------------------------------------------------------------
Method-id. "Method4".
*>--------------------------------------------------------------
*> Testing for EXIT PROGRAM or GOBACK, but not using Exception
*> Handling techniques. Also note the EXIT PROGRAM/GOBACK works,
*> even without an explicit EXIT METHOD

Procedure Division.
    perform PARA-4A
    perform PARA-4B
    .
*> EXIT METHOD. I've deliberately commented this out to check
*>                          the GOBACK

PARA-4A.
display "This is Method4, Paragraph 4A".
display "Becuase of GOBACK/EXIT - I don't do Method 4 Para 4B"
*>EXIT PROGRAM.
 GOBACK.

PARA-4B.
display "This is Method4, Paragraph 4B".

End Method "Method4".

*> This Method displays
*> This is Method4, Paragraph 4A
*> Becuase of GOBACK/EXIT - I don't do Method 4 Para 4B

*> Then using either EXIT PROGRAM/GOBACK, via the Animator,
*> I see it takes me back to STOP RUN in the trigger program

*>--------------------------------------------------------------
END FACTORY.
*>--------------------------------------------------------------
OBJECT.         *> Don't need either
END OBJECT.     *> of these lines for this demo
*>--------------------------------------------------------------
End CLASS Exception02.
*>--------------------------------------------------------------
```

#### ↳ Re: OO Exception Handling

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-13T22:43:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D598D16.9905DC31@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca>`

```


"James J. Gavan" wrote:

> Donald and Grinder,
>

This is a follow up to my previous. Recall I wrote EXIT PROGRAM/GOBACK
didn't do it for me in OO - I was right. It did in the methods I showed -
BUT not in the following sequence, where I've introduced a Method 5 :-

*>---------------------------------------------------------------
Method-id. "begin".
*>---------------------------------------------------------------
Procedure Division.
 invoke self "Method1"
 invoke self "Method2"
 invoke self "Method3"
 invoke self "Method4"
 invoke self "Method5"
End Method "begin".
*>---------------------------------------------------------------
Method-id. "Method4".
*>---------------------------------------------------------------
Procedure Division.
    perform PARA-4A
    perform PARA-4B
    .
 EXIT METHOD.

PARA-4A.
display "This is Method4, Paragraph 4A".
display "Because of GOBACK/EXIT - I don't do Method 4 Para 4B"
GOBACK.

PARA-4B.
display "This is Method4, Paragraph 4B".

End Method "Method4".
*>--------------------------------------------------------------
Method-id. "Method5".
*>---------------------------------------------------------------
Procedure Division.
    display "I'm in Method 5"
End Method "Method5".
*>---------------------------------------------------------------

I automatically get the display from Method 5, (GOBACK or no GOBACK) - oh
hum, back to the drawing board. That's been my problem all along; *every*
Method will action all statements until it drops through to End Method,
unless you are testing for some condition and explicity instruct it to EXIT
METHOD.

Jimmy
```

##### ↳ ↳ Re: OO Exception Handling

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-14T03:06:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajd33502tvi@enews4.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3D598D16.9905DC31@shaw.ca...
>
>
…[5 more quoted lines elided]…
> This is a follow up to my previous. Recall I wrote EXIT
PROGRAM/GOBACK
> didn't do it for me in OO - I was right. It did in the
methods I showed -
> BUT not in the following sequence, where I've introduced a
Method 5 :-
>
>
*>-------------------------------------------------------------
```

###### ↳ ↳ ↳ Re: OO Exception Handling

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-15T01:43:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5B08B7.1446FEF5@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com>`

```


Grinder wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
> news:3D598D16.9905DC31@shaw.ca...
…[76 more quoted lines elided]…
> get invoked?

That's Step 2. Having initially dismissed my earlier assumption that
GOBACK wouldn't work (purely in OO Class syntax), and now confirmed it
doesn't work - now I'll move over to dabbling with the existing
Exception Handler. What hasn't yet twigged is that you can use features
to propagate up through a nested series of classes/methods, (and even
much more comprehensively in the draft Standard) - but I'm still looking
for the Nirvana, which avoids the necessity of individually checking
within each method, 'in the chain', with an automatic feature that takes
you straight back to Class 1 Method 1.

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 4)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-08-14T22:43:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KuE69.6405$2T2.1121915@news20.bellglobal.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca>`

```

"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3D5B08B7.1446FEF5@shaw.ca...
>
>
…[93 more quoted lines elided]…
>

What is wrong with "EXIT METHOD", or "STOP RUN" if you want an abort?

Donald
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 5)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-15T10:25:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajgh5q020hg@enews2.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com>`

```
> What is wrong with "EXIT METHOD", or "STOP RUN" if you want
an abort?

Can't speak for Jimmy, but both of these have problems
(conceptually) if they work as I think they do.

EXIT METHOD
This would just exit the current method -- wouldn't execution
resume at the next statement after the invocation of the exited
method?

STOP RUN
Does this stop the entire process?  Since there may be cleanup
to be done in the calling methods, they would be denied that
opportunity.  In short, the method does not have enough context
to decide if the error is fatal to the run.

I hope I properly understand the nature of these statements.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-08-15T11:05:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajgjfv$3rr$1@nntp9.atl.mindspring.net>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com>`

```
Some of this MIGHT be fixed by the (still under development) FINALIZER
functionality.  This is an "auto-method" that gets  control as an object
instance is "going away".
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 6)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-08-15T12:36:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uQQ69.6937$2T2.1234863@news20.bellglobal.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:ajgh5q020hg@enews2.newsguy.com...
> > What is wrong with "EXIT METHOD", or "STOP RUN" if you want
> an abort?
…[8 more quoted lines elided]…
>

Yes.

> STOP RUN
> Does this stop the entire process?  Since there may be cleanup
…[3 more quoted lines elided]…
>

Stop run is suppose to end the run unit entirely, and do all the garbage
collections required to clean up stray methods, etc.  Certainly, one can
take corrective action, like rebuilding an Isam file on a 39 error.  In
fact, on "39" errors, I bring up a screen and give the choice of abort (stop
run), a rebuild, or start a new empty file. Of the latter two, the rebuild
is another method, while the starting of a new file simply opens the file in
output, closes it, and re-opens in IO mode.

"GOBACK" is neither of the above.  "GOBACK" exits to the higher level run
unit, so if I am in a Cobol program that calls a sub-program that invokes a
method, then the GOBACK goes to the higher level run unit (it is a
subroutine return, not a method exit). The code after the invocation is
never reached.  GOBACK is for subroutine and mainline use only, IMO. I would
never use "GOBACK" in a method.  I would use either stop run to abort
everything, exit method to return an error to the invoking level, or simply
correct the problem and continue.

END METHOD has nothing whatsoever to do with any of the above.  It is simply
the end of the source module the same as "IDENTIFICATION DIVISION" or
"METHOD-ID." is the start.  It does not get compiled, per se, it is a
delimiter. Since the spec states that falling off the end of a program does
a return of some sort, then that is what happens when you hit the "END
METHOD" statement.  Falling off the end of a regular Cobol program does a
similar thing, regardless of whether you code an "END PROGRAM or not.  The
main reason it is required is that most OOP source has more than one
"program" in it. I think an "END PROGRAM" is required in non-oop when you
have more than one program in a source code file as well, but have never
done it, so am not sure.

Donald


Donald

> I hope I properly understand the nature of these statements.
>
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 7)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-15T12:20:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajgnsj0r6a@enews1.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com>`

```
> Stop run is suppose to end the run unit entirely, and do all
the garbage
> collections required to clean up stray methods, etc.
Certainly, one can
> take corrective action, like rebuilding an Isam file on a 39
error.  In
> fact, on "39" errors, I bring up a screen and give the choice
of abort (stop
> run), a rebuild, or start a new empty file. Of the latter
two, the rebuild
> is another method, while the starting of a new file simply
opens the file in
> output, closes it, and re-opens in IO mode.

So if "method1" invokes "method2"--perhaps in another object,
and that method does a STOP RUN, is method1's execution stopped
as well?

> "GOBACK" is neither of the above.  "GOBACK" exits to the
higher level run
> unit, so if I am in a Cobol program that calls a sub-program
that invokes a
> method, then the GOBACK goes to the higher level run unit (it
is a
> subroutine return, not a method exit). The code after the
invocation is
> never reached.  GOBACK is for subroutine and mainline use
only, IMO. I would
> never use "GOBACK" in a method.

EXIT METHOD, then, returns execution to who[m]ever has invoked
that method?

Sorry to be so unitiated, but can you describe a few terms, and
how they relate to each other:

method
run unit
subroutine
sub-program

I'm likely confusing myself (an others) because of
inappropriately transplanted terminology.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 8)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-08-15T16:02:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QPT69.5342$DO6.1502516@news20.bellglobal.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com> <ajgnsj0r6a@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:ajgnsj0r6a@enews1.newsguy.com...
> > Stop run is suppose to end the run unit entirely, and do all
> the garbage
…[14 more quoted lines elided]…
> as well?

Yes, exactly so.  STOP RUN is an absolute abort, there is nothing more I can
do, end it now. According to spec, it should do everything required to clean
up memory, release any file/record locks, find and stop child processes,
etc., etc., etc.  Even for multi threaded stuff within the run unit.

>
> > "GOBACK" is neither of the above.  "GOBACK" exits to the
…[13 more quoted lines elided]…
>

Yes. It will return to the statement after the invoke.

> Sorry to be so unitiated, but can you describe a few terms, and
> how they relate to each other:
>
> method

Code with a "method id" that works ... <G>.  A procedure within an object.

> run unit

A command line execution.  IE-If I start a second Cobol.EXE from within a
first, that is a second run unit. If, within the run, I start ten threads,
they are all still part of the run unit.  That may be a bit different on a
mainframe, but I expect it is similar ... a second job would be a second run
unit. One execute at the OS level = one run unit.

> subroutine

called routine, not invoked.  Same as most languages.

> sub-program

Same thing as a subroutine, really, though I tend to use the term for
complete modules that do not take arguements.  Any Cobol program can also be
called as a subroutine from another, provided that you use a GOBACK instead
of a STOP RUN.  The only differnce is the linking.  GOBACK combines the
"return from subroutine" with the "stop this program" of most languages.
When you use it in an executed program, it returns to the OS as if the OS
had called it.

That is the real reason for the GOBACK ...  so that any program can be
either a program or be executed from a higher level program as a called
routine.  The exit is the same, regardless of whether the OS calls it or
another Cobol program calls it.  Source is identical, object(code) is
identical.

>
> I'm likely confusing myself (an others) because of
> inappropriately transplanted terminology.
>

<G>  I think everybody is.  I think computers are at the "Tower of Babel"
stage, and we are evolving ways to talk as we speak.

Donald
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 9)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-15T16:09:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajh5a701kb0@enews1.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com> <ajgnsj0r6a@enews1.newsguy.com> <QPT69.5342$DO6.1502516@news20.bellglobal.com>`

```
> Yes, exactly so.  STOP RUN is an absolute abort, there is
nothing more I can
> do, end it now. According to spec, it should do everything
required to clean
> up memory, release any file/record locks, find and stop child
processes,
> etc., etc., etc.  Even for multi threaded stuff within the
run unit.

There's considerable debate about a similar construct in VB --
the dreaded "End" statement.  Although I'm not as visceral as
some of my counterparts, I've found no reason to use this --
ever -- in a VB application.  Error-handling should be
constructed such that your application can terminate
"naturally."

It's my sense that this applies to OO-COBOL as well.  The
theory being, that there will only be one object (at the top of
the call stack) that has application scope.  All others, if
properly encapsulated, wouldn't have the context to make such a
global judgement call.

This is no declaration on my part though -- Does this sound
reasonable?

> > run unit
> A command line execution.  IE-If I start a second Cobol.EXE
from within a
> first, that is a second run unit. If, within the run, I start
ten threads,
> they are all still part of the run unit.  That may be a bit
different on a
> mainframe, but I expect it is similar ... a second job would
be a second run
> unit. One execute at the OS level = one run unit.

It's correct to say, then: run unit = process?

> > subroutine
> called routine, not invoked.  Same as most languages.

A subroutine, although it may be a child process, still is a
_different_ process with its own address space?

I thought as much from your usage, though I wanted to make sure
as subroutine is sometimes a generic term for functions or
methods.  Indeed, in VB for instance, a function with no return
value is a "Sub."

> > I'm likely confusing myself (an others) because of
> > inappropriately transplanted terminology.
>
> <G>  I think everybody is.  I think computers are at the
"Tower of Babel"
> stage, and we are evolving ways to talk as we speak.

More like -- "Tower of Babble"

Thanks for the run-down, I want to try to minimize my own
visible idiotry.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 10)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-08-15T18:38:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D6W69.7106$2T2.1288879@news20.bellglobal.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com> <ajgnsj0r6a@enews1.newsguy.com> <QPT69.5342$DO6.1502516@news20.bellglobal.com> <ajh5a701kb0@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:ajh5a701kb0@enews1.newsguy.com...

> > Yes, exactly so.  STOP RUN is an absolute abort, there is
> There's considerable debate about a similar construct in VB --
…[13 more quoted lines elided]…
> reasonable?

I suppose.  I only use "stop run" as an out for complete fuckups, so to
speak.

There are lots of places in data processing that ending it all is simple
prudance ...
Hardware does fail, data does get corupted.  Without it, how do you handle
"if you get here the world is about to end" errors?

If, for example, I am in a routine and find a completely unviable situation
(like
my server has just been hit by a truck) and I ask the user if I should quit,
and
the user says yes, then I think it dangerous to start setting flags for
higher levels
and return to them, trusting them to do the right thing.

It is sort of like the idea that only the boss has the right to pull a fire
alarm.

>
> > > run unit
…[10 more quoted lines elided]…
> It's correct to say, then: run unit = process?

Not absolutely quite, but almost.  There are Cobol's that can handle
multi-threading within them that may even work, at least so I hear.
Certainly if it is an OS process rather than a Cobol run time process,
then yes. (How is that for squirming?) On the PC, that is so.  Other
universes may vary.

>
> > > subroutine
…[9 more quoted lines elided]…
>

Not sure where you are going here.  A subroutine has an address space,
but your use of the word "child" makes me think in terms of parallel
processing rather than serial.  A subroutine is part of the same Turing
machine at at the logical level.  It is sequentially executed, while it is
executing
nothing else in the run unit is, and it then returns.

I think of a "child" process as something that is started, then it runs
in parallel, independently, like a device handler.

Donald
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 11)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-16T01:32:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aji69l022mg@enews2.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com> <ajgnsj0r6a@enews1.newsguy.com> <QPT69.5342$DO6.1502516@news20.bellglobal.com> <ajh5a701kb0@enews1.newsguy.com> <D6W69.7106$2T2.1288879@news20.bellglobal.com>`

```
> There are lots of places in data processing that ending it
all is simple
> prudance ...
> Hardware does fail, data does get corupted.  Without it, how
do you handle
> "if you get here the world is about to end" errors?

Kick an error, or don't handle an error that's already been
raised, at that low level.  Let the topmost -- application
level -- logic terminate the app.

>
> If, for example, I am in a routine and find a completely
unviable situation
> (like
> my server has just been hit by a truck) and I ask the user if
I should quit,
> and
> the user says yes, then I think it dangerous to start setting
flags for
> higher levels
> and return to them, trusting them to do the right thing.
>
> It is sort of like the idea that only the boss has the right
to pull a fire
> alarm.

It took me awhile to embrace it, but I've come to believe that
error raising and handling is a valuable means of
communication -- not just firewall that _has_ to be put in.

> > > > run unit
> > > A command line execution.  IE-If I start a second
Cobol.EXE
> > from within a
> > > first, that is a second run unit. If, within the run, I
start
> > ten threads,
> > > they are all still part of the run unit.  That may be a
bit
> > different on a
> > > mainframe, but I expect it is similar ... a second job
would
> > be a second run
> > > unit. One execute at the OS level = one run unit.
…[3 more quoted lines elided]…
> Not absolutely quite, but almost.  There are Cobol's that can
handle
> multi-threading within them that may even work, at least so I
hear.
> Certainly if it is an OS process rather than a Cobol run time
process,
> then yes. (How is that for squirming?) On the PC, that is so.
Other
> universes may vary.

I was under the impression, for Unix and Windows, that running
an EXE, even from another EXE, spawns a new process.  It can be
a child process, but it still has it's address space.  Child
processes has some task priority and termination conditions
imposed by the parent, but it's got its own chunk of memory.

Does run unit correlate to thread, then?  ie, multiple threads
within a process = multiple run units.  If that's the case,
then I guess it matches up to distinct points of execution.
That makes the name sound correct at any rate.

> Not sure where you are going here.  A subroutine has an
address space,
> but your use of the word "child" makes me think in terms of
parallel
> processing rather than serial.  A subroutine is part of the
same Turing
> machine at at the logical level.  It is sequentially
executed, while it is
> executing
> nothing else in the run unit is, and it then returns.
>
> I think of a "child" process as something that is started,
then it runs
> in parallel, independently, like a device handler.

Yes, that was my intent -- perhaps asynchronously is a better
generalization that parallel.  So a subroutine is a synchronous
process initiated by another process.

Hey -- thanks for all of the info.  I feel like I'm narrowing
in a bit.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-08-15T13:08:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajgqmh$1ig$1@slb0.atl.mindspring.net>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com>`

```
Donald,
  What you say about GoBack in a method may (or may not) be how some
implementation does it today - but it certainly is NOT what the draft
Standard says.

According to the draft Standard (and I think *must* implementations today) a
GoBack within a method is EXACTLY the same thing as an EXIT METHOD.

In the draft Standard both of these statements have (the compatible) RAISING
phrase which works with PROPAGATE to send "exceptions" up the application
(whether to a higher program or higher method).  This is the new "activating
process" concept.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 8)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-08-15T16:09:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QPT69.5343$DO6.1502518@news20.bellglobal.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com> <ajgqmh$1ig$1@slb0.atl.mindspring.net>`

```

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:ajgqmh$1ig$1@slb0.atl.mindspring.net...
> Donald,
>   What you say about GoBack in a method may (or may not) be how some
…[3 more quoted lines elided]…
> According to the draft Standard (and I think *must* implementations today)
a
> GoBack within a method is EXACTLY the same thing as an EXIT METHOD.
>
> In the draft Standard both of these statements have (the compatible)
RAISING
> phrase which works with PROPAGATE to send "exceptions" up the application
> (whether to a higher program or higher method).  This is the new
"activating
> process" concept.
>

Hi Bill.

I certainly hope things get a bit more standardized.  That seems to be the
problem with a lot of the OOP code, and you actually warned me of it about
five years ago when I started to use it.  At that time, there was no
standard.  What I said in the previous post was true when I started testing
stuff back then, and may be wrong on my current version.  I certainly have
had no problems with any of the code that followed those rules.  Maybe I
should sit down and write some test code again.  Been three versions since I
actually did the tests.

Donald
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 9)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-08-16T00:30:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c244bb$fb0b7380$6495f243@chottel>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com> <ajgqmh$1ig$1@slb0.atl.mindspring.net> <QPT69.5343$DO6.1502518@news20.bellglobal.com>`

```
Do you think vendors that have implemented OOCobol for a long time will be
willing to change their compiler to match the new standard, even though
doing so will break all of their customers OOCobol programs?

I know IBM "dropped" SOMObjects, but apparently not many people were using
it.

<snip>

> 
> Hi Bill.
> 
> I certainly hope things get a bit more standardized.  That seems to be
the
> problem with a lot of the OOP code, and you actually warned me of it
about
> five years ago when I started to use it.  At that time, there was no
> standard.  What I said in the previous post was true when I started
testing
> stuff back then, and may be wrong on my current version.  I certainly
have
> had no problems with any of the code that followed those rules.  Maybe I
> should sit down and write some test code again.  Been three versions
since I
> actually did the tests.
> 
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-16T05:48:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5C933E.791EB40F@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <ajgh5q020hg@enews2.newsguy.com> <uQQ69.6937$2T2.1234863@news20.bellglobal.com> <ajgqmh$1ig$1@slb0.atl.mindspring.net> <QPT69.5343$DO6.1502518@news20.bellglobal.com> <01c244bb$fb0b7380$6495f243@chottel>`

```


Charles Hottel wrote:

> Do you think vendors that have implemented OOCobol for a long time will be
> willing to change their compiler to match the new standard, even though
…[4 more quoted lines elided]…
>

Well vendors that have *actually* implemented OO - correct me if I'm wrong :-

- IBM - Just what will they implement from the new Standard ?
- Fujitsu - Late 'bloomers' so some of their syntax is closer to the Standard,
but they sure seem to be putting their eggs in the MS .Net basket.
- Hitachi - They keep their cards close to their chest - only in Japan
- Micro Focus - have stated a commitment to follow up on the standard.

Assuming Hitachi also *has* - the last three are not going to give up on their
approach to GUIs - Standard or no bloody Standard. And while J4 is
prevaricating on 'Finalizer'(auto garbage collection), they will stick with
their current approach. Similarly the last three also have their own versions
of Standard Classes, (includes Base, Behavior, Collections/Dictionaries etc.),
which J4 is just getting warmed up on although the topic goes back to '96.

I used to 'dream' of portable COBOL - it's obvious it is becoming a bloody
joke so far as OO COBOL is concerned. By the time Finalizer/Standard Classes
are determined - there will be so much PC-code written, that even if somebody
sounds Gabriel's trumpet announcing the 'new, bright Finalizer/Standard
Classes' - developers will say, "Who gives a s.....!".

Vendor wise - it will probably behoove them to stick with, "Yes our compiler
follows the Standard about 80% with syntax, but we've added our own goodies
for GUIs/Collections/Java calls etc.".

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-15T19:10:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5BFE0C.E44D691A@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com>`

```


Donald Tees wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
> news:3D5B08B7.1446FEF5@shaw.ca...
…[99 more quoted lines elided]…
> Donald

Don,

Yes there are occasions where you genuinely want to ABORT such as crashed
index, (Alternative to that is to feed automatically into an ISAM Rebuild - if
that fails - then ABORT). The other side of the coin, you can continue with
the application using 'OK' programs, knowing that this particular one has to
be fixed. (Even without spelling it out, we know that smart users latch onto
this type of thing). It's important to get it fixed real quick, but it doesn't
necessarily have to bring the whole application crashing down.

I would suggest knocking over your computer hut with a bloody big truck fits
into the category of an ABORT <G>.

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 6)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-08-15T16:13:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fZT69.5348$DO6.1504352@news20.bellglobal.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3D5BFE0C.E44D691A@shaw.ca...
>
>
…[91 more quoted lines elided]…
> > > Exception Handler. What hasn't yet twigged is that you can use
features
> > > to propagate up through a nested series of classes/methods, (and even
> > > much more comprehensively in the draft Standard) - but I'm still
looking
> > > for the Nirvana, which avoids the necessity of individually checking
> > > within each method, 'in the chain', with an automatic feature that
takes
> > > you straight back to Class 1 Method 1.
> > >
…[10 more quoted lines elided]…
> index, (Alternative to that is to feed automatically into an ISAM
Rebuild - if
> that fails - then ABORT). The other side of the coin, you can continue
with
> the application using 'OK' programs, knowing that this particular one has
to
> be fixed. (Even without spelling it out, we know that smart users latch
onto
> this type of thing). It's important to get it fixed real quick, but it
doesn't
> necessarily have to bring the whole application crashing down.
>
> I would suggest knocking over your computer hut with a bloody big truck
fits
> into the category of an ABORT <G>.
>
> Jimmy
>

According to the standard god (Bill that is<G>), it SHOULD work the way you
say.  GOBACK and EXIT METHOD should work identically.  When I started
testing this stuff about 4-5 years back, I got the same results as you, and
it has been an annoyance to me ever since. GOBACK made subroutine use a 1000
times easier.

Donald
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-08-15T20:44:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajh3q9$r31$1@peabody.colorado.edu>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com>`

```
When I started IBM CoBOL we used something called "CALL EXIT", to exit our
programs because of problems with STOP RUN.  It wasn't standard CoBOL, but it
did the job.

Maybe we need to update this concept for OO exception handling.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 8)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-15T16:11:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajh5e301kjg@enews1.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:ajh3q9$r31$1@peabody.colorado.edu...
> When I started IBM CoBOL we used something called "CALL
EXIT", to exit our
> programs because of problems with STOP RUN.  It wasn't
standard CoBOL, but it
> did the job.
>
> Maybe we need to update this concept for OO exception
handling.

How does CALL EXIT differ from STOP RUN?
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-16T05:26:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5C8E11.656C1D23@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <ajh5e301kjg@enews1.newsguy.com>`

```


Grinder wrote:

> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
> news:ajh3q9$r31$1@peabody.colorado.edu...
…[9 more quoted lines elided]…
> How does CALL EXIT differ from STOP RUN?

I'm not ignoring messages from either Donald or Grinder - reading 'em
all - phew - there's so many points to answer. I think Howard's
reference to CALL EXIT is similar to my tentative (?) 'EXIT CLASS'.

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-16T05:21:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5C8D1A.47D273EA@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> When I started IBM CoBOL we used something called "CALL EXIT", to exit our
> programs because of problems with STOP RUN.  It wasn't standard CoBOL, but it
> did the job.
>
> Maybe we need to update this concept for OO exception handling.

Trying to emulate the other OO languages - maybe COBOL has gotten too
complicated. A real nice catch-all would be DECLARATIVES - but until I've read
the draft Standard in detail, which is replete with Exception Handling, I don't
know.

However our Standard's God (I like that moniker Donald <G>), would possibly have
made some comment by now. He did suggest elsewhere that I could use a mix of
DECLARATIVES with DEBUGGING MODE to achieve somewhat of the future Standard
contents. However, even using M/F Answer Exchange I didn't get the DEBUGGING MODE
to work.

As is,  DECLARATIVES is primarily for checking status for COBOL files only - wont
handle SQLCODE/SQLSTATE.  I don't think it is a part of the proposed Standard but
currently with DEBUGGING MODE we have :-

*>Use for Debugging on ALL REFERENCES of id-1.
*>Use for Debugging on filename-1.
*>Use for Debugging on procedure-name-1.
*>Use for Debugging on ALL PROCEDURES.

Either #1 or #4 could probably give me what I'm after, possibly coupled with a
Callback. A Callback is where you specify a method as an object reference then
invoke the Callback, briefly like so :-

*>---------------------------------------------------------------
Method-id. "Shopping1".
*>---------------------------------------------------------------
*> Original taken from Adele Goldberg's Smalltalk 80

Procedure Division.

*>Without listing all the code I create a collection (ValueBag2)
*>and then add a list of grocery items with quantity/retail price.
*>I want to get a check-out total.

*> create Bag/add individual items.........
*>Now the Callback which is an object reference :-

 invoke Callback "new"
    using self "ShoppingBill " returning ls-MethodName
 move zeroes to ws-BillTotal
 invoke os-ValueBag2 "do" using ls-MethodName
*> The contents (elements) of ValueBage2 are already known, so we  get 'n'
*> 'do' using ls-MethodName
 display ws-BillTotal

 End Method "Shopping1".
*>---------------------------------------------------------------
Method-id. "ShoppingBill".
*>---------------------------------------------------------------
Local-storage section.
01 ls-price              pic 9(03)v9(02).
Linkage section.
01 lnk-Product.
   10 ProductName        pic x(10).
   10 P-filler           pic x.
   10 ProductPrice       pic x(04).

Procedure Division using lnk-Product.
   compute ls-price = function numval (ProductPrice)
   add ls-price to ws-BillTotal
End method "ShoppingBill".
*>------------------------------------------------------------

In the above both methods are contained in the same class, but the Callback
doesn't have to be - I could 'direct' the above class to look for the Callback in
an invoking Class. Back to my example of Class 3 this would find the Callback in
Class2.

One other avenue is the current Exception Handling class in Net Express - which
illustrates error handling, certainly things like file-status but can also be
validity checks. It doesn't illustrate propagating up a chain of nested
classes/methods. I have to absorb a reply from Calin, one of my N/E 'whiz kids' -
can I create a sub-class Exception Handler to pass back results from
Class3--->Class2----->Class1 ?

I've got to be sure before I cry,  "Wolf !"  It could just be that the addition
of the syntax 'EXIT CLASS"  specific to class programs would serve the same
purpose as GOBACK/EXIT PROGRAM for procedural programs - i.e., it would negate
outstanding code in the methods activated in the current class.. As you exit of
course, and go up in the nested tree of classes/methods you need some mechanism
to also tell them to jump to EXIT CLASS - finishing up back at the Menu.

Include STOP RUN anywhere in the nested chain and your problems are over <G>.

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 9)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-16T01:56:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aji7m2024ru@enews2.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <3D5C8D1A.47D273EA@shaw.ca>`

```
> I've got to be sure before I cry,  "Wolf !"  It could just be
that the addition
> of the syntax 'EXIT CLASS"  specific to class programs would
serve the same
> purpose as GOBACK/EXIT PROGRAM for procedural programs -
i.e., it would negate
> outstanding code in the methods activated in the current
class.. As you exit of
> course, and go up in the nested tree of classes/methods you
need some mechanism
> to also tell them to jump to EXIT CLASS - finishing up back
at the Menu.
>
> Include STOP RUN anywhere in the nested chain and your
problems are over <G>.

A classes' method, Method A is invoked by Program 1.  It, in
turn, invokes Method B which then invokes Method C.  Methods A,
B and C are in the same class, and are operating on the same
object.  The entire mess is part of the same process and
thread.

If you EXIT CLASS in Method C, does program flow immediately go
to the statement after the invocation in Program 1?
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-16T21:55:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5D7663.C13B2C9@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <3D5C8D1A.47D273EA@shaw.ca> <aji7m2024ru@enews2.newsguy.com>`

```


Grinder wrote:

> > I've got to be sure before I cry,  "Wolf !"  It could just be
> that the addition
…[21 more quoted lines elided]…
> to the statement after the invocation in Program 1?

Ok - you may have some other name for it in other languages, but COBOL
drops through code until told to specifically 'exit.'

Procedural - Program1 call ProgramX/Perform ParaA--->Perform
ParaB-->Perform ParaC

OO - Program1/Class1 invoke ClassX/MethodA-->invoke self MerthodB---->
invoke self MethodC

Either Procedural or OO the code chain above is going to continue until
specifically told to 'exit'

For Procedural you can have EXIT PERFORM/SECTION or the program
'terminator' GOBACK/EXIT PROGRAM, and of course STOP RUN .

For OO we *currently* have implied or explicit code for EXIT METHOD -
which is akin to the EXIT PERFORM (i.e. compare a    PERFORM PARAGRAPH
to an INVOKE METHOD) - but although available as an option in OO code
GOBACK/EXIT PROGRAM doesn't act as an immediate shortcut to get out of
the class.

Narrowing it down to your example :-

Class X MethodA -
--------------------
display "I'm starting MethodA"
invoke self "MethodB"
display "I'm back from MethodB"
if field-x = error
    GOBACK
    EXIT METHOD *> "Exit Method' NOT 'Goback' gets you out of this
method
end-if
display "I'm still in MethodA"
do this....
do this...
do this
End Method (implied EXIT METHOD)

The above also applies to your methods B or C. Stick 'artificial exits'
(GOBACK/EXIT PROGRAM) wherever you like - the mini programs (methods)
are going to perform like Method A above.

By no means conclusive - but I would see EXIT CLASS acting identically
to GOBACK/EXIT PROGRAM as they function for a Procedural program. The
alternative, rather than additional syntax, would be for GOBACK/EXIT
PROGRAM to function for Class syntax exactly as they do for Procedural
syntax.

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 11)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-17T14:26:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajm81i02q1m@enews2.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <3D5C8D1A.47D273EA@shaw.ca> <aji7m2024ru@enews2.newsguy.com> <3D5D7663.C13B2C9@shaw.ca>`

```
> By no means conclusive - but I would see EXIT CLASS acting
identically
> to GOBACK/EXIT PROGRAM as they function for a Procedural
program. The
> alternative, rather than additional syntax, would be for
GOBACK/EXIT
> PROGRAM to function for Class syntax exactly as they do for
Procedural
> syntax.

Code not in Class X
--------------------
display "I'm starting execution"
invoke objX "MethodA"
display "I'm back from MethodA"

Class X MethodA -
--------------------
display "I'm starting MethodA"
invoke self "MethodB"
display "I'm back from MethodB"
End Method


Class X MethodB -
--------------------
display "I'm starting MethodB"
invoke self "MethodC"
display "I'm back from MethodC"
End Method

Class X MethodC -
--------------------
display "I'm starting MethodC"
EXIT CLASS
End Method

So what would the output from this truncated example look like.

Would it be like this?

I'm starting execution
I'm starting MethodA
I'm starting MethodB
I'm starting MethodC
I'm back from MethodA
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-18T03:10:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5F11BC.3E621BEE@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <3D5C8D1A.47D273EA@shaw.ca> <aji7m2024ru@enews2.newsguy.com> <3D5D7663.C13B2C9@shaw.ca> <ajm81i02q1m@enews2.newsguy.com>`

```


Grinder wrote:

> > By no means conclusive - but I would see EXIT CLASS acting
> identically
…[42 more quoted lines elided]…
> I'm back from MethodA

See Bill's comments. You and me both - we are talking about OO classes
<G>.
Yeas - as you've illustrated - subject to testing for errors in Methods
A through C to EXIT METHOD as appropriate bringing you back to your
'start execution' either Procedural or OO.

See my reply to Rick - enough of this nonsense. For the moment I'll
stick with the original :-
                    if ContinueProgram
                        do this..........

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2002-08-17T19:43:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ultndnj9p8gn94@corp.supernews.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <3D5C8D1A.47D273EA@shaw.ca> <aji7m2024ru@enews2.newsguy.com> <3D5D7663.C13B2C9@shaw.ca>`

```

James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3D5D7663.C13B2C9@shaw.ca...
>
[snip]
> Ok - you may have some other name for it in other languages, but COBOL
> drops through code until told to specifically 'exit.'
…[5 more quoted lines elided]…
> invoke self MethodC

Also, for nested programs:
Nested Procedural - Program1 call ProgramX --> call NestedProgramA -->
call NestedProgramB --> call NestedProgramC

> Either Procedural or OO the code chain above is going to continue until
> specifically told to 'exit'
>
> For Procedural you can have EXIT PERFORM/SECTION or the program
> 'terminator' GOBACK/EXIT PROGRAM, and of course STOP RUN .

GOBACK/EXIT PROGRAM in a nested program is not a program
'terminator'. Nested 'procedural' programs more closely match the
OO syntax for 'invoke self'.

> For OO we *currently* have implied or explicit code for EXIT METHOD -
> which is akin to the EXIT PERFORM (i.e. compare a    PERFORM PARAGRAPH
…[30 more quoted lines elided]…
> syntax.

But, it would not act identically to GOBACK/EXIT PROGRAM,
if the current 'procedural' program is nested (contained within
another program.)

IMO, J4 looks for things like that and I have learned to look for
those things J4 looks for. <G>

There is a lot in the FDIS I have not 'absorbed' but it seems to
me that you could define EC-USER-EXIT-ALL by using the
directive >>TURN EC-USER-EXIT-ALL CHECKING ON;
place a declarative in Program1 to catch the exception; use
>>PROPAGATE ON for ClassX (or ProgramX); then RAISE
EC-USER-EXIT-ALL when desired. If the declarative,
EC-USER-EXIT-ALL, has the statement RESUME NEXT
STATEMENT, that would probably accomplish what you are
looking for and it would work the same for nested programs.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-18T03:05:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5F1083.65C4C56A@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <3D5C8D1A.47D273EA@shaw.ca> <aji7m2024ru@enews2.newsguy.com> <3D5D7663.C13B2C9@shaw.ca> <ultndnj9p8gn94@corp.supernews.com>`

```


Rick Smith wrote:

> James J. Gavan <jjgavan@shaw.ca> wrote in message
> news:3D5D7663.C13B2C9@shaw.ca...
…[62 more quoted lines elided]…
>

OK - my reply to Bill - I'm talking using only OO class syntax.

> IMO, J4 looks for things like that and I have learned to look for
> those things J4 looks for. <G>
…[9 more quoted lines elided]…
> looking for and it would work the same for nested programs.

Yes I've browsed the above, and you've looked further in depth - and what
you've quoted looks like it might fit the bill.

Now to reality - what do I do as of today ?  While much of the 'Exception
Handling' in the draft covers both Procedural and OO, as Bill indicated some
time back, compiler vendors even at this stage might be well advised to be
wary of what the draft contains - awaiting the ISO people (WG4) putting on
their hob-nailed boots and clomping all over the draft Standard !

It is most likely that, even though already covered in the draft, 'Exception
Handling' for OO needs to be supported by classes subordinate to Base, that
J4 haven't as yet determined.

Consider the history of OO COBOL -

- First mooted probably back in 1991-1992, then summarized in Ray Obin's
handbook of  April 1993

- Standard Classes - a TREMENDOUS amount of work put into this topic by
Russell Clarke (Australia) in his original paper of 1996. It didn't stop
there. It got to WG4, because that's the first time they put on their
hob-nailed boots, stomping over his document with comments. Then the topic
goes on ice. Meanwhile Russell says "Hey ho !",  gives up on COBOL and now
programs solely in Java !

- Naughty Bill Klein "resurrects" Russell's paper in 2001.

- Follow on from that - a paper from Thane -  KISS - 2002

- And the latest Minutes of J4 - Meeting 238 - July 2002 :-

------------------------------------------------------------------------------------------------------------------

13. Development of a TR for a Class Library
J4 investigated various areas of class library development. J4 believes the
development of individual Technical Reports for selected technical areas
provides the greatest flexibility of scheduling and design in addressing each
of these areas.
------------------------------------------------------------------------------------------------------------------

Sensible approach, get as many ideas as possible - except - who are the ideas
going to come from apart from Fujitsu, Hitachi and Micro Focus ? Some other
members of J4, (and we are currently talking a total of NINE),  may be
familiar with other OO languages - but it's not exactly comparing apples with
apples. Scheduling ? Target Date ? How about tentatively July 2004 as the
final date for J4 to produce a TR - add to that the WG4 hob-nailed boot
procedure and we could be talking 2005 ! So given Calendar Date "X" - when
can we anticipate the vendors (four of 'em at most) will introduce compilers
that have OO Exception Handling as per the Standard, probably embraced in
Standard Classes.

Meanwhile I gotta a problem. So back to where all this started :-
*>------------
method-id. "mainline"
*>-------------
set ContinueProgram to true
invoke method1
if ContinueProgram invoke method2
    if ContinueProgram invoke method3
        if ContinueProgram invoke method4
*>--------------
Method1. get some info.
*>----------------------
invoke Customerfile 'getName' using prime key returning results (status and
name)
if FileError
    set CancelProgram to true
    EXIT METHOD
else................
End-if
*>--------------------------------------

I don't go beyond Method1 in the 'Mainline'.

It requires care - but hell it works - compared to trying to do cartwheels
with what is currently available and at some as yet unspecified date, what
will be attainable !

Meanwhile folks you can enlist in J4 if you abide by the rules - attend 'n'
meetings per year, $200 fee for attendance at each meeting and small
ancillaries like food, travel and accommodation, associated with each meeting
!

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 13)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2002-08-18T01:31:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ulubpvdfnibvb9@corp.supernews.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <3D5C8D1A.47D273EA@shaw.ca> <aji7m2024ru@enews2.newsguy.com> <3D5D7663.C13B2C9@shaw.ca> <ultndnj9p8gn94@corp.supernews.com> <3D5F1083.65C4C56A@shaw.ca>`

```

James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3D5F1083.65C4C56A@shaw.ca...
>
[snip]
> Now to reality - what do I do as of today ?

The big advantage to Exception Handling as defined in the
draft standard is the reduction in code that is necessary for
other methods. One possibility is to borrow a mechanism
from C programming or simulate the try/catch of C++. I have
never had to use this technique in either COBOL or C. In all
cases, exceptions where handled in the same program or
function; or the exception was returned to the calling program
or function, which then handled it.

In the 'main' program (and wherever else required) define

01 Application-Exception pic s9(9) comp-5 external.

After each invoke (or call), where an exception may occur,
insert code like the following.

evaluate Application-Exception
    when 0
        continue
    when < a value I can handle >
        < code to handle the exception >
        move 0 to Application-Exception
    when other
        < clean-up code >
        goback
end-evaluate

Wherever part of the application encounters a situation it
cannot handle directly, insert code like the following.

if < condition I cannot handle >
    < clean-up code >
    move < a defined value > to Application-Exception
    goback
end-if

After returning to the 'main' program, any non-zero value
in Application-Exception is an 'unhandled' exception.

>  While much of the 'Exception
> Handling' in the draft covers both Procedural and OO, as Bill indicated
some
> time back, compiler vendors even at this stage might be well advised to be
> wary of what the draft contains - awaiting the ISO people (WG4) putting on
> their hob-nailed boots and clomping all over the draft Standard !

However, Bill indicated, recently, that it is now, Yes or No.

> It is most likely that, even though already covered in the draft,
'Exception
> Handling' for OO needs to be supported by classes subordinate to Base,
that
> J4 haven't as yet determined.

While there are some requirements not covered in the draft,
I think the requirements for exception handling are not among
them.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 14)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-19T03:16:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D60646B.F46201CB@shaw.ca>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <KuE69.6405$2T2.1121915@news20.bellglobal.com> <3D5BFE0C.E44D691A@shaw.ca> <fZT69.5348$DO6.1504352@news20.bellglobal.com> <ajh3q9$r31$1@peabody.colorado.edu> <3D5C8D1A.47D273EA@shaw.ca> <aji7m2024ru@enews2.newsguy.com> <3D5D7663.C13B2C9@shaw.ca> <ultndnj9p8gn94@corp.supernews.com> <3D5F1083.65C4C56A@shaw.ca> <ulubpvdfnibvb9@corp.supernews.com>`

```


Rick Smith wrote:

> James J. Gavan <jjgavan@shaw.ca> wrote in message
> news:3D5F1083.65C4C56A@shaw.ca...
…[12 more quoted lines elided]…
>

That's where we came in Rick <G>. That's where Grinder joined the fray thinking
in terms of the try/catch technique from Pascal and other languages. In Ada I
think it is Begin/End (?)

>
> In the 'main' program (and wherever else required) define
…[16 more quoted lines elided]…
>

Different words, but I started out and am doing exactly as you suggest,
primarily related to testing COBOL file status or SQLSTATE codes. So after each
'access' of a DB return a result :-

Evaluate true
    when FileError
    when TableError
        set CancelProgram to true
        EXIT METHOD
    when RecFound
        do this....
    when RecNotFound
        do this......
End-evaluate

It's fine and dandy - the trick is *remembering* to pass that CancelProgram back
up through the chain of nested methods either in this class or previous classes.
(CancelProgram is a Level 88 which is global to all methods in the current
class, but must also be signaled back to any invoking classes). As you suggest
you could introduce an External Exception Handling class, (or in my case use the
existing N/E Exception Handler), but you still have to do your test,
particularly in any method which contains further code after the invocation
which created the failure - it's not automatic.

> Wherever part of the application encounters a situation it
> cannot handle directly, insert code like the following.
…[17 more quoted lines elided]…
> However, Bill indicated, recently, that it is now, Yes or No.

Let him answer <G>. I think he is still cautionary at this stage.

>
> > It is most likely that, even though already covered in the draft,
…[7 more quoted lines elided]…
> them.

PS:  I bet any of the 'boys' at Newbury reading this are laughing their socks
off - and thinking - 'Dumb bastard' <G>

Jimmy
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 4)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-15T10:30:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajghf7021cg@enews2.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca>`

```
> > If you raise an error instead of making a GOBACK, does
Method5
> > get invoked?
>
> That's Step 2. Having initially dismissed my earlier
assumption that
> GOBACK wouldn't work (purely in OO Class syntax), and now
confirmed it
> doesn't work - now I'll move over to dabbling with the
existing
> Exception Handler. What hasn't yet twigged is that you can
use features
> to propagate up through a nested series of classes/methods,
(and even
> much more comprehensively in the draft Standard) - but I'm
still looking
> for the Nirvana, which avoids the necessity of individually
checking
> within each method, 'in the chain', with an automatic feature
that takes
> you straight back to Class 1 Method 1.

A great way to do this is to use the exception as your means of
communication.  I'm not sure this is how any OO-COBOL works,
but it's a common enough mechanism in other environments.

If you raise an error, or something you invoke raises an error,
execution should jump to the most local error-handler.  If you
only have an error handler in your top-level method, you should
expect execution to return there.

If you have intermediate (in the call stack) methods that need
to cleanup, but cannot necessarily handle the error, they can
catch it, do their cleanup, then re-raise the error.

Reading TEXT_FDIS_1989.pdf suggested this mechanism is in
place, but I'm unclear as to the syntax.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 5)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-08-15T12:53:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mYQ69.6940$2T2.1235659@news20.bellglobal.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <ajghf7021cg@enews2.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:ajghf7021cg@enews2.newsguy.com...
> > > If you raise an error instead of making a GOBACK, does
> Method5
…[35 more quoted lines elided]…
>

This, I think, is quite a differnt topic.  How "on exception" works. that
is.  I, personally, code all that stuff in the declaratives.  I seldom used
declaratives before OOP, but find that most code I write now requires them
(a matter of style change, really).

From an archetectural standpoint, I seldom code a "program" anymore.  I find
the OOP model far better for handling even procedural code.  For example,
thousands of programs written in Cobol follow the model of a main menu
program that calls several dozen main programs.

Simply changing the library to a "sytem object" that contains each main
program as a system method makes the system far more versatile.  The main
programs change only in that the program-id becomes a method-id, and the
goback/stop run statements become exit method statements.  Converting a
program thusly is a five minute job.  The calls become invokes, with an
almost identical systax.

However, once it is done, you get all sorts of extra versatility.  For
example, I can introduce a runtime flag into the method, name it a property,
and set it from outside the program.  That saves having to introduce a new
calling sequence, and possibly buggering up other calls in other programs.
The setting of that flag is also checked at compile time, rather than at run
time, at least for compatability factors.  It also gives the versatility of
being able to create two instances of the same method, at the same time.
The only way of doing that with subroutines is to make a second copy under a
different name.

Donald
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 6)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2002-08-15T12:25:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ajgo5u0rn0@enews1.newsguy.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <ajghf7021cg@enews2.newsguy.com> <mYQ69.6940$2T2.1235659@news20.bellglobal.com>`

```
> From an archetectural standpoint, I seldom code a "program"
anymore.  I find
> the OOP model far better for handling even procedural code.
For example,
> thousands of programs written in Cobol follow the model of a
main menu
> program that calls several dozen main programs.
>
> Simply changing the library to a "sytem object" that contains
each main
> program as a system method makes the system far more
versatile.  The main
> programs change only in that the program-id becomes a
method-id, and the
> goback/stop run statements become exit method statements.
Converting a
> program thusly is a five minute job.  The calls become
invokes, with an
> almost identical systax.
>
> However, once it is done, you get all sorts of extra
versatility.  For
> example, I can introduce a runtime flag into the method, name
it a property,
> and set it from outside the program.  That saves having to
introduce a new
> calling sequence, and possibly buggering up other calls in
other programs.
> The setting of that flag is also checked at compile time,
rather than at run
> time, at least for compatability factors.  It also gives the
versatility of
> being able to create two instances of the same method, at the
same time.
> The only way of doing that with subroutines is to make a
second copy under a
> different name.

Does this also result in your code sharing a common "process
space" -- memory, task priority, that type of thing?

If I'm understanding properly, this makes your main and
subordinate programs into libraries utilized by a single "main"
program.
```

###### ↳ ↳ ↳ Re: OO Exception Handling

_(reply depth: 7)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-08-15T16:23:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j5U69.5352$DO6.1505627@news20.bellglobal.com>`
- **References:** `<3D5590B9.B38DF038@shaw.ca> <3D598D16.9905DC31@shaw.ca> <ajd33502tvi@enews4.newsguy.com> <3D5B08B7.1446FEF5@shaw.ca> <ajghf7021cg@enews2.newsguy.com> <mYQ69.6940$2T2.1235659@news20.bellglobal.com> <ajgo5u0rn0@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:ajgo5u0rn0@enews1.newsguy.com...
> > From an archetectural standpoint, I seldom code a "program"
> anymore.  I find
…[43 more quoted lines elided]…
>

Yes to the first, sort of to the second.  You always have to have some code
somewhere that is the "mainline".  However, there is nothing to stop you
from starting with a dozen little batch programs, then combining them into
one main line with a menu that is the "main" program.  Later, you can take a
dozen "mainlines", and repeat the process.  I do exactly that with my
accounting, as there are often several companies sitting on one computer.

For a second company, the mainline simply looks up a company disk drive in a
"system" data base, then sets that area into the property of the accounting
object. It then invokes accounting.  The actual accounting module defaults
to a specific area for a single use for a single company, and can be placed
on the desktop as it sits.

Donald
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
