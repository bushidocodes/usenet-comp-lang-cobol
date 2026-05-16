[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# z/OS and OS/VS Cobol

_58 messages · 11 participants · 2004-08 → 2005-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: z/OS and OS/VS Cobol

- **From:** dr_te_z <dr_te_z.1bn35m@mail.codecomments.com>
- **Date:** 2004-08-27T03:34:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dr_te_z.1bn35m@mail.codecomments.com>`

```

Mike wrote:
> *Okay I've searched the IBM website and am inundated with over
> 150,000 hits so I'm just going ask.
…[16 more quoted lines elided]…
> Thank You. *
You've got 2 options: to recompile or not to recompile...
Currently I work at a shop where they did not recompile. The've got a
mix now of old OS/VS load's and new OS/390 load's. Quite an
achievement....Seems to work fine.... Conversion was some time
ago....People forget about the old compiler.....
Strange things start to go wrong: when you do a minor change (recompile
because of a copybook change) programs crash at unexpected situations.
Little things come to haunt you (in the middle of the night). Take
"subscrips out of range", this kind of constructions:

Code:
--------------------
  
  01  some-array.
  03 some-def occurs 3
  05 some-field pic x.
  01  some-storage pic x.
  ......
  move 4      to subscript.
  if some-field (subscript) equal ...
  
--------------------
 
Get the picture? Some programmer coded this more than 15 years ago. Now
you recompile and guess what? The program abends on the "IF" statement
with an subscript out of range. It has been out-of-range more than 15
years but all of the sudden you get called in the middle of the
night... 

Bottom line: if you don't want this issue to haunt you for another 15
year than *recompile* the whole bloody lot. If not, manouvre yourself
in a positions that some else gets called at night ;)
```

#### ↳ Re: z/OS and OS/VS Cobol

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-27T19:03:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ALXc.222055$M95.47262@pd7tw1no>`
- **In-Reply-To:** `<dr_te_z.1bn35m@mail.codecomments.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com>`

```
dr_te_z wrote:

>Bottom line: if you don't want this issue to haunt you for another 15
>year than *recompile* the whole bloody lot. If not, manouvre yourself
>in a positions that some else gets called at night ;)
>  
>
I'm not in the mainframe world, but that sure sounds like good advice to 
me ! Even at PC-Level for a small shop, Unix etc., it makes sense. Some 
15-20 years ago Towers Perrin based here and a subsidiary of T & P in 
the States - specialized in Human Resources in Pension schemes etc.  The 
used Micro Focus COBOL, early days, didn't like M/F file performance so 
wrote their own. Then They moved to M/F Product B, then they moved to 
M/F Product C. At the time I was job hunting they had stuff written and 
working in A, B and C - LUVERLY !

Jimmy, Calgary AB
```

##### ↳ ↳ Re: z/OS and OS/VS Cobol

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-27T20:06:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no>`

```
On Fri, 27 Aug 2004 19:03:27 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:

> The 
>used Micro Focus COBOL, early days, didn't like M/F file performance so 
>wrote their own. Then They moved to M/F Product B, then they moved to 
>M/F Product C. At the time I was job hunting they had stuff written and 
>working in A, B and C - LUVERLY !

Perhaps an old gunny shouted 'If it ain't broke, don't fix it.'

I worked on a Spectra/70 that had a poor file system (LIOCS), so I
rewrote it. No problemo. It was a drop-in replacement. As a bonus, it
could read and write RCA-301 files natively, with regular JCL. Wave
bye to the emulator.

One could do stuff like that in the Good Old Days. Today, security
people would swarm like killer bees. You did WHAT?! Are you crazy?
This is a CERTIFIED SYSTEM! I'll give you five minutes. If it's there
when I return, I'm calling Mister Big.

Down the hall, a department manager drafts a job ad asking for out of
the box thinkers. Hyprocrisy, thy name is Prosaic.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

- **From:** docdwarf@panix.com
- **Date:** 2004-08-27T16:22:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgo56s$2ll$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com>`

```
In article <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:

[snip]

>Down the hall, a department manager drafts a job ad asking for out of
>the box thinkers. Hyprocrisy, thy name is Prosaic.

It has been that way for a goodly while, Mr Wagner; as Sam Goldwyn is said 
to have put it: 'I don't want any yes-men around me. I want everybody to 
tell me the truth even if it costs them their jobs.'

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 4)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-28T06:30:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ki70j0p5vr55ni7vmuh6gf5eqh0hb31kt9@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <cgo56s$2ll$1@panix5.panix.com>`

```
On 27 Aug 2004 16:22:52 -0400, docdwarf@panix.com wrote:

>In article <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com>,
>Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
…[8 more quoted lines elided]…
>tell me the truth even if it costs them their jobs.'

Sam and department managers don't understand poetry. They think it has
no utility in bidness. The closest approximations they can muster are
Yogi Berra-isms such as you quoted.

 One company does grok what's going on, Microsoft. In a leap of faith
in 1995, they bet the farm on GUI. Had it failed, hundreds of BILLIONS
would have gone down the drain. 

IBM didn't have the courage, some would say recklessness, nor did
others. If it were up to Sam and Armonk, we'd still be looking at
green screens and talking about IRMA boards as thougth they meant
something. Oh yeah, LU 6.2, we're fully compliant with dinosaur
standards.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-28T03:22:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408280222.7700ba0c@posting.google.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <cgo56s$2ll$1@panix5.panix.com> <ki70j0p5vr55ni7vmuh6gf5eqh0hb31kt9@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote


> Sam and department managers don't understand poetry.

Yet another broad brush nonsense.

>  One company does grok what's going on, Microsoft. In a leap of faith
> in 1995, they bet the farm on GUI. Had it failed, hundreds of BILLIONS
> would have gone down the drain. 

Load of crap.  MS Windows had been growing since 1990. '95 was just
another step. I have no idea where your nonsense 'hundreds of
billions' comes from.  Certainly not anything from MS.  If '95 failed
then MS just keeps selling 3.11 until NT which was being developed in
1995.
 
> IBM didn't have the courage, 

IBM did OS/2.  It may surprise you to know that OS/2 had a GUI.

> some would say recklessness, nor did
> others. If it were up to Sam and Armonk, we'd still be looking at
> green screens and talking about IRMA boards as thougth they meant
> something. Oh yeah, LU 6.2, we're fully compliant with dinosaur
> standards.

You locked yourself in a cupboard for too many decades.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-28T10:46:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgq5sr$2dk$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <cgo56s$2ll$1@panix5.panix.com> <ki70j0p5vr55ni7vmuh6gf5eqh0hb31kt9@4ax.com>`

```
In article <ki70j0p5vr55ni7vmuh6gf5eqh0hb31kt9@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On 27 Aug 2004 16:22:52 -0400, docdwarf@panix.com wrote:
>
…[13 more quoted lines elided]…
>no utility in bidness.

If that is true, Mr Wagner, then they would seem to be in accord with 
Socrates; in The Republic he says that poets have no place in his City, 
either.

>The closest approximations they can muster are
>Yogi Berra-isms such as you quoted.

'Include me out' is not poetry?

>
> One company does grok what's going on, Microsoft. In a leap of faith
>in 1995, they bet the farm on GUI.

Others might wish to address the tactics employed by Microsoft that 
insured the inclusion of its GUI on most PCs sold.

>Had it failed, hundreds of BILLIONS
>would have gone down the drain. 
>
>IBM didn't have the courage, some would say recklessness, nor did
>others.

When I was at the Deutsche Bank, Mr Wagner, I found something that looked, 
initially, to be odd.  There was an M&A (Mergers and Acquisitions) 
department... and it was subdivided into three different, almost 
autonomous departments, one for companies worth US$20 million or less, one 
for US$21 - 100 million and one for US$100 million and above.  I pondered 
what reason they might have for doing this...

... and concluded that in business, as in other things, a difference in 
quantity can make for a difference in quality.  The characteristics of 
people who run smaller businesses just might not be the same as the 
characteristics of those who run larger ones... what is considered 
important, what is a 'matter of scale', as it were, might be entirely 
different to a fellow who has managed to string together a bunch of 
trucking firms and to a CEO of a small multi-national.

For dealing with different kinds of people one might need... different 
kinds of people, hence three departments.  So it might be with IBM, a 
grey, hoary institution accustomed to dealing with grey, hoary 
institutions.  To use an analogy from the jungle... a big cat will not pay 
attention to a mouse - or even to a field full of mice - while a housecat 
will make meals out of them.

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-28T05:55:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7VXc.228871$M95.152820@pd7tw1no>`
- **In-Reply-To:** `<oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com>`

```
Robert Wagner wrote:

>On Fri, 27 Aug 2004 19:03:27 GMT, "James J. Gavan" <jjgavan@shaw.ca>
>wrote:
…[13 more quoted lines elided]…
>
But there's the rub Robert. It was BROKE. That's why they were 
recruiting, expecting some joker to put on all three hats as necessary.

Now me some 20 years ago did this oil/gas application in RM/COBOL ('74). 
Then I moved over to M/S and M/F with DOS so now I'm at '85. Then of 
course as soon as I hit VISOC/Net Express "technically" (not yet 
rubber-stamped), I'm real close to COBOL 2002. So I'm thinking 
if...End-if, in-line performs, all the END syntax , plus of course the 
EVALUATE, plus I go LOWERCASE.

The joker I was writing for was a techno-freak, dreaming up all sorts of 
new additions - can't wait for you to get the hang of Windows, GUIs and 
the OO stuff. Go back and do it in RM '74. Attuned to nested IFs and 
EVALUATES, I found it a challenge to go back to the '74 syntax, 
(completely bypassing '85 in between). plus of course I always forgot to 
go UPPERCASE., and even correct case COBOL '74 was an unhappy camper 
with END-IF.  What a royal pain in the butt - literally had to unscrew 
my head and put on a different brain-box. After about two years of this 
crap - he and I parted company.

<pause for smoke>

While outside thought on it. Why didn't I just transfer the application 
to Net Express as is. (CONVERT3 even supplies me a conversion from RM 
'74 data files to M/F format, but not '85 files). But get stuck on the 
screen displays which I think were specifically RM's  own. I did just 
take a peek at DIRECTIVES but didn't spot anything to do with DISPLAY.  
Bearing in mind I *was* trying to move forwards with N/E - again I could 
have converted to M/F's Screen Section - could have used their screen 
attributes, colouring, and what would have really appealed to him - the 
MOUSE - but that hassle would have delayed me yet some more.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-28T10:58:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgq6id$3bj$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no>`

```
In article <b7VXc.228871$M95.152820@pd7tw1no>,
James J. Gavan <jjgavan@shaw.ca> wrote:

[snip]

>Go back and do it in RM '74. Attuned to nested IFs and 
>EVALUATES, I found it a challenge to go back to the '74 syntax, 
…[3 more quoted lines elided]…
>my head and put on a different brain-box.

'... literally had to unscrew my head and put on a different brain-box.'

Hee hee hee... great minds and similar, small circles and all; just 
recently it was posted from:

<http://groups.google.com/groups?selm=cetnri%241hv%241%40panix5.panix.com&output=gplain>

--begin quoted text:

What caused me mirth is that when I started coding in 'OLDBOL' I dropped 
all uses of '85-or-above constructs... no reference-modification, no 
Evaluate... reflexively coding with '74 limitations.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 4)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-28T19:52:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no>`

```
On Sat, 28 Aug 2004 05:55:19 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:

> Attuned to nested IFs and 
>EVALUATES, I found it a challenge to go back to the '74 syntax, 
…[4 more quoted lines elided]…
>crap - he and I parted company.

You'd be forced to make the same regression if you worked for some
mainframe shops, where shop standards mandate '70s style programming. 
When management wants to do something new, say GUI, it's easier to
switch to another language than to fight the entrenched conservatism.

>While outside thought on it. Why didn't I just transfer the application 
>to Net Express as is. (CONVERT3 even supplies me a conversion from RM 
…[6 more quoted lines elided]…
>MOUSE - but that hassle would have delayed me yet some more.

I wouldn't have tried to convert screen code. I'd have ripped it out
and written new code .. packaged in a callable program. By
coincidence, I just did four programs that way. It wasn't screen code,
but the situation was analogous.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-28T21:23:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GJ6Yc.247736$J06.103950@pd7tw2no>`
- **In-Reply-To:** `<s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com>`

```
Robert Wagner wrote:

>I wouldn't have tried to convert screen code. I'd have ripped it out
>and written new code .. packaged in a callable program. By
…[3 more quoted lines elided]…
>
You are a bit like Attila the Hun - slash and burn  :-)     But I 
understand what you are getting at. Remember the application starts on a 
Radio Shack with RM/COBOL and 'Lonesome Dove' up here teaches himself 
COBOL.  With due modesty, I didn't do badly, supplemented by Daniel 
McCracken's 'Structured COBOL'. BUT - most  important I didn't have 
source from others to look at. Hurray! Micro Focus CompuServe Forum. Ask 
and you shall receive (most of the time).

Pete Dashwood posts something about Three-Tier Systems. I don't recall 
if he even spelled out what that meant - but Zappo - I zeroed in on that 
phrase and got the message. Sure went that route in M/F DOS and most 
emphatically in OO - because they blend like milk and cream. But 
unfortunately my old programs, although paragraphed, didn't take 
advantage of Three-Tier - the screen stuff popped up all over the place.

Yes you are right - even though it would have caused a fair bit of 
effort I should have hived off the screen stuff to separate callable 
programs - just like people are able to do with Flexus SP2..

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-29T02:22:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no>`

```
On Sat, 28 Aug 2004 21:23:50 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:

>You are a bit like Attila the Hun - slash and burn  :-)    

Get in and get out; take no prisoners. I learned it in Special Ops
and, later, in gonzo programming. :)

> But I 
>understand what you are getting at. Remember the application starts on a 
…[4 more quoted lines elided]…
>and you shall receive (most of the time).

McCracken is all you needed.  He showed good Cobol style before the
'85 standard. He dropped out of programming some time around 1982 to
become a Catholic monk, which he pursued for 10-15 years before
returning as a CS professor at NY City College. His best work was
probably "Numeric Analysis and FORTRAN Programming".

>Pete Dashwood posts something about Three-Tier Systems. I don't recall 
>if he even spelled out what that meant - but Zappo - I zeroed in on that 
…[3 more quoted lines elided]…
>advantage of Three-Tier - the screen stuff popped up all over the place.

Three-tier usually means client/server, where the tiers are hardware
platforms -- client, application server and database server. 

I live in that world, but don't think it's a valid model. Client and
application server can run on the same machine, separated only by
architecture. Using ODBC or JDBC, the database could theoretically
reside on the same machine as well. 

I don't think the separation need be enforced by hardware platforms.
It can be done with software discipline.

>Yes you are right - even though it would have caused a fair bit of 
>effort I should have hived off the screen stuff to separate callable 
>programs - just like people are able to do with Flexus SP2..

Flexus SP/2 is the quickest and easiest way to do GUI in Cobol. Not
just Windows but also Unix and Web pages. It's faster than VB and
DevStudio/C++. If only decision-makers understood ..
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-29T05:09:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FydYc.257236$gE.214955@pd7tw3no>`
- **In-Reply-To:** `<8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com>`

```
Robert Wagner wrote:

>>Pete Dashwood posts something about Three-Tier Systems. I don't recall 
>>if he even spelled out what that meant - but Zappo - I zeroed in on that 
…[11 more quoted lines elided]…
>
Nope on that one Robert you are wrong.  What you are describing is one 
aspect. When Pete mentioned it he was still into M/F in DOS mode so far 
as I'm aware - no fancy Client/Server stuff on his plate as I recall. He 
was watching, watching us with VISOC and when the price for that ZOOMED 
- he was off to using Fujitsu. At what stage he actually got into OO, I 
don't know.

Now OO - nothing to do with Client/Server - and let me stress - 
absolutely bugger all to do with GUIs. You could have an OO COBOL 
application invoking Report Writer or Screen Section. Just so happens 
GUIs are a neat extension -  follow it through, Simula--->Smalltalk----> 
Stevie Boy "borrows" for Apple -------> then gets real pissed off when 
Billy G. uses the GUI techniques for Windows.

Without question GUI-ing/Webbing/ or Client-Server  - great with OO - 
but take your pick they are the User Interface in a Three Tier System, 
the other two being obvious, Business Logic (I *really* hate 'Public 
Domain) and the data storage be it COBOL files or a DB. (Anyway even in 
pure Procedural on big iron you cold effectively use Three-Tier).

 It doesn't end there for me - by a bit of sub-classing I can repeat 
features in each of the Three-Tier elements - but I'm no way yet into 
Webbing in any fashion.

 McCracken isn't the only one who was chosen, but opted out  - very 
short time - kinda wished I stayed. My lot used to make a decent drop of 
red and white down in the Nappa Valley..

Jimmy
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 8)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-30T18:44:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no>`

```
On Sun, 29 Aug 2004 05:09:57 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:

>Robert Wagner wrote:
>
…[22 more quoted lines elided]…
>Billy G. uses the GUI techniques for Windows.

I don't understand the connection between OO, GUI, cyrptic languages
and immature personalities managing the computer industry.

>Without question GUI-ing/Webbing/ or Client-Server  - great with OO - 
>but take your pick they are the User Interface in a Three Tier System, 
>the other two being obvious, Business Logic (I *really* hate 'Public 
>Domain) and the data storage be it COBOL files or a DB. (Anyway even in 
>pure Procedural on big iron you cold effectively use Three-Tier).

Let me see if I've got this right. The three tiers are screen, logic
and disk?

> McCracken isn't the only one who was chosen, but opted out  - very 
>short time - kinda wished I stayed. My lot used to make a decent drop of 
>red and white down in the Napa Valley..

Drink enough vino and sub-classing becomes a blur.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 9)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-30T22:56:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-ADD5B2.22563430082004@knology.usenetserver.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com>`

```
In article <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com>,
 Robert Wagner <robert@wagner.net.yourmammaharvests> wrote:

> On Sun, 29 Aug 2004 05:09:57 GMT, "James J. Gavan" <jjgavan@shaw.ca>
> wrote:
…[25 more quoted lines elided]…
> >Billy G. uses the GUI techniques for Windows.

For the record, Steve J. and Apple paid Xerox PARC a huge sum of money 
for a 24-hour look at the Smalltalk environment being deveolped there.  
IIRC, it was far more revenue that the Xerox GUI systems ever generated 
via sales.   Then they hired the visionary that envisioned the idea, and 
first published it in 1968 as his masters thesis, to create it for 
Apple.  It was Jeff Raskins idea, he took it to Parc, he took it to 
Apple, he could take it where ever he wanted to, it was his.

That theft from Xerox story is just a cover to make M$ feel better for 
stealing the prerelease OS code it got to build Excel and Word and 
turning it into Windows 1.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-31T06:05:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VyUYc.275578$J06.237629@pd7tw2no>`
- **In-Reply-To:** `<joe_zitzelberger-ADD5B2.22563430082004@knology.usenetserver.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com> <joe_zitzelberger-ADD5B2.22563430082004@knology.usenetserver.com>`

```
Joe Zitzelberger wrote:

>In article <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com>,
> Robert Wagner <robert@wagner.net.yourmammaharvests> wrote:
…[51 more quoted lines elided]…
>
But what you haven't covered, nor mentioned in her own book,(Smalltalk 
80),  Stevie zeroed in on Adele Goldberg to tell him what he wanted to 
know at Xerox PARC. She spent at least an hour with her immediate boss 
pleading , "No, no, no...We will be giving away our trade secrets..". 
All to no avail. Her boss was adamant, telling her she had to talk to 
Stevie's Apple gang, (who were waiting while she and her boss were 
arguing), the order had come from above. She subsequently found out that 
was not case..

Very brief scene of Adele in the video, "The Pirates of Silicone Valley" 
- the life and times of S.J. and B.G.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 11)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-31T16:50:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4oa9j09tv0hv64biqvm1cnl8g8e97f85ug@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com> <joe_zitzelberger-ADD5B2.22563430082004@knology.usenetserver.com> <VyUYc.275578$J06.237629@pd7tw2no>`

```
On Tue, 31 Aug 2004 06:05:41 GMT, "James J. Gavan" <jjgavan@shaw.ca>
wrote:


>Very brief scene of Adele in the video, "The Pirates of Silicone Valley" 
>- the life and times of S.J. and B.G.

Silicone Valley is the San Fernando valley, northwest of Los Angeles,
where they make porn films. I wasn't aware Adele had that in her
skillset. She's a multifarious woman.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-31T12:04:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408311104.676532a6@posting.google.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com> <joe_zitzelberger-ADD5B2.22563430082004@knology.usenetserver.com> <VyUYc.275578$J06.237629@pd7tw2no>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote

> Very brief scene of Adele in the video, "The Pirates of Silicone Valley" 

I think that _Silicone_ Valley is somewhere else entirely, amongst the
hills of Hollywood perhaps.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 9)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-08-31T05:54:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2oUYc.275546$J06.188839@pd7tw2no>`
- **In-Reply-To:** `<t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com>`

```
Robert Wagner wrote:

>I don't understand the connection between OO, GUI, cyrptic languages
>and immature personalities managing the computer industry.
>
>  
>
Cryptic languages maybe, and your assessment of immature personalities, 
which could be true.. But they have enough green backs to wrap you and 
me and turn us into very expensive mummies.! I *wish* I was so immature !

>Let me see if I've got this right. The three tiers are screen, logic
>and disk?
>
>  
>
Noble effort. Almost -  8 out of 10. Way back when you and I were 
playing it "blind" - there were no VDUs.
Three-Tier - (1) Logic,  (2) Disk (perhaps some only had mag tape) and 
(3) UI - User Interface - punched cards, paper tape,  OCR, OMR etc. And 
as we were playing it 'blind' - those tabulations or printed reports 
could also be considered UI.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-30T23:23:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408302223.67c4e9ab@posting.google.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote 

> >Now OO - nothing to do with Client/Server - and let me stress - 
> >absolutely bugger all to do with GUIs. You could have an OO COBOL 
…[6 more quoted lines elided]…
> and immature personalities managing the computer industry.

No. But many of us may well understand the connection.

   Simula     - the first OO language
   Smalltalk  - an OO language at PARC - ie the first GUI
   'Stevie Boy' - Apple paid for a visit to PARC and to use the ideas
   'Bill G'    -  Apple paid MS to write applications for Lisa/Mac
                  MS stole the ideas and wrote Windows

The languages are only 'cryptic' to those who are unfamiliar with them.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 10)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-31T17:26:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0sb9j0li36mc8jhqd086jf0oo8udr8lrmp@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com> <217e491a.0408302223.67c4e9ab@posting.google.com>`

```
On 30 Aug 2004 23:23:36 -0700, riplin@Azonic.co.nz (Richard) wrote:

>   'Bill G'    -  Apple paid MS to write applications for Lisa/Mac
>                  MS stole the ideas and wrote Windows

Graphics is not a recent discovery. It's been used since the days of
cave paintings.

Lisa and Mac were circa. 1983. Microsoft began work on Windows two
years earlier and announced it would be available in 1983. As it
turned out,  Windows 1 didn't hit retail shelves until 1985.

GEM was a copy of Mac. Windows was inspired most by VisiOn.

The applications MS wrote for Mac were Word and Excel. Apple didn't
pay for development, retail customers eventually paid.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-01T01:03:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409010003.2a3c11b1@posting.google.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com> <217e491a.0408302223.67c4e9ab@posting.google.com> <0sb9j0li36mc8jhqd086jf0oo8udr8lrmp@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote

> >   'Bill G'    -  Apple paid MS to write applications for Lisa/Mac
> >                  MS stole the ideas and wrote Windows
> 
> Graphics is not a recent discovery. It's been used since the days of
> cave paintings.

What has that to do with it ?  
 
> Lisa and Mac were circa. 1983. Microsoft began work on Windows two
> years earlier and announced it would be available in 1983. As it
> turned out,  Windows 1 didn't hit retail shelves until 1985.

Sigh!!  Microsoft started working on Lisa (early 83) and then Mac
_before_ they were released.  They announced Windows in November 1983
and _then_ started working on it, which is why it wasn't out until the
end of 1985, by which time GEM had sold a million copies.

Your 'two years earlier' is quite wrong, at that time they were barely
getting DOS under control. They certainly were working on Apple       
                                                   products in '81 and
this is where MS got its ideas.  It was building Word and rewriting
Multiplan to run on Lisa/Mac and later developed Windows to run these
on top of.

> GEM was a copy of Mac. 

Let us see how likely that is.  GEM was developed from the ealier GSX
and was demonstrated in Novemeber 1983 at Comdex.  Not unconnected was
MS announcing the completely vapourware Windows at the same show. The
Mac was not until 1984.

GEM was developed entirely from Xerox PARC, exactly as Lisa/Mac was. 
You may also be confused by the fact that TOS for the Atari which ran
GEM was developed from CP/M-68K for the Macintosh - both being 680x0
machines.

> Windows was inspired most by VisiOn.

Vision may have been prior to Windows and GEM, and MS may steal ideas
from anyone, but Windows 1 owed more to LISA than to VisiOn. For
example it internals were designed for Pascal, same as Apple's. 
VisiOn was overlapped windows while Windows 1 was tiled only.

> The applications MS wrote for Mac were Word and Excel. Apple didn't
> pay for development, retail customers eventually paid.

Apple needed applications, they 'funded' part of the development. They
also had to give MS access to the internals.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 12)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-02T03:59:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d14dj0pfuldaevkgqbnl5e6m1phrrl9vnv@4ax.com>`
- **References:** `<3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com> <217e491a.0408302223.67c4e9ab@posting.google.com> <0sb9j0li36mc8jhqd086jf0oo8udr8lrmp@4ax.com> <217e491a.0409010003.2a3c11b1@posting.google.com>`

```
On 1 Sep 2004 01:03:17 -0700, riplin@Azonic.co.nz (Richard) wrote:

>Robert Wagner <robert@wagner.net.yourmammaharvests> wrote

>> Lisa and Mac were circa. 1983. Microsoft began work on Windows two
>> years earlier and announced it would be available in 1983. As it
…[5 more quoted lines elided]…
>end of 1985, by which time GEM had sold a million copies.

The truth is probably inbetween. The first announced delivery date was
November 1983. My guess is they had a few people Working on Windows in
'81. Some time in '82 or '83 they changed direction and started over.

>Your 'two years earlier' is quite wrong, at that time they were barely
>getting DOS under control. They certainly were working on Apple       
…[3 more quoted lines elided]…
>on top of.

They had a good GUI Word for DOS in '86 (I was trying to compete with
it) but Mac Word came in '85 (or sooner) and was  better.

>> GEM was a copy of Mac. .
>
>GEM was developed entirely from Xerox PARC, exactly as Lisa/Mac was. 

Ok, they had a common ancestor.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 13)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-02T12:34:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409021134.4834aa12@posting.google.com>`
- **References:** `<3ALXc.222055$M95.47262@pd7tw1no> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <GJ6Yc.247736$J06.103950@pd7tw2no> <8cf2j05vjhj0il0lpvue5h9ehrjlu4v2qi@4ax.com> <FydYc.257236$gE.214955@pd7tw3no> <t0i6j0h6c2j417gf0qva8ja6ppe7dm2g27@4ax.com> <217e491a.0408302223.67c4e9ab@posting.google.com> <0sb9j0li36mc8jhqd086jf0oo8udr8lrmp@4ax.com> <217e491a.0409010003.2a3c11b1@posting.google.com> <d14dj0pfuldaevkgqbnl5e6m1phrrl9vnv@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote

> The truth is probably inbetween. The first announced delivery date was
> November 1983. 

No. In November 1983 they announced that they would have a GUI.  They
did not give a delivery date (beyond their usual 'any day now'), and
if they had given a date it could not have been the same week that
they first mentioned the idea.

The first actual delivery was two years later.  DRI's GEM (which in
many opinions was better than Windows 1) was developed in much less
time than that.

It seems that they were prompted into announcing by DRI
_demonstrating_ a GUI at the same show.

Most MS product announcements seem designed to stop people buying
competitors products while MS throws something together, or buys in a
product they can claim as their own.

> My guess is 

Why do you think that guesses are useful ?

> they had a few people Working on Windows in '81. 

You may try looking at earlier discussions about 'future directions'
such as Paul Allen's speech which was published in Byte in mid '82
about what would be in the 'next release' of MS-DOS.  That also said
'any day now' yet it was over a year later that it came out and only
had half of what was promised.

In fact some of the things that were in the speech din't arrive until
MS-DOS 5, such as command-line editing, and probably only then because
DR-DOS 5 had it (and many other things) and was eating their lunch.

> Some time in '82 or '83 they changed direction and started over.

So the earlier 'thing' _wasn't_ 'Windows'.

In fact in Paul Allen's speech he talks about extending the ANSI.SYS
to emulate a graphics terminal and providing a Help system, and
generally things much like the menuing system in MS-DOS 4.01.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-28T20:44:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgr8td$oij$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com>`

```
In article <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On Sat, 28 Aug 2004 05:55:19 GMT, "James J. Gavan" <jjgavan@shaw.ca>
>wrote:
…[10 more quoted lines elided]…
>mainframe shops, where shop standards mandate '70s style programming. 

Hmmmmmm... I'm not sure about this.  One of the things I was taught about 
writing code - both maintaining it and new development - is that it is a 
Very Good Idea to try to stay close to 'that which has gone on before', to 
keep what you are doing close to the shop's style.  Data Processing... 
errrr, Information Science... errrr, Management Information Services... 
errrr, humping code for big-iron shops seems to have had a kind of 
'freeze' in the late 1960's to the mid-late 1970's, where standards were 
discussed in committees, written down and typed up by secretaries and 
placed in three-ring binders that get locked up every night, along with 
the Job Restart procedures; I haven't seen many 'shop standards' that 
include the constructs of COBOL '85.

A lot of the code written two, three decades back is still running... and 
when it blows up and needs to be fixed, or when it needs to be extended to 
cover the recently-acquired subsidiary, or when a new system needs to be 
built to do stuff with its data it is a bit of a delicate balance; on the 
one hand one needs to maintain the structure - so that a shopful of coders 
who know, reflexively, to look in the 7000- level paragraphs for IO 
routines don't get thrown by your putting a REWRITE in the 3000- level 
edit routines - and at the same time be able to make use of the full range 
of the language (which has changed a wee bit since then).

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-29T03:39:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e5j2j0590glqnfqn0etr76q80f00sbs5n9@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com>`

```
On 28 Aug 2004 20:44:29 -0400, docdwarf@panix.com wrote:

>  One of the things I was taught about 
>writing code - both maintaining it and new development - is that it is a 
…[8 more quoted lines elided]…
>include the constructs of COBOL '85.

Those shop standards are killing the Cobol I love.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-29T11:04:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgsr91$3t8$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <e5j2j0590glqnfqn0etr76q80f00sbs5n9@4ax.com>`

```
In article <e5j2j0590glqnfqn0etr76q80f00sbs5n9@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On 28 Aug 2004 20:44:29 -0400, docdwarf@panix.com wrote:
>
…[12 more quoted lines elided]…
>Those shop standards are killing the Cobol I love. 

Those shop standards are also in place for organisations which process 
staggering amounts of data with 'six sigma' accuracy... and have been 
doing so since before anyone made a buzzword of 'six sigma' accuracy.

Funny ol' world, ain't it?

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 8)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-30T00:01:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<agr4j0tubf99n9cn2ufhcfih8h35m9r0ag@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <e5j2j0590glqnfqn0etr76q80f00sbs5n9@4ax.com> <cgsr91$3t8$1@panix5.panix.com>`

```
On 29 Aug 2004 11:04:01 -0400, docdwarf@panix.com wrote:

>In article <e5j2j0590glqnfqn0etr76q80f00sbs5n9@4ax.com>,
>Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
…[18 more quoted lines elided]…
>doing so since before anyone made a buzzword of 'six sigma' accuracy.

Do you know what 'six sigma' means?

It's hyperbole, self-congratulation unsupported by fact. In the real
world of finite numbers and limited life expectancy, there is a 50%
probability that five sigma exists.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-29T20:34:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgtsn4$d6l$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <e5j2j0590glqnfqn0etr76q80f00sbs5n9@4ax.com> <cgsr91$3t8$1@panix5.panix.com> <agr4j0tubf99n9cn2ufhcfih8h35m9r0ag@4ax.com>`

```
In article <agr4j0tubf99n9cn2ufhcfih8h35m9r0ag@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On 29 Aug 2004 11:04:01 -0400, docdwarf@panix.com wrote:
>
…[22 more quoted lines elided]…
>Do you know what 'six sigma' means?

Meaning is the result of interpretation, Mr Wagner... some interpret six 
sigma accuarcy as 99.99966%, some as 99.9997%.

>
>It's hyperbole, self-congratulation unsupported by fact. In the real
>world of finite numbers and limited life expectancy, there is a 50%
>probability that five sigma exists. 

And, of course, 87.2% of UseNet statistics are made up on the spot.  Did 
you know, Mr Wagner, that since every lottery ticket has a 50% chance of 
being a winner?  After all, either it is a winner or it is not, since the 
only options are one of two then 50% is a valid conclusion...

... and I am the King of England.

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 10)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-31T00:23:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<60h7j0hm8c2h1sn5c8ebmje1gjbbcb1iuj@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <e5j2j0590glqnfqn0etr76q80f00sbs5n9@4ax.com> <cgsr91$3t8$1@panix5.panix.com> <agr4j0tubf99n9cn2ufhcfih8h35m9r0ag@4ax.com> <cgtsn4$d6l$1@panix5.panix.com>`

```
On 29 Aug 2004 20:34:44 -0400, docdwarf@panix.com wrote:

>In article <agr4j0tubf99n9cn2ufhcfih8h35m9r0ag@4ax.com>,
>Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:

>>Do you know what 'six sigma' means?
>
>Meaning is the result of interpretation, Mr Wagner... some interpret six 
>sigma accuarcy as 99.99966%, some as 99.9997%.

That's what they say. They're wrong. 

Most calculators don't go to six standard deviations. This one almost
does (its JavaScript can be modified to go higher).

http://www.swogstat.org/stat/public/normal_calculator.htm

Tell it to calculate the standard deviation ("critical value"), enter
.999997 in the bottom box and observe the answer: 4.5

Try .999999999 (nine 9s). It's still not up to 6

Why do we trust quality to people who can't do  basic statistical
calculations?
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-30T22:16:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ch0n1u$rm8$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <agr4j0tubf99n9cn2ufhcfih8h35m9r0ag@4ax.com> <cgtsn4$d6l$1@panix5.panix.com> <60h7j0hm8c2h1sn5c8ebmje1gjbbcb1iuj@4ax.com>`

```
In article <60h7j0hm8c2h1sn5c8ebmje1gjbbcb1iuj@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On 29 Aug 2004 20:34:44 -0400, docdwarf@panix.com wrote:
>
…[8 more quoted lines elided]…
>That's what they say. They're wrong. 

That's what you say.  You're wrong.  See how easy it is?  Now, for a 
cite... how about

>
>Most calculators don't go to six standard deviations.

And this has an effect on the defining of six sigma as '3.4 defects per 
million units produced'... how?

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 9)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2004-09-02T04:37:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040902003712.03719.00000036@mb-m26.aol.com>`
- **References:** `<agr4j0tubf99n9cn2ufhcfih8h35m9r0ag@4ax.com>`

```
>From: Robert Wagner robert@wagner.net.yourmammaharvests 
>Date: 8/29/04 8:01 PM Eastern Daylight Time

>
>Do you know what 'six sigma' means?
>

Around my shop we call it 'sick' sigma.

I have been called in to 'testify' in numerious green belt and black belt
projects to reduce the bane of everyone's existence (at least listening to the
people contacting me) called Unbilled.  

I've told them I knew exactly how to reduce this horrendous problem.  You do A,
B, C and D and it'll be reduced by at least 75%. After that it should be easy
to identify the rest.

So far I don't know of any projects that have been completed.

BTW - if anyone has a Black Belt I believe their hiring :)

>
>It's hyperbole, self-congratulation unsupported by fact. In the real
>world of finite numbers and limited life expectancy, there is a 50%
>probability that five sigma exists. 
>

You're optomistic :)
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2004-09-02T05:27:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ch6p22$kb9$1@panix5.panix.com>`
- **References:** `<agr4j0tubf99n9cn2ufhcfih8h35m9r0ag@4ax.com> <20040902003712.03719.00000036@mb-m26.aol.com>`

```
In article <20040902003712.03719.00000036@mb-m26.aol.com>,
YukonMama <yukonmama@aol.com> wrote:
>>From: Robert Wagner robert@wagner.net.yourmammaharvests 
>>Date: 8/29/04 8:01 PM Eastern Daylight Time
…[9 more quoted lines elided]…
>people contacting me) called Unbilled.  

Hmmmmm... to the best of my knowledge there are two ways: enforce the POD 
(Pay Or Die) mailings or write 'em off.

>
>I've told them I knew exactly how to reduce this horrendous problem.  You do A,
…[3 more quoted lines elided]…
>So far I don't know of any projects that have been completed.

Now let me get this straight: you claim to have a way to increase 
successful billings (reduced unbilled = more billed) and it has not even 
been attempted?

Whose turf would it be stepping on?

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 11)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2004-09-09T02:02:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040908220248.22107.00003221@mb-m07.aol.com>`
- **References:** `<ch6p22$kb9$1@panix5.panix.com>`

```
>Subject: Re: z/OS and OS/VS Cobol
>From: docdwarf@panix.com
>Date: 9/2/04 5:27 AM Eastern Daylight Time
>

>Now let me get this straight: you claim to have a way to increase 
>successful billings (reduced unbilled = more billed) and it has not even 
…[3 more quoted lines elided]…
>

A four letter car company's.

I'd say 50% is caused by not having a PO in the first place.  New parts go out
the door to the customer as negotiations for a price are still in the works.

Another 45% is caused by bad PO numbers being used to ship.  The shipping
clerks key in what ever they want if they can't find the PO at a moments notice
because the truck has to get out or we shut down the JIT manufacturing plants. 
My idea would be to kill the override switch (they get an error and can put an
X in a field and override it).

The last 5% consists of miskeyings (zero instead of oh), bad quantites (PO is
for 10 and they ship 100 - usually the PO is wrong not the shipment) and what
we call class codes - this determines if the part being shipped is a production
part (ie original part of the automobile) or a service part (ie being fixed or
recalled or what have you after it leave the production line).

It is the 45% that can be corrected and some of the last 5% depending on the
solution they want to use.

But one shall not (carved as the 11th commandment) shut down the customers
production plants.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2004-09-08T22:08:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chodur$nvf$1@panix5.panix.com>`
- **References:** `<ch6p22$kb9$1@panix5.panix.com> <20040908220248.22107.00003221@mb-m07.aol.com>`

```
In article <20040908220248.22107.00003221@mb-m07.aol.com>,
YukonMama <yukonmama@aol.com> wrote:
>>Subject: Re: z/OS and OS/VS Cobol
>>From: docdwarf@panix.com
…[10 more quoted lines elided]…
>A four letter car company's.

Don't ask me how I know to ask such a question... sometimes the magic 
works, sometimes it doesn't.

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 6)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-29T09:43:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com>`

```
In article <cgr8td$oij$1@panix5.panix.com>, docdwarf@panix.com wrote:

> In article <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com>,
> Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
…[36 more quoted lines elided]…
> DD

My shop is one of the 15 largest IBM shops in the world (up from top 25 
a few years ago).  We have an application that was completely written in 
Cobol-85 from the early 1990's that contains about 60,000 unique 
elements (programs, copybooks, IMS segment layouts and DB2 table 
layouts).

That latest enhancement is to add XML WebServices to access all of the 
business functions of the system.  All of the XML parsing, WSDL 
generation, etc is written in Cobol-85.  A very modern approach 
considering the usual complaints about the z/OS platform and the Cobol 
language.

This system never saw a Cobol-74 style compiler, yet we had standards 
that reflected an overt hostility toward Cobol-85 features from the 
beginning.  For example, nested programs were verboten.  All performs 
must be out-of-line perform/thru with a corresponding exit paragraph.  
The paragraphs must be numbered.  Certain 85 statements were discouraged 
(SORT/SEARCH/INSPECT/EVALUATE).

(The original head of the standards committee just took an early 
retirement.  In the intervening months the perform/thru standard has 
been made optional and the numbers are coming into question next week. 
;-)

The problem with staying close to 'what has gone before' is that you 
often ignore 'new features that are available'.  New features are 
usually added to address some need.  To not use them leaves one with the 
old limitations.

What is the true benefit of 70's style programming?  Does it run faster?  
With less bugs?  Is it quicker to write?  Is it easier to understand?
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-29T11:47:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgstrd$9f3$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>`

```
In article <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <cgr8td$oij$1@panix5.panix.com>, docdwarf@panix.com wrote:

[snip]

>> Hmmmmmm... I'm not sure about this.  One of the things I was taught about 
>> writing code - both maintaining it and new development - is that it is a 
…[8 more quoted lines elided]…
>> include the constructs of COBOL '85.

[snip]

>This system never saw a Cobol-74 style compiler, yet we had standards 
>that reflected an overt hostility toward Cobol-85 features from the 
…[3 more quoted lines elided]…
>(SORT/SEARCH/INSPECT/EVALUATE).

The only one of these which is an '85 statement' is EVALUATE.

>
>(The original head of the standards committee just took an early 
>retirement.  In the intervening months the perform/thru standard has 
>been made optional and the numbers are coming into question next week. 
>;-)

This might be a sign as to why the standards were written as they were; I 
have run across shops where prohibitions against SORT and SEARCH were in 
place due to a single person's dislike thereof.  INSPECT and STRING were 
frequently prohibited because the code they compiled to was seen to be a 
drag for the online (CICS) programs.

>
>The problem with staying close to 'what has gone before' is that you 
>often ignore 'new features that are available'.  New features are 
>usually added to address some need.  To not use them leaves one with the 
>old limitations.

Life is Balance, aye.

>
>What is the true benefit of 70's style programming?  Does it run faster?  
>With less bugs?  Is it quicker to write?  Is it easier to understand?

'Benefits' of any kind are evaluated differently; one balances time, 
money, aesthetics and comfort.  As for 'true'... Pilate's question springs 
to mind.  It might be that, as mentioned above, the Guy in the Corner 
Office is uncomfortable with certain constructs and bans them... or it 
might be that when the company had twin, slaved 360s the Head Programmer 
ran some 'tests' which validated his prejudices... errrrr, proved the 
inefficiencies of certain constructs and they were removed, as well.

'Easier to understand', as has been noted before, might be dependent on 
what one is accustomed to... and *that* might be the strongest argument of 
all.

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 8)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-30T08:40:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C3FA80.08403930082004@knology.usenetserver.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <cgstrd$9f3$1@panix5.panix.com>`

```
In article <cgstrd$9f3$1@panix5.panix.com>, docdwarf@panix.com wrote:

> In article <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>,
> Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[37 more quoted lines elided]…
> drag for the online (CICS) programs.

The prohabitions against those relate back to the release of one of the 
pre-85 compilers that did OS getmains when executing those statements, 
eventually causing CICS regions to go SOS.  In this sense it was very 
much like the READ-INTO discussion we just had -- because IBMs Cobol-74 
compiler once screwed it up, it's use shall be forbidden forever --  
regardless of fixes to the Cobol-85 compiler that corrected the problem.


> >The problem with staying close to 'what has gone before' is that you 
> >often ignore 'new features that are available'.  New features are 
…[15 more quoted lines elided]…
> inefficiencies of certain constructs and they were removed, as well.

To allow such things to remain through compiler releases or runtime/OS 
releases is a great disservice to the shop.  I would be slacking, both 
as a stockholder and an employee, if I didn't speak up about a company 
wasting time, resources and money on four-decade-old workarounds to 
no-longer-existant problems.


> 'Easier to understand', as has been noted before, might be dependent on 
> what one is accustomed to... and *that* might be the strongest argument of 
> all.

I tend to think that if one is selling oneself as a 'programmer' of a 
certain language, one ought to read and be familier with the reference 
for said language -- e.g. understand all of it.  Cobol is reasonably 
finite, IBMs version even more so, many features are unimplemented or 
unused in many installations, it is not an unreasonable request.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-30T10:07:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgvcbe$bp6$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <cgstrd$9f3$1@panix5.panix.com> <joe_zitzelberger-C3FA80.08403930082004@knology.usenetserver.com>`

```
In article <joe_zitzelberger-C3FA80.08403930082004@knology.usenetserver.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <cgstrd$9f3$1@panix5.panix.com>, docdwarf@panix.com wrote:
>
>> In article <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>,
>> Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:

[snip]

>> This might be a sign as to why the standards were written as they were; I 
>> have run across shops where prohibitions against SORT and SEARCH were in 
…[9 more quoted lines elided]…
>regardless of fixes to the Cobol-85 compiler that corrected the problem.

So... it seems that at one point there were Very Sound Reasons for some 
standards but the mechanism for maintaining the standards is not keeping 
up with changes in technology, a sort of 'corporate inertia'.  This is not 
unique to corporate entities; it is easy to hear legislators bemoan the 
fact that technology is changing faster than the laws applicable to it 
are, as in the case of, say, what can be covered by a wiretapping warrant.

[snip]

>> >What is the true benefit of 70's style programming?  Does it run faster?  
>> >With less bugs?  Is it quicker to write?  Is it easier to understand?
…[13 more quoted lines elided]…
>no-longer-existant problems.

Hee hee hee... I *knew* I carried this around for a reason!  From Beyond 
Computing Magazine, May, 1996, pg. 51, sidebar entitled 'Cultural 
Contradictions' (caps original):

--begin quoted text:

MANAGEMENT WELCOMES YOUR CRITICISM.
As long as they like what they hear.

...

SPEAK UP AT MEETINGS.
And get shot down.

FRESH IDEAS, NEW WAYS OF DOING THINGS ARE WHAT MANAGEMENT WANTS.
All we hear is, 'If it ain't broke, don't fix it.'

--end quoted text

>
>
…[8 more quoted lines elided]…
>unused in many installations, it is not an unreasonable request.

Read it, sure, be familiar with it, fine... but implement it?  That just 
might be another story.

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-29T12:38:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408291138.13164383@posting.google.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>`

```
Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote 

> (The original head of the standards committee just took an early 
> retirement.

> What is the true benefit of 70's style programming?  Does it run faster?  
> With less bugs?  Is it quicker to write?  Is it easier to understand?

The advantage is: The head of the standards committee wrote them as
the highlight of his career in the 60s and no one dared tell him to
bugger off and do something else less harmful.

In other words The dvantage of keeping the standards is that you kept
your job.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 7)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-30T00:02:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>`

```
On Sun, 29 Aug 2004 09:43:23 -0400, Joe Zitzelberger
<joe_zitzelberger@nospam.com> wrote:


>What is the true benefit of 70's style programming?  Does it run faster?  
>With less bugs?  Is it quicker to write?  Is it easier to understand?

It's 'what I'm comfortable with.' It's 'what I learned 30 years ago
and have been doing since.' It marches under the banner of
conservatism -- preserving the past under the belief tried-and-true is
a safer choice than untested. 

The issue appears to be evolution vs. revolution. There is strong
support for the idea that evolution is better. See for example
Alexander's 'Notes on the Synthesis of Form' (Harvard Press). But the
people we're talking about aren't evolving. They're digging their
claws into the '70s and refusing to let go. They are not
conservatives, they're reacionaries. 

Simply put, they stopped learning new skills in the '70s out of
personal laziness.  Why should companies support their personal sloth?
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-29T20:38:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgtstf$dgq$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com>`

```
In article <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On Sun, 29 Aug 2004 09:43:23 -0400, Joe Zitzelberger
><joe_zitzelberger@nospam.com> wrote:
…[3 more quoted lines elided]…
>>With less bugs?  Is it quicker to write?  Is it easier to understand?

[snip]

>Simply put, they stopped learning new skills in the '70s out of
>personal laziness.  Why should companies support their personal sloth?

Perhaps it is because the results - quantified, numerically-qualified 
results, the numbers in the inventory, on the reports and, most 
importantly, on the profit-and-loss statements - keep the company in a 
sufficient amount of profit so that ROI on alternate systems is deemed 
insufficient to merit change.

Double-entry bookkeeping was invented a few centuries back, last I looked.

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 9)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-31T00:23:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mvg7j01grnidt51a7hoqmhss7p87r2prmh@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <cgtstf$dgq$1@panix5.panix.com>`

```
On 29 Aug 2004 20:38:07 -0400, docdwarf@panix.com wrote:

>In article <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com>,
>Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
…[16 more quoted lines elided]…
>insufficient to merit change.

They can't say that without comparative numbers, which they don't
have. I've seen it both ways in the same shop -- before massive
rewrite and after. After rewrite, the number of lines of source to
maintain went down by 50%, run times went down by 30%, errors
(measured in abends) went down substantially (I neglected to keep the
numbers), maintenance was faster and less error-prone (measured in IT
budget).

With clean code, we were able to add features that wouldn't have been
attempted or practical with the old code. For instance, well over 99%
of general ledger entries were computer generated and every one of
them had a reference to the document of original entry. As a result,
we closed the books and published statements four days after the end
of the fiscal period. At the end of the fiscal year, the computer
printed corporate tax returns, including all book-to-tax adjustments,
untouched by human hands. 

What's the value of integrated systems and timely information? Ask
management. They loved it. They thought it was worth more than keeping
obsolete programming standards.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-30T22:18:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ch0n5a$rpm$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <cgtstf$dgq$1@panix5.panix.com> <mvg7j01grnidt51a7hoqmhss7p87r2prmh@4ax.com>`

```
In article <mvg7j01grnidt51a7hoqmhss7p87r2prmh@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On 29 Aug 2004 20:38:07 -0400, docdwarf@panix.com wrote:
>
…[21 more quoted lines elided]…
>have.

They can say anything they want to, Mr Wagner... as long as they're in a 
country which allows such speech; as to what 'they' do or don't have... 
who knows?

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 8)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-30T00:14:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408292314.43d72c73@posting.google.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote

> >What is the true benefit of 70's style programming?  Does it run faster?  
> >With less bugs?  Is it quicker to write?  Is it easier to understand?
…[14 more quoted lines elided]…
> personal laziness.  Why should companies support their personal sloth?

This is just your usual rant against mainframe programmers.  You make
personal insults against them when, for the most part, they are
following what their employers are telling them to do.

Do you rant against McDonald employees because they are 'too ignorant
and lazy' to bring in their own home made vegetarian meals to serve to
the customers ?

Do you think they should rise up against their oppressors and put the
standards setters to the guillotine ?

Throwing insults at them does not make them your friends who want to
support your aims.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 9)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-31T00:23:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2vg7j0dshk49ab5ogk43v9b6mlpr7r9o0m@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <217e491a.0408292314.43d72c73@posting.google.com>`

```
On 30 Aug 2004 00:14:51 -0700, riplin@Azonic.co.nz (Richard) wrote:

>Robert Wagner <robert@wagner.net.yourmammaharvests> wrote

>> Simply put, they stopped learning new skills in the '70s out of
>> personal laziness.  Why should companies support their personal sloth?
…[3 more quoted lines elided]…
>following what their employers are telling them to do.

Executives and stockholders don't even know, much less care, about
obsolete programming style. If you're talking about their agent, the
white-haired guy in the corner office, he's about to retire. His
replacement grew up on C and has no investment in UPPER-CASE
PROGRAMMING.

>Do you rant against McDonald employees because they are 'too ignorant
>and lazy' to bring in their own home made vegetarian meals to serve to
>the customers ?

I used to .. in rec.food.veg. The ones who were pissed weren't
omnivores, they were fanatic 'religious' vegans who thought I didn't
go far enough. Do you recognize the name of net-kook Dr. Jai Maharaj?
This newsgroup is mild compared to what they dish out. And they were
mild compared to alt.smokers, where quasi-religious opposition reached
a crescendo that defies description. As a result of that experience,
I've read every name-calling, cheap shot, emotion-based argument
possible. It prompted me to write articles on logical fallacies. 

If you want to hone your 'craft', look to alt.flame or alt.2600. I
haven't been there in ten years but back in the day some of the
players were brilliant. Every message was original, not repetitive.
Here's a sample (Gentle readers should probably fast forward at this
point. What's coming up will probably gross you out.)

: The scientology kooks have a "church" here in Austin, right across
: the street from the UT campus.  They often have a table on the sidewalk,
: in a pathetic attempt to sell lies to anybody with $.  I frequently
: ride past on my bicycle, and steal a few books, usually a couple times
: per week, then use the pages for toilet paper.  Once I ran out of
: rolling papers, and rolled a joint with part of one of those funny,
: nearly blank pages with just a column of odd phrases on the left side.
: When I was stealing books from them just a few weeks ago, one of them
: who claimed to be "Everclear 14" or something wierd like that, saw me
: and started chasing me down the street.  I went slow deliberately, and
: he caught up around the corner, at the entrance to the alley.  I acted
: scared, my hands shaking seemingly from fear, but really because my
: adrenalin was pumping, ready for action.  Everclear 14 demanded the
: return of the books, and I stuttered as I protested my innocence, based
: upon a claim of urgent need for the knowledge of Hubbard.  Everclear 14
: hesitated, then started to pitch the bogus classes at a bargain price.
: I feigned interest, and suggested that we move up the alley a few yards,
: in order not to be interrupted by passersby.  We walked up the alley
: a short way, I leaned my bike up against a building, then with a quick,
: fluid motion, kicked Everclear 14 in the knee, a soft, satisfying crunch
: as ligament and cartilage crushed, an urgent stiffy bulging outward the
: front of my trousers as I waded in, right-left-right hook combinations
: staggering the evil demagogue backwards into a pile of rubbish.  He
: pleaded incoherently, hands out in front of his face with fingers
: splayed, eyes rimmed with the whiteness of total terror, a thick
: glistening viscous pendant of slobber waving as he babbled.  I jammed
: a straight right karate punch into the center of the noise, snapping
: his index finger without slowing, my knuckles crunching cartilage,
: blood gushing out of a double-barrel nosebleed, head laid back on his
: shoulders then bouncing forward as Everclear 14 planted his teeth in
: the pavement.  I rifled his pockets, scoring a fat wad of cash and
: a secret scientology code book, which I will be posting in the near
: future.  As Everclear 14 lay comatose, twitching seductivley, I
: found my fulfillment in the warm, wet, slippery and tight socket
: which formerly housed his left eye.  I walked down the alley, informed
: a few of the scuzziest street people that there was good pickings,
: waited until they'd made off with his clothing, then rode home.

>Do you think they should rise up against their oppressors and put the
>standards setters to the guillotine ?
>
>Throwing insults at them does not make them your friends who want to
>support your aims.

I don't want to count dumb-asses and sell-outs among my 'friends'.
They'd sell me out just as readily.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-30T22:21:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ch0nc0$rum$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <217e491a.0408292314.43d72c73@posting.google.com> <2vg7j0dshk49ab5ogk43v9b6mlpr7r9o0m@4ax.com>`

```
In article <2vg7j0dshk49ab5ogk43v9b6mlpr7r9o0m@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:

[snip]

>If you want to hone your 'craft', look to alt.flame or alt.2600. I
>haven't been there in ten years but back in the day some of the
…[5 more quoted lines elided]…
>: the street from the UT campus.

I do not know anyone whose 'craft' might be honed by looking at an 
apparently adolescent fantasy of violence and sex, Mr Wagner... but some 
might find it interesting that you thought it worthy of posting.

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 11)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-31T11:50:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4p8j05uss5o7a48du20c1l8jefds2fupm@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <217e491a.0408292314.43d72c73@posting.google.com> <2vg7j0dshk49ab5ogk43v9b6mlpr7r9o0m@4ax.com> <ch0nc0$rum$1@panix5.panix.com>`

```
On 30 Aug 2004 22:21:52 -0400, docdwarf@panix.com wrote:

>In article <2vg7j0dshk49ab5ogk43v9b6mlpr7r9o0m@4ax.com>,
>Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
…[14 more quoted lines elided]…
>might find it interesting that you thought it worthy of posting.

I thought it was a good example of creative writing. Sure, it was
adolescent, probably written by a college student. But I liked the way
it painted imagery with words. Wish we had more of that here.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2004-08-31T08:01:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ch1pa6$nmi$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <2vg7j0dshk49ab5ogk43v9b6mlpr7r9o0m@4ax.com> <ch0nc0$rum$1@panix5.panix.com> <a4p8j05uss5o7a48du20c1l8jefds2fupm@4ax.com>`

```
In article <a4p8j05uss5o7a48du20c1l8jefds2fupm@4ax.com>,
Robert Wagner  <robert@wagner.net.yourmammaharvests> wrote:
>On 30 Aug 2004 22:21:52 -0400, docdwarf@panix.com wrote:
>
…[20 more quoted lines elided]…
>it painted imagery with words. Wish we had more of that here.

There are places where one might find equal quality, Mr Wagner, which does 
not express the desire to mutilate a fellow human being whose primary 
ire-arousing quality appears to be a following of a different creed.

But hey... there's a full moon out, that might have something to do with 
your motives, as well.

DD
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-08-31T00:06:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0408302306.1eab0815@posting.google.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <217e491a.0408292314.43d72c73@posting.google.com> <2vg7j0dshk49ab5ogk43v9b6mlpr7r9o0m@4ax.com>`

```
Robert Wagner <robert@wagner.net.yourmammaharvests> wrote

> Executives and stockholders don't even know, much less care, about
> obsolete programming style. If you're talking about their agent, the
> white-haired guy in the corner office, he's about to retire. His
> replacement grew up on C and has no investment in UPPER-CASE
> PROGRAMMING.

You should be pleased, he may even add pointers to the 'best practice'
list and drag the site into the 70s.
 
> >Throwing insults at them does not make them your friends who want to
> >support your aims.
> 
> I don't want to count dumb-asses and sell-outs among my 'friends'.
> They'd sell me out just as readily.

Some may see this as revealing your real intent:  You don't want have
the support of the mainframe programmers to support 'modernising
Cobol', you only want them there to throw insults at and feel superior
to.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 11)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-31T17:50:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63e9j01v8qmkd7s5l6e0mbg1ga7chfcdho@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <217e491a.0408292314.43d72c73@posting.google.com> <2vg7j0dshk49ab5ogk43v9b6mlpr7r9o0m@4ax.com> <217e491a.0408302306.1eab0815@posting.google.com>`

```
On 31 Aug 2004 00:06:59 -0700, riplin@Azonic.co.nz (Richard) wrote:

>Robert Wagner <robert@wagner.net.yourmammaharvests> wrote
>
…[7 more quoted lines elided]…
>list and drag the site into the 70s.

It's more likely he'd add OO. If he had the budget, he'd rewrite in
Java.
 
>> I don't want to count dumb-asses and sell-outs among my 'friends'.
>> They'd sell me out just as readily.
…[4 more quoted lines elided]…
>to.

Only the ones rooted in the '70s. There are some bright lights in
mainframe Cobol.
```

###### ↳ ↳ ↳ When have companies supported employees?

_(reply depth: 8)_

- **From:** Paul Robinson <postmaster@paul.washington.dc.us>
- **Date:** 2005-01-25T14:30:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cKsJd.508$2i4.368@trnddc01>`
- **In-Reply-To:** `<vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com>`

```
Robert Wagner wrote:

> Simply put, they stopped learning new skills in the '70s out of
> personal laziness.  Why should companies support their personal sloth?

Maybe this is slightly off topic, but given the practices of downsizing, 
layoffs, management incompetence in designing systems that cannot be 
implemented without massive unpaid overtime, (or sometimes plain can't 
be implemented) and lots of other bonehead stunts can we even argue that 
companies in general support their employees at all?

Are the companies willing to pay for the training for their employees to 
keep up on important skills, or do they presume that if they do so, the 
employee will move someplace else for more money?

Are they willing to pay people on the basis of performance?  Are they 
going to pay more as people learn more about their profession and become 
more productive?

Want to bet that if a competitor raised the rates they pay Cobol 
programmers in order to get better people, they would be screaming in 
outrage about how it is drying up the supply (but they won't train new 
people)?  Yet if that same company's competitor raised CEO or Board of 
Directors pay, yoc can bet that there wouldn't be one note of protest as 
the very same company that would otherwise be complaining about the 
raising of pay of Cobol programmers then matched or exceeded the pay 
scale of their competitor for executives.
```

###### ↳ ↳ ↳ Re: When have companies supported employees?

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2005-01-25T10:21:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ct5o5q$5ep$1@panix5.panix.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <cKsJd.508$2i4.368@trnddc01>`

```
In article <cKsJd.508$2i4.368@trnddc01>,
Paul Robinson  <postmaster@paul.washington.dc.us> wrote:
>Robert Wagner wrote:
>
…[7 more quoted lines elided]…
>companies in general support their employees at all?

If 'a company in general' exists in order to maximise shareholder value 
then any 'support of their employees' must be weighed against this end.  
As for training... somebody posted this here back in 1997 and to the best 
of my knowledge not much has changed since then:

<http://groups-beta.google.com/group/comp.lang.cobol/msg/6c29c3f3dc17173c?hl=en&lr=&ie=UTF-8>

--begin quoted text:

It is a Well-Known Fact that if you give someone training they will 
immediately jump ship to a higher-paying company because said company is 
foolish enough to think that a person, trained, is more valuable than a 
person, untrained... don't they know that Gratitude Is Enough?

[snip]

Let's look at it another way... assume that an organisation has invested a 
great deal of money in the upgrading of the physical plant. If sufficient 
investment has been made then it is likely that serious consideration will 
be given to upgrading the security system (new locks, etc.) to prevent 
these improvement from 'walking off'. Also consider the common term of 
'golden handcuffs', a recognised metaphor for increasing salary/benefits 
to prevent human capital from *physically* walking away. Now, consider the 
investment of money in humans to upgrade skills in order to make them more 
valuable to the company. Consider how many times you have seen a corporate 
policy stating that an increase in salary/benefits accompanies the 
successful completion of such an upgrade (courses).

Years ago the Wall Street Journal did a story on one of the major NY 
houses... I think it was Morgan Stanley or Morgan Guaranty or the like. 
They hired *only* the 'unhireable'... kids with BAs in Library Science, 
Art History, etc... they put these kids through two years of hell, 60 - 70 
hr weeks, and turned them into *crackerjack* programmers... and then saw 
said kids being hired away by the competition at double or triple the 
salary. When asked why a raise did not accompany the completion of the 
course the HR representative replied 'Oh, we cannot do that... all the 
money has been taken up by training.' (compare this with 'Oh, we cannot 
upgrade the door-locks... all the money went into oil-paintings to hang on 
the walls.')

After a few years of seeing themselves serve as Wall Street's unofficial 
programming school the company finally 'wised up'... and cancelled the 
program entirely.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: When have companies supported employees?

_(reply depth: 9)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2005-01-25T16:34:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85scv05ohrh6ieolcn0skr22k43jo23ih6@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <vgr4j0lkigj6e46l93t35vppgat6gvdlhn@4ax.com> <cKsJd.508$2i4.368@trnddc01>`

```
On Tue, 25 Jan 2005 14:30:32 GMT, Paul Robinson
<postmaster@paul.washington.dc.us> wrote:

>Robert Wagner wrote:
>
…[11 more quoted lines elided]…
>employee will move someplace else for more money?

It depends on whether the employee is viewed as an asset or expense.
If he or she is in a support or admin role, expense. If working in a
money-losing segment of the business, expense. But if working AS A
DEVELOPER on a  'mission critical' system in the company's profitable
core, he or she is a valuable asset worthy of training and high
salary. 

For example, in the oil and gas business, programmers working on the
refinery system are overhead but those on the exploration side of the
house are lavished with money. In the pharmaceutical industry,
manufacturing is an expense that reluctantly gets 10% of sales while
research is seen as the source of profit, thus gets 25% of sales
without complaint. 

If you want to make big bucks, understand the industry and position
yourself where they're being spent. Rule of thumb: ask whether the
company would ever outsource this job to India.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-08-29T20:48:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SHvYc.34772$5s3.6746@fe40.usenetserver.com>`
- **In-Reply-To:** `<joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com>`

```
Joe Zitzelberger wrote:

> (The original head of the standards committee just took an early 
> retirement.  In the intervening months the perform/thru standard has 
> been made optional and the numbers are coming into question next week. 
> ;-)

Yeah!  :)  Fight the good fight!

(I'd hate to think of what I'd have to do to someone who said that 
Evaluate was a bad idea...)
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 8)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-08-30T08:42:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-051BFA.08424130082004@knology.usenetserver.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <cgr8td$oij$1@panix5.panix.com> <joe_zitzelberger-171846.09432329082004@knology.usenetserver.com> <SHvYc.34772$5s3.6746@fe40.usenetserver.com>`

```
In article <SHvYc.34772$5s3.6746@fe40.usenetserver.com>,
 LX-i <lxi0007@netscape.net> wrote:

> Joe Zitzelberger wrote:
> 
…[8 more quoted lines elided]…
> Evaluate was a bad idea...)

Bad idea?  Hell, imagine what you would say to someone who said:

"Evaluate? What does that do?"

...pause to hear evaluate explained...

"Oh, well, that IS nifty.  What will they think of next."
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-08-29T04:38:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s5dYc.1454$8d1.1113@newsread2.news.pas.earthlink.net>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com>`

```
"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message 
news:s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com...
> On Sat, 28 Aug 2004 05:55:19 GMT, "James J. Gavan" <jjgavan@shaw.ca>
> wrote:
<snip>
>
> You'd be forced to make the same regression if you worked for some
…[3 more quoted lines elided]…
>

Robert,
  I won't ask you for any current "real world" examples of this type of "<IBM> 
mainframe shop" - because from all your other posts, I suppose that would be 
just the type of shop that would actually hire you.

In my experiences with current IBM mainframe shops, they DO have "shop 
standards" - but not for "70s style programing" (except possibly for avoiding 
END-IF's if they use a preprocessor as has been reported in this group that 
creates invalid code for such source.
```

###### ↳ ↳ ↳ Re: z/OS and OS/VS Cobol

_(reply depth: 6)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-30T18:44:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ck6j0d511288tb5qhhlnvmmclqc1v6ulb@4ax.com>`
- **References:** `<dr_te_z.1bn35m@mail.codecomments.com> <3ALXc.222055$M95.47262@pd7tw1no> <oi2vi05c3qd89kbktig0lr2j0pu0o4e326@4ax.com> <b7VXc.228871$M95.152820@pd7tw1no> <s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com> <s5dYc.1454$8d1.1113@newsread2.news.pas.earthlink.net>`

```
On Sun, 29 Aug 2004 04:38:48 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>"Robert Wagner" <robert@wagner.net.yourmammaharvests> wrote in message 
>news:s4n1j05qvid3g7kvl6tkaae7cji4fhkkiv@4ax.com...
…[13 more quoted lines elided]…
>just the type of shop that would actually hire you.

Shops that don't use contractors are just as bad.

>In my experiences with current IBM mainframe shops, they DO have "shop 
>standards" - but not for "70s style programing" (except possibly for avoiding 
>END-IF's if they use a preprocessor as has been reported in this group that 
>creates invalid code for such source.

Their '70s style appears in code samples posted here -- perform thru,
numbered paragraphs, monolithic programs, periods.

I haven't encountered the END-IF preprocessor problem.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
