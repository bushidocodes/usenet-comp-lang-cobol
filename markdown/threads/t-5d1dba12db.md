[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# three-digit subprocedure listing

_13 messages · 7 participants · 1999-01 → 1999-02_

---

### three-digit subprocedure listing

- **From:** john_meyer@my-dejanews.com
- **Date:** 1999-01-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78vebs$im$1@nnrp1.dejanews.com>`

```
Hi, our professor wants us to use the nnn-<verb>-<adj>-<noun> approach to
naming subprocedures.  Problem is, I can't find the directory listing what
all the nnn numbers are (100 level versus a 999 level).  Can somebody help
me?

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: three-digit subprocedure listing

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-01-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b39bf4@news3.ibm.net>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com>`

```
john_meyer@my-dejanews.com wrote in message
<78vebs$im$1@nnrp1.dejanews.com>...
>Hi, our professor wants us to use the nnn-<verb>-<adj>-<noun> approach to
>naming subprocedures.  Problem is, I can't find the directory listing what
>all the nnn numbers are (100 level versus a 999 level).  Can somebody help
>me?


You make them up as you go !!!
There are several schools of thought here. I personally think that the nnn
just makes it harder to reuse or reorganize the code, but other people
simply
cannot program without them, so....


Typical layout :


procedure division.
000-main-line.
     perform 100-open-files
     perform 200-do-our-thing
         until work-is-done
     perform 900-close-files
     stop run
     .

100-open-files,
       ....

200-do-you-thing.
       .....

300-close-files.
       ...
```

##### ↳ ↳ Re: three-digit subprocedure listing

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36B5C369.25EF14C0@NOSPAMhome.com>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com> <36b39bf4@news3.ibm.net>`

```
It's harder to reuse or reorganize, but not much harder.  It's not as
though we have to repunch cards, our editors can handle it.  But it
makes it easier to browse a program listing and can create implicit
paragraph groups without sections.  

(I use 4 digit prefixes, allowing more room for inserted paragraphs)

> You make them up as you go !!!
> There are several schools of thought here. I personally think that the nnn
…[22 more quoted lines elided]…
>        ...
```

#### ↳ Re: three-digit subprocedure listing

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-01-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ncJs2.1348$Xl5.1355083@news1.mia>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com>`

```
john_meyer@my-dejanews.com wrote:
>Hi, our professor wants us to use the nnn-<verb>-<adj>-<noun> approach to
>naming subprocedures.  Problem is, I can't find the directory listing what
>all the nnn numbers are (100 level versus a 999 level).  Can somebody help
>me?

It is common custom in COBOL to append a numeric prefix to paragraph
names.  I know of no ubiquitous method for assigning the numbers, other
than that you would want them to be in ascending order from top to
bottom of the program.  Perhaps he has some method of his own devising.
If your professor wants you to use only three digits for the prefix,
then he is expecting you to write some pretty small programs.  In many
production programs, even five digits is too small.  Are you sure your
professor means use *exactly* three digits?  If not, then below is the
method I use for paragraph numbering.  Note that a number of programmers
here objected strongly to my method when I posted it a while back.  But
take that with a grain of salt.  Like many programming standards, you
really have to use it for a while to appreciate its utility.  What is
more significant to mymind is the fact that none of the many programmers
to whom I have taught this method have abandoned it voluntarily, some
even after more than twenty years.


                        COBOL Paragraph Numbering

I was taught as a beginning programmer to use ascending numeric prefixes
on all my paragraph names.  Over the years, I have kept this practice, and
have embellished it in a number of ways.  I like to use paragraph numbers
to reflect a relative structure hierarchy.  Over the years, I have also
learned to appreciate ease of copying code from one program into another,
so I have standardized on a six digit prefix.  Below is a stylized example
of how a program might be structured, and how the paragraph numbers would
be used to reflect the hierarchy.  Note the way the paragraph numbering
reflects the actual structural hierarchy of the program.  By reflecting
the structural hierarchy of the code in the paragraph numbering, it makes
it very easy to recognize the program structure.  A paragraph does not
only PERFORM a paragraph of a subordinate level, of course.  The 'global
utility' paragraphs are for routines which are not necessarily subordinate
to the major functions of the program, but can be used by them.  Examples
might be a date edit, or field convert of some kind.  For independent
routines of one paragraph, I use 00nn00, and for routines with several
subordinate paragraphs, I use 00n000 for the top level paragraph.  In
general, paragraph 120000 will have every paragraph 12nnnn subordinate to
it (12300 -> 123nnn, 123400 -> 1234nn, 123450 -> 12345n).  As an aside,
when we used to use sections to segment our code, paragraph 000000 would
start a section, and each different nn0000 paragraph would start another
section.

Many of you may use a similar method.  But I have found this to be a very
flexible and valuable tool over the years, and I like using it very much.
Only rarely do I need to move a group of paragraphs to a different 'level'.
It has contributed a great deal to my productivity, and the effect is
cumulative.  The more code I collect which is similarly structured and
easy to use, the less code I need to write.  The advantages I have reaped
from this are too many to enumerate.  It is easy to find any paragraph in
the program, you do not need to think up unique paragraph names for two
very similar routines in different parts of the program (e.g. doing the
same thing to different tables), it is easy to see the hierarchical program
structure, etc.  That last one is extremely valuable.

      *
      *  ** TOP LEVEL CONTROL STRUCTURE (000000) **
      *
       000000-CONTROL.
           PERFORM 000100-INITIALIZE
           PERFORM 000200-PROCESS
               UNTIL (end of data).
           PERFORM 000300-TERMINATE.
           STOP RUN.

      *
      *  ** SECOND LEVEL CONTROL STRUCTURE (000n00) **
      *
       000100-INITIALIZE.
           Get today's date, open files, read first input record, etc.

       000200-PROCESS.
           PERFORM 010000-major-function-1.
           PERFORM 020000-major-function-2.
           ...
           PERFORM 990000-major-function-99.

       000300-TERMINATE..
           Print ending totals, close files, etc.

      *
      *  ** GLOBAL UTILITY ROUTINES (00nn00) **
      *
       001000-utility-routine.
       001100-utility-routine.
       001200-utility-routine.
           ...

      *
      *  ** MAJOR FUNCTIONS (nn0000) **
      *
       010000-major-function-1.
           PERFORM 011000-intermediate-function-1-1.
           PERFORM 012000-intermediate-function-1-2.
           ...

      *
      *  ** INTERMEDIATE FUNCTIONS (nnx000) **
      *
       011000-intermediate-function-1-1.
           PERFORM 011100-minor-function-1-1-1.
           PERFORM 011200-minor-function-1-1-2.
           ...

      *
      *  ** MINOR FUNCTIONS (nnnx00) **
      *
       011100-minor-function-1-1-1.
           PERFORM 011110-sub-function-1-1-1-1.
           PERFORM 011120-sub-function-1-1-1-2.
           ...

      *
      *  ** SUB FUNCTIONS (nnnnx0) **
      *
       011110-sub-function-1-1-1-1.
           PERFORM 011111-low-function-1-1-1-1-1.
           PERFORM 011112-low-function-1-1-1-1-2.
           ...

      *
      *  ** LOW FUNCTIONS (nnnnnx) **
      *
       011111-low-function-1-1-1-1-1.
           ...

       011111-low-function-1-1-1-1-2.
           ...


       011120-sub-function-1-1-1-2.
           ...


       011200-minor-function-1-1-2.
           ...

       012000-intermediate-function-1-2.
           PERFORM 012100-minor-function-1-2-1.
           PERFORM 012200-minor-function-1-2-2.
           ...

       012100-minor-function-1-2-1.
           ...

       012200-minor-function-1-2-2.
           ...


       020000-major-function-2.
           PERFORM 021000-intermediate-function-2-1.
           PERFORM 022000-intermediate-function-2-2.
           ...

       021000-intermediate-function-2-1.
           PERFORM 022100-minor-function-2-1-1.
           PERFORM 022200-minor-function-2-1-2.
           ...

       021100-minor-function-2-1-1.
           ...

       021200-minor-function-2-1-2.
           ...

       022000-intermediate-function-2-2.
           PERFORM 022100-minor-function-2-2-1.
           PERFORM 022200-minor-function-2-2-2.
           ...

       022100-minor-function-2-2-1.
           ...

       022200-minor-function-2-2-2.
           ...
```

#### ↳ Re: three-digit subprocedure listing

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b5ecf7.540011675@news.freeserve.net>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com>`

```
On Sat, 30 Jan 1999 17:09:22 GMT, john_meyer@my-dejanews.com wrote:

>Hi, our professor wants us to use the nnn-<verb>-<adj>-<noun> approach to
>naming subprocedures.  Problem is, I can't find the directory listing what
>all the nnn numbers are (100 level versus a 999 level).  Can somebody help
>me?

There is no rule to this unless your professor has a standard to which
you should adhere. Common practice at one place I've worked used to be
to have a letter then three digits. You'd have something like


I001-Initialization-start


W050-Write-record


F010-compute-vat


Where I was initialization code, W was file handling and F was
functional code.

Personally I think it's the biggest pile of horse droppings going. The
problem with numbering your routines and ordering them makes it
difficult to reuse code. 

Modern editors have code completion. So I type the first few letters
of the name of the data-item or section name, press the code
completeion key and it fills in the rest. If all your sections are
called something like...

I010-Init-start
I010-middle-loop
I010-jump-here
I010-error-during-init
I010-end

then it will list a heap of section names. Madness. Anyone persisting
with this archaic practice should be shot at dawn. We don't need to
manually order sections these days - compiler tools have come a long
way.
```

##### ↳ ↳ Re: three-digit subprocedure listing

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k7Ht2.2584$Xl5.3057930@news1.mia>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com> <36b5ecf7.540011675@news.freeserve.net>`

```
Shaun C. Murray wrote:
>
>Personally I think it's the biggest pile of horse droppings going. The
>problem with numbering your routines and ordering them makes it
>difficult to reuse code.

No offense Shaun, but that statement is clear evidence that you either
have not tried to use a good numbering scheme, or you did not understand
it.  I have averaged around 200,000 lines of code per year for the last
twelve years, at least.  The only way I can turn out that much code
consistently is by a great deal of code reuse.  Let me give a practical
example of why what you just said is 'horse droppings.' ;-)

Consider a section of code written to process an input screen.  The code
is written using the first two digits of the paragraph number to match
the number in the screen layouts in Working Storage.

   01  RECV-05-SCREEN     REDEFINES RECEIVE-SCREEN.
       03  RECV-05-...
       03  RECV-05-...
   ...
   01  SEND-05-SCREEN     REDEFINES SEND-SCREEN.
       03  SEND-05-...
       03  SEND-05-...

   050000-process-something.
   05nnnn-...

To duplicate that screen under number 22 instead of 05, all I have to do
is to make a copy of the code, then replace "RECV-05-" with "RECV-22-"
and "SEND-05-" with "SEND-22-".  Next I use a regular expression search
and replace to change all the 05nnnn- paragraph numbers to 22nnnn-.  In
Brief, that string would be replace: " 05{[0-9][0-9][0-9][0-9]-}" with:
" 22\0".  Now I have an exact copy of the screen, but changed to be
screen 22 rather than screen 05.  The main menu screens used in these
systems use numbers 1, 2, etc. to select functions.  The screen layouts
in the programs have that same number, the paragraph numbers begin with
the same number, etc.  If I need two routines in different screens with
the same name, because they do almost identical functions, except on
slightly different data, I don't have to think up stupid similar names
which are difficult to remember and misuse, because the paragraph
numbers make that unnecessary.  I even have a small BASIC program which
scans my source code to flag all the times I reference a RECV-??- or
SEND-??- field that do not match the current paragraph prefix.  You
would not have any kind of cross-check like that without the paragraph
numbering scheme.  But the scheme must be a complete system, it must
reflect the program structure, and you must actually use it long enough
to understand its benefits.  I have taught this system to dozens and
dozens of programmers, and have yet to see one of them drop it.  Some
of them were dragged into it kicking and screaming, but once they used
it for a while, they would kick and scream if made to use anything
else.  It works, and it works well.  I have never brought up a new
system around someone unfamiliar with my techniques, without them
making some comment about being impressed by the low error rate.  This
is in large part because of heavy code reuse.  The benefit is there,
as I have proved again and again to many skeptics over the years.  The
productivity is there, the accuracy is there.  But you will never
realize that until you give it a fair trial. :-)
```

###### ↳ ↳ ↳ Re: three-digit subprocedure listing

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b77d79.642541575@news.freeserve.net>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com> <36b5ecf7.540011675@news.freeserve.net> <k7Ht2.2584$Xl5.3057930@news1.mia>`

```
On Tue, 02 Feb 1999 18:05:04 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:

>Shaun C. Murray wrote:
>>
…[6 more quoted lines elided]…
>it. 

Or it just doesn't fit in with the way I develop code and prefer other
members of the team I'm working in to code. Horse droppings was a bit
strong I guess but the number before name naming convention screws up
modern development tools' code completion schemes. COBOL coders are
the *only* people I've seen using it and usually ex-mainframers. Are
your editors really that bad still?


> I have averaged around 200,000 lines of code per year for the last
>twelve years, at least.  The only way I can turn out that much code
>consistently is by a great deal of code reuse.

Your definition of code reuse does not fit mine. You seem to change
your code during the re-use process and that's a serious no-no for me.
Once code is written and it works, it's filed off into the repository.
I may create another section of code that does something different but
that is another 'object'. Decent cataloguing means I can usually find
what I want fairly quickly.

It would involve a large configuration management headache if the only
things changed between one piece of code and the next is the paragraph
names. Incidently, I don't use paragraph names ever.

My only prefixing method comes down to ls- for linkage section items
which is a useful visual clue for inefficiency whilst coding. If I'm
doing too much with an ls-, it's time for a rethink. I prefix 78's
with 78- at the front also as I can then spot constants more easily. I
use Error- at the start of error numbers which relate to an error
handlers function.

>  Let me give a practical
>example of why what you just said is 'horse droppings.' ;-)

;-)

>
>Consider a section of code written to process an input screen.  The code
…[12 more quoted lines elided]…
>   05nnnn-...

I generally don't use screen layouts,  but I'll follow on...

>
>To duplicate that screen under number 22 instead of 05, all I have to do
…[5 more quoted lines elided]…
>screen 22 rather than screen 05.

If you have two identical screens, why not just work out the
commonality and re-use the same storage space in working storage?

Alternatively, stick the screen definition in a copy book and COPY ...
REPLACE it in. I'm not a fan of COPY ... REPLACING myself but that's
the usual way I've seen screen defs reused.

>  The main menu screens used in these
>systems use numbers 1, 2, etc. to select functions.  The screen layouts
…[4 more quoted lines elided]…
>which are difficult to remember and misuse,

Why not just use the same names again. What's stupid about two
programs having 'Write-Payroll-Record', 'Initialize-Staff-Data'. Seems
emminently more sensible and readible than 050000-Process-Screen-05?


> because the paragraph
>numbers make that unnecessary.  I even have a small BASIC program which
>scans my source code to flag all the times I reference a RECV-??- or
>SEND-??- field that do not match the current paragraph prefix.  

I understand the sensible approach to having similarly named data and
code but I don't have to remember the data names at all. A rough guess
is all you need - the editor does the rest. Guess I'm spoiled in that
manner. I also keep my code as small as possible and mostly event
driven so my code is usually at it's purest form, for interactive code
at least...

working-storage section.
copy "common78.cpy"        *> common #defs
copy "localws.cpy"         *> data specific to this module
copy "commonstruct.cpy"    *> shared data
procedure division.
    perform Initialize-data
    perform Initialize-display
    perform Display-Main-Screen
    perform event-loop until event-exit
    perform tidy-up
    stop run.

initialize-data section.
    ....

initialize-display section.
    move Screen-Handler-Init to Screen-Handler-Func
    call "screen-handler" using Screen-Handler-Func
    	on exception 
             move Error-Screen-Handler-Init to Error-No
             perform call-error-handler
    end-call
    .

Event-Loop section.
    perform Wait-for-event
    evaluate Event
    when No-Event
        perform sleep
    when Main-screen-exited
        perform process-main-screen
    when 
    when ...

    when Error-occurred
        perform call-error-handler
    end-evaluate
    .


Display-Main-Screen section.
   move Display-Screen to Screen-Handler-Func
   move Main-Screen to Screen-No
   call "screen-handler" using Screen-Handler-Func
                               Screen-No
                               return-data
       on exception
           move Error-Main-Screen to Error-No
           move Error-occurred to Event
   end-call
   move Next-Event to Event
   .

Call-Error-handler section.
   call "error-handler" using Error-no
   .


etc...

I usually use copy books only for data and prefer to keep my
procedural code in the one main file splitting it into called modules.
I don't let programs get so huge that they perform more than is
specific to them so Errors, screen handling, file handling and event
handling aren't part of the business logic so I keep them all in
seperate programs. Often the main program simply is there to farm out
events to the correct program. The file handlers and screen handlers
are usually generic so I can replace the file handler with a
networkable version or an SQL based version. It may involve a middle
file interface program or screen interface.

>You
>would not have any kind of cross-check like that without the paragraph
>numbering scheme.

I agree but I haven't coded that way from scratch for a long time. I
come across quite a few old programs like that, usually from a 4GL and
I adhere to that standard where it's used but almost everything I
write involves a seperate screen handler and data handler so that they
can be as abstract as possible. That way the application I write today
can be scaled to SQL Server or X-windows tomorrow without having to
re-write the core business logic.

>  But the scheme must be a complete system, it must
>reflect the program structure, and you must actually use it long enough
>to understand its benefits.

I can see that working on a screen based system but that's not the way
PC's work.

>  I have taught this system to dozens and
>dozens of programmers, and have yet to see one of them drop it.  Some
>of them were dragged into it kicking and screaming, but once they used
>it for a while, they would kick and scream if made to use anything
>else.  It works, and it works well.

I'm not doubting it. Any formalized methodolgy strictly enforced and
backed up with a coding standard will. However, I have enough problems
these days trying to get graduate programmers to understand non object
oriented coding. Some find it a real struggle.

Keeping the program in small event driven chunks and trying to
encapsulate as much as possible though not to the point of hiding
data, even with non-object COBOL works wonders for reliability, re-use
and maintenance given the correct tools.

>  I have never brought up a new
>system around someone unfamiliar with my techniques, without them
>making some comment about being impressed by the low error rate.

Ditto and made maintenance less of a chore. Break a problem down into
small chunks and keep it simple.

>  This
>is in large part because of heavy code reuse.  The benefit is there,
>as I have proved again and again to many skeptics over the years.  The
>productivity is there, the accuracy is there.  But you will never
>realize that until you give it a fair trial. :-)

Have you tried 'my' method above? 

I say 'my' as that's just about the way every major interactive app is
written within Micro Focus and you can see it externally if you've
ever used Dialog System, Panels (2), Fileshare, Animator2
```

###### ↳ ↳ ↳ Re: three-digit subprocedure listing

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6bMt2.2992$Fs.2793820@news4.mia>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com> <36b5ecf7.540011675@news.freeserve.net> <k7Ht2.2584$Xl5.3057930@news1.mia> <36b77d79.642541575@news.freeserve.net>`

```
Shaun C. Murray wrote:
>Judson McClendon wrote:
>>Shaun C. Murray wrote:
…[14 more quoted lines elided]…
>your editors really that bad still?


It has to do more with the kinds of programs written in COBOL than the
editor you use.  I write code in a number of languages.  I do not use
numbers in other languages for good reasons.  I use numbers in COBOL,
also for good reasons.  If you examined one of my C programs, for
example (say BIGCALC.ZIP from my website below), you would probably
agree with the structure.

>> I have averaged around 200,000 lines of code per year for the last
>>twelve years, at least.  The only way I can turn out that much code
…[7 more quoted lines elided]…
>what I want fairly quickly.

You're thinking of code designed to be reused.  Of the thousands of
COBOL programs I have seen, only a small percentage of the code would
classify for that kind of reuse.  For those routines, I certainly do
catalogue them as you suggest.  But the way I work, ALL the code is
suceptible for reuse, often even the whole program, sometimes with
minor changes.  And by modifying that code on reuse, I get tailored
code, specific to the needs of the task, just as if it had been
written that way, but with the advantage of being largely debugged
when it leaves my editor.  Not some 'supposed to fit' square-peg-in-a-
round-hole unchangable module.  Surely you have heard the wailing and
gnashing of teeth from those trying to make OO classes work the way
we were told OO would work? ;-)

>It would involve a large configuration management headache if the only
>things changed between one piece of code and the next is the paragraph
>names. Incidently, I don't use paragraph names ever.

The final result would not be two identical pieces of code, but two
very similar pieces of code.  Why would it require more 'management'
to maintain a piece of code, just because it was copied from another
program?  You have a narrow view of code reuse, which is part of what
I am trying to say here.  There is a broader view, which encompasses
your view of code reuse, but takes it a big step farther.

>>To duplicate that screen under number 22 instead of 05, all I have to do
>>is to make a copy of the code, then replace "RECV-05-" with "RECV-22-"
…[7 more quoted lines elided]…
>commonality and re-use the same storage space in working storage?

The point is that they are *not* identical, but often very *close* to
being the same.  That is why you often need a number of paragraphs in
one program which do the same thing, just slightly differently.  The
problem is, they are not similar enough to use a common routine.  With
no paragraph names, you are stuck trying to make one routine fit two
different uses, thus richly complicating the code, or of writing two
routines and thinking of different but similar names.  In larger COBOL
programs, there may be many of these.  Alpha prefixes would also do
the trick, but there are certain advantages to numeric prefixes.  The
ability to use them as subscripts, for example.  I won't go into the
details of that here, but there are a number of advantages to paragraph
numbers that I haven't even mentioned.  As I said, it is a whole system,
a whole different approach to code reuse.

>Alternatively, stick the screen definition in a copy book and COPY ...
>REPLACE it in. I'm not a fan of COPY ... REPLACING myself but that's
>the usual way I've seen screen defs reused.

If you could see these screens you would understand why that is not a
good idea.

>>  The main menu screens used in these
>>systems use numbers 1, 2, etc. to select functions.  The screen layouts
…[8 more quoted lines elided]…
>emminently more sensible and readible than 050000-Process-Screen-05?

Because screen 05 is unique!  And screen 07 is very, very similar, but
also unique!  And so is screen 22.  And you know for certain that screen
07 is going to be modified significantly, but screens 05 and 22 aren't.
(Not that you would know which specific screen will be changed, just
that clients do that.)  Like I said, it is the type of programs which
make this a worthwhile thing, not your programming tools.

>> because the paragraph
>>numbers make that unnecessary.  I even have a small BASIC program which
…[8 more quoted lines elided]…
>at least...

You're thinking data-names, but I'm talking about procedure names.  The
reason for adding a numeric part to screen names is that it helps when
you are associating the screen with the code, and when you want to
relocate the code or duplicate it elsewhere.  I do not recommend placing
numeric prefixes to all data-names, only in screen names, because they
are a special case.  Again, you need to see the programs to appreciate
how this works.

>>  But the scheme must be a complete system, it must
>>reflect the program structure, and you must actually use it long enough
…[3 more quoted lines elided]…
>PC's work.

They can when you use the COBOL SCREEN SECTION, which will be in the
next standard.  Not every application needs GUI.  When you have a clerk
sitting at a terminal/PC all day entering data, a GUI can actually be
significantly counterproductive.  There is no human who can take their
hands from the keyboard to the mouse, move the mouse and click the
button, faster than they can press a single key.  Yet the conventional
wisdom is "GUI is better".  GUI *can* be better, for some things, but
GUI *can* be worse for other things.

>Keeping the program in small event driven chunks and trying to
>encapsulate as much as possible though not to the point of hiding
>data, even with non-object COBOL works wonders for reliability, re-use
>and maintenance given the correct tools.

I have nothing against those goals.  But different kinds of programming
tasks can often be better approached using different methods.  Just as
GUI is not better for every application, specific coding techniques are
not always best suited for avery kind of application.  There is a
mindset today which says "newer is better".  Our culture is virtually
addicted to change.  Newer is often better, but newer is sometimes worse,
too.  And newer is very seldom better in all cases and for all things.
The hammer is a tool which has not been improved in a long, long time.
Not because people haven't tried, but because some things cannot be
improved, or at least not easily.

>>  This
>>is in large part because of heavy code reuse.  The benefit is there,
…[4 more quoted lines elided]…
>Have you tried 'my' method above?

Absolutely!  The methods I use depend on what kind of application I am
writing, and in what language I am writing it.  What I am trying to say
is that many people have "thrown the baby out with the dishwater", when
they relagate all older coding practices to the trash heap and assume
that only newer techniques are best.  I say evaluate techniques on how
productive they are in proven situations, not how well they reflect the
coding paradigm 'du jour'.  For example, our industry has "bought a pig
in a poke" by mindlessly running for OO without sufficient real live
data showing that it will do what it
```

###### ↳ ↳ ↳ Re: three-digit subprocedure listing

_(reply depth: 5)_

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b81e18.683660912@news.freeserve.net>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com> <36b5ecf7.540011675@news.freeserve.net> <k7Ht2.2584$Xl5.3057930@news1.mia> <36b77d79.642541575@news.freeserve.net> <6bMt2.2992$Fs.2793820@news4.mia>`

```
On Tue, 02 Feb 1999 23:50:26 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:

>Shaun C. Murray wrote:
>
…[3 more quoted lines elided]…
>numbers in other languages for good reasons.

Are you writing the same kinds of programs though? or picking your
language for it's specific benefits?

That would kind of make programming practice a bit tricky to compare.
If you're writing the same program in each language, why alter
practices drastically across C, COBOL or BASIC?

Incidently, I don't see how you could apply a traditional COBOL
methodolgy to current BASIC and C++ RAD compilers without using them
in a way that would prove obtuse to non-COBOL developers.

>  I use numbers in COBOL,
>also for good reasons.  If you examined one of my C programs, for
>example (say BIGCALC.ZIP from my website below), you would probably
>agree with the structure.

Your C code is lovely. Not too dissimilar to the way I wrote C
programs. You can spot the COBOL influence of simple statements and
not too much embedded in one statement.


>
>>> I have averaged around 200,000 lines of code per year for the last
…[10 more quoted lines elided]…
>You're thinking of code designed to be reused.  

Almost all my code is designed to be reused. It pays dividends in the
long run. The reuseable asset manangement system we have in place at
work has....<opens web browser>...<click>...<click>....18,412
reuseable chunks of code, docs, graphics and other bits sorted by
language, certification level, market sector, use, description etc.


>Of the thousands of
>COBOL programs I have seen, only a small percentage of the code would
>classify for that kind of reuse.

..then I suggest you take a new look at reuse and your code practices.
100% reusability is next to impossible but if you are only approaching
'a small percentage' in new systems I'd be concerned.


>  For those routines, I certainly do
>catalogue them as you suggest.  But the way I work, ALL the code is
>suceptible for reuse, often even the whole program, sometimes with
>minor changes.

perfectly valid.

>  And by modifying that code on reuse, I get tailored
>code, specific to the needs of the task, just as if it had been
>written that way, but with the advantage of being largely debugged
>when it leaves my editor.

That's fine but it's a new 'asset'. If I find an asset that almost
fits what I want I usually ask myself,  'Are you sure you couldn't
have written the code fragment in a more reusable way in the first
place?' and 'Before I put this new code back, can I make it work in a
reusable way such that it supercedes the old code?'

>  Not some 'supposed to fit' square-peg-in-a-
>round-hole unchangable module.  Surely you have heard the wailing and
>gnashing of teeth from those trying to make OO classes work the way
>we were told OO would work? ;-)

Sure. Done it myself with Delphi and a reusable set of business
objects that weren't quite what I wanted. Re-useable code assets have
nothing to do with OO though. 

>
>>It would involve a large configuration management headache if the only
…[6 more quoted lines elided]…
>program?

Because if you fix a bug in one program, what practice is in place to
ensure that the same fix gets into the other similar piece of code?

I spent 6 years porting english language products to Japan. Each time
a new version of the english product came out, I had to retrofit fixes
into it before adding links into my Japan specific parts. Eventually I
managed to get the english product guys to take my code changes and
the code ran happily on both.


>  You have a narrow view of code reuse, which is part of what
>I am trying to say here.  There is a broader view, which encompasses
>your view of code reuse, but takes it a big step farther.

IMNSHO, code reuse via taking an existing working section of code and
modifying to run in two places is a very narrow view of code reuse
that can only create problems in later life. It would be a
retrogressive step if I went back to reusing code the old way.

[snip]

>  The
>problem is, they are not similar enough to use a common routine.  With
>no paragraph names, you are stuck trying to make one routine fit two
>different uses,

No. Look back at my code. If I had two different screens, they'd
generate a different event and/or screen id. Evaluate on that, perform
the specific routine. My sections are single purpose.

> thus richly complicating the code, or of writing two
>routines and thinking of different but similar names.

No problem but I prefer to use Update-Order-Screen to
05000-update-screen-05.


>  In larger COBOL
>programs, there may be many of these.

I don't tend to use large COBOL programs. Typically each program has a
self contained purpose. I don't have programs that generate multiple
reports, I'll have a program for each report and a generic report
handler.

>  Alpha prefixes would also do
>the trick, but there are certain advantages to numeric prefixes.  The
>ability to use them as subscripts, for example.  I won't go into the
>details of that here, 

I'd rather you didn't.

>but there are a number of advantages to paragraph
>numbers that I haven't even mentioned.  As I said, it is a whole system,
>a whole different approach to code reuse.

Forgive me for sounding facetious but it sounds like 'The Old Ways'. I
stopped doing that 8-9 years ago for large projects. I may still
revert to it for one-offs for a quick hack but it's of no use to me in
my usual development.

>
>>Alternatively, stick the screen definition in a copy book and COPY ...
…[4 more quoted lines elided]…
>good idea.

;-) All I was saying is I've seen that used extensively.

>>
>>Why not just use the same names again. What's stupid about two
…[8 more quoted lines elided]…
>make this a worthwhile thing, not your programming tools.

Usually, each program I have looks after a particular screen or two
and no more so usually the program is associated with a screen and not
a particular paragraph so having sensible names and reuseing the same
name in each is no problem.

>
>You're thinking data-names, but I'm talking about procedure names.  The
>reason for adding a numeric part to screen names is that it helps when
>you are associating the screen with the code,

I work on the event level so the screen is abstracted from the
business logic. That way, my procedure code is not directly associated
with any screen layout.

> and when you want to
>relocate the code or duplicate it elsewhere.  I do not recommend placing
>numeric prefixes to all data-names, only in screen names, because they
>are a special case.  Again, you need to see the programs to appreciate
>how this works.

Not really, I used that in the past. 

>
>>>  But the scheme must be a complete system, it must
…[6 more quoted lines elided]…
>They can when you use the COBOL SCREEN SECTION,

I've only rarely used screen section code. It's to tied to the
procedural code to enable scaling the application unless you treat
each screen and the code to handle the screen as a single entity. Then
it's no big deal if you have to re-write a dinky small screen accept
program.

Even then, I prefer to use working-storage and run-time calls to
display screens and manipulate attributes.

But that's old hat. Much prefer to use a seperate screen handler. Even
prefer Dialog system to doing it the old way.


> which will be in the
>next standard.  Not every application needs GUI.

You miss the point. I abstract the interface from the application so
the interface could be anything. Tying you business logic to interface
code results in all your programs looking the same and no reuse of
business logic without attached screens. If one client wants text
based and the other wants GUI but the underlying logic is the same
that means two specific programs.

>  When you have a clerk
>sitting at a terminal/PC all day entering data, a GUI can actually be
…[4 more quoted lines elided]…
>GUI *can* be worse for other things.

Agree entirely. That's why I don't tie the logic with the interface.

>
>>Keeping the program in small event driven chunks and trying to
…[13 more quoted lines elided]…
>improved, or at least not easily.

Agree again entirely. But I also believe in not re-inventing the wheel
again.

>
>>>  This
…[11 more quoted lines elided]…
>that only newer techniques are best.

I'm not assuming anything. 

>  I say evaluate techniques on how
>productive they are in proven situations, not how well they reflect the
>coding paradigm 'du jour'.

I can hardly be described as being 'du jour'. Current 'du jour' would
be 'patterns' and object modelling languages or am I a little passe.


>  For example, our industry has "bought a pig
>in a poke" by mindlessly running for OO without sufficient real live
>data showing that it will do what it

Agree again but I've yet to come across a development project that
really understands what OO means. My earlier bit about reusable assets
is a step in the right direction but all too often I see OO
development where they haven't reused their objects - what's the
point.
```

##### ↳ ↳ Re: three-digit subprocedure listing

- **From:** NoLonger@ix.netcom.com (OldUncleMe)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b6750e.30548290@news>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com> <36b5ecf7.540011675@news.freeserve.net>`

```
On Mon, 01 Feb 1999 18:14:28 GMT "scm@bolo.freeserve.co.uk (Shaun C. Murray)" posted
to "comp.lang.cobol" about: "Re: three-digit subprocedure listing" :

-->On Sat, 30 Jan 1999 17:09:22 GMT, john_meyer@my-dejanews.com wrote:
-->
-->>Hi, our professor wants us to use the nnn-<verb>-<adj>-<noun> approach to
-->>naming subprocedures.  Problem is, I can't find the directory listing what
-->>all the nnn numbers are (100 level versus a 999 level).  Can somebody help
-->>me?
-->
-->There is no rule to this unless your professor has a standard to which
-->you should adhere. Common practice at one place I've worked used to be
-->to have a letter then three digits. You'd have something like
-->
<..snop..>

-->Modern editors have code completion. So I type the first few letters
-->of the name of the data-item or section name, press the code
-->completeion key and it fills in the rest.
-->Shaun


I haven't ever seen/used an (cobol) editing program with code completion.  Never
heard of it before.  In fact, the only cobol specific editor I have encountered is
the editor that comes with Fujitsu v.3.  

Are there any examples of such that you know of for pc or linux?   Or is this a
mainframe specific resource?   Thanks, preciate any pointers.   TS


"Come to think of it, there are already a million monkeys on a million
 typewriters, and Usenet is NOTHING like Shakespeare." Blair Houghton
*********No generalization is wholly true, not even this one**********
++++++****tauceti****@****abraxis****.****com****for***email****++++++
```

###### ↳ ↳ ↳ Re: three-digit subprocedure listing

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b70599.611853588@news.freeserve.net>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com> <36b5ecf7.540011675@news.freeserve.net> <36b6750e.30548290@news>`

```
On Tue, 02 Feb 1999 03:50:11 GMT, NoLonger@ix.netcom.com (OldUncleMe)
wrote:


>
>
…[6 more quoted lines elided]…
>

Micro Focus have had it in their Editor/Animator since 1994-5 ish.
Delphi, VB, VC++ etc all have it too although Delphi is less than
perfect until you add GExperts to get Grep and a decent procedure
lookup.

Most of the Windows based programmers editors like SlickEdit and
MultiEdit have source code intelligence too but even though I used to
work for Micro Focus, I can honestly say, no-one that I've seen have
done it better.
```

#### ↳ Re: three-digit subprocedure listing

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-02-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<798at7$e5j$1@oak.prod.itd.earthlink.net>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com>`

```
And yet another reason for paragraph numbering.

     PERFORM BOOGIE-BOOGIE

And just where in the hell in this 60-page listing is
paragraph BOOGIE-BOOGIE? OTHO,

   PERFORM P1310-BOOGIE-BOOGIE

is easier to find.
```

##### ↳ ↳ Re: three-digit subprocedure listing

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36b82e96.687883293@news.freeserve.net>`
- **References:** `<78vebs$im$1@nnrp1.dejanews.com> <798at7$e5j$1@oak.prod.itd.earthlink.net>`

```
On Tue, 2 Feb 1999 20:11:06 -0600, "Jerry Peacock"
<bismail@bisusa.com> wrote:

>And yet another reason for paragraph numbering.
>
…[3 more quoted lines elided]…
>paragraph BOOGIE-BOOGIE? OTHO,

Paper. How quaint.;-)

It's easy. I stick the cursor on BOOGIE-BOOGIE and hit Ctrl+L

>
>   PERFORM P1310-BOOGIE-BOOGIE
>
>is easier to find.

No it isn't.

Now try remembering what you prefixed your BOOGIE-BOOGIE routine with
when you're 10 pages away from it. 
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
