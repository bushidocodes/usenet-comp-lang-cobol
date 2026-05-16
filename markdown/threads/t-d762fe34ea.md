[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Test request (for Enter;prise COBOL)

_10 messages · 3 participants · 2010-07_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### Test request (for Enter;prise COBOL)

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-07-12T21:08:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com>`

```
I don't have current access to an IBM Enterprise COBOL compiler (either V3.x 
or V4.x).  If someone who has could try to compile the program in this ntoe 
with FLAG(I,I) and FLAGSTD(H) turned on, I would be interested in what FIPS 
messages you get.  I have NOT compiled it with any compiler yet, so there 
may be simply (typo) type errors in it, either tell me what they are or send 
it back to me to correct.

My guess is that the last two MOVE statments will be flagged and probably 
get the same message.  If they do not, could you please (off list) send me 
the compiler lisging.  If they do, then just email me or post the message 
that you get.

I don't need this program run (and don't really care what the results ae), 
bu if you want to run it, it should execute.

If anyone wants to try this with some other compiler with "Standard 
conformaqnce flagging" turned on, I might be interested in that too.  (You 
will probably need to commentout the initial "CBL" card).

Thanks in advance.

Downloadable verion is at:
  http://home.comcast.net/~wmklein/IBM/TestInd.CBL

 * * * * * * * * * * * * * * * * * *

        CBL Flagstd(H) Flag(I,I)

       Identification Division.

         Program-Id. TestInd..

       Data Division.

         Working-Storage Section.

       01  aTable.

           05 TheOccurs occurs 30 indexed anInd.

               10 anElem pic x(10).

       01  Table1.

           05 Occurs1 occurs 30.

               10 Elem1 pic x(10).

       01  Table2.

           05 Occurs2 occurs 60.

            10 Elem2 pic x(05).

        01  Table3.

           05 Occurs3 occurs 20 indexed aInd.

               10 Elem3 pic x(15).

       01 Recv Pic X(20).

       01 Num Pic 9.

       Procedure Division.

         Mainline.

           Move All "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

             to aTable Table1 Table2 Stable3

           Compute Num = Function Integer (Funtion Current-Date (6:1))

           set anInd to Num

           Move AnElem (anInd) to Recv

             Display Recv

           Move Elem1 (anInd) to Recv

             Display Recv

           Move Elem2 (anInd) to Recv.

             Display Recv

           Move Elem3 (anInd) to Recv

           Display Recv

           Stop Run.
```

#### ↳ Re: Test request (for Enter;prise COBOL)

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-13T12:27:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1hm47$mlr$1@reader1.panix.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com>`

```
In article <SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com>,
Bill Klein <wmklein@noreply.ix.netcom.com> wrote:
>I don't have current access to an IBM Enterprise COBOL compiler (either V3.x 
>or V4.x).  If someone who has could try to compile the program in this ntoe 
>with FLAG(I,I) and FLAGSTD(H) turned on, I would be interested in what FIPS 
>messages you get.

Well... how about this'un, for starters:

000022         002300    Move All "abcdefghijklmnopqrstuvwxyzABCDE (etc)

==000022==> IGYPS0009-E "MOVE" should not begin in area "A".

Kind of hard to go on from there... but what's Life without Struggle?

Changing that line to fit in between Ye Olde Marginse yielded:

000002         000300  Program-Id. TestInd..

==000002==> IGYDS0001-W A blank was missing before character "." (etc)

==000002==> IGYDS1089-S ". " was invalid.

... and changing the double-period/full stop in *that* line yielded:

000024         002400      to aTable Table1 Table2 Stable3

==000024==> IGYPS2121-S "STABLE3" was not defined as a data-name.

... and that which I was told thrice is true.

DD
```

##### ↳ ↳ Re: Test request (for Enter;prise COBOL)

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-07-13T08:45:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com> <i1hm47$mlr$1@reader1.panix.com>`

```
As I say, I don't have a compiler available at the moment. Sorry about the 
"typo" compiler errors. I think (hope) I have fixed them atll in the 
(updated) version at:
   http://home.comcast.net/~wmklein/IBM/TestInd.CBL

Let me know if there are still some that I need to fix.

<docdwarf@panix.com> wrote in message news:i1hm47$mlr$1@reader1.panix.com...
> In article <SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com>,
> Bill Klein <wmklein@noreply.ix.netcom.com> wrote:
…[33 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Test request (for Enter;prise COBOL)

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-13T14:21:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1hsq5$so4$1@reader1.panix.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com> <i1hm47$mlr$1@reader1.panix.com> <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com>`

```
In article <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com>,
Bill Klein <wmklein@noreply.ix.netcom.com> wrote:
>As I say, I don't have a compiler available at the moment. Sorry about the 
>"typo" compiler errors. I think (hope) I have fixed them atll in the 
…[3 more quoted lines elided]…
>Let me know if there are still some that I need to fix.

All righty... the first compile gave another bunch o' stuff but I think 
you said you were interested in FIPS errors, of which there was one:

28.13  IGYPS8233  Index-name does not appear in "INDEXED BY" phrase

Is this sufficient meat or shall I get back to things like

000023         002400      Compute Num = Function Integer

==000023==> IGYPS2288-E Too many arguments were specified for function "INTEGER"

000024         002500              (Funtion Current-Date (6:1))

==000024==> IGYPS2121-S "FUNTION" was not defined as a data-name.

==000024==> IGYPS2121-S "CURRENT-DATE" was not defined as a data-name.

==000024==> IGYPS2070-E Expected a right parenthesis, but found ":"

... et and cetera?

>
><docdwarf@panix.com> wrote in message news:i1hm47$mlr$1@reader1.panix.com...
…[37 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Test request (for Enter;prise COBOL)

_(reply depth: 4)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-07-13T11:09:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Bc0%n.467592$Up1.103262@en-nntp-09.dc1.easynews.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com> <i1hm47$mlr$1@reader1.panix.com> <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com> <i1hsq5$so4$1@reader1.panix.com>`

```
Which statements got the "IGYPS8233" message?  The last 3 MOVE statements?

I will update the source code, but if you want to try for a clean (cleaner?) 
compile, fix the spelling of "function" from "funtion" before CURRENT-DATE. 
That seems to be what those other messages are about.

<docdwarf@panix.com> wrote in message news:i1hsq5$so4$1@reader1.panix.com...
> In article <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com>,
> Bill Klein <wmklein@noreply.ix.netcom.com> wrote:
…[71 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Test request (for Enter;prise COBOL)

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2010-07-13T18:13:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1iabs$3is$1@reader1.panix.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com> <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com> <i1hsq5$so4$1@reader1.panix.com> <Bc0%n.467592$Up1.103262@en-nntp-09.dc1.easynews.com>`

```
In article <Bc0%n.467592$Up1.103262@en-nntp-09.dc1.easynews.com>,
Bill Klein <wmklein@noreply.ix.netcom.com> wrote:
>Which statements got the "IGYPS8233" message?  The last 3 MOVE statements?

Statements 28, 30 and 32 (which, for reasons of clarity, were called 
'28.13, 30.13, 32.13) and are, respectively:

000028         002900      Move Elem1 (anInd) to Recv 

000030         003100      Move Elem2 (anInd) to Recv.

000032         003300      Move Elem3 (anInd) to Recv

The message, in its entirety, reads:

=>000028.13 IGYPS8233   Index-name does not appear in "INDEXED BY" phrase 
for the table: nonconforming nonstandard, IBM extension to ANS/ISO 1985.

>I will update the source code, but if you want to try for a clean (cleaner?) 
>compile, fix the spelling of "function" from "funtion" before CURRENT-DATE. 
>That seems to be what those other messages are about.

You have no idea, Mr Klein, how supremely motivated I am to fix up someone 
else's code that I've downloaded twice and compiled a half-dozen times in 
order to discover nuances of this sort of subtlety.

DD

[top posted, nothing new here]

><docdwarf@panix.com> wrote in message news:i1hsq5$so4$1@reader1.panix.com...
>> In article <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com>,
…[74 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Test request (for Enter;prise COBOL)

_(reply depth: 6)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-07-13T13:37:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pn2%n.308691$ot7.253799@en-nntp-16.dc1.easynews.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com> <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com> <i1hsq5$so4$1@reader1.panix.com> <Bc0%n.467592$Up1.103262@en-nntp-09.dc1.easynews.com> <i1iabs$3is$1@reader1.panix.com>`

```
DD (and Charles who didn't post here),
   Thank you for running the test for me.  I am sorry that my original 
source code had errors in it.  I do hope to have a compiler available again 
in the near future to avoid making such requests (at least with compiler 
errors) in the future.

<docdwarf@panix.com> wrote in message news:i1iabs$3is$1@reader1.panix.com...
> In article <Bc0%n.467592$Up1.103262@en-nntp-09.dc1.easynews.com>,
> Bill Klein <wmklein@noreply.ix.netcom.com> wrote:
…[112 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Test request (for Enter;prise COBOL)

_(reply depth: 7)_

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-07-14T01:51:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yuOdnQzroIftw6DRnZ2dnUVZ_gGdnZ2d@giganews.com>`
- **In-Reply-To:** `<Pn2%n.308691$ot7.253799@en-nntp-16.dc1.easynews.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com> <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com> <i1hsq5$so4$1@reader1.panix.com> <Bc0%n.467592$Up1.103262@en-nntp-09.dc1.easynews.com> <i1iabs$3is$1@reader1.panix.com> <Pn2%n.308691$ot7.253799@en-nntp-16.dc1.easynews.com>`

```
On 7/13/2010 1:37 PM, Bill Klein wrote:
> DD (and Charles who didn't post here),
>     Thank you for running the test for me.  I am sorry that my original
…[8 more quoted lines elided]…
 >>> (snip)

My results were similar DocDwarf's.  The only error I corrected was the 
spelling of "FUNTION".  The results appeared to be identical between 
these two compilers:

PP 5655-G53 IBM Enterprise COBOL for z/OS 3.4.1
PP 5655-S71 IBM Enterprise COBOL for z/OS 4.2.0

If I get some time on Wednesday I will try again with the revised source 
code.  I will be interested to see how the intrinsic functions work with 
the additional parentheses.  The programmers in my shop (including me!) 
don't take advantage of intrinsic functions very often.
I use current-date and when-compiled, but never nested inside another 
function.

We're just beginning to convert to COBOL 4.2.0.

Kind regards,
```

###### ↳ ↳ ↳ Re: Test request (for Enter;prise COBOL)

_(reply depth: 7)_

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-07-15T02:16:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ncudnVA-ybslKKPRnZ2dnUVZ_qWdnZ2d@giganews.com>`
- **In-Reply-To:** `<Pn2%n.308691$ot7.253799@en-nntp-16.dc1.easynews.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com> <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com> <i1hsq5$so4$1@reader1.panix.com> <Bc0%n.467592$Up1.103262@en-nntp-09.dc1.easynews.com> <i1iabs$3is$1@reader1.panix.com> <Pn2%n.308691$ot7.253799@en-nntp-16.dc1.easynews.com>`

```
On 7/13/2010 1:37 PM, Bill Klein wrote:
> DD (and Charles who didn't post here),
>     Thank you for running the test for me.  I am sorry that my original
> source code had errors in it.  I do hope to have a compiler available again
> in the near future to avoid making such requests (at least with compiler
> errors) in the future.

I downloaded the corrected source and was able to compile it and execute 
it using both IBM Enterprise COBOL for z/OS 3.4.1 and 4.2.0



PP 5655-S71 IBM Enterprise COBOL for z/OS  4.2.0               TESTIND 
  Date 07
   Line.Col Code       FIPS message text

            IGYSC8208  "APOST" compiler option:  nonconforming 
nonstandard, IBM e

            IGYSC8292  "FASTSRT" compiler option:  nonconforming 
nonstandard, IBM

            IGYSC8227  "TRUNC(OPT)" compiler option:  nonconforming 
nonstandard,

     30.13  IGYPS8233  Index-name does not appear in "INDEXED BY" phrase 
for the
                       ANS/ISO 1985.

                       Same message on line:     32.13     34.13


********************************* TOP OF DATA ***********
ijklmnopqr
ijklmnopqr
ijklm
ijklmnopqrstuvw
******************************** BOTTOM OF DATA *********


PP 5655-G53 IBM Enterprise COBOL for z/OS  3.4.1               TESTIND 
  Date 07
   Line.Col Code       FIPS message text

            IGYSC8208  "APOST" compiler option:  nonconforming 
nonstandard, IBM e

            IGYSC8292  "FASTSRT" compiler option:  nonconforming 
nonstandard, IBM

            IGYSC8227  "TRUNC(OPT)" compiler option:  nonconforming 
nonstandard,

     30.13  IGYPS8233  Index-name does not appear in "INDEXED BY" phrase 
for the
                       ANS/ISO 1985.

                       Same message on line:     32.13     34.13
FIPS Messages        Total      Standard      Nonstandard      Obsolete
                          6           0               6              0

********************************* TOP OF DATA **************
ijklmnopqr
ijklmnopqr
ijklm
ijklmnopqrstuvw
******************************** BOTTOM OF DATA ************
```

###### ↳ ↳ ↳ Re: Test request (for Enter;prise COBOL)

_(reply depth: 8)_

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-07-15T06:01:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%TB%n.302769$pj7.93383@en-nntp-15.dc1.easynews.com>`
- **References:** `<SUP_n.575383$vr1.32401@en-nntp-07.dc1.easynews.com> <e6__n.647735$Hq1.36925@en-nntp-04.dc1.easynews.com> <i1hsq5$so4$1@reader1.panix.com> <Bc0%n.467592$Up1.103262@en-nntp-09.dc1.easynews.com> <i1iabs$3is$1@reader1.panix.com> <Pn2%n.308691$ot7.253799@en-nntp-16.dc1.easynews.com> <ncudnVA-ybslKKPRnZ2dnUVZ_qWdnZ2d@giganews.com>`

```
Thanks for the report.

"Arnold Trembley" <arnold.trembley@att.net> wrote in message 
news:ncudnVA-ybslKKPRnZ2dnUVZ_qWdnZ2d@giganews.com...
> On 7/13/2010 1:37 PM, Bill Klein wrote:
>> DD (and Charles who didn't post here),
…[69 more quoted lines elided]…
> http://www.arnoldtrembley.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
