[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hiding methods

_12 messages · 8 participants · 2000-03_

---

### Hiding methods

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C92303.4E8B6E3A@cusys.edu>`

```
We have some purchased code which have called routines (sometimes more
than one program deep) to do common I/O.

One of these accesses a KSDS file.  We first pass it values to open the
file, later, to access records, and finally to close the file.  I have
no idea what advantage we gain over doing these commands in our program.

But I have had to copy some of these programs to my PDS, and compile to
my load library, to find out what's going on.

For instance, I did an open, and the VSAM program passed back an error
code of 7.  This is a generic error for a return code of not '00'.  So I
made a copy of this with some displays and discovered that the return
code was '97', which means "OPEN statement execution successful:  File
integrity verified."

The word shouldn't be "hide", it should be "obfuscate".

I'm afraid that there are too many programmers of the quality of those
who designed and wrote this system, and that if they do so using OO,
they will find it much easier to obfuscate without becoming better at
designing and programming.
```

#### ↳ Re: Hiding methods

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C94911.E785F744@home.com>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu>`

```


Howard Brazee wrote:
> 
> The word shouldn't be "hide", it should be "obfuscate".
…[4 more quoted lines elided]…
> designing and programming.

Lots of merit in that thought. But - let's make packages of public
domain OO source code (gotta have generic classes Ken - I'll come back
to that with numbers). Who does these packages - people like Judson for
dates, Michael M. for pic 9 conversion routines, Cheesle, Ib, Guy, Lief,
Thane etc.- you wouldn't accept code from these guys ? Dare you ! Say it
publicly :-)

Now the interesting thing is if we've got these 'dedicated' people
utilizing the language giving us all sorts of well proven public domain
classes that we can pull from - kinda reduces the need for our large
COBOL workforce doesn't it ?

Remember Pete Dashwood and his "Who Cares ?". "Please print me an
invoice, Mr. computer", and the logic that the oh-so-so programmers
become obsolete. With these comprehensively tested  packaged modules,
because they've been broken down into simple, effective methods - why
are all those programmers re-inventing the wheel to tackle Windows GUIs
- see Judsons's recent thoughts on the latter topic. (??????)

Jimmy
```

#### ↳ Re: Hiding methods

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8abn1j$sl$1@nnrp1.deja.com>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu>`

```


> So I
> made a copy of this with some displays and discovered that the return
> code was '97', which means "OPEN statement execution successful:  File
> integrity verified."
>

Howard,

A sidenote (FWIW), one reason you'll get a '97' is because the file is
open and enabled to CICS.

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Hiding methods

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C9691C.BB25C5AA@cusys.edu>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu> <8abn1j$sl$1@nnrp1.deja.com>`

```
WOB Consulting wrote:
> 
> > So I
…[10 more quoted lines elided]…
> WOB

That makes sense.  Or it would, if we had CICS.  Maybe IDMS was the last
thing to use it.  At any rate - the obfuscating program which turned a
non-zero VSAM return code into a 7 return code from their table didn't
realize that a VSAM return of 97 was a successful value.  If it had
returned the VSAM return code, I could have decided to continue
processing.  And it is difficult to go through the channels to change
and test a program which gets called so often.

If a commonly used called program (or an OO object) needs to be changed,
most programmers under a deadline (I would guess that more than 3% of
all programmers are under deadlines) will find a way around using the
common module, if given half of a chance.

That is, unless they don't believe in testing, don't have to document
their changes, and don't need to get permission to make changes which
effect other applications...

I wonder how much this enters into the figures I have seen about low
rates of object reuse?
```

#### ↳ Re: Hiding methods

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<igUMOGA0rWy4EwOJ@ld50macca.demon.co.uk>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu>`

```
Howard, you must be much younger than me. I too have encountered code as
you describe and believe it was written that way for two reasons: top
down modular programming was all the rage and (in those days) people had
difficulty understanding VSAM file accessing and return code processing.
By coding modules that correctly check and process return codes then you
can save effort and prevent incorrect status code checking. One program
I encountered (written in Natural and not Cobol) had 16 hard-coded reads
of a file. Half of them checked for end of file and change of key and
half did not. I believe that the program was pricing incorrectly, and
still is, but could not prove my case.

VSAM status code 97 is an error as far as I am aware. Right now I can
not find my VSAM error codes list but all 9x statuses (why am I thinking
of Windows?) are errors.

Finally, the guys who wrote the code about which you are complaining
were only doing their best at that time. Personally, I hate top-down
structured programs and love JSP.

In article <38C92303.4E8B6E3A@cusys.edu>, Howard Brazee
<howard.brazee@cusys.edu> writes
>We have some purchased code which have called routines (sometimes more
>than one program deep) to do common I/O.
…[19 more quoted lines elided]…
>designing and programming.
```

##### ↳ ↳ Re: Hiding methods

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C97342.7049B585@cusys.edu>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu> <igUMOGA0rWy4EwOJ@ld50macca.demon.co.uk>`

```
Alistair Maclean wrote:
> 
> Howard, you must be much younger than me. I too have encountered code as
…[8 more quoted lines elided]…
> still is, but could not prove my case.

I wrote my first COBOL program in 1969.  While I may be much younger
than you, I suspect your first COBOL program isn't much older than
mine.  I do remember when VSAM came out and the confusion which
resulted.  I also converted all of the files from a Univac 9030 to VSAM
to keep the same functionality we had before.  There were more RRDS than
KSDS files and more ESDS than RRDS files in that system.  Who uses RRDS
and ESDS anymore?  Heck, even KSDS is being replaced by databases more
places than not.

But this program still requires that you know how to open, access, and
close your file, except that you now check different return codes for a
smaller number of different values.  Is it easier to look at that
program to determine return codes than at the VSAM manual?

We also have a called program which reads input cards, for no reason
that I can discover.

I guess these calling programs mean that we don't have to have SELECT
clauses, if that is an advantage.
```

###### ↳ ↳ ↳ Re: Hiding methods

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8196C4A9B566C30C.9237BEDB8D67098B.AEBBDD6BCB96E72E@lp.airnews.net>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu> <igUMOGA0rWy4EwOJ@ld50macca.demon.co.uk> <38C97342.7049B585@cusys.edu>`

```
On Fri, 10 Mar 2000 15:12:18 -0700, Howard Brazee
<howard.brazee@cusys.edu> enlightened us:

>Alistair Maclean wrote:
>> 
…[29 more quoted lines elided]…
>clauses, if that is an advantage.

Howard the company I work for, which writes and markets mainframe
software, has a similar set of subroutines to do all I/O.  One of the
reasons is that we must support VSE and MVS systems, and the way I/O
is handled in Cobol is different.  We can leave the main Cobol
programs alone and just distribute different I/O routines (written in
Assembler).  Also, it is a way to standardize DD names (DLBL in VSE)
between our systems and programs.  Another, now less necessary reason,
is speed.  Not that long ago, Cobol I/O routines were much slower than
I/O written in Assembler using I/O macroes.  That isn't true anymore.

As for design considerations, these subroutines were written more than
10 years ago and have never needed to be changed.  We also distribute
the source code for these and a way for the client to generate their
own Assembler I/O routines.  I've been using these for so long now I'd
be hard pressed to write a Select statement in Cobol without looking
it up first!

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Only in America... do we use the word "politics" to
describe the process so well: "Poli" in Latin meaning
"many" and "tics" meaning "blood-sucking creatures"... 




Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: Hiding methods

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CAC198.A9DB87BE@home.com>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu> <igUMOGA0rWy4EwOJ@ld50macca.demon.co.uk> <38C97342.7049B585@cusys.edu> <8196C4A9B566C30C.9237BEDB8D67098B.AEBBDD6BCB96E72E@lp.airnews.net>`

```


SkippyPB wrote:
> 
> On Fri, 10 Mar 2000 15:12:18 -0700, Howard Brazee
…[8 more quoted lines elided]…
> it up first!

Skippy, Interesting what you are describing - but my interest is that
this should be public domain source code. Heavens No ! Says the boss.
But you've already given it away to your clients, and their programming
teams - they haven't purloined a copy as they moved on ?. Same goes for
you own guys ten years back surreptitiously stuffing a briefcase with
goodies on their way out the door. (But we had legal documents drawn up.
Ha!)

I wonder just how many mainframe installations have taken a round object
and invented exactly the same wheel as you. If people forget privacy and
personal ego - public domain source can only but benefit the COBOL clan.

Jimmy
```

###### ↳ ↳ ↳ Re: Hiding methods

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E017A69CD5ECBDEE.BC755D0317500213.B3B014A02178CB7E@lp.airnews.net>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu> <igUMOGA0rWy4EwOJ@ld50macca.demon.co.uk> <38C97342.7049B585@cusys.edu> <8196C4A9B566C30C.9237BEDB8D67098B.AEBBDD6BCB96E72E@lp.airnews.net> <38CAC198.A9DB87BE@home.com>`

```
On Sat, 11 Mar 2000 22:03:23 GMT, "James J. Gavan" <jjgavan@home.com>
enlightened us:

>
>
…[25 more quoted lines elided]…
>Jimmy

Interesting point for which I have no answer.  I can say having seen
other companies software products that I've had to convert off of that
I've never seen anything similar to our I/O routines.  That doesn't
mean they don't exist.  The idea of making them Public Domain is a
good one as they are very beneficial.  In Cobol you don't need to code
Selects or FD's.  The record descriptions are all in Working Storage.
There are standardized I/O return codes that cover all errors no
matter what the file structure (VSAM, Sequential, tape, disk etc). And
there is never any confusion on variable record size as the the 4
bytes are alsways described in the Working Storage record description
and the Assembler I/O routines takes care of everything else.
Personally I'd love to publish this, but as I've had to sign a non
disclosure agreement way back when, that is not possible.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Only in America... do we use the word "politics" to
describe the process so well: "Poli" in Latin meaning
"many" and "tics" meaning "blood-sucking creatures"... 




Remove nospam to email me.

 Steve
```

##### ↳ ↳ Re: Hiding methods

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38c9e0e7.183731089@news.cox-internet.com>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu> <igUMOGA0rWy4EwOJ@ld50macca.demon.co.uk>`

```
On Fri, 10 Mar 2000 21:36:52 +0000, Alistair Maclean
<LD50Macca@ld50macca.demon.co.uk> wrote:

>VSAM status code 97 is an error as far as I am aware. Right now I can
>not find my VSAM error codes list but all 9x statuses (why am I thinking
>of Windows?) are errors.
>

I've seen 97's on the first open of a VSAM file after the last program
updating the file crashed.  IBM didn't used to return that status, and
it's the only 9X status that is not an error.  The next time the file
is opened, 00 is returned.
```

#### ↳ Re: Hiding methods

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7Pgy4.1940$xL1.214243@dfiatx1-snr1.gtei.net>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu>`

```
Sometimes "hiding" is good.

I am currently doing some re-engineering of a client's system, and have I
"learned" some new techniques for working with VSAM files:

1. If the value to be tested for validity against a VSAM file has a business
rule which precludes it's being valid, use this code:

    MOVE  23   to  FILE-STATUS

2. If, on the other hand, the value is auomatically valid (e.g., preferred
customer):

   MOVE ZEROES      to  FILE-STATUS

3. And in case your education is not complete, I did not forget that while
FILE STATUS is defined as alphanumeric on IBM Mainframes, it can be so
convenient to define it as PIC 99.

Needless to say, the original author was not terribly facile about handling
a "virgin" KSDS VSAM file. So instead of checking for status '35', she just
ignored OPEN errors and let the program ABEND when the first READ failed.

Now, tell me I don't have a case for writing a a file I-O module and hiding
the source.
```

##### ↳ ↳ Re: Hiding methods

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8acc0i$lh7$1@news.igs.net>`
- **References:** `<38C92303.4E8B6E3A@cusys.edu> <7Pgy4.1940$xL1.214243@dfiatx1-snr1.gtei.net>`

```
Maybe you should hide it where nobody can ever find it again...

Michael Mattias wrote in message
<7Pgy4.1940$xL1.214243@dfiatx1-snr1.gtei.net>...
>Sometimes "hiding" is good.
>
…[3 more quoted lines elided]…
>1. If the value to be tested for validity against a VSAM file has a
business
>rule which precludes it's being valid, use this code:
>
…[40 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
