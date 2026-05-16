[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL intrinsic functions

_10 messages · 4 participants · 2009-01_

---

### COBOL intrinsic functions

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-01-05T14:57:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sd7nfF5cp4kU1@mid.individual.net>`

```
I needed to quickly ascertain whether something was actually a valid date, 
in COBOL

I have components that can check this in spades and return all kinds of 
different formats if the date is valid, and I use these for my own programs, 
but this is generated COBOL code for people who are not me. I don't 
neccessarily want to include a date handling package with the generated 
code, and I don't want to generate a performed date checking subroutine.

The thought occurred to me that the existing intrinsic functions must 
validate dates so I tried:

compute somenumber = function INTEGER-OF-DATE (YYYMMDD), where YYMMDD was 
preset to be a valid date. It worked as expected.

I couldn't find anything on exception handling for intrinsic functions, so I 
tried:

compute somenumber = function INTEGER-OF-DATE (YYYMMDD)
      ON SIZE ERROR  move zero to somenumber             *> can't use ON 
EXCEPTION with compute...
end-compute

Making YYYYMMDD = to 29th Feb, 1900 (an invalid date, as 1900 WASN'T a leap 
year...)

The intrinsic function corrrectly picked up the date as an error... (exactly 
what I wanted)

Unfortunately, it displays an exception and abends the program.

I don't want to use Declaratives or any abnormal runtime directives, as I 
cannot easily generate declaratives in the place where the code would need 
them, and I cannot reasonably expect people to use non-site-standard 
directives with the compiled code.

It would be SO good if COBOL had a simple date validation intrinsic...

compute someBoolean = function isDate (YYYYMMDD)   *> isDate() returns TRUE 
or FALSE (1 or zero if you like...)

if someBoolean = TRUE...

Please don't respond with dozens of ways to check dates in COBOL, unless 
they are less than 3 lines of code... : - )

Maybe some of the people working on new COBOL implementations could consider 
an extension...?

I considered usng the SQL "IsDate" function, but it's a bit of an overhead 
for a very simple test... :-)

Pete.
```

#### ↳ Re: COBOL intrinsic functions

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-01-04T20:36:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sme8l.68756$9i5.59666@en-nntp-07.dc1.easynews.com>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net>`

```
Which compiler are you using?

The original Intrinsic Function facility had NO way of handling/detecting 
problems (with dates, square roots of negative numbers, or anything).  Some 
compilers "abended" some ignored the bad input, anything was allowed.

In the '02 Standard, there are a number of NEW functions that do exactly what 
you want, e.g.
15.73 TEST-DATE-YYYYMMDD function

   ...

The returned value is:

a) If the value of argument-1 is less than 16010000 or greater than 99999999,

(1)

NOTE 1 The year is not within the range 1601 to 9999.

b) Otherwise, if the value of FUNCTION MOD ( argument-1 10000 ) is less than 100 
or greater than 1299,

(2)

NOTE 2 The month is not within the range 1 through 12.

c) Otherwise, if the value of FUNCTION MOD (argument-1 100) is less than 1 or 
greater than the number of

days in the month determined by FUNCTION INTEGER ( FUNCTION MOD ( argument-1 
10000 ) / 100 ) of

the year determined by FUNCTION INTEGER ( argument-1 / 10000 ),

(3)

NOTE 3 The day is not valid for the given year and month.

d) Otherwise,

(0)

NOTE 4 The date is valid.

    ***

I know that OpenCOBOL and Micro Focus have already implemented this.  I don't 
know which other compilers already have it.

If your compiler does NOT have this function (or similar one), then there is no 
"easy way" in Standard COBOL to do it - without do the "part by part" test 
yourself.
```

##### ↳ ↳ Re: COBOL intrinsic functions

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-01-06T09:29:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sf8t6F5boqnU1@mid.individual.net>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net> <sme8l.68756$9i5.59666@en-nntp-07.dc1.easynews.com>`

```
William M. Klein wrote:
> Which compiler are you using?
>

Fujitsu Net and PowerCOBOL.

> The original Intrinsic Function facility had NO way of
> handling/detecting problems (with dates, square roots of negative
…[4 more quoted lines elided]…
> 15.73 TEST-DATE-YYYYMMDD function

Aha, that looks good...
>
>   ...
…[32 more quoted lines elided]…
> NOTE 4 The date is valid.

That looks pretty much like what is needed. In the case I mentioned I just 
want to know if it is a valid date before proceeding. If it isn't, it gets 
fed back to the user for correction so the details of WHY it isn't valid are 
pretty mucvh irrelevant. (But I agree that different return codes pointting 
to the error are good to have.)
>
>    ***
>
> I know that OpenCOBOL and Micro Focus have already implemented this. I 
> don't know which other compilers already have it.

Unfortunately OpenCOBOL is non-viable for this customer because it hasn't 
implemented OO.

And Micro Focus require runtime fees which are a show stopper in this case.

>
> If your compiler does NOT have this function (or similar one), then
> there is no "easy way" in Standard COBOL to do it - without do the
> "part by part" test yourself.

Hmmm... that's the conclusion I was reluctantly coming to... (I hate it when 
there is "no way" :-))

Usually when people say: "There is no way you can do that" or "Nope, that 
can't be done..."  what they are really saying is: "I don't know how to do 
this."

Given that I have the utmost respect for your knowledge of things COBOL, 
Bill, this might be a case where it actually can't be done... :-)

I might opt for the SQL test as it is minimal generated code and the 
overhead is slight. However, the generated program has to be "performance 
aware" as it is a system utility that will be used often.

I guess I can try it and run some tests... not a pretty solution, though.

Thanks for your time and response.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL intrinsic functions

- **From:** "tleaders...gmail.com" <tleaders@gmail.com>
- **Date:** 2009-01-05T13:14:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<418f6e7b-2e03-425f-8858-c8d5703998a0@t26g2000prh.googlegroups.com>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net> <sme8l.68756$9i5.59666@en-nntp-07.dc1.easynews.com> <6sf8t6F5boqnU1@mid.individual.net>`

```
On Jan 5, 3:29 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> William M. Klein wrote:
> > Which compiler are you using?
>
> Fujitsu Net and PowerCOBOL.
>


This may be a silly question, but why don't you write it in vb.net or
c# using the date functions there and invoke the routines?

Tom
```

###### ↳ ↳ ↳ Re: COBOL intrinsic functions

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-01-06T13:22:55+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sfmj0F2jb5dU1@mid.individual.net>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net> <sme8l.68756$9i5.59666@en-nntp-07.dc1.easynews.com> <6sf8t6F5boqnU1@mid.individual.net> <418f6e7b-2e03-425f-8858-c8d5703998a0@t26g2000prh.googlegroups.com>`

```
tleaders...gmail.com wrote:
> On Jan 5, 3:29 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
>

Not a silly question at all.

I don't want to require a COBOL program that is being generated and intended 
for running in a COBOL environment, to make calls on something foreign to 
the local programmers. (If it was for myself, I'd do the whole thing in C# 
and be done with it :-))

The real point of my original post was that COBOL DOES do date checking in 
certain of the intrinsic functions, but through some kind of incredible 
oversight, the Standard which allowed intrinsic functions never specified 
error handling for them... the intrinsics don't even set RETURN-CODE like 
most of the MF subroutines do...

The resulting chaos is what Bill described earlier.

I haven't totally abandoned the idea of trapping the error by "brute force" 
when it is raised,(a bit like taking ESTAE exits on an IBM mainframe)  but 
it would mean a hook into the Windows interrupt system, just like the old 
days writing TSRs in 8086 assembler... :-). I know the customer won't let me 
do this (quite rightly...) but I just HATE it when there's no way... :-)

I'll ponder this over the next few days and post back what I finally 
decide...

Pete.
```

###### ↳ ↳ ↳ Re: COBOL intrinsic functions

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-01-05T15:53:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Vjv8l.21865$tg5.18368@en-nntp-05.dc1.easynews.com>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net> <sme8l.68756$9i5.59666@en-nntp-07.dc1.easynews.com> <6sf8t6F5boqnU1@mid.individual.net>`

```
Pete,
  I don't think so, but does Fujitsu offer (for free) "IBM LE emulation 
routines"?  I know that MF does, but I again, I don't think that Fujitsu does 
(even for its IBM mainframe customers)?  If they DO, then there are some 
"CEExxxx" routines that you can call to validate that a data is correct.

Sorry to keep coming up with "not in Fujitsu" answers, but you never know which 
one MIGHT work.

Have you tried your application with "OpenCOBOL" yet?  It may not have 
everything that you want, but I think it does have the TEST-xxxx functions.

see the list of supported functions at:
   http://www.opencobol.org/modules/bwiki/index.php?Features

I do NOT know if anyone has tried this yet (or how much of a run-time 
PERFORMANCE hit this would have) but you might be able to write a SUBPROGRAM in 
OpenCOBOL to do the date testing and call this from your existing Fujitsu 
application.  It *should* be just like calling any other "C" subprogram - as 
that is what OpenCOBOL creates.
```

###### ↳ ↳ ↳ Re: COBOL intrinsic functions

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-01-06T13:50:55+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sfo7gF5lui4U1@mid.individual.net>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net> <sme8l.68756$9i5.59666@en-nntp-07.dc1.easynews.com> <6sf8t6F5boqnU1@mid.individual.net> <Vjv8l.21865$tg5.18368@en-nntp-05.dc1.easynews.com>`

```
William M. Klein wrote:
> Pete,
>  I don't think so, but does Fujitsu offer (for free) "IBM LE emulation
…[3 more quoted lines elided]…
> that a data is correct.

Good idea. I'm not in contact with Fujitsu so I don't know. I should think 
it is unlikely.
>
> Sorry to keep coming up with "not in Fujitsu" answers, but you never
> know which one MIGHT work.
>

Sure, I'm very happy to look at any and all suggestions. Sometimes things 
get triggered by other unrelated suggestions.

> Have you tried your application with "OpenCOBOL" yet?  It may not have
> everything that you want, but I think it does have the TEST-xxxx
> functions.
> see the list of supported functions at:
>   http://www.opencobol.org/modules/bwiki/index.php?Features

Yes, I looked at that, and I received your list mail on same, thanks.

I'm not sure about combining flavours of COBOL... If you could do it at 
SOURCE level, then, maybe..

(Do you remember the old early implementations of COBOL where you could say: 
ENTER <some other language, usually the pertinent Assembler> then go 
straight into coding what you needed in the alternate language until ENTER 
COBOL brought you back again...? It was very useful in the days when COBOL 
was still evolving and lacked facilities that Assembler programmers took for 
granted.

I suppose, something like:

    move input-date to common-field  *> common-field  is defined as EXTERNAL
    ENTER  "Open-COBOL"
          compute RETURN-CODE = function TEST-DATE-YYYYMMDD (common-field)
    ENTER COBOL
    if RETURN-CODE NOT = zero...

That might be cool... But it is only because of  "missing" bits in different 
COBOL implementations that it is even necessary to consider it.

See, If I write a subroutine (In ANYTHING...) I still have to call it and 
pass parameters to it. I might as well just write the subroutine in Fujitsu 
COBOL...
>
> I do NOT know if anyone has tried this yet (or how much of a run-time
…[4 more quoted lines elided]…
>

If you're going to write a subroutine, you might as well use the language 
you have, in my opinion.

The real solution, I think, is for COBOL to define specific exception 
trapping for intrinsic functions using ON EXCEPTION, so that programmers can 
decide whether they wish to continue or not, instead of having the compiler 
vendor make that decision for them.

Thanks for the ideas.

Pete.
```

###### ↳ ↳ ↳ Re: COBOL intrinsic functions

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-01-05T20:02:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SYy8l.97895$NN4.92849@en-nntp-08.dc1.easynews.com>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net> <sme8l.68756$9i5.59666@en-nntp-07.dc1.easynews.com> <6sf8t6F5boqnU1@mid.individual.net> <Vjv8l.21865$tg5.18368@en-nntp-05.dc1.easynews.com> <6sfo7gF5lui4U1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:6sfo7gF5lui4U1@mid.individual.net...
<snip>
> The real solution, I think, is for COBOL to define specific exception trapping 
> for intrinsic functions using ON EXCEPTION, so that programmers can decide 
> whether they wish to continue or not, instead of having the compiler vendor 
> make that decision for them.
>
Pete,
  You aren't alone in thinking that this is (was) needed.  In fact, the very 
first draft of the Intrinsic Function Amendment *had* "when things went bad" 
returned values from those functions with limits on their arugments. 
UNFORTUNATELY, some (many?) of them were values that COULD actually occur with 
"good arguments".  This was withdrawn in the final version of the Intrinsic 
Funcitons module with a "promise to fix it soon".

Well, the Intrinsic Functions Module was approved in 1991 (as I recall) and 11 
years later, in the '02 Standard, this was really (well mostly<G>)  fixed.

If you had a "fully conforming" 2002 COBOL compiler, you could test for an
  EC-ARGUMENT
exception condition and it would give you all (most?) of the information you 
would need to determine which argument had a problem, how to fix it, and to then 
let you return to processing.

OpenCOBOL has implemented much of the '02 Exception Handling model.  I am not 
certain how much Micro Focus has implemented yet. (I think they have a 
"Throw/Catch - C-like" exception processing facility - at least in their .NET 
product), IBM lets you "trap" many LE exceptions (including invalid dates),
  but (again) Fujitsu hasn't done any of this (that I know of ).

I supposed that this is where I do my usual plug that (for COBOL not for other 
or "modern" languages), it looks like you get as much development and 
enhancements (in commercial compilers at least) as you pay for in run-time 
licenes or other developer costs <G>.
```

#### ↳ Re: COBOL intrinsic functions

- **From:** Alain Reymond <arwebmail@skynet.be>
- **Date:** 2009-01-05T09:54:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4961cb0f$0$2847$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<6sd7nfF5cp4kU1@mid.individual.net>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net>`

```
Pete,

Depending on your compiler - it works with Micro Focus NE v5 -, you can
write your own function :

isdate.cbl :
      $set repository (update on)
       identification division.
       function-id. isdate as "isdate".
       working-storage section.
       linkage section.
       1 myDate pic 9(8).
       1 OK pic 9.
       procedure division using myDate returning OK.
         *> Test myDate
         move 1 to OK
         exit function.
       end function isdate.

testisdate.cbl :
      $set repository(checking off)
       repository.
           function isdate as "isdate".
       data division.
       working-storage section.
       1 myDate pic 9(8).
       1 bool pic 9.
       procedure division.
           move 20090105 to myDate
           if isDate(myDate) = 1 then
              display "Correct"
           else
              display "False"
           end-if
           exit program
           stop run
           .

The only lines you have to include in your code are :
       repository.
           function isdate as "isdate".

And it's done.

Regards

Alain

Pete Dashwood a ï¿½crit :
> I needed to quickly ascertain whether something was actually a valid date, 
> in COBOL
…[51 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL intrinsic functions

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-01-06T13:06:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sflk3F5rs44U1@mid.individual.net>`
- **References:** `<6sd7nfF5cp4kU1@mid.individual.net> <4961cb0f$0$2847$ba620e4c@news.skynet.be>`

```
Alain Reymond wrote:
> Pete,
>
> Depending on your compiler - it works with Micro Focus NE v5 -, you
> can write your own function :
>

This is Fujitsu NetCOBOL and PowerCOBOL. Unfortunately, they haven't 
implemented user functions in the version I'm using. BUT, they are both full 
OO compilers so I COULD include one of my date handling components and 
connect it through the repository as you did below with your function.

I was hoping to avoid making extra source part of the deliverable. (In fact, 
I don't really want to supply extra components at all, not because I am mean 
spirited by nature :-), but because it complicates the deployment...)

I'm trying to encourage them into late binding, so a repository based 
solution is unattractive (but certainly not ruled out...)

I really like this solution, Alain.

I'll think some more about providing a component to them...

> isdate.cbl :
>      $set repository (update on)
…[35 more quoted lines elided]…
> And it's done.

This is quite elegant.  The main drawback for me is that I have to provide 
the IsDate function either as source or object (or both) and that 
complicates the delivery. Nevertheless, it is a very nice idea.

Thanks Alain.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
