[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# An OO Contest!

_65 messages · 16 participants · 2000-03_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### An OO Contest!

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8adj2h$97n$1@nnrp1.deja.com>`

```




Hi:                                                    3/11/00

Perhaps it would help resolve the OO issue by having a contest.

Thane and I recently discussed developing an OO program and
presenting its evolution to the throng.

I will write a my-way program and we can compare it to the OO
program as it is developed. Since Thane is an admitted novice
when it comes to OO it wouldn't be fair to expect him to write it,
so, the OO fraternity should nominate an OO advocate as the primary
author with others making contributions, perhaps.

These are the rules:

A. It must actually work and run on the PC under any flavor of Windows.

There are no other rules.

We have to have a simple, real-world application which everyone
can relate to and I think the Time-clock thing would do the trick.

These are the requirements of the application:

1. The ability to record employee-id (initials), name, address,
social-security number, and phone number. The program must be
able to add new employees, and change or delete them.

2. Employees can punch-in and punch-out.

3. Program must make backups of the personnel file.

A real-world program would also print the employee file and print
an hours-worked report. We can leave this sort of stuff out to
keep it small and simple.

In my-way, there are four steps to development:

a. Design screen format.
b. Design record format.
c. Write program.
d. Be happy.

The my-way program will be written in MF COBOL and use the wonderful
SP2.

The first step in the contest will be to design the screen.
The second step in the contest will be to design the file.
The third step in the contest will be to write the procedure division.

I think the exercise will be of value to those wanting to know more
about OO, and, it might be of value to those new to programming.

Any takers?

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: An OO Contest!

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CA8982.FC3A7234@home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> Hi:                                                    3/11/00
> 
> Perhaps it would help resolve the OO issue by having a contest.

IT WONT resolve the OO issue - but it should generate some interesting
comparisons.
> 
> Thane and I recently discussed developing an OO program and
…[46 more quoted lines elided]…
> about OO, and, it might be of value to those new to programming.

You couldn't possibly be thinking of moi could you :-) OK you're on.
Now you know what I'm going to produce, because you already have it !
And this isn't to attempt to show what a clever bugger I am - just my
approach to using OO. And my thinking could be way out of wack and a
complete travesty of OO methodology.

Now I've got to introduce some sub-rules to the game. 

- (S1) - The only thing I know, and have access to, is Windows 98 - so  
that's the only flavour I am going to address.

- (S2) - we are talking single thread and I am not into multi-user

- (S3) This is not a speed test. I've got other things on my plate at
the moment :- 

(a) cobolreport.com articles

(b) RM/COBOL - Reluctantly, having revamped the system to OO my end-user
insisted on us switching to Y2K in RM - what a bugger - I'm talking
about a compiler written in 1980 - the same bloody compiler that young
Barak in Israel is trying to do pop-ups with ! Now having switched the
system it doesn't finish there. I provided the user with In/Out ascii
delimiteds - because RM rebuilds then were a real pain. So now I'm in
the process of changing those ASCII's - from yymm to ccyymm.

(b) More importantly I'll be in UK late May/June - first time in 25
years - catching the tail-end of the J4 at Newbury, and then see family
(actually only cousins - sadly we are now the 'old' generation in the
family)

-(S4) - To make this thing consistent - I think the following should
happen, and you are playing analyst, giving us the design specification
:-

	(i) You decide the file formats - If I disagree I'll say why -
	    and don't come up with cryptic field-names, make them 
	    plain and meaningful. It's all I've got, so it has to be 
	    flat-files.
	(ii) Doesn't make sense for each of us to dream up a set of
	     validity rules for checking - so you set the validity 		    
checks
	(ii) You give us a jpg file or whatever, with a snapshot of
	     your screens - then we can all try building the same 		    
animal. Now don't go artsy fartsy on this one and throw
	     in irrelevancies like bit maps - keep it simple and
	     business-like

- (S4) - When it's all done - I will announce the 'secret' rule # 4 -
Not trying to catch you out, but up front, you ALL have to agree to
abide by this rule.

THIRD approach - Now here's an interesting thing - and I'm not plugging
NetExpress - just that I'm aware certain people use different features
of a product and can also give us comparative examples. OK, so some of
the suggested participants below aren't into OO - but the comparisons
could be quite interesting if they are prepared to play ball :-

- Judson - Do want to give it a shot using structured with 		
Screen Section

- Don - want to give it a shot - using Fujitsu and your approach to OO
with Screen Section. Doesn't seem much point to you doing it SP2 - Thane
and Tony have already got that one covered off. (Or is it too early in
the game for you to come up with some workable goods ?)

- Ken Mullins - Are you interested in showing how you would do it with
direct calls to APIs

- Ray - I know you could do it in a variety of ways - interested in
showing how you would do it with Dialog System

- Simon - want to give it a shot with OOs in you own particular style

- Cheesle - want to give it a shot using AcuCOBOL 'dual screen'

- Ib or anybody else who would be interested in contributing - want to
join in the fray and illustrate your particular approach		

- Howard - sorry you're out of the game - we aren't interested in you
mainframers - No seriously, if you can produce something for a PC -
might be another interesting comparison.

Pete - Yes Mr. Dashwood, you think CLC is a waste of time - so put your
money where your mouth is :-) Give it to us using Activex - sorry sport,
no Database - we are talking flat files

Gene - How about OO and Visual Basic combination ?

Ken Foskey - gawd I don't want it in C++ - I want to be able to read it
:-)

Alistair in UK - or any others who are 'modest' enough to think they are
in Bill Reed's elite 5% - want to show how you would do it ?

TIME-LINE - because of our various commitments, maybe we should target
for late June for the finished goods ?

Totally ignoring the OO issue, if all suggested participants join in, it
should produce some very interesting comparisons, both in approach and
techniques.

Jimmy
```

##### ↳ ↳ Re: An OO Contest!

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aea42$ol2$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com>`

```
Hi:


Jimmy said:

Now I've got to introduce some sub-rules to the game.

- (S1) - The only thing I know, and have access to, is Windows 98 - so
that's the only flavour I am going to address.


SORRY-If you are using a development system which restricts you to
Windows 98 then there is something wrong.  I will use MF COBOL
and SP2 on a 95 machine and the EXE will run on any flavor of
Windows. If your program would be restricted to 98 for some
reason, it loses mucho points.


- (S2) - we are talking single thread and I am not into multi-user

SORRY-This has to be a real-world thing.  It must be multi-user.



- (S3) This is not a speed test. I've got other things on my plate at
the moment

DEFINITELY - this is not a race.  In fact it needs to be organized. I
will organize it if everyone agrees.




(b) RM/COBOL - Reluctantly, having revamped the system to OO my end-user
insisted on us switching to Y2K in RM - what a bugger - I'm talking
about a compiler written in 1980.

If the RM antique is all you have, then you should not compete. Get
the Fujitsu free compiler.


-(S4) - To make this thing consistent - I think the following should
happen, and you are playing analyst, giving us the design specification


	(i) You decide the file formats - If I disagree I'll say why
	    and don't come up with cryptic field-names, make them
	    plain and meaningful. It's all I've got, so it has to be
	    flat-files.

SORRY- The contestant must design their own file. Remember, the
essence of system-design is file-design.

	(ii) Doesn't make sense for each of us to dream up a set of
	     validity rules for checking - so you set the validity
checks

OK-Program requires entry of initials (prime key), name, street address,
social-security number, city, state and zip. All but second line of
address are required entries. State must be validated. You have to be
able to add new employees, change or delete them in addition to being
able to punch-in and punch-out. Any specific questions, just email me.

	(ii) You give us a jpg file or whatever, with a snapshot of
	     your screens - then we can all try building the same
            animal. Now don't go artsy fartsy on this one and throw
	     in irrelevancies like bit maps - keep it simple and
	     business-like


SORRY-You must design your own screen(s). Besides, I will use SP2
to design the screen and everyone does not have SP2 (although they
should).  I don't know why a program should not have some artistic
merit - I mean, even if it doesn't work, it should be at least
nice to look at (isn't that the Microsoft philosophy?).


- (S4) - When it's all done - I will announce the 'secret' rule # 4
Not trying to catch you out, but up front, you ALL have to agree to
abide by this rule.

OK



Here are some more rules.

It must use BRAND NEW CODE written specifically for this contest.
(The exception to this is that it may use already-written subroutines
such as a standard error routine, a routine to get the date and time,
etc. I have many such odds and ends which I have used for more than
30 years, and I will use them. Anyone not having such things would
be well advised to get them pronto.)

As each lump of code is developed it should be presented to the group.
This way, the throng can follow the code as it is developed.
The final product must be a real-live working program which you
would happily present to your user.

These are the steps as I see them.

Step 1. You must design your screen(s) first. These must be submitted
separately in jpg format. You can email them to me and I will
consolidate all contestant's stuff into a ZIP file which can be
downloaded or gazed upon via the Web.


Step 2. Will be file design. It must be multi-key ISAM or something
comparable within the capability of the compiler. I cannot imagine
that anyone would design a NEW application around flat files.
I suppose it is OK to use something other than ISAM, but I would wonder
why one would want to.

Step 3. The rest of it.

So far as your suggestions about other approaches, I suggest:

1. A structured example would be interesting if someone would
   volunteer to do one.

2. I don't think that direct calls to APIs should be considered but
   that is only because I don't know how one would do that using
   COBOL - unless indirectly via SP2.  Ken should do it then
   so long as it is mostly a COBOL program.

3. I don't know what Dialog System is (its amazing how much I don't
know)but a version using it would be welcome.

My version, of course, is going to be written in a style to make
everyone purple - riddled with go to and perform statements.


TIME-LINE - because of our various commitments, maybe we should target
for late June for the finished goods ?

Let's not have a time-line, there is too much chocolate to eat.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An OO Contest!

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38cab3a2.237687047@news.cox-internet.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com>`

```
Posted and mailed and long.

On Sat, 11 Mar 2000 20:25:41 GMT, Foodman <foodman123@aol.com> wrote:

Sorry, but there's several things here I can't agree with (And I
invented the idea <G>).

>Hi:
>
…[13 more quoted lines elided]…
>reason, it loses mucho points.

I don't think this is an issue.  If we can agree on 32 bit Windows
that's fine by me.

>
>
…[3 more quoted lines elided]…
>

This one I DO agree with - Come on Jimmy, add a record locked check
and let's get on with it. <G>.


>
>
…[4 more quoted lines elided]…
>will organize it if everyone agrees.

Maybe - I'm reserving judgement.  Read on!

>(b) RM/COBOL - Reluctantly, having revamped the system to OO my end-user
>insisted on us switching to Y2K in RM - what a bugger - I'm talking
…[3 more quoted lines elided]…
>the Fujitsu free compiler.

Jimmy has NetExpress (What version Jimmy? 2 or 3?).  He is working
with RM right now for a paying client.  Let me take this chance as an
aside to let people know what the heck I am doing.

I work full time for a company in support, mainly, of an invoicing
system and for some transaction fulfilment in a service company that
processes, for our over 15,000 customers, around 2 million
transactions a month.  My main work is on VMS using COBOL 85, on NT
using SQL, JAVA (learning presently) and Oracle databases and  on
OS/390 using VSAM and the latest and greatest IBM COBOL compiler.  I
do things in other languages and handle the management of a tax
package that is used company wide.  

On the side, in my spare time, I work for myself, developing (Very
slowly I might add) a few different software products that will be
marketed to end users.  In addition I maintain several systems that I
wrote in the past and sold.  I answer email about my book, and I
handle reader problems as they crop up -- Thankfully, few and far
between.  I dabble in writing for Journals, such as my work for IEEE
Software (Thanks Ed) and some past work for The COBOL Report.  

I have dreams of someday working only for myself, but the level of
work I have to do, while increasing, is not at critial mass yet where
I can jump.  Someday maybe.  Anyway, I also am presently working for
my old COBOL mentor (when I first started out) to help him convert
some Realia 16 bit code to Fujitsu 32 bit code.  A large portion of
this involves some very specialized Assembler routines that I am
converting from 16 to 32 bit ASM (Not as trivial as it might first
seem).  I have another life too, and I restrict myself to 2 hours a
night of real work(4 days a week), with 4 hours on Sunday.  This news
group I consider fun.

Anyway, I agree this cannot be a speed contest, I don't have the time,
presently, for that kind of investment.  But learning this stuff will
be worthwhile in the long run.


>
>-(S4) - To make this thing consistent - I think the following should
…[9 more quoted lines elided]…
>essence of system-design is file-design.

I think we need a common file structure - but I intend to make an
application I can actually put to good use.  I think some general
guidelines are in order, but I have some specialized stuff I want to
include for my own use.
>
>	(ii) Doesn't make sense for each of us to dream up a set of
…[7 more quoted lines elided]…
>able to punch-in and punch-out. Any specific questions, just email me.

This is all ancillary stuff that is just going to slow us down I
think.  Silly things like state validation can be left for later -
they are not core to the application.  For *MY* needs, all I really
need ot track is a persons name!

>
>	(ii) You give us a jpg file or whatever, with a snapshot of
…[10 more quoted lines elided]…
>nice to look at (isn't that the Microsoft philosophy?).

Go ahead and design a screen Tony.  If we can do it with Sp2, Jimmy
can do it with native API calls - having the same screen (even if we
fail to match at the end) will show some strengths and weaknesses of
the various products.  I am especially interested in seeing how well
AcuCOBOL does attempting to generate the screen you come up with.

>
>
…[4 more quoted lines elided]…
>OK

This one sound interesting.

>
>
…[8 more quoted lines elided]…
>be well advised to get them pronto.)

This is my main objection.  The WHOLE point to OO is code re-use.
Reuse whatever you have that fits - this is supposed to be real world!
You can reuse code too!  No reason to make this all new!
is way, the throng can follow the code as it is developed.

>Step 1. You must design your screen(s) first. These must be submitted
>separately in jpg format. You can email them to me and I will
>consolidate all contestant's stuff into a ZIP file which can be
>downloaded or gazed upon via the Web.

I really don't like this one.  The whole thing needs to be designed
from the inside out, not the outside in.  This may be "The key" to
understanding and properly implementing OO.  The UI can actually be
left for LAST in the design phase.


>
>
…[4 more quoted lines elided]…
>why one would want to.

Jimmy uses "FLAT" files to mean indexed and sequential - or at least I
think he does!  He just means non database.  Again, I don't really
think this matters - it will be isolated from the system and it too
can be left for near the end of the design phase.


>
>TIME-LINE - because of our various commitments, maybe we should target
…[3 more quoted lines elided]…
>

OK by me.  I agree with Ken though - we do not need a contest.
Watching the OO develop will be interesting enough!  But if you want
to "compete" I can't see anything preventing us all from learning
something from the process.

PS - if this never comes to pass, no one is to blame.  Life happens.
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aeja6$uko$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com>`

```
Hi:

Thane and Jimmy said:


I don't think this is an issue.  If we can agree on 32 bit Windows
> that's fine by me.


TONY SAYS-When 500mhz PCs are $350.00, does it really matter whether
you use a 16-bit or 32-bit compiler? I have a 16-bit compiler which
produces DLLs which work on all flavors of Windows. The whole issue
of 16 vs 32 bit software isn't worth talking about. Except in extreme
cases, I doubt if you could tell the difference in execution speed.
For sure, I ain't gonna spend no moolah on a 32-bit compiler.
I think it would be sad to develop an application which required
a particular flavor of Windows. Why go through all the aggravation
of converting from 16 to 32 bit, why?


> >
> >-(S4) - To make this thing consistent - I think the following should
> >happen, and you are playing analyst, giving us the design
specification
> >
> >
…[11 more quoted lines elided]…
> include for my own use.

TONY SAYS-I feel strongly that each contestant should design their
own file. The quality of the program will be a reflection of the
quality of the file design. Perhaps this is an exercise in system
design and programming and implementation rather than an OO coding
exercise.  However, I think that is what it should be. Otherwise,
all sorts of annoying little details will be ignored in the examples
created.


> This is all ancillary stuff that is just going to slow us down I
> think.  Silly things like state validation can be left for later -
> they are not core to the application.  For *MY* needs, all I really
> need ot track is a persons name!
>

TONY SAYS- Thane, how could you?  If you consider state validation
a 'silly thing' you should be ashamed. I have a state-validation
routine which I have used for about 35 years. It takes three lines
of code to validate the state. You MUST have such a thing. Further
on, you comment about OO being all about reusable code. Well,
it doesn't have to be OO to be reusable and my state validation
routine has been used thousands of times by me and my subordinates
(when I had them). Doesn't EVERYBODY have a state routine?


> >
> >	(ii) You give us a jpg file or whatever, with a snapshot of
…[17 more quoted lines elided]…
>

TONY SAYS-Again, I feel strongly that one should design one's own
screen. The quality of the program will reflect the quality of the
design.

If you all yell at me, I will design one but you won't like it.


>
> This is my main objection.  The WHOLE point to OO is code re-use.
> Reuse whatever you have that fits - this is supposed to be real world!
> You can reuse code too!  No reason to make this all new!

TONY SAYS- Certainly, my whole philosophy of programming is that you
NEVER code the same thing twice. I haven't written a program from
scratch in years but I have 'manufactured' hundreds. I don't need OO to
save me from rewriting stuff. Of course, code has to be DESIGNED to be
easily reusable.


> >Step 1. You must design your screen(s) first. These must be submitted
> >separately in jpg format. You can email them to me and I will
…[6 more quoted lines elided]…
> left for LAST in the design phase.


TONY SAYS-Sorry but I must strongly disagree. Presumably, in the
real world, the application would be developed for a user who
should OK the design before programming begins. Therefore, the
screen should be designed first. This establishes what the program
will do, how many data fields are required, editing criteria, etc.
The user must gaze upon it and bless it before going to the next step.
For sure doing it the other way, would probably require modifications
to stuff you had already done because you assumed things before the
user saw what he was going to get.


> Jimmy uses "FLAT" files to mean indexed and sequential - or at least I
> think he does!  He just means non database.  Again, I don't really
> think this matters - it will be isolated from the system and it too
> can be left for near the end of the design phase.
>


TONY SAYS-Sorry, I thought a flat file was a sort of plain sequential
thing.

>
> OK by me.  I agree with Ken though - we do not need a contest.
> Watching the OO develop will be interesting enough!  But if you want
> to "compete" I can't see anything preventing us all from learning
> something from the process.


TONY SAYS-This became a different sort of contest because of a private
email I received. The email suggested that others approach the problem
using various methods, including a structured approach. I think that
makes it more interesting because anybody who is so inclined can
make a contribution. We can have a spaghetti version, a structured
version, an OO version, a whatever version.

 >
> PS - if this never comes to pass, no one is to blame.  Life happens.
>
TONY SAYS-Amen.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CAFD96.5C3058B2@home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> Hi:
…[4 more quoted lines elided]…
> 
AND JIMMY SAYS - Piss on it. I'm no longer interested !
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 5)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VYEy4.3937$Hq3.158889@news2.rdc1.on.home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com>`

```

"Foodman" <foodman123@aol.com> wrote in message
news:8aeja6$uko$1@nnrp1.deja.com...
> Hi:
>
…[15 more quoted lines elided]…
> of converting from 16 to 32 bit, why?

You obviously haven't tried to run a 16-bit windows application on NT or
Win2000 or you wouldn't be making such a bold statement. I really want to
see your 16-bit application run on an other-than-Intel Windoes platform like
an Alpha or MIPS processor. Does the application have to run on Windows CE?

P.S. I think your idea of contest is a thinly disguised homework assignment.
Do your own homework! ;-)
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ag3u8$u52$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com> <VYEy4.3937$Hq3.158889@news2.rdc1.on.home.com>`

```
In article <VYEy4.3937$Hq3.158889@news2.rdc1.on.home.com>,
  "Oscar T. Grouch" <dustbin@home.com> wrote:
>
> "Foodman" <foodman123@aol.com> wrote in message
> news:8aeja6$uko$1@nnrp1.deja.com...
> You obviously haven't tried to run a 16-bit windows application on NT
or
> Win2000 or you wouldn't be making such a bold statement. I really
want to
> see your 16-bit application run on an other-than-Intel Windoes
platform like
> an Alpha or MIPS processor. Does the application have to run on
Windows CE?


TONY SAYS-This is, of course, purely a compiler issue. Given the
compiler, it will run on anything. My stuff will only run on all the
Windows flavors, including NT. (I have no experience and no knowledge,
nor the desire to acquire any, of NT.) I am a COBOL programmer and
don't want to know, nor should I have to know, all this other STUFF!
It just isn't necessary. I never tried to see if my stuff will run
on CE not having a CE gadget.

>
> P.S. I think your idea of contest is a thinly disguised homework
assignment.
> Do your own homework! ;-)

TONY SAYS-How did you guess?

Thanks


>
>
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CB6C2B.20B3E225@zip.com.au>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> TONY SAYS-Sorry but I must strongly disagree. Presumably, in the
…[7 more quoted lines elided]…
> things before the user saw what he was going to get.

Then you have lost the analysis battle before you have begun.

Before you do anything you work out what needs to be done.  Designing
the screen is a fairly low level process, it immediately supposes that
you know what you are doing, for example:

In our application we can have:   clients that have multiple projects,
that in turn have multiple tasks, that in turn have multiple types of
work.  Do I design my screen with all four fields in it?  Do I ask my
user 'Do these tasks have unique identifiers?' first.  Oops I made a
mistake, I don't even know that the four tiered structure is real or
my imagination on the task at hand.

The starting point is deciding what we want to achieve.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ag4la$ugi$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com> <38CB6C2B.20B3E225@zip.com.au>`

```
In article <38CB6C2B.20B3E225@zip.com.au>,
  Ken Foskey <waratah@zip.com.au> wrote:

> Then you have lost the analysis battle before you have begun.
>
> Before you do anything you work out what needs to be done.  Designing
> the screen is a fairly low level process, it immediately supposes that
> you know what you are doing, for example:

TONY SAYS-But I do know what I am doing! Don't you? <g>
>
> In our application we can have:   clients that have multiple projects,
…[6 more quoted lines elided]…
> The starting point is deciding what we want to achieve.


TONY SAYS-It's amazing how these threads change direction.
I am talking about designing NEW systems. Working with old
stuff can be different.

Any new system must start at the data-entry level. (If your data
exists, then you don't need data-entry screens.)

In the case of the Time-Clock, nothing exists. We are designing
a simple data-entry system. We are going to decide what items of
information are required and depict them on a screen so the user
can bless it.  You could design the file first if you wanted to
but in this case it isn't necessary.

Surely, every data processing system in the world starts somewhere
at the data-entry level, no?

What would your VERY first step be, Ken?

(This seems to be a sensitive issue since it has been criticized more
than once and is worthy of a thread of its own.

Thanks


> Thanks
> Ken Foskey
> http://www.zipworld.com.au/~waratah/
>
```

###### ↳ ↳ ↳ Analysis techniques

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CCDF0B.30FCA7E2@zip.com.au>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com> <38CB6C2B.20B3E225@zip.com.au> <8ag4la$ugi$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> TONY SAYS-It's amazing how these threads change direction.
…[18 more quoted lines elided]…
> than once and is worthy of a thread of its own.

There are fundamentally three ways to analyse a new function:

1.  What data do we have (data driven as you described)
2.  What do you want to do (functionality driven)
3.  what are there and what do they do (Object oriented)

There is nothing intrinsically wrong with your approach, I just
sparked on 'define files first'.  Even in data driven approach you
would do a relationship design first and then flesh it in.  With this
sort of application you may compress this by 'doing it in your mind'
on more complex designs this is not possible.  I also want to be very
clear to the young hot shots that read this that this is not the
typical way to go about designing a system. (Careful the children
might hear you sort of thing).

OK:  My approach

My first step is TOTALLY reusable on ALL design methodologies called
use cases.  Developed for OO but there is nothing OO in them, they are
an excellent way to present information to the customer at a high
level level.  Examples for this project follow:

Use case:  Enter Time sheet

Actors:  Users - people who record time sheets.

Pre conditions:  User must be 'logged on' to the system

Description:
- The user selects a person to enter time entries against
- Selects data of entry
- records time in against various tasks within many projects.
- stores data on permanent record for later retrieval

Exceptions:
- User not authorized to update another user's time.  Selection of
  person is skipped and they are automatically selected.

Post conditions:  Data is stored for later retrieval

Use Case:  Create project

Actors:  Project managers

Preconditions:  User must be logged onto system

Description:
- User defines name for new project
- completes description, expected beginning and ending date, ...
- records data onto permanent store for later retrieval

Exceptions:  N/A

Post conditions:  Project is defined for the rest of the system.

Use case:  Retrieve data

Actors:  Accountant, project managers, CEO.

Preconditions:  User is logged onto system and is authorized for
		download.
Description:
- User selects either client, project, user of task to extract.
- select date range of extract
- selects fields to extract and output format.
- selects output filename and directory

Exceptions:
- No date range is selected, use a default of 01/01/1999 to very large
date.
- User not authorized for client, project or user data.  Extraction is
terminated with a security message.

Post conditions:  File is created on disk for later use.

Use case:  Time clock ....
Use case:  Define / change employee details...
Use case:  Define task category...

To the user of the product  - presumably Thane - you mentioned
invoicing, what do you really mean by this.  What other functions do
you perceive the system should have.  Is there anyone else affected by
this system (actors).  Do you agree with the use case provided.

.....

This is the basic approach,  describe the obvious functions and find
out what is missing.  Tidy it up and do it again.  This can really be
done quickly with the user sitting with you working out who is
affected.  On very large systems it will obviously take a long time.

The thing I instantly liked with this approach is:
1.  It is not OO specific
2.  It is in English with some structure
3.  The exceptions are buggers to handle in paragraphs

For exceptions have you every tried to write a spec where there are so
many if's but's and maybes that the description ends up unreadable. 
This template solves that very simply by writing the standard rule and
then the exceptions.

The level of detail may seem over kill, but working out what the user
really wants and what the user needs is really tricky stuff, they are
often not equal.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/

PS:  p.l.e.a.s.e. Drop the Tony says bit.
```

###### ↳ ↳ ↳ Re: Analysis techniques

_(reply depth: 8)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ait8q$q7q$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com> <38CB6C2B.20B3E225@zip.com.au> <8ag4la$ugi$1@nnrp1.deja.com> <38CCDF0B.30FCA7E2@zip.com.au>`

```
In article <38CCDF0B.30FCA7E2@zip.com.au>,
  Ken Foskey <waratah@zip.com.au> wrote:
> Foodman wrote:

Hi:

OK, I will drop TONY SAYS.  The reason I did it is because I find
it a bit hard to figure out who is saying what when responses are
intermingled with the thing being replied to and assumed others have
that problem to - heck I can't even follow my own responses!.

Anyway, thanks for your voluminous response.

I don't know how to respond. It is obviously a highly formalized
approach to doing something and could be of value in large projects.
In our case, it seems like extra work.

However, I hope you enter the contest and include this sort of thing
along with your source code.

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Analysis techniques

_(reply depth: 9)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE2D01.1BB348E2@zip.com.au>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com> <38CB6C2B.20B3E225@zip.com.au> <8ag4la$ugi$1@nnrp1.deja.com> <38CCDF0B.30FCA7E2@zip.com.au> <8ait8q$q7q$1@nnrp1.deja.com>`

```
Foodman wrote:

> I don't know how to respond. It is obviously a highly formalized
> approach to doing something and could be of value in large projects.
> In our case, it seems like extra work.

There is a break between the chaos and structure that the real world
lives.  Learn the formal approach and then cull it down, don't throw
the baby out with the bath water.

A simple time sheet system would typically take about a week to
define, and implement.  Such a detail analysis is probably a waste. 
For an educational example, it is worth while.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Analysis techniques

_(reply depth: 10)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE4861.68FD2BA2@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com> <38CB6C2B.20B3E225@zip.com.au> <8ag4la$ugi$1@nnrp1.deja.com> <38CCDF0B.30FCA7E2@zip.com.au> <8ait8q$q7q$1@nnrp1.deja.com> <38CE2D01.1BB348E2@zip.com.au>`

```
Ken Foskey wrote:
> 
> Foodman wrote:
…[11 more quoted lines elided]…
> For an educational example, it is worth while.

I did such analyses to get my masters, but haven't yet (in the year
since) been in a situation where OO analysis was appropriate for my job.

Certainly when I get beyond analysis to actual coding, our needs haven't
warranted changing from standard structured coding.  In fact, I would be
delighted if I could enforce structured coding - but since our vendors
haven't gotten past early 1980's style coding stuck over an older
(obviously VSAM based) design, most maintenance wouldn't be over good
code anyway.
```

###### ↳ ↳ ↳ Re: Analysis techniques

_(reply depth: 10)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<401tcsgjrhi6v11l50117nmn42q20qidbu@4ax.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com> <38CB6C2B.20B3E225@zip.com.au> <8ag4la$ugi$1@nnrp1.deja.com> <38CCDF0B.30FCA7E2@zip.com.au> <8ait8q$q7q$1@nnrp1.deja.com> <38CE2D01.1BB348E2@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

>A simple time sheet system would typically take about a week to
>define, and implement.  Such a detail analysis is probably a waste. 
>For an educational example, it is worth while.

hmm. let me think.

write punchin, punchout
seek on intials
	edit and rewrite
add employee, verify state
fire employee
report hours by employee

all using gui. yea, i guess a week is a good estimate.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CCFDD0.83B3BE88@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38cab3a2.237687047@news.cox-internet.com> <8aeja6$uko$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> > This is my main objection.  The WHOLE point to OO is code re-use.
…[7 more quoted lines elided]…
> easily reusable.

Then both cases should document which code is new and which is reused. 
Then we can judge how difficult it was to find, integrate, & use
existing code in this exercise.  (that's a better word than "contest").
```

###### ↳ ↳ ↳ Re: An OO Contest!

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CABC0F.EC23A09E@home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> Hi:
…[13 more quoted lines elided]…
> 
Again SORRY - I am opting out based on your rules - I didn't say the
tool was lacking features - I am. I have no knowledge of NT etc.
nor do I have access to the stuff you want to kick. Just my humble
desktop.

> SORRY-This has to be a real-world thing.  It must be multi-user.

And again decline for the same reason.
 
> SORRY- The contestant must design their own file. Remember, the
> essence of system-design is file-design.

Please don't remind me about systems design. I was into that area 50
years ago, long before these kompooters were available. To quote an old
RAF saying, "I was in Baghdad before you were in Dad's bag !".

Seems to me you've missed the boat here. Consider what you are saying.
This started off as a comparison of programming technique using
different flavours of one language - COBOL. It has nothing to do with
how you perceive what a system should look like or what I think it
should look like. The purpose surely, was not to test analytical skills
but programming methodology.

Similarly why introduce screen 'gimmicks' if one so feels - are you
trying to test my coding skills ? I'll concede that point to you right
now, if it will make you happy - but if you want to talk about SYSTEMS
designing a large application - then I'll meet you right head-on - and
I'll be there with you or CONSIDERABLY BETTER than you - so there's a
real brag ! (The difference being, I suspect, my interest is system
design, and I consider the programming an adjunct to the design).

You want fifteen different flavours of tackling the same problem -
interesting in its own way but doesn't fit your original title 'OO
contest' - we are unable to compare apples with apples.

As I say - count me out. By no means defeated - just can't meet your
refined definition of the rules - and be buggered if I'm going to run
out and spend money, (which I can ill afford), on additional/necessary
software/hardware to theoretically make a point - when all in all you
probably don't buy into OO and have the mindset 'everybody should be
using SP2' - no reflection on SP2 Bob - as originally stated it would
have been an interesting comparison.

Jimmy
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ag5am$utc$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CABC0F.EC23A09E@home.com>`

```
In article <38CABC0F.EC23A09E@home.com>,
  "James J. Gavan" <jjgavan@home.com> wrote:
>
>
…[4 more quoted lines elided]…
> > - (S1) - The only thing I know, and have access to, is Windows 98 -
so
> > that's the only flavour I am going to address.
> >
…[9 more quoted lines elided]…
> desktop.



TONY SAYS-I do not believe that a COBOL programmer should need to
know anything about NT. I don't and my stuff runs just fine on NT.
What does one need to know about it to write a COBOL program?


>
> > SORRY-This has to be a real-world thing.  It must be multi-user.

> And again decline for the same reason.

TONY SAYS-???


> You want fifteen different flavours of tackling the same problem -
> interesting in its own way but doesn't fit your original title 'OO
> contest' - we are unable to compare apples with apples.

TONY SAYS-Jimmy, you were the one who made the suggestions to get
people to contest using other methods. I think that is a good idea
and I would like to see all various proponents make an entry.

By the way, I do plug SP2 all the time because I like it. This
does not, by any stretch of the imagination mean that is perfect
and the only product of its type. With COBOL and SP2 I can do
just about anything I want.


Thanks.
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 4)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38cd2a98.16072324@news.epix.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CABC0F.EC23A09E@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote:

Jimmy:

[snip all before] - no reflection on SP2 Bob - [snip all after]

I completely understand what you are saying and have no problem with
it whatsoever.  This is indeed an interesting thread!  I am staying
completely out of this one and will continue to lurk in the background
unless someone has a question for me.





Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: An OO Contest!

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aee6l$1vo$1@news.cerf.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com>`

```
"Foodman" <foodman123@aol.com> wrote in message
news:8aea42$ol2$1@nnrp1.deja.com...
> SORRY-If you are using a development system which restricts you to
> Windows 98 then there is something wrong.  I will use MF COBOL

When Jimmy says he only have a computer with Win98, that is not the same as
saying that the product is not portable.

> - (S2) - we are talking single thread and I am not into multi-user
>
> SORRY-This has to be a real-world thing.  It must be multi-user.

I guess you guys are misunderstanding each other? Multi thread and multi
user is two different things...

> I will organize it if everyone agrees.

You have my vote.

> If the RM antique is all you have, then you should not compete. Get
> the Fujitsu free compiler.

Objection. Cobol is Cobol, I see no reason why we should refuse RM 1980, if
anyone solving the task, feel they can do it with RM 1980.

> Here are some more rules.

May I ask you to make one complete final listing of the specifications and
the rules, so it won't be necessary to jump back and forth?

> TIME-LINE - because of our various commitments, maybe we should target
> for late June for the finished goods ?

Seconded.

> Let's not have a time-line, there is too much chocolate to eat.


If so, how would we know to draw a line?

Cheesle
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ag5s2$v8k$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <8aee6l$1vo$1@news.cerf.net>`

```
In article <8aee6l$1vo$1@news.cerf.net>,
  "Cheesle" <cheesle@online.NoSpamPlease.no> wrote:

> I guess you guys are misunderstanding each other? Multi thread and
multi user is two different things...



TONY SAYS-As a COBOL programmer, I don't think I should need to know
what multi-thread is. I DO need to know and understand multi-user
file and record-locking stuff. I have a dim idea of what multi-thread
is but look upon it as an operating consideration.


> > If the RM antique is all you have, then you should not compete. Get
> > the Fujitsu free compiler.
>
> Objection. Cobol is Cobol, I see no reason why we should refuse RM
1980, if
> anyone solving the task, feel they can do it with RM 1980.
>

TONY SAYS- I agree COBOL is COBOL. But the impression I got from
Jimmy was that his compiler was dysfunctional. Even if you didn't
have ISAM, you could figure out a way to do it.


> > Here are some more rules.
>
> May I ask you to make one complete final listing of the
specifications and
> the rules, so it won't be necessary to jump back and forth?
>

TONY SAYS-See new subject to be posted shortly.



Thanks
```

###### ↳ ↳ ↳ Re: An OO Contest!

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com>`

```
On Sat, 11 Mar 2000 20:25:41 GMT, Foodman <foodman123@aol.com>
enlightened us:

>Hi:
>
…[60 more quoted lines elided]…
>

Okay I'm on eo fthose mainframers Jimmy doesn't want, but I have to
comment on the above edit criteria.  Tony, you've got people from
outside of the US participating in this little contest, therefore you
need to expand ssn to include either tax id or citizen id, whatever
the country of the particular coder has.  Secondly not every country
has states, so this needs to either be dropped or changed to country
code.  Again zip code is US specific.  It should be Postal Code which
would cover the US and most other countries.  The length needs to be
variable as well.

Okay I'm done.  I shall now return control to you Pee Cee er's.


>	(ii) You give us a jpg file or whatever, with a snapshot of
>	     your screens - then we can all try building the same
…[78 more quoted lines elided]…
>Before you buy.

          ////
         (o o)
-oOO--(_)--OOo-

Only in America... do we use the word "politics" to
describe the process so well: "Poli" in Latin meaning
"many" and "tics" meaning "blood-sucking creatures"... 




Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8agp0q$c1t$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net>`

```
In article
<1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net>,
  SkippyPB <swiegand@neo.rr.com.nospam> wrote:
> On Sat, 11 Mar 2000 20:25:41 GMT, Foodman <foodman123@aol.com>
> enlightened us:
…[11 more quoted lines elided]…
> Okay I'm done.  I shall now return control to you Pee Cee er's.


TONY SAYS-OK, aliens can substitute the postal code etc., or whatever
they use in their lands. Stateless lands can drop the state.

thanks


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38cd4a03.407280830@news.cox-internet.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net> <8agp0q$c1t$1@nnrp1.deja.com>`

```
On Sun, 12 Mar 2000 18:52:12 GMT, Foodman <foodman123@aol.com> wrote:


>
>TONY SAYS-OK, aliens can substitute the postal code etc., or whatever
>they use in their lands. Stateless lands can drop the state.
>

Whew - that's a relief.  Glad I'm in Texas, now I don't have to invent
a state validator!
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD00A6.EE8D78A4@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net> <8agp0q$c1t$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> TONY SAYS-OK, aliens can substitute the postal code etc., or whatever
> they use in their lands. Stateless lands can drop the state.

I had a job where we needed to do lots of address cleansing.  Part of
the effort checked postal code to country.   This is a small world and
is getting smaller.

Maybe a better test would be to first design for your particular country
- then show how hard it would be for your methodology to expand various
name and address fields to accept world standards.

To do this, it may be good to start off requiring Mr. Mrs. or Miss, a
fixed length postal code, and last name, first name, middle initial -
anything overly restrictive would work well.  Don't have a place for
country on your screen, and make the screen's postal code exactly the
"right" size.

Then you adjust to changing conditions after you have a working program
- maybe cursing the original specs for being short sighted.
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ajc9t$6d9$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net> <8agp0q$c1t$1@nnrp1.deja.com> <38CD00A6.EE8D78A4@cusys.edu>`

```
In article <38CD00A6.EE8D78A4@cusys.edu>,

> I had a job where we needed to do lots of address cleansing.  Part of
> the effort checked postal code to country.   This is a small world and
> is getting smaller.
>
> Maybe a better test would be to first design for your particular
country
> - then show how hard it would be for your methodology to expand
various
> name and address fields to accept world standards.


I think that contestants (if there are any) should design for
their own country.  If they want to add a couple of fields which
we don't care about it doesn't matter.

Thanks

Tony DIlworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 7)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD3694.31C3EC37@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net> <8agp0q$c1t$1@nnrp1.deja.com> <38CD00A6.EE8D78A4@cusys.edu> <8ajc9t$6d9$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <38CD00A6.EE8D78A4@cusys.edu>,
…[13 more quoted lines elided]…
> we don't care about it doesn't matter.

Fine as far as design goes - I really would like to see this exercise
expanded into a bit of maintenance.
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38cd4a84.407409995@news.cox-internet.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net> <8agp0q$c1t$1@nnrp1.deja.com> <38CD00A6.EE8D78A4@cusys.edu> <8ajc9t$6d9$1@nnrp1.deja.com> <38CD3694.31C3EC37@cusys.edu>`

```
On Mon, 13 Mar 2000 11:42:28 -0700, Howard Brazee
<howard.brazee@cusys.edu> wrote:

>Fine as far as design goes - I really would like to see this exercise
>expanded into a bit of maintenance.

Me too.  My MAIN concern with OO is - is the code maintainable.  Does
it require a different method of maint?
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 8)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ajlao$dni$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net> <8agp0q$c1t$1@nnrp1.deja.com> <38CD00A6.EE8D78A4@cusys.edu> <8ajc9t$6d9$1@nnrp1.deja.com> <38CD3694.31C3EC37@cusys.edu>`

```
In article <38CD3694.31C3EC37@cusys.edu>,>
> Fine as far as design goes - I really would like to see this exercise
> expanded into a bit of maintenance.
>


The rules state that you have to be able change and delete records
in the employee file, is that not 'maintenance'?

Thanks

TOny DIlworth
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 9)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD63A5.5EBC7C8C@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net> <8agp0q$c1t$1@nnrp1.deja.com> <38CD00A6.EE8D78A4@cusys.edu> <8ajc9t$6d9$1@nnrp1.deja.com> <38CD3694.31C3EC37@cusys.edu> <8ajlao$dni$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <38CD3694.31C3EC37@cusys.edu>,>
…[9 more quoted lines elided]…
> TOny DIlworth

That's data maintenance, I want to see programming maintenance.  A
program is designed for one purpose and the requirements have been
changed in unanticipated ways.  You know, what most programmers work
at.  (changing other programmer's work)

It is easy to write a program either way (if you know how) - I want to
test how hard it is to live with it after it has been written.
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD6444.4A439775@home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <1ED190A27EDC7BFC.78EA15E7270989ED.0C1AF2C2F104DDFA@lp.airnews.net> <8agp0q$c1t$1@nnrp1.deja.com> <38CD00A6.EE8D78A4@cusys.edu> <8ajc9t$6d9$1@nnrp1.deja.com> <38CD3694.31C3EC37@cusys.edu> <8ajlao$dni$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <38CD3694.31C3EC37@cusys.edu>,>
…[6 more quoted lines elided]…
> 

Boy! You really are NOT on the same wave length as Howard with this one
are you ? Perhaps he will elucidate.

Jimmy
```

###### ↳ ↳ ↳ ISAM????

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CCFBDA.6D2C09D5@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> Step 2. Will be file design. It must be multi-key ISAM or something
…[3 more quoted lines elided]…
> why one would want to.

Interesting.  From my perspective I have been assuming that ISAM is
dying, being replaced by databases.  If not, how can the COBOL committee
possibly turn down a proposal to READ PREVIOUS?
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 4)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ED7z4.14957$Hq3.295565@news2.rdc1.on.home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu>`

```

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:38CCFBDA.6D2C09D5@cusys.edu...
> Foodman wrote:
> >
…[8 more quoted lines elided]…
> possibly turn down a proposal to READ PREVIOUS?

Standards vary. READ PREVIOUS cannot be supported on a number of platforms
because the native file system does not implement a doubly-linked list. The
closest approximation on these platforms is to define an alternate key which
is the inverse of the primary key based on collating sequence. IMHO, it
seems a bit unfair to demand that compiler writers implement a feature that
is not supported by the OS, which is what placing it in the standard would
do. It would be just as fair to demand that all compilers provide native
support for the hierarchical file system that exists in Data General
machines, or the circular queues that are part of the HP 3000 native file
system.
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 5)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yacz4.7569$7L.525780@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <ED7z4.14957$Hq3.295565@news2.rdc1.on.home.com>`

```

"Oscar T. Grouch" <dustbin@home.com> wrote in message
news:ED7z4.14957$Hq3.295565@news2.rdc1.on.home.com...
>
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
…[6 more quoted lines elided]…
> > > I suppose it is OK to use something other than ISAM, but I would
wonder
> > > why one would want to.
> >
> > Interesting.  From my perspective I have been assuming that ISAM is
> > dying, being replaced by databases.  If not, how can the COBOL
committee
> > possibly turn down a proposal to READ PREVIOUS?
>
> Standards vary. READ PREVIOUS cannot be supported on a number of
platforms
> because the native file system does not implement a doubly-linked list.
The
> closest approximation on these platforms is to define an alternate key
which
> is the inverse of the primary key based on collating sequence. IMHO, it
> seems a bit unfair to demand that compiler writers implement a feature
that
> is not supported by the OS, which is what placing it in the standard
would
> do. It would be just as fair to demand that all compilers provide native
> support for the hierarchical file system that exists in Data General
> machines, or the circular queues that are part of the HP 3000 native file
> system.
>

Very interesting.  Has anyone ever thought about why these different
"methods" were "invented" to begin with?

Some might say that by doing it a new way the results would be harder to
convert to some other system.  I know I've had that thought from time to
time.

Others might say, our computer design is better, and doing things the way
we do takes advantage of the system's features to make it more competitive.

I say (after reading about OO here for some time)
Engineering a computer requires a lot of input including that from the
SALES department. Even then unless watched closely, engineering people like
to invent.  This invention may or may not backfire.  In the best cases, it
causes everyone to adopt the new techniques or methods or hardware design.

Consequently, I believe "problem solvers" who use computers to solve them
SHOULD tell the engineers what they want, and let the engineers figure out
how to do it.  I don't believe ISAM and VSAM and Indexed Sequential have
any propriotary basis, but if they do, they belong in the public domain.

Warren Simmons
w.g.simmons@worldnet.att.net
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ajnqv$8j1$1@slb2.atl.mindspring.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <ED7z4.14957$Hq3.295565@news2.rdc1.on.home.com>`

```
Both READ PREVIOUS and START LESS THAN are in the draft of the next Standard
already.  They are, however, in the processor dependent list - which means
that they probably will NOT appear in any environment where the ISAM file
structure would make them "difficult".
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD25C7.5B7F2D44@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <ED7z4.14957$Hq3.295565@news2.rdc1.on.home.com>`

```


"Oscar T. Grouch" wrote:
> 
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
…[22 more quoted lines elided]…
> system.

I see where you're coming from when PC compilers have to overcome lacks
in their operating system(s).  But a feature could be added which
returns a run-time error when a command is attempted against a file
which won't support that command.  Kind of like opening a printer for
input...
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ajd2f$6vb$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu>`

```
In article <38CCFBDA.6D2C09D5@cusys.edu>,


> Interesting.  From my perspective I have been assuming that ISAM is
> dying, being replaced by databases.  If not, how can the COBOL
committee
> possibly turn down a proposal to READ PREVIOUS?
>



It is apparent to me that ISAM is despised by the compiler/software
manufacturers. It is not in their interest to have compatible
file methods. We have to remember that all compiler/software
enterprises are money-making organizations with profit as
the key motive. People invent things like Oracle because they
believe it to be better than someone elses stuff and they want
to have yachts and Bentleys like Larry Ellison.


I dimly recall that IBM's first COBOL had a single-key ISAM,
which, for all practical purposes, made ISAM useless. There
interest, of course, was in selling CICS to their customers
and to be sure that software developed by IBM worked only on
IBM machines to prevent their customers going to, for example,
(if you go back that far) RCA's Spectra 70. Remember the PS/2?

I have asked the following question on more than one
occasion and I don't think that anyone has given me a good
answer.

Question:  What can Oracle or whatever do that Multi-key ISAM
cannot do? (And I don't mean something useless like reading
every third record backwards.)

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 5)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gjbz4.15339$Hq3.301810@news2.rdc1.on.home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com>`

```

"Foodman" <foodman123@aol.com> wrote in message
news:8ajd2f$6vb$1@nnrp1.deja.com...
> In article <38CCFBDA.6D2C09D5@cusys.edu>,
>
…[39 more quoted lines elided]…
> Before you buy.

Once again a loaded question from Tony. If you're too stubborn to accept any
of the previous arguments concerning relational databases, then you won't
accept this one either.

---- begin futile argument ---

Okay, so there's nothing you can do in a relational database that cannot be
done in with ISAM and lots of COBOL code. Similarily there's nothing that
COBOL does that cannot be done with assembler instructions, but it doesn't
mean I would prefer doing the work in assembler.

Coding ISAM I/O in COBOL moves database navigation and database integrity
into application code, increasing the work, the coding effort, the amount of
duplicate code needed in a system, and the risk of errors that show up at 2
a.m..

Here are some examples where a relational database does the job more
readiliy:

1) If I want to build up a list of all customers who ordered a particular
part on a particular day using a particular credit card, it might take
dozens READ statements to do the work of a single SELECT.

2) If I were building an order entry system it would take a whole lot of
deletes to get rid of the header and all the associated detail lines. With a
relational database it's a single DELETE; referential integrity is left to
the database.

3) If I want to add a customer address (U.S.) and the postal code isn't
valid, then the foreign key relationship between the POSTALCODE field and
the list of valid postal codes in postal code table will prevent the record
from being added when the state is not valid; without writing a single line
of code.

4) Suppose I want to change my data model by adding a column to a table
('field to a file record'). With a relational database I add the column, and
the job is done. Any program that needs to work with that new column can.
Any existing programs that don't care stay untouched. With ISAM I have to
change the copybook and recompile every program that accesses the file,
whether or not they care about the new column.

5) Suppose I want to find the latest sales order for a particular
customer... the SQL query would be a single 'SELECT MAX' statement. If I'm
lucky and READ PREVIOUS is supported I might be able to get at this record
with a START and READ PREVIOUS, assuming my keys were defined correctly.
Otherwise, I have to figure out the most efficient way to get at that sales
order by coding my own database navigation. No thanks.

--- end futile argument ---

Karl Wagner
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD4F30.4B69EEEB@home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <Gjbz4.15339$Hq3.301810@news2.rdc1.on.home.com>`

```


"Oscar T. Grouch" wrote:
> 
> "Foodman" <foodman123@aol.com> wrote in message
…[44 more quoted lines elided]…
> --- end futile argument ---

Good ! That is not a futile argument. That is the first time I've seen
somebody spell it out succinctly. As the line goes from My Fair Lady "By
George (s)he's go it". Merci, je comprends.

But to be honest - on my applcation - which is very specialized, I'm not
sure the DB approach would give me any edge. But I do see clearly the
tremendous advatages in large applications.

As I said re this Newdgroup elsewhere, "Seek and you shall find".

Jimmy
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 7)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.133cb0731ac81369989987@news.mersinet.co.uk>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <Gjbz4.15339$Hq3.301810@news2.rdc1.on.home.com> <38CD4F30.4B69EEEB@home.com>`

```
I noticed that James J. Gavan as jjgavan@home.com said...
> 
> Good ! That is not a futile argument. That is the first time I've seen
…[5 more quoted lines elided]…
> tremendous advatages in large applications.

I'm ambivalent about RDBMS - they do have an advantage in some 
circumstances but a lot of my programming has been done with accounting 
systems and the necessity for any form of database management system is 
not particularly credibly argued for an application that is essentially a 
sequential process by its very nature.

The basic rules of accounting were established a few hundred years ago 
and the information derived is pretty much defined by statute in most 
countries, and mostly to the same standards and criteria.  A management 
accountant may want to run some odd queries occasionally but, by and 
large, information retrieval is just the same this month as it was last 
month and it's actually a lot easier for the application programs to 
maintain the data integrity than to hand off this responsibility to a 
database system, especially the likes of Oracle and other so-called RDBMS 
which aren't genuine full-on RDBMS if you go by Codd's concept.

The advantages of a RDBMS are in the flexibility of data retrieval that 
is offered and probably are out and out necessities in certain areas.  My 
own take on it is very much along the lines of the old argument here for 
COBOL being good at what it's designed for.

IME, accounting users aren't bothered about the flexibility offered by 
RDBMS and SQL because generally they don't need it.  This doesn't mean to 
say that a sales ordering system, for example, wouldn't feel the benefit 
for the purposes of, for example, extracting sales statistics.

One of the key concepts about SQL is that it is, in theory, a user tool 
but how many of us know users who can do SQL queries, who can be bothered 
to try to do them or who occasionally are allowed sufficient access 
authority to do them?
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ajl7b$dmj$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <Gjbz4.15339$Hq3.301810@news2.rdc1.on.home.com>`

```
In article <Gjbz4.15339$Hq3.301810@news2.rdc1.on.home.com>,
  "Oscar T. Grouch" <dustbin@home.com> wrote:
>
> Once again a loaded question from Tony. If you're too stubborn to
accept any
> of the previous arguments concerning relational databases, then you
won't
> accept this one either.

(I don't think my questions are LOADED, they are not intended to be.
but I am hard to convince.)




I must confess that I do not read every single post on every single
subject, so I might have missed something.

Your response, to my knowledge, is the first real one with real
answers about ISAM vs DBMS. Thank you. These are the sort of answers
I have been waiting for.


>
> ---- begin futile argument ---
…[4 more quoted lines elided]…
> 1) If I want to build up a list of all customers who ordered a
particular
> part on a particular day using a particular credit card, it might take
> dozens READ statements to do the work of a single SELECT.

The bottom line is that it all depends on how the files are designed.
If one had a key consisting of customer/date/credit card type then
one could start the file at the first one and read just the ones
you wanted to read, no?  My program would only have ONE read statement
executed for the number of records which existed.

>
> 2) If I were building an order entry system it would take a whole lot
of
> deletes to get rid of the header and all the associated detail lines.
With a
> relational database it's a single DELETE; referential integrity is
left to
> the database.


Sorry, I don't understand the business about deleting. It isn't
necessary to elaborate because what you mention is a system-design
issue.



>
> 3) If I want to add a customer address (U.S.) and the postal code
isn't
> valid, then the foreign key relationship between the POSTALCODE field
and
> the list of valid postal codes in postal code table will prevent the
record
> from being added when the state is not valid; without writing a
single line
> of code.


You do however have to create and maintain the postal code table.
If the postal code table was an ISAM file, all you would have to
do is stick the new code in (using a COBOL program for that purpose)
and have the same result you have. No code required.

>
> 4) Suppose I want to change my data model by adding a column to a
table
> ('field to a file record'). With a relational database I add the
column, and
> the job is done. Any program that needs to work with that new column
can.
> Any existing programs that don't care stay untouched. With ISAM I
have to
> change the copybook and recompile every program that accesses the
file,
> whether or not they care about the new column.
>

You have me on this one. However, I don't think recompiling is
such a big thing. One can write a little batch file to recompile
(at least, I can).  Obviously this requires file conversion too.
But is that so bad?  If you are talking about Gigantor files, it
may be problem but 90% of all files are not gigantor. The practicality
of this might depend upon the particular installation.

Also, because diskspace is cheap, files can be designed with
'filler' in both keys and data to allow insertion of new stuff
without recompiling, if deemed desirable.

Is the ADVANTAGE worth the OVERHEAD and cost of the DBMS?



> 5) Suppose I want to find the latest sales order for a particular
> customer... the SQL query would be a single 'SELECT MAX' statement.
If I'm
> lucky and READ PREVIOUS is supported I might be able to get at this
record
> with a START and READ PREVIOUS, assuming my keys were defined
correctly.
> Otherwise, I have to figure out the most efficient way to get at that
sales
> order by coding my own database navigation. No thanks.
>


Again, if the file is designed properly it would be just a start for
that customer. And, I don't need to know SQL.


I don't think that your arguments are futile, it is just that noone
has said anything which CONVERTS me. I don't think the overhead and
expense of DBMS is worth it, or, at least, no one has convinced me.


Thanks

TOny Dilworth

> --- end futile argument ---
>
> Karl Wagner
>
>
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 7)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE33AB.D906D6F@zip.com.au>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <Gjbz4.15339$Hq3.301810@news2.rdc1.on.home.com> <8ajl7b$dmj$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> In article <Gjbz4.15339$Hq3.301810@news2.rdc1.on.home.com>,
…[12 more quoted lines elided]…
> 

If you did not think of it before designing you table or this is a one
off requirement?  You would sequentially pass the file from beginning
to end.  Optimizations in the database allow it to only read certain
pages not the whole file if you 'key' appears on any index.

> >
> > 2) If I were building an order entry system it would take a whole
…[6 more quoted lines elided]…
> issue.

SQL:   delete from order where order-number = :ws-order-number

Cobol:

move ws-order-number to fd-order-lines-key
start key
Perform until key not matched
	delete order lines
	get next key
end-perform
delete order

The Cobol code is at least 7 times more difficult to maintain. 
Probably more when you flesh it out properly.  NOte I have not coded
error checking.  This is a coding error that can potentially have
catastrophic results, the SQL is correct as it stands.

> 
> > 3) If I want to add a customer address (U.S.) and the postal code
…[8 more quoted lines elided]…
> and have the same result you have. No code required.

SQL (no manual sorry if it is wrong):

insert into customer (:addr1, :Adsdr2, :addr3, :postcode, ...)
if sqlcode not = 0
	oops
end-if

Cobol:

read key equal postcode-file.
if not found
	....  do something ...
else
	insert ...
end-if

The problem with the Cobol is if you do not centralize you customer
insert (monolithic code is still the flavour of the day) then you
might forget somewhere and then you have garbage in your file.

Second what happens when you forgot a business rule.  With SQL you
define a new constraint and your whole system automatically enforces
it.  It can even check for integrity problems that have already
occurred so you can correct them.


> > 4) Suppose I want to change my data model by adding a column to a

Is the filler worth the overhead of not having the database. Just
being argumentative, fundamentally you are right.
> 
> > 5) Suppose I want to find the latest sales order for a particular

Snipped

One final addition and most important thing a DBMS supports is....

transactional processing.

IF you are processing an order for the warehouse.  You progress though
each order line subtracting the items from each product until on the
final line the program crashes.

With cobol you have a half processed update.  With the database the
updates are rolled back to the same values as they did before the
processing has started.  This is commonly extended to point in time
recovery where the DBMS logs can roll back a complete days work if
necessary.

You close a transaction by a commit.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD4C1A.7D2D30CD@home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <38CCFBDA.6D2C09D5@cusys.edu>,
…[4 more quoted lines elided]…
> every third record backwards.)

I'm with you on this one becuase I just don't know. Grrh! will say
Warren Simmons who was there at the start. What does any database give
me as pluses that we can't do with ISAMs. Not rejecting DBs - but tell
Tony and myself exactly what it is we are missing.

Jimmy
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 6)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#nXFxzSj$GA.255@cpmsnbbsa05>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <38CD4C1A.7D2D30CD@home.com>`

```
The best thing to do is go to a local book store or library, and browse
through the SQL books.
If they have "SQL for Smarties" by Joe Celko(?), see what's in it.
SQL is a very powerful tool.
It is a programming language in its own right.

Karl Wagner gave some of the benefits of Relation databases in his response.

James J. Gavan <jjgavan@home.com> wrote in message
news:38CD4C1A.7D2D30CD@home.com...
>
>
…[14 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD762E.3704D712@home.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <38CD4C1A.7D2D30CD@home.com> <#nXFxzSj$GA.255@cpmsnbbsa05>`

```


DennisHarley wrote:
> 
> The best thing to do is go to a local book store or library, and browse
…[5 more quoted lines elided]…
> Karl Wagner gave some of the benefits of Relation databases in his response.

Thanks for suggestion Dennis, but as you'll see I already buy into what
Karl has described.

Now you and me both, we don't want to spend endless hours browsing the
bookshelves, and these techhie books aint cheap ! So if one can get a
succinct description of what a topic is about, and it turns your crank,
then off to the bookstore for a look see.

Now want a brief description of OO - Hell ! Have you got a week to spare
? Ha ! Ha ! Says some smart ass. It aint no good, based on the fact you
can't describe the 'new philosophy' in a sentence. Now if you are
talking about some neat methodology gimmick with an incomprehensible
name, that they can easily assimilate - then they buy in.

OO COBOL- as Warren Simmons says "Where is it different from the
language we invented back in the 60s ?". It isn't; same animal with some
added gizmos. And it's your choice, (providing you've looked at it in at
least a little depth), as to whether or not you think it can be useful -
or categorize it in your mind as just a new gimmick. (Trouble is of
course, it has to be irrelevant if your current compiler doesn't support
OO - you can't study or run something in it).

Re : Bookstores. With big-box bookstores, (If anybody is in UK, I gather
you don't use the term - but think of something as big as "Toys R Us",
which I know you have) - COBOL coverage is basically down to Thane's
'Teach YC in 24 Hours', 'COBOL Unleashed" and 'COBOL for Dummies' - the
few remaining tomes were written for when you used a pick and shovel
with COBOL. And as for OO COBOL - Zilch !

Jimmy
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 8)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Obxpb2Yj$GA.250@cpmsnbbsa04>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <38CD4C1A.7D2D30CD@home.com> <#nXFxzSj$GA.255@cpmsnbbsa05> <38CD762E.3704D712@home.com>`

```

James J. Gavan <jjgavan@home.com> wrote in message
news:38CD762E.3704D712@home.com...
>
>
…[8 more quoted lines elided]…
> > Karl Wagner gave some of the benefits of Relation databases in his
response.
>
> Thanks for suggestion Dennis, but as you'll see I already buy into what
…[12 more quoted lines elided]…
>
SQL, the language of Relational Databases, fits into the same category as
OO.
I can scratch the surface, but to get a good feel for it you have to do some
research.

The problem is that in giving a solution to a particular problem, you will
have some who say "I don't need to do that, therefore I don't have a need
for SQL".

I don't know anyone who has used Relational technology who would make ISAM
or VSAM their access method of choice. I'm glad to see that Karl has sparked
your interest.

As for browsing the bookshelves, I don't mind. I sometimes meet women there.
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 7)_

- **From:** joe_celko@my-deja.com
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8amuja$pfe$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <38CD4C1A.7D2D30CD@home.com> <#nXFxzSj$GA.255@cpmsnbbsa05>`

```

>> The best thing to do is go to a local book store or library, and
browse through the SQL books. If they have SQL FOR SMARTIES by Joe
Celko, see what's in it. <<

I and mcy house payment agree with you on that <g>.  But I recommend
that you do not buy SQL FOR SMARTIES untilyou have worked with SQL for
a bout a year -- long enough to know the syntax, and to have gotten to
the point you are having real problems instead of beginner problems.

The way for a newbie to use SQL in a Cobol host program is to get
someone to write a query that give them a cursor that looks as if it
were a simple sequential file, with exactly the required data, already
sorted in the right order.  The host program can then be a preamble, a
WHILE loop over the cursor and a postamble most of the time.  And it
will be a few hundred lines shorter than the same program written with
a file system.

--CELKO--


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 6)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cDfz4.195$qN1.15868@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com> <38CD4C1A.7D2D30CD@home.com>`

```
Well Jimmy,

When we added DB to the file management features (or should I say we tried
to add it) our objective was to provide "network" data base structures.
Our input included IDS from GE/Honeywell; a system developed at the GM
Research Labs who were writing programs for the use of engineers who
designed autoparts, and other systems like the Bill Of Material Application
required.  We had input from the DIA  who keep all kinds of information not
related by table entry, and others.

As I understand it, RDB, or table organization files for fast query won out
because research showed that this could be done using math concepts whereas
with network data base concepts there is a need to keep lots of "pointers"
to next, previous, head, and perhaps other files.   I personally believe
there is room for fast answer organization for some group of applications,
but I don't think the Bill of Material and other application systems fit it
as well as Integrated Data Store did.

I think this "happening" resulted from two different ideas of what was
needed.  In general, IDS supports sharing of information for various
uses/departments/etc.  As in many computer related methods, a change in the
size and cost of direct access storage has had an influence in how things
are done.

Indexed Sequential no mater how many keys is not the same.  Certainly the
logic to find and update files differ.

All, IMHO.

Warren Simmons
w.g.simmons@worldnet.att.net

"James J. Gavan" <jjgavan@home.com> wrote in message
news:38CD4C1A.7D2D30CD@home.com...
>
>
…[14 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38cd4fcf.408765445@news.cox-internet.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <8ajd2f$6vb$1@nnrp1.deja.com>`

```
On Mon, 13 Mar 2000 18:46:41 GMT, Foodman <foodman123@aol.com> wrote:

>
>I have asked the following question on more than one
…[6 more quoted lines elided]…
>

I can add a row (field) to a table (record) without changeing a line
of source code or recompileing a single program.  In addition I don't
have to do to a data file conversion, and I can do it all while
systems are accessing/updating the data.
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 4)_

- **From:** "don ferrario" <don@ferrario.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_Lgz4.1087$Ys3.30886@nnrp1.ptd.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu>`

```
Howard,

if you want to do "read previous", just do the following

(assuming you have already read a particular record,
and want to go backwards from there)

start filename
   key = primary-key-name
   reverse
end-start
read filename next record


works exactly like a "read previous"
any subsequent "read next" statements will continue
in reverse order, until you do a random read, or another
"start" statement

don ferrario
http://www.ferrario.com



Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:38CCFBDA.6D2C09D5@cusys.edu...
> Foodman wrote:
> >
…[8 more quoted lines elided]…
> possibly turn down a proposal to READ PREVIOUS?
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 5)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CE4929.185A4ED2@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <_Lgz4.1087$Ys3.30886@nnrp1.ptd.net>`

```
With which version(s) of COBOL?  Will this be a standard?

don ferrario wrote:
> 
> Howard,
…[32 more quoted lines elided]…
> > possibly turn down a proposal to READ PREVIOUS?
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8alleb$p00$1@nntp9.atl.mindspring.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <_Lgz4.1087$Ys3.30886@nnrp1.ptd.net> <38CE4929.185A4ED2@cusys.edu>`

```
No,
  "reverse" is not/will not be "standard".

I have never seen it as an extension, so I am curious which implementation
supports it as well.

(As stated elsewhere START LESS THAN and READ PREVIOUS *will* be Standard -
and are already implemented in several implementations.)
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 6)_

- **From:** "don ferrario" <don@ferrario.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2QCz4.3107$Ys3.39942@nnrp1.ptd.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <_Lgz4.1087$Ys3.30886@nnrp1.ptd.net> <38CE4929.185A4ED2@cusys.edu>`

```
I use Fujitsu, for Windows 98/NT.  Don't know about other
implementations.  I assume it would work in other Fujitsu
environments.

I've seen it in several cobol instruction books.  I just assumed
it was "standard".  Are you saying that "START...REVERSE"
is not available in some implementations?

don ferrario


Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:38CE4929.185A4ED2@cusys.edu...
> With which version(s) of COBOL?  Will this be a standard?
>
…[22 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: ISAM????

_(reply depth: 7)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CF9C3E.F702B57B@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aea42$ol2$1@nnrp1.deja.com> <38CCFBDA.6D2C09D5@cusys.edu> <_Lgz4.1087$Ys3.30886@nnrp1.ptd.net> <38CE4929.185A4ED2@cusys.edu> <2QCz4.3107$Ys3.39942@nnrp1.ptd.net>`

```


don ferrario wrote:
> 
> I use Fujitsu, for Windows 98/NT.  Don't know about other
…[7 more quoted lines elided]…
> don ferrario

I haven't seen it in my various mainframe environments.
```

##### ↳ ↳ Re: An OO Contest!

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-03-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aedmv$1kj$1@news.cerf.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote in message
news:38CA8982.FC3A7234@home.com...
> - Cheesle - want to give it a shot using AcuCOBOL 'dual screen'

Do I have a choice? :-)
Let me see the final spec before I commit. As you point out yourself, it is
a matter of time.

Cheesle
```

###### ↳ ↳ ↳ Re: An OO Contest!

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ag606$vfs$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aedmv$1kj$1@news.cerf.net>`

```
In article <8aedmv$1kj$1@news.cerf.net>,
  "Cheesle" <cheesle@online.NoSpamPlease.no> wrote:
> "James J. Gavan" <jjgavan@home.com> wrote in message
> news:38CA8982.FC3A7234@home.com...


TONY SAYS-We don't want to impose time-limits. It can take months.
I agree that the contest should be open to all comers. If done
properly, it could prove to be quite educational.

Thanks.


> > - Cheesle - want to give it a shot using AcuCOBOL 'dual screen'
>
> Do I have a choice? :-)
> Let me see the final spec before I commit. As you point out yourself,
it is
> a matter of time.
>
> Cheesle
>
>
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 4)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ahmi1$dil$1@news.cerf.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aedmv$1kj$1@news.cerf.net> <8ag606$vfs$1@nnrp1.deja.com>`

```
"Foodman" <foodman123@aol.com> wrote in message
news:8ag606$vfs$1@nnrp1.deja.com...
> --
> what is a signature?

Is that a question?

Cheesle
```

###### ↳ ↳ ↳ Re: An OO Contest!

_(reply depth: 5)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ain1o$llt$1@nnrp1.deja.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com> <8aedmv$1kj$1@news.cerf.net> <8ag606$vfs$1@nnrp1.deja.com> <8ahmi1$dil$1@news.cerf.net>`

```
In article <8ahmi1$dil$1@news.cerf.net>,
  "Cheesle" <cheesle@online.NoSpamPlease.no> wrote:
> "Foodman" <foodman123@aol.com> wrote in message
> news:8ag606$vfs$1@nnrp1.deja.com...
…[7 more quoted lines elided]…
>

I suppose it is a reflection of the incompetence of whoever wrote
the deja thing.  The stupid 'What is a signature' bit appears
when you go to post, most people either don't see it or fail to
remove it. If I am making a new post, I remove it. If I reply
and the originator didn't remove it, I leave it there.

Thanks

TOny Dilworth
```

##### ↳ ↳ Re: An OO Contest!

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CCFA87.E21206D4@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CA8982.FC3A7234@home.com>`

```
"James J. Gavan" wrote:
> 
> - Howard - sorry you're out of the game - we aren't interested in you
> mainframers - No seriously, if you can produce something for a PC -
> might be another interesting comparison.

Agreed.  PCs seem to be the leading edge.  Too bad though, as it may be
a better test to see how well traditional, non-GUI programming needs fit
into OO.  (everybody claims that OO is not about GUI)

It could be that they fit in well enough if the programmers understand
OO, but not well enough to be cost effective to convert.  Maybe we need
GUIs and/or a tightly integrated system for the advantages of OO to be
cost effective.
```

#### ↳ Re: An OO Contest!

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9j1ocs0d0q2j80pd390um38unrg3rf4nnt@4ax.com>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com>`

```
Foodman <foodman123@aol.com> wrote:

>Perhaps it would help resolve the OO issue by having a contest.

a couple of questions:

a> how do you determine the winner?
code size, speed?
b>do you test for maintenance?
such as having two related files, and changing one.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

##### ↳ ↳ Re: An OO Contest!

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD00DD.FBACB31F@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <9j1ocs0d0q2j80pd390um38unrg3rf4nnt@4ax.com>`

```
G Moore wrote:
> 
> a> how do you determine the winner?
> code size, speed?

Anybody who learns from this exercise wins.
```

#### ↳ Re: An OO Contest!

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CA5A35.783C20CE@zip.com.au>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> Perhaps it would help resolve the OO issue by having a contest.

I personally would politely decline.

I want to use this as an open development to show how the process is
built up for a start.  Competition would cause too much confusion,
what I might do for a competition would not be good for explaining the
concepts.

Second I personally do not have time to take on any more challenges. 
Work, University and wife and three kids are competing enough as it
is.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: An OO Contest!

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CCF8BC.4BB14DF0@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> Hi:                                                    3/11/00
…[4 more quoted lines elided]…
> presenting its evolution to the throng.

That might be fun, interesting, and educational, but it won't resolve
any OO issues of mine.  My issues are all related to OO as an enterprise
standard, specifically in regards to maintenance, but also about actual
rates of reuse, testing difficulties, and labor issues.

But I have a question:   What is an OO program?  

Also:
Do people write stand alone OO programs without being part of an OO
environment?
```

##### ↳ ↳ Re: An OO Contest!

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aj390$pia$1@news.cerf.net>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CCF8BC.4BB14DF0@cusys.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:38CCF8BC.4BB14DF0@cusys.edu...
> Do people write stand alone OO programs without being part of an OO
> environment?

What do you think of by saying OO environment?

Cheesle
```

###### ↳ ↳ ↳ Re: An OO Contest!

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38CD21F2.B00A2C00@cusys.edu>`
- **References:** `<8adj2h$97n$1@nnrp1.deja.com> <38CCF8BC.4BB14DF0@cusys.edu> <8aj390$pia$1@news.cerf.net>`

```
Cheesle wrote:
> 
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
…[6 more quoted lines elided]…
> Cheesle

Where objects are used in many programs which fit into a system which
has at least partially integrated design.  You might have some business
rules or standards or interfaces designed as objects which are used as
needed by individual programs.  

From the outside, this looks like the selling point of OO.  An isolated
program is easy enough to write and maintain the old way.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
