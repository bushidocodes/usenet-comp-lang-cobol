[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The Cost of COBOL

_25 messages · 12 participants · 2000-03_

---

### The Cost of COBOL

- **From:** Patrick Riley <p_riley@pipeline.com>
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com>`

```
Every three years or so I have this urge to rewrite my 10 year old
COBOL and SCREENIO written application and every time I look around at
the cost of upgrading the compilers/GUI interface I'm horrified at the
cost and just go back to making a few minor modifications and living
with it for another few years.

Guys, the price of these products is just out of this world in both
absolute terms and proportional to other computer products I use on a
day to day basis. NT4 which I installed late last year cost me around
$160 and is a little more complex than any COBOL compiler or screen
editor. Agent which I use daily cost $30. WordPerfect, another daily
use, around $150. In contrast we're talking $895 for ScreenIO and
god-only-knows for a current CA-Realia compiler and linkage editor. As
a guide to the latter Fujitsu seem to be about $1500. Nope, can't
justify this.

I'm sure you're thinking that I'm making an unfair comparison; after
all, NT is used by millions of people and the cost of development can
be spread over a lot more sales. OK, that's true. I accept that and
I'm not accusing Norcom or even CA of raking in oodles of bucks and
living high on the hog. If that were the case we'd see lots more
competition. But from my perspective--how many bucks I personally pay
out--it's what I get for my money that's important, not how much the
product cost to develop.

An analogous item would be a specialty truck (dump truck or similar)
which also costs a lot to build (for slightly different reasons) and
has a small potential market. The large construction company buys
their truck for big bucks and uses it daily (this is like the
corporate programmer); a carting company buys one and uses it daily on
many jobs (the contract programmer); but the guy who just wants to
move 10 tons of topsoil (me) rents the truck for a day or even by the
hour. The latter pays a premium price but only uses the truck rarely
so it's more advantageous for him. By sharing the truck with others he
reduces the cost to an acceptable level.

Unfortunately this idea of renting software (at least with COBOL
compilers, etc) doesn't seem to have occurred to anyone and yet the
COBOL manufacturers are missing out on a market because of insisting
on treating all the potential consumers like large corporations with
in-house data processing departments. Even they have budgets and a
high cost of a compiler is one more reason to rewrite the application
in something less costly especially if there's only one or two minor
aps in COBOL.

Might I suggest the compiler/screen builders consider the question.
Practically what I would suggest is that they sell/license the
compiler etc for a low price (say $50 for ScreenIO--not picking on
them; just that they're good enough to disclose their prices and lots
of detail on their website) and sell n uses of the software. The cost
of n would be such that it equated to the average cost of corporate
programmer use multiplied out. For example, if the corporate
programmer used the product 300 times in a year the price of n would
be $895 / 300 or $3.00 (rounded). The units of use could be sold in
advance via the web to reduce fraud.

In this way, I could buy (say) 20 uses for $60 plus the initial $50
and rewrite my application at a reasonable price. Note that the units
of use are how many times I compile the program, not how many times I
use the resulting application. The trunk rental agency doesn't charge
me for the subsequent use of the topsoil.

Since I don't have too much hope that such a change would occur in my
lifetime, let me ask the collected body of knowledge that frequent
this group what other product could do the task? (Hey, I like COBOL
but I also like fast Italian sports cars--I can't afford either at
present.)

You can think of my application as the IMDB (internet movie data base
www.imdb.com) without the web involvement and with the links (to
outside reviews etc) resolved to be the actual text. Think about data
entry: movies, a small text editor for reviews, alternate movie names,
stars and their alternate names, details about stars (date of birth
etc). And about output: selecting by characteristic (date of movie,
stars Smith and Jones, etc) and/or printing the entire shebang to a
file. And not some rinky-dink-limited-to-1000-records product either;
file quantities are currently at 50,000 movies, 70,000 stars, and
250,000 star/movie combinations.

Thanks in advance for your comments.
```

#### ↳ Re: The Cost of COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d14072.667015727@news.cox-internet.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com>`

```
Snipped a rant I could have written.....

I symptathize with your Patrick.  Years ago I bought Realia COBOL and
Screenio for about $1300.00 combined.  Was the price too high?  No -
because there is no runtime fee for either one.  When I wanted to make
the jump to Windows I did the same search you did - and was shocked to
find that I could not buy just a basic compiler - I had to buy the
whole suite at quite a premium.  I found Flexus Sp2
(http://www.flexus.com) which let me get to Windows but stay with my
trusty Realia compiler.  

However, if you look back in the comp.lang.cobol of a few years ago
you will see my similar lament.  Since that time, a new player has
entered the scene - Fujitsu COBOL (http://www.adtools.com) and you can
get a basic compiler from them for $750.00.  They still price and
offer products based on the features included and sent.  You can find
a $3000.00 version of their products as well - but you need only buy
what you want, and like Realia there is no runtime fee.  I now use
Fujitsu COBOL with Flexus sp2 for my GUI and I am a happy 32-bit COBOL
programmer.
```

##### ↳ ↳ Re: The Cost of COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D14E5F.B966D64B@home.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38d14072.667015727@news.cox-internet.com>`

```


Thane Hubbell wrote:
> 
> Snipped a rant I could have written.....

I'll comment separately to Patrick; clarification Thane. Taking the
Fujitsu version you are talking about, (I know, I know, Pete Dashwood -
you state Fujitsu gives you the OO stuff in the background), but Thane
is talking about seriously getting into OO 'direct'.

Does the current version let you do what you are planning - or have you
had to go up one notch ? And if you say you can do it with what you
currently have - exactly what are those whistles and bells in the $3K
version that would tempt anybody to go that route - what would be the
cost justification ?

Jimmy
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d1501d.671026598@news.cox-internet.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38d14072.667015727@news.cox-internet.com> <38D14E5F.B966D64B@home.com>`

```
On Thu, 16 Mar 2000 21:18:23 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[15 more quoted lines elided]…
>Jimmy

First OO, the project manager and the class browser are part of the
"Standard Edition", so I do not need to upgrade.  I pay my maint every
year (twice so far) so upgrades to later versions are free.  

The detailed explanation of what you get for your money is at:

http://www.adtools.com/info/whatcobol.htm

In a nutshell with the "standard edition" you get the compiler, a
runtime installer, and the project manager - with class browser.  You
also get a rudimentary version of the data file utility in order to
recover corrupt files (but you don't need it, as you can call that
directly).

The next level up gives you PowerCOBOL - the OO, event driven Dialog
System competitor (it uses COBOL behind the objects).  It's like VB
for COBOL.  It does obscure the full source code from the programmer
and is fully OO.  I've not used it beyond evaluation - my only
compaints relate to the event driven nature of the beast (just like
DS) and the tedium that gets you involved with.  

The next level gives you things designed for use in the "enterprise".
Code sharing with multiple developers, (via Power Gem), PowerForm for
printing via Windows.  You get the full on data converter, data file
editor (I tried an eval version a long time ago, it's pretty darn
neat).

The v5 beta I have has an extended CGI/ISAPI, interface for creating
CGI applications or ISAPI DLL's.  It's unclear if this is available to
me with the standard edition - I just read the docs, I didn't play
with it.  Also, with PowerCOBOL you can create ACTIVEX and COM objects
from your PowerCOBOL applications - something not available to me in
the standard edition.

For what *I* am doing the Standard Edition is more than adequet.  I
applaud Fujitsu for offering it.
```

##### ↳ ↳ Re: The Cost of COBOL

- **From:** "Jimmy" <Jkeeble@hotmail.com>
- **Date:** 2000-03-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8baqed$9kd$1@spider.cqu.edu.au>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38d14072.667015727@news.cox-internet.com>`

```
Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:38d14072.667015727@news.cox-internet.com...
> Snipped a rant I could have written.....
> I symptathize with your Patrick.  Years ago I bought Realia COBOL and
…[6 more quoted lines elided]…
> trusty Realia compiler.

Oh my god.  OK, I'm a student and I've just starting to learn COBOL as part
of my Info Systems degree and I decide to check around if there were any
*free* compilers out there that I could use, as RMCOBOL came with the
textbooks, but since its an education edition it does not create a
stand-alone EXE file.  But from what you guys are talking about, I'm worried
that somehow I don't think I'll be giving my programs away to my friends for
a while.

Are there any freeware compilers out there???

James.
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d9403e.1190855907@news.cox-internet.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38d14072.667015727@news.cox-internet.com> <8baqed$9kd$1@spider.cqu.edu.au>`

```
On Thu, 23 Mar 2000 01:55:52 +1000, "Jimmy" <Jkeeble@hotmail.com>
wrote:
>
>Oh my god.  OK, I'm a student and I've just starting to learn COBOL as part
…[8 more quoted lines elided]…
>

You can get Version 3 of Fujitsu COBOL for Windows in my book, Sams
Teach Yourself COBOL in 24 Hours, or in COBOL Unleashed, or from
http://www.etk.com or from http://www.adtools.com.
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

- **From:** jets@nbnet.nb.ca (Tony M. Mina)
- **Date:** 2000-03-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d98e24.254119@allnews.nbnet.nb.ca>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38d14072.667015727@news.cox-internet.com> <8baqed$9kd$1@spider.cqu.edu.au>`

```
Check Fujitsu Cobol v3.0.  This is free and I believe you can download
it.  Their site is www.adtools.com

Tony M. Mina




On Thu, 23 Mar 2000 01:55:52 +1000, "Jimmy" <Jkeeble@hotmail.com> wrote:

>Thane Hubbell <thaneH@softwaresimple.com> wrote in message
>news:38d14072.667015727@news.cox-internet.com...
…[22 more quoted lines elided]…
>
```

#### ↳ Re: The Cost of COBOL

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kEfA4.4456$34.86037@news.swbell.net>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com>`

```
There are companies that will sell you a COBOL compiler for a
substantial sum AND charge you a per-copy license. On the other hand,
The Fujitsu compiler (Version 3) is free and you can do your GUI
front-end in VisualBasic (Enterprise Edition $1300).


Patrick Riley <p_riley@pipeline.com> wrote in message
news:ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com...
> Every three years or so I have this urge to rewrite my 10 year old
> COBOL and SCREENIO written application and every time I look around
at
> the cost of upgrading the compilers/GUI interface I'm horrified at
the
> cost and just go back to making a few minor modifications and living
> with it for another few years.
>
> Guys, the price of these products is just out of this world in both
> absolute terms and proportional to other computer products I use on
a
> day to day basis. NT4 which I installed late last year cost me
around
> $160 and is a little more complex than any COBOL compiler or screen
> editor. Agent which I use daily cost $30. WordPerfect, another daily
> use, around $150. In contrast we're talking $895 for ScreenIO and
> god-only-knows for a current CA-Realia compiler and linkage editor.
As
> a guide to the latter Fujitsu seem to be about $1500. Nope, can't
> justify this.
>
> I'm sure you're thinking that I'm making an unfair comparison; after
> all, NT is used by millions of people and the cost of development
can
> be spread over a lot more sales. OK, that's true. I accept that and
> I'm not accusing Norcom or even CA of raking in oodles of bucks and
> living high on the hog. If that were the case we'd see lots more
> competition. But from my perspective--how many bucks I personally
pay
> out--it's what I get for my money that's important, not how much the
> product cost to develop.
…[5 more quoted lines elided]…
> corporate programmer); a carting company buys one and uses it daily
on
> many jobs (the contract programmer); but the guy who just wants to
> move 10 tons of topsoil (me) rents the truck for a day or even by
the
> hour. The latter pays a premium price but only uses the truck rarely
> so it's more advantageous for him. By sharing the truck with others
he
> reduces the cost to an acceptable level.
>
…[5 more quoted lines elided]…
> high cost of a compiler is one more reason to rewrite the
application
> in something less costly especially if there's only one or two minor
> aps in COBOL.
…[4 more quoted lines elided]…
> them; just that they're good enough to disclose their prices and
lots
> of detail on their website) and sell n uses of the software. The
cost
> of n would be such that it equated to the average cost of corporate
> programmer use multiplied out. For example, if the corporate
…[5 more quoted lines elided]…
> and rewrite my application at a reasonable price. Note that the
units
> of use are how many times I compile the program, not how many times
I
> use the resulting application. The trunk rental agency doesn't
charge
> me for the subsequent use of the topsoil.
>
> Since I don't have too much hope that such a change would occur in
my
> lifetime, let me ask the collected body of knowledge that frequent
> this group what other product could do the task? (Hey, I like COBOL
…[3 more quoted lines elided]…
> You can think of my application as the IMDB (internet movie data
base
> www.imdb.com) without the web involvement and with the links (to
> outside reviews etc) resolved to be the actual text. Think about
data
> entry: movies, a small text editor for reviews, alternate movie
names,
> stars and their alternate names, details about stars (date of birth
> etc). And about output: selecting by characteristic (date of movie,
> stars Smith and Jones, etc) and/or printing the entire shebang to a
> file. And not some rinky-dink-limited-to-1000-records product
either;
> file quantities are currently at 50,000 movies, 70,000 stars, and
> 250,000 star/movie combinations.
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: The Cost of COBOL

- **From:** Patrick Riley <p_riley@pipeline.com>
- **Date:** 2000-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84qadsgv3m3ur7demcsich49l84q673deu@4ax.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <kEfA4.4456$34.86037@news.swbell.net>`

```
"Jerry P" <bismail@bisusa.com> wrote:

>There are companies that will sell you a COBOL compiler for a
>substantial sum AND charge you a per-copy license. On the other hand,
>The Fujitsu compiler (Version 3) is free and you can do your GUI
>front-end in VisualBasic (Enterprise Edition $1300).

Free, eh! That's about the price I like to pay for everything <g>. I
downloaded V3 however I note that the website states "In the free
version of Fujitsu COBOL Version 3 both ODBC connectivity and
optimization are disabled. You will need to purchase Fujitsu COBOL
Version 4 to obtain these functions."

Hmmm. Is that ODBC-connectivity and ODBC-optimization or
ODBC-connectivity and optimization-in-general? Since I have no idea
what ODBC is I presume I don't need it. Is that correct?

Presuming that optimization doesn't just refer to ODBC is that
compiler optimization or code for the application program
optimization? Does that mean it will take longer to compile or longer
to run or just that it will occupy more memory than it could? If it's
speed of the resulting application how much slower are we talking? 

As to the Visual Basic I just happen to have access to Visual Studio
6.00 so that's also priced right. Not that I know the first thing
about Visual Basic. Any suggestions for a good book? Like "Visual
Basic for COBOL people who just want to use it to develop screens"
<heh, heh>.

I presume I can just call the VB program, let it display the screen
and after a user action return control to my COBOL program. Is this
correct? Sounds too simple.

Oh, and something else. I presume modern compilers such as the Fijitsu
V3 have eliminated the annoying problems of my 10-year old compiler
such as:

- limit of 640K per program
- 64K data division
- 32000 entries in a table
- memory fragmentation when calling other programs
- duplicate called programs in memory
- the need to run a linkage editor <g>
- the unsupported nature of the STRING statement where the INTO field
is the same as the sending field. Example: STRING data-name-1
DELIMITED BY ',' data-name-2,...DELIMITED BY SIZE '," DELIMITED BY
SIZE INTO data-name-1. This works but I understand it's unsupported. I
use it a lot.

Thanks for your suggestions (to all who responded).
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-03-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000319224303.07676.00000695@nso-cc.aol.com>`
- **References:** `<84qadsgv3m3ur7demcsich49l84q673deu@4ax.com>`

```
In article <84qadsgv3m3ur7demcsich49l84q673deu@4ax.com>, Patrick Riley
<p_riley@pipeline.com> writes:

>
>Free, eh! That's about the price I like to pay for everything <g>. I
…[8 more quoted lines elided]…
>

  When you get something for free, you hav to expect some feature reduction.
  The optimization is the application program optimization out of the 
  Compile/Link process.  Overall, the runtime is not significantly impacted on
  most interactive type processes.  It is noticeable when running batch
applications
  that process 100K+ records.

>Presuming that optimization doesn't just refer to ODBC is that
>compiler optimization or code for the application program
…[13 more quoted lines elided]…
>
  I have no experience in this area.  I would imagine that the VB GUI 
  is going to be the main that would call the COBOL program to exercise
 the data.  I am sure that there is probably some way of creating a DLL
 that could be called to pass data back and forth for a user interactive type
 process.

>Oh, and something else. I presume modern compilers such as the Fijitsu
>V3 have eliminated the annoying problems of my 10-year old compiler
…[15 more quoted lines elided]…
>
  I am certain that the 640K problem is not an issue, I am not certain about
the
 64K data division and 32000 table entry limits.  These seem to have been
resolved
 to some degree.  I believe that current limits may be relative to 16-bit and 
standards.  LINK process is still a required process to take an OBJ file from
 compile to an EXE.  You other questions will have to be answered by others.

Hope that this gets you started with some usable information.
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VVRC4.756$Id7.15178@news.swbell.net>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <kEfA4.4456$34.86037@news.swbell.net> <84qadsgv3m3ur7demcsich49l84q673deu@4ax.com>`

```

Patrick Riley <p_riley@pipeline.com
>
> Hmmm. Is that ODBC-connectivity and ODBC-optimization or
> ODBC-connectivity and optimization-in-general? Since I have no idea
> what ODBC is I presume I don't need it. Is that correct?

"Open Data Base Connectivity" You can write code and hook it to
Oracle, MS-Access, whatever.

>
> Presuming that optimization doesn't just refer to ODBC is that
> compiler optimization or code for the application program
> optimization? Does that mean it will take longer to compile or
longer
> to run or just that it will occupy more memory than it could? If
it's
> speed of the resulting application how much slower are we talking?

Longer to run - hundreds of milliseconds longer.

>
> As to the Visual Basic I just happen to have access to Visual Studio
…[3 more quoted lines elided]…
> <heh, heh>.

We hire 12-year-olds to do this.
>
> I presume I can just call the VB program, let it display the screen
> and after a user action return control to my COBOL program. Is this
> correct? Sounds too simple.

That's it. Or you can go the other way - have a COBOL program invoke
VB (or C++ or API or whatever)

>
> Oh, and something else. I presume modern compilers such as the
Fijitsu
> V3 have eliminated the annoying problems of my 10-year old compiler
> such as:
>
> - limit of 640K per program == No limit. Windows pages code in and
out
> - 64K data division == No limit
> - 32000 entries in a table == Don't know. For huge stuff, we let
Windows handle it (send stuff to a list box, for example - sucker
really slows down when we send 60,000 lines to a list box, but what's
art without suffering?)
> - memory fragmentation when calling other programs == Don't know,
don't care. Buy more memory or a faster machine.
> - duplicate called programs in memory == Not a problem unless you
try something exotic
> - the need to run a linkage editor <g> == Yes, you must still Link
(as an EXE or DLL)
> - the unsupported nature of the STRING statement where the INTO
field
> is the same as the sending field. Example: STRING data-name-1
> DELIMITED BY ',' data-name-2,...DELIMITED BY SIZE '," DELIMITED BY
> SIZE INTO data-name-1. This works but I understand it's unsupported.
I
> use it a lot. == No, all that's part of the standard and fully
supported.

Get "Mastering COBOL," Carol Baroudi, Sybex Publishing, ISBN
0-7821-2321-X, $49.95 (USD)

>
> Thanks for your suggestions (to all who responded).
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DC2ECD.BD1730BF@home.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <kEfA4.4456$34.86037@news.swbell.net> <84qadsgv3m3ur7demcsich49l84q673deu@4ax.com> <VVRC4.756$Id7.15178@news.swbell.net>`

```


Jerry P wrote:
> 
> Patrick Riley <p_riley@pipeline.com
…[4 more quoted lines elided]…
> art without suffering?)

Jerry do you truly send those sort of volumes to a listbox ? I believe
you are working in tables - so what's your "occurs from (a) to (b)
depending on (c)" look like - or do you use some other neat twist.

> but what's art without suffering? - who gets nominated to do the suffering ?

Jimmy
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 5)_

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bo191$a8f$1@news.cerf.net>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <kEfA4.4456$34.86037@news.swbell.net> <84qadsgv3m3ur7demcsich49l84q673deu@4ax.com> <VVRC4.756$Id7.15178@news.swbell.net> <38DC2ECD.BD1730BF@home.com>`

```
Jerry P wrote:
>
> Patrick Riley <p_riley@pipeline.com
…[4 more quoted lines elided]…
> art without suffering?)

This sounds like a paged listbox to me, that is, you do only read the
visible amount, and the responds to events, to provide more items. You
should never fill a listbox with 60000 items.

Cheesle
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 5)_

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38dfcac3.5911410@wingate>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <kEfA4.4456$34.86037@news.swbell.net> <84qadsgv3m3ur7demcsich49l84q673deu@4ax.com> <VVRC4.756$Id7.15178@news.swbell.net> <38DC2ECD.BD1730BF@home.com>`

```
On Sat, 25 Mar 2000 03:19:06 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>Jerry do you truly send those sort of volumes to a listbox ? I believe
>you are working in tables - so what's your "occurs from (a) to (b)
>depending on (c)" look like - or do you use some other neat twist.
>
>> but what's art without suffering? - who gets nominated to do the suffering ?

Jimmy,

We implemented this in a virtual listview in our GUI ScreenIO screen
manager, which eliminates the limits (and headaches) associated with
using a very large listbox.  Plus, listviews handle columnar data.  

By caching the area of interest in the listview, you are only carrying
a small amount of the total data and still can provide excellent
performance.

Took a little more work on our part, of course...

Kevin
NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DFE036.31D1063D@home.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <kEfA4.4456$34.86037@news.swbell.net> <84qadsgv3m3ur7demcsich49l84q673deu@4ax.com> <VVRC4.756$Id7.15178@news.swbell.net> <38DC2ECD.BD1730BF@home.com> <38dfcac3.5911410@wingate>`

```


Kevin Hansen wrote:
> 
> On Sat, 25 Mar 2000 03:19:06 GMT, "James J. Gavan" <jjgavan@home.com>
…[18 more quoted lines elided]…
> Took a little more work on our part, of course...

 
Kevin,

Jerry wrote to me privately :-
-----------------------------------------------------------------------

Nope. No tables or arrays - at least not in our Fujitsu PowerCOBOL code.
In
one program we construct a report line (REPORT-LINE) defined as PIC
X(300).
Then we perform the following (caution - actual code follows):

 P540-SCREEN.
                INVOKE LV-SCREEN OF GRP-SCREEN "Add" USING 1 1 RETURNING
                        WK-INDX
                IF WK-INDX > 0
                        MOVE "ListItems"(WK-INDX) OF LV-SCREEN OF
GRP-SCREEN
                                TO POW-PCMLIST
                        MOVE REPORT-LINE(1:REPORT-LINE-LEN) TO "Text"(1)
OF POW-PCMLIST
                        END-IF.

If the above looks kinda goofy, it's because we have a ListView box of
only
ONE (very wide) column. We do this because the user can arrange the
layout
of data elements on the report line to suit himself - he can also send
this
same report line to the printer.

I'll attempt to decode the above:
1. LV-SCREEN is the name of the ListView box within a group whose group
name
is GRP-SCREEN.
2. The INVOKE statement with "Add" returns the pointer to the next
available
item for the LV box.
3. Note the pointer of the WK-INDXth item in the ListView box. Call it
POW-PCMLIST.
4. Move the REPORT-LINE to the 1st column of POW-PCMLIST.

We can actually send 60,000 lines to the above ListView box. Runs like a
rabbit until (it seems) it fills available memory then Windows starts
paging
and execution slows down (way down).

Hope this helps. Let me know if your curiosity was satisfied.
-----------------------------------------------------------------------

Jerry can respond - but looking at his code above "Add using an Index" -
and as he is using PowerCOBOL - it looks suspiciously to me like he's
using Fujitsu OO collections - maybe he doesn't know it :-). 

Subject to memory constraints, his 'list/collection' can be as small/big
as he wants. Pure guess - the slowdown he refers to, is as the
pointer(index) is working its way sequentially down through the
list/collection - and of course that Windows paging he refers to, also
comes into play. (???)

Anyway, regardless of the mechanics, it's nice to know that my OO
collections 'could' be much bigger than I use now, should I ever have
the need.

Jimmy
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 7)_

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e146ba.103182939@wingate>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <kEfA4.4456$34.86037@news.swbell.net> <84qadsgv3m3ur7demcsich49l84q673deu@4ax.com> <VVRC4.756$Id7.15178@news.swbell.net> <38DC2ECD.BD1730BF@home.com> <38dfcac3.5911410@wingate> <38DFE036.31D1063D@home.com>`

```
On Mon, 27 Mar 2000 22:32:14 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>...stuff regarding Fujitsu Listview implementation  ...and slowdown as list gets larger...

It looks to me as though the Fujitsu  implementation loads the list
sequentially, which could take awhile if the user drags the thumb to
the end of, say, a 1 million record list.

In GUI ScreenIO if the user does this, we just ask you to start
providing records starting from the thumb position, a percentage with
quite a bit of precision.  It's very fast, easy, and requires very
little memory.    Most database managers will let you start a browse
at a percentage along a keypath so it's not usually a big deal.  We
cache records as you provide them so that you get great performance in
the region of interest.

As a result, we can handle, theoretically, a file with up to 4 billion
records or so, although the true limit is as I recall, more like one
billion.  

Just another approach to the problem...

Kevin
NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E17554.54AF49AA@home.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <kEfA4.4456$34.86037@news.swbell.net> <84qadsgv3m3ur7demcsich49l84q673deu@4ax.com> <VVRC4.756$Id7.15178@news.swbell.net> <38DC2ECD.BD1730BF@home.com> <38dfcac3.5911410@wingate> <38DFE036.31D1063D@home.com> <38e146ba.103182939@wingate>`

```


Kevin Hansen wrote:
> 
> On Mon, 27 Mar 2000 22:32:14 GMT, "James J. Gavan" <jjgavan@home.com>
…[21 more quoted lines elided]…
> 
Agreed. I recall Richard Plinston (I'm guessing here, going from memory)
takes this same approach (DOS-wise Screen Section), 'listing' entries in
a block. Same approach with a Listbox, set a viewing limit, store 'last
key' you used then Start PrimeKey > = that 'last key ' be it Prime or
Alternate. 

Jerry was talking about report rcords I believe - not selecting to
scroll through a zillion records. But with the Listbox/Collection index
concept you are using the index(pointer) to get the Primekey of the
record(object) you are after.

Nevertheless, with sufficient memory Jerry's approach is intersting.


Jimmy
```

#### ↳ Re: The Cost of COBOL

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D282AA.68566297@home.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com>`

```


Patrick Riley wrote:

etc.....

The following is an UNADULTERATED message from Pete Dashwood :-

----------------------------------------------------------------------
Hi Jimmy,

I have no idea what this about as I haven't seen the context. If you
guys
are STILL arguing about what it costs to buy a COBOL compiler that just
confirms to me how sad things are in CLC....

If you intend to quote me in CLC, please Quote ALL of what I wrote. No
more
out-of-context spinning, please...
>>>
Thanks for the clarification Thane. Now Peter, I know you are using
Activex, ( and yes I DO BELIEVE you - you can get it up and running in
short order) - so for Activex are you using exactly the same as Thane,
or did it necessitate going 'up one'. I know your ISP problems - so post
to me and I'll repeat your message here. (Don't go all 'flowery' on us
about Fujitsu - Thane's already done a good job on that :-).
<<<
I don't know what you mean by going 'up one'. If Thane has waxed
eloquent
about Fujitsu, that simply confirms my opinion that he is a sensible
professional.

>>>
So as they used to say in Dragnet, "Just want the facts ma'am. Just want
the facts". And remember, the original context was the 'horrendous cost
of compilers', not which one is better than another.
<<<
OK, I'm NOT going to give a free plug to Fujitsu (I couldn't care less
WHAT
compiler ANYBODY uses...)

You requested Dragnet; here's Dragnet: (Just the facts, Joe Friday,
style...)

1996 -97: Became disillusioned with MicroFocus. Unhappy with
non-existent
support, and callous disregard of the small business User base. VISOC 
fiasco was the final straw. Looked for alternatives. Fujitsu offered
free
Version 3 (16 bit) compiler and Power COBOL environment. Tried it. Not
overkeen. Different to MF. Persevered, and started to realise how
excellent
PowerCOBOL was. Built a commercial Application using it (From the FREE
version...). Although 32 bit run time was included, decided that I
needed
the full 32 bit compiler and accessories.

1998: Bought COBOL version 4. 0 for $US460.00. It included COBOL 97
(previous version had COBOL 85), supported OO and came with a number of
useful ancillaries (especially one which converted all my existing MF
COBOL to Fujitsu). Also included one year's support.

I converted all my existing MF routines and went totally Fujitsu (Prior
to
that I had been using and supporting both MF and Fujitsu environments.
PowerCOBOL (32 bit version) was also included in this packet. Converted
the
existing Commercial app. to 32 bit and enhanced it. Customer
delighted...paid more money (so the cost of buying it was WELL
covered...)

1999: Encountered some problems with COBOL 4.0 Sought Fujitsu
support....expected runaround a la MF. Response within 12 hours, problem
solved. Several other problems followed: same superb support every time.
On
one occasion they actually called me from the States to UK and talked me
through the problem. No extra charge for this. Upgraded to new 4.2 when
it
was released. No charge. Exemplary support continued until one year of
support expired. They contacted me just before it expired and asked if I
wanted to renew it. I did. Paid $US 250.00 (approx. can't remember exact
amount...) on the understanding that  this gave me another year of
support
and entitled me to version 5.0 upgrade when released (any time now.) 

Realised in 1999 that 4.2 gave very strong support for ActiveX and COM
controls. Started trying this approach and building my own controls for
inclusion in VB, C++, HTML, and COBOL programs. No problem. Also easily
able to embed controls written in other languages, and/or provided by
third
parties, into COBOL.

So, Total paid: a little over $US 720.00 over 2 years. Return on
investment: 30 to 40 times cost of software (so far... prospects could
easily double this figure) PLUS introduction into ActiveX and cutting
edge
Windows and Web development.

Learning curve now complete, requirement for support minimal but still
have
good relationship with support team.

Very Happy Bunny.

Close case file....Dang! Da Dang Dang!Daaaaaaaaaaa!

Regards,

Pete.

-----------------------------------------------------------------------

Pete one thought - how come Richard Plinston can get in here and you
can't with your ISP. Are you two living on different islands ? Maybe you
Kiwis should link together a bit more :-)

Patrick, with regard to prices - I agree with your overall comments
about pricing - it robs small users of the chance to use COBOL. Think
about the school business of 'COBOL is dead' - could be because COBOL is
too pricey, so there are many kids jumping into the esoteric languages
and giving COBOL a big miss. I agree with Pete about the VISOC fiasco -
problem is how do you split a product down to offer people different
modules doing different things - no doubt such an approach will hiccup
somewhere.

Now I don't want to belabour this one - but to mind VISOC WAS the right
price - presumably based on the concept of low price, sell a lot more -
end result - lots of moolah like Microsoft. I believe Bill Klein will
disagree, as will probably many Micro Focus/Merant people. VISOC was a
kid's Meccano set that came without a glossy brochure showing Dick, Jane
and Spot pictures of what you could build. Plus, the OO concept was
difficult to swallow/comprehend. So, (and it strikes me as weird
marketing - they jacked up the price - rechristening it NetExpress, plus
adding additional 'goodies' of course).

Now in latest reincarnations, they have produced book-like on-line helps
on different topics, and they are very well done - just as Thane
referred to the excellent job that Fujitsu have done for OO - BUT, BUT,
BUT - although they have given me a whole daffy of references showing a
list of methods per class - they have not as yet taken that same 'book'
approach to take the reader, step-by-step, through the concepts or usage
of OO. Nobody is going to use it in depth if they can't understand the
premise of OO as it applies to COBOL.

Consider where M/F missed out - Flexus and Norcom realized Windows was a
bugger, you had to get to know the whole beast. All three had to analyse
Windows to see what it was about before producing their product - they
discovered what we would need to know, if we researched it ourselves.
The approach of the latter two - don't fret, you do it in COBOL and
we'll provide you the mechanism to link to the mystery animal. M/F could
have done exactly the same with their product, (in the OO/GUI module).
They've done it partially, (80-90% ?) with Dialog System - but it
doesn't go all the way - net result, a much higher priced product, (and
a very well constructed and comprehensive product), which still gives
you a challenge to 'talk' to Windows.

Jimmy
```

##### ↳ ↳ Re: The Cost of COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d2aeb0.760787472@news.cox-internet.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38D282AA.68566297@home.com>`

```
On Fri, 17 Mar 2000 19:13:47 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:



>Patrick, with regard to prices - I agree with your overall comments
>about pricing - it robs small users of the chance to use COBOL. Think
…[6 more quoted lines elided]…
>

VISOC failed for the same reason Fujitsu ALMOST failed.

1.  Intially the beta was Free.  That's just too good to be true!
With Fujitsu there were endless messages about how their free offer
could not be true.

2.  When priced - it was still cheap!  Fujitsu persevered with their
marketing model, and by all accounts have succeeded.  

MicroFocus, however, did something really interesting.  Almost as it
was released the branded VISOC dead.  When it came out we were in the
throws of deciding between junking COBOL for C++ and going to Dialog
System.  When VISOC came out, I thought our prayers were answered.
However, it was in DIRECT competition with DS.  Having decided at that
point that DS was probably the way to go, my boss was miffed.  He
called MicroFocus and asked them what the future was.  Was DS 16 bit
only forever?  Would VISOC replace it?  The two were so divergent as
to be incompatible approaches to the same end.  MF said that VISOC was
just an experiment and not a real product, and that DS was the way of
the future.  He made them put it in writing.  

So MF killed their own product.
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

- **From:** warnersoft@my-deja.com
- **Date:** 2000-03-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8b8q9t$ui5$1@nnrp1.deja.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38D282AA.68566297@home.com> <38d2aeb0.760787472@news.cox-internet.com>`

```
I have that VISOC beta, is it possible to do
anything with it? I've never had time to get past
the tutorial. I thought that VISOC became "Net
Express"?! Is that what everyone's refering to
when they say they left MF for Fujitsu? Anyone
with experience with Visual Age? I just installed
it here, but I'm mainframe development and
haven't had a chance to try out windows stuff.
I just got a small contract to build a custom
invoicing front end for Quickbooks, and was kind
of hoping to use Visoc. If I can't it'll have to
be MS-Access.
Any comments will be appreciated.



In article <38d2aeb0.760787472@news.cox-
internet.com>,
thaneH@softwaresimple.com (Thane Hubbell) wrote:
> On Fri, 17 Mar 2000 19:13:47 GMT, "James J.
Gavan" <jjgavan@home.com>
> wrote:
>
> >Patrick, with regard to prices - I agree with
your overall comments
> >about pricing - it robs small users of the
chance to use COBOL. Think
> >about the school business of 'COBOL is dead' -
could be because COBOL is
> >too pricey, so there are many kids jumping
into the esoteric languages
> >and giving COBOL a big miss. I agree with Pete
about the VISOC fiasco -
> >problem is how do you split a product down to
offer people different
> >modules doing different things - no doubt such
an approach will hiccup
> >somewhere.
> >
>
> VISOC failed for the same reason Fujitsu ALMOST
failed.
>
> 1. Intially the beta was Free. That's just too
good to be true!
> With Fujitsu there were endless messages about
how their free offer
> could not be true.
>
> 2. When priced - it was still cheap! Fujitsu
persevered with their
> marketing model, and by all accounts have
succeeded.
>
> MicroFocus, however, did something really
interesting. Almost as it
> was released the branded VISOC dead. When it
came out we were in the
> throws of deciding between junking COBOL for
C++ and going to Dialog
> System. When VISOC came out, I thought our
prayers were answered.
> However, it was in DIRECT competition with DS.
Having decided at that
> point that DS was probably the way to go, my
boss was miffed. He
> called MicroFocus and asked them what the
future was. Was DS 16 bit
> only forever? Would VISOC replace it? The two
were so divergent as
> to be incompatible approaches to the same end.
MF said that VISOC was
> just an experiment and not a real product, and
that DS was the way of
> the future. He made them put it in writing.
>
> So MF killed their own product.
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D807B0.6A92D040@home.com>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38D282AA.68566297@home.com> <38d2aeb0.760787472@news.cox-internet.com> <8b8q9t$ui5$1@nnrp1.deja.com>`

```


warnersoft@my-deja.com wrote:
> 
> I have that VISOC beta, is it possible to do
…[12 more quoted lines elided]…
> 

I have to really cast my mind back now. If it's the beta, isn't there a
time-stamp on it to stop using it after a certain date ? Similarly in
the Beta version there must be some reference to not using it for
re-sale ? Really can't remember. There was a release version of Visoc -
and as some of the 'oldies' here will know our friend Jose Capucho is
using it Portugal :-).

NetExpress is the immediate successor to Visoc - very similar, but
souped-up version and re-introduces M/F Dialog System. (With Visoc
basically three options (a) Screen Section (b) Direct calls to Win APIs
and (c) OO/GUIs as you will see in the demo examples.

Yes I'm afraid "Is that what everyone's referring to when they say they
left MF for Fujitsu?", is correct -  based on a lack of understanding
about OO/GUIs - here we go again - followed by a really jacking-up the
price for NetExpress.

Frankly, if you are only partially interested in the COBOL aspect to
front-end Quickbooks, (and you did say a 'small contract'), - use any
current flavour of COBOL you have and look at the possibility of
interfacing with Flexus SP2 or NORCOM - two packages geared to COBOL
syntax should you require to get into windowing. Fire your specific
questions at them and they will confirm.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: The Cost of COBOL

- **From:** khansen@screenio.com (Kevin Hansen)
- **Date:** 2000-03-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d28a8a.6575915@wingate>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38D282AA.68566297@home.com>`

```
On Fri, 17 Mar 2000 19:13:47 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

...Much snipped out...
>
>Consider where M/F missed out - Flexus and Norcom realized Windows was a
…[6 more quoted lines elided]…
>Jimmy

Thanks for mentioning us!  

Regarding the cost of the compilers, yes, they seem pretty expensive.
Particularly if you don't use most of the stuff that's shovelled in;
CICS, version control, (cumbersome) dialog systems, editors you don't
want or need, whatever...  

OTOH, the world we're addressing today is an order of magnitude more
complex; consider this:

Our original character mode DOS ScreenIO was conceived and brought to
market within six months with no real hair-pulling issues.  Very
simple design, straightforward internals.  It took us less than 1,000
hours of effort to get it on the street.  Lots of work, but nothing
you couldn't overcome by sheer determination.

GUI ScreenIO (our new Windows screen manager) took over three years
and over 8,000 hours of exceedingly finicky work to design and
implement.  This was only partly due to the complexity of the Windows
environment.  

The other BIG factor is, of course, that GUI ScreenIO does waaaayyy
more neat stuff than the old product, and we had to make it easy to
use.  Simplifying the Windows interface is no easy task; look at the
failure of the compiler vendors' GUI tools (or lack of them).  If it
were easy, there wouldn't be such a large demand for third-party COBOL
screen managers.

In order to be competitive these days you need to deliver excellence
because the market is FAR more demanding than it used to be.  The bar
has gone up considerably.

...not to say that I wouldn't like to see compiler prices come down,
of course!

Kevin
NORCOM COBOL Programming Tools
GUI ScreenIO; a cool COBOL/Windows Screen Manager
http://www.ScreenIO.com
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D2C8DF.EBE6153E@zip.com.au>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38D282AA.68566297@home.com> <38d28a8a.6575915@wingate>`

```
Kevin Hansen wrote:
> 
> GUI ScreenIO (our new Windows screen manager) took over three years
…[13 more quoted lines elided]…
> has gone up considerably.

This is chicken and egg.  I cannot get a GUI product into work running
cobol until it is proven on a real project and my company wont shell
out huge amounts for a potentially dead development stream.

If it was entry level pricing I might do some myself, prove it's worth
and effectively sell into the company (and country).  I can get
Borland C++ for free for 30 days,  the compiler after that for
nothing, the professional development version costs $1,500 Australian,
this is half of the prices I have seen here (about $1 aus = 60 cents
US).  The tools I have under Borland are very refined, compared to
some of the Cobol products I have seen.

Fujitsu Power Cobol just does not cut it with me (sorry)  It works on
a wizard method building gobs of code for you.  When you upgrade
versions, in order to guarantee the best facilities under the new
release the only choice is to rebuild the application from the
wizards. Compare this to SP2 where a new release means a relink (?)
and a new DLL.  All bugs fixes are contained in a clean package, if
the package is broken fix the package.  If there is a bug in the code
generation in Power cobol then you must advise the customers of the
problem and they must amend their code, potentially lots of it.

I commend Fujitsu for giving us the free compiler, I hope they
continue to do so.  I would hope that they release 4 the same way once
5 is firmly on the pavement.  This is the only way the language is
going to stay live.  I hope GNU cobol keeps singing along and takes
it's rightful place, the GNU C compiler is the best C compiler, no
flash tools but most innovation occurs there first.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 4)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-03-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d3bd08.10887300@news.epix.net>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38D282AA.68566297@home.com> <38d28a8a.6575915@wingate> <38D2C8DF.EBE6153E@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

[snip]
>
>This is chicken and egg.  I cannot get a GUI product into work running
…[16 more quoted lines elided]…
>and a new DLL.  All bugs fixes are contained in a clean package, if

Ken...I wanted to resolve the question mark in your comment.  Yes,
re-linking is needed for a couple of the compilers we support, but not
for all.  I agree with you that there is something to be said for
externalizing all of the fancy stuff!

>the package is broken fix the package.  If there is a bug in the code
>generation in Power cobol then you must advise the customers of the
…[11 more quoted lines elided]…
>http://www.zipworld.com.au/~waratah/


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: The Cost of COBOL

_(reply depth: 5)_

- **From:** jets@nbnet.nb.ca (Tony M. Mina)
- **Date:** 2000-03-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d5040c.1609225@allnews.nbnet.nb.ca>`
- **References:** `<ig32ds0m6nskc7ouhk21t86db1rf5voh6e@4ax.com> <38D282AA.68566297@home.com> <38d28a8a.6575915@wingate> <38D2C8DF.EBE6153E@zip.com.au> <38d3bd08.10887300@news.epix.net>`

```
On Sat, 18 Mar 2000 17:33:20 GMT, rtwolfe@flexus.com (Bob Wolfe) wrote:

>Ken Foskey <waratah@zip.com.au> wrote:
>
…[4 more quoted lines elided]…
>>out huge amounts for a potentially dead development stream.

We have been running Cobol on our production box for over a year now and
have not encountered any problems so far.

We use Cobol on the client/server side using Fujitsu and SP2 for the GUI
interface.  The system communicates with our Unisys 2200 mainframe using
Tuxedo from BEA systems to do online inquiry/update to our database.

All our current developments are using Cobol and SP2.  We have just
implemented a financial system about 2 months ago that monitors and
prints retirement income cheques all using Cobol and SP2. 

>>
>>If it was entry level pricing I might do some myself, prove it's worth
…[5 more quoted lines elided]…
>>some of the Cobol products I have seen.

This is one of the reason why we moved from Micro Focus to Fujitsu.  The
other is support.  The price of Fujitsu is better than most of the Cobol
compilers.  

>>
>>Fujitsu Power Cobol just does not cut it with me (sorry)  It works on
…[4 more quoted lines elided]…
>>and a new DLL.  All bugs fixes are contained in a clean package, if

We are using Fujitsu Cobol not the Fujitsu Power Cobol and use SP2 from
Flexus for our GUI interface.  The decision to use SP2 is portability
which it did happen to us when we moved from Micro Focus to Fujitsu.
None of the SP2 codes on the Micro Focus were changed.

We have been implementing new versions of SP2 and we never recompiled or
relinked our programs.  Only when there is a change in our programs.

For Fujitsu, the only thing we do for new versions is to reinstall the
Cobol runtime. No relinking or recompiling.

>
>Ken...I wanted to resolve the question mark in your comment.  Yes,
…[23 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
