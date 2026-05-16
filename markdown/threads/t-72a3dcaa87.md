[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_66 messages · 14 participants · 2007-07_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-04T14:29:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<138nprdpf6ucu82@corp.supernews.com>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5dna71F35l0l3U1@mid.individual.net...
>
[snip]
> Do you think it might be useful to have Regular Expressions in COBOL?
> [...]

I think it is useful to have Regular Expressions
available to COBOL programs; but there are
reasons why such common REs should not be
made part of the COBOL language standard.

Regular Expressions "grew up" in C and used the
older C character set (ASCII) as a means for
specifying the REs. When C went through ISO
standardization, it adopted ISO 646 for its
character set. In most cases, there is no difference.
In a few cases, for some countries, some of the
standard C graphic characters are replaced with
national characters. To accommodate these
replacements, the C standard specifies certain
"trigraph" sequences (from the ISO 646-1083
Invariant Code Set) to replace the missing characters.
This is the first problem. To include REs, as commonly
used, would require expansion of the COBOL Basic
character set to include the missing characters and
the introduction of "trigraphs".

At least one character, the circumflex ("^") is not
defined for EBCDIC (according to my "Yellow
Card" (Second Edition (September 1972)) and
other sources). The circumflex apparently maps
to the logical not ("�"). The second, perhaps not
so big, problem is the variations that occur with
different vendors' character sets.

The POSIX definition of REs is, apparently (I am
relaying on statements about "lex" which uses REs
and certain comments about how POSIX 2 affects
portability of those REs), somewhat different than
what is commonly presented. Certain common patterns
now have specific names in order to accommodate
portability across platforms and locales. These
names were adopted from ISO C. Some examples
are: [A-Z] is [:upper:], [a-z] is [:lower:], [A-Za-z] is
[:alpha:], [0-9] is [:digit:], and [A-Za-z0-9] is
[:alnum:]. The keywords "upper", "lower", etc. also
include any locale specific upper- and lower-case
letters. This is the third problem: The inclusion of
commonly used REs in standard COBOL would
probably require conformance to the POSIX
standard and, from what I've seen, there seems to
be little desire to conform to that standard; but that
might be because I see REs written by those who
use English and may not be concerned with other
languages.

The processing of REs, having developed using
delimited strings, would require the use of ANY
LENGTH items in COBOL (200x with PREFIXED
or DELIMITED phases). While I have not looked
at ANY LENGTH, at length, there are some
complaints that it is defective (or, at least has
problems). This the fourth problem, potentially.
Whatever problems exist with ANY LENGTH must
be resolved before REs could be added to COBOL.

I have only scratched the surface; but, like the scratch-
'n-sniff ads in magazines, I don't care for the odor!
If I want to write C instead of COBOL, I will write
C instead of COBOL!

I think a better way might be to input a RE to a code
generator, which would create a COBOL program
to process the RE.
```

#### ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-05T16:35:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f3anoF38l4hvU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:138nprdpf6ucu82@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[74 more quoted lines elided]…
>

I disagree :-). (But I really don't care, so don't expect a passionate 
debate about this... :-))

I'm using REs in an environment where they work properly so I don't have any 
of the problems you mentioned. In fact I can process Unicode strings with 
REs if I want. AND I can do it from COBOL.

(Of course, I use MicroSoft, but, strangely as some might expect, I have not 
broken out in warts all over my body, been invited to midnight orgies in 
worship of Bill Gates, or been required to sacrifice any children so my code 
will work. It just does...)

To input REs to a preprocessor that then "creates a COBOL program to process 
the RE"  is certainly a POSSIBLE solution, but very unwieldy, and, in most 
cases where you would want to use a Regular Expression, not worth the 
effort.

Given that there are numerous RE components available, and some of these are 
in formats that can be called from COBOL, I see it as being the same problem 
which some people perceive COBOL to have with processing XML. (I've been 
processing XML from COBOL for years now, using the standard components that 
come with my Operating System (because they are free). If I want the code to 
run on a different Operating System it would be a matter of moments to plug 
in a third party component (assuming there isn't one in the new environment) 
and away we go... Processing XML has never been a problem for COBOL or 
anything else; the functionality to do it has been encapsulated long ago and 
is freely available.

(However, a pointless exercise is now being embarked on to add that to the 
language as well. It's almost as if "Not invented by us...therefore 
worthless" is the motto of the people responsible for what facilities COBOL 
offers.)

So instead, huge amounts of effort, time, and (to a lesser extent) money, 
are expended to re-invent the wheel, solve problems that were already solved 
in ancient time, come up with a better mousetrap, when there aren't any 
mice...

I see REs as being exactly in this category.

But then, rather than scratching and sniffing problems, I tend to first 
decide whether there is an existing solution that doesn't require me to 
break the seal.

I see two such solutions here:

        1. Call a component that does it.

        2. Let your vendor provide a runtime component that does it (maybe 
HE can call an existing one for you...)

COBOL verbs are really an interface to tell the compiler writer which 
components need to be in the runtime.

Yet the assumption is made in certain quarters that Native Code or 
intermediate code will be generated from every verb coded by the programmer.

Vendors (usually...and I am talking about the "good" ones :-)) don't 
generate all the machine code every time you write READ; they access a 
runtime component. The interface is consistent and common. They do the same 
when you use SEARCH, or UNSTRING,  or CLASS tests like ALPHANUMERIC...

Vendors could simply add RE and XML components to their runtimes. (It could 
be implementor defined, just as so many other things are...) (Then it would 
be a simple matter to decide whether you will CALL a component yourself or 
whether you will use the one provided...)

Simple constructs could be added to the language to define an interface to 
RE and XML components, included by the vendor in the runtime. It is no more 
difficult than defining access to data or driving a screen section. (It IS 
more difficult if you expect the wheel to be reinvented every time someone 
codes it...)

"All ya gotta do" is...:-)

01 match-string pic x(whatever) usage is REGULAR-EXPRESSION. *> Allows the 
compiler writer to know that some
                                                                             
                               *> possibly invalid (for COBOL) characters 
may be
                                                                             
                               *> found in this location, and also to syntax 
check
                                                                             
                               *> the RE in accordance with what he has 
implemented.
01 data-to-be-parsed pic x(whatever). *> if this area gets expanded by the 
RE process, it will be truncated in
                                                           *> accordance 
with the standard COBOL rules for ALPHANUMERIC
                                                           *> MOVE 
truncation. (Programmers pad the size if they think it is likely
                                                           *> to expand. NO 
requirement for ANY-LENGTH at all.)
01 RE-result   pic x value space.
     88 RE-matched value '1'.
     88 RE-unmatched value '0'.

...

SPEC:

"A string must contain one, and only one "@" symbol. There can be any number
of alphanumeric characters preceding the "@", but there MUST be at least
one. Other characters can be ignored. (There can be dots, for example).
Succeeding the "@" symbol there must be at least one alphanumeric symbol
preceding one or more dots. A dot cannot be the final symbol in the string
and must always be "surrounded" by at least one alphanumeric character on
either side of it."

(Assuming my compiler vendor is "MicroSoft friendly"... (both Fujitsu and 
MicroFocus are MS partners))


        *> check email address
            move "(\\w+)@(\\w+)\\.(\\w+)" to match-string *> the rules for 
what would be acceptable here
                                                                             
        *> would be in the vendor's COBOL manual.
                                                                             
        *> I have used the MS shorthand for [A-Za-z0-9]
            move email-address to data-to-be-parsed
            move zero to myTally
            inspect email-address
                tallying myTally
                    for ALL "@"
            if myTally =  1
                REGEX
                            MATCH  data-to-be-parsed
                              USING  match-string
                    RETURNING  RE-result
              ON OVERFLOW  perform internal-error *> the result overflowed 
the data-to-be-parsed buffer.
                                                                             
   *> (Impossible in the case of MATCH)
               END-REGEX
               if RE-unmatched
                  move 2 to MyTally
               end-if
            end-if
            if myTally NOT = 1
                ... process as invalid email address
            end-if
         *>  address appears to be valid...

Nah, too easy...(still, a lot less effort than writing a couple of hundred 
lines of COBOL)

Pete.
```

##### ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-05T19:49:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<138r0t5o311iu77@corp.supernews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5f3anoF38l4hvU1@mid.individual.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[82 more quoted lines elided]…
> I'm using REs in an environment where they work properly so I don't have
any
> of the problems you mentioned. In fact I can process Unicode strings with
> REs if I want. AND I can do it from COBOL.
>
> (Of course, I use MicroSoft, but, strangely as some might expect, I have
not
> broken out in warts all over my body, been invited to midnight orgies in
> worship of Bill Gates, or been required to sacrifice any children so my
code
> will work. It just does...)
>
> To input REs to a preprocessor that then "creates a COBOL program to
process
> the RE"  is certainly a POSSIBLE solution, but very unwieldy, and, in most
> cases where you would want to use a Regular Expression, not worth the
> effort.
>
> Given that there are numerous RE components available, and some of these
are
> in formats that can be called from COBOL, I see it as being the same
problem
> which some people perceive COBOL to have with processing XML. (I've been
> processing XML from COBOL for years now, using the standard components
that
> come with my Operating System (because they are free). If I want the code
to
> run on a different Operating System it would be a matter of moments to
plug
> in a third party component (assuming there isn't one in the new
environment)
> and away we go... Processing XML has never been a problem for COBOL or
> anything else; the functionality to do it has been encapsulated long ago
and
> is freely available.
>
> (However, a pointless exercise is now being embarked on to add that to the
> language as well. It's almost as if "Not invented by us...therefore
> worthless" is the motto of the people responsible for what facilities
COBOL
> offers.)
>
> So instead, huge amounts of effort, time, and (to a lesser extent) money,
> are expended to re-invent the wheel, solve problems that were already
solved
> in ancient time, come up with a better mousetrap, when there aren't any
> mice...
…[18 more quoted lines elided]…
> intermediate code will be generated from every verb coded by the
programmer.
>
> Vendors (usually...and I am talking about the "good" ones :-)) don't
> generate all the machine code every time you write READ; they access a
> runtime component. The interface is consistent and common. They do the
same
> when you use SEARCH, or UNSTRING,  or CLASS tests like ALPHANUMERIC...
>
> Vendors could simply add RE and XML components to their runtimes. (It
could
> be implementor defined, just as so many other things are...) (Then it
would
> be a simple matter to decide whether you will CALL a component yourself or
> whether you will use the one provided...)
>
> Simple constructs could be added to the language to define an interface to
> RE and XML components, included by the vendor in the runtime. It is no
more
> difficult than defining access to data or driving a screen section. (It IS
> more difficult if you expect the wheel to be reinvented every time someone
…[10 more quoted lines elided]…
>                                *> found in this location, and also to
syntax
> check
>
…[8 more quoted lines elided]…
>                                                            *> to expand.
NO
> requirement for ANY-LENGTH at all.)
> 01 RE-result   pic x value space.
…[7 more quoted lines elided]…
> "A string must contain one, and only one "@" symbol. There can be any
number
> of alphanumeric characters preceding the "@", but there MUST be at least
> one. Other characters can be ignored. (There can be dots, for example).
…[41 more quoted lines elided]…
> lines of COBOL)

First, let's deal with the regular expression: "(\\w+)@(\\w+)\\.(\\w+)".
This is actually quite "lame" for validating e-mail addresses.
I did some digging at < www.microsoft.com > to get a better
understanding of Microsoft's "perversion" of regular expressions
and found the following:

< http://msdn2.microsoft.com/en-us/library/aa332116(VS.71).aspx >
-----
.NET Framework Class Library
Regex.IsMatch Method (String, String)
Indicates whether the regular expression finds a match in the
input string using the regular expression specified in the
pattern parameter.

[C#]
public static bool IsMatch(
 string input,
 string pattern
);

Parameters

input
The string to search for a match.

pattern
The regular expression pattern to match.

Return Value
true if the regular expression finds a match; otherwise, false.
-----

And
< http://msdn2.microsoft.com/en-us/library/1400241x.aspx >
-----
\w
 Matches any word character including underscore. Equivalent
to '[A-Za-z0-9_]'.
-----

The IsMatch method will find whether the pattern exists
anywhere in the string. "(\\w+)@(\\w+)\\.(\\w+)" means letters,
numbers, or underscores; followed by "@"; followed by more
letters, numbers, or underscores; followed by a dot (".");
followed by even more letters, numbers, or underscores will
match without regard to the position of the pattern in the string.

This means that IsMatch will return true (valid e-mail address)
when these strings are tested with the given regular expression.:

"The quick brown fox@henhouse.net jumped over" and
"Apples 5lbs@1.29 per pound - On sale"

Clearly these complete strings are not valid e-mail addresses;
only the matched portion may be.

Microsoft provides an example, which I have modified.

< http://msdn2.microsoft.com/en-us/library/aa720056(VS.71).aspx >
-----
.NET Framework Developer's Guide
Example: Confirming Valid E-Mail Format
The following code example uses the static Regex.IsMatch
method to verify that a string is in valid e-mail format. The
IsValidEmail method returns true if the string contains a valid
e-mail address and false if it does not, but takes no other action.
You can use IsValidEmail to filter out e-mail addresses
containing invalid characters before your application stores the
addresses in a database or displays them in an ASP.NET page.

...

[C#]bool IsValidEmail(string strIn)
{
    // Return true if strIn is in valid e-mail format.
    return Regex.IsMatch(strIn,

@"^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA
-Z]{2,4}|[0-9]{1,3})(\]?)$");
}
-----

With the IP address and extra parentheses removed:
 @"^([\w-\.]+)@(([\w-]+\.)+)([a-zA-Z]{2,4}$"

For our purposes, the initial "@" is ignored.

The "^" means beginning of line, therefore nothing may precede
the pattern.

The "([\w-\.]+)" means letters, numbers, underscores, hyphens,
and dots, in any order; but at least one character must be present.

The "@" must be present.

The "(([\w-]+\.)+)" is a "nested" pattern with at least one letter,
number, underscore, or hyphen followed by a dot ".". This
pattern must occur at least once.

The "([a-zA-Z]{2,4}" means at least two; but not more than
four letters.

The "$" means end of line.

As may been seen, there is room for one and only one e-mail
address to be validated. The use of the caret ("^") and dollar
sign ("$") means that other characters can not precede nor
follow the e-mail address.

When I wrote "The processing of REs, having developed using
delimited strings, would require the use of ANY LENGTH
items in COBOL (200x with PREFIXED or DELIMITED
phases)"; I had the end of line character ("$") in mind. The
position of the end of line may need to vary depending on the
length of text to be searched for a match and for the regular
expression, itself. I suppose for a COBOL fixed-length field
the definition might be changed to include trailing spaces that
are not part of the text or expression; but I think that's messy
and I am not sure what effect it might have on the regular
expression.

While I can not, at this point, image what implementors might
do to incorporate regular expressions into COBOL, I did
find the following at the University of Limerick.

< http://www1.csisdmz.ul.ie/curstudents/fyp/suggestions/mcoughlan >
-----
ID: MC06
Title: Regular Expressions for COBOL

COBOL does not have any way of evaluating regular expressions.
In certain situations, such as validating user input, regular
expressions would greatly simplify coding. To rectify this omission
this project will create a set of external sub-programs for COBOL
that can be used to evaluate regular expressions.
-----

Some of the changes made for COBOL 2002 were intended to
accommodate such sub-programs; but the ability to incorporate
programs written in other languages may be limited; that is, if the
result of the project is source programs written in standard
COBOL, then regular expressions may be more easily added.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-06T15:48:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f5sdcF3an649U1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:138r0t5o311iu77@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[383 more quoted lines elided]…
> expression.

Well, thank you for the improved RE string. However that wasn't the point of 
the post. (And I have been using the "lame" string for some time now without 
problem. It is sufficient to my purposes. Having said that, a "tighter" one, 
as you have described above, could be useful for cases where the email 
actually "really matters", but, in those cases I would ping the URL 
anyway...)

I think the point here is that COBOL could implement things through syntax 
and let implementors (vendors) decide how they want to do it (usinmg 
existing components, or not). Instead, it seems that everything has to be 
spelled out to last detail with people who are not even writing the compiler 
deciding how it must work.

As is often the case with procedural programming, the focus is on HOW when 
it should be on WHAT.



>
> While I can not, at this point, image what implementors might
…[13 more quoted lines elided]…
> -----

University of Limerick has been a strong supporter of COBOL for many years. 
Unfortunately, their solutions are not always the best. Again, as long as 
the focus is on source code (let's generate a sub-program...) instead of 
functionality (we need some functionality; does it exist? How could we 
incorporate it or use it?), the solution is going to be a less than optimum 
one.

Universities can afford to spend time re-inventing wheels; commerce cannot.
>
> Some of the changes made for COBOL 2002 were intended to
…[4 more quoted lines elided]…
>

And if an RE engine is included in the run time nothing has to be added at 
all.

Pete.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-06T08:38:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<138sduqriahhhbb@corp.supernews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5f5sdcF3an649U1@mid.individual.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[12 more quoted lines elided]…
> >> >> Do you think it might be useful to have Regular Expressions in
COBOL?
> >> >> [...]
> >> >
…[3 more quoted lines elided]…
> >> > made part of the COBOL language standard.

[snip]

> Well, thank you for the improved RE string. However that wasn't the point
of
> the post. (And I have been using the "lame" string for some time now
without
> problem. It is sufficient to my purposes. Having said that, a "tighter"
one,
> as you have described above, could be useful for cases where the email
> actually "really matters", but, in those cases I would ping the URL
> anyway...)

Mr Dashwood, it was never about you or your use of the RE.
The RE was presented as something found on the web and as
a solution to a problem. I called it "lame", explained why, then
offered a different solution (also found on the web), explained
it, and showed why it is more effective for the purpose. My
comments were intended for others who might have been
tempted to use that RE without understanding its limitations.
It was an alternative and, in that sense, no different than your
presenting C# as an alternative to COBOL; though I wish
you wouldn't! <G>


> I think the point here is that COBOL could implement things through syntax
> and let implementors (vendors) decide how they want to do it (usinmg
> existing components, or not). Instead, it seems that everything has to be
> spelled out to last detail with people who are not even writing the
compiler
> deciding how it must work.

Mr Dashwood, you seem not to grasp that the COBOL
standard (indeed, any programming language standard)
is a "specification" document. Everything necessary for
portability of source code and resulting behavior of the
compiled code must "be spelled out to last detail", where
"last detail" is understood to be "everything necessary ...".

This means for specifying a regular expression and the
metacharacters that make up a regular expression must
be identified and the effect of those metacharacters on
the processing of the regular expression must be defined
to the last detail. And that was my point at the start of this
thread.

Consider the less common type of regular expression
that is used in the PICTURE clause. (It is a regular
expression; "we just don't call it that"!) If implementors
were free to define the metacharacters that make up
the "picture", some might have chosen C-type format
strings, instead. Such source code would not be portable.

> As is often the case with procedural programming, the focus is on HOW when
> it should be on WHAT.

I have no idea what point you are trying to make.

Procedure-names, function-names, and method-names
identify what. Procedures, functions, and methods
focus on how; or, so it seems to me.

Object-Oriented design and functional design are
reducible to procedural design. Object-Oriented
programs and functional programs are reducible to
procedural programs (albeit with some name-mangling)
before compiling.

Object-Oriented programming, functional programming, and
procedural programming, all, focus on how; that is, how to
partition a programming problem.

I see conceptual and practicable differences among these;
but see no fundemental difference.

>
>
…[17 more quoted lines elided]…
> University of Limerick has been a strong supporter of COBOL for many
years.
> Unfortunately, their solutions are not always the best. Again, as long as
> the focus is on source code (let's generate a sub-program...) instead of
> functionality (we need some functionality; does it exist? How could we
> incorporate it or use it?), the solution is going to be a less than
optimum
> one.
>
> Universities can afford to spend time re-inventing wheels; commerce
cannot.

It seems to me that commerce spends at lot of time
re-inventing wheels (for commercial advantage); how else
could the existence of C# be explained? <g>
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-07T04:41:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f79m1F3a58vtU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:138sduqriahhhbb@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[39 more quoted lines elided]…
> a solution to a problem.

Well, Mr. Smith as it was I who started the whole conversation about RE 
here, as it was I who posted (in response to a request from someone else) an 
example which I use, and contrasted it with what would be required in COBOL 
to achieve the  same end, I believe I have every right to post the response 
I did above.


I called it "lame", explained why, then
> offered a different solution (also found on the web), explained
> it, and showed why it is more effective for the purpose.

Yes, and you did a good job of that. However, it was not what this thread 
was about.

You went to levels of detail which were quite unnecessary, as you always do, 
in pursuit of something which really isn't worth the effort. Nobody cares 
whether a particular  (more complex) RE is better for validating email 
strings in 1 out of a couple of thousand cases; as I pointed out, if it was 
REALLY important, the address would be validated by pinging anyway.

The point of the conversation is whether or not this facility could or 
should be part of COBOL. You came up with a whole bunch of problems (without 
doing detailed investigation) that would preclude it. I suggested some 
alternatives that would make it fairly easy.

>My
> comments were intended for others who might have been
> tempted to use that RE without understanding its limitations

Ha! Given that people using COBOL are unlikely to try and use RE anyway, and 
given that I posted a full explanation of what it did when I first posted 
it, that would seem somewhat superfluous.

> It was an alternative and, in that sense, no different than your
> presenting C# as an alternative to COBOL; though I wish
> you wouldn't! <G>

Alternatives should be discussed.

I don't see C# as an alternative to COBOL, I see it as a more useful 
replacement. Too bad if that offends you; your pedantry has the same effect 
on me.

>
>
…[13 more quoted lines elided]…
> "last detail" is understood to be "everything necessary ...".

Mr. Smith, you seem incapable of grasping that a specification can be 
functional as well as technical. It isn't hard to see why COBOL is in the 
state it is and releases of standards took so long. Functionality can be 
spelled out to the last detail, but that doesn't mean existing wheels must 
be re-invented.

Reading your post just makes me thankful we have vendors who are pragmatic 
enough to simply get on and do it... There'd be no COBOL if it was left to 
COBOL committees.

>
> This means for specifying a regular expression and the
…[5 more quoted lines elided]…
>

Nope. It is NOT necessary to go to that level of detail. There are existing 
standards for RE. These could be referenced and vendors could make their own 
choice within an existing standard. The same applies to XML. It is YOU 
personally, who wants to look at every single metacharacter because that is 
your nature. Most people don't. Neither do they need to.



> Consider the less common type of regular expression
> that is used in the PICTURE clause. (It is a regular
…[3 more quoted lines elided]…
> strings, instead. Such source code would not be portable.

PICTURE Clauses were developed at a time when there was no alternative. 
Implementors would not have chosen C type format strings because C was not 
invented. PICTURE was developed to remove the necessity to code SIZE, CLASS 
and USAGE, as we had to do in the early implemations of COBOL. In fact, to 
this day you can define data fields in COBOL without using PICTURE.

My point is that PICTURE was NOT a re-invention of the wheel; it was a 
useful addition to the language which saved people time.

As for portability, COBOL isn't portable anyway. The best you can do is hope 
to keep it less of a hassle to convert by using a strict subset of 
constructs. It doesn't have the portability of Java or of C#.
>
>> As is often the case with procedural programming, the focus is on HOW 
…[3 more quoted lines elided]…
> I have no idea what point you are trying to make.

No, I know. It's sad...
>
> Procedure-names, function-names, and method-names
…[7 more quoted lines elided]…
> before compiling.

Oh sure, and all computers execute one instruction at a time so procedural 
has to be the way to go...

>
> Object-Oriented programming, functional programming, and
> procedural programming, all, focus on how; that is, how to
> partition a programming problem.

Sure. If all you can see is a programming problem...
>
> I see conceptual and practicable differences among these;
> but see no fundemental difference.
>

Perhaps you need more practice at looking?

>>
>> >
…[30 more quoted lines elided]…
> could the existence of C# be explained? <g>

I don't get emotional about programming languages. C# exists because it gets 
the job done.

If it stopped doing that, I'd move to something else. As to commerce 
re-inventing existing wheels, perhaps you'd like to run that argument past 
all the people who moved from COBOL to SAP, Siebel, Peoplesoft and Oracle in 
the last few years... ?

Dashwood.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-07-06T11:39:52-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net>`

```
On Sat, 7 Jul 2007 04:41:37 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I don't see C# as an alternative to COBOL, I see it as a more useful 
>replacement. Too bad if that offends you; your pedantry has the same effect 
>on me.

...

>I don't get emotional about programming languages. C# exists because it gets 
>the job done.

I'm curious.   Certainly C# has its strengths, and there are jobs it
does quite well.    But as someone who doesn't believe that one tool
is the best for all jobs, I don't see that C#'s strengths and uses are
a good match for CoBOL's.

But that doesn't mean you aren't right.   I tend to think CoBOL is
being replaced by something even more different than C# is - and
that's a combination of intelligent databases, report programs, and
interfaces instead of any one language.

I don't see companies replacing their CoBOL green bar report program
with a C# XML report program.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-07-06T19:27:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T_idnRKFgOeYcRPbnZ2dnUVZ_umlnZ2d@comcast.com>`
- **In-Reply-To:** `<23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com>`

```
Howard Brazee wrote:
> On Sat, 7 Jul 2007 04:41:37 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[13 more quoted lines elided]…
> a good match for CoBOL's.

At my last assignment, our formerly-on-the-mainframe source code control 
system was moved to the web, with parts in C#.  (In fact, that big thing 
I posted back in February was part of it.)

> But that doesn't mean you aren't right.   I tend to think CoBOL is
> being replaced by something even more different than C# is - and
…[4 more quoted lines elided]…
> with a C# XML report program.     

(As you like to say) For various values of "language".  :)

I'd venture to say that most all systems use more than one language - 
the aircraft maintenance system that I worked on at my last base used 
COBOL, Java, JavaScript, HTML, XML, XSLT, SQL, and a proprietary network 
database language called DML.

What you've described above falls nicely within the Model View 
Controller methodology.  The "model" is the persistent data store, the 
"view" is the way information is presented to the user, and the 
"controller" is the bridge between the two.

Then, is XML a language in the same way as COBOL, Java, or C#?  I've 
seen XML used for lots of things - configuration parameters, a 
structured way of passing data internally between modules, formatting 
data for exchange with other systems, even as the output displayed to 
the user (formatted with XSLT).

I'm not saying you're wrong about this - just adding to it.  I see the 
common factor coming down to XML.  No matter how you get to it (COBOL, 
C#, Java, QuickBASIC), and no matter what you do with it (look at it 
with human eyes, load it into a database, or use it to tell other 
software what to do), XML is the glue that holds it all together.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-07T17:58:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f8ocpF3biap7U1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <T_idnRKFgOeYcRPbnZ2dnUVZ_umlnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:T_idnRKFgOeYcRPbnZ2dnUVZ_umlnZ2d@comcast.com...
> Howard Brazee wrote:
>> On Sat, 7 Jul 2007 04:41:37 +1200, "Pete Dashwood"
…[51 more quoted lines elided]…
>

I agree with your point on the importance of XML, Daniel. Especially as the 
web starts to bite and web services become more important.

But, as Howard pointed out, it isn't any ONE factor (language, methodology, 
or even management approach) that will shape the future.

It is a complete rethink. A paradigm shift that started with people 
realising the benefits of Object technology and moving on from there.

Pete.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-07T07:24:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183818257.623951.98610@q75g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<T_idnRKFgOeYcRPbnZ2dnUVZ_umlnZ2d@comcast.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <T_idnRKFgOeYcRPbnZ2dnUVZ_umlnZ2d@comcast.com>`

```
On 7 Jul, 02:27, LX-i <lxi0...@netscape.net> wrote:
> Howard Brazee wrote:
>
> > I don't see companies replacing their CoBOL green bar report program
> > with a C# XML report program.    
>

My boozy chum once expressed a requirement for a program to convert a
output report into XHTML so that it could be viewed using any browser.
I'm tempted to write it in, guess what?, COBOL.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-07T17:53:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f8o2sF3amt6qU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com...
> On Sat, 7 Jul 2007 04:41:37 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[20 more quoted lines elided]…
> interfaces instead of any one language.

Yes, you are quite right. It isn't about any particular language. 
Nevertheless, and I stress it is simply a personal opinion, for the jobs 
that I WOULD have used COBOL in the past, I now find C# serves me better.

>
> I don't see companies replacing their CoBOL green bar report program
> with a C# XML report program.

That's the nub of it. Until people start to realise that paper reports are 
really not as valuable as they have been any more, there will continue to be 
managers who demand them. These days it is about INFORMATION. It needs to be 
timely (up to the millisecond), easily digestible (graphic and summarised, 
with drill down capabilities) and it should only be committed to paper as a 
last resort.

This is a major shift for many managers. I think that's why I get tired of 
debating languages here. It is a paradigm shift. It isn't just about 
languages, it is about whole new ways of looking at things, and in 
particular, software  and system development.

It is really crazy for me to sit here and debate the use of Object 
technology with people who can only see it in terms of a programming 
solution, and think it is just procedural code re-invented. It isn't. RAD, 
component (object) based system design is so far removed from the Waterfall 
and procedural code that the programming part of it pales into 
insignificance.

Anyway, I realise I have let some of this get to me and I really shouldn't.

I'll be a less frequent visitor here in the future and many people will be 
pleased to hear that.

Pete.
```

###### ↳ ↳ ↳ Hard Copy reports (was: Regular Expressions and Standard COBOL

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-07-07T11:32:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DRKji.112754$Xu1.100559@fe07.news.easynews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5f8o2sF3amt6qU1@mid.individual.net...
>
> "Howard Brazee" <howard@brazee.net> wrote in message 
> news:23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com...
>> On Sat, 7 Jul 2007 04:41:37 +1200, "Pete Dashwood"
>> <dashwood@removethis.enternet.co.nz> wrote:
<snip>
>> I don't see companies replacing their CoBOL green bar report program
>> with a C# XML report program.
…[6 more quoted lines elided]…
> last resort.

Pete,
  As I don't work (much less in "Fortune 500-type companies", I am curious 
whether current "big company" requirements by Auditors - and especially (in the 
US) with new "regulatory requirements" allows for 'non-hard-copy solutions. 
This really is a question on my part and not intended to argue with what you 
posted.

It seems to me that for "day-to-day" buiseness needs - having "real time access 
to information" is the critical requirement of much of IT.  On the other hand, 
for "tracking and auditor and regulation" purposes, it seems to me that the need 
for (remarkly frequently changing) hard-copy reports is growing, not 
diminishing.

As a COBOL report writer fan, these types of reports can EASILY be produced and 
modified in COBOL.  As a "Workstaion-attached PDF and 'graphic' report fan, I 
would think that COBOL  is not a good (much less the best) tool for the job.>

P.S.  "Monthly" hard-copy (or soft - but looks like hard copy) bills are anoterh 
place where "batch COBOL-type" processing works well - IMHO.  Again, although 
many/most "customers" like real-time online access to the current state of their 
accounts/bills, at least in the US, I still see that most such buisness still 
provide a hard-copy (or looks like hard-copy) version of monthly 
bills/statements. We (CLC) have discussed such things before, however, I know of 
few "large companies" that have converted their "traditional procedural" 
applications for such bill/statement processing to OO - even if they DO provide 
"real time" versions of the information via OO applications.

Are you (Pete or anyone else) aware of any large companies that still produce 
monthly (or quarterly or year-end)  bills/statementes that have converted such 
procesisng to any OO solution?  I would think there must be SOME somewhere, but 
I certainly haven't heard of this being common.
```

###### ↳ ↳ ↳ Re: Hard Copy reports (was: Regular Expressions and Standard COBOL

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-08T04:27:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f9t6pF3c0r4lU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:DRKji.112754$Xu1.100559@fe07.news.easynews.com...
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
> news:5f8o2sF3amt6qU1@mid.individual.net...
…[22 more quoted lines elided]…
>

Auditors here require reports, BUT they are pleased to accept them in 
computer sensible form. Random checks can be made online and only 
hard-copied if there is something untoward or needing further investigation.

Obviously, it may be different in the US.

> It seems to me that for "day-to-day" buiseness needs - having "real time 
> access to information" is the critical requirement of much of IT.  On the 
> other hand, for "tracking and auditor and regulation" purposes, it seems 
> to me that the need for (remarkly frequently changing) hard-copy reports 
> is growing, not diminishing.

I haven't seen that. Most places I have worked are committed to cutting down 
on paper rather than increasing it. Spreadsheets and databases seem to be 
replacing what used to be reports in many cases. This means users can 
manipulate the data into whatever format they want and filter the stuff they 
are not interested in. Kind of like a flexible report format... Only when it 
is organised how they want  it, MIGHT they then print it, although this is 
generally discouraged in the places I've worked here.

It is certainly true that this is becoming more the norm, as more users 
become "computer literate" and deal with spreadsheets and databases as a 
matter of course. Previously, (before PCs and people growing up with them) 
it wasn't possible, as the user was not capable of extracting data himself 
and had to go to the IT department to get anything done. This is changing, 
and it is PC technology ( and the network) which has empowered it.

>
> As a COBOL report writer fan, these types of reports can EASILY be 
> produced and modified in COBOL.  As a "Workstaion-attached PDF and 
> 'graphic' report fan, I would think that COBOL  is not a good (much less 
> the best) tool for the job.>

In some places they will have no choice other than to do them in COBOL. If 
the data is in VSAM  or ISAM files it is not easily interchangeable to other 
software and needs to have programs written to extract it. If it is on a 
database, ODBC means that the whole network has access to it (given the 
appropriate permissions, of course) and so there is no need for Report 
Writer.

>
> P.S.  "Monthly" hard-copy (or soft - but looks like hard copy) bills are 
> anoterh place where "batch COBOL-type" processing works well - IMHO.

Yes, it does. And has done so for many years. But the world is changing, and 
so are the people in it. Many people (self included) DON'T want "monthly" 
bills and statements. Rather they want to see all their transactions for a 
period they can call off themselves. My bank offers this facility and has 
done for a number of years now. I believe the percentage of customers using 
it is over 60% and increasing. The bank has saved a fortune by encouraging 
people to move off paper statements. But it does mean smarter systems and 
more transaction processing power. Coincidentally, the same bank moved off 
their mainframes about 5 years ago. It was very hard for them and cost a 
fortune. They had a project in Sydney that cost several hundred million 
dollars (I know a couple of the people who worked on it). It was almost a 
disaster and was only salvaged by rescoping and increasing the budget. The 
point is that they didn't get to the very desirable state they have now, 
without considerable pain. But their systems are modern and effective, and I 
think if you asked them, they would say the cost was worth it.

I've noticed that more and more organisations are offering "do-it-yourself" 
accounts of this nature... American Express and my London Bank are just two 
that have moved to it comparatively recently.


> Again, although many/most "customers" like real-time online access to the 
> current state of their accounts/bills, at least in the US, I still see 
…[6 more quoted lines elided]…
>

Yes, they are giving people options. Eventually it will be phased out 
because the demand for it will dry up... "You get paper statements from your 
bank? How quaint..."

It is still possible to get black and white TV. Do you know of anyone who 
has one? In the U.K. of course the license fee is cheaper for B/W so that 
will encourage some people.

> Are you (Pete or anyone else) aware of any large companies that still 
> produce monthly (or quarterly or year-end)  bills/statementes that have 
> converted such procesisng to any OO solution?  I would think there must be 
> SOME somewhere, but I certainly haven't heard of this being common.
>

I can't confirm for sure, so I can't comment. Certainly a bank that is 
running a completely networked system that uses objects locally and 
remotely, along with web services and web based accounting, probably 
qualifies. I know a few of these, but I can't confirm that they don't also 
still use batch processing for their back office. This comes back to the 
discussion we had a while ago about the blurring of front and back office 
processing. Eventually, there will only be processing and it will be 
transactional. I know of a number (more than 6, less than a dozen) of large 
organizations which are moving that way (including my own bank, mentioned 
above) but iI cannot confirm that they are there yet.

I think that as the world changes its mind about batch processing and hard 
copies, so will the systems. It won't be next week :-)

Pete.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-07-07T17:07:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com>`
- **In-Reply-To:** `<DRKji.112754$Xu1.100559@fe07.news.easynews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com>`

```
William M. Klein wrote:
  > It seems to me that for "day-to-day" buiseness needs - having "real 
time access
> to information" is the critical requirement of much of IT.  On the other hand, 
> for "tracking and auditor and regulation" purposes, it seems to me that the need 
> for (remarkly frequently changing) hard-copy reports is growing, not 
> diminishing.

Not necessarily.  In fact, reliable electronic records are growing more 
important.  We have an entire "Electronic Records Management" (ERM) 
system, with various levels of training required based on what level of 
responsibility you have.

My previous message praising XML is also rooted in experience.  DoD has 
mandated that all data interchange between system be in XML.  It's 
bulkier, but we've got the bandwidth.  With an XSD schema applied, it 
can actually validate the data before it's sent to the receiving system.

> As a COBOL report writer fan, these types of reports can EASILY be produced and 
> modified in COBOL.  As a "Workstaion-attached PDF and 'graphic' report fan, I 
> would think that COBOL  is not a good (much less the best) tool for the job.>

Report Writer can even be used to generate XML, although it's output is 
not the most efficient.  Ideally, in an OO environment, you would have 
an XML document object, and let it deal with generating the actual XML. 
  A guy I heard last week said "XML is sort of like lye; it's very 
useful in small quantities, but you should never touch it with your bare 
hands."  :)

> P.S.  "Monthly" hard-copy (or soft - but looks like hard copy) bills are anoterh 
> place where "batch COBOL-type" processing works well - IMHO.  Again, although 
…[11 more quoted lines elided]…
> I certainly haven't heard of this being common.

I'm not sure - I know that the only hard-copy bill I get now is from 
Comcast.  :)  I think that approved electronic records are gaining in 
popularity.  What they're generated with, though, I'm not sure.  I know 
that the biggest request we have is for Excel files; we've found that if 
we send an HTTP header with the content type as excel (not quite sure of 
the exact value), then output an HTML table.  Once it's in Excel, they 
can slice and dice and do their analysis; I doubt anyone is printing 
them out.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 10)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2007-07-09T11:17:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184005071.921556.98990@57g2000hsv.googlegroups.com>`
- **In-Reply-To:** `<nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com>`

```
On Jul 7, 7:07 pm, LX-i <lxi0...@netscape.net> wrote:
> William M. Klein wrote:
>
…[11 more quoted lines elided]…
>

My experience in the FDA-regulated and FDA-audited world is that
things are moving to "paperless", but hmmmm, not quickly, only
steadily, if not downright slowly. One can google "21 CFR Part 11" for
FDA guidance regarding Electronic Records / Electronic Signatures (ER/
ES) systems to replace paper systems.

For what the FDA calls "commissioning", "qualification", and
"validation" of hardware/software systems that involve "direct
contact" with the manufacture of medical products, I believe there is
still a significant bias toward a paper hardcopy product that one can
afix a traditional ink pen signature to.

In a tangentially related matter, some years back I had occasion to
ask a CPA an opinion about a business matter. I got one opinion "over
the phone", and after asking for one in writing, got a completely
different opinion word-processed upon a piece of paper, along with an
invoice for a couple of hundred dollars, for a couple of hours work.
The paper had only the printed name of the CPA at the bottom, under
the text of the opinion.

I sent it back for a _signature_ before I paid.

To this day I am still somewhat uncertain whether I was just being a
jerk, or if I was making a legitimate "statement". Anyway, I got the
signature on the next version, and then I signed mine to the check,
and sent it off.

Fair exchange.

Ken
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 11)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-09T11:49:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184006973.926455.246540@w3g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<1184005071.921556.98990@57g2000hsv.googlegroups.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com>`

```
On 9 Jul, 19:17, "klsha...@att.net" <klsha...@att.net> wrote:
> On Jul 7, 7:07 pm, LX-i <lxi0...@netscape.net> wrote:
>
…[19 more quoted lines elided]…
> Ken

A signed document, to which you adhere, would not remove your
liability for non-conformance.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 12)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2007-07-09T12:01:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184007718.342668.279250@w3g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<1184006973.926455.246540@w3g2000hsg.googlegroups.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com>`

```
On Jul 9, 2:49 pm, Alistair <alist...@ld50macca.demon.co.uk> wrote:
> On 9 Jul, 19:17, "klsha...@att.net" <klsha...@att.net> wrote:
>
…[30 more quoted lines elided]…
> - Show quoted text -

Agreed, for civil liability anyway. I do remember having the feeling
that my requiring a signature established some due diligence on my
part which, perhaps naively, I believed would offer me some defense in
any criminal liability, however. The numbers were such that I was
really being overly cautious anyway.

Ken
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-07-09T13:41:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com>`

```
On Mon, 09 Jul 2007 12:01:58 -0700, "klshafer@att.net"
<klshafer@att.net> wrote:

>Agreed, for civil liability anyway. I do remember having the feeling
>that my requiring a signature established some due diligence on my
>part which, perhaps naively, I believed would offer me some defense in
>any criminal liability, however. The numbers were such that I was
>really being overly cautious anyway.


I notice the sign in the locker room saying "Not Responsible for Lost
or Stolen Items".    I take this to mean primarily "Please do not sue
us".   While their legal protection is probably a little more, their
biggest protection is in persuading us to be a bit more responsible.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 14)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2007-07-09T12:52:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184010765.799055.242070@n60g2000hse.googlegroups.com>`
- **In-Reply-To:** `<pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com>`

```
On Jul 9, 3:41 pm, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 09 Jul 2007 12:01:58 -0700, "klsha...@att.net"
>
…[10 more quoted lines elided]…
> biggest protection is in persuading us to be a bit more responsible.

Exactly. The other feeling I remember having is along the lines of,
"I've just paid a hundred dollars an hour for an expert opinion. I
deserve to know for sure that it was the CPA herself who wrote this
up, and who is responsible for it, and not just some intern sending
out the text under the CPA's letterhead."

I believe it is this kind of accountability which is behind the
"signature requirement", whether it be ink-pen or ER/ES (established
by secure password.)

Ken
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 14)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-10T11:18:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184091531.720739.12080@r34g2000hsd.googlegroups.com>`
- **In-Reply-To:** `<pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com>`

```
On 9 Jul, 20:41, Howard Brazee <how...@brazee.net> wrote:
> On Mon, 09 Jul 2007 12:01:58 -0700, "klsha...@att.net"
>
…[10 more quoted lines elided]…
> biggest protection is in persuading us to be a bit more responsible.

In the UK, a garage put up a sign saying that they were not
responsible for accidents on their forecourt. They lost their case
when sued by an aggrieved driver.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 15)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-07-10T14:29:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net>`
- **In-Reply-To:** `<1184091531.720739.12080@r34g2000hsd.googlegroups.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com>`

```
Alistair wrote:
> On 9 Jul, 20:41, Howard Brazee <how...@brazee.net> wrote:
>> On Mon, 09 Jul 2007 12:01:58 -0700, "klsha...@att.net"
…[15 more quoted lines elided]…
> 

"I am not responsible for banks I rob" does not work either. I do not 
know anywhere that putting up a sign cancels your legal obligations. 
They are no more than legal posturings.

Donald
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 16)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-07-10T13:22:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kum79314pmoou6h6ik9r20d3junptulca6@4ax.com>`
- **References:** `<5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net>`

```
On Tue, 10 Jul 2007 14:29:27 -0400, donald tees <donald@execulink.com>
wrote:

>"I am not responsible for banks I rob" does not work either. I do not 
>know anywhere that putting up a sign cancels your legal obligations. 
>They are no more than legal posturings.

There is some protection - if I tell a customer that this is beta code
and it doesn't work, I doubt if they can sue.   And a sign saying
"keep of the ice" might protect me from an adult who fell through the
lake in my back yard.

It just is one piece of evidence to show that I am not negligent.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 17)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-07-10T16:47:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S_-dnUduVPHWbQ7bnZ2dnUVZ_hadnZ2d@golden.net>`
- **In-Reply-To:** `<kum79314pmoou6h6ik9r20d3junptulca6@4ax.com>`
- **References:** `<5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <kum79314pmoou6h6ik9r20d3junptulca6@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 10 Jul 2007 14:29:27 -0400, donald tees <donald@execulink.com>
> wrote:
…[10 more quoted lines elided]…
> It just is one piece of evidence to show that I am not negligent. 

Neither are are a valid defense in this country. Telling somebody that 
something may not work does not alleviate your responsibility a whit.

When you sell it, you take responsibility, like it or not. If you have 
no responsibility towards the safety of your lake, then you are not 
responsible for those that drown.  However, if it is your job to provide 
a lifeguard, then you can post signs 'til hell freezes over, and you are 
still responsible when someone drowns.

Donald
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 17)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-11T11:27:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184178449.132882.114080@m3g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<kum79314pmoou6h6ik9r20d3junptulca6@4ax.com>`
- **References:** `<5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <kum79314pmoou6h6ik9r20d3junptulca6@4ax.com>`

```
On 10 Jul, 20:22, Howard Brazee <how...@brazee.net> wrote:
> On Tue, 10 Jul 2007 14:29:27 -0400, donald tees <don...@execulink.com>
> wrote:
…[10 more quoted lines elided]…
> It just is one piece of evidence to show that I am not negligent.

So, knowing that  there is a problem (thin ice) and doing nothing
absolves you of negligence? In the UK, the sign indicates knowledge
and the accident indicates negligence. The sign 'beware of the dog'
does not absolve you from responsibility for the dog's actions. It
just makes your payout to the burglar so much bigger.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 17)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-11T11:30:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184178636.717806.216850@n2g2000hse.googlegroups.com>`
- **In-Reply-To:** `<kum79314pmoou6h6ik9r20d3junptulca6@4ax.com>`
- **References:** `<5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <kum79314pmoou6h6ik9r20d3junptulca6@4ax.com>`

```
On 10 Jul, 20:22, Howard Brazee <how...@brazee.net> wrote:
> On Tue, 10 Jul 2007 14:29:27 -0400, donald tees <don...@execulink.com>
> wrote:
…[10 more quoted lines elided]…
> It just is one piece of evidence to show that I am not negligent.

Further to my post in response to this posting I should add that
putting up the sign and a fence to prevent people from getting to the
ice also will not protect you from legal claims if the fence is poorly
maintained (or the dog in the other example is not properly muzzled)
or not tall enough to prevent easy access. My father successfully sued
on the improper maintenance case when I was blinded in my right eye as
a kid.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 16)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-07-10T16:50:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com>`
- **In-Reply-To:** `<x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net>`

```
donald tees wrote:
> 
> "I am not responsible for banks I rob" does not work either. I do not 
> know anywhere that putting up a sign cancels your legal obligations. 
> They are no more than legal posturings.

I personally don't care for the litigious lifestyle.  I currently don't 
know where a swimming pool is with a diving board.  This happened when 
pools had diving boards, and any time someone screwed up their dive and 
hurt themselves, they'd sue the pool owner.

It would be nice if people would just use their judgment to analyze a 
situation, then accept responsibility for the outcome of their actions. 
  Heresy, I know...
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 17)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-07-10T19:37:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eO-dnYWJpsDQhQnbnZ2dnUVZ_ufinZ2d@golden.net>`
- **In-Reply-To:** `<jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com>`

```
LX-i wrote:
> donald tees wrote:
>>
…[12 more quoted lines elided]…
> 

In Ontario, it is illegal for a lawyer to work on commission.  To sue, 
you have to hire a lawyer and pay them, win or lose. It makes for far 
less lawsuits, though the sins of the insurance industry are limiting 
our freedoms far more than legislation.

Donald
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 18)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-07-10T21:58:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9LSdnZnm4YQVyAnbnZ2dnUVZ_jqdnZ2d@comcast.com>`
- **In-Reply-To:** `<eO-dnYWJpsDQhQnbnZ2dnUVZ_ufinZ2d@golden.net>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com> <eO-dnYWJpsDQhQnbnZ2dnUVZ_ufinZ2d@golden.net>`

```
donald tees wrote:
> LX-i wrote:
>> donald tees wrote:
…[17 more quoted lines elided]…
> less lawsuits,

That sounds good.  Almost as good as "loser pays."  :)

> though the sins of the insurance industry are limiting 
> our freedoms far more than legislation.

What sins would those be?
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 19)_

- **From:** donald tees <donald@execulink.com>
- **Date:** 2007-07-11T00:05:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RrWdne-FrP2QygnbnZ2dnUVZ_jydnZ2d@golden.net>`
- **In-Reply-To:** `<9LSdnZnm4YQVyAnbnZ2dnUVZ_jqdnZ2d@comcast.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com> <eO-dnYWJpsDQhQnbnZ2dnUVZ_ufinZ2d@golden.net> <9LSdnZnm4YQVyAnbnZ2dnUVZ_jqdnZ2d@comcast.com>`

```
LX-i wrote:
> donald tees wrote:
>> LX-i wrote:
…[26 more quoted lines elided]…
> 
Well, for example, it is impossible to put on a fireworks display 
anymore, as the law mandates liability insurance, and the premiums are 
simply too high.

Donald
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 17)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-11T11:31:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184178692.257568.69830@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com>`

```
On 10 Jul, 23:50, LX-i <lxi0...@netscape.net> wrote:
> donald tees wrote:
>
…[11 more quoted lines elided]…
>   Heresy, I know...

Are you really an American?     :-)
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 18)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-07-11T20:21:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dp6dnQPLlqbEDQjbnZ2dnUVZ_urinZ2d@comcast.com>`
- **In-Reply-To:** `<1184178692.257568.69830@d55g2000hsg.googlegroups.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com> <1184178692.257568.69830@d55g2000hsg.googlegroups.com>`

```
Alistair wrote:
> On 10 Jul, 23:50, LX-i <lxi0...@netscape.net> wrote:
>> donald tees wrote:
…[13 more quoted lines elided]…
> Are you really an American?     :-)

Last time I checked...  :)  We all used to feel that way.  Imagine what 
this country would be like if, every time a wagon wheel came off, the 
settlers went back to the city where they started, so they could file a 
lawsuit with the carriage-making company...
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-12T16:53:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5flqf1F3da3p4U1@mid.individual.net>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com> <1184178692.257568.69830@d55g2000hsg.googlegroups.com> <Dp6dnQPLlqbEDQjbnZ2dnUVZ_urinZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:Dp6dnQPLlqbEDQjbnZ2dnUVZ_urinZ2d@comcast.com...
> Alistair wrote:
>> On 10 Jul, 23:50, LX-i <lxi0...@netscape.net> wrote:
…[19 more quoted lines elided]…
> lawsuit with the carriage-making company...

:-)
This is excellent, Daniel. I shall unashamedly steal it (with proper 
attribution, of course...)

Pete.
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 19)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-07-12T08:21:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f74oa2$das$1@reader2.panix.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com> <1184178692.257568.69830@d55g2000hsg.googlegroups.com> <Dp6dnQPLlqbEDQjbnZ2dnUVZ_urinZ2d@comcast.com>`

```
In article <Dp6dnQPLlqbEDQjbnZ2dnUVZ_urinZ2d@comcast.com>,
LX-i  <lxi0007@netscape.net> wrote:

[snip]

>Imagine what 
>this country would be like if, every time a wagon wheel came off, the 
>settlers went back to the city where they started, so they could file a 
>lawsuit with the carriage-making company...

Well, the broken wagon-wheel might not be as common a home-decoration as 
it is now...

... and the population and conditions of the American aboriginal 
population might be a bit different, as well.

DD
```

###### ↳ ↳ ↳ Re: Hard Copy reports

_(reply depth: 19)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-12T09:25:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184257549.429230.22840@q75g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<Dp6dnQPLlqbEDQjbnZ2dnUVZ_urinZ2d@comcast.com>`
- **References:** `<5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <nNadnTQEQLQkgQ3bnZ2dnUVZ_rKvnZ2d@comcast.com> <1184005071.921556.98990@57g2000hsv.googlegroups.com> <1184006973.926455.246540@w3g2000hsg.googlegroups.com> <1184007718.342668.279250@w3g2000hsg.googlegroups.com> <pm3593hu6p22ieemlj3df4crl0s3ub76ov@4ax.com> <1184091531.720739.12080@r34g2000hsd.googlegroups.com> <x62dnW1VKZFgUg7bnZ2dnUVZ_s3inZ2d@golden.net> <jIudnUSgHPPbkAnbnZ2dnUVZ_sSmnZ2d@comcast.com> <1184178692.257568.69830@d55g2000hsg.googlegroups.com> <Dp6dnQPLlqbEDQjbnZ2dnUVZ_urinZ2d@comcast.com>`

```
On 12 Jul, 03:21, LX-i <lxi0...@netscape.net> wrote:
> Alistair wrote:
> > On 10 Jul, 23:50, LX-i <lxi0...@netscape.net> wrote:
…[20 more quoted lines elided]…
>

Or what might have happened if the US had sued Sitting Bull before the
Little Big Horn rather than hounding him with Goldilocks and the
Seventh Cavalry.
```

###### ↳ ↳ ↳ Re: Hard Copy reports (was: Regular Expressions and Standard COBOL

_(reply depth: 9)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2007-07-07T22:57:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kiZji.12420$aP2.11947@newsfe16.lga>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com>`

```

> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:5f8o2sF3amt6qU1@mid.individual.net...
…[9 more quoted lines elided]…
> > That's the nub of it. Until people start to realise that paper reports
are
> > really not as valuable as they have been any more, there will continue
to be
> > managers who demand them. These days it is about INFORMATION. It needs
to be
> > timely (up to the millisecond), easily digestible (graphic and
summarised,
> > with drill down capabilities) and it should only be committed to paper
as a
> > last resort.
>

I would question this.  Suppose you have a on-line project status report.
It is up to the second as of 9a.m. but  a whole swag of updates and
corrections come by at 9:03a.m.  Therefore  you must re-query the report at
9:04a.m.  And that'll go on all day.  If you're going to take action based
on the information that you have available, it by definition is the
information that you have at that point in time, regardless of whether it's
been updated 3 seconds later or not.  Sooner or later you have to drop out
of real time and decide what you're going to do.  Sooner or later you're
going to have to live with the fact that the decisions you've made may have
been based on slightly out-of-date information.  Otherwise you will reread
and reread... ad infinitum and never do anything!  Either that or you wait
until some time when you KNOW there aren't going to be any updates for a
while - or mandate it that no updates will occur for an hour or so - which
means that it won't be real time any more anyway.

PL
```

###### ↳ ↳ ↳ Re: Hard Copy reports (was: Regular Expressions and Standard COBOL

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-09T01:44:12+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fc81dF3bou4tU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <kiZji.12420$aP2.11947@newsfe16.lga>`

```

"tlmfru" <lacey@mts.net> wrote in message 
news:kiZji.12420$aP2.11947@newsfe16.lga...
>
>> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[42 more quoted lines elided]…
>

OK, some further clarification...

The on-line status report  (under the ideal scenario, which was the basis of 
my post and is still being sought by many organizations) would not be "up to 
the second as of 9:00 am". It would be in either of two states:

1. As of a specific time which you request. (Could be yesterday, could be 
last week, could be as of 5 minutes ago...)

2. (By default) as of right now.

And yes, you are quite correct that a bunch of events could happen a few 
minutes (or seconds) after you looked at it, that invalidate it. BUT, 
provided you know the point on the timeline that your information reflects, 
you are no worse off than you would be with a batch report dated yesterday. 
And at least you CAN re-query (right now) if you suspect something 
extraordinary may have happened.

Obviously, to be able to achieve this, the information processing capability 
has to be outstanding.  The techniques currently employed may not be up to 
it (any form of sequential processing, unless it is across a limited result 
set on very powerful hardware, is unlikely to do it).

Although this type of information retrieval is already in place in some 
organizations, (using conventional data access, but with carefully designed 
and networked databases that can leverage parallel processing, and usually 
summarized (pivot table or cube)) levels of the data warehouse), it is 
limited to only certain applications.

Organizations going down this path will be looking to emerging techniques 
for data handling  and increases in processor and data storage power, in 
order to implement it fully.

This means Query Syntax (which generates Lambda functions that can be 
deferred and parallel processed, against any kind of data -not just 
Relational - 
http://weblogs.asp.net/scottgu/archive/2007/04/21/new-orcas-language-feature-query-syntax.aspx - 
it looks like SQL, and SQL can be easily converted to it, but it is MUCH 
more powerful in its execution than existing SQL could ever hope to be), 
functional programming, deferred evaluation, and use of multiple cores. This 
is without considering new breaktrhroughs in storage technology that mean 
much more data can be accessed much faster, and the coming of age of content 
addressable stores that will completely change the way data is stored and 
accessed.

In fact, I believe the goal of "outstanding information processing 
capability" mentioned above will be achieved by 4 factors, some of which are 
already here and the others are not more than 10 years away (already 
established "proof of concept"...):

1. Query Syntax. (Enabling Lambda functions and deferred processing on 
multiple simultaneous cores)
2. New (possibly molecular) storage capability which will pack large amounts 
of data into very small spaces so enabling faster access to it.
3. Increased CPU processing power with multiple cores.
4. Exponential increase in Network bandwith, with wireless replacing fiber.

We have the software approaches, can evolve "what we do now" fairly easily 
into "what we are gonna do...", and the new technology is hardware 
independent; it runs on what we have now, and will run on what we can see in 
the medium future.

It won't happen overnight, but there are already organizations who are 
moving towards a complete transactional processing model. (I already my 
mentioned my Bank, and I know an insurance company who are going completely 
to web services and transactional processing, using the network.  Currently, 
they still use a mainframe as well, but their long term plan is to phase out 
and refactor the COBOL based systems on it. The tools outlined above will 
make it possible.)

Obviously, Client/Server networks are really not interested in Batch 
processing and would much rather see this sidelined to an "offline" 
mainframe, or, better still, eliminated altogether.

When you think about it, from the time we first saw green 3270 screens being 
driven in 32K from Foreground 1, on a partitioned DOS mainframe, many of us 
just wanted ALL processing to work like that...:-)

On-line processing is more fun to write, provides a more timely, more 
interactive experience for the user, and enables a far better model of the 
real world to be maintained by the system. The only thing that stopped us 
doing it long ago was that we simply didn't have the resources to update 
everything within a two second envelope. So, we wrote transaction files and 
batch processed them later. The batch process can join tables, filter, sort, 
do whatever is necessary and (provided it doesn't exceed the Holy Overnight 
Batch Window) we are ready to go again the following morning. For data 
retrieval we could tolerate it taking a few more seconds, but it would be a 
whole lot more pleasant if it didn't.

Try and imagine a Data Warehouse with asynchronous "agents" runnning on 
different servers that are constantly consolidating, organizing, building 
pivots and cubes, as real time transactions are processed across the 
network. As fast as events occur they are processed, and the data model is 
accurate to within milliseconds. (Every item timestamped and available to 
other reporting agents that can extract data in parallel and asynchronously 
bring it to a presentation layer. Then top it off with still further 
processes that archive everything.)

It takes a lot of processor power, network capability, and very fast data 
storage. Previously, we didn't have it, now we are on the threshold of it.

Within a few years it will be freely available.

Pete.
```

###### ↳ ↳ ↳ Re: Hard Copy reports (was: Regular Expressions and Standard COBOL

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-07-09T12:06:14-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v3u493lvb2nlhpueecqu54g3opdhb5ate2@4ax.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <kiZji.12420$aP2.11947@newsfe16.lga> <5fc81dF3bou4tU1@mid.individual.net>`

```
On Mon, 9 Jul 2007 01:44:12 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>1. As of a specific time which you request. (Could be yesterday, could be 
>last week, could be as of 5 minutes ago...)
>
>2. (By default) as of right now.

I haven't had to worry about this - but for some applications "right
now" has to be adjusted to mean "the point of time that this
transaction started".     A report that takes 5 minutes to compile in
a real time environment might have some unacceptable blurring.
```

###### ↳ ↳ ↳ Too big to build (was Hard Copy reports)

_(reply depth: 11)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2007-07-09T23:22:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MRDki.45388$aP2.39017@newsfe16.lga>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <kiZji.12420$aP2.11947@newsfe16.lga> <5fc81dF3bou4tU1@mid.individual.net>`

```

Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message > >> >
>
> 1. Query Syntax. (Enabling Lambda functions and deferred processing on
> multiple simultaneous cores)
> 2. New (possibly molecular) storage capability which will pack large
amounts
> of data into very small spaces so enabling faster access to it.
> 3. Increased CPU processing power with multiple cores.
> 4. Exponential increase in Network bandwith, with wireless replacing
fiber.
>

Re point 2: I've written a rather tongue-in-cheek essay to prove that, given
a few assumptions - the most important one being that we stick with current
technology - a computer with 2**64 bytes memory space would be a minimum of
40 x 40 x 82 metres!

PL
```

###### ↳ ↳ ↳ Re: Too big to build (was Hard Copy reports)

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-10T22:44:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fh67vF3cjdmeU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <23vs83hk665ks484ctf7vdcsspi79erhaq@4ax.com> <5f8o2sF3amt6qU1@mid.individual.net> <DRKji.112754$Xu1.100559@fe07.news.easynews.com> <kiZji.12420$aP2.11947@newsfe16.lga> <5fc81dF3bou4tU1@mid.individual.net> <MRDki.45388$aP2.39017@newsfe16.lga>`

```

"tlmfru" <lacey@mts.net> wrote in message 
news:MRDki.45388$aP2.39017@newsfe16.lga...
>
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message > >> >
…[18 more quoted lines elided]…
>

:-)

Ah, those were the days... remember the first 360s...? 2**15 bytes in 10 x 
10 x 3 metres...(with false flooring and peripherals...)

http://sanjose.bizjournals.com/sanjose/stories/2005/02/21/story5.html

Pete.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-06T17:09:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<138tbv0h4hkd243@corp.supernews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5f79m1F3a58vtU1@mid.individual.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[30 more quoted lines elided]…
> >> Well, thank you for the improved RE string. However that wasn't the
point
> > of
> >> the post. (And I have been using the "lame" string for some time now
…[12 more quoted lines elided]…
> here, as it was I who posted (in response to a request from someone else)
an
> example which I use, and contrasted it with what would be required in
COBOL
> to achieve the  same end, I believe I have every right to post the
response
> I did above.

You have a right to respond in any way you like. But, I
believe my reaction would have been the same, or at least
similar, regardless of who posted it. In fact, if you check
the prior posts, you will find I posted an RE for checking
e-mail addresses about 20 minutes before your posting of
one. We both responded to the same post by Mr Brady.

Now, try to imagine *my* reaction! A much shorter RE
said to accomplish about the same thing. Preposterous!

>
> I called it "lame", explained why, then
…[4 more quoted lines elided]…
> was about.

When you reposted that RE, in this thread, I felt a need
address the issue and without regard for the immediate
topic of discussion.

>
> You went to levels of detail which were quite unnecessary, as you always
do,
> in pursuit of something which really isn't worth the effort. Nobody cares
> whether a particular  (more complex) RE is better for validating email
> strings in 1 out of a couple of thousand cases; as I pointed out, if it
was
> REALLY important, the address would be validated by pinging anyway.

Mr Dashwood, you may have found the level of detail
to be unnecessary, others may have not. My suspecting
that some others, in this group, have no knowledge of REs,
I felt others mught appreciate a full explanation of what they
were seeing. Once agian, it was never about you!

> The point of the conversation is whether or not this facility could or
> should be part of COBOL. You came up with a whole bunch of problems
(without
> doing detailed investigation) that would preclude it. I suggested some
> alternatives that would make it fairly easy.

I did not miss that.

> >My
> > comments were intended for others who might have been
> > tempted to use that RE without understanding its limitations
>
> Ha! Given that people using COBOL are unlikely to try and use RE anyway,
and
> given that I posted a full explanation of what it did when I first posted
> it, that would seem somewhat superfluous.

Mr Dashwood, people using COBOL are unlikely to use
what they do not know about. You had complained there
was no interest in discussing REs a year ago. Now they
have been discussed. Those who are interested will
investigate further. Ultimately, what they may do depends
upon their needs.

> > It was an alternative and, in that sense, no different than your
> > presenting C# as an alternative to COBOL; though I wish
…[5 more quoted lines elided]…
> replacement. Too bad if that offends you; your pedantry has the same
effect
> on me.

"(I'm "guilty" of mentioning C#, certainly, but only in the context of
alternatives to COBOL. Why should we consider alternatives to COBOL? See
below...)"

Perhaps you do not recall having written that!

> >
> >
…[3 more quoted lines elided]…
> >> existing components, or not). Instead, it seems that everything has to
be
> >> spelled out to last detail with people who are not even writing the
> > compiler
…[13 more quoted lines elided]…
> be re-invented.

H'm! Functional or portable, choose one. In the COBOL
standard, there is functionality that is implementor-defined;
but this functionality has little or no effect on portability of
source code. For example, the specifications of COMP
and PACKED-DECIMAL are functional.

> Reading your post just makes me thankful we have vendors who are pragmatic
> enough to simply get on and do it... There'd be no COBOL if it was left to
> COBOL committees.

Eventhough, some vendors participate on those committees?

> >
> > This means for specifying a regular expression and the
…[7 more quoted lines elided]…
> Nope. It is NOT necessary to go to that level of detail. There are
existing
> standards for RE. These could be referenced and vendors could make their
own
> choice within an existing standard. The same applies to XML. It is YOU
> personally, who wants to look at every single metacharacter because that
is
> your nature. Most people don't. Neither do they need to.

Perhaps, most people do not take the viewpoint required
to understand the process for amending the COBOL standard.
I look at such things because I know that J4 will look at such
things and it is in my nature to try to anticipate problems.

>
>
…[9 more quoted lines elided]…
> invented. PICTURE was developed to remove the necessity to code SIZE,
CLASS
> and USAGE, as we had to do in the early implemations of COBOL. In fact, to
> this day you can define data fields in COBOL without using PICTURE.

No, implementors could not choose C-type format strings
because such strings would not conform to the standard;
but, if you like, substitute FORTRAN-type formats; same
result.

> My point is that PICTURE was NOT a re-invention of the wheel; it was a
> useful addition to the language which saved people time.
>
> As for portability, COBOL isn't portable anyway. The best you can do is
hope
> to keep it less of a hassle to convert by using a strict subset of
> constructs. It doesn't have the portability of Java or of C#.

Implementors claiming conformance to the standard are
required to provide a means for identifying which constructs
do not conform. Most of what affects portability is confined
to the environment division.

Portability of Java and C# is irrelevant in a COBOL
newgroup. <g>

> >
> >> As is often the case with procedural programming, the focus is on HOW
…[5 more quoted lines elided]…
> No, I know. It's sad...

Well, you could have rephrased and tried again.

> >
> > Procedure-names, function-names, and method-names
…[10 more quoted lines elided]…
> has to be the way to go...

Well, no! The Power PC, as I understand it, can execute
multiple integer and floating-point operations, each, at the same
time.

> >
> > Object-Oriented programming, functional programming, and
…[3 more quoted lines elided]…
> Sure. If all you can see is a programming problem...

Programming methods to partition programming problems.
Seem to follow naturally!

> >
> > I see conceptual and practicable differences among these;
…[3 more quoted lines elided]…
> Perhaps you need more practice at looking?

Or, you might try to understand that I don't see what you
see and then try to understand why. For example, a great
deal of what has been put forth as Object-Oriented
programming, I see as implementation of procedural
or functional design; that is, decide what procedures or
functions to perform and put them into methods. I see this
happening; but I'm reasonably sure those doing the
programming don't understand they are doing it. Mind
you, I no longer seek out cases where this happens; but
I've seen enough to recognize the pattern.

What I have rarely seen is implementation of an
Object-Oriented design, which, it seems to me, is the
point of Object-Orientation.

> >>
> >> >
…[18 more quoted lines elided]…
> >> Unfortunately, their solutions are not always the best. Again, as long
as
> >> the focus is on source code (let's generate a sub-program...) instead
of
> >> functionality (we need some functionality; does it exist? How could we
> >> incorporate it or use it?), the solution is going to be a less than
…[10 more quoted lines elided]…
> I don't get emotional about programming languages. C# exists because it
gets
> the job done.

Of course you get emotional about progamming languages!
You convey that emotion by raving about C# and by damning
COBOL. You did the same with Java. You do it with SQL
versus COBOL ISAM.

Love and hate are emotions; their opposite is apathy. If you
didn't care, you wouldn't express opinions about programming
languages!

> If it stopped doing that, I'd move to something else. As to commerce
> re-inventing existing wheels, perhaps you'd like to run that argument past
> all the people who moved from COBOL to SAP, Siebel, Peoplesoft and Oracle
in
> the last few years... ?

Do you mean from COBOL to group of re-invented wheels
trying to gain a commercial advantage over each other?
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-07-06T23:08:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6mi13$kb9$1@reader2.panix.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com>`

```
In article <138tbv0h4hkd243@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:

[snip]

>Love and hate are emotions; their opposite is apathy.

Oh, I *cannot* resist...

... love and hate are conditions that you can work up some feeling 
about... as for apathy, who cares?

DD
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-07T07:21:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183818066.878643.299190@n2g2000hse.googlegroups.com>`
- **In-Reply-To:** `<f6mi13$kb9$1@reader2.panix.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <f6mi13$kb9$1@reader2.panix.com>`

```
On 7 Jul, 00:08, docdw...@panix.com () wrote:
> In article <138tbv0h4hkd...@corp.supernews.com>,
>
…[11 more quoted lines elided]…
> DD

I can not resist either...

Apathetic people may care but are not inclined to do anything about
it.


And as for the toing-and-throing in the thread; I am reminded that
there is no zealot like a convert. This may explain PD's enthusiasm
for OO, Java, C# and RDBMS observed elsewher in the thread..
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-08T05:32:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fa115F39nqvbU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <f6mi13$kb9$1@reader2.panix.com> <1183818066.878643.299190@n2g2000hse.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1183818066.878643.299190@n2g2000hse.googlegroups.com...
> On 7 Jul, 00:08, docdw...@panix.com () wrote:
>> In article <138tbv0h4hkd...@corp.supernews.com>,
…[23 more quoted lines elided]…
>
Yes, or it could be that I'm just enthusiastic by nature. Funny, I've never 
thought of it as being a bad thing...or needed to apologize for it.

And I am neither convert (I still use COBOL, but recognise its limitations 
and where it is going) nor zealot. Please don't apologise for me, if that is 
what you were doing.

Pete.

I'm starting to think that my work here is done. It isn't fun any more and 
ly think my work here is done.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-07T20:10:50+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5f904cF3bffdfU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com>`

```
This is my last response on this.

See below.

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:138tbv0h4hkd243@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[64 more quoted lines elided]…
> one. We both responded to the same post by Mr Brady.

Except that Mr Brady was responding to a post from me.

>
> Now, try to imagine *my* reaction! A much shorter RE
> said to accomplish about the same thing. Preposterous!
>

Nope. That's what it does. You never considered the spec which accompanied 
it, instead you decided a whole lot more stuff was required. In reality, the 
only effective way to check an email address is to mail to it  (and even 
that is not foolproof). You were so excited by a chance to expound on REs 
that you lost sight of what the actual requirement was.

>>
>> I called it "lame", explained why, then
…[23 more quoted lines elided]…
> were seeing. Once agian, it was never about you!

You keep saying that.. I never considered it was about me, and never have 
considered that in any posts here, apart from off-topic ones regarding 
personal beliefs or opinions.  I don't actually need the approval of CLC (or 
you) in order to feel good about myself. What I described was subjective 
experience using REs. You were so outraged that I would use a MS 
implementation ("perversion" was the condescending word you used; why don't 
you ask the millions of people who use MS REs every day whether they think 
it is a "perversion"?)  that you jumped into a conversation that was nothing 
to do with you, and decided the innocent masses must be protected, by boring 
them to death. No-one actually asked you; but you felt it was important... 
then you try to say it isn't about me :-). At least I respond when I'm 
asked, I don't assume people are waiting to hang on my every word. It's a 
public forum; anyone can post anywhere, but you could have started another 
thread for  your soapbox.

I found your post hostile, condescending, and not of much real value. So 
that's one man's opinion. Unfortunately it prompted me to respond in kind 
and that is just as stupid. I won't be doing it any more.



 >
>> The point of the conversation is whether or not this facility could or
…[18 more quoted lines elided]…
> was no interest in discussing REs a year ago.

It was not a complaint, it was an observation. I actually couldn't care less 
whether people use REs or they don't. I'm not driven to expound on it and 
responded only when someone asked me to.

Now they
> have been discussed. Those who are interested will
> investigate further. Ultimately, what they may do depends
> upon their needs.

Gosh, d'you think...?
>
>> > It was an alternative and, in that sense, no different than your
…[14 more quoted lines elided]…
> Perhaps you do not recall having written that!

I certainly do recall writing that, and, like everything I write, it was 
true at the time. However, since then, I have moved on and my opinion is now 
as stated above. Some of us don't live in a fixed condition and reserve the 
right to change our minds in the light of new experience. I started out 
seeing C# as a possible alternative to COBOL. And it was not the only one I 
considered. Tried it, liked it, got more facile with it, now I'm happy with 
it. End of story.

The fact that you would search archives to try and make me look 
inconsistent, speaks volumes to me. I suppose that kind of attack "isn't 
about me" either?

It was that single comment from you that made me decide to respond to this 
thread.

>
>> >
…[24 more quoted lines elided]…
> H'm! Functional or portable, choose one.

The two are only mutually exclusive in your mind.


>In the COBOL
> standard, there is functionality that is implementor-defined;
…[10 more quoted lines elided]…
> Eventhough, some vendors participate on those committees?

I'm glad you mentioned that (I wouldn't have... it would be a cheap shot.) 
Care to comment on exactly how many vendors have withdrawn their support in 
...ooh, say, the last 5 years?  No? Yes, probably best not to...
>
>> >
…[21 more quoted lines elided]…
>

I guess that's how you developed your scratch 'n sniff methodology...

>>
>>
…[19 more quoted lines elided]…
> result.

Thankfully, at the time PICTURE was introduced, COBOL was in much better 
hands than it is today. They actually produced a standard that was simple 
and easily implemented. Vendors had no need to resort to non-standard 
strings because the standard was simple, clear, and straightforward. It 
wasn't written in legalese by pedants who would agonise over the 
interpretation of every word. (Neutral readers might like to try reading the 
2002 standard and draw their own conclusions.)


>
>> My point is that PICTURE was NOT a re-invention of the wheel; it was a
…[10 more quoted lines elided]…
> to the environment division.

Ever done any porting of COBOL across platforms? I have. It is a non-trivial 
exercise. The people who invented COBOL had vision and a dream of a language 
that would run on ANY mainframe (That's all there was at the time). Over the 
years that vision has become so corrupted (sometimes necessarily, in the 
pursuit of competitive advantage...) that it is no longer true. If there had 
been a strong and effective standards body (with the same vision and 
aspiration as CODASYL) who actually cared about the language and who had 
some credibility, this could have been rectified. Instead, we eventually 
arrived at the situation we have today... small wonder it isn't 
transportable.


>
> Portability of Java and C# is irrelevant in a COBOL
> newgroup. <g>

So is an exposition on Regular Expressions. Not part of the language.

>
>> >
…[8 more quoted lines elided]…
> Well, you could have rephrased and tried again.

Yes. Would it make any difference? I said at the start I didn't intend to 
debate this, and to do so with someone who is demonstrably hostile is simply 
a waste of time. It's a rainy Saturday here so I'm prepared to make this 
post, but it will certainly be my last one in this thread, and you won't be 
surprised if I don't respond to your posts for some time in the future.

>
>> >
…[17 more quoted lines elided]…
>

Golly! Is there no end to the elucidation...
>> >
>> > Object-Oriented programming, functional programming, and
…[16 more quoted lines elided]…
> see and then try to understand why.

Now, it's funny you should say that, Mr. Smith. I recognise that you 
certainly don't see what I see and I'm fine with that.

Most of the people who know me consider me to be an understanding and 
sympathetic sort of person, I try to be there for friends and my shoulder 
has often been dampened by the tears of the distressed, but I seem to be 
short of understanding when it comes to people who call the solutions I use 
"lame" and anything that doesn't conform to their particular viewpoint, a 
"perversion".

Even rising above that, and I it doesn't really matter, I simply cannot 
understand the world you inhabit. It seems to me to be a world of dusty 
tomes and Acadaemia, where whatever is written down is true. You quote 
chapters and verse as if they were Holy Writ and require no further scrutiny 
or proving; it is enough that they are in the book. Your attention to detail 
would be commendable if it weren't so obsessive.

Your reduction below of Object use, into purely procedural programming terms 
is simply staggering.  It shows a narrowness of vision that I simply cannot 
comprehend.

So, yes, you're right, I don't understand. However, I have tried.

For example, a great
> deal of what has been put forth as Object-Oriented
> programming, I see as implementation of procedural
…[5 more quoted lines elided]…
> I've seen enough to recognize the pattern.

Ah, so people who are doing it everyday are not blessed with your superior 
wisdom and don't realise they are NOT REALLY dealing with objects; instead 
they are conforming to a conceptual pattern that is really based in 
procedural code. OK... I think I have to go now... (looks at watch)...
>
> What I have rarely seen is implementation of an
> Object-Oriented design, which, it seems to me, is the
> point of Object-Orientation.
>

Well, of course. The whole thing's a misnomer if it doesn't comply to what 
you have read somewhere. The fact that the wole world is running with it 
shouldn't let us get away with calling it something it isn't (according to 
Mr. Smith).


>> >>
>> >> >
…[40 more quoted lines elided]…
> COBOL.
 Er... it isn't actually me that's raving just now... could you lower your 
voice a bit?  I have never damned COBOL. I have waxed enthusiastic about C#. 
No apology for it.

You did the same with Java. You do it with SQL
> versus COBOL ISAM.

And, of course, there is absolutely no possibility I could be right? 
Remember, it isn't about me... try GOOGLing on "Java programming" 
(170,000,000 hits), or "SQL" (169,000,000 hits), then do the same with 
"COBOL programming" (2,220,000 hits) and "ISAM" (1,380,000 hits)..."

Well, tickle me with a teacake, looks like Dashwood isn't the only person 
who holds such an opinion...the world is going to Hell in a handcart... 
can't they see that COBOL and ISAM are the only true solution...?

OK. So a contrary viewpoint (to that held by R. Smith...not necessarily 
contrary to that held by millions of other people), expressed honestly, 
without malice, and stated to be opinion, is now a rave? I call 'em like I 
see 'em. Always have, always will. I don't need to rave to do that, and I 
also realise that my opinions on these things are not Life and Death. It is 
only computer programming.

>
> Love and hate are emotions; their opposite is apathy. If you
> didn't care, you wouldn't express opinions about programming
> languages!

I care about a lot of things that I neither love nor hate.

I guess I have apathy as well, because I really don't care about whether you 
listen to me or not.


>
>> If it stopped doing that, I'd move to something else. As to commerce
…[8 more quoted lines elided]…
>

Whatever...

Dashwood... out.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-07-07T12:39:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6o1hi$siv$1@reader2.panix.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net>`

```
In article <5f904cF3bffdfU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>This is my last response on this.
>
…[3 more quoted lines elided]…
>news:138tbv0h4hkd243@corp.supernews.com...

[snip]

>> Mr Dashwood, you may have found the level of detail
>> to be unnecessary, others may have not. My suspecting
…[14 more quoted lines elided]…
>then you try to say it isn't about me :-).

Mr Dashwood, what you comment here on - editorialising aside - is Mr 
Smith's having posted to a thread in which he had not (to a point) 
previously participated and in which he had not been addressed directly.

That sounds... that sounds an *awful* lot like what happens with a fair 
amount of frequency in many unmoderated UseNet fora, doesn't it?

[snip]

>> "(I'm "guilty" of mentioning C#, certainly, but only in the context of
>> alternatives to COBOL. Why should we consider alternatives to COBOL? See
…[6 more quoted lines elided]…
>as stated above.

'At the time'?  Mr Dashwood, *I* was not familiar with your having made 
that statement... and I found that the datestamp on it (as shown in 
<http://groups.google.com/group/comp.lang.cobol/msg/f694a97526aa446b?dmode=source>) 
is Mon, 18 Jun 2007 23:56:15 +1200.

Your posting to which I am responding now is... oh, that whacky 
International Date Line... let's call it 7 July 2007, a hair over two 
weeks.

>Some of us don't live in a fixed condition and reserve the 
>right to change our minds in the light of new experience.

Others might consider that a position on a professional matter which was 
stated in public nineteen days ago and not in any wise modified in the 
intervening time to be still held or considered at least... moderately 
valid.

>I started out 
>seeing C# as a possible alternative to COBOL. And it was not the only one I 
>considered. Tried it, liked it, got more facile with it, now I'm happy with 
>it. End of story.

For the moment, perhaps... until another nineteen days passes, when a 
mention of what's said today might generate a response of 'That was then, 
this is now... Calendar Reform, all is different, I've moved on, why can't 
you?'

>
>The fact that you would search archives to try and make me look 
>inconsistent, speaks volumes to me. I suppose that kind of attack "isn't 
>about me" either?

It may be about the foundations of discussion, Mr Dashwood, and how you, 
as a participant, expect your statements to be seen and considered.  Since 
you are the best source for statements of your intent and you made - in 
what some might call a rather short time - two contradictory statements of 
intent a question to you about how these contradictions might be 
reconciled seems to be completely and utterly in order.

That an archive was searched - if such a thing happened - also seems to be 
completely and utterly in order.  Mr Smith reads you saying 'A' on 6 July 
(or thereabouts) and mutters 'Wait a minute... didn't he just say 'B' 
scarecly a fortnight back?'  To turn to the archives allows for 
verification outside of the notorious porosity of memory that some here 
have demonstrated.

>
>It was that single comment from you that made me decide to respond to this 
>thread.

It seems to have allowed you to demonstrate a great deal, Mr Dashwood... 
it may be left up to the Gentle Readers to determine 'a great deal of 
what?'.

DD
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-08T05:17:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fa056F3avi0vU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net> <f6o1hi$siv$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f6o1hi$siv$1@reader2.panix.com...
> In article <5f904cF3bffdfU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[33 more quoted lines elided]…
> previously participated and in which he had not been addressed directly.

Yes, I was wondering how long before you commented. (It is the 
predictability of this forum that makes it so...predictable.)

OK, let's address the pronouncements of the poison Dwarf... :-)
>
> That sounds... that sounds an *awful* lot like what happens with a fair
> amount of frequency in many unmoderated UseNet fora, doesn't it?
>

Yes. And I said as much but you conveniently snipped it.

"It's a
public forum; anyone can post anywhere, but you could have started another
thread for  your soapbox."

Sounds fair to me.



> [snip]
>
…[19 more quoted lines elided]…
>

Well, I'm glad things are so slack in Midgetville that you have nothing 
better to do than get involved in something that is nothing to do with you. 
I should be flattered tby the fact that a change in my position on something 
(albeit, a minimal and normal one), has sent you scurrying to your keyboard 
to try and make an issue out of it.

Slack news day?


>>Some of us don't live in a fixed condition and reserve the
>>right to change our minds in the light of new experience.
…[4 more quoted lines elided]…
> valid.
Fortunately there is no evidence that  "others" do think that. "Others" 
really don't give a shit. They quite rightly realise that my personal 
opinion about a programming language (or anything else, for that matter) can 
be subject to change. At least when I do change my mind, I explain why.

Furthermore, you missed the fact that enlightenment or epiphany can happen 
at any time. What I personally think about a given programming language was 
not under discussion. Except that it irks Mr. Smith so he made it an issue.

The new position is a logical progression from the old one and was explained 
as such in my post. This time you left the quote in (thank you)...

>
>>I started out
…[4 more quoted lines elided]…
>>it. End of story.

So, what part of "growth" do you have a problem with?

>
> For the moment, perhaps... until another nineteen days passes, when a
> mention of what's said today might generate a response of 'That was then,
> this is now... Calendar Reform, all is different, I've moved on, why can't
> you?'

Exactly. And why wait nineteen days? It could happen tomorrow...
>
>>
…[9 more quoted lines elided]…
> reconciled seems to be completely and utterly in order.

Fair comment, if it were true. The statements made were NOT contradictory. 
One was an extension of the other, and explanation was given to that effect.

And don't start getting Holy about the "foundations of discussion"... It's a 
Usenet Forum. I discuss things here as fairly as anyone else does.

>
> That an archive was searched - if such a thing happened - also seems to be
…[5 more quoted lines elided]…
>

Had it been done in that spirit my reaction to it would certainly have been 
different. It was done with hostile intent and that changes everything.

>>
>>It was that single comment from you that made me decide to respond to this
…[4 more quoted lines elided]…
> what?'.

Yes, I'm sure they're staying up nights.

Now let's get to you...

What exactly is your stake here? Just wanted to point out that it's 
perfectly OK to search stuff?

Never was an issue. Of course it is.

However the reaction encountered when doing so, may vary with the search 
motivation.

Still, it's good to know you are on the case...:-)

Pete.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-07-08T00:53:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6pchs$lia$1@reader2.panix.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net> <f6o1hi$siv$1@reader2.panix.com> <5fa056F3avi0vU1@mid.individual.net>`

```
In article <5fa056F3avi0vU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f6o1hi$siv$1@reader2.panix.com...
…[38 more quoted lines elided]…
>predictability of this forum that makes it so...predictable.)

If this has been said before I commented, Mr Dashwood, then it might have 
been called predicting; as it comes afterwards it... might now.

>
>OK, let's address the pronouncements of the poison Dwarf... :-)

Perhaps it might be more advantageous to see if something might better be 
found to occupy your time, Mr Dashwood... after all, you're a busy man, 
remember?

DD
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-08T13:42:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fatorF3b7tnjU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net> <f6o1hi$siv$1@reader2.panix.com> <5fa056F3avi0vU1@mid.individual.net> <f6pchs$lia$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f6pchs$lia$1@reader2.panix.com...
> In article <5fa056F3avi0vU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[48 more quoted lines elided]…
>

:-)

>>OK, let's address the pronouncements of the poison Dwarf... :-)
>
…[3 more quoted lines elided]…
>
All too well aware of that old chum. Normally, I'd post here as a welcome 
break from some very intense and stressful stuff that is occupying me at the 
moment.

As it isn't fun any more, I'll look at finding another outlet. (Cheers all 
round...:-))

Pete.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-07-08T11:52:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6qj6a$srd$1@reader2.panix.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5fa056F3avi0vU1@mid.individual.net> <f6pchs$lia$1@reader2.panix.com> <5fatorF3b7tnjU1@mid.individual.net>`

```
In article <5fatorF3b7tnjU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:f6pchs$lia$1@reader2.panix.com...
…[4 more quoted lines elided]…
>>>news:f6o1hi$siv$1@reader2.panix.com...

[snip]

>>>> Mr Dashwood, what you comment here on - editorialising aside - is Mr
>>>> Smith's having posted to a thread in which he had not (to a point)
…[9 more quoted lines elided]…
>:-)

Glad you enjoyed... and my apologies for the typographic error, the last 
word I posted should have been 'not' instead of 'now'.

>
>>>OK, let's address the pronouncements of the poison Dwarf... :-)
…[7 more quoted lines elided]…
>moment.

That there is stress *somewhere* in your existence, Mr Dashwood, might be 
apparent, at least by some interpretations of the responses you've shown 
here of late.

>
>As it isn't fun any more, I'll look at finding another outlet. (Cheers all 
>round...:-))

'Fun' is in the mind of the beholder... and it is difficult to escape the 
village in the pack that one carries on one's back.  To search the 
archives - if such a thing is polite - yields 
<http://groups.google.com/group/comp.lang.cobol/msg/2573afac4b2540d3?dmode=source>

--begin quoted text:

Here's a story for you...

Are you sitting comfortably? Good. Then I'll begin....

A traveller approaches the Gates of a great city.

He sees an old man, dressed in rags, sitting in the dust, warming his 
ancient bones in the hot sun.

The traveller addresses the old man...

"What are the people in this City like?"

"What were the people in the City you came from like?"

The traveller shudders at the memory.

"They were awful. Mean, money-grubbing, unkind, impolite, unfriendly, 
unhelpful, a real bunch of nasty no-hopers. That's why I left..."

The old man nods gently and says:

"I'm afraid they're just the same here..."

The traveller decides to move on and try his luck at the next city.

The old man dozes...

Presently, the sound of a tired horse approaching makes him raise his 
head. Another traveller stands before him and asks the same question:

"What are the people in this City like?"

The old man responds...

"What were the people in the City you came from like?"

"Ah, they were marvellous! Good, decent, generous folk. Always a smile and 
a helping hand where needed, truly the salt of the Earth. In fact I'm 
wondering if the Wander Lust that brought me here was such a good thing... 
I had many good and genuine friends back there..."

The old man stands up and opens the gate.

"You will find the same decent people here. Welcome to our City..."

They go into the City together.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-09T02:17:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fc9v2F3cbj68U1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5fa056F3avi0vU1@mid.individual.net> <f6pchs$lia$1@reader2.panix.com> <5fatorF3b7tnjU1@mid.individual.net> <f6qj6a$srd$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:f6qj6a$srd$1@reader2.panix.com...
> In article <5fatorF3b7tnjU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[28 more quoted lines elided]…
>

I suspected as much...

>>
>>>>OK, let's address the pronouncements of the poison Dwarf... :-)
…[20 more quoted lines elided]…
> village in the pack that one carries on one's back.

Ah, the Village...

"Who are you?"

"I am the new Number Two"

"Who is Number 1?"

"You, are Number 6..."

"I am not a number!!! I am a free man!!!"

There is no pack or anything else on my back. And no amount of giant 
inflated condoms will keep me here if I don't enjoy it.

> To search the
> archives - if such a thing is polite - yields
…[55 more quoted lines elided]…
>
:-) Touche.

Pete.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 8)_

- **From:** Richard Brady <rrllbrrady@worrlldnet.att.net>
- **Date:** 2007-07-07T20:01:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<5f904cF3bffdfU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net>`

```
Messrs. Dashwood, Smith et al;

Pete Dashwood wrote:
> This is my last response on this.
> 
> See below.

[snip]

Other than the personal attacks, which I deem quite unnecessary, (lame? 
  maybe not as thorough, but lame?) betwixt two such intelligent, 
thoughtful people and other thinking people who have commented as well 
(William, Howard, Charles, Alistair & Daniel and Doc), I found the 
discussion quite enlightening.  I thank all of you for contributing.

Mr. Dashwood, I thank you once more for your explanation of the RE that 
you use.  And Mr. Smith, I thank you as well for your improved RE and 
for defining the fine points that argue against Mr. Dashwood's ideas for 
improving or modernizing COBOL.  This forum has been quite eye-opening. 
  The state of the language, of the minds of COBOL programmers express a 
range of thoughts, solutions and feelings that remind me of the tower of 
Babel.  We cannot expect a committee to do any more than reflect the 
multiple voices.  Camels are horses ...

I know that certain strong feeling were evoked by this thread and it's 
relatives.  That is a good thing.  It is only by the continuing 
discussion that the finer points of an idea can be brought to light.  I 
would ask that the rhetoric attacking people be left out since it 
doesn't further anyone's understanding.  I suggest that responding to 
such attacks doesn't help either.

This is a forum for discussion.  It is wonderful.  You folks are 
incredible, taking the time to explain your ideas to the world.  Please 
do not silence your own voice or an other's voice.  I am ashamed that I 
caused such a row.

Richard Brady
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-07-07T16:50:39-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fP2dnRd8gMxahQ3bnZ2dnUVZ_s2vnZ2d@comcast.com>`
- **In-Reply-To:** `<iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net> <iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net>`

```
Richard Brady wrote:
> I am ashamed that I caused such a row.

Don't sweat it.  You should have been here when the debates over periods 
/ full stops were raging...  :)  There are also some personality 
conflicts, as with any group of folks.  IMO, I think the term "lame" may 
have been what set it off...
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-08T13:51:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5faua1F3bng11U1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net> <iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net> <fP2dnRd8gMxahQ3bnZ2dnUVZ_s2vnZ2d@comcast.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message 
news:fP2dnRd8gMxahQ3bnZ2dnUVZ_s2vnZ2d@comcast.com...
> Richard Brady wrote:
>> I am ashamed that I caused such a row.
…[5 more quoted lines elided]…
>
That was certainly a contributing factor.

Nevertheless, I could have behaved better... just ran out of patience.

Thanks for your post, Daniel.

Blessed, indeed, are the Peacemakers... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-07-08T11:54:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6qj9o$3hg$1@reader2.panix.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net> <fP2dnRd8gMxahQ3bnZ2dnUVZ_s2vnZ2d@comcast.com> <5faua1F3bng11U1@mid.individual.net>`

```
In article <5faua1F3bng11U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>Blessed, indeed, are the Peacemakers... :-)

... for they shall draw fire from *both* sides.

DD
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-07-08T13:32:08+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fat4pF3bnmtgU1@mid.individual.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net> <iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net>`

```

"Richard Brady" <rrllbrrady@worrlldnet.att.net> wrote in message 
news:iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net...
> Messrs. Dashwood, Smith et al;
>
…[8 more quoted lines elided]…
>
Don't be. This is Usenet. We have fights here all the time... :-)

It rarely gets personal, but it did on this occasion.

No one died...:-)

You are not responsible.

Pete.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 9)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-07-09T06:06:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1183986384.801648.82530@57g2000hsv.googlegroups.com>`
- **In-Reply-To:** `<iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net> <iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net>`

```
On 7 Jul, 21:01, Richard Brady <rrllbrr...@worrlldnet.att.net> wrote:
> Messrs. Dashwood, Smith et al;
>
…[34 more quoted lines elided]…
> Richard Brady

Row? What row? This is only  a minor spate.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 9)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-09T12:26:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1394og3llff27cd@corp.supernews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net> <iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net>`

```

"Richard Brady" <rrllbrrady@worrlldnet.att.net> wrote in message
news:iiSji.154348$Sa4.52581@bgtnsc05-news.ops.worldnet.att.net...

[snip]

> Other than the personal attacks, which I deem quite unnecessary, (lame?
>   maybe not as thorough, but lame?) betwixt two such intelligent,
> thoughtful people and other thinking people who have commented as well
> (William, Howard, Charles, Alistair & Daniel and Doc), I found the
> discussion quite enlightening.  I thank all of you for contributing.

"[B]ut lame?" Well, actually, yes!

I began programming in C in the late 80's (Microsoft C 5.0)
and began using C professionally in the early 90's. I was aware
of regular expressions since the 80's and have studied and,
occasionally, used the form in question for at least six years.
The question of validating e-mail addresses using regular
expressions was raised; I investigated; then posted a regular
expression for doing just that--one I understood to be
adequate to the task.

Then the code in question was posted. While I did not know
what "\w" entailed, I did know that the regular expression was
inadequate (having seen one that was) and I could see that the
code was clumsy in its attempt to deal with two "@" characters.
I made no further comment about the code (my calling the "\w"
a perverion, intending "non-standard usage", was a comment
about Microsoft).

One definition of "lame" is "weak; inadequate; clumsy". Two
weeks and two renamed threads later, the regular expression
and the same code, modified to COBOL, was presented in a
post to me. As one with sufficient profressional qualification and
knowledge to make judgments about such code--code that I
found to be inadequate and clumsy--I used the simple inclusive
term "lame" to describe it.

[snip]

> [...]  I am ashamed that I
> caused such a row.

Mr Brady, you didn't! It was a disagreement about the code
between two people with different points of view.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-07T18:55:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13906hm62vgj6e0@corp.supernews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <5f5sdcF3an649U1@mid.individual.net> <138sduqriahhhbb@corp.supernews.com> <5f79m1F3a58vtU1@mid.individual.net> <138tbv0h4hkd243@corp.supernews.com> <5f904cF3bffdfU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5f904cF3bffdfU1@mid.individual.net...
> This is my last response on this.
>
…[26 more quoted lines elided]…
> >> >> >> > news:5dna71F35l0l3U1@mid.individual.net...

[snip]

> >> > Mr Dashwood, it was never about you or your use of the RE.
> >> > The RE was presented as something found on the web and as
> >> > a solution to a problem.

[snip]

> I found your post hostile, condescending, and not of much real value. So
> that's one man's opinion. Unfortunately it prompted me to respond in kind
> and that is just as stupid. I won't be doing it any more.

Hositility was never my intent. What I intended was to
keep from insinuating that your use of the RE and its
associated code was unprofessional.

[snip]

> Your reduction below of Object use, into purely procedural programming
terms
> is simply staggering.  It shows a narrowness of vision that I simply
cannot
> comprehend.
>
…[15 more quoted lines elided]…
> procedural code. OK... I think I have to go now... (looks at watch)...

I wrote "Object-Oriented programming" not "dealing with
objects" nor "Object use". Perhaps you are not understanding
because you translate my words to fit your conceptions; instead
of understanding me.

Perhaps some examples will clarify my point.

This was the original.
-----
    public static bool IsValidEmailAddress(string sEmail)
    {
        if (sEmail == null)
        {
            return false;
        }

        int nFirstAT = sEmail.IndexOf('@');
        int nLastAT = sEmail.LastIndexOf('@');

        if ((nFirstAT > 0) && (nLastAT == nFirstAT) &&
        (nFirstAT < (sEmail.Length - 1)))
        {
            // address is ok regarding the single @ sign
            return (Regex.IsMatch(sEmail, @"(\w+)@(\w+)\.(\w+)"));
        }
        else  // I don't believe this is necessary but I left it in, in
deference to the original programmer. Pete.
        {
            return false; // this could be unconditional; if there is a
match the expression will return TRUE anyway...
        }
    }
-----
This following is sufficient to accomplish the same end
(actually, it does a bit more).
-----
    public static bool IsValidEmailAddress(string sEmail)
    {
    // Return true if SEmail is in valid e-mail format.
        return
Regex.IsMatch(sEmail,@"^([\w-\.]+)@(([\w-]+\.)+)([a-zA-Z]{2,4}$");
    }
-----
Both of the above are procedural.
The following is OO.
-----
    public static bool IsValidEmailAddress(string sEmail)
    {
    // Return true if SEmail is in valid e-mail format.
        Regex r = new Regex(@"^([\w-\.]+)@(([\w-]+\.)+)([a-zA-Z]{2,4}$");
        return r.IsMatch(sEmail);
    }
-----

The first was apparently the result of not understanding regular
expressions and how IsMatch works. In particular, the use of
the caret and dollar sign surrending the regular expression
prevents more than one e-mail address (additional occurrences
of "@"), which is the apparent purpose for the extraneous code.
In other words, though simple, it lacks professionalism.

The first and second are procedural use of objects. In these
cases, apparently, a temporary object is created, used, then
discarded. This is no different than the COBOL sequence:

    call "IsMatch" using bool, sEmail, email-re
    cancel "IsMatch"

The third creates an object initializing it with the regular
expression. It then uses the object and could do so repeatedly
because the regular expression is held in the object and not
passed through the interface. Holding data in the object is part
of Object-Oriented programming.

These examples are small and the differences are subtle; but
these are the patterns I see.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-07-06T04:10:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3hjji.4471$Od7.1437@newsread1.news.pas.earthlink.net>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:138r0t5o311iu77@corp.supernews.com...
>
<snip>

> When I wrote "The processing of REs, having developed using
> delimited strings, would require the use of ANY LENGTH
…[9 more quoted lines elided]…
>
First of all I am ignorant about any POSIX definition for regular 
expressions.  I am not expert with Java regular expressions but I do know a 
little about them.  Java has in its platform APIs a package of classes that 
process regular expressions on Java strings.  Java strings are not delimited 
strings.  There is no null character or any other character marking the end 
of a Java string.  So I guess I am not seeing why you have to have delimited 
strings in order to have regular expression processing.  Admittedly my mind 
is elsewhere these days and I am having a lot of trouble concentrating so 
maybe I am just miissing something or have not properly understood your 
point.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-06T05:50:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<138s45hk1fspnef@corp.supernews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <3hjji.4471$Od7.1437@newsread1.news.pas.earthlink.net>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message
news:3hjji.4471$Od7.1437@newsread1.news.pas.earthlink.net...
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
…[17 more quoted lines elided]…
> expressions.  I am not expert with Java regular expressions but I do know
a
> little about them.  Java has in its platform APIs a package of classes
that
> process regular expressions on Java strings.  Java strings are not
delimited
> strings.  There is no null character or any other character marking the
end
> of a Java string.  So I guess I am not seeing why you have to have
delimited
> strings in order to have regular expression processing.  Admittedly my
mind
> is elsewhere these days and I am having a lot of trouble concentrating so
> maybe I am just miissing something or have not properly understood your
> point.

My reference to "delimited strings" was historical; that is,
the common REs of today were developed using
variable-length, null-terminated (delimited) strings. Any use
of variable-length strings, today, continues that tradition.

COBOL data-items are not defined as variable-length,
except for the ANY LENGTH qualified items I mentioned.
Currently, COBOL data-items may be made variable-length,
programmatically, by using an OCCURS DEPENDING ON
phrase or by insertion of a delimiter; but the occurrence count
or delimiter used are separate data-items.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 5)_

- **From:** "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2007-07-06T13:58:36+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f6lapc$gha$1@nntp.fujitsu-siemens.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <3hjji.4471$Od7.1437@newsread1.news.pas.earthlink.net> <138s45hk1fspnef@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag 
news:138s45hk1fspnef@corp.supernews.com...
> My reference to "delimited strings" was historical; that is,
> the common REs of today were developed using
…[9 more quoted lines elided]…
>
Using OO-language elements, ANY LENGTH items are already available in COBOL 
STD2002! For a rough sketch, how regualar expressions could be made 
available to a COBOL program without invoving any standardization 
committees, see below.
Note 1: these are only the easy parts - the demanding parts are all 'to be 
supplied'
Note 2: this definition still allows the methods to have their task done by 
existing services/libraries/etc of the operating system or to proviede their 
own implementation - and by using inheritance, even more or less capable or 
specially tuned expression processing can be provided at the same time.

>>>    INTERFACE-ID.        reg-ex-factory.
       PROCEDURE DIVISION.

+++    METHOD-ID.           create-expression-validator.
       DATA DIVISION.
       LINKAGE SECTION.
       01 rxf-expression      PIC X ANY LENGTH.
       01 rxf-new-object      OBJECT REFERENCE ACTIVE-CLASS.
       PROCEDURE DIVISION USING rxf-expression
                          RETURNING rxf-new-object.
       END METHOD           create-expression-validator.
       END INTERFACE        reg-ex-factory.

>>>    INTERFACE-ID.        reg-ex-object.
       PROCEDURE DIVISION.

+++    METHOD-ID.           validate-expression.
       DATA DIVISION.
       LINKAGE SECTION.
       01 rxo-string          PIC X ANY LENGTH.
       01 rxo-result          PIC 1.
       PROCEDURE DIVISION USING rxo-string
                          RETURNING rxo-result.
       END METHOD           validate-expression.
       END INTERFACE        reg-ex-object.

>>>    CLASS-ID.            regular-expression
                              INHERITS base.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       REPOSITORY.
           CLASS base
           INTERFACE reg-ex-factory
           INTERFACE reg-ex-object.
FFF    FACTORY.               IMPLEMENTS reg-ex-factory.
       DATA DIVISION.
       *> to be supplied!
       PROCEDURE DIVISION.

+++    METHOD-ID.           create-expression-validator.
       DATA DIVISION.
       LINKAGE SECTION.
       01 rxf-expression      PIC X ANY LENGTH.
       01 rxf-new-object      OBJECT REFERENCE ACTIVE-CLASS.
       PROCEDURE DIVISION USING rxf-expression
                          RETURNING rxf-new-object.
       1.
           INVOKE SUPER "new" RETURNING rxf-new-object
           INVOKE rxf-new-object "remember-expression"
                                 USING rxf-expression.
       2.
           EXIT METHOD.
       END METHOD           create-expression-validator.
       END FACTORY.

OOO    OBJECT.
       DATA DIVISION.
      *> to be supplied, e.g. the regular expression remembered
      *> probably in a form to make later validation easy
       PROCEDURE DIVISION.

+++    METHOD-ID.           validate-expression.
       DATA DIVISION.
       LINKAGE SECTION.
       01 rxo-string          PIC X ANY LENGTH.
       01 rxo-result          PIC 1.
       PROCEDURE DIVISION USING rxo-string
                          RETURNING rxo-result.
      *> to be supplied!
       END METHOD           validate-expression.

+++    METHOD-ID.           remember-expression.
       DATA DIVISION.
       LINKAGE SECTION.
       01 rxo-expression      PIC X ANY LENGTH.
       PROCEDURE DIVISION USING rxo-expression.
      *> to be supplied!
       END METHOD           remember-expression.

      *> may be more 'internal' methods

       END OBJECT.
       END CLASS            regular-expression.

Karl Kiesel
Fujitsu Siemens Computers, M�nchen
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-06T09:54:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<138sievlpd5cu04@corp.supernews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <3hjji.4471$Od7.1437@newsread1.news.pas.earthlink.net> <138s45hk1fspnef@corp.supernews.com> <f6lapc$gha$1@nntp.fujitsu-siemens.com>`

```

"Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com> wrote in message
news:f6lapc$gha$1@nntp.fujitsu-siemens.com...
> "Rick Smith" <ricksmith@mfi.net> schrieb im Newsbeitrag
> news:138s45hk1fspnef@corp.supernews.com...
…[12 more quoted lines elided]…
> Using OO-language elements, ANY LENGTH items are already available in
COBOL
> STD2002! For a rough sketch, how regualar expressions could be made
> available to a COBOL program without invoving any standardization
> committees, see below.

Well, you made me take a closer look at ANY LENGTH
in both the current and draft standards! My statements, above,
are correct; though I don't understand why, in 2002, ANY
LENGTH can not be used in the linkage section of a program,
other than a contained program.

I wrote that, currently, a data-item may be made variable-length
by insertion of a delimiter. Under 2002, the source element
referencing an ANY LENGTH item must know what
delimiter (or other means) was used. Under the draft standard,
the delimiter is explicit by the DELIMITED phrase or defaults
to X"00" for pic X, or X"0000" for pic N. With this change,
the LENGTH function may be used to find the length of an
ANY LENGTH item. The 2002 standard leaves it to the
user to calculate the length. [The LENGTH function also now
works with ANY LENGTH PREFIXED items.] Thus,
under the draft standard ANY LENGTH items become true
variable-length items.

So, regular expressions could be implemented in COBOL 85.
They are less messy in COBOL 2002. And, as far as I can
tell, the draft standard removes the last wrinkles to developing
a class or functions for the processing of regular expressions,
as they are commonly understood.
```

###### ↳ ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-07-06T10:53:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<138slsqi7lpu49b@corp.supernews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <3hjji.4471$Od7.1437@newsread1.news.pas.earthlink.net> <138s45hk1fspnef@corp.supernews.com> <f6lapc$gha$1@nntp.fujitsu-siemens.com> <138sievlpd5cu04@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message
news:138sievlpd5cu04@corp.supernews.com...
[snip]
>  Under the draft standard,
> the delimiter is explicit by the DELIMITED phrase or defaults
> to X"00" for pic X, or X"0000" for pic N.

That should be NX"0000" for pic N.

My apologies.
```

###### ↳ ↳ ↳ ANY LENGTH (was: Regular Expressions and Standard COBOL

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-07-06T19:02:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Alwji.23326$%q4.2615@fe08.news.easynews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <5f3anoF38l4hvU1@mid.individual.net> <138r0t5o311iu77@corp.supernews.com> <3hjji.4471$Od7.1437@newsread1.news.pas.earthlink.net> <138s45hk1fspnef@corp.supernews.com> <f6lapc$gha$1@nntp.fujitsu-siemens.com> <138sievlpd5cu04@corp.supernews.com>`

```
"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:138sievlpd5cu04@corp.supernews.com...
>
> "Karl Kiesel" <Karl.Kiesel@fujitsu-siemens.com> wrote in message
> news:f6lapc$gha$1@nntp.fujitsu-siemens.com...
<much snippage>
> I wrote that, currently, a data-item may be made variable-length
> by insertion of a delimiter. Under 2002, the source element
…[10 more quoted lines elided]…
>

I won't guarantee this, but it my impression that at the latest WG4 meeting 
there was direction (partially in response from J4) to DRMATICALLY change the 
"ANY LENGTH" (prefixed and delimited) as defined in the current draft of the 
next Standard.  I would NOT "count on" what is in the (current) draft ever 
seeing the "light of day" in a Standard - or an implemetnation.

NOTE:
  The 01-level in Linkage Section of some - not all - entitities that was 
available in the '02 Standard will probably remain - but may (or may not) be 
made optional.
```

#### ↳ Regular Expressions and Standard COBOL (was Re: Use of Class conditions in COBOL)

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-07-05T12:19:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<468CE1EF.6F0F.0085.0@efirstbank.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com>`

```
Just an interesting web page I found when looking to see whether or not
EBCDIC does indeed not have a caret character.

http://www.everything2.com/index.pl?node=!%3D

Interestingly, I did an experiment where I used FTP to transfer an ASCII
file containing a caret to our mainframe.  It ended up translating the caret
to hex B0.  When I viewed the uploaded file from my TN3270 session it just
showed as '?', which is what shows for all 'non-display' characters.  I
don't know if the '?' is put there by the mainframe program I was working
with or by my TN3270 client.  I think the former.

I have a photocopy of a "yellow card" (though I think the one I copied was
green!) and it indeed does not show B0 as meaning caret, or anything else
for that matter.

Also interestingly is this page:
http://publib.boulder.ibm.com/infocenter/pdthelp/v1r1/index.jsp?topic=/com.i
bm.entcobol4.doc/rlebccs.htm.
It shows "the collating sequence for single-byte EBCDIC code page 1140",
which shows B0 as, indeed, being a caret.

I'd never heard of code page 1140, but apparently it is code page 037 + the
Euro symbol:

037 (IBM EBCDIC US-Canada) 
1047 (IBM EBCDIC Latin 1/Open System)
1140 (IBM EBCDIC US-Canada (037 + Euro symbol); IBM EBCDIC (US-Canada-Euro)
)

Yet another interesting page:
http://en.wikipedia.org/wiki/EBCDIC_8859

Hmm, here it shows code page 037 having the caret as B0:
http://en.wikipedia.org/wiki/EBCDIC_037.

Code pages are fun!  (Not.)

Frank
```

##### ↳ ↳ Re: Regular Expressions and Standard COBOL (was Re: Use of Classconditions in COBOL)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-07-05T22:08:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xZdji.137941$ia2.104478@fe01.news.easynews.com>`
- **References:** `<138nprdpf6ucu82@corp.supernews.com> <468CE1EF.6F0F.0085.0@efirstbank.com>`

```
Traditionally (as I recall) there were issues with the caret vs "not sign" for 
IBM mainframe shops (that used PL/I - and did some workstation development).  I 
don't recall all the details, but do recall SOME cases where these two were used 
to equate with each other.

At
  http://www.redbooks.ibm.com/redbooks/GG244473.html

there is a section with the following information:

"Characters  entered  at  a  non-3270  workstation  are  normally  translated 
by  the 3270  emulation  program  into  the  CECP  used  by  the  MVS  system. 
Any differences  between  the  CECP  and  Code  Page  01047  (the  code  page 
used  by OpenEdition  MVS;  see  6.1,  "EBCDIC  Character  Encoding"  on  page 
39)  need  to be  allowed  for.    In  our  case  the  CECP  used  was 
U.S./Canada  Country  Extended Code  Page  00037.    There  are  four 
characters  with  different  representations.    They are:
    � Left  square  bracket  ( [)
  � Right  square  bracket  (])
  � Circumflex  (caret)  (^)
 � Not  symbol  (� )"

I don't know if this is "useful" or not
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
