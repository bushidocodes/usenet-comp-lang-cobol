[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# More Structure.. Perform from Read

_235 messages · 38 participants · 2001-06 → 2001-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### More Structure.. Perform from Read

- **From:** "Lynn Randall" <LERandall@yahoo.com>
- **Date:** 2001-06-04T18:07:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1c3343_2@news1.prserv.net>`

```
I have been lurking for a bit... but now I need some input...
At the risk of starting another religious discussion, I would like to
solicit some opinions (the civil ones).

In my job, I have the task of reviewing programs of my co-workers before the
programs are allowed to go to production.  My expectations are for
efficiency, understandability, adherence to standards, and maintainability
(the "understandable" and "maintainable" requirements are admittedly
related).

Part of the "maintainabiliy", is creating "structured" programs.  There has
already been a certain amount of philosophical discussion about "structure"
in recent days in this newsgroup; and I don't really want to rehash all
that.  I just would like some feedback on a couple of my "guidelines" -- I
need to determine if I'm still looking for "structure", or if I've crossed
the line to imposing my "style" upon my co-workers.

Here is the current issue...

When coding a read paragraph, is it appropriate to perform another paragraph
from within the Read? (Same question goes for Fetch paragraphs when dealing
with an SQL cursor).

For example:

0000-Mainline.
    Perform 1000-Initialization
    Perform 2000-Read
                    until file-eof
    Perform 9000-Finalization

1000-Initialization.
   ... some init stuff..

2000-Read
    Read Input-File into WS-Input-File
        at end
              set file-eof to true
        not at end
              Perform 3000-Process-records
        end-read

3000-Process-records
  ... main processing logic here...

9000-Finalization
  ...  control totals, etc. here....

The way Paragraph 2000- is coded, in my mind, violates the structured
programming principle of cohesion.  That is, each paragraph should perform
one and only one function.  Here, 2000- performs the Read AND it drives the
rest of the processing.  That seems wrong to me, but one of co-workers
showed me a textbook where this "structure" was advocated.   I've seen the
"structure" recently (let's say the last 3 years) from various programmers,
whereas previously (the prior 12 years or so), NO ONE I knew coded that way.
Have standards changed?  In addition, I was originally taught that all file
I-O should be isolated in its own paragraph to ease dump-solving.  How that
might help is not very clear from this example; so consider if the "not at
end" condition led to an Evaluate statement, or a series of If/Else
statements.

Just for grins... here is how I would have coded it traditionally...

0000-Mainline.
    Perform 1000-Initialization
    If file-eof
           next sentence
    else
           Perform 2000-Process-Records
                until file-eof
    end-if
    Perform 9000-Finalization

1000-Initialization.
   ... some stuff..
    Perform 2000-Read

2000-Read
    Read Input-File into WS-Input-File
        at end
              set file-eof to true
       end-read

3000-Process-records
  ... main processing logic here...
    Perform 2000-Read

9000-Finalization
  ...  control totals, etc. here....

As you can see, one of my other "expectations" is that all paragraphs are
numbered.  Judging by the posts to this newsgroup, that also seems to be out
of vogue.    Years ago, I would not have coded a priming read in the
1000-Init paragraph; but I was persuaded otherwise...

I might add that, where COBOL is concerned, I am purely a mainframe
programmer (though I have some training in VB, and web stuff).  So stuff
specific to Fujitsu or MicroFocus Cobol are of less interest to me.

Thanks..
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-05T03:36:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1C5418.5F2E208F@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```


Lynn Randall wrote:

> Here is the current issue...

> When coding a read paragraph, is it appropriate to perform another paragraph
> from within the Read? (Same question goes for Fetch paragraphs when dealing
> with an SQL cursor).
>

First off, you really didn't want to *know* about Micro Focus. Well...... vive
le difference! Now I wish I could just get the J4 guys to recognize that too,
(i.e. mainframe and PC 'special' requirements') !

> Just for grins... here is how I would have coded it traditionally...
>
…[26 more quoted lines elided]…
>

Using OO I don't see that I do anything dramatically different from your code
above. Ignore all the OO BS, but just like a factory making cookies, there's a
production line, and for Business Classes it is procedural just like you have.
(It is only random Windows events which make an OO/Structured program do a hop,
skip and a jump).

The only major difference, and this is being used by others not into OO, is that
your paragraph 2000-Read, to me becomes :-

        invoke MyFileClass "read-primekey"
            using thisKey returning fileStatusResult and data

OR   invoke MyFileClass "read-next"
              returning fileStatusResult and data

All reference to accessing a file is in one Class - prove that right and can be
reused over and over again. Whether the retrieved record is relevant is
determined in the Business Class - which is in response to your, "When coding a
read paragraph, is it appropriate to perform another paragraph from within the
Read? ".

Although at the experimental stage with SQL, essentially I'm doing the same
thing - a separate class per Table. From my initial scribblings, looks like the
same approach will work out nicely. As regards your FETCH using cursor, I cheat.
I stay within the Class Table method doing the Fetching, building up a
collection, (equivalent of a Table occurs x times, without having to specify 'x
times'), of  rows or columns required until I hit 'No more rows' - the
collection gets returned to the Business class. A subtle difference between
COBOL file handling and SQL FETCH. Selectively choosing rows/columns is
determined from the parameters passed to the fetch-method.

Purely preference - but I wouldn't do that Initial Read up front in your
Initialization processes - but largely depends on what the program is doing.

>
> As you can see, one of my other "expectations" is that all paragraphs are
…[7 more quoted lines elided]…
>

I'm beyond paragraph numbering, now using method-names which one can remember,
but would suggest it is primarily a question of style. When I first started I
used to segment :-

    A010-DO-THIS,  A020-DO-SOMETHING-ELSE
    P010-PRINT-REPORT, P020-GET-REPORT-LINE etc....

but my thinking tied back to memory limitations and the 'alpha' numbering
mentally gave me my resident segments and overlays.

Two cents worth from one of the little guys on PCs <G>

Jimmy, Calgary AB
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-06-05T09:10:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.gegklh0.pminews@news.wanadoo.es>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```
On Mon, 4 Jun 2001 18:07:28 -0700, Lynn Randall wrote:
>
>For example:
…[73 more quoted lines elided]…
>
Lynn,

Although I prefer your solution, I don't think the other one is too bad. I
don't think that any programmer who has to modify one of those programs will
have trouble understanding it.
Also, don't forget that the READ ... AT END ... NOT AT END construction
didn't exist when you started programming.

My reason to prefer your solution is another one to start a religious war, I
hate switches.
Of course, you can argue about what is a switch and what is not, but for end
of file conditions, I always use the file's status field.
You can call this a switch, but the important thing to me is that I never
touch it, so I can't forget setting or resetting it.

I would prefer it this way

0000-Mainline.
    Perform 1000-Initialization
    Perform 2000-Read.
    Perform 2000-Process-Records
                until file-status = '10'
    Perform 9000-Finalization

1000-Initialization.
   ... some stuff..

2000-Read
    Read Input-File into WS-Input-File
  
3000-Process-records
  ... main processing logic here...
    Perform 2000-Read

9000-Finalization
  ...  control totals, etc. here....

Of course, an 88 level on the file status is perfectly acceptable.

Just my $0.02





Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2001-06-05T09:38:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010605053853.24160.00000837@ng-ca1.aol.com>`
- **References:** `<jvyyrzubevmbagrfvasbezngvpnpbz.gegklh0.pminews@news.wanadoo.es>`

```
>From: "Willem Clements" willem@horizontes-informatica.com 
>Date: 2001-06-05 03:10 Eastern Daylight Time
>On Mon, 4 Jun 2001 18:07:28 -0700, Lynn Randall wrote:

>>2000-Read
>>    Read Input-File into WS-Input-File
…[5 more quoted lines elided]…
>>

I don't like this.  It is a very popular approach, though, and I
have seen it at several places.  To me, it represents a good
example of structured code without structured logic.  
Logically, "Process-records" is not a natural subfunction
of "Read."  The only thing I would like to see after "not at end"
is "add 1 to input-counter" or things of that ilk.  
Reading input, on the other hand, is a natural subfunction
of procesing records.


>0000-Mainline.
>    Perform 1000-Initialization
…[13 more quoted lines elided]…
>    Perform 2000-Read

I like this. 

However, Lynn Randall asked whether one or the other should
be enforced.  By the manager?  Absolutely not.  One thing
you can do is call a shop coding standards meeting and call 
for a vote.  The important thing about a structuring standard
is not that it be structured but that it be standard.  

Ross
http://www.geocities.com/ross_klatte/
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "Lynn Randall" <LERandall@yahoo.com>
- **Date:** 2001-06-05T11:12:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1d2394_2@news1.prserv.net>`
- **References:** `<jvyyrzubevmbagrfvasbezngvpnpbz.gegklh0.pminews@news.wanadoo.es> <20010605053853.24160.00000837@ng-ca1.aol.com>`

```

Ross Klatte <klatteross@aol.commmm> wrote in message
news:20010605053853.24160.00000837@ng-ca1.aol.com...
>snippage>

> I like this.
>
…[9 more quoted lines elided]…
>
I'm not a manager (thank heavens!)... my title is "technical specialist"
(ie: a programmer with enough experience and pushiness to get to the top of
the heap of programmers in my team).  And I do plan on bringing this up for
discussion.. I just wanted to see if anyone "out there" could give me some
good, coherent arguments for each side.  Just trying to be prepared.

thanks much for your feedback.  :-)
Lynn
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** Timothy_S_Coffey@bankone.com (Tim Coffey)
- **Date:** 2001-06-05T05:53:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e32280da.0106050453.4fbe3bb4@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```
"Lynn Randall" <LERandall@yahoo.com> wrote in message news:<3b1c3343_2@news1.prserv.net>...

I`m a big fan of putting all I/O in "black boxes" (ie, separate
paragraphs).
For files with variant record types, each 'write' of a type would also
get it's
own paragraph. For VSAM files using direct/browsed retrieval, each
kind of
'start/read' (full or partial key) would get it's own paragraph also. 

So to answer your question, it seems that '2000-READ' should only
READ, and not
process records. In this sense it is mislabeled. It shouid be
'2000-PROCESS', which calls 'XXXX-READ'.

> 2000-Read
>     Read Input-File into WS-Input-File
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-05T07:58:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1CE58C.882D0959@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <e32280da.0106050453.4fbe3bb4@posting.google.com>`

```
Tim Coffey wrote:

> "Lynn Randall" <LERandall@yahoo.com> wrote in message news:<3b1c3343_2@news1.prserv.net>...
>
…[6 more quoted lines elided]…
> 'start/read' (full or partial key) would get it's own paragraph also.

I have never been a fan of this, unless the I/O paragraph is large.  I would rather see the
line of code when I get to it in the logic than assume it to be correct.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2001-06-05T11:45:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DA048FC8927CDDE5.500B8062DF7D96A3.3F03EEEBDD0F7432@lp.airnews.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <e32280da.0106050453.4fbe3bb4@posting.google.com> <3B1CE58C.882D0959@brazee.net>`

```
On Tue, 05 Jun 2001 07:58:36 -0600, Howard Brazee <howard@brazee.net>
enlightened us:

>Tim Coffey wrote:
>
…[11 more quoted lines elided]…
>line of code when I get to it in the logic than assume it to be correct.

While I've used the style of having paragraphs that are performed for
all I/O and each file in its own paragraph, I am reminded of what the
prime directive of using a perform is.  That is to group code that is
used more than once in a program in one place to avoid duplication of
code.

In your example, you only need to read the file in one place (process
paragraph).  What purpose does putting the read into a paragraph by
itself then performing it, if that read is only needed for location?
Is it more readable?  Not necessarily.  Is it more efficient.
Absolutely not (you're generating a store, and a branch and link to
another location in your program which must also do a store and a
branch and link to a location outside of your program then a restore
then another branch).

So you're writing in this style because it "looks" structured?  Not a
good reason.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Last night I played a blank tape full blast. 
The mime next door went nuts.


DON'T DRILL in the Artic National Wildlife Refuge
Read the real facts at:

http://www.worldwildlife.org/arctic-refuge/

also

http://www.savepolarbears.org/


Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-06-05T19:29:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010605152941.04512.00000023@nso-fl.aol.com>`
- **References:** `<DA048FC8927CDDE5.500B8062DF7D96A3.3F03EEEBDD0F7432@lp.airnews.net>`

```
In article <DA048FC8927CDDE5.500B8062DF7D96A3.3F03EEEBDD0F7432@lp.airnews.net>,
SkippyPB <swiegand@neo.rr.com.nospam> writes:

>
>In your example, you only need to read the file in one place (process
…[3 more quoted lines elided]…
>

Placing the access logic in a separate performed area, allows for changing 
the access method/file structure without a major impact on the detail
processing.
I 'prefer' the style where the access logic for each file is separated into 
individual paragraphs that can be performed from any area that needs 
to 'touch' the file in some way.  It sets up the code to permit reasonably 
easy transition from standard COBOL file access verbs to CALL USING 
syntax of external file handlers  or whatever other destination may be 
dreamed up in the future.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** "Lynn Randall" <LERandall@yahoo.com>
- **Date:** 2001-06-05T13:01:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1d3d27_2@news1.prserv.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <e32280da.0106050453.4fbe3bb4@posting.google.com> <3B1CE58C.882D0959@brazee.net> <DA048FC8927CDDE5.500B8062DF7D96A3.3F03EEEBDD0F7432@lp.airnews.net>`

```
First, let me say I appreciate your response...  It's good to hear from the
"other side". <g>
See below for more....

SkippyPB <swiegand@neo.rr.com.nospam> wrote in message
news:DA048FC8927CDDE5.500B8062DF7D96A3.3F03EEEBDD0F7432@lp.airnews.net...
> On Tue, 05 Jun 2001 07:58:36 -0600, Howard Brazee <howard@brazee.net>
> enlightened us:
…[3 more quoted lines elided]…
> >> "Lynn Randall" <LERandall@yahoo.com> wrote in message
news:<3b1c3343_2@news1.prserv.net>...
> >>
> >> I`m a big fan of putting all I/O in "black boxes" (ie, separate
…[7 more quoted lines elided]…
> >I have never been a fan of this, unless the I/O paragraph is large.  I
would rather see the
> >line of code when I get to it in the logic than assume it to be correct.
>
…[5 more quoted lines elided]…
>

I'm not sure I agre with your assessment of "prime directive".  Yes, "To
group code" -- that is the essence of cohesion... but "that is used more
than once..to avoid duplication"...  I think not necessarily.   It seems to
me that grouping code for the purpose of structure, thus making it easier to
understand and maintain, has merits on its own.

> In your example, you only need to read the file in one place (process
> paragraph).  What purpose does putting the read into a paragraph by
…[6 more quoted lines elided]…
>

Ahh.. processing efficiency... there, you've scored some points.  That is
certainly a consideration, and I appreciate your perspective.  However,
taken to an extreme, one could argue that fall-thru (and goto) logic is more
efficient than structured programming in general.  Somewhere along the way,
you have to weigh the benefits of structure against what you give up in
efficiency.  I'm guessing my threshhold for that trade-off is just a bit
different from yours.   However, my original question was whether this was a
matter of "style" or "structure"; and by offering a cogent argument from the
"opposition", you've caused me to take a few more steps to the "style"
option.  Thanks a bunch.  <g>

> So you're writing in this style because it "looks" structured?  Not a
> good reason.
>

Actually, I disagree (re: earlier comments).  I think good structure (and
resulting ease of maintenance) is a good reason to write code a certain way.

thanks....  Lynn
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "David P. Bretz" <DBretz@mescoma.com>
- **Date:** 2001-06-05T15:25:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1D3235.119D2DFE@mescoma.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <e32280da.0106050453.4fbe3bb4@posting.google.com>`

```
I go back and forth on this point.   If the program has just one read and/or write to a file, I
see no harm in putting the command in with the program logic.  If there are a bunch of files to
be read or written, or if one file is read from more than one place in the program, then it
makes more sense to put it in a separate paragraph.

I think the important thing to remember when coding is that there is no hard and fast "rule"
for any situation.  Sometimes, even something that may seem "illogical" may make perfect sense
in the context of a particular problem resolution.  I've done things in programs I swore I'd
never do because to work around them was much more confusing and in the long run would have
made the program harder to maintain.

The only "rules" I go by when examining my programmer's code are:

1.  Does it do what it's supposed to do?

2.  Does it make sense?

3.  Could I come back in a year and modify it easily?

Other than that, unless there is some glaringly inefficient or confusing code, I let them code
the way they want.  About the only hard and fast rules I have are that every paragraph has to
be numbered and they paragraphs have to appear in numerical order in the program.

Dave


P.S.   OH yes.............and meaningful data and paragraphs names.


Tim Coffey wrote:

> "Lynn Randall" <LERandall@yahoo.com> wrote in message news:<3b1c3343_2@news1.prserv.net>...
>
…[20 more quoted lines elided]…
> >
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** "Joseph J Katnic" <josephk@josephk.iinet.net.au>
- **Date:** 2001-06-05T22:22:44+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1ceb6b$0$7381@echo-01.iinet.net.au>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```
In article <3b1c3343_2@news1.prserv.net>, "Lynn Randall"
<LERandall@yahoo.com> wrote:

<snip>
> 0000-Mainline.
>     Perform 1000-Initialization If file-eof
…[22 more quoted lines elided]…
> 
The above is harder to immediately understand as you have
to notice that the Intialization does a read before you
can understand why a test for EOF is done after Initializtion.
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-06-05T17:48:34+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<burphtc9gffkd8vnn74c5gqgeuncie4dtt@4ax.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au>`

```
On Tue, 05 Jun 2001 22:22:44 +0800 "Joseph J Katnic"
<josephk@josephk.iinet.net.au> wrote:

:>In article <3b1c3343_2@news1.prserv.net>, "Lynn Randall"
:><LERandall@yahoo.com> wrote:

:><snip>
:>> 0000-Mainline.
:>>     Perform 1000-Initialization If file-eof
:>>            next sentence
:>>     else
:>>            Perform 2000-Process-Records
:>>                 until file-eof
:>>     end-if Perform 9000-Finalization
 
:>> 1000-Initialization.
:>>    ... some stuff..
:>>     Perform 2000-Read
 
:>> 2000-Read
:>>     Read Input-File into WS-Input-File
:>>         at end
:>>               set file-eof to true
:>>        end-read
 
:>> 3000-Process-records
:>>   ... main processing logic here...
:>>     Perform 2000-Read
 
:>> 9000-Finalization
:>>   ...  control totals, etc. here....
 
:>The above is harder to immediately understand as you have
:>to notice that the Intialization does a read before you
:>can understand why a test for EOF is done after Initializtion.

And it is unnecessary (though I guess NEXT SENTENCE might skip
9000-Finalization - I don't use it) since the PERFORM of 2000-Process has it
as the UNTIL clause.  
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "Lynn Randall" <LERandall@yahoo.com>
- **Date:** 2001-06-05T11:26:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1d26e9_3@news1.prserv.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <burphtc9gffkd8vnn74c5gqgeuncie4dtt@4ax.com>`

```
Good point!  My mistake!
Lynn

Binyamin Dissen <postingid@dissensoftware.com> wrote in message
news:burphtc9gffkd8vnn74c5gqgeuncie4dtt@4ax.com...
> On Tue, 05 Jun 2001 22:22:44 +0800 "Joseph J Katnic"
> <josephk@josephk.iinet.net.au> wrote:
…[35 more quoted lines elided]…
> 9000-Finalization - I don't use it) since the PERFORM of 2000-Process has
it
> as the UNTIL clause.
>
…[5 more quoted lines elided]…
> Director, Dissen Software, Bar & Grill - Israel
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-06T07:08:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1dd527.1567018@news1.attglobal.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <burphtc9gffkd8vnn74c5gqgeuncie4dtt@4ax.com> <3b1d26e9_3@news1.prserv.net>`

```
On Tue, 5 Jun 2001 11:26:56 -0700, "Lynn Randall"
<LERandall@yahoo.com> wrote:
In your original message you mentioned that you considered a perform
of a loop that then controlled another process to be potentially
unstructured - because a perform should handle only a single task.

I see nothing wrong with a loop like this:

Perform until all-done
   Read input-file
      at end 
          set all-done to true
      not at end
          perform process-the-record
End-Perform

when the "read loop" is the mainline function.  

At any rate, a lot of this is a matter of preference, perception and
experience.  The paragraph that triggers off other paragraphs that
might trigger off other paragraphs can still be considered "Single
funciton" paragraphs.  You could have:

Perform Process-The-File


Then in Process-the-file

Perform Open-File
Perform Read-And-Do until End-of-File
Perform Close-Fille
 

Process-the-file performs only "process the file" function.  Even
though it might have subroutines - that doesn't make it unstructured.

I'm not being critical, just sharing my observation.  Additionally, I
don't use numbered paragraphs and don't see any reason to do so in
todays environemt where text searches are easy.  If the argument is
that you want to be able to visualize the entire structure I would
argue that once you break it down into the individual routines, your
focus need only be on the individual section of code you are working
on and who cares what the number of the paragraph is.

This is simply preference, however.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-10T22:49:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B23F972.91116313@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <burphtc9gffkd8vnn74c5gqgeuncie4dtt@4ax.com> <3b1d26e9_3@news1.prserv.net> <3b1dd527.1567018@news1.attglobal.net>`

```
Thane Hubbell wrote:
> 
> On Tue, 5 Jun 2001 11:26:56 -0700, "Lynn Randall"
…[15 more quoted lines elided]…
> when the "read loop" is the mainline function.

Thane, I'm with you. I really don't see any need for the older ways of
coding read loops since the '85 standard was implemented because the
READ is now a balanced construct, before all we had was the "at end"
clause which is what lead to the other solutions, e.g., priming reads,
etc.

As always, YMMV,
LiamD
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "Lynn Randall" <LERandall@yahoo.com>
- **Date:** 2001-06-05T11:24:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1d266c_3@news1.prserv.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au>`

```

Joseph J Katnic <josephk@josephk.iinet.net.au> wrote in message
news:3b1ceb6b$0$7381@echo-01.iinet.net.au...
> In article <3b1c3343_2@news1.prserv.net>, "Lynn Randall"
> <LERandall@yahoo.com> wrote:
…[30 more quoted lines elided]…
> can understand why a test for EOF is done after Initializtion.

Yes.. that was my initial objection to using a priming read in the Init
paragraph.  But the alternative is to start the Processing paragraph with a
Read and immediately follow it with an If statement, such as:

2000-Process
    Perform 2010-Read
    If file-eof
          next sentence
    esle
         .... the entire main processing in the middle of the if ....
    end-if.

I don't like having the entire logic of any paragraph buried in an IF
statement (this, I suspect, is merely personal preference); therefore, I
went to the priming read in the Init (I made that change years ago).

The other alternative... (this will start another religious debate)...  is
to perform-thru-exit.  Then you could have

"If file-eof,
    goto 2000-exit".

 And actually, I prefer perform-thru's for that reason.   That means goto is
*only* used to goto the paragraph exit...   I expect this to go away when we
get an "exit paragraph" verb added to Cobol.  In this way, you could also
avoid the priming read.

Lynn
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2001-06-05T20:48:10+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.gehgwa0.pminews@news.wanadoo.es>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <3b1d266c_3@news1.prserv.net>`

```
On Tue, 5 Jun 2001 11:24:53 -0700, Lynn Randall wrote:


>
>2000-Process
…[22 more quoted lines elided]…
>Lynn

Lynn,

Your PERFORM ..... UNTIL contains an implicit IF. You don't have to code it

Just code

PERFORM 2010-READ.
PERFORM 3000-PROCESS
         UNTIL END-OF-FILE.



Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "Russell Styles" <rwstyles@worldnet.att.net>
- **Date:** 2001-06-06T04:42:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bxiT6.5524$Ji.463524@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <3b1d266c_3@news1.prserv.net>`

```

"Lynn Randall" <LERandall@yahoo.com> wrote in message
news:3b1d266c_3@news1.prserv.net...
>
<< snip >>
> Yes.. that was my initial objection to using a priming read in
the Init
> paragraph.  But the alternative is to start the Processing
paragraph with a
> Read and immediately follow it with an If statement, such as:
>
…[5 more quoted lines elided]…
>          .... the entire main processing in the middle of the
if ....
>     end-if.
>
> I don't like having the entire logic of any paragraph buried in
an IF
> statement (this, I suspect, is merely personal preference);
therefore, I
> went to the priming read in the Init (I made that change years
ago).
>
> The other alternative... (this will start another religious
debate)...  is
> to perform-thru-exit.  Then you could have
>
…[3 more quoted lines elided]…
>  And actually, I prefer perform-thru's for that reason.   That
means goto is
> *only* used to goto the paragraph exit...   I expect this to go
away when we
> get an "exit paragraph" verb added to Cobol.  In this way, you
could also
> avoid the priming read.
>
> Lynn
>
     I like the exit paragraph too, but it is important to
remember that it
will not get you out of a perform thru (unless you happen to be
in the
last paragraph anyway).  Since I always have the last paragraph
contain
only an "EXIT" statement, that is not helpfull.

   I suppose that the exit section verb might work, if you
can retrain your head around sections instead of paragraphs.

   I have had best results by eliminating the perform thru.  But
I don't really want to.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-06T07:16:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1E2D27.CA80663E@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <3b1d266c_3@news1.prserv.net> <bxiT6.5524$Ji.463524@bgtnsc04-news.ops.worldnet.att.net>`

```

Russell Styles wrote:

>      I like the exit paragraph too, but it is important to
> remember that it
…[10 more quoted lines elided]…
> I don't really want to.

I don't really see any advantage in having an EXIT SECTION over a GO TO
THIS-SECTION-EXIT.   If you have multiple paragraphs in a perform (why
else have a section), then you have drop through code.    The EXIT
PARAGRAPH seems designed to facilitate getting rid of drop through
code.  If someone moves to using the EXIT verb, why keep using sections?
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "Russell Styles" <rwstyles@worldnet.att.net>
- **Date:** 2001-06-07T04:29:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7rDT6.67928$4f7.5147518@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <3b1d266c_3@news1.prserv.net> <bxiT6.5524$Ji.463524@bgtnsc04-news.ops.worldnet.att.net> <3B1E2D27.CA80663E@brazee.net>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:3B1E2D27.CA80663E@brazee.net...
>
> Russell Styles wrote:
…[3 more quoted lines elided]…
> > will not get you out of a perform thru (unless you happen to
be
> > in the
> > last paragraph anyway).  Since I always have the last
paragraph
> > contain
> > only an "EXIT" statement, that is not helpfull.
…[4 more quoted lines elided]…
> >    I have had best results by eliminating the perform thru.
But
> > I don't really want to.
>
> I don't really see any advantage in having an EXIT SECTION over
a GO TO
> THIS-SECTION-EXIT.   If you have multiple paragraphs in a
perform (why
> else have a section), then you have drop through code.    The
EXIT
> PARAGRAPH seems designed to facilitate getting rid of drop
through
> code.  If someone moves to using the EXIT verb, why keep using
sections?
>
    I agree.  I tend to use  "GO TO DOIT-X." type code myself.
When
I do this, I can get everything, the open, the close, and the
loop in one
locical area, with a perform thru.  I am carefull to insure that
all paragraphs
in this perform range start the same (Ie DOIT, DOIT-LOOP,
DOIT-END, DOIT-X).

    I also insure that nobody uses any of these paragraphs in any
other manner.

    No, it is not idiot proof.  Yes, there are many other ways to
do it, and
some may well be better in some ways.  My complaint was that if
you are in a
perform thru, the EXIT PARAGRAPH only exits the current
paragraph, not
the entire range, and EXIT PERFORM is not legal.

    Frankly, I don't trust myself enough to risk using a perform
section.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-07T06:04:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1f185e.33904201@news1.attglobal.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <3b1d266c_3@news1.prserv.net> <bxiT6.5524$Ji.463524@bgtnsc04-news.ops.worldnet.att.net> <3B1E2D27.CA80663E@brazee.net>`

```
I ran into something recently.  I learn new things everyday.  Here's
the deal.....

First-Section Section.
...
...
Sect-Exit.  Exit.

Second-Section Section.
...
...
Sect-Exit.  Exit.

Third-Section Section.
...
...
Sect-Exit.  Exit.


When one performs any of these sections one may, anywhere in any
section, code : Go To Sect-Exit.  

This will cause you to exit the present section WITHOUT "fall through"
code - and has existed for a long time.  This is the functionality
more formally supported in the next standard by "Exit Section" - with
the addition fo Exit Paragraph, etc.

I agree with Howard - this type of Section construct will no longer be
necessary, but I wanted to show how it could be done today (And 20+
years ago) using standard COBOL.






On Wed, 06 Jun 2001 07:16:23 -0600, Howard Brazee <howard@brazee.net>
wrote:

>
>Russell Styles wrote:
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-10T22:52:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B23FA1D.26D83AC3@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au> <3b1d266c_3@news1.prserv.net>`

```
Lynn Randall wrote:
> 
(snip)
> > >
> > The above is harder to immediately understand as you have
…[13 more quoted lines elided]…
>     end-if.

See Thane's post from 06 Jun 2001, at 7:08 GMT. It's no longer necessary
to code READ loops this way and, IMHO, it's a bad idea to continue to do
so.

LiamD
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-06T07:06:10+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1DC852.32614DE4@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b1ceb6b$0$7381@echo-01.iinet.net.au>`

```
> >     If file-eof
> >            next sentence
…[4 more quoted lines elided]…
> > 

> > You have coded a NEXT SENTENCE in an IF ... END-IF.  This is invalid
> > Cobol code and a bug looking for a place to happen.
> 
> While it probably is a bug, it is valid CoBOL code.   

In the rules for IF in ANS85:

  "If the END-IF phrase is specified, the NEXT SENTENCE phrase must not
be specified."

It is a compiler extension that allows these to be together in the same
IF statement.  

There have been some who contrive a 'valid' structure where IFs are
nested and the innermost has a NEXT SENTENCE and the outer has END-IF in
order to defeat the rule and mix these just so they can 'punish' any
later programmer who may change the full-stops or naively add a
statement between the IF and the target full-stop in the expectation
they are outside the control of the IF.

This case, however is not even nested and thus is not valid standard
Cobol.
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-05T15:56:46+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1CF32E.8C818B5D@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```
Lynn Randall wrote:
> 
> Just for grins... here is how I would have coded it traditionally...
…[9 more quoted lines elided]…
>     Perform 9000-Finalization

!!!! SERIOUS BUG ALERT !!!

You have coded a NEXT SENTENCE in an IF ... END-IF.  This is invalid
Cobol code and a bug looking for a place to happen.  The effect of the
NEXT SENTENCE is that it is a GO TO next-full-stop.  This means that
9000-Finalisation may or may not be done depending on whether someone
puts a full-stop on the END-IF or takes it off.

I can't tell whether you intended the NEXT SENTENCE to be used to skip
Finalisation or not because you haven't affed the full-stops, but the
next programmer won't be able to tell either as some fastidious zealot
may have added or removed full-stops wherever possible without regard to
this 'feature'.

It is best to avoid NEXT SENTENCE even though the compiler hasn't
flagged it as non-standard.

The IF file-eof is actually redundant anyway.  The program will work
with:

       PERFORM Initialisation
       PERFORM Process-Records
           UNTIL file-eof
       PERFORM Finalisation

becasue the PERFORM is by default WITH TEST BEFORE.

 
> As you can see, one of my other "expectations" is that all paragraphs are
> numbered.  Judging by the posts to this newsgroup, that also seems to be out
> of vogue.    

Paragraph numbering was really useful when you had to find your way
around a box of several thousand punched cards.  It was probably also
useful when text editors were 'forwards only', as in the 70s.  When I
got my first full screen editor that went backwards and forwards 30 odd
years ago the whole point of numbering disappeared.  I suspect some
still organise their programs that way though, especially when rewriting
the same batch program over again.
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Robaire <rmiller@linux.ca>
- **Date:** 2001-06-05T08:56:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99lphtcq2ojfcne06c9f6ea7ti9uujarga@4ax.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz>`

```
Le Tue, 05 Jun 2001 15:56:46 +0100, Richard Plinston
<riplin@Azonic.co.nz> a ï¿½crit:

>Lynn Randall wrote:
>> 
…[50 more quoted lines elided]…
>the same batch program over again.

I expect that this was a slip-up ( admittedly a nasty one to detect )-
that the author would have written CONTINUE, instead of NEXT SENTENCE.
I suppose that the author will address this eventually.

CONTINUE would have been syntactically and logically acceptable here;
I also expect that another religious war will be started ( dï¿½jï¿½-vu? )
concerning the use of CONTINUE versus negating the condition in the IF
test.

Robaire
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-10T22:56:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B23FB05.E87B9B29@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <99lphtcq2ojfcne06c9f6ea7ti9uujarga@4ax.com>`

```
Robaire wrote:
> 
(snip)
> 
> I expect that this was a slip-up ( admittedly a nasty one to detect )-
…[6 more quoted lines elided]…
> test.

I work with a great number of people who stubbornly code NEXT SENTENCE
instead of CONTINUE even though they're coding END-IF nowadays. They're
probably lucking out because they're also coding periods everywhere they
can.

LiamD
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-11T07:07:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B24C285.B4D8A096@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <99lphtcq2ojfcne06c9f6ea7ti9uujarga@4ax.com> <3B23FB05.E87B9B29@optonline.net>`

```
Liam Devlin wrote:

> I work with a great number of people who stubbornly code NEXT SENTENCE
> instead of CONTINUE even though they're coding END-IF nowadays. They're
…[3 more quoted lines elided]…
> LiamD

Do they state any reasons for using NEXT SENTENCE?
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-13T00:57:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B26BA84.C6AE0F44@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <99lphtcq2ojfcne06c9f6ea7ti9uujarga@4ax.com> <3B23FB05.E87B9B29@optonline.net> <3B24C285.B4D8A096@brazee.net>`

```
Howard Brazee wrote:
> 
> Liam Devlin wrote:
…[8 more quoted lines elided]…
> Do they state any reasons for using NEXT SENTENCE?

Because they've always done it that way. It's a good thing we didn't
depend on COBOL programmers to explore the savannas and walk upright,
we'd still be living in caves.
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-05T07:54:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1CE496.764D90AE@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz>`

```


Richard Plinston wrote:

> Lynn Randall wrote:
> >
…[15 more quoted lines elided]…
> Cobol code and a bug looking for a place to happen.

While it probably is a bug, it is valid CoBOL code.   Certainly it is a bad idea
to stop using full stop periods and continue to use NEXT SENTENCE.   Since I use a
pre-compiler which automatically inserts NEXT SENTENCE in its IDMS commands, I am
not even tempted to remove periods from my coding style.

> The IF file-eof is actually redundant anyway.  The program will work
> with:
…[6 more quoted lines elided]…
> becasue the PERFORM is by default WITH TEST BEFORE.

That's what I would have done (with periods), but a little redundancy doesn't
hurt.


> > As you can see, one of my other "expectations" is that all paragraphs are
> > numbered.  Judging by the posts to this newsgroup, that also seems to be out
…[8 more quoted lines elided]…
> the same batch program over again.

I can't remember the last mainframe shop I worked in which didn't use them.
Reading a listing, they are nice, and it is easy to see "PERFORM 9000-FINALIZE"
will point to a paragraph at the end of the program.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-05T13:23:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fj83e$g45$1@slb7.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net>`

```
Just to "end" the debate before it gets too heated,

The use of NEXT SENTENCE in an IF statement that is terminated by an END-IF
is *NON* Standard - whether it is or is not "valid" COBOL, depends entirely
on the compiler vendor (and whether or not they have such an extension).

IBM and MERANT definitely *do* have (documented - and flagged if using
FLAGSTD) extensions allowing NEXT SENTENCE before END-IF (and END-SEARCH).
I believe that Realia also supports this extension.  I am LESS certain about
AcuCOBOL, Liant, PerCOBOL, and Fujitsu.

In Richard's "original" note he started talking about it being "invalid
COBOL <sic> source code" but later on talks about it not being "flagged".
Any vendor that allows this syntax (as an extension) and does NOT flag it as
an extension is violating the ANSI/ISO ('85) Standard.  However, any vendor
that DOES explicitly allow (and flag) this as an extension is FULLY ANSI
conforming.

P.S.  The "classic" (confirmed by ANSI/J4) example of how to get around this
restriction and STILL be ANSI conforming is to code something like the
following:

Let's say you want to code:

Read ABC
  At End
    If A = "B"
        Next Sentence
    Else
       Display "A doesn't equal 'B'"
    End-IF       *> this is non-standard
  Not At End
     Display "Not at end"
  End-Read
  Display "Still in same sentence"
      .
  Display "Next Sentence is here"
     .

The way that you can code this EXACT same logic and be ANSI Standard is as
follows:

   01  Next-Sentence-Flag Pic X  Value "X".
          ...
Read ABC
  At End
    If Next-Sentence-Flag = "X"
        If A = "B"
            Next Sentence
        Else
           Display "A doesn't equal 'B'"
     Else
          Display "never executed"
     End-IF       *> this is now standard as the END-IF is not for the same
"IF"
                       *> as the NEXT SENTENCE
  Not At End
     Display "Not at end"
  End-Read
  Display "Still in same sentence"
      .
  Display "Next Sentence is here"
     .

   ****

I do *not* recommend this 2nd approach as being "self-documenting" or not
"error-prone" - but it is ANSI/ISO conforming.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-06-05T21:35:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ogcT6.3146$Q64.353716@paloalto-snr1.gtei.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net>`

```
William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:9fj83e$g45$1@slb7.atl.mindspring.net...
> Just to "end" the debate before it gets too heated,

Ooh, ooh, may I try, too?

      SELECT ABC
          FILE STATUS IS INPUT-FILE-STATUS
          .....

01  FILE-STATII.
     05 INPUT-FILE-STATUS    PIC X(02).
        88 INPUT-FILE-AT-END  VALUE '10'.
...
[paragraph-name.]
 Read ABC
 IF INPUT-FILE-AT-END
   badda bing
ELSE
  badda bang
END-IF


MCM
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** Tony.Harmon@bnsf.com (Tony)
- **Date:** 2001-06-07T15:25:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1f9c44.502143404@news.swbell.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <ogcT6.3146$Q64.353716@paloalto-snr1.gtei.net>`

```
On Tue, 05 Jun 2001 21:35:17 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
>news:9fj83e$g45$1@slb7.atl.mindspring.net...
…[18 more quoted lines elided]…
>END-IF

I wanna try too. ;']

      SELECT ABC
...
[paragraph-name.]
READ ABC
  AT END
	BADDA BANG
  NOT AT END
	BADDA BING
END-READ

>
>
…[3 more quoted lines elided]…
>

Thanks,
Tony


===================================
Should have been easy, but its golf
===================================

"A day without hitting golf balls,
is a day longer to getting better"
  - Hennie Bogan

"Hogan was really talkative today.
Yeah? What'd he say? You're still
out!"
===================================
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-07T09:59:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1FA4EA.846B3576@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <ogcT6.3146$Q64.353716@paloalto-snr1.gtei.net> <3b1f9c44.502143404@news.swbell.net>`

```
Tony wrote:

>
> >[paragraph-name.]
…[17 more quoted lines elided]…
> END-READ

So you guys can't agree on whether to bing or to bang?
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-06-07T23:55:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ovUT6.1221$ep3.235111@dfiatx1-snr1.gtei.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <ogcT6.3146$Q64.353716@paloalto-snr1.gtei.net> <3b1f9c44.502143404@news.swbell.net> <3B1FA4EA.846B3576@brazee.net>`

```

Howard Brazee <howard@brazee.net> wrote in message
news:3B1FA4EA.846B3576@brazee.net...
>
> So you guys can't agree on whether to bing or to bang?

Do I gets my druthers?

MCM
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** "Lynn Randall" <LERandall@yahoo.com>
- **Date:** 2001-06-05T18:08:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1d84f1_1@news1.prserv.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net>`

```
I should probably add that I always use periods.  Mostly because I learned
to code when they were still required, there were no end-of-scope
terminators, and no "continue" verb.  Also, as a woman, I find missing a
period to be very disconcerting. <G>  But that's a discussion of a different
sort of "standard".

Anyway, I apologize to all for leaving off the periods in my example (and
indeed, for the poor coding in general), although I have found this
discussion interesting.

By the way, our compiler (IBM mainframe) option is set at NOFLAGSTD,
courtesy of our systems programmers.  My guess is they didn't want all our
really old code to get flagged all over the place. Anyway, the way my
original example was coded (with NEXT SENTENCE in the IF statement before
the END-IF) goes through our compiler without a squawk -- does that make it
"existentially" valid (albeit buggy) COBOL?

ler.

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:9fj83e$g45$1@slb7.atl.mindspring.net...
> Just to "end" the debate before it gets too heated,
>
> The use of NEXT SENTENCE in an IF statement that is terminated by an
END-IF
> is *NON* Standard - whether it is or is not "valid" COBOL, depends
entirely
> on the compiler vendor (and whether or not they have such an extension).
>
> IBM and MERANT definitely *do* have (documented - and flagged if using
> FLAGSTD) extensions allowing NEXT SENTENCE before END-IF (and END-SEARCH).
> I believe that Realia also supports this extension.  I am LESS certain
about
> AcuCOBOL, Liant, PerCOBOL, and Fujitsu.
>
> In Richard's "original" note he started talking about it being "invalid
> COBOL <sic> source code" but later on talks about it not being "flagged".
> Any vendor that allows this syntax (as an extension) and does NOT flag it
as
> an extension is violating the ANSI/ISO ('85) Standard.  However, any
vendor
> that DOES explicitly allow (and flag) this as an extension is FULLY ANSI
> conforming.
>
> P.S.  The "classic" (confirmed by ANSI/J4) example of how to get around
this
> restriction and STILL be ANSI conforming is to code something like the
> following:
…[32 more quoted lines elided]…
>      End-IF       *> this is now standard as the END-IF is not for the
same
>                        *> > "IF" as the NEXT SENTENCE
>   Not At End
…[17 more quoted lines elided]…
> >

>snip<
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-06T03:14:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1DA0AC.CD375D35@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net>`

```


Lynn Randall wrote:

> I should probably add that I always use periods.  Mostly because I learned
> to code when they were still required, there were no end-of-scope
…[3 more quoted lines elided]…
>

Well..... I did wunder. Thought perhaps maybe 'Lynn' was one of the guys. Had it
been 'Lynne', then definitely you're a lady <G>

Yes I also learned to code using full stops, (that avoids any ambiguity !), plus
of course miserable UPPERCASE only, even on the first desktops. But I hate red
tape and reduce my coding to as little as possible.

There are very few instances required for full stops in OO. The significant one
is if a method performs paragraphs, (i.e. paragraphs contained within the
method).
The last line before the next paragraph name must contain one or Net Express
will give me a compiler error, (unlike as Bill Klein just pointed out, IBM gives
you options and I think he said a warning flag for this one).

Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-06T11:06:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9flkd6$r56$1@slb1.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com>`

```
Jimmy - I think you will find that MERANT (NetExpress) actually has a
compiler option that allows you to "omit" the period before paragraph names.
HOWEVER, to use this feature, you must turn on A-/B-margin "checking" which
most NE users are HAPPY to get rid of.

("Logically" it is impossible for a compiler to BOTH get rid of A-/B-margin
restrictions and the requirement for periods before paragraph names.  You
can get rid of either - as an extension to the '85 Standard - but not both
at the same time.)
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-06T17:58:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1E6FD6.DB3D1E4E@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <9flkd6$r56$1@slb1.atl.mindspring.net>`

```


"William M. Klein" wrote:

> Jimmy - I think you will find that MERANT (NetExpress) actually has a
> compiler option that allows you to "omit" the period before paragraph names.
…[6 more quoted lines elided]…
> at the same time.)

Bill, thanks for the tip - but as I've said before I just DO NOT mess around
with  default settings !  Having now delved into SQL - that's the first time
I've started using "$set..........", but that's obligatory for the pre-processor
to kick in.

Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-07T08:22:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1F2BCE.4F45EC38@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <9flkd6$r56$1@slb1.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Jimmy - I think you will find that MERANT (NetExpress) actually has a
> compiler option that allows you to "omit" the period before paragraph names.

But why would you want to (unless you have a whole load of source where
the programmers relied on this dubious non-standard 'feature').  It
doesn't 'defeat' the NEXT SENTENCE going to the end of the current
paragraph because the 'next full stop' is on the paragraph name.

It would be preferable to process the source to make it 'valid COBOL',
using, say, a PERL or Python script (or even ReXX).
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-08T16:58:31+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B20F627.67F31F81@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com>`

```
James J. Gavan wrote:

>             full stop period        <G>

I never did understand why the Americans [mis]used the term 'period' to
refer the full-stop.

With every other usage of the word period, such as 'historical period'
or 'musical period' this refers to the content or time from the start to
the end.  The 'period of a sentence of words' should be 'from the first
word to the last' just as the 'period of a prison sentence' refers to
the 'first day to the last'.

Yet Americans use 'period' to refer to the character that lies beyond
'the period of the sentence', the character that stops the sentence, the
full-stop.

(it is a full stop because a comma, semi-colon or colon are only partial
stops).
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** Robaire <rmiller@linux.ca>
- **Date:** 2001-06-08T10:13:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz>`

```
Le Fri, 08 Jun 2001 16:58:31 +0100, Richard Plinston
<riplin@Azonic.co.nz> a ï¿½crit:

>James J. Gavan wrote:
>
…[16 more quoted lines elided]…
>stops).

F.Y.I. ( and quite off topic )

I won't deny that Americans (and anglophone Canadians, for that
matter) favour the word "period" over "full stop" but, in this case,
that doesn't mean it is incorrect usage.

The Concise Oxford Dictionary 7th ed. describes the period as "6. full
pause at end of sentence; =FULL stop..."

"Modern American Usage" (Wilson Follett, 1966) describes "THE PERIOD"
in a 20+ line paragraph without ever mentioning the expression full
stop.

R. Miller
_______________________________

Do people who prefer their spaghetti " al dante " (sic)
also prefer their lasagna " al inferno " ?
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-06-08T17:06:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QC7U6.8956$DW1.360567@iad-read.news.verio.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com>`

```
In article <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com>,
Robaire  <rmiller@linux.ca> wrote:
>Le Fri, 08 Jun 2001 16:58:31 +0100, Richard Plinston
><riplin@Azonic.co.nz> a �crit:
…[6 more quoted lines elided]…
>>refer the full-stop.

[snippage]

>The Concise Oxford Dictionary 7th ed. describes the period as "6. full
>pause at end of sentence; =FULL stop..."

The not-Concise OED gives, from

<http://dictionary.oed.com/cgi/entry/00175602?query_type=word&queryword=period&sort_type=alpha&edition=2e&first=1&max_to_show=10&search_id=OGzM-1DygK3-3069>

--begin quoted text:

11. a. A full pause such as is properly made at the end of a sentence.

    b. The point or character that marks the end of a complete sentence; a
full stop (.).

1609 J. DAVIES Holy Roode (1878) 20/2 No Commaes but thy Stripes; no
Periods But thy Nailes. 1612 BRINSLEY Lud. Lit. 95 In reading, that he
[the scholar] doe it distinctly, reading to a Period or full point, and
there to stay.

--end quoted text

Both these citings appear to antedate anything which might accurately be
labelled 'American' use.

DD
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-09T08:20:54+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B21CE56.631E3BEA@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net>`

```
NA wrote:
> 
> 1609 J. DAVIES Holy Roode (1878) 20/2 No Commaes but thy Stripes; no
> Periods But thy Nailes. 1612 BRINSLEY Lud. Lit. 95 In reading, that he
> [the scholar] doe it distinctly, reading to a Period or full point, and
> there to stay.

> Both these citings appear to antedate anything which might accurately be
> labelled 'American' use.

Yes, of course.  I should have realised that it was archaic English (in
England).  

Quite a number of 'Americanisms', or 'Australianisms', or similar were
actually common usage in the country of origin of the immigrants at the
time they left.  England (and some other Europeans) have always evolved
their language, which is why we no longer speak middle-English or
Normandy-French.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-08T21:53:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B214A03.D024044F@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz>`

```


Richard Plinston wrote:

> NA wrote:
> >
…[15 more quoted lines elided]…
> Normandy-French.

Still off topic - but it can be fascinating.

As an extension to that regarding the former colonies - they don't have any
problem with GLOUCESTER in New England, like you and me they *know* all about
Dr. Foster. Also in New Hampshire they pronounce PORTSM'TH the same way I do.

I was initially puzzled when I first came over here why our American friends
pronounce it 'erbs as opposed to herbs - logic it's the Cockneys who are
supposed to drop their 'aitches'. Alistair Cooke on PBS Masterpiece Theatre
wised me up - seems the they took the word directly from the French whereas we
anglicized it.

Richard, you may not  know about PBS/Masterpiece Theatre, but recall the BBC's
weekly "Letter from America" - might still be done, but I'm reckoning he has
to be in his 90s by now, if still alive. Now a US citizen, apart from
Churchill, he was the only other Brit given the distinction of addressing the
US  Congress. Still even Alistair made boo-boos, said Charles Dickens was born
in Chatham, (where his dad moved for work) - correction - Commercial Road,
Portsmouth; still a museum.

Quiz time - any takers ? Guess how this (Norman French) is pronounced in
England - Hatch Beauchamp. Boy! Did I get stuck once here in Calgary. I asked
the girl bean counters, "Who has the ledger sheets for Dauphin ?" Blank looks,
then, "Oh, you mean Dolfin".

You shouldn't be wasting your time programming if you know the origin of this
street name I once lived in - Amwell Street, Islington, N.London - believe it
or not 'Amwell' is corrupted from three words ! (Clues for Bill -  the English
were much more into religion in the Middle Ages, and remember telling me
"Repeat after me, it is...... <G>).

Jimmy.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-10T23:06:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B23FD64.5B91A739@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com>`

```
"James J. Gavan" wrote:
> 
(snip)
> 
> 
> Quiz time - any takers ? Guess how this (Norman French) is pronounced in
> England - Hatch Beauchamp.

"aitch beecham"? ("hatch" just seems way too obvious) 

Well?

LiamD
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-11T00:18:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B240F19.D9C9E705@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <3B23FD64.5B91A739@optonline.net>`

```


Liam Devlin wrote:

> "James J. Gavan" wrote:
> >
…[10 more quoted lines elided]…
> LiamD

Bloody good guess Liam. Comes out 'HATCH BEECHAM'. One of the UK
pharmaceutical firms was/is called Beechams - fair bet it started out as
Beauchanmp - might even have ben an 's' on the end. With those weirdos that
occur in UK, the name Auchinleck comes out 'AFFLECK'. There are family members
who use the spelling 'Affleck'.

Now when it comes to Celtic names, even with roots back to the 'Auld Sod' - I
get real tounge-tied. So how does your first name come out phonetically., (I
prefer Christian name - but what the hell).  I'd been inclined to say LEE-AM
but I suspect it's more like L'EEM.

Jimmy (Seamus if you like <G>).
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 13)_

- **From:** "Tim Scrivens" <tim.scrivens@nz.eds.com>
- **Date:** 2001-06-11T15:30:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g1e0m$cjs$1@hermes.nz.eds.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <3B23FD64.5B91A739@optonline.net> <3B240F19.D9C9E705@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B240F19.D9C9E705@home.com...
>
>
…[7 more quoted lines elided]…
> > > Quiz time - any takers ? Guess how this (Norman French) is pronounced
in
> > > England - Hatch Beauchamp.
> >
…[8 more quoted lines elided]…
> Beauchanmp - might even have ben an 's' on the end. With those weirdos
that
> occur in UK, the name Auchinleck comes out 'AFFLECK'. There are family
members
> who use the spelling 'Affleck'.
>
> Now when it comes to Celtic names, even with roots back to the 'Auld
Sod' - I
> get real tounge-tied. So how does your first name come out phonetically.,
(I
> prefer Christian name - but what the hell).  I'd been inclined to say
LEE-AM
> but I suspect it's more like L'EEM.
>
> Jimmy (Seamus if you like <G>).

How about some of the old standards, name-wise

Chomondoley
Coughtry (5 pronunciations)
Dondall
even Powell
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 14)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-11T05:30:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B245831.13A20ADD@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <3B23FD64.5B91A739@optonline.net> <3B240F19.D9C9E705@home.com> <9g1e0m$cjs$1@hermes.nz.eds.com>`

```


Tim Scrivens wrote:

Still off topic :

> How about some of the old standards, name-wise
>
…[3 more quoted lines elided]…
> even Powell

Yes Chomondoley = Chumley. But guess you kinda got me on the rest, don't recall
them. The only reference I can think of is the Boy Scout founder "My name is
Baden-Powell as in Garden Trowel" - but there he's stressing the German origin.

Just thought - there's always Featherstonhaugh = Fanshaw. I knew a Univac
salesman here in Calgary who was unaware it came out Fanshaw - still pronounced
it as officially written. I suppose it was enough of a challenge, that having
mentally noted it, people ALWAYS wrote/typed his surname correctly !

Jimmy.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 14)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2001-06-11T05:41:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2459A5.9F738A51@worldnet.att.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <3B23FD64.5B91A739@optonline.net> <3B240F19.D9C9E705@home.com> <9g1e0m$cjs$1@hermes.nz.eds.com>`

```
Tim Scrivens wrote:
> 
> How about some of the old standards, name-wise
…[4 more quoted lines elided]…
> even Powell

Cholmondoley = Chumley?  Sounds like a P.G. Wodehouse festival.

How do you pronounce Mainwaring?
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 15)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-11T20:32:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B252B9B.C910A7C8@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <3B23FD64.5B91A739@optonline.net> <3B240F19.D9C9E705@home.com> <9g1e0m$cjs$1@hermes.nz.eds.com> <3B2459A5.9F738A51@worldnet.att.net>`

```


Arnold Trembley wrote:

> Tim Scrivens wrote:
> >
…[9 more quoted lines elided]…
> How do you pronounce Mainwaring?

In exactly the same way a Cockney spiv nicknames a Scot 'Taffy" ! What a
delight as Captain Mainwaring/Mannering or the crafty little Irish
priest in "Bless Me Father".

Name wise there's always Mrs. Bouquet/Bucket from 'Keeping Up
Appearances'. Nah ! She aint fictional - believe me they still EXIST  !

PS: 'Spiv' - First used in WW2 - best I can suggest is - smart-assed,
street-wise and that particular spiv was a 'black marketer' - got
rationed goods, (petrol/clothing/food)  by stealing, or 'under the
table' and re-sold for profit.

PPS : That snobbery conveyed by Mrs. Bouquet was a rampant part of
British society - certainly back in the WW2 era, at which  'Dad's Army'
poked fun. But to show you its impact - and this is for real :-

Battle of Britain is in progress and two young 'chappies' join the RAF
as fighter pilots to combat the Luftwaffe onslaught. One is not 'Qu-ite
right', perhaps he doesn't hold hs knife and fork correctly, or slurps
over his beer. One becomes a commissioned pilot officer, the latter a
lowly sergeant.

They both on the same day shoot down an Me-109. They are recognized for
bravery and duly trot up to Buckingham Palace where the King (George VI)
will pin a medal (gong) on their chest. The Hossifer and Gentleman - he
gets the DFC (Distinguished Flying Cross), but the yobbo sergeant - DFM
(Distinguished Flying Medal) ! Aint democracy and equal opportunity just
great !

They've discreetly let that 'difference' drop since.

Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 15)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-13T01:03:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B26BBBF.BCF2BF4@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <3B23FD64.5B91A739@optonline.net> <3B240F19.D9C9E705@home.com> <9g1e0m$cjs$1@hermes.nz.eds.com> <3B2459A5.9F738A51@worldnet.att.net>`

```
Arnold Trembley wrote:
> 
> Tim Scrivens wrote:
…[10 more quoted lines elided]…
> How do you pronounce Mainwaring?

"Luxury Yacht"

(sorry, couldn't resist such a good setup)

LiamD
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 13)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-13T01:01:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B26BB73.27EAF5DC@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <3B23FD64.5B91A739@optonline.net> <3B240F19.D9C9E705@home.com>`

```
"James J. Gavan" wrote:
> 
> Liam Devlin wrote:
> 
(snip)
> 
> Bloody good guess Liam. Comes out 'HATCH BEECHAM'. One of the UK
…[3 more quoted lines elided]…
> who use the spelling 'Affleck'.

Like fair Ben in "Pearl Harbor"?

> Now when it comes to Celtic names, even with roots back to the 'Auld Sod' - I
> get real tounge-tied. So how does your first name come out phonetically., (I
> prefer Christian name - but what the hell).  I'd been inclined to say LEE-AM
> but I suspect it's more like L'EEM.

Kind of, it's sort of "LEE-um" where the "um" part is hardly there. I
have no idea how it's supposed to be pronounced since no one in my
family was actually from Ireland.
 
> Jimmy (Seamus if you like <G>).

Yes, I do, Seamus, good name, lad.

LiamD
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** Robaire <rmiller@linux.ca>
- **Date:** 2001-06-11T10:35:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com>`

```
Le Fri, 08 Jun 2001 21:53:35 GMT,
 "James J. Gavan" <jjgavan@home.com> a ï¿½crit:

>Still off topic - but it can be fascinating.
>
…[8 more quoted lines elided]…
>anglicized it.
  <large snip>
>Jimmy.

Continuing fff-topic ( just mentioning this - I've heard that some
people use this newsgroup to discuss COBOL).

The French exerted a strong influence in England in the vocabulary
( and improvement, I expect ) of the culinary arts. When several big
wigs were losing their heads during the French Revolution, many chefs
(french) were, as a corollary, losing their jobs. They emigrated "en
masse" to England where they set up restaurants, or worked for the
British aristocracy. Apparently, that is why, today, anglophones do
not eat pig, but pork (from the French "porc"), not sheep, but mutton
("mouton"), not calf, but veal ("veau") and not cow, but beef ("boeuf)
- I'm sure you get the picture.

As for herbs losing its leading "h" when pronounced by Americans, I
can't see that - the influence of the French on american "cuisine"
can't possibly have been that great, apart from Cajun cooking, which
apparently reached Louisiana via French Canada.

What I can see in "erbs" is the american "penchant" for efficiency.
At the beginning of the century, Henry Fowler , besides warning us
against the dangers of using gallicisms in English (French-Candian
will get a big charge out of that), he also stated:

"There is a real danger of our literature's veing americanized, and
that not merely in details of vocabulary ... but in its general tone."
He then gives an example of Rudyard Kipling's work, pointing out its
"...sort of remorseless and scientific efficiency..."

Alistair Cook dropping his h's - it seems to me he dropped mostly
crumbs - oh no! - that was Alistair Cookie on Monsterpiece Theatre.
"The Monsters of Venice" was my favourite play!

R. Miller
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-11T09:00:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B24DD07.8DF4EE35@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com>`

```
Robaire wrote:

> The French exerted a strong influence in England in the vocabulary
> ( and improvement, I expect ) of the culinary arts. When several big
…[6 more quoted lines elided]…
> - I'm sure you get the picture.

I thought this was from the Normans who spoke French, while their farmers were
Anglo-Saxon.


> As for herbs losing its leading "h" when pronounced by Americans, I
> can't see that - the influence of the French on american "cuisine"
…[6 more quoted lines elided]…
> will get a big charge out of that), he also stated:

This is an exception - for the most part Americans pronounce words much more
phonetically than do the Brits.  After all, most of our (American) ancestors were
literate when they first learned English.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-12T08:07:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B25BFB4.24FA466@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com>`

```
Robaire wrote:
> 
> The French exerted a strong influence in England in the vocabulary
…[7 more quoted lines elided]…
> - I'm sure you get the picture.

It goes back further that, to the Normans.  When the Normans took over
they became the ruling class and spoke Norman-French (Normans were
originally North-men or Vikings).  The English remained serfs.  As there
was a separation between the meat-eating French speakers and the animal
raising Middle English speakers (unable to afford to eat meat) the two
sets of terms became separated.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 13)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-13T01:07:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B26BCB7.B57F3B34@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz>`

```
Richard Plinston wrote:
> 
> Robaire wrote:
…[16 more quoted lines elided]…
> sets of terms became separated.

Fortunately they could agree on hating the bog dwelling Irish.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 14)_

- **From:** R. Miller <robaire@sympatico.ca>
- **Date:** 2001-06-13T09:31:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<udqeit80ukffsqlsac35157dif71h7vr91@4ax.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net>`

```
On Wed, 13 Jun 2001 01:07:22 GMT, Liam Devlin <LiammD@optonline.net>
wrote:

>Richard Plinston wrote:
>> 
…[19 more quoted lines elided]…
>Fortunately they could agree on hating the bog dwelling Irish.

I wasn't aware of that - that the Irish were bog dwellers.

As for the French hating them, it reminds of something that I've
wondered about for a long time: that is, why do Microsoft have
software translated into the French, in Ireland. I don't know how much
of it is done there, but I recall seeing such a notice more than once.

I know it's taking the off-topic subject off topic, but at least were
getting closer to computers again, if not to COBOL.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 15)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-13T17:08:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B279EB6.EE24DE82@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com>`

```


"R. Miller" wrote:

> >
> >Fortunately they could agree on hating the bog dwelling Irish.
>
> I wasn't aware of that - that the Irish were bog dwellers.
>

Well they aren't, anymore than they keep their pigs in the front parlour ! It's
just part of the English (Anglo-Saxon) denigration of the Irish. Nothing new -
here in Canada there used to be numerous jokes about Ukrainian immigrants, and
my neighbour opposite, (died about a month ago) definitely experienced racism
towards Ukrainians as a kid - and he was Canadian born. (The historical
background is that the Ukraine was a supporter/ally of Germany against Imperial
Russia during WW1).

Similarly of course you have the mocking of early immigrant Swede accents in
the States. Then of course there's the numerous slurs towards Wops in the
States etc. (I think you would be treading on very dangerous ground to make an
Irish slur in the Boston area <G>).

>
> As for the French hating them, it reminds of something that I've
…[3 more quoted lines elided]…
>

French didn't hate the Irish, if that's what you meant. Remember they were
initially co-religionists, (i.e. until the French Revolution made France 'no
religion').. Never finished it, but there was a novel, potentially was going to
be turned into a movie, "The Year of the French" - late 1700s - French navy was
supposed to support an Irish rebellion. (I don't know the historical facts -
perhaps somebody from "Bog" country can fill in).

>
> I know it's taking the off-topic subject off topic, but at least were
> getting closer to computers again, if not to COBOL.

Well back onto the topic of COBOL - just don't use GO TO <G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 16)_

- **From:** R. Miller <robaire@sympatico.ca>
- **Date:** 2001-06-13T14:04:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com>`

```
Please allow me correct the attribution of quotes here :

>Liam Devlin <LiammD@optonline.net> wrote:
>> > Fortunately they could agree on hating the bog dwelling Irish.

>"R. Miller" wrote:
>> I wasn't aware of that - that the Irish were bog dwellers.

On Wed, 13 Jun 2001 17:08:13 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Well they aren't, anymore than they keep their pigs in the front parlour ! It's
>just part of the English (Anglo-Saxon) denigration of the Irish.

I was not aware of Mr. Devlin's origin (English, from what you say)
and my comment should have read ( sloppy editing on my part )
>> I wasn't aware of that - that the Irish were considered bog dwellers.

I was aware that it was a racial slur, but did not properly express
that I was curious as to why they are called that.

>Nothing new - 
>here in Canada there used to be numerous jokes about Ukrainian immigrants, and
…[9 more quoted lines elided]…
>
I can feel for them - I was the only anglophone student in a working
class ( Maisonneuve, in Montreal ) francophone grade school in the
1950s - and I didn't even speak French - horrible memories.

Since you mention the term "Wops", the French-Canadian author of a
book on Tramways (Jacques Pharand) attributes the term to bookkeepers,
According to him, the activity of the mostly Italian labourers who
were repaving roads in Montreal during WWWII  was described by
bookkeepers as "Working On Pavement", abbreviated W.O.P.

Anyone to contradict or complement this information ?

>> As for the French hating them, it reminds of something that I've
>> wondered about for a long time: that is, why do Microsoft have
…[10 more quoted lines elided]…
>
More explicitely, why do you call it Bog country? (I have not yet been
there.)
>>
>> I know it's taking the off-topic subject off topic, but at least were
…[4 more quoted lines elided]…
>Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 17)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-06-13T18:18:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48OV6.9551$DW1.389208@iad-read.news.verio.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com>`

```
In article <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com>,
R. Miller  <robaire@sympatico.ca> wrote:

[snippage]

>Since you mention the term "Wops", the French-Canadian author of a
>book on Tramways (Jacques Pharand) attributes the term to bookkeepers,
…[4 more quoted lines elided]…
>Anyone to contradict or complement this information ?

The term pre-dates WWII; I had been taught that it was an abbreviation of
'giuappa', a Neapolitan word for 'beautiful ones'.

DD
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 18)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-06-14T11:36:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B730BA26CBC624F4.36E90785E7D4A2E8.43F2B21C68F25D4C@lp.airnews.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com> <48OV6.9551$DW1.389208@iad-read.news.verio.net>`

```
On Wed, 13 Jun 2001 18:18:40 GMT, docdwarf@clark.net (  NA)
enlightened us:

>In article <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com>,
>R. Miller  <robaire@sympatico.ca> wrote:
…[14 more quoted lines elided]…
>DD

Close Doc.  Actually, the word wop has several derivations from
different languages.  They are:

Italian dialectal guappo, thug, from Spanish guapo, handsome, dashing,
braggart, bully, from French dialectal wape, rogue, from Latin vappa,
flat wine, scoundrel.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Sticks and stones may break my bones, 
But whips and chains excite me!


DON'T DRILL in the Artic National Wildlife Refuge
Read the real facts at:

http://www.worldwildlife.org/arctic-refuge/

also

http://www.savepolarbears.org/


Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 17)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-13T12:23:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B27AFB8.4747A801@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com>`

```
"R. Miller" wrote:

> Since you mention the term "Wops", the French-Canadian author of a
> book on Tramways (Jacques Pharand) attributes the term to bookkeepers,
…[4 more quoted lines elided]…
> Anyone to contradict or complement this information ?

This type of "explanation" is common, the most popular one being the prison with the
notice "For Unlawful Carnak Knowledge".   Several years ago, I read a National
Geographic article on Naples which said that Neapolitan young men liked to be called
"guapo", which term got shortened and turned into an insult.  I bet it's older than
WWII.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 18)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-06-13T18:55:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cGOV6.9553$DW1.387335@iad-read.news.verio.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com> <3B27AFB8.4747A801@brazee.net>`

```
In article <3B27AFB8.4747A801@brazee.net>,
Howard Brazee  <howard@brazee.net> wrote:
>"R. Miller" wrote:
>
…[12 more quoted lines elided]…
>WWII.

Well, at least I don't have to reply to my own posting.

From : http://parallel.park.uga.edu/distance/texts/berlitz.html

--begin quoted text:

Italians, whether in America or abroad, have been given other more
picturesque appellations. Wop, an all-time pejorative favorite, is
curiously not insulting at all by origin, as it means, in Neapolitan
dialect, "handsome," "strong" or "good looking." Among the young Italian
immigrants some of the stronger and more active--sometimes to the point of
combat--were called guappi, from which the first syllable, "wop," attained
an "immediate insult" status for all Italians.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 19)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-14T00:37:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2807E9.7FB50A6A@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com> <3B27AFB8.4747A801@brazee.net> <cGOV6.9553$DW1.387335@iad-read.news.verio.net>`

```


NA wrote:

> --begin quoted text:
>
…[8 more quoted lines elided]…
> --end quoted text

Interesting. When we took citizenship here in the Great White North the citizenship judge
asked my 10 year old boy, "What is a Paki ?" (slur for Pakistani). Much squirming by
young kid and then a mumbled reply, "Well it's a bad word for Indians (East)".

"Well", says the judge. "Not exactly. It really translates to 'beautiful flower'".
.
Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 17)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-13T22:38:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B27EC01.8ED6A55D@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com>`

```


"R. Miller" wrote:

Rather than repeat the previous messages.

Liam implied his (current) family weren't Irish - the branch in the States ?.
Certainly his first name is and to my mind his last name DEVLIN has an Irish ring to
it. But might also be a derivation from French and could be Anglo/French or indeed
Irish/French.   Liam - care to clarify.

As to Bog country. Regrettably I have not as yet been to Ireland though both
parents and sets of grandparents were born in 'bog country'. The reference is
primarily to the bogs, swampy ground, from which the Irish (used to ?) cut peat -
because of a lack of coal. Note : The country is also nicknamed the Auld Sod - a
reference to peat again.

As of some 25 years ago, my Canadian sister-in-law said it was beautiful but
impoverished. I believe that has largely changed, due to entry into the Common
Market, plus the large resource of well educated people without jobs - US and German
firms have moved in to capitalize on that resource - paid off for everybody.

Example from a TV program sometime back - you submit an insurance claim in New York;
chances are the paperwork is flown to Ireland where your claim is assessed. Either
you get some bucks or don't - and that gets determined in Ireland. Their assessment
is flown back to the States. (Of course you can now update that scenario if you
think in terms of e-mail).

As to the actual facts - we need a 'home bred' Irishman to comment.

Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 18)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-15T03:04:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B297B21.E68C3F10@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com> <3B27EC01.8ED6A55D@home.com>`

```
"James J. Gavan" wrote:
> 
> "R. Miller" wrote:
…[6 more quoted lines elided]…
> Irish/French.   Liam - care to clarify.

Sorry for the confusion. We're definitely Irish, but all my Irish
relatives were born in the US. My paternal grandfather & grandmother
were born in New Haven, Conn., in 187x. I don't know where their parents
were born. 
 
> As to Bog country. Regrettably I have not as yet been to Ireland though both
> parents and sets of grandparents were born in 'bog country'. The reference is
…[7 more quoted lines elided]…
> firms have moved in to capitalize on that resource - paid off for everybody.

The Irish economy had been depressed for decades (if not longer), which
is why many manufacturers located plants there, e.g., DeLorean. IIRC the
Irish economy turned 1990-ish and has been booming since. 

> Example from a TV program sometime back - you submit an insurance claim in New York;
> chances are the paperwork is flown to Ireland where your claim is assessed. Either
…[4 more quoted lines elided]…
> As to the actual facts - we need a 'home bred' Irishman to comment.

Righto.

LiamD
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 17)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-14T07:29:18+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2859BE.2E70A6C7@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com>`

```
> 
> >> I wasn't aware of that - that the Irish were considered bog dwellers.

The main reason that they may have been called 'bog dwellers' is because
the English landlords have burnt down the houses because they weren't
paying the rent.  (see 'history').

 
> Since you mention the term "Wops", the French-Canadian author of a
> book on Tramways (Jacques Pharand) attributes the term to bookkeepers,
…[4 more quoted lines elided]…
> Anyone to contradict or complement this information ?

Since the 1920s Britain had an Air Force operating in the near east to
keep the local tribes from fighting.  They often used locals as
'Wireless Operators' or 'Wireless Operator/Gunners' and this, as far as
I can tell is the origin of WOP and WO/G in that service.  Even the
English in these jobs were usually working class so it was a generally
derisive term regardless of race.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 18)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-15T03:09:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B297C47.95F73BD6@optonline.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com> <3B2859BE.2E70A6C7@Azonic.co.nz>`

```
Richard Plinston wrote:
> 
> >
(snippage)
> 
> Since the 1920s Britain had an Air Force operating in the near east to
…[4 more quoted lines elided]…
> derisive term regardless of race.

I was told in college that the term "WOG" meant "worthy oriental
gentleman" and that historically the Brits said "the WOGs begin at
Calais". Post-WW II that's supposed to have changed to "the WOGs begin
at Liverpool". Who says there's no value in a liberal arts education?

LiamD :-)
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 19)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-15T04:02:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B29899F.713F3520@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B279EB6.EE24DE82@home.com> <3j9fitgo0nod80kfi832ovi3djgqu9hkrs@4ax.com> <3B2859BE.2E70A6C7@Azonic.co.nz> <3B297C47.95F73BD6@optonline.net>`

```


Liam Devlin wrote:

> Richard Plinston wrote:
> >
…[15 more quoted lines elided]…
> LiamD :-)

I'll go with your definition Liam but it was more slurrish, "Western Oriental
Gentleman" - e.g. think of Peter Sellers, "I am having most greatest
difficulty sir, even though I am having a degree Bombay Honours failed".

But who know Richard might be right - given the RAF W.O.G. in a two-seater
plane back in the '20s. The Royal Flying Corps (Army) became the RAF in 1918,
the "daddy" of the RAF being Marshal of the RAF Lord Trenchard. (Kind of a
'revered' figure like Jimmy Doolittle).

I knew it as the Middle East but for the time period Richard quotes, probably
was Near East, when Iraq was referred to as Mesopotamia.

Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 15)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-14T07:20:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2857C5.F903D04F@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com>`

```
R. Miller wrote:
> 
> >Fortunately they could agree on hating the bog dwelling Irish.
…[3 more quoted lines elided]…
> As for the French hating them, 

The Normams were not French, they were Vikings while the French were
Francs.  The Normans spoke French but only because they had lived there
for some time.

The French and the Irish often joined up together to fight the English
(and probably still would).
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 16)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-13T22:11:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B27E5E2.A4638070@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com> <QC7U6.8956$DW1.360567@iad-read.news.verio.net> <3B21CE56.631E3BEA@Azonic.co.nz> <3B214A03.D024044F@home.com> <c7j9itsinodl5l7qgv0e7rcg87c9m0qud1@4ax.com> <3B25BFB4.24FA466@Azonic.co.nz> <3B26BCB7.B57F3B34@optonline.net> <udqeit80ukffsqlsac35157dif71h7vr91@4ax.com> <3B2857C5.F903D04F@Azonic.co.nz>`

```


Richard Plinston wrote:

> R. Miller wrote:
> >
…[8 more quoted lines elided]…
> for some time.

To substantiate Richard's statement - if you can - go to your video store,
B & W movie, I think, guess at name - 'The Warlord", starred Charlton
Heston and Richard Boone. (Hey ! It's got to be 'factual' if it is filmed
by Hollywood <G>).

Worth also remembering, for a long time, the (Norman) kings of England from
1066 onwards, while vassals to the French king, controlled more of modern
France than he did. Hence this past year the anniversary movie/TV shows on
Joan of Arc  This came to an end with the loss of Calais during reign of
Mary Tudor 15??????

>
> The French and the Irish often joined up together to fight the English
> (and probably still would).

Can't speak about the French - but possibly <G> Don't know how factual, but
my brother always quotes - if the English are in a war the Irish are there
along with them, either with them or on the other side.  He claims there
was an Irish regiment (contingent) fought for Napoleon at Waterloo.
(Churchill was sure pissed at de Valera's neutral stance in WW2).

He can't be totally correct - my grandfather fought for Queen and country
at Omdurman in 1898 - to the best of my knowledge there were no Irish,
using black shoe polish, disguised as the Mahdi's Sudanese fuzzie wuzzies
(  your reference to Wogs).

I recall that delicious scene in 'Braveheart'. "Send in the infantry
(Irish)", says King Edward I. The 'Paddies' advance towards the Scots. They
initially pause and then embrace their Celtic cousins; they would ALL
rather have a piss-up, than fight. (After all, in typical Irish fashion, I
know from my own family members, it's the piss-ups that cause the fights
<G>)

 "Oh the Irish", sighs King Edward - played by IRISH actor Patrick
MacGooghan !
(wrong spelling of name, but close phonetically).

Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-08T17:40:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B210EBE.6E6EA53F@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com>`

```


Robaire wrote:

> >>             full stop period        <G>
> >
…[12 more quoted lines elided]…
>

Well be careful of that phrase 'anglophone Canadians' - I would use
'Americanized Canadians' due to the fact that I'm told the majority of our
schoolbooks are printed in the U.S.  Here in Calgary you will see signs to
the local shopping mall "South Center Mall" or "South Centre Mall".

Seems like we really don't know 'which way is up' - we should - seeing as we
mockingly refer to ourselves as the Great White North <G>

Jimmy

PS: Just so long as we don't let 'em print our history books. Haven't seen
it, but a lady some ten years younger than me was very disappointed with
'Pearl Harbor', note deference to our "cousins" -  'Harbour'. (When in
Rome.....).

A THREE hour film about a spectacular ONE hour air attack First hour devoted
to our two heroes who had the hots for the same heroine. The actual 'battle'
filming was spectacular. Then, (my friend's observation), they spoiled it by
including a US attack on Japan - I'm assuming this was the sixteen Jimmy
Doolittle B25-Mitchells taking off from aircraft carriers - in April 1942.
This appeared to add a 'jingoistic' flavour to the film.

Pity - so far as I'm concerned, and am aware, Holywood had already produced
two balanced and excellent movies, "Tora, Tora, Tora" and "Midway". And FDR's
famous words to Congress still echo down the passages of time.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-09T08:04:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B21CA97.568D05DF@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <opm1it06c47o009u3j6316ueui9u7lsp2q@4ax.com>`

```
Robaire wrote:
> 
> >I never did understand why the Americans [mis]used the term 'period' to
> >refer the full-stop.
 
> F.Y.I. ( and quite off topic )
> 
…[5 more quoted lines elided]…
> pause at end of sentence; =FULL stop..."

So, perhaps it is 'the period of the pause'.  That is, the use of some
punctuation is to indicate where pauses should be placed when speaking
the words and how long thay should be (I don't think that schools teach
this anymore).

The '.' indicates a 'long period pause' and the ',' indicates a short
period pause.



> "Modern American Usage" (Wilson Follett, 1966) describes "THE PERIOD"
> in a 20+ line paragraph without ever mentioning the expression full
> stop.

No, it wouldn't.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** klatteross@aol.commmm (Ross Klatte)
- **Date:** 2001-06-09T10:25:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010609062551.11353.00000544@ng-ce1.aol.com>`
- **References:** `<3B21CA97.568D05DF@Azonic.co.nz>`

```
>From: Richard Plinston riplin@Azonic.co.nz 
>Date: 2001-06-09 03:04 Eastern Daylight Time

>So, perhaps it is 'the period of the pause'.  That is, the use of some
>punctuation is to indicate where pauses should be placed when speaking
…[5 more quoted lines elided]…
>

Personally, I like the recent introduction of the term "dot" for the 
little round punctuation mark that has so many overloaded
constructors.  
What do the British call the dots in St. Ives, or Mr. Ed, 
or N. Ireland, or 3.14, or...?

Drifting off topic for this newsgroup, which is supposed to
be limited to critical analysis of British misusage of the
American language, one poster mentioned alternate
spellings of "centre" or "center" in shopping malls as
meaningful.  I don't think shopping malls, stores, or pricey
specialty shoppes are a good source of spelling information.
A local mall calls itself "Pointe West."  (I suppose our
British friends would have this as "Full Stoppe West.")  


Ross
http://www.geocities.com/ross_klatte/
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-09T18:37:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B226D8A.7E64C3ED@home.com>`
- **References:** `<3B21CA97.568D05DF@Azonic.co.nz> <20010609062551.11353.00000544@ng-ce1.aol.com>`

```


Ross Klatte wrote:

>
> Personally, I like the recent introduction of the term "dot" for the
…[4 more quoted lines elided]…
>

Dunno - but 'decimal point' for the last one <G> Having visited Canada in
'74 and returned home, a business acquaintance sent me a letter. The little
lass who typed it, assumed it made far more sense to address it, "Creech
Street Michael, Taunton', rather than "Creech St. Michael, Taunton".

>
> Drifting off topic for this newsgroup, which is supposed to
…[7 more quoted lines elided]…
>

Hey the Centre/Center bit ISN'T the retailers - it's the City's road sign
department !

Or you could say General Douglas McArthur did his cadet training at West
Full Stop <G>
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-10T07:51:40+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2318FC.A48AFE0F@Azonic.co.nz>`
- **References:** `<3B21CA97.568D05DF@Azonic.co.nz> <20010609062551.11353.00000544@ng-ce1.aol.com>`

```
Ross Klatte wrote:
> 
> >So, perhaps it is 'the period of the pause'.  

> 
> What do the British call the dots in St. Ives, or Mr. Ed,
> or N. Ireland, or 3.14, or...?

Well they certainly are not 'periods', or 'full stops', in the sense of
creating a pause.
 
> Drifting off topic for this newsgroup, which is supposed to
> be limited to critical analysis of British misusage of the
> American language, one poster mentioned alternate
> spellings of "centre" or "center" in shopping malls as
> meaningful.  

Here in the antipodes we officially don't really care which spelling is
used.  I myself will use alternates as I see fit.  If a particular place
is called 'center', or 'centre' then that is its name and that is how it
should be spelt.  It can use 'sentre' if it chooses.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** chammond@lc.cc.il.us
- **Date:** 2001-06-08T15:44:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fqrsi$84k$1@news.netmar.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz>`

```
In article <3B20F627.67F31F81@Azonic.co.nz>, Richard Plinston 
<riplin@Azonic.co.nz> writes:
>James J. Gavan wrote:
>
…[4 more quoted lines elided]…
>
My manual from IBM uses the term Period.

However I can not seem to locate the term "FULL STOP" anywhere in my IBM COBOL
manual.

The definition in my IBM manual of a "STATEMENT" says it is one or more
commands ending with a separator period.

I don't know where the term "FULL STOP" originates is it in the COBOL
Standard?

Where does the term originate?

COBOL is suppose to be a language that is readable.  In other words, if it is
readable you would end any command just like a sentence with a period.

 -----  Posted via NewsOne.Net: Free (anonymous) Usenet News via the Web  -----
  http://newsone.net/ -- Free reading and anonymous posting to 60,000+ groups
   NewsOne.Net prohibits users from posting spam.  If this or other posts
made through NewsOne.Net violate posting guidelines, email abuse@newsone.net
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-09T07:57:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B21C8C1.47898F95@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <9fj83e$g45$1@slb7.atl.mindspring.net> <3b1d84f1_1@news1.prserv.net> <3B1DA0AC.CD375D35@home.com> <3B20F627.67F31F81@Azonic.co.nz> <9fqrsi$84k$1@news.netmar.com>`

```
chammond@lc.cc.il.us wrote:

> COBOL is suppose to be a language that is readable.  In other words, if it is
> readable you would end any command just like a sentence with a period.

Do you mean like this: ?

  	ADD 1 TO LINE-COUNT.
        IF LINE-COUNT GREATER THAN 55
        THEN MOVE PAGE-END-TEXT TO PRINT-LINE.
             WRITE PRINT-LINE BEFORE PAGE.
             MOVE 1 TO LINE-COUNT.
             MOVE PAGE-HEAD TO PRINT-LINE.
             etc

What you probably mean is that you would 'end any command [sic] .. with
a period (full-stop)' except in conditions where this wouldn't work.

The use of the full-stop in Cobol is flawed.  It was intended to make
the language more English-like, but unlike the use of the semi-colon in
C as a statement separator, it also is used as a means of terminating
blocks of code, such as in the IF statement.  In C blocks are surrounded
by curly braces {}, in Pascal they use BEGIN .. END (but the language is
broken too because the semi-colon is statement a terminator not a
separator).

Because the full-stop terminates the conditional statement it means that
the rules of use should vary depending on whether it is in a conditional
or out of it.  If it becomes necessary to change some code, or copy it,
to be under the control of an IF then all the full-stops must be
removed, conversely if the IF can be removed then you add all the
full-stops back.

This always seemed to me to in the class of: 'if you don't know what you
are doing then do it neatly'.

If the English sentence structure had been done properly in the first
place there would be mechanisms to indicate blocks of code as is done
with BEGIN .. END in Pascal.  I will call these blocks 'paragraphs' and
what is now paragraphs should be called 'chapters', with chapter
headings (labels).  Paragraph ends are indicated by blank lines. Then we
would have the much more English like:

  	ADD 1 TO LINE-COUNT.

        IF LINE-COUNT GREATER THAN 55 THEN MOVE PAGE-END-TEXT 
        TO PRINT-LINE. WRITE PRINT-LINE BEFORE PAGE. MOVE 1 
        TO LINE-COUNT. MOVE PAGE-HEAD TO PRINT-LINE. WRITE 
        PRINT-LINE BEFORE 1.
                                          < end of IF 'paragraph'
        WRITE DATA-LINE FROM PRINT-LINE BEFORE 1.

This doesn't make it more readable to me, how about you ?
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "Tom McFarland" <tmcfarland@uturn.home.com>
- **Date:** 2001-06-07T03:50:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dSCT6.212283$K5.21835470@news1.rdc1.nj.home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net>`

```

"Howard Brazee" <howard@brazee.net <mailto:howard@brazee.net>> wrote in
message
<news:3B1CE496.764D90AE@brazee.net>...
>
snip
> While it probably is a bug, it is valid CoBOL code. Certainly it is a
bad idea
> to stop using full stop periods and continue to use NEXT SENTENCE. Since
I use a
> pre-compiler which automatically inserts NEXT SENTENCE in its IDMS
commands, I am
> not even tempted to remove periods from my coding style.
>
snip

Howard,

While I only lurk here occasionally, I've seen you make this statement
before
about the IDMS pre-compiler. I've never seen the IDMS precompiler insert
NEXT SENTENCE (or even CONTINUE) in the code generated for the calls. Can
you provide an example? What versions of IDMS & COBOL are you using?
Batch/DC/CICS?

I've been period-less (except for ending paragraphs) for several years in
many IDMS shops without incident.

Tom McFarland
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-07T07:25:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1F80D1.3E6E6828@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <dSCT6.212283$K5.21835470@news1.rdc1.nj.home.com>`

```


Tom McFarland wrote:

> "Howard Brazee" <howard@brazee.net <mailto:howard@brazee.net>> wrote in
> message
…[23 more quoted lines elided]…
> many IDMS shops without incident.

I just checked - all of my supplied NEXT SENTENCE are in IDMS COPY
statements.  These could easily be fixed.
But the precompiler still does create IF logic without END-IF.  I suppose it
is possible to understand what the generated statements will be sufficiently
to put the correct number of END-IF statements after an IDMS command, but it
makes it easier for a new maintenance programmer to see a full stop period.

Illustrating for non IDMS programmers:
Source code:
****** HJBDEBUG START
     OBTAIN CALC IABRCAA
         ON ANY-ERROR-STATUS
             DISPLAY 'SKIPPING ' FINDER-ID ' NOT FOUND'    (yes, I know this
doesn't make sense)
     IF IABRCAA-IABRCBD EMPTY
         DISPLAY 'IABRCAA-EMPTY'
****** HJBDEBUG END

Generated code:
****** HJBDEBUG START
*    OBTAIN CALC IABRCAA
*        ON ANY-ERROR-STATUS
           MOVE 8 TO DML-SEQUENCE
           CALL 'IDMS' USING SUBSCHEMA-CTRL
                   IDBMSCOM (32)
                   SR1406
                   IDBMSCOM (43)
           IF NOT ANY-ERROR-STATUS PERFORM IDMS-STATUS;
           ELSE
             DISPLAY 'SKIPPING ' FINDER-ID ' NOT FOUND'
*    IF IABRCAA-IABRCBD EMPTY
           MOVE 9 TO DML-SEQUENCE
           CALL 'IDMS' USING SUBSCHEMA-CTRL
                   IDBMSCOM (64)
                   IABRCAA-IABRCBD;
           IF ERROR-STATUS EQUAL TO '0000'
         DISPLAY 'IABRCAA-EMPTY'
****** HJBDEBUG END

Obviously, the lack of generated END-IFs mean that this above code isn't what
was wanted.

We could change shop standards so that the status checking isn't implicit - If
you're using periodless code, your standards have to proscribe the use of
AUTOSTATUS and ON statements.

The use of full stop periods though mean the commands will work no matter what
standards are applied.  That is a big advantage, where I haven't seen any
particular advantage to leaving periods out.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavab@home.com>
- **Date:** 2001-06-07T16:08:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B1FA7A9.FF0616D4@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <dSCT6.212283$K5.21835470@news1.rdc1.nj.home.com> <3B1F80D1.3E6E6828@brazee.net>`

```


Howard Brazee wrote:

>
> The use of full stop periods though mean the commands will work no matter what
> standards are applied.  That is a big advantage, where I haven't seen any
> particular advantage to leaving periods out.

Hey that's neat. As a result of Lynn's monthly cycles have we now coined a new
Anglo/American programming phrase :-

            full stop period        <G>

Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "Tom McFarland" <tmcfarland@uturn.home.com>
- **Date:** 2001-06-08T02:24:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tHWT6.217495$K5.22413975@news1.rdc1.nj.home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <dSCT6.212283$K5.21835470@news1.rdc1.nj.home.com> <3B1F80D1.3E6E6828@brazee.net>`

```

Howard Brazee <howard@brazee.net> wrote in message
news:3B1F80D1.3E6E6828@brazee.net...
>
>
…[9 more quoted lines elided]…
> > > to stop using full stop periods and continue to use NEXT SENTENCE.
Since
> > I use a
> > > pre-compiler which automatically inserts NEXT SENTENCE in its IDMS
…[10 more quoted lines elided]…
> > NEXT SENTENCE (or even CONTINUE) in the code generated for the calls.
Can
> > you provide an example? What versions of IDMS & COBOL are you using?
> > Batch/DC/CICS?
> >
> > I've been period-less (except for ending paragraphs) for several years
in
> > many IDMS shops without incident.
>
> I just checked - all of my supplied NEXT SENTENCE are in IDMS COPY
> statements.  These could easily be fixed.
> But the precompiler still does create IF logic without END-IF.  I suppose
it
> is possible to understand what the generated statements will be
sufficiently
> to put the correct number of END-IF statements after an IDMS command, but
it
> makes it easier for a new maintenance programmer to see a full stop
period.

There is no mystery as to the number of END-IFs that would be required to
terminate the IDMS ON.  It's 1.  If any more are required, it's because
there is/are additional programmer coded IFs subordinate to the ON.

The precompiler never inserts terminating logic for the generated IF-ELSE
statement.  It uses whatever you use to terminate the IDMS ON statement.  So
if you terminate it with an END-IF, that's what you'll get.  If you
terminate with a period, you'll get a period.

code this:
OBTAIN CALC CUSTOMER-RECORD
ON DB-REC-NOT-FOUND
    imperative statement
END-IF

and you will get:
* OBTAIN CALC CUSTOMER-RECORD
* ON DB-REC-NOT-FOUND
   CALL 'IDMS' USING etc
   IF NOT DB-REC-NOT-FOUND   ----generated
         PERFORM IDMS-STATUS     ---generated
   ELSE                                               ---generated
        imperative statement                    ---your code
   END-IF                                           ---your code

Replace the END-IF with a period, and the resultant IF-ELSE will end with a
period.

> Illustrating for non IDMS programmers:
> Source code:
…[3 more quoted lines elided]…
>              DISPLAY 'SKIPPING ' FINDER-ID ' NOT FOUND'    (yes, I know
this
> doesn't make sense)
>      IF IABRCAA-IABRCBD EMPTY
…[24 more quoted lines elided]…
> Obviously, the lack of generated END-IFs mean that this above code isn't
what
> was wanted.

Not sure I understand your example, but if you didn't want the IDMS IF to be
subordinate to the ON, then that's just a coding error, not a compiler
unpredictability issue.

> We could change shop standards so that the status checking isn't
implicit - If
> you're using periodless code, your standards have to proscribe the use of
> AUTOSTATUS and ON statements.

Not at all.  This duscussion would be moot if we weren't assuming the use of
AUTOSTATUS.

> The use of full stop periods though mean the commands will work no matter
what
> standards are applied.  That is a big advantage, where I haven't seen any
> particular advantage to leaving periods out.

I don't wan't to get into a religious war on the use or non-use of periods,
but using them in every case to terminate your IDMS calls kind of prevents
you from coding any IDMS statements at any level you choose within a nested
IF structure.  Obviously, if you have shop standards that require you to use
copied code containing NEXT SENTENCE, your options are limited.  But it's
definitely not the pre-compiler's fault.

Tom McFarland
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-07-05T21:06:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CF417.3843$G_1.373104@newsread2.prod.itd.earthlink.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B1CF32E.8C818B5D@Azonic.co.nz> <3B1CE496.764D90AE@brazee.net> <dSCT6.212283$K5.21835470@news1.rdc1.nj.home.com>`

```
I haven't kept up with the technical stuff lately but I remember when the
CICS preprocessor added options to support Cobol II and then full ANSI 85
Cobol e.g. Cobol/370; hasn't IDMS been updated similarly to support
options to tell the IDMS preprocessor to generate nice structured current
type code as well? If not, they should certainly make that enhancement.
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-06-05T22:17:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0UcT6.126680$NK4.7929298@news2.aus1.giganews.com>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```

"Lynn Randall" <LERandall@yahoo.com>

Maybe I'm missing something, but isn't the problem you describe one of
paragraph naming?

Original:

Perform 1000-Init.
Perform 2000-Read until file-eof.
Perform 9000-Quit

2000-Read
   Read Input-file
      not at-end Perform 3000-process
      end-read.

vs.

Perform 1000-Init.
Perform 2000-Process until file-eof
Perform 9000-Quit

2000-Process.
   Perform 3000-Read
   If not file-eof
      (do some things)
   End-if.

3000-Read
   Read (etc.)

The hierarchy difference seems: Is the read subordinate to the
processing or is the processing subordinate to the read? Inasmuch as
the processing code could have many elements under its control, I
would vote for the processing code to contain the read routine as a
subset. That is, the processing drives the reading rather than the
read driving the processing. To me this makes more logical sense, but
I suppose others may differ. There are those who are opposed to hot
water.

By the way, we preface paragraph numbers with a letter (i.e.,
"P1000-"). This makes them easier to 'Find,' although I suppose, now
that I think on it, that we COULD look for "1000-". Oh well.
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2001-06-05T21:47:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fk594$4klji$1@ID-39920.news.dfncis.de>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```

Lynn Randall <LERandall@yahoo.com> wrote in message
news:3b1c3343_2@news1.prserv.net...
> I have been lurking for a bit... but now I need some input...
> At the risk of starting another religious discussion, I would like to
> solicit some opinions (the civil ones).
>
> In my job, I have the task of reviewing programs of my co-workers before
the
> programs are allowed to go to production.  My expectations are for
> efficiency, understandability, adherence to standards, and maintainability
…[3 more quoted lines elided]…
> Part of the "maintainabiliy", is creating "structured" programs.  There
has
> already been a certain amount of philosophical discussion about
"structure"
> in recent days in this newsgroup; and I don't really want to rehash all
> that.  I just would like some feedback on a couple of my "guidelines" -- I
…[5 more quoted lines elided]…
> When coding a read paragraph, is it appropriate to perform another
paragraph
> from within the Read? (Same question goes for Fetch paragraphs when
dealing
> with an SQL cursor).
>

I think that there are times when it is appropriate.  Consider the
following:

0000-MAIN.
    PERFORM 1000-INIT.
    PERFORM 2000-READ-FILE UNTIL EOF.
    PERFORM 9000-FINAL.

1000-INIT.
    ...

2000-READ-FILE.
    READ INPUT-FILE INTO INPUT-RECORD
        AT END
            SET EOF TO TRUE
        NOT AT END
            PERFORM 3000-CHECK-STATUS
    END-READ.

3000-CHECK-STATUS.
        EVALUATE INPUT-STATUS
            WHEN '00'
                CONTINUE
            WHEN
                ....     you get the picture   ..
        END-EVALUATE.

9000-FINAL.
    ...


In this example, the check file status paragraph was related to the read.
Therefore, I would consider it valid (although unnecessary)....

> For example:
>
…[25 more quoted lines elided]…
> one and only one function.  Here, 2000- performs the Read AND it drives
the
> rest of the processing.  That seems wrong to me, but one of co-workers
> showed me a textbook where this "structure" was advocated.   I've seen the
> "structure" recently (let's say the last 3 years) from various
programmers,
> whereas previously (the prior 12 years or so), NO ONE I knew coded that
way.
> Have standards changed?  In addition, I was originally taught that all
file
> I-O should be isolated in its own paragraph to ease dump-solving.  How
that
> might help is not very clear from this example; so consider if the "not at
> end" condition led to an Evaluate statement, or a series of If/Else
…[30 more quoted lines elided]…
>

This is how I would code it...

0000-MAIN.
    PERFORM 1000-INIT.
    PERFORM 2000-READ-FILE.
    PERFORM 3000-PROCESS-RECORDS UNTIL EOF.
    PERFORM 9000-FINAL.

1000-INIT.
    ...

2000-READ-FILE.
    READ INPUT-FILE INTO INPUT-RECORD
        AT END
            SET EOF TO TRUE
        NOT AT END
            check file status -- we always check our file status, don't
we????
    END-READ.

3000-PROCESS-RECORDS.
    ...
    PERFORM 2000-READ-FILE.

9000-FINAL.
    ...


> As you can see, one of my other "expectations" is that all paragraphs are
> numbered.  Judging by the posts to this newsgroup, that also seems to be
out
> of vogue.    Years ago, I would not have coded a priming read in the
> 1000-Init paragraph; but I was persuaded otherwise...
>

I tend to code the prime read in the main paragraph -- to make it stand out
a bit better.  I also use numbered paragraphs.  I don't think there is
anything wrong about not numbering the paragraphs - just my preference.  To
me, it makes the paragraph easier to find within the program.


> I might add that, where COBOL is concerned, I am purely a mainframe
> programmer (though I have some training in VB, and web stuff).  So stuff
…[3 more quoted lines elided]…
>

Oh, just as a note, the PERFORM until EOF will first check the end condition
(unless you specify WITH TEST AFTER), making the IF structure unnecessary...
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2001-06-06T03:17:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010605231759.24105.00001047@ng-ca1.aol.com>`
- **References:** `<9fk594$4klji$1@ID-39920.news.dfncis.de>`

```
While I have my own preference as to how to code a program (which has been
noted somewhere else so I won't reiterate) I really don't care as long as:

1) It does what it's supposed to do.

2) If by some chance it doesn't do what it is supposed to do at 2am I can
figure it out while still 1/2 asleep or

3) Figure it out in the morning after 1 cup of coffee.

Any program that requires 2 or more cups of coffee to be understood should be
rewritten.

Eileen
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "Lynn Randall" <LERandall@yahoo.com>
- **Date:** 2001-06-05T22:02:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b1dbbd2_1@news1.prserv.net>`
- **References:** `<9fk594$4klji$1@ID-39920.news.dfncis.de> <20010605231759.24105.00001047@ng-ca1.aol.com>`

```
<G>  I like your "standards"!...    A bit hard to define for a team of
programmers tho...  after all, what takes you and me only 1 cup of coffee to
figure out, might take a MAN several pots of coffee....

(although... given the poor quality of my original example code, I suppose
I'm not in a position to throw male-bashing stones...)

ler.

YukonMama <yukonmama@aol.com> wrote in message
news:20010605231759.24105.00001047@ng-ca1.aol.com...
> While I have my own preference as to how to code a program (which has been
> noted somewhere else so I won't reiterate) I really don't care as long as:
…[8 more quoted lines elided]…
> Any program that requires 2 or more cups of coffee to be understood should
be
> rewritten.
>
> Eileen
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-06-06T11:11:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vdoT6.570$T67.19192@dfiatx1-snr1.gtei.net>`
- **References:** `<9fk594$4klji$1@ID-39920.news.dfncis.de> <20010605231759.24105.00001047@ng-ca1.aol.com> <3b1dbbd2_1@news1.prserv.net>`

```
Lynn Randall <LERandall@yahoo.com> wrote in message
news:3b1dbbd2_1@news1.prserv.net...
> (although... given the poor quality of my original example code, I suppose
> I'm not in a position to throw male-bashing stones...)

Please do not use the words, "male", "stones" and "bashing" in the same
sentence.

MCM
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** Liam Devlin <LiammD@optonline.net>
- **Date:** 2001-06-10T23:28:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2402AC.1184B2C4@optonline.net>`
- **References:** `<9fk594$4klji$1@ID-39920.news.dfncis.de> <20010605231759.24105.00001047@ng-ca1.aol.com> <3b1dbbd2_1@news1.prserv.net> <vdoT6.570$T67.19192@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> Lynn Randall <LERandall@yahoo.com> wrote in message
…[7 more quoted lines elided]…
> MCM

Right! <shudder>
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** chammond@lc.cc.il.us
- **Date:** 2001-06-06T19:24:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fm00n$ch5$1@news.netmar.com>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```
In article <3b1c3343_2@news1.prserv.net>, Lynn Randall <LERandall@yahoo.com>
writes:
>I have been lurking for a bit... but now I need some input...
>At the risk of starting another religious discussion, I would like to
…[99 more quoted lines elided]…
>


 -----  Posted via NewsOne.Net: Free (anonymous) Usenet News via the Web  -----
  http://newsone.net/ -- Free reading and anonymous posting to 60,000+ groups
   NewsOne.Net prohibits users from posting spam.  If this or other posts
made through NewsOne.Net violate posting guidelines, email abuse@newsone.net
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** chammond@lc.cc.il.us
- **Date:** 2001-06-06T19:59:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fm23e$e4i$1@news.netmar.com>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```
In article <3b1c3343_2@news1.prserv.net>, Lynn Randall <LERandall@yahoo.com>
writes:
>I have been lurking for a bit... but now I need some input...
>At the risk of starting another religious discussion, I would like to
>solicit some opinions (the civil ones).
>
You have to decide what you want to see or adhered to.  At the risk of making
you go ballistic maybe you should have an open meeting and discuss your
standards.  Either that, or send everyone what you think is wrong or what
your key points are and solicit feedback.   Then you can discuss why you
think the way you do.  If I was told I couldn't do something a certain way I
would be asking for some kind of SOP or training manual or an example book or
something. You could take the program in question and rewrite it the way you
think it should be written and then use it as an example for a training
session.  You can not enforce a standard you have not established and train
the programmers to adhere to.  The standard has to be established before it
can be enforced.



 -----  Posted via NewsOne.Net: Free (anonymous) Usenet News via the Web  -----
  http://newsone.net/ -- Free reading and anonymous posting to 60,000+ groups
   NewsOne.Net prohibits users from posting spam.  If this or other posts
made through NewsOne.Net violate posting guidelines, email abuse@newsone.net
```

#### ↳ Re: More Structure.. Perform from Read

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-10T12:55:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106101155.1441bc5a@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net>`

```
"Lynn Randall" <LERandall@yahoo.com> wrote in message > Here is the current issue...
> 
> When coding a read paragraph, is it appropriate to perform another paragraph
…[27 more quoted lines elided]…
> 


This is essentially the way I would do it, with one serious exception.

NOT AT END works ONLY if there is a successful READ. Unless you are
using DECLARATIVES (which are absolutely non-structured), there is no
provision for error-recovery.  Testing the file status (even for
sequential files) provides for more structured code.
Additionally, there is the issue that use of AT END ... NOT AT END
makes  the processing subordinate to the READ, which bothered a number
of people  conceptually (including Ms Randall), particularly the OO
programmers.  Using file statuses makes the syntax agree with concept.

    2000-READ-AND-PROCESS.
        READ INPUT FILE INTO WS-INPUT-FILE.
   *           (this is the first "process" at this level.  There is 
   *            no need 
   *            to perform a paragraph containing only one statement.
   *            This single statement would be diagrammed as a
"module"
   *            just as much as a performed routine.)
   *           (Note that if the sequential READ were to be changed to
   *            a different kind of access, this single statement
could
   *            easily be replaced with a different sentence or even a
   *            PERFORM statement.)

        EVALUATE INPUT-FILE-STATUS
           WHEN '00'
               PERFORM 3000-PROCESS-RECORDS
                  THRU 3000-EXIT
            WHEN '10'
   *             (at end)  
               CONTINUE
            WHEN OTHER
               go to or perform exception/abend processing
        END-EVALUATE.  
   *           (this is the second "process" at this level.  The 
   *            CONTINUE will fall thru to the paragraph end or 
   *            an explicit EXIT.)
   *           (Note that if the sequential READ were to be changed 
   *            to a  different kind of access, structure still 
   *            contains the complete processing logic, even tho 
   *            the codes may have to be changed.)

*-------------------- related rant ---------------------

   CONTINUE could be replaced by EXIT-PARAGRAPH in those compilers
which have already implemented this "feature".  DON'T DO IT! 
EXIT-PARAGRAPH, EXIT-SECTION and EXIT-PERFORM-CYCLE are ALL disguised
GO TO's!  BAD! BAD! BAD!   Write to J4 (and/or your National Body) and
tell them to get rid of these abominations before they get into the
new official standard!

*-------------------- END-RANT ---------------------

Stephen J Spiro
Wizard Systems

PS: HEY! YOU could be on the J4 Committee and help our language!
E-mail me!
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-10T21:16:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B23E468.BB9968BA@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com>`

```


Stephen J Spiro wrote:

> This is essentially the way I would do it, with one serious exception.
>
> NOT AT END works ONLY if there is a successful READ. Unless you are
> using DECLARATIVES (which are absolutely non-structured), there is no

Well I agree with you about the DECLARATIVES - but watch it ! Bill is big fan of
Declaratives <G>. As regards the intended list of Exception Conditions (120 plus ?) -
no comment. I'll await their arrival, and when I've coded - then make comment.

>
> provision for error-recovery.  Testing the file status (even for
…[4 more quoted lines elided]…
> programmers.  Using file statuses makes the syntax agree with concept.

As regards OO - how about a 'belt and braces approach' :-

*>--------------------------------------------------------------
Method-ID. "access-file".
*>--------------------------------------------------------------
input-output section.
copy "clients1.cpy" replacing ==(tag)== by ==Data==.

File Section.
FD  Data-File.
01  Data-record.
copy "clients2.cpy" replacing ==(tag)== by ==Data==.

Linkage Section.
copy "fileactn.cpy".
01 lnk-PrimeKey                          pic x(06).
01 lnk-result                            pic x(4) comp-5.

Procedure Division Using     file-action
                             lnk-PrimeKey
                   returning lnk-result.

   set file-result-ok to true
   initialize ws-Error-Data

   Evaluate TRUE

     When read-PrimeKey
      move lnk-PrimeKey to Data-PrimeKey
      Read Data-File
        Invalid key
          Set record-not-found to True
        Not invalid key
          Move Data-record to os-record
      End-Read

     When read-next
          .......
     When start-PrimeKey
          ........
     When etc.......
          ......
    When other
      invoke super "invalid-action" using file-action
      set file-error to true

   End-evaluate

   if ws-filestatus <> "00"
      move os-PrimeKey  to ws-error-key
      move os-Shortname to ws-error-name
      invoke super "check-file-status"
             using     ws-ErrorFields
                       file-action
                       ws-file-result
             returning lnk-result

   else move ws-file-result to lnk-result
   End-if
End Method "access-file".
*>--------------------------------------------------------------

The above is old code, and thanks to my good friend Mr. Hubbell , inclusion of file
definition in methods is now a No-No ! Same applies to Declaratives. (But Thane's
reasoning was sound).

Reviewing that code above I would now break it out into separate methods per type of
file access; then I can zero-in more closely on the file-status associated with the
particular file VERB. I think you could interpret the phrase "break it out into separate
methods" as being the non-OO parlance, 'more structured'.

Jimmy
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-11T07:05:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B24C21A.82661AB0@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com>`

```


Stephen J Spiro wrote:


> This is essentially the way I would do it, with one serious exception.

>
> NOT AT END works ONLY if there is a successful READ. Unless you are
…[6 more quoted lines elided]…
> programmers.  Using file statuses makes the syntax agree with concept.

Good point - but this is a flaw in our CoBOL.  CoBOL should have English language
commands which do everything that status code checking does.  The spirit of CoBOL is
that a non-programmer should be able to read what it does.  Status codes are cryptic and
require expertise to read.  (not much expertise, but nevertheless it is not English).

> *-------------------- related rant ---------------------
>
…[7 more quoted lines elided]…
> *-------------------- END-RANT ---------------------

EXIT-PARAGRAPH will be used to replace GO TO XXXX-EXIT.   When this is adopted, more
sites will adjust their standards to proscribe PERFORM THRU statements.   This will be a
good thing.     They aren't letting go of their GO TO xxxx-EXIT statements yet.

The hard thing though is the line "When this is adopted".  Lots of sites were using
ANSI-68 code until they were forced to upgrade to handle the century changes.  They
might not feel a need to spend money to upgrade compilers at all.
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-11T16:00:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B24DD1C.4E6C5874@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com>`

```
Stephen J Spiro wrote:
> 
>     2000-READ-AND-PROCESS.
…[4 more quoted lines elided]…
>                   THRU 3000-EXIT

Just one tiny criticism.  They may be (in fact are) cases were a valid
[sic] read returns a status that is not '00'.  For example an indexed
file with a duplicate key being read sequentially may give a status of
'02' to indicate that the next record has the same key.

It is important to only check the first byte for being zero as a means
of detecting successful reads.

> *-------------------- related rant ---------------------
> 
…[7 more quoted lines elided]…
> *-------------------- END-RANT ---------------------

I quite agree.  

However, you used an example of:

>                PERFORM 3000-PROCESS-RECORDS
>                   THRU 3000-EXIT

Now the _only_ point of doing a PERFORM THRU (or a PERFORM SECTION) is
to allow for using GO TOs (explanation available upon request), so I
don't know if your objection to EXIT-something is because it is a GO TO
or because it is disguised.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-11T05:19:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B245565.E295C93B@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B24DD1C.4E6C5874@Azonic.co.nz>`

```


Richard Plinston wrote:

For Stephen - not you  Richard <G>

> > *-------------------- related rant ---------------------
> >
…[8 more quoted lines elided]…
>

I only read your 'rant' in detail as a result of Richard's message. Might be
the case in non-OO, but for OO I would say you are out to lunch <G>

Given that a method is a 'mini-program' - I regularly use EXIT PERFORM and
my equivalent of your EXIT PARAGRAPH/EXIT SECTION is the OO EXIT METHOD. .

Again OO-wise, why loop through a Perform if you can jump out immediately on
a given condition. Same with the EXIT METHOD.

EXIT METHOD and EXIT PERFORM (depending on how you have coded for the
latter),  get you directly to END METHOD - and you are out of there !
(Thane's on record - he LUVS the Exit Method).

Stephen, as and when UDFs(User Defined Functions) become available with
mainframe compilers - would you still contend your No-No approach is valid ?

I'm only aware of UDFs in passing as they have no application to me in OO -
but I would have thought EXIT PERFORM was just as valid. I'm pretty sure
there isn't an EXIT FUNCTION - might have been a nice feature.

PS:

Did search CD 1.10 to try and confirm about the UDF format, but gave up in
frustration  - I know you guys are used to it, but how I hate that document
when attempting to zero-in on something - and that crappy Acrobat 'Search
Box" rather than a simple F3 (forward) or F4(backwards) to repeat the
search. I suppose, other than currently conforming to ISO format, the actual
document presentation has existed since time immemorial. I just think
somebody should hand this one over to a bunch of technical writers with NO
PROGRAMMING experience and get their reactions.

Of course, I could make EXACTLY  the same comments about Vendors' on-line
help - i.e. use a bunch of computer illiterates and you might just finish up
with something that is literate !

(Don't use WMK - he's already 'confessed' to performing as a technical
writer - but with prior computer knowledge <G>)

Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-12T10:21:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106120921.5e33ab0c@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B24DD1C.4E6C5874@Azonic.co.nz> <3B245565.E295C93B@home.com>`

```
Jimmy,

If you download the PDF instead of opening it in your browser, and
then open it with Acrobat - the F3 works to continue the search.

I have no comments on the other topics except to say that the
likelyhood of removing features at this late date (especially as the
country vote was virtually unanimous in favor of the draft -- one
abstention) is zero.

"James J. Gavan" <jjgavan@home.com> wrote in message news:<3B245565.E295C93B@home.com>...
> Richard Plinston wrote:
> 
…[52 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-11T07:15:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B24C461.A75C0CAC@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B24DD1C.4E6C5874@Azonic.co.nz>`

```


Richard Plinston wrote:

> Stephen J Spiro wrote:
> >
…[13 more quoted lines elided]…
> of detecting successful reads.

I was maintaining a purchased system where our I/O would call a program
which called a program.   The called program would return a '7' when the
VSAM file failed to open.  I pulled down that program and found out '7' was
"not '00'".   Rerunning the job would work correctly.  I traced down this
intermittent problem to find out that VSAM returned a '97', which means OPEN
statement execution successful: File integrity verified.   Since this
program gets called by everybody and his brother, making this minor fix
would mean significant testing and signing off, giving operators
instructions to restart, or adding a verify step before the program.   This
system had the worst features of OO without the benefits.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-11T17:01:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g3f46$c36$1@slb0.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B24DD1C.4E6C5874@Azonic.co.nz> <3B24C461.A75C0CAC@brazee.net>`

```
Howard,
  The "issue" of IBM's use of VSAM files returning a file-status code of
"97" when a "verify" is required (and done by the IBM COBOL run-time itself)
is a "little" interesting (and has some discussion).

In (at least one) theory, IBM is "non-conforming" by using a "9x" file
status code for something that they (themselves) call a "successful" I/O
statement.  On the other hand, the "behavior" after all 9x codes is
"implementor defined" - so they can (and at a HIGHLY theoretical level have)
said that this really is an "unsuccessful" I/O statement that results in
processing "as if" it were successful.

Much of this MAY go away in the future, when the new draft Standard allows
for "0x" file status codes indicating implementor defined SUCCESSFUL
conditions.  Also (as I recall) the "newer" COBOL (IBM COBOL for
this-and-that) *tend* to issue  "97" less often than you used to get with
OS/VS COBOL.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-11T10:22:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106110922.5bc4b9b4@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B24DD1C.4E6C5874@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<3B24DD1C.4E6C5874@Azonic.co.nz>...
> Stephen J Spiro wrote:
> > 
…[13 more quoted lines elided]…
> of detecting successful reads.

**-----------------------
Very easy to say 
               WHEN '00' OR '02'
Some of the '9x' (user-defined) codes may be  OK, as well.
Additionally, one or more '0x' codes may be unacceptable in a
particular, programmer-defined case.  Thus, I prefer testing for all
applicable codes, in full.

**-----------------------


> 
> > *-------------------- related rant ---------------------
…[20 more quoted lines elided]…
> or because it is disguised.

*LOL* NEVER say the ONLY reason for doing something is "xxx"!
In the Old, Original COBOL, you performed a paragraph THRU a parahraph
and a section THRU a section.  I got in the habit a long time ago. 
When I started programming, many people (myself included) performed
multiple paragraph groups, and an EXIT paragraph was a nice, clean way
to show the end of the performed group, even if there was only one
paragraph, or even if you did not use GO TO. At this point, I do not
use GO TO, and I never perform more than one paragraph at a time. 
Using the EXIT is just a habit, now.  I suppose I should change my
style, it doesn't accomplish anything, altho I like to think it makes
the code neater.

Yes, my objection to EXIT-PARAGRAPH, EXIT-SECTION and
EXIT-PERFORM-CYCLE are because they are GO TO's .... AND because they
are disguised.

Stephen J Spiro
Member, J4 COBOL Standards committee

PS: YOU (all of you!) could join the standards committee and make a
difference!
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-11T12:21:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B250C2C.9FDB0BFB@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B24DD1C.4E6C5874@Azonic.co.nz> <4145699b.0106110922.5bc4b9b4@posting.google.com>`

```
Stephen J Spiro wrote:

> *LOL* NEVER say the ONLY reason for doing something is "xxx"!
> In the Old, Original COBOL, you performed a paragraph THRU a parahraph
> and a section THRU a section.

I have never seen a section THRU a section.  In my early days paragraph THRU paragraph was rare in
my experience, becoming real common in the late 1970s, and early 1980s.


> Yes, my objection to EXIT-PARAGRAPH, EXIT-SECTION and
> EXIT-PERFORM-CYCLE are because they are GO TO's .... AND because they
> are disguised.

Please continue.  The reason I object to GO TO's is because they allow for drop through code to new
paragraphs.  Since this isn't the case here, your objection must lie elsewhere.  Why do you object
to GO TO's in this case?
```

##### ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2001-06-11T14:48:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B252083.ECA4ECCB@mb.sympatico.ca>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com>`

```
Stephen J. Spiro wrote

>    CONTINUE could be replaced by EXIT-PARAGRAPH in those compilers
> which have already implemented this "feature".  DON'T DO IT!
…[5 more quoted lines elided]…
> *-------------------- END-RANT ---------------------

You're treading on very dangerous ground here, friend.

ANY kind of verb that redirects program flow is a go to!!!  Whether it is expressed in
that way or not, every such verb represents the concept: the program is executing a
statement HERE but is going to remove itself to executing a statement THERE.  Even a
PERFORM 100 TIMES  has an implied but explicit transfer of execution back to the top of
the perform.  Just because it doesn't say GO TO doesn't mean it doesn't do it.  Try
writing a program as one long set of statements , top to bottom with no deviations, and
you'll have to agree that you can't avoid control transfers.  QED.

At the risk of seeming archaic, stubborn, out of it, etc., (insert your own adjective),
I strongly question your use of the word "Abominations".  Consider a program:

IF A = B
...
500 lines of code with enough conditions and if's to make it interesting
...
END-IF.

I've had to maintain enough of such code to have decided opinions on its worthiness.  To
locate that terminal END-IF (especially considering the no-comment no-paragraph style of
prgramming so popular these days) I've been reduced to printing the program with an
indented listing and then taking a ruler to it; or using an editor (with indented code)
and finding an END-IF in the same column as the starting IF.  Then I always had to
examine the listing or screen very carefully to convince myself that I had it right.

Now consider the same program coded with a GOTO:

IF A = B NEXT SENTENCE
    ELSE GO TO 110-NEXT.

(coded that way as some people get disturbed at a NOT in an IF)
...
500 lines of code with enough conditions and if's to make it interesting
...
(.) Terminal period.

110-NEXT.

Elapsed time to find the "end of the IF" - about ten seconds.  Utterly unambiguous.
Simple as spilling one's tea.

How is it, then, that the first method of programming is so much better?  Why is the
first one supposed to be easier to understand?  Is it a question of better control of
one's facial muscles?  Is ambiguity preferable?  Is it because programs with GOTO's can
be a horrible mess?  (If so, then better eliminate GOTO-less programs too, because you
can get horrible messes without GOTO's!  There is a thread still open that displays an
absolutely monstrous use of EVALUATE).

The GOTO argument has been "going" on for over 25 years now.  That fact alone should be
sufficient argument that there is equal merit to both sides.

With all possible respect, people who insist that such and such verbs must be removed
from the compiler are as stubborn and hidebound as those who use GOTOs and create
reliable, easy-to-maintain code.

End of MY rant.
```

###### ↳ ↳ ↳ GO TO and draft Standard (was: More Structure.. Perform from Read

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-11T17:10:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g3fkf$nmf$1@slb7.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca>`

```
FYI - one national Standards body (the Netherlands) *has* specifically
requested that GO TO be placed in the "archaic" (*not* OBSOLETE) category in
this revision of the Standard.

I have NOT seen how J4 "processed" this request and NOTHING will be final on
it until the WG4 meeting in November.  HOWEVER, from past "discussion" my
GUESS is that this will be "rejected".

If you have an opinion on whether GO TO should or should not be made
"archaic," then I think you MIGHT want to send a note to the J4 Chair asking
for you "input" to be considered on this topic.  He can be reached
electronically at:

    doncobol <at> mediaone.net

Just so there is no confusion, the following are what the terms "archaic"
and "obsolete" mean in the draft Standard.

E.1 Archaic language elements

The purpose of the archaic language element designation is to discourage the
use in new programs of some features that are unreliable, poor programming
practice, or ill-defined -- where better programming techniques are
available in standard COBOL. These elements are classified as archaic rather
than obsolete because their use in existing programs is too extensive to
warrant removal in the next revision of standard COBOL.

Archaic language elements are intended to remain in the next revision of
standard COBOL. There is no plan for the removal of archaic elements;
however, should their use in program inventories become insignificant, they
may be considered for designation as obsolete by future architects of
standard COBOL."

     ***

E.2 Obsolete language elements

Obsolete language elements are elements that will be removed in the next
edition of this draft International Standard because those elements no
longer needed or are rarely used. To limit the impact of removal, those
elements are designated as obsolete to serve as a notice of the intention to
remove them.

No elements will be removed from any future edition of this draft
International Standard without first having been designated as obsolete
language elements in the preceding edition.

Obsolete language elements have not been enhanced nor modified in this draft
International Standard and will not be maintained. The interaction between
obsolete language elements and other language elements is undefined unless
otherwise specified in this draft International Standard.

A conforming implementation is required to support obsolete language
elements except for elements that are also optional or processor-dependent."
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-11T18:51:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106111751.58cf6bb8@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<9g3fkf$nmf$1@slb7.atl.mindspring.net>...
> FYI - one national Standards body (the Netherlands) *has* specifically
> requested that GO TO be placed in the "archaic" (*not* OBSOLETE) category in
…[11 more quoted lines elided]…
>     doncobol <at> mediaone.net


<snip>

Unless they did it the day I slept late, Netherlands comments have not
yet been processed.  We hope to finish the international comments in
Portland, Ore at the beginning of August.
I, personally, also requested that GO TO be made "archaic", in one of
MY public review comments.  My proposal was rejected by a vote of 8 to
1.  If Netherlands lobbies hard for it, it could still be done at the
next WG4 meeting.

Stephen J Spiro
Member, J4 COBOL Standards Committee

PS: Still a lot of work left, ALL OF YOU could join J4 and make a
difference!
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-12T02:33:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B257FEC.D95F904A@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com>`

```


> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<9g3fkf$nmf$1@slb7.atl.mindspring.net>...
> > FYI - one national Standards body (the Netherlands) *has* specifically
…[11 more quoted lines elided]…
>

"Bewitched, bothered and bewildered, am I" - Pal Joey - Richard Rodgers & Lorenz Hart..

So how long does this malarkey go on with the Standards, a bouncing ball between ANSI/J4 and ISO ?

Wont hold you to it Bill, and you can be speculative - but just so we can get some handle on this schmozzle. Assuming
a proposed deadline of December 2002 - care to show some milestones (Month and Year) what happens from here on in
until December 2002

Jimmy
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-11T22:30:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106112130.47a37099@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote > 
> So how long does this malarkey go on with the Standards, a bouncing ball between ANSI/J4 and ISO ?
> 
…[4 more quoted lines elided]…
> Jimmy

"Official" schedule:

Last WG4 Convener's schedule:
http://www.ncits.org/tc_home/j4htm/m226/00-0424.doc

WG4 Homepage Schedule:
http://anubis.dkuug.dk/jtc1/sc22/wg4/open/projects#milestones

Jimmy, this a bleeding _ISO_ committee! You didn't think there would
be SCHEDULES? *L*

Stephen J Spiro
Member, J4 COBOL Standards Committee

PS: All of you could join the J4 standards committee and help us keep
this schedule, or make a better standard!
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-12T19:54:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B26741F.FF743898@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com>`

```


Stephen J Spiro wrote:

> "James J. Gavan" <jjgavan@home.com> wrote >
> > So how long does this malarkey go on with the Standards, a bouncing ball between ANSI/J4 and ISO ?
…[17 more quoted lines elided]…
>

May I remind you sir, you are a Yank. You may NOT arbitrarily use Brit colloquialisms, "Bleeding.........." indeed ! <G>
Well, I'll concede I'd let WMK do it 'cos he's a bit 'TransAtlantic' .

OK so you had a good laugh. So would I, but the Brit expression is, "Not funny ha ha, but funny peculiar (pathetic)".
Thanks for the references and I took a look see - one is a bit out of date, but the other is informative. Just let's hope
in the screwing around it doesn't cause a delay. Seems funny to me - you've already been through the process with the CD
1.10 comments. Agreed you've got to fine tune based on those comments - but to drag it out from today until December 2002 ?
Even that warns with a caveat - not necessarily, but could become xxx 2003 ?

What's with the ISO bit, you J4, ARE (A)merican NSI, though you do speak as a group with divers tounges and accents. Bottom
line, and translate to nice diplomatic-ese as you wish.:-

"Look you jerks running ANSI/ISO, there are over 3 million people world wide who make their bread, either designing COBOL
compilers or developing applications using COBOL. We have a concrete 40 year track record of success.

You #4@##! people are screwing us around with your hidebound bureaucratic procedures. If you wont acknowledge our concerns,
when we want to quickly and easily introduce changes to OUR COBOL community language, we will do our 'own thing' and you
can stick your respective bureaucracies where the sun don't shine !"

PS: Reference "divers dialects above." From my wife. Mind you she has to choose her customers carefully, they don't all
necessarily have a sense of humour. She works part-time at a retail cash desk for pin money and to keep herself active :-

Customer says pleasantly, "I love your English accent". "Accent ?", replies my Eileen, sweetly. "I don't have an accent.
It's you colonials who have an accent !".
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-12T19:03:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g6ak0$vvr$1@slb7.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com>`

```
The "coordination" between ANSI (J4 & NCITS) and ISO (WG4 & SC22) is WELL
defined at this stage.  If anyone (myself included) wanted to change this
now, it would definitely be CONTROVERSIAL - and probably would result in
delays.

The steps (from the FCD review on) - but without dates are:

A) International FCD review starts (4 month review)
B) US does a two-month public review
C) J4 TAG determines which US public review comments get forwarded to the
international review process.
B1-C1 "similar" actions occur in other countries who do whatever they want
to determine and then submit their national comments
D) International review period on FCD ends
  >>>   (we are here)
E) J4 (as subcontractor to WG4) drafts responses to ALL internationally
submitted comments (this includes the US comments that were submitted
internationally - but NOT all the original US Public review comments)
F) WG4 has a meeting to "process" the J4 recommendations on international
comments.  This usually involves at least a "little" tweaking but MIGHT be a
total reversal - or a "rubber stamp".  I have NO way to project what will
happen
G) AFTER WG4 "reconciliation" of comments, their "official" response is
forwarded back up to SC22 for sending back to all national standards bodies
(including ANSI).
H) Assuming no country changes from "yes with comments" or "yes" to "NO" on
the basis of these responses,
I) J4 develops proposals to "implement" the responses sent to all the
countries (when some changes were required).  Actually, work has already
begun on these "tentative" proposals but they ABSOLUTELY are not applied to
the FCD document until AFTER the (Nov 2001) WG4 meeting.
I1 - J4 actually creates and sends out all of the replies to the US FCD
public review comments.  They are delayed until this time - in case WG4
direction makes some of the "draft" US replies inappropriate.
J) J4 finishes all "substantive changes" and does an "editing meeting"
(possibly with or by WG4 or possibly just a "subgroup".
K) The output of this work (proposals and editing work) results in an FDIS
document "Final Draft International Standard).
L) This FDIS then goes out to another 4 month international review period.
Normally, (Unless something has gone DRASTICALLY wrong) this is a "straight"
up or down vote.  During this 4 month period the US does another 2 month
public review.
M) Assuming this FDIS "passes" (and there are explicit rules for what a
"pass" is) at the international processing, this FDIS becomes an
   International Standard
N) In the US as soon as this document becomes an ISO Standard, it will
"automagically" also become an ANSI Standard.  This may work differently in
other countries.

   ***

The existing schedules actually have a "little" slack in them to end up with
a December 2002 "completion".  So far I have seen nothing that is likely to
change this, but there certainly COULD turn out to be something
"controversial" or "hard to implement" coming out of the November 2001 WG4
meeting.  I doubt it, but it is possible.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-12T19:46:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106121846.563b9f0b@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote 
<snip>
>Agreed you've got to fine tune based on those comments - but to drag
it out from today until December 2002 ?
> Even that warns with a caveat - not necessarily, but could become xxx 2003 ?
> 
…[9 more quoted lines elided]…
> 
<snip>

*-----------
Jimmy, have you looked at the National Comments with which we must
deal?  Go to
http://people.ne.mediaone.net/doncobol/ and find document 01-0373 on
May 31. Then look at 01-0376, Tim Josling's comments, on Jun 3.  We
are treating his comments almost as if they were national body
comments -- he put a fantastic amount of work into them, and we
appreciate it. This takes TIME!

Also, vendors respond to the market with extensions; the standard, in
many cases, catches up.

I DO hope we can do the next one faster; I have covered some of the
reasons for the inordinate delay in this standard in other posts.

Stephen J Spiro
Member, J4 COBOL Standards Committee

PS: All of you could join J4 and help us get this backlog of work
cleaned up!
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-13T03:54:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B26E4C3.BEF3F732@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com>`

```


Stephen J Spiro wrote:

> Jimmy, have you looked at the National Comments with which we must
> deal?  Go to
…[5 more quoted lines elided]…
>

I concur. And I'm extremely glad you have given Tim's efforts recognition. Please don't lose sight - I'm not knocking you J4
guys. As Ann candidly admitted, you took on too much in one meal. I accept that, (been there, seen it, done it - and regretted
it). Similarly you had to prioritize - OO was lower down the list - and I accept that.
(Logical - 90% of COBOL is for mainframes, and how many of them are using OO).

What I'm really, truly frustrated about - are the hoops you folks have to jump through with ANSI/ISO.

Here's one for thought - why the secrecy (closed meetings) for ISO - is its real purpose to allow some stupid SOB to do a number,
just like the US recently getting chucked off two UN committees ? Bloody ridiculous - there isn't a UN without the States.

And I recall a recent message from Chuck, I think he listed about six or more different sets of initials covering
'COBOL-connected' organizations. God help us !

And your latter comments - no problem with the Standard as it stands, including OO - but as Thane well knows I really don't like
the approach of a TR for 'Finalizer'.

Pete - I think they are going to do it again - a TR for standard classes/collections !

Stephen your byline below - keep at it - somebody might just wake up <G>

>
> PS: All of you could join J4 and help us get this backlog of work
> cleaned up!
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-14T02:23:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2778e5_3@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B26E4C3.BEF3F732@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B26E4C3.BEF3F732@home.com...
>
>
…[3 more quoted lines elided]…
> > deal?

Jimmy,

It's a self-inflicted wound. Nobody said they HAD to do it this way...they
CHOSE to. And they can't even see that it is an archaic out-moded and
obsolete process which is totally out of touch with the User base.

There IS no effective communication or interaction between the Standards
committee and the User base. There are just impediments to this actually
occurring.

The whole thing is a nice little earner for the people concerned, especially
ANSI.
 (well, it's worth another $5 - $15 an hour to say in your CV you were on
the Committee...[Not my words...those of a Committee Member]).

It is a boondoggle for the vested interests. The Compiler vendors go along
with it because it makes it look like they are really paying attention to
standardising the Language, (when, in fact, they are driven by the
Marketplace), the large Corporations go along with it because it is an arse
cover if everything goes pear shaped ("Hey! we developed all the Mission
Critical stuff using a version which was ANSI approved...Not our fault if it
doesn't have the necessary functionality for today...it'll be in the 2050
standard...maybe...") and the rest if us go along with it because it seems
logical that there MUST be a standard...

They could've run an Internet forum with a separate thread for each
controversial  (or User raised issue) point in the Standard and let the User
community post their suggestions, solutions, concerns, or even just comments
on each point for a given period of time. Then a decision would be made
based on the posts received. And that's just ONE possible scenario for
increasing the interaction between the User base and the Marble Halls of J4.
There are many...

The process is fundamentally flawed.

Who the Hell are J4 or ANSI or ANY body that extracts money for its services
(whether it is technically non-profit or not) to decide what will or will
not go into OUR language?

If the Language MUST be administered (and that is an arguable proposition)
it should be adminstered with due regard to the feelings and concerns of the
people who make their living out of it, and it should be EFFECTIVE
administration. In the wildest delusions of an imbecile, 12 years to produce
a standard could not be considered EFFECTIVE.

If Boeing could write an engineering manual for an aircraft with many
millions of parts, describing every bolt, nut, screw, and assembly of it,
and take 4 years to do so, then J4 should have produced standards for the
next bloody Starship Enterprise by now... (I wonder what Boeing did
right...)

The people who founded COBOL wrote a Charter for it that said it would NOT
become the property of ANYBODY. You bet I'm sick about it, I'm spewing...

However, I also realise there is absolutely NOTHING I can do about it.

I have therefore ceased to care.

The lunatics are running the asylum; it is just a question of time before
the patient dies.

>>>
>> Go to
…[5 more quoted lines elided]…
> >
<<<

So why wasn't the time required allocated and managed BEFORE the event? Did
the committee seriously expect there would be NO comment from ANYBODY?

>>>
>
> I concur. And I'm extremely glad you have given Tim's efforts recognition.
Please don't lose sight - I'm not knocking you J4
> guys.
<<<

Why Not?! They bloody well deserve it...

>>>
> And your latter comments - no problem with the Standard as it stands,
including OO - but as Thane well knows I really don't like
> the approach of a TR for 'Finalizer'.
>
<<<

See how much impact your disapproval has on the end result...(Construct a
sentence here that uses the words "jot", "tittle", "iota" and "NOT"...)

>>>
> Pete - I think they are going to do it again - a TR for standard
classes/collections !
>
<<<
Sadly Jimmy, you're confusing me with someone who cares...<G>
(I REALLY don't any more. Given up. It just upsets me too much...)

>>>>
> Stephen your byline below - keep at it - somebody might just wake up <G>
…[3 more quoted lines elided]…
> > cleaned up!
<<<

Or we could just go and join Arthur Andersen... They seem to be about as
effective as J4...<G>

Oops! Gotta stop, sense of humour returning...

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-14T00:24:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2804EB.176AB386@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B26E4C3.BEF3F732@home.com> <3b2778e5_3@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

Pete I both agree and disagree with some of what you wrote. But this one.

> They could've run an Internet forum with a separate thread for each
> controversial  (or User raised issue) point in the Standard and let the User
…[4 more quoted lines elided]…
> There are many...

I endorse the idea. But in practice would it work, although I'd most certainly
give it a shot. Perhaps through promotion of the site through Legacy, InfoWorld,
cobolreport.com, various vendor sites etc...,  it would create a wider
awareness. Unfortunately if we take this News Group as being in anyway
representative, (and covering 3 million folks, I hope to God it isn't), you
don't exactly see them jumping up an down about where COBOL should be going.

Even Stephen's latest change of career venture - trying to get 'em involved in
J4 gets as much enthusiasm as a pork pie in a synagogue.

(Now, now  Jerry and Benjamin down in Israel - that isn't a reflection on your
historical/religious roots. It's just like I could have put, 'Is the pope on the
side of the catholics ?", in a different context - see a real touch of ecumenism
<G>)

Jimmy
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 12)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-14T17:35:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b284df8_1@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B26E4C3.BEF3F732@home.com> <3b2778e5_3@Usenet.com> <3B2804EB.176AB386@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B2804EB.176AB386@home.com...
>
>
> "Peter E. C. Dashwood" wrote:
>
> Pete I both agree and disagree with some of what you wrote.

You'll get a crease in your arse from fence sitting, Jimmy. Take my advice,
trying to be all things to all people is a certain recipe for disaster...<G>

And I wash my hands in your lukewarm, chicken soup, statement...<G>


>But this one.
>
> > They could've run an Internet forum with a separate thread for each
> > controversial  (or User raised issue) point in the Standard and let the
User
> > community post their suggestions, solutions, concerns, or even just
comments
> > on each point for a given period of time. Then a decision would be made
> > based on the posts received. And that's just ONE possible scenario for
> > increasing the interaction between the User base and the Marble Halls of
J4.
> > There are many...
>
> I endorse the idea. But in practice would it work, although I'd most
certainly
> give it a shot. Perhaps through promotion of the site through Legacy,
InfoWorld,
> cobolreport.com, various vendor sites etc...,  it would create a wider
> awareness. Unfortunately if we take this News Group as being in anyway
> representative, (and covering 3 million folks, I hope to God it isn't),
you
> don't exactly see them jumping up an down about where COBOL should be
going.
>
See, it was just a suggestion. It could be MADE to work, given the will The
real point here is that J4 needs to get in touch with the User Base. There
is technology available to do this, but they won't use it.

Could it be any worse than what we've got?

> Even Stephen's latest change of career venture - trying to get 'em
involved in
> J4 gets as much enthusiasm as a pork pie in a synagogue.
>
Because it's like volunteering for the Legion of the Damned...(Did I mention
Arthur Andersen...<G>?)
You can hardly expect a rush to join the queue for unpaid, thankless work,
in an organization with pitiful motivation, archaic management techniques,
and a track record of failure.

If the image was different and it looked like they were going somewhere, or
even TRYING to review and overhaul the procedures, you'd probably get people
coming forward.
(I'd probably be somewhere in the queue if I believed COBOL could be served
by this organisation, but no way while they are stuck in the practices and
attitudes which they currently manifest...)

If you can have no effect on the policy  (when it is blatantly obvious that
the policy NEEDS change) there isn't much point in joining.

That's why I've given up on it.

Pete.



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-14T07:26:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B28BBA3.670233C6@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B26E4C3.BEF3F732@home.com> <3b2778e5_3@Usenet.com> <3B2804EB.176AB386@home.com> <3b284df8_1@Usenet.com>`

```
"Peter E. C. Dashwood" wrote:

> > Pete I both agree and disagree with some of what you wrote.
>
…[3 more quoted lines elided]…
> And I wash my hands in your lukewarm, chicken soup, statement...<G>

You're absolutely correct.   Mostly.   Except when the other side has valid
points as well.   It's a nice view from on top of this fence - I can see both
yards.   And your wife left your bedroom drapes open...
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 14)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-15T11:42:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b294d45_3@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B26E4C3.BEF3F732@home.com> <3b2778e5_3@Usenet.com> <3B2804EB.176AB386@home.com> <3b284df8_1@Usenet.com> <3B28BBA3.670233C6@brazee.net>`

```
LOL!

Good one. Thanks Howard. <G>

I would stress that there is nothing wrong with examining viewpoints and
stating if/why you agree/disagree with them. My objection is to lukewarm
"inoffensive" statements, which really say nothing.

And I agree that sometimes the view from the fence can make it worth sitting
there for a little while at least...<G>


Pete.
"Howard Brazee" <howard@brazee.net> wrote in message
news:3B28BBA3.670233C6@brazee.net...
> "Peter E. C. Dashwood" wrote:
>
> > > Pete I both agree and disagree with some of what you wrote.
> >
> > You'll get a crease in your arse from fence sitting, Jimmy. Take my
advice,
> > trying to be all things to all people is a certain recipe for
disaster...<G>
> >
> > And I wash my hands in your lukewarm, chicken soup, statement...<G>
>
> You're absolutely correct.   Mostly.   Except when the other side has
valid
> points as well.   It's a nice view from on top of this fence - I can see
both
> yards.   And your wife left your bedroom drapes open...
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-16T14:42:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2b7029.229448864@news1.attglobal.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B26E4C3.BEF3F732@home.com>`

```
On Wed, 13 Jun 2001 03:54:57 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>And your latter comments - no problem with the Standard as it stands, including OO - but as Thane well knows I really don't like
…[3 more quoted lines elided]…
>

If you desire the process to be accellerated - then a TR is the way to
go.  This will eventually be incorporated into the actual standard --
but the TR requires less review and has fewer procedural roadblocks
within ANSI/ISO.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-16T15:55:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ggh29$uvo$1@slb2.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B26E4C3.BEF3F732@home.com> <3b2b7029.229448864@news1.attglobal.net>`

```
Thane,
  Correction - a TR (of one of the types) *may* eventually be incorporated
into a future Standard.  There is, however, NO "guarantee" (and depending on
topic - no expectation) of upward compatibility.

The original reason that WG4 directed that the Class Library be a TR was
because it was felt that the "technology was not yet stable enough" to get a
finalized (planned for upward compatibility) specification.

That was in '97, so I don't know what WG4 thinks about this now.  However,
given the fact that neither WG4 nor J4 (which can't act until WG4 does) have
started the procedures for getting a work item going, AND the fastest
estimate is that a TR could be approved after 18 months from the time the
work item is approved, we certainly are NOT looking at a fixed and common
definition in the short-term.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-16T21:48:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2BD4DF.32C52E8A@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B26E4C3.BEF3F732@home.com> <3b2b7029.229448864@news1.attglobal.net>`

```


Thane Hubbell wrote:

> On Wed, 13 Jun 2001 03:54:57 GMT, "James J. Gavan" <jjgavan@home.com>
> wrote:
…[11 more quoted lines elided]…
> within ANSI/ISO.

Making such a suggestion to Pete or myself, you know you are preaching to the unconverted <G> But that doesn't mean we are right. If
in fact 'TR'-ing obviates roadblocks, put "TR" on the whole bloody Standard document !

Jimmy
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-13T17:30:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B27953F.EC8B0F3E@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com>`

```
Stephen J Spiro wrote:

> Stephen J Spiro
> Member, J4 COBOL Standards Committee
> 
> PS: All of you could join J4 and help us get this backlog of work
> cleaned up!

The 'Rule of Committees' is that the time taken is proportional to the
square of the number of people involved.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** "Russell Styles" <rwstyles@worldnet.att.net>
- **Date:** 2001-06-14T04:14:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz>`

```
    Personally, I don't see why the vendors, at least those
vendors that
pay attention to their users don't just get together and work
this
out.  Ignore the various offical organizations.  After all, the
only
Cobol that really matters is what the vendors end up supporting.

    If a vendor fails to support something the users want, they
suffer.



"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3B27953F.EC8B0F3E@Azonic.co.nz...
> Stephen J Spiro wrote:
>
…[3 more quoted lines elided]…
> > PS: All of you could join J4 and help us get this backlog of
work
> > cleaned up!
>
> The 'Rule of Committees' is that the time taken is proportional
to the
> square of the number of people involved.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-14T17:54:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2851b0_6@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net>`

```
At last !

Somebody posts something that makes SENSE !

Well done, Russell and I endorse what you say. What you suggest is, in
reality, what is currently happening (although the "official" standards body
would never admit it...).

Vendors ARE listening to the Market Place and they ARE producing what is
needed...(And just as well for all of us that they are...<G>)

The attempt to put an "Official" stamp of Approval on it just muddies the
water and causes me personally much wailing and gnashing of teeth...
(Or it did, until recently when I  realised it was pointless to worry about
it...).

The best solution would be a vendor/user forum where all vendors could
promote their products and their ideas for enhancements, directly to the
User Base and get direct feedback on what was needed and wanted. This would
obviate the need for an "official" standards body, thus removing the
associated boondoggles and attitudes. (Much wailing and gnashing of teeth on
the OTHER side of the fence, instead...<G>)

It won't happen because there is too much at stake (I can't see the
"Official" body just rolling over), but it would be nice to think it
might....

Pete.


"Russell Styles" <rwstyles@worldnet.att.net> wrote in message
news:HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net...
>     Personally, I don't see why the vendors, at least those
> vendors that
…[26 more quoted lines elided]…
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-14T12:12:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9gar9m$m1$1@slb6.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com>`

```
Not that I "like" the current system, but the CLAIM has been made
(especially by the large vendors with LOTS of lawyers) that there are
"anti-trust" issues in their "talking" outside the ANSI/ISO (or similar)
structures.

This does NOT stop each vendor from implementing what their users want - and
copying what other vendors have created, but does (according to SOME
theories) stop them from "talking to each other" about what to add - outside
of some "protecting" agency.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 13)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-15T12:38:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b295bbe_3@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net>`

```
An interesting comment, Bill.

So, if a large Corporation has some good ideas for improving COBOL, they
can't tell anyone EXCEPT the "official" Standards body, for fear of being
perceived as trying to manipulate the COBOL market to their advantage?

I wonder how it ever got that crazy?

I further wonder how an anti-trust suit could proceed when the whole process
was SEEN to be OPEN with discussion via public forums on the Internet and
ALL interested parties (including the Corporation's competition)
contributing?

We are NOT looking at a market advantage lever here, we are looking at the
PUBLIC ownership of COBOL.

Can it be that the potential COBOL market is SO lucrative that nobody dares
to be perceived as dominating it? That would certainly explain why ANSI/ISO
won't let it go, and it would also validate my earlier post regarding the
vested interests...

But I don't seriously believe that. (Besides, there are no statistics
readily available as to the estimated value of today's COBOL market...that
would be something worth seeing...)

It MIGHT have been true prior to 1980 when COBOL was really "the only game
in town", but not today...

At the very best, COBOL today is a two-edged sword for the vendors. It can
suck up a very large block of resources to develop and maintain the compiler
and utilities, and the rewards are becoming more and more doubtful, BECAUSE
the Language is controlled by a moribund Standards authority which cannot
produce a standard for it in a time frame acceptable to anyone.

I admire the tenacity of companies like Fujitsu, who are hanging in there
with a stated policy and even a strategic plan of where they are going with
COBOL. Anybody who commits to COBOL when it is in the state it is in, gets
my vote. (Hence my support for Tiny COBOL also.)

But even with the vast resources of a Global giant like Fujitsu, they can
only pour good money after bad for a finite period of time, UNLESS there is
some light at the end of the tunnel...

IF we could get it back into the hands of the User Base (in conjunction with
the vendors, who could wear two "hats": "User" and "Provider") there WOULD
be some light at the end of the tunnel.

Progress is being made. People throughout the IT industry are starting to
re-evaluate the worth of COBOL as a commercial development language. It is
far too early to throw the baby out with the bathwater. But, just at the
time when we should be able to point to a modern standard as the basis of
the Language, we get the "maybe in 2 years" bullshit from the "official"
custodians of the Language.

Leaving that aside for a moment, there is still a lot to be done regarding
the attitude of COBOL programmers, too.

When I see a thread like Ross Klatte's "10 reason's why Java is better than
COBOL" and the responses to it, it makes me realise that maybe we DESERVE
what we have.

People with little or no knowledge of what they are talking about, taking
something that was said with tongue in cheek, and responding to it with a
serious post in support of their own prejudices...

There is still a huge backlog of fear and resistance to change on the shop
floor.

There are many who see it as a war between COBOL and new technology.

There are many who see COBOL as "work" and don't want to do anything in
their own time to improve their skills and marketability.

There are many "One Language Wonders" with their heads so far up their arses
they can't see what is happening in the daylight. It would be foolishly
optimistic to expect such people to contribute to the development of the
Language, even if they had the opportunity.

For the remainder, those of us who actually love the language and care what
happens to it, the picture is not good. If we elect to "use the machine"
(and it is like having to hitch up a team of oxen to go on a 100 mile
journey, when you have a Ferrari in the garage...) and post our views and
concerns to ANSI we get nowhere. (Well, Stephen says "it takes time"; when
you are under resourced, it certainly does.)

A public consortium between the Vendors and the User Base would be the BEST
thing that could happen to COBOL. It wouldn't cost a lot to set up and COBOL
people from all over the World could have a voice in it.

If Bill is right, and this can never happen because of anti-trust fears then
there truly is no hope for it...

(Now, where can I download Python...<G>)

Pete.


"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9gar9m$m1$1@slb6.atl.mindspring.net...
> Not that I "like" the current system, but the CLAIM has been made
> (especially by the large vendors with LOTS of lawyers) that there are
…[3 more quoted lines elided]…
> This does NOT stop each vendor from implementing what their users want -
and
> copying what other vendors have created, but does (according to SOME
> theories) stop them from "talking to each other" about what to add -
outside
> of some "protecting" agency.
>
…[17 more quoted lines elided]…
> > The attempt to put an "Official" stamp of Approval on it just muddies
the
> > water and causes me personally much wailing and gnashing of teeth...
> > (Or it did, until recently when I  realised it was pointless to worry
…[8 more quoted lines elided]…
> > associated boondoggles and attitudes. (Much wailing and gnashing of
teeth
> on
> > the OTHER side of the fence, instead...<G>)
…[47 more quoted lines elided]…
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 14)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-14T21:57:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106142057.645b9fc9@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote 
> 
> So, if a large Corporation has some good ideas for improving COBOL, they
> can't tell anyone EXCEPT the "official" Standards body, for fear of being
> perceived as trying to manipulate the COBOL market to their advantage?
> 
*---------------
No they get in touch with the vendor of the compiler which they use. 
This, I suspect, is from where most extensions come.

*---------------
 

> IF we could get it back into the hands of the User Base (in conjunction with
> the vendors, who could wear two "hats": "User" and "Provider") there WOULD
> be some light at the end of the tunnel.
> 

*----------------
Excellent idea, Pete! I can assume we will see you and 30 (or 300)
like-mided people at the J4 meeting in Portland, so that you will all
have voting rights for the following meetings, where you members of
the "User Base" can take full control.  And, of course, I am sure you
will all become active in Standards New Zealand, to make sure that it
sends a delegation (with you and your like-minded friends as
delegates) to the WG4 meeting this year.  And of course, with just a
few more delegations (Australia is not currently a member and Canada
has not sent a delegation in several years, for instance) there are
certainly enough concerned COBOL "User Base" members that we can take
control of the entire ISO bureaucracy in no time at all, and show them
how things OUGHT to be done!

Pate, I am really excited that you are finally going to DO something,
instead of just taking potshots at he people who ARE doing something.
Thank you very much!  I am looking forward to working with you!

Stephen J Spiro
Member, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 15)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-16T02:40:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2a1e9f_5@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com>`

```
"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106142057.645b9fc9@posting.google.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote
> >
> > So, if a large Corporation has some good ideas for improving COBOL, they
> > can't tell anyone EXCEPT the "official" Standards body, for fear of
being
> > perceived as trying to manipulate the COBOL market to their advantage?
> >
…[4 more quoted lines elided]…
> *---------------

Good. So we don't need an Official standard then, do we?

> > IF we could get it back into the hands of the User Base (in conjunction
with
> > the vendors, who could wear two "hats": "User" and "Provider") there
WOULD
> > be some light at the end of the tunnel.
> >
…[4 more quoted lines elided]…
> the "User Base" can take full control.

Oh! shock! horror! The Users actually taking control? Why do I need "voting
rights" to do that?

See, Stephen it is you guys who have laid down the "required
procedures"...attend this meeting and then we'll condescend to allow you to
attend another meeting, and, if you attend enough meetings we MAY actually
let you vote on something which has ALWAYS belonged to you, since its
inception.

Nope. I don't think so...(besides, why Oregon? Someone slipped up
there...Florida, California, or somewhere sunny, surely?)

> And, of course, I am sure you
> will all become active in Standards New Zealand, to make sure that it
> sends a delegation (with you and your like-minded friends as
> delegates) to the WG4 meeting this year.

Oh Boy! Another boondoggle...just what I need. Travel to the US at someone
else's expense and meet up with a bunch of like minded committee oriented
movers and shakers...so we can sit around and decide what qualifications and
voting rights are required for membership of WG4 and then discuss the venue
for that...(COBOL? aw...that's just something which we'll consider once we
have the voting rights, procedures, committees, and venues organised. "these
things take time"...)

I am no more likely to become active in the NZ Standards organisation than I
am in any other. And for the same reasons. Until there is some indication of
a fundamental shift in attitude and organisational procedures  (and that
will be the day Satan wears an anorak) I'll take a swerve on it thank you...

>And of course, with just a
> few more delegations (Australia is not currently a member and Canada
…[4 more quoted lines elided]…
>

Congratulations Oz and Canada! Hope NZ keeps out of it too... Vote with your
feet! Show them where to put their "voting rights"!

> Pate, I am really excited that you are finally going to DO something,
> instead of just taking potshots at he people who ARE doing something.
> Thank you very much!  I am looking forward to working with you!
>
(Pate?! Where's the toast <G>?)
Your sarcasm is water off a duck's back...I have been DOING something to
advance COBOL for the whole of my working life; solving problems with it,
promoting it, training people in the use of it, and persuading Managers to
support it and instigate training programs for their staff in it. I learned
it in 1967 and as of this date I have personally trained over 100
professional COBOL programmers (and I'm still tutoring for free via the
Internet...there's an Idea you could mention to J4; this fantastic
technology lets people from all over the World interact with each other
instantly; 'course, there are no committees, or forms to be filled in, so
there's not much paper to push around, and nobody gets a title that looks
good on a C.V., or little jaunts to exotic places like Oregon... but people
do actually seem to derive benefit from it, nevertheless...)

My potshots are not personal. However, people who congratulate themselves on
achieving nothing are always irritating and bring out the worst in me... If
the attitude was different, I would load lighter shot...(maybe even put the
sniper rifle away altogether).

The best I can hope for is that other people will see this standards farce
for what it is, and refuse to have anything to do with it either. If enough
people do that, we might be able to regain control of COBOL.

I don't think you can begin to imagine how upset I am over this...

Tell you what...

You say you're sorry for the delay in the Standard (unequivocally, no
excuses, simply take responsibility for it as a group) and I'll load lighter
shot.

You say that J4 is opening a public Internet forum to elicit user feedback,
from anywhere on the Planet, (and this will "fast track" all future public
reviews) and I'll drop my criticism altogether.

You say that there will be no more little jaunts to discuss things (and
thereby qualify for the next little jaunt or get voting rights or Brownie
points or any other Goddamned inducement),  instead, all discussion will be
OPEN and PUBLIC via the Internet, with finite timeboxes on it so EVERYONE
knows what the timeframe is, and I'll commend you and sing your praises in
every public forum and magazine to which I have access.

Finally, get the 2004 standard out by 2002, and I'll see that all of you get
your names on the Golden Scroll, "writ large in the Book of Life"  (I can do
that...<G>)

Pete.

PS If you don't like the sniper fire, try digging a different trench, wave a
white flag, or keep your head down....<G>
(It's the Internet; last bastion of freedom of expression...)





Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 16)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-15T16:12:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106151512.327040a4@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz
<snip>
> wrote 
> Oh Boy! Another boondoggle...just what I need. Travel to the US at someone
> else's expense 
<snip>
*-----------------
No, no, no, Pete! At one's OWN expense!


You just don't get it...  The problem is not the procedures.  The
problem really is that there are not enough people willing and able to
do the work.   When this standard is published, it will be the largest
(in words and pages) standard in all of ISO/IEC.  We need more help,
and, in spite of your obvious interest and expertise, you are not
providing any.

I'll smile at your humor, I'll pay attention when you speak on
technical threads, but I'm having more and more difficulty respecting
your opinion on the standard.

By the way, you don't get a vote until the second meeting specifically
to prevent someone from walking in with 30 friends and hijacking the
project.  If you come back again, we can assume you are serious, and
deserve a vote.  Incidentally, you DO get to participate in the
(non-binding, for direction only) "straw votes" at the first meeting.

Stephen J Spiro
Member, J4 COBOL Standards Committee

PS: Standards Committees are where Standards are made. All of you,
join one!
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 17)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-16T12:31:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2aa99c_1@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com>`

```
"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106151512.327040a4@posting.google.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz
> <snip>
> > wrote
> > Oh Boy! Another boondoggle...just what I need. Travel to the US at
someone
> > else's expense
> <snip>
…[10 more quoted lines elided]…
>

No Stephen, it's you who don't get it. The problem IS the procedures. They
are so red taped as to be unworkable. I accept that you need help, and I
suggest that if the process were OPEN (and I suggested how this could be
achieved) then you WOULDN'T need the help you do at the moment.

The whole process is predicated on the fact that only "certain people" are
"able to do the work". I dispute that vehemently. ANYONE who uses COBOL is
qualified to have input to the process of building the language.  If the
standard was written in plain English, many more people would probably
contribute. I don't like this elite thing that says ANSI knows what's good
for us... The language belongs to the User Base; it always has. Neither you,
an unelected Elite, nor ANYONE else has any right to hijack it.

I am not providing direct help because I don't believe in the way it is
being done, (and you really wouldn't enjoy having me in your meetings
anyway...<G>).



> I'll smile at your humor, I'll pay attention when you speak on
> technical threads, but I'm having more and more difficulty respecting
> your opinion on the standard.
>

Well, I can live with that...

I respect all the people applying the effort, but until some work is done, I
am not persuaded. And your "difficulty" is your problem...<G> (I guess if I
get to make you smile that's a start...)


> By the way, you don't get a vote until the second meeting specifically
> to prevent someone from walking in with 30 friends and hijacking the
…[3 more quoted lines elided]…
>

See, its words like "deserve" in the context above that really rattle my
chain. Can you not see how pompous and arrogant this sounds?  The whole
attitude is out of place when we are talking about something that belongs to
EVERYBODY. Who exactly are "you" (I don't mean you personally) to decide
that those will be the rules and nobody is taken seriously until they have
attended twice? Get it out of closed committees and into OPEN PUBLIC domain.
That way there's a chance it can be saved.

Sorry, truce is over...<reloads...>

Pete.





Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 17)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-16T15:49:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9gggn6$dji$1@slb0.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com>`

```
Stephen,
  You just don't get it (IMHO) - it is the PROCEDURES and not the lack of
people (although the lack of people doesn't help - and the number of members
who can't dedicate 18 weeks a year, 6 for meeting, 6 for preparation and 6
for post-meeting work) does add to the problem.

But it IS the procedures (both ANSI and ISO) that make it difficult for
"interested people" to work as their resources and interests allow.

Furthermore, it is the ISO rules on "voting" that make it more important to
"compromise" than get somethings "right".  (Along with the fact that ISO
meetings, papers, etc are all "closed")

Remember that this draft (when it was first "started") was SUPPOSED to be a
FAST and LIMITED revision.  It was the "procedures" that encouraged NEVER
saying "NO" to any additional enhancement, and to constantly changing
previous decisions that lead (at least in some part) to the delays.

Remember that there have been at most 3 (and I think only 2) meetings in the
last 6 years when the "agenda" was actually finished in the allocated time.
This means that there were ENOUGH people to prepare papers to fill the full
week of meeting time.  It is true that if most of the members were actually
PREPARED to discuss the papers, they might have been processed faster, but
simply adding for "occasional" members would NOT have speed up the
development at all (IMHO).
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 18)_

- **From:** "Grinder" <no.spam@no.spam.spam.spam.net>
- **Date:** 2001-06-23T12:58:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net>`

```
>   You just don't get it (IMHO) - it is the PROCEDURES and not the
lack of
> people (although the lack of people doesn't help - and the number of
members
> who can't dedicate 18 weeks a year, 6 for meeting, 6 for preparation
and 6
> for post-meeting work) does add to the problem.

It's a bit glib, but to paraphrase Ayn Rand, "no good idea was ever
conceived
by a committee.  If you look at those languages (or just concepts in
general)
that have evolved the fastest, they have had the benefit of a small
group of
designers doing what they thought was right.  Invariably, though,
after a large
group of people develop a stake in what's done to the concept,
advances bog
out.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 19)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-23T20:20:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B34F9C9.A2EE42C2@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com>`

```


Grinder wrote:

> >   You just don't get it (IMHO) - it is the PROCEDURES and not the
> lack of
…[16 more quoted lines elided]…
> out.

Your comments about small groups is valid - applies to Xerox PARC for
Smalltalk and Sun's Java - the latter for which there is as yet no
ANSI/ISO standard.

The Ayan Rand quote is not strictly true. COBOL with a committee of
vendors and the D of D was conceived in 6 MONTHS - obviously not all the
whistles and bells we are familiar with to day - but nevertheless a
REMARKABLE ACHIEVEMENT.

Regardless of Stephen's defensiveness of the process most of us view COBOL
has having 4 versions over a 40 year period, (COBOL 1 - 1968, COBOL 2 -
1974, COBOL 3 - 1985 and COBOL 4 - 2002). Now that just has to be wacky in
the fast paced technology that we are in. Not yet part of the standard
until COBOL 2002 - OO has been on-going since approx. 1991/1992 (?), and
at this point J4 are still deliberating on standard classes/collections,
in order to have something ready between now and December 2002.

There is no denigration of the people who participate in J4, they are all
tuned in, dedicated and intelligent, and IMPARTIAL - no vendor
arm-twisting goes on.. What has happened, as with any committee structure,
is that they have fallen into the trap of 'business as usual' - this has
gone on for eons, why change it. Further they are severely restricted by
the ANSI/ISO mechanisms - which is BIll's point. And for those who may not
be aware, Bill has several times admitted that as a contributor he has
been 'seduced' into the process over a number of years - it's his latter
day thinking that causes him to raise objections to the process.

Briefly Joe Blow in Toronto can volunteer and finish up on J4 - and he
puts forward a new innovation for COBOL, one hell of a good idea that his
fellow J4 members buy into. Meanwhile, yours truly, sat in Calgary, also
thinks he wants to get involved, but joins the more clandestine outfit the
Canadian arm of ISO. J4 produces a draft including Joe's new innovation. I
read it and determine "it is a crock....", my own personal view, although
it has already gone through the J4 sieve for credibility. I convince my
fellow Canadian ISO members, whoever they might be, that "it truly is a
crock'. The Canadians chat to the Brits, Aussies, Kiwis, Germans etc., and
persuade those ISO delegates also 'that it is a crock' Closed door
sessions of ISO - Joe's innovation gets side winded and rejected - and
poor Joe doesn't even know that it was some fellow Canadian SOB who
scotched him !

Obvious question - why are Joe and I sat on separate committees to achieve
the same end ?

The other question - why not an update to COBOL every TWO YEARS - if the
wish list that J4 gets, indicates this ?

Jimmy
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 20)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-24T16:00:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106241500.70eaab63@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com>`

```
Jimmy, I have to apologise.  As a former representative of my company
to J4, I should have continued sending you the J4 e-mails when you
were dropped from the J4 mailing list. I will make an effort to do so
from now on....  You will see that it is easy to get in on the
discussions, even if you are NOT on J4.
By the way, if you WERE on the Canadian WG4 delegation, you could be
put on the J4 mailing list on request.


Incidentally....

Anyone outside of the US who wants to be on their country's delegation
to the next WG4 meeting, get in touch with your standards body now.

Here is the info:
Meeting 234, co-located with WG4, will be at the Embassy Suites in Las
Vegas, Nevada; room rate is $105.  COMDEX is the week after our
meeting; room reservations must be made in late August to avoid
significant penalties.  Meeting notice will be distributed within the
next two weeks.  Meeting notice will include descriptions of some
family-oriented activities in Las Vegas.   Room reservations need to
be made by 9 October 2001, but they should be made by the end of
August.  Also, transportation  needs to be arranged early because of
COMDEX.   WG4 will be 5-8 November; J4 will meet 1-3 and 9-10.  4
November will be off.  If WG4 finishes early, there  will be ad-hoc J4
work done in preparation for the closing two days of the J4 meeting.


Las Vegas was NOT chosen for it's resort status; the J4 Chairman lives
in Las Vegas half the year.  Cheaper hotels are easily available, but
book early because of COMDEX.

Stephen J Spiro
Member, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 21)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-25T13:51:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b369afd_1@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com>`

```
Stephen,

You didn't think I'd pass on this one did you...<G>

Pete.

"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106241500.70eaab63@posting.google.com...
>
> Las Vegas was NOT chosen for it's resort status; the J4 Chairman lives
> in Las Vegas half the year.  Cheaper hotels are easily available, but
> book early because of COMDEX.
>
ROFL! ("Lifestyles of the Rich and Famous")

D'you reckon he'd let us park the RV on his lawn...<G>?

I find this SO amusing I am tempted to turn up...<G> However, fortunately
(for all concerned <G>) I will be in Germany in November... (so you can
relax, Stephen..<G>)

I STILL say it should be done via the INTERNET so that EVERYONE can
participate.

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 22)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-24T22:55:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106242155.47171ec3@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3b369afd_1@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote 
> 
> D'you reckon he'd let us park the RV on his lawn...<G>?
*--------------
I'm sure he would. I believe his family lives in an RV, themselves, 
when they are in Vegas.
> 
Actually, we DO try to pick a place that is at least a little
interesting, because many wives attend.  Ask Jimmy Gavan, the
delegates are working from 8:30 to 6....

Stephen
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 21)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-25T05:40:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B36CE91.2B69584E@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com>`

```


Stephen J Spiro wrote:

> Jimmy, I have to apologise.  As a former representative of my company
> to J4, I should have continued sending you the J4 e-mails when you
…[4 more quoted lines elided]…
> put on the J4 mailing list on request.

Sorry Stepehen.

Can't recall what it was I said that you feel you need to apologise. By
all means get me copies of J4 stuff that deals specifically with OO.

WG4 - I did contact Canadian ISO because I would have liked to observe
their deliberations at Newbury. No can do - closed shop. And to get on to
the Canuck ISO - reams of BS, plus air trips across Canada for meetings.
(Anyway,  as I've already commented - why TWO committees ?)

Let me reiterate - I'm not a committee man - I've done my penance. Agreed
at the current time you can submit proposals to J4 quite openly, but it is
somewhat of a 'formalized' approach. I really would like to see somebody
take up Pete Dashwood's idea - J4 e-mail sessions, separate threads per
topic, and as I added, monitored, NOT censored. Let a whole daffy of
people zero in on one aspect of COBOL, not the whole, and get a consenus
where J4 should be going. This Newsgroup is a very small microcosim of the
whole - but hell, where else can you go to discuss COBOL.

Recall that over the years you have had to prioritize to get through the
mass. Given the J4 e-mail approach - you might  finish up with a different
priority list - based on user input.

Good on yer - keep plugging for volunteers though <G>

Jimmy
```

###### ↳ ↳ ↳ comp.std.cobol

_(reply depth: 22)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-25T01:26:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106250026.60974186@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote
<snip> 
> I really would like to see somebody
> take up Pete Dashwood's idea - J4 e-mail sessions, separate threads per
…[11 more quoted lines elided]…
> Jimmy

The appropriate newsgroup is comp.std.cobol, which does not exist.  It
needs a news-server on which to be set up.  If anyone knows how to go
about this, I will moderate it (hopefully, with a little {LOT!} help
from my friends). Not the kind where messages go thru the sysop before
being posted.... all I want to be able to do is delete off-topic
posts.
This would necessarily be informal, but I think most J4 members would
tune in.


Stephen J Spiro
Member, J4 COBOL Standards Committee

Stephen J Spiro

Anyone out there can help.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 23)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-25T22:51:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3717e7_3@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com>`

```
"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106250026.60974186@posting.google.com...
> "James J. Gavan" <jjgavan@home.com> wrote
> <snip>
…[4 more quoted lines elided]…
> > where J4 should be going. This Newsgroup is a very small microcosim of
the
> > whole - but hell, where else can you go to discuss COBOL.
> >
> > Recall that over the years you have had to prioritize to get through the
> > mass. Given the J4 e-mail approach - you might  finish up with a
different
> > priority list - based on user input.
> >
…[19 more quoted lines elided]…
> Anyone out there can help.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 23)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-26T00:55:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b373468_6@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com>`

```
"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106250026.60974186@posting.google.com...
> "James J. Gavan" <jjgavan@home.com> wrote
> <snip>
> > I really would like to see somebody
> > take up Pete Dashwood's idea - J4 e-mail sessions, separate threads per
> > topic, and as I added, monitored, NOT censored. >

When I saw this I got quite excited...

> The appropriate newsgroup is comp.std.cobol, which does not exist.  It
> needs a news-server on which to be set up.

This will cost. Not a lot ... well within the means of a non-profit making
organisation like ANSI. I would suggest using Usenet (they already support
over 90,000 NewsGroups, so one more really won't hurt..<G>)

> If anyone knows how to go
> about this, I will moderate it (hopefully, with a little {LOT!} help
> from my friends). Not the kind where messages go thru the sysop before
> being posted.... all I want to be able to do is delete off-topic
> posts.

Oh Really? The function of a moderator is to moderate. Yes, Off-topic
threads could be removed but only after they have been posted publicly and
the author of the post gets a chance to modify it to bring it back within
the boundaries of the Group. There have to be very clear and strictly
enforced rules as to what gets "moderated" and what the rules for posting
are... Furthermore, the Moderation should be undertaken on a roster of
Committee members and volunteers, rather than any one person.

Like I said, I got really excited about this as I thought it represented
real progress (I even took the 'scope off the sniper's rifle...)

Then I saw this...

> This would necessarily be informal, but I think most J4 members would
> tune in.
>

The key here is "informal". In other words, not recognised or acknowledged
as being part of the COBOL Standards process by J4. No power to actually DO
anything; the decisions still vested in a committee... the timescales still
decided by a committee.

In reality, it is a unilateral move on Stephen's part (and I respect him for
doing it) to try and show some willingness to include the hoi polloi in the
process, but without empowering them in any way or committing J4 or ANSI to
any kind of public answerability.

Here's what I would like to see:

1. An official ANSI/J4 forum that IS formal, controlled and run by the J4
chair, recognised as an ESSENTIAL part of getting the Standard out, and
moderated by delegated persons to ensure that the rules of the group are
kept to.

2. Separate threads for each section of the Proposed Standard, with
comments, suggestions, arguments, proposals accepted from anyone, anywhere
on the planet. (No particular qualification...it's just another way of
ensuring exclusivity and "membership" of an elitist club...). The emphasis
MUST be on OPENNESS and PUBLIC contribution.

3. A defined timebox for each thread during which submissions can be made.
At the end of that time, submissions are closed and the committee (with
volunteers) comb through the posts and arrive at a consensus regarding the
points raised in each thread. If there are no posts, then it will be assumed
that the proposed standard (in this area) is acceptable. Silence constitutes
acquiescence. Submissions are summarised and posted as the "result" with the
Standard text which has been altered, added or deleted, as a result of the
public submissions.

No timebox should be greater than 6 weeks from the time the Draft is
available (as it is currently available, this would mean from the time the
server is up and running the new forum.)

4. Where there is dissension or controversy, the disputed points are put to
a public vote through the same forum. The majority rule. In the event of a
tie (or no submissions) the Chair of J4 decides. (Votes are collected
through the forum over a 14 day period).

5. Procedures in ANSI are changed so that, once this process has completed,
the Draft cannot be amended or changed. In other words, the decisions taken
from the public submissions are binding and cannot be reversed by ANSI or an
yone else.

6. Where Technical Reports are required, the need for them would be posted
publicly and contributions solicited. These contributions then form the
basis of the new draft. It is exactly the same principle as outlined above.
Existing members of the committees have the same right as everyone else to
contribute.

Vendors can assign their own representatives to present their Company
perspective in the Forum.

The difference is that it is a PUBLIC process. In many ways this can make it
faster because there are more people able to contribute easily via the Net.
There is then no real need for a "committee" at all. All that is required is
a "pool" of moderators and a Chair to hold a casting vote. These could be
elected (at the moment they are an unelected "elite") by the contributors to
the forum. This ensures that there is no financial qualification to be a
part of COBOL's future (buying membership of ANSI and attending the
boondoggles are options which are NOT open to ALL; what we want is something
that IS open to ALL and is SEEN to be open to ALL. It is then likely that
the user base may actually participate...)

Can you imagine the CREDIBILITY the ANSI standard would have if it were seen
to be administered in this way? No-one could argue with it. Democracy in
action.

Think about what credibility it has at the moment...could any alternative
actually be worse?

What is so difficult or unreasonable about this?

Pete.
>
> Anyone out there can help.
>
Yes, Stephen, but only on your terms...(I don't mean you, personally). Your
move is a good one, but people need to know they can make a difference.
"Necessarily informal" just doesn't cut it...well, not for me anyway.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 24)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-25T17:30:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3774D9.ABA3E40A@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

> "Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
> news:4145699b.0106250026.60974186@posting.google.com...
…[14 more quoted lines elided]…
>

<snip all the good stuff>

Your proposals make a sound starting point, plus your emphasis that it is all
part of a formalized function.

Just one minor comment - Your six week cut-off. No,  I'm not asking for umpteen
months, but there may be issues where a longer debating period than six weeks is
required. People need to chew over others comments, and start to see the
'problem' in a slightly different perspective and come up with a revised
argument.

As an example - standard classes or more specifically collections/dictionaries.
We ALREADY have three implementations that work in COBOL, Fujitsu, Hitachi and
Micro Focus. Further we can turn to Smalltalk and Java for advice, and any of
the other languages which offer a 'neat' solution.. Thane made the comment that
the Java people he spoke to were not particularly 'thrilled' with this aspect of
OO. The Smalltalk people are using them all the time, and they are a source of
constant discussion in their Newsgroups. Back to Thane's comment - One Smalltalk
developer said he finds it difficult (not easy) to clone classes in Smalltalk -
and where did he turn for help - he uses Java to clone his collection classes !

As I've already stressed elsewhere, put the above vendor/language classes and
method names under the microscope, do we need this class, do we need all its
methods etc..., what can we combine, what is not really needed etc. This is a
much longer process than your six week timeline.

OK - the above looks like I'm plugging OO yet once again - I'm merely using it
as an illustration. So let's take another example - accepting that you are gung
ho for DBs, but nevertheless you are in a position to comment on COBOL files, as
would be many others who constantly use them. Recall our problem with producing
a generic ISAM, and your solution for me. I'm not going to develop the idea
here, BUT if Reference Modification could be added to file definition syntax to
recognize Prime Keys, Alternate Keys and Split Keys - we could possibly be home
and dry. So somebody promotes the topic, others jump in with differing points of
view, it's a no go or yes 'if it had the following variations'. What do we
finish up with - perhaps an even more flexible COBOL file system and the option
of using DBs. In this area think on Tom Morrison's comment about 'Relativity'
offering DB access to COBOL files. I have no idea of the details, perhaps there
is a case for a COBOL DB. (Ed's book on OO made a passing reference that a COBOL
DB was in the works - presumably he must have gleaned that from some J4 source
?). Note I'm not making a case for a COBOL DB - just that some might think it
merits discussion.

Want another topic - how about GUIs as part of COBOL <G>. Surely you can hardly
reject this out of hand, (re your "Jimmy, you must be out of your mind to
suggest this..............."),  particularly as you have now latched on to
POWERCOBOL's GUI features to do your beloved components <G>

If this idea (your e-mail forum), is seriously taken up then I would suggest the
very first topic should be take your draft and turn it into an official set of
rules - and this is one which must not take more than SIX WEEKS if you idea is
adopted.

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 25)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-26T13:44:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b37eaa8_3@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <3B3774D9.ABA3E40A@home.com>`

```
Thanks Jimmy,

Comments below...

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B3774D9.ABA3E40A@home.com...
>
>
…[7 more quoted lines elided]…
> > > > take up Pete Dashwood's idea - J4 e-mail sessions, separate threads
per
> > > > topic, and as I added, monitored, NOT censored. >
> >
…[5 more quoted lines elided]…
> > This will cost. Not a lot ... well within the means of a non-profit
making
> > organisation like ANSI. I would suggest using Usenet (they already
support
> > over 90,000 NewsGroups, so one more really won't hurt..<G>)
> >
…[3 more quoted lines elided]…
> Your proposals make a sound starting point, plus your emphasis that it is
all
> part of a formalized function.
>
> Just one minor comment - Your six week cut-off.

As Patience is not one of my virtues (thinking about it...I don't really
have many<G>) I accept that what to me seems like an ample amount of time
may not be... I would have no objection to it being lengthened by agreement
in the group.

> No,  I'm not asking for umpteen
> months, but there may be issues where a longer debating period than six
weeks is
> required. People need to chew over others comments, and start to see the
> 'problem' in a slightly different perspective and come up with a revised
> argument.
>
> As an example - standard classes or more specifically
collections/dictionaries.
> We ALREADY have three implementations that work in COBOL, Fujitsu, Hitachi
and
> Micro Focus. Further we can turn to Smalltalk and Java for advice, and any
of
> the other languages which offer a 'neat' solution.. Thane made the comment
that
> the Java people he spoke to were not particularly 'thrilled' with this
aspect of
> OO. The Smalltalk people are using them all the time, and they are a
source of
> constant discussion in their Newsgroups. Back to Thane's comment - One
Smalltalk
> developer said he finds it difficult (not easy) to clone classes in
Smalltalk -
> and where did he turn for help - he uses Java to clone his collection
classes !
>
> As I've already stressed elsewhere, put the above vendor/language classes
and
> method names under the microscope, do we need this class, do we need all
its
> methods etc..., what can we combine, what is not really needed etc. This
is a
> much longer process than your six week timeline.
>
How about this... The period for major tasks (like collections) could be 6
months, but broken into 6 week timeboxes and iterated. We decide in the
first time box what the Class priorities will be, then we do a first cut.
This is then re-prioritised and iterated. Four iterations should allow the
process to be refined enough for issue. The same principle applies to all
major "chunks" of work. Priorities are assigned on the "MoSCow" model: MUST
have, SHOULD have, COULD have, and WANT. (If you are amused by this, come
and get the full story from my presentation on Dynamic Project Management at
CW2001; I am deadly serious...)


> OK - the above looks like I'm plugging OO yet once again - I'm merely
using it
> as an illustration. So let's take another example - accepting that you are
gung
> ho for DBs, but nevertheless you are in a position to comment on COBOL
files, as
> would be many others who constantly use them. Recall our problem with
producing
> a generic ISAM, and your solution for me. I'm not going to develop the
idea
> here, BUT if Reference Modification could be added to file definition
syntax to
> recognize Prime Keys, Alternate Keys and Split Keys - we could possibly be
home
> and dry. So somebody promotes the topic, others jump in with differing
points of
> view, it's a no go or yes 'if it had the following variations'. What do we
> finish up with - perhaps an even more flexible COBOL file system and the
option
> of using DBs. In this area think on Tom Morrison's comment about
'Relativity'
> offering DB access to COBOL files. I have no idea of the details, perhaps
there
> is a case for a COBOL DB. (Ed's book on OO made a passing reference that a
COBOL
> DB was in the works - presumably he must have gleaned that from some J4
source
> ?). Note I'm not making a case for a COBOL DB - just that some might think
it
> merits discussion.
>
Personally, I wold have no interest in enhancing the COBOL file system so
long as it remains closed, but that's no reason why others can't pull it
around.

> Want another topic - how about GUIs as part of COBOL <G>. Surely you can
hardly
> reject this out of hand, (re your "Jimmy, you must be out of your mind to
> suggest this..............."),  particularly as you have now latched on to
> POWERCOBOL's GUI features to do your beloved components <G>
>
It is not viable for COBOL to implement a cross platform, event driven,
model to produce GUI screens, in the same way that it has a cross platform
console display statement. Besides, there is no need to. Products like SP2
and DIALOG, and  PowerCOBOL render it unnecessary. And that particular boat
sailed long ago... Such a model would have to run on mainframes and
Client/Server. I don't see CICS  or IMS/DC being seriously threatened by
"Display upon GUI Screen" ...


> If this idea (your e-mail forum), is seriously taken up then I would
suggest the
> very first topic should be take your draft and turn it into an official
set of
> rules - and this is one which must not take more than SIX WEEKS if you
idea is
> adopted.
>
To paraphrase Eliza Dolittle..."Wooden it be Luverly?"

I'm a betting man and at the moment I can't back it. But you never know what
closed door discussions are thaking place even as we tap our keyboards. An
eternal optimist, I live in Hope...

Pete.




Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 26)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-26T02:53:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B37F848.4A700321@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <3B3774D9.ABA3E40A@home.com> <3b37eaa8_3@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

> >
> How about this... The period for major tasks (like collections) could be 6
…[7 more quoted lines elided]…
> CW2001; I am deadly serious...)

OK I'll buy the general outline you show above. Now for Stephen's sake this is
not fine tuning. All that effort wasted back in 93/96 (?). Collections at this
point in time are truly a new topic to COBOL - but I accept your overall comment
about fine tuning *existing*

> To paraphrase Eliza Dolittle..."Wooden it be Luverly?".

My turntable is kaput, so can't play the LP. As Professor 'Iggins said, "Why
can't the English set a good example........", then went on to make some comment
about "the Americans don't really care just so long.....(memory fades......)".
And the dig about Americans was written by a American lyricist and composer <G>

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 24)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-25T14:42:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9h847s$ub7$1@slb6.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com>`

```
<all previous parts "snipped">

Whether I like or dislike the current J4 procedures, I did want to point out
the current situation (again) - just so there is NO question/concern about
what can be done already.

*ALL* J4 papers are posted on the worldwide web at:
    http://people.ne.mediaone.net/doncobol/index.html

This is where the "current" papers are - but there is also a link to the
archives, so "older" papers (and a document log) are available.

J4 is OPEN to all input.  Anyone (US citizen or not; COBOL programmer or
not; anyone) can submit a "comment" on any existing paper (or paper up for
discussion).  Although there is a "preferred" format for such papers, this
is NOT required for non-J4 members.  All you need to do is send an email to
the J4 chair at
   doncobol <at> mediaone.net
and request that he submit it as a J4 paper.

J4 *does* (and I can't think of ANY exception to this) give "full"
consideration to all papers that are submitted by non-members - no matter
when or how they are submitted.  Much of the current revision was done by or
influenced by non-members.  (This includes OO, Screen Section, Validate,
Standard Arithmetic, etc).

Although this would NOT be "formal" in the sense that you would "vote" on
how J4 should act upon a specific issue, it really REALLY does work for
getting "user input" to the committee WHEN people bother to sit down and
just send an email note with comments or suggestions.

FINALLY,  I assume that no one is thinking of (significantly) changing the
existing FCD (or related procedures) before it becomes official, as I think
that will be strongly discouraged.  However, if you DO have input on
FINALIZER, Class Libraries, or any other "future" feature - or if you see a
serious "technical flaw" (not omission) in the FCD, please
     PLEASE
do take the time to send an email not to the J4 chair at your earliest
possible time.

P.S.  As far as using the internet, WWW, or anything else to do "formal
work" of J4 (including non-members in the "official" actions, that is and
will remain impossible as long as J4 is authorized by ANSI).

P.P.S.  I am in the minority on this (again) but I *do* think it would be
useful (given the lack of progress on them) if some (as many as possible)
national Standards bodies indicated to ISO that the FINALIZER and Class
Library work (and any future COBOL work) *not* be done in a "two committee"
development process.  That either J4 (and ANSI) have full development
responsibilities and authority OR that WG4 (and ISO) have them - and that
this "two committee development technique" be ended as soon as possible.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 25)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-25T20:40:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B37A17D.8902B554@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net>`

```


"William M. Klein" wrote:

> <all previous parts "snipped">
>
…[48 more quoted lines elided]…
> this "two committee development technique" be ended as soon as possible.

First off, I *hope* we are all on the same wavelength - but I don't think any
sensible person would suggest putting the breaks, (enhancements or negatives),
on the proposed COBOL 2002 - let J4 get to conclusion as quickly as possible.

I can live with the TR on 'Finalizer" - but my preference would be stick with
standard classes/collections as we already have them in Fujitsu, Hitachi and
Micro Focus - which would make them all 'extensions' so far as COBOL 2002 was
concerned - and come up with a finite proposal after 2002 - the alternative
being the current proposed TR to give us a 'quickie' as a temporary solution..

Again, and you have reiterated this often - J4 is an open process for ANYBODY to
submit papers. Where I find Pete's proposal positive is the multi-channel
dialogue from all interested parties in a SPECIFIC topic.

I'm curious - can you or Robert give feedback ? I know Robert (Jones) has
submitted several (many) suggestions, and it was convenient that the meeting was
in Newbury May/June 2000, so Robert could whistle up by car from Gloucester and
was party to at least some of the discussion. Just looking at paraphrased
minutes of meetings from the J4 archives doesn't tell you a great deal about
either acceptance or rejection of an idea. As opposed to Pete's 'open forum' -
what feedback does a submitter get from the current process. (Hey ! Other than I
*know* Thane took along copies of my comments on "Finalizer' - no feedback).

Then of course there's the ANSI/ISO boondoggle - though of course *IF* J4, (and
I'm referring to you, our own COBOL people, not the disinterested bureaucrats
that comprise ANSI and NCITS),  accepted Pete's e-mail approach as an effective
mechanism - don't see why this should get the ANSI organization into a tizzy.
Not just COBOL, but ALL languages would probably benefit from such an approach.
We have to get around the mindset that ANSI was initially set up to categorize
rules for things you can kick - nuts, bolts, the Materials tables I use etc.
Language whether spoken or written is a different ball game.

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 26)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-25T18:09:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106251709.36cfb798@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com>`

```
I think that most of the agitation for "reform" is coming from folks
who do not realize that relatively few of the papers considered, and
relatively little of the work done, involves brand-new proposals for
adding/changing/deleting features.  Most of it deals with fine-tuning
the standard for features already added/chaged/deleted.  For instance,
after all this work, it turns out that there is not an official
("normative") definition of RUN UNIT in the standard (and it is not a
waste of time; the undefined term may mean different things on
different platforms).  So there is a paper on providing a definition.
See
http://people.ne.mediaone.net/doncobol/01-0433.doc.
MOST of the papers are involved with tightening up the language and
definitions. We are writing a STANDARD. Take a look at the lists of
papers at
http://people.ne.mediaone.net/doncobol/.  There are links to each
paper, so you can see the kind of work that has to be done.

And locking in a feature once approved --- let me give you a
f'rinstance.  A couple of years ago, DYNAMIC TABLES were a hot item:
tables that could grow to the size of the available storage. All the
European groups wanted it, and it was popular in the US. I wrote a
paper to define the feature, and Don Schricker wrote a paper
tightening it up, which was approved.  A little later, compiler
writers started coming back to tell us that there was NO WAY they
could implement it EFFICIENTLY.  And they were using different
algorithms, so it wasn't just lack of imagination.   Accordingly, it
was backed out of the standard.  Stuff like that happens...

*------------

I am not defending the process as is, by the way.
ISO/IEC procedures are too secret and closed, and I think that all the
press releases asking for public comment on computer subjects are sent
to plumbing and textile publications....
*----------

Jimmy, your stuff on finalizer has not been acknowledged because J4
itself has not taken it up, or possibly Thane has not yet submitted it
as a paper.

We are still working on Josling's paper; the result of that will be a
good idea of how seriously we take outside ideas. I'll post the
address when it is ready.


Stephen J Spiro
Member, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 27)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-26T03:17:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B37FDD3.AD65D1FF@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com>`

```


Stephen J Spiro wrote:

>
> Jimmy, your stuff on finalizer has not been acknowledged because J4
> itself has not taken it up, or possibly Thane has not yet submitted it
> as a paper.
>

Just to clarify - I'm not DEMANDING an acknowledgement - that would be too
unwieldy. It's just that the open process that Pete refers to gives the
two-way traffic automatically so that you are au fait with what's going
down. At the end of the 'session' regardless of timespan it finishes up in
summary form.

>
> We are still working on Josling's paper; the result of that will be a
> good idea of how seriously we take outside ideas. I'll post the
> address when it is ready.
>

Excellent ! I'm sure Tim's comments are worth the effort.

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 27)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-26T23:19:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b386f31_1@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com>`

```
"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106251709.36cfb798@posting.google.com...
> I think that most of the agitation for "reform" is coming from folks
> who do not realize that relatively few of the papers considered, and
> relatively little of the work done, involves brand-new proposals for
> adding/changing/deleting features.  Most of it deals with fine-tuning
> the standard for features already added/chaged/deleted.

I want "reform" irrespective. The whole process stinks and it is time it was
overhauled.  The scenario I have outlined could be used to do fine tuning or
to write new technical papers, or to do "first cut" amendments to an
existing paper... It is not the subject that is wrong, it is the process. (I
have said this all along throughout this debate...) The process has failed
to deliver the goods; change the process.


>  For instance,
> after all this work, it turns out that there is not an official
…[10 more quoted lines elided]…
>
Definitions should be "Standards 101". How can a definition be missing after
all this time? Given that this is the case (and carefully putting away the
cat whip <G>) can you not see how a public debate on suggested definitions
could have led to acceptable definitions being proposed in the first place?
Remember, I am including the current committee members and the vendor
representatives as "public" in this sense. EVERYBODY has the right to
contribute and it is OPEN, so EVERYBODY can see the contributions and
comment or not.


> And locking in a feature once approved --- let me give you a
> f'rinstance.  A couple of years ago, DYNAMIC TABLES were a hot item:
…[8 more quoted lines elided]…
>
Again if your paper had been publicly posted in the appropriate thread,
EVERYBODY (not just you and Don (in this instance there is no implicit
criticism of the work done by you both)) could have seen what was being
proposed. This would include Vendor representatives who could have stated AT
THAT TIME that it would be very difficult to implement. No need to "back it
out afterwards", it would have been included or not depending on the
consensus.

If it was included, and vendors would not or could not implement it, then
they would need to state that their current implementation was lacking
(non-compliant with the approved ANSI standard) in this regard (first one to
do it steals a march on the rest and Market Forces do the rest...).

If the consensus was that it really was non effective and we could live
witout it, then it wouldn't be in the standard and everybody could move on
without losing sleep over it. The people who originally proposed it would
see it considered in a public debate and have to accept the outcome just
like everybody else, on any other issue.

How is that a problem?

> *------------
>
…[5 more quoted lines elided]…
>
In the light of this very fair comment, Stephen, I have ejected half the
magazine from my sniper rifle...<G>
(Seriously, it is gratifying to know that you are not attempting to defend
the indefensible.)

> Jimmy, your stuff on finalizer has not been acknowledged because J4
> itself has not taken it up, or possibly Thane has not yet submitted it
> as a paper.
>
Again, if it was in a public thread (NOTE: I am NOT saying a Download site)
it would already have undergone considerable scrutiny and public comment.
Why should it be incumbent on any J4 member to have to submit something
before it is considered?

> We are still working on Josling's paper; the result of that will be a
> good idea of how seriously we take outside ideas. I'll post the
> address when it is ready.
>
>
Personally, I don't care what you're working on or how seriously you take
it. I want it posted where we can ALL work on it and the results of this
work can make a DIFFERENCE to what goes in the Standard.

Pete.



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 28)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-26T13:08:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106261208.213378ab@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote 
> "Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
> news:4145699b.0106251709.36cfb798@posting.google.com...

> 
> >  For instance,
…[19 more quoted lines elided]…
> comment or not.
*----------------------
This particular item probably got caught when someone tried to
implement a feature that required the definition.  The need or lack
for the definition was simply overlooked by a lot of people.
These things are not JUST discussed in J4 and WG4.  Many people in
Vendor organizations and national groups (particularly the German and
Japanese) go over the standard in great detail.  Probably a lot more
people than participate in this Newsgroup are already reviewing the
standard.  Most of the work on mathematical operations, REPORT WRITER
and OO has been done by non-members of J4.  The process is actually
very open.  All documents are posted publicly at
http://people.ne.mediaone.net/doncobol/
and anyone can respond (the chairman's e-mail address is at the top of
the site).

*-------------------

> Again if your paper had been publicly posted in the appropriate thread,
> EVERYBODY (not just you and Don (in this instance there is no implicit
…[17 more quoted lines elided]…
> How is that a problem?
*-------------------
A whole bunch of compiler writers, THEMSELVES, participated in the
discussion.  It was not until they tried actually to implement it that
they realized the situation.
And, again, a whole lot more people than participate in this
Newsgroup, from all over the world, were involved in reviewing the
proposal.

*-----------------

I have always favored maximizing participation in the process.  I
think most of J4 monitors this Newsgroup, even if they do not all
participate.  When someone here brings up a substantive (not
procedural) issue with the standard, Bill Klein makes sure that the
issue is raised in e-mails to J4 members, and, if appropriate, an
official paper to the committee.

I'd like to have a comp.std.cobol newsgroup, but I am not in a
position to organize it.
 
I will propose to J4 that a special e-mail reflector be set up so that
ANYONE interested in following J4 can get the official mail ... and
maybe turn it into a discussion forum.
MEANWHILE, anyone who would like to get J4 official e-mail forwarded
to them, send ME your e-mail and I will do the forwarding.

Now, Pete, what are YOU going to do to open the process? <G>

Stephen J Spiro
President, Wizard Systems
Member, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 29)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-26T15:16:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9haqj4$ec3$1@nntp9.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com>`

```
Actually,  I was the one that discovered that there was no "current"
definition of a run-unit.  HOWEVER, there was a semi-(poor) definition of it
in the '85 Standard - but that text was moved from the "normative" text to
the "informative" text in the FCD.

I came across this "omission" in the FCD when trying to understand one of
the IBM comments (on GoBack) during the FCD US Public Review.

In general, the "world of definitions" has been (and IMHO continues to be) a
controversial one at J4.  This is due in part to

   - ISO rules that state that definitions ARE normative but may not specify
rules (and PLEASE don't ask me what this means)
  - J4 (and WG4) "desire" not to duplicate the same information in multiple
places in the Standard (as we tend to "miss" duplications when doing
maintenance causing conflicting information)
  - A "majority" (but FAR from consensus) view in J4 that the list of
definitions should be as SMALL as possible - as these are only suppose to
"explain" terms that are used in the COBOL specification in a manner that is
NOT what "common usage" would require.
```

###### ↳ ↳ ↳ Definitions vs. Index Entries in the FCD (was Re: comp.std.cobol)

_(reply depth: 30)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-06-26T15:49:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hb3hr$bl1$1@mail.pl.unisys.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <9haqj4$ec3$1@nntp9.atl.mindspring.net>`

```

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:9haqj4$ec3$1@nntp9.atl.mindspring.net...

> In general, the "world of definitions" has been (and IMHO continues to be)
a
> controversial one at J4.  This is due in part to
>
>    - ISO rules that state that definitions ARE normative but may not
specify
> rules (and PLEASE don't ask me what this means)
>   - J4 (and WG4) "desire" not to duplicate the same information in
multiple
> places in the Standard (as we tend to "miss" duplications when doing
> maintenance causing conflicting information)
>   - A "majority" (but FAR from consensus) view in J4 that the list of
> definitions should be as SMALL as possible - as these are only suppose to
> "explain" terms that are used in the COBOL specification in a manner that
is
> NOT what "common usage" would require.

This too was discussed at some length at the last J4 meeting (as it happens,
at least partly in response to a number of Tim Josling's comments requesting
more definitions).    I think there's more consensus on this subject after
the meeting than there may have been before it.

I tend to think that a fully-implemented index is at least as useful as a
glossary, particularly in those cases in which the "definition" of a term
involves the specification of rules.  If a "rule" of one of the various
categories adequately describes a term as used in the standard, and the
index for that term points to that rule, I don't see the need for a separate
glossary entry for that term containing the same information, and would
argue not only that such definitions not be added, but that those that might
be found to exist might well be deleted.

ISO's drafting rules mean that what is appropriate wording in one place is
not appropriate in another, and this in turn makes maintenance of both texts
a nightmare in the general case.  There were about 314 definitions in the
'85 standard, many of which were actually "rules" in the terminology of
ISO/IEC drafting rules.  This number grew to somewhere close to 500 in the
Draft process, and many of these have been weeded out (as duplicate
information, as erroneous definitions, as violations of ISO/IEC document
drafting rules, or as some combination of all three) so that the list in the
FCD stands at 189 definitions; ISTM the intent has been to ensure that those
that no longer appear in the "definitions" list are defined in the rules
themselves, and are properly indexed.

Given this "documentation design decision" (imposed at least in part by
those who are ultimately responsible for the content of the standard,
ISO/IEC), as I see it the *best* place to look for the definition of a term
is in the context in which the term occurs; the *second best* place is in
the *index* for other references where the term might be used; and only if
both of those "search algorithms" fail should one resort to the
"Definitions" list.   For those with "paper" copies, the index is not
difficult to find; for those with "paperless" versions, the appropriate
mouse clicks should get you where you need to be -- in fact, they are likely
to get you there more readily than searching Section 4 would!

In the case of "run unit", you're absolutely right, Bill, there's neither a
"Definitions" entry nor an "Index" entry for this term.

Page 6, section 3.3, "A conforming run unit", comes close to defining "run
unit"; *maybe* all that's needed is to have an index entry for "run unit"
that points to it.  If that's not complete enough, then perhaps some
clarification of wording in Section 3.3 would be appropriate.   I'm
personally uncomfortable with resolving the problem by adding an entry to
the "Definitions" chapter.

And in the general case:  for any given term whose meaning is not
immediately obvious, it seems to me that an index entry that points to
wording in the rules that describe the context and the use of the term
provides a more complete picture of the meaning and use of the term than
would a disembodied definition without any immediate context.    If the
rules need fixing because they're ambiguous, then let's fix the rules.   If
the problem is that the existing rules are adequate as they stand but aren
't cross-referenced clearly enough in the index, the more effective solution
is to improve the index.  Adding definitions to resolve an ambiguity in the
rules -- or even to avoid an ambiguity or lacuna in the index -- is by no
means a guarantee that the ambiguity is resolved thereby.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Definitions vs. Index Entries in the FCD (was Re: comp.std.cobol)

_(reply depth: 31)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-27T00:37:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B392A78.7362937D@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <9haqj4$ec3$1@nntp9.atl.mindspring.net> <9hb3hr$bl1$1@mail.pl.unisys.com>`

```


Chuck Stevens wrote:

>
> This too was discussed at some length at the last J4 meeting (as it happens,
…[3 more quoted lines elided]…
> <snip>

Lots of informative stuff, but of course those damned ISO rules again. For
simplicity, to me it would suggest a very, very COMPREHENSIVE index. Short and
sweet.

Coming new to a topic, say like learning Java  from a text, I may browse the
contents for an overall view  - but if I want to zero-in on something - the
index.

PS: Check out Local-Storage Section - is it adequately cross-referenced now ?
And that is no reflection on the Editor - it is a HUGE task.

Jimmy
```

###### ↳ ↳ ↳ Re: Definitions vs. Index Entries in the FCD (was Re: comp.std.cobol)

_(reply depth: 32)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-26T20:17:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hbc7l$upi$1@slb2.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <9haqj4$ec3$1@nntp9.atl.mindspring.net> <9hb3hr$bl1$1@mail.pl.unisys.com> <3B392A78.7362937D@home.com>`

```
Adding index entries is something that is VERY DEFINITELY "in order" at this
time of the FCD.  If you (ANYONE) has some index entries from the FCD that
they want added, please

    PLEASE

send them to the Project Editor at:

  donfnelson <at> aol.com

However, please do NOT send him a note saying something like
  "add more index entries"
      or
  "add the correct/more index entries for Local-Storage"

Instead, send him a note like

"Currently the index entry for
     Local-storage section
points only to page 243

I think you should also add entries pointing to:
    8.6.3 Automatic, initial, and static internal items
    C.4.2 Recursive and initial programs"

    or

"There is an index entry for
    STANDARD phrase
         arithmetic clause 186
  but there is no entry under the index entry
    Standard arithmetic
       pointing to 186
  I think that should be added."
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 29)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-26T21:09:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B38F9B1.CA5E4CCE@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com>`

```


Stephen J Spiro wrote:

> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote
> > "Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
…[19 more quoted lines elided]…
> Now, Pete, what are YOU going to do to open the process? <G>

Let's be realists Stephen.  Pete spends his 30 days (according to Skippy), goes
off into the wide blue yonder and set this thing up. Where do we go from there.
Unless J4 gets 'sold' on the idea it aint goin' nowhere. (Now here's where Pete
gets upset 'cos I mentioned J4). Simply this thing is not going to happen unless
there is some official 'blessing'. Maybe at some future stage we overcome the
ANSI/ISO dual nonsense - but for the moment our focal point is called "J4".

Chuck just wrote you are considering the case for examples. Prioritize this
J4-e-mail-forum as MOST URGENT for the very next J4 meeting - either concede that
it is a good idea, which has merit, and should be pursued in a timely fashion - or
just back-off.

I'm afraid 'some' do not take kindly to criticism - they have put long hours into
this J4 exercise. Unfortunately if somebody digs over my veggie plot, and from my
viewpoint, still leaves in a lot of weeds, should I congratulate him/her on a job
well done, rather than, "You might think you've done a good job, but I'm sorry, I
don't".

And to clarify that - you HAVE done a good job with a tremendous amount of effort.
But it does appear to have become 'business as usual', plod, plod, plod - 1985 -
2002.  The sense of urgency to keep up with other computer innovations just seems
to have slipped by COBOL. Add to that the stupid hurdles ANSI/ISO throw on the
running track to trip you up.

So... Next J4 Meeting - "Item 1 - Let's Involve the Whole COBOL community".

(To avoid any confusion - no buggering around with COBOL 2002 - keep going as is
to get it finished. The Item #1 is discuss the machinery, as to a viable model,
once COBOL 2002 is put to bed. It can then start to be implemented in say
Spring/Summer 2002 so that it could be the mechanism to arrive at COBOL 2004/5 -
if a wish list indicates changes).

PS: Something I should have said in response to Chuck's message about examples.
Note the FCD contains fairly exhaustive examples on Inspect/Replace - obviously
because that was considered a 'stinker' without some illustration.

OO is a bit in the same category - particularly the new syntax devoted to use of
classes/methods which are not as yet a part of Fujitsu or Micro Focus
implementations. I quickly looked at some of this stuff, (I can't currently use
it), and my response was, 'Duh....?" Somewhere, somehow, it can only be got across
to its intended audience by examples, either in the FCD or elsewhere. I haven't
looked - but really Screen Section is in the same category without examples. And
if I did use R/W - oh how I wish I could get my hands on that 1970-ish book that
went to great lengths with examples. Never did find it - one of the first
questions I asked here, and William K. immediately responded by searching for me -
no dice.

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 30)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-26T17:16:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hb1k3$tm3$1@slb0.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com>`

```
Just a matter to "consider".

It is my perception that some J4 members HATE "prolonged" discussions at J4
meetings (especially when it gets down to "detail junk").  Some of these
same people hate EVEN MORE email or electronic discussions that go on for
more than a note or two.

Therefore, my crystal ball (and it could be wrong) would say that you would
get "luke warm" at best reception for ongoing "electronic discussion"
procedures.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 31)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-27T00:48:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B392D14.DA69AFA@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net>`

```


"William M. Klein" wrote:

> Just a matter to "consider".
>
…[4 more quoted lines elided]…
>

To an extent I can understand where they are coming from. For the short while I
was on the J4 List, (which is about C-O-B-O-L), you can imagine I wasn't
terribly interested in getting messages throwing roadblocks in the way about the
next scheduled meeting because it conflicted with somebody's kid's bah mitzvah
or First Holy Communion !

Similarly while fascinated by WMK's comments on use of German re NLS - that
didn't turn me on either; it was a specialty item applicable to those
conversant. As you can imagine, your latest (copies via Stephen) about floating
point etc., left this rocket scientist dead cold - don't be offended, both items
are EXTREMELY important - but with no positive input to give, not to this
Johnny.

The 'prolonged discussions" that some may dislike should NOT occur at J4
'Summary' meetings. This is the whole objective of Pete's e-mail approach. Some
J4 members may be totally turned off by OO; why should they be subjected to a
long debate. Let those that are comfortable with the topic 'chew it to death'
and arrive at a set of conclusions - Then it is put forward in summarized form
to the J4 committee.

There's only one or two of us 'jumping up and down' about the process, I really
wish others could see that they should get involved. It is O-U-R language that
we use to earn our bread.

Things just have to change, nothing stands still. Here's an example from my boy
blue days. Various departments in the Air Ministry, London would make different
policy decisions, anything from bomb loading safety features, technical training
of various skills, medical, dental, aircrew training, promotion schemes, style
of uniforms, badges or rank  - just goes on and on. Similarly at Gloucester in
those days the RAF Record Office - archives for non-coms' records released
policy papers.

So based on the Air Ministry decisions, going to the keeper of the keys, they
would get an AMO (Air Ministry Order Number), next sequential number regardless
of topic. The Record Office used to do the same, (but here it's narrowed down to
non-coms) issuing ROMs, (Record Office Memoranda). So on an average week, you'd
get a bunch of AMOs, covering all sorts of topics, numbered AMO 123/59 through
AMO 127/59. You dutifully filed these bloody things in sequential order.
Problem, some six months later a query from a technical officer - "Can you turn
up the AMO that dealt with modifications to Vanguard staff cars ?". What a
bloody hopeless mess. BTW they never issued a subject index - though I think
they did just as I left for civvy street.

I nearly forgot - AMO  126/59, replaced AMO 789/57 - Rules about when not to fly
the Purple Airway - that is, don't get your damn plane in the Royal Flight Path
when Queen Lizzie is flying on HM1 !

Now any one of you guys/gals out there reading this, if you are worth your salt
in EDP, can probably offer at least six practical solutions to clarify the above
mess. Had I even intimated a change they would have put me before a firing squad
! The bureaucracy was so entrenched.

Commerce just doesn't stand still in its techniques - nor can procedures like
defining computer languages.

> Therefore, my crystal ball (and it could be wrong) would say that you would
> get "luke warm" at best reception for ongoing "electronic discussion"
> procedures.

Ouch  ! I'm sincerely hoping you are wrong and have 'mis-guessed' on this one.
If J4 really resist being the leader, what are the alternatives - "Man the
barricades ! Start a revolution ?". Or do all those kids silently slip away and
use C++ and Java - so that in  5/10 years time Gartner reports "COBOL users USED
to be 3 million, now they are down to 0.5 million".

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 32)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-27T16:50:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b396829_2@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net> <3B392D14.DA69AFA@home.com>`

```
Excellent post, Jimmy.

comments below...

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B392D14.DA69AFA@home.com...
>
>
…[4 more quoted lines elided]…
> > It is my perception that some J4 members HATE "prolonged" discussions at
J4
> > meetings (especially when it gets down to "detail junk").  Some of these
> > same people hate EVEN MORE email or electronic discussions that go on
for
> > more than a note or two.
> >
>
> To an extent I can understand where they are coming from. For the short
while I
> was on the J4 List, (which is about C-O-B-O-L), you can imagine I wasn't
> terribly interested in getting messages throwing roadblocks in the way
about the
> next scheduled meeting because it conflicted with somebody's kid's bah
mitzvah
> or First Holy Communion !
>
> Similarly while fascinated by WMK's comments on use of German re NLS -
that
> didn't turn me on either; it was a specialty item applicable to those
> conversant. As you can imagine, your latest (copies via Stephen) about
floating
> point etc., left this rocket scientist dead cold - don't be offended, both
items
> are EXTREMELY important - but with no positive input to give, not to this
> Johnny.
>
> The 'prolonged discussions" that some may dislike should NOT occur at J4
> 'Summary' meetings. This is the whole objective of Pete's e-mail approach.
Some
> J4 members may be totally turned off by OO; why should they be subjected
to a
> long debate.

That is PRECISELY the reasoning behind my proposal. And the fact that the
PUBLIC should not only NOT be excluded, it should be EASY for EVERYONE to
participate

>  Let those that are comfortable with the topic 'chew it to death'
> and arrive at a set of conclusions - Then it is put forward in summarized
form
> to the J4 committee.
>
Nope. I don't see it going to ANY committee for approval, only for
administering. The forum should be empowered to take decisions, based on the
post within a specified timeframe.

> There's only one or two of us 'jumping up and down' about the process, I
really
> wish others could see that they should get involved. It is O-U-R language
that
> we use to earn our bread.
>
Amen! The fact is that most of the User Base have been excluded for so long
they have given up on it.

As far as the "Official Standard" is concerned, so have I... with the
present procedures and in its present form I see it as an irrelevance.

However, I am certainly prepared to revise this opinion if some kind of move
is made to make it more OPEN, and actively encourage the participation of
the User Base with empowerment of this process.

<snipped stuff about RAF...makes you wonder how they ever won the Battle of
Britain...(Of course, they had a Kiwi running it...Air Vice Marshal Sir
Keith Park <G>) >
>
> Commerce just doesn't stand still in its techniques - nor can procedures
like
> defining computer languages.
>
Amen again!

> > Therefore, my crystal ball (and it could be wrong) would say that you
would
> > get "luke warm" at best reception for ongoing "electronic discussion"
> > procedures.
>
> Ouch  ! I'm sincerely hoping you are wrong and have 'mis-guessed' on this
one.
> If J4 really resist being the leader, what are the alternatives - "Man the
> barricades ! Start a revolution ?". Or do all those kids silently slip
away and
> use C++ and Java - so that in  5/10 years time Gartner reports "COBOL
users USED
> to be 3 million, now they are down to 0.5 million".
>
Exactly!

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 33)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-27T05:18:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B396C5E.E68D01AD@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net> <3B392D14.DA69AFA@home.com> <3b396829_2@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

> <snipped stuff about RAF...makes you wonder how they ever won the Battle of
> Britain...(Of course, they had a Kiwi running it...Air Vice Marshal Sir
> Keith Park <G>) >

One of my heroes - I wasn't there of course. Must have waltzed into his former
office many times in my last six months when the HQ 11 Group building,
(Hillingdon House, Uxbridge)  was the RAF School of Education. Christ ! You
telling me they actually produced something(body) useful in Kiwi land <G>

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 34)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-28T00:16:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b39cf9d_2@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net> <3B392D14.DA69AFA@home.com> <3b396829_2@Usenet.com> <3B396C5E.E68D01AD@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B396C5E.E68D01AD@home.com...
>
>
> "Peter E. C. Dashwood" wrote:
>
> > <snipped stuff about RAF...makes you wonder how they ever won the Battle
of
> > Britain...(Of course, they had a Kiwi running it...Air Vice Marshal Sir
> > Keith Park <G>) >
>
> One of my heroes - I wasn't there of course. Must have waltzed into his
former
> office many times in my last six months when the HQ 11 Group building,
> (Hillingdon House, Uxbridge)  was the RAF School of Education. Christ !
You
> telling me they actually produced something(body) useful in Kiwi land <G>
>
Well...yeah ...we've had a few. When we're not shagging sheep we get to
thinking, and doing... A few who are not immediately recognised as being
Kiwis (by people outside New Zealand...Of course, WE know who they are <G>):

Jean Batten - pioneer aviatrix.

Richard Pearse - pioneer aviator who is reputed to have developed powered
flight in 1903 about 6 months before the Wright Brothers, but never
Officially recognised (Probably had trouble getting an ANSI committee to
recognise his aircraft <G>)

Sir (later Lord) Ernest Rutherford - first man to split the atom.

Sir Edmund Hilary - first man to climb Mt. Everest (Sagamatha).  Shared with
Sherpa Tenzing Norgay.

Dame Kiri Te Kanawa - Opera singer.

Denny Hulme & Bruce McLaren - Legends of Motor Racing ...to  this day the
McLaren Team compete in Formula One.

Charles Upham - War Hero (First man ever to be awarded VC and Bar - Highest
award for Gallantry in the British Forces (akin to the US Congressional
Medal of Honour)...twice.)

In Sports of course, there are far too many to mention. For a Nation with
the population of  North London, we have a very disproportionate number of
names in the record books. I won't even start on Rugby and Sailing....

Guess who holds the America's Cup (arguably the highest Trophy for
International sailing), which was the "property" of the USA for 150 years?
(During the last defense of it, (some of which I went to Auckland and
watched) the US had a total budget in excess of $200,000,000 - latest high
tech designs, boats and gadgetry - we had 10% of that, a team of
enthusiastic amateurs (admittedly led by a couple of Kiwi professionals),
and some software written after school...<G>) The victory party went on for
a week and no-one in Auckland went to work...

I smiled at your mention of Hillingdon House in Uxbridge.

I worked on a fairly long computer contract for Rank Xerox in Uxbridge back
in the late seventies.

The U.K. Government had built a new Joint HQ (from which Margaret Thatcher
consulted with her War Cabinet daily during the Falklands crisis in '82)
which was reputed to have Nuclear shelters and life support etc. underneath
it, just on the edge of Uxbridge, and I used to drive past it every day. It
was an unbelievably ugly brick Building. I believe it has now been
decommissioned and opened to the public...could be an interesting tour...<G>

(See, even "Top Secret" establishments are being opened to the public, and
it hasn't yet brought about the downfall of Western Civilisation....J4
please note...<G>)

Pete.






Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 35)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-27T19:40:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3A3661.CAE46E07@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net> <3B392D14.DA69AFA@home.com> <3b396829_2@Usenet.com> <3B396C5E.E68D01AD@home.com> <3b39cf9d_2@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

> You
> > telling me they actually produced something(body) useful in Kiwi land <G>
…[4 more quoted lines elided]…
>

Shame on me - I should have remembered Kiri Te Kanawa and  Edmund Hilary. I
vividly recall the newscast while in Egypt in '53 - I believe his and  Sherpa
Tenzing Norgay's achievement of being the first to the top of Everest was
broadcast on the same day as the Queen's coronation. Then I reflected, could
also throw in Nyree Dawn Porter as the heroine in BBC TV's acclaimed, (on both
sides of the Atlantic), "Forsyte Saga".

Rutherford I didn't know about. The others didn't ring a bell.  Meanwhile howz
it goin' with the sheep - are you satisfied <G>

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 36)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-28T15:12:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3aa0ac_1@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net> <3B392D14.DA69AFA@home.com> <3b396829_2@Usenet.com> <3B396C5E.E68D01AD@home.com> <3b39cf9d_2@Usenet.com> <3B3A3661.CAE46E07@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message 

> Meanwhile howz
> it goin' with the sheep - are you satisfied <G>
> 
As you will have gleaned from my posts to CLC, I am NEVER satisfied...<G>

Pete.



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 32)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-26T23:17:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106262217.6dfe15e6@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net> <3B392D14.DA69AFA@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote 
> As you can imagine, your latest (copies via Stephen) about floating
> point etc., left this rocket scientist dead cold - don't be offended, both items
…[10 more quoted lines elided]…
> Jimmy

Those discussions about floating point in the e-mails between J4
members (and non-members -- Jordan Wouk is NOT a member, but he is one
of the two people to whom we refer the mathematical issues) means that
the issue will be settled rather quickly at the next J4 meeting. 
Consensus will have already been reached, and if Bill finishes his
paper early enough, there may even be some comments/discussion about
wording, and THAT may all be settled before the meeting.

I'll repeat my offer... anyone who wants to get J4 e-mails, and
possibly participate in the discussions, send me your e-mail address,
and I will forward them to you.  And I will bring up the issue of
putting all interested parties on the committee e-mail reflector.

Stephen J Spiro
Member, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 33)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-27T17:24:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3A168D.8A8F66A9@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net> <3B392D14.DA69AFA@home.com> <4145699b.0106262217.6dfe15e6@posting.google.com>`

```


Stephen J Spiro wrote:

>
> Those discussions about floating point in the e-mails between J4
…[6 more quoted lines elided]…
>

Excellent - you are consulting people who are not part of J4. But here's the real
point of Pete's proposal. You have a topic in which people have expertise, and as you
say "he is one of the two people to whom we refer.............". Wrong ! If you
include others including the academic community, those teaching COBOL, there may well
be 100 people who can join in the discussion as well as Jordan Wouk. Jordan may well
give you the right answers you are looking for - but a lively discussion by some 100
specifically interested in this particular topic, will allow you to arrive at a more
finite conclusion.

You've said you have a problem with OO - no shame in that. Why should you be an expert
on 'everything COBOL', or any other J4 member for that matter. I don't know whether or
not you use it but you may, plus others, have useful input on the Report Writer
module. I don't use it - but seeing what the 'topic group' says,  I could throw in,
"but for me to use it effectively on a PC,  I need............".

Let's take a pertinent thread at the moment - Multiple Inheritance in OO. Thane is
valiantly making a case for it. At the same time two others (or should that be three),

Grinder, Joe in Australia and Richard in New Zealand, to the best of my knowledge,
none of them using OO COBOL, are making sound observations on the topic. With people
like these, and presumably their conclusions are drawn from access to other OO
languages, we get a much more in depth discussion. Add to that mix those in the
academic world, (and there are a fair number promoting OO COBOL to their students in
the States),  a forum topic would give a much more detailed and conclusive result. The
net effect - we DO NEED multiple inheritance in COBOL, or 'interesting as a nice to
have, but we really DON'T need multiple inheritance'. It just makes sense to thrash
out the topic, addressed by a wider audience, rather than try and do it with the
willing few who comprise J4.

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 31)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-27T16:35:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b39648f_2@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com> <3B38F9B1.CA5E4CCE@home.com> <9hb1k3$tm3$1@slb0.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9hb1k3$tm3$1@slb0.atl.mindspring.net...
> Just a matter to "consider".
>
> It is my perception that some J4 members HATE "prolonged" discussions at
J4
> meetings (especially when it gets down to "detail junk").  Some of these
> same people hate EVEN MORE email or electronic discussions that go on for
> more than a note or two.
>
So why do they attend? Nice lunch? Paid time off work? Enjoy travelling?
<G>

Surely the goal is to produce a document, not to cater to the personal whims
of the attendees. If you don't want to be there, don't attend.

> Therefore, my crystal ball (and it could be wrong) would say that you
would
> get "luke warm" at best reception for ongoing "electronic discussion"
> procedures.
>
See, if these discussions were PUBLIC (by e-mail, as I have consistently
proposed) then they wouldn't HAVE to contribute would they? They could post
a note or two and move on to something else. Respond if they feel that
someone else's note is rubbish, but not get into prolonged harangues (unless
they want to...)

If you are right, Bill, and the general feeling is against "ongoing
"electronic discussion"", then it is because it is much more attractive to
sit round a table behind a closed door... That's why it's taken 10 years...
lots of sitting, not too much PERTINENT discussion... (yes, I know,
everybody has their own idea of what is pertinent, but this is another case
where a moderated NG is worth its weight in gold...start wandering off the
focus and Moderator waves red flag...)

Pete.




Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 29)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-27T16:18:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3960ef_2@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <4145699b.0106261208.213378ab@posting.google.com>`

```

"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106261208.213378ab@posting.google.com...

<snipped>
> Now, Pete, what are YOU going to do to open the process? <G>
>
Absolutely NOTHING as long as the process is powerless and REQUIRES the
approval of some faceless committee that meets behind closed doors.

Make it PUBLIC and EMPOWERED and I'll gladly participate.

(You knew I would say that so why bother...<G>)

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 28)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-26T13:34:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106261234.27455897@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:<3b386f31_1@Usenet.com>...
> 
> > Jimmy, your stuff on finalizer has not been acknowledged because J4
…[7 more quoted lines elided]…
> 

I submitted Jimmy's Finalizer paper and it's on the Finalizer Ad Hoc
agenda and has been for months.

Note: the reason for the submission is so that others have TIME to
review the items, the carefully CONSIDER them, and to ready questions
and opinions so that when the issue is raised, a carefully considered
position and argument can be presented.  To do otherwise would risk
knee jerk reaction and inclusion of ideas that are not well thought
out.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 29)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-26T21:33:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B38FF7B.CBC7E587@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com>`

```


Thane Hubbell wrote:

> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:<3b386f31_1@Usenet.com>...
> >
…[18 more quoted lines elided]…
> out.

Thane,

Good reply, re no knee-jerk reaction  - and note in my message to Stephen I was not seeking an
acknowledgement. At the current time just how often must we zip off to the J4 site to see 'what is'.
Surprisingly from the last time I looked - months ago - I assumed your TR was 'up and running' ! (As George
G. wrote, "It aint necessarily so").

Now this is one where I don't buy Pete's six-week timescale; it has to be 'eaten' then 'digested',
particularly as we know the other languages haven't been conclusive. But exactly what timescale is in mind
to make the Finalizer TR come to fruition ? I'm not going to look it up - but the 'Finalizer' topic has to
be more than one year old - too long.

I realize because of the HUGE list of enhancements/modifications currently under review plus comments back
on the FCD - 'Finalizer' is just one of many. That's why for the future there has to be a cut off to reduce
the number of topics being covered at any one point in time.

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 30)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-26T17:13:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hb1dg$rcb$1@slb7.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com>`

```
FYI - there has been ZERO action on FINALIZER for quite a while.  There was
a meeting with an Ad Hoc and some J4 discussion, but we have been waiting
(and waiting) for the FIRST draft of the TR for either J4 or Ad Hoc
discussion.

The "reason" (previously given) for this delay included work on the FCD
national body "studies" - but I don't think that I (at least) have seen any
change in its status since the international bodies had their "cut-off".

J4 is particularly bad (IMHO) in "multi-tasking".  It seems obvious to me
(and totally ridiculous to others) that we MUST be working on Finalizer and
Class Libraries *WHILE* finishing up the FCD (FDIS) work.  If we wait until
everything is "done" on the FCD to start work on the other items, then the
delay in "deliverables" will be unacceptable (yet again) in my opinion.

NOTE WELL: As implied above, this is NOT the common J4 opinion that seems to
think that we don't have the time/resources to work on finishing up one
thing at the same time we are progressing others.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 31)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-26T19:26:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106261826.1d6e1b52@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<9hb1dg$rcb$1@slb7.atl.mindspring.net>...
> FYI - there has been ZERO action on FINALIZER for quite a while.  There was
> a meeting with an Ad Hoc and some J4 discussion, but we have been waiting
…[19 more quoted lines elided]…
>  wmklein <at> ix.netcom.com


I have to disagree with Bill about reasons for the delay.  In the
first place, many of us on J4 do not have the expertise to participate
usefully in some of the OO discussions.  That is why the Finalizer and
Class Libraries have been assigned to Ad-hoc subcommittees.  The last
meeting of one of those ad-hocs was cancelled, I believe, for lack of
participation.
What did I say before? Not enough participation!

I am NOT involved.  I do NOT have the expertise. Bob Karlin was
heading up the effort, I believe.  I will send him a copy of this;
maybe he will post his e-mail address and an e-mail committee can be
established. Similarly, Thane Hubbell, I believe is in touch with an
OO COBOL e-mail discusssion group, but I do not know if this is an
open or closed group. Thane?

Stephen J Spiro
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 32)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-27T17:04:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b39c165_4@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com>`

```

"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106261826.1d6e1b52@posting.google.com...
> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:<9hb1dg$rcb$1@slb7.atl.mindspring.net>...
> > FYI - there has been ZERO action on FINALIZER for quite a while.  There
was
> > a meeting with an Ad Hoc and some J4 discussion, but we have been
waiting
> > (and waiting) for the FIRST draft of the TR for either J4 or Ad Hoc
> > discussion.
> >
> > The "reason" (previously given) for this delay included work on the FCD
> > national body "studies" - but I don't think that I (at least) have seen
any
> > change in its status since the international bodies had their "cut-off".
> >
> > J4 is particularly bad (IMHO) in "multi-tasking".  It seems obvious to
me
> > (and totally ridiculous to others) that we MUST be working on Finalizer
and
> > Class Libraries *WHILE* finishing up the FCD (FDIS) work.  If we wait
until
> > everything is "done" on the FCD to start work on the other items, then
the
> > delay in "deliverables" will be unacceptable (yet again) in my opinion.
> >
> > NOTE WELL: As implied above, this is NOT the common J4 opinion that
seems to
> > think that we don't have the time/resources to work on finishing up one
> > thing at the same time we are progressing others.
…[12 more quoted lines elided]…
> What did I say before? Not enough participation

What did I say before? Empower people, OPEN the doors and you'll get the
participation you desire. Maybe you missed my previous post...

Do you seriously expect people with high expertise to sit down and spend
hours (maybe even days) of unpaid labour preparing documents which will be
discussed without them being present, and can be dismissed out of hand with
no recourse, because the people writing them are not in the "club"?

It ain't gonna happen. (Well, certainly not as far as I'm concerned). Open
it up. Empower it. It'll happpen.


> I am NOT involved.  I do NOT have the expertise. Bob Karlin was
> heading up the effort, I believe.  I will send him a copy of this;
…[4 more quoted lines elided]…
>
Still misses the whole key point. Empowerment. Going through the motions
with accepting e-mail for consideration by a closed committe, is NOT the
same thing as an empowered public debate where the decisions voiced by the
forum are binding.

Still a long way to go...

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 32)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-26T22:07:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106262107.b238bfe@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com>`

```
Bill has been particularly good at stirring the pot lately.  Just to
set the record straight.

There was no Ad Hoc cancelled at the last J4 meeting - it simply
wasn't scheduled.  We have progressed to the point on Finalizer that
we think we have a consensus on all major issues raised.  Based on an
earlier proposal to change the base document to add Finalizers, and
with this direction, a base document Technical Report is being created
that we *should* have available for the Portland meeting and thus we
will be able to actualy scrutinize it and adjust it as necessary.

On the Class Library - work is ongoing.  Not wanting to recreate the
wheel, we are collecting old information that is presently only
available on paper and are getting it in an electronic format for easy
distribution and reading.  Also some J4 members are working -- with an
obviously lower priority than the present J4 work of reply to public
review comments -- on putting together a list of what other languages
and what various OO COBOL vendors offer for a common Class Libary.

To say the work is stalled is inaccurate.  To say we are not
multi-tasking is inaccurate.  We are prioritizing.  To say more
participants would help these two items *IS* partially accurate.  More
research in the class library area and more opinions on it would be
very helpful.  Finalizer opinions, in my opinion, should be held until
we have the base document Technical Report - and then the opinions
should be submitted.

I hope that helps clear the muddied waters.


stephenjspiro@hotmail.com (Stephen J Spiro) wrote in message news:<4145699b.0106261826.1d6e1b52@posting.google.com>...
> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<9hb1dg$rcb$1@slb7.atl.mindspring.net>...
> > FYI - there has been ZERO action on FINALIZER for quite a while.  There was
…[38 more quoted lines elided]…
> Stephen J Spiro
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 33)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-27T08:15:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hcm99$7l0$1@slb3.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com>`

```
As Stephen moved part of this discussion to the J4 distribution list and
Thane replied both to J4 and comp.lang.cobol, let me "repeat" what I sent to
J4 in reply to his note.


> -----Original Message-----
 <snip>
>
> There was no Ad Hoc cancelled at the last J4 meeting - it simply
…[10 more quoted lines elided]…
> to actualy scrutinize it and adjust it as necessary.

Even in the "out of context" quotation from Stephen, I never claimed that
any Ad Hoc was ever cancelled.   I think that it is important to state that
even at J4 and the Ad Hoc, the "consensus" was WITHIN J4 and one of the
things that was explicitly "called out" was the fact that the sooner a draft
TR could be DISTRIBUTED to the "public to get their input" the better it
would be.

I am (individually) unhappy with several of the "consensus" decisions (on
side-effects, auto-methods, etc) - but know that I don't think it "useful"
to comment on them until I actually see a draft TR.  My concern was (and is)
that we have been expecting this "first draft" of the TR for quite a while
now with "several" meetings at which it was "expected at the next meeting".
I hope it is available for the Portland meeting *and* that there is time and
resources for looking at it - and getting a version that can (unofficially
or officially) get some "outside" input and direction on whether the current
J4 consensus will or will not "hold up".

>
> On the Class Library - work is ongoing.  Not wanting to recreate the
…[10 more quoted lines elided]…
> multi-tasking is inaccurate.  We are prioritizing.

There may be "multi-tasking" going on somewhere, but it is NOT reflected in
the "recognized" J4 documents.  The "prioritization" *is* reflected in J4
output - but my personal view (which I have held since early in the revision
process) is that there simply isn't sufficient attention to what the
"implications" are in not doing "preliminary work" on the NEXT project while
continuing to do more active work on the "main" project.

I repeat what I have previously asked.
  If (for example) WG4 (via its convenor) does *not* initiate a "work item"
for a TR on Class Library this year, then what is the EARLIEST that a TR
might actually be delivered?

  ***

I did NOT post my original note in comp.lang.cobol "in the abstract" - it
was part of a thread on getting work done (and when things might be
expected).  I won't complain about Stephen deciding that it should go to the
entire J4 list, but I think that some of the "inaccuracies" in his reply
gives a pretty good impression of what is and is not actually understood by
J4 and its communication with the COBOL community.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 34)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-28T15:24:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3aa2c4_6@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net>`

```
It's becoming more apparent that the some of the J4 establishment are not
happy about public discussion of issues.

No wonder we are unlikely to see the Forum I am proposing.

Thanks for your post here, Bill.

It makes interesting reading.

Pete.

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9hcm99$7l0$1@slb3.atl.mindspring.net...
> As Stephen moved part of this discussion to the J4 distribution list and
> Thane replied both to J4 and comp.lang.cobol, let me "repeat" what I sent
to
> J4 in reply to his note.
>
…[18 more quoted lines elided]…
> any Ad Hoc was ever cancelled.   I think that it is important to state
that
> even at J4 and the Ad Hoc, the "consensus" was WITHIN J4 and one of the
> things that was explicitly "called out" was the fact that the sooner a
draft
> TR could be DISTRIBUTED to the "public to get their input" the better it
> would be.
…[3 more quoted lines elided]…
> to comment on them until I actually see a draft TR.  My concern was (and
is)
> that we have been expecting this "first draft" of the TR for quite a while
> now with "several" meetings at which it was "expected at the next
meeting".
> I hope it is available for the Portland meeting *and* that there is time
and
> resources for looking at it - and getting a version that can (unofficially
> or officially) get some "outside" input and direction on whether the
current
> J4 consensus will or will not "hold up".
>
…[14 more quoted lines elided]…
> There may be "multi-tasking" going on somewhere, but it is NOT reflected
in
> the "recognized" J4 documents.  The "prioritization" *is* reflected in J4
> output - but my personal view (which I have held since early in the
revision
> process) is that there simply isn't sufficient attention to what the
> "implications" are in not doing "preliminary work" on the NEXT project
while
> continuing to do more active work on the "main" project.
>
> I repeat what I have previously asked.
>   If (for example) WG4 (via its convenor) does *not* initiate a "work
item"
> for a TR on Class Library this year, then what is the EARLIEST that a TR
> might actually be delivered?
…[5 more quoted lines elided]…
> expected).  I won't complain about Stephen deciding that it should go to
the
> entire J4 list, but I think that some of the "inaccuracies" in his reply
> gives a pretty good impression of what is and is not actually understood
by
> J4 and its communication with the COBOL community.
>
…[4 more quoted lines elided]…
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 35)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-06-28T05:41:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0106280441.7e4cecb6@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com>`

```
Pete, 
I don't see how you reached that conclusion from this message. 
Stephen simply posted his reply to the J4 reflector - and I cross
posted mine - this lets J4 members who are not here benefit from this
conversation.

I'd like to set one other thing straight while I am here... About the
"cancelled" Finalizer meeting.  We scheduled an ad hoc meeting for
November 2000 via an internet meeting tool called WebEx - the meeting
was not cancelled due to lack of interest as was asserted but instead
because an individual demanded that we not have it because sufficient
"formal" notice of the meeting was not made (Two months in advance --
as NCITS rules require).  All of the participants knew about the
meeting and were ready to participate - there was no lack of interest.


"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:<3b3aa2c4_6@Usenet.com>...
> It's becoming more apparent that the some of the J4 establishment are not
> happy about public discussion of issues.
…[108 more quoted lines elided]…
>                 http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 36)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2001-06-28T22:41:13+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3B4209.765884F3@iinet.net.au>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com>`

```
Thane Hubbell wrote:
> 
> Pete,
…[13 more quoted lines elided]…
> 
But this is exactly the point about a News forum style formal
communication method. It does not require any of the participants to be
"together" at the same time. Also, if any one participant cannot
contribute immediately, they are free to contribute at a later time.

So, "Meetings" would not be required. What would be required, and I'm
not sure how to approach this, is to be able to collect votes on a topic
and to have a for each topic that is responsible for collating the
information from the posts and creating a formal votable specification.
I suspect the coordinator could be selected from amongst those
contributing to the general discussion via volunteer or possibly vote if
more than one volunteer steps forward.

Voting may require the use of some encryption to ensure that there is
only one vote per person. PGP could be used to achieve this, via using
it to create a public key and having the public registered with the
coordinator. Then you simply write a small text file containing YES or
NO and encrypt this with the PGP private key. You attach this file to a
News Article as an attachment, and hopefully, the coordinator can detach
the files. Then buy running the PGP public keys against the appropriate
files, we get the vote. Anything that does not decrypt correctly gets
binned as an invalid vote.

Thats the general drift. But how to impliment this in a news server, I
mot sure about. Maybe it's not required in the new server and the
coordinators have to take on the task at the time of the vote. To
register to vote, merely post your PGP public key against the topic to
be voted on.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 37)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-29T13:18:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3bd750_2@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com> <3B3B4209.765884F3@iinet.net.au>`

```
Joe,

I think what you're proposing is fine. I see no reason why PGP couldn't be
used to ensure that votes are authenticated. However, there are a number of
ways in which this COULD work.

Sadly, unless an empowered Forum is agreed to, we will never get the CHANCE
to vote (on anything).

When the Forum is in place, we could have a more pertinent discussion about
how voting should work...<G>

Pete.


"Joseph J Katnic" <josephk@iinet.net.au> wrote in message
news:3B3B4209.765884F3@iinet.net.au...
> Thane Hubbell wrote:
> >
…[45 more quoted lines elided]…
> Joe Katnic.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 36)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-28T16:31:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3B5B89.8461003E@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com>`

```


Thane Hubbell wrote:

> Pete,
> I don't see how you reached that conclusion from this message.
…[12 more quoted lines elided]…
>

Taking the facts as given, and IF it is a PHYSICAL gathering, then I can see you have to have a reasonable
notice period for intended participants to make travel/hotel arrangements, time off from work etc.. (I wont
define 'reasonable' here but two months would seem adequate).

IF as you are saying it was an electronic meeting, and here the point is convenience (or speed is of the
essence), then regardless I would have thought one month was adequate notice. To be caught up in NCITS
carved-in-stone rules is sheer BS.

With no detriment to the COBOL language - some of this bureaucratic BS must be challenged head on. It may
have had some validity back in the 1950s due to lack of communication techniques - but in the 21st century ?

Not your baby Thane - but possibly one Chuck or Bill could respond to - within the parameters of either
ANSI/ISO rules - is there anything stopping WG4 or J4 from 'customizing' the rules to suit the 'convenience'
of our COBOL committees ? (Unfortunately I think I already know the answer to that one - particularly as
some paper shuffler forgot to use a bring-forward card system to remind us COBOL '85 is 'technically dead'
'cos we didn't ask for a formal rubber stamp).

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 37)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-28T13:56:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hfulf$k03$1@slb7.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com> <3B3B5B89.8461003E@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B3B5B89.8461003E@home.com...
>
 <snip>
> Not your baby Thane - but possibly one Chuck or Bill could respond to -
within the parameters of either
> ANSI/ISO rules - is there anything stopping WG4 or J4 from 'customizing'
the rules to suit the 'convenience'
> of our COBOL committees ? (Unfortunately I think I already know the answer
to that one - particularly as
> some paper shuffler forgot to use a bring-forward card system to remind us
COBOL '85 is 'technically dead'
> 'cos we didn't ask for a formal rubber stamp).
>

I don't think there is ANYTHING that WG4 can do with the ISO rules.
However, J4 is allowed to add *additional* (more stringent) rules than ANSI.
Such "internal procedures" are reviewed by NCITS and "if approved" by them
become specific rules for the TC (technical committee).

J4 has one "long standing" modification that it does not allow abstentions
on "technical issues" (while NCITS does).  Currently we have a "new" rule
that is undergoing "review" and that concerns how many days you must attend
a meeting to meet the "attendance requirements".

There are *also* de facto "procedures". For example, (and this is slightly
relevant to this dicussion), J4 (for many years) has taken TWO votes on
motions during meetings where guests (non-members) are present or when more
than one person from the same company is present.  The first "unofficial"
vote reflects all present - while the "official" vote is that of the
members.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 38)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-28T19:09:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B3B80B7.D35E7B7F@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com> <3B3B5B89.8461003E@home.com> <9hfulf$k03$1@slb7.atl.mindspring.net>`

```


"William M. Klein" wrote:

> "James J. Gavan" <jjgavan@home.com> wrote in message
> news:3B3B5B89.8461003E@home.com...
…[28 more quoted lines elided]…
> members.

Thanks Bill.

Para 2. Not unreasonable - (1) 'We only have 'Yes' or 'No' in COBOL, no
'maybes'" (2) Attendance - "Are you taking this seriously ?".

Para 3 - I saw evidence of this whilst at Newbury.

Both the above are 'inernals'. But it's the logjam caused by the NCITS rule -
two months notice, when religiously applied to electronic meetings..

Jimmy
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 38)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-28T14:22:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106281322.1d04f3d@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com> <3B3B5B89.8461003E@home.com> <9hfulf$k03$1@slb7.atl.mindspring.net>`

```
Comments below.....

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<9hfulf$k03$1@slb7.atl.mindspring.net>...
> "James J. Gavan" <jjgavan@home.com> wrote in message
> news:3B3B5B89.8461003E@home.com...
…[28 more quoted lines elided]…
> members.

*--------------
Actually, J4 is usually very informal on the practical application of
the rules. If no one objects to the strict interpretation, we go with
what is expeditious.

Had no one objected to the notice rule, the meeting would have
proceeded as scheduled.

The J4 member who made the objection is a regular contributor here.  

Stephen J Spiro
Member, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 39)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-28T22:17:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hgrvl$1m7$1@slb3.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com> <3B3B5B89.8461003E@home.com> <9hfulf$k03$1@slb7.atl.mindspring.net> <4145699b.0106281322.1d04f3d@posting.google.com>`

```
Actually, the person who objected to that meeting, Ann Bennett, has NEVER
contributed to comp.lang.cobol - as far as I know.

Again, Stephen - I really suggest you "check your facts" before speaking on
such public issues.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 40)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-28T22:39:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hgt94$mbf$1@slb7.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com> <3B3B5B89.8461003E@home.com> <9hfulf$k03$1@slb7.atl.mindspring.net> <4145699b.0106281322.1d04f3d@posting.google.com> <9hgrvl$1m7$1@slb3.atl.mindspring.net>`

```
Correction (I think) I *may* have been the one confusing two things.

I think that Ann had a TAG meeting cancelled and I asked for an AGENDA that
was not posted the week before - for a FINALIZER meeting.

I publicly apologize to Stephen.
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 36)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-29T13:13:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3bd74d_2@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com> <3B38FF7B.CBC7E587@home.com> <9hb1dg$rcb$1@slb7.atl.mindspring.net> <4145699b.0106261826.1d6e1b52@posting.google.com> <bfdfc3e8.0106262107.b238bfe@posting.google.com> <9hcm99$7l0$1@slb3.atl.mindspring.net> <3b3aa2c4_6@Usenet.com> <bfdfc3e8.0106280441.7e4cecb6@posting.google.com>`

```
"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0106280441.7e4cecb6@posting.google.com...
> Pete,
> I don't see how you reached that conclusion from this message.
…[3 more quoted lines elided]…
>
OK, if it is as innocent as that, I withdraw my comment.

Then I have to ask: "If people in some other group are interested in what
goes on here, then why aren't they here?"

Pete.



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 29)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-27T16:55:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b39682f_2@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <3b373468_6@Usenet.com> <9h847s$ub7$1@slb6.atl.mindspring.net> <3B37A17D.8902B554@home.com> <4145699b.0106251709.36cfb798@posting.google.com> <3b386f31_1@Usenet.com> <bfdfc3e8.0106261234.27455897@posting.google.com>`

```

"Thane Hubbell" <thaneh@softwaresimple.com> wrote in message
news:bfdfc3e8.0106261234.27455897@posting.google.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:<3b386f31_1@Usenet.com>...
> >
> > > Jimmy, your stuff on finalizer has not been acknowledged because J4
…[3 more quoted lines elided]…
> > Again, if it was in a public thread (NOTE: I am NOT saying a Download
site)
> > it would already have undergone considerable scrutiny and public
comment.
> > Why should it be incumbent on any J4 member to have to submit something
> > before it is considered?
…[10 more quoted lines elided]…
> out.

And of course, they are doing this continuously over the months right? No
other distractions or work so there is no danger of a knee jerk when they
realise 2 days before it is due...? Like none of us have pulled all nighters
to get assignments done a day before they are due?

There is no reason why posts to a forum cannot be carefully considered
before being responded to, any more than allocating months before something
is raised in a committee leads to careful consideration.

Pete.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 23)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-26T00:56:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b373a10_1@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com>`

```
"Stephen J Spiro" <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106250026.60974186@posting.google.com...
> "James J. Gavan" <jjgavan@home.com> wrote
> <snip>
> > I really would like to see somebody
> > take up Pete Dashwood's idea - J4 e-mail sessions, separate threads per
> > topic, and as I added, monitored, NOT censored. >

When I saw this I got quite excited...

> The appropriate newsgroup is comp.std.cobol, which does not exist.  It
> needs a news-server on which to be set up.

This will cost. Not a lot ... well within the means of a non-profit making
organisation like ANSI. I would suggest using Usenet (they already support
over 90,000 NewsGroups, so one more really won't hurt..<G>)

> If anyone knows how to go
> about this, I will moderate it (hopefully, with a little {LOT!} help
> from my friends). Not the kind where messages go thru the sysop before
> being posted.... all I want to be able to do is delete off-topic
> posts.

Oh Really? The function of a moderator is to moderate. Yes, Off-topic
threads could be removed but only after they have been posted publicly and
the author of the post gets a chance to modify it to bring it back within
the boundaries of the Group. There have to be very clear and strictly
enforced rules as to what gets "moderated" and what the rules for posting
are... Furthermore, the Moderation should be undertaken on a roster of
Committee members and volunteers, rather than any one person.

Like I said, I got really excited about this as I thought it represented
real progress (I even took the 'scope off the sniper's rifle...)

Then I saw this...

> This would necessarily be informal, but I think most J4 members would
> tune in.
>

The key here is "informal". In other words, not recognised or acknowledged
as being part of the COBOL Standards process by J4. No power to actually DO
anything; the decisions still vested in a committee... the timescales still
decided by a committee.

In reality, it is a unilateral move on Stephen's part (and I respect him for
doing it) to try and show some willingness to include the hoi polloi in the
process, but without empowering them in any way or committing J4 or ANSI to
any kind of public answerability.

Here's what I would like to see:

1. An official ANSI/J4 forum that IS formal, controlled and run by the J4
chair, recognised as an ESSENTIAL part of getting the Standard out, and
moderated by delegated persons to ensure that the rules of the group are
kept to.

2. Separate threads for each section of the Proposed Standard, with
comments, suggestions, arguments, proposals accepted from anyone, anywhere
on the planet. (No particular qualification...it's just another way of
ensuring exclusivity and "membership" of an elitist club...). The emphasis
MUST be on OPENNESS and PUBLIC contribution.

3. A defined timebox for each thread during which submissions can be made.
At the end of that time, submissions are closed and the committee (with
volunteers) comb through the posts and arrive at a consensus regarding the
points raised in each thread. If there are no posts, then it will be assumed
that the proposed standard (in this area) is acceptable. Silence constitutes
acquiescence. Submissions are summarised and posted as the "result" with the
Standard text which has been altered, added or deleted, as a result of the
public submissions.

No timebox should be greater than 6 weeks from the time the Draft is
available (as it is currently available, this would mean from the time the
server is up and running the new forum.)

4. Where there is dissension or controversy, the disputed points are put to
a public vote through the same forum. The majority rule. In the event of a
tie (or no submissions) the Chair of J4 decides. (Votes are collected
through the forum over a 14 day period).

5. Procedures in ANSI are changed so that, once this process has completed,
the Draft cannot be amended or changed. In other words, the decisions taken
from the public submissions are binding and cannot be reversed by ANSI or an
yone else.

6. Where Technical Reports are required, the need for them would be posted
publicly and contributions solicited. These contributions then form the
basis of the new draft. It is exactly the same principle as outlined above.
Existing members of the committees have the same right as everyone else to
contribute.

Vendors can assign their own representatives to present their Company
perspective in the Forum.

The difference is that it is a PUBLIC process. In many ways this can make it
faster because there are more people able to contribute easily via the Net.
There is then no real need for a "committee" at all. All that is required is
a "pool" of moderators and a Chair to hold a casting vote. These could be
elected (at the moment they are an unelected "elite") by the contributors to
the forum. This ensures that there is no financial qualification to be a
part of COBOL's future (buying membership of ANSI and attending the
boondoggles are options which are NOT open to ALL; what we want is something
that IS open to ALL and is SEEN to be open to ALL. It is then likely that
the user base may actually participate...)

Can you imagine the CREDIBILITY the ANSI standard would have if it were seen
to be administered in this way? No-one could argue with it. Democracy in
action.

Think about what credibility it has at the moment...could any alternative
actually be worse?

What is so difficult or unreasonable about this?

Pete.
>
> Anyone out there can help.
>
Yes, Stephen, but only on your terms...(I don't mean you, personally). Your
move is a good one, but people need to know they can make a difference.
"Necessarily informal" just doesn't cut it...well, not for me anyway.


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 23)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-06-25T10:18:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EDBD9E4493AE4F2D.A91F049E0C43714F.A015021E570CEC9E@lp.airnews.net>`
- **References:** `<3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com>`

```
On 25 Jun 2001 01:26:09 -0700, stephenjspiro@hotmail.com (Stephen J
Spiro) enlightened us:

>"James J. Gavan" <jjgavan@home.com> wrote
><snip> 
…[30 more quoted lines elided]…
>Anyone out there can help.

You do not need to pay to set up a news group.  The trick is to get
the major news group organizations (Airnews, Giganews, Supernews etc.)
and ISP's who keep newsgroups to carry it.

Vist www.isc.org for some background info.  Spend some time in
newsgroups alt.how.to.create.a.newsgroup and alt.config.

You'll need to write a charter and you'll need to write a proposal
which must be debated (usually in alt.config for 7-14 days).  Once it
is approved, you'll send out a control message that will cause the new
newsgroup to be created on all those places I mentioned previously.  

That's a very brief summary of how it is done.  Visit the places I
mentioned and do a little research.  Creating a moderated newsgroup
could take a little longer.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

My girlfriend told me I should be more affectionate.  
So I got two girlfriends.

DON'T DRILL in the Artic National Wildlife Refuge
Read the real facts at:

http://www.worldwildlife.org/arctic-refuge/

also

http://www.savepolarbears.org/


Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 24)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-25T11:38:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106251038.6d0653f8@posting.google.com>`
- **References:** `<3b2851b0_6@Usenet.com> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <EDBD9E4493AE4F2D.A91F049E0C43714F.A015021E570CEC9E@lp.airnews.net>`

```
SkippyPB <swiegand@nospam.neo.rr.com> wrote 
> 
> You do not need to pay to set up a news group.  The trick is to get
…[15 more quoted lines elided]…
> Regards,

Thank you, SkippyPB!

Ho-wily sheet! I quickly browsed thru some of those links (and their
links)... this is a major project, takes months, there is a procedure
with a bureaucracy (you would love it, Pete Dashwood), and I still
haven't found how to get a news-server to "sponsor" (I'm sure that is
not the right word, but I mean be the official place where it is, and
where the old messages are stored) it.  I'm sure the info is in there,
along with much of which I haven't even thought.

This would be a good Master's project for a graduate student in
Computer Studies. Or an ambitious undergraduate.

I'm sorry, guys and ladies, but I am not in a position to do this on
my own....
I'm not even in a position to co-ordinate the effort.  But if someone
else wants to co-ordinate, I will offer enthusiastic help!

IF there is a fee/cost by an ISP to host (That's the word!) a
newsgroup, I MAY be able to help with getting some commercial support.

Ideas, anyone?

Stephen J Spiro
Memeber, J4 COBOL Standards Committee
```

###### ↳ ↳ ↳ Re: comp.std.cobol

_(reply depth: 25)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-06-26T11:42:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A2B8627753488E08.E067D4C7ADDD602B.DF02FA5B8A672621@lp.airnews.net>`
- **References:** `<3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com> <4145699b.0106241500.70eaab63@posting.google.com> <3B36CE91.2B69584E@home.com> <4145699b.0106250026.60974186@posting.google.com> <EDBD9E4493AE4F2D.A91F049E0C43714F.A015021E570CEC9E@lp.airnews.net> <4145699b.0106251038.6d0653f8@posting.google.com>`

```
On 25 Jun 2001 11:38:53 -0700, stephenjspiro@hotmail.com (Stephen J
Spiro) enlightened us:

>SkippyPB <swiegand@nospam.neo.rr.com> wrote 
>> 
…[27 more quoted lines elided]…
>

It's possible a "moderated" newsgroup would need a central place for
its messages to be stored and then sent out from there.  I'm not sure
about that.  My feeling, knowing the way newsgroups work, is all
messages are sent to the moderator who posts to whatever ISP or
newsgroup agency he belongs to.  Again, no fee, other than your normal
connect fees, would be due.

FYI, newsgroups work off of a peerage system.  ISPs and the major
newsgroup agencies all subscribe to feeds from each other and from
other sources.  This is how messages get propagated.  However, not all
news groups are carried by everyone.  For example, my ISP carries over
60,000 newsgroups.  But Airnews, my newsgroup server, carries only
around 45,000.  So to create a newsgroup and have it propagated
everywhere is no mean feat, but it can be done.

>This would be a good Master's project for a graduate student in
>Computer Studies. Or an ambitious undergraduate.
…[10 more quoted lines elided]…
>

Actually, it should take you no more than 30 days to do this and this
is not doing it full time.  The hardest part is writing the charter
and the proposal.  Then, if no one at ALT.CONFIG strenuously objects,
your good to go.

>Stephen J Spiro
>Memeber, J4 COBOL Standards Committee

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

My girlfriend told me I should be more affectionate.  
So I got two girlfriends.

DON'T DRILL in the Artic National Wildlife Refuge
Read the real facts at:

http://www.worldwildlife.org/arctic-refuge/

also

http://www.savepolarbears.org/


Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 20)_

- **From:** "Russell Styles" <rwstyles@worldnet.att.net>
- **Date:** 2001-06-25T04:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h6zZ6.8970$3d3.705286@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3b2a1e9f_5@Usenet.com> <4145699b.0106151512.327040a4@posting.google.com> <9gggn6$dji$1@slb0.atl.mindspring.net> <6K4Z6.2203$f4.99834@e420r-atl1.usenetserver.com> <3B34F9C9.A2EE42C2@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B34F9C9.A2EE42C2@home.com...

<snip>

> The Ayan Rand quote is not strictly true. COBOL with a
committee of
> vendors and the D of D was conceived in 6 MONTHS - obviously
not all the
> whistles and bells we are familiar with to day - but
nevertheless a
> REMARKABLE ACHIEVEMENT.
>

    As someone once said (more or less), nothing focuses your
attention like the knowledge that you are to be
hanged in the morning.

    Was the original COBOL developed during a war?




<SNIP>
```

###### ↳ ↳ ↳ Draft Standard (was: many other things.....

_(reply depth: 15)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-15T19:30:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2A632E.D75F1489@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com>`

```


Stephen J Spiro wrote:

> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote
> >
…[7 more quoted lines elided]…
>

OK - I sense your frustration Stephen and I understand. In response to Pete's
reference to my 'agree and disagree" I am preparing, I regret, a very LONG answer
to cover the topic, I hope impartially, and then shut up - simply because I don't
see a chance of anything changing.

Back to your frustration. You got into COBOL in '75 having been tutored in
Structured. Although considerably older than you, yours truly got into COBOL out
of necessity - to earn a living. So I taught my self starting in 80/81 with
RM/COBOL '74 for Radio Shack clunkers Model II.

As you can imagine I produced some of the best spaghetti outside of Italy ! Got
the message eventually, from Dan McCracken's 'Structured COBOL'. This all
Do-It-Yourself stuff, and surprise, surprise, I think I'm on the same wavelength
as you in your message about a structured program. No genius, but not bad for
somebody working in pure isolation without peers to converse with. Remember, back
then no Internet and no technical support. RM/COBOL may or may have not mentioned
X/Open - if they did what the hell was that ? Where, in those days could I even
speculate there might be a resource covering the topic.

Involvement with the Internet - roughly some 5 years ago as a result of wanting to
keep up-to-date on M/F's VISOC - that's when I 'met' Pete - through the Micro
Focus CompuServe forum, and Michael M. I should also add.

Zowee ! The global village, the world is your oyster. Look at all the info you can
get. You've got a problem, and here is somebody who can offer a solution, or even
have the same or differing opinions on a topic.

It must be absolutely frustrating for both J4 members, and equally for COBOL
compiler vendors that some of us come across as so negative. Take the vendors,
"Jeepers, we offer these guys the best we can think up, and all the bastards do is
gripe and complain". If you think back to when Warren Simmons and Gracie were
involved with COBOL - there wasn't even an electric typewriter - the nearest
automation was Morse code, the telephone or a teleprinter. As regards COBOL that
means committees as such were working in a vacuum, (not intentionally) but the
'communication tools' just weren't available. OK there was written user feedback -
but absolutely MINIMAL compared to what we can now achieve with the Net.

So back to this NewsGroup - it became a real eye opener. I've designed for
mainframes but not programmed for them. Similarly, a tremendous amount of
information emanating from Bill and insights into the mechanics of J4 and its
boondoggle partners. Note he was the only human 'mouthpiece', who bothered to get
involved with CLC from J4, primarily because of his passion for the language.
(Much gritting and gnashing of teeth from some on J4 when you mention the WMK
initials - we should all toe the party line, and speak without dissension - right
?)  I welcome with enthusiasm your contributions now, and Chuck's - just so long
as he doesn't throw a list of those bloody ISO/ANSI committee names at me !

So vendor processes, and yours (J4) have gotten more sophisticated as time goes
on. Although as I have previously noted, there was no take-up on John P's
suggestion about more e-mailing and teleconferencing, instead of the air travel,
hotel accommodation etc.

Touching on that one and your reference to no Canuck on J4 - I got in touch with
'our' man because of Bill. Story is - he was sick for quite a while and working in
Canada for an American company. Health back, he returned to work - to find a
completely deserted building - they hadn't even bothered to tell him they shut up
shop. (I've referred elsewhere to the rapacious, inhuman attitude of modern
commerce). I can confirm his story - initially I phoned his supposed office, a
ringing tone but no reply. In their haste to clear out, they did everything but
get the phone disconnected.

So he gets a new job - can hardly immediately turn around to his new employer and
say, "Do you mind if I have time off to attend J4 meetings ?" Even if he got such
a concession, he would still have to pick up the tab for membership and expenses.

Both you and vendors may have gotten more sophisticated - but in exactly the same
way, so have we. We have insight into what is going on and as regards the time
frame  some of us just don't accept the concept of the only major change for COBOL
being in the time frame 1985 - 2002. You can manipulate those 17 years as much as
you like, to reduce it, but not just here in CLC,  I can assure you there are
others, certainly in the States,  who view the long time factor as unacceptable.

I've done my penance on committees and have absolutely no interest at this point
in my life in getting involved in such a frustrating exercise. However, note, that
although no COBOL'guru' I'll willingly offer my two cents for the bits that I use
and have a little familiarity with - namely OO. But not at committee level ! I had
speculated, way before Newbury, that long sessions would likely leave the
participants feeling mentally like wet rags. Seeing the last days of that joint
J4/WG4 session at Newbury - I don't think I was far off the mark. I doubt anybody
went away with bubbling enthusiasm, and probably it was more a feeling of 'Oh hum.
And when/where is our next meeting to be held....."

How blunt must I be ? Having been there - committees - voluntary, charity,
commercial, or technical - the objectives and enthusiasm to push forward has to
come from the top. When your chairman is on record as saying "It hasn't really
been that long........". Check it out - Mike Sheehan's Dissertation on COBOL, one
of the appendices - available at cobolreport.com. Mike's question wasn't loaded,
he was making a logical observation.

Now I'll agree with you - Pete stop taking potshots from the sidelines and
replying with witty ripostes. Get involved ! But Stephen, like me he ISN'T going
to get involved in a committee. But given the opportunity I'm damn certain he
would contribute to a properly Standards focused forum, broken down into separate
threads, impartially monitored but NOT CENSORED. E-mail represents a rapid way of
getting heated, lively and relevant discussion going on a topic - doesn't involve
a teremendous cost nor does it need a gathering of the clans to formally discuss
issues. Have your committee meetings if you must - but they should be a
rubber-stamping session devoted to the results obtained from the e-mail
discussions, which of course are summarized into formal proposals/specifications..

As to Pete's second suggestion - Horace Rumpole from Illinois scotched that one -
although Pete doesn't buy it. So Big Blue has this whole bevy of high-priced legal
sharks keeping them on the right tracks. They like the 'Kiwi suggestion'. "Whoa
!", scream their hired suits. "Anti-trust, monopolistic, etc. etc....."  IBM would
have to be out of their minds not to take the advice. Can't you just see some
bright eyed, bushy tailed kid trying to make a name for himself in the legal
profession, prosecuting Big Blue all the way to the US Supreme Court. He would
absolutely salivate at the thought of getting the head of the IBM CEO on a silver
platter, just like John the Baptist !

We need disagreement to arrive at agreement.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Draft Standard (was: many other things.....

_(reply depth: 16)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-16T20:49:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2b1d25_6@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3B2A632E.D75F1489@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B2A632E.D75F1489@home.com...
>
> OK - I sense your frustration Stephen and I understand. In response to
Pete's
> reference to my 'agree and disagree" I am preparing, I regret, a very LONG
answer
> to cover the topic, I hope impartially, and then shut up - simply because
I don't
> see a chance of anything changing.
>

I have no problem with you (or anyone else) "agreeing or disagreeing" as
long as you you are specific about what it is you agree/disagree with. When
you say "some of your post" ...then you have really managed to say nothing
of any use. Why comment at all if you are not prepared to adopt a position
on something or seek clarification? That's what I mean by "lukewarm chicken
soup"...bland, watery, with no substance to it, intended as a mollifying
palliative...

<snipped interesting but not really pertinent walk down memory lane...>
(BTW Jimmy, I reckon Daniel MacCracken's book on COBOL was the WORST one I
ever read. Sadly it was the required reading for the COBOL course at
Auckland Tech (I was never on this course but I had to "repair" a number of
people who were...<G>). OK, to be fair, it suffered by comparison to other
books (like McCameron's).

>
> It must be absolutely frustrating for both J4 members, and equally for
COBOL
> compiler vendors that some of us come across as so negative. Take the
vendors,
> "Jeepers, we offer these guys the best we can think up, and all the
bastards do is
> gripe and complain". If you think back to when Warren Simmons and Gracie
were
> involved with COBOL - there wasn't even an electric typewriter - the
nearest
> automation was Morse code, the telephone or a teleprinter. As regards
COBOL that
> means committees as such were working in a vacuum, (not intentionally) but
the
> 'communication tools' just weren't available. OK there was written user
feedback -
> but absolutely MINIMAL compared to what we can now achieve with the Net.
>

Exactly. And apparently these 1940s methods are still OK for  some
quarters...

> So back to this NewsGroup - it became a real eye opener. I've designed for
> mainframes but not programmed for them. Similarly, a tremendous amount of
> information emanating from Bill and insights into the mechanics of J4 and
its
> boondoggle partners. Note he was the only human 'mouthpiece', who bothered
to get
> involved with CLC from J4, primarily because of his passion for the
language.
> (Much gritting and gnashing of teeth from some on J4 when you mention the
WMK
> initials - we should all toe the party line, and speak without
dissension - right
> ?)  I welcome with enthusiasm your contributions now, and Chuck's - just
so long
> as he doesn't throw a list of those bloody ISO/ANSI committee names at me
!
>

Well, you'd hardly expect an elite group like the Guardians of COBOL to come
and mix it up with the hoi polloi in CLC now, would you <G>?
(In reality, I agree it is good to see people like Chuck and Stephen
contributing here (whether I agree with them or not). As I have always said,
my objections are not personal. "I may not agree with what you say, but I
shall defend until Death your right to say it..."

> So vendor processes, and yours (J4) have gotten more sophisticated as time
goes
> on. Although as I have previously noted, there was no take-up on John P's
> suggestion about more e-mailing and teleconferencing, instead of the air
travel,
> hotel accommodation etc.
>
Er... I have been saying that for a very long period now, both here and in
certain other forums. Funny how I received the same response as John... It
doesn't need teleconferencing even; it could be done on the Net just as this
exchange is being posted on the Net.


> Touching on that one and your reference to no Canuck on J4 - I got in
touch with
> 'our' man because of Bill. Story is - he was sick for quite a while and
working in
> Canada for an American company. Health back, he returned to work - to find
a
> completely deserted building - they hadn't even bothered to tell him they
shut up
> shop. (I've referred elsewhere to the rapacious, inhuman attitude of
modern
> commerce). I can confirm his story - initially I phoned his supposed
office, a
> ringing tone but no reply. In their haste to clear out, they did
everything but
> get the phone disconnected.
>
> So he gets a new job - can hardly immediately turn around to his new
employer and
> say, "Do you mind if I have time off to attend J4 meetings ?" Even if he
got such
> a concession, he would still have to pick up the tab for membership and
expenses.
>
I'd love to be on the Committee that decide what the "membership" is going
to cost...

("So what d'you reckon the traffic will bear this year?  Well, we have a
number who are busting a gut to write "ANSI Committee Member" on their CVs
(apparently, it's worth money...) so let's try $1000 bucks for openers...
Too steep? Naw...with our credibility they'll pay it gladly...Where the
Hell's that lunch we ordered...") -
<disclaimer>
The preceding conversation is entirely a figment of my tortured imagination
and bears no similarity to actual conversations which may or may not have
taken place behind the walls of ANSI. This is simply another unworthy
potshot at an Organisation we all realise is doing a fantastic job (just ask
them...).
</disclaimer>

So ANSI is a non-profit Organisation purely through mis-management <G>? Or
is it because once you hide the profit by creative accounting, you come out
with none?

Oops, I forgot the overheads of running a business based around volunteers
who either pay their own expenses or get their employer to sponsor them,
must be horriffic...no wonder the cost of getting copies is so high...

> Both you and vendors may have gotten more sophisticated - but in exactly
the same
> way, so have we. We have insight into what is going on and as regards the
time
> frame  some of us just don't accept the concept of the only major change
for COBOL
> being in the time frame 1985 - 2002. You can manipulate those 17 years as
much as
> you like, to reduce it, but not just here in CLC,  I can assure you there
are
> others, certainly in the States,  who view the long time factor as
unacceptable.
>

Gorn! And I believed I was the ONLY one...

The problem of course is what we can realistically do about it.

And No, Stephen, joining the Legion of the Damned is NOT an option (any more
than joining Arthur Andersen is...<G>). When the enemy has overrun your
country, has you surrounded, out resourced, outmanned, and outgunned, the
ONLY option is guerilla warfare...potshots, quick raids, harassment. Until
you can hopefully turn the tide of opinion and start a revolution which will
bring real change. Only when I am totally satisfied that that is never going
to happen, will I drop this. As long as other people feel (like me) that it
is "unacceptable" I'll be here...

> I've done my penance on committees and have absolutely no interest at this
point
> in my life in getting involved in such a frustrating exercise. However,
note, that
> although no COBOL'guru' I'll willingly offer my two cents for the bits
that I use
> and have a little familiarity with - namely OO. But not at committee level
! I had
> speculated, way before Newbury, that long sessions would likely leave the
> participants feeling mentally like wet rags. Seeing the last days of that
joint
> J4/WG4 session at Newbury - I don't think I was far off the mark. I doubt
anybody
> went away with bubbling enthusiasm, and probably it was more a feeling of
'Oh hum.
> And when/where is our next meeting to be held....."
>
> How blunt must I be ? Having been there - committees - voluntary, charity,
> commercial, or technical - the objectives and enthusiasm to push forward
has to
> come from the top. When your chairman is on record as saying "It hasn't
really
> been that long........". Check it out - Mike Sheehan's Dissertation on
COBOL, one
> of the appendices - available at cobolreport.com. Mike's question wasn't
loaded,
> he was making a logical observation.
>

I didn't know that. <lapses into humble silence...>

> Now I'll agree with you - Pete stop taking potshots from the sidelines and
> replying with witty ripostes.

Yeah, you're right, I should try some stupid ripostes...there is no place
for wit in CLC <G>


>Get involved !

Er...do you think I spend time writing these posts because I'm NOT involved?
Save your motivational aphorisms for your local Church Committee...when I
want your opinion I'll give it to you <G>.

>But Stephen, like me he ISN'T going
> to get involved in a committee.

You got THAT right...!!! (Well, not the Committees we currently see in ANSI.
I am currently a member of 2 committees  (until recently, 3) and they are
all achieving their goals and serving their Membership.)

> But given the opportunity I'm damn certain he
> would contribute to a properly Standards focused forum, broken down into
separate
> threads, impartially monitored but NOT CENSORED. E-mail represents a rapid
way of
> getting heated, lively and relevant discussion going on a topic - doesn't
involve
> a teremendous cost nor does it need a gathering of the clans to formally
discuss
> issues.

Very high probability I would contribute to something like this, if asked.

> Have your committee meetings if you must - but they should be a
> rubber-stamping session devoted to the results obtained from the e-mail
> discussions, which of course are summarized into formal
proposals/specifications..
>

Nope. We part company here. That would mean the actual "power" to do
anything would still be vested in the Committee and the rest of it would
simply be lip service. I know you said "rubber stamp" but without it, it
wouldn't be valid, so that is real power.

I have found from managing RAD projects that things happen when the
hierarchical power structure is truly delegated down to the people doing the
job. There is no stopping an enthusiastic shop floor which has been
genuinely empowered. The boundaries of this power are very clearly defined
(and often surprisingly liberal, especially in organizations which are known
for their Conservatism), but within those limits, decisions made by the
Project Team do not get reversed by ANYBODY.

> As to Pete's second suggestion - Horace Rumpole from Illinois scotched
that one -
> although Pete doesn't buy it.

Sorry...I do buy what Bill says on this, I just don't see how it could apply
to an OPEN public discussion.

> So Big Blue has this whole bevy of high-priced legal
> sharks keeping them on the right tracks. They like the 'Kiwi suggestion'.
"Whoa
> !", scream their hired suits. "Anti-trust, monopolistic, etc. etc....."
IBM would
> have to be out of their minds not to take the advice. Can't you just see
some
> bright eyed, bushy tailed kid trying to make a name for himself in the
legal
> profession, prosecuting Big Blue all the way to the US Supreme Court.

It's been done. A man named Bill Norris (CEO of Control Data Corporation at
the time) brought an anti-trust suit against IBM  in the 70s, despite
emphatic legal advice from his Corporate people NOT to do so. He won (it was
the FIRST time EVER that anyone had ever successfully sued IBM), and IBM
paid hundreds of millions, picked up CDC's R & D budget for several years
and signed over their entire US Dial-360 network. (To IBM it was petty cash,
but I still remember the party in Minneappolis...)

The point about law suits is that if you have a case you try it. If you
don't, then you don't.

>
> We need disagreement to arrive at agreement.
>

Oh, I certainly don't agree with that...<G>!!!

Pete.



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Draft Standard (was: many other things.....

_(reply depth: 17)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-16T21:42:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2BD381.56BFFDC@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3B2A632E.D75F1489@home.com> <3b2b1d25_6@Usenet.com>`

```


"Peter E. C. Dashwood" wrote:

> I have no problem with you (or anyone else) "agreeing or disagreeing" as
> long as you you are specific about what it is you agree/disagree with. When
…[5 more quoted lines elided]…
>

Be patient you SOB <G>. I actually do some program coding as well as write here.
I will send when ready  - and it is my personal view, not necessarily Pope
Peter's <G>

> >Get involved !
>
…[3 more quoted lines elided]…
>

Still potshots - see below.

> > But given the opportunity I'm damn certain he
> > would contribute to a properly Standards focused forum, broken down into
…[9 more quoted lines elided]…
> Very high probability I would contribute to something like this, if asked.

Why not a DEFINITELY I WOULD contribute WITHOUT being asked.
Isn't this what you are basically after - excluding your qualifications on
'rubber-stamping'. Like all things, it is a starting point which is adjusted as
seen fit to make it more and more effective. Compromise, compromise, Pete - or
must one continue to sling Molotov cocktails, long after they have had any
effective use.

>
> It's been done. A man named Bill Norris (CEO of Control Data Corporation at
…[6 more quoted lines elided]…
>

Yeah and some SOB (with an Irish surname <G>), threatened to pull the same trick
on COBOL back in early '80s when they gave thought to cutting loose with
backwards compatibility. He screamed blue murder, threatening to sue COBOL
members individually. Resulted in a cautious rethink. That's close to the time
COBOL went for ISO blessing - Feb '84 - what Jerome Garfunkel (singer's
brother),  referred to as the "St. Valentine's Day Massacre, 1984".

Jimmy
```

###### ↳ ↳ ↳ Re: Draft Standard (was: many other things.....

_(reply depth: 18)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-17T12:41:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2c0c11_3@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <3B257FEC.D95F904A@home.com> <4145699b.0106112130.47a37099@posting.google.com> <3B26741F.FF743898@home.com> <4145699b.0106121846.563b9f0b@posting.google.com> <3B27953F.EC8B0F3E@Azonic.co.nz> <HSWV6.78377$t12.6494157@bgtnsc05-news.ops.worldnet.att.net> <3b2851b0_6@Usenet.com> <9gar9m$m1$1@slb6.atl.mindspring.net> <3b295bbe_3@Usenet.com> <4145699b.0106142057.645b9fc9@posting.google.com> <3B2A632E.D75F1489@home.com> <3b2b1d25_6@Usenet.com> <3B2BD381.56BFFDC@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3B2BD381.56BFFDC@home.com...
>
>
…[3 more quoted lines elided]…
> > long as you you are specific about what it is you agree/disagree with.
When
> > you say "some of your post" ...then you have really managed to say
nothing
> > of any use. Why comment at all if you are not prepared to adopt a
position
> > on something or seek clarification? That's what I mean by "lukewarm
chicken
> > soup"...bland, watery, with no substance to it, intended as a mollifying
> > palliative...
> >
>
> Be patient you SOB <G>. I actually do some program coding as well as write
here.
> I will send when ready  - and it is my personal view, not necessarily Pope
> Peter's <G>

You missed the whole point of the above. It was not a complaint about taking
too long. I really don't care how long you take or even if you ever respond.
My comment was directed to pertinency, not punctuality.

As for calling me a SOB and the Pope (in the same paragraph) neither is
accurate nor appropriate.

What ever makes you think I would expect your "personal view" to reflect
mine? The day that happens I'll be really scared...


>>>>>
> > > But given the opportunity I'm damn certain he
> > > would contribute to a properly Standards focused forum, broken down
into
> > separate
> > > threads, impartially monitored but NOT CENSORED.
> > E-mail represents a rapid
> > way of
> > > getting heated, lively and relevant discussion going on a topic -
doesn't
> > involve
> > > a teremendous cost nor does it need a gathering of the clans to
formally
> > discuss
> > > issues.
> >
> > Very high probability I would contribute to something like this, if
asked.
>
> Why not a DEFINITELY I WOULD contribute WITHOUT being asked.
> Isn't this what you are basically after - excluding your qualifications on
> 'rubber-stamping'. Like all things, it is a starting point which is
adjusted as
> seen fit to make it more and more effective. Compromise, compromise,
Pete - or
> must one continue to sling Molotov cocktails, long after they have had any
> effective use.
<<<<<
First off, I decide what I will and will not contribute to.

And what is an acceptable compromise (for me) and what is not. This is not.
It is also a hypothetical situation because no such scenario is likely to be
forthcoming.

So, according to Governor Gavan, I should commit myself to something before
it even eventuates, because it sounds like it might be fairly close to
something he thought I wanted. Yeah, right...!

No person (unless they are politically extremely naive) will even answer a
hypothetical question, let alone commit in print to it before it eventuates.

"Very high probability I would contribute to something like this, if asked."

That's my statement, I stand by it, it is a fair one.

You don't like it, Jimmy? Guess what....

Pete.



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-06-12T11:42:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com>`

```
On 11 Jun 2001 18:51:48 -0700, stephenjspiro@hotmail.com (Stephen J
Spiro) enlightened us:

>"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<9g3fkf$nmf$1@slb7.atl.mindspring.net>...
>> FYI - one national Standards body (the Netherlands) *has* specifically
…[29 more quoted lines elided]…
>difference!

If you are going to try and have GO TO be made "archaic" in the Cobol
Standard, then I suggest you also petition IBM to make the following
Assembler instructions  "archaic":

B
BE
BNE
BAL
BALR
BNO
BO
BCT
BCTR
BCR
BM
BXH
BXLE
BP

And while your at it, I believe there is a JMP instruction in some PC
Assemblers, so you should petition Intel and others to make it
"archaic" as well.

And while you're at it, I'm sure that Microsoft's VB and Q-Basic have
some offending branch instructions that you could petition them to
make "archaic" as well.

And what about C and C++?  Aren't there some branch instructions in
those languages that should be made "archaic" as well?

Hell, let's revolutionize the entire set of computer languages to
eliminate branching altogether because some people think this kind of
operation is "archaic".  Once that is done and all the mainframe and
PC operating systems have been rewritten then we can all get back to
work writing Cobol and other computer language programs that only use
"non-archaic"  commands.  The birds will sing, the world will be
perfect....

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Sticks and stones may break my bones, 
But whips and chains excite me!


DON'T DRILL in the Artic National Wildlife Refuge
Read the real facts at:

http://www.worldwildlife.org/arctic-refuge/

also

http://www.savepolarbears.org/


Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-12T10:04:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B263D97.E50030D5@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net>`

```
SkippyPB wrote:

> If you are going to try and have GO TO be made "archaic" in the Cobol
> Standard, then I suggest you also petition IBM to make the following
> Assembler instructions  "archaic":

What do good assembler programming practices have to do with good CoBOL programming practices?


>
> B
…[12 more quoted lines elided]…
> BP

We can do ALTER GO TO's quite easily in assembler as well.   Just because we can do something in assembler doesn't
mean we can't recommend against doing it in CoBOL.   (Making it archaic simply is a recommendation that it not be
used).


> And while your at it, I believe there is a JMP instruction in some PC
> Assemblers, so you should petition Intel and others to make it
…[15 more quoted lines elided]…
> perfect....

And even if they recommend that we don't use GO TO in CoBOL, there are lots of recommended ways to branch in CoBOL.
Methinks you are being silly.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-06-13T12:31:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net>`

```
On Tue, 12 Jun 2001 10:04:39 -0600, Howard Brazee <howard@brazee.net>
enlightened us:

>SkippyPB wrote:
>
…[48 more quoted lines elided]…
>Methinks you are being silly.

The only thing "silly" is taking a valid command that is basic to ANY
computer language (and logic) and having the standard and the vendors
proclaim such command as "archaic".  And why?  Because it doesn't fit
in with some people's idea of stylistic Cobol constructs?  

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Sticks and stones may break my bones, 
But whips and chains excite me!


DON'T DRILL in the Artic National Wildlife Refuge
Read the real facts at:

http://www.worldwildlife.org/arctic-refuge/

also

http://www.savepolarbears.org/


Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-13T14:39:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106131339.6811ef71@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net> <FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net>`

```
My understanding is that there is no equivalent of GO TO in Smalltalk.
 All program logic (procedural code) is encapsulated in the Smalltalk
equivalent of PERFORMed routines.  The language was designed so that
only modular, structured techniques can be used.  Elimination of GO TO
in COBOL would go a long way towards enforcing the same techniques.

Stephen J Spiro
Member, J4 COBOL Standards Committee

PS: Attention, Managers!  If you want to KEEP a valuable employee, get
him/her a position on a standards committee! You know there aren't
enough other employers who will offer this professional recognition!
  
*------------------------
SkippyPB <swiegand@nospam.neo.rr.com> wrote in message news:<FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net>...
> On Tue, 12 Jun 2001 10:04:39 -0600, Howard Brazee <howard@brazee.net>
> enlightened us:
…[80 more quoted lines elided]…
> Steve
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-06-14T12:04:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<606DD743BB0C5F2D.14079A2A3A9D4845.31D75F8C0DA3CF45@lp.airnews.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net> <FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net> <4145699b.0106131339.6811ef71@posting.google.com>`

```
On 13 Jun 2001 14:39:56 -0700, stephenjspiro@hotmail.com (Stephen J
Spiro) enlightened us:

>My understanding is that there is no equivalent of GO TO in Smalltalk.
> All program logic (procedural code) is encapsulated in the Smalltalk
…[6 more quoted lines elided]…
>

I don't care what Smalltalk does or does not have.  Bottom line is if
you looked at it's object code you would be sure to find a GO TO
equivalent command.  And your statement of elimination of GO TO to
enforce a coding technique, a.k.a. style, is exactly what I am railing
about.  It is not a valid reason to discard a very valid and usable
command.


>PS: Attention, Managers!  If you want to KEEP a valuable employee, get
>him/her a position on a standards committee! You know there aren't
…[63 more quoted lines elided]…
>> 

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Sticks and stones may break my bones, 
But whips and chains excite me!


DON'T DRILL in the Artic National Wildlife Refuge
Read the real facts at:

http://www.worldwildlife.org/arctic-refuge/

also

http://www.savepolarbears.org/


Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-14T10:25:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B28E587.62397CA5@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net> <FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net> <4145699b.0106131339.6811ef71@posting.google.com> <606DD743BB0C5F2D.14079A2A3A9D4845.31D75F8C0DA3CF45@lp.airnews.net>`

```
SkippyPB wrote:

> I don't care what Smalltalk does or does not have.  Bottom line is if
> you looked at it's object code you would be sure to find a GO TO
…[3 more quoted lines elided]…
> command.

And comparing it to object code provides a valid reason?   The only place it makes sense to look at object code (in this argument) is
when comparing alternative coding practices to see which produces the most efficient object code.   The object could have equivalents
of ALTER GO TO for all I care.

Valid arguments include:
1.  Does this style work?
2.  Is this style more or less likely to be bug free?
3.  Is this style easier to maintain and debug?
4.  Is this style significantly different in operational efficiency?
5.  Is it easier to train new programmers in this style?
6.  A is getting cheaper while B is getting more expensive, so let's use a style which concentrates on making B more efficient.

Invalid arguments include:
1.  Other languages do it.
2.  The object code does it.
3.  If things were different, it would be better.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-06-14T21:43:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9eaW6.217553$NK4.13934161@news2.aus1.giganews.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net> <FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net> <4145699b.0106131339.6811ef71@posting.google.com> <606DD743BB0C5F2D.14079A2A3A9D4845.31D75F8C0DA3CF45@lp.airnews.net> <3B28E587.62397CA5@brazee.net>`

```

"Howard Brazee" <howard@brazee.net>
>
> Valid arguments include:
…[5 more quoted lines elided]…
> 6.  A is getting cheaper while B is getting more expensive, so let's
use a style which concentrates on making B more efficient.

I'll disagree. I don't think "Style" has any place in determining a
standard - other than a permissive nature (such as free-form). "Style"
certainly should not prohibit a language construct.


>
> Invalid arguments include:
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-15T07:06:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2A084D.B3A938A0@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net> <FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net> <4145699b.0106131339.6811ef71@posting.google.com> <606DD743BB0C5F2D.14079A2A3A9D4845.31D75F8C0DA3CF45@lp.airnews.net> <3B28E587.62397CA5@brazee.net> <9eaW6.217553$NK4.13934161@news2.aus1.giganews.com>`

```


Jerry P wrote:

> "Howard Brazee" <howard@brazee.net>
> >
…[11 more quoted lines elided]…
> certainly should not prohibit a language construct.

What should determine standards?  I think it is criteria such as what I
listed.  Whether standards which fit such criteria - such as "no ALTER GO
TO's allowed", is called "Style", doesn't matter.   So don't call it
"style", call it "boogabooga" if you like.   But when you evaluate whether
a language construct is to be recommended, recommended against,
proscribed, or whatever in your company, use valid business criteria.


> >
> > Invalid arguments include:
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-15T12:45:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b295bcd_3@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net> <FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net> <4145699b.0106131339.6811ef71@posting.google.com> <606DD743BB0C5F2D.14079A2A3A9D4845.31D75F8C0DA3CF45@lp.airnews.net>`

```
Steve,

Don't worry about it.

Despite all the purist bullshit, they will NEVER remove GO TO from the COBOL
Language. There is too much investment in existing code to make the removal
of it an acceptable risk in the currently projected lifetime of COBOL.

While I don't personally use it unless it makes sense to, removing it
altogether would be insane.

(However, I could be wrong on this...insanity seems to be currently
prevalent in things COBOL...<G>)

Pete.
"SkippyPB" <swiegand@nospam.neo.rr.com> wrote in message
news:606DD743BB0C5F2D.14079A2A3A9D4845.31D75F8C0DA3CF45@lp.airnews.net...
> On 13 Jun 2001 14:39:56 -0700, stephenjspiro@hotmail.com (Stephen J
> Spiro) enlightened us:
…[24 more quoted lines elided]…
> >SkippyPB <swiegand@nospam.neo.rr.com> wrote in message
news:<FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net>...
> >> On Tue, 12 Jun 2001 10:04:39 -0600, Howard Brazee <howard@brazee.net>
> >> enlightened us:
…[3 more quoted lines elided]…
> >> >> If you are going to try and have GO TO be made "archaic" in the
Cobol
> >> >> Standard, then I suggest you also petition IBM to make the following
> >> >> Assembler instructions  "archaic":
> >> >
> >> >What do good assembler programming practices have to do with good
CoBOL programming practices?
> >> >
> >> >
…[16 more quoted lines elided]…
> >> >We can do ALTER GO TO's quite easily in assembler as well.   Just
because we can do something in assembler doesn't
> >> >mean we can't recommend against doing it in CoBOL.   (Making it
archaic simply is a recommendation that it not be
> >> >used).
> >> >
> >> >
> >> >> And while your at it, I believe there is a JMP instruction in some
PC
> >> >> Assemblers, so you should petition Intel and others to make it
> >> >> "archaic" as well.
> >> >>
> >> >> And while you're at it, I'm sure that Microsoft's VB and Q-Basic
have
> >> >> some offending branch instructions that you could petition them to
> >> >> make "archaic" as well.
…[5 more quoted lines elided]…
> >> >> eliminate branching altogether because some people think this kind
of
> >> >> operation is "archaic".  Once that is done and all the mainframe and
> >> >> PC operating systems have been rewritten then we can all get back to
> >> >> work writing Cobol and other computer language programs that only
use
> >> >> "non-archaic"  commands.  The birds will sing, the world will be
> >> >> perfect....
> >> >
> >> >And even if they recommend that we don't use GO TO in CoBOL, there are
lots of recommended ways to branch in CoBOL.
> >> >Methinks you are being silly.
> >>
…[28 more quoted lines elided]…
> Steve


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-06-15T13:28:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c4oW6.194$q_2.91880@paloalto-snr1.gtei.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net> <FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net> <4145699b.0106131339.6811ef71@posting.google.com> <606DD743BB0C5F2D.14079A2A3A9D4845.31D75F8C0DA3CF45@lp.airnews.net> <3b295bcd_3@Usenet.com>`

```
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
news:3b295bcd_3@Usenet.com...
> Despite all the purist bullshit, they will NEVER remove GO TO from the
COBOL
> Language. There is too much investment in existing code to make the
removal
> of it an acceptable risk in the currently projected lifetime of COBOL.
>
> While I don't personally use it unless it makes sense to, removing it
> altogether would be insane.
>

"Purists" and "investments" aside, of course it doesn't make sense, because
GO TO compiles to very efficient code, and can and does "make sense" when
optimizing a specific routine. (IIRC, the IBM M/F COBOL optimizers convert
some loops into the equivalent of a bunch of GO TOs. Other compilers do not
optimize as well, requirng the programmer to optimize by hand).

MCM
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 12)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-16T05:40:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b2a48ce_5@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net> <3B263D97.E50030D5@brazee.net> <FC1947A249588AC4.941D3E95351ADA21.0B1A570B92BB8ACC@lp.airnews.net> <4145699b.0106131339.6811ef71@posting.google.com> <606DD743BB0C5F2D.14079A2A3A9D4845.31D75F8C0DA3CF45@lp.airnews.net> <3b295bcd_3@Usenet.com> <c4oW6.194$q_2.91880@paloalto-snr1.gtei.net>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message news:c4oW6.194>
> "Purists" and "investments" aside, of course it doesn't make sense,
because
> GO TO compiles to very efficient code, and can and does "make sense" when
> optimizing a specific routine. (IIRC, the IBM M/F COBOL optimizers convert
> some loops into the equivalent of a bunch of GO TOs. Other compilers do
not
> optimize as well, requirng the programmer to optimize by hand).
>

Back in the old days (before PCs) there was IBM and the BUNCH (Burroughs,
Univac, NCR, CDC, and Honeywell). I once had to write some benchmark
programs that had to run on all these platforms. (Of course, we used
COBOL...<G>) In the course of this work I had access to manuals and just out
of curiosity checked the execution time of various machine language
instructions. Without fail, on EVERY platform, the Unconditional Branch was
the winner.

I didn't know about the optimisers you mention, Michael, but the result
doesn't surprise me in the least...

Pete


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-13T14:13:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b26ce0d_2@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net>`

```
Steve,

Thanks for a breath of fresh air in an incredibly stupid thread...

Loved it!

Pete.

"SkippyPB" <swiegand@nospam.neo.rr.com> wrote in message
news:D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net...
> On 11 Jun 2001 18:51:48 -0700, stephenjspiro@hotmail.com (Stephen J
> Spiro) enlightened us:
>
> >"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:<9g3fkf$nmf$1@slb7.atl.mindspring.net>...
> >> FYI - one national Standards body (the Netherlands) *has* specifically
> >> requested that GO TO be placed in the "archaic" (*not* OBSOLETE)
category in
> >> this revision of the Standard.
> >>
> >> I have NOT seen how J4 "processed" this request and NOTHING will be
final on
> >> it until the WG4 meeting in November.  HOWEVER, from past "discussion"
my
> >> GUESS is that this will be "rejected".
> >>
> >> If you have an opinion on whether GO TO should or should not be made
> >> "archaic," then I think you MIGHT want to send a note to the J4 Chair
asking
> >> for you "input" to be considered on this topic.  He can be reached
> >> electronically at:
…[80 more quoted lines elided]…
> Steve


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** Robaire <robaire@sympatico.ca>
- **Date:** 2001-06-15T10:34:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oa5kitsdcak771vg29k9qj8no8p4is5n8j@4ax.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com> <D942787F6022C17F.99B97099AE4CC74C.D5369F7D89EABC11@lp.airnews.net>`

```
On Tue, 12 Jun 2001 11:42:02 -0400, SkippyPB
<swiegand@nospam.neo.rr.com> wrote:

<snipped>
>And while your at it, I believe there is a JMP instruction in some PC
>Assemblers, so you should petition Intel and others to make it
>"archaic" as well.

Branching on the PC.
I just hope I can eventually locate a set of assembly language
instructions that were proposed for the PC in a magazine in the 1970s;
I can remember BRL (Branch to Random Location) and RDK (Rewind Disk);
I'll search for it.

As for Intel machines, yes, there is the JMP instruction, which jumps
unconditionally to a label.

>And while you're at it, I'm sure that Microsoft's VB and Q-Basic have
>some offending branch instructions that you could petition them to
>make "archaic" as well.

Visual Basic.
Yes, Skippy, there is a GoTo statement in VB,
but it is a kinder, gentler GoTo - 
it transfers control to the statement following the label named in the
GoTo, which label must be located in the same procedure as the Goto.

e.g.

If mfhgyt = 7 then GoTo Skippy
...
'   mfhgy-related stuff here

Skippy:
'   mfhgy-related stuff may, or may not have been done  ...
'   could have "fallen" into this part after doing the 
'   mfhgy-related stuff.

Pascal.
Also, for your interest, even Delphi (based on Pascal) has a goto
keyword(same label and goto syntax as in VB above) .
It allows jumping out of a block of statements (recommended use)
but also allows jumping into a block (produces unpredictable results).

>And what about C and C++?  Aren't there some branch instructions in
>those languages that should be made "archaic" as well?
…[7 more quoted lines elided]…
>perfect....

<snipped lengthy signature>

But since a concern in this newsgroup is, I think, among others, to
get COBOL back into the spotlight for people making decisions on what
language to use in companies, why not take a cue from Pascal (now
appearing as Delphi) and Basic (remember, Visual Basic is not your
father's BASIC) -  "officially" bring back COBOL under another, more
glamourous  name, and give it a fully integrated GUI environment
face-lift to justify the new image - works for stars, people who
declare bankruptcy, political parties ...

Is not image something that is preventing COBOL from making a
comeback; if it is, then is it seriously being addressed?

Any ideas for what it might be called?

R. Miller
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-06-12T11:43:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g5ns1$484$1@mail.pl.unisys.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <4145699b.0106111751.58cf6bb8@posting.google.com>`

```
Stephen J Spiro <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0106111751.58cf6bb8@posting.google.com...

> Unless they did it the day I slept late, Netherlands comments have not
> yet been processed.

We did "process" this item at Meeting #231 just completed, but did not
produce a final answer; the comment was accepted as a project by a J4 member
who, it is presumed, will prepare a proposed response to be discussed in
Portland.  There were a handful of international comments whose processing
was "tabled" until the Portland meeting because they related to areas
already being researched elsewhere, but this particular comment isn't one of
them.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-07-06T03:39:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net>`

```
Interesting. Maybe GoTo should be archaic but obsolete is fine with me;
Alter should be obsolete. Perform Thru and Next Sentence and Exit (the
plain version at least) should immediately be designated as archaic to put
people on notice that these are also unnecessary and dangerous programming
practice. After this, maybe even Sections could be done this way, but
that'll probably never fly. Besides, sections are useful during the
intermediate stages of cleaning up a program. A good compromise might be
to completely prohibit Perform Thru of Sections.

The On statement and maybe a few other oldies like exhibit etc. might
ought to be resurrected or at least supported as archaic. If On is
supported, an End-On scope terminator should be added and On could be
supported only (or at least more fully) if used with End-On.

I'm not sure I like the new Exit statements, but they're probably much
better than GoTo. Perhaps any kind of exit that terminates a loop should
be allowed for inline loops only, not out of line.

For that matter, as far as terminating-in-the-middle loops go, many
programming languages seem to take the approach of using some kind of exit
or break statement which then must be included in the scope of an If,
which tempts programmers to add extra logic, e.g.:

Loop
..stmts
..If condition
....stmts
....Break
..EndIf
..stmts
EndLoop

This can get out of hand with lots of If's and cases and more logic so
that the break of the loop gets deeply nested and different statements are
executed for each case. While to some extent this is tolerable in a
disciplined approach as implemented by e.g. Cobol's Search statement, it
can get out of hand. I've always preferred all loop exit statements to be
standalone at the level they need to be, including their own conditions as
needed, e.g.

Loop
..stmts
ExitWhen condition
..stmts
EndLoop

This keeps the loop exits at the same level as the loop delimiters and
easier to spot, and separates the termination condition logic from other
processing logic which may be conditioned on the same condition one day
but a different one the next, in other words put the processing logic in a
separate If block either entirely within the loop before the exit or after
the end of the loop. This seems much cleaner to me, and is still much more
convenient than having only a While or Repeat type of loop which allows
only one termination condition which much be at the beginning or end
respectively.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-07-06T09:52:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i4qbt$6rf$1@mail.pl.unisys.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net>`

```

Robert M. Pritchett - RMP Consulting Partners LLC wrote in message
news:Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net...

<<Interesting. Maybe GoTo should be archaic but obsolete is fine with me;>>

Archaic, according to the FCD, requires that the compiler warn the user
about his code.   I remain unconvinced that GO TO warrants this treatment.
Also see below.

<<Alter should be obsolete.>>

Actually, ALTER was marked "obsolete" in the '85 standard, and is *gone*
from the FCD altogether.

<<Perform Thru and Next Sentence and Exit (the plain version at least)
should immediately be designated as archaic to put people on notice that
these are also unnecessary and dangerous programming practice. >>

A COBOL compiler can't tell the difference between a program that's been
running pretty much as is for decades and one that's being written from
scratch according to the latest fashion of COBOL usage.

Managers who want upward compatibility of millions of lines of code that
already runs their businesses should not be expected to spend great gobs of
money to "fix" code that works just fine the way it is!

As to "Archaic language elements" in general, from the FCD: "There is no
plan for the removal of archaic elements; however, should their use in
program inventories become insignificant, they may be considered for
designation as obsolete by future architects of standard COBOL."

In order for the use of these features (GO TO, PERFORM THRU, NEXT SENTENCE
and unadorned EXIT) to be substantially reduced (to say nothing of rendering
their presence in program inventories insignificant), lots and lots of users
are going to have to spend lots AND LOTS of money reengineering their
applications.  I don't see businessmen being very happy about that prospect,
particularly since the only reason for doing so is that the usage violates
*style conventions* and receives a slap on the wrist from the compiler when
the constructs are encountered.  Given that these constructs are present in
a high percentage of the COBOL program inventory currently in existence, I
seriously doubt that all that many people would pay attention to the warning
about their use.  Those who avoid it in new programs -- whether by choice or
by site convention -- will avoid it.  Those who are maintaining existing
programs will almost certainly ignore it, and will find it an annoyance.
Those who have chosen a style of coding for their sites that includes these
constructs will deeply resent the suggestion by conforming compilers that
any choice to do so is hopelessly declasse'.

There are too many lines of code in existence containing these constructs
for the inventory of programs containing them to be reduced substantially,
much less rendered insignificant, anytime in the near future.  Since
escalation from "archaic" to "obsolete" is highly unlikely based on usage,
the only impact of marking them archaic is to require the compiler to slap
the user's hands anytime one of these constructs is used.  As I've said
before, the characterization of such choices as somehow substandard
practice, regardless of the reasons for making the choices,  strikes me as a
holy war upon which I don't think the standards committees, or the standard,
should take a side.   And my guess is that if these constructs *were* marked
as archaic in the standard, one of the first extensions we'd see across all
conforming compilers is a way to turn that particular warning off.

      -Chuck Stevens
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2001-07-06T13:53:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B46091C.B75A3F3@mb.sympatico.ca>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com>`

```
Chuck Stevensa wrote:

<snip>

>
> In order for the use of these features (GO TO, PERFORM THRU, NEXT SENTENCE
…[16 more quoted lines elided]…
>

Hear, hear.  Chuck's contribution is well presented, polite and complete, and
accurate.  This is the sort of discussion that is required to handle these
issues.

I might add that reading this and the thread on EXIT PARAGRAPH definition makes
me think that an enormous amount of thought and effort is being expended on
replacing a simple, easily understood and totally unambiguous verb by one that
is none of the above.

Just my opinion.

PL
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-07-06T12:26:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i53cb$fvj$1@mail.pl.unisys.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com> <3B46091C.B75A3F3@mb.sympatico.ca>`

```

Peter Lacey <lacey@mb.sympatico.ca> wrote in message
news:3B46091C.B75A3F3@mb.sympatico.ca...


<<I might add that reading this and the thread on EXIT PARAGRAPH definition
makes me think that an enormous amount of thought and effort is being
expended on replacing a simple, easily understood and totally unambiguous
verb by one that is none of the above.>>

I am as yet uncertain that the problem lies with EXIT PARAGRAPH and EXIT
SECTION; it may well relate to scope termination for the likes of in-line
PERFORM.  I also don't think anybody has much of a question what these verbs
are supposed to do; the problem is in describing what they're supposed to do
*in clear terms*.

The original question that was raised by Germany basically boils down to
"When an in-line PERFORM that's the last statement in a paragraph contains
an EXIT PARAGRAPH statement, does that EXIT PARAGRAPH behave like an EXIT
PERFORM or like an EXIT PERFORM CYCLE when it's executed?", although it's
not stated in those terms.  I don't think anyone would argue the former, but
the commentor couldn't assert one way or another *from the current rules*.

I haven't yet gotten to study Rick Smith's latest comments about static vs.
dynamic interpretation of EXIT GR's 10 and 11; if we do retain the current
FCD wording, it may be appropriate for us to add a "note" to the standard
clarifying the intent of these two General Rules.    Even if the current
wording is precisely correct, anything that generates *this* much discussion
is obviously less than clear and could benefit from attention before
publication of the standard!

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-07-06T22:01:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6zq17.2726$7J5.219922@dfiatx1-snr1.gtei.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com> <3B46091C.B75A3F3@mb.sympatico.ca> <9i53cb$fvj$1@mail.pl.unisys.com>`

```
Chuck Stevens <charles.stevens@unisys.com> wrote in message
news:9i53cb$fvj$1@mail.pl.unisys.com...
>
> Peter Lacey <lacey@mb.sympatico.ca> wrote in message
…[3 more quoted lines elided]…
> <<I might add that reading this and the thread on EXIT PARAGRAPH
definition
> makes me think that an enormous amount of thought and effort is being
> expended on replacing a simple, easily understood and totally unambiguous
…[4 more quoted lines elided]…
> PERFORM....

>... EXIT PARAGRAPH behave like an EXIT PERFORM or like an EXIT PERFORM
CYCLE ...


If you think ambiguous EXITs are bad in COBOL, you'll enjoy this BASIC code
I wrote week, which shows multiple LEVELS of EXIT and ITERATE (ITERATE is
the same as the COBOL "EXIT PERFORM CYCLE").

=====  BELOW IS NOT COBOL ===========

    FOR I = 0 TO 6              ' for each datatype in which we are
interested
        SELECT CASE I
               CASE 0
                    pLit = VARPTR (dbi.lit_sql_char)
               CASE 1
                    pLit = VARPTR (dbi.lit_sql_integer)
               CASE 2
                    pLit = VARPTR (dbi.lit_sql_date)
               CASE 3                                        ' not in use
                    pLit = VARPTR (dbi.lit_sql_money)
               CASE 4
                    pLit = VARPTR (dbi.lit_sql_number)
               CASE 5
                    pLit = VARPTR (dbi.lit_sql_varchar)
               CASE 6
                    pLit = VARPTR (dbi.lit_sql_smallint)
        END SELECT
        FOR J = 0 TO 6                                   ' for each possible
type we can use, in order...
            FOR K = 1 TO %NUMBER_OF_DESIRED_DATATYPES
                IF dbi.dd(K).SqlDataType = PT(I,J) THEN  ' we got a hit
                   @pLit = dbi.dd(K).DBMSLiteral         ' set our literal
equal to the database name
>>>>                EXIT, EXIT, ITERATE                   ' go to next
datatype
                END IF
            NEXT K
       NEXT J
   NEXT I


MCM
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-08T08:22:46+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B480A45.161122E2@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com> <3B46091C.B75A3F3@mb.sympatico.ca> <9i53cb$fvj$1@mail.pl.unisys.com> <6zq17.2726$7J5.219922@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:
> 
> =====  BELOW IS NOT COBOL ===========
…[12 more quoted lines elided]…
>    NEXT I

One of us doen't understand this code.   ;=)

How does it get to execute the 2nd 'EXIT' on that line ?  It appears to
me that the 2nd EXIT and the ITERATE are dead code.  Why won't the
execution of the first EXIT terminate the inner loop immediately ?
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-07-08T11:22:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%nX17.2399$m%1.406633@dfiatx1-snr1.gtei.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com> <3B46091C.B75A3F3@mb.sympatico.ca> <9i53cb$fvj$1@mail.pl.unisys.com> <6zq17.2726$7J5.219922@dfiatx1-snr1.gtei.net> <3B480A45.161122E2@Azonic.co.nz>`

```
Well, the way the compiler works is that it generates a stack of current
loops (there's about six verbs which qualify as "loop verbs"). When the code
is compiled, it knows how many levels of stack to pop when it gets to a
series of  EXIT or ITERATE verbs, so it can generate the code at compile
time to effect multiple exits in one line of source code. It's a pretty neat
feature of that compiler.

But to go a little further...

in EXIT, EXIT, ITERATE...,

EXIT 1 means "Exit the current loop." In this case, the loop controlled by
variable "K."

EXIT 2 means, "Exit the next outermost loop."  In this case, the loop
controlled by variable "J."

ITERATE means, "Repeat the NEXT outermost loop." , in this case, the loop
controlled by variable I.

So what this code does is, when the condition is met, it skips the rest of
the "K", skips the rest of the "J" and goes on to execute with the next "I"

Let me see if I can do it in COBOL....

PERFORM VARYING I FROM 0 BY 1 UNTIL I  GREATER 6
      PERFORM VARYING J FROM 0 BY 1 UNTIL J GREATER  6
           PERFORM VARYING K FROM 1 BY 1 UNTIL K  GREATER
NUMBER_OF_DATATYPES
                   IF CONDITION
                        move data
                        set exit-J-loop to true
                        set iterate-I-loop to true
                       EXIT PERFORM                <<< Exit the K loop
                   END-IF
           END-PERFORM
           IF EXIT-J-LOOP
              EXIT PERFORM                        <<< Exit the J Loop
          END-IF
     END-PERFORM
     IF Iterate-i-loop
         EXIT PERFORM CYCLE               <<< repeat I-loop with next value
of I
     END IF
     [Extra statements in VARYING I loop]
END-PERFORM

Except for the 'Extra Statements in VARYING I Loop,' EXIT PERFORM CYCLE is
redundant, as there are no statements up to the END-PERFORM which terminates
the I-loop scope, and you would expect the I-loop to repeat with the next
value of I anyway.

If you do not exit, all the "VARYING" clauses will be executed. In this
application,  I was looking for the FIRST value of a possible many values
which could have satisfied the condition. Had I kept going, I would have
gotten the LAST value matching. (I had made a table of "what I will accept,
in order of preference").

When the code is generated, it does not compile and execute  "verb by verb";
rather, it compiles and executes "logical unit by logical unit" - in this
case, the logical unit is the line containing EXIT, EXIT, ITERATE.

Like I said, it's a pretty neat feature of the compiler.

That said, it allows something REALLY weird, which I would never do...

DO
     WHILE        Condition
           FOR    I = 1 to n
               FOR J = 1 to m
                       IF CONDITION
                            EXIT DO      <<<<  skip three levels and jump
out of the outer "DO" loop
                       END IF
              NEXT J
          NEXT I
     WEND
LOOP
[Next line to be executed after EXIT DO]

(Instead of EXIT DO,  you could use EXIT, EXIT, EXIT, EXIT)

MCM

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3B480A45.161122E2@Azonic.co.nz...
> Michael Mattias wrote:
> >
> > =====  BELOW IS NOT COBOL ===========
> >
> >         FOR J = 0 TO 6                                   ' for each
possible
> > type we can use, in order...
> >             FOR K = 1 TO %NUMBER_OF_DESIRED_DATATYPES
> >                 IF dbi.dd(K).SqlDataType = PT(I,J) THEN  ' we got a hit
> >                    @pLit = dbi.dd(K).DBMSLiteral         ' set our
literal
> > equal to the database name
> > >>>>                EXIT, EXIT, ITERATE                   ' go to next
…[10 more quoted lines elided]…
> execution of the first EXIT terminate the inner loop immediately ?
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-08T08:30:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B480C2A.F49A7B42@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com> <3B46091C.B75A3F3@mb.sympatico.ca> <9i53cb$fvj$1@mail.pl.unisys.com> <6zq17.2726$7J5.219922@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:

> In the FCD, the following are marked "Archaic":
> 
> 3)  NEXT SENTENCE in IF and SEARCH:  Confusing; it does not transfer control
> to the scope terminator but to the code following the period that terminates
> the statement.  Use CONTINUE and scope terminators instead.

NEXT SENTENCE is currently ('85) not allowed in an IF that has a scope
terminating END-IF.  There is a contrived way around this by having a
NEXT SENTENCE in an inner IF that does not have a scope terminator, it
is implicitly terminated.  I assume that the 'archaic' marking is of all
uses of NEXT SENTENCE.

In my view the standards committee should have clarified this issue
years ago by imposing the constraint on NEXT SENTENCE to be disallowed
_anywhere_ within an IF ... END-IF, not just at that level.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-07-09T20:42:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B4A0940.495313F6@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com> <3B46091C.B75A3F3@mb.sympatico.ca> <9i53cb$fvj$1@mail.pl.unisys.com> <6zq17.2726$7J5.219922@dfiatx1-snr1.gtei.net>`

```
Michael Mattias wrote:

> when it gets to a
> series of  EXIT or ITERATE verbs, so it can generate the code at compile
> time to effect multiple exits in one line of source code. It's a pretty neat
> feature of that compiler.

So 'EXIT' isn't really 'EXIT', it is 'EXIT' after doing the rest of the
current line.

> Let me see if I can do it in COBOL....
> 
…[20 more quoted lines elided]…
> END-PERFORM

What is wrong with:

     MOVE SPACES      TO Data-Item
     PERFORM VARYING I FROM 1 BY 1
         UNTIL I > 6 OR Data-Item NOT = SPACES 
 
         PERFORM VARYING J ..
             UNTIL ... OR Data-Item NOT = SPACES

             PERFORM VARYING K ..
                 UNTIL .. OR Data-Item NOT = SPACES

                 IF ( some-condition )
                     MOVE Table-Data(I, J, K)  TO Data-Item
                 END-IF
             END-PERFORM
          END-PERFORM
       END-PERFORM

EXIT-PERFORM is for those too lazy to construct the code properly   ;-)
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-07-09T14:39:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gmj27.667$8T1.68011@dfiatx1-snr1.gtei.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com> <3B46091C.B75A3F3@mb.sympatico.ca> <9i53cb$fvj$1@mail.pl.unisys.com> <6zq17.2726$7J5.219922@dfiatx1-snr1.gtei.net> <3B4A0940.495313F6@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3B4A0940.495313F6@Azonic.co.nz...
> Michael Mattias wrote:
>
> > when it gets to a
> > series of  EXIT or ITERATE verbs, so it can generate the code at compile
> > time to effect multiple exits in one line of source code. It's a pretty
neat
> > feature of that compiler.
>
> So 'EXIT' isn't really 'EXIT', it is 'EXIT' after doing the rest of the
> current line.

 Correct.

>
> > Let me see if I can do it in COBOL....
…[6 more quoted lines elided]…
> EXIT-PERFORM is for those too lazy to construct the code properly   ;-)

Well, no, I wouldn't go that far. The (COBOL) code I fabricated was
specifically to demonstrate "the way multiple loop exits work in the
compiler I use." COBOL 'EXIT PERFORM' has its uses but this ain't one of
them.

MCM
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-07-07T15:07:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b467d83_6@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com>`

```
It is refreshing to find myself, for once, in total agreement with your
post, Chuck...<G>

And expressed in plain English...

Bottom Line:

"The Standard is NO place for a style war."

Pete.


"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:9i4qbt$6rf$1@mail.pl.unisys.com...
>
> Robert M. Pritchett - RMP Consulting Partners LLC wrote in message
> news:Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net...
>
> <<Interesting. Maybe GoTo should be archaic but obsolete is fine with
me;>>
>
> Archaic, according to the FCD, requires that the compiler warn the user
…[17 more quoted lines elided]…
> already runs their businesses should not be expected to spend great gobs
of
> money to "fix" code that works just fine the way it is!
>
…[6 more quoted lines elided]…
> and unadorned EXIT) to be substantially reduced (to say nothing of
rendering
> their presence in program inventories insignificant), lots and lots of
users
> are going to have to spend lots AND LOTS of money reengineering their
> applications.  I don't see businessmen being very happy about that
prospect,
> particularly since the only reason for doing so is that the usage violates
> *style conventions* and receives a slap on the wrist from the compiler
when
> the constructs are encountered.  Given that these constructs are present
in
> a high percentage of the COBOL program inventory currently in existence, I
> seriously doubt that all that many people would pay attention to the
warning
> about their use.  Those who avoid it in new programs -- whether by choice
or
> by site convention -- will avoid it.  Those who are maintaining existing
> programs will almost certainly ignore it, and will find it an annoyance.
> Those who have chosen a style of coding for their sites that includes
these
> constructs will deeply resent the suggestion by conforming compilers that
> any choice to do so is hopelessly declasse'.
…[8 more quoted lines elided]…
> practice, regardless of the reasons for making the choices,  strikes me as
a
> holy war upon which I don't think the standards committees, or the
standard,
> should take a side.   And my guess is that if these constructs *were*
marked
> as archaic in the standard, one of the first extensions we'd see across
all
> conforming compilers is a way to turn that particular warning off.
>
>       -Chuck Stevens
>
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-07-07T13:22:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<C72D1D9586CB6E79.D9F2DE98CD781C2E.A2B10C0058BD49B8@lp.airnews.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i4qbt$6rf$1@mail.pl.unisys.com>`

```
On Fri, 6 Jul 2001 09:52:10 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> enlightened us:

>
>Robert M. Pritchett - RMP Consulting Partners LLC wrote in message
…[61 more quoted lines elided]…
>

Thank you Chuck for your response.  I was beginning to think that no
one on the J4 was sane or possessed even a modicum of common sense.
That they were all members of the style police trying to stuff their
idea of what a Cobol program should look like down our collective
throats and force the compiler writers and vendors to adhere to their
vision of Cobol.  At least now I know there is as least one ray of
hope and sanity on the J4.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

-----------------------------
  Fear Leads to Anger;
  Anger Leads to Stress;
  Stress Leads to Doobies;
  Doobies Lead to Twinkies.  
-----------------------------

Rest In Peace John Lee Hooker


Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "David P. Bretz" <DBretz@mescoma.com>
- **Date:** 2001-07-06T17:27:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B462D36.3009C33F@mescoma.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net>`

```
Well..............at the risk of being flamed, I totally disagree.   I write
clear, concise, easy to follow, easy to maintain code...........and I use
perform thru and go to (only to a paragraph exit), etc.    Each paragraph in
my programs has one function, and the program executes by performing these
functions in an appropriate order.  If a new function needs to be added, a new
paragraph is written, and the perform thru is placed in the appropriate
place.   There is always more than one way to accomplish a goal, and to be
forced to comply with some "utopian" view of COBOL is completly in left field
(IMHO).

Dave Bretz

"Robert M. Pritchett - RMP Consulting Partners LLC" wrote:

> Interesting. Maybe GoTo should be archaic but obsolete is fine with me;
> Alter should be obsolete. Perform Thru and Next Sentence and Exit (the
…[62 more quoted lines elided]…
> "archaic," ...
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-07-07T15:20:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b4680c0_1@Usenet.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <3B462D36.3009C33F@mescoma.com>`

```

"David P. Bretz" <DBretz@mescoma.com> wrote in message
news:3B462D36.3009C33F@mescoma.com...
> Well..............at the risk of being flamed, I totally disagree.   I
write
> clear, concise, easy to follow, easy to maintain code...........and I use
> perform thru and go to (only to a paragraph exit), etc.    Each paragraph
in
> my programs has one function, and the program executes by performing these
> functions in an appropriate order.  If a new function needs to be added, a
new
> paragraph is written, and the perform thru is placed in the appropriate
> place.   There is always more than one way to accomplish a goal, and to be
> forced to comply with some "utopian" view of COBOL is completly in left
field
> (IMHO).
>

I do something similar to the above (I use a SECTION, instead of a
Perform...thru, but also have a single exit) also, and I totally endorse the
sentiment expressed in your last sentence...<G>

And before certain people start putting on white robes and setting fire to
crosses, I DON'T CARE!

It is just Computer code. It ISN'T Life and Death!

Don't worry about being flamed, David, do what you are comfortable with and
what works for you. A discussion forum is just that; a place for discussion.
It doesn't mean you need the approval or disapproval of those contributing.
If they don't like it, screw 'em!  (and that goes for your reaction to my
opinion, as well as anybody else's <G>)

Pete.





Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-07-06T15:23:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i5dov$q1l$1@mail.pl.unisys.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net>`

```

Robert M. Pritchett - RMP Consulting Partners LLC wrote in message
news:Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net...

<<Maybe GoTo should be archaic but obsolete is fine with me;>>

I didn't note this when I responded earlier.  I think there's a
misunderstanding lurking in the above assertion.

An "obsolete" element in the language is marked for unconditional
elimination from the next standard; an "archaic" element is merely flagged
as a potential candidate for "obsolete" status in some future (but unstated)
standard *after* the next one.  Occurrences of either must, however, be
flagged and identified in the documentation for any conforming
implementation.

Stated another way, marking a construct "obsolete" indicates that it's Going
Away Real Soon Now, whereas marking it "archaic" indicates that it Might Go
Away Someday If Nobody's Still Using It By The Time We Check Back.

The following actual examples should help the reader understand the relative
force of the two terms:

In the FCD, the following are marked "Archaic":

1) Continuation of COBOL words:  Creates programs that are difficult to read
and is incompatible with free-format COBOL.

2)  MOVE of alphanumeric figuratives to numeric destinations:  The results
rarely, if ever, produce a defined result.   (Note that ALL <literal> with
numeric items was obsolete in the '85 standard and isn't supported by the
FCD).

3)  NEXT SENTENCE in IF and SEARCH:  Confusing; it does not transfer control
to the scope terminator but to the code following the period that terminates
the statement.  Use CONTINUE and scope terminators instead.

4)  CALL ... ON OVERFLOW ... :  Misleading; the conditions are not normally
related to an "overflow" condition.   CALL ... ON EXCEPTION ... is typically
more meaningful and accomplishes the same thing.

5)  COPY ... REPLACING identifier-n (text-n):  Many new forms of
<identifier> are allowed in the FCD than in the previous standard,
significantly complicating the process; only those formats supported by the
previous standard are permitted here.  Pseudo-text delimiters are preferred
in such contexts.

The following are marked "Obsolete":

1)  The COMMUNICATION facility:  This capability is dependent on a
multiple-queue model; new environments require different facilities and
approaches.  A modernized facility is under consideration for a future
standard.

2)  Debugging lines and the DEBUGGING MODE phrase:  Rarely used, and has
several problems (interaction with COPY and REPLACE, for example).
Conditional compilation provides all of the functionality, is more clearly
defined, and is more robust, and should be used instead.

3)  PADDING CHARACTER clause:   Has never been well-defined, and is more
appropriate to an external specification.  There are no implementations
known to J4 that treat this clause as other than a comment.

In the '85 standard, such things as MEMORY SIZE (more appropriate to the
operating system), RERUN (ditto), MULTIPLE FILE TAPE (ditto), VALUE OF
(ditto), DATA RECORDS (redundant, and may cause misleading documentation),
ALTER (we all know about this one; GO TO ... DEPENDING can do the same
thing), OPEN REVERSED (Infrequently implemented and not a good candidate for
standardization), STOP <literal> (substantially defined by the implementor
and not a good candidate for standardization), and the segmentation module
(better provided at the operating system level) are all marked as obsolete.

Note that the '85 standard also called for the elimination of the entire
DEBUG module, and USE FOR DEBUGGING and the DEBUG-ITEM did indeed go away in
the FCD.  The elimination of the two fragments that remain of this feature
(see above) is delayed until the next standard,  I suspect because there was
no defined mechanism in the '85 standard that could be used to replace it.

       -Chuck Stevens
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-07-06T20:20:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0107061920.5d2198d9@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com>`

```
One of the effects of declaring a feature "archaic", overlooked by
previous contributors, is that it will no longer ber taught in courses
to new programmers, and textbooks will discourage it. As programs are
withdrawn from production, the total inventory of programs using the
features will shrink.  When the time is ripe, it will become obsolete,
and then dropped.

Stephen J Spiro
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-07-09T13:39:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9id4qh$5ib$1@mail.pl.unisys.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com> <4145699b.0107061920.5d2198d9@posting.google.com>`

```
Stephen J Spiro <stephenjspiro@hotmail.com> wrote in message
news:4145699b.0107061920.5d2198d9@posting.google.com...

<<One of the effects of declaring a feature "archaic", overlooked by
previous contributors, is that it will no longer ber taught in courses to
new programmers, and textbooks will discourage it. >>

And how are new-hire maintenance programmers supposed to figure out what
this mystery statement does if it's not taught in courses?  As to textbooks
discouraging it, isn't that already the case, at least for those COBOL
courses that purport to teach any sort of style?

While I have no problem with either textbooks or professors *discouraging*
the use of GO TO in new programs, I would contend that a professor or a
textbook or a standard that asserts that the mere presence of a GO TO
statement in an existing program is itself grounds for immediately
considering the replacement of the program does NOT do the future of COBOL a
service!   Moreover, a professor or a textbook that refuses to admit the
very existence of GO TO in the COBOL language does NOT assist the new
programmer in learning how to understand and maintain the billions of lines
of code out there that actually contain GO TO statements already.

It is true that, with the introduction of scope delimiters and other
features, COBOL now has enough features that most programs that can be
written CAN be written clearly without the use of GO TO statements.

It is also true that many sites spent a great deal of money migrating to,
and enforcing, a popular "structured" approach stylistic approach (GO TO
only to the exit point of the paragraph you are in).    But it is a fact
that having all conforming implementations of COBOL2002 mark any programs
using this style as archaic (in the '2002 standard) or obsolete (in later
ones) is good for the future of COBOL?

<<As programs are withdrawn from production, the total inventory of programs
using the features will shrink.>>

True enough.  But I do not believe that will happen rapidly.  I also do not
believe the problems with maintainability with GO TO have been anything like
as severe as they were with ALTER, and I believe the percentage of
*valuable* programs containing GO TO statements today is very high.

Marking that large number of programs with "archaic" flags runs counter to
the idea that a *businessman* who has his programs written in COBOL is
making an investment, and he can expect that investment to pay dividends for
a very, very long time.

<<When the time is ripe, it will become obsolete, and then dropped.>>

I wouldn't personally stand in the way of a move to introduce a "note" in
the FCD to the effect that COBOL provides a rich array of constructs that
many programmers feel provides a better approach to the problem of logic
flow than GO TO provides, and that the use of alternative constructs is
encouraged.  But I strongly believe that requiring every COBOL2002-compliant
compiler to issue a warning for every instance of GO TO encountered in every
program it compiles is NOT in the best interests of the future or the image
of COBOL, and issuing just such a warning is required by the process of
making GO TO "archaic".

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-09T21:36:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9idpop$i7j$1@slb1.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com> <4145699b.0107061920.5d2198d9@posting.google.com> <9id4qh$5ib$1@mail.pl.unisys.com>`

```
Chuck,
  Remember that archaic flagging (like obsolete flagging) is BY DEFINITION
"user selectable". Therefore, if a programmer doesn't want to see those
messages, they don't have to.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-07-10T08:59:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9if8o7$go9$1@mail.pl.unisys.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com> <4145699b.0107061920.5d2198d9@posting.google.com> <9id4qh$5ib$1@mail.pl.unisys.com> <9idpop$i7j$1@slb1.atl.mindspring.net>`

```
You're right; I did see "that optionally can be invoked by the user at
compile time" but my mind blanked it out ...

    -Chuck Stevens


William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:9idpop$i7j$1@slb1.atl.mindspring.net...
> Chuck,
>   Remember that archaic flagging (like obsolete flagging) is BY DEFINITION
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 6)_

- **From:** "David P. Bretz" <DBretz@mescoma.com>
- **Date:** 2001-07-07T03:47:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B46BEA7.2E869250@mescoma.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com>`

```
Well...........two of the elements mentioned here I would really like to keep.
First, the NEXT SENTENCE in an IF and SEARCH.   If you realize that the NEXT
SENTENCE goes to the verb after the period, then it can be useful.  I've written
IF and SEARCH statements where I've used both the NEXT SENTENCE and CONTINUE in
the same construct, and they've made perfect sense.  It's really a matter for
the programmer to make it clear....not the language.

Next, the DEBUGGING MODE......despite what you say about it being rarely used, I
use it all the time.  Whenever I want to trace a program, for instance.  Or when
I'm in a testing mode, I might put in some displays and mark them in col 7 with
a "D" so I can turn the on or off until the program goes into production, when I
remove them all together.  I have found the DEBUGGING MODE with used in
conjunction with DECLARATIVES to be a very handy debugging
tool........especially at 3:00 am when something has crashed in production!

Dave Bretz

Chuck Stevens wrote:

> Robert M. Pritchett - RMP Consulting Partners LLC wrote in message
> news:Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net...
…[75 more quoted lines elided]…
>        -Chuck Stevens
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-07-09T09:22:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9icln9$jh2$1@mail.pl.unisys.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com> <3B46BEA7.2E869250@mescoma.com>`

```

David P. Bretz <DBretz@mescoma.com> wrote in message
news:3B46BEA7.2E869250@mescoma.com...
> Well...........two of the elements mentioned here I would really like to
keep.
> First, the NEXT SENTENCE in an IF and SEARCH.   If you realize that the
NEXT
> SENTENCE goes to the verb after the period, then it can be useful.  I've
written
> IF and SEARCH statements where I've used both the NEXT SENTENCE and
CONTINUE in
> the same construct, and they've made perfect sense.  It's really a matter
for
> the programmer to make it clear....not the language.
>

The problem is ambiguity in the presence of END-SEARCH and END-IF.  The FCD
is clear, control does indeed go to the next SENTENCE.  The problem is that
some might mistakenly think it actually goes to the STATEMENT after the IF
or SEARCH statement, and that's NOT the case.  The FCD says "It is a common
belief among users that control is transferred to a position after the
scope-deliminter rather than to a separator period that follows it
somewhere.  In addition, it is a common source of errors, especially for
maintenance programmers who inadvertently insert a period somewhere before
the actual terminating separator period.  The CONTINUE statement and scope
delimiters can be used to accomplish the same functionality and such
constructs are clearer and less prone to error."  I'm inclined to agree with
the FCD.


> Next, the DEBUGGING MODE......despite what you say about it being rarely
used, I
> use it all the time.  Whenever I want to trace a program, for instance.
Or when
> I'm in a testing mode, I might put in some displays and mark them in col 7
with
> a "D" so I can turn the on or off until the program goes into production,
when I
> remove them all together.  I have found the DEBUGGING MODE with used in
> conjunction with DECLARATIVES to be a very handy debugging
> tool........especially at 3:00 am when something has crashed in
production!

It's important to note that USE FOR DEBUGGING (along with the entirety of
the DEBUG module!)  was already marked obsolete in the '85 standard, so this
is hardly a precipitous decision.  What happened in the FCD is that a couple
of minor features got retained when the rest of the module was eliminated
(as planned for nearly twenty years).    There's no reason other than
lethargy and habit to use debugging lines and the DEBUGGING MODE phrase in a
compiler that also has conditional compilation; the latter is a much more
powerful tool (and its power is by no means limited to debugging).

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 8)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-07-09T14:57:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0107091357.1a956cdd@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com> <3B46BEA7.2E869250@mescoma.com> <9icln9$jh2$1@mail.pl.unisys.com>`

```
Another reason for retention of the "D" is because even *I* have a
hundred programs that have the D in them - presently considered a
comment!
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 9)_

- **From:** nospam@nospam.nospam (Tony)
- **Date:** 2001-07-10T14:32:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b4b116e.69268172@news.swbell.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com> <3B46BEA7.2E869250@mescoma.com> <9icln9$jh2$1@mail.pl.unisys.com> <bfdfc3e8.0107091357.1a956cdd@posting.google.com>`

```
On 9 Jul 2001 14:57:35 -0700, thaneh@softwaresimple.com (Thane
Hubbell) wrote:

>Another reason for retention of the "D" is because even *I* have a
>hundred programs that have the D in them - presently considered a
>comment!


HEAR HEAR! I had heard that the reason for the removal of the D was
because there are so many good debug facilities out their... Hogwash.
Does someone know if ASSERT is leaving C?

Now commenting out debug code in a large program will look messy!
Where the D is simple. I would hope that this is re-addressed...


Thanks,
Tony Harmon

T o n y (dot) H a r m o n (at) b n s f (dot) c o m

===================================

"A golfer with great dreams, can 
accomplish great things."
-- Bob Rotella

===================================

"A day without hitting golf balls,
is a day longer to getting better"
-- Ben Hogan

===================================

"The average golfer's problem is 
not so much a lack of ability as 
it is a lack of knowing what he
should do." 
-- Ben Hogan

===================================
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-10T19:08:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ig5ea$ek2$1@nntp9.atl.mindspring.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com> <3B46BEA7.2E869250@mescoma.com> <9icln9$jh2$1@mail.pl.unisys.com> <bfdfc3e8.0107091357.1a956cdd@posting.google.com> <3b4b116e.69268172@news.swbell.net>`

```
It may not be "pretty" but if you have source code with D in column 7 and
sometimes you want to "do the code" and sometimes you don't (and if you have
a compiler that doesn't support it - and remember that because it is
OBSOLETE in *this upcoming* Standard which means that it will NOT be removed
from the Standard until the NEXT one after this one), then you could use

a REPLACE statement to
   change it to a space when you want to execute it
   change it to a comment delimiter (*>) when you don't

This seems as easy to me as using the WITH DEBUG MODE phrase.
```

###### ↳ ↳ ↳ Re: GO TO and draft Standard (was: More Structure.. Perform from Read

_(reply depth: 11)_

- **From:** nospam@nospam.nospam (Tony)
- **Date:** 2001-07-11T16:46:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b4c8211.5669742@news.swbell.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <9g3fkf$nmf$1@slb7.atl.mindspring.net> <Dpa17.6657$oa1.629824@newsread1.prod.itd.earthlink.net> <9i5dov$q1l$1@mail.pl.unisys.com> <3B46BEA7.2E869250@mescoma.com> <9icln9$jh2$1@mail.pl.unisys.com> <bfdfc3e8.0107091357.1a956cdd@posting.google.com> <3b4b116e.69268172@news.swbell.net> <9ig5ea$ek2$1@nntp9.atl.mindspring.net>`

```
On Tue, 10 Jul 2001 19:08:06 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>It may not be "pretty" but if you have source code with D in column 7 and
>sometimes you want to "do the code" and sometimes you don't (and if you have
…[8 more quoted lines elided]…
>This seems as easy to me as using the WITH DEBUG MODE phrase.

Except for code that is commented out because it is currently
obsolete, but could be put back into service sometime. It just seems
silly to me that now I have to come up with some kind of commenting
scheme that any maintenance programmer that goes into my stuff will
have to make sure to read (that thought just makes me shudder). The
language should be concise not ambiguous. It may not be a commonly
used part of the language, but it makes sense and it should stay. 

>
>--
…[47 more quoted lines elided]…
>

Thanks,
Tony Harmon

T o n y (dot) H a r m o n (at) b n s f (dot) c o m

===================================

"A golfer with great dreams, can 
accomplish great things."
-- Bob Rotella

===================================

"A day without hitting golf balls,
is a day longer to getting better"
-- Ben Hogan

===================================

"The average golfer's problem is 
not so much a lack of ability as 
it is a lack of knowing what he
should do." 
-- Ben Hogan

===================================
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** stephenjspiro@hotmail.com (Stephen J Spiro)
- **Date:** 2001-06-11T21:08:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4145699b.0106112008.186720a5@posting.google.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca>`

```
Peter Lacey <lacey@mb.sympatico.ca> wrote

   <snip> 
> You're treading on very dangerous ground here, friend.
> 
> ANY kind of verb that redirects program flow is a go to!!!  
   <snip>
*-------------------

I'm sorry, but if you do not understand the conceptual difference
between a physical transfer of control and the unrestricted use of GO
TO in programming methodology, then we do not have a common
vocabulary.  Further discussion on the topic (between you and me)
would waste both of our time.

Stephen J Spiro
Wizard Systems
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-06-12T09:14:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B25CF4E.833DF9B3@Azonic.co.nz>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca>`

```
Peter Lacey wrote:
> 
> At the risk of seeming archaic, stubborn, out of it, etc., (insert your own adjective),
…[6 more quoted lines elided]…
> END-IF.
 
> Now consider the same program coded with a GOTO:
> 
…[9 more quoted lines elided]…
> 110-NEXT.

From my perspective the cause of the problem is not the IF ... END-IF or
the lack/use of GO TO Exit, but is much more subtle.

You obviously use a style of PERFORMed SECTIONs where the labels are
numbered.  You may even have these numbered to represent both the
'level' and the position in the source file.

This imposes a restriction and an overhead on creating a sub-block that
could be performed.  Because of this overhead it becomes too difficult
to break the code down into more managable routines.  This leads to long
ponderous lumps of code that are difficult to navigate.  As you quite
rightly say, a 500 line IF ... END-IF makes it difficult to understand. 
Using a GO TO, however, introduces other problems.

If the code was structured then instead of (say):
 
           something or other
           IF ( Customer-Type = "R" )
               120 lines calculating price
               150 lines calculating discount
               70 lines calculating tax
           END-IF


You would write:

           IF ( Customer-Type = "R" )
               PERFORM Calculate-Retail-Price
               PERFORM Calculate-Retail-Discount
               PERFORM Calculate-Retail-Tax
           END-IF
           .
      Calculate-Retail-Price.
           120-lines
      etc.

But your style PREVENTS you from doing this.  Well not exactly prevents
but makes it too much hard work.  You probably have to invent new
numbers (ensuring no clash), move the code to its correct sequential
position in the source, ensure the correct SECTION header and Exit
paragraph and that it is correctly terminated by the next SCTION
keyword.

The result is that the code gets separated from its parent and it is
then even more difficult to work between the IF and the code.

So the programmers code long meandering SECTIONs and put in GO TOs
because it is easier than the overheads and problems above.

This is _not_ a result of IF ... END-IF, or of trying to avoid GO TO (or
EXIT SECTION). It is directly the result of making 'routines' too
difficult to create (the overhead).

Try an experiment.  Take a long meandering SECTION that should only have
two paragraphs in it, the (implied or specific) code paragraph and the
nnn-Exit.

Now break down the code into logical blocks and give each a meaningful
name.  For each put a PERFORM at the start of the section.  If there is
an overall IF or IF .. GO TO then put this in the initial block of code.

The 500 lines may turn into a 20 line of so summary of the code followed
by a dozen or so routines that do the work, and these are in the same
place.  Because the summary can be IF ... END-IF withoutout meandering
over many pages you won't _need_ any GO TO Exit, so kill that
paragraph.  It no longer _needs_ to be a SECTION so make the initial
paragraph what is PERFORMed.  Get a decent text editor that can do a
search by placing the cursor on a name and pressing a key, you no longer
_need_ number to find things, or to put them in some sort of artificial
order (this was necessary when programs were in boxes of cards).

The _cause_ of the 500 line IF ... END-IF is not 'GO TO less
programming', but attempting to avoid GO TO _within_ a high overhead
PERFORM SECTION style that has created the 500 line paragraphs in the
first place.

To go to 'GO TO Less' programming it is necessary to _also_ reject all
the red-tape that goes with the 'PERFORM SECTION with GO TO exit'.  As
you have discovered, trying to get to it in steps fails miserably.  Now
try and find enlightenment little cricket   ;-)

Yes, I know, you or your site have been doing it one way for 30 years
....
 
> End of MY rant.

Feeling better now ?  I do.   ;-)
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-06-12T06:58:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B261209.6496AA34@brazee.net>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <3B25CF4E.833DF9B3@Azonic.co.nz>`

```
Richard Plinston wrote:

> You would write:
>
…[15 more quoted lines elided]…
> keyword.

I do this all the time.   First of all, there generally is plenty of room to insert new
numbers where they belong.  If I want to add paragraphs between 1100-CUSTOMER-LOOP &
2000-CALCULATE-INTEREST, I have some choices available.   And global changes don't take much
work anyway.
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 4)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2001-06-12T11:33:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B264459.88A99A5C@mb.sympatico.ca>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <3B25CF4E.833DF9B3@Azonic.co.nz>`

```
Richard Plinston wrote:

> From my perspective the cause of the problem is not the IF ... END-IF or
> the lack/use of GO TO Exit, but is much more subtle.
…[3 more quoted lines elided]…
> 'level' and the position in the source file.

Better stop right now.  I never use sections except as the input and output procedures for a
sort (and I'm getting away from that).   I do use numbered paragraphs but the only
relationship the numbers have to the position in the program is that all the paragraph names
within sort procedures have the same intial digit as the section name
    INPUT PROCEDURE IS 200-INPUT
    200-INPUT SECTION.
    201-GO.

    210-...

etc.

Beyond that, the paragraph numbers are in strictly increasing order.  Reason is that it makes
navigating within the source code infinitely easier.  Also paragraph names are guaranteed to
be unique.

Therefore, I must respectfully point out that, because of your jumping to an incorrect
conclusion, your whole subsequent argument is irrelevant.

My point in the post was to ask why, in the example I gave, GOTO-less coding should be
considered "better" and "less ambiguous"?  You did acknowledge the point but didn't really
answer it.

>
>
…[11 more quoted lines elided]…
>

Of course.  This is certainly the way I'd do it (with numbers prefixed to the names).

>   Now
> try and find enlightenment little cricket   ;-)

No need to be condescending.  I was polite and (I hope) reasonably humorous.

> Yes, I know, you or your site have been doing it one way for 30 years

Now that really is a bit much.  I happily gave up on cards once a decent editor was
available.  I leaped upon the PERFORM...END-PERFORM and similar constructions when they
became available.  I stopped using sections for memory conservation once useful memory sizes
were there.  I have moved along to using GUI (although some of the earlier implementations
were "klunky") and continue to refine my use of it.  I'm beginning to try OO.  Now if in the
course of "30 years" I have found a particular programming technique useful, easy, and
maintainable in the face of enlightened (or not) opinio, I'm Entitled!!

PL
```

###### ↳ ↳ ↳ Re: More Structure.. Perform from Read

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-12T17:52:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B2657A1.7C113EC7@home.com>`
- **References:** `<3b1c3343_2@news1.prserv.net> <4145699b.0106101155.1441bc5a@posting.google.com> <3B252083.ECA4ECCB@mb.sympatico.ca> <3B25CF4E.833DF9B3@Azonic.co.nz> <3B264459.88A99A5C@mb.sympatico.ca>`

```


Peter Lacey wrote:

> I stopped using sections for memory conservation once useful memory sizes
> were there.  I have moved along to using GUI (although some of the earlier implementations
> were "klunky") and continue to refine my use of it.  I'm beginning to try OO.

Ooh ! Re OO - Which compiler, and what is your success to date ? (You do realize you are swimming
against the generally 'accepted' tide <G>)

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
