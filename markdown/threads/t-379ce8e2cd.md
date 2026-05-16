[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Beginner's Question

_219 messages · 24 participants · 2003-04_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Beginner's Question

- **From:** auburn82@iolfree.ie (Auburn)
- **Date:** 2003-04-02T09:36:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<df4392fb.0304020936.2ef02cfe@posting.google.com>`

```
I am working on an assignment for college and am stuck on the
following:
My program reads in a logfile and then analyses it and produces a
report. The fields are all separated by blank characters but some of
the fields may be varying lengths, eg. IP address, resource path. I
need to access the CountryCode and return its name (I know how to do
this bit).
I know I need to access fields by looking for the space character but
am confused about how to do this. Any suggestions appreciated.

     FILE SECTION.
       FD Logfile.
       01 LogfileRecord.
           88   EndOfLogfile            VALUE HIGH-VALUES.
           02   Date                    PIC X(10).
           02   Time                    PIC X(8).
*          May be less than 15 chars
           02   IPAddress               PIC X(15).
           02   CountryCode             PIC X(2).
*          May be less than 80 chars
           02   ResourcePath            PIC X(80).
```

#### ↳ Re: Beginner's Question

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-02T18:03:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6f8ls$mp0$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com>`

```

On  2-Apr-2003, auburn82@iolfree.ie (Auburn) wrote:

> I know I need to access fields by looking for the space character but
> am confused about how to do this. Any suggestions appreciated.
…[11 more quoted lines elided]…
>            02   ResourcePath            PIC X(80).

Check the following two items in your reference manual:
1.  Reference modification   e.g.   MyRecord (i:i)
2.  Unstring

But as in any programming problem the big need is to "know your data".   Program
for what can happen.   E.g.  Can you have a space as a valid character within a
field?  Should you use a different delimiter?

If you use reference modification, consider whether to move from the front to
the back, or from the back to the front, as scan your data in a perform loop.
```

#### ↳ Re: Beginner's Question

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-02T15:44:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z6acndfUY-o9xBajXTWcrg@giganews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com>`

```

"Auburn" <auburn82@iolfree.ie> wrote in message
news:df4392fb.0304020936.2ef02cfe@posting.google.com...
> I am working on an assignment for college and am stuck on the
> following:
…[18 more quoted lines elided]…
>            02   ResourcePath            PIC X(80).

This can't be the input file as you've defined field lengths here as fixed.

Move this definition to working storage and define your input record as:

01  LOGREC   PIC X(200).

You now have reduced the problem to one of parsing an 80-byte record
plucking off the stuff you want. One way is to step through the input record
putting successive bytes into "Date" until you hit a space, then put
successive bytes into "Time" etc.

There's an easy way to do this - hint: study UNSTRING (especially the "ALL"
parameter).

This assignment is not trivial in that the problem represented here -
decomposing (or creating) - a record with delimited fields (rather than
fixed length fields) - is a fairly common experience.
```

#### ↳ Re: Beginner's Question

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-03T01:11:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8b88b4.148093455@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com>`

```
auburn82@iolfree.ie (Auburn) wrote:

>I am working on an assignment for college and am stuck on the
>following:
…[18 more quoted lines elided]…
>           02   ResourcePath            PIC X(80).

Others will tell you to use UNSTRING. Wrong. Your ResourcePath can contain
embedded spaces, which will be enclosed in quotes. UNSTRING cannot correctly
parse quoted strings. You'll have to do it yourself. 

Here is a simplified version of the parser in a Demo Program I posted here a
month ago. It is building a list entry for each word. You'll probably want to
put them into a table, so replace the list building code with simpler table
logic. 

Do try to write the parser as a separate 'program' within the same compile unit.
Doing so will get you extra points. 

 identification division.
 program-id. word-function.
*>author. Robert Wagner.
*>  Parser. Constructs word entries.
*>
 data division.
 working-storage section.
 01  unqualified-variables.
        05  n                   comp    pic s9(04).
        05  filler                      pic  x(01).
                88  in-a-word value 'w'.
                88  not-in-a-word value low-value.
        05  quote-character             pic  x(01).
        05  a-byte                      pic  x(01).

 01  a-word-area.
     05  a-word-length          comp   pic s9(04).
     05  a-word.
         10  a-word-byte occurs 1 to 300 depending on a-word-length pic x.

 linkage section.
     copy 'pfstruc.cpy'.

 procedure division using root-variables, program-entry.
 main.
     move low-values to unqualified-variables
     set address of line-entry to last-line
     set previous-last-line to last-line
     set address of word-entry to null

     perform varying n from 1 by 1 until n greater than line-length
         move line-byte (n) to a-byte  *> for speed
*> test whether this byte terminates the previous word
*> and  whether this byte begins or ends a quoted string
         if  a-byte equal to x'22' or x'27'
             evaluate true
                 when quote-character equal to low-value
                     if  in-a-word
                         perform end-word
                     end-if
                     move a-byte to quote-character
                 when quote-character equal to a-byte
                     perform end-word
                     move low-value to quote-character
             end-evaluate
         end-if
*> put this byte into a word if not a space
         evaluate true
             when quote-character not equal to low-value
                 perform put-byte-in-word
             when a-byte equal to space
                 continue
             when other
                 perform put-byte-in-word
         end-evaluate
     end-perform

     if  in-a-word
         perform end-word
     end-if

     goback.

 put-byte-in-word.
     if  not in-a-word
         perform start-word
     end-if
     add 1 to a-word-length
     move a-byte to a-word-byte (a-word-length).

 start-word.
     set in-a-word to true
     move zero to a-word-length
     move low-values to a-word-area.

 end-word.
     set not-in-a-word to true
     compute allocation-length =
         length of fixed-portion of word-entry + 2 + a-word-length
     set allocation-pointer to null
     call 'malloc' using allocation-length, allocation-pointer
     if  allocation-pointer equal to null
         set malloc-error to true
         display 'pf error constructing word ' return-code
         goback
     end-if
     set address of word-entry to last-word
     if  first-word equal to null
         set first-word to allocation-pointer
     else
         set next-word to allocation-pointer
     end-if
     set address of word-entry to allocation-pointer
     move a-word-length to word-length
     move low-values to fixed-portion of word-entry
     move last-word to previous-word
     move allocation-pointer to last-word
     move a-word to word-text.

 end program word-function.
```

##### ↳ ↳ Re: Beginner's Question

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-03T14:42:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6hh8b$nk8$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net>`

```

On  2-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> Others will tell you to use UNSTRING. Wrong. Your ResourcePath can contain
> embedded spaces, which will be enclosed in quotes. UNSTRING cannot correctly
> parse quoted strings. You'll have to do it yourself.

I told him to look at UNSTRING (and reference modification) - but also told him
that he needs to Know His Data.

Then I didn't write his program for him, figuring he will learn a lot better
with hints than by cutting and pasting someone else's work.
```

###### ↳ ↳ ↳ Re: Beginner's Question

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-04T01:59:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8ccc34.230921866@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  2-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[9 more quoted lines elided]…
>with hints than by cutting and pasting someone else's work.

The code I posted was deliberately approximate. He'd have to modify it for his
environment (table vs. list).

I see nothing wrong with students modelling code after well written examples as
opposed to using intuition. That's how I've taught programmers -- copy my style
until you feel confident you've developed your own voice. Then let's talk about
it. Trial-and-error and intuition are poor teachers.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-04T14:58:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6isep$qh5$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net>`

```
Robert Wagner wrote:

> The code I posted was deliberately approximate. 

But commpletely inappropriate.

> I see nothing wrong with students modelling code after well written
> examples 

Tell us again how you cried over the beauty of it.

> I see nothing wrong with students modelling code after well written 
> examples [...]
> Trial-and-error ... are poor teachers.

Trial and error is the _only_ mechanism for learning, good teachers create 
the trials and show how to notice the errors.

Poor teachers just prattle on about how wonderfully clever they are, and 
how everyone should copy what they do.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-04T18:29:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8dba83.32538985@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:

>> I see nothing wrong with students modelling code after well written 
>> examples [...]
…[3 more quoted lines elided]…
>the trials and show how to notice the errors.

I've never taught in a classroom setting. You seem to have experience, so I'll
grant you might be right. When teaching on the job, there is no time for trial
and error.

>Poor teachers just prattle on about how wonderfully clever they are, and 
>how everyone should copy what they do.

The purpose is education, not ego-gratification. After they develop skills,
which usually takes three months, they're encouraged to develop their own style.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-04T18:35:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6kja5$i5j$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net>`

```

On  4-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >Trial and error is the _only_ mechanism for learning, good teachers create
> >the trials and show how to notice the errors.
…[3 more quoted lines elided]…
> and error.

I don't see too many on-the-job CoBOL students asking beginner's questions here
- if they are being taught the way you recommend, they just get the answer from
the teacher.   If the teacher tells them to find out on their own, they
sometimes ask us - and we try to assist them in finding out on their own.

On the job training usually assumes that the person can program, but needs
assistance in what the shop needs.

> >Poor teachers just prattle on about how wonderfully clever they are, and
> >how everyone should copy what they do.
…[3 more quoted lines elided]…
> style.

I haven't seen this.   Do you encourage your students to develop their own
styles?   You certainly seem to demand that we switch to your style.  What makes
the people who work in your shop better suited for programming in a style
different from yours than we are?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T09:13:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8e8dbe.10017252@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  4-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[4 more quoted lines elided]…
>> I've never taught in a classroom setting. You seem to have experience, so
I'll
>> grant you might be right. When teaching on the job, there is no time for
trial
>> and error.

>On the job training usually assumes that the person can program, but needs
>assistance in what the shop needs.

No. I once hired a waitress who had no programming experience but had the
aptititude. I also hired a PhD whose only programming was in Fortran. 

Newbies can be easier to teach because you don't have to break bad habits
learned elsewhere. 

>> >Poor teachers just prattle on about how wonderfully clever they are, and
>> >how everyone should copy what they do.
…[6 more quoted lines elided]…
>styles?   You certainly seem to demand that we switch to your style.  What
makes
>the people who work in your shop better suited for programming in a style
>different from yours than we are?

We discuss the issues as reasonable (non-flaming) adults. If they convince me
their style is better, I adopt it. That has happened several times. The setting
is colleagues working in concert. 

Here we have people working in opposition. The flaming should make that evident.
There is no synergy here. It's just people shouting at each other. They're
looking to defend what they have rather than growing.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-05T11:05:57+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8eaa90_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e8e8dbe.10017252@news.optonline.net...
> "Howard Brazee" <howard@brazee.net> wrote:
>
>
> Here we have people working in opposition. The flaming should make that
evident.
> There is no synergy here. It's just people shouting at each other. They're
> looking to defend what they have rather than growing.
>

That applies to EVERYBODY here <G>?

I don't accept that the above describes my own behaviour or attitude, but it
is exactly the kind of statement that makes people flame and shout.

Beware of applying the general to the particular.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T18:46:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f16dd.45126250@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[10 more quoted lines elided]…
>That applies to EVERYBODY here <G>?

No, your posts have been informative and unemotional (until someone pulls on
your cape). 

>I don't accept that the above describes my own behaviour or attitude, but it
>is exactly the kind of statement that makes people flame and shout.

Nah. Personal criticism is brushed aside, except by a few thin-skinned
individuals. What sets them off is attacking the things they love .. periods,
mainframes, packed, etc. 

>Beware of applying the general to the particular.

It sounds better in Latin. Use in a sentence: 'You stupid shithead; you are
making the logical error of dicto simpliciter.'
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-07T14:56:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s3ih$8ak$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net>`

```

On  5-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >I don't accept that the above describes my own behaviour or attitude, but it
> >is exactly the kind of statement that makes people flame and shout.
…[3 more quoted lines elided]…
> mainframes, packed, etc.

Or we dislike being insulted, and we dislike being told that our ways are wrong
without backing them up with good reasons.

Funny how people don't like to be insulted.   Funny how when give examples that
are contrary to your claims - we are thick-skinned because we love periods,
mainframes, packed, etc.

Saying there is a place the above isn't "love".   And saying that your mandate
that we modernize by getting rid of periods misses the mark isn't "love".

Funny how the people who quote the manuals are wrong, and the person who
remembers things from 20 years ago is right.

Funny how when there is one person on one side vs the world - it is the world
which is thick-skinned.

We don't like being insulted.  We do like statements being backed up with logic.
  We don't like it when the person insulting us claims that what he said isn't
what he meant and only our stupidity caused this argument.

We don't like being insulted.

We don't like it when our arguments are discarded.  We don't like it when our
evidence is discarded.

We don't like being insulted.

There are flaming newsgroups that I have no intention of accessing.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T22:31:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e91c37c.75185032@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu>`

```
You the only participant _insulted_ every time the topic of periods comes up. If
it doesn't come up, you reintroduce it.

We have been over this ad nauseum. Everyone else is tired of hearing about it.
End of discussion .. PERIOD.  (see, you got the last word)


"Howard Brazee" <howard@brazee.net> wrote:

>
>On  5-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[24 more quoted lines elided]…
>We don't like being insulted.  We do like statements being backed up with
logic.
>  We don't like it when the person insulting us claims that what he said isn't
>what he meant and only our stupidity caused this argument.
…[8 more quoted lines elided]…
>There are flaming newsgroups that I have no intention of accessing.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-08T14:36:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6ump1$g9c$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net>`

```

On  7-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> You the only participant _insulted_ every time the topic of periods comes up.

If I am paranoid, I wouldn't know it - so I had better test this hypothesis.  It
would be useful for me to recognize a problem in myself and then start working
on it.

So everybody...

Is the above quote true?

Has Robert Wagner insulted only me?   Or has he insulted nobody and I am
paranoid in thinking that he has insulted me?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 13)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-08T09:22:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6usvu$1q52$1@si05.rsvl.unisys.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b6ump1$g9c$1@peabody.colorado.edu...

> If I am paranoid, I wouldn't know it - so I had better test this
hypothesis.  It
> would be useful for me to recognize a problem in myself and then start
working
> on it.
>
…[5 more quoted lines elided]…
> paranoid in thinking that he has insulted me?

I think he's insulted you.

I also think he's insulted the intelligence and the expertise of just about
all of the readership in this forum.

From my personal standpoint, my concern is that I believe he has repeatedly
and consistently demeaned and ridiculed the company I work for, the products
it makes, the manner which it supports its customers, and its continued
contributions to the history and future of COBOL.   I am personally more
concerned about that summary dismissal of the relevance of Unisys
Corporation in the computer industry than I am about any slights I might
regard as personal, and only hope that the readership recognizes these
dismissals as having as much relevance and factual substance as his
assertions that ACCEPT ... FROM DATE produces an eight-significant-digit
numeric value by default when the destination can contain at least eight
digits.

Since he has consistently demonstrated the ability to be flat wrong in
assertions of fact, my concern (and the primary reason for my continued
participation) is that the readership not be misled by such assertions.

      -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-08T17:04:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6uvea$lhk$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com>`

```

On  8-Apr-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> factual substance as his
> assertions that ACCEPT ... FROM DATE produces an eight-significant-digit
> numeric value by default when the destination can contain at least eight
> digits.

I forgot to mention - CoBOL on the VAX had this full date when I used it in the
1980s.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-08T17:11:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6uvre$lrs$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com>`

```

On  8-Apr-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> From my personal standpoint, my concern is that I believe he has repeatedly
> and consistently demeaned and ridiculed the company I work for, the products
> it makes, the manner which it supports its customers, and its continued
> contributions to the history and future of COBOL.

Maybe that's why I take the insults more personally than I do on, say a politics
or recreational forum.   Not only are my contributions demeaned, any company
that would hire me is also demeaned.  The tools that I use are demeaned.   All
the companies that I have worked for are doomed.

My career means something to me, as does my professionalism.  Might as well
insult my grandchildren (almost).

I were wrong in my arguments, I would feel the same way.  Being dismissed
doesn't lead me to listen as well as I should though.

But - even though I have been declared the loser, I haven't seen supporting
evidence to that "fact".   Evidence doesn't seem to matter though.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 15)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T00:53:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e936117_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com> <b6uvre$lrs$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b6uvre$lrs$1@peabody.colorado.edu...
>
> On  8-Apr-2003, "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>
> > From my personal standpoint, my concern is that I believe he has
repeatedly
> > and consistently demeaned and ridiculed the company I work for, the
products
> > it makes, the manner which it supports its customers, and its continued
> > contributions to the history and future of COBOL.
>
> Maybe that's why I take the insults more personally than I do on, say a
politics
> or recreational forum.   Not only are my contributions demeaned, any
company
> that would hire me is also demeaned.  The tools that I use are demeaned.
All
> the companies that I have worked for are doomed.
>

Howard, that is just patently untrue. I am required to hire people all the
time and if I could get guys of your calibre, I'd take them in a heartbeat.

You don't seriously think that one person's posts in a newsgroup are going
to affect your career, do you? (Irrespective of who wins the "argument"). If
you believe that, then you really ARE paranoid <G>.

> My career means something to me, as does my professionalism.  Might as
well
> insult my grandchildren (almost).
>

Professionalism is good. Pride in what you do is good. Professional pride is
VERY good. Exaggerate it and it becomes pomposity  (Not Good.)  How could
you, or would you, let an individual in a newsgroup destroy your
professional pride?  The answer is that you shouldn't and wouldn't.

> I were wrong in my arguments, I would feel the same way.  Being dismissed
> doesn't lead me to listen as well as I should though.
>
> But - even though I have been declared the loser, I haven't seen
supporting
> evidence to that "fact".   Evidence doesn't seem to matter though.

OK consider this...

"If you call a tail a leg, how many legs does a horse have?" (Attributed to
Abe Lincoln).

Many people will be persuaded to the answer: "Five".

Old Abe used to smile and say: "Nope. A horse has four legs. Calling a tail
a leg, doesn't make it one..."

Being declared the loser (by someone whose opinion you don't value anyway)
does not make you the loser...

The only way that statement can be true is if YOU agree with it <G>.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-09T14:18:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b71a49$1d1$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com> <b6uvre$lrs$1@peabody.colorado.edu> <3e936117_1@127.0.0.1>`

```

On  8-Apr-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> Being declared the loser (by someone whose opinion you don't value anyway)
> does not make you the loser...
>
> The only way that statement can be true is if YOU agree with it <G>.

You're right.  But I'm too human sometimes.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e96264f.362671018@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com> <b6uvre$lrs$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>My career means something to me, as does my professionalism.  Might as well
>insult my grandchildren (almost).

Same here. I have a personal investment in the stuff I posted. I'm  not a troll
or joke. Seeing it dismissed as stupid/C-style/whatever distressed me. 

>I were wrong in my arguments, I would feel the same way.  Being dismissed
>doesn't lead me to listen as well as I should though.

The reason I didn't reply to your NUMEROUS posts about periods was because they
didn't contain any new information. They were like spam mail. If you post
something substantive, I'll certainly respond.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T00:37:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e935d45_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:b6usvu$1q52$1@si05.rsvl.unisys.com...
>
> "Howard Brazee" <howard@brazee.net> wrote in message
…[15 more quoted lines elided]…
> I think he's insulted you.

Oh, Great, Chuck <G>... I guess you put fires out with gasoline too, right?


> I also think he's insulted the intelligence and the expertise of just
about
> all of the readership in this forum.
>

Well, we've all done that at some point <G>.

> From my personal standpoint, my concern is that I believe he has
repeatedly
> and consistently demeaned and ridiculed the company I work for, the
products
> it makes, the manner which it supports its customers, and its continued
> contributions to the history and future of COBOL.

Get a Grip! (Have you any idea how pompous that sounds? try reading it
aloud...) There is NO WAY that any poster here (let alone Robert) could in
any way diminish a reputable company like UNISYS. He's disagreed about the
way he THINKS UNISYS does things. Companies like IBM, MicroSoft, ORACLE, and
UNISYS get themselves and their products and representatives "demeaned and
ridiculed" every day. Usually it is done in heat, by people who are often
(not always...) uninformed. I've seen Richard make scathing comments about
MicroSoft (and their products), I've seen others here make negative comments
about Fujitsu and MicroFocus, I've seen mainframers ridicule Client server
and vice versa, and if I had a dollar for every negative comment I've made
about IBM, their products, their Managers....(don't start me <G>) I'd be a
VERY wealthy man (and I'm not...so just goes to show how far it gets you
<G>). The fact is that whether these criticisms are well founded, fair, or
just hopelessly off the beam, it makes no difference to the Companies
concerned.

Only if you start giving this kind of thing credence by taking it on board,
could it possibly be damaging.


>  I am personally more
> concerned about that summary dismissal of the relevance of Unisys
…[6 more quoted lines elided]…
>

Well, that it is a proper and noble position to take, but the fact is that
Robert's opinion about UNISYS, dates, or anything else, will have as much
effect on UNISYS as a company, as a mosquito might make on the exterior of
an Abrams tank.

> Since he has consistently demonstrated the ability to be flat wrong in
> assertions of fact, my concern (and the primary reason for my continued
> participation) is that the readership not be misled by such assertions.
>

Rest assured, they won't be.

They are far more likely to be turned off CLC by pedantic pointless
ego-massaging arguments, that go on for weeks, than they are to be swayed by
some corporate mudslinging.

Besides, you are here to set the record straight and have done so, right
<G>?

I have to confess my amazement when I see people of the calibre of yourself
and Howard perpetuating this nonsense.

If the guy winds you up so badly, then don't respond.  Or make a simple
rebuttal and leave it at that.

It is becoming very obvious to me that there are some very active minds here
with time on their hands...

That's sad.

Pete.





----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Unisys (was Re: Beginner's Question)

_(reply depth: 14)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-08T20:42:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E937A87.2030206@Knology.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
 > contributions to the history and future of COBOL.   I am personally more
 > concerned about that summary dismissal of the relevance of Unisys
 > Corporation in the computer industry than I am about any slights I might
 > regard as personal, and only hope that the readership recognizes these

Where do you work?  I've had lots of contact with Unisys people from
Montgomery and Niceville.  All outstanding folks that were more than
willing to help us.  Of course, we've been working on something that
seems to be a first in a deployed system - DMS and RDMS together in a
UCOB program with dual-commit.  :)

One of our contractors has been contacted by the folks who run the Unite
conference to do a one-hour speech about this.  I may get to tag along
to help answer questions on the application/MCB/DPS side of it.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e962abc.363804381@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>From my personal standpoint, my concern is that I believe he has repeatedly
>and consistently demeaned and ridiculed the company I work for, the products
…[3 more quoted lines elided]…
>Corporation in the computer industry

Give it a break. I haven't commented on Unisys, pro or con. 

When you last expressed a similar complaint, I bent over backwards to change the
language in my paper to avoid marginalizing Unisys and others such as Tandem.
This time there is nothing to change.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-14T13:20:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7f56a$pd9$1@si05.rsvl.unisys.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com> <3e962abc.363804381@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e962abc.363804381@news.optonline.net...

> Give it a break. I haven't commented on Unisys, pro or con.

You have continued to describe what "all compilers" and "all mainframes" do,
when neither "all compilers" nor "all mainframes" do what you claim.  Every
time you use such a generalization, any implementation that does not behave
the way you think it ought to behave is excluded from what "all compilers"
and "all mainframes" do.

> When you last expressed a similar complaint, I bent over backwards to
change the
> language in my paper to avoid marginalizing Unisys and others such as
Tandem.

I've pointed it out since then, I believe more than once, and I've pointed
out where you have marginalized Unisys products and the products of other
firms.

Despite that, you have continued to describe, and continue to describe, what
"all compilers" and "all mainframes" do, when neither "all compilers" nor
"all mainframes" do what you claim.  Just about every time you make such a
generalization, it's a case in which showing that the generalization is
false is a trivial exercize.

While you may have changed the document in which you originally made this
error, you have not taken care to change your style of presentation, in
which you dismiss as irrelevant all implementations save those with which
you are familiar.

> This time there is nothing to change.

This isn't just a matter of Unisys, or Tandem, it's a matter of
presentation.

A recent example:  "Contractors are not permitted to "protest loudly".  If
they try ..."  is another example.  Not all people hired as contract
programmers are subjected to such treatment.

Another, with respect to testing:  "In large shops, application programmers
do only Unit Test Plans, which are pretty much meaningles. ...".  In how
many large shops *outside* the handful you've described as being within your
experience?

Another, with respect to internal politics:  "In LARGE shops, there are
specialists who handle each task.  ... Application programmers spend 10% of
their time cranking code and 90% covering their boss' ass with
'documentation' which documents little except revealing who's at fault when
things go wrong. "   While I do not doubt that this has been true in *some*
large shops, and I also do not doubt that it has been your misfortune to
find this true in *all* the "large shops" in which you have worked, I work
in a shop that  I would characterize as  "large", and I don't find that
characterization to be true here.

Another, with respect to vendor responses to trouble reports with their
products:  "They don't listen ... or say it will take YEARS to effect a fix.
Justice delayed is justice denied.  I do the best I can with reality."   Our
goal in the products I work on is to have a correction for all demonstrable
errors in implementation for which the customer has requested a
high-priority response in the customer's hands within fifteen days of the
filing of the original trouble report.  There are exceptions -- for example,
if a trivial change to the program avoids the problem, or the customer fails
to provide us sufficient information to reproduce the problem, or the change
represents an architectural limitation within the product -- but by and
large that's the rule, and our record in conforming to that rule is, I
believe, quite good.  Here is a case in which the ubiquitous "they" paints
Unisys in a broad light because of inappropriate *inclusion* in a group
rather than *exclusion* from it.

These are some I've gleaned from within the last few days.  I'm sure a
dedicated Google search would unearth a few more.

It's the fact that you continue to generalize *all of* reality from your
experience, and by doing so you marginalize all those whose experience does
not match yours.  It's the presentation of your experience as the only
reality of note.  I grant that it may be the only reality of note *to you*,
but to state that your reality is normative for everyone else is
fundamentally dismissive.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 16)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-15T02:50:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9b6630.107679399@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com> <3e962abc.363804381@news.optonline.net> <b7f56a$pd9$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:


>While you may have changed the document in which you originally made this
>error, you have not taken care to change your style of presentation, in
>which you dismiss as irrelevant all implementations save those with which
>you are familiar.

As COBOL programmers, we've ALL been marginalized .. for the last twenty years.
If your skin is so sensitive, perhaps you should subscribe to the Language of
The Month Club. 

>This isn't just a matter of Unisys, or Tandem, it's a matter of
>presentation.
…[3 more quoted lines elided]…
>programmers are subjected to such treatment.

Just my anecdotal evidence, unanimously supported by anecdotes from other
contractors. 

>Another, with respect to testing:  "In large shops, application programmers
>do only Unit Test Plans, which are pretty much meaningles. ...".  In how
>many large shops *outside* the handful you've described as being within your
>experience?

All that employ a formal methodology. 

>Another, with respect to internal politics:  "In LARGE shops, there are
>specialists who handle each task.  ... Application programmers spend 10% of
…[6 more quoted lines elided]…
>characterization to be true here.

You're fortunate to work for an OEM and _medium sized_ company with annual
revenues of $5B. The smallest compay in the Fortune 50 had annual revenues of
$18B.  

http://www.fortune.com/fortune/fortune500/
>
>Another, with respect to vendor responses to trouble reports with their
…[12 more quoted lines elided]…
>rather than *exclusion* from it.

Having never dealt with Unisys support, I have no reason to doubt it is as you
represent.

>It's the fact that you continue to generalize *all of* reality from your
>experience, and by doing so you marginalize all those whose experience does
…[3 more quoted lines elided]…
>fundamentally dismissive.

I like your elegant lexicon in the last sentence. Very good.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 17)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-14T22:44:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304142144.46d2bb15@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6usvu$1q52$1@si05.rsvl.unisys.com> <3e962abc.363804381@news.optonline.net> <b7f56a$pd9$1@si05.rsvl.unisys.com> <3e9b6630.107679399@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> As COBOL programmers, we've ALL been marginalized .. for the last twenty years.


Speak for yourself, what evidence do you have that I have been 'marginalised' ?

In any case, if you have been marginalised, it may not be because of Cobol.
```

###### ↳ ↳ ↳ RW's insults (was: Beginner's Question

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-08T16:16:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6ve74$d4i$1@slb9.atl.mindspring.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu>`

```
Howard,
   If I recall correctly, the first time that I saw a post from Robert
Wagner in this newsgroup was his "best practices" posts.  Since that time, I
have seen him insult almost everyone who thinks that "their preferred style"
differs from HIS "best practice" style.  He tends to concentrate on
mainframe programmers (probably IBM mainframe programmers - as he seems
pretty ignorant of non-IBM mainframe environments - which is NOT to say that
he is correct in many of his assumptions about current IBM mainframe
environments).

You (Howard) are not the only person who has posted that you have reasons
for using periods in the procedure division where they are NOT required.
However, most of the other supporters of that viewpoint are less active in
this newsgroup.

RW seems quite unable to see the difference between "style" and
"requirements".  He assumes that his preferred style *must* be both the BEST
style and the only "modern" style.   As someone who actually DOES (in my
personal style) actually use a similar style to his for the use of periods,
I certainly understand that it is a STYLE issue and not something that has
no PROs and CONs.

Many of the people that RW has insulted and/or have "depressed" have given
up on either replying to him, or in some cases even participating in  the
NG.  This is not because he has EVER "won an argument" but rather because he
is so unwilling to admit his errors or even when something that he states is
an opinion rather than a fact. (Intelligent and thoughtful people don't need
to ALWAYS "have the last word" - RW does.)

A number of us have TRIED to explain to him why he is so widely "disparaged"
within the NG, but he seems totally unable to understand it.  I believe that
he probably has some pathological emotional/mental problems, but without
knowing him (God forbid!) in "real life" it is impossible for me to know
whether this is true or what type of "cure" he should seek.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-08T18:36:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6vitk$7gc$1@panix1.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net>`

```
In article <b6ve74$d4i$1@slb9.atl.mindspring.net>,
William M. Klein <wmklein@ix.netcom.com> wrote:

[snip]

>
>A number of us have TRIED to explain to him why he is so widely "disparaged"
…[4 more quoted lines elided]…
>

Mr Klein I try to leave matters of pathology to The Professionals... but 
years ago I was at a social gathering where a Professional was asked for 
an off-the-cuff diagnosis of a moderately odious character.

His evaluation was 'It is nothing a good case of reincarnation wouldn't 
cure.'

DD
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 15)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-08T15:48:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6vjj1$29dm$1@si05.rsvl.unisys.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <b6vitk$7gc$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b6vitk$7gc$1@panix1.panix.com...

> Mr Klein I try to leave matters of pathology to The Professionals... but
> years ago I was at a social gathering where a Professional was asked for
…[3 more quoted lines elided]…
> cure.'

My personal favorite along these lines described someone as having
"delusions of adequacy".

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-09T21:28:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b72hc3$rp3$1@panix5.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6ve74$d4i$1@slb9.atl.mindspring.net> <b6vitk$7gc$1@panix1.panix.com> <b6vjj1$29dm$1@si05.rsvl.unisys.com>`

```
In article <b6vjj1$29dm$1@si05.rsvl.unisys.com>,
Chuck Stevens <charles.stevens@unisys.com> wrote:
>
><docdwarf@panix.com> wrote in message news:b6vitk$7gc$1@panix1.panix.com...

[snip]

>> His evaluation was 'It is nothing a good case of reincarnation wouldn't
>> cure.'
>
>My personal favorite along these lines described someone as having
>"delusions of adequacy".

The one I recall along that line was 'delusions of competence'.

DD
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T01:25:07+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e93686d_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b6ve74$d4i$1@slb9.atl.mindspring.net...
> Howard,
>    If I recall correctly, the first time that I saw a post from Robert
> Wagner in this newsgroup was his "best practices" posts.  Since that time,
I
> have seen him insult almost everyone who thinks that "their preferred
style"
> differs from HIS "best practice" style.  He tends to concentrate on
> mainframe programmers (probably IBM mainframe programmers - as he seems
> pretty ignorant of non-IBM mainframe environments - which is NOT to say
that
> he is correct in many of his assumptions about current IBM mainframe
> environments).
>
I never saw the "Best Practice" document. Would I be as incensed as
everybody else if I had?

> You (Howard) are not the only person who has posted that you have reasons
> for using periods in the procedure division where they are NOT required.
> However, most of the other supporters of that viewpoint are less active in
> this newsgroup.
>

However, Howard IS the only one who regularly responds on this topic. (Not
commenting on the rights and wrongs; just the observable fact...)

> RW seems quite unable to see the difference between "style" and
> "requirements".  He assumes that his preferred style *must* be both the
BEST
> style and the only "modern" style.   As someone who actually DOES (in my
> personal style) actually use a similar style to his for the use of
periods,
> I certainly understand that it is a STYLE issue and not something that has
> no PROs and CONs.
>
Absolutely. That is why style wars are a waste of time here. They come down
to preferences, not rights and wrongs.

> Many of the people that RW has insulted and/or have "depressed" have given
> up on either replying to him, or in some cases even participating in  the
> NG.

I know. I've seen it. I am not certain that RW alone is totally responsible
for this.


This is not because he has EVER "won an argument" but rather because he
> is so unwilling to admit his errors or even when something that he states
is
> an opinion rather than a fact. (Intelligent and thoughtful people don't
need
> to ALWAYS "have the last word" - RW does.)
>
> A number of us have TRIED to explain to him why he is so widely
"disparaged"
> within the NG, but he seems totally unable to understand it.  I believe
that
> he probably has some pathological emotional/mental problems, but without
> knowing him (God forbid!) in "real life" it is impossible for me to know
…[27 more quoted lines elided]…
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-09T14:25:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b71agd$1jn$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3e93686d_1@127.0.0.1>`

```

On  8-Apr-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> However, Howard IS the only one who regularly responds on this topic. (Not
> commenting on the rights and wrongs; just the observable fact...)

Thanks for the feedback.  I shall desist.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T01:40:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e936bfd_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net>`

```
Sorry,

My response to this was posted prematurely. This post picks up from where
the other one left off...

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b6ve74$d4i$1@slb9.atl.mindspring.net...
>  This is not because he has EVER "won an argument" but rather because he
> is so unwilling to admit his errors or even when something that he states
is
> an opinion rather than a fact. (Intelligent and thoughtful people don't
need
> to ALWAYS "have the last word" - RW does.)
>
> A number of us have TRIED to explain to him why he is so widely
"disparaged"
> within the NG, but he seems totally unable to understand it.  I believe
that
> he probably has some pathological emotional/mental problems, but without
> knowing him (God forbid!) in "real life" it is impossible for me to know
> whether this is true or what type of "cure" he should seek.

So, if he doesn't agree after having it "explained" he is mentally unstable
<G>?

Anyone who doesn't accept the "explanation" is a loony?

Isn't this exactly the position that Robert stands accused of adopting, in
his posts to others?

When did the cure become the disease?

What is SO IMPORTANT here that a group of educated, intelligent,
professional people will get so unwrapped or slink off and sulk about it?

There is an old adage that it is impossible to insult an honest man. (If the
insult is true, he simply accepts it, if it isn't, he ignores it; either way
his equilibrium is undisturbed...)

It is only computer programming...meanness and other Human emotions are best
left out of it.

Pete.







----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 15)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-08T20:04:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E937197.50205@Knology.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3e936bfd_1@127.0.0.1>`

```
Peter E.C. Dashwood wrote:
> 
> It is only computer programming...meanness and other Human emotions are best
> left out of it.

So that's why I'm a troll who doesn't have any business laying a line of 
COBOL?  :)

(sorry - couldn't resist...)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T09:55:55+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e93e025_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3e936bfd_1@127.0.0.1> <3E937197.50205@Knology.net>`

```

"LX-i" <DanielJS@Knology.net> wrote in message
news:3E937197.50205@Knology.net...
> Peter E.C. Dashwood wrote:
> >
> > It is only computer programming...meanness and other Human emotions are
best
> > left out of it.
>
…[4 more quoted lines elided]…
>
<G> It's OK...it's a free forum...

I didn't say you had no business laying a line of COBOL. Those are YOUR
words...

I did assume you were trolling.   Despite strong indications to support
this, I may have been wrong, and I apologized for it in a subsequent post.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 15)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-09T15:50:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304091450.34b21917@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3e936bfd_1@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> There is an old adage that it is impossible to insult an honest man. (If the
> insult is true, he simply accepts it, if it isn't, he ignores it; either way
> his equilibrium is undisturbed...)

But then there is a difference between this and concluding that
because one is insulted therefore one is an honest man.

Or indeed that if it is ignored it therefore must be not true.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-09T21:36:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b72hqp$sdi$1@panix5.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6ump1$g9c$1@peabody.colorado.edu> <3e936bfd_1@127.0.0.1>`

```
In article <3e936bfd_1@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>What is SO IMPORTANT here that a group of educated, intelligent,
>professional people will get so unwrapped or slink off and sulk about it?
>

Eh?  What's that?  Where have you found such a group?  Would you be so 
kind as to arrange an introduction for me?

DD
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-10T02:59:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94d001_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6ump1$g9c$1@peabody.colorado.edu> <3e936bfd_1@127.0.0.1> <b72hqp$sdi$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b72hqp$sdi$1@panix5.panix.com...
> In article <3e936bfd_1@127.0.0.1>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
…[9 more quoted lines elided]…
>
It's OK, Doc...I should have stated that you were not included...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-10T06:31:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b73h5v$3r9$1@panix5.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e936bfd_1@127.0.0.1> <b72hqp$sdi$1@panix5.panix.com> <3e94d001_2@127.0.0.1>`

```
In article <3e94d001_2@127.0.0.1>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b72hqp$sdi$1@panix5.panix.com...
…[12 more quoted lines elided]…
>It's OK, Doc...I should have stated that you were not included...<G>

Story of my life aye.

DD
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-10T02:30:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94d717.276842182@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3e936bfd_1@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:


>It is only computer programming...meanness and other Human emotions are best
>left out of it.

Your posts are a model of equanimity. Please don't stop. Especially the part
about freedom of speech.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 14)_

- **From:** Steve Thompson <n_o_spam.steve_t@ix.netcom.com>
- **Date:** 2003-04-08T21:07:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E937263.4060301@ix.netcom.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net>`

```
William M. Klein wrote:
> Howard,
>    If I recall correctly, the first time that I saw a post from Robert
…[6 more quoted lines elided]…
> environments).
<snip>

Periods to me are somewhat of a "religious" thing. So I bowed 
out. I use them to avoid AMBIGUITY. I also use END-IF and the like.

Top down structure (ridged adherence) to me is also a religious 
argument. It is because I am an ALC programmer (first) and a 
COBOL programmer second that I have the style that I do for 
writing code.

In ALC I normally write "normal" code that flows and doesn't 
contain the hard and odd instructions (e.g., BXH, BXLE, PLO, 
etc.). But the moment I have to write or fix an SVC or other high 
use systems routine I change gears radically and start writing 
code based on CACHE LINES and PIPELINE processing. The end result 
of that looks like "spaghetti" code.

So when we talk of best practices, I try to write code that 
someone who follows me will be able to read and modify. I try to 
use the "crystal ball" to figure out what will possibly need to 
be done to the program in the future when I am writing it.

Because of having also been an RPG programmer, I like and prefer 
to use Report Writer if it is available. So that also tends to 
taint my view of things.

I've been involved in migrations between various different 
platforms, but I also do program on other than a Mainframe. I 
prefer to use hi-level languages when I'm not on a mainframe or 
other architecture that I am well versed with.

I've dealt with all kinds of people at the management level and 
in the trenches (I've been on both sides of the desk).

It did not take me very much time to realize where things were 
going. 25+ years of experience where I did far more than repeat 
the first 6 months 50+ times.

And as you will recall, I even went sparring with J4 over the 
free format design because of a problem that I can see coming.

So, I chose to bail early and because of how busy I am with a 
client that is hell bent for leather to leave the mainframe, I've 
just not had a lot of time to spend. I've also got articles to 
review and write for two publications (I'm both an author and an 
editor). Plus, I have to do 1-2 presentations a month. So I am 
rather busy.

I don't take long to review resumes (I do them, not HR) and I 
don't take long to interview someone technically.

So it did not take me long to realize this guy was a troll. I'm 
sorry it took the rest of you so long.

<rant>

All the bulls**t about freedom of speech and the like. I've heard 
it all before. If I can train a dog or cat to be house broken, 
then I should be able to train a child. And if I can't then how 
could I possibly deal with a bore? Logic, just plain old logic, 
and some experience tells me that when my daughter can't get what 
she wants by whining she will change her methods. When my son 
can't manipulate me into doing what he wants (he's 18), he finds 
that he follows the rules or he will be living on the front porch 
or under the deck or at some "friend's" house.

"History will have to record that the greatest tragedy of this 
period of social transition was not the vitriolic words and 
violent actions of the 'bad' people ï¿½ but the appalling silence 
and indifference of the 'good' people." [When Good People Do 
Nothing, by James Randall Noblitt and Pamela Perskin]

</rant>
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 15)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T11:13:20+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e93ec4e_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com>`

```
 A good rant, Steve.

The ONLY thing I take issue with is that "Freedom of Speech" is Bullshit.

If we don't defend it, it will be <G>.

Pete.

"Steve Thompson" <n_o_spam.steve_t@ix.netcom.com> wrote in message
news:3E937263.4060301@ix.netcom.com...
> William M. Klein wrote:
> > Howard,
> >    If I recall correctly, the first time that I saw a post from Robert
> > Wagner in this newsgroup was his "best practices" posts.  Since that
time, I
> > have seen him insult almost everyone who thinks that "their preferred
style"
> > differs from HIS "best practice" style.  He tends to concentrate on
> > mainframe programmers (probably IBM mainframe programmers - as he seems
> > pretty ignorant of non-IBM mainframe environments - which is NOT to say
that
> > he is correct in many of his assumptions about current IBM mainframe
> > environments).
…[83 more quoted lines elided]…
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 16)_

- **From:** Steve Thompson <n_o_spam.steve_t@ix.netcom.com>
- **Date:** 2003-04-09T08:19:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E940FC7.6070001@ix.netcom.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1>`

```
Peter E.C. Dashwood wrote:
>  A good rant, Steve.
> 
…[4 more quoted lines elided]…
> Pete.
<snip>

Your rights end where they intersect with mine is the point I am 
trying to get people to see. Even the courts recognize this, 
hence the idea that you can't yell "FIRE" in a theatre. Your 
freedom of speech ends where exercise of same would do damage to 
someone else. It also ends where I don't want to hear it and 
decide to turn off the device or stop paying attention.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 17)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-10T01:44:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94be7c_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com>`

```

"Steve Thompson" <n_o_spam.steve_t@ix.netcom.com> wrote in message
news:3E940FC7.6070001@ix.netcom.com...
> Peter E.C. Dashwood wrote:
> >  A good rant, Steve.
> >
> > The ONLY thing I take issue with is that "Freedom of Speech" is
Bullshit.
> >
> > If we don't defend it, it will be <G>.
…[10 more quoted lines elided]…
>
It's an interesting idea. I don't believe that your turning off the device
or not paying attention, ends my right to Free Speech. Obviously, in a
democracy we should all pay attention to the rights of individuals. However,
I am of the opinion (and I respect your right to disagree...<G>) that there
are some basic fundamental Human Rights that cannot, and must not be
compromised. Free Speech is one of these.

I have no problem with you not listening and I respect your right to turn
off, lower the volume, or turn away and do something else. But  I cannot
accept that the exercise of this right will do "damage to someone else".

See, if I believed that, I would have to believe that ANYTHING that
"damaged" ANYBODY (read; "is unpalatable to them" or "is not in agreement
with the Party Line") should be banned.

The next step is the banning of controversial ideas because they might upset
some people.

Before too long this path arrives at the "Nanny State" where someone in
"Authority" decides what you can look at and what you can be allowed to hear
or see...

Across the centuries of recorded Human History people have died for the
right to a voice. If  you personally feel that that impinges on your rights
then you have the right to not listen. You do NOT have the right to suppress
the voice...

As for yelling "FIRE" in a theatre, that is NOT an exercise of Free Speech,
that is simply mischief. <G>.

Pete.

>
> --
…[8 more quoted lines elided]…
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 18)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-04-10T02:24:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030409222456.26027.00001111@mb-fd.aol.com>`
- **References:** `<3e94be7c_2@127.0.0.1>`

```
>From: "Peter E.C. Dashwood" dashwood@enternet.co.nz 
>Date: 4/9/03 8:44 PM Eastern Daylight Time

>I have no problem with you not listening and I respect your right to turn
>off, lower the volume, or turn away and do something else. But  I cannot
>accept that the exercise of this right will do "damage to someone else".
>

>
>See, if I believed that, I would have to believe that ANYTHING that
>"damaged" ANYBODY (read; "is unpalatable to them" or "is not in agreement
>with the Party Line") should be banned.
>

It's already starting - can you say "Polictically Correct"?  

>banned.
>
>The next step is the banning of controversial ideas because they might upset
>some people.
>

It's already happening - how many radio talk show hosts (mostly locals I'll
admit) have been fired, censured, etc etc because they voiced or allowed a
caller to voice an opinion that upset some biggy wiggy.  In my market a
particularly brillant commentator was first sent to 'sensitivity' training
because he made a so call 'racist' and 'rude' remark about the Reverend Jackson
and the local equivalent got up on his pulpit, then later he used the remark of
a caller calling our US Congresswoman - oops Congressional Representative (see
comment above <g>), a Democratic whore in his promo spot and that finally got
him fired.  And I believe both CNN and FOX have interviewed a 'dj' from public
radio that was also fired for an 'opinion'.

'tis a fine line between free speech and yelling FIRE in a crowded theater.  It
takes a well educated public to know the difference and that unfortunately is
also something we don't have.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 19)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-10T06:36:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b73hft$465$1@panix5.panix.com>`
- **References:** `<3e94be7c_2@127.0.0.1> <20030409222456.26027.00001111@mb-fd.aol.com>`

```
In article <20030409222456.26027.00001111@mb-fd.aol.com>,
YukonMama <yukonmama@aol.com> wrote:
>>From: "Peter E.C. Dashwood" dashwood@enternet.co.nz 
>>Date: 4/9/03 8:44 PM Eastern Daylight Time
…[22 more quoted lines elided]…
>caller to voice an opinion that upset some biggy wiggy.

Ummmmmm... last I looked a 'radio station' despite certain public 
responsibilities, is still a privately-owned enterprise (even the old 
'equal time' restrictions have been toned-down); the owner of said 
enterprise can put on the air or take off the air whoever it sees fit 
(within of course, legal limits).

I cannot remember the source but... 'freedom of the press belongs to those 
who own one'; there is no legal requirement to provide a forum.

DD
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-10T13:43:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b73sdt$77h$1@peabody.colorado.edu>`
- **References:** `<3e94be7c_2@127.0.0.1> <20030409222456.26027.00001111@mb-fd.aol.com>`

```

On  9-Apr-2003, yukonmama@aol.com (YukonMama) wrote:

> >See, if I believed that, I would have to believe that ANYTHING that
> >"damaged" ANYBODY (read; "is unpalatable to them" or "is not in agreement
…[3 more quoted lines elided]…
> It's already starting - can you say "Polictically Correct"?

It's always been around - can you say "heresy"?
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 18)_

- **From:** Steve Thompson <n_o_spam.steve_t@ix.netcom.com>
- **Date:** 2003-04-09T23:18:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E94E28C.9010405@ix.netcom.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1>`

```
Peter E.C. Dashwood wrote:
<snip>
> I have no problem with you not listening and I respect your right to turn
> off, lower the volume, or turn away and do something else. But  I cannot
> accept that the exercise of this right will do "damage to someone else".
<snip>
Suppose that I were to tell anyone who would listen, "Are you 
aware that E.C. Dashwood is a serial murderer and rapist"?

And now, is your right to privacy being infringed on? Or am I 
just exercising my right to "free speech?"

If you look at the US Constitution, the 1st Amendment refers to 
POLITICAL free speech.

My telling everyone that you have committed some crime that is 
not true is something that you are saying I have a right to do.
<snip>
> 
> See, if I believed that, I would have to believe that ANYTHING that
> "damaged" ANYBODY (read; "is unpalatable to them" or "is not in agreement
> with the Party Line") should be banned.
<snip>
So, I should be allowed to commit slander and/or defamation?
<snip>
> 
> The next step is the banning of controversial ideas because they might upset
…[12 more quoted lines elided]…
> that is simply mischief. <G>.
<snip>
But you have now decided that my idea of controlling a crowd to 
get what I want regardless of their needs or comfort is not Free 
Speech.

Me thinks you need to re-think the whole free speech issue. And 
if your ideas are based on what is spelled out in the "Bill of 
Rights", then perhaps you (just as the Supremes) should go back 
and read them again to be sure of what they actually say.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 19)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-10T12:14:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e955227_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com>`

```

"Steve Thompson" <n_o_spam.steve_t@ix.netcom.com> wrote in message
news:3E94E28C.9010405@ix.netcom.com...
> Peter E.C. Dashwood wrote:
> <snip>
> > I have no problem with you not listening and I respect your right to
turn
> > off, lower the volume, or turn away and do something else. But  I cannot
> > accept that the exercise of this right will do "damage to someone else".
…[3 more quoted lines elided]…
>
The people who know me would laugh in your face, the ones who don't wouldn't
care, and I would exercise my right of Free Speech to rebut your accusation,
always assuming that I felt threatened by your accusation. Do you not think
that sometime in my life I have been subject to calumny and false
accusation, Steve? Most of us have. Our right to a hearing is the best
defense we have against it.

> And now, is your right to privacy being infringed on? Or am I
> just exercising my right to "free speech?"
>
My right to privacy has little to do with your right to free speech. If what
you are saying is obviously untrue, you can shout it from the rooftops or
drop a million leaflets over the city where I live, and it still won't
infringe my privacy. (It WOULD infringe my privacy if you had people with
telephoto lenses hiding in the shrubbery around my house, but that is a
separate issue, and besides, after a few of them were eaten by the trained
tigers and crocodiles, the rest would probably take the hint and seek other
employment...<G>)

> If you look at the US Constitution, the 1st Amendment refers to
> POLITICAL free speech.
>

Sorry, I don't have a copy of the US Constitution to hand, and no matter how
worthwhile this document undoubtedly is, my defense of Free Speech is not
predicated on it, so I don't really care what it says. I don't live in the
USA so I am not "protected" by it.

My defence of Free Speech is not based on the rights guaranteed by ANY
political document; rather, I believe it is a fundamental right that ALL
Human Beings are entitled to, simply by virtue of the fact that, as a
species, we have developed communication and language skills to a very high
degree (to the point where we can ponder abstract thoughts and have this
conversation), and this ability has been fundamental to the progress of
Mankind. History has shown that the first thing tyrants do is try to prevent
the free exchange of ideas. (That is why Police States control the press and
communication media and don't allow groups of people to get together in
public.)

> My telling everyone that you have committed some crime that is
> not true is something that you are saying I have a right to do.
> <snip>

Absolutely. You have a right to make a fool of yourself if that is what you
want to do.

> >
> > See, if I believed that, I would have to believe that ANYTHING that
> > "damaged" ANYBODY (read; "is unpalatable to them" or "is not in
agreement
> > with the Party Line") should be banned.
> <snip>
…[3 more quoted lines elided]…
> > The next step is the banning of controversial ideas because they might
upset
> > some people.
> >
> > Before too long this path arrives at the "Nanny State" where someone in
> > "Authority" decides what you can look at and what you can be allowed to
hear
> > or see...
> >
> > Across the centuries of recorded Human History people have died for the
> > right to a voice. If  you personally feel that that impinges on your
rights
> > then you have the right to not listen. You do NOT have the right to
suppress
> > the voice...
> >
> > As for yelling "FIRE" in a theatre, that is NOT an exercise of Free
Speech,
> > that is simply mischief. <G>.
> <snip>
> But you have now decided that my idea of controlling a crowd to
> get what I want regardless of their needs or comfort is not Free
> Speech.

Sorry, I fail to see any logical connection here. You would need to expand
your argument so I can grasp it. (I'm not very bright sometimes...<G>) How
does yelling "Fire!" relate to controlling a crowd to get what you want? I'm
lost....
>
> Me thinks you need to re-think the whole free speech issue. And
…[3 more quoted lines elided]…
>

I have thought about this issue and defended it for most of my working life.
It comes from working on a newspaper when I was very young and absorbing
some of the values of my older, wiser, mentors. However, in light of this
discussion I am happy to revisit my position on this and think it through
again...(makes coffee, ponders the question of Free Speech for 15 minutes
and finds that his mind hasn't changed for the last 40 years on this...<G>
Does that mean I am an incurable reactionary, or is it that what I adopted
forty years ago still seems perfectly valid in the light of today's world?
There are some axioms of existence which have always been true and will
always be true, fundamental truths that we must not allow to be diluted,
warped, politicised, or demeaned. The right to Free Speech is one such. "I
may not agree with what you say, but I shall defend unto death, your right
to say it." (I don't know who first said that, but it sure works for
me..<G>)

As for the Bill of Rights, I already explained above that my defense of free
speech is not based on ANY political document.

It is bigger than politics.

However, it is interesting to note in passing that various people have tried
to politically enshrine this right when they have been oppressed, and the
result has been some truly awe-inspiring documents (like the US
Constitution, the Bill of Rights, the United Nations Charter, and Magna
Carta...)

It is probably no accident that the Dashwood family motto is "pro Magna
Carta"...I guess our family has felt  very strongly about this for a very
long time <G> (Magna Carta was signed by King John in 1215 and gave rights
to the people of England, one of which was the right to a hearing before a
group of your peers - the first intimations of free speech in the UK at
least...)

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 20)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-10T06:26:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E955500.7090501@Knology.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1>`

```
Peter E.C. Dashwood wrote:
> My defence of Free Speech is not based on the rights guaranteed by ANY
> political document; rather, I believe it is a fundamental right that ALL
…[4 more quoted lines elided]…
> Mankind.

Our Declaration of Independence agrees with you.  "...that they are 
endowed by their Creator with certain inalienable rights..."  The source 
of the rights is -not- the Constitution, but the Creator.  :)  The 
Constitution (and its amendments, specifically the first 10) just spells 
them out.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 21)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-10T13:47:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b73sm3$78a$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net>`

```

On 10-Apr-2003, LX-i <DanielJS@Knology.net> wrote:

> Our Declaration of Independence agrees with you.  "...that they are
> endowed by their Creator with certain inalienable rights..."  The source
> of the rights is -not- the Constitution, but the Creator.  :)  The
> Constitution (and its amendments, specifically the first 10) just spells
> them out.

I never quite "got" this part.   I have never been able to tell the difference
between inalienable rights and alienable rights.   Certainly states have long
histories of not letting everybody exercise these rights.    Is there any way to
observe and quantify our natural rights?   How do we tell the difference between
a right and a want?

I feel better by demanding that my leaders agree to the limitations to their
powers as set on paper in the Constitution.
```

###### ↳ ↳ ↳ OT: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 22)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-10T17:28:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E95F010.70804@Knology.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b73sm3$78a$1@peabody.colorado.edu>`

```

Howard Brazee wrote:
> On 10-Apr-2003, LX-i <DanielJS@Knology.net> wrote:
> 
…[12 more quoted lines elided]…
> a right and a want?

Just because there is a history of states not allowing these rights 
doesn't mean that they're any less inherent.

- The right to life is a no-brainer (although that phrase would ignite a 
discussion that no one probably wants in this group).

- The right to liberty, of necessity, involves restrictions on certain 
sorts of behavior, especially that which interferes with other's 
aforementioned right to life.  This is where the government "of the 
people, by the people, for the people" comes in.  Our republic allows 
our elected legislators to enact laws that encourage order.  Have 
legislatures abused this responsibility?  Absolutely.  That doesn't 
diminish the principle, though.

- The right to the pursuit of happiness is the most subjective of these 
rights, but again, is allowed, provided your behavior falls within 
established laws.  It may make you happy to shoot someone who annoys 
you, but that is where the laws come in and clarify that, no, you can't 
really pursue happiness -that- way.  :)

> I feel better by demanding that my leaders agree to the limitations to their
> powers as set on paper in the Constitution.

How about amendment #10 - All powers not expressly given to the federal 
government shall be reserved to the several states...  That's one's gone 
out the window.  And, on this point, we agree - the biggest problem with 
our government today is that we're doing far more in our government than 
the founders of our country ever intended.  Besides, we always hear how 
government screws things up - why then do so many special interest 
groups want the government to do things for them?  The only advantage I 
can see for them is that they can make everyone in America pay for it. 
There's a reason we weren't founded as a socialist nation...


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: OT: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 23)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-11T00:56:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E96116F.5CC6D9B2@shaw.ca>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b73sm3$78a$1@peabody.colorado.edu> <3E95F010.70804@Knology.net>`

```


LX-i wrote:

> Howard Brazee wrote:
> > On 10-Apr-2003, LX-i <DanielJS@Knology.net> wrote:
…[22 more quoted lines elided]…
> sorts of behavior,

<snip>

You can beat your breast on this one - individual freedoms and interpretation of
written statutes. But here's a sobering thought -

ALL of us in this News Group have the citizen's right to vote for the government we
want, (hoping that our (wo)man gets in).  However NOT ONE OF US has ever had the
opportunity to vote for our country's foreign policy. This is determined by the
currently governing elite backed up by the big commercial money !

If anybody disputes above about foreign policy - which election and which politician's
agenda did you go for.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: OT: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 24)_

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-04-11T08:59:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0304110759.362d1001@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b73sm3$78a$1@peabody.colorado.edu> <3E95F010.70804@Knology.net> <3E96116F.5CC6D9B2@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3E96116F.5CC6D9B2@shaw.ca>...
> LX-i wrote:
> 
…[4 more quoted lines elided]…
> (wo)man gets in).

Well, you are right, but only in the sense that many totalitarian
states block access to Google ;-)

Thus we are a preselected sample -- if we can get here it is highly
likely that we were able to vote...
```

###### ↳ ↳ ↳ Re: OT: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 25)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-11T21:19:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E97779D.20400@Knology.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b73sm3$78a$1@peabody.colorado.edu> <3E95F010.70804@Knology.net> <3E96116F.5CC6D9B2@shaw.ca> <16e2f010.0304110759.362d1001@posting.google.com>`

```
Joe Zitzelberger wrote:
> "James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3E96116F.5CC6D9B2@shaw.ca>...
> 
…[6 more quoted lines elided]…
>>(wo)man gets in).

I don't know how you snipped that, but that's not what I wrote - that's 
what someone else wrote...

> Well, you are right, but only in the sense that many totalitarian
> states block access to Google ;-)
> 
> Thus we are a preselected sample -- if we can get here it is highly
> likely that we were able to vote...

Voting is great - whether a democracy or a republic (although I tend to 
prefer the latter)...  :)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: OT: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-11T14:50:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76kng$oc1$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b73sm3$78a$1@peabody.colorado.edu> <3E95F010.70804@Knology.net>`

```

On 10-Apr-2003, LX-i <DanielJS@Knology.net> wrote:

> > I never quite "got" this part.   I have never been able to tell the
> > difference
…[26 more quoted lines elided]…
> really pursue happiness -that- way.  :)

You pretty much said what it says.   I repeat my question:   Is there any way to
observe and quantify our natural rights?   How do we tell the difference between
a right and a want?

The answer almost has to be "it's intuitively obvious".     Obviously we can't
always exercise these rights.   So what's the difference between rights that we
have and can't use and not having them as rights?   I don't see any way of
measuring a difference.

> > I feel better by demanding that my leaders agree to the limitations to their
> > powers as set on paper in the Constitution.
>
> How about amendment #10 -

Or even #9.
```

###### ↳ ↳ ↳ Re: OT: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 24)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-12T00:26:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e974f45_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b73sm3$78a$1@peabody.colorado.edu> <3E95F010.70804@Knology.net> <b76kng$oc1$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b76kng$oc1$1@peabody.colorado.edu...
>
> You pretty much said what it says.   I repeat my question:   Is there any
way to
> observe and quantify our natural rights?   How do we tell the difference
between
> a right and a want?
>

The rights we are talking about are Axiomatic. (Self-evidently true).

The right to free speech is a right, rather than a want, because it took us
millions of years to develop it and without it, communication is rendered
extremely difficult. Without communication and the ability to pass
information to current and future generations, we would not have developed
the intelligence that gives us our favoured position on this planet.

Unless our intelligence is challenged it will atrophy.

Exposure to new and different ideas provides this stimulation.

Every individual should be encouraged to participate because otherwise, we
cannot know what new ideas or perspectives their heads may contain.
Sometimes their ideas will be wicked and evil, sometimes they will be
unpalatable and unworthy, sometimes they will be ineffable and sublime.
Unless we hear them we cannot decide.

That's why free speech is important.

You have the right not to listen. You certainly have the right to disagree.
You do NOT have the right to suppress the communication.

(Of course, how you react if you DO listen, is a measure of your personal
growth and has nothing to do with the right of free speech... Blaming free
speech because you are not hearing what you would like to, is like trying to
ban bananas because sometimes people have an accident with the carelessly
discarded skin....)

Like I said earlier, it is much bigger than politics and does not need to
draw on any particular document  (or Religious Being)for its power.
Arguments based on the wording of documents (whether Holy or Secular) make
no difference to the underlying principle. You have a RIGHT to free speech.

> The answer almost has to be "it's intuitively obvious".     Obviously we
can't
> always exercise these rights.   So what's the difference between rights
that we
> have and can't use and not having them as rights?   I don't see any way of
> measuring a difference.
>

The only time we can't exercise these rights is when other people try to
take them off us, usually for their own ends or with a view to controlling
us.

And that is why people will struggle for lifetimes to regain the exercise of
what they know innately is a fundamental right.

And so Empires, Dictators and Tyrants are eventually, inevitably, toppled.

> > > I feel better by demanding that my leaders agree to the limitations to
their
> > > powers as set on paper in the Constitution.
> >

Limiting the power of an elected authority is a sensible thing to do;
suppressing the rights of a populace is another thing entirely.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: OT: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T23:58:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e97563b.53922700@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b73sm3$78a$1@peabody.colorado.edu> <3E95F010.70804@Knology.net> <b76kng$oc1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:


>The answer almost has to be "it's intuitively obvious".     Obviously we can't
>always exercise these rights.   So what's the difference between rights that we
>have and can't use and not having them as rights?   I don't see any way of
>measuring a difference.

I answered this question in the original thread. Look for Puritan and Locke.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-10T22:50:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e95f278.349397767@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b73sm3$78a$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 10-Apr-2003, LX-i <DanielJS@Knology.net> wrote:
…[9 more quoted lines elided]…
>histories of not letting everybody exercise these rights.    Is there any way
to
>observe and quantify our natural rights?   How do we tell the difference
between
>a right and a want?
>
>I feel better by demanding that my leaders agree to the limitations to their
>powers as set on paper in the Constitution.

A good working definition of 'right' is 'a privilege explicitly granted by law.'
There are no 'inalienable' rights. The notion came from two sources:

[clipped from an article about Oliver Cromwell I wrote ten years ago]
 The fundamental source of liberty is a culture's spiritual attitude to
 tolerate (or not) unconformity. This, in turn, is a function of the
 balance of power between the people as a whole vs. the privileged few
 who lead. Throughout most of history the government was assumed to be
 supreme. The Puritan Revolution of the 1640's, which drew its strength
 from the religious concept of freedom of conscience, established the
 principle of congregationalism. It stated for the first time that
 political authority rested with the people, who were the true
 sovereign, and that government was its servant not its master. This
 change in thinking is the direct source of the US Bill of Rights,
 particularly the first amendment. It had enormous impact on political
 thinking.

 Indeed, it seems
 counterintuitive that Puritans, the most repressive of religious
 movements, would be the ones to 'invent' liberty. Not so. They invented
 it as self-protection from their own intolerance, which they
 recognized would cause their destruction if allowed to run unchecked.
 Whereas other political styles could muddle through with less
 rigorous control of power relationships, puritans cannot. 
[end of quote]

A second source was the English philosopher John Locke, whose most influential
work was his Second Treatise on Government, published in 1690. He too argued
that man had inalienable rights, and that government existed only with the
people's permission. 

We now fast forward to the 1770's, when the Founding Fathers referred to these
principles in the Declaration of Independence and later cast them into law (just
to be sure) in the Bill of Rights. 

We seem to have a chicken-and-egg problem. Where did the people's rights come
from, if not from government? Both the Puritans and Locke said they came from
god. It's a weak argument, considering the complete lack of evidence. They
didn't come from god (nor from John Calvin); they came from John Locke and New
World Puritan leaders Francis Higginson, Samuel Skelton and others. In the case
of Americans (and citizens of other countries as well), they come from the
constitution. I've never seen a court case on free speech based on the legal
theory of 'inalienable god-given rights'. They always cite the First Amendment
as their authority, as they should in a country where church and state are
separate. 

What government can giveth, government can taketh away. There are no inalienable
rights, no matter how philosophical or official the term sounds.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 21)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-04-10T12:36:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b74a2l02t9n@enews1.newsguy.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net>`

```

"LX-i" <DanielJS@Knology.net> wrote in message
news:3E955500.7090501@Knology.net...
> Peter E.C. Dashwood wrote:
> > My defence of Free Speech is not based on the rights
guaranteed by ANY
> > political document; rather, I believe it is a fundamental
right that ALL
> > Human Beings are entitled to, simply by virtue of the fact
that, as a
> > species, we have developed communication and language
skills to a very high
> > degree (to the point where we can ponder abstract thoughts
and have this
> > conversation), and this ability has been fundamental to the
progress of
> > Mankind.
>
> Our Declaration of Independence agrees with you.  "...that
they are
> endowed by their Creator with certain inalienable rights..."
The source
> of the rights is -not- the Constitution, but the Creator.  :)
The
> Constitution (and its amendments, specifically the first 10)
just spells
> them out.

Taking the constitution as a whole, not really.

What about those "other persons?"  Perhaps it's the largest
shortfall of the document, but "We the people" did not include
slaves or any other non-citizen.  Slavery has been abolished,
but we still manage to overlook the "rights" of enemy
combatants -- even when they are U.S. citizens.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 22)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-10T18:40:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-97315A.18400710042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com>`

```
In article <b74a2l02t9n@enews1.newsguy.com>,
 "Grinder" <grinder@no.spam.maam.com> wrote:

> Taking the constitution as a whole, not really.
> 
…[4 more quoted lines elided]…
> combatants -- even when they are U.S. citizens.

Which rights are those exactly?  Our standard of living for EPWs are 
better in many cases that the standards they enjoyed as active members 
of their respective opposing forces.

Are the tortured?  Starved?  Denied medical care?  Denied religious 
services?  No, none of the above.  In fact they are treated with far 
greater respect than they treat their own captives.  They are feed very 
well, provided all possible medical care, given access to clergy, etc.

I assume you are speaking of the Taliban/Al Queda held at Gitmo.  They 
are the best treated EPWs in the history of the world, any army, any 
country, any conflict.   What exactly is your complaint?
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 23)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-11T00:46:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E960F3B.9AED9047@shaw.ca>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com>`

```


Joe Zitzelberger wrote:

> In article <b74a2l02t9n@enews1.newsguy.com>,
>  "Grinder" <grinder@no.spam.maam.com> wrote:
…[20 more quoted lines elided]…
> country, any conflict.   What exactly is your complaint?

Joe,

I hope to God you are right. If not then *we* (Westerners) are in deep
trouble. Other than the American media being lead by the nose, what
substantive proof is there that everything is honky dory ?

When does Habeus Corpus come into play ? Now ask yourself the question -
'Why are they in Guitanamo, rather than a barbed wired facility, say, in
New Mexico or even George Dubya's  Lone Star State ?'

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 24)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-11T02:33:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-D6F370.02331411042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com> <3E960F3B.9AED9047@shaw.ca>`

```
In article <3E960F3B.9AED9047@shaw.ca>,
 "James J. Gavan" <jjgavan@shaw.ca> wrote:
> 
> Joe,
…[10 more quoted lines elided]…
> 

One reason is that Gitmo has not had much of a function since the end of 
the cold war, and even less with Viequez out of service.  It had plenty 
of guards and space already.  As part of the mission of the Navy/Marines 
is to "be friendly and show the world the benefits of democracy" it just 
doesn't do to close it.  They could have gone to Guam, or Johnson Atol, 
but Cubans are especially in need of friendly examples and the marines 
needed a mission.  Coincidence?

All of the old EPW camps in the US have been torn down or used for 
something else (nearby Ft Benning's old EPW camp has been mechanized 
infantry school for the last 40-odd years).  I don't know of any old 
camps available -- I'm not sure what we did in Korea or Vietnam, but I 
don't think we brought the EPWs to the states, I could be wrong.  
Anyway, I think those camps were out of service for over 50 years, torn 
down or reused.

Since the Geneva convention will not allow the use of prisons (not that 
we have too many of those free either) you need some place secure, 
isolated and easy to keep control of.  A ship would have worked, but it 
would have been damn expensive and I think a possible violation as well, 
I'm not sure.  Somewhere in the southwest like New Mexico or perhaps 
Montana/Wyoming would have worked -- but there are no troops there, no 
infrastructure to support a post.  It isn't something that could be 
built quickly.  Or all the liberals would be complaining about the poor 
afganis having to sleep in tents (thought being completely unconcerned 
that our own troops were sleeping in the same kind of tents).

Gitmo has all that and one special advantage -- one of the 
thousand-or-so federal judges (and it only takes one) cannot command the 
release of the prisoners on the grounds of their civil rights or some 
such being violated.  (how the hell did we ever make it 225 years???)

This is important, as it is the primary complaint made by many that are 
against the "unlawful combatant" status instead of the "enemey prisoner 
of war" status.

Some background is needed here.  Many people assume that anyone captured 
in the course of a war is automatically a "prisoner of war" (hereafter 
EPW), this is quite incorrect.  There are several critera required by 
the geneva convention:

  -- they must be members of some sort of organized force (volunteer or 
paid) with a valid command structure.
  -- they must wear distinctive uniforms, it doesn't have to be fancy, 
but it must allow them to be distinguished from a civilian.
  -- they must clearly be under arms (e.g. booby traps and suicide 
bombers are verboten)
  -- their "side" must respect the laws of war


   The first, a valid command structure, may or may not apply.  Does Al 
Queda count?  Well, maybe, they can file with Geneva for non-national 
status but they have not.  Does the Taliban count?  Certainly.  Do 
troops of loosely organized local 'warlords' or extra-national 'true 
belier jihadists' count?  Maybe, but perhaps questionable.  For the sake 
of simplicity I am willing ot grant all three groups EPW status under 
this condition.

   The second, that they wear distinctive uniforms, is one where 2.5 of 
the three fail.  I know of no distinctive uniform or insignia worn by 
any of the Afganis, Al-Queda or other irregulars.  I've heard people 
question this, but it really does make a great deal of sense.  
   Put yourself in the position of having to decide to shoot someone or 
not -- Are they a civilian kid walking up to you holding out an empty 
bowl looking for food?  Or a soldier in civies walking up to you holding 
a grenade?  Choose wrong and that starving non-combatant kid will haunt 
your dreams for the rest of your life, but choose quickly because that 
tricky combatant will end your life.  It is a delima that no soldier 
should ever have to face -- and one that no honorable soldier would ever 
create.  
   If both sides follow this it saves a great many civilians who would 
otherwise have died at the hands of either side "just in case".    
Following this one is a clear win-win for all parties involved.
   Not only did they all violate the letter in all cases, but they 
violated the letter and spirit in the specific case of posing as 
civilians (or aiding and abetting the posing) to conduct combat 
operations.

   They must be clearly under arms.  No hidden grenades, no C4 around 
the waist, no passenger plane loaded with fuel.  Here Al-Queda and the 
various irregulars have failed to comply, in fact it is one of their 
favorite tactics.  And the Taliban harbored and assisted them in doing 
so.  Were an American soldier to do such a thing and survive he/she 
would face charges.

   The other side must respect the laws of war.  That means not 
intentionally targeting civilians.  Gong!  They failed here too.  This 
is a very important one.  EPWs are free to go at the end of the war, no 
reprisals.  Those who have committed or assisted in the commission of 
war crims (e.g. intentional murder of civilians) do not have to be 
released.  They can be tried and sentenced appropriately.  If this were 
not the rule the Nuremburg would never have happened -- we would have 
had to let them go at the end of hostilities.  When we finally 
disassemble all of Al-Queda do you think we should release, free and 
clear, people that planned, assisted, supported the murder of 3000+ 
civilians?
   It does say something about the American army that has honored the 
Geneva convention even when fighting apponents that did not honor it. 

   Even if the American media is being lead by the nose it really 
doesn't matter.   I don't know what their treatment is beyond what the 
media has offered.  But even 10 years out of active service I know how 
the army and marines train to handle captives -- I can say that they 
will be treated all the respect and decency they would if their status 
was EPW.  (I'm not saying it is a picnic, but those "unlawful 
combatants" have it as good or better than any EPWs in history.)

   But I have no facts, only opinion, to answer your question "what 
substantive proof is there that everything is honky dory?"

   I can offer you the opinion that we are a decent people with a much 
greater respect for our fellow man BECAUSE of our democracy and the 
belief that we are all equal.

   Don't take my word for it -- ask the citizens of Kabul who threw down 
their veils and cranked up the rock-n-roll when we liberated -- ask the 
citizens of Bagdad as they cheer our tanks and slap pictures of their 
oppressor with shoes and drag his decapitated bronze head through the 
streets -- ask the mothers who would brave oceans on a cardboard box in 
hope of freedom for a child -- or the person crawling through a snow 
covered minefield to escape east germany  -- ask any citizen of Pruage, 
Budapest or Bejing who ever faced a tank of his _own_ government -- ask 
the Vietnamese clinging to helicopter skids in the spring of 75 (not our 
finest hour), or the ones that overloaded boats by two orders of 
magnitude, in hopes of getting _anywhere_else_ -- ask the citizens of 
Kuwait, Japan, South Korea, Grenada, et al who were liberated by the 
same troops guarding the 'unlawful combatants'.

   (But if you ask France, please remember, 'that which we secure to 
easily, we esteem to lightly'.  The freedom that those soldiers have 
guarenteed for the last 60 years includes the right to be wrong, 
ungrateful, or just plain stupid.)

   I have no substansive proof of the condition of the non-EPWs.  But I 
do know that the troops guarding the 'unlawful combatants' have built up 
a great deal of honor-equity throughout the world in the last sixty or 
so years.  If they say things are "honky dory" then I will grant them 
benefit of doubt based on that.


   Whew, I've been hitting this keyboard harder than Iron Butterfly's 
drummer full of crank.  That was the second multi-page-off-topic-rant of 
the evening.

  I need another hobby...
```

###### ↳ ↳ ↳ OT: Human rights - Them or Us

_(reply depth: 25)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-11T20:03:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E97209B.C111000D@shaw.ca>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com> <3E960F3B.9AED9047@shaw.ca> <joe_zitzelberger-D6F370.02331411042003@corp.supernews.com>`

```


Joe Zitzelberger wrote:

>
> One reason is that Gitmo has not had much of a function since the end of
…[5 more quoted lines elided]…
> needed a mission.  Coincidence?

<snip>

Well reasoned rebuttal Joe. But I couldn't help but feel that Donald Rumsfeld
would have been quite happy to use your text. I didn't ask the question, "How
long are you going to keep them as prisoners ?". In his usual abrasive style
Don would probably reply, "As long as it takes....".

Having given all the 'logistical' reasons for shuffling them off to Gitmo, you
did give the one which really burns the Administration's ass :-

>Gitmo has all that and one special advantage -- one of the
>thousand-or-so federal judges (and it only takes one) cannot command the
>release of the prisoners on the grounds of their civil rights or some
>such being violated.  (how the hell did we ever make it 225 years???)


Just in case you get a mixed message - for want of a name I am a 'liberal
centrist' NOT a bleeding heart liberal. In the white heat of anger after 9/11
I would have been perfectly happy if none of the Taliban/El Qaeda  had made it
to Gitmo. But ignoring the 'niceties' of the Geneva Convention and what it
allows you to do/not do - those prisoners represent a potential human time
bomb. Are you going to keep them imprisoned forever - OR - when released, THEN
what will they do ?

USA touts itself as the greatest democracy - so it has to follow through. What
is the human impact. You may be familiar with former Viet Nam US POWs, but
some 'snapshots' from my own experience. No, I was never a combatant - that's
not a role you play as a desk-jockey <G>. I'll hide their identities by just
using first names. Ironically, though both are from 'different sides of the
trench' their reactions are dramatically similar.

Wing Commander Harry B.... was commissioned as a flyer prior to W.W.II.
Although not a product of  either Eton or Harrow, it's a fair bet he went to a
fee paying 'private' school. As a squadron leader he led a bomber squadron. I
met up with him in Egypt in 1952. He didn't talk too much about his war
experiences, but I recall vividly him expressing his reluctance to attack a
civilian passenger train.  He did, and with a sigh of relief, discovered it
was a disguised ammunition train. Anyway he was shot down probably in
1941/1942, and was awarded both the DSO and DFC in his short wartime career
and spent the remainder of the war as a POW. They weren't mistreated, but nor
were they staying at the Hotel Hilton. The really important thing that came
across about his psyche was the prevailing mood of having been 'caged' for
some 3 to 4 years.

Then we reach the point where he was stationed in Egypt as a staff officer.
About 45, married but childless, he looked on this young 20/21 year old kid as
the son he would never have. My working days would start with 'Corporal !", in
his plum voice - which was the signal to get him his glass of water so that he
could plonk hs Alka Seltzer into the glass and sit mesmerized as it fizzled
and dissolved. This was his regular 'breakfast' after a night on the booze.

Naturally, while he was in the 'tank' his subordinates were still fighting and
getting promoted, some beyond him. Came the peace and the RAF had a lot of
surplus flyers. The Air Force List shows officers by Branch (trade) and their
seniority by rank. The book had pages and pages, and pages..... of flyers with
the rank of wing commander all having the same seniority date of October 1946.
One of the sideline jobs we had was to scour the half annual signals that came
from the Air Ministry, New Years Honours List and King's/Queen's Birthdays
Honours List, noting those who had been given medal awards or promotions. Wg.
Cdr. Harry could see fellow officers begin promoted to Grp. Captain
(Brigadier), and sweated he might get lucky. He never did. With a photographic
memory I could pick out the names of all seniors serving in the MEAF - he
looked to me for reassurance and was saddened when my eyes indicated a
negative.

Not only was this man scarred by internment, but an accident of fate, his
pre-war dreams of career were also shattered.  We lost touch when I returned
to UK. My best guess is he was 'bowler hatted' with the rank of wing commander
when there was a shake-up in 1955.

Entirely different character - John I.... About 18/20 when W.W.II broke out.
Definitely a 'lefty' and a sincere conscientious objector. 'No can do", said
the government and shipped these malcontents across to the Channel Islands,
(just off the French coast), where along with others he was employed as a farm
labourer. That was OK until the fall of France in 1940. German aircraft flew
over the Channel Islands, dropping leaflets, "Hang white sheets etc. from your
windows, signifying surrender.... or ELSE....".  (There were no military in
the CIs - there was nothing of significance to defend).

Well, the Germans weren't going to leave able bodied young men in the CIs - so
John was shipped off to a POW camp in Austria for civilians of all
nationalities, Poles, Czechs, Brits, Slavs etc. Again not mistreated, but
conditions appear to have been pretty grim.  His 'vacation' period would have
been from June 1940 until V-E Day 1945.

Again that same horrific reaction to being caged. He returned unrepentant,
still a socialist, but definitely had a phobia - CLEANLINESS. Always
impeccably dressed he was constantly washing himself - reflecting back on the
awful conditions in the POW camp. Twice married, and with his second and
Chilean wife, spent time in Chile, but left that country when the CIA did a
number on the Chilean regime.

Sadly two VERY REAL human lives encapsulated into a couple of brief paragraphs
- but both suffering the dreadful 'hurt' of having been caged.

Now back to Gitmo - what do you think will happen if these people are ever
released. By all means provide them with decent ethnic food, prayer mats and a
copy of the Q'uran  - we, (rather you), are still creating scarred human time
bombs..

Just let's hope the US can be a little more enlightened in Iraq - although
with what appears to be a lack of planning to handle administration, policing,
looting, (common to every war), it doesn't look too rosy..

Jimmy, Calgary AB

>
```

###### ↳ ↳ ↳ Re: OT: Human rights - Them or Us

_(reply depth: 26)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-12T23:06:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-CA95E9.23060312042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com> <3E960F3B.9AED9047@shaw.ca> <joe_zitzelberger-D6F370.02331411042003@corp.supernews.com> <3E97209B.C111000D@shaw.ca>`

```
In article <3E97209B.C111000D@shaw.ca>,  "James J. Gavan" 
<jjgavan@shaw.ca> wrote:

> Well reasoned rebuttal Joe. But I couldn't help but feel that Donald Rumsfeld
> would have been quite happy to use your text. I didn't ask the question, "How
> long are you going to keep them as prisoners ?". In his usual abrasive style
> Don would probably reply, "As long as it takes....".

I would be honored if he wanted to use my text...


> Just in case you get a mixed message - for want of a name I am a 'liberal
> centrist' NOT a bleeding heart liberal. In the white heat of anger after 9/11
…[4 more quoted lines elided]…
> what will they do ?

I was not directing that 'bleeding heart' crack at you.  Just at some in 
general that turn to our courts for the most extreem things that would 
never get past a representive body.

I know captivity is not nice, but neither is it terrible in all cases.  
After the Korean war the US had +70k CCF troops that requested NOT to be 
repatriated.  We must have treated them decently enough. 

For some, I hope they are imprisoned forever, esp. all the Al-Queda, for 
others...I really don't know.


> Wing Commander Harry B.... AND John I.... 
:
> Sadly two VERY REAL human lives encapsulated into a couple of brief paragraphs
> - but both suffering the dreadful 'hurt' of having been caged.

This is indeed a very tragic cost of war.  But what else could they have 
done?  You certainly cannot release them to continue fighting, entire 
wars have turned on things like this (Stalingrad and the 6th Army comes 
to mind).

I have usually seen people turn the Harry B's method of coping with war, 
et al.  Alcohol seems to some to be a universal cure-all.  I wonder how 
that will shake out for devout islamic ex-EPWs.

In this specific case, that of extra-national terrorists bent on 
destruction of america/isreal/the-great-satan/infidels-in-general should 
we just tag them and release them to wreck more havok?  (Marlin Perkins 
does the Mideast...hmmmm)

There needs to be some guarentee that the release troops will not 
continue to behave in murderous fashion.  I'm just not sure how that can 
be arrived at without them showing great cooperation or great remorse.

For what it is worth, I checked the DoD website.  Taliban regulars were 
granted EPW status and some have now been released.  Total captivity not 
greater than a year.


> Now back to Gitmo - what do you think will happen if these people are ever
> released. By all means provide them with decent ethnic food, prayer mats and a
> copy of the Q'uran  - we, (rather you), are still creating scarred human time
> bombs..

Some should never be released.  If they had sailed up the East River, 
warned the civillian occupents of the towers to get out, and then 
proceeded to bring them down by whatever means, then I could see 
releasing them 'without reprisals'.  It would have been valid -- though 
extrodinarily stupid and useless -- conduct of war.

As it is, many of them deserve trials for war crimes, and subsequent 
imprisonment if convicted.  I'm not especially concerned with the state 
of mind of the members of Al-Queda and related organizations.  Just as I 
am equally unconcerned with the feelings of, for example, the Manson 
family, now locked up over thirty years.


> Just let's hope the US can be a little more enlightened in Iraq - although
> with what appears to be a lack of planning to handle administration, policing,
> looting, (common to every war), it doesn't look too rosy..


In the First Oil War*** we were quite kind to our prisoners.  Most were 
held for a few short months and release, having received much better 
treatment from us than they did from their own army.  They really had a 
poor choice -- be shot by your army for trying to surrender in the face 
of futility, or face an unbeatable force.  In many cases, specifically 
food, tobacco and medical care, they were much better of with us.  True, 
they had to be hooded and zip-cuffed occasionally, but mostly they had 
nice pavillions and tents and just too much time on thier hands.  In the 
interveining 12 years I've not heard tail of any of them that were 
scared by us.

(***I coined it thus back when everyone was trying to decide on a better 
name for Desert Storm.  They all settled on "Gulf War", well, that is 
now dated and will require massive revisions.  My choice of names was 
designed with expansion in mind...)

But the current one is amazing -- 21 days in and everyone wants a nice 
civil authority in place taking care of everything or else it is a 
quagmire.  To put that in context, 21 days in France 1944 left the 
allies still in the hedgerows.  (we won't mention what 21 days got in 
1940, as that might hurt my case)  Give them a few weeks to get things 
organized.  The are already feeding the civilians, electric will be 
restored soon, and they will get to go about life with free from fear.  
Soon enough a civil authority will present itself, but the war is quite 
young.

Those EPWs we are holding now will likely be released in a few months -- 
my guess is sometime in June.
```

###### ↳ ↳ ↳ Re: OT: Human rights - Them or Us

_(reply depth: 27)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-13T12:55:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L6dma.133$%13.100460@newssrv26.news.prodigy.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com> <3E960F3B.9AED9047@shaw.ca> <joe_zitzelberger-D6F370.02331411042003@corp.supernews.com> <3E97209B.C111000D@shaw.ca> <joe_zitzelberger-CA95E9.23060312042003@corp.supernews.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message
news:joe_zitzelberger-CA95E9.23060312042003@corp.supernews.com...
> In article <3E97209B.C111000D@shaw.ca>,  "James J. Gavan"
> <jjgavan@shaw.ca> wrote:
>
> After the Korean war the US had +70k CCF troops that requested NOT to be
> repatriated.  We must have treated them decently enough.

Along the same lines I read something in the Milwaukee Journal Sentinel
maybe six, eight weeks ago...

A couple of years ago a North Korean emigrated (escaped?) to South Korea.
Naturally, he was interviewed by officials of the ROK. The interviewers came
away from the experience somewhat amazed : they determined when the
individual arrived he truly believed:
- The standard of living in the DPRK (North) was better than in the ROK
(South)
- All the humanitarian food assistance given the DPRK by the US, each bag
marked as all food aid is marked, "a gift from the people of the United
States of America," had been supplied as a tribute to Kim Jong Il.

Amazing thing is in spite of these beliefs, the guy STILL LEFT!

(Maybe Kim needs to enhance his English-language skills. I suggest he start
with two words: "regime" and "change.")

MCM
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 25)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98353b.111019087@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com> <3E960F3B.9AED9047@shaw.ca> <joe_zitzelberger-D6F370.02331411042003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>Since the Geneva convention will not allow the use of prisons (not that 
>we have too many of those free either) you need some place secure, 
…[7 more quoted lines elided]…
>that our own troops were sleeping in the same kind of tents).

There are recently abandoned bases all over the country, with perfectly good
housing units, fences around them, guard posts, etc. The one I'm familiar with
is (former) Reese Air Force Base near Lubbock, Tx. It would be perfect.

>Gitmo has all that and one special advantage -- one of the 
>thousand-or-so federal judges (and it only takes one) cannot command the 
>release of the prisoners on the grounds of their civil rights or some 
>such being violated.  (how the hell did we ever make it 225 years???)

In Texas?? Where they say, 'get a rope'. <g>

>   Even if the American media is being lead by the nose it really 
>doesn't matter.   I don't know what their treatment is beyond what the 
…[3 more quoted lines elided]…
>was EPW.  

You wouldn't say that if you'd seen POW camps _we_ ran in the Marine Corps. The
guy in charge had been defrocked as a drill instructor because he was 'too
sadistic.' Right, that's like an accountant criticised for being too
detail-oriented, or a lawyer for being too verbose. 

But then, we didn't expect to keep them longer than a few days. We just wanted
to get information out of them. When people are fearful enough, they'll tell you
anything you want to know.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 23)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-04-10T20:03:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7549c0omn@enews1.newsguy.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com>`

```
> What exactly is your complaint?

I wasn't complaining, just reacting to the supposition (formed
by Peter and LX-i's comments) that the US identifies
fundamental human rights.  The Constitution does have verbiage
to that point, but it carefully distinguishes between _the_
people and "other persons," who aren't recognized as having
those rights.

This is presumptive comment though, as LX-i's quote is from the
Declaration of Independence.  The logical jump that I perhaps
should not have made, is that the Bill of Rights is a practical
implementation of the "unalienable Rights" referred to by
Jefferson.  If you accept this, however, it presents a schizm
in political theory of the Constitution.

> Which rights are those exactly?  Our standard of living for
EPWs are
> better in many cases that the standards they enjoyed as
active members
> of their respective opposing forces.
>
> Are the tortured?  Starved?  Denied medical care?  Denied
religious
> services?  No, none of the above.  In fact they are treated
with far
> greater respect than they treat their own captives.  They are
feed very
> well, provided all possible medical care, given access to
clergy, etc.
>
> I assume you are speaking of the Taliban/Al Queda held at
Gitmo.  They
> are the best treated EPWs in the history of the world, any
army, any
> country, any conflict.

I'm not disputing this -- though I doubt any detainee is
"enjoying" their stay.

______

I will go so far as to say, though, that I think Joseph Padilla
should be afforded his rights as a US citizen.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-11T14:55:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76l1u$of2$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com>`

```

On 10-Apr-2003, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> Which rights are those exactly?  Our standard of living for EPWs are
> better in many cases that the standards they enjoyed as active members
> of their respective opposing forces.

The right to a trial.   Those that are found guilty should be punished.  Those
that are found innocent should be let go.

We don't want to let any go, so we don't try them.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 24)_

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-04-11T13:11:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0304111211.25ce5d67@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <joe_zitzelberger-97315A.18400710042003@corp.supernews.com> <b76l1u$of2$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<b76l1u$of2$1@peabody.colorado.edu>...
> On 10-Apr-2003, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:
> 
…[7 more quoted lines elided]…
> We don't want to let any go, so we don't try them.

But we have released some of the unlawful combatants.  Just a few
weeks ago NPR (of all people) had a newsbyte about a few that were
released talking about the good medical care they received from the
navy.

Still, lawful or unlawful combatant, they do not deserve either trial
or release until the end of the conflict.
```

###### ↳ ↳ ↳ OT: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 22)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-10T18:01:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E95F7E0.4000809@Knology.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com>`

```
Grinder wrote:
>>Our Declaration of Independence agrees with you.  "...that
> 
…[23 more quoted lines elided]…
> combatants -- even when they are U.S. citizens.

"We the people" -did- include all people - that's a common misconception
about our founding documents.  True, there were census provisions that
counted slaves and other non-citizens were only counted 1/3 toward each 
state's population, but this made them no less a person, and no less 
endowed with the basic rights.  I think the civil rights movement made 
great strides towards ensuring that this was enforced.  Of course, they 
missed the point when the movement lost Dr. MLK, and started trying to 
make the American taxpayer "pay them back" for wrongs done to their 
ancestors.

And, as far as enemy combatants, they are not under the US Constitution 
- they are covered under the Geneva Conventions and military law.  Can't 
mix apples with oranges - all part of "providing for the common defence".


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: The US Constitution (was: RW's insults (was: Beginner's Question))

_(reply depth: 23)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-04-10T20:15:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7550d0spi@enews1.newsguy.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3E94E28C.9010405@ix.netcom.com> <3e955227_2@127.0.0.1> <3E955500.7090501@Knology.net> <b74a2l02t9n@enews1.newsguy.com> <3E95F7E0.4000809@Knology.net>`

```
> "We the people" -did- include all people - that's a common
misconception
> about our founding documents.  True, there were census
provisions that
> counted slaves and other non-citizens were only counted 1/3
toward each
> state's population, but this made them no less a person, and
no less
> endowed with the basic rights.

Slaves weren't citizens were they?
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 18)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e960425.353924148@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>Across the centuries of recorded Human History people have died for the
>right to a voice.

An interesting fact: of all the people born since the beginning of historical
time (roughly 4,000 BC), 90% are living today. In other words, only 10% of
humans have died.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 19)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-11T21:02:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b760cf$f4b$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net>`

```
Robert Wagner wrote:

> An interesting fact: of all the people born since the beginning of
> historical time (roughly 4,000 BC), 90% are living today. In other words,
> only 10% of humans have died.

That is simply not true.  

In 1900 there was 1.6 billion world population population.  Those people 
are all dead now (or so nearly all it doesn't matter - except to them).

Today there are 6 billion.

So if those two groups were the only people ever then 21% of the 7.6 
billion total have died.

However, obviously they were not the only people.  Billions were born and 
died wholely within the C20th (and thus are not part of the 1.6 or the 6 
billion).
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 20)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T13:35:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9814c8.102710818@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[9 more quoted lines elided]…
>Today there are 6 billion.

Whoops. I got it backwards. Make that 10% are living today. 

Cumulative births are estimated by some, such as John Leslie, to be 60 billion.
Others, notably Nathan Keyfitz, estimate 110 billion.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 21)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-12T15:25:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9821e9_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net>`

```
So is it 10% living or 90% or some other percent or none of the above?

This is an interesting idea. I really want to know.

Pete.

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e9814c8.102710818@news.optonline.net...
> Richard Plinston <riplin@Azonic.co.nz> wrote:
>
…[3 more quoted lines elided]…
> >> historical time (roughly 4,000 BC), 90% are living today. In other
words,
> >> only 10% of humans have died.
> >
…[9 more quoted lines elided]…
> Cumulative births are estimated by some, such as John Leslie, to be 60
billion.
> Others, notably Nathan Keyfitz, estimate 110 billion.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 22)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:24:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e984ab5.116518084@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>So is it 10% living or 90% or some other percent or none of the above?
>
>This is an interesting idea. I really want to know.

It is between 6 and 10 percent living today, and going up. Prophets of doom say
the system will fail when the percent hits some limit (pick a number, any
number). 


>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e9814c8.102710818@news.optonline.net...
…[26 more quoted lines elided]…
>http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000
Newsgroups
>---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 23)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-12T14:30:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304121330.11e3a59e@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> It is between 6 and 10 percent living today, and going up. Prophets of doom say
> the system will fail when the percent hits some limit (pick a number, any
> number). 

> >> >> An interesting fact: of all the people born since the beginning of
> >> >> historical time (roughly 4,000 BC), 90% are living today. In other
>  words,
> >> >> only 10% of humans have died.

This factoid looks like it came from some door-knocker.  Working from
a basis that there were 2 people 7644 years ago (or whatever), and
taking a linear expansion to 6 billion (and thus totally ignoring all
facts and censuses), the door-knocker would probably work it out to
this.

Millions of Prophets of Doom have been wrong for several millenia, but
then it only takes _one_ of them to be right    ;-)

Never mind, Bush will do his best to solve the problem.    ;-)  ;-)
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T01:29:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e98a377.15036845@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <217e491a.0304121330.11e3a59e@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
>> It is between 6 and 10 percent living today, and going up. Prophets of doom
say
>> the system will fail when the percent hits some limit (pick a number, any
>> number). 
…[7 more quoted lines elided]…
>a basis that there were 2 people 7644 years ago (or whatever),

The first humans were born between 100K and 2M years ago, depending on which
anthropologist is correct. When you say 7644 (presumably the date of Adam &
Eve), it makes you sound like a door-knocker. 

FWIW, when the first two humans were born, they comprised 100% of the cumulative
population. 

> and taking a linear expansion to 6 billion (and thus totally ignoring all
>facts and censuses),

It's not linear, it's exponential.

But given the declining birth rate, experts think the percentage will level out
at 6% and stay there. 

Unless terrorists unleash something like Black Plague.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 25)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-12T22:58:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304122158.3915e182@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <217e491a.0304121330.11e3a59e@posting.google.com> <3e98a377.15036845@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >This factoid looks like it came from some door-knocker.  Working from
> >a basis that there were 2 people 7644 years ago (or whatever),

> When you say 7644 (presumably the date of Adam &
> Eve), it makes you sound like a door-knocker. 

It shouldn't have, I was talking in the third person. perhaps you
missed that little subtlety.

> > and taking a linear expansion to 6 billion (and thus totally ignoring all
> >facts and censuses),
> 
> It's not linear, it's exponential.

That is why I had added "and thus totally ignoring ..", did you you
ignore that bit ?
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 26)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T06:34:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e99005f.38824243@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <217e491a.0304121330.11e3a59e@posting.google.com> <3e98a377.15036845@news.optonline.net> <217e491a.0304122158.3915e182@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
…[7 more quoted lines elided]…
>missed that little subtlety.

The evidence shows I'm no good at subtlety. Sorry. Please just say what you
mean.

>> > and taking a linear expansion to 6 billion (and thus totally ignoring all
>> >facts and censuses),
…[4 more quoted lines elided]…
>ignore that bit ?

Prophets of doom make a big deal over exponential growth. They think it explains
why we're doomed. 

Actually, using current fecundity rates, population isn't increasing as
exponentially as previously thought. The 'replacement rate' in Germany is
negative and in the rest of Europe about even. It is stable even in China.
```

###### ↳ ↳ ↳ OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 23)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-13T11:40:04+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e993e8f_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e984ab5.116518084@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[4 more quoted lines elided]…
> It is between 6 and 10 percent living today, and going up. Prophets of
doom say
> the system will fail when the percent hits some limit (pick a number, any
> number).

Hmmm...  I got to thinking about this.

So this means that something less than 10% of all the people who have ever
lived are alive today.

This is the only proportion of Humanity who will have been exposed to the
Technology we currently "enjoy", who will have access to the thoughts of all
the Great Thinkers who have gone before, who will have a chance at
education, the arts, sports, decent food and drink, advanced medicine, and
enough leisure to consider it.

It is tempting to think that we should expect something earth shattering
from such a priveleged group <G>.

But then we see that of this "something less than 10%", it is only a small
proportion who have access to the above facilities.

I wonder how many potentially brilliant minds are starving to death or being
killed in wars and civil unrest around the World?

We are so bright, but we never seem to learn...

No wonder we haven't solved Star Travel yet <G>.

I guess you could invert this idea and say it is a miracle that such a tiny
percentage have managed to get us where we are.

And, it is fair to say, that while life in the 21st century for most of the
inhabitants of Sol 3 is not perfect, it is far better than it was in
preceding centuries.

Guess I'll continue for bit, just to see what the Hell is going to happen
next...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 24)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-13T16:55:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e998d79.74951713@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[21 more quoted lines elided]…
>enough leisure to consider it.

I disagree about food. Its quality keeps going down due to mass production
techniques -- both at home and fast food.

>It is tempting to think that we should expect something earth shattering
>from such a privileged group <G>.
>We are so bright, but we never seem to learn...

Human nature doesn't change. We're running on firmware (instincts) which evolved
during the first 98% of human existance ... before there were books, education,
medicine and shopping malls. Most human behavior becomes understandable when
cast into the hunter-gatherer environment. 

>I wonder how many potentially brilliant minds are starving to death or being
>killed in wars and civil unrest around the World?

I too think about that, frequently. 

>And, it is fair to say, that while life in the 21st century for most of the
>inhabitants of Sol 3 is not perfect, it is far better than it was in
>preceding centuries.

We've replaced one challenge -- starvation -- with a host of others that we're
less equipped to handle. Your sanguinity seems overly subjective.
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 25)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-13T19:12:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e99a8b0_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e998d79.74951713@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[11 more quoted lines elided]…
> >> the system will fail when the percent hits some limit (pick a number,
any
> >> number).
> >
> >Hmmm...  I got to thinking about this.
> >
> >So this means that something less than 10% of all the people who have
ever
> >lived are alive today.
> >
> >This is the only proportion of Humanity who will have been exposed to the
> >Technology we currently "enjoy", who will have access to the thoughts of
all
> >the Great Thinkers who have gone before, who will have a chance at
> >education, the arts, sports, decent food and drink, advanced medicine,
and
> >enough leisure to consider it.
>
> I disagree about food. Its quality keeps going down due to mass production
> techniques -- both at home and fast food.
>

Depends where you live and what you can afford to buy. (As it is something
very dear to my heart - I enjoy both cooking and eating - I try most local
food in most localities. In New Zealand, because it is an Agricultural
nation, with very little industrial pollution or intensive farming, the
general standard of produce is better than many other places. You don't HAVE
to eat mass produced food...If it bothers you, buy organic or grow it
yourself...)

Having said that, the quality of food today in general, is MUCH better than
it was 900 years ago when rotting meat was disguised with spices, (when you
could get meat...the general population ate what they killed and they
weren't supposed to kill meat as it was left to the Lords...)  and wine was
safer to drink than water... Even up to 150 years ago the general quality
and availability of food was nowhere near as good as it is now.

> >It is tempting to think that we should expect something earth shattering
> >from such a privileged group <G>.
> >We are so bright, but we never seem to learn...
>
> Human nature doesn't change.

I believe that one is arguable. I know it is a platitude that "everybody
knows" but it doesn't stand up to inspection... I have seen people change,
and I have seen it in myself.  Certainly, "21st century Man" is a LOT
different in his attitudes and ideas than his antecedents of, say, 100,000
years ago, so it is important that some kind of timeframe is specified if
you intend to argue this one...

It could be argued that we are still evolving. The process is slower than I
(for one) would like, and that's what I mean when I say we never seem to
learn. (The fact is we DO learn, but it takes an awful long time...<G>)

>We're running on firmware (instincts) which evolved
> during the first 98% of human existance ... before there were books,
education,
> medicine and shopping malls. Most human behavior becomes understandable
when
> cast into the hunter-gatherer environment.
>

I agree that there are definite traces in modern behaviour of our primitive
past. I'm not sure about the instincts...probably true, but how does an
"instinct" evolve? It gets into the DNA somehow and for some  good "survival
related" reason...


> >I wonder how many potentially brilliant minds are starving to death or
being
> >killed in wars and civil unrest around the World?
>
> I too think about that, frequently.
>
> >And, it is fair to say, that while life in the 21st century for most of
the
> >inhabitants of Sol 3 is not perfect, it is far better than it was in
> >preceding centuries.
>
> We've replaced one challenge -- starvation -- with a host of others that
we're
> less equipped to handle. Your sanguinity seems overly subjective.

My sanguinity is a product of my heredity and environment (just like most of
my other behaviours...<G>). It is just as easy to  be optimistic as it is to
be depressed; and, as I have to endure my own company for a lifetime, I'd
rather have a cheerful companion than a sour one...<G>.

I'd rather be alive today that at any time in the past. We've all played the
game of "Wish I'd been born in the x century..." but we expect to live THEN
with the knowledge and personality we have NOW. It wouldn't work like
that...

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 26)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T15:48:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b813rh$23f$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1>`

```

On 13-Apr-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> > I disagree about food. Its quality keeps going down due to mass production
> > techniques -- both at home and fast food.
…[8 more quoted lines elided]…
> yourself...)


Assuming we are not talking starvation (which occurred in the past too)...
And while our winter tomatoes aren't wonderful, we at least have tomatoes in
winter.   And we have a big variety of foods we can grow.  We have a wide
variety of foods we can import.   If we have a choice to eat crap for
convenience or money - we can still choose to eat better for less than our
ancestors did.
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 27)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-21T18:02:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA4339A.78B67542@shaw.ca>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> Assuming we are not talking starvation (which occurred in the past too)...
> And while our winter tomatoes aren't wonderful, we at least have tomatoes in
…[3 more quoted lines elided]…
> ancestors did.

I'm glad it was an American who wrote, "And while our winter tomatoes aren't
wonderful, we at least have tomatoes in winter.".

With a climate which gives us only about three frost free months, (in Alberta),
elevation and closeness to the mountains - you'll appreciate growing veggies can
be a challenge. Consequently 'most' are imported from the States, primarily from
California; but I noticed the other day we had some strawberries from Texas. From
memory, I think it takes about 36 hours continuous trucking to get refrigerated
vans from California to Calgary.

Much of the time tomatoes come GREEN partially ripening, (well at least turning
red) en route. Big, plump and tasteless. The latest gimmick of course being
'tomatoes from the vine' or 'sun dried tomatoes'. Seeing as you admit to being a
grandfather, like me you must recall home grown/greenhouse tomatoes, where merely
touching the leaves of the plant and smelling your fingers, gave you that
distinctive tomato smell - also passed on to the fruit itself.

Same goes for strawberries - BIG, (really BIG, double or triple the size of those
grown in a garden bed) - but absolutely  TASTELESS  Even sliced and sugared they
are nothing like the small real McCoys. So much for mass food production.

Like you I can get all the exotic foods from south of the Texas border - but be
damned can I get gooseberries or a traditional English type 'cooking apple'.
Discount Granny Smiths - I'm talking the humungous apples that grow easily in UK
- even when you slaver them in sugar and take a bite, your face squirls up - just
like you see those rubber faced comedians without apparently any teeth <G>. No,
even the apple province, (B.C) doesn't produce true cooking apples. The other
irony is I can go to the river banks here or up in the mountains and see wild
gooseberries growing - but minuscule and you would spend a day picking from
umpteen bushes to fill one pie.

There's a local pie shop close to me (fruit pies mainly). We go there to buy
blackberries in bulk. (It's one of our family traditions to have a blackberry and
apple pie on Boxing Day) - again these grow in BC but not here in Alberta. This
retailer's source for fruits - blackberries from China and rhubarb from Poland.
(The latter grows very easily here). Go figure......

I envy Pete and Richard their NZ lamb - which was always a staple in the UK prior
to the Common Market. It is  atrociously priced in Alberta and that doesn't make
sense. We have sheep farming in southern Alberta, and as I once wrote to Pete, we
have bumper stickers which read, "Eat Alberta lamb. 30,000 coyotes can't be wrong"
<G>

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 28)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T18:27:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b81d71$65b$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu> <3EA4339A.78B67542@shaw.ca>`

```

On 21-Apr-2003, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> Much of the time tomatoes come GREEN partially ripening, (well at least
> turning
…[6 more quoted lines elided]…
> distinctive tomato smell - also passed on to the fruit itself.

Don't have to have that long of a memory.  I just need to remember when they
were growing in gardens, and when they were for sale in farmers' markets.


> There's a local pie shop close to me (fruit pies mainly). We go there to buy
> blackberries in bulk. (It's one of our family traditions to have a blackberry
…[5 more quoted lines elided]…
> (The latter grows very easily here). Go figure......

What I always look for is my wife's favorite - black raspberries.

> I envy Pete and Richard their NZ lamb - which was always a staple in the UK
> prior
…[5 more quoted lines elided]…
> wrong"

Lamb is very variable.  If you find a supplier you trust, pay the extra money
and make sure the butcher knows you.
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 29)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-22T11:15:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea47b7e_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu> <3EA4339A.78B67542@shaw.ca> <b81d71$65b$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b81d71$65b$1@peabody.colorado.edu...
>
> On 21-Apr-2003, "James J. Gavan" <jjgavan@shaw.ca> wrote:
<snipped interesting (and nostalgic) stuff on fruit and tomatoes - "black
raspberries"?>

> Lamb is very variable.  If you find a supplier you trust, pay the extra
money
> and make sure the butcher knows you.

Not if it is New Zealand lamb it isn't. All export lamb is approved to a
standard and stamped accordingly. You can be assured if you buy it, it will
be excellent.

When I was a student I worked in one of the South Auckland Freezing Works. I
was amazed at the high standards of hygiene and inspection, all designed to
ensure a consistent export quality.

NZ lamb is frozen within 2 hours of being killed, and if you let it defrost
naturally overnight and cook it the next day, it is indistinguishable from
fresh lamb.

As I write this I am roasting pork (the smell is driving me nuts...<G>) but
now I wish it was lamb... (Thanks, Howard...<G>)

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 28)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-21T21:22:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-A0D217.21221021042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu> <3EA4339A.78B67542@shaw.ca>`

```
In article <3EA4339A.78B67542@shaw.ca>,
 "James J. Gavan" <jjgavan@shaw.ca> wrote:

> I'm glad it was an American who wrote, "And while our winter tomatoes aren't
> wonderful, we at least have tomatoes in winter.".
…[7 more quoted lines elided]…
> to get refrigerated vans from California to Calgary.

But you get two great benefits in exchange for living with those three 
frost free months -- you don't have to put up with California AND you 
get Lake Louise close by.
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 29)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-22T22:06:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA5B8E9.A66E99BD@shaw.ca>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu> <3EA4339A.78B67542@shaw.ca> <joe_zitzelberger-A0D217.21221021042003@corp.supernews.com>`

```


Joe Zitzelberger wrote:

>
> But you get two great benefits in exchange for living with those three
> frost free months -- you don't have to put up with California AND you
> get Lake Louise close by.

True, true, true <G> Only go about once a year but love to gaze at the glacier
backdrop from the Hotel frontage just when the poppies are out in late summer.

If you come up again and have previously missed it - Kananaskiss  our local
provincial jewel. Still take the Banff highway west from Calgary but turn off
south about an hour and thirty minutes from Calgary.

Time and again I keep saying to myself, 'Why not live somewhere else ?'. You've
supplied the answer, plus confirmed by a doctor from Somerset, Kentucky and an
annual visitor from Colorado - "Your mountains are awesome".

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 30)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-22T22:52:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-A678CB.22524722042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu> <3EA4339A.78B67542@shaw.ca> <joe_zitzelberger-A0D217.21221021042003@corp.supernews.com> <3EA5B8E9.A66E99BD@shaw.ca>`

```
In article <3EA5B8E9.A66E99BD@shaw.ca>, "James J. Gavan" 
<jjgavan@shaw.ca> wrote:

> annual visitor from Colorado - "Your mountains are awesome".
> 

They are indeed.  I took my wife up there last March for her first 
visit.  She is now looking at immagration requirements for Alberta.
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 31)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2003-04-23T04:29:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0304230329.46e30dcf@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu> <3EA4339A.78B67542@shaw.ca> <joe_zitzelberger-A0D217.21221021042003@corp.supernews.com> <3EA5B8E9.A66E99BD@shaw.ca> <joe_zitzelberger-A678CB.22524722042003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message news:<joe_zitzelberger-A678CB.22524722042003@corp.supernews.com>...
> In article <3EA5B8E9.A66E99BD@shaw.ca>, "James J. Gavan" 
> <jjgavan@shaw.ca> wrote:
…[5 more quoted lines elided]…
> visit.  She is now looking at immagration requirements for Alberta.

Just for herself...<G>?

Pete.
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 32)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-23T08:28:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-0DD8AB.08282123042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu> <3EA4339A.78B67542@shaw.ca> <joe_zitzelberger-A0D217.21221021042003@corp.supernews.com> <3EA5B8E9.A66E99BD@shaw.ca> <joe_zitzelberger-A678CB.22524722042003@corp.supernews.com> <b3638c46.0304230329.46e30dcf@posting.google.com>`

```
In article <b3638c46.0304230329.46e30dcf@posting.google.com>,
 dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:

> Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message 
> news:<joe_zitzelberger-A678CB.22524722042003@corp.supernews.com>...
…[11 more quoted lines elided]…
> Pete.

See said I could visit in ski season if I kept the hotel bills paid the 
rest of the year...
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 32)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-23T19:18:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA6E330.837BC150@shaw.ca>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu> <3EA4339A.78B67542@shaw.ca> <joe_zitzelberger-A0D217.21221021042003@corp.supernews.com> <3EA5B8E9.A66E99BD@shaw.ca> <joe_zitzelberger-A678CB.22524722042003@corp.supernews.com> <b3638c46.0304230329.46e30dcf@posting.google.com>`

```


"Peter E. C. Dashwood" wrote:

> Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote in message news:<joe_zitzelberger-A678CB.22524722042003@corp.supernews.com>...
> > In article <3EA5B8E9.A66E99BD@shaw.ca>, "James J. Gavan"
…[9 more quoted lines elided]…
>

You are a bad bugger <G>. That's exactly what I thought when I read his message.
She's gonna leave him down their earning the bread, with the assumption he will continue to support her,  and take advantage of the
dollar exchange rate living in Alberta <G>

Jimmy
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 28)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-04-22T01:24:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030421212458.19022.00000265@mb-m16.aol.com>`
- **References:** `<3EA4339A.78B67542@shaw.ca>`

```
>From: "James J. Gavan" jjgavan@shaw.ca 
>Date: 4/21/03 2:02 PM Eastern Daylight Time

> like me you must recall home grown/greenhouse tomatoes, where merely
>touching the leaves of the plant and smelling your fingers, gave you that
>distinctive tomato smell - also passed on to the fruit itself.

As a girl my father had a small garden plot in the back yard where he grew
tomatoes, corn, peas, carrots etc etc.  My brother and I were charged with
watering the plot with emphasis on the tomatoes.  He would buy several
different varieties and some years hand pollenate some of the plant cross the
varieties and plantint the seeds the following years just to see what he would
get.  I remember the taste and smell of those tomatoes and try to think of it
as I eat what passes for tomatoes today. It is amazing though that today those
that do grow their own can't seem to give them away!  People at work will
sometimes bring in a bag or two of tomatoes and leave them in the common area
for anyone to take and there they sit at the end of the day (I personally take
some and thank the person who brought them in - definately better than store
bought).

There are several berry farms in the area that have pick your own and once a
summer we go out and pick red raspberries.  They don't have pick your own black
raspberries but I'm notified when they are ready to be picked up.  They can be
in my kitchen within hours of being picked. There used to be pick your own
strawberries too where as a girl we'd go out and pick several quarts (and my
brother and I probably ate a quart apiece in the process :D ).  

I have no idea where the lamb in the area is raised.  There are two grocery
stores that sell lamb at what I think a reasonable price and one where it is
double the other two. Loin chops are outrageously priced (imho) but I prefer
shoulder chops or a roast.  Leg of lamb also seems to be quite the rage lately
as well.  On the leg packages the words 'free range' are promenent (free range
also seems to be quite the rage as well not only in lamb but chickens and beef
too).
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 29)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-22T22:53:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA5C41C.EA77C3FF@shaw.ca>`
- **References:** `<3EA4339A.78B67542@shaw.ca> <20030421212458.19022.00000265@mb-m16.aol.com>`

```


YukonMama wrote:

> >From: "James J. Gavan" jjgavan@shaw.ca
> >Date: 4/21/03 2:02 PM Eastern Daylight Time
…[17 more quoted lines elided]…
>

We are way, way off topic - but it's fascinating isn't it <G> Our unofficial
moderator WMK is probably saying to himself, "I'd rather read RW's messages - at
least they *are* about COBOL !".

Are you or Howard going to confirm. The black raspberry is that a hybrid from
raspberries and blackberries. Do they grow on raspberry canes as opposed to
blackberries which throw out 'branches' randomly in hedgerows.

Things that grow easily here - and Calgarians go nuts in late May when the nursery
gardens make a killing - most of the traditional flowers, bushes, (not azaleas or
rhododendrons - soil is wrong and winters are too severe),  peas, beans, (the 1
foot tall plants, green and yellow varieties), broad beans (in UK and called
Windsor broad beans in Canada), chard, spinach (if you can pick it quick enough
before it bolts), red and pale green cabbages - if you can get at them before the
slugs; maize/corn; courgette/zucchini - like your home grown tomatoes - a challenge
to pick them and give them away before they get too big and resemble an English
marrow If you can find a friendly Indian shaman to chant over your seeds, you can
get lucky and grow Scarlet Runner Beans (pole beans ?)

Fruit wise - rhubarb, strawberries and inferior eating apple species, red and black
currants. Yes and gooseberries. About ten years back my sister-in-law watched
fascinated as I picked them - so small. Her comment, "That size ? We leave those on
the bushes at home and don't bother". When she emplaned for UK, I went home and
thought, 'Screw You !" - and dug the useless gooseberry bushes up <G>

Ironically only last night I made a blackberry and apple pie as we had friends
coming over. Grow  blackberries here - forget it. It is not the cold; it is the hot
and cold. Pacific warm winds blow in over the mountains in what we call Chinook
winds  This prevails all year. As an example, during April/May you can get up and
see everything covered in snow. A Chinook arrives and by midday gonzo ! In the
afternoon you can spend your time sun bathing. We have a Calgarian saying, "Wait an
hour and the weather will change".

Last Christmas was a Brown not White Christmas. There is far more snow in the east
- Quebec, Ontario and down into NY State.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 30)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-04-23T01:53:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030422215323.18807.00000354@mb-m26.aol.com>`
- **References:** `<3EA5C41C.EA77C3FF@shaw.ca>`

```
>From: "James J. Gavan" jjgavan@shaw.ca 
>Date: 4/22/03 6:53 PM Eastern Daylight Time

>Are you or Howard going to confirm. The black raspberry is that a hybrid from
>raspberries and blackberries. Do they grow on raspberry canes as opposed to
>blackberries which throw out 'branches' randomly in hedgerows.
>

I cannot confirm or deny this.  I will say that when I moved into my current
abode many moons ago there were raspberries growing in the backyard behind the
garage, both black and red and I couldn't tell the plants apart except for the
tags I put on each plant after the first year.  Unfortunately my neighbor
killed them off when he poisoned the day lilly patch next to them.
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 31)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-23T02:36:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA5F767.76D8E1C@shaw.ca>`
- **References:** `<3EA5C41C.EA77C3FF@shaw.ca> <20030422215323.18807.00000354@mb-m26.aol.com>`

```


YukonMama wrote:

> >From: "James J. Gavan" jjgavan@shaw.ca
> >Date: 4/22/03 6:53 PM Eastern Daylight Time
…[10 more quoted lines elided]…
> killed them off when he poisoned the day lilly patch next to them.

From what you describe, still a raspberry growing on canes, and probably 'mated'
with a blackberry at some time.

Jimmy
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 30)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-23T13:38:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8651b$ed4$1@peabody.colorado.edu>`
- **References:** `<3EA4339A.78B67542@shaw.ca> <20030421212458.19022.00000265@mb-m16.aol.com> <3EA5C41C.EA77C3FF@shaw.ca>`

```

On 22-Apr-2003, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> Things that grow easily here - and Calgarians go nuts in late May when the
> nursery
> gardens make a killing - most of the traditional flowers, bushes, (not azaleas
> or
> rhododendrons - soil is wrong and winters are too severe),


Greenhouses work quite well when you are at the latitude of Germany.   You get
enough sun.
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 31)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-23T19:33:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA6E698.F3311F0C@shaw.ca>`
- **References:** `<3EA4339A.78B67542@shaw.ca> <20030421212458.19022.00000265@mb-m16.aol.com> <3EA5C41C.EA77C3FF@shaw.ca> <b8651b$ed4$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> On 22-Apr-2003, "James J. Gavan" <jjgavan@shaw.ca> wrote:
>
…[7 more quoted lines elided]…
> enough sun.

Now we are back to tomatoes. About 25 years ago there were a couple of attempts to
grow tomatoes locally, using heat from gas plants fed into greenhouses - actually
'blimp' like structures, transparent version of air balloon material, spread over
lightweight aluminium structures for shape.

For a year or two there was produce in the supermarkets - but the idea fizzled out -
a guess - lots of maintenance on the skin where it kept tearing from wind gusts.
Plus of course, increased heating costs during the winter period.

Latitude wise - take a gander at a map - Calgary and Taunton, Somerset are roughly
the same latitude - but oh what a difference due to elevation and the closeness of
the mountains. Taunton is about 150 feet above sea level and we did smell the odd
rose in the garden on Christmas Day.

Jimmy
```

###### ↳ ↳ ↳ Re: OT Re: Humanity (was:R W's insults (was: Beginner's Question))

_(reply depth: 27)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-22T02:57:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea4a896.274805966@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz> <3e9814c8.102710818@news.optonline.net> <3e9821e9_2@127.0.0.1> <3e984ab5.116518084@news.optonline.net> <3e993e8f_2@127.0.0.1> <3e998d79.74951713@news.optonline.net> <3e99a8b0_1@127.0.0.1> <b813rh$23f$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 13-Apr-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
…[19 more quoted lines elided]…
>ancestors did.

True. Good point. But the vast majority of Americans opt for crap food. At least
95% of them. I suspect it's the same everywhere except, perhaps, in the
Middle-East and Mexico, both of which have a long tradition of vegetarianism. 

People think Indians are all vegetarians. Wrong. There is nothing in the Hindu
religion saying they should be. The country with the highest percentage of
vegetarians is Mexico, and it has nothing to do with religion.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 20)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-12T12:51:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304121151.3bedd2df@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b760cf$f4b$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote 

> In 1900 there was 1.6 billion world population population.  Those people 
> are all dead now (or so nearly all it doesn't matter - except to them).

Actually I forgot my Great Aunt Judy, my Grandfather's sister on my
mother's side.  She is 103, and does matter to me (though I haven't
seen her for some time).
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 19)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-11T15:13:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e96cd8b_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e960425.353924148@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[3 more quoted lines elided]…
> An interesting fact: of all the people born since the beginning of
historical
> time (roughly 4,000 BC), 90% are living today. In other words, only 10% of
> humans have died.

While this is an interesting fact(oid?), Robert, it entirely misses the
point of my post, which was not saying that large percentages of the
population have died for the right to a voice, simply that some people have
paid the ultimate price in trying to get heard.

It really doesn't matter how many.

We should be aiming to ensure that NOBODY is stifled or killed in trying to
say what they think. If we can achieve that, it has some extremely
beneficial knock-on effects for Society as a whole.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-11T14:57:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76l5n$ofb$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net>`

```

On 10-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> An interesting fact: of all the people born since the beginning of historical
> time (roughly 4,000 BC), 90% are living today. In other words, only 10% of
> humans have died.

I bet there is a slight majority who have died.   Do you have figures?
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 20)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-04-11T12:11:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b76svs02m9a@enews1.newsguy.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b76l5n$ofb$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b76l5n$ofb$1@peabody.colorado.edu...
>
> On 10-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
>
> > An interesting fact: of all the people born since the
beginning of historical
> > time (roughly 4,000 BC), 90% are living today. In other
words, only 10% of
> > humans have died.
>
> I bet there is a slight majority who have died.   Do you have
figures?

Just offering data:

Year        Millions
-10000     4
-8000      5
550       250
1567       450
1825       1000
1903       1600
1954       3000
1984       5000
1996       5800

http://www.pbs.org/kqed/population_bomb/danger/time.html
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 21)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T00:31:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e975e20.55943825@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b76l5n$ofb$1@peabody.colorado.edu> <b76svs02m9a@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote:

>
>"Howard Brazee" <howard@brazee.net> wrote in message
…[26 more quoted lines elided]…
>http://www.pbs.org/kqed/population_bomb/danger/time.html

Thank you for saving me the trouble of looking it up. I would have produced
similar numbers. 

Human population in prehistoric times is unknown but probably very low, less
than 2-4 million in -10,000 and probably less than 100,000 before -100,000.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 20)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-12T17:17:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e983c61.112849058@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com> <3e93ec4e_1@127.0.0.1> <3E940FC7.6070001@ix.netcom.com> <3e94be7c_2@127.0.0.1> <3e960425.353924148@news.optonline.net> <b76l5n$ofb$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On 10-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[5 more quoted lines elided]…
>I bet there is a slight majority who have died.   Do you have figures?

After looking them up, I realize I got it backwards. Only 10% are living today.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 21)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-19T06:31:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7o67g$i3i$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e960425.353924148@news.optonline.net> <b76l5n$ofb$1@peabody.colorado.edu> <3e983c61.112849058@news.optonline.net>`

```
Robert Wagner wrote:

> After looking them up, I realize I got it backwards. 

About 80% of the traffic in this group could be cut out if you could do 
this on a regular basis _before_ posting.    ;-)
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-10T02:30:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94bfe5.270903169@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net> <3E937263.4060301@ix.netcom.com>`

```
Steve Thompson <n_o_spam.steve_t@ix.netcom.com> wrote:

>So it did not take me long to realize this guy was a troll. I'm 
>sorry it took the rest of you so long.

It is not entirely clear who "this guy" refers to, but it SEEMS to refer to me. 

If so, you got it wrong, I'm not a troll.
```

###### ↳ ↳ ↳ Re: RW's insults (was: Beginner's Question

_(reply depth: 14)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-10T02:30:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94d6a5.276728554@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <b6ve74$d4i$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>A number of us have TRIED to explain to him why he is so widely "disparaged"
>within the NG, but he seems totally unable to understand it.  I believe that
>he probably has some pathological emotional/mental problems, but without
>knowing him (God forbid!) in "real life" it is impossible for me to know
>whether this is true or what type of "cure" he should seek.

The range of expertise in this newsgroup is impressive. Not only do we have
expert COBOL programmers but also psychologists who can 'diagnose from afar'.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-08T18:30:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6vii7$3q7$1@panix1.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu>`

```
In article <b6ump1$g9c$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On  7-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[3 more quoted lines elided]…
>If I am paranoid, I wouldn't know it - so I had better test this hypothesis.

This is similar to an exchange I recall from the film 'Awakenings':

'Are you aware of the unconscious hostility you are exhibiting to this 
group?'

'If I were aware of it then it wouldn't be unconscious.'

DD
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 13)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-04-08T22:56:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2fe22$0244c640$6bccf943@chottel>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu>`

```
Just because you are paranoid doesn't mean that they aren't out to get you
:-)

Howard Brazee <howard@brazee.net> wrote in article
<b6ump1$g9c$1@peabody.colorado.edu>...
> 
> On  7-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
> 
> > You the only participant _insulted_ every time the topic of periods
comes up.
> 
> If I am paranoid, I wouldn't know it - so I had better test this
hypothesis.  It
> would be useful for me to recognize a problem in myself and then start
working
> on it.
> 
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T00:08:18+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e93566d_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b6ump1$g9c$1@peabody.colorado.edu...
>
> On  7-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
>
> > You the only participant _insulted_ every time the topic of periods
comes up.
>
> If I am paranoid, I wouldn't know it - so I had better test this
hypothesis.  It
> would be useful for me to recognize a problem in myself and then start
working
> on it.
>
…[5 more quoted lines elided]…
> paranoid in thinking that he has insulted me?

OK, let me start by saying I am not going into the rights and wrongs of
either the personalities or the posts, I am simply responding to your
request, Howard.

I feel totally unbiased here as I really can't decide who is behaving more
stupidly...somebody with an unfortunate attitude or a bunch of professionals
who really should know better.

1. You are sensitive about the use of periods in COBOL. (It is true that you
usually respond on threads about this...). I wouldn't go so far as to say
you are paranoid. (But that doesn't mean they're not out to get you...<G>)

2. He has insulted you, but don't feel singled out... He insults everybody.
(A lot of the time he does it without even realising he's doing it...<G>)
His insults are not malicious. There is no venom and spite in it. He is
responding to the fact that every time he posts here he gets jumped on by a
number of people (usually the same ones...no names but just follow my eyes
<G>), no attempt is made to understand what he means (as opposed to the
letter of what he said), his posts have become like red rags to a bull, so
it was only a matter of time before it would degenerate into name-calling
and personal insults.

It has gone way beyond the rights and wrongs of reasoned argument. If he
could be banned from the group he would have been (THAT is the ONLY bit that
really concerns me...I explained why, in a previous post, which everyone
either disagreed with, or was so enraged about real or imagined insults,
they never even saw the importance of the underlying principle.)

The whole "contest" between Robert and "the Rest" is becoming boring in the
extreme and it is no wonder that people are leaving the group. (I hope
Volker is still lurking...his inputs were always valuable.)

I mentioned once before that a similar long-winded, pointless exchange
(between two guys who have become two of the most valuable posters to this
group) was like "two bald men fighting for a comb"...this is worse than
that. Arguing with Robert is like a blind man, in a darkened room, looking
for a black cat...that isn't there.

If you really MUST continue this (and I respect your right to...) could we
at least agree NOT to get to the point where personal offense is taken?

Hey, maybe we could have another prefix on the Subject (like we have "OT"
for "Off Topic"... I suggest: VLTFOPM - Very long thread full of pointless
mudslinging... then those of us who are wearying of it could simply not look
at it. This simple device might prevent the group from deteriorating into a
handful of people massaging their egos by trying to score points off each
other...

Pete <yawn>





----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 14)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-09T09:13:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C6B070.09131909042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <3e93566d_1@127.0.0.1>`

```
In article <3e93566d_1@127.0.0.1>,
 "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> The whole "contest" between Robert and "the Rest" is becoming boring in the
> extreme and it is no wonder that people are leaving the group. (I hope
> Volker is still lurking...his inputs were always valuable.)

I thought he was on a holiday cruise sans laptop.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-09T14:21:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b71a9c$1ja$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <3e93566d_1@127.0.0.1>`

```

On  8-Apr-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> If you really MUST continue this (and I respect your right to...) could we
> at least agree NOT to get to the point where personal offense is taken?

I'll make this effort.   I will attempt to limit my responses to content instead
of personality.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 15)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-10T01:47:48+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94bf3f_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <3e93566d_1@127.0.0.1> <b71a9c$1ja$1@peabody.colorado.edu>`

```
Excellent Howard!

It would be a shame indeed if you allowed interaction here to bring you
down, depress you, or cause you to not contribute any further.

It is just a forum... <G>

Pete.


"Howard Brazee" <howard@brazee.net> wrote in message
news:b71a9c$1ja$1@peabody.colorado.edu...
>
> On  8-Apr-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> > If you really MUST continue this (and I respect your right to...) could
we
> > at least agree NOT to get to the point where personal offense is taken?
>
> I'll make this effort.   I will attempt to limit my responses to content
instead
> of personality.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 13)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-04-08T22:07:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0304082107.7d6928b3@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message news:<b6ump1$g9c$1@peabody.colorado.edu>...
> On  7-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
> 
…[11 more quoted lines elided]…
> paranoid in thinking that he has insulted me?

I dunno about the insulting or paranoia, but I would think if you
really were paranoid you would have had some physical reaction to
typing the three periods after "everybody".............

So - since you actually didn't pass out reading all those periods I
just posted, I would say you are NOT paranoid.

Period.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-09T14:23:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b71ac8$1jh$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <b6hh8b$nk8$1@peabody.colorado.edu> <3e8ccc34.230921866@news.optonline.net> <b6isep$qh5$1@aklobs.kc.net.nz> <3e8dba83.32538985@news.optonline.net> <b6kja5$i5j$1@peabody.colorado.edu> <3e8e8dbe.10017252@news.optonline.net> <3e8eaa90_2@127.0.0.1> <3e8f16dd.45126250@news.optonline.net> <b6s3ih$8ak$1@peabody.colorado.edu> <3e91c37c.75185032@news.optonline.net> <b6ump1$g9c$1@peabody.colorado.edu> <bfdfc3e8.0304082107.7d6928b3@posting.google.com>`

```

On  8-Apr-2003, thaneh@softwaresimple.com (Thane Hubbell) wrote:

> I dunno about the insulting or paranoia, but I would think if you
> really were paranoid you would have had some physical reaction to
> typing the three periods after "everybody".............

Aggh!  flop.

> So - since you actually didn't pass out reading all those periods I
> just posted, I would say you are NOT paranoid.

Where am I?  Oh.   That's good.
```

##### ↳ ↳ Re: Beginner's Question

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-03T11:11:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304031111.2d0a79e2@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >     FILE SECTION.
> >       FD Logfile.
…[12 more quoted lines elided]…
> parse quoted strings. You'll have to do it yourself. 

Given that this is a log file and the 'resource path' is most probably
a URL then it will most likely _not_ contain spaces, or be quoted. Can
you provide a refernce where URLs get quoted ?

In fact the spaces should be represented by %20.

But even if the the resource path _does_ contain spaces, any
programmer with two clues can use UNSTRING without any problem:

           MOVE 1      TO log-pointer
           UNSTRING LogFileRecord
               DELIMITED BY ALL SPACES
               INTO Bits-Date Bits-Time
                    Bits-IP Bits-Country
               WITH POINTER log-pointer
           MOVE LogFileRecord(log-pointer:)  TO Bits-Resource

Dtae and Time may be concatenated in the data.

> Do try to write the parser as a separate 'program' within the same compile unit.
> Doing so will get you extra points. 

Copying someone else's program will get no points at all.

>      set address of line-entry to last-line
>      set previous-last-line to last-line
>      set address of word-entry to null

The answer is supposed to be in Cobol.

>      set allocation-pointer to null
>      call 'malloc' using allocation-length, allocation-pointer

If the tutor wanted a C program he would have asked it to be written
in C.

Al in all a few pages of marginal Cobol that can be done by a couple
of Cobol statements (by anyone who _understands_ UNSTRING).
```

###### ↳ ↳ ↳ Re: Beginner's Question

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-03T19:36:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6i2gd$3m9$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com>`

```

On  3-Apr-2003, riplin@Azonic.co.nz (Richard) wrote:

> Given that this is a log file and the 'resource path' is most probably
> a URL then it will most likely _not_ contain spaces, or be quoted. Can
> you provide a refernce where URLs get quoted ?
>
> In fact the spaces should be represented by %20.

Which is why the primary rule is "know the data".

> But even if the the resource path _does_ contain spaces, any
> programmer with two clues can use UNSTRING without any problem:
…[9 more quoted lines elided]…
> Dtae and Time may be concatenated in the data.

But a beginner asking for help doesn't have the two clues unless we share them.
Clue #1 is to look up UNSTRING.   Clue #2 modifies this to give a hint on how to
overcome the delimiter problem.  (or to suggest an alternative way of solving
the problem).

I've worked with lots of programmers who would have to spend 20 minutes to
figure out the above code.  (and some who would have gotten it in 2 minutes, and
some who needed 2 seconds).
```

###### ↳ ↳ ↳ Re: Beginner's Question

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-04T01:59:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8cd754.233770482@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[18 more quoted lines elided]…
>you provide a refernce where URLs get quoted ?

They don't. I thought ResourcePath might be a Unix path/file, which could
contain embedded spaces. 

>But even if the the resource path _does_ contain spaces, any
>programmer with two clues can use UNSTRING without any problem:
…[9 more quoted lines elided]…
>Date and Time may be concatenated in the data.

I hate reference modification. Either use COBOL parsing via UNSTRING or do it
all yourself. Yours is a hybrid solution. 

>> Do try to write the parser as a separate 'program' within the same compile
unit.
>> Doing so will get you extra points. 
>
…[6 more quoted lines elided]…
>The answer is supposed to be in Cobol.

That was the 'list building stuff' he needed to delete. 

>>      set allocation-pointer to null
>>      call 'malloc' using allocation-length, allocation-pointer
>
>If the tutor wanted a C program he would have asked it to be written
>in C.

If you'd read the sample program, you would have seen that 'malloc' was indeed a
COBOL program, not a call to the C library. In the instant case, that's 'list
building stuff' he needed to delete. 

>Al in all a few pages of marginal Cobol that can be done by a couple
>of Cobol statements (by anyone who _understands_ UNSTRING).

It is more valuable for a student to know how to do it himself because, in the
real world, UNSTRING will let him down more times than not. I'm trying to teach
basics.

In a later post, Auburn (the famous college in Alabama?) said UNSTRING was what
the instructor was looking for. Fine. Wait till he hits the the real world and
discovers the deficiencies of UNSTRING.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-04T14:51:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6is1m$qbf$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net>`

```
Robert Wagner wrote:

>>But even if the the resource path _does_ contain spaces, any
>>programmer with two clues can use UNSTRING without any problem:
…[7 more quoted lines elided]…
>>           MOVE LogFileRecord(log-pointer:)  TO Bits-Resource
 
> I hate reference modification. Either use COBOL parsing via UNSTRING or do
> it all yourself. 

Why should we do it some other way just because _YOU_ hate it ?

> Yours is a hybrid solution.

It use two different Cobol statements, what is your point ?  Do you only 
like solutions that use just one Cobol statement ?

Perhaps, just to show your skills you could construct a replecement for the 
MOVE using a second UNSTRING.  It is possible, easy even.

> That was the 'list building stuff' he needed to delete.

He needed to delete the whole of your code.

>If the tutor wanted a C program he would have asked it to be written
>>in C.
…[3 more quoted lines elided]…
> that's 'list building stuff' he needed to delete.

I do know that your 'malloc' is Cobol code that calls something else to 
actually get the memory.

But it is still a 'C program' written in Cobol code.  ie it is in the same 
form as a C program would be and is not how a Cobol program would be.

> It is more valuable for a student to know how to do it himself because, in

So why did you supply pages of code ?  ego-boosting was it ?

> the real world, UNSTRING will let him down more times than not. 

It may have 'let you down', as did your attempts at initialize and many 
other things that you never understood.  UNSTRING works well for those with 
the skills to read the manual.

> I'm trying to teach basics.

It didn't seem to me that using a few pages of code that does an 
inappropriate parsing using memory allocation was 'basic'.

> In a later post, Auburn (the famous college in Alabama?) said UNSTRING was
> what the instructor was looking for. Fine. Wait till he hits the the real
> world and discovers the deficiencies of UNSTRING.

Oh god, not another rehash of 'what initialize should do', just because you 
can't grok UNSTRING.

Come on then tell us about these 'deficiencies' are.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T09:13:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8e756e.3792496@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6is1m$qbf$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[22 more quoted lines elided]…
>MOVE using a second UNSTRING.  It is possible, easy even.

Yes, it is easy. 

unstring LogFileRecord delimited by 'nonesuch' into  Bits-Resource with pointer
log-pointer

>But it is still a 'C program' written in Cobol code.  ie it is in the same 
>form as a C program would be and is not how a Cobol program would be.

I think you meant 'should be'. Within the last three months, I've written
>20,000 lines of COBOL in this style. The problem couldn't have been solved with
traditional COBOL. 

>> In a later post, Auburn (the famous college in Alabama?) said UNSTRING was
>> what the instructor was looking for. Fine. Wait till he hits the the real
…[5 more quoted lines elided]…
>Come on then tell us about these 'deficiencies' are.

It cannot even parse COBOL source, much less the equivocal documents I deal
with. For instance:

It cannot preserve quoted strings as a single 'word'.

I want ALL non-alphabetic & non-numeric characters to act as delimiters.
UNSTRING would have me list them. It should have a NOT option: delimited by all
(space or not (alphabetic or numeric)). If it did, a line of hyphens, equal
signs or periods would be a single delimiter, whereas "+-+-" would be four
delimiters. 

It cannot handle context-sensitivity:

"period." should be rendered as two words; "123.45" and "123." should each
return one word. You and COBOL standard will say the delimiter is '. ' (period-
space). What about malformed input where the space is missing, as in  "..
periods.Any idiot ..."? Software should be smart enough to supply the missing
space. 

"AC/DC" and 'his/her" and "tweedledum+tweedledumber" and "a+b" should return
three words. "2003/03/03" and "123+" should return one word.  In these examples,
'/' and '+' are sometimes delimiters, sometimes not. 

"COBOL-COmmon Business" should return four words. Hyphen is a minefield of
context-sensitivity. It can be a negative sign, a line drawing character (where
it should be treated as spaces), punctuation (as in ---), a character in a
hyphenated-word, a date separator, a colon equivalent (above), a substitute for
zero in a report column and an arithmetic operator. 

Another issue is missing delimiters, which can be inferred by context. In
addition to the period-space above:

"123USD" should return two words. "1,234,5671,234,567" should also return two
words; report columns ran together. 

You'll say it's unreasonable to expect UNSTRING to have that much intelligence.
I'd reply that any sixth-grade child could disambiguate the above cases.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-06T07:53:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6ncb4$e9n$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6is1m$qbf$1@aklobs.kc.net.nz> <3e8e756e.3792496@news.optonline.net>`

```
Robert Wagner wrote:

>>Come on then tell us about these 'deficiencies' are.
> 
…[8 more quoted lines elided]…
> "123USD" should return two words. 

UNSTRING is a _statement_ not a complete application.  Name one statement 
in any other language that _can_ do these.

> You'll say it's unreasonable to expect UNSTRING to have that much
> intelligence. 

Did you know that ADD is entirely deficient because it won't print my 
invoices, it won't even do division, or walk the dog.

> I'd reply that any sixth-grade child could disambiguate the
> above cases.

The child can also do division and walk the dog.

But I bet you can't instruct the child to do it with a single statement.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-05T21:55:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f42d9$1_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6is1m$qbf$1@aklobs.kc.net.nz> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b6ncb4$e9n$1@aklobs.kc.net.nz...
> Robert Wagner wrote:
>
…[4 more quoted lines elided]…
>
"Kid, walk the dog."
"Kid, what is 9 divided by 3?"

Or the compound conditional form...

"Kid, if you want your allowance AND you want to get to be a BIG kid, walk
the dog and divide 9 by 3 for me..."

Pete.
(Extreme experience in programming other people's children...<G>)




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-06T10:49:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6nmje$k7n$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6is1m$qbf$1@aklobs.kc.net.nz> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <3e8f42d9$1_1@127.0.0.1>`

```
Peter E.C. Dashwood wrote:

>> But I bet you can't instruct the child to do it with a single statement.
>>
> "Kid, walk the dog."

Yes, but then someone is bound to whine that the instruction has 
'deficiencies' because the kid did not walk the dog to the park, did not 
use the lead, did not feed it and did not also brush the dog afterwards,

Actually I had hoped the 'do it' referred back to RW's 'deficiencies', I 
obviously needed to make that more explicit.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-05T16:03:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-99422B.16030605042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6is1m$qbf$1@aklobs.kc.net.nz> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz>`

```
In article <b6ncb4$e9n$1@aklobs.kc.net.nz>,
 Richard Plinston <riplin@Azonic.co.nz> wrote:

> UNSTRING is a _statement_ not a complete application.  Name one statement 
> in any other language that _can_ do these.

I think you can do it in Perl using a single statement...I'll look 
around for that perl log file processor example...
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-06T10:59:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6nn6a$khg$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <joe_zitzelberger-99422B.16030605042003@corp.supernews.com>`

```
Joe Zitzelberger wrote:

>> UNSTRING is a _statement_ not a complete application.  Name one statement
>> in any other language that _can_ do these.
> 
> I think you can do it in Perl using a single statement...I'll look
> around for that perl log file processor example...

I, for one, would be quite happy for RW to move on to PERL and 
comp.lang.perl.  I am sure they would both be very happy.

Of course processing a log file is well within the designed abilities of 
UNSTRING, even RW could manage that.

It may have been possible to design UNSTRING to do what RW wants, but the 
syntax would be extensive and just as obscure as PERL.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-06T03:49:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f90c0.76333876@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <joe_zitzelberger-99422B.16030605042003@corp.supernews.com> <b6nn6a$khg$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:


>I, for one, would be quite happy for RW to move on to PERL and 
>comp.lang.perl.  I am sure they would both be very happy.

You wish. I'm here to hold your nose to it.

Tell us how you feel about periods. Don't hide behind 'freedom of choice', just
say whether you use them or not. I know the answer will embarrass you. 

>Of course processing a log file is well within the designed abilities of 
>UNSTRING, even RW could manage that.

Imagine .. even an idiot could do it.

>It may have been possible to design UNSTRING to do what RW wants, but the 
>syntax would be extensive and just as obscure as PERL.

Forget PERL, write it in COBOL. It would need an external Rules File to define
parsing rules.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-05T23:51:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304052351.67b403a8@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <joe_zitzelberger-99422B.16030605042003@corp.supernews.com> <b6nn6a$khg$1@aklobs.kc.net.nz> <3e8f90c0.76333876@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> You wish. I'm here to hold your nose to it.

Are you really here to hold my nose to your excrement ?  How nice.

> Tell us how you feel about periods. Don't hide behind 'freedom of choice', 

Don't you believe in 'freedom of choice' ?  Do you want to be a
dictator ?  Should we all be grateful to the illumination that you
have brought to this site ?

(NOTE: the last was s.a.r.c.a.s.m - look it up if you don't know what
this is).

> just say whether you use them or not. 

I use full stops.  I have seen your code and I know that you use full
stops. In a recent post you had 22 lines of Cobol containing 23 full
stops.

> I know the answer will embarrass you.

You seem to use the word 'know' in a strange and unnatural way, one
that I am unfamiliar with..

In fact I have posted samples of my code here and at least it works as
advertised.  It is you that should be embarrassed by your code due to
failings that I have already pointed out.

If you can't work out my approach to full stops from the sample code
then you should be embarrassed yourself.
 
> >Of course processing a log file is well within the designed abilities of 
> >UNSTRING, even RW could manage that.
> 
> Imagine .. even an idiot could do it.

That's the one.  It didn't need several pages of code to do something
completely irrelevant, such as breaking down 'resources' into separate
[possible] 'words' just to have it assembled back again, when it could
be moved as a complete block once the start point was established.

Of course your solution will fail if 'nonesuch' exists in the resource
name, for example if it was a web page discussing London Bridge in the
16thCentury, or small towns in Kentucky, or record companies, or ...

A small failure rate maybe, but a more appropriate choice may have
been a character that could not occur, such as high-value.
 
> >It may have been possible to design UNSTRING to do what RW wants, but the 
> >syntax would be extensive and just as obscure as PERL.
> 
> Forget PERL, write it in COBOL. It would need an external Rules File to define
> parsing rules.

Use appropriate tools. If it can be easily done in some specialised
language then call that from Cobol or execute a program in that
language to produce results to be read back into Cobol to produce the
report.

I don't complain that my hammer is 'deficient' because it won't
tighten bolts, nor would I weld a spanner head to my hammer just
because it had a nice handle.

But, no, I _won't_ write it in Cobol, and I really don't care if you
do or not.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-06T16:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9048f3.123496525@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <joe_zitzelberger-99422B.16030605042003@corp.supernews.com> <b6nn6a$khg$1@aklobs.kc.net.nz> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote

>> just say whether you use them or not. 
>
>I use full stops. 

I had not seen your code, so I found some in the archive. There are no
unnecessary periods. 

>I have seen your code and I know that you use full
>stops. In a recent post you had 22 lines of Cobol containing 23 full
>stops.

In the data division, where they are required. Who is being disingenuous now?

>Of course your solution will fail if 'nonesuch' exists in the resource
>name, for example if it was a web page discussing London Bridge in the
>16thCentury, or small towns in Kentucky, or record companies, or ...

I used 'nonesuch' to illustrate a point. Had I used high-values, someone might
think there _was_ a high-value to be found.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-08T07:24:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6sj9l$40m$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net>`

```
Robert Wagner wrote:

> I had not seen your code, so I found some in the archive. There are no
> unnecessary periods.

Is that as close to an apology as I am likely to get ?

> I used 'nonesuch' to illustrate a point. Had I used high-values, someone
> might think there _was_ a high-value to be found.

Not by anyone who _understands_ UNSTRING.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-08T06:37:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e924e67.110753300@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[3 more quoted lines elided]…
>Is that as close to an apology as I am likely to get ?

Ok, I apologize for thinking you might be Old School.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-08T12:10:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304081110.6b4e1ceb@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> >> I had not seen your code, so I found some in the archive. There are no
> >> unnecessary periods.
…[3 more quoted lines elided]…
> Ok, I apologize for thinking you might be Old School.

Whatever gave you the idea that I had anything in common with an old fart like you ?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 15)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-10T02:30:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94a48e.263902747@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[7 more quoted lines elided]…
>Whatever gave you the idea that I had anything in common with an old fart like
you ?

You had to ruin it .. flaming an apology.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 16)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-10T00:00:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304092300.5a3b295d@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com> <3e94a48e.263902747@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >> Ok, I apologize for thinking you might be Old School.
> >
…[3 more quoted lines elided]…
> You had to ruin it .. flaming an apology.

I'm sorry, I misunderstood what you meant by 'Old School', I took it
as one of your 'class' issues.

I see that you are using it as a term for the mainframers from way
back. Well I am one of them, having started in the '60s.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e95fd00.352094736@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com> <3e94a48e.263902747@news.optonline.net> <217e491a.0304092300.5a3b295d@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote
>
>> >> Ok, I apologize for thinking you might be Old School.
>> >
>> >Whatever gave you the idea that I had anything in common with an old fart
like
>> you ?
>> 
…[3 more quoted lines elided]…
>as one of your 'class' issues.

I don't raise 'class' issues. Few Americans do; that's a British thing. I was
joshing when I referred to German -> shoes, Americans -> autos. 

>I see that you are using it as a term for the mainframers from way
>back. Well I am one of them, having started in the '60s.

Me too. I think many/most CLC posters have had 40 year careers. Some are anxious
about obsolescence.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-10T13:50:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b73sr2$7he$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com> <3e94a48e.263902747@news.optonline.net>`

```

On  9-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >> Ok, I apologize for thinking you might be Old School.
> >
…[3 more quoted lines elided]…
> You had to ruin it .. flaming an apology.

Just curious (with no comment).   If that was an apology is "Old School" an
insult?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 17)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-10T20:35:02+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e95c773$1_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com> <3e94a48e.263902747@news.optonline.net> <b73sr2$7he$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:b73sr2$7he$1@peabody.colorado.edu...
>
> On  9-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[3 more quoted lines elided]…
> > >Whatever gave you the idea that I had anything in common with an old
fart
> > >like you ?
> >
> > You had to ruin it .. flaming an apology.
>
> Just curious (with no comment).   If that was an apology is "Old School"
an
> insult?

I can think of at least one "Old School" I attended that was an apology for
an educational institution...<G>

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 18)_

- **From:** stringer@es.co.nz (stringer)
- **Date:** 2003-04-10T21:30:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b74npo$cdf$1@lust.ihug.co.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com> <3e94a48e.263902747@news.optonline.net> <b73sr2$7he$1@peabody.colorado.edu> <3e95c773$1_2@127.0.0.1>`

```
In article <3e95c773$1_2@127.0.0.1>, dashwood@enternet.co.nz says...
>
>
…[6 more quoted lines elided]…
>
Pete, 

Obviously not Christ's College??? Or was it?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 19)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-11T15:29:41+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e96d160_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com> <3e94a48e.263902747@news.optonline.net> <b73sr2$7he$1@peabody.colorado.edu> <3e95c773$1_2@127.0.0.1> <b74npo$cdf$1@lust.ihug.co.nz>`

```

"stringer" <stringer@es.co.nz> wrote in message
news:b74npo$cdf$1@lust.ihug.co.nz...
> In article <3e95c773$1_2@127.0.0.1>, dashwood@enternet.co.nz says...
> >
> >
> >
> >I can think of at least one "Old School" I attended that was an apology
for
> >an educational institution...<G>
> >
…[7 more quoted lines elided]…
>
I forgot there was at least one other Kiwi here...<G>

My lips are sealed... <G> But I will admit to attending Rongotai and
Wellesley Colleges, which were both excellent.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 18)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:36:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9636db.366907583@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com> <3e94a48e.263902747@news.optonline.net> <b73sr2$7he$1@peabody.colorado.edu> <3e95c773$1_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Howard Brazee" <howard@brazee.net> wrote in message
…[17 more quoted lines elided]…
>an educational institution...<G>

This reminds me of a quote:

 Lettered gentility .. is achieved at King's College at the cost of
 certain theatricality. It is hard, at times, to recall that the
 pictures are real, the port is real, that the candles in the
 candlesticks are real candles and not electric lights pretending to be
 candles; above all, that the people are creatures of flesh and bone.
 In my two years there as a Fellow, I found that a sense of illusion
 was rapidly becoming my standard experiential mode. The air of charade
 was all-pervasive: the sons of suburbia, like myself, parodied the
 lettered gentry; and the lettered gentry parodied the sons of suburbia
 parodying themselves ... Brilliant young scientists who knew nothing
 of life or art gave ham performances of the role "brilliant young
 scientist who knows nothing of life or art." Vain art historians gave
 virtuoso performances of "art historian being distastefully vain." And
 the institution itself rose repeatedly to heights of dramatic
 absurdity.
                         - Liam Hudson, "The Cult of the Fact"'
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 17)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-11T03:28:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e95fb10.351598914@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <3e9048f3.123496525@news.optonline.net> <b6sj9l$40m$1@aklobs.kc.net.nz> <3e924e67.110753300@news.optonline.net> <217e491a.0304081110.6b4e1ceb@posting.google.com> <3e94a48e.263902747@news.optonline.net> <b73sr2$7he$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  9-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[9 more quoted lines elided]…
>insult?  

Not quite. It's a stylistic weakness.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-07T15:05:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s43i$8i3$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <joe_zitzelberger-99422B.16030605042003@corp.supernews.com> <b6nn6a$khg$1@aklobs.kc.net.nz> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com>`

```

On  6-Apr-2003, riplin@Azonic.co.nz (Richard) wrote:

> Don't you believe in 'freedom of choice' ?  Do you want to be a
> dictator ?  Should we all be grateful to the illumination that you
> have brought to this site ?

Remember, he said he welcomes people who program for him to develop their own
styles.

How many people believe him?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-08T06:46:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6sh27$2nb$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f90c0.76333876@news.optonline.net> <217e491a.0304052351.67b403a8@posting.google.com> <b6s43i$8i3$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

>> Don't you believe in 'freedom of choice' ?  Do you want to be a
>> dictator ?  Should we all be grateful to the illumination that you
…[5 more quoted lines elided]…
> How many people believe him?

I haven't seen any evidence that we should believe _anything_ that he says.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-07T15:03:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s407$8hu$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <joe_zitzelberger-99422B.16030605042003@corp.supernews.com> <b6nn6a$khg$1@aklobs.kc.net.nz> <3e8f90c0.76333876@news.optonline.net>`

```

On  5-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> Tell us how you feel about periods. Don't hide behind 'freedom of choice',
> just
> say whether you use them or not. I know the answer will embarrass you.

Someone telling me that periods are wrong should provide evidence, not insults.

Since I already said I use explicit terminators, and don't use NEXT SENTENCE,
the only arguments I have seen are:

1.  They can be hard to see.
2.  They make more work in cutting and pasting.

If you expect periods in a shop that already uses them, (1) isn't an issue,
unless we change standards and have some programs with periods and some without.
 So why change standards?

If we do a lot of cutting and pasting to within conditional code - we should
edit anyway - align up the code.   Better yet, put the code in a preformed
paragraph.


I'm not saying a shop that has standards to not use periods should change.  I'm
saying that a shop with standards to include periods should not be forced to
change for no better reason than to avoid being insulted by you.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-06T01:08:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f417d.56039240@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6is1m$qbf$1@aklobs.kc.net.nz> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[3 more quoted lines elided]…
>> It cannot preserve quoted strings as a single 'word'.
<snip>
>
>UNSTRING is a _statement_ not a complete application.  Name one statement 
>in any other language that _can_ do these.

struc word_list = lex(input_statement)
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-06T00:45:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304060045.3029a899@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6is1m$qbf$1@aklobs.kc.net.nz> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <3e8f417d.56039240@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote

> >UNSTRING is a _statement_ not a complete application.  Name one statement 
> >in any other language that _can_ do these.
> 
> struc word_list = lex(input_statement)

You will find that lex() is not a statement in C, it is an
implementation of YACC as a callable function, and thus is thousands
of statements.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-07T04:52:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6obqm$vk5$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8e756e.3792496@news.optonline.net> <b6ncb4$e9n$1@aklobs.kc.net.nz> <3e8f417d.56039240@news.optonline.net>`

```
Robert Wagner wrote:


>>> It cannot even parse COBOL source,
>>> It cannot preserve quoted strings as a single 'word'.
…[5 more quoted lines elided]…
> struc word_list = lex(input_statement)

And this parses Cobol source ?

If this does work then why would you want Cobol UNSTRING to do it too ?  
There is no point in simply duplicating what something else can do 
perfectly well.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-04T11:51:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8d63c4_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net>`

```
Robert,

while I accept that you may have a personal bias against UNSTRING, it is
really out of order to pass this bias on to a student.

If you really want to help, you should try and stay neutral on what
constructs are appropriate.

Personally, I use STRING, UNSTRING, and reference modification (controlled
properly) all the time and do NOT experience the problems you mention. (Not
even with SPACES and/or QUOTES in the strings...) I was surprised when I
noticed the byte-by-byte approach in your sample code.

While I make no comment on the code itself, I believe it was a "skipped
gradient" for a student to have this thrown at him/her before (s)he has
mastered basic constructs.

Maybe your experience could have been better contributed by pointing out
some of the conceptual pitfalls, rather than posting "advanced" COBOL?

I have been in the "real world" as long as you have and I strongly dispute
your claimed "deficiencies in the use of UNSTRING". The point is that these
are opinions. It is far, far, better if the student forms his/her OWN
opinions by experiment, rather than adopting yours or mine or their tutor's
as gospel...

We must all be careful not to rob them of that chance when attempting to
help them.

Pete.

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e8cd754.233770482@news.optonline.net...
> riplin@Azonic.co.nz (Richard) wrote:
>
…[14 more quoted lines elided]…
> >> Others will tell you to use UNSTRING. Wrong. Your ResourcePath can
contain
> >> embedded spaces, which will be enclosed in quotes. UNSTRING cannot
correctly
> >> parse quoted strings. You'll have to do it yourself.
> >
…[20 more quoted lines elided]…
> I hate reference modification. Either use COBOL parsing via UNSTRING or do
it
> all yourself. Yours is a hybrid solution.
>
> >> Do try to write the parser as a separate 'program' within the same
compile
> unit.
> >> Doing so will get you extra points.
…[17 more quoted lines elided]…
> If you'd read the sample program, you would have seen that 'malloc' was
indeed a
> COBOL program, not a call to the C library. In the instant case, that's
'list
> building stuff' he needed to delete.
>
…[3 more quoted lines elided]…
> It is more valuable for a student to know how to do it himself because, in
the
> real world, UNSTRING will let him down more times than not. I'm trying to
teach
> basics.
>
> In a later post, Auburn (the famous college in Alabama?) said UNSTRING was
what
> the instructor was looking for. Fine. Wait till he hits the the real world
and
> discovers the deficiencies of UNSTRING.
>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-04T13:24:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qIfja.1863$kd1.1797828@newssrv26.news.prodigy.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3e8d63c4_1@127.0.0.1...
>
> Personally, I use STRING, UNSTRING, and reference modification (controlled
> properly) all the time and do NOT experience the problems you mention.
(Not
> even with SPACES and/or QUOTES in the strings...)

It's not the paintbrush, it's the artist.

MCM
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-04T14:41:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6k5iq$cll$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1>`

```

On  4-Apr-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> I have been in the "real world" as long as you have and I strongly dispute
> your claimed "deficiencies in the use of UNSTRING". The point is that these
> are opinions. It is far, far, better if the student forms his/her OWN
> opinions by experiment, rather than adopting yours or mine or their tutor's
> as gospel...

But it is legitimate to express that he has found problems with UNSTRING.

Except for a bug I discovered in a Univac 9030 UNSTRING command 20 years ago, I
haven't found such problems.   But we can make recommendations based upon
experience - as long as we're willing to back up those recommendations.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-04T11:32:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6kfjh$fb0$1@slb3.atl.mindspring.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1> <b6k5iq$cll$1@peabody.colorado.edu>`

```
My personal experience with UNSTRING (string and reference-modification are
very different issues) is that it is often difficult to get a "final" answer
on the nature of the data to be processed.  It should be noted, that almost
all issues with "funny" data that impact UNSTRING *also* will impact using
byte-by-byte "processing".

Certainly the "classic" real-world problem is unstring names.   There have
been many past posts in CLC on this issue - and it is particularly relevant
in that some of the discussions have pointed out the difference between
student "exercises" with RELATIVELY simply names in files versus all the
"oddities" of real world commercial files/data-bases with name fields.

It is my personal impression that *IF* you can get a true description of the
data to be processed (with all its possible variations) *and* you actually
learn how UNSTRING works, then it is definitely a useful tool.  If you
canNOT get an adequate definition of all the variations in your "input
data" - then doing a byte-by-byte analysis won't work any more reliably than
UNSTRING and almost always will be "less intuitive" to those OTHERS who
might be required to do maintenance on your programs.

P.S.  STRING almost never has this type of problem - but may (like UNSTRING)
have a SLIGHT performance penalty when compared to "doing it yourself".

  IMHO, Reference modification - which has been a "built-in" part of the
COBOL language definition for almost 20 years now, is incredibly useful in
cases where:
  - too many "conflicting" redefinitions of a field would be required to be
"self-documenting"
  - start position or lengthy need to be "dynamically" determined at
run-time
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-04T09:50:43-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6kglk$q6j$1@si05.rsvl.unisys.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1> <b6k5iq$cll$1@peabody.colorado.edu> <b6kfjh$fb0$1@slb3.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b6kfjh$fb0$1@slb3.atl.mindspring.net...

> P.S.  STRING almost never has this type of problem - but may (like
UNSTRING)
> have a SLIGHT performance penalty when compared to "doing it yourself".

In some implementations, certain subsets of STRING and UNSTRING (and, for
that matter, INSPECT) logic have a DRAMATIC performance ADVANTAGE over
"doing it yourself".

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-04-05T04:09:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2fb29$0823f3c0$9b91f243@chottel>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1>`

```
Your post reminded me of this quote:

"The greatest deception men suffer is from their own opinions." Leonardo Da
Vinci

Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in article
<3e8d63c4_1@127.0.0.1>...
> Robert,
> 
…[6 more quoted lines elided]…
> Personally, I use STRING, UNSTRING, and reference modification
(controlled
> properly) all the time and do NOT experience the problems you mention.
(Not
> even with SPACES and/or QUOTES in the strings...) I was surprised when I
> noticed the byte-by-byte approach in your sample code.
…[8 more quoted lines elided]…
> I have been in the "real world" as long as you have and I strongly
dispute
> your claimed "deficiencies in the use of UNSTRING". The point is that
these
> are opinions. It is far, far, better if the student forms his/her OWN
> opinions by experiment, rather than adopting yours or mine or their
tutor's
> as gospel...
> 
…[33 more quoted lines elided]…
> > They don't. I thought ResourcePath might be a Unix path/file, which
could
> > contain embedded spaces.
> >
…[13 more quoted lines elided]…
> > I hate reference modification. Either use COBOL parsing via UNSTRING or
do
> it
> > all yourself. Yours is a hybrid solution.
…[31 more quoted lines elided]…
> > It is more valuable for a student to know how to do it himself because,
in
> the
> > real world, UNSTRING will let him down more times than not. I'm trying
to
> teach
> > basics.
> >
> > In a later post, Auburn (the famous college in Alabama?) said UNSTRING
was
> what
> > the instructor was looking for. Fine. Wait till he hits the the real
world
> and
> > discovers the deficiencies of UNSTRING.
…[5 more quoted lines elided]…
> ----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet
News==----
> http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000
Newsgroups
> ---= 19 East/West-Coast Specialized Servers - Total Privacy via
Encryption =---
>
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T09:13:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8e94d4.11832130@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

Your points are valid, and expressed well. I shall think twice before responding
to another student request for help. 

>Robert,
>
…[25 more quoted lines elided]…
>help them.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-05T11:38:17+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8eb224_2@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1> <3e8e94d4.11832130@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e8e94d4.11832130@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> Your points are valid, and expressed well. I shall think twice before
responding
> to another student request for help.
>
Ah, please don't learn the WRONG lesson...<G>

You have a huge amount of experience and knowledge and many students will be
pleased to benefit from it. Don't go away and decide you cannot contribute.

If your comment above means that you will continue to contribute, but will
simply consider your responses, then that's great. If it means you don't
intend to respond any more, I believe that would be a poor result.

What I am suggesting is that you think through what the purpose of helping
students is.

You said elsewhere that you haven't been involved in a formal teaching
environment so it is not surprising that you may not have thought about what
needs to be achieved with students.

The purpose is to help, and encourage them to grow.
(Personally, I believe the latter is FAR more important than the former; if
a student fails their COBOL or whatever, but has benefitted from the
experience of trying to learn it, I reckon that is a good result...But then,
I have never been into the "paper chase" and I accept that many people will
disagree...You can always re-take your course if it is essential for your
survival, but you may never have the same stimulations and opportunities for
growth that occur when you attempt difficult tasks, have to apply yourself
to them, and are exposed to thoughts and ideas from others who understand
the problem. These opportunities are precious, and the posters in this
newsgroup are often part of them. That's why it is essential that responses
to students  should be very carefully considered.)

Posters to this Newsgroup can't assist students to achieve either of the
above goals, by doing any of the following:

1. Doing their homework for them.
2. Showing them how clever we are when they are hopelessy unable to
understand the demonstration. <G>
3. Passing on our personal prejudices and biases to them. (That is why style
wars are so irrelevant...)

Rather, by demonstrating an effective approach to problem solving, directing
their attention to the key areas of the problem and cutting through the
jargon and fuzz, they can be encouraged to arrive at their OWN conclusion.
This is much more valuable for all concerned than simply laying down one
given approach as being the "best" or "only" one.

(Besides, if this approach was good enough for Socrates, it is good enough
for me...<G>)

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T18:46:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f19f7.45920146@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1> <3e8e94d4.11832130@news.optonline.net> <3e8eb224_2@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[5 more quoted lines elided]…
>> to another student request for help.

>If your comment above means that you will continue to contribute, but will
>simply consider your responses, then that's great. If it means you don't
>intend to respond any more, I believe that would be a poor result.

I'm not leaving. 

>You said elsewhere that you haven't been involved in a formal teaching
>environment so it is not surprising that you may not have thought about what
>needs to be achieved with students.

This statement has some truth in it. Because my background is on-the-job
education, I'm inclined to do it for the student the first time.

I wish I'd had models to emulate when I was learning COBOL. The learning process
would have been much faster than trial and error. 

>Rather, by demonstrating an effective approach to problem solving, directing
>their attention to the key areas of the problem and cutting through the
…[5 more quoted lines elided]…
>for me...<G>)

Socrates elicited 'truth' by asking endless questions. The assumption was the
student already knew the answer. What if the student does _not_ know the answer?
I know, prompt him to do experiments which will lead him to discover 'truth' on
his own.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-05T21:58:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f4397_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1> <3e8e94d4.11832130@news.optonline.net> <3e8eb224_2@127.0.0.1> <3e8f19f7.45920146@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e8f19f7.45920146@news.optonline.net...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> >
> >"Robert Wagner" <robert@wagner.net> wrote in message
> Socrates elicited 'truth' by asking endless questions. The assumption was
the
> student already knew the answer. What if the student does _not_ know the
answer?
> I know, prompt him to do experiments which will lead him to discover
'truth' on
> his own.

Truly, Glasshopper, the wisdom concentrated in your last sentence is as the
dewdrop catching the morning light on the lotus blossom.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-06T01:08:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f63d7.64834972@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1> <3e8e94d4.11832130@news.optonline.net> <3e8eb224_2@127.0.0.1> <3e8f19f7.45920146@news.optonline.net> <3e8f4397_1@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>Truly, Glasshopper, the wisdom concentrated in your last sentence is as the
>dewdrop catching the morning light on the lotus blossom.

<laughing and rushing out to rent Crouching Tiger, Hidden Dragon for the third
time>
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-05T16:01:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-3096FD.16013505042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <3e8d63c4_1@127.0.0.1> <3e8e94d4.11832130@news.optonline.net> <3e8eb224_2@127.0.0.1> <3e8f19f7.45920146@news.optonline.net>`

```
In article <3e8f19f7.45920146@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:

> Socrates elicited 'truth' by asking endless questions. The 
> assumption was the student already knew the answer. What 
> if the student does _not_ know the answer?  I know, prompt
> him to do experiments which will lead him to discover 'truth' 
> on his own. 

Often the student does not know enough to ask the question.  They have 
to know something is possible before they can begin to ask how it is 
done.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-04T14:38:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6k5d5$cfo$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net>`

```

On  3-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> I hate reference modification. Either use COBOL parsing via UNSTRING or do it
> all yourself. Yours is a hybrid solution.

Could you explain why you hate reference modification.  Do you think new
programmers should also hate it?
Could you explain why "a hybrid solution" should be avoided?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T18:46:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f114c.43700200@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6k5d5$cfo$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>
>On  3-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
…[4 more quoted lines elided]…
>Could you explain why you hate reference modification.  

Because it reminds me of Basic, and because it's favored by lazy programmers.
You can accomplish the same by defining meaningfully named fields within a group
name. Worst case, you can define the group as an array of bytes. 

>Do you think new programmers should also hate it?

Yes, because it obscures meaning. How am I supposed to know that
'address-3[26:5]' is the ZIP code?

>Could you explain why "a hybrid solution" should be avoided?

When a low-level function must use two or more paradigms, there is something
wrong with the design or the tool.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-06T00:36:42-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304060036.317e930b@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6k5d5$cfo$1@peabody.colorado.edu> <3e8f114c.43700200@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

> Because it reminds me of Basic, and because it's favored by lazy programmers.

Have you a reference that confirms a statistical relationship between
'lazy' and 'use of reference notation' ?  Extra points will be given
if a causal relationship (either way) is established. Or is this just
another of your factoids.

> You can accomplish the same by defining meaningfully named fields within a
> group name. 

No. You are wrong.  This _may_ be true for a very limited sub-set of
usage where the integers are literals, but you may not realise that
variables can be used for both start point and position so that
variable data can be extracted, and this _cannot_ be done with named
fields in a group.

> Worst case, you can define the group as an array of bytes. 

No. You are wrong, that is _not_ the 'worst case', it would only be
'the worst case' for a reference that has a length of 1 character. 
The _actual worse case is to have to redefine the group for every
combination of start point and length. That would be thousands of
redefinitions.

> Yes, because it obscures meaning. How am I supposed to know that
> 'address-3[26:5]' is the ZIP code?

It may be possible to criticise the use of reference notation with
fixed literals, but, if you read the manual, you will find that it is
rather more flexible than that and rather more difficult to emulate
appropriate usage with fixed position variables.
 
> >Could you explain why "a hybrid solution" should be avoided?
> 
> When a low-level function must use two or more paradigms, there is something
> wrong with the design or the tool.

So if I have use a spanner _and_ a screwdriver to tighten a machine
screw then there is something wrong with the design of the
screw-driver ? Or was that the design of the screw ?

Personally I find that I choose from all the tools that I have
available so that I get the most appropriate without having to abide
by some silly aphorisms that have been made up to support some
unfounded prejudice.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-06T16:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e904b2a.124063465@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6k5d5$cfo$1@peabody.colorado.edu> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 

>> You can accomplish the same by defining meaningfully named fields within a
>> group name. 
…[5 more quoted lines elided]…
>fields in a group.

In my limited, sheltered experience with production COBOL, _all_ reference
modifiers were literals. It was used on fixed-length, fixed-format fields
because the programmer was too lazy to sub-define the field's components. 

>It may be possible to criticise the use of reference notation with
>fixed literals, but, if you read the manual, you will find that it is
>rather more flexible than that and rather more difficult to emulate
>appropriate usage with fixed position variables.

The manual says UNSTRING ... WITH POINTER accomplishes the same. You even
provided an example. If you want to pick off five bytes, unstring into a five
byte field followed by add 5 to pointer. 

>So if I have use a spanner _and_ a screwdriver to tighten a machine
>screw then there is something wrong with the design of the
>screw-driver ? Or was that the design of the screw ?

A torque-limited spanner could have done the job in one pass.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-07T19:28:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6pv5i$s1n$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net>`

```
Robert Wagner wrote:

> The manual says UNSTRING ... WITH POINTER accomplishes the same. You even
> provided an example. 

There is a subset of problems which can be done in alternate ways.  In 
other cases one mechanism is more suitable than others.  That is: UNSTRING 
could do the same thing in that particular case, this does not mean they 
can 'accomplish the same thing' in all cases.

> If you want to pick off five bytes, unstring into a
> five byte field 

It may not be 5 bytes that are required.  ZIP codes here are 4, in UK they 
are longer.  

> followed by add 5 to pointer.

Read the manual again, the pointer is updated by the UNSTRING.

But _now_ you are using _two_ different statements: an UNSTRING and an ADD, 
you criticised solutions that used two different things.
 
>>So if I have use a spanner _and_ a screwdriver to tighten a machine
>>screw then there is something wrong with the design of the
>>screw-driver ? Or was that the design of the screw ?
> 
> A torque-limited spanner could have done the job in one pass.

No. I had said 'machine screw' specifically, perhaps you are unaware of 
such subtlties (clue: it only resembles a bolt).

There was also no requirement in the specification for a specific torque so 
a torque-limited spanner may be over-specing the solution.
```

###### ↳ ↳ ↳ Reference Modification (was: Beginner's Question

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-06T15:00:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6q10d$tvi$1@slb1.atl.mindspring.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz>`

```
(agreeing with Richard - but expanding a bit)

Reference modification may use an ARITHMETIC EXPRESSION as either the
starting point, the length, or both.

Unstring may use a POINTER (set via an arithmetic expression) as the
starting point - but has no way to "dynamically" set the length of what is
"processed".

Arithmetic expression MAY include intrinsic functions (among other things).

All of this boils down the fact that UNSTRING is a powerful and useful tool
for "parsing" an input field. Reference modification is a useful and
powerful tool for accessing a "dynamically determined" portion of a field.
Either method may be used for some cases - one or the other is best for some
other cases.

COBOL (and probably most other "robust" programming languages) has a
multitude of ways to do the same task.  In some - but certainly NOT ALL -
cases, one method may be the "best" either for run-time efficiency or
self-documentation.  However, just because a specific feature is best for
solving one problem, it does NOT follow that the same feature is best for
solving some other problem.

Learning (and understanding) the "new" (well new in 1985 or 1989 or later -
depending on the specific compiler vendor) new features of the language may
WELL provide a "better" way to do a task that used to be best done by
another means.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T02:49:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e90a401.1578481@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>Robert Wagner wrote:
>
…[6 more quoted lines elided]…
>can 'accomplish the same thing' in all cases.

Yes it can. The generalized equivalent of 'move a-string(p:n) to foo'  is: 

01  p pic 999.
01  n pic 99.
01  a-pointer  pic 999.
01  a-string    pic x512). 
01  foo-length pic 99.
01  foo.
     05  filler occurs 0 to 99 depending on foo-length pic x.

move n to foo-length
move p to a-pointer
unstring a-string delimited by high-value into foo with pointer a-pointer
add n to p

>> If you want to pick off five bytes, unstring into a
>> five byte field 
>
>It may not be 5 bytes that are required.  ZIP codes here are 4, in UK they 
>are longer.

In that case, you're looking for a delimiter, so you do need UNSTRING.

>> followed by add 5 to pointer.
>
>Read the manual again, the pointer is updated by the UNSTRING.

I know. Make it a disposible field, as I did above. 

>But _now_ you are using _two_ different statements: an UNSTRING and an ADD, 
>you criticised solutions that used two different things.

I criticized programs using two string-handling facilities. No program except
the most trivial can be written with a single verb, but it is reasonable to
expect a family of string functions to be complete. In OO terms, class.String
should not inherit from disparate sources. 

>>>So if I have use a spanner _and_ a screwdriver to tighten a machine
>>>screw then there is something wrong with the design of the
…[8 more quoted lines elided]…
>a torque-limited spanner may be over-specing the solution.

The reason you used a screwdriver was to avoid over tightening the screw and
thereby stripping the nut. By doing so, you created an ad hoc torque
specification. 
>
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-04-06T23:53:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0304062253.5d61a9f6@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz> <3e90a401.1578481@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote 

>>could do the same thing in that particular case, this does not mean
they
>>can 'accomplish the same thing' in all cases.

> Yes it can. The generalized equivalent of 'move a-string(p:n) to foo'  is: 

That is one particular use of reference notation.  One that can mostly
be emulated by UNSTRING.

However reference notation can also be used as a receiving field.

      MOVE ALL "*"    TO Chart-Line(start-day: day-count)
 
Tell me how you can do this with UNSTRING.

Of course you can contrive to do it with STRING, but like your
UNSTRING example it takes several statements.  You could also do it
with a PERFORM loop.

But then you can also do a multiply by using a PERFORM loop and and a
add so why should there be a separate MULTIPLY statement ?

> 01  foo.
>      05  filler occurs 0 to 99 depending on foo-length pic x.

Variable length is a second string handling mechanism, just when you
were saying that only one should be required.

> unstring a-string delimited by high-value into foo with pointer a-pointer
> add n to p

And if a-string contains a high-value ?

> >No. I had said 'machine screw' specifically, perhaps you are unaware of 
> >such subtlties (clue: it only resembles a bolt).
…[6 more quoted lines elided]…
> specification. 

No. Wrong. The reason I used a screwdriver is that a 'machine screw'
has a slotted head.

You really do struggle to avoid looking like a complete prat.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T22:31:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e91c65a.75919180@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz> <3e90a401.1578481@news.optonline.net> <217e491a.0304062253.5d61a9f6@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert@wagner.net (Robert Wagner) wrote 
>
…[16 more quoted lines elided]…
>UNSTRING example it takes several statements.  

Do it with STRING. That's not contrived, it is the corrolary of the other case.
Here you're inserting something into a string rather than extracting from it. 

>You could also do it with a PERFORM loop.

Personally, that would be my choice. But I'm advocating it here.

>But then you can also do a multiply by using a PERFORM loop and and a
>add so why should there be a separate MULTIPLY statement ?

In specialized cases, you must. For instance, when precision is larger than the
COBOL's maximum. Everyone should write a four-function calculator that operates
on 1,000 digit numbers .. as a learning experience. 

>> 01  foo.
>>      05  filler occurs 0 to 99 depending on foo-length pic x.
>
>Variable length is a second string handling mechanism, just when you
>were saying that only one should be required.

It is not a 'mechanism', it's a data type. I didn't say anything about your
code's use of fixed length strings. 

>> unstring a-string delimited by high-value into foo with pointer a-pointer
>> add n to p
>
>And if a-string contains a high-value ?

It doesn't .. guaranteed. Watch .. I'll type alt-255 .. high-value = "_". See?
It was translated to underbar. 

>> >No. I had said 'machine screw' specifically, perhaps you are unaware of 
>> >such subtlties (clue: it only resembles a bolt).
…[11 more quoted lines elided]…
>You really do struggle to avoid looking like a complete prat.

Inside your PC are many screws which can be driven by either a nut driver or a
Phillips screwdriver. They are called "hex head machine screws" (they are not
sheet metal screws nor bolts). You said you started with a spanner and finished
with a screwdriver, so you must have been referring to that type of screw. A
slotted head screw cannot be started with a spanner.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-08T14:38:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6umtm$gd1$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz> <3e90a401.1578481@news.optonline.net> <217e491a.0304062253.5d61a9f6@posting.google.com> <3e91c65a.75919180@news.optonline.net>`

```

On  7-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> In specialized cases, you must. For instance, when precision is larger than
> the
> COBOL's maximum. Everyone should write a four-function calculator that
> operates
> on 1,000 digit numbers .. as a learning experience.

I did that once - it was fun.

Another exercise I did once was using DCL (DEC Control Language), I wrote an
arithmetic processor using left and right bit shifting to do its arithmetic.   I
was monitoring jobs and had time to kill.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-07T08:02:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s3u8$2tuf$1@si05.rsvl.unisys.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz> <3e90a401.1578481@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e90a401.1578481@news.optonline.net...

> Yes it can. The generalized equivalent of 'move a-string(p:n) to foo'  is:
>
…[11 more quoted lines elided]…
> add n to p

Since I don't know what "generalized equivalent" means I'm not sure what the
assertion is here.  But it is not at all clear to me that the former and the
latter sequences would unconditionally generate execution-time code of
identical efficiency and thus of identical usefulness in all circumstances.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T22:31:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e91ce40.77941147@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz> <3e90a401.1578481@news.optonline.net> <b6s3u8$2tuf$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[20 more quoted lines elided]…
>identical efficiency and thus of identical usefulness in all circumstances.

Every programming book I've read (both of them) advises against
'pre-optimization'. They say write the code for clarity and style. If code
_later_ is found to be a performance drain, _then_ optimize it. 

Has that changed?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-07T16:07:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6t0ak$fva$1@si05.rsvl.unisys.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz> <3e90a401.1578481@news.optonline.net> <b6s3u8$2tuf$1@si05.rsvl.unisys.com> <3e91ce40.77941147@news.optonline.net>`

```
Robert Wagner wrote:

> >> Yes it can. The generalized equivalent of 'move a-string(p:n) to foo'
is:
> >>
> >> 01  p pic 999.
…[9 more quoted lines elided]…
> >> unstring a-string delimited by high-value into foo with pointer
a-pointer
> >> add n to p

I replied:

> >Since I don't know what "generalized equivalent" means I'm not sure what
the
> >assertion is here.  But it is not at all clear to me that the former and
the
> >latter sequences would unconditionally generate execution-time code of
> >identical efficiency and thus of identical usefulness in all
circumstances.

Robert Wagner responded:

> Every programming book I've read (both of them) advises against
> 'pre-optimization'. They say write the code for clarity and style. If code
> _later_ is found to be a performance drain, _then_ optimize it.

It's not obvious to me which you regard as "clear".  You've already
indicated elsewhere your dislike for UNSTRING, and you've also demonstrated
some misunderstandings regarding reference modification.

In the implementation with which I'm familiar -- which allows reference
modification, UNSTRING and the "COBOL68-style" step-through-a-byte-at-a-time
method -- the reference modification variant of this code is by far the most
efficient.  It's even more efficient if the variables p and n were described
as BINARY instead of DISPLAY.    UNSTRING is improved somewhat if a-pointer
were also in BINARY, but not enough to make comparison with reference
modification worthwhile.  I haven't bothered to hard-code the step-through
method.  There are cases in which UNSTRING really shines in our
implementation; this isn't one of them.

As for me, in this instance, reference modification works, reference
modification is clear, reference modification is fast, reference
modification's been around officially for nigh onto twenty years now.  I
don't see all that much reason to avoid using it; I find this *particular*
case of UNSTRING considerably less clear.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-08T23:27:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6t1gp$bji$1@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e90a401.1578481@news.optonline.net> <b6s3u8$2tuf$1@si05.rsvl.unisys.com> <3e91ce40.77941147@news.optonline.net>`

```
Robert Wagner wrote:


A:
>>> move a-string(p:n)    to foo

B:
>>> move n to foo-length
>>> move p to a-pointer
>>> unstring a-string delimited by high-value into foo with pointer
>>> a-pointer 
>>> add n to p

> They say write the code for clarity and style. 

Which is exactly why I would use A: in preference to B: other things being 
equal.

That it also happens to be more efficient would be a bonus.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-08T14:42:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6un4i$gjj$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6pv5i$s1n$1@aklobs.kc.net.nz> <3e90a401.1578481@news.optonline.net> <b6s3u8$2tuf$1@si05.rsvl.unisys.com> <3e91ce40.77941147@news.optonline.net>`

```

On  7-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> Every programming book I've read (both of them) advises against
> 'pre-optimization'. They say write the code for clarity and style. If code
> _later_ is found to be a performance drain, _then_ optimize it.
>
> Has that changed?

Has what changed?

I have read different advice in different books.    When optimization has come
up, they generally stress the following:

1.  Know your data.
2.  Make your data smaller sooner rather than later.   (extract just the amount
of records you intend to work with).
3.  Don't process a million times an initialization that only needs to be
initialized once.

An optimizing compiler might take care of 3.   It isn't likely to take care of 1
& 2.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-07T15:13:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s4i4$8pf$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6k5d5$cfo$1@peabody.colorado.edu> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net>`

```

On  6-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> In my limited, sheltered experience with production COBOL, _all_ reference
> modifiers were literals. It was used on fixed-length, fixed-format fields
> because the programmer was too lazy to sub-define the field's components.

The only time I have seen this was in cases where a DBA would be needed to
sub-define the field's components.

Most times I have seen it fits into this thread - as an alternative to UNSTRING.
  That IS what this thread is about.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 9)_

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-07T17:17:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E91F90A.1060902@Knology.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6k5d5$cfo$1@peabody.colorado.edu> <3e8f114c.43700200@news.optonline.net> <217e491a.0304060036.317e930b@posting.google.com> <3e904b2a.124063465@news.optonline.net> <b6s4i4$8pf$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
>>In my limited, sheltered experience with production COBOL, _all_ reference
…[8 more quoted lines elided]…
>   That IS what this thread is about.

I recently did some work on the system-level "traffic" logic.  The 
output line was redefined into an indexed table of 80 Pic X(01) 
occurrences.  The output area of 2200 characters was similarly 
redefined.  There were loops that stepped through, character by 
character, setting the index down by one until it found the first 
non-space character.  Then, it moved from the first through to that one, 
character by character, moving the traffic line to the output message.

I rewrote this logic to search backward through the line using reference 
modification.  Then, when I find the first non-space character, I can 
move the entire chunk to the next chunk in the output message area, add 
the length to the index of the output message area, and continue.  Many 
fewer instructions, and code that isn't continually doing Set commands.

So, I would beg to differ with the argument that reference modification 
is "bad" or "wrong".  However, I agree that it should not be used as a 
substitute for predefined, meaningful names.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-07T15:11:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s4e6$8p9$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <217e491a.0304031111.2d0a79e2@posting.google.com> <3e8cd754.233770482@news.optonline.net> <b6k5d5$cfo$1@peabody.colorado.edu> <3e8f114c.43700200@news.optonline.net>`

```

On  5-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >Do you think new programmers should also hate it?
>
> Yes, because it obscures meaning. How am I supposed to know that
> 'address-3[26:5]' is the ZIP code?

We were discussing reference modification as an alternative to unstring.   If
you know where the zip code is, you won't use either one.
```

##### ↳ ↳ Re: Beginner's Question

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-04T11:46:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<-sqcnbcp87NiWRCjXTWc2Q@giganews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e8b88b4.148093455@news.optonline.net...
> auburn82@iolfree.ie (Auburn) wrote:
>
…[23 more quoted lines elided]…
> embedded spaces, which will be enclosed in quotes. UNSTRING cannot
correctly
> parse quoted strings. You'll have to do it yourself.

Auburn,

Some (one) will tell you to avoid UNSTRING inasmuch as it cannot parse
imbedded blanks in a quoted string. UNSTRING can't but you sure can. You
just have to use a double-secret-unstring. Here's how.

(convert imbedded spaces within quotes to LOW-VALUES*)
(convert all quotes to SPACES)

MOVE 1 TO STR-PTR.
MOVE SPACE TO MYWORDS.
PERFORM VARYING INDX FROM 1 BY 1
    UNTIL INDX > MAX-WORDS
    UNSTRING MY-REC DELIMITED BY ALL '  ' INTO
         MY-WORD(INDX) WITH POINTER STR-PTR
END-PERFORM
INSPECT MYWORDS REPLACING ALL LOW-VALUES BY ' '.

Jerry Mouse

Notes:
*SPACE to LOW-VALUES within quotes

MOVE 1 TO FLIP.
PERFORM VARYING INDX FROM 1 BY 1 UNTIL INDX > REC-LEN
   IF REC(INDX:1) = '"'
      COMPUTE FLIP = 3 - FLIP
      END-IF
   IF FLIP = 2
      AND REC(INDX:1) = SPACE
      MOVE LOW-VALUES TO REC(INDX:1)
      END-IF
END-PERFORM.
```

###### ↳ ↳ ↳ Re: Beginner's Question

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T18:46:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f1390.44281116@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

>Some (one) will tell you to avoid UNSTRING inasmuch as it cannot parse
>imbedded blanks in a quoted string. UNSTRING can't but you sure can. You
…[28 more quoted lines elided]…
>END-PERFORM.

Better yet, parse the thing while stepping through the bytes and forget about
UNSTRING and INSPECT. 

I understand this was an attempt at programming humor. I would have written "3 -
FLIP" as "0 - FLIP" or, better yet, as an XOR.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-05T15:23:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KoycndZi-8Oh1BKjXTWcpg@giganews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net>
>
> I understand this was an attempt at programming humor. I would have
written "3 -
> FLIP" as "0 - FLIP" or, better yet, as an XOR.

No humor was intended.

It's a programming artifact of mine left from the days of switching tape
drives (which were numbered). Input was on drive 1 & 2 (hence the 3), output
was on 3 & 4 (using a 7).

Every time I see that old code, I long to return to the days of illiterate
bosses, malicious operators, pomposity, and people generally insane,
equipped with my new skills and attitudes.

For example, today I carry a gun.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-06T01:08:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f6689.65524857@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

>
>"Robert Wagner" <robert@wagner.net>
…[5 more quoted lines elided]…
>No humor was intended.

Good. Don't give up your day job. 

>It's a programming artifact of mine left from the days of switching tape
>drives (which were numbered). Input was on drive 1 & 2 (hence the 3), output
…[4 more quoted lines elided]…
>equipped with my new skills and attitudes.

Technology may change but human nature doesn't. People like that are still our
colleagues. For documentation, see Dilbert. 

>For example, today I carry a gun.

In case you find the world overwhelming? In case you are overcome with ennui?
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-04-05T20:21:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OBWdnTvDcrqWEhKjXTWJjA@giganews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net>
>
> Technology may change but human nature doesn't. People like that are still
our
> colleagues. For documentation, see Dilbert.

Right. It finally dawned on me that as long as I was cursed to work for a
fool, I might as well be self employed.

>
> >For example, today I carry a gun.
>
> In case you find the world overwhelming? In case you are overcome with
ennui?

Of course not, silly person. I carry a gun in case I run into someone who
needs killing. Or if I encounter someone who prattles on about full stops,
ANSI standards, or the good old days of programming a reproducing gang punch
machine.... but that's pretty much the same thing.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-06T04:56:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8fb209.84856087@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote:

> Or if I encounter someone who prattles on about full stops,
>ANSI standards, or the good old days of programming a reproducing gang punch
>machine.... but that's pretty much the same thing.

What would you like to know about the 519 reproducing gangpunch? I used to be an
ace at wiring its boards. 

I was in USMC Special Ops, briefly attached to SEAL team, handled every kind of
weapon imaginable. Today I don't carry a gun and think they shouldn't be legal
for civilians. I've been shot at one too many times by redneck assholes. The
clincher was from five feet away (passenger in a pickup vs. me on a bicycle). I
don't know how he missed. Then the driver tried to run over a six year-old girl
riding to school. When I tried to get justice, I was told juveniles are immune. 

Given that the system won't protect us, the only solution is take guns away from
idiot abusers. There is no reason civilians NEED guns. They say defense. For
every successful defense, there are ten 'crimes of passion' in which people
shoot their neighbor, wife or drinking buddy .. or those who prattle on about
ANSI standards or tab machines. 
 
The Second Amendment talks about "militia". I have no problem with State or
National Guard using weapons. Joe sixpack is not a member of the militia.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-06T21:21:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6qjrl$nt$1@panix1.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net>`

```
In article <3e8fb209.84856087@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:

[snip]

>Joe sixpack is not a member of the militia. 


Mr Wagner, *you* may not be a member of the militia... but 'Joe sixpack', 
if he is an able-bodied male between the ages of 17 and 45, most certainly 
is.

DD
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T03:55:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e90f3b4.21984492@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net> <b6qjrl$nt$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e8fb209.84856087@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[8 more quoted lines elided]…
>is.

Now wonderful .. a 'gun nut' argument in CLC. 

You know, Logic is the basic raw material of programming. One would expect
people who've practiced it professionally all their lives would have higher
skills than the unwashed masses, who read tabloids on their way to work. One
would hope they could make life decisions based on reason rather than emotion. 

Alas, none of these expectations holds true. We're back to square zero.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-07T13:16:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e916c10_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net> <b6qjrl$nt$1@panix1.panix.com> <3e90f3b4.21984492@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e90f3b4.21984492@news.optonline.net...
> docdwarf@panix.com wrote:
>
…[9 more quoted lines elided]…
> >if he is an able-bodied male between the ages of 17 and 45, most
certainly
> >is.
>
…[3 more quoted lines elided]…
> people who've practiced it professionally all their lives would have
higher
> skills than the unwashed masses, who read tabloids on their way to work.

I protest strongly!!! (As both a regular tabloid reader, bather, and daily
showerer).<G>

Please desist from these stereotypical, generalized, derogatory assertions,
for which there is no basis in fact.

Pete. (who lives comfortably on square zero...)




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-07T08:57:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6rskk$re7$1@panix1.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8fb209.84856087@news.optonline.net> <b6qjrl$nt$1@panix1.panix.com> <3e90f3b4.21984492@news.optonline.net>`

```
In article <3e90f3b4.21984492@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[12 more quoted lines elided]…
>Now wonderful .. a 'gun nut' argument in CLC. 

Mr Wagner, please read carefully.  No argument was presented, you were 
given a statement of fact.

>
>You know, Logic is the basic raw material of programming. One would expect
>people who've practiced it professionally all their lives would have higher
>skills than the unwashed masses, who read tabloids on their way to work. One
>would hope they could make life decisions based on reason rather than emotion. 

It is the experience of some, Mr Wagner, that the 'unwashed masses' refer 
to facts counter to their assertions as '-nut arguments'... and it is the 
experience of others that referring to 'masses' of any kind is a way to 
dodge an obvious demonstration of error by attempting to play upon class 
differences.

>
>Alas, none of these expectations holds true. We're back to square zero.

Blessed are those who expect nothing, Mr Wagner, as they are rarely 
disappointed.

Now, back to matters of fact... Mr Wagner, *you* may not be a member of
the militia... but 'Joe sixpack', if he is an able-bodied male between the
ages of 17 and 45, most certainly is.

DD
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T22:31:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e91d373.79272008@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8fb209.84856087@news.optonline.net> <b6qjrl$nt$1@panix1.panix.com> <3e90f3b4.21984492@news.optonline.net> <b6rskk$re7$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <3e90f3b4.21984492@news.optonline.net>,
>Robert Wagner <robert@wagner.net> wrote:
…[17 more quoted lines elided]…
>given a statement of fact.

You are referring to 10 USC 13.311, primarily, and US Constitution Art. 1, s. 8,
14. If it was an undisputable fact, there would not be endless debate (in more
appropriate forums) over what it means. For an unbiased analysis see:

http://www.lectlaw.com/def2/m110.htm

.. which says, in part:

MILITIA - The military force of the nation, consisting of citizens CALLED FORTH
[emphasis added]  to execute the laws of the Union, suppress insurrection and
repel invasion.

Under the clauses of the constitution, the following points have been decided.

If congress had chosen, they might by law, have considered a militia man, called
into the service ot the United States, as being, from the time of such call,
constructively in that service, though not actually so, although he should not
appear at the place of rendezvous. But they have not so considered him, in the
acts of congress, till after his appearance at the place of rendezvous; previous
to that, a fine was to be paid for the delinquency in not obeying the call,
which fine was deemed an equivalent for his services, and an atonement for
disobedience.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-07T20:28:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v945728mvmaeff@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8fb209.84856087@news.optonline.net> <b6qjrl$nt$1@panix1.panix.com> <3e90f3b4.21984492@news.optonline.net> <b6rskk$re7$1@panix1.panix.com> <3e91d373.79272008@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e91d373.79272008@news.optonline.net...
> docdwarf@panix.com wrote:
>
…[12 more quoted lines elided]…
> >>>Mr Wagner, *you* may not be a member of the militia... but 'Joe
sixpack',
> >>>if he is an able-bodied male between the ages of 17 and 45, most
certainly
> >>>is.
> >>
…[5 more quoted lines elided]…
> You are referring to 10 USC 13.311, primarily, and US Constitution Art. 1,
s. 8,
> 14. If it was an undisputable fact, there would not be endless debate (in
more
> appropriate forums) over what it means. For an unbiased analysis see:
>
…[4 more quoted lines elided]…
> MILITIA - The military force of the nation, consisting of citizens CALLED
FORTH
> [emphasis added]  to execute the laws of the Union, suppress insurrection
and
> repel invasion.

First, the militia clauses are Article I, Section 8, Clauses 15 and 16.
See "The Constitution of the United States of America: Analysis
and Interpretation" available at
< http://www.access.gpo.gov/congress/senate/constitution/toc.html >
Download the PDF document: Article I. Legislative Department.

In that document, page 278,

"Under the National Defense Act of 1916, the militia, which
hitherto had been an almost purely state institution, was brought
under the control of the National Government. The term 'militia
of the United States' was defined to comprehend 'all able-bodied
male citizens of the United States and all other able-bodied males
who have . . . declared their intention to become citizens of the
United States,' between the ages of eighteen and forty-five."

It follows that the definition, you supplied, is not in agreement with
the National Defense Act of 1916, or its interpretation under the
Constitution, whichever applies.

You might also find "Second Amendment - Bearing Arms"
from that same site, to be of interest.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-07T22:05:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6taom$89s$1@panix1.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e90f3b4.21984492@news.optonline.net> <b6rskk$re7$1@panix1.panix.com> <3e91d373.79272008@news.optonline.net>`

```
In article <3e91d373.79272008@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>docdwarf@panix.com wrote:
>
…[22 more quoted lines elided]…
>14.

Very good, Mr Wagner.

>If it was an undisputable fact, there would not be endless debate (in more
>appropriate forums) over what it means.

That just might possibly be one of the reasons why I referred to it as 
'fact', Mr Wagner, not as 'undisputed fact'.  It is a matter of law; such 
things are, as many human constructs, malleable.

> For an unbiased analysis see:

It might be wise, Mr Wagner - to say nothing of 'honest' or 'avoiding
hyprocisy' - , to follow your own advice and keep such things for what you
see to be 'more appropriate forums'.

DD
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 13)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-08T07:42:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e9275eb.120870693@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e90f3b4.21984492@news.optonline.net> <b6rskk$re7$1@panix1.panix.com> <3e91d373.79272008@news.optonline.net> <b6taom$89s$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:


>It might be wise, Mr Wagner - to say nothing of 'honest' or 'avoiding
>hyprocisy' - , to follow your own advice and keep such things for what you
>see to be 'more appropriate forums'.

Fair enough.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-07T15:27:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s5d1$963$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net> <b6qjrl$nt$1@panix1.panix.com> <3e90f3b4.21984492@news.optonline.net>`

```

On  6-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >Mr Wagner, *you* may not be a member of the militia... but 'Joe sixpack',
> >if he is an able-bodied male between the ages of 17 and 45, most certainly
> >is.
>
> Now wonderful .. a 'gun nut' argument in CLC.

Either that or he's a believer in rule of law.   That's not a bad characteristic
for a programmer to have.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-07T15:25:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s59m$94j$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net>`

```

On  5-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> The Second Amendment talks about "militia". I have no problem with State or
> National Guard using weapons. Joe sixpack is not a member of the militia.

It is pretty easy to parse out the meaning of:

A well regulated Militia, being necessary to the security of a free State, the
right of the people to keep and bear Arms, shall not be infringed.


(I could care less about guns, but care deeply about the Constitution)
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T22:31:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e91f897.88781712@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net> <b6s59m$94j$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>On  5-Apr-2003, robert@wagner.net (Robert Wagner) wrote:
>
…[6 more quoted lines elided]…
>right of the people to keep and bear Arms, shall not be infringed.

Then why is it illegal for me to own a hand grenade, keep a bazooka under my
bed, or make a sawed-off shotgun? All three are 'Arms' that could reasonably be
used by a militia. 

No, it isn't easy to ascertain what the Founding Fathers meant, or guessed might
happen in the future. In some cases, the Supreme court has permitted
introduction of their unofficial writing in attempting to figure it out. Such
vagary is a poor basis for a legal system.

>(I could care less about guns, but care deeply about the Constitution)

So do I, and I'm saddened to see it raped by politicians responding to the issue
de jour. The Tenth Amendment says the Federal government has no authority except
that explicitly granted to it in the Constitution. The Constitution is silent on
Education, Public Health and Transportation (excepting interstate commerce). So
why do we have massive Federal bureaucracies regulating all three? These are
more important issues than Joe sixpack's 'right' to own a Saturday Night Special
with no conceivable military usefulness. Sadly, nobody but 'gun nuts' seems to
care about defending the Constitution.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-07T20:19:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-24CB6C.20192107042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net> <b6s59m$94j$1@peabody.colorado.edu> <3e91f897.88781712@news.optonline.net>`

```
In article <3e91f897.88781712@news.optonline.net>,
 robert@wagner.net (Robert Wagner) wrote:

> Then why is it illegal for me to own a hand grenade, keep a bazooka under my
> bed, or make a sawed-off shotgun? All three are 'Arms' that could reasonably 
> be used by a militia. 

Because a bunch of Stalinist apologists, fellow travelers and useful 
idiots have spent the last 6 decades violating your rights, convincing 
you that it needs to be that way, and making you like having them 
violated.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-07T22:09:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6tb08$a7a$1@panix1.panix.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8fb209.84856087@news.optonline.net> <b6s59m$94j$1@peabody.colorado.edu> <3e91f897.88781712@news.optonline.net>`

```
In article <3e91f897.88781712@news.optonline.net>,
Robert Wagner <robert@wagner.net> wrote:
>"Howard Brazee" <howard@brazee.net> wrote:
>
…[12 more quoted lines elided]…
>used by a militia. 

Mr Wagner, didn't you make some manner of noise about 'more apropriate 
forums'?

DD
```

###### ↳ ↳ ↳ [OT - US] The Tenth Amendment (was: Re: Beginner's Question)

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-04-07T22:44:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v94d7secbnru71@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net> <b6s59m$94j$1@peabody.colorado.edu> <3e91f897.88781712@news.optonline.net>`

```

Robert Wagner <robert@wagner.net> wrote in message
news:3e91f897.88781712@news.optonline.net...
[snip]
> No, it isn't easy to ascertain what the Founding Fathers meant, or guessed
might
> happen in the future. In some cases, the Supreme court has permitted
> introduction of their unofficial writing in attempting to figure it out.
Such
> vagary is a poor basis for a legal system.
>
[snip
>
> [...[ The Tenth Amendment says the Federal government has no authority
except
> that explicitly granted to it in the Constitution.

See "The Constitution of the United States of America: Analysis
and Interpretation" available at
< http://www.access.gpo.gov/congress/senate/constitution/toc.html >
Download the PDF document: Tenth Amendment - Reserved Powers.

That's not quite what it says and was an issue in United States
v. Sprague (1931) and United States v. Darby (1941) where the
Supreme Court, in my opinion, erred.

The Tenth Amendment says "The powers not delegated to the
United States by the Constitution, nor prohibited by it to the
States, are reserved to the States respectively, or to the people."

To me, the following statement, from the referenced document,
seems rather odd, "That this provision was not conceived to be
a yardstick for measuring the powers granted to the Federal
Government or reserved to the States was firmly settled by the
refusal of both Houses of Congress to insert the word 'expressly'
before the word 'delegated,' and ...."

It is apparent, from its relation to the Declaration of Independence,
that the Bill of Rights (the first ten amendments) was intended
to prevent "... a long train of abuses and usurpations ..."; that the
first eight amendments addressed specific abuses, the ninth
amendment was a general prohibition against abuses, and the
tenth amendment was a general prohibition against usurpation.

The greatest threat to a free people does not come from invasion
or insurrection; but from the steady erosion of rights and powers
by a "beneficent" government.

> The Constitution is silent on
> Education, Public Health and Transportation (excepting interstate
commerce). So
> why do we have massive Federal bureaucracies regulating all three?

The Supreme Court has yet to realize that Article VI, Clause 2,
"This Constitution, and the Laws of the United States which
shall be made in Pursuance thereof; and ... shall be the supreme
Law of the Land; ..." means that laws not in pursuance of the
Constitution are not the supreme law of the land and therefore
have no standing; and that pursuance of the constitution means
that laws exercising powers not expressly delegated and laws
in conflict with the Bill of Rights must be prohibited.

See the PDF document "Article VI. Prior Debts, National
Supremacy, Oaths of Office" at the referenced site, for some
comments that begin to approach this opinion.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-08T14:52:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6unnu$gv2$1@peabody.colorado.edu>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com> <3e8fb209.84856087@news.optonline.net> <b6s59m$94j$1@peabody.colorado.edu> <3e91f897.88781712@news.optonline.net>`

```

On  7-Apr-2003, robert@wagner.net (Robert Wagner) wrote:

> >A well regulated Militia, being necessary to the security of a free State,
> >the
…[4 more quoted lines elided]…
> be used by a militia.

Because the law isn't like programming.   What we say isn't always what we get.
 None of the Constitution is enforced absolutely.   The Constitution also
doesn't give exceptions to say that we can't yell "Fire" in a crowded theater.

I don't know of anybody who wants to allow felons in prison to have their 2nd
amendment right.   But in general, I prefer us to get as close to the
Constitution as we practically can.   And don't make the exceptions by
pretending that it doesn't say what it means.

But I don't have the power to enforce this wish.


> >(I could care less about guns, but care deeply about the Constitution)
>
…[3 more quoted lines elided]…
> except that explicitly granted to it in the Constitution.

The 9th and 10th amendments are virtually ignored.   The federal system should
be very useful - with some states profiting by giving disenfranchised people
rights earlier than other states for instance - or by allowing a state to have,
say state supported medicine - and letting the rest of us observe this
experiment and decide whether to emulate it.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-06T21:39:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e90909d_1@127.0.0.1>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <OBWdnTvDcrqWEhKjXTWJjA@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message
news:OBWdnTvDcrqWEhKjXTWJjA@giganews.com...
>
> "Robert Wagner" <robert@wagner.net>
> >
> > Technology may change but human nature doesn't. People like that are
still
> our
> > colleagues. For documentation, see Dilbert.
…[3 more quoted lines elided]…
>
I like that JerryMouse! Hope you don't mind if I use it...<G>

The best instance of justifying self-employment that I can recall was some
years ago when I managed a project for an upper class twit who used the old
school tie to obtain contracts, which he then sub-let to people who could
actually do the work.
(Fortunately, his breed in Modern Britain is a dying one, and in the 20-odd
years I have been working in the UK I have been pleased to see the slow
erosion of Management attained by Class rather than ability...)

Anyway, with a team of dedicated people we delivered his project and he duly
paid us and took the credit. He than asked me if I would consider working
for him as a permanent employee. I politely declined, explaining that being
a free lance suited my temperament, personality, and life-style. He was a
bit miffed and suggested that I would never become much unless I formed
alliances with people who could open doors...(He might have been right, but
the point he missed was...I don't care <G>)

Some years later I happened to be having a few drinks with some friends in a
North London pub when said Impresario walks in with a few other people who
appeared to be of similar ilk.

In an effort to embarrass me he called in a loud voice: "Hello, Peter! Still
a one-man-band are we?"

In one of those rare moments when the brain functions perfectly under
stress, I replied: "Actually, Ron, I can't get by with any less..."  My
friends fell about, and he walked off with his mates, which was exactly the
result I wanted. I've never seen him since.

But I reckon your reason for being self-employed would have been just as
effective.

Pete.




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-07T05:12:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6od1b$oq$2@aklobs.kc.net.nz>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net>`

```
Robert Wagner wrote:

> Technology may change but human nature doesn't. People like that are still
> our colleagues. For documentation, see Dilbert.

I hate to disillusion you, but the X-Files isn't a documentary, and Dilbert 
isn't a real person (clue: he's a drawing).
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-04-06T14:38:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gZWja.19509$vI3.587483@twister.austin.rr.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <b6od1b$oq$2@aklobs.kc.net.nz>`

```
Oh! To the contrary!

Dilbert is a mirror of actual life. I can prive that from actual personal anecdotes!

-Paul

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message news:b6od1b$oq$2@aklobs.kc.net.nz...
> Robert Wagner wrote:
>
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-06T16:54:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-7A0B12.16542906042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net>`

```

"JerryMouse" and "Robert Wagner" wrote:

JM: For example, today I carry a gun.

RW: In case you find the world overwhelming? In case you are overcome 
with ennui?


There are very few problems that an AK-47 and a rooftop will not cure...
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T02:49:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e90b066.4752303@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <KoycndZi-8Oh1BKjXTWcpg@giganews.com> <3e8f6689.65524857@news.optonline.net> <joe_zitzelberger-7A0B12.16542906042003@corp.supernews.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

>
>"JerryMouse" and "Robert Wagner" wrote:
…[6 more quoted lines elided]…
>There are very few problems that an AK-47 and a rooftop will not cure...

In the Marine Corps they say, "There are few problems that superior tactical
firrepower will not overcome." 

You gotta use the right tool for the job. In my specialty, information
gathering, we used small, full-auto weapons with accuracy no better than a
thrown rock. Their function was to make a lot of noise and throw lead at random,
so the bad guys would keep their heads down long enough for us to escape. We
weren't trying to hit anyone; it was purely defensive. 

AK-47 was designed for reliability and high rate of fire. It is notoriously
inaccurate beyond 2-300 meters. You'd be much better off with an M24, good to
1,000 meters, an iron-sighted M1 Garand, good to 1,000 meters in the right hands
(raising hand), or the ultimate MB2A1, good to 2,000 meters -- one mile away.
They'll admire your sophisticated weaponry as they squeegie you off the rooftop.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-04-07T08:05:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6s431$2tvg$1@si05.rsvl.unisys.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e8f1390.44281116@news.optonline.net...

> Better yet, parse the thing while stepping through the bytes and forget
about
> UNSTRING and INSPECT.

In some implementations, stepping through the bytes can be *significantly*
more expensive than certain flavors of UNSTRING and INSPECT intended to
produce the same results.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T22:31:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e91f92a.88928763@news.optonline.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <b6s431$2tvg$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

>
>"Robert Wagner" <robert@wagner.net> wrote in message
…[8 more quoted lines elided]…
>produce the same results.

I was responding to JerryMouse's attempt at programming humor (copied below for
reference), in which he steps through bytes replacing spaces with low-values,
just so he can do an UNSTRING. I said, in effect, if you're gonna step through
bytes, you might as well parse them and forget the UNSTRING. 

Intel processors permit searching for a delimiter with a _single machine
instruction_. It is 'repne scasb'. After finding it, one can move the string
with another single machine instruction. Moreover, when doing a SEARCH on a
table of bytes and looking for a single equal condition, the same instruction
can be used. Realia, from day one, produced those instructions as _inline_ code.
That's why I loved it.

FWIW, IBM mainframes are capable of doing the same, using the TRT instruction
followed by an MVC. It's actually better because it can look for multiple
delimiters.  I haven't seen an IBM compiler that come remotely close to groking
this. Maybe Joe Z. will prove me wrong. 

---- begin quote ---
MOVE 1 TO STR-PTR.
MOVE SPACE TO MYWORDS.
PERFORM VARYING INDX FROM 1 BY 1
    UNTIL INDX > MAX-WORDS
    UNSTRING MY-REC DELIMITED BY ALL '  ' INTO
         MY-WORD(INDX) WITH POINTER STR-PTR
END-PERFORM
INSPECT MYWORDS REPLACING ALL LOW-VALUES BY ' '.

Jerry Mouse

Notes:
*SPACE to LOW-VALUES within quotes

MOVE 1 TO FLIP.
PERFORM VARYING INDX FROM 1 BY 1 UNTIL INDX > REC-LEN
   IF REC(INDX:1) = '"'
      COMPUTE FLIP = 3 - FLIP
      END-IF
   IF FLIP = 2
      AND REC(INDX:1) = SPACE
      MOVE LOW-VALUES TO REC(INDX:1)
      END-IF
END-PERFORM.


>
>
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-04-07T22:52:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c2fd58$472ee440$d795f243@chottel>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <3e8b88b4.148093455@news.optonline.net> <-sqcnbcp87NiWRCjXTWc2Q@giganews.com> <3e8f1390.44281116@news.optonline.net> <b6s431$2tvg$1@si05.rsvl.unisys.com> <3e91f92a.88928763@news.optonline.net>`

```
Actually it is usually a TRT followed by a length calculation followed by
the EX of an MVC.

<snip>
> 
> FWIW, IBM mainframes are capable of doing the same, using the TRT
instruction
> followed by an MVC. It's actually better because it can look for multiple
> delimiters.  I haven't seen an IBM compiler that come remotely close to
groking
> this. Maybe Joe Z. will prove me wrong. 
> 
<snip>
```

#### ↳ Re: Beginner's Question

- **From:** "Charles W. Cribbs II" <charlescribbs@earthlink.net>
- **Date:** 2003-04-03T02:09:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yJMia.6329$4P1.480553@newsread2.prod.itd.earthlink.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com>`

```
I would suggest just doing this as a table and then read the table for the
character you are looking for and take the index of the county code that is
the same index number.

Many programs that work at the byte level will put the whole record into a
table and read along the table to determine what character they have.

That saves you from unstring and reference modification both of which they
don't teach very well in school.


"Auburn" <auburn82@iolfree.ie> wrote in message
news:df4392fb.0304020936.2ef02cfe@posting.google.com...
> I am working on an assignment for college and am stuck on the
> following:
…[19 more quoted lines elided]…
>
```

#### ↳ Re: Beginner's Question

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-02T21:53:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-62D8AC.21530602042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com>`

```
In article <df4392fb.0304020936.2ef02cfe@posting.google.com>,
 auburn82@iolfree.ie (Auburn) wrote:

> I am working on an assignment for college and am stuck on the
> following:
…[18 more quoted lines elided]…
>            02   ResourcePath            PIC X(80).

If you are guarentted a space between fields then:

   Unstring LogFileRecord
      Delimited by all " "
      into my-Date
           my-Time
           my-IP
           my-CountryCode
           my-ResourcePath
   End-Unstring

Will break your columns apart.  You could then use a compiled regex to 
validate and/or parse each (see recent post by S.C.) or build up a 
little validation FSM.

Alternatively you could build your own unstring with a perform loop and 
reference modification, like so:

   Set State-Date to true
   Move 1 to J
   Perform varying i from 1 by 1
     until i > length of LogFileRecord

     Evaluate true
        when State-date
           If LogFileRecord(i:1) not = spaces
              Move LogFileRecord (i:1) to my-date (j:1)
           Else
              perform varying i from 1 by 1
                until logfilerecord(i:1) not = spaces
              end-perform
              compute i = i - 1
              move 1 to j
              set state-time to true
           End-If

        when state-time
           If LogFileRecord(i:1) not = spaces
              Move LogFileRecord (i:1) to my-time (j:1)
           Else
              perform varying i from 1 by 1
                until logfilerecord(i:1) not = spaces
             end-perform
             compute i = i - 1
             move 1 to j
             set state-time to true
           End-If

        when state-ip
            ...you get the idea...

        when state-country-code
            ...you get the idea...

        when state-resource-path
            ...you get the idea...

        when other
           perform 123456789-scream-loudly-and-die

     End-Evaluate

   End-Perform


The first style is easy, but the second style can be turned into a 
recursive decent parser with ease if you want to get calculatable valuse 
out of date, time, IP, etc.
```

#### ↳ Re: Beginner's Question

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-04-02T21:19:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6g98n$of3$1@ngspool-d02.news.aol.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com>`

```
I think there are some way too complicated answers for this
problem. This is only a simple beginners homework assignment.
If the original poster is reading it would help if you'd
actually post a bit of the data file so we can what you've
really got. Also the actual program specs would be good too.
Also this record layout you included is not valid. You can't
have an 88 level on the group 01. What field is this
supposed to go with?

----------------------------------------------------------


"Auburn" <auburn82@iolfree.ie> wrote in message news:df4392fb.0304020936.2ef02cfe@posting.google.com...
> I am working on an assignment for college and am stuck on the
> following:
…[18 more quoted lines elided]…
>            02   ResourcePath            PIC X(80).
```

##### ↳ ↳ 88 Levels (was: Beginner's Question

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-02T23:13:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6gftc$4su$1@slb6.atl.mindspring.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6g98n$of3$1@ngspool-d02.news.aol.com>`

```
Just a "side comment"

regarding


"Anon" <anon@anon.org> wrote in message
news:b6g98n$of3$1@ngspool-d02.news.aol.com...
 <snip>
> You can't
> have an 88 level on the group 01. What field is this
…[5 more quoted lines elided]…
> "Auburn" <auburn82@iolfree.ie> wrote in message
news:df4392fb.0304020936.2ef02cfe@posting.google.com...
 <snip>
> >        FD Logfile.
> >        01 LogfileRecord.
> >            88   EndOfLogfile            VALUE HIGH-VALUES.
> >            02   Date                    PIC X(10).
> >            02   Time                    PIC X(8).
<snip>

This is perfectly valid COBOL i.e., you can code:

  01  Group-1.
           88   Group1-88   Value "123".
       05  Group-2.
              88   Group2-88   Value "45".
          10  Elem-1        Pic X.
              88  Elem-1-88   Value "6"
          10  Elem-2      Pic X.
              88  Elem-2-88   Value "7".
       05  Elem-3         Pic X.
             88  Elem-3-88   Value "8".

I am *not* saying that this is "common" (or even necessarily "good") - but
it is VALID COBOL.
```

###### ↳ ↳ ↳ Re: 88 Levels (was: Beginner's Question

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-04-03T16:59:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6iec5$rv5$1@ngspool-d02.news.aol.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6g98n$of3$1@ngspool-d02.news.aol.com> <b6gftc$4su$1@slb6.atl.mindspring.net>`

```
Really? I have absolutely never seen this before in over
20 years of coding Cobol. I always thought 88 had to go
under an elementary level. That is good to know.

So if you code:
01  the-record.
  88 good-record value '123'.
  05 field-1 pic x(10).
  05 field-2 pic 9(5).
  05 field-3 pic x(30).

What does this mean?
Is "if good-record ..." equivalent to:

    if the-record (1:3) = '123'
      or
    if the-record = '123' (where the rest of the data
                           must be spaces)

============================================================
```

###### ↳ ↳ ↳ Re: 88 Levels (was: Beginner's Question

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-03T17:30:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6ig7i$5vo$1@slb5.atl.mindspring.net>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6g98n$of3$1@ngspool-d02.news.aol.com> <b6gftc$4su$1@slb6.atl.mindspring.net> <b6iec5$rv5$1@ngspool-d02.news.aol.com>`

```
It is the latter (i.e. it refers to the entire field - with trailing spaces)
```

##### ↳ ↳ Re: Beginner's Question

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-03T01:07:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C9C396.01075003042003@corp.supernews.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6g98n$of3$1@ngspool-d02.news.aol.com>`

```
In article <b6g98n$of3$1@ngspool-d02.news.aol.com>,
 "Anon" <anon@anon.org> wrote:

> I think there are some way too complicated answers for this
> problem. This is only a simple beginners homework assignment.
…[5 more quoted lines elided]…
> supposed to go with?


Que?  Can't have an 88 on an 01?

One of us has been smoking something unusual...88 goes with entire 
01...you wanna beef about that?
```

###### ↳ ↳ ↳ Re: Beginner's Question

- **From:** auburn82@iolfree.ie (Auburn)
- **Date:** 2003-04-03T09:20:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<df4392fb.0304030920.11fa0e8f@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6g98n$of3$1@ngspool-d02.news.aol.com> <joe_zitzelberger-C9C396.01075003042003@corp.supernews.com>`

```
Many thanks to everyone for your help, much appreciated. 

UNSTRING worked perfectly for what I want. There are probably more
complicated (and elegant :) ways of solving this problem, but they are
beyond the scope of what I'm covering in college at the moment. I'll
use a table for the Country Codes.
Re: posting the spec and data file: I don't really want to post them
because this is an assignment and I should code it myself, but thanks
anyway.
```

###### ↳ ↳ ↳ Re: Beginner's Question

- **From:** "Anon" <anon@anon.org>
- **Date:** 2003-04-03T17:04:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6iel5$sdr$1@ngspool-d02.news.aol.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6g98n$of3$1@ngspool-d02.news.aol.com> <joe_zitzelberger-C9C396.01075003042003@corp.supernews.com>`

```
> Que?  Can't have an 88 on an 01?
>
> One of us has been smoking something unusual...88 goes with entire
> 01...you wanna beef about that?


I don't want to beef and I'm not a drug addict.
There's no point in this arrogant accusatory response.
This is unhelpful and inflammatory.
You could have just explained it like Mr. Klein did.
```

###### ↳ ↳ ↳ Re: Beginner's Question

_(reply depth: 4)_

- **From:** psychedelic-harry@mindless.com (Joe Zitzelberger)
- **Date:** 2003-04-04T09:23:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<16e2f010.0304040923.64064812@posting.google.com>`
- **References:** `<df4392fb.0304020936.2ef02cfe@posting.google.com> <b6g98n$of3$1@ngspool-d02.news.aol.com> <joe_zitzelberger-C9C396.01075003042003@corp.supernews.com> <b6iel5$sdr$1@ngspool-d02.news.aol.com>`

```
"Anon" <anon@anon.org> wrote in message news:<b6iel5$sdr$1@ngspool-d02.news.aol.com>...
> > Que?  Can't have an 88 on an 01?
> >
…[6 more quoted lines elided]…
> You could have just explained it like Mr. Klein did.

It was intended to be humorous and light-hearted.

I realize that postings cannot be read in the surrounding in which
they were written -- the house was full of some loud and boisterous
gangsta rap as I wrote it.  It certainly can alter ones vocabulary.

I could have explained, but in the 15 seconds it took to type that it
didn't actually occur to me that you seriously didn't know you could
put an 88 under pretty much anything.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
