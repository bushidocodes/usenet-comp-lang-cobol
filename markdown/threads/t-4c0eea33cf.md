[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus Cobol

_13 messages · 7 participants · 2005-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus Cobol

- **From:** mnews <mnews@ecolpay.com>
- **Date:** 2005-04-11T23:46:28+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3er88$r7j$1@ctb-nnrp2.saix.net>`

```
Hi

I am new at micro focus (from m/f)

All my cobol programs from xenix compile, but on screen output programs 
i get an error on the "screen section".

The error say "verb unknown" ?

what could be wrong ?

Thanks
Mark
```

#### ↳ Re: Micro Focus Cobol

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-04-11T22:56:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgD6e.963628$Xk.292360@pd7tw3no>`
- **In-Reply-To:** `<d3er88$r7j$1@ctb-nnrp2.saix.net>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net>`

```
mnews wrote:
> Hi
> 
…[11 more quoted lines elided]…
> 
Give us a clue ! Which compiler Name and Version # and presumably MS 
Windows (Version # - e.g., 98, NT, XP etc.) The compile listing that 
contains "verb unknown" should be pointing at the line in your source. 
Is it in relation to Screen Section usage ? (Does Screen Section work 
with MS XENIX ?).

Jimmy, Calgary AB
```

#### ↳ Re: Micro Focus Cobol

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-04-11T21:45:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<115mdirqsodfj95@news.supernews.com>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net>`

```
mnews wrote:
> Hi
>
…[8 more quoted lines elided]…
>

You requested an action that is unknown to the language. Some examples are:

KISS
MOSEY
CLIMB
EAT
TWIDDLE
SHUCK
HOE-SAY-DOE
PLUCK
REAP
SACRIFICE
FLY
NOTARIZE
GRAB-BY-STACKING-SWIVEL

and so on
```

##### ↳ ↳ Re: Micro Focus Cobol

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-04-12T06:16:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WIJ6e.967976$Xk.712109@pd7tw3no>`
- **In-Reply-To:** `<115mdirqsodfj95@news.supernews.com>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com>`

```
HeyBub wrote:
> mnews wrote:
> 
…[31 more quoted lines elided]…
> 
Seems to me you are about as brilliant at COBOL as you are at politics !
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-04-12T21:32:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<115nn0g3khhqrf5@news.supernews.com>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no>`

```
James J. Gavan wrote:
> HeyBub wrote:
>> mnews wrote:
…[33 more quoted lines elided]…
> politics !

Aw, shucks... Thanks. Nice of you to say so.
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

- **From:** mnews <mnews@ecolpay.com>
- **Date:** 2005-04-13T07:27:37+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3iakc$8gr$1@ctb-nnrp2.saix.net>`
- **In-Reply-To:** `<WIJ6e.967976$Xk.712109@pd7tw3no>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no>`

```
Hi James

Dum Dum don't respond if you don't understand the question !!

Just for you I will have to explain in very much more detail.

Why does micro focus cobol on windows respond with "verb unknown.." for 
the line "SCREEN SECTION" yet it compiles on micro focus for unix ?

Understand the question now jamesie...

Don't worry i got the answer from someone that do not need long 
explanations and that are not a bit slow. The answer is that "SCREEN" is 
a reserved word on the Micro Focus for windows and not so for Micro 
Focus on Unix. The compiler just made a mistake in the error message, it 
should have said "reserved word used ...."

Mark
PS: Will know in future to explain very nicely just for you james.:))

James J. Gavan wrote:
> HeyBub wrote:
> 
…[34 more quoted lines elided]…
> Seems to me you are about as brilliant at COBOL as you are at politics !
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

_(reply depth: 4)_

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2005-04-13T15:40:46+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3ja2p$q2e$1@hyperion.microfocus.com>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no> <d3iakc$8gr$1@ctb-nnrp2.saix.net>`

```
Mark,

Which version of COBOL are you running on Windows, and which compiler 
directives are you using?

Reason I ask, is that if SCREEN was a reserved word by default, some of our 
sample programs from either Cobol Workbench or Net Express would not compile 
(and they do using default directives).

SimonT.
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-04-13T19:05:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<14e7e.4282593$Zm5.674727@news.easynews.com>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no> <d3iakc$8gr$1@ctb-nnrp2.saix.net>`

```
The answer that you got was WRONG.

"SCREEN" is a reserved word for Micro Focus *ON ALL PLATFORMS* - depending upon 
which dialect directives you have turned on.

the "real" answer to your original quesiton is that your two compilers have 
different defaults (or explicitly selected) dialect directives turned on.

If you place
  $SET MF

at the top of your source code, I can't think of any option (environment) in 
which a Screen Section will fail to compile with ANY release of Micro Focus - on 
ANY operating system.

To see ALL the "variations" on what is and is not a reserved word (and 
implicitly what features of the language are supported) based on dialect 
directives,

1) Go to:
   http://supportline.microfocus.com//documentation/index.asp

2) Select the product that you are using

3) Select the "Language Reference" from the list of available manuals

4) Use the index (or outline of chapters" to go to the Appendix with Reserved 
Words

   ***

You will see (for example) that for "SCREEN"  any/all of the following will 
"turn this on":


 I2 XO MF3 MS2

(FYI, "MF3" means any setting of "MF(n)" at or above "MF(3)" - including the 
default of MF)
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

_(reply depth: 5)_

- **From:** mnews <mnews@ecolpay.com>
- **Date:** 2005-04-14T00:25:13+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d3k68v$slf$1@ctb-nnrp2.saix.net>`
- **In-Reply-To:** `<14e7e.4282593$Zm5.674727@news.easynews.com>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no> <d3iakc$8gr$1@ctb-nnrp2.saix.net> <14e7e.4282593$Zm5.674727@news.easynews.com>`

```
Hi William

Thanks. I tried it and that solved the problem. Thanks also for the 
directives and notes.

Mark

William M. Klein wrote:

> The answer that you got was WRONG.
> 
…[38 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-04-13T23:03:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Gyh7e.1004884$6l.320881@pd7tw2no>`
- **In-Reply-To:** `<d3iakc$8gr$1@ctb-nnrp2.saix.net>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no> <d3iakc$8gr$1@ctb-nnrp2.saix.net>`

```
mnews wrote:
> Hi James
> 
…[16 more quoted lines elided]…
> PS: Will know in future to explain very nicely just for you james.:))

Don't put yourself to any bother. Just stick your head up your arse !
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

_(reply depth: 4)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-04-13T19:11:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3414e$425db536$45491f85$25129@KNOLOGY.NET>`
- **In-Reply-To:** `<d3iakc$8gr$1@ctb-nnrp2.saix.net>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no> <d3iakc$8gr$1@ctb-nnrp2.saix.net>`

```
mnews wrote:
> Hi James
> 
> Dum Dum don't respond if you don't understand the question !!

The temptation is very great to respond in kind here, but I won't. 
Suffice it to say that the smart-alecky answer was from HeyBub, not Mr. 
Gavan.  Mr. Gavan's remark to HeyBub stem from their apparent difference 
of political persuasion.

> Just for you I will have to explain in very much more detail.

The story above kind of loses its humor when it has to be explained in 
much more detail...

> Why does micro focus cobol on windows respond with "verb unknown.." for 
> the line "SCREEN SECTION" yet it compiles on micro focus for unix ?
> 
> Understand the question now jamesie...

That's certainly clearer than your original question (left at the bottom 
of this post).  While you are in the thick of what you are doing, there 
are people here who likely aren't even close.  Spelling out details, 
similar to your restatement above, can often help you get a much quicker 
(and accurate) answer.

> Don't worry i got the answer from someone that do not need long 
> explanations and that are not a bit slow.

And this is how you inspire someone to help you?  I'll certainly think 
twice before replying to any more of your posts...

> The answer is that "SCREEN" is 
> a reserved word on the Micro Focus for windows and not so for Micro 
> Focus on Unix. The compiler just made a mistake in the error message, it 
> should have said "reserved word used ...."

Thank you for sharing that - *that* is some useful information, the 
exchange of which is the existence of this forum in the first place.

history below...  (top-posting is also discouraged...)

> PS: Will know in future to explain very nicely just for you james.:))
> 
…[40 more quoted lines elided]…
> 
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

_(reply depth: 5)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-04-13T22:03:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1113451485.488562.260700@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<3414e$425db536$45491f85$25129@KNOLOGY.NET>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no> <d3iakc$8gr$1@ctb-nnrp2.saix.net> <3414e$425db536$45491f85$25129@KNOLOGY.NET>`

```
>> The answer is that "SCREEN" is
>> a reserved word on the Micro Focus for windows and not so for Micro
>> Focus on Unix. The compiler just made a mistake in the error
message, it
>> should have said "reserved word used ...."

> Thank you for sharing that - *that* is some useful information,

I am not quite sure that it is actually 'useful', it seems to
misrepresent the situation entirely. The statement is 100% wrong.

'SCREEN' _is_ a reserved word, it is reserved for use in the header
'SCREEN SECTION' and nowhere else.  It _is_ a reserved word when the
Unix compiler compiled the program correctly (the opposite of what
mnews claimed), it _isn't_ a reserved word when the program was
compiled under Windows (the opposite of what mnews claimed).

This is easy to determine from the behaviour.  The program compiled
correctly under Unix and failed under Windows with the message 'verb
unknown'. The compiler having reached the word 'SCREEN' and noticing
this _wasn't_ in the reserved word list, decided that it must be a
procedure label, and in fact a procedure division section called
Screen.  It then looked at the _next_ line and tried to process it as a
procedure division statement, but it wasn't a valid verb. The compiler
actually wouldn't complain about SCREEN, but would complain at the next
line.

Given that, the error message is perfectly correct and sensible from
the compiler's point of view.  The compiler did not get the message
wrong (as mnews claimed), it should _not_ have given an error message
'reserved word used' (as mnews claimed) because for that compile
'SCREEN' was not a reserved word.

In 4 lines mnews made 4 claims and got all 4 wrong.

The problem is that 'SCREEN SECTION' is an X/Open feature and not a
standard ANS'85 syntax.  If the compiler on Windows is set to only
process standard ANS'85 and/or reject MicroFocus and/or X/Open
extensions then 'SCREEN SECTION' will be taken to be a procedure
division section header.  Everything following will then be treated as
if it is Procedure division code.

By using a MF compiler directive (for example) the compiler is made to
treat 'SCREEN' as a reserved word and it then processes correctly the
code following.
```

###### ↳ ↳ ↳ Re: Micro Focus Cobol

_(reply depth: 6)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-04-14T07:54:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<47bc0$425e6802$45491f85$3028@KNOLOGY.NET>`
- **In-Reply-To:** `<1113451485.488562.260700@l41g2000cwc.googlegroups.com>`
- **References:** `<d3er88$r7j$1@ctb-nnrp2.saix.net> <115mdirqsodfj95@news.supernews.com> <WIJ6e.967976$Xk.712109@pd7tw3no> <d3iakc$8gr$1@ctb-nnrp2.saix.net> <3414e$425db536$45491f85$25129@KNOLOGY.NET> <1113451485.488562.260700@l41g2000cwc.googlegroups.com>`

```
Richard wrote:
>>>The answer is that "SCREEN" is
>>>a reserved word on the Micro Focus for windows and not so for Micro
…[11 more quoted lines elided]…
> misrepresent the situation entirely. The statement is 100% wrong.

Okay - maybe I should have said "*that* is some useful information, if 
it is accurate".  :)  My lack of Micro Focus experience is showing...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
