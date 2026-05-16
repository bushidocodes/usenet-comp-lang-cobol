[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Parser to parse a COBOL file

_38 messages · 16 participants · 2001-12 → 2002-01_

---

### Parser to parse a COBOL file

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2001-12-09T05:14:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com>`

```
Hi,

I have to design a parser to compare function calls between COBOL and
C.
Something like
PROGRAM_ID. abc.
LINKAGE SECTION.
01 A_IN S9(4) COMP.

PROCEDURE DIVISION USING BY VALUE A_IN.

is equal to 

void abc(short a_in);

This what I plan to do to achieve the above. Eliminate multiple spaces
(between words, before words) using "tr". Then parse for PROGRAM-ID
(would give me the function name), WORKING-STORAGE SECTION(would give
me variables used in CALL statements), LINKAGE SECTION (would give me
variables used in PROCEDURE DIVISION statement), PROCEDURE DIVISION
(to get function arguments) and CALL (to get details of functions
called by this function / procedure).

Since, the position is fixed I can look for WORKING-STORAGE SECTION
then go on parsing till I get a LINKAGE SECTION.

Would help if I could get some comments/ views on this.

Thanks and Regards,
M Shetty
```

#### ↳ Re: Parser to parse a COBOL file

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-10T03:06:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c137367_10@Usenet.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com>`

```
Looks fine to me...

Remember to check for upper/lower case or convert each source line to upper
before trimming. (you may have intrinsic "TO-UPPER" depending on your
COBOL).

You are trimming spaces then checking for the reserved words you want. I
wouldn't do this; I'd forget the trimming and simply use transition
diagramming to detect immediately what is required with fewer byte compares.
The transition code can flush the lines that fail, quicker than your compare
for the length of the reserved word. This could be a sledgehammer to crack a
nut (when I first did this I was working on a COBOL compiler for
Burroughs...<G>) Tell you what though...the syntax scanning flew!

I wrote a paper on this around 10 years ago but I can't find it now. It was
published by Ed Arranga in one of the early paper copies of COBOL Report. He
might still have it somewhere.

If you are really interested, mail me and I'll write some code samples to
give you the idea.

Pete.
mshetty <mshetty@mail.com> wrote in message
news:bfbb8fd4.0112090514.4fb0f2ec@posting.google.com...
> Hi,
>
…[27 more quoted lines elided]…
> M Shetty



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

##### ↳ ↳ Re: Parser to parse a COBOL file

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2001-12-09T18:53:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0112091853.491f01ed@posting.google.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <3c137367_10@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message news:<3c137367_10@Usenet.com>...
> Looks fine to me...
> 
> Remember to check for upper/lower case or convert each source line to upper
> before trimming. (you may have intrinsic "TO-UPPER" depending on your
> COBOL).
Thanks
> 
> You are trimming spaces then checking for the reserved words you want. I
…[12 more quoted lines elided]…
> give you the idea.

I'd be really grateful, if you could send me some samples. 

Thanks and Regards,
M Shetty
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-12-12T05:15:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c16346d_1@Usenet.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <3c137367_10@Usenet.com> <bfbb8fd4.0112091853.491f01ed@posting.google.com>`

```
Notes on transition diagramming despatched by private mail.

I think David's suggestion is a good one too, but your needs are much less
than a full blown parser.

Pete.
mshetty <mshetty@mail.com> wrote in message
news:bfbb8fd4.0112091853.491f01ed@posting.google.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:<3c137367_10@Usenet.com>...
> > Looks fine to me...
> >
> > Remember to check for upper/lower case or convert each source line to
upper
> > before trimming. (you may have intrinsic "TO-UPPER" depending on your
> > COBOL).
…[4 more quoted lines elided]…
> > diagramming to detect immediately what is required with fewer byte
compares.
> > The transition code can flush the lines that fail, quicker than your
compare
> > for the length of the reserved word. This could be a sledgehammer to
crack a
> > nut (when I first did this I was working on a COBOL compiler for
> > Burroughs...<G>) Tell you what though...the syntax scanning flew!
> >
> > I wrote a paper on this around 10 years ago but I can't find it now. It
was
> > published by Ed Arranga in one of the early paper copies of COBOL
Report. He
> > might still have it somewhere.
> >
> > If you are really interested, mail me and I'll write some code samples
to
> > give you the idea.
>
…[3 more quoted lines elided]…
> M Shetty



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

#### ↳ Re: Parser to parse a COBOL file

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2001-12-12T22:12:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C1846B6.46FC4EC2@attglobal.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com>`

```
In addition to the other suggestions, you could simply parse COBOL using a
COBOL program.  I do so, in writing a Standards Checker that ensures our
programmers follow our rules.  This program gets executed with every COBOL
compile.

mshetty wrote:

> Hi,
>
…[27 more quoted lines elided]…
> M Shetty
```

#### ↳ Re: Parser to parse a COBOL file

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 2001-12-18T11:02:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c1f74b5$1@giga.realtime.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com>`

```
If you are doing serious comparisons of function signatures in both
languages,
it seems to me that you have to be able to parse both function signatures
(with all their complexities) in both languages..
Then you have to define carefully what you mean by "equal"
(does "char *" mean "zero terminated"?  How do you zero terminate a COBOL
string?),
and then implement the comparision routine itself.

For that, you need a single tool that can parse both at the same time,
and provide you with structured access to the parsed results.
Our DMS Software Reengineering Toolkit can do that;
you can put tested C and COBOL parsers into the same
custom analyzer, get parse trees, and implement
your equality check.

Maybe your problem is constrained (can be constrained?) enough
so that an ad hoc string hacking solution is sufficient,
but if you can really do that, I'd guess your situation
doesn't really warrant such an automated check at all.

How many function calls to C (count'em) exist
in your COBOL code total?
```

##### ↳ ↳ Re: Parser to parse a COBOL file

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-12-18T17:32:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20011218123257.14901.00000663@mb-fp.aol.com>`
- **References:** `<3c1f74b5$1@giga.realtime.net>`

```
Ira Baxter writes ...

[snip]

> How do you zero terminate a COBOL string?),

Use a 'z' data type (at least in IBM COBOL for OS/390 & VM or later).

[snip]

<ad>
This is covered in detail (with lots more, of course) in our course "Beyond
COBOL II" which discusses all the changes to the IBM mainframe COBOL compilers
from COBOL II on, up through COBOL for OS/390 & VM V2.2.1. The new "IBM
Enterprise COBOL for z/OS and OS/390" changes will be in a new course out first
quarter 2002.

</ad>

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-12-18T18:12:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C1F867C.4995D8F8@shaw.ca>`
- **References:** `<3c1f74b5$1@giga.realtime.net> <20011218123257.14901.00000663@mb-fp.aol.com>`

```


S Comstock wrote:

> Ira Baxter writes ...
>
…[7 more quoted lines elided]…
>

Similarly in Net Express using OO :-

    01 myTitle pic x(13) value z"Dialog Title".

Note - one extra character for the Null terminator. OR :-

 move z"ReturnCustomerPrimeKey "  to ls-MethodName - again note "extra space"
before closing quote, denoting the x'00'.

Have no idea whether the IBM or Micro Focus approaches are part of the future
Standard. Still according to Bill's latest, we'll only know when ISO consent to let
us take a look see at the final document. (If it isn't part of the Standard - you
have to wonder, considering two 'major players' introduced it to their compilers.)

You have to despair at the bureaucracy !

Jimmy
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-12-18T22:37:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QyPT7.17$PO5.2862@newsread1.prod.itd.earthlink.net>`
- **References:** `<3c1f74b5$1@giga.realtime.net> <20011218123257.14901.00000663@mb-fp.aol.com>`

```
Or (NOT currently available with any IBM COBOL compiler - but available with
many others), use the syntax that will become ANSI/ISO conforming some time
at the end of next year and use

   "literal " & X"00"

type structures.
```

#### ↳ Re: Parser to parse a COBOL file

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2002-01-05T07:51:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0201050751.10cae749@posting.google.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com>`

```
Hi,

This is what I am doing to parse for lines containing PROGRAM-ID/
WORKING-STORAGE/ LINKAGE SECTION etc.
1. I read a line of input
2. Remove delimiters like space, comma, tab and enter.
3. Parse the first word in the "line read" and
4. Compare it with the set of known keywords like PROGRAM_ID,
WORKING-STORAGE etc.

Alternatively, I can read a character from the file and compare it
with the
first letter in the list of known keywords.

Like read the "I" of Identification Division and compare it with the
"P" (PROGRAM-ID/ PROCEDURE), "W"(WORKING-STORAGE) and so on.

If it matches with a particular keyword. I go on to read the next
character from the input file and compare it with the next character
in the keyword. If all the characters match, I have found a line
containing the particular keyword.

Would help if I could get some comments on the advantages and
disadvantages of using Approach I or II.

(In the first approach I can re-use the logic that splits a line into
words and returns the first word.)

Thanks and Regards,
M Shetty
```

##### ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-01-05T16:38:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JZFZ7.368$Ml3.45284@dfiatx1-snr1.gtei.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201050751.10cae749@posting.google.com>`

```
mshetty <mshetty@mail.com> wrote in message
news:bfbb8fd4.0201050751.10cae749@posting.google.com...
> 1. I read a line of input...
> Alternatively, I can read a character from the file...
> ..
> Would help if I could get some comments on the advantages and
> disadvantages of using Approach I or II.

The Obvious #1:
What is important to you? Run-time execution speed? Resource utilization?
Ease of programming/maintenance? (I believe you get your choice of two of
these).

The Obvious #2:
Depending on what is important to you, why not write a little test program
to see which method best serves your desires?

My parsers (of anything) look for whole keywords. Of course, these are
written in BASIC, which supports variable-length strings which are not
supported in COBOL, so that's a consideration.
```

##### ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-01-05T20:35:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C376463.1984EC06@shaw.ca>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201050751.10cae749@posting.google.com>`

```


mshetty wrote:

> Hi,
>
…[27 more quoted lines elided]…
> M Shetty

Not sure what you are after, but as Michael has already indicated use
'whole words'. I recently went through this exercise checking out Micro
Focus Collection classes, to be able to check something like the
following :-

*>--------------------------
Method-id. "doSomething".
*> This method is PRIVATE

0                  2     3
8                  7     3
procedure division using amessage lnkPtr anelement lnkoccurs
               returning defaultreturn.     OR :-
0                  2         3
8                  7         7
procedure division returning lnkBool.

ETC...

Reading the source in sequentially, I first converted each line with
function  Uppercase. In my case I was checking for (1) Comment lines
(*>), (2) whether the method was 'PRIVATE' as opposed to Public, (3)
'METHOD-ID' (4) 'PROCEDURE DIVISION ' and (5) any series of 'USING'
parameters and (6) any 'RETURNING' parameters.

Having positioned on the keywords, I could then use Reference
Modification to move through each line.

Unfortunately my example uses Collections to store parameters, so it
probably wont be of much use to you. But if you are interested in an
overall general approach, mail me privately.

PS - To avoid confusion - in OO most methods are PUBLIC and can be
invoked(called) from another class. Where designated as 'PRIVATE" as in
the comment line above, this means the method is ONLY invoked from within
the same class. The differentiation of Public/Private is NOT part of
COBOL 2002.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Parser to parse a COBOL file

- **From:** jraben@cascinc.com (Jeff Raben)
- **Date:** 2002-01-07T19:15:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c39f29a.5918138@news.bullseyetelecom.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201050751.10cae749@posting.google.com>`

```
mshetty@mail.com (mshetty) wrote:

>Hi,
>
…[9 more quoted lines elided]…
>with the

snip

For a massive cross referencing process I had to look for source and
object field. i.e. ADD ???? to MASTER-FILE-POST-CTR or MOVE
MASTER_FILE_POST_CTR to ???.
I found that UNSTRINGING DEDLIMITED BY SPACE INTO ... ... ... ...
and a SEARCH into a sorted table of key words worked well.

I had to worry about continuations and quoted text (sometimes
rebuilding the continuations with STRING.

I worked and was fast.

I've done it both in BASIC and COBOL.

Regardless of the total project, I found whole word search much faster
and tighter code (always good for debugging).

Jeff
and stir with a Runcible spoon...
```

#### ↳ Re: Parser to parse a COBOL file

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2002-01-06T05:56:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0201060556.2e38ffb8@posting.google.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com>`

```
Hi,

I am using the following logic to delete spaces at the beginning of the line read.

//pos1 =  Search for the first space 
//pos2 =  Search for the first character ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJ
KLMNOPQRSTUVWXYZ19234567890")
// Eliminate all characters till pos2

Is this sufficient ?? Would I get a character outside the set mentioned above??

Would help if I could get some comments on the above.

Thanks and Regards,
M Shetty
```

##### ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-06T14:34:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1accr$8j8$1@nntp9.atl.mindspring.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com>`

```
The following are valid lines of COBOL (adjust columns accordingly):

    05  Data-name-1  Pic X(100)   Value "abc
-   "  continued literal"
         .

   ***

Even

    Procedure Div
-          ision Us
-         Ing  ABC
         ,   XYZ
         ;   yet-more
      .
   Para-Name
      .
      Move ABC
         (sub1) t
-       o   Xyz (1
        :2)

Is valid (but UGLY) COBOL.
```

##### ↳ ↳ Re: Parser to parse a COBOL file

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2002-01-19T04:58:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0201190458.41ce2de5@posting.google.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com>`

```
Hi,

While parsing a COBOL file, is there a way to identify a group data
item ?? I want to distinguish between group data items and elementary
data items.

Would help if I could get some comments on the same.

Thanks and Regards,
M Shetty
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "JerryMouse" <jerrymouse@invalid.com>
- **Date:** 2002-01-19T13:18:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pme28.77028$rA.4955343@bin6.nnrp.aus1.giganews.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190458.41ce2de5@posting.google.com>`

```

"mshetty" <mshetty@mail.com>

> While parsing a COBOL file, is there a way to identify a group data
> item ?? I want to distinguish between group data items and elementary
> data items.

No.

Why do you want to differentiate between group/elementary data items in the
code generating the data?
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-19T12:35:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2ce9p$88k$1@nntp9.atl.mindspring.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190458.41ce2de5@posting.google.com>`

```
As far as I know, the only "official" way to determine if something is a
group vs elementary item is to look at the LEVEL number (and redefines
phrase) of the next defined item.

A) If the next "phrase" is a new section or division (or in file section, a
new FD/SD), then this item is an elementary item.

B) If the next item's level number is 01 or 77, then this item is an
elementary item.

C) if the next level number is HIGHER (greater) than the current level
number - but is not 88, then this is a group item.  If the next item is an
88 level, then you need to "read" to the next non-88 level (or non-data
item) and apply the other rules in this list to figure out if this is or is
not an group item.

D) If the next data item includes the REDEFINES phrase  then this item is an
elementary item.

   ***

I don't guarantee it, but I think that covers all cases.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-20T08:57:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4A8692.D0D93CC3@Azonic.co.nz>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190458.41ce2de5@posting.google.com> <a2ce9p$88k$1@nntp9.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> C) if the next level number is HIGHER (greater) than the current level
> number - but is not 88, then this is a group item.  

    not ( 88 or 66 )
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-19T14:09:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2cjpo$nek$1@slb0.atl.mindspring.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190458.41ce2de5@posting.google.com> <a2ce9p$88k$1@nntp9.atl.mindspring.net> <3C4A8692.D0D93CC3@Azonic.co.nz>`

```
I was going to add that when I signed back on.  I remembered that later.  If
the next item is 66, then the current item must be an elementary item.

FYI - depending upon the compiler (and extensions) other "odd" level numbers
(greater than 49) may also exist - such as 78-levels.

Also (although INCREDIBLY uncommon) if the "end of source code" follows the
data item, then it is an elementary item.  (The procedure division *IS*
optional in the '85 Standard - and an EXIT PROGRAM is assumed - but I know
of almost NO source code that is done this way.)
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 5)_

- **From:** "Edwin Earl Ross" <EdwinEarl@yahoo.com>
- **Date:** 2002-01-23T06:51:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U3t38.4512$Jw3.1737829443@newssvr11.news.prodigy.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190458.41ce2de5@posting.google.com> <a2ce9p$88k$1@nntp9.atl.mindspring.net> <3C4A8692.D0D93CC3@Azonic.co.nz>`

```
not 88, 66, or 77.

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3C4A8692.D0D93CC3@Azonic.co.nz...
> William M. Klein wrote:
> >
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-23T21:00:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4F2483.E807A227@Azonic.co.nz>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190458.41ce2de5@posting.google.com> <a2ce9p$88k$1@nntp9.atl.mindspring.net> <3C4A8692.D0D93CC3@Azonic.co.nz> <U3t38.4512$Jw3.1737829443@newssvr11.news.prodigy.com>`

```
Edwin Earl Ross wrote:
> 
> not 88, 66, or 77.

77 had been catered for earlier in rule B.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "Edwin Earl Ross" <EdwinEarl@yahoo.com>
- **Date:** 2002-01-23T06:55:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o7t38.4513$cC3.1738184767@newssvr11.news.prodigy.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190458.41ce2de5@posting.google.com>`

```
As you may have figured out already, COBOL is complex, so writing a parser
is difficult. In my experience, parsing COBOL is an order of magnitude more
difficult than any other 3GL.

"mshetty" <mshetty@mail.com> wrote in message
news:bfbb8fd4.0201190458.41ce2de5@posting.google.com...
> Hi,
>
…[7 more quoted lines elided]…
> M Shetty
```

##### ↳ ↳ Re: Parser to parse a COBOL file

- **From:** mshetty@mail.com (mshetty)
- **Date:** 2002-01-19T05:33:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbb8fd4.0201190533.4ac09168@posting.google.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com>`

```
Hi,

My compiler compiles this, don't know if it is valid and if it is used.

01 xxx USAGE POINTER.
   02 yyy USAGE POINTER.

Would the following be considered as a group ??
01 TEMP PIC 9(9).
 88 HOT VALUE 0.
 88 COLD VALUE 0.

Would help if I could get some comments on the above.

Thanks and Regards,
M Shetty
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2002-01-19T14:59:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com>`

```
Elementary items have PICTUREs; group items don't.  That's the definition.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-19T12:24:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2cdkl$1fp$1@slb6.atl.mindspring.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com>`

```
Unfortunately, not true.

  01  Group1.
     05  Ptr  Usage Pointer.
     05  Float-for-IBM  Comp-1.
     05 anIndex  Usage Index.

shows at least 3 usages that do not ALLOW picture clauses for elementary
items.

However, simply having a USAGE clause also does not indicate whether an item
is elementary or not.

 01 Group Usage Comp.
    05 ThisIsComp   Pic S9(04).

is valid.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-20T08:46:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4A83ED.2CB90A27@Azonic.co.nz>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com>`

```
Terry Heinze wrote:
> 
> Elementary items have PICTUREs; group items don't.  That's the definition.

No.  There is no need to have a PICTURE clause to define a field, it can
be done with USAGE and SIZE.


> > 01 xxx USAGE POINTER.
> >    02 yyy USAGE POINTER.

USAGE on a group item is valid.  It means that the usage applies to all
appropriate subsiduary items.

> > Would the following be considered as a group ??
> > 01 TEMP PIC 9(9).
> >  88 HOT VALUE 0.
> >  88 COLD VALUE 0.

No.  88 levels are conditionals not fields.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 5)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2002-01-19T15:05:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yfk28.22976$o_.4886249@news20.bellglobal.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com> <3C4A83ED.2CB90A27@Azonic.co.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3C4A83ED.2CB90A27@Azonic.co.nz...
> Terry Heinze wrote:
> >
> > Elementary items have PICTUREs; group items don't.  That's the
definition.
>
> No.  There is no need to have a PICTURE clause to define a field, it can
…[8 more quoted lines elided]…
>
So is this legal?

01 xxx usage pointer.
    02 pointer1.
    02 pointer2.
    02 pointer3.

Donald ... learning something I've never used.





> > > Would the following be considered as a group ??
> > > 01 TEMP PIC 9(9).
…[3 more quoted lines elided]…
> No.  88 levels are conditionals not fields.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-20T10:43:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4A9F6C.B00F8482@Azonic.co.nz>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com> <3C4A83ED.2CB90A27@Azonic.co.nz> <yfk28.22976$o_.4886249@news20.bellglobal.com>`

```
Donald Tees wrote:
> >
> > USAGE on a group item is valid.  It means that the usage applies to all
…[7 more quoted lines elided]…
>     02 pointer3.

I can't think of any reason why not, except that POINTER is not part of
ANS'85.  Certainly if it was USAGE INDEX it should be valid.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-19T16:32:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2csfi$hic$1@slb3.atl.mindspring.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com> <3C4A83ED.2CB90A27@Azonic.co.nz> <yfk28.22976$o_.4886249@news20.bellglobal.com> <3C4A9F6C.B00F8482@Azonic.co.nz>`

```
Although, I thought there was a rule specifying which USAGEs could and could
not be specified at the group level, the following is the actual rule from
the '85 Standard (some implementors may have extensions to this).

"(2) If the USAGE clause is written in the data description entry for a
group item, it may also be written in the data description entry for any
subordinate elementary item or group item, but the same usage must be
specified in both entries."

(see page VI-46 - or page 369 in the latest draft of the next COBOL
Standard)

This means that in the '85 Standard

 01  Group-not-index Usage Index.
     05  Ind-data-item  Usage Index.

*is* conforming, but

 01  Group-not-index Usage Index.
     05  Ind-data-item.

is NOT conforming source code. For the next COBOL Standard, this means that
the example (from an earlier part of this thread),

 01 xxx usage pointer.
     02 pointer1.
     02 pointer2.
     02 pointer3.

will *not* be conforming source code, but

 01 xxx usage pointer.
     02 pointer1 pointer.
     02 pointer2 pointer.
     02 pointer3 pointer.

WILL be conforming - while

 01 xxx usage pointer.
     02 pointer1 pointer.
     02 AlphaNum  Pic X.

will NOT be conforming (because the last elementary item has a different
IMPLICIT usage than that specified at the group level.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-20T15:35:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4AE3D7.B1B9BCAB@Azonic.co.nz>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com> <3C4A83ED.2CB90A27@Azonic.co.nz> <yfk28.22976$o_.4886249@news20.bellglobal.com> <3C4A9F6C.B00F8482@Azonic.co.nz> <a2csfi$hic$1@slb3.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> "(2) If the USAGE clause is written in the data description entry for a
> group item, it may also be written in the data description entry for any
                 ^^^
> subordinate elementary item or group item, but the same usage must be
> specified in both entries."

I would interpret 'may' as 'you can do, but don't need to'.

> This means that in the '85 Standard
> 
…[8 more quoted lines elided]…
> is NOT conforming source code. 

I cannot think of any reason why it isn't conforming.  Earlier I had
thought that a data description entry may be required to attach the
USAGE to, but now I can't find any actual requirement for there to be
anything other than the USAGE on the group in this case. 'May' doesn't
mean 'must'.

>  01 xxx usage pointer.
>      02 pointer1.
…[3 more quoted lines elided]…
> will *not* be conforming source code, but

Really ?  Is there a specific requirement for an individual data
description ?

>  01 xxx usage pointer.
>      02 pointer1 pointer.
…[3 more quoted lines elided]…
> IMPLICIT usage than that specified at the group level.

That's always been true hasn't it, for example with USAGE COMP ?
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-20T19:19:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2fqbl$cac$1@nntp9.atl.mindspring.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com> <3C4A83ED.2CB90A27@Azonic.co.nz> <yfk28.22976$o_.4886249@news20.bellglobal.com> <3C4A9F6C.B00F8482@Azonic.co.nz> <a2csfi$hic$1@slb3.atl.mindspring.net> <3C4AE3D7.B1B9BCAB@Azonic.co.nz>`

```
I am now QUITE confused about what is and is not conforming in the '85
Standard.  I think that you (Richard) are probably right.  However, I have
sent out a couple of notes to J4/WG4 to see if I am missing yet another
rule.

I *clearly* agree that the "may" means that you don't need to use the USAGE
clause for elementary items, I am just not positive (although I am leaning
to agree with you) that the USAGE at the group level APPLIES to the
elementary items.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 10)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-01-21T13:05:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cmU28.103$ST3.89860@paloalto-snr1.gtei.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com> <3C4A83ED.2CB90A27@Azonic.co.nz> <yfk28.22976$o_.4886249@news20.bellglobal.com> <3C4A9F6C.B00F8482@Azonic.co.nz> <a2csfi$hic$1@slb3.atl.mindspring.net> <3C4AE3D7.B1B9BCAB@Azonic.co.nz> <a2fqbl$cac$1@nntp9.atl.mindspring.net>`

```
William M. Klein <wmklein@ix.netcom.com> wrote in message
news:a2fqbl$cac$1@nntp9.atl.mindspring.net...
> I am now QUITE confused about what is and is not conforming in the '85
> Standard....I *clearly* agree that the "may" means that you don't need to
use the USAGE
> clause for elementary items, I am just not positive (although I am leaning
> to agree with you) that the USAGE at the group level ...


My $0.02 sez that finding all the supported/possible methods of expressing
the USAGE of elementary or group items is just an exercise in exotica.

Seems to me the subject,  "USAGE clause at the group level versus USAGE
clause at the elementary level " is a topic better suited to, and should be
included in,  "shop coding standards."

In this thread, the subject comes in the context of parsing a COBOL source
program; methinks one would need to go one step further, asking, "parsing
for WHAT?".  Looking for unused datanames? Trying to generate a storage map
of group items?  Checking syntax for compliance with shop/ANSI standards? I
can see different *parsing* rules for each application.

My goodness, this almosts appears a nascent "religious" topic like GOTO, the
use of scope-terminators vs. full stops, PERFORM THRU ......

MCM
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 10)_

- **From:** SkippyPB <swiegand@neo.rr.com>
- **Date:** 2002-01-21T11:16:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<915BD5589E4830B5.F00EB25F6B3B9787.F89597BA5850C503@lp.airnews.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com> <3C4A83ED.2CB90A27@Azonic.co.nz> <yfk28.22976$o_.4886249@news20.bellglobal.com> <3C4A9F6C.B00F8482@Azonic.co.nz> <a2csfi$hic$1@slb3.atl.mindspring.net> <3C4AE3D7.B1B9BCAB@Azonic.co.nz> <a2fqbl$cac$1@nntp9.atl.mindspring.net>`

```
On Sun, 20 Jan 2002 19:19:37 -0600, "William M. Klein"
<wmklein@ix.netcom.com> enlightened us:

>I am now QUITE confused about what is and is not conforming in the '85
>Standard.  I think that you (Richard) are probably right.  However, I have
…[6 more quoted lines elided]…
>elementary items.

I don't know about standards or not, but in the mainframe world going
back to at least Cobol-D (or whatever the official title is..I knew
them as Cobol-D which was followed by Cobol-F), the USAGE at the group
level was valid.  In fact you didn't even need to say USAGE.  You
could just say something like:

01  MY-COUNTERS   COMP-3.
     05  MY-CNT1                        PIC S999  VALUE +0.
.
.
.
.
    05  MY-CNT9                        PIC S999  VALUE +0.

In this every element would be a two byte packed numeric field.  I've
used this construct many times just to save typing.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

The secret of a happy marriage remains a secret.
                                -- Henny Youngman
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-01-20T14:27:30+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c4a2198_13@Usenet.com>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <wRf28.6103$v44.1088952468@newssvr16.news.prodigy.com> <3C4A83ED.2CB90A27@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3C4A83ED.2CB90A27@Azonic.co.nz...
> Terry Heinze wrote:
> >
> > Elementary items have PICTUREs; group items don't.  That's the
definition.
>
> No.  There is no need to have a PICTURE clause to define a field, it can
…[5 more quoted lines elided]…
>

A valid example, but to be completely accurate it is not just SIZE and USAGE
that are required, it is SIZE, CLASS, and USAGE.

I remember coding COBOL  before the PICTURE clause was available. We used
these 3 clauses to describe data. For example:

a-numeric-field  SIZE 4 CLASS numeric         USAGE display. [modern
equivalent = PIC 9(4).]
a-text-field        SIZE 4 CLASS alphanumeric USAGE display. [modern
equivalent = PIC X(4).]

Sometimes the CLASS is implicit in the USAGE (as in the example you quoted).
It is interesting that COBOL still retains the CLASS test (if  NUMERIC...,
if ALPHABETIC.... etc.) even though I believe the CLASS and SIZE clauses may
no longer be in the Standard, having been rendered redundant by "PICTURE".

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-01-19T15:06:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-v6V3ELzXdd2l@thishost>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com>`

```
On Sat, 19 Jan 2002 13:33:47 UTC, mshetty@mail.com (mshetty) wrote:

> Hi,
> 
…[4 more quoted lines elided]…
>

That should not be valid (I think).
 
> Would the following be considered as a group ??
> 01 TEMP PIC 9(9).
>  88 HOT VALUE 0.
>  88 COLD VALUE 0.
> 

No this is a data element with condition definitions.

Level number 88 is a special use level that defines a condition name 
for the preceding data element.

> Would help if I could get some comments on the above.
> 
> Thanks and Regards,
> M Shetty

A group looks like this

02 data-name.
  03  part-of-group-1 pic x.
  03  part-of group-2 pic xx.

The data element that is the start of a group item does not contain a 
picture clause and is followed by data elements that have a higher 
level number.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-19T12:24:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2cdm3$fa7$1@slb7.atl.mindspring.net>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com>`

```
Which compiler allows USAGE POINTER both at the "group" and elementary
level?  I don't recall any that DOCUMENTS this as valid - although there
certainly may be some.
```

###### ↳ ↳ ↳ Re: Parser to parse a COBOL file

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-01-20T08:54:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C4A85AD.EF4324F2@Azonic.co.nz>`
- **References:** `<bfbb8fd4.0112090514.4fb0f2ec@posting.google.com> <bfbb8fd4.0201060556.2e38ffb8@posting.google.com> <bfbb8fd4.0201190533.4ac09168@posting.google.com> <a2cdm3$fa7$1@slb7.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Which compiler allows USAGE POINTER both at the "group" and elementary
> level?  I don't recall any that DOCUMENTS this as valid - although there
> certainly may be some.

> > 01 xxx USAGE POINTER.
> >    02 yyy USAGE POINTER.

I don't see whay it is _not_ valid.  The usage on the item  yyy may be
redundant but is not invalid.  It may be in fact that it is required
because there needs to be some type definition on yyy to make it a field
rather than a group and no other type clause can be applied.

In the case of:

     01  group-comp        USAGE COMP.
         03  item-number   PIC S9(4).

The PIC is a type definition that carries the COMP from the group but it
would not be invalid to repeat this:

         03  item-another  PIC S9(4) USAGE COMP.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
