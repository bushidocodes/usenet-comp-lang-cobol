[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Structure me this - Part 2

_36 messages · 19 participants · 2000-05_

---

### Structure me this - Part 2

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fm7me$a26$1@nnrp1.deja.com>`

```



Hi:

It's all Bob Wolfe's fault. If he had never told
me about the CLC, I would never have gotten into
this mess. . .

Anyway, since I did get into this mess I have
been called self-serving, arrogant, myopic,
thick, an idiot, and had my words described as
'horseshit'. This is probably because
people take my remarks personally and may
feel guilty. . .  :)

One would wonder why I continue, so I did.
After wondering, I came to the conclusion
that I believe in what I talk about but
regret that I cannot make my points in
a way which would create less vitriolic
responses. :(

What provoked the 'Structure me this' thread
was the comment that some nitwit gave some
guy an 'F' because he used a single GO TO
in his test program. I was further provoked
by those who insist that the use of GO TO
should be totally abolished and GO TO
should never appear in a COBOL program for
any reason and that to use GO TO is
tantamount to pissing on the altar of
structured programming.

To me this nonsense about banishing GO TO
is RIDICULOUS. To fail someone for using
a single GO TO is ABSURD. To maintain
that GO TO should never be used under
any circumstances is PREPOSTEROUS.

Has programming become the art of figuring
out how to do stuff without the use of
GO TO and in accordance with a lot of
arbitrary, structured rules without
regard to whether it actually makes sense?

Another thing which I find annoying is the
use of incomplete examples to illustrate the
structured style. One of the respondents to
the original thread used 'perform open-file-for-io'
instead of the code I posted. Of course, he
did not include the 'open-file-for-io'
paragraph. Similarly, people post stuff
like:

evaluate blob
 when blob is this perform that
 when blob is something-else perform something-else
 when blob is another-thing perform another-thing

and so on. They never include the 'that' code or
the 'something-else' code or the 'another-thing'
code so, to me, the samples are useless for it
is in the 'that' and the 'something-else' paragraphs
where the meat of the program is, the evaluate
is just fat. (Dear Flamers: In the above, ignore
the fact that the condition-name and the name of
the performed paragraph are the same.)

To carry it to its absurd conclusion -
why not just do this:

procedure division
perform do-what-is-required
stop run
.

So, I slung together a few lines of code
and asked people to show me how to make
it better by eliminating the GO TOs. I
did not stop to consider the ramifications
inherent in the hostile environment into
which it was introduced.

Whether the code originally offered is
good or bad or right or wrong or
whatever, it was provided for one purpose
only, to give people the opportunity to show
me how to do it with no GO TOs.

Whether the code is all in upper-case
is irrelevant.

Whether it is not in accordance with
your stylistic preference is irrelevant.
After all, the object of the exercise
is to rewrite it in the style of your
choice. . .

Whether 'Filename' is a reserved word
on VAX is irrelevant.

Whether using 'FILE-STATUS' in both
paragraphs rather than two separate
fields is irrelevant.

Whether the file-status may be subject
to interpretation depending on platform
is irrelevant.

Whether the code uses commas is irrelevant.

Whether the code is reusable is irrelevant.

Whether the naming convention is right or
wrong or good or bad is irrelevant.

Whether the user has 'permissions' or
an 'inode' (whatever that might be)
is irrelevant.

Whether the file-status checks after the
OPEN OUTPUT and the CLOSE are omitted
is irrelevant. (If I put them in then
the assignment to eliminate the GO TO
becomes much harder.) They were left
out to keep it simple.

Making the sort of dwarfian comment like
'well if all this is irrelevant, why
bother' is avoiding the issue.

So, in your roles as the senior citizens
of the COBOL community, pretend that I
am some thick idiot who is just learning
to code and doesn't know any better who
wrote the stuff originally posted, and,
in your unusual kind and gentle way, show me
how to write the functional equivalent
without using GO TO - show me The Way.

Whether the code works or whether
any of the stuff mentioned above
(all of which were taken from
messages posted to the original
thread) is relevant is not the
point.

Just take those few lines of code
and rewrite them so that you have
a FUNCTIONAL EQUIVALENT without the
GO TOs and SHOW ME. (Thank you,
Mr. Brandke for your amusing example.)

Please, do not post to this thread unless
you are going to post functionally
equivalent code. If you want to challenge
things I have said in this message, start
a new thread called 'Dilworth is a dimwit'
or 'Drop Dead Dilly' or 'F-Off Foodman' or
something, but let's not clutter up this
thread with irrelevant stuff. I will be
pleased to continue jousting in another
thread, he said. . .

Hey, look at it this way, if it weren't
for me, you'd just have to talk about how
to make your Netexpress program write
files to be read by a Java program
using Oracle on a Unix box so that a C++
program on a mainframe could convert
the file so that it could be used by VB
under NT running Novell and whether or
not to use RAD or OO to do it, and similarly
rewarding topics, he said sarcastically,
ignoring, pro tem, the fact that sarcasm
is the lowest form of wit.

:)

Thanks

Tony Dilworth




Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Structure me this - Part 2

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fmao5$ddl$1@nnrp1.deja.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com>`

```
Hi:

Since I started this thread, Bill Klein provided us
with a sample of how the code would be written in
the structured GO TO-less style in the other "structure
me this' thread.

The example Bill provided was the sort of thing which
I was expecting to receive.

As Bill points out in his message, he wouldn't do it
that way.

I wonder, why would anyone do it that way? In the name
of eliminating GO TO? In order to live within the
structured rules?

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Structure me this - Part 2

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fmdn9$ola$1@news.igs.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <8fmao5$ddl$1@nnrp1.deja.com>`

```
Foodman wrote in message <8fmao5$ddl$1@nnrp1.deja.com>...

>I wonder, why would anyone do it that way? In the name
>of eliminating GO TO? In order to live within the
>structured rules?
>
He did it that way because you begged him to.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fmk0t$mg5$1@nnrp1.deja.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <8fmao5$ddl$1@nnrp1.deja.com> <8fmdn9$ola$1@news.igs.net>`

```

> >
> He did it that way because you begged him to.
>
>

Hi:

I really didn't want to make this a thread, but I am
not going to ignore your comment because of that. So,
if people want to post in here go ahead.

I didn't beg him to do anything. Furthermore, he
took the time and effort to perfectly illustrate
how someone would do something NOT using GO TO
and in accordance with the 'rules' of structured
coding which was what I was looking for in the
first place. Maybe I didn't make that clear
enough, oh well.

From what I have seen, people do actually code
things in the style which Mr. Klein illustrated
and, that style is often touted as the one
and only way.

My whole observation is that adding these
arbritrary rules and regulations about not
GO TOing and being rigidly structured add
additional layers of 'fat' which do not
necessarily make things easier to understand.

As I keep on saying, you can write lean and
efficient and easily understood and easily
modified programs without resorting to that
stuff.

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Structure me this - Part 2

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gvdjk$m8e$1@slb6.atl.mindspring.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <8fmao5$ddl$1@nnrp1.deja.com>`

```

"Foodman" <foodman123@aol.com> wrote in message news:8fmao5
>
> As Bill points out in his message, he wouldn't do it
…[5 more quoted lines elided]…
>

The answer to this one is that I *would* do it if I was working in a shop
that this was a "required shop standard".  Now the next question would be WHY
would one (i.e. managment) make this a required shop standard.  The answer to
that one is that SOME programmers use GO TO's in "hard to maintain" ways.
Therefore, (in some LARGE shops - with new programmers who are not adequately
supervised) it is easier to prohibt GO TOs completely rather than to try and
train and monitor so that they are only used in a "structured" (and
maintainable) way.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OTOY4.286$js2.24916@dfiatx1-snr1.gtei.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <8fmao5$ddl$1@nnrp1.deja.com> <8gvdjk$m8e$1@slb6.atl.mindspring.net>`

```
William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8gvdjk$m8e$1@slb6.atl.mindspring.net...
>
> "Foodman" <foodman123@aol.com> wrote in message news:8fmao5
…[8 more quoted lines elided]…
> that this was a "required shop standard".  Now the next question would be
WHY
> would one (i.e. managment) make this a required shop standard.  The answer
to
> that one is that SOME programmers use GO TO's in "hard to maintain" ways.
> Therefore, (in some LARGE shops - with new programmers who are not
adequately
> supervised) it is easier to prohibt GO TOs completely rather than to try
and
> train and monitor so that they are only used in a "structured" (and
> maintainable) way.
>


Excellent point, sir: Easier to prohibit the use altogether than invest in
the training required for responsible use.

But please, do not construe these kudos as applying to personal firearms!

MCM
```

#### ↳ Re: Structure me this - Part 2

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kfAT4.2360$hm2.371456@dfiatx1-snr1.gtei.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com>`

```
Foodman <foodman123@aol.com> wrote in message
news:8fm7me$a26$1@nnrp1.deja.com...
>
> Anyway, since I did get into this mess[c.l.c] I have
> been called self-serving, arrogant, myopic,
> thick, an idiot, and had my words described as
> 'horseshit'.

I am sorry. What did we forget?

Sheesh, look at the bright side: there are those here who would prefer to
just shoot someone who can be positively identified as the instigator of a
"GO TO" war!

MCM
```

##### ↳ ↳ Re: Structure me this - Part 2

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fmks0$nj8$1@nnrp1.deja.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <kfAT4.2360$hm2.371456@dfiatx1-snr1.gtei.net>`

```

>
> Sheesh, look at the bright side: there are those here who would
prefer to
> just shoot someone who can be positively identified as the instigator
of a
> "GO TO" war!
>
> MCM

Hi:

Oh well, not having been in CLC for that long (although
sometimes it feels like years), I didn't know that
GO TO wars were frowned upon. This is the first
one I have participated in.

Thanks

TONy Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3920056D.57C79105@cusys.edu>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <kfAT4.2360$hm2.371456@dfiatx1-snr1.gtei.net> <8fmks0$nj8$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> Oh well, not having been in CLC for that long (although
> sometimes it feels like years), I didn't know that
> GO TO wars were frowned upon. This is the first
> one I have participated in.

Me neither.  I always liked the issue of Life Magazine GOes TO war.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 4)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k8p0iso81750o2f21gq53henj77rmg260l@4ax.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <kfAT4.2360$hm2.371456@dfiatx1-snr1.gtei.net> <8fmks0$nj8$1@nnrp1.deja.com> <3920056D.57C79105@cusys.edu>`

```
i have never done bug-proofed code, but here's how i would handle the
open-read-close

	SELECT somefile ASSIGN TO "somefile"
	organization is indexed
	record key is somekey
	access is sequential
	FILE STATUS IS file-status
	.

	02 file-status-compare.
		03 first-char pic x.
		03 second-char pic x.
	02 end-condition pic x.

	open input somefile
	if file-status-compare = "35"
		display "creating file"
		open output somefile
		close somefile
		open input somefile
	end-if
	move first-char to end condition
	perform with test before until end-condition is not zero
		READ somefile.
*you'll notice the period
			if file-status is zeros
				perform your-report-stuff-here
			end-if
	end-perform
	if file-status is not zeros
		display "there was some error"
	end-if
	exit-program
	.

*i am not even sure if this code works, it was a 5 minute job for the
*structured read challenge.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 5)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<al62is0f9qms06ho9025mhdfgt7jhhr0p2@4ax.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <kfAT4.2360$hm2.371456@dfiatx1-snr1.gtei.net> <8fmks0$nj8$1@nnrp1.deja.com> <3920056D.57C79105@cusys.edu> <k8p0iso81750o2f21gq53henj77rmg260l@4ax.com>`

```
On Mon, 15 May 2000 19:06:56 -0400, G Moore <gvwmoore@spam.ix.netcom.com> wrote:

<skipped>
>	perform with test before until end-condition is not zero
>		READ somefile.
>*you'll notice the period

Yep - and this is (at least with my compiler from IBM) a serious error, as the dot will
not only terminate the READ, but the PERFORM as well.  The following error messages are
issued

 000035                    perform with test before until end-condition not equal zero
 000036      1                READ somefile.
 000037               *    you'll notice the period
 000038                       if file-status is equal zeros
 000039      1                   CONTINUE
 000040               *          perform your-report-stuff-here
 000041                       end-if
 000042                    end-perform

35  IGYPS2112-E   The "PERFORM" verb did not have a matching scope terminator.  A 
                  scope terminator was inserted on line 38.  The execution results
                  may not be correct.

42  IGYPS2113-E   The explicit scope terminator "END-PERFORM" was found without a 
                  matching verb.  The scope terminator was discarded.

You might want to replace the period with an END-ADD.  And, as there is no AT END/NOT AT
END, you can actually omit the END-ADD altogether



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



         Strike while the iron is hot.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gvdq3$t12$1@slb0.atl.mindspring.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <kfAT4.2360$hm2.371456@dfiatx1-snr1.gtei.net> <8fmks0$nj8$1@nnrp1.deja.com>`

```
FYI - the only thing that is more "fruitless" (and equally common) than GO TO
wars are paragraph versus section wars.  Both of these come up medium often
and come to absolutely not "conclusive" resolutions.  People always come out
of the "wars" thinking exactly what they thought before the current skirmish
began.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9eMY4.2447$HD6.39166@iad-read.news.verio.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <kfAT4.2360$hm2.371456@dfiatx1-snr1.gtei.net> <8fmks0$nj8$1@nnrp1.deja.com> <8gvdq3$t12$1@slb0.atl.mindspring.net>`

```
In article <8gvdq3$t12$1@slb0.atl.mindspring.net>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:

[snip]

>People always come out
>of the "wars" thinking exactly what they thought before the current skirmish
>began.

Oooooohhhhhhhh... is *that* what you think?

DD
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 4)_

- **From:** Art Perry <eowynfuzz@my-deja.com>
- **Date:** 2000-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h10us$llo$1@nnrp1.deja.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <kfAT4.2360$hm2.371456@dfiatx1-snr1.gtei.net> <8fmks0$nj8$1@nnrp1.deja.com> <8gvdq3$t12$1@slb0.atl.mindspring.net>`

```
In article <8gvdq3$t12$1@slb0.atl.mindspring.net>,
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> FYI - the only thing that is more "fruitless" (and equally common)
than GO TO
> wars are paragraph versus section wars.  Both of these come up medium
often
> and come to absolutely not "conclusive" resolutions.  People always
come out
> of the "wars" thinking exactly what they thought before the current
skirmish
> began.

Why dignify these threads with your responses, then?  Apparently you
have an opinion...  <G>

-Art


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Structure me this - Part 2

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fniu4$d8f$1@news.cerf.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com>`

```
"Foodman" <foodman123@aol.com> wrote in message
news:8fm7me$a26$1@nnrp1.deja.com...
> What provoked the 'Structure me this' thread
> was the comment that some nitwit gave some
…[7 more quoted lines elided]…
> structured programming.

Dear Tony,

I have consciously stayed out of this thread, just because of what you have
experienced. A complete war, and it is totally nonsense.

I use GO TO, and I am proud of it! When that is said, one should also take
into consideration that I always, yes ALWAYS program with SECTIONs. Without
SECTIONs, I can agree that GO TOs are suicide, with SECTIONs it's not.
Personally, I never seen the point with paragraphs. Hence, the GO TO them
selves are not the problem, but the environment they are used in, a
paragraph based application is bound to be restricted from GO TOs. But then,
it is the choice of paragraph design that is the failure and not the use of
GO TOs.

However, I suspect this is a matter of taste and I respect others disagree
with me.

I do procedural programming in Cobol, Delphi and C. I have recursive
functions for breakfast and enjoy a lunch with memory pointers. If I really
want to be extra ordinary, I do some OO in Delphi for dinner. And yet, yes I
do use GO TOs in ALL THREE languages if I find it beneficial.

Isn't life wonderful.

Cheesle
```

#### ↳ Re: Structure me this - Part 2

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TtJT4.654$d36.173877@news1.mco>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com>`

```
Actually, properly used, Sarcasm is highly refined wit.

here you go complete COBOL 85 /AKA COBOL II

WORKING-STORAGE SECTOIN.
01  SWITCHES.
       05  FILLER   PIC X VALUE 'N'.
             88  FILE-1-OPEN  VALUE 'Y'.
       05  FILLER   PIC X VALUE 'N'.
             88  FILE-2-OPEN  VALUE 'Y'.
       05  FILLER   PIC X VALUE 'N'.
             88  WS-ERROR VALUE 'Y'.

PROCEDURE DIVISION.
Perform until ws-file-1-open
                  OR WS-ERROR
    OPEN I-O FILE1
    IF FILE1-STATUS = 35
        OPEN OUTPUT FILE1
        CLOSE FILE-1
    ELSE
        IF FILE1-STATUS = 0
            SET FILE-1-OPEN TO TRUE
        ELSE
            SET WS-ERROR TO TRUE
        END-IF
    END-IF
   END-PERFORM
Perform until ws-file-2-open
                  OR WS-ERROR
    OPEN I-O FILE2
    IF FILE2-STATUS = 35
        OPEN OUTPUT FILE2
        CLOSE FILE-2
    ELSE
        IF FILE2-STATUS = 0
            SET FILE-2-OPEN TO TRUE
        ELSE
            SET WS-ERROR TO TRUE
        END-IF
    END-IF
   END-PERFORM


Now, here's a real-life one I did in 93:


019900 01  FLAG-FILE-STATUS                    PIC X(2)  VALUE "00".
020000     88  FLAG-FILE-STATUS-OK             VALUE "00".
5.00.00
020100     88  FLAG-FILE-WAS-THERE             VALUE "01".
5.00.00
020200     88  FLAG-FILE-EXISTS                VALUE "35".
5.00.00
020300
5.00.00
020400 01  FLAG-FILE-MODE                      PIC X VALUE "O".
5.00.00
020500     88  OPEN-OUTPUT                           VALUE "O".
5.00.00
020600     88  OPEN-INPUT                            VALUE "I".
5.00.00

074300 OPENING-PROCEDURE.
5.00.01
074900     MOVE "O" TO FLAG-FILE-MODE.
5.00.00
075000     OPEN OUTPUT FLAG-FILE.
075100     IF FLAG-FILE-WAS-THERE
5.00.00
075200        OPEN I-O FLAG-FILE,
075300        READ FLAG-FILE INTO RESTART-CHECK,
5.00.00
075400        CLOSE FLAG-FILE,
5.00.00
075500        MOVE "01" TO FLAG-FILE-STATUS,
5.00.01
075600     ELSE
5.00.00
075700        MOVE SPACES TO FLAG-RECORD,
5.00.00
075800        WRITE FLAG-RECORD,
5.00.00
075900        CLOSE FLAG-FILE.
5.00.00
076000     IF RESTART-SELECTING
5.00.00
076100        PERFORM OPEN-CUSTOMER-FILE.
076200
.......
077000     IF NOT FLAG-FILE-WAS-THERE
5.00.01
077100        PERFORM OPEN-PATIENT-WORK-FILE.
5.00.01
077200


NOW, HAVING said ALL that, let me state for the RECORD:

when coding interactive, it is nigh impossble to write efficient code
without
GO/GOTO.  It is just much easier and keeps the actual number of lines of
code down!

There are however rules to follow:
    MY own (learned from Shelley/Cashman and experience)

    1) to terminate the program ABNORMALLY, it is better to GOTO a label
            (Z000-ABEND-PGM, for examnple) than to set up some other
mechanism
    2)  to simulate the 'CASE' in COBOl befoe the EVALUATE, do this:
        PERFORM B000-EDIT-DATATHRU B599-EDIT-DATA-EXIT.
        ....

    B000-EDIT-DATA.
* set up the edits so that the SEVERE errors are checked FIRST, when any one
is
    encountered (and you don't need to list all of them), then GO TO EXIT.

            check some conditions  if error go to B599-EDIT-DATA-EXIT.
            check some more

  B100-MORE-EDITS.
            check some conditions
            check some more
   B200-MORE-EDITS.
            check some conditions
            check some more
   B599-EDIT-DATA-EXIT.
        EXIT.

    3)  It is OK to GO back to the top OF THE same paragrapgh
        e.g. in a read routine that has to check a lot of conditons.

    (Try to make a perform until if you can, but with many (>250K records,
may not
        be suitable)




Foodman <foodman123@aol.com> wrote in message
news:8fm7me$a26$1@nnrp1.deja.com...
>
>
…[186 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Structure me this - Part 2

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39211F97.52DBC2E5@zip.com.au>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <TtJT4.654$d36.173877@news1.mco>`

```
mangogwr wrote:
> 
> NOW, HAVING said ALL that, let me state for the RECORD:
…[3 more quoted lines elided]…
> of lines of code down!

There is a new construct called an exception,  this will eliminate the
need for these gotos.  I will post a simple example in my spare time I
have to read up on the cobol syntax of this first (about two weeks
time).

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: Structure me this - Part 2

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-05-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3922b326.9805228@news.epix.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com>`

```
Foodman <foodman123@aol.com> wrote:

>
>
…[5 more quoted lines elided]…
>this mess. . .

Tony:

I have followed the thread and am not quite sure whether you are
blaming me in jest or are serious about attributing the blame for the
lively GO TO discussion to myself.

If you are charging me in jest, then perhaps a little "winkey" face or
the classic <g> might have made it a bit more obvious.

I am indeed guilty as charged for introducing you to CLC and am
willing to accept my punishment from the group.  Although I have no
experience in these matters, I think that I would prefer a firing
squad.  I will also be so bold as to choose my executioners, including
Thane, Donald, Howard, Richard and Bill Klein.  I suspect that Donald
will choose a howitzer and not stop at a single round.  (Donald,
please aim *above* the belt and *below* the neck.)

;-)    <---see, a little "winkey" which says, "I'm only kidding!"

In my defense, I must testify, that I have never supplied a single
character, word, paragraph, idea, suggestion, thought, postulate,
sermon, gospel, essay, thesis or any other communication of any sort
to you on the subject of GO TOs.

I have always been and will continue to remain completely neutral on
the subject, because I am a bona fide "weasel" and suggest that
whether or not mankind uses GO TO's is one of the great philosphical
issues which regularly try men's souls.

With apologies to Jimmy's favorite author, Billy Shakespeare, I submit
to you, 

To "GO TO," or not to "GO TO" - that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous PERFORMs...blah, blah, blah!

I have spoken to the fair nymph, Ophelia (whatta babe!) and she
suggests that the thread be dropped faster than Yorick's skull!

Thank you.

;-)


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: Structure me this - Part 2

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fummt$d88$1@news.igs.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net>`

```
Bob Wolfe wrote in message

<snip>

>Thane, Donald, Howard, Richard and Bill Klein.  I suspect that Donald
>will choose a howitzer and not stop at a single round.  (Donald,
>please aim *above* the belt and *below* the neck.)

<snip>

>I have spoken to the fair nymph, Ophelia (whatta babe!) and she
>suggests that the thread be dropped faster than Yorick's skull!
>

You are mixing plays.  However, since you bring up Ophelia, I will respond.

The quality of mercy is not strained,
It droppeth as the gentle rain from CLC
Upon the Bob below.

Donald
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** "William C. Bub" <fathafluff@hotmail.com>
- **Date:** 2000-05-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3925f4df_2@nebula.superior.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <8fummt$d88$1@news.igs.net>`

```

donald tees <donald@willmack.com> wrote in message
news:8fummt$d88$1@news.igs.net...
>
> You are mixing plays.  However, since you bring up Ophelia, I will
respond.
>
> The quality of mercy is not strained,
…[4 more quoted lines elided]…
>
I believe you're quoting Portia, from The Merchant of Venice.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 4)_

- **From:** docdwarf@clark.net (NA)
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<URtV4.26994$0o4.300918@iad-read.news.verio.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <8fummt$d88$1@news.igs.net> <3925f4df_2@nebula.superior.net>`

```
In article <3925f4df_2@nebula.superior.net>,
William C. Bub <fathafluff@hotmail.com> wrote:
>
>donald tees <donald@willmack.com> wrote in message
…[11 more quoted lines elided]…
>I believe you're quoting Portia, from The Merchant of Venice.

Maybe he's driving Porsche, the automobile from Germany?

DD
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3923e8a8.1721395@news.epix.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <8fummt$d88$1@news.igs.net>`

```
"donald tees" <donald@willmack.com> wrote:

>Bob Wolfe wrote in message
>
…[12 more quoted lines elided]…
>You are mixing plays.  However, since you bring up Ophelia, I will respond.

Don:

I don't think so.....the nymph babe, Ophelia thought that Hamlet was a
major stud.  Hamlet had the hots for "Ophie" but her big 'bro told her
to steer clear of his home boy Hammie because he was "big cheese"
royalty in the homeland of our buddy Lief S. and she was not worthy of
a dude so important.

I did actually mix plays...the Howitzer wasn't introduced in Hamlet,
but in a much later, very obscure play which Will wrote called, "Bring
Them Doughboys Home, 'Afore They Git Hitched To Those Gorgeous
European Women."  It did poorly at the box office and therefore very
few have ever heard of it!  ;-)


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: Structure me this - Part 2

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3923242A.E4792C16@home.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net>`

```


Bob Wolfe wrote:
> 
> 
…[6 more quoted lines elided]…
>
How presumptuous of you sir. I don't think I've admitted to the above -
although on reflection it's close.

> I am indeed guilty as charged for introducing you to CLC and am
> willing to accept my punishment from the group.  Although I have no
> experience in these matters, I think that I would prefer a firing
> squad.  <snip>......

One cautionary note Bobby. Be careful who you talk to next time. Your
penance - write a COBOL program using ScreenIO with GO TOs and ALTERs,
sections, flags, switches, and exits are optional :-). 

Jimmy
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-05-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bib6isobh0ska6jmqrtgfqgs5602aougm4@4ax.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <3923242A.E4792C16@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote:

>One cautionary note Bobby. Be careful who you talk to next time. Your
>penance - write a COBOL program using ScreenIO with GO TOs and ALTERs,
>sections, flags, switches, and exits are optional :-). 

i dont think i'll be able to sleep now.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3923EBA7.B422B24A@cusys.edu>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <3923242A.E4792C16@home.com>`

```
> Bob Wolfe wrote:
>
…[6 more quoted lines elided]…
> The slings and arrows of outrageous PERFORMs...blah, blah, blah!


Now I have seen code and documentation written by a lawyer wannabe
(neither the code nor the documentation could be figured out without
tremendous work).  I really haven't seen "literary" code though.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39256be6.53125135@news.cox-internet.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <3923242A.E4792C16@home.com> <3923EBA7.B422B24A@cusys.edu>`

```
On Thu, 18 May 2000 07:09:59 -0600, Howard Brazee
<howard.brazee@cusys.edu> wrote:

>
>Now I have seen code and documentation written by a lawyer wannabe
>(neither the code nor the documentation could be figured out without
>tremendous work).  I really haven't seen "literary" code though.

My first real world use of "Evaluate" was downright poetic.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39267F20.3D8F7B71@zip.com.au>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <3923242A.E4792C16@home.com> <3923EBA7.B422B24A@cusys.edu>`

```
Howard Brazee wrote:
> 
> Now I have seen code and documentation written by a lawyer wannabe
> (neither the code nor the documentation could be figured out without
> tremendous work).  I really haven't seen "literary" code though.

That was literate programming by the guy who who Tex, can't remember
the name though :-}

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Literate Programming (was: Re: Structure me this - Part 2)

_(reply depth: 5)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g5kl9$21el$1@news.hitter.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <3923242A.E4792C16@home.com> <3923EBA7.B422B24A@cusys.edu> <39267F20.3D8F7B71@zip.com.au>`

```

Ken Foskey wrote in message <39267F20.3D8F7B71@zip.com.au>...
>Howard Brazee wrote:
>>
…[5 more quoted lines elided]…
>the name though :-}

From the < news:comp.programming.literate > FAQ

"6.  What is Literate Programming?
  Literate programming is the combination of documentation and source
  together in a fashion suited for reading by human beings.  In fact,
  literate programs should be enjoyable reading, even inviting!  (Sorry
  Bob, I couldn't resist!)  In general, literate programs combine source
  and documentation in a single file.  Literate programming tools then
  parse the file to produce either readable documentation or compilable
  source.  The WEB style of literate programming was created by D.E.
  Knuth during the development of his TeX typsetting software."

D.E. Knuth (aka, Donald E. Knuth) wrote "The Art of Computer
Programming," Addison-Wesley.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<693208A1102E8B6E.5D0941FA089A754F.0EF7540202FA2649@lp.airnews.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <3923242A.E4792C16@home.com>`

```
On Wed, 17 May 2000 22:59:47 GMT, "James J. Gavan" <jjgavan@home.com>
enlightened us:

>
>
…[22 more quoted lines elided]…
>Jimmy

That wouldn't be punishment as all Bob would have to do is make a copy
of Windows98 :)

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Why do we play in recitals and recite in plays?


Boycott Mitsubishi Industries

Remove nospam to email me.

 Steve
```

##### ↳ ↳ Re: Structure me this - Part 2

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392345A0.A2CFC66D@worldnet.att.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net>`

```
Bob Wolfe wrote:
> 
(snip)
> 
> I am indeed guilty as charged for introducing you to CLC and am
> willing to accept my punishment from the group.

He admits the dastardly deed!

> Although I have no experience in these matters, I think that I would prefer a firing
> squad.  I will also be so bold as to choose my executioners, including
> Thane, Donald, Howard, Richard and Bill Klein.

I expected you to ask them to form a circle <bfg>

Bill Lynch
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3923ef5b.3436320@news.epix.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <392345A0.A2CFC66D@worldnet.att.net>`

```
William Lynch <wblynch@worldnet.att.net> wrote:

>Bob Wolfe wrote:
>> 
…[11 more quoted lines elided]…
>I expected you to ask them to form a circle <bfg>

What?  And drop to the ground when the command is given to fire?
Great idea!  


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 4)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3923F744.C626E01F@cusys.edu>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <392345A0.A2CFC66D@worldnet.att.net> <3923ef5b.3436320@news.epix.net>`

```

Bob Wolfe wrote:
> 
> What?  And drop to the ground when the command is given to fire?
> Great idea!

It depends whether they are firing at Will or some other playwright.
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 4)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392413D2.12F66A64@worldnet.att.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <392345A0.A2CFC66D@worldnet.att.net> <3923ef5b.3436320@news.epix.net>`

```
Bob Wolfe wrote:
> 
> William Lynch <wblynch@worldnet.att.net> wrote:
…[17 more quoted lines elided]…
> Great idea!

It's the punch line to the old joke about how the Italian firing squad
lines up, visualize what happens to the firing squad. 
'Guess it wasn't literary enough for you:-) I'll have to see if Oscar
Wilde had any quips concerning siring squads.

Bill Lynch <VBG>
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 5)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-05-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39257a40.19933950@news.epix.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <392345A0.A2CFC66D@worldnet.att.net> <3923ef5b.3436320@news.epix.net> <392413D2.12F66A64@worldnet.att.net>`

```
William Lynch <wblynch@worldnet.att.net> wrote:

>> What?  And drop to the ground when the command is given to fire?
>> Great idea!
…[6 more quoted lines elided]…
>Bill Lynch <VBG>

Bill:

I did understand the logic of the circle.....and when I drop to the
ground, nothing happens to me, but the firing squad turns to swiss
cheese.

I doubt that Oscar Wilde has any quips on siring squads.....but I'll
bet that Larry Flynt does.

I must politely decline the quips from Oscar Wilde regarding siring
squads.  Although I may be willing to face a firing squad, I will
certainly refuse to face a siring squad.  

I've heard rumors that the guys on a siring squad show absolutely no
mercy at all!

;-)



Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 6)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39260719.57C01227@worldnet.att.net>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <392345A0.A2CFC66D@worldnet.att.net> <3923ef5b.3436320@news.epix.net> <392413D2.12F66A64@worldnet.att.net> <39257a40.19933950@news.epix.net>`

```
Bob Wolfe wrote:
> 
> William Lynch <wblynch@worldnet.att.net> wrote:
…[17 more quoted lines elided]…
> I doubt that Oscar Wilde has any quips on siring squads.

Okay, okay, you could have tossed in a "(sic)".

Bill Lynch :-)
```

###### ↳ ↳ ↳ Re: Structure me this - Part 2

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392626C5.133D614B@home.com>`
- **References:** `<8fm7me$a26$1@nnrp1.deja.com> <3922b326.9805228@news.epix.net> <392345A0.A2CFC66D@worldnet.att.net> <3923ef5b.3436320@news.epix.net> <392413D2.12F66A64@worldnet.att.net> <39257a40.19933950@news.epix.net> <39260719.57C01227@worldnet.att.net>`

```


William Lynch wrote:
> 
> Bob Wolfe wrote:
…[22 more quoted lines elided]…
> 
Now seeing it was Roberto who threw in the Edwardian, Oscar Wilde (what
a jump from Shakespeare !) - the good Oscar did sire two kids although
he knew about AC/DC before they became a pop group :-)

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
