[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Perform forever

_54 messages · 14 participants · 2005-09_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-06T15:26:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o4gk2F44vdgU1@individual.net>`

```
 
Does anyone have a favourite way of specifying that a PERFORM should 
continue indefinitely?

Consider the following code:

               move low-values to wpppauthorblurb
               perform until 1 = 2
                 perform get-input
                 if itsa-tag OR finished
                    exit perform
                 end-if
                 string
                      wpppauthorblurb
                         delimited by low-values
                      INPUT-RECORD (1:INPUT-LEN)
                         delimited by size
                      '<br> '
                         delimited by size
                            into
                              wpppauthorblurb
                 end-string
               end-perform

The first PERFORM should keep going until it is exited by the EXIT PERFORM 
on line 5.

The best I could do on the spot was create a condition that can never be 
true (1 = 2), but I think this is pretty lame...:-)

This is Fujitsu NetCOBOL but I'd be interested in seeing any solutions 
anyone has.

PERFORM FOREVER   would be cool...

Pete.
```

#### ↳ Re: Perform forever

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-09-06T03:47:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<3o4gk2F44vdgU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```


Pete Dashwood wrote:

>  
> Does anyone have a favourite way of specifying that a PERFORM should 
…[33 more quoted lines elided]…
> Pete.

My favorite way involved defining a condition name.

PERFORM UNTIL INFINITE-LOOP-DONE

Others might prefer a condition name such as HELL-FREEZES-OVER or 
DOCDWARF-GETS-THE-LAST-WORD.  The actual definition of the condition 
name is an exercise left to the programmer, but like all old mainframe 
programmers, I prefer a one character alphanumeric field.

With kindest regards, and apologies to DocDwarf...
```

##### ↳ ↳ Re: Perform forever

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-05T21:08:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125979722.501759.93200@g43g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net>`

```
> DOCDWARF-GETS-THE-LAST-WORD

Doesn't that always get to be true eventually, no matter how it takes ?
```

##### ↳ ↳ Re: Perform forever

- **From:** docdwarf@panix.com
- **Date:** 2005-09-06T05:08:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfjm9g$ftg$1@panix5.panix.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:

[snip]

>With kindest regards, and apologies to DocDwarf...

zzzzZZZZzzzzzz... zzzzaaAAWWWKKHHHHhhh... eh? whuh? huh?  Oh, sorry, I was 
just... resting my eyes, did I miss something?

DD
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-06T23:30:25+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o5cumF49s7dU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net>`

```
 
Thanks Arnold.

Comments below...

"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net...
>
>
…[40 more quoted lines elided]…
> PERFORM UNTIL INFINITE-LOOP-DONE

I immediately thought of using a condition name like FOREVER, but I'm 
ashamed to say  I  couldn't see how it would it work. (I was thinking of how 
I could attach an 88 level to a comparison, but of course, it really only 
needs to be a set value...Guess I've been away from COBOL too long :-)) Of 
course, some hours later, in the cool of the evening, I can see immediately, 
but I just couldn't at the time...

>
> Others might prefer a condition name such as HELL-FREEZES-OVER or 
> DOCDWARF-GETS-THE-LAST-WORD.  The actual definition of the condition name 
> is an exercise left to the programmer, but like all old mainframe 
> programmers, I prefer a one character alphanumeric field.

I agree on the one character (can't shake off my IBM youth where a CLI 
instruction was better than any alternative... :-)), but I studiously make 
no comment regarding the temperature of Hell or the loquaciousness of a 
certain dwarf... :-)

Pete.
```

##### ↳ ↳ Re: Perform forever

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-09-06T19:06:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1598d$431e2f06$45491c57$22316@KNOLOGY.NET>`
- **In-Reply-To:** `<Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <Yi8Te.13960$qY1.4299@bgtnsc04-news.ops.worldnet.att.net>`

```
Arnold Trembley wrote:
> Others might prefer a condition name such as HELL-FREEZES-OVER or 
> DOCDWARF-GETS-THE-LAST-WORD.

The latter definitely wouldn't mimic an infinite loop...  Of course, you 
could use "not" in front of it.  ;)
```

#### ↳ Re: Perform forever

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-05T20:59:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125979159.288975.177940@g49g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3o4gk2F44vdgU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
> This is Fujitsu NetCOBOL but I'd be interested in seeing
> any solutions anyone has.
>
> PERFORM FOREVER   would be cool...

Then look in your Fujitsu manual, Format 5 is:

    PERFORM WITH NO LIMIT

IMHO the EXIT PERFORM is poor usage and should be put in the same bin
as GO TO, NEXT SENTENCE, EXIT PARAGRAPH and EXIT SECTION (and a few
others).

For example, if I wanted to reuse part or all of the imperitive
statement in the in-line PERFORM I could extract it and make it a
performable paragraph. My definition of 'clean code' is that which can
be moved without regard to any positional dependencies. The EXIT
PERFORM is not clean code, it would fail to work as designed if moved
to a paragraph.

(Actually I think it would continue to work correctly in Unisys if I
understood what was said).
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-06T23:35:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o5d8sF401d3U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1125979159.288975.177940@g49g2000cwa.googlegroups.com>`

```
 

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1125979159.288975.177940@g49g2000cwa.googlegroups.com...
>> This is Fujitsu NetCOBOL but I'd be interested in seeing
>> any solutions anyone has.
…[5 more quoted lines elided]…
>    PERFORM WITH NO LIMIT

Ouch.

OK, it was quicker to post here than look there...(Hangs head and mumbles 
sheepishly...)
>
> IMHO the EXIT PERFORM is poor usage and should be put in the same bin
> as GO TO, NEXT SENTENCE, EXIT PARAGRAPH and EXIT SECTION (and a few
> others).
>
I'm a swinging voter. Undecided as yet. Ask me again in 20 years... :-) I 
restrained the urge to use EXIT SECTION :-).

> For example, if I wanted to reuse part or all of the imperitive
> statement in the in-line PERFORM I could extract it and make it a
…[6 more quoted lines elided]…
> understood what was said).

I believe it would continue to work as long as it was wrapped by the PERFORM 
and END-PERFORM :-)

Seriously, I take your point.

Thanks for the post.

Pete.
```

##### ↳ ↳ Re: Perform forever

- **From:** Peter Lacey <lacey@mts.net>
- **Date:** 2005-09-06T10:34:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<431DB6F3.F72C6244@mts.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1125979159.288975.177940@g49g2000cwa.googlegroups.com>`

```
Richard wrote:

> My definition of 'clean code' is that which can
> be moved without regard to any positional dependencies. The EXIT
> PERFORM is not clean code, it would fail to work as designed if moved
> to a paragraph.
> 


Can you write a program without at least one immovable statement?  I'd
have thought that at the very least you'd need the very first executable
statement to say PERFORM THE-PROGRAM.

PL
```

###### ↳ ↳ ↳ Re: Perform forever

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-09-06T15:56:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfke87$s1p$1@peabody.colorado.edu>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1125979159.288975.177940@g49g2000cwa.googlegroups.com> <431DB6F3.F72C6244@mts.net>`

```

On  6-Sep-2005, Peter Lacey <lacey@mts.net> wrote:

> Can you write a program without at least one immovable statement?  I'd
> have thought that at the very least you'd need the very first executable
> statement to say PERFORM THE-PROGRAM.

That statement seems redundant to me.   If it is necessary, wouldn't PERFORM
THE-PERFORM-THE-PROGRAM-PERFORM be necessary?
```

#### ↳ Re: Perform forever

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-05T21:05:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1125979546.273782.256380@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<3o4gk2F44vdgU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
> perform until 1 = 2

Some compilers may notice this and could either 1) optimize it as
always false or 2) flag an error that comparing two literals is
obviously wrong.
```

##### ↳ ↳ Re: Perform forever

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-09-06T17:33:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqkTe.256676$on1.72233@clgrps13>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1125979546.273782.256380@o13g2000cwo.googlegroups.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1125979546.273782.256380@o13g2000cwo.googlegroups.com...
>> perform until 1 = 2
>
> Some compilers may notice this and could either 1) optimize it as
> always false or 2) flag an error that comparing two literals is
> obviously wrong.

    If I were to write a COBOL compiler, I would try very hard for it do do 
(1) and try very hard for it not to do (2). The comparison of two literals 
is a valid expression (whose value, in this case, is "false"), and should be 
treated like any other valid expression (e.g. it shouldn't be flagged as an 
error).

    - Oliver
```

#### ↳ Re: Perform forever

- **From:** Steve Rainbird <steve.rainbirdxxxxx@mssint.com.removex>
- **Date:** 2005-09-06T09:47:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o53cdF46f37U1@individual.net>`
- **In-Reply-To:** `<3o4gk2F44vdgU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
Pete Dashwood wrote:
>  
> Does anyone have a favourite way of specifying that a PERFORM should 
…[36 more quoted lines elided]…
> 


In Microfocus

PERFORM UNTIL EXIT
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-06T23:36:52+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o5daoF49a68U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <3o53cdF46f37U1@individual.net>`

```
 

"Steve Rainbird" <steve.rainbirdxxxxx@mssint.com.removex> wrote in message 
news:3o53cdF46f37U1@individual.net...
> Pete Dashwood wrote:
>>  Does anyone have a favourite way of specifying that a PERFORM should 
…[42 more quoted lines elided]…
>
Oh Dear! That's horribly ambiguous...

Thanks for pointing it out, anyway.

Pete.
```

#### ↳ Re: Perform forever

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-06T02:49:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126000191.100198.280090@g47g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<3o4gk2F44vdgU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
> Consider the following code:

I much prefer:

       perform get-input
       move low-values to wpppauthorblurb
       perform
             with test after
             until itsa-tag OR finished

             string
                  wpppauthorblurb delimited by low-values
                  INPUT-RECORD (1:INPUT-LEN)
                               delimited by size
                  '<br> '   delimited by size
                  into wpppauthorblurb
               end-string
               perform get-input
       end-perform
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-06T23:22:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o5cf5F4aan6U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com>`

```
 

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1126000191.100198.280090@g47g2000cwa.googlegroups.com...
>> Consider the following code:
>
…[17 more quoted lines elided]…
>
Yes, you make a very good case, Richard.

I don't like (and use extremely rarely) PERFORM WITH TEST AFTER, but I 
understand why it is necessary here and you have managed to remove the 
requirement for PERFORM FOREVER..., which is a very useful way to solve 
problems... :-)

I think your solution is elegant and I'm going to use it.

Thanks.

Pete.
```

##### ↳ ↳ Re: Perform forever

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-06T14:55:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D5iTe.6626$4i6.5414@tornado.tampabay.rr.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com>`

```
For Pete in response to Richard:

Perform Forever is usually a way of saying "perform this until something 
happens somewhere else"....It's much easier to understand "perform this 
until exit condition is met".

DO...WHILE's were removed from popularity some time ago...

This is just a quick note, so no flaming if I'm wrong !  Just a gentle 
rebuke will be fine.

In Richard's example the problem is that you always execute the string with 
the low values.....but that's a small bug on his part (reverse the call and 
the initialize I would guess) :-)

BUT - What happens if you don't want to perform this at least once?  Say the 
first entry is - "no I don't want to do anything" ?   You may have to 
combine TEST BEFOREs with TEST AFTERs which is IMHO ugly.

I most often see what you want implemented as follows (which is not "a 
perform forever" as this could be a "perform never"....where Richard's is a 
"perform at least once").

This method means that there is duplicate code in the form of a condition 
set....I've seen issues where more was done than simply managing a condition 
so I don't like this: you can end up with a lot of "exit management" type 
code in two places.

PERFORM GET INPUT

IF  GET-EXIT-CRITERIA-MET
      SET EXIT-CONDITION TO TRUE
END-IF

PERFORM UNTIL EXIT-CONDITION

       PERFORM WHAT-YOU-WANT-TO-DO  {in line if short enough}

       PERFORM GET INPUT

       IF GET-EXIT-CRITERIA-MET
            SET EXIT-CONDITION TO TRUE
       END-IF
END-PERFORM

What I would do is actually just what the other posts were saying but 
without the exit perform -though I wouldn't mind the exit perform - it's 
just not my thing: I *personally* like logic that has no jumps except at 
conditions and the like....

01 CONDS          PIC X VALUE ' '.
     88 EXIT-CONDITION          VALUE 'X'.

PERFORM UNTIL EXIT-CONDITION
   PERFORM GET-INPUT

   IF GET-EXIT-CRITERIA-MET
      SET EXIT-CONDITION TO TRUE
   ELSE
      PERFORM WHAT-YOU-WANT-TO-DO  {in line if short enough}
   END-IF

END-PERFORM.

You could of course use NOT GET-EXIT-CRITERIA-MET but some people don't like 
negative checks....or you could have negative and positive conditions (some 
people don't like that because it's a nasty aliasing problem sometimes) 
...but that's all style and dependent on the amount of code and 
readability - they are to me all acceptable just at different times some are 
preferable :-)

I personally don't like the first branch of an IF checking the exception but 
whatever, that's cool :-)  I always put the AT END on a READ so 
inconsistency with myself is bearable.

JCE

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1126000191.100198.280090@g47g2000cwa.googlegroups.com...
>> Consider the following code:
>
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Perform forever

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-06T11:58:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126033089.875600.312430@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<D5iTe.6626$4i6.5414@tornado.tampabay.rr.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <D5iTe.6626$4i6.5414@tornado.tampabay.rr.com>`

```
> In Richard's example the problem is that you always execute the string with
> the low values...

Oops, remove 'with test after'.

      perform get-input
       move low-values to wpppauthorblurb
       perform
             until itsa-tag OR finished

             string
                  wpppauthorblurb delimited by low-values
                  INPUT-RECORD (1:INPUT-LEN)
                               delimited by size
                  '<br> '   delimited by size
                  into wpppauthorblurb
               end-string
               perform get-input
       end-perform
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-07T11:49:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o6o83F4epd8U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com>`

```
 
When I came to insert Richard's solution into the program I realised that it 
cannot work.

I liked the idea very much and I liked removing the need for PERFORM 
FOREVER, but the suggested solution, for me, is not practical. (The main 
'advantage' is the avoidance of EXIT PERFORM, and I don't have the same 
aesthetic objection to that that Richard does. I DO have an aesthetic 
objection to PERFORM WITH TEST BEFORE  (I think it is confusing because it 
is easier to 'manage' PERFORM code when it works consistently, and there is 
one thing less to have to think about every time you write it.))

I also feel uncomfortable about getting input and NOT checking immediately 
whether it is a tag or EOF...

I understand that much of this is simply opinion, and I am grateful for all 
the posts received, particularly Richards suggestion.

To help clarify for the bewildered lurker here is some quick background from 
the REMARKS:

*    This program reads a text file containing data from The Write Place
*    column in Saturday's BOP Times, and writes it to the MEDEA database.
*
*    The MEDEA database is used to generate dynamic HTML pages when the
*    Write Place archives are accessed from the Tauranga Writers website.
*
*    INPUT:
*         A line sequential text file containing the following tagged
*          lines:
*          %1
*          Write Place for (date)
*          %2
*          Heading (as added by newspaper subs.)
*          %3
*          Write Place text = any number of lines in plain text -
*          line breaks, blank lines, and indenting should be preserved
*          %4
*          Poet's corner - this will be ignored because it is not
*          required except as a placemarker
*          %5
*          Title of poem
*          %6
*          Text of poem  = any number of lines in plain text -
*          line breaks, blank lines, and indenting should be preserved
*          %7
*          Poet's name
*          %8
*          A blurb about the poet  = any number of lines in plain text -
*          line breaks, blank lines, and indenting should be preserved
*
*     OUTPUT:
*          Correctly populated rows on the writeplace table of
*          the MEDEA DB, with the sequential key generated and added.
**
The code snippets are dealing with handling the %8 tag. On entry we have the 
%8 tag sitting in the input and must grab all the lines up until the next 
tag (or EOF). These are strung into a field which will be written to the 
database. Each input line has a <br> HTML tag appended to it before being 
strung into the output buffer, so that when it is retrieved the original 
line breaks are preserved.

Here is the code I have ended up with:
           ...
           when '%8 '
               move low-values to wpppauthorblurb
               perform until forever
                    perform get-input
                    if itsa-tag OR finished
                       exit perform
                    end-if
                    string
                        wpppauthorblurb
                             delimited by low-values
                        INPUT-RECORD (1:INPUT-LEN)
                             delimited by size
                        '<br> '
                             delimited by size
                        into
                              wpppauthorblurb
                     end-string
               end-perform
            ...
And here is the get-input subroutine....

*-------------------------------------------------------------------
 get-input section.
 gi000.
     read INPUT-FILE
        AT END
              set finished to TRUE
        NOT AT END
              set not-finished to true
              if INPUT-RECORD (1:1) = '%'
                   set itsa-tag to TRUE
                   move INPUT-RECORD (1:3) to current-tag
              else
                   set not-atag to TRUE
                   move space to current-tag
              end-if
     end-read
     .

Many thanks to all who contributed their viewpoints and code on this.

Pete.

TOP POST - nothing new below...

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1126000191.100198.280090@g47g2000cwa.googlegroups.com...
>> Consider the following code:
>
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Perform forever

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-08T04:36:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wdPTe.28760$xl6.5793@tornado.tampabay.rr.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net>`

```
Pete,

I think it's interesting that you've approached the problem of parsing the 
document in a manner that is opposite to the way that I would have done 
given what I can see from your example.  This may be because I've 
predominantly used SAX XML processors versus DOM XML processors...it's 
faster and easier to manage for the small config files that I've built in 
the past.

Your approach is to actively "process" the document: that is read and look 
for certain things, and then based on conditions take action.

That is : < if I get a %8 tag loop through until i get to the next tag or 
end of file >

I would work more on a passive "callbackish" mechanism where the READ 
continues until it reaches the end, or there is a I/O issue and depending on 
the nature of the data calls the appropriate method - perhaps more passive 
but far more flexible.  The flow through the document is very predictable 
and simply managed.

That is : <if I get a %tag then call "I-GOT-A-TAG" if I get text then call 
"I-GOT-TEXT">

So the code for your %8 tag would look somewhat like:

READ FILE
AT END
      ..done...
NOT AT END
    PERFORM SIMPLE-DATA-PARSING
    IF TAG THEN
         PERFORM NEW-TAG
         PERFORM HANDLE-TAG
    ELSE
         PERFORM HANDLE-TEXT
END-READ

NEW-TAG.
      EVALUATE CURRENT-TAG
        WHEN 1....
        WHEN 2....
        WHEN 8...WRITE DATA
        OTHER...
      END-IF.

HANDLE-TAG.
      MOVE NEW-TAG TO CURRENT-TAG
      EVALUATE NEW-TAG
        WHEN 1....
        WHEN 2....
        WHEN 8....
        OTHER...
      END-IF.

HANDLE-TEXT.
      EVALUATE CURRENT-TAG
        WHEN 1....
        WHEN 2....
        WHEN 8....PERFORM STRING-IT
      END-EVALUATE.

I'm not suggesting that I'm right, it's just another approach...as a *very* 
good songwriter once declared "a point of view creates more waves".....

Some comments instreamed also.

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3o6o83F4epd8U1@individual.net...
>
> When I came to insert Richard's solution into the program I realised that 
…[4 more quoted lines elided]…
> aesthetic objection to that that Richard does.

I found it to be more practical advice than aesthetic opinion; however, 
given the limited audience and modifiers of your code it's perhaps not a 
practicality that has much worth...I know your feelings on source code 
management :-)

> I DO have an aesthetic objection to PERFORM WITH TEST BEFORE  (I think it 
> is confusing because it is easier to 'manage' PERFORM code when it works 
> consistently, and there is one thing less to have to think about every 
> time you write it.))

Perhaps COBOL is not your optimum language for that philosophy :-) I assume 
you mean that you have an objection to the explicit "WITH TEST BEFORE" given 
that is likely the default (I don't follow or care about standards that much 
to know if its a standards default or just my vendor default).

> I also feel uncomfortable about getting input and NOT checking immediately 
> whether it is a tag or EOF...

There's a lot to be said for locality of function.

> I understand that much of this is simply opinion, and I am grateful for 
> all the posts received, particularly Richards suggestion.

Yeah, screw the rest of us ;-)

> To help clarify for the bewildered lurker here is some quick background 
> from the REMARKS:
…[114 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-09-08T05:10:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RIPTe.303553$WN5.83098@fe02.news.easynews.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com>`

```
For what its worth, both of you MIGHT be interested in how the Standards 
committees are TRYING to add "native" syntax to COBOL to handle all of this. 
See:

 http://www.cobolportal.com/j4/files/05-0211.doc

and browse the "Concepts" section.

J4 is working quite hard to get a "revised" version of this done for the WG4 
meeting in October, so I think any problems, ideas, whatever that you have MIGHT 
be of particularly "timely" import.

I know Pete's usual opinion of J4/WG4 work (and I don't disagree fundamentally 
with it) but I still think that comments on this document MIGHT prove useful for 
what some COBOL implementors actually provide.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-07T22:55:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126158949.473890.314280@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<RIPTe.303553$WN5.83098@fe02.news.easynews.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com> <RIPTe.303553$WN5.83098@fe02.news.easynews.com>`

```
> that comments on this document MIGHT prove useful

Personally I find the approach that they have taken to be completely
useless.  I tend to prefer working with dynamic languages (especially
Python) and try to build programs that don't embody the data variables
in the source code. Typically I will have a configuration file that
gives names to the data fields on input and templates for output that
use the names. The program just manipulates dictionaries and lists.

This is helped by database access providing a dictionary of tuples for
the results of a select.

XML output is easy to process with templates. In fact the templating
does not even need to know it is XML, by specifying a different
template file name the output could be CSV, or HTML, or Postscript or
simple text report.

Processing input is rather more complicated but is not far removed from
dealing with other formats such as HTML or EDIFACT.  In many cases it
is necessary to pick out the parts that are required and ignore the
bits that are irrelevant to the problem. This allows the sender to add
tags for other purposes without affecting the program. An input
processing program should also cater for alternate ways of specifying
the data.

Building a program that must exactly match the structure of the XML is
the exact antithesis of what I would consider rational. It gives no
flexability, it would require recompiling for every fiddly change in
format and it seems to me to be very much a '70s style structure.

Consider: we moved from fixed FDs to the more flexible SQL database
where we can have a 'view' that subsets or a join that supersets the
fields.  XML is even more structurally flexible and yet J4 is
attempting to make it rigidly inflexible with 'FDs' that even removes
the ability to name differently.

> committees are TRYING to add "native" syntax to
COBOL

They are wasting their time (IMHO). They should be adding native
support for tuples, lists, dictionaries and templating and then use
these to handle XML in a parametarised way. Never mind, I'll do it in
Python.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-09T01:16:27+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3oartiF4vqoeU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com> <RIPTe.303553$WN5.83098@fe02.news.easynews.com> <1126158949.473890.314280@g14g2000cwa.googlegroups.com>`

```
 

"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1126158949.473890.314280@g14g2000cwa.googlegroups.com...
>> that comments on this document MIGHT prove useful
>
> Personally I find the approach that they have taken to be completely
> useless.

Me too. Though not for quite the same reasons. (I don't disagree with your 
reasons...)

> I tend to prefer working with dynamic languages (especially
> Python) and try to build programs that don't embody the data variables
…[24 more quoted lines elided]…
>

Absolutely.

> Consider: we moved from fixed FDs to the more flexible SQL database
> where we can have a 'view' that subsets or a join that supersets the
…[11 more quoted lines elided]…
>

I think 'should' is too strong in the above (I don't think they 'should' be 
doing anything with XML; to me it is not a language dependent facility and 
components exist to parse it anyway), but I concur fully with your 
conclusions.

I had a quick look at Python a few weeks back and have it marked for 'more 
investigation'. Do you find it useful?

Pete.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 7)_

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2005-09-08T14:59:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ilYTe.166445$wr.47296@clgrps12>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com> <RIPTe.303553$WN5.83098@fe02.news.easynews.com> <1126158949.473890.314280@g14g2000cwa.googlegroups.com> <3oartiF4vqoeU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3oartiF4vqoeU1@individual.net...
> I had a quick look at Python a few weeks back and have it marked for 'more 
> investigation'. Do you find it useful?

    I had a university professor who was very fond of Python, so in that 
course, it was a requirement that all our assignments and the final project 
be written in Python.

    Except for one issue (which I will get to later), I found the language 
as useful, expressive, easy-to-use, whatever as any other language. I don't 
like the way they implemented object-oriented stuff ("private" variables are 
faked by some sort of name mangling system, and an instance of the current 
object has to actually be passed to every method of that object), but they 
weren't real "show-stoppers" for me. Similarly, usually don't like 
weakly-typed languages (which Python is), but I can force myself to think 
longer and harder about my code instead of depending on compile-time errors 
without too much aggravation.

    The real annoyance for me, though, was that Python does not ignore 
whitespace. The way Python knows when a the body of a loop-type construct 
ends, for example, is when the indentation changes. I prefer languages that 
use explicit tokens to mark the beginning and end of structures (e.g. 
"PERFORM" and "END-PERFORM" in COBOL, or "{" and "}" in Java, C, C++, etc.) 
I just couldn't get used to the idea that the indentation would actually 
affect the semantics of my program. So that's why *I* personally don't use 
Python.

    Might be less of an issue for programmers who are already used to taking 
into account whether their code lies in Area A or Area B.

    - Oliver
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-09T03:25:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ob3ekF53u6kU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com> <RIPTe.303553$WN5.83098@fe02.news.easynews.com> <1126158949.473890.314280@g14g2000cwa.googlegroups.com> <3oartiF4vqoeU1@individual.net> <ilYTe.166445$wr.47296@clgrps12>`

```
 
Thanks Oliver,

valuable feedback and very perceptive. (I  think you're probably right about 
people used to indenting at A and B margins having less problem with it.)

I guess it would be possible to use braces, as in Java etc. then simply edit 
them into tabs (?), or use a similar type of 'transformation' or 
'precompile'.

I'm too busy to look at it at the moment but I do plan on doing so.

Pete.

TOP POST - nothing new below.

"Oliver Wong" <owong@castortech.com> wrote in message 
news:ilYTe.166445$wr.47296@clgrps12...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
…[32 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 8)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-09-08T11:55:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1126205753.195570.292930@o13g2000cwo.googlegroups.com>`
- **In-Reply-To:** `<ilYTe.166445$wr.47296@clgrps12>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com> <RIPTe.303553$WN5.83098@fe02.news.easynews.com> <1126158949.473890.314280@g14g2000cwa.googlegroups.com> <3oartiF4vqoeU1@individual.net> <ilYTe.166445$wr.47296@clgrps12>`

```
> The way Python knows when a the body of a loop-type construct
> ends, for example, is when the indentation changes.

Yes, that was an annoyance for me when my editor would put tabs in the
source. One needs to have an editor which will automatically always use
spaces or always use tabs otherwise you are screwed.  It is also useful
to have a block-indent/outdent feature.

It does force the use of correct indenting and does make it easier to
see the structure correctly once you get used to it.  In other
languages sometimes poor indenting hides the actual structure.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-09T01:05:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3oar9gF50bi4U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com> <RIPTe.303553$WN5.83098@fe02.news.easynews.com>`

```
 

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:RIPTe.303553$WN5.83098@fe02.news.easynews.com...
>
> For what its worth, both of you MIGHT be interested in how the Standards 
…[13 more quoted lines elided]…
> MIGHT prove useful for what some COBOL implementors actually provide.

Bill, my disagreements about the approach to XML in COBOL being adopted by 
the committee, go WAY beyond my general opinion of J4/WG4 (which is a matter 
of record and don't get me started... :-)) I see it as simply wasting a lot 
of valuable time and resource on something that has already been solved. I 
process XML in COBOL using an XML parser component provided free as part  of 
my Operating Environment. It is the same principle as using ODBC to connect 
to a Database, or using a component to provide a Tree View, or scheduling 
grid; it isn't required to be part of the language. While time is spent on 
this there are things that ARE required which we don't have.

Sadly, (or perhaps not...) I no longer use COBOL enough to care what they do 
with it.

I love the language, and always will, but I was heartbroken by the hijacking 
of it long ago. Now, it is just an old flame that I meet on the street and 
go for coffee with...We remember old times, exchange pleasantries, then go 
our respective ways... I have Java, ASP,  and JavaScript waiting for me at 
home; they are fundamentally Object Oriented and understand how I need the 
Web...(I'm flirting with PHP and Python also at the moment but it's not 
serious yet :-))

I stopped making a living from COBOL years ago. I don't have the right to 
criticise J4/WG4, even though I do have the right to an opinion about 
them...

Pete.
<snipped remainder>
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-09T00:40:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3oapq6F52j0hU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com>`

```
 

"jce" <defaultuser@hotmail.com> wrote in message 
news:wdPTe.28760$xl6.5793@tornado.tampabay.rr.com...
>
> Pete,
…[6 more quoted lines elided]…
> the past.

My experience of this has been mainly with DOM, but I don't think it 
coloured my judgement. The solution was devised using the same principles I 
ALWAYS use when writing computer program code:

1. Small is beautiful.
2. Avoid duplication. Say it once unless there is really no other viable 
way.
3. Format code to be clear.
4. Check results from subroutines immediately on return (locality of code, 
if you like)
5. In COBOL, let it document itself.
6. Write it top down.
7. Use the power of the language. (Unless you are writing code for someone 
else, whose standards preclude you from doing so.)

We have departed a long way from the discussion of PERFORM FOREVER and this 
code  was not intended for public display when it was written, or meant to 
be an example of anything other than a specific problem solution, as I see 
it. However, I have posted more than  originally intended because it made 
sense to do so and the discussion is an interesting one. I don't plan to 
publish the full program here, even when it is complete (sighs of relief all 
round... :-)).
>
> Your approach is to actively "process" the document: that is read and look 
…[4 more quoted lines elided]…
>
Yes, I did consider the prossibility of doing it as you suggest.

The approach adopted uses the tags to drive the process. There is a certain 
amount of similar (though not exactly the same) code. The advantage is that 
it is easy to add further tags in the future, and it is easy to find 
immediately in the source where the processing for a given tag occurs. There 
is also no requirement for the data to contain tags in any particular 
sequence. Each tag is used to identify data that will update a specific 
database field. (Except for the END OF TAG SET tag which triggers writing to 
the database.)

> I would work more on a passive "callbackish" mechanism where the READ 
> continues until it reaches the end, or there is a I/O issue and depending 
…[3 more quoted lines elided]…
>
I don't see how that is 'more flexible'. I can easily add new tag processing 
or change existing tag processing without complex logic or remembering what 
tag I'm on. The document consists of a series of tag sets. The flow through 
each set is simple.

> That is : <if I get a %tag then call "I-GOT-A-TAG" if I get text then call 
> "I-GOT-TEXT">
>

That would eliminate some of the code, certainly. On balance, I decided 
against it, but I don't think this is a 'wrong' approach, or that the 
approach I have adopted is the only (or even necessarily the best) viable 
one.

> So the code for your %8 tag would look somewhat like:
>
…[27 more quoted lines elided]…
>      END-IF.

Up to here, this is almost exactly how it works, except I see no need for 
TWO EVALUATES. Here is the actual control logic:

 PROCEDURE DIVISION.
 main section.
*
*  General process flow is as follows:
*  Get input and check for tags
*  Process each tag, loading respective HVs with the data
*  At end of 'tag set' write the HVs to the writeplace table
*  Repeat until EOF
*
 control-logic.
     open input INPUT-FILE
     set not-finished to TRUE
     set not-atag to TRUE
     set not-forever to TRUE
     move zero to in-count out-count display-count tagset-count
     move low-values to
                        wpauthorlastname   *> These are Host Variables for 
SQL
                        wpauthorfirstname
                        wphed
                        wptext
                        wpppauthorlastname
                        wpppauthorfirstname
                        wppptitle
                        wpppfirstline
                        wppptext
                        wpauthorblurb
                        wpppauthorblurb
                        wpppaside           *> This init is really not 
necessary as each HV is initialised
                                                   *>  before use. I may 
remove it later. Meanwhile...
                                                   *>  'belt and braces'.
     EXEC SQL
          connect to 'MEDEA'
     END-EXEC
     if SQLSTATE  = '00000'
         perform process-cycle
         until finished
     else
        display 'Connection failed - SQLSTATE ='  SQLSTATE upon syserr
        display SQLMSG upon syserr
     end-if
     close INPUT-FILE
     stop run
     .
*-----------------------------------------------------------------
 process-cycle section.
 pc001.
     perform get-input
        until itsa-tag
        OR
        finished
     if itsa-tag
        evaluate current-tag
           when '%1 '  *> 'Write Place for (date)' beginning of tag set
                   (processing for %1 tag here)
           when '%2 '
                    (processing for %2 tag here)
           ...and so on...
        end-evaluate
     end-if
     .

This approach will flush (ignore) any data that is there without a tag at 
the start of the document or between tag sets, without any specific logic 
being required to trap these conditions. The processing for each tag leaves 
the document positioned on the next tag (or EOF).
>
> HANDLE-TEXT.
…[5 more quoted lines elided]…
>
The problem is that STRING-IT cannot easily be  a generalised routine 
because it involves Host Variables of different size.
And there are now THREE EVALUATES in your solution.

I believe ONE is adequate. Again, it is a personal preference, not a 
question of right or wrong.

> I'm not suggesting that I'm right, it's just another approach...as a 
> *very* good songwriter once declared "a point of view creates more 
> waves".....

Sure, thanks for the input.

>
> Some comments instreamed also.
…[14 more quoted lines elided]…
> management :-)

You do? :-) If you mean that I don't believe in it, that is true for 
COMPONENTS. This is a batch process. Later it will be rewrapped into 
PowerCOBOL and the code will be extensively hacked about (by me) so that it 
will NOT be a batch process and tag processing will occur interactively. I 
don't expect that to be problematic.

>
>> I DO have an aesthetic objection to PERFORM WITH TEST BEFORE  (I think it 
…[3 more quoted lines elided]…
>

OUCH! On reading that again, I should have said 'WITH TEST AFTER', BEFORE 
is, of course, the implicit default for every COBOL I have ever written 
(<disclaimer> Comment may not apply to UNISYS sites, and no criticism of 
them is expressed or implied </disclaimer>).

> Perhaps COBOL is not your optimum language for that philosophy :-) I 
> assume you mean that you have an objection to the explicit "WITH TEST 
…[3 more quoted lines elided]…
>
Yes.

>> I also feel uncomfortable about getting input and NOT checking 
>> immediately whether it is a tag or EOF...
…[6 more quoted lines elided]…
> Yeah, screw the rest of us ;-)

That is neither true nor fair. I have followed and considered all comments 
posted to this thread and found it interesting. I happened to like Richard's 
solution because it removed the need for PERFORM FOREVER altogether and to 
me, removing a problem entirely is always an elegant solution. I know your 
commment was made with tongue in cheek, but I assure you I value all the 
posts made in response to my specific request.

>
>> To help clarify for the bewildered lurker here is some quick background 
…[87 more quoted lines elided]…
>>
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 5)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-08T13:12:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9NWTe.35074$p_1.22800@tornado.tampabay.rr.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com> <3oapq6F52j0hU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3oapq6F52j0hU1@individual.net...
>>> I understand that much of this is simply opinion, and I am grateful for 
>>> all the posts received, particularly Richards suggestion.
…[8 more quoted lines elided]…
> you I value all the posts made in response to my specific request.

If you know it's tongue in cheek why get defensive!

I think your record of always (that I can recall) posting a follow up or 
response to a request says enough :)

JCE
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-09T03:31:03+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ob3pvF52mgiU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <1126000191.100198.280090@g47g2000cwa.googlegroups.com> <3o6o83F4epd8U1@individual.net> <wdPTe.28760$xl6.5793@tornado.tampabay.rr.com> <3oapq6F52j0hU1@individual.net> <9NWTe.35074$p_1.22800@tornado.tampabay.rr.com>`

```
 

"jce" <defaultuser@hotmail.com> wrote in message 
news:9NWTe.35074$p_1.22800@tornado.tampabay.rr.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
…[13 more quoted lines elided]…
> If you know it's tongue in cheek why get defensive!

Er... because many people read this and some of them (who may not even have 
English as a first language) may miss the subtlety?


>
> I think your record of always (that I can recall) posting a follow up or 
> response to a request says enough :)
>
I do my best :-)
Pete
```

#### ↳ Re: Perform forever

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-09-06T14:11:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfk83e$op7$1@peabody.colorado.edu>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```

On  5-Sep-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> The best I could do on the spot was create a condition that can never be
> true (1 = 2), but I think this is pretty lame...:-)

You may need to say ONE = TWO, so the compiler doesn't recognize that it's
always false.   Don't worry about it being somehow lame.   If it is obvious and
it works, how can it be lame?
```

##### ↳ ↳ Re: Perform forever

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-06T15:18:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7riTe.6629$4i6.1861@tornado.tampabay.rr.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <dfk83e$op7$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:dfk83e$op7$1@peabody.colorado.edu...
>
> On  5-Sep-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
…[7 more quoted lines elided]…
> it works, how can it be lame?

Donald Trump's "piece" is obvious and it works - want to defend that not 
being lame?

JCE
```

###### ↳ ↳ ↳ Re: Perform forever

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-09-06T16:01:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfkegl$s8b$1@peabody.colorado.edu>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <dfk83e$op7$1@peabody.colorado.edu> <7riTe.6629$4i6.1861@tornado.tampabay.rr.com>`

```

On  6-Sep-2005, "jce" <defaultuser@hotmail.com> wrote:

> > You may need to say ONE = TWO, so the compiler doesn't recognize that it's
> > always false.   Don't worry about it being somehow lame.   If it is
…[4 more quoted lines elided]…
> being lame?

I'm not familiar with his "piece". What definition of "lame" applies to these
two sentences?

Code that works and is obvious isn't crippled.   It isn't a fabric interwoven
with threads of metal.   It isn't someone who doesn't understand what is going
on.  It isn't pathetically lacking in force or effectiveness.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 4)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-06T16:44:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mHjTe.6692$4i6.2125@tornado.tampabay.rr.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <dfk83e$op7$1@peabody.colorado.edu> <7riTe.6629$4i6.1861@tornado.tampabay.rr.com> <dfkegl$s8b$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:dfkegl$s8b$1@peabody.colorado.edu...
>
> On  6-Sep-2005, "jce" <defaultuser@hotmail.com> wrote:
…[10 more quoted lines elided]…
> I'm not familiar with his "piece".

Maybe I jumped the gun.

http://globalguestpoll.com/vote.cgi?handle=HAIR111&VOTE=A&SUBMIT1=Results

>What definition of "lame" applies to these
> two sentences?
…[4 more quoted lines elided]…
> on.  It isn't pathetically lacking in force or effectiveness.

Any of the definitions not found in the fuddy duddy books of m-w.  The code 
1=2 is lame - even Pete acknowledges that fact!  Doesn't make doing it 
reprehensible...it's just lame.

Here are some _real_ uses of the word lame.  Same question to you - how do 
your definitions apply.

--------------------
sarah got a butterfly tattoo on her lower back. that's so lame, i'd rather 
get a "Bite Me" on my butt, at least i'll be more original.

Diddy sucks, he's so lame

Dude, it's ****ing lame camping on this map. Lame noob - I'll pwn him next 
round.

DocDwarf's posts on clc are super-lame if you do nae have a sense of humour

That dillhole wears technocolor t-shirts, that's SO LAME!
--------------------

No more posts from me on the relevance and use of dictionaries :^)
JCE
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2005-09-06T13:29:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfkjm9$358$1@panix5.panix.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <7riTe.6629$4i6.1861@tornado.tampabay.rr.com> <dfkegl$s8b$1@peabody.colorado.edu> <mHjTe.6692$4i6.2125@tornado.tampabay.rr.com>`

```
In article <mHjTe.6692$4i6.2125@tornado.tampabay.rr.com>,
jce <defaultuser@hotmail.com> wrote:

[snip]

>DocDwarf's posts on clc are super-lame if you do nae have a sense of humour

zzzzznnnuuurrrkkkhhh... sssssskkkNNNXXXXxxxx... huh? whuh?  Some folks 
might say were I any more lame I'd need a crutch... others would rather 
see from me less laming and more halting.

(note to those for whom English is not a primary language: 'halt' is one 
of those wonderful words with more than one definition.  On the one hand 
it can be 'to limp or hobble', hence the old phrase 'the halt and the 
lame'; the more common use is 'to stop')

DD
```

#### ↳ Re: Perform forever

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-09-06T11:48:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfko6u$24h4$1@si05.rsvl.unisys.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
The idea of a "perform forever" in COBOL was brought up some time ago as a
possible new feature for standard COBOL.

I think to have a fully symmetrical syntax for this, however, it pretty much
requires that the contexts in which EXIT PERFORM is allowed be expanded to
"out-of-line" PERFORMs, and there was a *lot* of resistance to that idea at
WG4.

From a performance standpoint, the implementor always has the ability to
detect the use of, say, a condition-name whose data item is never changed,
and eliminate the test code altogether, so there's no particular *practical*
advantage of, say, PERFORM ... WITH NO TEST (thereby avoiding the addition
of a new reserved word FOREVER) over what the programmer might be able to do
on his own.

And since the programmer *can* accomplish this today through syntax like
"UNTIL PIGS-FLY", there's not a whole lot of support for adding *yet
another* way to do this in standard COBOL.

Personally, I'm with you, Pete.  ALGOL has WHILE TRUE DO BEGIN ... END and
DO BEGIN ... END UNTIL FALSE,  Pascal has REPEAT ... UNTIL FALSE and WHILE
TRUE DO ..., and SDL/UPL, arguably the closest to a Dijkstra-compliant
language I know of, had DO FOREVER as its only looping mechanism.  I think
the lack of *syntactic* support for the equivalent in COBOL is quaint.

But I understand the argument that it's so trivial to do the same thing
through conditionals there's not much point in adding syntax for it, and I
think that's the main reason you're not going to see it in standard COBOL.

    -Chuck Stevens
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-07T12:12:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o6piqF4ib50U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <dfko6u$24h4$1@si05.rsvl.unisys.com>`

```
 

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message 
news:dfko6u$24h4$1@si05.rsvl.unisys.com...
>
> The idea of a "perform forever" in COBOL was brought up some time ago as a
…[31 more quoted lines elided]…
>
Thanks Chuck, interesting background.

I understand why it isn't in COBOL and I don't feel deprived... :-)

I haven't been writing COBOL for some time and chose to do this exercise in 
it because it is primarily a batch process doing data processing. (Best 
tools for the job... :-)). There is a big backlog of newspaper columns that 
need to be archived to our database; COBOL makes sense.  When I came back to 
coding in COBOL I suddenly realised there was no PERFORM...FOREVER and it 
prompted my post.

Pete.
```

#### ↳ Re: Perform forever

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2005-09-06T13:38:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o69h8F4ffv9U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
If only the following were possible!:

               move low-values to wpppauthorblurb
               perform until get-input = itsa-tag or finished
                 string
                      wpppauthorblurb
                         delimited by low-values
                      INPUT-RECORD (1:INPUT-LEN)
                         delimited by size
                      '<br> '
                         delimited by size
                            into
                              wpppauthorblurb
                 end-string
               end-perform

Yes, I learned C before I learned COBOL.

I'd guess that if get-input was a user-defined function instead of a
paragraph then this might actually work, but...

(Of course this doesn't actually answer your question...)

Frank

--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> Pete Dashwood<dashwood@enternet.co.nz> 9/5/2005 9:26:52 PM >>>
 
Does anyone have a favourite way of specifying that a PERFORM should 
continue indefinitely?

Consider the following code:

               move low-values to wpppauthorblurb
               perform until 1 = 2
                 perform get-input
                 if itsa-tag OR finished
                    exit perform
                 end-if
                 string
                      wpppauthorblurb
                         delimited by low-values
                      INPUT-RECORD (1:INPUT-LEN)
                         delimited by size
                      '<br> '
                         delimited by size
                            into
                              wpppauthorblurb
                 end-string
               end-perform

The first PERFORM should keep going until it is exited by the EXIT PERFORM 
on line 5.

The best I could do on the spot was create a condition that can never be 
true (1 = 2), but I think this is pretty lame...:-)

This is Fujitsu NetCOBOL but I'd be interested in seeing any solutions 
anyone has.

PERFORM FOREVER   would be cool...

Pete.
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-07T11:59:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o6or0F4hun9U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <3o69h8F4ffv9U1@individual.net>`

```
 

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:3o69h8F4ffv9U1@individual.net...
>
> If only the following were possible!:
…[13 more quoted lines elided]…
>               end-perform

Yes, having get-input as an inline function would be kinda nice :-). I 
believe there is something on this in the new standard but Chuck would be in 
a better position to comment.

  Unfortunately at the time this code is entered, itsa-tag is true, so it is 
necessary to do another get-input, otherwise the stringing will never be 
performed. (You were not to know that and I have posted clarification back 
up the thread in response to Richard.)

>
> Yes, I learned C before I learned COBOL.
…[5 more quoted lines elided]…
>
Well, it does answer my request for ideas and any favourite ways of doing 
this. I wasn't looking for a coded solution to my problem (I don't expect 
people to write code for me unless I am way out of my depth and need an 
example...that is not the case here :-)) It has been interesting to see the 
various responses and it gave me a wakeup about 88 levels that I had almost 
forgotten...

Pete.
```

###### ↳ ↳ ↳ Re: Perform forever

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2005-09-07T11:54:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o8nqjF4f0a1U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <3o69h8F4ffv9U1@individual.net> <3o6or0F4hun9U1@individual.net>`

```
It's been a while since I've done C programming, but I wonder if this would
be how you might do it:

while (!(in_len = getinput(&input, &itsatag)))
    if (!itsatag)
        string(&wppauthorblurb, &input, in_len);


The function getinput() would read in 'input', set itsatag to 0 or 1
depending on if input is or is not a tag, and it would return the length of
the input.  If the length of the input was zero then the while loop would
exit.  If the length of the input was not zero then it would check to see if
itsatag is 'true' or 'false', and if it's false it would perform the string
function, passing &wppauthorblurb, &input, and in_len.

Or something like that.  So in COBOL with user-defined functions perhaps it
would look like

    perform until get-input(wpppauthorblurb, input, input-len, itsatag-sw)
is equal to zero
          if not itsatag
               string
                      wpppauthorblurb
                         delimited by low-values
                      INPUT-RECORD (1:INPUT-LEN)
                         delimited by size
                      '<br> '
                         delimited by size
                            into
                              wpppauthorblurb
                 end-string
         end-if
   end-perform

In C you can both assign a value to what the function returns and compare
what the function returns to another value, all at the same time.  It's
quite useful, in my opinion.  I don't see how you can do that with even
COBOL 2002, so I had to pass input-len as a parameter.

Still not sure if it's quite what you are looking for, but hey.

Frank


--- 
Frank Swarbrick
Senior Developer/Analyst - Mainframe Applications
FirstBank Data Corporation - Lakewood, CO  USA

>>> Pete Dashwood<dashwood@enternet.co.nz> 9/6/2005 5:59:22 PM >>>
 

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:3o69h8F4ffv9U1@individual.net...
>
> If only the following were possible!:
…[13 more quoted lines elided]…
>               end-perform

Yes, having get-input as an inline function would be kinda nice :-). I 
believe there is something on this in the new standard but Chuck would be in

a better position to comment.

  Unfortunately at the time this code is entered, itsa-tag is true, so it is

necessary to do another get-input, otherwise the stringing will never be 
performed. (You were not to know that and I have posted clarification back 
up the thread in response to Richard.)

>
> Yes, I learned C before I learned COBOL.
…[5 more quoted lines elided]…
>
Well, it does answer my request for ideas and any favourite ways of doing 
this. I wasn't looking for a coded solution to my problem (I don't expect 
people to write code for me unless I am way out of my depth and need an 
example...that is not the case here :-)) It has been interesting to see the

various responses and it gave me a wakeup about 88 levels that I had almost

forgotten...

Pete.
```

#### ↳ Re: Perform forever

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-09-06T19:04:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6f1a$431e2e99$45491c57$22316@KNOLOGY.NET>`
- **In-Reply-To:** `<3o4gk2F44vdgU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
Pete Dashwood wrote:
>  
> Does anyone have a favourite way of specifying that a PERFORM should 
> continue indefinitely?

See this newsgroup, about a year ago...  :)  Is your memory that bad?  ;)

>                perform until 1 = 2
> 
> The best I could do on the spot was create a condition that can never be 
> true (1 = 2), but I think this is pretty lame...:-)

I would create an 88-level, and never change it.  Make it something like...

*>  If I find anyone changing the value of this variable,
*>  you'd better be able to run faster than me...
01  hfoSwitch       pic X(01) value space.
     88  hellFreezesOver       value "X".
     88  explicitlyToldToExit  value "X".

...Then...

perform until hellFreezesOver
     ....
end-perform

Or, if you wanted to make it clearer...

perform until explicityToldToExit
     ....
end-perform

I'm just jealous that you have "Exit Perform".  :)
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-07T13:24:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o6tr9F4g14oU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <a6f1a$431e2e99$45491c57$22316@KNOLOGY.NET>`

```
 

"LX-i" <lxi0007@netscape.net> wrote in message 
news:a6f1a$431e2e99$45491c57$22316@KNOLOGY.NET...
> Pete Dashwood wrote:
>>  Does anyone have a favourite way of specifying that a PERFORM should 
…[3 more quoted lines elided]…
>

Harrumph! Cheeky young whippersnapper...!

Let's just say that, given the VAST store of information in my head, as age 
encroaches my memory is becoming more 'selective'... :-)

>>                perform until 1 = 2
>>
…[5 more quoted lines elided]…
>

Yes, so would I :-) That is what I've done. I just had a mental block on how 
to use an 88 level for this purpose... Slipped a gear. I'm OK now... (runs 
hot bath and wonders when meals on wheels will arrive and nurse will change 
his poultice...)

> *>  If I find anyone changing the value of this variable,
> *>  you'd better be able to run faster than me...
…[17 more quoted lines elided]…
>
Ah, that's life here at the cutting edge ... :-)

Pete.
```

#### ↳ Re: Perform forever

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-09-06T20:26:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e37f$431e41c3$45491c57$3110@KNOLOGY.NET>`
- **In-Reply-To:** `<3o4gk2F44vdgU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
Pete Dashwood wrote:
>                  string
>                       wpppauthorblurb
…[7 more quoted lines elided]…
>                  end-string

Just a note - you could make that say '<br />' instead, and it would be 
ready for XHTML compliance.  :)
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-07T13:29:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o6u40F42l8rU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <9e37f$431e41c3$45491c57$3110@KNOLOGY.NET>`

```
 
Thanks Daniel, I'll do that.

Pete.

"LX-i" <lxi0007@netscape.net> wrote in message 
news:9e37f$431e41c3$45491c57$3110@KNOLOGY.NET...
> Pete Dashwood wrote:
>>                  string
…[24 more quoted lines elided]…
>
```

#### ↳ Re: Perform forever

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-09-07T00:06:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net>`

```
Well, you really don't mean it should continue indefinitely.  You 
clearly state that you want it to stop with (itsa-tag OR finished).  
That is a totally reasonable exit condition.

So why not:


   move low-values to wpppauthorblurb
   perform get-input
   perform until (itsa-tag or finished)
      string
          wpppauthorblurb
             delimited by low-values
          INPUT-RECORD (1:INPUT-LEN)
             delimited by size
          '<br> '
             delimited by size
          into
             wpppauthorblurb
      end-string
      perform get-input
   end-perform

This has the benefit of letting the compiler know when you want to exit 
in a well-defined and easy to parse manner.  And it looks clean and nice.

They way you have it coded, the compiler writer needs to make his/her 
"IF" production aware of its nesting within a "PERFORM" production.  
Adds a ton of complexity that usually isn't worth the trouble.

In article <3o4gk2F44vdgU1@individual.net>,
 "Pete Dashwood" <dashwood@enternet.co.nz> wrote:
> Does anyone have a favourite way of specifying that a PERFORM should 
> continue indefinitely?
…[32 more quoted lines elided]…
> Pete.
```

##### ↳ ↳ Re: Perform forever

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-07T21:45:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o7s0mF48ukqU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com>`

```
 
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
news:joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com...
>
> Well, you really don't mean it should continue indefinitely.  You
> clearly state that you want it to stop with (itsa-tag OR finished).
> That is a totally reasonable exit condition.

I see what you're saying, but actually I DO want the controlling PERFORM to 
keep going indefinitely. There are other exit conditions that the code does 
not currently cater for; like output buffer overflow, for example. I'll add 
them once what I have is working. I like to 'evolve' code, rather than just 
write it...

It just so happens that I will exit from on it on the stated conditions. 
(The conditions could change, and there could be other instances where I 
need an indefinite PERFORM that will work until some event occurs, for 
example...)


> So why not:
>
…[16 more quoted lines elided]…
>
Yes, that is nice clean code and I would have no real objection to it. 
However, it requires two calls to the get-input routine and I prefer that 
code does not have two calls where one will do. (It's just an old habit and 
a personal preference; there is nothing wrong with your code.) I also like 
to see the checking of what happened in a subroutine, immediately following 
the return from the subroutine. For me, the second 'get-input' is hanging 
because the checking of what happened has been moved to the main PERFORM 
loop. I don't think this is 'wrong'; it just isn't my preference.

> This has the benefit of letting the compiler know when you want to exit
> in a well-defined and easy to parse manner.  And it looks clean and nice.
>
How is helping the compiler a consideration here? I don't care what the 
compiler makes of it as long as the object code is correct... :-)

My solution will not be difficult to compile anyway.

> They way you have it coded, the compiler writer needs to make his/her
> "IF" production aware of its nesting within a "PERFORM" production.
> Adds a ton of complexity that usually isn't worth the trouble.

 Not a consideration. The compiler has already been written and deals with 
what I'm asking of it perfectly well. As an ex-compiler writer/maintainer 
myself, I don't agree with you about it adding a ton of complexity, 
anyway...
>

I still like your example, and thanks for posting it. It is very interestng 
to see the different considerations people have when coding COBOL. Here's my 
final code (until I find in testing I have to change it... :-)):

               move low-values to wpppauthorblurb
               perform until forever
                    perform get-input
                    if itsa-tag OR finished
                       exit perform
                    end-if
                    string
                         wpppauthorblurb
                             delimited by low-values
                         INPUT-RECORD (1:INPUT-LEN)
                             delimited by size
                         '<br> / '
                             delimited by size
                         into
                              wpppauthorblurb
                     end-string
               end-perform

Pete.
```

###### ↳ ↳ ↳ Re: Perform forever

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-07T12:39:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NbBTe.7438$4i6.771@tornado.tampabay.rr.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com> <3o7s0mF48ukqU1@individual.net>`

```

"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3o7s0mF48ukqU1@individual.net...
>
> "Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote in message 
…[7 more quoted lines elided]…
> to keep going indefinitely.

Except when you EXIT it, no doubt.

> There are other exit conditions that the code does not currently cater 
> for; like output buffer overflow, for example. I'll add them once what I 
…[5 more quoted lines elided]…
> example...)

I *never* understood the need for a do forever, nothing is done forever.
So it's like life?

I think I'm going to live forever until some other sudden event comes along 
and runs me over - but I'm not sure where that will happen.

JCE
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-08T04:23:32+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o8ig9F4oo2kU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com> <3o7s0mF48ukqU1@individual.net> <NbBTe.7438$4i6.771@tornado.tampabay.rr.com>`

```
 

"jce" <defaultuser@hotmail.com> wrote in message 
news:NbBTe.7438$4i6.771@tornado.tampabay.rr.com...
>
>
…[13 more quoted lines elided]…
> Except when you EXIT it, no doubt.

No, I explained that below. When I exit it I don't care whether it keeps 
running or not...(The fact is that the nature of the hardware it is running 
on, is such that it will stop running once it is exited, but supposing it 
wasn't? From my point of view whatever happens to it after I exit it is 
irrelevant...until the next time I need to use it...)

I would agree that it is a fine and philosophical point, rather than a 
computer programming practice.

>
>> There are other exit conditions that the code does not currently cater 
…[10 more quoted lines elided]…
>

Consider a 'default' process. You want it to proceed until some event 
occurs, but that event may never occur. Or other events which require 
varying responses may occur, and some of these may require exiting the 
process and some of them may not.. This is the major difference between 
interrupt driven programming and the normal sequential processing we do with 
procedural code. (In the case in point, it is a sequential procedural 
process and it really doesn't matter whether the PERFORM keeps its control 
forever or until it is exited; but there might be other occasions when it 
DOES matter, in other programs.)

> I think I'm going to live forever until some other sudden event comes 
> along and runs me over - but I'm not sure where that will happen.
>

And probably just as well... (Not that it will happen, but that you don't 
know when...:-).

It's not quite the same. Although we don't know when, we do know with 
certainty that our lives must end. That is not necessarily the case with the 
PERFORM.

That is the nub of what I'm trying to convey. I don't know how long the 
PERFORM needs to run, so I can't know when it should be terminated. (In this 
instance it will depend on how many lines there are following the %8 tag, 
and that will vary as different tag sets are processed...) So, the approach 
is to run it forever and quit when you've had enough.

Pete.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 5)_

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2005-09-08T03:42:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5rOTe.28744$xl6.14803@tornado.tampabay.rr.com>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com> <3o7s0mF48ukqU1@individual.net> <NbBTe.7438$4i6.771@tornado.tampabay.rr.com> <3o8ig9F4oo2kU1@individual.net>`

```
"Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
news:3o8ig9F4oo2kU1@individual.net...
> "jce" <defaultuser@hotmail.com> wrote in message 
> news:NbBTe.7438$4i6.771@tornado.tampabay.rr.com...
…[19 more quoted lines elided]…
> exit it is irrelevant...until the next time I need to use it...)

In your example, after you EXIT, it's no longer the controlling  PERFORM so 
it's not "running" or am I missing something?  Sure you can enter the loop 
again....

> I would agree that it is a fine and philosophical point, rather than a 
> computer programming practice.

I don't pretend to understand it, but it doesn't bother me so much that I 
care to argue.
I've made comments, asked questions and even made a quatement (that's a 
statement I'm not confident in) :-)  I'm always interested in the way 
different people see different problems (well solutions I should say).

>>> There are other exit conditions that the code does not currently cater 
>>> for; like output buffer overflow, for example. I'll add them once what I 
…[10 more quoted lines elided]…
> occurs, but that event may never occur.

That statement there is still not a do forever... it's a do until event 
....the event not occurring is happenstance unless the event is impossible 
(1=2) - which as we know is not true for sufficiently large quantities of 1.

> Or other events which require varying responses may occur, and some of 
> these may require exiting the process and some of them may not.. This is 
…[4 more quoted lines elided]…
> might be other occasions when it DOES matter, in other programs.)

I was under the impression that "infinite loops" use "polling" and that part 
of the charm of "interrupts" is that they get rid of the wasted loop.
I can understand in code like Entropy polling or Service rendering...but 
they nearly _always_ have a shutdown mechanism....even my USB hardware wants 
to be removed properly!

>> I think I'm going to live forever until some other sudden event comes 
>> along and runs me over - but I'm not sure where that will happen.
…[11 more quoted lines elided]…
> approach is to run it forever and quit when you've had enough.

Well actually, by your definition it will end after a certain number of 
lines following the %8 tag...and you cannot run forever AND quit
That's almost as daft as the ending of Highlander :-)

JCE
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-09T01:35:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3oat1pF54vusU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com> <3o7s0mF48ukqU1@individual.net> <NbBTe.7438$4i6.771@tornado.tampabay.rr.com> <3o8ig9F4oo2kU1@individual.net> <5rOTe.28744$xl6.14803@tornado.tampabay.rr.com>`

```
 
"Upon mine honour, I have done my best."

It is a difficult and tenuous concept to explain why I consider FOREVER 
necessary.

The fact is that I do, and like you stated, I don't care to argue it 
further. :-)

(And it isn't really important; it's only computer programming...)

Pete.

"jce" <defaultuser@hotmail.com> wrote in message 
news:5rOTe.28744$xl6.14803@tornado.tampabay.rr.com...
>
> "Pete Dashwood" <dashwood@enternet.co.nz> wrote in message 
…[92 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Perform forever

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2005-09-07T13:33:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dfmq78$9j2$1@peabody.colorado.edu>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com> <3o7s0mF48ukqU1@individual.net>`

```

On  7-Sep-2005, "Pete Dashwood" <dashwood@enternet.co.nz> wrote:

> > Well, you really don't mean it should continue indefinitely.  You
> > clearly state that you want it to stop with (itsa-tag OR finished).
…[11 more quoted lines elided]…
> example...)

That's not forever.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-08T04:25:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o8ij8F4osf3U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com> <3o7s0mF48ukqU1@individual.net> <dfmq78$9j2$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:dfmq78$9j2$1@peabody.colorado.edu...
>
>
…[22 more quoted lines elided]…
>
It is if the events never occur. See my response to JCE.

Pete.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2005-09-12T07:54:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dg41bb$3qg$1@peabody.colorado.edu>`
- **In-Reply-To:** `<3o8ij8F4osf3U1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com> <3o7s0mF48ukqU1@individual.net> <dfmq78$9j2$1@peabody.colorado.edu> <3o8ij8F4osf3U1@individual.net>`

```
Pete Dashwood wrote:
>  

>>>It just so happens that I will exit from on it on the stated conditions.
>>>(The conditions could change, and there could be other instances where I
…[8 more quoted lines elided]…
> Pete. 


It's not even a billion years, which is nothing compared to forever. 
You program for events which allow it to terminate the way you want. 
It doesn't matter when those events occur (if ever), you program for them.
```

###### ↳ ↳ ↳ Re: Perform forever

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-09-13T14:35:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3oms8dF6p7hfU1@individual.net>`
- **References:** `<3o4gk2F44vdgU1@individual.net> <joe_zitzelberger-A059E5.00063607092005@ispnews.usenetserver.com> <3o7s0mF48ukqU1@individual.net> <dfmq78$9j2$1@peabody.colorado.edu> <3o8ij8F4osf3U1@individual.net> <dg41bb$3qg$1@peabody.colorado.edu>`

```
 

"Howard Brazee" <howard@brazee.net> wrote in message 
news:dg41bb$3qg$1@peabody.colorado.edu...
> Pete Dashwood wrote:
>>
…[17 more quoted lines elided]…
>
Did I at any point suggest NOT programming for them?

The issue here is whether the PERFORM continues forever...

My argument is that it can, I just don't care... Some events may require it 
to terminate, others may not, some events may never occur, others may always 
occur. Interrupt driven programming requires events to be 'handled'. As long 
as they are, it makes no difference whether the controlling loop (or poller, 
or interrupt handler, or scheduler, or whatever) terminates or doesn't.

And 'forever', in this context, is 'as long as the machine is running this 
process' so a billion years is not relevant (we could reasonably expect the 
machine to be dust and the power supply to be exhausted by then, assuming 
that there hasn't been a BSOD or other OS abend...)

A subtle and diffcult to explain difference in concept here. It isn't worth 
arguing, so this is my last on it... I don't think you're wrong; I just see 
it slightly differently...

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
