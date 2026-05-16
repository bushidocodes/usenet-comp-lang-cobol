[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Why COBOL is losing the POWER struggle

_122 messages · 12 participants · 2009-06 → 2009-07_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future)

---

### Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-21T05:22:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a4k6jF1tog9jU1@mid.individual.net>`

```
I have commented more than once here that the newer languages are simply 
more concise and more powerful than COBOL. Less writing means fewer errors.

I know it's hard to believe this when you've been writing COBOL for years 
and have been astonished at how much you can do with relatively "tight" 
code. Nevertheless, one measure of the success of a language is how powerful 
it is.

Here's an example from real life that really pissed me off... :-)

Simple COBOL routine, the intention is clear for all to see...:

*---------------------------------------------------------------------------------
 transform-DDL-OUTPUT-record   section.
 tdor000.
     move function UPPER-CASE (DDL-OUTPUT-record) to DOR-work
     inspect DOR-work
             replacing ALL "TEXT(" by "CHAR("
                           ALL "DATE," by "DATETIME,"
                           ALL "CURRENCY," by "DECIMAL (14, 4),"
     move DOR-work to DDL-OUTPUT-record
     .
 tdor999.
     exit.
*---------------------------------------------------------------------------------

BUT, it is illegal and won't compile because operands for REPLACING must be 
the same length...

It is a simple global edit.  The buffers involved are large (16380 
characters). I DON"T WANT TO write a bloody PERFORM loop to look at each 
character, garner the context, and adjust the output buffer accordingly, 
but, apparently, I have no choice... so I end up with this:

      *> J will be input pointer
      *> K will be output pointer
      move spaces to DOR-work
      move 1 to K
      perform
           varying J
               from 1
                  by 1
                until J > function STORED-CHAR-LENGTH (DDL-OUTPUT-record)
                                                           OR
                       K > 16363
                    if DDL-OUTPUT-record (J:1) = space
                       if  function UPPER-CASE (DDL-OUTPUT-record (J + 1:5)) 
= "TEXT("
                           move " CHAR(" to DOR-work (K:6)
                           add 5 to J
                           add 6 to K
                       else
                          if  function UPPER-CASE (DDL-OUTPUT-record (J + 
1:5)) = "DATE,"
                              move " DATETIME," to DOR-work (K:10)
                              add 5 to J
                              add 10 to K
                          else
                             if  function UPPER-CASE (DDL-OUTPUT-record (J + 
1:9)) = "CURRENCY,"
                                 move " DECIMAL (14, 4)," to DOR-work (K:17)
                                 add 9 to J
                                 add 17 to K
                             else
                                 add 1 to K *> position (K) is already a 
space so no need to move.
                             end-if
                           end-if
                        end-if
                    else
                        move DDL-OUTPUT-record (J:1) to DOR-work (K:1)
                        add 1 to K
                    end-if
     end-perform


   ... which is pretty ghastly, not to mention, tiresome to work out and 
debug (I haven't debugged this and am not looking forward to spending an 
hour  stepping through it to ensure it functions correctly...) And, it will 
only work in Fujitsu COBOL because of the STORED-CHAR-LENGTH function...
(Fortunately, because it is a part of a COBOL COM component which will run 
with C# in the .NET Framework, it doesn't matter what language it is written 
in, so the dialect of COBOL is immaterial.)

Even if you code in a more compressed style than my 31 lines above, why 
should you have to get your head around every bloody byte that needs to be 
moved? Remembering that J gets incremented when K doesn't, by the 
controlling loop and so on... It's a horror show and in this day and age we 
shouldn't have to deal with it. If I WANT this kind of nonsense I can code 
in Assembler. The INSPECT functionality is clear and simple and expresses 
exactly what is intended... why can't it manage operands of different 
lengths for REPLACING?

To devise, write, and debug the above is at least 90 minutes, more, if there 
are problems with it.

In C# I can use a Regular Expression, code 3 lines and get on with more 
important things...

outBuffer = RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");
outBuffer = RegEx.Replace(outBuffer.ToUpper(), "DATE,","Datetime,");
outBuffer = RegEx.Replace(outBuffer.ToUpper(), "CURRENCY,","Decimal (14, 
4),");

Two minutes to think about and write, and a pretty fair chance it will not 
require debugging because the IDE ensures the names and syntax are correct 
long before the code is ever compiled and run.

This is an excellent example of what I mean when I say my productivity has 
increased  at least two-fold since moving off COBOL.

It isn't always as dramatic as this, but there is no case I can think of 
where it was actually quicker to write something in COBOL than in C#.

Pete.
```

#### ↳ Re: Why COBOL is losing the POWER struggle

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-20T15:01:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net>`

```
On Jun 21, 5:22 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> I have commented more than once here that the newer languages are simply
> more concise and more powerful than COBOL. Less writing means fewer errors.
…[99 more quoted lines elided]…
> 4),");

You are comparing apples and semolina. 'RegEx.Replace' is a method, or
subroutine and is likely to be much, much more than the 31 lines of
code you wrote above, but does it by something like that.

Of course the routine is provided for you, but in your 40 years or
more did you never write general purpose routines that you could re-
use ? Did you always solve every detail with new code ?

BTW I think that your technique is not particularly good. I would do
the replaces with a table, or list, and iterate through this as I
tried to replace each item. The replace subroutine would then work
with one replacement at a time, just like the C# code. Also you could
do it with an UNSTRING WITH POINTER/STRING loop.

I have written many code generating programs and, of course,
templating is all about replacing tags with values and I was doing
that before C# was dreamed up, even before Java, PERL, Python or
Borland's C++.

It seems that you rant about this because you have come late to the
newer languages and are a 'born again' programmer. You said in a
recent message 'why didn't we have this years ago'. Well _we_ did, or
at least _I_ (and many others) did. It seems that you kept old clunky
stuff and then 'discovered' VisualStudio and thought that it was some
magic that had never been done before. It may be that C# and VS does
have some fancy features and puts them all together in a particular
way, but it has nothing that hasn't been available in some form over
the last couple of decades.


> Two minutes to think about and write, and a pretty fair chance it will not
> require debugging because the IDE ensures the names and syntax are correct
…[10 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-21T13:08:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a5fgmF1tcqi6U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com>`

```
riplin wrote:
> On Jun 21, 5:22 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[109 more quoted lines elided]…
> code you wrote above, but does it by something like that.

So is INSPECT... REPLACING. That isn't the point. It is having facilities 
available and at your fingertips that is important.


>
> Of course the routine is provided for you, but in your 40 years or
> more did you never write general purpose routines that you could re-
> use ? Did you always solve every detail with new code ?

No, of course not. I use components all the time.

When I realized that INSPECT wasn't up to the task it is supposed to be have 
been designed for, I immediately thought of CGI code I have which could be 
used to do these replacements.

It is on another machine which isn't even switched on. By the time I go and 
boot it up, connect it ot the LAN, search the system to find the code I 
need, cut and paste it to the current code,  tinker with the interface, and 
make sure it works, I am still up for at least an hour's work.

(And it means getting out of my chair... :-))

FINDING code to reuse can be problematic. I have my C# stuff better 
organised than my COBOL, which was written over decades and is on different 
machines, in different environments.

>
> BTW I think that your technique is not particularly good. I would do
> the replaces with a table, or list, and iterate through this as I
> tried to replace each item.

So post the code and we can argue about it.


>The replace subroutine would then work
> with one replacement at a time, just like the C# code. Also you could
> do it with an UNSTRING WITH POINTER/STRING loop.
>

Yes, I thought about using UNSTRING. You obviously didn't. This is a 16K 
buffer that could have ANY number of the target strings in ANY order.
 So how big an array do I unstring them into?  Terminated by WHAT? A space? 
I don't think so... Put up or shut up. Show me the code.


 > I have written many code generating programs and, of course,
> templating is all about replacing tags with values and I was doing
> that before C# was dreamed up, even before Java, PERL, Python or
> Borland's C++.

I know about templating and replacing and have used it with web based stuff 
for years also. Long before I was using C#.

What beariing does it have on the fact that INSPECT REPLACING can't handle 
different length operands?
>
>
> It seems that you rant about this because you have come late to the
> newer languages and are a 'born again' programmer.

No Richard, I didn't come down in the last shower and I have been 
programming computers probably longer than you have. I'm ranting about this 
because a simple function doesn't do what it SHOULD do and in other 
languages it DOES. We don't even have a Regex facility in COBOL and, yes, 
you can call the VB one (I have done that on one occasion), but it is 
unwieldy and unfriendly. The code speaks for itself.

You can pontificate all you like about there being better ways of doing it, 
but until you post code you have no credibility.
My point (see the thread subject) is that COBOL is LESS POWERFUL than C# or 
Java (as just 2 "for instances"). It doesn't matter really what I think 
about it; the fact is that other people are seeing the same thing.

COBOL simply doesn't compete with modern languages, largely because it was 
designed for a different environment than the one we have, and because it 
focusses on ease of maintenance of source code, which is only important when 
everything is written in ONE language and has to be maintained in that 
language. It's kind of ironic that despite it being English-like and easy to 
read, it still takes many more hours to maintain it than it does the 
equivalent in a modern language. This is largely because there is just so 
much MORE of it to be maintained. Again, the posted code speaks for itself.


>You said in a
> recent message 'why didn't we have this years ago'. Well _we_ did, or
> at least _I_ (and many others) did.

Yes, I should have been careful about the use of "we"... COBOL was (and 
is...) primarily used on mainframe sites in mainframe environments. While 
the IDEs have improved significantly, there just has never been the 
facilities that are in VS. My point was that there should have been. (It's a 
bit pointless now, I guess, because, like COBOL, it has been overtaken by 
events.). Many mainframe sites have moved development off the mainframe and 
CAN use IDEs like VS or Eclipse.

> It seems that you kept old clunky
> stuff and then 'discovered' VisualStudio and thought that it was some
> magic that had never been done before.

Oh, sure. I TREASURED the Fujitsu and Micro Focus IDEs and was thrilled to 
have themt. I LOVED using ISPF and TSO and wouldn't have swapped them for 
the world. I have clung on to clunky junk because I LOVE antiques... The 
fact is that there WAS no other option. YOU may have been using 
non-IBM/Microsoft solutions and getting good value from it but it simply 
wasn't deployed or deployable on the sites where I was working.

What you run for yourself is NOT necessarily what the majority of employers 
are running. These days I can use whatever I like and I do. I wish there had 
been tools like VS available in the environments where I worked, years ago. 
However, it is academic. There weren't and, on many sites, there still 
aren't even today. I am much more interested in what I can use NOW than a 
pissing contest about how long I didn't use something, especially when it 
simply wasn't available in the environments I was working in.

Even if I discovered VS yesterday, that doesn't make it any less powerful a 
tool. I'm not interested in what has been done before, I'm interested in 
what I can use NOW to get applications up and working. Cobbling together 
thousands of lines of COBOL code when I can write a few lines to do the same 
thing in a more powerful languiage is the point of this thread.


>It may be that C# and VS does
> have some fancy features and puts them all together in a particular
> way, but it has nothing that hasn't been available in some form over
> the last couple of decades.
>

Good. So what does that mean to me TODAY?

>
>> Two minutes to think about and write, and a pretty fair chance it
…[9 more quoted lines elided]…
>>

I did debug the code I posted last night and it only needed a couple of 
minor things to do exactly what I wanted. But I still spent over an hour on 
something which, if INSPECT did its job, should have been a couple of 
minutes.

I feel much better now... :-)

Pete.
 -- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-21T14:15:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net>`

```
On Jun 21, 1:08 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> riplin wrote:
> > On Jun 21, 5:22 am, "Pete Dashwood"

> When I realized that INSPECT wasn't up to the task it is supposed to be have
> been designed for, I immediately thought of CGI code I have which could be
> used to do these replacements.

INSPECT is exactly "up to the task it is ... designed for". It works
in situ on strings. It was not 'designed for' copy and replace which
is what regex.replace() does. As Doc says, you are tying to use a
screwdriver for something else.


> It is on another machine which isn't even switched on. By the time I go and
> boot it up, connect it ot the LAN, search the system to find the code I
…[3 more quoted lines elided]…
> (And it means getting out of my chair... :-))

In what ways is that the fault of Cobol ?

> FINDING code to reuse can be problematic. I have my C# stuff better
> organised than my COBOL, which was written over decades and is on different
> machines, in different environments.

In what ways is that the fault of Cobol ?


> > BTW I think that your technique is not particularly good. I would do
> > the replaces with a table, or list, and iterate through this as I
…[8 more quoted lines elided]…
> Yes, I thought about using UNSTRING. You obviously didn't.

I obviously _did_, and you failed to see how it could be done.

> This is a 16K
> buffer that could have ANY number of the target strings in ANY order.
>  So how big an array do I unstring them into?  

Let the master show you,

> Terminated by WHAT? A space?

No. Terminated by the string you want to replace.

> I don't think so... Put up or shut up. Show me the code.
>
…[10 more quoted lines elided]…
> different length operands?

It has significant bearing because templating can't be done with the
wrong tool either.

> > It seems that you rant about this because you have come late to the
> > newer languages and are a 'born again' programmer.
…[33 more quoted lines elided]…
> CAN use IDEs like VS or Eclipse.

Exactly, many mainframe sites do development on systems which have
better tools, and have done so for years.

> > It seems that you kept old clunky
> > stuff and then 'discovered' VisualStudio and thought that it was some
…[7 more quoted lines elided]…
> wasn't deployed or deployable on the sites where I was working.

I have been fortunate in that I have been able to use _my_ tools
wherever I went. Just a condition of me doing work.

> What you run for yourself is NOT necessarily what the majority of employers
> are running. These days I can use whatever I like and I do. I wish there had
…[41 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T14:22:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a886lF1s84o2U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com>`

```
riplin wrote:
> On Jun 21, 1:08 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[10 more quoted lines elided]…
> screwdriver for something else.

So, what part of REPLACING do you not understand :-)?

I wanted my buffer replaced in situ as a string. The ONLY reason I needed a 
second buffer was because INSPECT wasn't up to the task.
>
>
…[8 more quoted lines elided]…
> In what ways is that the fault of Cobol ?

OK, first off, I am NOT finding fault with COBOL. The thread is about the 
POWER of languages. The fault here is with a Standard that limits the 
replace function, so that other languages which have no such limitation are 
perceived as being more powerful.

Second off, My comment was made with tongue in cheek. Are you losing your 
sense of humour?

>
>> FINDING code to reuse can be problematic. I have my C# stuff better
…[3 more quoted lines elided]…
> In what ways is that the fault of Cobol ?

In the same way that the price of fish is simply outrageous these days. Have 
you tried to buy a schnapper fillet recently? Need a mortgage on the house 
to get a decent piece of hapuka...

I am not now, and never was, discussing the fault of COBOL, or any faults of 
COBOL. I posted a fact. That fact contributes to the perception of POWER in 
the language.
>
>
…[22 more quoted lines elided]…
> No. Terminated by the string you want to replace.

Yes, I saw your code. I didn't consider that approach and you did a good job 
of it.

>
>> I don't think so... Put up or shut up. Show me the code.
>>

You did, and it was good.

It still is not as powerful as a single line.

>>> I have written many code generating programs and, of course,
>>
…[11 more quoted lines elided]…
> wrong tool either.

It can be done with COBOL. The question is whether COBOL is the "best" (most 
powerful) tool to do it with.

>
>>> It seems that you rant about this because you have come late to the
…[26 more quoted lines elided]…
>>
I appreciate that you didn't snip the above, and I stand by it.

>>> You said in a
>>> recent message 'why didn't we have this years ago'. Well _we_ did,
…[28 more quoted lines elided]…
>
That is fortunate indeed. Regrettably it is NOT the case for most of us.

>> What you run for yourself is NOT necessarily what the majority of
>> employers are running. These days I can use whatever I like and I
…[41 more quoted lines elided]…
>>

Y'know, in retrospect, looking back a couple of days later, I really was 
agitated over this :-)

I've become used to things simply working. And working simply.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-22T15:48:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1o946$2s5$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net>`

```
In article <7a886lF1s84o2U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>I wanted my buffer replaced in situ as a string. The ONLY reason I needed a 
>second buffer was because INSPECT wasn't up to the task.

Wait, I am confused.  The situ of 'DATE' is four bytes and 'DATETIME' 
requires eight.  To place in the situ of a four-character string an 
eight-character one requires a... curious bit of mathematics, to say the 
least.

[snip]

>I am not now, and never was, discussing the fault of COBOL, or any faults of 
>COBOL. I posted a fact. That fact contributes to the perception of POWER in 
>the language.

Mr Dashwood, once again: what language has the POWER to fill startpos 8, 
len 4 with an eight-byte string without some sort of compression?

[snip]

>It still is not as powerful as a single line.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T13:14:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aaojaF1v66vqU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7a886lF1s84o2U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
> the least.

Perhaps a more carefulreading would reveal that what I said was "my BUFFER 
replaced in situ". There is plenty of room in the buffer for expansion of 
individual bits of it.
>
> [snip]
…[6 more quoted lines elided]…
> 8, len 4 with an eight-byte string without some sort of compression?

C#,  Java, and Visual Basic ALL do it easily. The actual operand(s) is/are 
not compressed; the buffer which it/they occurs in is not changed in length 
either. A Regular Expression can expand or compress replacement operands 
within a buffer. If it runs out of expansion space then the last part of 
what the buffer contains is truncated accordingly; if the string it contains 
becomes shorter, then it is padded with whatever character you designate 
(space by default).  And all of this requires ONE line of code. (Actually, 
that is not even scratching the surface of what you can do with Regular 
Expressions in ONE line of code, it is just a simple example... have a look 
at: http://www.design215.com/toolbox/regexp.php  THAT is powerful.

If INSPECT ...REPLACING could do that it would be more powerful than it is.

Sure, the non-English-like syntax of Regex strings looks weird and 
unfamiliar to COBOL people (It was devised by a mathematician and there is a 
mathematical simplicity and elegance to it once you start to understand it), 
but there is no denying the POWER of it...

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-22T19:00:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net>`

```
On Jun 23, 1:14 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> docdw...@panix.com wrote:
> > In article <7a886lF1s84o...@mid.individual.net>,
…[33 more quoted lines elided]…
> (space by default).

You are wrong. The replace routine does not work 'in situ':

> outBuffer = RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");

outBuffer.ToUpper() possibly could change all the characters in
outBuffer to upper case in situ though it is more likey to create a
new buffer. This new buffer is then passed to replace() which creates
another _new_ buffer that is passed back and assigned to your object
reference variable. The old outBuffer object is discarded. You do this
three times so there are six buffers in the garbage.

You should note that your resulting outBuffer will be all upper case
except 'ecimal' which may not be the result you wanted.

Try:

outBuffer = RegEx.Replace(outBuffer, "[Tt][Ee][Xx][Tt](","Char(");
outBuffer = RegEx.Replace(outBuffer, "[Dd][Aa][Tt][Ee],","Datetime,");
outBuffer = RegEx.Replace(outBuffer, "[Cc][Uu][Rr][Rr][Ee][Nn][Cc]
[Yy],","Decimal (14,4),");

Or there may be some setting that makes it case insensitive on
searching.

> And all of this requires ONE line of code. (Actually,
> that is not even scratching the surface of what you can do with Regular
> Expressions in ONE line of code, it is just a simple example... have a look
> at:http://www.design215.com/toolbox/regexp.php THAT is powerful.

But is not part of 'the C# language'.


> If INSPECT ...REPLACING could do that it would be more powerful than it is.
>
> Sure, the non-English-like syntax of Regex strings looks weird and
> unfamiliar to COBOL people

Regular expressions (eg grep) have been part of my toolkit for 30
years. I even implemented grep on my Concurrent-CP/M-86 systems that I
developed for in the early 80s.

> (It was devised by a mathematician and there is a
> mathematical simplicity and elegance to it once you start to understand it),
…[4 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T15:21:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ab01lF1uqgnmU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com>`

```
riplin wrote:
> On Jun 23, 1:14 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[39 more quoted lines elided]…
> You are wrong. The replace routine does not work 'in situ':

It does as far as I am concerned. What it does under the covers is 
irrelevant.
>
>> outBuffer = RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");
…[6 more quoted lines elided]…
> three times so there are six buffers in the garbage.

Don't care. All I am dealing with is outBuffer.
>
> You should note that your resulting outBuffer will be all upper case
> except 'ecimal' which may not be the result you wanted.

Not so. My default Regex options specify case insensitive.
>
> Try:
…[4 more quoted lines elided]…
> [Yy],","Decimal (14,4),");

No need...

>
> Or there may be some setting that makes it case insensitive on
> searching.

Yes.
>
>> And all of this requires ONE line of code. (Actually,
…[5 more quoted lines elided]…
> But is not part of 'the C# language'.

It is part of the Framework used intrinsically by C# and the other .NET 
languages. I don't have to "call out" to it or do anything other than 
reference the .dll.
>
>
…[16 more quoted lines elided]…
>> "I used to write COBOL...now I can do anything."
Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-22T21:10:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net>`

```
On Jun 23, 3:21 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> riplin wrote:
> > On Jun 23, 1:14 pm, "Pete Dashwood"
…[41 more quoted lines elided]…
> irrelevant.

No, it is not "irrelevant". It is especially not irrelevant when you
try to describe what happens under the covers and tell it wrong.


> >> outBuffer = RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");
>
…[12 more quoted lines elided]…
> Not so. My default Regex options specify case insensitive.

> >> outBuffer = RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");

So you are saying that the 'outBuffer.ToUpper()' is a null operation
and does nothing at all ?

Have you actually tested this code and looked at the output ?


> > Try:
>
…[22 more quoted lines elided]…
> reference the .dll.


> >> If INSPECT ...REPLACING could do that it would be more powerful than
> >> it is.
…[18 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T20:30:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7abi47F1uovqiU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com>`

```
riplin wrote:
> On Jun 23, 3:21 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[48 more quoted lines elided]…
>
Well, Gee, it's just as well I didn't do that, then...

At no time in this conversation have I ever tried to describe what happens 
under the covers in either COBOL or C# or the .NET framework support for 
Regex. I am on record as stating that I don't care. I don't. It isn't me who 
is wrong here. (You may have mistaken my description above of the process as 
it appears to a user (functional) for an attempt to explain how it works 
(technical))
>
>>>> outBuffer = RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");
…[19 more quoted lines elided]…
> and does nothing at all ?

No, I'm saying nothing about it other than that I put it in from force of 
habit and I need not have.

I've already said that elsewhere.

I don't intend to discuss it further.

The code is not "real" code. I wrote it from memory to make a point. (As I 
did with the COBOL sample.) I was annoyed at the time, but I did say that I 
had not checked or debugged the COBOL code. I should have said the same 
about the C#.

The problem (for me) is that it is not about the details of the code. It is 
about the fact that something I expected to work didn't and it cost me over 
an hour to get round it. I see that as a failing with COBOL because it was 
COBOL that didn't work as expected.

If I were being fair I could admit that my understanding of it was flawed 
and I should not have TRIED to use it. It DOES work as documented. Under 
pressure, fairness sometimes goes out the window.

The irritation is compounded (again this is for me) because that kind of 
thing DOESN'T happen to me when I use C#. Maybe I am checking C# constructs 
more carefully, maybe the environment enforces more accuracy, I don't know. 
I DO know I can do things much more quickly with C# than I can with COBOL. I 
put this down to the relative power of the the two languages. It is 
arguable, and we've argued it. I still think C# is more powerful 
(apparently, a lot of other people do too, although that doesn't bother me.)

The world (and me) are voting with their feet.

I made the post partly to let off steam and partly because I do think COBOL 
should implement INSPECT REPLACING so it actually replaces operands of 
differing size.

I appreciate you posting your COBOL solution, although it is more lines than 
mine and I reckon it will run slower (I haven't tested it so you can prove 
me wrong if you want to.) It is clean, general code, and is an approach I 
did not consider, although I thought about and discarded the use of 
UNSTRING.

 I'm not going to respond further on this unless people discuss the actual 
topic, and even then I think I have made my position clear.

I DID learn a few things from this, largely thanks to Michael.

1. I SHOULD have used string replace. (He rightly pointed out that the 
operands did not contain any Regex symbols.)

2. It is probably worth my taking the time to find out more about some of 
the  more obscure (to me) functions available in C#. (I'm actually too busy 
writing software to do this at the moment.)

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T14:13:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qnuq$inb$2@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net>`

```
In article <7abi47F1uovqiU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>The problem (for me) is that it is not about the details of the code. It is 
>about the fact that something I expected to work didn't and it cost me over 
>an hour to get round it. I see that as a failing with COBOL because it was 
>COBOL that didn't work as expected.

COBOL works, for the most part, the way The Manual says it does.  This 
seems less a failing of the language than a failing in your expectations 
for it.

>
>If I were being fair I could admit that my understanding of it was flawed 
>and I should not have TRIED to use it. It DOES work as documented. Under 
>pressure, fairness sometimes goes out the window.

That, Mr Dashwood, is, in my experience, a dodge.   Fairness did not go 
out the window... it was ignored, or tossed aside, by a person.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:30:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad6rvF1u99r8U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net> <h1qnuq$inb$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7abi47F1uovqiU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[18 more quoted lines elided]…
> go out the window... it was ignored, or tossed aside, by a person.

"Blessed are the merciful..."

Thanks, Doc.

If I were attempting a "dodge" it would be because I feared the consequences 
of something.

I don't. Don't do it in real life and I don't do it here. I have been 
scrupulously honest as to what happened, even down to accepting 
responsibility for the fact that it DOES work as advertised and I should 
have read the advertisement. I'm really sorry if that kind of robs you of an 
opportunity to beat me up.

Are you so perfect that you never got annoyed about something and let it 
blur your vision?

Fairness went out the window, it was NOT consciously discarded. I try to be 
strictly fair in everything I do, including posts to this forum.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-24T00:52:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1rtbk$pv4$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7abi47F1uovqiU1@mid.individual.net> <h1qnuq$inb$2@reader1.panix.com> <7ad6rvF1u99r8U1@mid.individual.net>`

```
In article <7ad6rvF1u99r8U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7abi47F1uovqiU1@mid.individual.net>,
…[21 more quoted lines elided]…
>"Blessed are the merciful..."

... 'cause they're so hard to find?  I remember reading an interview with 
(I think) a US Supreme Court Justice who had gone to a Jesuit-run grade 
school; he'd been caught in some kind of infraction and - those being the 
days when they still could - the priest strode towards the lad with the 
obvious intent of Not Spoiling the Child.  The lad, as 10-year-olds do, 
tried to whine and dodge and let loose with something like 'Aw, c'mon, 
Father, show a little mercy, willya?'

The priest's response was 'Mercy is the province of Our Father in Heaven, 
we are the Jesuits and we dispense Justice.'

>
>Thanks, Doc.
>
>If I were attempting a "dodge" it would be because I feared the consequences 
>of something.

Assertion of motive and kind of difficult to verify.

[snip]

>Are you so perfect that you never got annoyed about something and let it 
>blur your vision?

Quite the reverse... many a schoolchild knows 'takes one to know one' and 
many a detective knows 'set a thief to catch a thief'.  What I have done 
and my reasons for it have no place in how and why another person behaves 
in a particular way; I am not of Such Stature that I am worthy of 
emulation.

>
>Fairness went out the window, it was NOT consciously discarded. I try to be 
>strictly fair in everything I do, including posts to this forum.

Mr Dashwood, fairness - being a human invention - goes where humans put it 
and does as humans have it do, it posses no volens.

For example... a few millennia an idea of equality went along the lines of 
'an eye for an eye'... until someone said 'Wait a minute... some people 
have strong constitutions and some less so, what might cause one person 
to lose an eye would cause another to die.  Where lies fairness?'

(the last is a trick question, of course... fairness, being fair, tells no 
lies... wonderful language, this English)

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T08:32:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgp1451l68ppfkp52nujagkvp9qcbm5nqn@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net>`

```
On Tue, 23 Jun 2009 20:30:00 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I made the post partly to let off steam and partly because I do think COBOL 
>should implement INSPECT REPLACING so it actually replaces operands of 
>differing size.

One of CoBOL's misses was not adjusting to modern styles of variable
field and record sizes.    The trouble is, string processing has
become relevant to a business language, and the language should have
adapted.

My other complaint was that its error handling was an early attempt
that should have been changed.    We have lots of code that checks to
see if we can do the next command.    It certainly is clumsy to have a
library function that checks to see if we can run the next library
function!  (can't translate a date until we verify that the field is a
date).

But adaptation is difficult when we have expensive compiled languages
that go through years of bureaucracy to get anything changed enough
for users to even try out new changes.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 12)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-06-23T17:10:50-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jkd245lb6h84imsj535fs946hnort483qg@4ax.com>`
- **References:** `<7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net> <vgp1451l68ppfkp52nujagkvp9qcbm5nqn@4ax.com>`

```
On Tue, 23 Jun 2009 08:32:49 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Tue, 23 Jun 2009 20:30:00 +1200, "Pete Dashwood"
><dashwood@removethis.enternet.co.nz> wrote:
…[19 more quoted lines elided]…
>for users to even try out new changes.

Here the problem is the bureaucracy and not the language.  Change
control requirements should be language and platform independent.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T14:38:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<l6f245t6keq2bflpve3da64bsd1nq6jf6a@4ax.com>`
- **References:** `<4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net> <vgp1451l68ppfkp52nujagkvp9qcbm5nqn@4ax.com> <jkd245lb6h84imsj535fs946hnort483qg@4ax.com>`

```
On Tue, 23 Jun 2009 17:10:50 -0300, Clark F Morris
<cfmpublic@ns.sympatico.ca> wrote:

>>But adaptation is difficult when we have expensive compiled languages
>>that go through years of bureaucracy to get anything changed enough
…[3 more quoted lines elided]…
>control requirements should be language and platform independent.

Having to create a compiler contributes.   Library languages tend to
get people actually getting stuff working cheaply before needing to
work the process.    That makes a difference.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:34:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad74uF1v1mcmU1@mid.individual.net>`
- **References:** `<4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net> <vgp1451l68ppfkp52nujagkvp9qcbm5nqn@4ax.com> <jkd245lb6h84imsj535fs946hnort483qg@4ax.com> <l6f245t6keq2bflpve3da64bsd1nq6jf6a@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 23 Jun 2009 17:10:50 -0300, Clark F Morris
> <cfmpublic@ns.sympatico.ca> wrote:
…[10 more quoted lines elided]…
> work the process.    That makes a difference.

These are the real issues that I was hoping would be debated. Unfortunately, 
it is now too late for COBOL.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-23T13:29:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1r8451i0@news7.newsguy.com>`
- **In-Reply-To:** `<7abi47F1uovqiU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> At no time in this conversation have I ever tried to describe what happens 
> under the covers in either COBOL or C# or the .NET framework support for 
> Regex. I am on record as stating that I don't care. I don't. It isn't me who 
> is wrong here.

I'm afraid this is precisely the error, though.

In an indirect-reference, garbage-collected environment, such as .NET
(and this applies to all .NET languages, including COBOL), you can
generally get away with not caring whether your Regex replace
operation alters your original data or gives you a new object with the
new data.

But not always - for example, if you have other references to the
original data, you had best know that they will continue to refer to
the original data.

And in an environment with direct memory access, such as the typical
COBOL program runs in, you *have to* care, because copying your data
will orphan pointers to the old data, and freeing the old data will
invalidate such pointers. And there's no way for a direct-access
implementation to know whether such pointers exist or when they might
be used. And that's one reason why COBOL's REPLACE verb can't simply
copy data under the covers - that would violate the semantics of the
language.

So in fact it's absolutely critical to know what the implementation
does, if you're going to critique what features it exposes to the
programmer.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:32:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad6vlF1uot4gU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net> <h1r8451i0@news7.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[28 more quoted lines elided]…
> programmer.

Ok, I'll try to be a more caring programmer in future... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-23T13:02:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e223e5b-31fd-4feb-aa47-03363dbae3f0@w35g2000prg.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <c814f8a0-90c0-41cb-8ca4-27d2a1689c65@o21g2000prn.googlegroups.com> <7abi47F1uovqiU1@mid.individual.net>`

```
On Jun 23, 8:30 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> riplin wrote:
> > On Jun 23, 3:21 pm, "Pete Dashwood"
…[54 more quoted lines elided]…
> Regex.

What part if this is not "tried to describe what happens under the
covers" ?

"""C#, Java, and Visual Basic ALL do it easily. The actual perand(s)
is/are not compressed; the buffer which it/they occurs in is not
changed in length either. A Regular Expression can expand or  compress
replacement operands within a buffer. If it runs out of expansion
space then the last part of what the buffer contains is truncated
accordingly; if the string it contains becomes shorter, then it is
padded with whatever character you designate (space by  default)."""

Of course it is fundamentally wrong and misleading. For example
'truncated' and 'padded' will not occur. A new string is created that
is the length required to contain the characters and it is only your
assignment (outBuffer =) that replaces the value of the object
reference (pointer) with the new string reference.


> I am on record as stating that I don't care. I don't. It isn't me who
> is wrong here. (You may have mistaken my description above of the process as
> it appears to a user (functional) for an attempt to explain how it works
> (technical))

No, it is not a "description as it appears to a user", it was an
attempt to respond to a technical question, but simply a wrong-headed
one.

For example if you had written only:

   RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");

Then the contents of outBuffer would not be changed at all.


> >>>> outBuffer = RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");
>
…[21 more quoted lines elided]…
> habit and I need not have.

What you did also say was "Not so", denying what the code you had
written would actually do.

While your rant was complaining about how Cobol's INSPECT REPLACING
did not do what you imagined it should (in spite of 35 years of the
spec being quite clear about what it will do), you also seem to be
similarly unaware of what happens in the code that you wrote in C#. It
will not pad or truncate, it will make it all upper case except the
final replacement.

You are advocating C# because it is 'more powerful'. You are certainly
showing that it is possible to have more errors per line than Cobol.

Also a Ferrari is 'more powerful', but I wouldn't hand these out to my
delivery drivers.


> I've already said that elsewhere.
>
…[10 more quoted lines elided]…
> COBOL that didn't work as expected.

Exactly. And the C# code also "didn't work as expected". That is also
a failure of C# ???


> If I were being fair I could admit that my understanding of it was flawed
> and I should not have TRIED to use it. It DOES work as documented. Under
…[3 more quoted lines elided]…
> thing DOESN'T happen to me when I use C#.

You have shown a fundamental misunderstanding of how C# (and Java)
work and have shown code which does not do as you expect and then you
claim it 'doesn't happen when I use C#'.

I refer you to an early sentence from you:

"""You can pontificate all you like about there being better ways of
doing it, but until you post [working] code you have no
credibility."""


> Maybe I am checking C# constructs
> more carefully, maybe the environment enforces more accuracy, I don't know.
…[13 more quoted lines elided]…
> me wrong if you want to.)

In the actual program it is just one line per replace. Granted that
particular routine was not provided by the vendor or the environment.

It may run slower than your code, but yours does all 3 replacements in
one pass (if it works). If a further or different replacement were
required than your code would be rewritten.

But then my code was simply to illustrate how an UNSTRING WITH
POINTER / STRING loop works, which you implied wouldn't with your
snipe of "Yes, I thought about using UNSTRING. You obviously didn't.",
and to answer your questions about:

"""This is a 16K buffer that could have ANY number of the target
strings in ANY order.  So how big an array do I unstring them  into?
Terminated by WHAT? A space? I don't think so... Put up or shut up.
Show me the code."""

Well I had obviously thought about it in ways that you had not
expected.


> It is clean, general code, and is an approach I
> did not consider, although I thought about and discarded the use of
…[16 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T14:08:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qnki$inb$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net>`

```
In article <7ab01lF1uqgnmU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>riplin wrote:
>> On Jun 23, 1:14 pm, "Pete Dashwood"
>> <dashw...@removethis.enternet.co.nz> wrote:

[snip]

>>> C#, Java, and Visual Basic ALL do it easily. The actual operand(s)
>>> is/are not compressed; the buffer which it/they occurs in is not
…[9 more quoted lines elided]…
>It does as far as I am concerned.

This may be one of the difficulties that is showing up in this thread.  Mr 
Dashwood, 'as far as you are concerned' is not 'what the machine is 
doing'.  What I am attempting to do is understand the latter, not the 
former.

>What it does under the covers is 
>irrelevant.

When it comes to attempting to grasp a new concept, Mr Dashwood, what you 
consider relevant or not might be less useful in both this and future 
situations than What Actuall Is Going On Down There.  My concerns stem 
from days when a coder had to be able to find the PSW, go back to the 
previous imperative and determine what was going wrong so that the 
tax-reports could run within the window that had been allotted to it them 
and the company remain in compliance with The Law.

That's what I get paid for, at times... and giving my client decent value 
for a decent dollar is how I try to do it.

[snip]

>Don't care. All I am dealing with is outBuffer.

Oh, I forgot... a Big Picture Guy!

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T08:26:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gep145dgt7hhbd4q1jhg1oisaknf4rtpih@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net>`

```
On Tue, 23 Jun 2009 15:21:27 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:


>"I used to write COBOL...now I can do anything." 

That's a fun SIG - but as an old time COBOL programmer, you have to
admit that there are more difficult languages out there.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:36:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad77nF1ut7omU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <7ab01lF1uqgnmU1@mid.individual.net> <gep145dgt7hhbd4q1jhg1oisaknf4rtpih@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 23 Jun 2009 15:21:27 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[5 more quoted lines elided]…
> admit that there are more difficult languages out there.

I don't HAVE to admit it, but I will do so freely. My SIG is ambiguous by 
intention. :-)

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T09:00:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n5p145t34137moinutdq5a45blbpbfofot@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com>`

```
On Mon, 22 Jun 2009 19:00:45 -0700 (PDT), riplin <riplin@Azonic.co.nz>
wrote:

>Regular expressions (eg grep) have been part of my toolkit for 30
>years. I even implemented grep on my Concurrent-CP/M-86 systems that I
>developed for in the early 80s.

One would think *all* search engines would have the option of regular
expressions by now.    That includes all on-line search engines, as
well as CoBOL library functions, Apple's search on their desktop and
in iTunes, all e-mail and document processing programs, and browsers.

I often choose TSO/ISPF to find particular records even after I have
FTPd the file to a desktop, as I have more powerful record and column
search abilities in that "obsolete" technology.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T15:29:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qsbv$r0t$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <n5p145t34137moinutdq5a45blbpbfofot@4ax.com>`

```
In article <n5p145t34137moinutdq5a45blbpbfofot@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>I often choose TSO/ISPF to find particular records even after I have
>FTPd the file to a desktop, as I have more powerful record and column
>search abilities in that "obsolete" technology.

After fat-fingering enough errors to require retransmission I have 
developed the following moderately-clumsy technique:

1) get the file

2) use Edit to get MYUID.JCL.CNTL(DUMMY) (or any other member) and issue a 
BROWSE at the command line

3) BROWSE the transmitted dataset (ISPF VIEW still confuses me as being 
too similar to EDIT... in BROWSE everything is blue, period)

4) when done, JUST TO BE SURE... can out of everything.

Haven't had a lick of trouble with that'un.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T10:47:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mn12455kek467ragti0psjk226p5hhi4ta@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <n5p145t34137moinutdq5a45blbpbfofot@4ax.com> <h1qsbv$r0t$1@reader1.panix.com>`

```
On Tue, 23 Jun 2009 15:29:04 +0000 (UTC), docdwarf@panix.com () wrote:

>After fat-fingering enough errors to require retransmission I have 
>developed the following moderately-clumsy technique:
…[11 more quoted lines elided]…
>Haven't had a lick of trouble with that'un.

I prefer VIEW as, I make lots of use of the EXCLUDE command.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T17:46:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1r4eh$fik$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <n5p145t34137moinutdq5a45blbpbfofot@4ax.com> <h1qsbv$r0t$1@reader1.panix.com> <mn12455kek467ragti0psjk226p5hhi4ta@4ax.com>`

```
In article <mn12455kek467ragti0psjk226p5hhi4ta@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>>2) use Edit to get MYUID.JCL.CNTL(DUMMY) (or any other member) and issue a 
>>BROWSE at the command line

[snip]

>I prefer VIEW as, I make lots of use of the EXCLUDE command.

That would be preferable, aye... but I think I was responding to your 
statement of 'I often choose TSO/ISPF to find particular records' and 
using EXCLUDE to find records is... well, a bit strange, at first glance.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T15:00:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chg245h20qanqf0el8q486g1776rash833@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <n5p145t34137moinutdq5a45blbpbfofot@4ax.com> <h1qsbv$r0t$1@reader1.panix.com> <mn12455kek467ragti0psjk226p5hhi4ta@4ax.com> <h1r4eh$fik$1@reader1.panix.com>`

```
On Tue, 23 Jun 2009 17:46:57 +0000 (UTC), docdwarf@panix.com () wrote:

>
>>I prefer VIEW as, I make lots of use of the EXCLUDE command.
…[3 more quoted lines elided]…
>using EXCLUDE to find records is... well, a bit strange, at first glance.

I do a lot of 
x all;f my-string all

I sometimes use the FLIP command
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:38:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad7ceF1u3a1dU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <6af2c4a5-7010-49f0-a976-24e05f21920d@d38g2000prn.googlegroups.com> <n5p145t34137moinutdq5a45blbpbfofot@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 22 Jun 2009 19:00:45 -0700 (PDT), riplin <riplin@Azonic.co.nz>
> wrote:
…[12 more quoted lines elided]…
> search abilities in that "obsolete" technology.

I worked with ISPF for a couple of decades and never complained about it. It 
always did what I wanted/needed and it was completely reliable and robust.

Nevertheless, having glimpsed another world, I realise we were deprived of 
facilities which we should have had in our COBOL IDE.

It's all really academic now...

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T13:56:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qmua$9tb$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net>`

```
In article <7aaojaF1v66vqU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7a886lF1s84o2U1@mid.individual.net>,
…[14 more quoted lines elided]…
>individual bits of it.

Perhaps my knowledge is antiquated, Mr Dashwood, but as I recall it *all* 
data manipulations are done in buffers (or areas of core similar 
thereunto)... remember RESERVE n AREAS?  Fine, there's a bunch of room in 
the buffer, sure... but then the data have to go *somewhere*.

>>
>> [snip]
…[8 more quoted lines elided]…
>C#,  Java, and Visual Basic ALL do it easily.

This confuses me; perhaps I did not state mysel clearly.  Given a 12-byte 
buffer (pardon my EBCDIC)

FFFFFFFCCEC
11111114135

... what language has the POWER to fill startpos 8, len 4 with

CCECECDC
41353945

without some manner of compression?  What would the data area look like?


>The actual operand(s) is/are 
>not compressed; the buffer which it/they occurs in is not changed in length 
>either.

The buffer (startpos 8, len 4) can contain 4 characters.  Unless there is 
a translation table someplace ('for this particular buffer starpos 8, len 
1, X'C4' = X'C4C1') there seems to be room for only four characters.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-23T13:18:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1r8450i0@news7.newsguy.com>`
- **In-Reply-To:** `<7aaojaF1v66vqU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> C#,  Java, and Visual Basic ALL do it easily. The actual operand(s) is/are 
> not compressed; the buffer which it/they occurs in is not changed in length 
> either.

They all allocate a new buffer and copy the data, replacing it as
necessary. The old buffer becomes available for garbage collection
when there are no more references to it. None of these languages
operate on the source data - it's not a mutable object.

> A Regular Expression can expand or compress replacement operands 
> within a buffer.

No, it can't. A regular expression itself doesn't change anything at
all - it's a format pattern-matching construct. More relevantly,
implementations of RE-based replacement algorithms almost always
operate on a copy-and-replace basis. Performing replacement on the
source data is much more computationally expensive, and even in the
best case only saves as much memory as the size of the source plus a
small constant.

And, again, you can do the same thing in any COBOL variant where you
can invoke an RE-based string-replacement facility. Which is pretty
much all of them.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:42:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad7jgF1ubcp7U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <h1r8450i0@news7.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[22 more quoted lines elided]…
> much all of them.

The description above was a functional one of how things appear to the user. 
You interpreted it, as Richard did, as being a description of how things 
work. That was never the intent.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-26T16:39:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h23dm60cpt@news2.newsguy.com>`
- **In-Reply-To:** `<7ad7jgF1ubcp7U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <h1r8450i0@news7.newsguy.com> <7ad7jgF1ubcp7U1@mid.individual.net>`

```
Pete Dashwood wrote:
> Michael Wojcik wrote:
>> Pete Dashwood wrote:
…[11 more quoted lines elided]…
> The description above was a functional one of how things appear to the user. 

We've discussed this issue already elsewhere in this thread (which has
developed an impressive degree of parallel redundancy :-), but this
comment made me aware of another factor contributing to the
disagreement that inspired a number of posts.

What Pete described was how the operation of Regex.Replace appeared to
him, as the programmer using it - a role in which he didn't feel
compelled to consider how it was working under the covers. (That's
often just fine. It's the whole point of abstraction and patterns,
after all - you have a pattern that's proven to solve a certain
problem under a general set of circumstances, so you use it.)

But to another user, that operation might appear to work quite
differently.

I've done quite a bit of work with functional languages. That's
trained me to distinguish between purely-functional operations and
ones with destructive side effects. A Replace operation that altered
its source is destructive (it doesn't guarantee that the original data
can be recovered). Regex.Replace, on the other hand, is purely
functional. So even as a user of a feature provided by the framework,
functional-vs-destructive is automatically one of the attributes I
consider.

And much of my work is in C. In C, the distinction between references
and values is explicit and important to the programmer; and tracking
allocations is explicit and important. So a C developer would
naturally notice that in a statement like:

   outBuffer = RegEx.Replace(outBuffer.ToUpper(), "TEXT(","Char(");

assignment is being performed, and the old value of outBuffer is being
discarded. That implies that Regex.Replace is returning a new value,
not modifying an existing one. By the same token, the fact that
outBuffer isn't even a parameter to Regex.Replace (explicitly, or
implicitly through invoking a method on it) implies that Regex.Replace
must be functional rather than destructive (unless we imagine that
ToUpper is destructive and returns a reference to the original object).

What this boils down to is that even in a given statement of code,
things which may be abstracted away for one programmer are obvious (or
important enough to demand researching) for another programmer. And
I'd suggest that distinction is a matter of each programmer's
particular experience, not an indication of who's the better programmer.

Similarly, someone who writes a lot of code for scientific data
processing may be very alert to questions of floating-point rounding
modes, signalling versus non-signalling NaNs, and such - things that
many of us have only the vaguest knowledge of. That becomes part of
how that code appears to that programmer - but it's not part of how it
appears to many others.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-28T15:19:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ao5pmF1vsqmeU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <h1r8450i0@news7.newsguy.com> <7ad7jgF1ubcp7U1@mid.individual.net> <h23dm60cpt@news2.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>> Michael Wojcik wrote:
…[67 more quoted lines elided]…
> appears to many others.

A very interesting post, Michael.

Do you think it is possible that programmer "interests" change over time as 
well?

There was a time when I loved playing with bytes (even bits, I have a strong 
affinity for Boolean Algebra and Propositional Calculus, and once wrote an 
entire executable program which read data and listed it using ONLY Boolean 
instructions and binary literals in ICL 1900 PLAN, for a bet. I was very 
young (around 21) at the time and the whole world of computing was just a 
big crossword puzzle and there for my entertainment... :-))

As time went by I become more subject to the pressures of actually producing 
stuff. When you're a junior programmer, you are pretty much cannon fodder; 
you are an inexpensive resource and no-one expects a great deal from you, so 
to at least some extent, you can indulge your personal interest. The same is 
not true for a Team Leader or Senior Programmer who is carrying part of the 
can for the system under development. Contract programmers and Consultants 
are perceived as expensive resources and expected to deliver, or they won't 
be around very long. All of this has a subtle effect on a person's approach 
to programming. Since the invention of the Personal Computer, we can indulge 
our personal interests without misusing company hardware, but these days, at 
the end of a day in the cubicle, most of us are not interested in hobby 
programming.

For myself, I simply don't care about how things work when I'm writing code 
(except at the really grossest level; obviously, I don't do things that are 
wildly inefficient, and even the COBOL sample for replacing different length 
operands which I posted here is relatively "efficient"), but I honestly 
don't believe it so important any more and I write this way because it "used 
to matter" rather than because "it still matters", for anything but the most 
specific applications.

I like the levels of abstraction which enable me to work at a "higher 
level", and that is probably why I have taken to OO, where I can deal with 
objects and behaviours rather than the mind numbing details of how those 
behaviours are produced (even if I actually wrote the methods myself 
originally).

Since the recent interchange I have become more aware of watching C# 
functions (and thinking about why some of them are provided... :-))  but I 
still remain primarily interested in getting results.

Your posts have been thought provoking.

Thanks.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-07-14T15:07:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h3il970bv2@news1.newsguy.com>`
- **In-Reply-To:** `<7ao5pmF1vsqmeU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <h1r8450i0@news7.newsguy.com> <7ad7jgF1ubcp7U1@mid.individual.net> <h23dm60cpt@news2.newsguy.com> <7ao5pmF1vsqmeU1@mid.individual.net>`

```
[Sorry to take so long to respond - I'm on vacation and haven't been
reading Usenet for a while. This was in response to my post about how
a programmer's training and interests shape the mental models that
programmer uses, and condition which details are important and which
can be abstracted away.]

Pete Dashwood wrote:
> 
> Do you think it is possible that programmer "interests" change over time as 
> well?

Definitely. When I first began to write code, in BASIC on the
Commodore PET (an early personal computer), my main concerns was
control flow. I was writing little experimental programs that didn't
do anything significant in terms of data storage or real processing.

One interesting consequence: I thought of variables essentially as
names for pieces of data that once assigned didn't change during a run
of the program. I still remember a key insight I had very early on
when learning to program. A friend and I were in some sort of
"computer camp" (we must have been in junior high at the time),
writing a program to display the simple Fibonacci sequence in BASIC.
We started with something like:

10 LET A=1
20 LET B=1
30 LET C=A+B
40 PRINT A
50 PRINT B
60 PRINT C

As we were trying to figure out how to go on to the next number in the
sequence in a general way that would let us compute N terms, we
realized that *we no longer needed A, and we could assign it the
current value of C*. So rather than have A, B, and C be the first
three terms of the sequence, they could be the two most recently
computed terms and their sum.

I think that was the first time I thought of programs in terms of
functions, rather than in terms of a recipe - that is, as a list of
ingredients and steps for putting those ingredients together.

> There was a time when I loved playing with bytes (even bits, I have a strong 
> affinity for Boolean Algebra and Propositional Calculus, and once wrote an 
…[3 more quoted lines elided]…
> big crossword puzzle and there for my entertainment... :-))

I think that's how lots of programmers learn to stretch their mental
models - by treating it as a game and giving themselves challenges.

> As time went by I become more subject to the pressures of actually producing 
> stuff. When you're a junior programmer, you are pretty much cannon fodder; 
…[3 more quoted lines elided]…
> can for the system under development.

That's often true, though sometimes senior folk are given
responsibility to research some new area, and get to do some of that
playing around. (In the Scrum methodology, that's called a "spike" - a
prototype for a complex new piece of functionality that's isn't
understood well enough yet to break into functional pieces for
scheduling.)

> Contract programmers and Consultants 
> are perceived as expensive resources and expected to deliver, or they won't 
> be around very long. All of this has a subtle effect on a person's approach 
> to programming.

Sure. So can other constraints, such as security and legal compliance,
which can add to the cost of trying new things.

> I like the levels of abstraction which enable me to work at a "higher 
> level", and that is probably why I have taken to OO, where I can deal with 
> objects and behaviours rather than the mind numbing details of how those 
> behaviours are produced (even if I actually wrote the methods myself 
> originally).

Yes, and this tension - between needing to know implementation
details, and working at higher levels of abstraction - exists in lots
of fields. If I'm in industrial logistics, say, I want to know about
relative costs of different shipping methods for various kinds of
cargo and routes. But I don't need to know if one of my subcontractors
uses Volvo trucks or Mitsubishi ones, as long as they can provide a
certain known level of service with good probability.

If I'm a woodcarver, I might want to know what kind of steel my
chisels are made from - or maybe I just know that such-and-such a
brand is a reliable product, and I don't care about carbon content and
that sort of thing.

Agile development methodologies try to help people determine the
appropriate level of abstraction, with principles like "good enough",
rapid releases, and incremental improvement.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-23T13:35:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1r8462i0@news7.newsguy.com>`
- **In-Reply-To:** `<7aaojaF1v66vqU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net>`

```
Pete Dashwood wrote:
> docdwarf@panix.com wrote:
>> In article <7a886lF1s84o2U1@mid.individual.net>,
…[11 more quoted lines elided]…
> individual bits of it.

Of course, the INSPECT verb can't know that until it performs the
replacements. So if it allowed replacement text that was larger than
the source text, the standard would have to determine how to handle
overflow - probably with truncation and an ON OVERFLOW optional
clause, but that significantly complicates the semantics of the verb.
The language spec tries to strike a balance between addressing the
needs of developers and considering the resources of implementors.

REPLACING where replacement text is shorter than source text doesn't
raise the issue of overflow, of course, but it still offers the
complication of shifting data in the buffer, and without also allowing
longer replacements it doesn't offer that much additional functionality.

That said, would it be nice if REPLACING supported longer and shorter
replacements? Sure. Of course, then you'd need to support INSPECT ...
ON OVERFLOW. And maybe EXAMINE ... REPLACING should support
replacements that aren't a single byte. And maybe there should be a
MOVE ... REPLACING.

Or perhaps COBOL programs should just use functionality in the
environment for this sort of thing, rather than language built-ins.

It's true that COBOL tries to include a lot of functionality in the
language syntax itself - functionality that most later languages
(particularly everything influenced by C) provide as explicit library
calls or the equivalent. That's really just syntactic sugar; COBOL
verbs can be implemented as library calls, and library calls in other
languages can be expanded inline.

The problem with COBOL that Pete's highlighted here is that the
presence of syntactic sugar like the REPLACING verb in COBOL leads the
programmer to expect to be able to accomplish certain things using the
base language syntax that are really better left to special-function
libraries (or "modules" or "assemblies" or what have you). That, I
think, is the real source of frustration - COBOL's kitchen-sink
approach is disappointing when you want something that's almost but
not quite available in the base language.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:44:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad7mrF1si0hsU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <h1r8462i0@news7.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>> docdwarf@panix.com wrote:
…[51 more quoted lines elided]…
> not quite available in the base language.

Yep, that sums it up nicely. Thank you, Michael.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-06-25T23:37:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2gY0m.221609$Xo1.96799@en-nntp-07.dc1.easynews.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net>`

```
See my other note.  Although INSPECT REPLACING doesn't do what you want, 
UNSTRING, INSPECT/REPLACING (or even MOVE) followed by STRING would do it.

Or as your original note indicated, a PERFORM loop would also do it.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-26T10:08:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<his945ho5pg6e4pp48hvjtrvscphvge59e@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5fgmF1tcqi6U1@mid.individual.net> <4ebbf249-1c38-4408-9885-a23dce1d6879@d19g2000prh.googlegroups.com> <7a886lF1s84o2U1@mid.individual.net> <h1o946$2s5$1@reader1.panix.com> <7aaojaF1v66vqU1@mid.individual.net> <2gY0m.221609$Xo1.96799@en-nntp-07.dc1.easynews.com>`

```
On Thu, 25 Jun 2009 23:37:15 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>See my other note.  Although INSPECT REPLACING doesn't do what you want, 
>UNSTRING, INSPECT/REPLACING (or even MOVE) followed by STRING would do it.
>
>Or as your original note indicated, a PERFORM loop would also do it.

I have found most of my string/unstring commands and some of my
inspect/replacing commands have been replaced by reference
modification loops, which are clearer and fast.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-21T14:19:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net>`

```
On Jun 21, 1:08 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> riplin wrote:
> > On Jun 21, 5:22 am, "Pete Dashwood"
> > <dashw...@removethis.enternet.co.nz> wrote:

Here's how to use a UNSTRING WITH POINTER / STRING loop. Do this once
in your lifetime.

       IDENTIFICATION DIVISION.
       PROGRAM-ID.      "replace".
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  tobuffer             PIC X(16384).
       01  workbuffer           PIC X(16384).
       01  FPoint               PIC S9(6).
       01  TPoint               PIC S9(6).
       01  slen                 PIC S9(6).
       01  tlen                 PIC S9(6).
       01  wlen                 PIC S9(6).
       01  WorkDelimiter        PIC X(128).
       LINKAGE SECTION.
       01  buffer               PIC X(16384).
       01  sfrom                PIC X(128).
       01  sto                  PIC X(128).
       PROCEDURE DIVISION USING buffer sfrom sto.
       Replace-String.

           MOVE SPACES        TO tobuffer
                                 workbuffer
                                 WorkDelimiter
           MOVE 1             TO FPoint
                                 TPoint
           MOVE ZERO          TO slen
                                 tlen
           INSPECT sfrom TALLYING slen
               FOR CHARACTERS BEFORE LOW-VALUE
           INSPECT sto TALLYING tlen
               FOR CHARACTERS BEFORE LOW-VALUE

           PERFORM
               UNTIL WorkDelimiter(1:1) = LOW-VALUE

               MOVE ZERO     TO wlen
               UNSTRING buffer
                   DELIMITED BY sfrom(1:slen)
                             OR LOW-VALUE
                   INTO Workbuffer
                       DELIMITER IN WorkDelimiter
                       COUNT IN wlen
                   WITH POINTER FPoint

               STRING workbuffer(1:wlen)
                   DELIMITED BY SIZE
                   INTO tobuffer
                   WITH POINTER TPoint

               IF ( WorkDelimiter(1:1) = LOW-VALUE )
                   STRING WorkDelimiter(1:1)
                       DELIMITED BY SIZE
                       INTO tobuffer
                       WITH POINTER TPoint
               ELSE
                   STRING sto(1:tlen)
                       DELIMITED BY SIZE
                       INTO tobuffer
                       WITH POINTER TPoint
               END-IF
           END-PERFORM
           MOVE tobuffer        TO buffer
           .

Then you can use this just as you use the regex.replace:

       IDENTIFICATION DIVISION.
       PROGRAM-ID.      testreplace.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  blen               PIC S9(6).
       01  buffer             PIC X(16384) VALUE
       "This has two Date(8) strings in it Date(2) here." & LOW-VALUE.


       PROCEDURE DIVISION.
       Replace-Test.

           CALL "replace" USING buffer
                                "Date(" & LOW-VALUE
                                "DATETIME(" & LOW-VALUE

           MOVE ZERO     TO blen
           INSPECT buffer TALLYING blen
               FOR CHARACTERS BEFORE INITIAL LOW-VALUE
           DISPLAY buffer(1:blen)
           .
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T13:53:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a86gqF1u0qurU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com>`

```
riplin wrote:
> On Jun 21, 1:08 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[92 more quoted lines elided]…
>            .
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T13:56:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a86ldF1td595U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com>`

```
Thank you, Richard.

It is good code.

But I prefer to use ONE line...

(BTW, I have used UNSTRING with POINTER on numerous occasions)

Pete.

TOP POST - nothing new below.


riplin wrote:
> On Jun 21, 1:08 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[92 more quoted lines elided]…
>            .
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-21T19:38:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3e8cdd1-abac-4d64-96f2-17f4422c08f6@y34g2000prb.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com> <7a86ldF1td595U1@mid.individual.net>`

```
On Jun 22, 1:56 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Thank you, Richard.
>
> It is good code.
>
> But I prefer to use ONE line...

There yer go: one line

  CALL "replace" USING buffer "Date(" & x"00" "DATETIME(" & x"00"


> (BTW, I have used UNSTRING with POINTER on numerous occasions)
>
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:07:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rf7v3511mr6lmg6s7tokmmlge9k1u5po5c@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com> <7a86ldF1td595U1@mid.individual.net>`

```
On Mon, 22 Jun 2009 13:56:04 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>But I prefer to use ONE line...

Sometimes someone has a reason for his preferences - other times, it
is just taste.   Nothing wrong with the latter.   But do you have a
reason to prefer one line?
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T13:15:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aaokoF1uqodhU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com> <7a86ldF1td595U1@mid.individual.net> <rf7v3511mr6lmg6s7tokmmlge9k1u5po5c@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 22 Jun 2009 13:56:04 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[5 more quoted lines elided]…
> reason to prefer one line?

The less code I write, the fewer errors I make.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T14:15:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qo23$inb$3@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a86ldF1td595U1@mid.individual.net> <rf7v3511mr6lmg6s7tokmmlge9k1u5po5c@4ax.com> <7aaokoF1uqodhU1@mid.individual.net>`

```
In article <7aaokoF1uqodhU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>Howard Brazee wrote:
>> On Mon, 22 Jun 2009 13:56:04 +1200, "Pete Dashwood"
…[8 more quoted lines elided]…
>The less code I write, the fewer errors I make.

A logical conclusion of this would be that your error-free programs 
consist of no code written by you, Mr Dashwood.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:46:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad7psF1uoq4mU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a86ldF1td595U1@mid.individual.net> <rf7v3511mr6lmg6s7tokmmlge9k1u5po5c@4ax.com> <7aaokoF1uqodhU1@mid.individual.net> <h1qo23$inb$3@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7aaokoF1uqodhU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[15 more quoted lines elided]…
> DD

Or, as is actually the case back in the real world, the errors were fixed by 
a process colloquially referred to as "debugging"...

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-24T00:57:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1rtle$pv4$2@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7aaokoF1uqodhU1@mid.individual.net> <h1qo23$inb$3@reader1.panix.com> <7ad7psF1uoq4mU1@mid.individual.net>`

```
In article <7ad7psF1uoq4mU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7aaokoF1uqodhU1@mid.individual.net>,
…[17 more quoted lines elided]…
>a process colloquially referred to as "debugging"...

If 'the less code I write' is equated to 'the less code that is written by 
me' (I believe Rules of Grammar permit this) then the debugging you refer 
to seems to center on removing as much of the code written by you as 
possible so fewer errors remain... wonderful language, this English.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T08:50:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9up145dn2m2ti313ellskmd57td5qb1jas@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com> <7a86ldF1td595U1@mid.individual.net> <rf7v3511mr6lmg6s7tokmmlge9k1u5po5c@4ax.com> <7aaokoF1uqodhU1@mid.individual.net>`

```
On Tue, 23 Jun 2009 13:15:06 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Sometimes someone has a reason for his preferences - other times, it
>> is just taste.   Nothing wrong with the latter.   But do you have a
>> reason to prefer one line?
>
>The less code I write, the fewer errors I make.

OK.

But for me - 

The fewer shortcuts I take, the easier it is to figure out what I
wrote.

Also, since this is a CoBOL group - we have all come across
abbreviation problems, trying to remember whether the variable is
ACCT-NBR or ACCTNG-NUM.    I make fewer errors typing it out.

In CoBOL, there is more typing in typing END-IF as opposed to typing a
period.    I suspect there are fewer errors with the former.

Admittedly, you are comparing CoBOL with other languages - which I can
do too - how about the very concise RPG?

Nah, for me, I don't find a strong correlation between less code and
fewer mistakes - for the same desired result.

YMMV.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:55:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad8bbF1sf4biU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com> <7a86ldF1td595U1@mid.individual.net> <rf7v3511mr6lmg6s7tokmmlge9k1u5po5c@4ax.com> <7aaokoF1uqodhU1@mid.individual.net> <9up145dn2m2ti313ellskmd57td5qb1jas@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 23 Jun 2009 13:15:06 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[16 more quoted lines elided]…
> ACCT-NBR or ACCTNG-NUM.    I make fewer errors typing it out.

Yep. Many times. That's why I love Intellisense... it won't let you make 
those mistakes and if there is ambiguity, it spots that too and makes you 
choose. It does the same with procedure (Method) names, even popping up a 
prototype of what parameters are required and their datatypes, whenever you 
reference them. How often have you written a PERFORMed routine then not been 
quite sure what you called it? No more... Visual Studio rules...

>
> In CoBOL, there is more typing in typing END-IF as opposed to typing a
> period.    I suspect there are fewer errors with the former.

I'd agree. But if the IDE can type "end-if" for me then it isn't a problem 
is it?


>
> Admittedly, you are comparing CoBOL with other languages - which I can
> do too - how about the very concise RPG?

Yeah, how 'bout that RPG? Reckon they'll take the Rose Bowl this year... :-)

>
> Nah, for me, I don't find a strong correlation between less code and
> fewer mistakes - for the same desired result.

Because you correct the mistakes in the debugging and testing phases of your 
development.

"fewer mistakes" Is not the ONLY reason I prefer concise code, but it is a 
major one.

(Another reason is that it is quicker to read and pick up what code is doing 
if it was written by someone else, when there is less of it.)

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-24T06:36:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cb7445husood30p8k9btvusgilee67j2qk@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <7a5fgmF1tcqi6U1@mid.individual.net> <eb5bdb82-f6fc-4563-b7ef-9fc275306d67@z8g2000prd.googlegroups.com> <7a86ldF1td595U1@mid.individual.net> <rf7v3511mr6lmg6s7tokmmlge9k1u5po5c@4ax.com> <7aaokoF1uqodhU1@mid.individual.net> <9up145dn2m2ti313ellskmd57td5qb1jas@4ax.com> <7ad8bbF1sf4biU1@mid.individual.net>`

```
On Wed, 24 Jun 2009 11:55:21 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:


>> Also, since this is a CoBOL group - we have all come across
>> abbreviation problems, trying to remember whether the variable is
…[7 more quoted lines elided]…
>quite sure what you called it? No more... Visual Studio rules...

Which tool assists us in overcoming some of the shortcomings of
conciseness.
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-21T16:33:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1lnd1$ll9$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com>`

```
In article <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com>,
riplin  <riplin@Azonic.co.nz> wrote:

[snip]

>It seems that you rant about this because you have come late to the
>newer languages and are a 'born again' programmer.

Everybody's a psychologist... Mr Plinston, Mr Dashwood seems to be 
complaining that COBOL cannot be used, in an easy and simple fashion, as a 
text-processing language.

'Durned screwdriver... why can't it thread a rod properly?'

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T14:03:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a873aF1u33geU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article
> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com>,
…[11 more quoted lines elided]…
> 'Durned screwdriver... why can't it thread a rod properly?'

Fair comment and similar to the one from HeyBub.

The problem is not that COBOL isn't a text processing language, it is that 
other, more powerful screwdrivers CAN thread a rod properly (as well as 
drive screws...)

The thread is about POWER of languages.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-21T19:34:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net>`

```
On Jun 22, 2:03 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> docdw...@panix.com wrote:
> > In article
…[20 more quoted lines elided]…
> The thread is about POWER of languages.

But this isn't being done by the language (syntax), it is being done
by a set of routines that is outside the language itself.

My replace routine is just like (except for some restrictions) how you
used the regex.replace() routine. Maybe regex.replace() is actually
written in C# or maybe it is in C or assembler.

It happens that with C# (and several others) these routines are
provided with the run time.

Just because you can write a text editor in C# does not mean that I
should rewrite my accounting applications into C# (or Python or
Java).

As it happens I use multiple languages, I do have templating routines
and programs in Cobol because they were written before it was viable
to use C, let alone Java or C#. I also have some written in C before
Python was viable when I extended the system to cater for merging data
into postscript templates. I also have stuff in Python because that is
what new stuff uses.  My Cobol programs can call or execute the other
language programs, so stuff uses whatever is suitable.


> Pete.
> --
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T15:22:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a8bmkF1ssfdaU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com>`

```
riplin wrote:
> On Jun 22, 2:03 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[25 more quoted lines elided]…
> by a set of routines that is outside the language itself.

And languages that can deal with sets of routines outside themselves and 
written in ANY language (because the source is totally unimportant) are 
perceived as more POWERFUL than languages that can't do that. That is the 
nub of my argument. COBOL cannot currently do it and that is one reason why 
it is losing the POWER battle.
>
> My replace routine is just like (except for some restrictions) how you
> used the regex.replace() routine. Maybe regex.replace() is actually
> written in C# or maybe it is in C or assembler.

Three things:

1. What is written in is immaterial; it is the functionality that is 
important.
2. _I_ didn't have to write it. (Not even ONCE in a lifetime...)
3. It is at my fingertips, providing the FUNCTIONALITY I need, when I need 
it.

>
> It happens that with C# (and several others) these routines are
…[12 more quoted lines elided]…
> language programs, so stuff uses whatever is suitable.

That is a desirable situation. Most people cannot enjoy it.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-21T22:22:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net>`

```
On Jun 22, 3:22 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> riplin wrote:
> > On Jun 22, 2:03 pm, "Pete Dashwood"
…[32 more quoted lines elided]…
> it is losing the POWER battle.

That is _NOT_ a language issue. It is an implementation issue. A .NET
based implementation of Cobol would be able to use those routines.
OpenCobol and Fujitsu can (or should be able to) use all C routines
and any libraries written in C.

An OO Cobol should work fine with C++ or C# or Java (depending on
implementation).

It is likely that MS's C# won't use Java libraries or vv, but an
implementation of C# on the JVM could, and vv.

It happens that most Cobol users, especially mainframes, don't want to
write the types of applications that need the stuff in the C#
libraries (not language), or if they did they would use Rexx or Object
Rexx.


> > My replace routine is just like (except for some restrictions) how you
> > used the regex.replace() routine. Maybe regex.replace() is actually
…[8 more quoted lines elided]…
> it.

> > It happens that with C# (and several others) these routines are
> > provided with the run time.
…[13 more quoted lines elided]…
> That is a desirable situation. Most people cannot enjoy it.

So why are you promoting C# to people who cannot 'enjoy' it ?



> --
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T21:57:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a92rlF1t3g44U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com>`

```
riplin wrote:
> On Jun 22, 3:22 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[85 more quoted lines elided]…
>

I'm not "promoting" anything and I'm not on commision for C#.

I'm relaying my own personal experience and calling it like I see it. (I 
have done that consistently in this forum ever since it was started).

The FACT is that COBOL is declining in popularity. (Partly because it is 
perceived, rightly in my opinion, as being less powerful than alternatives 
now available, of which C# is one.) That means that even mainframe shops 
will eventually have to move off it. (If the "mainframe shop" actually 
survives without being reincarnated as somethig quite different...) There 
are also a number of COBOL sites running on client server that want to move 
off it but see no path that allows them to without simply starting over, or 
perpetuating COBOL because they see no alternative.

This is precisely the dilemma I faced myself a few years back.

I had a very large investment in COBOL, I couldn't get even reasonable 
support from the COBOL vendor, and it was costing me money every year for 
maintenance and support that was not forthcoming. Long term it would have 
been a disaster. Biting the bullet and moving to .NET was a desirable 
outcome, but I needed another expensive COBOL compiler in order to do it and 
it wasn't getting me out of COBOL long term.

The C# compiler is free, the VS Express version is free so I downloaded them 
both and tried them out. I searched for and found some really useful video 
tutorials (also free) that got me off the ground, and took it form there. It 
was a very pleasant experience and probably the best thing I ever did as far 
as my own software goes.

If I appear to be "promoting C#" that's the reason for it.

Judging by queries I am receiving from the COBOL21 web site, there are a 
number of people (more than I anticipated when I wrote the web site, and, 
interestingly, most of whom have never posted to this forum and are unknown 
to me) who are looking for an alternative for the long term. I see C#/.NET 
as being a very viable one.  I'm not saying it is the "only way", I'm saying 
it is the way I have walked and I'm more than satisfied with the journey. 
(Although it is "early days" the client's I have are also happy with this 
approach. People don't have to go "all the way". They can stay with COBOL or 
move to C#, but at least they have an OPTION...)

The important thing is to be able to leverage the COBOL you currently have 
and bring it into the new environment. Wrapping it as OO components does 
that. At the same time, moving from ISAM to a tiered RDB layer, also 
composed of components that can run in any environment, insulates sites 
against future changes in RDB technology (and there are some very 
interesting ones in the pipeline).

All of this is a lot of work if you have to do it manually and I wrote 
(primitive) tools to help me do it. As more people are showing interest in 
doing the same, I have improved and enhanced these tools. Today, a process 
that took me around 9 months can be done in a couple of weeks with the aid 
of tools that are no longer primitive. Most of the process is fully 
automated, right down to changing the source code in existing applications 
so it can invoke the DB objects instead of using ISAM. I'll be posting more 
about this (with demo screen shots) to the COBOL 21 web site as soon as I 
can manage to get some time.

The next big challenge is refactoring the COBOL code, which is still largely 
a manual process. Standard procedures for doing it have been devised, and 
experience has been gained but so far, it isn't automated. (This wasn't a 
big deal for me personally as most of my COBOL code was already 
components...)

If there are any volunteers to assist with this please mail me :-) I don't 
care what language you write it in as long as your solution is component 
based and wrapped as COM. Visual interface is unimportant as long as your 
modules clearly define what data they use and what processes they do with 
it(The COM wrapping isn't too important as I can show you how to do that 
very quickly if you use Fujitsu COBOL (I'm hoping to have some Micro Focus 
examples soon, but don't have any right now.)) The main thing is that the 
code should work. It would be exactly the same process as we demonstrated 
for Robert's COBDATA tool on the cobol21 web site, where standard COBOL was 
wrapped as COM and run in .NET ) The kind of things I would be interested in 
looking at are:

1. Processing COBOL source and identifying blocks of code that can be 
separated into separate components. (PERFORMED routines, CALLed modules, and 
inline code that is coherent, would all be prime candidates.)  The idea is 
to "decompose" an existing COBOL application into logical functions that can 
be encapsulated. There needs to be a way of getting the data field 
definitions that are referenced in the procedure code and building a new 
souce module that can compile as a callable subroutine. It's an interesting 
task and I'd love to be doing it, but I am way too busy with the existing 
tools right now.

2. Something that can process the same source as above and identify the 
control code and sequences from the refactored components. This probably 
needs to be a second step, after refactoring, because it isn't until that is 
done that you can know what is available as a component. It might produce a 
report or chart showing the sequence in which the components are activated 
currently.  If you want to get REALLY sexy, write it as a windows 
application where components and control actions (boxes?) can be visually 
dragged and dropped around the screen. Once you have a visual representation 
on the screen of the control and component flow, produce a compilable source 
in the language of your choice. (This is similar to the SSIS application I 
noted recently. In fact, it might be achieved by scripting SSIS if that is 
possible. I haven't had a chance to look at it...)

Maybe we need a separate thread to discuss this... I'll start one.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:29:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sl8v35tcn5hhnjuq01t1mpgml5i0mgh78e@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com> <7a92rlF1t3g44U1@mid.individual.net>`

```
On Mon, 22 Jun 2009 21:57:06 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>The next big challenge is refactoring the COBOL code, which is still largely 
>a manual process. Standard procedures for doing it have been devised, and 
>experience has been gained but so far, it isn't automated. (This wasn't a 
>big deal for me personally as most of my COBOL code was already 
>components...)

I am unconvinced there is a big need to refactor CoBOL code.   I
believe most shops will replace their CoBOL by replacing their IS
system.   They will buy existing packages and modify them to fit their
business requirements.    Existing *data* will be analyzed and
migrated, but existing programs won't be a significant part of this
process.

If the new system is written with a lot of CoBOL, fine.   If not, that
works too.    But shoehorning the old code into the new system doesn't
make business sense.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T13:31:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aapinF1uistrU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com> <7a92rlF1t3g44U1@mid.individual.net> <sl8v35tcn5hhnjuq01t1mpgml5i0mgh78e@4ax.com>`

```
Howard Brazee wrote:
> On Mon, 22 Jun 2009 21:57:06 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[12 more quoted lines elided]…
> process.

That is certainly true in some cases. Nevertheless, don't you think it is 
good to have OPTIONS?

One company I worked for had a very complex pricing plan, implemented in 
COBOL. It contained special deals for special customers
, promises made by salesmen in order to close deals, and a lot of historical 
stuff that wasn't documented anywhere. When I first encountered it as the 
new manager, I suggested we should take it apart and rewrite it. because it 
was a maintenance nightmare. There were general looks of 
consternation...They said it would take forever and was unnecessary as it 
worked fine ("If it ain't broke, don't fix it..."). I had a look through the 
code and could see their point... What we did was start a new pricing plan 
with standard pricing and extend that for special deals. We never maintained 
the "old" plan, but referred to it if a product or service was keyed in it. 
So it became an encapuslated black box that just did it's job. That would be 
a perfect candidate for salvage into any new system they decided to 
implement. That's just one example. There are cases where complex business 
rules are embodied in COBOL code. If it can be salvaged, that has to be a 
better option than starting again from scratch. (Provided that the cost of 
salvaging is way below the cost of rewriting. If the refactoring can be 
automated, that immediately reduces the cost of salvage.)




>
> If the new system is written with a lot of CoBOL, fine.   If not, that
> works too.    But shoehorning the old code into the new system doesn't
> make business sense.

It does if the cost of salvage is WAY LESS than the cost of rebuilding. And 
the two are not mutually exclusive. (Why would you be "shoehorning"? The new 
environment has unlimted space... You may salvage a lot, salvage some, or 
salvage none at all. Wrapping the code so it can run in the new environment 
as just another object, is a very useful way to go.

It gives you options...

Thanls for your response, Howard.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T08:53:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nuq145tb627b4r42ihm6rc5cars01261q9@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com> <7a92rlF1t3g44U1@mid.individual.net> <sl8v35tcn5hhnjuq01t1mpgml5i0mgh78e@4ax.com> <7aapinF1uistrU1@mid.individual.net>`

```
On Tue, 23 Jun 2009 13:31:05 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> I am unconvinced there is a big need to refactor CoBOL code.   I
>> believe most shops will replace their CoBOL by replacing their IS
…[6 more quoted lines elided]…
>good to have OPTIONS?

Sure.   Note the word "big" in the first line.

If the costs are right, encapsulating old code can be an option that
will sometimes be taken over analyzing the business needs and adapting
more than the language to new order.   Heck, lots of us CoBOL
programmers have jobs because of such attitudes.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:56:39+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad8dpF1s8tjfU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com> <7a92rlF1t3g44U1@mid.individual.net> <sl8v35tcn5hhnjuq01t1mpgml5i0mgh78e@4ax.com> <7aapinF1uistrU1@mid.individual.net> <nuq145tb627b4r42ihm6rc5cars01261q9@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 23 Jun 2009 13:31:05 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[16 more quoted lines elided]…
> programmers have jobs because of such attitudes.

Right... :-)

Pete
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T08:56:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<25r1455i9okukaphsked8dspbkh2h2t6vs@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com> <7a92rlF1t3g44U1@mid.individual.net> <sl8v35tcn5hhnjuq01t1mpgml5i0mgh78e@4ax.com> <7aapinF1uistrU1@mid.individual.net>`

```
On Tue, 23 Jun 2009 13:31:05 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> If the new system is written with a lot of CoBOL, fine.   If not, that
>> works too.    But shoehorning the old code into the new system doesn't
…[6 more quoted lines elided]…
>as just another object, is a very useful way to go.

If the new system is to do things the old way with new tools, it is
not shoehorning.

If the new system is adapted to new ways of doing business, then we
can adapt the old wing-tipped shoes to the new running environment.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-22T16:16:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1oaol$rm7$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com> <7a92rlF1t3g44U1@mid.individual.net>`

```
In article <7a92rlF1t3g44U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>The FACT is that COBOL is declining in popularity.

Mr Dashwood, the FACT was that, once upon a time, instructions were given 
to computers by plugging in wires.  That declined in popularity.

The FACT was that, once upon a time, cards in objectd decks were corrected 
by sitting down at the keypunch and re-punching the card.  That declined 
in popularity.

The FACT was that Assembley language was the easiest way for (some) folks 
to communicate necessary instructions to the Assembler to be rendered into 
object decks.  Time passed.

The FACT was that FORTAN and COBOL were the most common and 
readily-available languages to communicate these instructions... and, give 
or take a few million lines, still do what they were told to do.

The FACT was that Artificial Intelligence and Fourth-Generations languages 
were going to render all the preceding worthless... whoopsie!

The flowers of the field grow, blossom, go to seed and the next generation 
arrives... some the same, some mutated.  The environment (my apologies to 
the Creationists) will then determime which are most suited to survive.

We speak of a discipline in which ENIAC was unveiled about sixty years 
ago.

It took fifty years for factory design to shift from central-shaft 
water-driven design to decentralised, electricity-driven design.

That's almost... a FACT.

We are dealing here with something very, *very* young.  The Curtiss-JN4 
first saw service around 1915.  Forty-some years later the Boeing 707 was 
introduced.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T13:33:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aapn2F1ubofpU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com> <7a92rlF1t3g44U1@mid.individual.net> <h1oaol$rm7$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7a92rlF1t3g44U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[41 more quoted lines elided]…
> DD

I enjoyed your post, Doc, but I have no idea what it was about... :-)

Could you be a little less obtuse, please, for a simple mind such as mine?

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T14:18:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qo7c$inb$4@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a92rlF1t3g44U1@mid.individual.net> <h1oaol$rm7$1@reader1.panix.com> <7aapn2F1ubofpU1@mid.individual.net>`

```
In article <7aapn2F1ubofpU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7a92rlF1t3g44U1@mid.individual.net>,
…[45 more quoted lines elided]…
>Could you be a little less obtuse, please, for a simple mind such as mine?

Sorry, my apologies, I forgot that Managers prefer bullet-points.

 - Things change.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T11:58:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad8gnF1uu4mkU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a92rlF1t3g44U1@mid.individual.net> <h1oaol$rm7$1@reader1.panix.com> <7aapn2F1ubofpU1@mid.individual.net> <h1qo7c$inb$4@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7aapn2F1ubofpU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[55 more quoted lines elided]…
>

Ah, got it now...

Thanks.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-24T00:59:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1rtpb$pv4$3@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7aapn2F1ubofpU1@mid.individual.net> <h1qo7c$inb$4@reader1.panix.com> <7ad8gnF1uu4mkU1@mid.individual.net>`

```
In article <7ad8gnF1uu4mkU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> - Things change.
>>
>
>Ah, got it now...

Don't worry, they're working on a cure!

>Thanks.

Anytime.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:25:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4f8v35dq4gps2v8ckaf2j9fp8o836139gm@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net> <ff39ac26-02aa-4532-bdb5-19bdd15533a3@p6g2000pre.googlegroups.com>`

```
On Sun, 21 Jun 2009 22:22:00 -0700 (PDT), riplin <riplin@Azonic.co.nz>
wrote:

>That is _NOT_ a language issue. It is an implementation issue. A .NET
>based implementation of Cobol would be able to use those routines.
>OpenCobol and Fujitsu can (or should be able to) use all C routines
>and any libraries written in C.

Implementation issue or not - it's the way people see the language.   

I'm reminded of a security person who says there is no security
problem - he gave everybody instructions to use long randomly
generated passwords, to never write them down, and to never use the
same or similar password twice.     I guess his understanding of human
nature is that we can remember a dozen (hundred) different random
passwords with confidence.

Or he thinks security has nothing to do with human nature.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:22:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ci7v35hee9u18or49a7qlj69mtm0fa36s8@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <22f18d6d-5a5c-482f-9f28-c4e3743d7a2e@y34g2000prb.googlegroups.com> <7a8bmkF1ssfdaU1@mid.individual.net>`

```
On Mon, 22 Jun 2009 15:22:02 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>And languages that can deal with sets of routines outside themselves and 
>written in ANY language (because the source is totally unimportant) are 
>perceived as more POWERFUL than languages that can't do that. That is the 
>nub of my argument. COBOL cannot currently do it and that is one reason why 
>it is losing the POWER battle.

Power is attractive.    But it can lead to vulnerabilities.   The
obvious examples are when programmers design operating systems and
Internet interfaces to do nifty things - which nifty abilities have
been exploited by bad guys.

Less obvious are when a production program depends upon a routine that
came with someone else's software - but which is no longer supported.
For instance Apple's Snow Leopard won't support some old Apple
technologies, and won't work at all in non-Intel Macs.    Or we could
have used an interface to an old spreadsheet program or other tool
which our company is wanting to move past.

A hope is that ease of writing new programs will mean that when the
old system breaks - we will just replace it, instead of replacing
those vulnerable components with new components that sort of almost do
the same thing (but more safely).    But that doesn't mean that this
new paradigm doesn't have its own costs. 

Our industry - like most all industries, has had a history of
underestimating costs of new technologies (we're good at seeing the
benefits).    We did not sufficiently anticipate that when we moved to
client-server environments the application programming effort that we
saved would be countered by more systems programming to control
security, privacy, and connectivity.

I also remember estimates about how much re-use of components we would
have going OO, but see shop after shop that re-create components at a
far greater rate than anticipated.   It's easier to write something
new than to find the exact right component - and be confident that it
would always be available, reliable, and optimal.

Obviously - well, maybe not as obvious as it should be - we won't be
going back to the way we sort of remember things should have been in
our past.  (Conservative values rarely go back before our individual
pasts).    But (even though Liberal values usually assume we finally
have figured what needs to be done), there are costs to our current
ways of doing things - and to whatever ways replace it sooner than we
expect.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-22T15:54:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1o9f0$2s5$2@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net>`

```
In article <7a873aF1u33geU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article
…[18 more quoted lines elided]…
>drive screws...)

One may be able to thread a rod with a screwdriver, Mr Dashwood... with a 
great deal of effort, attention and excruciating attention to placement.

>
>The thread is about POWER of languages.

Oh... so a threading device, found in a standard tap-and-die kit, is more 
POWERful than a screwdriver?  Should be fine for driving resistant screws!

Use the tool designed for the job and the definition of POWER might 
change.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T15:14:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aavjtF1qv6t1U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <h1o9f0$2s5$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7a873aF1u33geU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[34 more quoted lines elided]…
> change.

Then there would be no place for multifunction printers, integrated PDAs and 
iPods, or more than one attachment for a powerdrill or power saw.

Even specific tools designed for specific jobs can be improved   (a power 
drill is definitely more powerful than a hand operated brace and bit, even 
though it may not be as finicky or gentle...)

If I can do something easily and quickly then I am getting more power.

The posted example showed that for INSPECT... REPLACING in COBOL there is 
NOT the power that the equivalent in other modern languages provides. It was 
a simple example, and COBOL, as a language, is not judged on this alone.

I can imagine a person, used to working with other languages, coming to 
COBOL and saying: "how do I dyamically allocate arrays?, how do I replace 
text in situ?, how do I manage collections?, how do I search a collection?, 
how can I listen for events I'm interested in?, how do I manage threading? 
What if I want asynchronous processing on more than one core? how do I 
access the Windows Registry? How do I generate XML and web pages?", and many 
more questions, and being told: "Well, you access the C libraries for some 
of that and the interface is a bit hairy and your COBOL will only work on 
this platform, and some of it nobody really wants to do so we don't worry 
about it,... try to understand COBOL is a BUSINESS language... " And said 
newbie replies: "But my BUSINESS runs on a Client server network. I have 
branches all over the world and they need to share information. I need to 
make remote procedure calls to shared objects around my network."

His perception is that COBOL is not powerful enough.

We can remind him that, for the things we currently do, COBOL is adequate, 
but he's not convinced.

I believe it is because of scenarios like this imaginary one, that COBOL is 
losing the POWER struggle.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-22T21:36:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b254fbed-528d-486b-9a9b-09e381f50245@z16g2000prd.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <5b52c2ad-7307-4a1f-8ed8-996091e97f97@j9g2000prh.googlegroups.com> <h1lnd1$ll9$1@reader1.panix.com> <7a873aF1u33geU1@mid.individual.net> <h1o9f0$2s5$2@reader1.panix.com> <7aavjtF1qv6t1U1@mid.individual.net>`

```
On Jun 23, 3:14 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> docdw...@panix.com wrote:
> > In article <7a873aF1u33g...@mid.individual.net>,
…[41 more quoted lines elided]…
> though it may not be as finicky or gentle...)

Actual it is not. A brace and bit can be used to drill holes that
would stall a commercial power drill and, with a power drill, one
still has to counter the torque.

> If I can do something easily and quickly then I am getting more power.
>
…[3 more quoted lines elided]…
>

While INSPECT _is_ part of the Cobol language, your regex is not part
of the C# language (it a CLR Library routine accessible from any
language).

> I can imagine a person, used to working with other languages, coming to
> COBOL and saying: "how do I dyamically allocate arrays?,

> how do I replace
> text in situ?,

Note that your code is _not_ "replacing text in situ', it is replacing
it into a new area and then discarding the old one.


> how do I manage collections?, how do I search a collection?,
> how can I listen for events I'm interested in?, how do I manage threading?

> What if I want asynchronous processing on more than one core?

With Fujitsu one does it much like Java does.

> how do I access the Windows Registry?

Exactly the same way that any other language does it, call and API
routine.

> How do I generate XML and web pages?",

Using templates so that one does not need to care whether it is XML,
HTML or a printed report.

> and many
> more questions, and being told: "Well, you access the C libraries for some
> of that and the interface is a bit hairy

> and your COBOL will only work on
> this platform,

How ironic then that you are writing code that "will only work on this
platform" (ie Windows XP/Vista with .NET 3.x)

Perhaps you think that 'cross platform' is that it runs on Vista Home
_AND_ Vista Premium.


> and some of it nobody really wants to do so we don't worry
> about it,... try to understand COBOL is a BUSINESS language... " And said
…[4 more quoted lines elided]…
> His perception is that COBOL is not powerful enough.

Or possibly that the person he asks is clueless about how to actually
do those things easily.

Or is pushing an agenda.


> We can remind him that, for the things we currently do, COBOL is adequate,
> but he's not convinced.
…[6 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T14:33:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qp38$4l$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a873aF1u33geU1@mid.individual.net> <h1o9f0$2s5$2@reader1.panix.com> <7aavjtF1qv6t1U1@mid.individual.net>`

```
In article <7aavjtF1qv6t1U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> Use the tool designed for the job and the definition of POWER might
>> change.
>
>Then there would be no place for multifunction printers, integrated PDAs and 
>iPods, or more than one attachment for a powerdrill or power saw.

... and there would still be place for single-function tools such as 
hammers, screwdrivers, hex-keys and the like.  One set does not rule out 
the other.

>
>Even specific tools designed for specific jobs can be improved   (a power 
>drill is definitely more powerful than a hand operated brace and bit, even 
>though it may not be as finicky or gentle...)

That depends on the kind of work being done, Mr Dashwood.  For boring 
through a couple of inches of steel, sure, fire up the Black and Decker 
and lean into it.

For placing dental work *just* so - and remember how HUGE a mere hair in 
the mouth can feel? - then the dentist uses a brace-and-bit, manually and 
carefully.  One size does not fit all.

>If I can do something easily and quickly then I am getting more power.

Ummmmm... I noticed the adjective 'accurately' missing from that 
assertion, Mr Dashwood... but you Just Forgot, right?

[snip]

>I can imagine a person, used to working with other languages, coming to 
>COBOL and saying: "how do I dyamically allocate arrays?, how do I replace 
>text in situ?, how do I manage collections?, how do I search a collection?, 
>how can I listen for events I'm interested in?, how do I manage threading? 

I can imagine a person used to speaking Spanish coming to English and 
saying 'how do I describe the hectic dissarry that happens when they 
'tirar la casa por la ventana'?

I recall being told - apocryphal or not, I do not know - about a C class 
where a COBOL greybeard asked 'what is this 'memory' stuff and why do I 
have to go about allocating it instead of just increasing the value on the 
PARM card'?

Things change... that's a bullet-point, you know.

DD
```

#### ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-06-20T17:13:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net>`

```
Pete Dashwood wrote:
> I have commented more than once here that the newer languages are
> simply more concise and more powerful than COBOL. Less writing means
…[7 more quoted lines elided]…
>

[...]

You ever try floating a dollar-sign in FORTRAN? Or computing the hyperbolic 
arctangent in COBOL?
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-21T13:26:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a5gi4F1ti027U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>> I have commented more than once here that the newer languages are
…[13 more quoted lines elided]…
> hyperbolic arctangent in COBOL?

Nope on both counts.

But I take your point. Some things are better for some things and everything 
has strengths and weaknesses.

I used to believe that very strongly, but being forced to work in a 
multi-language environment has changed my mind. Not entirely (obviously, 
there are some things that are best suited to particular languages), but I 
see modern languages that are simply better "all rounders" than COBOL.(I 
think it has to do with the different paradigm; OO is just a better way to 
think about things, so languages which implement it well are going to be 
more "useful".) Yes, there are some things that COBOL is "better" at, but 
most of those things are being improved in other languages so the gap is 
narrowing. I think what prompted my rant was really frustration that 
something that IS in COBOL just doesn't do what it needs to. This reflects a 
lack of "care" for the language with a Standards body that was 17 years in 
the wilderness, and a moribund user community that simply accepts whatever 
it gets, as long as it doesn't involve changing anything...especially your 
mind.

If I only wrote COBOL, I would have accepted that "That's how it 
works...bummer. Have to code round it..." and never said a word.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-06-20T20:51:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TbedneXyGtynD6DXnZ2dnUVZ_uOdnZ2d@earthlink.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> If I only wrote COBOL, I would have accepted that "That's how it
> works...bummer. Have to code round it..." and never said a word.
>

Wouldn't your life be simpler, with less stress, and devoid of crying in the 
wilderness about OO, if you simply forgot everything you've learned in the 
last decade?

Just go to sleep. Sleep ... Sleep ... and be born again into a world without 
fear and hate!
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-21T22:18:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a6fngF1bvgb0U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <TbedneXyGtynD6DXnZ2dnUVZ_uOdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>>
…[9 more quoted lines elided]…
> without fear and hate!

I've been crying in the Wilderness for more than a decade and not just about 
OO... :-)

First it was Relational DBs replacing ISAM... Man! That was even more 
unpopular than OO... There was some real vitriol in the posts (and not just 
my posts... :-))

I remember someone actually saying that the use of ISAM should be encouraged 
because it guaranteed COBOL job security... I imagine said poster is 
currently unemployed, or, hopefully, working in a different field.

But you're right Jerry... I need sleep... "Sleep, it is a gentle thing, 
beloved from pole to pole. Sleep which ravelleth up the knitted sleeve of 
care..."

"Awake! Sleep no more... MacBeth hath MURDERED Sleep!"

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2009-06-21T10:46:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kYCdneg0zNBuyKPXnZ2dnUVZ_oqdnZ2d@earthlink.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <TbedneXyGtynD6DXnZ2dnUVZ_uOdnZ2d@earthlink.com> <7a6fngF1bvgb0U1@mid.individual.net>`

```
Pete Dashwood wrote:
> HeyBub wrote:
>> Pete Dashwood wrote:
…[28 more quoted lines elided]…
>

Another thought too (mentioned by Riplin): You scratched out 50 lines of 
code to do something. But you only have to do that once in your entire 
career! You make the code segment a subprogram, or a copy book, or some sort 
of reusable  hunk.

It's not like you have to re-invent the wheel and re-discover vulcanization 
every time you have a flat tire.

COBOL is a Turing Machine. Anything doable in other Turing Machines, such as 
FORTRAN or C##, is (theoretically) doable in COBOL.

One kind of stuff (say, floating a currency sign) we don't think about in 
COBOL and the FORTRAN people write (one time) a subroutine. Stuff that's 
hard (like substituting one string for another), the C# people don't think 
about while we COBOL people scribble a subprogram.

It evens out.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T14:37:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a892uF1tv0tiU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <TbedneXyGtynD6DXnZ2dnUVZ_uOdnZ2d@earthlink.com> <7a6fngF1bvgb0U1@mid.individual.net> <kYCdneg0zNBuyKPXnZ2dnUVZ_oqdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>> HeyBub wrote:
…[34 more quoted lines elided]…
> book, or some sort of reusable  hunk.

Or an OO Component. Gee, I never would've thought of that... :-)

The problem is that this "once in a lifetime" code segment, subprogram, 
copy book, or some sort of  reusable hunk requires use 15 or 20years down 
the line and it is on a computer that was scrapped 10 years ago... If it 
were an intrinsic part of the development language you use (like the .NET 
Framework) you wouldn't have to hunt for it. I have recently demonstrated 
the reuse of some COBOL code I wrote 35 years ago, so I am not unsympathetic 
to your idea (http://primacomputing.co.nz/cobol21/S2NTestServer.aspx)

In those days you couldn't just copy stuff to a memory stick, CD or floppy 
disk... I kept listings of all the COBOL routines I wrote and found 
useful...
>
> It's not like you have to re-invent the wheel and re-discover
> vulcanization every time you have a flat tire.

But sometimes the spare isn't in the trunk and youcan't find it.
>
> COBOL is a Turing Machine. Anything doable in other Turing Machines,
…[7 more quoted lines elided]…
> It evens out.

No, it doesn't.

If it did, the world would be using COBOL.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-21T20:10:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93c4114a-5488-4154-bc10-d3967f95387c@w31g2000prd.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <TbedneXyGtynD6DXnZ2dnUVZ_uOdnZ2d@earthlink.com> <7a6fngF1bvgb0U1@mid.individual.net> <kYCdneg0zNBuyKPXnZ2dnUVZ_oqdnZ2d@earthlink.com> <7a892uF1tv0tiU1@mid.individual.net>`

```
On Jun 22, 2:37 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> HeyBub wrote:
> > Pete Dashwood wrote:
…[39 more quoted lines elided]…
> the line and it is on a computer that was scrapped 10 years ago...

That seems to indicate that it is not something commonly or frequently
used then.

> If it
> were an intrinsic part of the development language you use (like the .NET
> Framework) you wouldn't have to hunt for it.

You want someone else to develop code which you might use twice in 30
years ?  And, it seems, code that few others would care about at all.

Of course you could use the .NET routines from a suitable version of
Cobol.

Indeed you could use the C library of routines, or the C++ library in
suitable versions of Cobol too.


> I have recently demonstrated
> the reuse of some COBOL code I wrote 35 years ago, so I am not unsympathetic
…[27 more quoted lines elided]…
> If it did, the world would be using COBOL.

The world generally uses what is suitable for the task. If you want
cross-platform run-anywhere then use Java or Python. If you want web-
clientside use JavaScript.

Cobol is still used because:
 1) the cost of replacing the application is greater than the cost of
keeping it over a medium term.
 2) there is no replacement.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-06-21T09:07:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:7a5gi4F1ti027U1@mid.individual.net...
>
> But I take your point. Some things are better for some things and 
…[3 more quoted lines elided]…
> multi-language environment has changed my mind. ...

You think it possible that in the age of  twitter, amazon.com, iPhone and 
Travelocity,  all the "non-executable" code required to build a COBOL 
application (e.g., ENVIRONMENT DIVISION, DATA DIVISION et al ) is totally at 
odds with the today's  "now" culture, and that's why COBOL is less popular 
than some other language options?


MCM
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** SeaSideSam <sam@sea.side>
- **Date:** 2009-06-21T10:12:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adb02$4a3e4df8$6216372b$11232@ALLTEL.NET>`
- **In-Reply-To:** `<Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com>`

```
Michael Mattias wrote:
> 
> You think it possible that in the age of  twitter, amazon.com, iPhone and 
…[4 more quoted lines elided]…
> 

every generation creates 'their' world full of 'their' things... music, 
art, fashion, terminology; so why not their own computer language. 
cobol has it's roots in the 40s and 50s... created by the generation 
sometimes called the 'greatest generation'.

cobol has been dying since the early '70s, and eventually it will go 
away.  it would be interesting to be around when that happens to listen 
to the young hackers brag about bringing it down.  except... well... the 
young hackers and their tools sets will be gone as well.

there are those that have been espousing the virtues of oo since it's 
conception, and the promise of oo was/is impressive.  but from my 
perspective oo has delivered in one area more than all the others 
combined... the financial area.  oo sells a lot of memory.

the bottom line is that regardless of the language we choose to code in, 
eventually that code has to be converted into the language that a 
computer can work with.  ibm cobol is converted into assembler then into 
machine code.  rm/cobol is converted into something intermediate, then 
uses another machine-language program to translate the intermediate 
instructions.  open-cobol is attempting to convert cobol to c then to 
machine code (i'm not sure if the decision to follow this method was a 
wise one as it adds considerable complications to the project).  we all 
have our favorite tools, yet, in the final analysis, all our varied 
tools lead us to the same place.

when traveling from auckland to sydney one can swim, sail, or fly.  when 
traveling from perth to sydney one has the additional options of 
walking, running, or driving.  as a manager (as i practiced the 
position) i really don't care how you got to sydney as long as...
1) you got there on time
2) the trip was reproduceable by those following

i gotta shut up.  i'm close to 3 full days without rest/sleep.

sss
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T15:12:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a8b4sF1u9ranU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com> <adb02$4a3e4df8$6216372b$11232@ALLTEL.NET>`

```
SeaSideSam wrote:
> Michael Mattias wrote:
>>
…[16 more quoted lines elided]…
>

My view is a little different. I don't think anybody is trying to "bring 
COBOL down".

It is just about evolution and changing environments and requirements.

If the world was still as it was in the 60s (sometimes I really wish !!!) 
then COBOL would be fine and we'd all be running mainframes.


> there are those that have been espousing the virtues of oo since it's
> conception, and the promise of oo was/is impressive.  but from my
> perspective oo has delivered in one area more than all the others
> combined... the financial area.  oo sells a lot of memory.

Fortunately, memory has become extremely cheap, so even if you're correct, 
it doesn't matter.

I remember similar arguments being produced when virtual storage was first 
invented. (And disk drives were NOT cheap...)

>
> the bottom line is that regardless of the language we choose to code
…[9 more quoted lines elided]…
>
Yep. No argument.

The differences are in perception. The above is a technical view, and 
perfectly valid as far as it goes. But what if I don't care about memory or 
compilers or translators or even tools... suppose all I want is to get 
invoices to cusomers when they buy something, or to know how much profit I 
made last month (or even right up to this very minute), or to get myself the 
best deal on a flight to Hawaii... Suppose my perception is about 
functionality and I just accept that the technology can deal with it? THEN, 
a language like COBOL is much less attractive. It means I have to deal with 
very low level stuff, which I have neither the time nor the inclination to 
do. Instead, I find there are existing objects, already invented, that are 
pertinent to my needs. I'd rather plug Lego blocks together than work in the 
factory that makes them.

> when traveling from auckland to sydney one can swim, sail, or fly.

As far as I know, no-one has ever swum the 1100 miles involved... :-)

> when traveling from perth to sydney one has the additional options of
> walking, running, or driving.  as a manager (as i practiced the
…[4 more quoted lines elided]…
> i gotta shut up.  i'm close to 3 full days without rest/sleep.

Ah, obsession is a terrible thing... :-)

Seriously, Sam, hope you are feeling better soon.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2009-06-21T21:07:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70449d5c-9cb0-48da-8b47-0b7f3e9b9d29@d2g2000pra.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com> <adb02$4a3e4df8$6216372b$11232@ALLTEL.NET> <7a8b4sF1u9ranU1@mid.individual.net>`

```
I can't help it but I think I need to comment in 'general' what was
documented here.

I do like the 'shortcut' coding of C#, and I also like to use OOCobol
in most instances.

The real scenario is the 'deployment' issues.

Cobol; (a) using MF OOCobol coding (b) powerful on every platforms,
never had an issue if i transfer my applications from Microsoft to
Linux (c) .NET runtime is optional which is about 4MB in platform
resources (d) problem with licensing issues (e) neutral language for
several/open source platform

C#; (a) using MS Visual Studio (b) powerful language when I tried
in .NET version 2, but there is a problem with the deployed
application when the platform was 'upgraded' to .NET version 2.5 (c)
some coding needs adjustments and must be recompiled using .NET
version 2.5 again to work (d) in pure Linux; Microsoft-based
application will not run, it could execute in Linux Mono but there are
still complicated issues concerning ODBC connections (e) licensing is
not so much a problem (f) language is intended only to be run in
Microsoft platform

Can't speak of mid-range/mainframe platforms... but I knew they too
have their comments.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T22:13:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a93qqF1tpc4eU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com> <adb02$4a3e4df8$6216372b$11232@ALLTEL.NET> <7a8b4sF1u9ranU1@mid.individual.net> <70449d5c-9cb0-48da-8b47-0b7f3e9b9d29@d2g2000pra.googlegroups.com>`

```
Rene_Surop wrote:
> I can't help it but I think I need to comment in 'general' what was
> documented here.
…[23 more quoted lines elided]…
> have their comments.

Interested to hear your comments, Rene.

I have only tried running C# with Mono under Linux on one occasion and it 
was a fairly trivial experiment. It worked, but I didn't try connecting to a 
DB. I'm interested to hear about your "bad ODBC" experience as I'm doing a 
lot with ADO, DAO, ODBC, OleDB and LINQ at the moment. ODBC should work on 
Linux or Windows. Did you connect directly from the program (with a 
connection string for ODBC),or via an external control file, or via ADO or 
some other way?

If something is developed for .NET 2.0 and the platform is upgraded to a 
later version of .NET, it will still run as long as they don't uninstall the 
existing .NET framework. I have applications running in both .Net 2.0 and 
.Net 3.5 on the SAME platform. It sounds like they REPLACED their version of 
.NET which definitely means you need to rebuild the C# application. This 
shouldn't be a big deal; for me it means checking a box in the project 
properties in VS 2008.

I agree that although you CAN use C# on other platforms it is probably 
intended for Microsoft.

With regard to deployment in general, I really like MS ClickOnce and it is 
very simple for the developer and the client. I think it is many times 
better than the deployment required with Fujitsu COBOL (although later 
versions of that were definitely improved). I have used ClickOnce for web 
based deployment and for CD and had no problems at all with either.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** SeaSideSam <sam@sea.side>
- **Date:** 2009-06-22T01:30:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bed2$4a3f24f7$6216372b$24918@ALLTEL.NET>`
- **In-Reply-To:** `<7a8b4sF1u9ranU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com> <adb02$4a3e4df8$6216372b$11232@ALLTEL.NET> <7a8b4sF1u9ranU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> Seriously, Sam, hope you are feeling better soon.
> 
> Pete.

thanks for the thought mr dashwood.  the reality is that i have reached 
that point in this life were life is pain management.  my only real hope 
at feeling better is to arrive at that point where i don't feel at all. 
    feeling pain wont be important then.

i was reading earlier about how n1h1 is beating up on new zealand.  i'm 
not sure an old man like you, even in your good state of health, could 
survive n1h1; so do be careful yourself.

my only real complaint about c is that i haven't been able to learn it. 
  i do a lot of programming in visual basic (still haven't mastered 
'event driven' either) and have had numerous occasions of an 'object' 
that i would have to create myself.  when i say a lot of programming 
what i mean is a lot in time.  what used to take 3 days to do now takes 
3 months or more.

why am i programming in vb vs cobol?  rm/cobol did not come with 
sql-capabilities; vb did.  i first started using sql with oracle 1.1 on 
a pc, and use sql whenever i can.  it's commonsenseable, 
self-documenting, and powerful (one of your favorite words).  i was 
working in san francisco at the time and evaluated oracle and other 
products in preparation for finding a computer system that would meet 
the company's needs for the future as the future was expected to be. 
data processing did it's job, presented our findings, then left the 
room.  those-that-signed-the-checks then made a decision... the wrong 
one.  anyway; we migrated from a ibm 43xx mainframe to a ibm sys/38 
mini.  a good box just not the one we needed.  i was able to find a 
third-party sql package called sql/38 which allowed me to put up rpg and 
cl jobs in record time.  a very productive tool and i'm rambling on 
again.  i have had about an hour of sleep, but no rest.

happy winter time!  only 183 days until summer!

thanks for your thoughts...

sss
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T22:32:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a94uoF1uluriU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com> <adb02$4a3e4df8$6216372b$11232@ALLTEL.NET> <7a8b4sF1u9ranU1@mid.individual.net> <3bed2$4a3f24f7$6216372b$24918@ALLTEL.NET>`

```
SeaSideSam wrote:
> Pete Dashwood wrote:
>>
…[9 more quoted lines elided]…
> i was reading earlier about how n1h1 is beating up on new zealand.

Actually, it is beating up in Melbourne much worse than here in New Zealand. 
I have a client there and we were talking today. He says he has seen no sign 
of it and they have no businesses closed due to it. Schools get closed as is 
to be expected.

> i'm not sure an old man like you, even in your good state of health,
> could survive n1h1; so do be careful yourself.

Thanks.  I have lived in places where white people were not expected to 
survive, I've had  no serious illness since I was 14 years old, when I was 
expected to die but told them I wasn't ready to... and I am, obviously, 
still here.  I think military service at 22 was a big help. We were expected 
to be fighting in Viet Nam and received, over three days, a course of around 
30 different vaccinations and serums which left most of us on "light duties" 
and actually wishing the Viet Cong would finish us off... I believe having 
this at an early age prepared my immune system for just about anything. I am 
pretty confident that N1H1 would not terminate me but I have no wish to put 
it to the test... :-)
>
> my only real complaint about c is that i haven't been able to learn
…[5 more quoted lines elided]…
>
I'm sorry. It is sad to see anyone in that condition. Hopefully, your 
treatment will bring about some improvement.

> why am i programming in vb vs cobol?  rm/cobol did not come with
> sql-capabilities; vb did.  i first started using sql with oracle 1.1
…[7 more quoted lines elided]…
> one.

Unfortunately, not an uncommon event...

> anyway; we migrated from a ibm 43xx mainframe to a ibm sys/38
> mini.  a good box just not the one we needed.  i was able to find a
…[3 more quoted lines elided]…
>
You ramble all you want to... most of us who contribute here find it 
therapeutic  :-)

> happy winter time!  only 183 days until summer!
>
:-)

It is pretty weird. We are having beautiful sunshine and clear days but the 
temperature is rarely above 14 C. At night it drops dramatically to around 
zero, and there are frosts. I have moved to a winter duvet and electric 
blanket and my bed is so comfortable I don't want to get out of it :-)

Don't know why but writing that evoked an image I saw on you tube or 
somewhere of a great ugly mountain gorilla preparing his nest for the 
night...funny how minds work... :-)


> thanks for your thoughts...
>
Hang in there.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:39:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2b9v3594t04j61o2mqvonldleuvfb9u7ku@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com> <adb02$4a3e4df8$6216372b$11232@ALLTEL.NET> <7a8b4sF1u9ranU1@mid.individual.net> <3bed2$4a3f24f7$6216372b$24918@ALLTEL.NET> <7a94uoF1uluriU1@mid.individual.net>`

```
On Mon, 22 Jun 2009 22:32:54 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>We were expected 
>to be fighting in Viet Nam and received, over three days, a course of around 
>30 different vaccinations and serums which left most of us on "light duties" 
>and actually wishing the Viet Cong would finish us off...

In Fredric Pohl's delightfully named autobiography _The Way The Future
Was_, he mentioned how they pulled all of his fillings, and replaced
them with cold-weather fillings - then sent him to fight in North
Africa.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-22T16:34:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1obq1$rm7$4@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a8b4sF1u9ranU1@mid.individual.net> <3bed2$4a3f24f7$6216372b$24918@ALLTEL.NET> <7a94uoF1uluriU1@mid.individual.net>`

```
In article <7a94uoF1uluriU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>At night it drops dramatically to around 
>zero, and there are frosts. I have moved to a winter duvet and electric 
>blanket and my bed is so comfortable I don't want to get out of it :-)

I'd suggest a canine of some kind... me, I'm partial to pugs but if I 
recall you are a bit larger, check out the French bulldog 
< http://www.akc.org/breeds/french_bulldog/ >.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T15:42:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ab190F1ud90fU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a8b4sF1u9ranU1@mid.individual.net> <3bed2$4a3f24f7$6216372b$24918@ALLTEL.NET> <7a94uoF1uluriU1@mid.individual.net> <h1obq1$rm7$4@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7a94uoF1uluriU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[12 more quoted lines elided]…
> DD

Er... it would have to be a BRITISH bulldog for me... :-)

Funny you should say that, Doc. As a child I grew up with cats and dogs and 
the odd duck and lamb, and loving parents instilled a love of animals in me 
from an early age. I really do love them. For that reason, given the 
uncertainty of the travelling life I have enjoyed until fairly recently, I 
have not taken any on,  because I haven't been sure where I was going to be 
and I could never have a pet put down when it became an inconvenience. I 
know good homes can sometimes be found, but after a few years it would be 
like putting a family member up for adoption. It just doesn't work for me.

However, things appear to be changing in my life and it looks as though I'll 
be home for the duration  (although there is still some uncertainty...). I 
was thinking about a dog the other day. I have a couple of friends 
(families) who get me to baby sit their dogs for a weekend when they go away 
occasionally and I really enjoy this. One set of friends have a 
Bichon/Maltese cross and the others have a fox terrier. Both of these dogs 
are an absolute delight and amuse me no end. They are used to family life 
with noise and children, and the sedate relative quietness of my place is a 
complete change for them. Neither of them will stay in their doggie beds but 
insist on sleeping on my gorilla nest... :-) It isn't just the weather, it's 
the same winter or summer, they just like company while their respective 
families are away.

I can see myself descending into the stereotype of a cantankerous old man 
who abuses shop assistants, yells at women and children, waves his stick at 
bus drivers and health care workers, and is only loved by his faithful dog, 
which accompanies him everywhere... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-22T21:56:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ae097ad7-5bdc-424c-9673-83e8668334b3@v23g2000pro.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a8b4sF1u9ranU1@mid.individual.net> <3bed2$4a3f24f7$6216372b$24918@ALLTEL.NET> <7a94uoF1uluriU1@mid.individual.net> <h1obq1$rm7$4@reader1.panix.com> <7ab190F1ud90fU1@mid.individual.net>`

```
On Jun 23, 3:42 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> docdw...@panix.com wrote:
> > In article <7a94uoF1ulur...@mid.individual.net>,
…[37 more quoted lines elided]…
> families are away.


> I can see myself descending into the stereotype of a cantankerous old man
> who abuses shop assistants, yells at women and children, waves his stick at
> bus drivers and health care workers, and is only loved by his faithful dog,
> which accompanies him everywhere... :-)

What makes you think that you are not already there ?

Perhaps it is only the dog that is lacking.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T15:41:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qt3g$g8g$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a94uoF1uluriU1@mid.individual.net> <h1obq1$rm7$4@reader1.panix.com> <7ab190F1ud90fU1@mid.individual.net>`

```
In article <7ab190F1ud90fU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7a94uoF1uluriU1@mid.individual.net>,
…[14 more quoted lines elided]…
>Er... it would have to be a BRITISH bulldog for me... :-)

Don't let nationalism get in the way some enjoyments, Mr Dashwood... Brie, 
Emmenthaler and similar things come to mind.  There's room in life for 
Guiness and for Framboise Lambic Ale.

Actually, I chose the French because they not only have delightful 
personalities... but (carefully fed) they should max-weight to 30lbs 
(13.6Kg).  A British (or, to some, 'Real') Bulldog shows an American 
Kennel Club range of 40 - 50lb (18 - 23Kg) and a lifespan 10 years, the 
French 10 - 14.

As I recall of such things - I tend to pay more attention to things of the 
mind than of the body - you are not of the diminiutive somatotype... but 
tempus fugit, old man, and we age... and in another decade another 10 - 20 
lbs (or, given a soft-hearted owner, 25 - 35) of John Bull might present a 
greater challenge to deal with for things like walking, bathing, 
nail-grooming, anal-gland expressing and other grooming activities.

[snip]

>I can see myself descending into the stereotype of a cantankerous old man 
>who abuses shop assistants, yells at women and children, waves his stick at 
>bus drivers and health care workers, and is only loved by his faithful dog, 
>which accompanies him everywhere... :-)

Apophatically leaving aside the 'oh, the only difference is the dog'... 
don't forget that the Frenchie fits into a lap the way an English never 
could... and then circles... and then sssssiiiiiigggghhhhhssss... and 
all's better with the world.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T12:03:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad8r2F1v15n7U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a94uoF1uluriU1@mid.individual.net> <h1obq1$rm7$4@reader1.panix.com> <7ab190F1ud90fU1@mid.individual.net> <h1qt3g$g8g$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7ab190F1ud90fU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[46 more quoted lines elided]…
> sssssiiiiiigggghhhhhssss... and all's better with the world.

I noticed you and Richard could not resist... :-) It was pretty obvious but 
I guess subtlety is not always a goal.

>
> DD

Very good arguments. I am persuaded to at least check out availability and 
maybe go and see some of these dogs.

I also like the idea of simply going to the SPCA and rescuing some poor mutt 
that needs a good home and loving owner.

Thanks for your points, Doc.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-24T13:47:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1tapq$1u1$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7ab190F1ud90fU1@mid.individual.net> <h1qt3g$g8g$1@reader1.panix.com> <7ad8r2F1v15n7U1@mid.individual.net>`

```
In article <7ad8r2F1v15n7U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7ab190F1ud90fU1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>>> docdwarf@panix.com wrote:

[snip]

>>>> I'd suggest a canine of some kind... me, I'm partial to pugs but if
>>>> I recall you are a bit larger, check out the French bulldog
>>>> < http://www.akc.org/breeds/french_bulldog/ >.

[snip]

>Very good arguments. I am persuaded to at least check out availability and 
>maybe go and see some of these dogs.
>
>I also like the idea of simply going to the SPCA and rescuing some poor mutt 
>that needs a good home and loving owner.

One can combine the two, Mr Dashwood... I do not know how such things work 
in the Antipodes but here in the States there are organisations which are 
dedicated to 'rescue' for certain breeds, eg 
http://www.frenchbulldogrescue.org/ .  They get animals from bad 
situations... not necessarily abusive ones, sometimes people move into 
apartments where dogs are not allowed, someone shuffles off this Mortal 
Coil and leaves behind a faithful companion, an animal gets lost and 
cannot be traced... and the Rescue groups take over, first sending the pup 
to a foster home so it can become accustomed to living with folks again 
and making sure veterinary difficulties are noted, etc.

(animal fosterers are, in my opinion, a notch - and a very slight one - 
below saints)

When the beastie is ready it is put up for adoption... and, fingers 
crossed, all goes well.  http://www.nzkc.org.nz/ might be a good place to 
start.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-25T12:02:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7aft56F1vda21U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7ab190F1ud90fU1@mid.individual.net> <h1qt3g$g8g$1@reader1.panix.com> <7ad8r2F1v15n7U1@mid.individual.net> <h1tapq$1u1$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7ad8r2F1v15n7U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[38 more quoted lines elided]…
> DD
Thanks Doc.

I have some contacts in the Kennel Club and when things are more definite 
and I'm ready to settle down permanently, I'll get in touch and see if the 
French bulldog is even in NZ. (I had never heard of the breed until you 
mentioned it..)

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-25T13:53:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1vvh4$s92$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7ad8r2F1v15n7U1@mid.individual.net> <h1tapq$1u1$1@reader1.panix.com> <7aft56F1vda21U1@mid.individual.net>`

```
In article <7aft56F1vda21U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> When the beastie is ready it is put up for adoption... and, fingers
>> crossed, all goes well.  http://www.nzkc.org.nz/ might be a good
…[8 more quoted lines elided]…
>mentioned it..)

As I recall reading somewhere it has common ancestry with the English... 
Auld Blighters in France missed their companions and, over time, 
selectively bred a small version with many of the same characteristics.  
There's http://www.nzkc.org.nz/club/index.html?code=318 and from 
http://en.wikipedia.org/wiki/French_bulldog :

--begin quoted text:

While theories abound about the exact origin of the French Bulldog, the 
most prevalent opinion is that around the mid-1800s Normandy lace workers 
from England took smaller bulldogs with them when they sought work in 
France. In the farming communities north of France that the lace workers 
settled in, the little bulldogs became very popular as ratters and loyal 
family companions and their population began to swell. These little 
bulldogs were in fact "culls" of the established bulldog breeders in 
England, who were generally more than happy to sell these undersized 
examples of their breed to fanciers of the "new" breed in England. This 
was especially true of the "tulip" eared puppies that cropped up at times 
in bulldog litters. French bulldogs were originally bred as ratters, but 
are now bred as lap dogs and companions.

--end quoted text

... so they might be closer in temperment to the terriers (bred to hunt 
vermin) than you think... and already enjoy.

I often say 'There is no patch for the heart like a puppy'... I don't know 
if that is original but for me, when Killer's time comes and I am e'en 
more fragile and delicate than I am now I'm considering a Brussels Gryphon 
(Griffon Bruxellois) ( http://en.wikipedia.org/wiki/Brussels_Gryphon ) but 
that might be a bit on the wee side for a great strappin' laddie as 
yourself.  A strain of pug was introduced into the breed in the mid-late 
19th century and Killer, a female pug, is litterbox-trained.

E'en worse - if such a thing can be imagined - I own a shoulder-bag 
designed for doggie-carrying; a Frenchy would be too large but Killer fits 
in *just* right.  Children are usually the first to notice that 'hey, 
there's a guy over there carrying a purse... and he's got a *dog* in it' 
and, as the situation merits, I can respond 'That's *Sergeant* 
guy-over-there-with-a-purse-with-a-dog-in it, thank you... and if your 
parents give permission you are welcome to say 'hello', she's very shy.'

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:37:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s59v35h3d2f5q39phbu6jfb8uabetp5rqg@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com> <adb02$4a3e4df8$6216372b$11232@ALLTEL.NET> <7a8b4sF1u9ranU1@mid.individual.net>`

```
On Mon, 22 Jun 2009 15:12:34 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> when traveling from auckland to sydney one can swim, sail, or fly.
>
>As far as I know, no-one has ever swum the 1100 miles involved... :-)

Actually, more meaningful to this thread is the observation that
nobody travels from his home in Aukland to his destination in Sydney
via a single mode of transportation.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-22T14:55:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a8a4lF1u5lveU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com>`

```
Michael Mattias wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:7a5gi4F1ti027U1@mid.individual.net...
…[12 more quoted lines elided]…
>
That's a very interesting idea, Michael.

I hadn't thought about it, but, apart from library references (a bit like C 
header files) almost everything I code in C# is executable.  (I use region 
directives to show and hide code... can't immediately think of anything 
else.)

I honestly don't know how much of a consideration that is. I'd like to think 
it is not much.

At least, I think there are other more compelling reasons:

1. The OO paradigm rules  (except maybe in Texas... :-))
2. Modern laguages are less verbose. (I think that is part of what you're 
saying).
3. Modern languages are more POWERFUL. (You can do more, with less)
4. Cost of ownership is much less on modern languages, compared to COBOL. 
(Open COBOL is a step in the right direction, but it has a way to go yet and 
it needs OO support (or at least COM wrapping)).
5. Support for modern languages is immediate and free. COBOL should be so 
lucky...

I think it is about functionality versus technology and I covered it 
elsewhere.

However, when I look at the list above, I see that your point about the 
"now" generation could apply to most of them. People want fast simple 
solutions. Cobbling together thousands of lines of low level code is not 
attractive to them.OO lends itself to component based approaches, but 
COBOLlers have not embraced it.

It's a very interesting idea you raised.

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:40:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ce9v351s3f0serjrv7kg9cd1ssphc6vq71@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com> <7a8a4lF1u5lveU1@mid.individual.net>`

```
On Mon, 22 Jun 2009 14:55:24 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I hadn't thought about it, but, apart from library references (a bit like C 
>header files) almost everything I code in C# is executable.  (I use region 
…[4 more quoted lines elided]…
>it is not much.

Maybe not directly - but indirectly, executable languages are easier
and cheaper to learn and start using.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:34:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tu8v359q1iet0rfvf90vgo55h4gdghqjt1@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <Xfr%l.766$lv5.671@flpi149.ffdc.sbc.com>`

```
On Sun, 21 Jun 2009 09:07:11 -0500, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>You think it possible that in the age of  twitter, amazon.com, iPhone and 
>Travelocity,  all the "non-executable" code required to build a COBOL 
>application (e.g., ENVIRONMENT DIVISION, DATA DIVISION et al ) is totally at 
>odds with the today's  "now" culture, and that's why COBOL is less popular 
>than some other language options?

The definition of "language" is more variable now, although the "L" in
JCL and DCL stands of "language".    IBM wanted to replace JCL with
REXX, and shell scripts are more powerful versions of .BAT files. What
is the most popular language in the world today?    Excel macros?
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-22T16:23:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1ob5d$rm7$3@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net>`

```
In article <7a5gi4F1ti027U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>This reflects a 
>lack of "care" for the language with a Standards body that was 17 years in 
>the wilderness, and a moribund user community that simply accepts whatever 
>it gets, as long as it doesn't involve changing anything...especially your 
>mind.

Minds aside, Mr Dashwood... in Business, Commonly, change costs money.

DD
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T15:44:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ab1d0F1rauesU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <h1ob5d$rm7$3@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7a5gi4F1ti027U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
> DD
Yes, it does. But there is no progress without it...

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-23T08:59:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gbr145pvrfsia77oadl5hgtfsokbvctc94@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <h1ob5d$rm7$3@reader1.panix.com> <7ab1d0F1rauesU1@mid.individual.net>`

```
On Tue, 23 Jun 2009 15:44:34 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Minds aside, Mr Dashwood... in Business, Commonly, change costs money.
>>
>> DD
>Yes, it does. But there is no progress without it...

Lots of businesses want to progress with the old ways of doing things.
GM makes better cars than it did a generation ago - but its basic
business plan had not adapted.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T12:05:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad8tqF1ulvakU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <h1ob5d$rm7$3@reader1.panix.com> <7ab1d0F1rauesU1@mid.individual.net> <gbr145pvrfsia77oadl5hgtfsokbvctc94@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 23 Jun 2009 15:44:34 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
> business plan had not adapted.

Sorry Howard, I don't want to be picky here, but... How could they make a 
better car without changing the way they made cars?

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-24T06:44:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hg74451tuibq8kiflss8lm3bps9tc9o85o@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com> <7a5gi4F1ti027U1@mid.individual.net> <h1ob5d$rm7$3@reader1.panix.com> <7ab1d0F1rauesU1@mid.individual.net> <gbr145pvrfsia77oadl5hgtfsokbvctc94@4ax.com> <7ad8tqF1ulvakU1@mid.individual.net>`

```
On Wed, 24 Jun 2009 12:05:13 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Lots of businesses want to progress with the old ways of doing things.
>> GM makes better cars than it did a generation ago - but its basic
…[3 more quoted lines elided]…
>better car without changing the way they made cars?

It's business isn't limited to making cars.   Its business is making
money, and its primary way of making money is selling cars with a
markup and rate so that its income is greater than its expenses.

Looking at one word there, I will pick "rate".   If cars last longer,
cost more (as a percentage of the buyer's income), and look the same,
the business plan should not depend upon buyers trading in cars at the
rate they used to.     

And if in the old days, they fund retirements out of future profits
(instead of funded retirement plans), they shouldn't be surprised when
those profits go down when people retire.

It is easy to assume that the part of the business that we see - or
work in, is the business.   My program does exactly what the user said
he wanted and was willing to pay for.    But if I understood the
business model better - and knew alternative ways of helping the user
do his job - I could have provided him with a better tool.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-23T15:44:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1qt85$g8g$2@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <7a5gi4F1ti027U1@mid.individual.net> <h1ob5d$rm7$3@reader1.panix.com> <7ab1d0F1rauesU1@mid.individual.net>`

```
In article <7ab1d0F1rauesU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <7a5gi4F1ti027U1@mid.individual.net>,
…[12 more quoted lines elided]…
>Yes, it does. But there is no progress without it...

There are fewer botches with it, as well... which is why many here can 
attest to the fact that they work with code which is essentially the same 
as it was long before it was old enough to vote.

DD
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-22T16:21:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1ob1i$rm7$2@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com>`

```
In article <pOSdnQQl4MaLwqDXnZ2dnUVZ_oudnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>Pete Dashwood wrote:

[snip]

>> Here's an example from real life that really pissed me off... :-)
>>
…[4 more quoted lines elided]…
>arctangent in COBOL? 

My experience is limited, granted... but I never ran into a need for a 
hyperbolic arctangent in something Business Oriented.  If I did... I'd 
likely code it in something else as a subroutine and CALL away.

DD
```

#### ↳ Re: Why COBOL is losing the POWER struggle

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2009-06-21T02:48:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gv2r355vbumprihqv29sqam7vsedv49kil@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net>`

```
On Sun, 21 Jun 2009 05:22:24 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I have commented more than once here that the newer languages are simply 
>more concise and more powerful than COBOL. Less writing means fewer errors.
…[9 more quoted lines elided]…
>
snip - code not really important here

>
>In C# I can use a Regular Expression, code 3 lines and get on with more 
…[6 more quoted lines elided]…
>

The above example reminds me of a young boy a few years ago stating
that COBOL was crap as it would not allow list boxes and similar (and
this was in play TEXT mode cobol) - and he was saying that all windows
development tools had it. 
Was extremely hard to get into his dumb head that those languages HAD
the list boxes because someone HAD PROGRAMMED them in another language
and made them available to those languages. Only when I showed him a
small sample of a list box in cobol (from a client and as such I don't
have the code available) that he understood that it is all a question
of someone having it done beforehand and having it done in a generic
enough way to allow any other programmer to use it without going
through all the hassle of building one from scratch.


As a small example I am posting here something that COBOL (most
versions/vendors - I know of one that does have it) vendors DO NOT
have.
This is a small routine I wrote to justify text - Left (E-squerda),
right (D-ireita) and centered (C-entrado). 
This is a function that is very easy to do in any of the current
languages - but that still isn't available on COBOL - that does not
mean it would bother anyone to use my code - with small changes you
can make it work with bigger strings (or even a almost unlimited sized
one( not that I can see what use it would be).
This is a very old version - prior to 1992 - and was made for short
strings - don't have a more recent one at hand.


Just as a small note - this is one of many routines I made like this -
I, like many others, have built a significant amount of routines over
the years to allow us to take less time performing the common tasks
any program requires, and to dedicate ourselves more to the really
complex business rules we had.
I, as some others I know, have build screen designers/managers that
would allow us to just design the screen (using our own software) and
all the code related to accepts/displays would be dealt with within
sub-routines - this is pretty much what happens with common languages
where you do not have to code a list box or a text box
validation/processing and whatever else you have to think of - you
just say a text box is here, font is that, color is that input/output
format is that - and the underlying software will deal with those
attributes of that field of that particular screen. And I did it all
in COBOL.



       IDENTIFICATION DIVISION.
       PROGRAM-ID. ROTCENTR.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. ICL.
       OBJECT-COMPUTER. ICL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  XE                 PIC  99.
       01  XD                 PIC  999.
       01  Y                  PIC  999.
       01  Z                  PIC  999.
       01  W1-DES.
           05  W1-DES1        PIC  X(100) VALUE SPACES.
           05  W1-DES1R REDEFINES W1-DES1 OCCURS 100 PIC X.
       01  W2-DES.
           05  W2-DES1        PIC  X(100) VALUE SPACES.
           05  W2-DES1R REDEFINES W2-DES1 OCCURS 100 PIC X.
       LINKAGE SECTION.
       01  CTR-TAM            PIC  999.
       01  CTR-TAM1           PIC  999.
       01  CTR-VAR            PIC  X(100).
       01  CTR-JUST           PIC  X.
       01  CTR-FILLER         PIC  X(50).
       PROCEDURE DIVISION USING CTR-TAM CTR-TAM1 CTR-VAR CTR-JUST
                                                 CTR-FILLER.
       INIC.
           IF CTR-VAR = SPACES OR CTR-TAM = 0 GO FIM-MESMO.
           PERFORM CALC-TAM.
           IF CTR-JUST = "D" PERFORM JUST-D.
           IF CTR-JUST = "E" PERFORM JUST-E.
           IF CTR-JUST = "C" PERFORM JUST-C.
           MOVE W2-DES TO CTR-VAR.
       FIM-MESMO.
           EXIT PROGRAM.
       CALC-TAM.
           MOVE CTR-VAR TO W1-DES1.
           PERFORM VARYING XD FROM CTR-TAM BY -1
                             UNTIL XD < 1
                             OR W1-DES1R(XD) NOT = SPACES
                             END-PERFORM.
           MOVE CTR-VAR TO W1-DES1.
           PERFORM VARYING XE FROM 1 BY 1
                             UNTIL XE > CTR-TAM
                             OR W1-DES1R(XE) NOT = SPACES
                             END-PERFORM.
       JUST-C.
           COMPUTE Y = (CTR-TAM - XD) / 2 + 1 + (XE / 2).
           PERFORM VARYING Z FROM XE BY 1 UNTIL Z > XD
                   MOVE W1-DES1R(Z) TO W2-DES1R(Y)
                   ADD 1 TO Y
                   END-PERFORM.
       JUST-D.
           MOVE CTR-TAM TO Y.
           PERFORM VARYING Z FROM XD BY -1 UNTIL Z < XE
                             OR Z = 0
                   MOVE W1-DES1R(Z) TO W2-DES1R(Y)
                   SUBTRACT 1 FROM Y
                   END-PERFORM.
       JUST-E.
           MOVE 1 TO Y.
           PERFORM VARYING Z FROM XE BY 1 UNTIL Z > XD
                   MOVE W1-DES1R(Z) TO W2-DES1R(Y)
                   ADD 1 TO Y
                   END-PERFORM.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-21T23:43:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a6kmoF1tf86uU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <gv2r355vbumprihqv29sqam7vsedv49kil@4ax.com>`

```
Frederico Fonseca wrote:
> On Sun, 21 Jun 2009 05:22:24 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> snip - code not really important here

Oh, OK then... guess the machine can run without it... :-)
>
>>
…[7 more quoted lines elided]…
>>
Guess we should snip that too...:-)

>
> The above example reminds me of a young boy a few years ago stating
…[10 more quoted lines elided]…
> through all the hassle of building one from scratch.

Sure, that was never in dispute. My point was that COBOL HAS a facility that 
would do the job fine, but it doesn't "work" because it can't handle unequal 
length operands. That means going to a lower level of code.

No, this is not the first time  have ever needed to do a global replace in 
COBOL where the source and target operands were of different size and I DO 
have code (somewhere, on another machine...) that would do it for me. I 
explained elsewhere why it was no quicker to go and find it than it was to 
write something for the case at hand.
>
>
…[18 more quoted lines elided]…
> complex business rules we had.

Now you're talking... :-)

After I calmed down and everything was working I thought through exactly WHY 
I was annoyed.

I started working with objects around 12 years ago, first with Java and more 
recently with C#. Over that period of time new ideas and concepts have had 
time to "sink in". I've had this experience before, moving from Assembler to 
COBOL for example, and with various other packages and languages along the 
way.  It was always about computer programming and using technology to 
achieve results. But with the latest one I didn't really realize that my 
whole approach to designing and building systems has subtly moved. There was 
a time when I would have enjoyed throwing the bytes around and thought it 
was all "fun".

These days I don't think at that level. I see objects, with properties, 
events and behaviours. They are analogs of things in the real world and can 
interact and be manipulated just like real things.  I don't see record 
structures and files any more. I don't want to be counting bytes, there are 
methods and properties for doing that. I don't want to spend days poring 
over the best way to support ESQL;  write it in LINQ, assign it to a Lambda 
and forget about it. It isn't a series of tables with rows and columns any 
more, it is a SET of information that can be instanced and referenced as a 
single symbol. It can and should be manipulated as a SET, not row by row... 
(Robert Wagner posted at length about this a while back; I'm starting to 
understand what he was talking about.)

So, what is the fundamental difference between the way I see and do things 
now, and the way I used to?

It is a difference in focus:

In the old days I focussed on technology. Now I focus on functionality. I 
don't CARE how the operands in my buffer get replaced. I'm not interested 
one tiny bit in whether a subscript is slower than an index or whether I can 
save a few bytes with redefines or whether the buffer needs to be aligned to 
a word boundary for a given architecture. I just want them replaced. I need 
that functionality.

My frustration arose when I realized that the FUNCTIONALITY simply didn't 
work. It says "REPLACING", it doesn't say:"REPLACING IF THE LENGTHS ARE THE 
SAME"... I expected a certain functionality and it wasn't available. Because 
it wasn't I had to sit down and write it. And that threw me back into 
"technology focus" and I really don't like it any more.

Frederico, you are asolutely right about building libraries of functions and 
most of us have done that throughout our careers. For me, moving into OO and 
away from COBOL was just about technology change, at least for the first 
couple of years. But now I have reached a stage where it is so second nature 
to me that I really do just plug components together and smooth interfaces. 
I am presented with a problem and I immediately start thinking about the 
likely objects that will be needed and the functionality that will be 
required. (I DON'T think about record/table layouts and what data types must 
be accommodated...). In a formal situation Use Cases would be used to derive 
the objects.

Recently I've been getting to grips with SQL Server, which I have never 
really had much affinity for. Access meets most of my personal needs and I 
have dabbled with MySQL and PostgreSQL. (Both excellent...) In the old days 
I worked on DB2 sites and always found it adequate. Anyway, there are some 
things which were new to me about SQL Server (MSSQL) so I decided to invest 
in some education and searched the web for some suitable video tutorials. I 
found a facility called SQL Server Integration Services (SSIS). This takes 
the whole "functionality" view to another level.

In minutes, using a full graphical interface, you can define flows between 
objects, interfaces, sort, filter, add downstream feeds, handle errors, in 
fact, build something that would take days to write in COBOL (or any other 
procedural language), all by dragging and dropping what you need 
(functionality) to where you need it. Click a button and it runs. You can 
sample the data or view it at any point. Don't like the result? Shuffle 
things around and try again. I'm quite sure this package can't do EVERYTHING 
and it maybe doesn't deal well with things on the edge of the envelope, but 
I believe it may be a glimse of things to come.


> I, as some others I know, have build screen designers/managers that
> would allow us to just design the screen (using our own software) and
…[8 more quoted lines elided]…
>
Yep, so did I. Built my first screen painter that could produce screens (and 
corresponding buffers with attributes, PFKs, and AIDs) for IMS/DC or CICS 
BMS back in the late '70s, using mainframe COBOL and green 3270 screens. I 
even ported it to the PC when Micro Focus COBOL became available in the mid 
80s. (I've still got it somewhere. I sometimes thought about releasing it or 
selling it but it just seems so irrelevant in this day and age.)

But that was 25 years ago. Things have changed. I don't use ACCEPT and 
DISPLAY to drive GUI screens any more. That's what Windows is for.

<snipped code  - not really important here :-)>

Pete.
```

#### ↳ Re: Why COBOL is losing the POWER struggle

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-06-22T09:03:42-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<847v351ej4rrm2b183vmvn83pmk9r8oipm@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net>`

```
On Sun, 21 Jun 2009 05:22:24 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I have commented more than once here that the newer languages are simply 
>more concise and more powerful than COBOL. Less writing means fewer errors.

Possible.   But I've seen some subtle errors in very concise
languages, not to mention difficult to understand code.   This isn't
new - I worked in a shop that was at one time RPG only, and
programmers found things to do in RPG that it wasn't designed for.

Conciseness has advantages - and disadvantages.   There are other
criteria which I find to be much more useful in evaluating a
language's fit with particular business needs.
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-22T12:20:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1oeo31fjm@news5.newsguy.com>`
- **In-Reply-To:** `<847v351ej4rrm2b183vmvn83pmk9r8oipm@4ax.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <847v351ej4rrm2b183vmvn83pmk9r8oipm@4ax.com>`

```
Howard Brazee wrote:
> On Sun, 21 Jun 2009 05:22:24 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[5 more quoted lines elided]…
> languages, not to mention difficult to understand code.

Indeed. If Pete's thesis were true in general, we should all be
programming in APL.

There is no simple correlation between eliminating steps and
eliminating errors. Some steps are unnecessary and have a non-zero
probability of error, so eliminating them reduces the overall
probability of error. Some steps are error-prone, and if they can be
replaced with fewer, less-error-prone steps, that reduces the
probability of error.

But there are a host of examples from many fields where the opposite
is true. That's why we have failsafes and interlocks and checklists -
all extra steps introduced to reduce the overall probability of error.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T15:48:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ab1l8F1uo700U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <847v351ej4rrm2b183vmvn83pmk9r8oipm@4ax.com> <h1oeo31fjm@news5.newsguy.com>`

```
Michael Wojcik wrote:
> Howard Brazee wrote:
>> On Sun, 21 Jun 2009 05:22:24 +1200, "Pete Dashwood"
…[10 more quoted lines elided]…
> programming in APL.

:-)

I know some people in Madrid whowould fully endorse that idea... :-)

>
> There is no simple correlation between eliminating steps and
> eliminating errors.

Maybe not a simple correlation, but it is axiomatic that, given errors will 
occur in what you do, the less you do, the less you get wrong.


> Some steps are unnecessary and have a non-zero
> probability of error, so eliminating them reduces the overall
…[6 more quoted lines elided]…
> all extra steps introduced to reduce the overall probability of error.

I'll still go for concise simple code every time.

Pete.
```

#### ↳ Re: Why COBOL is losing the POWER struggle

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-22T12:09:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1oeo30fjm@news5.newsguy.com>`
- **In-Reply-To:** `<7a4k6jF1tog9jU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> In C# I can use a Regular Expression, code 3 lines and get on with more 
…[5 more quoted lines elided]…
> 4),");

Can you really? I'm pretty sure it's "Regex", with a lowercase "e". :-)

And in .NET COBOL, you can do exactly the same, since
System.Text.RegularExpressions.Regex is part of the framework. It
isn't part of C#.

The *only* difference between COBOL and C#, in the same environment
(ie, in the CLR), is the syntax for using Regex.Replace (and
String.ToUpper). And in any other environment, C# isn't even
available, so I think COBOL has the advantage there.

Incidentally, that's a rather suboptimal way of doing what you're
trying to do. No need to invoke outBuffer.ToUpper three times - after
the first time, you've replaced it with its uppercased version anyway.
(Or there wouldn't be any need to keep invoking it if your replacement
strings were in uppercase.) And since your regular expressions are
degenerate - they're all fixed strings with no regex operators -
there's no need to use Regex.Replace; String.Replace would do the job.
And rather than creating and discarding a handful of temporary
objects, use a mutable StringBuilder for multiple replacements:

StringBuilder tmpOutBuffer = new StringBuilder(outBuffer.ToUpper());
tmpOutBuffer.Replace(from, to);
...
outBuffer = tmpOutBuffer.ToString();

(Again, this would look essentially the same in .NET COBOL.)

In a single, standalone program, the difference is negligible; but if
this code were reused for large buffers in a service, where there
could be a lot of instances, that might have a significant effect on
resource consumption and performance.
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T15:50:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ab1o9F1ucfajU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <h1oeo30fjm@news5.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[40 more quoted lines elided]…
> resource consumption and performance.
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-23T16:34:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ab49rF1ue5j8U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <h1oeo30fjm@news5.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>>
…[10 more quoted lines elided]…
>

Yes, in C# it IS Regex (RegEx is for VB in Rational products.)



> And in .NET COBOL, you can do exactly the same, since
> System.Text.RegularExpressions.Regex is part of the framework. It
> isn't part of C#.

This is getting tiresome now so I won't be responding further.

I never said it WAS PART of C#... If you want to argue please READ WHAT I 
SAID (as you correctly did with my error on RegEx)

I said "In C# I _can use_ a Regular Expression..." Yes, I know, I can use 
one in COBOL too (I have done so) but the point was there is already a 
facility in COBOL which could reasonably be expected to server this purpose 
(outside of the .NET environment) and it doesn't.

> The *only* difference between COBOL and C#, in the same environment
> (ie, in the CLR), is the syntax for using Regex.Replace (and
> String.ToUpper). And in any other environment, C# isn't even
> available, so I think COBOL has the advantage there.

No, it doesn't because outside that environment it can't use Regex either. 
Why do you suppose I was using INSPECT... REPLACING in the first place? 
Don't you think if I had any choice I'd be using C#? COBOL has NO advantage 
and in fact, it simply disappoints because it can't do what one might 
reasonably expect of a function that claims to REPLACE.
>
> Incidentally, that's a rather suboptimal way of doing what you're
…[5 more quoted lines elided]…
> there's no need to use Regex.Replace; String.Replace would do the job.

Yes, I read several arguiments in C# forums about using string replace vs 
Regex. I could certainly have used it here but that wasn't my first thought. 
As for the upper case I did that to ensure a match as force of habit. In 
fact, I have case insensitivity set so I didn't need to do it at all.

Having established that I am not the world's greatest programmer and did not 
test the code I posted because it was an example written from memory, any 
more than I tested the COBOL code before posting it, can I just observe the 
following?:

1. My code generally works. (Some of it has been working in production for 
over 30 years).
2. If it isn't perfect, I don't care, as LONG as it works.
3. Neither myself nor others have any problems maintaining it.

These observations are true for every language I have ever programmed 
computers in, from NCR SLIP, through NEAT, NEAT3, IBM BAL, 1900 PLAN, 
Multiple varieties of COBOL, onto Intel and Motorola assemblers.

I really don't care if a buffer gets transposed more often than it needs to. 
If performance becomes a problem I'll look again at the code and seek to 
enhance it. This is exactly what I was talking about when discussing 
function and technology. What matters to me is the functionality; I want my 
operands transposed and I don't want to have to write 31 lines of code to do 
it, when there is a function in COBOL that purports to do it...

Having said that, I would PREFER that the code was better. It is part of a 
learning curve and I don't have a tutor, other than experience.

I'm still learning C# and I accept that I will write better code in it as 
time goes by.

In the meantime, I'm not going to wait until I'm perfect before developing 
applications.

> And rather than creating and discarding a handful of temporary
> objects, use a mutable StringBuilder for multiple replacements:
…[11 more quoted lines elided]…
> resource consumption and performance.

Well I'll keep an eye on it then... :-)

Seriously, thank you for the information.

I'll try and do better next time... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** riplin <riplin@Azonic.co.nz>
- **Date:** 2009-06-22T21:54:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e7ede08-232c-4665-8829-7f6ec1700f0e@y33g2000prg.googlegroups.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <h1oeo30fjm@news5.newsguy.com> <7ab49rF1ue5j8U1@mid.individual.net>`

```
On Jun 23, 4:34 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Michael Wojcik wrote:
> > Pete Dashwood wrote:
…[37 more quoted lines elided]…
> reasonably expect of a function that claims to REPLACE.

I am not sure why you had such difficulty with INSPECT REPLACING when
most Cobol programmers would have worked out what it could or could
not do, and how it did it, 35 years ago when it replaced EXAMINE.

It does do _exactly_ what one would reasonably expect from reading the
specs.


> > Incidentally, that's a rather suboptimal way of doing what you're
> > trying to do. No need to invoke outBuffer.ToUpper three times - after
…[30 more quoted lines elided]…
> it, when there is a function in COBOL that purports to do it...


INSPECT REPLACING _does_not_ purport to do what you attempted. The
specification says exactly what it will do.

It does replace characters.


> Having said that, I would PREFER that the code was better. It is part of a
> learning curve and I don't have a tutor, other than experience.
…[30 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-06-23T13:51:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1r8473i0@news7.newsguy.com>`
- **In-Reply-To:** `<7ab49rF1ue5j8U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <h1oeo30fjm@news5.newsguy.com> <7ab49rF1ue5j8U1@mid.individual.net>`

```
Pete Dashwood wrote:
> Michael Wojcik wrote:
>> Pete Dashwood wrote:
…[10 more quoted lines elided]…
> SAID (as you correctly did with my error on RegEx)

And I never said you said it was part of C#. I pointed out that what
you're doing in C# works precisely the same way in COBOL, in
environments where both exist. You claimed a contrast between C# and
COBOL; I pointed out the contrast is false, because the attribute in
question is not an attribute of either entity.

> I said "In C# I _can use_ a Regular Expression..." Yes, I know, I can use 
> one in COBOL too (I have done so) but the point was there is already a 
> facility in COBOL which could reasonably be expected to server this purpose 
> (outside of the .NET environment) and it doesn't.

Whether that's a "reasonable" expectation is subjective, of course.
I've noted in another post that I agree that expectation is the source
of the problem. This unfortunate aggregation of what should be
external features into the core language is a historical disadvantage
of older languages that were defined before componentization became a
significant concern in language design. On that, we agree.

>> The *only* difference between COBOL and C#, in the same environment
>> (ie, in the CLR), is the syntax for using Regex.Replace (and
…[3 more quoted lines elided]…
> No, it doesn't because outside that environment it can't use Regex either. 

Sure it can - it just has to call an external implementation,
precisely as it does in the .NET environment.

The point is that outside .NET, you *can* run a COBOL program, whereas
you can't run a C# one. Advantage COBOL.

>> Incidentally, that's a rather suboptimal way of doing what you're
>> trying to do. No need to invoke outBuffer.ToUpper three times - after
…[11 more quoted lines elided]…
> Having established that I am not the world's greatest programmer

Eh, who is?

> and did not
> test the code I posted because it was an example written from memory, any 
> more than I tested the COBOL code before posting it,

Sure - it was a Usenet post. I just went back and edited a message
before posting it because I realized it contained a glaring COBOL
error. A lot more of those no doubt slip through unnoticed by me.

> can I just observe the
> following?:
…[4 more quoted lines elided]…
> 3. Neither myself nor others have any problems maintaining it.

Sure. That's why I labeled my comment incidental. I thought it worth
making, because I assume most of us are interested in improving our
code and learning about the materials of our craft; but it wasn't
relevant to the main topic.

And Knuth rightly warns against premature optimization. StringBuffer
versus String tends to come up a lot in code, so it's one case where
it may be worth keeping an optimization in mind as you write code, but
for most programming tasks there aren't many of those. Source clarity
and working with tools that you know well usually trump optimization.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-24T12:08:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ad93hF1r4uo8U1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <h1oeo30fjm@news5.newsguy.com> <7ab49rF1ue5j8U1@mid.individual.net> <h1r8473i0@news7.newsguy.com>`

```
Michael Wojcik wrote:
> Pete Dashwood wrote:
>> Michael Wojcik wrote:
…[89 more quoted lines elided]…
> and working with tools that you know well usually trump optimization.

Thanks for this. I do value your posts and have learned from this exchange.

Pete.
```

#### ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-06-25T18:12:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kvT0m.264342$4p1.242353@en-nntp-03.dc1.easynews.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net>`

```
Pete,
  I haven't read this thread yet, but the "normal" way in COBOL ("COBOL-think") 
to do most regular expression stuff (and certainly this one) would be to 
UNSTRING your input into multiple fields, replace those that "match" what you 
want replaced and then to STRING them back together.  A PERFORM loop could be 
used if this was a particularly "performance sensitive" task (and MIGHT be 
faster).

Lack of "regular expression" handling (both at execution time AND at 
compile-time (e.g. COPY/REPLACING) is certainly a "lack" in COBOL.  The ability 
to create a user-defined function (or a method) to do what you want is there (in 
the Standard) but is probably NOT the solution that most would take.  In an IBM 
mainframe environment, if you are doing complex text manipulation tasks, the 
chances are that someone would suggest creating a REXX procedure to do it - 
instead of COBOL.  This highlights how COBOL (historically) plays in a 
"multi-language" environment.
```

##### ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-06-28T15:54:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ao7rlF209fcgU1@mid.individual.net>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <kvT0m.264342$4p1.242353@en-nntp-03.dc1.easynews.com>`

```
William M. Klein wrote:
> Pete,
>  I haven't read this thread yet, but the "normal" way in COBOL
…[3 more quoted lines elided]…
> them back together.

I considered this and other approaches, but, I was annoyed at the time and 
decided that  UNSTRING would require too much fiddling and setting up 
unstring areas. Richard posted a good example of doing it this way, but it 
is less efficeint and more code than the PERFORM loop. (However, it IS more 
"reusable")

I think the problem here is not that I don't know HOW or WHAT to do to get 
the result I want, rather, it was disappointment that something which I 
expected to work a certain way, simply didn't. It had been quite some time 
since I needed this requirement, I am working in three different languages 
(C#, COBOL, and, to a much lesser extent, Java) and I am getting old. I used 
an Upper Case function where I really didn't need to, simply as a matter of 
habit, and I had forgotten the fact that INSPECT ... REPLACING requires 
equal length operands. (I did know this and realised later it was a casualty 
of the thought processes occurring at another level. I guess I'm getting to 
the point where I can pull my whiskers and say: "Son, ah've fergotten more 
about COBOL than yew'll ever learn..." ... not that I would ever do that 
:-))

I am hammering through code, in full flow, and suddenly, something that 
should be a few lines, doesn't work and requires me to think at a much lower 
level and write 31 lines of relatively intricate code which then must be 
debugged. This simply breaks the flow and stops the roll I was on. Of course 
I got annoyed.

Posting a rant here made me feel better.


>A PERFORM loop could be used if this was a
> particularly "performance sensitive" task (and MIGHT be faster).
>
Depending on the cleverness of an optimizing compiler, it will almost 
certainly be faster, but that isn't why I chose it. It was quicker to write 
(for me) and less code, BUT, it took debugging time. Most importantly to me, 
it broke my train of thought and stopped something that was going like a 
train. I had been plugging OO objects together and achieving some really 
cool results and now, suddenly, I am jerked back to the world of bytes and 
loops and indexes, all because somethng that should REPLACE stuff, doesn't. 
Sure, I know it is documented and behaves as documented, and I SHOULD have 
remembered the limitation, but, I didn't.

> Lack of "regular expression" handling (both at execution time AND at
> compile-time (e.g. COPY/REPLACING) is certainly a "lack" in COBOL.

I'm not sure, Bill. If you use .NET COBOL you can use it, if you call to VB 
or C libraries, you can use it, mainframe COBOL can probably use it through 
Java... It's just "not easy" and not "intrinsic".  The problem I see here is 
not about Regex support in COBOL, it is about an existing facility being 
extended to do what it says it does. "REPLACE" should mean "Replace whatever 
you specify", not "Replace what you specify, as long as it is the same 
length as your source operand".



> The ability to create a user-defined function (or a method) to do
> what you want is there (in the Standard) but is probably NOT the
…[4 more quoted lines elided]…
> "multi-language" environment.

Fair comment.

I've responded to your comments because I know you are genuinely interested, 
but I've really said everything I wanted to on this topic (and I took the 
beating for it) so I won't be responding further. :-)

<snipped unreferenced original>

Pete.
```

###### ↳ ↳ ↳ Re: Why COBOL is losing the POWER struggle

- **From:** docdwarf@panix.com ()
- **Date:** 2009-06-28T15:29:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h2829a$ame$1@reader1.panix.com>`
- **References:** `<7a4k6jF1tog9jU1@mid.individual.net> <kvT0m.264342$4p1.242353@en-nntp-03.dc1.easynews.com> <7ao7rlF209fcgU1@mid.individual.net>`

```
In article <7ao7rlF209fcgU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>I think the problem here is not that I don't know HOW or WHAT to do to get 
>the result I want, rather, it was disappointment that something which I 
>expected to work a certain way, simply didn't.

Oh, I *cannot* resist...

... I've heard issuing from the cubicles of Junior Programmers the wail of 
'But why isn't it doing what it's *supposed* to?!?' for a few decades 
now.

After a bit of tutelage and some recourse to The Manual the conclusion is 
'It might be more fruitful not to expect a construct to work in a certain 
and more fruitful to be familiar with how The Manual says the construct 
should work... and even *then* you'll run across a surprise or two.'

[snip]

>I guess I'm getting to 
>the point where I can pull my whiskers and say: "Son, ah've fergotten more 
>about COBOL than yew'll ever learn..." ... not that I would ever do that 
>:-))

Whether you would or you wouldn't - BLL cells, anyone? - the boot in the 
buttocks seems to have been forgetting what it was you wanted to use.

[snip]

>Posting a rant here made me feel better.

It also allowed others to point fingers at you and laugh... not that 
anyone would do, at all times, what they were allowed to.

(for some reason I am reminded of a story told by teacher who, in 
Manhattan, saw an exhibitionist expose himself to a group of prostitutes.  
After a burst of laughter he heard one clear voice ring out with 'Honey, 
if I was you I'd keep that indoors!')

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
