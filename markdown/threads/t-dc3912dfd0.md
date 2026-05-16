[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Alternative COBOL "telco" source program

_46 messages · 14 participants · 2004-05 → 2004-06_

---

### Re: Alternative COBOL "telco" source program

- **From:** robin <robin_v@bigpond.mapson.com>
- **Date:** 2004-05-27T03:23:20+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au>`

```
From: "Michael Mattias" <michael.mattias@gte.net>, SBC http://yahoo.sbc.com
Date: Wed, 26 May 2004 12:09:48 GMT
.
| Some of these "can'ts" are so incredibly banal...
.
They all are.
.
| e.g., # 18 "CANT find last
| word index in trailing blank text using a loop   <= 3 statements."
.
Not only can this be done in PL/I,
it can be done by a beginner.
Furthermore, it can be done in PL/I in one statement.
.
| --
| Michael Mattias
```

#### ↳ Re: Alternative COBOL "telco" source program

- **From:** Tim Challenger <"timothy(dot)challenger(at)apk(dot)at">
- **Date:** 2004-05-27T07:57:52+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<53d19407aa879851e2b9806445347a89@news.teranews.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au>`

```
On Thu, 27 May 2004 03:23:20 GMT, robin wrote:

> From: "Michael Mattias" <michael.mattias@gte.net>, SBC http://yahoo.sbc.com
> Date: Wed, 26 May 2004 12:09:48 GMT
…[10 more quoted lines elided]…
> Furthermore, it can be done in PL/I in one statement.

We all know that DF's knowledge of PLI and imagination are lacking.

Here the code to demonstrate a 1 statement solution, a 3 statement loop and
a 2 statement loop. So Mr Frank if you're listening, take down #18.

It's complete except for Proc and end statements.
Compiler: VisualAge(TM) PL/I for Windows(R)  V2.R1.08


   dcl s char(80)
         init("The quick brown fox jumps over the lazy dog's back.");
   dcl i fixed bin(31) init(0);

   put edit(' one statement:')(skip, A);
   i = searchr(trim(s), ' ');
   put edit(substr(s, 1, i), substr(s, i+1))(skip, A);



   put edit(' 3 statement loop:')(skip(2), A);
   do i = length(trim(s))-1 to 1 by -1;
      if substr(s, i, 1) = ' ' then leave;
   end;
   put edit(substr(s, 1, i), substr(s, i+1))(skip, A);



   put edit(' 2 statement loop:')(skip(2), A);
   do i = length(trim(s))-1 to 1 by -1 while(substr(s, i, 1) ^= ' ');
   end;
   put edit(substr(s, 1, i), substr(s, i+1))(skip, A);




 Outputs:
 one statement:
The quick brown fox jumps over the lazy dog's 
back. 
                            
 3 statement loop:
The quick brown fox jumps over the lazy dog's 
back. 
                            
 2 statement loop:
The quick brown fox jumps over the lazy dog's 
back. 


***
If your compiler doesn't have SEARCHR it can be replaced by this:
   i = index(reverse(trim(s)), ' ');
   i = length(trim(s)) -i +1;

Which can easily be combined to 1 (somewhat untidy) statement:
i = length(trim(s)) - index(reverse(trim(s)), ' ') +1;


So Mr. Frank, any of these satisfy your "challenge"? Or are you going to
move the goalposts yet again?
```

##### ↳ ↳ Re: Alternative COBOL "telco" source program

- **From:** "David Frank" <dave_frank@hotmail.com>
- **Date:** 2004-05-27T12:11:38+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<_Vktc.25091$0X2.819447@twister.tampabay.rr.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <53d19407aa879851e2b9806445347a89@news.teranews.com>`

```

"Tim Challenger" <"timothy(dot)challenger(at)apk(dot)at"> wrote in message 
news:53d19407aa879851e2b9806445347a89@news.teranews.com...
> On Thu, 27 May 2004 03:23:20 GMT, robin wrote:
>
…[79 more quoted lines elided]…
>

Its interesting you recognize Robin's blather as just that, blather, and 
have
searched for cants you CAN tackle.

Congrats for providing loop solution(s) for #18, I will remove it from my
PLI_CANT.FAQ

BTW, why havent you tackled the TELCO benchmark challenge,
Robin says PL/I can do it in 43 lines but refuses to prove it.
```

#### ↳ Re: Alternative COBOL "telco" source program

- **From:** lruss@superlink.net (L Russ)
- **Date:** 2004-05-27T12:51:39-07:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<cfaeadf3.0405271151.20c59a4@posting.google.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au>`

```
robin <robin_v@bigpond.mapson.com> wrote in message news:<Iadtc.12799$L.1063@news-server.bigpond.net.au>...
> From: "Michael Mattias" <michael.mattias@gte.net>, SBC http://yahoo.sbc.com
> Date: Wed, 26 May 2004 12:09:48 GMT
…[3 more quoted lines elided]…
> They all are.

They are all worse, much worse, than banal.

> .
> | e.g., # 18 "CANT find last
…[4 more quoted lines elided]…
> Furthermore, it can be done in PL/I in one statement.

But if you do it in one statement, then it's not in a loop, and CAN'T
18 clearly states that you should use a loop, with at most 3
statements, implying that using a loop (with three statements or less)
is really the important thing when you do this task.  Even if the
language you use doesn't require that you do it that way.

Here's my version using C++, no loop. Another FORTRAN CAN'T.  Big
deal.
And yes, string and iostream are part of the C++ standard, so it's not
like anyone can't duplicate this code if you've got a conformant
compiler.

#include <string>
#include <iostream>
int main() {
 const std::string s = "The quick brown fox jumps over the lazy dog's
back.   ";
 std::cout << s.substr(0, s.find_last_not_of(" ")+1) << std::endl;
 return 0;
}

And I expect, as you've said, that PL/I offers something similar.

Anyone care to try this in SNOBOL?


LR
```

##### ↳ ↳ Re: Alternative COBOL "telco" source program

- **From:** Tim Challenger <"timothy(dot)challenger(at)apk(dot)at">
- **Date:** 2004-05-28T06:21:16+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<b762c08c946cd49e72a90526d05bb688@news.teranews.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com>`

```
On 27 May 2004 12:51:39 -0700, L Russ wrote:

> And I expect, as you've said, that PL/I offers something similar.
You probably saw my version of 1 stmt, a 2 stmt loop and a 2 stmt loop.

 
> Anyone care to try this in SNOBOL?
Blimey, is that still around? Used it once in 1981 and also SPITBOL, a
derivative. 
```

##### ↳ ↳ Re: Alternative COBOL "telco" source program

- **From:** "David Frank" <dave_frank@hotmail.com>
- **Date:** 2004-05-28T08:42:43+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<7YCtc.32762$Ol3.8747@twister.tampabay.rr.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com>`

```

"L Russ" <lruss@superlink.net> wrote in message 
news:cfaeadf3.0405271151.20c59a4@posting.google.com...
> robin <robin_v@bigpond.mapson.com> wrote in message 
> news:<Iadtc.12799$L.1063@news-server.bigpond.net.au>...
…[25 more quoted lines elided]…
> deal.

Wanna bet?

> And yes, string and iostream are part of the C++ standard, so it's not
> like anyone can't duplicate this code if you've got a conformant
…[10 more quoted lines elided]…
>

IMO, horrific syntax, but thats nothing new for C++  statements is it?
and its sure not apparent to me that above outputs 2 lines, does it?
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

- **From:** lruss@superlink.net (L Russ)
- **Date:** 2004-05-29T20:01:56-07:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<cfaeadf3.0405291901.250f89e@posting.google.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <7YCtc.32762$Ol3.8747@twister.tampabay.rr.com>`

```
"David Frank" <dave_frank@hotmail.com> wrote in message news:<7YCtc.32762$Ol3.8747@twister.tampabay.rr.com>...
> "L Russ" <lruss@superlink.net> wrote in message 
> news:cfaeadf3.0405271151.20c59a4@posting.google.com...
…[29 more quoted lines elided]…
> Wanna bet?
Don't be silly.


> 
> > And yes, string and iostream are part of the C++ standard, so it's not
…[13 more quoted lines elided]…
> IMO, horrific syntax, but thats nothing new for C++  statements is it?

It's actually quite beautiful.


> and its sure not apparent to me that above outputs 2 lines, does it?

No. You're right.  I made a mistake when I wrote that code.
Here is the corrected version, which I believe outputs exactly what
your code does, including the trailing blanks which result from
FORTRAN's fixed length strings.  It's a little difficult to format
things when I post.  Google is unfriendly to long lines and tabs.

#include <string>
#include <iostream>
int main() {
const int lengthOfDavidFranksFortranString = 80;
const std::string s1 = "The quick brown fox jumps over the lazy dog's
back.";
const std::string s = s1 +
               std::string(lengthOfDavidFranksFortranString-s1.length(),'
');
const std::string::size_type lastNonBlank = s.find_last_not_of(" ");
const std::string::size_type lastWordIndex =
                                 
s.substr(0,lastNonBlank).find_last_of(" ");
std::cout << s.substr(0, lastWordIndex+1) << "\n" <<
                                      s.substr(lastWordIndex+1) <<
std::endl;
	return 0;
}

Does FORTRAN have support for a varying length string? I mean other
than that thing that allows functions to be called with different
length strings, which isn't the same thing.  Wrong group to ask in?

BTW, you might find this link of interest.  Someone who has some bad
things to say about C++ and OOP, and some interesting things to say
about software development in general.  Can't say that I'm totally
convinced by all of it, but some thought provoking stuff.
http://www.leshatton.org/index.html

LR
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 4)_

- **From:** "David Frank" <dave_frank@hotmail.com>
- **Date:** 2004-05-30T06:56:29+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<xAfuc.14819$w34.664709@twister.tampabay.rr.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <7YCtc.32762$Ol3.8747@twister.tampabay.rr.com> <cfaeadf3.0405291901.250f89e@posting.google.com>`

```

"L Russ" <lruss@superlink.net> wrote in message 
news:cfaeadf3.0405291901.250f89e@posting.google.com...
> "David Frank" <dave_frank@hotmail.com> wrote in message 
> news:<7YCtc.32762$Ol3.8747@twister.tampabay.rr.com>...
…[45 more quoted lines elided]…
>

I'm not sure its even part of the new F2003 standard, there is a 
user-developed
varying length string module avail. that provides support.
I personally think using c-strings is all thats really needed if strings 
must be
manipulated while holding on to trailing blanks and have my own simple 
little
varying string module using c-strings that met challenges presented to 
translate
various PL/I varying  string examples several years back..

> BTW, you might find this link of interest.  Someone who has some bad
> things to say about C++ and OOP, and some interesting things to say
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Alternative COBOL "telco" source program

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-05-28T11:26:32+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<IlFtc.22734$sQ2.1475@newssvr31.news.prodigy.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com>`

```
"L Russ" <lruss@superlink.net> wrote in message
news:cfaeadf3.0405271151.20c59a4@posting.google.com...
> robin <robin_v@bigpond.mapson.com> wrote in message
news:<Iadtc.12799$L.1063@news-server.bigpond.net.au>...
> > From: "Michael Mattias" <michael.mattias@gte.net>, SBC
http://yahoo.sbc.com
> > Date: Wed, 26 May 2004 12:09:48 GMT
> > .
> > | e.g., # 18 "CANT find last
> > | word index in trailing blank text using a loop   <= 3 statements."

> But if you do it in one statement, then it's not in a loop, and CAN'T
> 18 clearly states that you should use a loop, with at most 3
> statements, implying that using a loop (with three statements or less)
> is really the important thing when you do this task.  Even if the
> language you use doesn't require that you do it that way.

Using PowerBASIC compiler you'd do it without  loop:

sentence$ = "The quick brown fox jumps over the lazy dog's  back.   "
nWord = PARSECOUNT (RTRIM$(sentence$, ANY CHR$(32)))
LastWord$ = RTRIM$(PARSE$(Sentence$, ANY CHR$(32), nWord)

Of course, you could make it into a three-sentence loop:

FOR Z = 1 TO 1
sentence$ = "The quick brown fox jumps over the lazy dog's  back.   "
nWord = PARSECOUNT (RTRIM$(sentence$, ANY CHR$(32)))
LastWord$ = RTRIM$(PARSE$(Sentence$, ANY CHR$(32), nWord)
NEXT Z


MCM
```

##### ↳ ↳ Re: Alternative COBOL "telco" source program

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-28T21:41:32-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bfu1iimqi3te9@corp.supernews.com>`
- **In-Reply-To:** `<cfaeadf3.0405271151.20c59a4@posting.google.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com>`

```
L Russ wrote:

> Here's my version using C++, no loop. Another FORTRAN CAN'T.  Big
> deal.
…[15 more quoted lines elided]…
> Anyone care to try this in SNOBOL?

Here's a COBOL version.  (Comments on newsreader-induced wrapping follow 
- it was compiled using Fujistu v3, using compiler options "MAIN" and 
"SRF(FREE,FREE)".  "*>" marks a comment.)

identification division.
   program-id.  numberEighteen.
data division.
   working-storage section.
*> Note - COBOL space-pads, so this string has lots of spaces at the end
77  textString  pic X(80) value "The quick brown fox jumps over the lazy 
dog's back.".
77  spaceLength pic 9(02) value zero.
procedure division.
doIt.
*>   Two statements, no loop
inspect function reverse (textString) tallying spaceLength for leading space
display "[" textString (1:80 - spaceLength) "]"
*>   Three statements in a loop
perform varying spaceLength from 80 by -1 until textString 
(spaceLength:1) not = space
    continue
end-perform
display "[" textString(1:spaceLength) "]"
*>   All done
stop run.

OK - it looks like the definition for "textString" wrapped, along with 
the line with the "inspect" statement and the "perform" statements. 
Bring the lines under them up (if they're wrapped in your reader) and 
you should be able to run it just fine.

(In theory, the loop could work as a one-liner too - just bring the 
"continue" and the "end-perform" up on the same line as the perform, and 
make sure they're separated by at least one space.)

Output from the above...

[The quick brown fox jumps over the lazy dog's back.]
[The quick brown fox jumps over the lazy dog's back.]


(That'll be $200 USD...  ;>  )
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

- **From:** "David Frank" <dave_frank@hotmail.com>
- **Date:** 2004-05-29T05:30:42+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<6eVtc.34937$Ol3.23233@twister.tampabay.rr.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:10bfu1iimqi3te9@corp.supernews.com...
>L Russ wrote:
>
…[63 more quoted lines elided]…
>

Not so fast, the objective is to find the index of the last word
and as my challenge at  http://home.cfl.rr.com/davegemini/pli_cant.faq
clearly shows, the subsequent output breaks the output into
2 lines...
The quick brown fox jumps over the lazy dog's
back.
```

###### ↳ ↳ ↳ How to "write a spec" (was: Alternative COBOL "telco" source program

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-29T06:09:53+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<ROVtc.14585$Tn6.1831@newsread1.news.pas.earthlink.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com>`

```
"David Frank" <dave_frank@hotmail.com> wrote in message
news:6eVtc.34937$Ol3.23233@twister.tampabay.rr.com...
>
<snip>
> Not so fast, the objective is to find the index of the last word
> and as my challenge at  http://home.cfl.rr.com/davegemini/pli_cant.faq
…[5 more quoted lines elided]…
>

Just in case anyone missed it ...

Compare the following from
  http://home.cfl.rr.com/davegemini/pli_cant.faq

with what is written above,

"18. CAN find last word index in trailing blank text using a loop"

Notice it does NOT say anything about "output" - much less two lines of output.
The

   SPECIFICATION

was for a way to find "the last word  ... using a loop"

The COBOL code (snipped from this post) did EXACTLY that.

Apparently, what Mr. Frank thinks is a "specification" is:
  - brief (incomplete)  summary
 - code in another language
 - sample output

It appears, that the ACTUAL specification that he *meant* to say (and talk about
USELESS facility) is:

Given an internal program "literal"  (exactly 80 bytes long) of
   "The quick brown fox jumps over the lazy dog's back.   "
Then, find the last word (defined by spaces before and after it) and you MUST
use a programming construct of a "loop"
Then output all of the text before the word on one line - and the final "word"
on a separate line.

If that is actually what he wants, then he should say so ...
  If he wants something else, then he should learn how to write an application
specification!

Once he actually modifies his specification to say what he wants, I am certain
that it will take about two minutes to code it in COBOL (or any other
programming language - that has a loop construct).
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-29T14:12:23-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bho1htfsbdr8c@corp.supernews.com>`
- **In-Reply-To:** `<6eVtc.34937$Ol3.23233@twister.tampabay.rr.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com>`

```
David Frank wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message 
> news:10bfu1iimqi3te9@corp.supernews.com...
…[33 more quoted lines elided]…
> back. 

I missed that - update pending...
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-29T17:57:47-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bi5879obpdo49@corp.supernews.com>`
- **In-Reply-To:** `<6eVtc.34937$Ol3.23233@twister.tampabay.rr.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com>`

```
David Frank wrote:
> Not so fast, the objective is to find the index of the last word
> and as my challenge at  http://home.cfl.rr.com/davegemini/pli_cant.faq
…[3 more quoted lines elided]…
> back. 

I missed that.  Here's the corrected version.  The three lines start 
with "inspect", "perform", and "display", so however it wraps, that's 
how it looks on my PC.

-=-=-=-=-

identification division.
   program-id.  numberEighteen.
data division.
   working-storage section.
*> Note - COBOL space-pads, so this string has lots of spaces at the end
77  textString  pic X(80) value "The quick brown fox jumps over the lazy 
dog's back.".
77  spaceLength pic 9(02) value zero.
77  spaceIdx    pic 9(02) value zero.
77  lastWordIdx pic 9(02) value zero.
procedure division.
doIt.
*>   Three lines including a loop
inspect function reverse (textString) tallying spaceLength for leading 
space  compute spaceIdx = 80 - spaceLength
perform varying lastWordIdx from spaceIdx by -1 until textString 
(lastWordIdx:1) = space continue end-perform
display textString(1:lastWordIdx) function char(14) function char (11) 
textString (lastWordIdx + 1:79 - lastWordIdx)
*>   All done
stop run.

-=-=-=-=-

That's not the only way to do it...  that display especially could be 
made shorter by defining a symbolic character or 2 in the configuration 
section.  That version looks like this...

-=-=-=-=-

identification division.
   program-id.  numberEighteen.
environment division.
   configuration section.
     special-names.  symbolic characters  asciiCR is 14  asciiLF is 11.
data division.
   working-storage section.
*> Note - COBOL space-pads, so this string has lots of spaces at the end
77  textString  pic X(80) value "The quick brown fox jumps over the lazy 
dog's back.".
77  spaceLength pic 9(02) value zero.
77  spaceIdx    pic 9(02) value zero.
77  lastWordIdx pic 9(02) value zero.
01  asciiCRLF.
     04  pic X value asciiCR.
     04  pic X value asciiLF.
procedure division.
doIt.
*>   Three lines including a loop
inspect function reverse (textString) tallying spaceLength for leading 
space  compute spaceIdx = 80 - spaceLength
perform varying lastWordIdx from spaceIdx by -1 until textString 
(lastWordIdx:1) = space continue end-perform
display textString(1:lastWordIdx)  asciiCRLF  textString (lastWordIdx + 
1:79 - lastWordIdx)
*>   All done
stop run.

-=-=-=-=-

That's one of the things I like about COBOL - there's always more than 
one way to do things.  You can be elegant and use all the features, but 
even the most basic features provide a way to do it, although the code 
is much longer.  Here's a version doing it the way a lot of the code I 
maintain is written (that code is over 20 years old, in some cases).

-=-=-=-=-

        identification division.
          program-id.  numberEighteen.
        environment division.
          configuration section.
           special-names.
             symbolic characters asciiCR is 14  asciiLF is 11.
        data division.
          working-storage section.
        77  lastWordIdx pic 9(02) value zero.
       *> Note - COBOL space-pads, so this string has lots of spaces at 
the end
        01  textString                    pic X(80) value
                "The quick brown fox jumps over the lazy dog's back.".
        01  textStringTbl            redefines textString.
            12  textStringElt        occurs 80 times
                                       indexed by textStringIdx
                                          pic X.
        01  outputLine                    pic X(80).
        01  outputLineTbl            redefines outputLine.
            12  outputLineElt        occurs 80 times
                                       indexed by outputLineIdx
                                          pic X.
        01  foundIdxSw                    pic X value "N".
            88  foundText                   value "T".
            88  foundIdx                    value "Y".
        procedure division.
        doIt.
       *>    "Verbose" way using COBOL 74-compliant code
            perform findTheIdx varying textStringIdx from 80 by -1
              until foundIdx.
            set  lastWordIdx   to textStringIdx.
            set  textStringIdx to 1.
            move spaces        to outputLine.
            perform moveTheText varying outputLineIdx from 1 by 1
              until textStringIdx > lastWordIdx.
            set  outputLineIdx up by 1.
            move asciiCR       to outputLineElt (outputLineIdx).
            set  outputLineIdx up by 1.
            move asciiCR       to outputLineElt (outputLineIdx).
            set  outputLineIdx up by 1.
            set  textStringIdx up by 1.
            perform moveTheText
              varying outputLineIdx from outputLineIdx by 1
                until textStringIdx > 80.
            display outputLine.
            stop run.

        findTheIdx.
            if foundText
                if textStringElt (textStringIdx) = space
                    move "Y" to foundIdxSw
                else
                    next sentence
            else
                if textStringElt (textStringIdx) not = space
                    move "T" to foundIdxSw.
        moveTheText.
            move textStringElt (textStringIdx)
              to outputLineElt (outputLineIdx).
            set  textStringIdx up by 1.

-=-=-=-=-

That's the verbose COBOL most folks are used to.  Put it in upper-case, 
and it would be what a lot of the world thinks COBOL is.  I've put these 
three here to illustrate that just because one may see crappy code 
written in a particular language, that doesn't meand that the language 
is incapable of having good code written in it.

As for a ForTran can't, I'll bet you can't write a ForTran program that 
is as long as the last one and only does what little it does.  ;)
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 5)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-29T20:04:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10bicm3o2735d6e@corp.supernews.com>`
- **In-Reply-To:** `<10bi5879obpdo49@corp.supernews.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com>`

```
LX-i wrote:
>       *>    "Verbose" way using COBOL 74-compliant code

Yes, I know I should have used single-quotes for my strings if I really 
wanted to compile it with a 74-compliant compiler - my mistake.

(omitted this from the PL/1 group...)

And yes, I know Mr. Frank seems to be one of those people with whom one 
cannot easily reason; but, as others have said, when Usenet records a 
permanent record, it's good to get good information out there for others 
(hence my self-correction here).  :)
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 5)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-30T02:42:25+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<40b94629.105551185@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote:

>        01  textString                    pic X(80) value
>                "The quick brown fox jumps over the lazy dog's back.".
…[8 more quoted lines elided]…
>                                          pic X.

Unnecessary REDEFINES are the signature feature of Bad Cobol. It drives me
crazy. Why don't they write:

 01  textString value "The quick brown fox jumps over the lazy dog's back.".
      12  testStringElt occurs 80 indexed testStrongldx pic x.
 01  outputLine.
      12 outputLineElt occurs 80 indexed outputLineldx pic x. 

Four lines vs. eleven. 

On the one hand they use abbreviations to avoid 'unnecessary typing'; on the
other hand they pad the program with superfluous words and spacing.
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-29T23:01:21-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bin1d5vuoe7c8@corp.supernews.com>`
- **In-Reply-To:** `<40b94629.105551185@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net>`

```
Robert Wagner wrote:
> LX-i <lxi0007@netscape.net> wrote:
> 
…[25 more quoted lines elided]…
> other hand they pad the program with superfluous words and spacing.

heh - I didn't say it was my preferred way of doing things, just that it 
mirrored what I maintain on a daily basis.  :)  I agree - when I 
discovered that I could put a value clause on a group item, it changed 
the way I defined tables (and other 01-level items).  With my compiler, 
there is a caveat (not sure if it's standard-imposed or not) - you can't 
use a usage clause under a group level item with a value clause.  So, 
for my bit-switches, I can't say...

01  MySwitches value zeroes.
     12  pic 1 binary-1.

...which kind of stinks, but I can understand the limitation as well.
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 7)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-30T11:55:20+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<40b9c05d.136840610@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote:

> when I 
>discovered that I could put a value clause on a group item, it changed 
…[8 more quoted lines elided]…
>...which kind of stinks, but I can understand the limitation as well.

Group names are implicitly pic x. It's an error to initialize bit/binary/packed
variables with F0 (EBCDIC) or 30 (ASCII). It's common for compilers to disallow
that value while permitting 'move zeroes to MySwitches'. Go figure.

I use Value only to initialize constants i.e. fields that will never change.
With regular variables, there are at least two potential bugtraps. One is the
Initialize verb which, according to the '85 Standard, does not use your Values.
The other is the operating system or Cobol runtime handling of called programs. 
If the caller does a Cancel, Values will be there on the next Call. But if the
caller forgets or abends or someone else calls your .dll, they probably won't
be. 

A third, less common, problem is Local-Storage. As discussed here, Micro Focus
used to leave it uninitialized. It didn't issue a warning about Value clauses,
as it would in Linkage-Section,  it just didn't use them. That's now fixed, but
there's a chance the shop's production compiler is older than its development
version, or another shop is using an old one.

For these reasons, I put 'individual' variables under a group name (rather than
using 77 or 01) and initialize it with 'move low-values to
unqualified-variables'.

FWIW, 'pic 1' seems like sufficient information for the compiler to define one
bit. It is on the AS/400. If your compiler makes you also write 'binary-1', that
seems redundant.
```

###### ↳ ↳ ↳ GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-30T19:07:09+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net>`

```
"Robert Wagner" <robert.deletethis@wagner.net> wrote in message
news:40b9c05d.136840610@news.optonline.net...
<snip>
> Group names are implicitly pic x. It's an error to initialize
bit/binary/packed
> variables with F0 (EBCDIC) or 30 (ASCII). It's common for compilers to
disallow
> that value while permitting 'move zeroes to MySwitches'. Go figure.
>

For those interested, the issue of group items versus the elementary items below
them was addressed in the 2002 ISO Standard (for *some* usages) - specifically
for BIT and NATIONAL groups.  For example, the following is valid 2002
conforming source code:

01  My-switchest Group-Usage Bit.
    05   Switch1  Pic 1 Bit.
    05   Switch2-3  Pic 1(2) Bit.

This lets you work with "my-switches" AS IF it were an elementary USAGE BIT
item.

   ***

If your "vendor of choice" supports BIT (or NATIONAL) items, check with them on
when/if they plan on providing this new data division clause.
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 9)_

- **From:** "Jeffery Swagger" <jeffos2@adelphia.net>
- **Date:** 2004-05-30T15:49:19-04:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<sfSdnat1Tdk2pyfdRVn-hg@adelphia.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net>`

```
ZippyDooDah to do with PL/I!
(Followup-To set to comp.lang.cobol)

----
Jeff

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net...
> "Robert Wagner" <robert.deletethis@wagner.net> wrote in message
> news:40b9c05d.136840610@news.optonline.net...
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 10)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-30T20:06:48-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bl163b8ln373c@corp.supernews.com>`
- **In-Reply-To:** `<sfSdnat1Tdk2pyfdRVn-hg@adelphia.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com>`

```
Jeffery Swagger wrote:

> ZippyDooDah to do with PL/I!
> (Followup-To set to comp.lang.cobol)

http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&safe=off&selm=c1.2c.2R9LTM%2401o%40localhost.mindspring.com

I guess you just don't see COBOL as a valuable tool...  'tis a pity, as 
I don't see PL/1 as an invaluable tool.  (I've also never used it - I 
try to make it a practice not to write off a tool until I've established 
its uselessness for myself.)
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 11)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-05-31T02:15:53+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<40BA956B.7080804@optonline.net>`
- **In-Reply-To:** `<10bl163b8ln373c@corp.supernews.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com> <10bl163b8ln373c@corp.supernews.com>`

```
LX-i wrote:
> Jeffery Swagger wrote:
> 
…[12 more quoted lines elided]…
> 

A little history here helps me love the buttons I have that say,

would you believe PL/2?

At the time the first spec of COBOL WAS about to be addressed by
the IBM OF THAT TIME, a Share Group was formed to do an end run on
COBOL. The chairman of the group, whose name and employer are not
available in my memory these days, called a meeting of several
IBM users  to Cincinnati, OH. Purpose, review the PL/1 draft
specs to see if there were suggestions the invitees wanted to make
to make the spec more like COBOL. Or any other purpose you want
to invent.

The people invited included about five representatives of large
IBM users. There were two of us from Pittsburgh.

Upon arrival, we were given a copy of the spec, and asked to
read it over night, and meet with them the next morning.

Suffice it to say, the objective of the meeting was not met.
There was no effort on our part to cut COBOL off at the pass.

Warren Simmons, New Jersey
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 12)_

- **From:** "John W. Kennedy" <jwkenne@attglobal.net>
- **Date:** 2004-05-31T03:09:25+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<Flxuc.18261$DC1.3829754@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<40BA956B.7080804@optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com> <10bl163b8ln373c@corp.supernews.com> <40BA956B.7080804@optonline.net>`

```
Warren Simmons wrote:
> At the time the first spec of COBOL WAS about to be addressed by
> the IBM OF THAT TIME, a Share Group was formed to do an end run on
…[5 more quoted lines elided]…
> to invent.

That story is grossly incompatible with the chronological facts.
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 13)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-05-31T17:04:42+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<KAJuc.33325$DC1.6037614@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<Flxuc.18261$DC1.3829754@news4.srv.hcvlny.cv.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com> <10bl163b8ln373c@corp.supernews.com> <40BA956B.7080804@optonline.net> <Flxuc.18261$DC1.3829754@news4.srv.hcvlny.cv.net>`

```
John W. Kennedy wrote:
> Warren Simmons wrote:
> 
…[10 more quoted lines elided]…
> That story is grossly incompatible with the chronological facts.
Give your chronology. Perhaps I can adjust my story to fit them.

Warren Simmons
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 14)_

- **From:** "John W. Kennedy" <jwkenne@attglobal.net>
- **Date:** 2004-05-31T23:14:29+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<p%Ouc.34639$DC1.7099796@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<KAJuc.33325$DC1.6037614@news4.srv.hcvlny.cv.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com> <10bl163b8ln373c@corp.supernews.com> <40BA956B.7080804@optonline.net> <Flxuc.18261$DC1.3829754@news4.srv.hcvlny.cv.net> <KAJuc.33325$DC1.6037614@news4.srv.hcvlny.cv.net>`

```
Warren Simmons wrote:
> John W. Kennedy wrote:
> 
…[15 more quoted lines elided]…
> Give your chronology. Perhaps I can adjust my story to fit them.

The first spec of COBOL was in 1959.
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 15)_

- **From:** Warren Simmons <wsimmons5@optonline.net>
- **Date:** 2004-06-01T01:53:46+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<KkRuc.1574$eU6.429465@news4.srv.hcvlny.cv.net>`
- **In-Reply-To:** `<p%Ouc.34639$DC1.7099796@news4.srv.hcvlny.cv.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com> <10bl163b8ln373c@corp.supernews.com> <40BA956B.7080804@optonline.net> <Flxuc.18261$DC1.3829754@news4.srv.hcvlny.cv.net> <KAJuc.33325$DC1.6037614@news4.srv.hcvlny.cv.net> <p%Ouc.34639$DC1.7099796@news4.srv.hcvlny.cv.net>`

```
John W. Kennedy wrote:
> Warren Simmons wrote:
> 
…[23 more quoted lines elided]…
> 
You are right. I was there. I'm talking about when the PL/1 entry
into the market took place.
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-30T22:09:24-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bl8bvtih6d88d@corp.supernews.com>`
- **In-Reply-To:** `<10bl163b8ln373c@corp.supernews.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com> <10bl163b8ln373c@corp.supernews.com>`

```
LX-i wrote:
> Jeffery Swagger wrote:
> 
…[8 more quoted lines elided]…
> I don't see PL/1 as an invaluable tool.

Make that "non-valuable"...
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 12)_

- **From:** "Jeffery Swagger" <jeffos2@adelphia.net>
- **Date:** 2004-05-31T10:03:42-04:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<-8mdnWcoJ9Kipibd4p2dnA@adelphia.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com> <10bl163b8ln373c@corp.supernews.com> <10bl8bvtih6d88d@corp.supernews.com>`

```
So are wrenches valuable tools. Does that mean we
should discuss proper wrench usage here?

Between David Frank and his egger-oners and now the
COBOLers, the signal-to-noise ratio of this group is
close to zero. Perhaps we should rename it to
comp.lang.talk.about.anything.at.all.EXCEPT.pl1.

----
Jeff

"LX-i" <lxi0007@netscape.net> wrote in message news:10bl8bvtih6d88d@corp.supernews.com...
> LX-i wrote:
> > Jeffery Swagger wrote:
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2004-05-31T10:41:11-04:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<c9fg67$bo8$1@panix5.panix.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <10bl163b8ln373c@corp.supernews.com> <10bl8bvtih6d88d@corp.supernews.com> <-8mdnWcoJ9Kipibd4p2dnA@adelphia.com>`

```
In article <-8mdnWcoJ9Kipibd4p2dnA@adelphia.com>,
Jeffery Swagger <jeffos2@adelphia.net> wrote:
>So are wrenches valuable tools. Does that mean we
>should discuss proper wrench usage here?

I can barely control what *I* discuss, let alone others.

If one's comments are in accord with the group's charter then feel free to 
post them.

If one's comments are not in accord with the group's charter then one
might realise that posting them might cause one to run afoul of one's
ISP's TOS.

If the newsgroup no longer fulfills one's needs or desires then one might 
wish to consider limiting one's participation (both active and passive) 
and/or establishing a new newsgroup, either open or moderated, which might 
more accurately manifest the aforementioned needs or desires.

These suggestions are, by no means, intended to be a complete listing of 
the courses of action which one might wish to take, nor are they intended 
to be a complete catalogue of all actions which might be available.

DD
```

###### ↳ ↳ ↳ Re: GROUP-USAGE (was Alternative COBOL "telco" source program

_(reply depth: 13)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-31T20:11:31-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bnlre7gjulb61@corp.supernews.com>`
- **In-Reply-To:** `<-8mdnWcoJ9Kipibd4p2dnA@adelphia.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <xhquc.15820$Tn6.4796@newsread1.news.pas.earthlink.net> <sfSdnat1Tdk2pyfdRVn-hg@adelphia.com> <10bl163b8ln373c@corp.supernews.com> <10bl8bvtih6d88d@corp.supernews.com> <-8mdnWcoJ9Kipibd4p2dnA@adelphia.com>`

```
Jeffery Swagger wrote:
> So are wrenches valuable tools. Does that mean we
> should discuss proper wrench usage here?

If you can think of an appropriate benchmark between wrench usage and 
PL/1...  :)

> Between David Frank and his egger-oners and now the
> COBOLers, the signal-to-noise ratio of this group is
> close to zero. Perhaps we should rename it to
> comp.lang.talk.about.anything.at.all.EXCEPT.pl1.

In comp.lang.cobol, this seems to come in waves.  There'll be a flurry 
of "noise", and then it'll phase out.  Then, there'll be the interesting 
debates, which somehow morph into other off-topic discussions.

I'm guessing it's just the nature of the beast.  Some folks enjoy the 
noise - it's funny how the noise of others is much more annoying than 
noise you're participating in.  :)  I try to live and let live - I don't 
tell the folks debating whether the government has told us the truth to 
take it to alt.black.helicopters; I just skim the thread.

I'll try not to post excessive non-PL/1 stuff to the group.  But, as 
Usenet provides a "permanent record", I also believe it's important to 
correct erroneous postings (especially when the errors are in my 
posting).  I'm sure once the TelCo thread goes away, so will the 
COBOLlers (except the ones that also participated there before this 
thread began).

No hard feelings?
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 8)_

- **From:** "Jeffery Swagger" <jeffos2@adelphia.net>
- **Date:** 2004-05-30T15:16:41-04:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<qOWdnUlukcWcrifd4p2dnA@adelphia.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net>`

```
WTF does *any* of this have to do with PL/I?
(Followup set to comp.lang.cobol)

----
Jeff

"Robert Wagner" <robert.deletethis@wagner.net> wrote in message news:40b9c05d.136840610@news.optonline.net...
> LX-i <lxi0007@netscape.net> wrote:
> 
…[36 more quoted lines elided]…
> seems redundant.
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-30T19:53:32-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bl0d7jor8nd4e@corp.supernews.com>`
- **In-Reply-To:** `<qOWdnUlukcWcrifd4p2dnA@adelphia.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <qOWdnUlukcWcrifd4p2dnA@adelphia.com>`

```
Jeffery Swagger wrote:

> WTF does *any* of this have to do with PL/I?

What does your ForTran or PL/1 have to do with us COBOLlers?  It's an 
offshoot of a cross-posted thread that may or may not drift back into 
the realm of meaningfulness to ForTran or PL/1 folks...  Threads often 
meander, and I find it interesting to see little snips of code here and 
there - helps expand my knowledge base.  That may not be your thing, but 
surely your skin isn't that thin, is it?
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 10)_

- **From:** "Jeffery Swagger" <jeffos2@adelphia.net>
- **Date:** 2004-05-30T21:31:54-04:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<A6WdneaVVMOWFifd4p2dnA@adelphia.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <qOWdnUlukcWcrifd4p2dnA@adelphia.com> <10bl0d7jor8nd4e@corp.supernews.com>`

```
Oh horse hockey!

There is a reason that different groups exist.
COBOL has its own peculiarities unique to its 
practitioners as does PL/I as does C as does ...

Just please stay on topic.

----
Jeff

"LX-i" <lxi0007@netscape.net> wrote in message news:10bl0d7jor8nd4e@corp.supernews.com...
> Jeffery Swagger wrote:
> 
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 11)_

- **From:** "PAUL RAULERSON" <pkraulerson@verizon.net>
- **Date:** 2004-05-31T03:46:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jUxuc.16340$g15.6086@nwrddc02.gnilink.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <qOWdnUlukcWcrifd4p2dnA@adelphia.com> <10bl0d7jor8nd4e@corp.supernews.com> <A6WdneaVVMOWFifd4p2dnA@adelphia.com>`

```
<grin> You do have thin skins don't you?!
Relax, and if you really don't want to see the thread, just tell your
newsreader to ignore it.
-Paul

"Jeffery Swagger" <jeffos2@adelphia.net> wrote in message
news:A6WdneaVVMOWFifd4p2dnA@adelphia.com...
> Oh horse hockey!
>
…[9 more quoted lines elided]…
> "LX-i" <lxi0007@netscape.net> wrote in message
news:10bl0d7jor8nd4e@corp.supernews.com...
> > Jeffery Swagger wrote:
> >
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 8)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-30T19:42:03-05:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<10bkvnnc74tuifb@corp.supernews.com>`
- **In-Reply-To:** `<40b9c05d.136840610@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net>`

```
Robert Wagner wrote:
> LX-i <lxi0007@netscape.net> wrote:
> 
…[16 more quoted lines elided]…
> that value while permitting 'move zeroes to MySwitches'. Go figure.

It disallows any usage clauses.  (I haven't tried "Display" - it may let 
that one slide...)

> I use Value only to initialize constants i.e. fields that will never change.
> With regular variables, there are at least two potential bugtraps. One is the
…[4 more quoted lines elided]…
> be. 

Right.  It would have been nice if the Initialize verb grabbed your 
initial values, instead of just spaces/zeroes.  Didn't I read that 
that's an option in the 2002 standard?  I've recently run into this 
issue, as I'm taking programs that were once-through guys, and made them 
loop endlessly (until the OS tells them to get lost).  You find all 
kinds of interesting stuff - variables not initialized, cursors not 
closed properly, etc.  :)

> A third, less common, problem is Local-Storage. As discussed here, Micro Focus
> used to leave it uninitialized. It didn't issue a warning about Value clauses,
> as it would in Linkage-Section,  it just didn't use them. That's now fixed, but
> there's a chance the shop's production compiler is older than its development
> version, or another shop is using an old one.

I have yet to use a compiler that has Local-Storage...  I'll file this 
in my head for future reference.

> FWIW, 'pic 1' seems like sufficient information for the compiler to define one
> bit. It is on the AS/400. If your compiler makes you also write 'binary-1', that
> seems redundant. 

I think it's required to flag it as an extension to the standard. 
There's a compiler option that says you don't have to have that there 
(and we use it), but it clutters up the print listings with extra 
remarks, so I try to use it.  As far as their rationale for requiring a 
usage clause on Pic 1's...  ?  (Maybe if I end up working for Unisys one 
day I can find out.)
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 9)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-31T19:14:47+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<40bb83c2.46409913@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <10bkvnnc74tuifb@corp.supernews.com>`

```
LX-i <lxi0007@netscape.net> wrote:

>Robert Wagner wrote:
>> LX-i <lxi0007@netscape.net> wrote:
…[15 more quoted lines elided]…
>> Group names are implicitly pic x. It's an error to initialize
bit/binary/packed
>> variables with F0 (EBCDIC) or 30 (ASCII). It's common for compilers to
disallow
>> that value while permitting 'move zeroes to MySwitches'. Go figure.
>
…[5 more quoted lines elided]…
>> Initialize verb which, according to the '85 Standard, does not use your
Values.
>> The other is the operating system or Cobol runtime handling of called
programs. 
>> If the caller does a Cancel, Values will be there on the next Call. But if
the
>> caller forgets or abends or someone else calls your .dll, they probably won't
>> be. 
…[9 more quoted lines elided]…
>> A third, less common, problem is Local-Storage. As discussed here, Micro
Focus
>> used to leave it uninitialized. It didn't issue a warning about Value
clauses,
>> as it would in Linkage-Section,  it just didn't use them. That's now fixed,
but
>> there's a chance the shop's production compiler is older than its development
>> version, or another shop is using an old one.
…[4 more quoted lines elided]…
>> FWIW, 'pic 1' seems like sufficient information for the compiler to define
one
>> bit. It is on the AS/400. If your compiler makes you also write 'binary-1',
that
>> seems redundant. 
>
…[18 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 9)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-31T19:16:22+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<40bb8449.46545186@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <10bkvnnc74tuifb@corp.supernews.com>`

```
Whoops. I pushed Send Reply by mistake.
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 10)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-05-31T20:13:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10bnlvomu76l293@corp.supernews.com>`
- **In-Reply-To:** `<40bb8449.46545186@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <10bkvnnc74tuifb@corp.supernews.com> <40bb8449.46545186@news.optonline.net>`

```
Robert Wagner wrote:

> Whoops. I pushed Send Reply by mistake.

I just thought you were running short on words...  ;)
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 11)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-06-01T13:22:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lq%uc.606$jS2.166@newssvr15.news.prodigy.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <10bkvnnc74tuifb@corp.supernews.com> <40bb8449.46545186@news.optonline.net> <10bnlvomu76l293@corp.supernews.com>`

```
"LX-i" <lxi0007@netscape.net> wrote in message
news:10bnlvomu76l293@corp.supernews.com...
> Robert Wagner wrote:
>
> > Whoops. I pushed Send Reply by mistake.
>
> I just thought you were running short on words...  ;)

Thought or hoped?
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 12)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-06-01T12:45:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10bpg3ii73nhpdb@corp.supernews.com>`
- **In-Reply-To:** `<Lq%uc.606$jS2.166@newssvr15.news.prodigy.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <10bkvnnc74tuifb@corp.supernews.com> <40bb8449.46545186@news.optonline.net> <10bnlvomu76l293@corp.supernews.com> <Lq%uc.606$jS2.166@newssvr15.news.prodigy.com>`

```
Michael Mattias wrote:
> "LX-i" <lxi0007@netscape.net> wrote in message
> news:10bnlvomu76l293@corp.supernews.com...
…[9 more quoted lines elided]…
> Thought or hoped?

I don't have the problem with him that some do...  He's had some good 
input on issues I've posted in the past.  Everyone posts things that 
need to be corrected (heck, I've done that several times over the last 
week, cross-posted to another NG, no less).

I understand the "assertion as fact" issue, but rather than berate him 
over it, I'd rather just infer what I thought he meant or, when he 
clarifies, adjust it.

So - "thought".  :)
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-05-30T20:49:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0405301949.50015a91@posting.google.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net>`

```
robert.deletethis@wagner.net (Robert Wagner) wrote

> The other is the operating system or Cobol runtime handling of called programs. 
> If the caller does a Cancel, Values will be there on the next Call. But if the
> caller forgets or abends or someone else calls your .dll, they probably won't
> be. 

If the caller 'forgets' to cancel and expects initial values then it
is a program bug.

If the caller 'abends' then it is unlikely that they will notice if or
not the next call to a program has initial values or not - it won't
get there.

If 'someone else calls your .dll' and gets your data values then that
would be a serious issue, but what systems would this occur with ?
 
> A third, less common, problem is Local-Storage. As discussed here, Micro Focus
> used to leave it uninitialized. It didn't issue a warning about Value clauses,
> as it would in Linkage-Section,  

MF has an extension that treat VALUE clauses in FDs, LINKAGE-SECTION
and LOCAL-STORAGE (depending on version) as documentary (except of
course on condition names where they are always valid).

> it just didn't use them. That's now fixed, 

That wasn't a 'bug' to be fixed, it was defined behaviour.

> but
> there's a chance the shop's production compiler is older than its development
> version, or another shop is using an old one.

Or even a different compiler vendor.
 
> For these reasons, I put 'individual' variables under a group name (rather than
> using 77 or 01) and initialize it with 'move low-values to
> unqualified-variables'.

One assumes that you only use binary types for these variables. 
Packed and display variables may be just as poorly initialised as
occurs with ascii zero characters on packed.

> FWIW, 'pic 1' seems like sufficient information for the compiler to define one
> bit. It is on the AS/400. If your compiler makes you also write 'binary-1', that
> seems redundant.

PIC 1 may (depending on version) be usage display or bit (or other). 
Display may be the default usage, in which case specifying the
required usage is not redundant.
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 9)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-05-31T16:29:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<K3Juc.4271$n65.2448@newssvr33.news.prodigy.com>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <217e491a.0405301949.50015a91@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0405301949.50015a91@posting.google.com...
> If the caller 'forgets' to cancel and expects initial values then it
> is a program bug.

Reminds me of an old saw, in which I still believe: "There is no such thing
as user error. There are only missed edits."

MCM
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 9)_

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-31T19:12:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40bb46e8.30829924@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <10bin1d5vuoe7c8@corp.supernews.com> <40b9c05d.136840610@news.optonline.net> <217e491a.0405301949.50015a91@posting.google.com>`

```
riplin@Azonic.co.nz (Richard) wrote:

>robert.deletethis@wagner.net (Robert Wagner) wrote
>
>> The other is the operating system or Cobol runtime handling of called 
>> programs. If the caller does a Cancel, Values will be there on the next Call.

>> But if the caller forgets or abends or someone else calls your .dll, they
>>probably won't be.
>
>If the caller 'forgets' to cancel and expects initial values then it
>is a program bug.

If program A forgets and program B expects initial values, where is the bug? I
think it's in the called program. Systems are more reliable when programs are
responsible for their own storage.

>If the caller 'abends' then it is unlikely that they will notice if or
>not the next call to a program has initial values or not - it won't
>get there.

If the called program is a .dll or .so, when the caller causes a general
protection exception, there is a good chance the OS will not decrement the
'usage count' of the called program. With a non-zero count, it will stay in
memory until the OS is rebooted. That's WHY installation packages tell you to
reboot.

Even when the usage count goes to zero, Windows will keep DLLs in memory if this
registry entry is missing, which it often is, or set to a value other than 1:
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\explorer\AlwaysUnloadDll


>If 'someone else calls your .dll' and gets your data values then that
>would be a serious issue, but what systems would this occur with ?

 Windows and Unix systems. 

One would hope that a call to GetModuleHandle() followed by a call to
FreeLibrary() would reduce the usage count by 1. It's not that easy.
GetModuleHandle() finds only modules linked to your task. If you don't know what
it does, calling it to establish a link could be dangerous.

>> For these reasons, I put 'individual' variables under a group name (rather 
>> then using 77 or 01) and initialize it with 'move low-values to
…[4 more quoted lines elided]…
>occurs with ascii zero characters on packed.

Packed-decimal, as used in Cobol, is a type defined by mainframe hardware. To an
Intel assembly language programmer, Packed means multiple integers stored in a
single 64-bit word, enabling the hardware to add or multiply up to eight
integers in parallel with a single instruction. For example, PADDUSB for "packed
add unsigned with saturation, byte". Its most common use is manipulating screen
pixels.

Initializing pic x to low-values requires only a shift in thinking about which
value means 'empty'.

I use display numbers for DISPLAY on screens, reports and files. There's no
reason to use that format for temporary variables in memory.

>> FWIW, 'pic 1' seems like sufficient information for the compiler to define 
>>one bit. It is on the AS/400. If your compiler makes you also write
…[4 more quoted lines elided]…
>required usage is not redundant.

Pic 1 was an extension before 2002, so it means whatever the vendor says. It
seems pointless to make it default to display. They already had pic 9. Why
invent a new type to do the same thing?

A more useful invention would have been SATURATED, meaning the highest value the
variable can store. We could turn an indicator on with 'set my-indicator to
saturated' and test with 'if my-indicator is saturated'. Syntax would be the
same for pic x, 9 or 1. We could also use it for arithmetic 'add a to b on size
error set b to saturated'. That's what PADDUSB does.
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-06-01T15:14:19+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<c9i6gb$i53$1@peabody.colorado.edu>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net>`

```

On 29-May-2004, robert.deletethis@wagner.net (Robert Wagner) wrote:

> Unnecessary REDEFINES are the signature feature of Bad Cobol. It drives me
> crazy. Why don't they write:

REDEFINES work when it fits the data.   When you are reading data that might
have different formats, redefines work better than anything else.


>  01  textString value "The quick brown fox jumps over the lazy dog's back.".
>       12  testStringElt occurs 80 indexed testStrongldx pic x.

That didn't use to be possible.

> Four lines vs. eleven.

What's the big deal about counting lines?

> On the one hand they use abbreviations to avoid 'unnecessary typing'; on the
> other hand they pad the program with superfluous words and spacing.

Who's "they"?    I don't mind typing.

P.S.  Why did you make your text string so long?   No need to have the word
"back".   Jump over the lazy dog.
```

###### ↳ ↳ ↳ Re: Alternative COBOL "telco" source program

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-06-01T12:47:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10bpg61d5kdr74d@corp.supernews.com>`
- **In-Reply-To:** `<c9i6gb$i53$1@peabody.colorado.edu>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com> <10bfu1iimqi3te9@corp.supernews.com> <6eVtc.34937$Ol3.23233@twister.tampabay.rr.com> <10bi5879obpdo49@corp.supernews.com> <40b94629.105551185@news.optonline.net> <c9i6gb$i53$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

> On 29-May-2004, robert.deletethis@wagner.net (Robert Wagner) wrote:
> 
…[5 more quoted lines elided]…
> "back".   Jump over the lazy dog.

That was in that "Can't 18" spec.
```

##### ↳ ↳ Re: Alternative COBOL "telco" source program

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-29T10:52:40+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1
- **Message-ID:** `<40b86948.48997765@news.optonline.net>`
- **References:** `<Iadtc.12799$L.1063@news-server.bigpond.net.au> <cfaeadf3.0405271151.20c59a4@posting.google.com>`

```
lruss@superlink.net (L Russ) wrote:


>Here's my version using C++, no loop. Another FORTRAN CAN'T.  Big
>deal.

Here's a three-line Cobol version:

inspect c tallying i for charcters before first '  '   <* two spaces
perform varying i from i by -1 until c(i:1) = ' '.
display c(1:i) x'0d0a' c(i+1)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
