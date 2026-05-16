[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do you count?

_73 messages · 20 participants · 2001-10 → 2001-11_

---

### How do you count?

- **From:** "Gary Crowley" <gc817@hotmail.com>
- **Date:** 2001-10-26T03:06:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com>`

```
I'm writing a program that reads a record (80 char long) and counts the
number of lines in the data file. The data file consist of 2 poems. I must
count the blank ones also.
Any idea what I need to do to read all the lines to create a summary of the
number of lines in the data file?

NorthenHeights (gc817@hotmail.com)
```

#### ↳ Re: How do you count?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-10-26T08:28:21+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com>`

```


How do you count?  Let's see:

one

two

three

four

five


HTH
                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      A likely impossibility is always preferable to an unconvincing possibility.
      
        (Another Wisdom from my fortune cookie jar)         
______________________________________________________________________________
Posted Via Binaries.net = SPEED+RETENTION+COMPLETION = http://www.binaries.net
```

##### ↳ ↳ Re: How do you count?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-26T10:10:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QEaC7.10217$ym4.448729@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com>`

```
In article <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com>,
Volker Bandke  <vbandke@bsp-gmbh.com> wrote:
>
>
…[13 more quoted lines elided]…
>HTH

What's all this fancy stuff?  Mr Bandke, with all due respect... need it
be pointed out to you that All Good Programmers start counting at 0?

Then there's this... strangeness you have.  'Two'?  What's that?  It might
be suggested that sticking with What's Best is... best, and counting:

   0
   1
  10
  11
 110
 111
1110
1111

... et and cetera.

DD
```

###### ↳ ↳ ↳ Re: How do you count?

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-10-26T12:57:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net>`

```
Sorry Doc to rattle your cage,

but I thought that this was a COBOL group, and of course COBOL starts
counting at on (The first subscript for a table is 1, not zero)

Of course, if this were a C of Java group, you would have been 100%
correct.  Are you doing some retraining right now <evil grin>


And of course I always count in binary, I only pronounce it in decimal
(that's why I used text, not numerals

</evil grin> ...Cheshire Cat act.....

                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      Good-bye. I am leaving because I am bored. -- George Saunders' dying words
      
        (Another Wisdom from my fortune cookie jar)         
______________________________________________________________________________
Posted Via Binaries.net = SPEED+RETENTION+COMPLETION = http://www.binaries.net
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 4)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-26T12:58:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<56dC7.10232$ym4.448959@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com>`

```
In article <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com>,
Volker Bandke  <vbandke@bsp-gmbh.com> wrote:
>Sorry Doc to rattle your cage,

If simple errors did that, Mr Bandke, then I would spend my life sounding
like a Yankee peddler.

(explanation: back in the Oldene Dayse, when folks who sold things - and
just about everyone else, for that matter - travelled by horse-and-wagon
things in transit tended to make more noise... whether the Yankees were
more prone towards audible expressions than anyone else has never been
documented)

>
>but I thought that this was a COBOL group, and of course COBOL starts
>counting at on (The first subscript for a table is 1, not zero)

Table displacements are one thing, Mr Bandke, but a Good Programmer needed
- again, in the Oldene Dayse - the ability to 'shoot a dump' to determine
errors.  Displacements in the dump (a snapshot of the core, or 'The Temple
of Truth') begin at zero.

>
>Of course, if this were a C of Java group, you would have been 100%
>correct.  Are you doing some retraining right now <evil grin>

In fact I am... but not in either of those.

>
>
>And of course I always count in binary, I only pronounce it in decimal
>(that's why I used text, not numerals

You use text to count in binary?  That can make for problems;
zeroonezeroonezeroone onezeroonezeroonezero does not maintain half-word
alignment, aber auf Deutsch nulleinsnulleinsnulleins
einsnulleinsnulleinsnull ganz gut ist.

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 5)_

- **From:** "James" <mangogrower@telocity.com>
- **Date:** 2001-10-26T12:14:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sYfC7.67$VF.215295@newsrump.sjc.telocity.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net>`

```
Actually counting starts at 1.  If you have ZERO items, you can't start
counting!
OFFSETS are not counting but rather adding a displacement to something.
That's what in 'C' et al, my_array[0] actually does just like in assembler.
Its says, get address of start of my_array, add 0, use this address.
In COBOL, we're saying   access the element at displacement position n.

" NA" <docdwarf@clark.net> wrote in message
news:56dC7.10232$ym4.448959@iad-read.news.verio.net...
> In article <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com>,
> Volker Bandke  <vbandke@bsp-gmbh.com> wrote:
…[37 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 6)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-26T16:41:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FmgC7.10250$ym4.449477@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net>`

```
In article <sYfC7.67$VF.215295@newsrump.sjc.telocity.net>,
James <mangogrower@telocity.com> wrote:
>Actually counting starts at 1.  If you have ZERO items, you can't start
>counting!

Of course you can start counting at zero... and if you have zero items you
stop there, as well.

>OFFSETS are not counting but rather adding a displacement to something.

... and this 'something' is where Good Programmers begin counting... at
zero.

>That's what in 'C' et al, my_array[0] actually does just like in assembler.
>Its says, get address of start of my_array, add 0, use this address.
>In COBOL, we're saying   access the element at displacement position n.

Displacement being calculated from The Beginning... or someplace else?

DD

>
>" NA" <docdwarf@clark.net> wrote in message
…[42 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Subscript wish

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-29T15:38:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rjt19$2vm$1@peabody.colorado.edu>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net>`

```
I really wish CoBOL would allow us to define a table range.

For instance

01  ACCOUNT-TABLE   OCCURS 1000 TIMES FROM 5000 TO 5999  VALUE ALL 'N'.
     05  ACCOUNT-TABLE-SWITCH   PIC X.
     88  ACCOUNT-FOUND                          VALUE 'Y'.


or even

01  ACCOUNT-TABLE   OCCURS 1000 TIMES FROM 0000 TO 0999  VALUE ALL 'N'.
     05  ACCOUNT-TABLE-SWITCH   PIC X.
     88  ACCOUNT-FOUND                          VALUE 'Y'.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-29T10:10:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rjv1r$ngj$1@nntp9.atl.mindspring.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu>`

```
This is the type of "enhancement request" that you can submit to J4 for
consideration as a "candidate for a future revision".  To do so, you should
send a not (like this one) to

   doncobol <at> mediaone.net
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-30T06:34:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdd943c_8@news.newsgroups.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu>`

```
Howard,

You have lost me here.

Please explain what you mean by the bit after the "FROM"...

I don't see how the range of 1000 values (whether it is 5000 to 5999 or 000
to 999) can be tied to a table which is defined with single byte entries...

Do you mean that the value of the subscript should be reflected in the
table, or "implicit" ... like entry 450 means Account number 450? How could
a compiler know what you intend to imply?

If you have a range of accounts from 5000 to 5999 and you have a table with
1000 entries, you would do some simple arithmetic on the subscript or index
to derive the Account number (like...compute account-number = subscript +
3999)  Are you saying you want the compiler to do this? If so, how would you
spell out what is necessary?

I am baffled by your post...please enlighten me. <G>

Some examples might help...

Pete.




"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:9rjt19$2vm$1@peabody.colorado.edu...
> I really wish CoBOL would allow us to define a table range.
>
…[11 more quoted lines elided]…
>      88  ACCOUNT-FOUND                          VALUE 'Y'.



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-29T19:11:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MRhD7.13$U7.7029@bin1.nnrp.aus1.giganews.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3bdd943c_8@news.newsgroups.com>`

```
I have ACCOUNT-CODE  PIC 9(5).

I read in a user supplied table of accounts and then walk through a database
looking for matching accounts.  An efficient way of doing this is to have a
hash table that contains "Y" for accounts I want to use and "N" for accounts
I don't want to use.

I say IF VALID-ACCOUNT(account-number) THEN PERFORM FOUND-ONE.

But valid accounts are from 00000 thru 99999, so I have to either check for
00000 and treat it as 10000 or I have to add one to each account.  Either
way, I am playing a trick rather than straightforward CoBOL type clarity.

Or maybe I have a bigger table with ACCOUNT-NUMBER, ACCOUNT-NAME, &
ACCOUNT-VALUE and the only accounts I am concerned with are 60000-69999.  
Then I either have to do arithmetic to translate the account number or have
a table much larger than what I use.

The former is anti-CoBOL - I don't like pretending that 60000 is 00001.

Of course, if my compiler standards allow for subscript overflow then I have
to do extra checking anyway for this second example.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-29T13:54:10-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rkc5h$iuj$1@slb1.atl.mindspring.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu>`

```
Not exactly what you are asking for - BUT at least a "current work-around"
to what you are doing.

Define your table as:

 01  ACCOUNT-TABLE   OCCURS 1000 VALUE ALL 'N'.
      05  ACCOUNT-TABLE-SWITCH   PIC X.
      88  ACCOUNT-FOUND                          VALUE 'Y'.

In your procedure division code *all* references to table elements with
"relative subscripting/indexing" - using a constant entry, i.e.

Move Account-Table-Switch (sub - const) to Some-other-field

You can then EITHER define your "const" value in one place (as 4999 - if you
want a range for "sub" of 5000 to 5999, OR even define it as "coming from a
compile-time variable" - so you could code the program to work on
"5000-5999" one time and then to "auto-magically" recompile working for
0-9999.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-29T20:19:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rkdgj$f1q$1@peabody.colorado.edu>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net>`

```

On 29-Oct-2001, "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

> Not exactly what you are asking for - BUT at least a "current work-around"
> to what you are doing.
…[18 more quoted lines elided]…
> 0-9999.

Could you explain this again - I'm not sure I'm understanding what you're
saying.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-29T15:32:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rkht2$bq$1@slb6.atl.mindspring.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu>`

```
Ok, lets try (using ONLY what is in the current Standard - '85)

As I understand the "business" objective, you want to have a table of ONLY
1000 entries, but you want them to be "indexed" by the values 5000 to 5999
(rather than 1 to 1000).  If this isn't what you are looking for, please
help me understand your desire better (and ignore my suggestion).

Today, you can define the following in WS.

01  MyOffset  Pic 9999  Value 4999.
01 Sub   Pic 9999  Binary Value Zero.
01  ACCOUNT-TABLE   OCCURS 1000 VALUE ALL 'N'.
       05  ACCOUNT-TABLE-SWITCH   PIC X.
       88  ACCOUNT-FOUND                          VALUE 'Y'.

Then in procedure division, wherever you might "normally" use Sub as the
subscript/index - instead you use
   (Sub - MyOffset)

The "valid values" for SUB would be 5000 thru 5999.  Therefore, to test if
an account exists you could code:
  Move test-account-number to Sub
  If Account-Found (sub - MyOffset)
    Display "This account exists"

or more directly (if you are "reading in" the test-account-number, you could
code
   If Account-Found (Test-account-number - MyOffset)
    Display "This account exists"

The only "major" difference in the draft of the next Standard is that you
don't have to "define" your MyOffset field as a "data-item".  Instead in can
be a "CONSTANT" (defined in your program - or "obtained" at compile-time
from a compilation variable).  If what confused you about my earlier post
was how to define and/or get CONSTANTs - I can explain that further.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 11)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-10-29T13:50:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rkiuh$2aus$1@si05.rsvl.unisys.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu> <9rkht2$bq$1@slb6.atl.mindspring.net>`

```
Can be done this way, I agree.   But I think, given the presence of
nondefault subscript ranges in languages like ALGOL for several decades, and
Pascal for only a few less, there's some justification for letting the
compiler do the work of adjusting the subscripts rather than requiring the
user to do so!   I think that's precisely the point.

        -Chuck Stevens

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9rkht2$bq$1@slb6.atl.mindspring.net...
> Ok, lets try (using ONLY what is in the current Standard - '85)
>
…[23 more quoted lines elided]…
> or more directly (if you are "reading in" the test-account-number, you
could
> code
>    If Account-Found (Test-account-number - MyOffset)
…[3 more quoted lines elided]…
> don't have to "define" your MyOffset field as a "data-item".  Instead in
can
> be a "CONSTANT" (defined in your program - or "obtained" at compile-time
> from a compilation variable).  If what confused you about my earlier post
…[21 more quoted lines elided]…
> > > In your procedure division code *all* references to table elements
with
> > > "relative subscripting/indexing" - using a constant entry, i.e.
> > >
> > > Move Account-Table-Switch (sub - const) to Some-other-field
> > >
> > > You can then EITHER define your "const" value in one place (as 4999 -
if
> > > you
> > > want a range for "sub" of 5000 to 5999, OR even define it as "coming
…[3 more quoted lines elided]…
> > > "5000-5999" one time and then to "auto-magically" recompile working
for
> > > 0-9999.
> >
> > Could you explain this again - I'm not sure I'm understanding what
you're
> > saying.
>
>
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-30T14:13:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YzyD7.11178$U7.566797@bin1.nnrp.aus1.giganews.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu> <9rkht2$bq$1@slb6.atl.mindspring.net> <9rkiuh$2aus$1@si05.rsvl.unisys.com>`

```

On 29-Oct-2001, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> Can be done this way, I agree.   But I think, given the presence of
> nondefault subscript ranges in languages like ALGOL for several decades,
…[5 more quoted lines elided]…
>         -Chuck Stevens


Exactly.  CoBOL should be about the data and business rules.  Converting
offsets and such shouldn't be part of the code.  Sure we do it, (and have to
remember whether the external sort uses offset or position) - but wherever
possible the code should look like the business environment.  If the
warehouse has bins labeled 5000-5999, our code should match.   (In my case
it is the account book, but you know what I mean)

CoBOL's strength is how well it matches up with the business world.

The compiler then translates the code to whatever the computer should see.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 13)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-11-01T20:31:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BE1B106.C037F643@Azonic.co.nz>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu> <9rkht2$bq$1@slb6.atl.mindspring.net> <9rkiuh$2aus$1@si05.rsvl.unisys.com> <YzyD7.11178$U7.566797@bin1.nnrp.aus1.giganews.com>`

```
Howard Brazee wrote:
> 
> If the
> warehouse has bins labeled 5000-5999, our code should match.   (In my case
> it is the account book, but you know what I mean)

I am in complete _dis_agreement with you.  If one particular warehouse
has bins number 5000-5999 (or accounts) then the _DATA_FILE_ should
match this and the code should process the data accordingly regardless
of what the _actual_ codes are.

What are you suggesting - a unique version of the program for each
warehouse (or department, company, division) and a rewrite of the system
if a new row of racking is added ?  If they move to a new warehouse will
you throw out all the programs and start again ?

In the Accounts file have a flag that indicates 'special processing'. 
Read the accounts file and pick up all those so marked.  These _may_
co-incidentally be all in the range 5000-5999 at one point in time.

> but wherever possible the code should look like the business environment. 

But building codes into the program is only following the _current_
business environment, it is then becoming a _constraint_ on it.

While originally those special codes were set to 5000-5999 in some
arbitrary way, they now _must_ be in that range because of the program. 
It is no longer the program looking like the business, the business must
look like the program.

If an account is needed to be changed from being special to not or vice
versa, the original must have all its transactions reversed then be
deleted and a new code set up with all the transactions added back just
to put it in range or out of it.

With a _properly_designed_ system the account (or bin) should be able to
be added or removed from the special range with a flag or other
indication.

For example if these were Customer accounts and the program treated
customers in the range 5000-5999 as being on 'stop supply' because they
hadn't paid for 3 months or were over their credit limit, then they
would have to be deleted and recreated to put them in this range or out
of it as appropriate, and all their transactions and history would also
be deleted and recreated.

If this mechanism actually was implemented then the programmer may well
claim that the program followed the business practice.  No - it enforced
the business practice.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-01T15:21:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rrp69$55f$1@peabody.colorado.edu>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu> <9rkht2$bq$1@slb6.atl.mindspring.net> <9rkiuh$2aus$1@si05.rsvl.unisys.com> <YzyD7.11178$U7.566797@bin1.nnrp.aus1.giganews.com> <3BE1B106.C037F643@Azonic.co.nz>`

```

On  1-Nov-2001, Richard Plinston <riplin@Azonic.co.nz> wrote:

> If this mechanism actually was implemented then the programmer may well
> claim that the program followed the business practice.  No - it enforced
> the business practice.

You can say that about virtually any business rule codified in a program.

Leave the business rules out, take out the input and output, and you will
never need to do maintenance!
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 15)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-11-02T07:04:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BE24585.32AAFC97@Azonic.co.nz>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu> <9rkht2$bq$1@slb6.atl.mindspring.net> <9rkiuh$2aus$1@si05.rsvl.unisys.com> <YzyD7.11178$U7.566797@bin1.nnrp.aus1.giganews.com> <3BE1B106.C037F643@Azonic.co.nz> <9rrp69$55f$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
> On  1-Nov-2001, Richard Plinston <riplin@Azonic.co.nz> wrote:
…[5 more quoted lines elided]…
> You can say that about virtually any business rule codified in a program.

The issue is the extent to which the program constrains the business.  

There was an example a couple of months ago where the program
implemented special processing of customer and product combinations with
a huge nested IF .. ELSE with the actual customer and sales codes buried
in the same code repeated in several programs.  Obviously a 'quick fix'
that had grown out of hand.  There is now no possible way of testing
whether those codes are correct and that the program works as required
without an enormous and exhaustive amount of test data.

If the accounts and sales codes had been flagged to indicate their
status, or a file of combinations had been built to indicate which were
appropriate then:

  a) the actual business rules could be proven with subset test data.
  b) the actual data combinations could be inspected and changed by
those responsible.
  c) 'maintenance' would involve changing the data, not rewriting the
programs.

In your case you are not only implementing the business rules into the
program, you are also implementing the data items to which these rules
apply.  Your bin number example is more clear, but is just the same as
the accounts.  Why would you write a program that specifies exactly what
the bin numbers in a warehouse should be ?

I probably go too far the other way and have a data file of 'decodes',
lots of very simple data items that the user can maintain that also
includes optional flags.  The program implements different sets of
business rules the data files (maintained by the user) specifies where
these rules apply.  This reduces the program maintenance for trivial
changes and allows the user (rather than the programmer) to control how
the system works.  It also means that the user must understand how the
_business_ operates rather than just accepting what the programmer
coded.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 16)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-11-01T18:49:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BE19920.D68AF7E6@home.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu> <9rkht2$bq$1@slb6.atl.mindspring.net> <9rkiuh$2aus$1@si05.rsvl.unisys.com> <YzyD7.11178$U7.566797@bin1.nnrp.aus1.giganews.com> <3BE1B106.C037F643@Azonic.co.nz> <9rrp69$55f$1@peabody.colorado.edu> <3BE24585.32AAFC97@Azonic.co.nz>`

```


Richard Plinston wrote:

> Howard Brazee wrote:
> >
…[42 more quoted lines elided]…
> coded.

Perhaps the best one I can think of to support what Richard is stressing - 30
years ago at Debenhams department store group. The former accountant of Harvey
Nichols, (the other 'snotty' store just down the road from Harrods of
Knightsbridge),  as a result of centralization, was based in West country with
us computer geeks. We were coming up to VAT and it seemed logical to re-design
the Chart-of-Accounts. He's a bean counter, so he knows all about account coding
systems - Right ?

So he pored through the coding systems being used by some 60 stores to come up
with a generic list. In the case of Payroll we produced pre-printed Journal
sheets to make it easier for the store accountants.

Having been 'caught' before, I designed the computer system, (Chart of
Accounts), to have 'flags' indicating which group each account belonged to, i.e.
Flag 1 = Current Assets, Flag-2 = Fixed Assets, etc. (Plus there were 'fillers'
so the flag system was expandable). I kept telling the 'committee' I was doing
this but it went over the heads of the bean counters as computerese.

There we are about a month away from VAT and he issues his list of account
codes  - all hell broke loose. Back came the store accountants, 'this' was
missing, and 'that' was missing. The committee looked on glumly when he admitted
to the shortcomings and said some of the additions required would break his
numeric groupings !

Then the bean counters got the message. I reiterated "I don't give a damn about
his groupings. I have made the computer system use flags, regardless of his
coding system". Phew ! Sighs of relief all around - but he 'hated' me for having
provided the solution.

AND - back 40 years ago when we were first cutting our teeth - the Marketing
Manager *insisted* our Customer Account numbers MUST include the salesman's
number, (to find out who is selling what).. We insisted, just as strongly, that
they wouldn't be included - we keypunched the individual Salesmen's numbers from
Order forms.. Six months later he revamped his sales territories !

Jimmy
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 17)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-11-01T20:00:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MRhE7.10747$ym4.469588@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3BE1B106.C037F643@Azonic.co.nz> <3BE19920.D68AF7E6@home.com>`

```
In article <3BE19920.D68AF7E6@home.com>,
James J. Gavan <jjgavan@home.com> wrote:

[snippimentico]

>Then the bean counters got the message. I reiterated "I don't give a damn about
>his groupings. I have made the computer system use flags, regardless of his
>coding system". Phew ! Sighs of relief all around - but he 'hated' me for having
>provided the solution.

As my Sainted Mother, may she sleep with the angels, told me when, as a
lad of 16, I got my first Real Job: 'When it comes to work you should
remember two things: you can be wrong about something... and be fired for
it... and you can be right about something... and be fired for it.'

DD
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 16)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-11-02T12:20:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QbwE7.496$Vf1.44702@paloalto-snr1.gtei.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu> <9rkht2$bq$1@slb6.atl.mindspring.net> <9rkiuh$2aus$1@si05.rsvl.unisys.com> <YzyD7.11178$U7.566797@bin1.nnrp.aus1.giganews.com> <3BE1B106.C037F643@Azonic.co.nz> <9rrp69$55f$1@peabody.colorado.edu> <3BE24585.32AAFC97@Azonic.co.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:3BE24585.32AAFC97@Azonic.co.nz...
>
> The issue is the extent to which the program constrains the business.


To which the correct answer is, "Software never constrains a business:
software exists to SUPPORT a business."

Sheesh, if I had a nickel for everyone I've met who thought software was a
substitute for good business practice, I'd be rich.

MCM
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 17)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-11-03T14:53:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3be34e92$1_5@news.newsgroups.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <9rkc5h$iuj$1@slb1.atl.mindspring.net> <9rkdgj$f1q$1@peabody.colorado.edu> <9rkht2$bq$1@slb6.atl.mindspring.net> <9rkiuh$2aus$1@si05.rsvl.unisys.com> <YzyD7.11178$U7.566797@bin1.nnrp.aus1.giganews.com> <3BE1B106.C037F643@Azonic.co.nz> <9rrp69$55f$1@peabody.colorado.edu> <3BE24585.32AAFC97@Azonic.co.nz> <QbwE7.496$Vf1.44702@paloalto-snr1.gtei.net>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:QbwE7.496$Vf1.44702@paloalto-snr1.gtei.net...
> Richard Plinston <riplin@Azonic.co.nz> wrote in message
> news:3BE24585.32AAFC97@Azonic.co.nz...
…[4 more quoted lines elided]…
>

Ah, I have acquired MANY nickels from people who believed exactly that...<G>

Pete.




-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 8)_

- **From:** ctimmerman@acsalaska.com (Curt Timmerman)
- **Date:** 2001-10-29T20:07:08
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns9149712AB3D94ctimmermanacsalaskac@10.136.100.32>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in 
<9rjt19$2vm$1@peabody.colorado.edu>:
This behaviour could be simulated with a table "object" in OO COBOL.

>I really wish CoBOL would allow us to define a table range.
>
…[11 more quoted lines elided]…
>     88  ACCOUNT-FOUND                          VALUE 'Y'.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-29T20:10:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDDB79E.62C74700@home.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu>`

```


Howard Brazee wrote:

> I really wish CoBOL would allow us to define a table range.
>
…[10 more quoted lines elided]…
>      88  ACCOUNT-FOUND                          VALUE 'Y'.

Three points Howard,

1) As Bill says "wishing" isn't going to make it happen - a submission to
J4 would be the way to go.

2) Pete's comment - no big deal currently to specify the table and add a
number so you get the "5000" A/c #'s you want.

3) Raises an interesting issue. How long do J4 have to play brass monkies
and produce standards for non-OO COBOL and OO-COBOL as though they were two
separatre animals, when in fact the latter is 90% coding in the former ?
You could make a case for your change but it necessitates a revision to the
compiler when in fact the feature you want is already available. Perhaps J4
should be *encouraging* users to consider OO COBOL as an *extra* when they
get their TR out on Collections/Dictionaries - further, maybe you mainframe
guys should be plugging with your mainframe vendors to provide these
utilities toute suite !

The followng is contrived, and I haven't compiled it, but it does
illustrate the flexibility of OO that you could include in a non-OO suite
of progrms :-

*>-------------
Class-id.            Check5000Accounts  inherits from Base.

Class-Control        Check5000Accounts    is class "fivethou"

                             OrdereredCollection     is class "ordclln"
                             Callback                       is class
"callback"
etc...

File definitions, working storage etc......
*>--------------------
Method-id. "do5000s".
*>-------------------
Local-storage seciton.
copy "mycopfile.cpy" replacing ==(tag)== by ==ls==.
*>-----------------------
01 tag-record.
 05 tag-key                        pic x(05).
 05 tag-type                        pic x.
      88 Wholesaler              value "W", "w".
      88 Retailer                   value "R", "r".
 05 tag-purchases               pic s(06)v9(02).
 05 tag-discount                 pic s9(04)v9(02).
*>-----------------------------------------
01 ls-CallbackMethod                    object reference.
01 MyCollection                            object reference.

Procedure Division.
  compute ls-length = function lenth (ls-record)
   invoke OrderedCollection "ofReferences"
          using ls-length returning MyCollection

 set FileNotFinis to true
 move "5000" to PrimeKey
 start MyFile key >=  Primekey
   invalid key set FileFinis to true
end-start

perform until FileFinis
 read MyFile
    at end
        SetFileFinis to true
    not at end
        if    PrimeKey > 5999
              EXIT PERFORM
        else  move PrimeKey to ls-key
                move Type to ls-type
                move Purhcases to ls-purchases
                move Discount to ls-discount
                invoke MyCollection "add" using ls-record
        End-if
End-perform

invoke MyCollection ":size" returning ls-size

if ls-size <> zeroes
  invoke Callback "new" using self "calcDiscount "
        returning ls-CallbackMethod
   invoke ls-CallbackMethod "do" using MyCollection
End-if

End-method "do5000s".
*>---------
Method-id. "calcDiscount".
*>------------------------
Linkage section.
copy "mycopfile.cpy" replacing ==(tag)== by ==lnk==.
Procedure Divison using lnk-record.

 *> I don't have to specify the collection size - it *knows* and will
iterate on all the records you want to action, subject to your selection
criteria  :-

Evaluate true
    when Retailer
         compute lnk-Discount = lnk-Discount + ( lnk-purchases * 0.5)
    when Wholesaler
         compute lnk-Discount = lnk-Discount + ( lnk-purchases * 0.7)
    when other
        etc.....
End-evaluate

End Method  "calcDiscount".
*>-----------------------------

'Standard' COBOL coupled with OO offers you so much flexibility !

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-29T20:23:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FUiD7.619382$Lw3.38877926@news2.aus1.giganews.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDDB79E.62C74700@home.com>`

```

On 29-Oct-2001, "James J. Gavan" <jjgavan@home.com> wrote:

> 'Standard' COBOL coupled with OO offers you so much flexibility !

If we ever see OO CoBOL in mainframes, it will be with this type of
couplings.   Parm file edits will be first, as these are easily perceived as
components, they tend to be somewhat unnecessary (the parms should be
correct anyway!), and nobody is worried about efficiency for them.

Integrated environments cause headaches for MIS shops.  But little tools are
well liked.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 9)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-10-30T02:47:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UwoD7.146579$3d2.5041999@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDDB79E.62C74700@home.com>`

```
To all involved in this chain....

Would you be willing to let someone use portions of this series of messages
to illustrate a public
COBOL USERS Manual?
If so, how would you condense it?

Yes, DD, I'm asking for someone to do some home work for me. <G>

Warren Simmons
James J. Gavan <jjgavan@home.com> wrote in message
news:3BDDB79E.62C74700@home.com...
>
>
…[25 more quoted lines elided]…
> and produce standards for non-OO COBOL and OO-COBOL as though they were
two
> separatre animals, when in fact the latter is 90% coding in the former ?
> You could make a case for your change but it necessitates a revision to
the
> compiler when in fact the feature you want is already available. Perhaps
J4
> should be *encouraging* users to consider OO COBOL as an *extra* when they
> get their TR out on Collections/Dictionaries - further, maybe you
mainframe
> guys should be plugging with your mainframe vendors to provide these
> utilities toute suite !
…[95 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 10)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-30T03:08:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MQoD7.10515$ym4.460128@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <9rjt19$2vm$1@peabody.colorado.edu> <3BDDB79E.62C74700@home.com> <UwoD7.146579$3d2.5041999@bgtnsc06-news.ops.worldnet.att.net>`

```
In article <UwoD7.146579$3d2.5041999@bgtnsc06-news.ops.worldnet.att.net>,
Warren Simmons <warren.simmons@worldnet.att.net> wrote:
>To all involved in this chain....
>
>Would you be willing to let someone use portions of this series of messages
>to illustrate a public
>COBOL USERS Manual?

Perhaps.

>If so, how would you condense it?

Carefully.

>
>Yes, DD, I'm asking for someone to do some home work for me. <G>

Really?

DD

>James J. Gavan <jjgavan@home.com> wrote in message
>news:3BDDB79E.62C74700@home.com...
…[136 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-30T04:15:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDE2948.5A94F091@home.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDDB79E.62C74700@home.com> <UwoD7.146579$3d2.5041999@bgtnsc06-news.ops.worldnet.att.net>`

```


Warren Simmons wrote:

> To all involved in this chain....
>
…[6 more quoted lines elided]…
>

Warren,

Feel free to use anything I post, but I doubt you want OO at this stage.
Condense it ? You'd have to expand it, because obviously I left out things which
would make it meaningless to a newcomer. I did say it wasn't compiled <G> - and
it  does have a boo-boo. I should have written :-

        invoke OrderdedCollection "ofValues" using.....returning.....

which gives you an intrinsic collection (text/numerics).

    invoke Ordered Collection "ofReferences" using.... returning....

is for a collection where the elements are object references - you turn the
intrinsic data into objects - typically something you would want to display
(Windows) as a Listbox or DropDownList.  So - display Listbox, do Mouse
selection, tells you which object (index) in the collection your are pointing
at, then 'unpack' the object back into an intrinsic before you can manipulate
text or numbers.

Obviously the example for Howard was "ofValues" - really just a more flexible
approach to non-OO Table features.

Just to show nothing is Black or White in COBOL. Like Richard I abhor 'ranges'
in programs, although in Howard's case A/c's 5000-5999 is pretty hard-set. That
gives him a neat starting point with Key >= 5000. But it does go belly-up when
some clown comes along and asks him to change the program, because the 'select
group', in addition to 5000-5999 now contains 7010 - 7060, but ignore 7035 !

Ideally,  the alternative is to allow for flags which can be used as an
alternate key, at the INITIAL design stage.  (Remember Eileen's horrible list of
Account Numbers ?). As so many people include file definitions in the body of
their programs, as opposed to a separate DBI(DataBase Interface), if, after a
period of 'calm' you suddenly change the meaning of the file layout - you can be
faced with horrendous testing for quite a small change, plus a Read and Rewrite
if you add a brand new alternate key.

Jimmy
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 11)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-10-30T21:50:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jgFD7.148441$3d2.5129403@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDDB79E.62C74700@home.com> <UwoD7.146579$3d2.5041999@bgtnsc06-news.ops.worldnet.att.net> <3BDE2948.5A94F091@home.com>`

```
Mainly to DD and James J.

This is homework for me as I have volunteered to help create a "users
manual" for TC.  Their feature list includes some things from the 200x
proposal, AND some things NOT in any other COBOL (perhaps)
My status on this homework is at the thinking stage of how, what, where,
etc.  I'm hoping some others are going to step in to help, and that the
space made available will allow room for http and pds version.
I will be reachable at warren@tinycobol.org where email will be forwarded to
my address.

Warren
James J. Gavan <jjgavan@home.com> wrote in message
news:3BDE2948.5A94F091@home.com...
>
>
…[4 more quoted lines elided]…
> > Would you be willing to let someone use portions of this series of
messages
> > to illustrate a public
> > COBOL USERS Manual?
…[8 more quoted lines elided]…
> Condense it ? You'd have to expand it, because obviously I left out things
which
> would make it meaningless to a newcomer. I did say it wasn't compiled
<G> - and
> it  does have a boo-boo. I should have written :-
>
…[6 more quoted lines elided]…
> is for a collection where the elements are object references - you turn
the
> intrinsic data into objects - typically something you would want to
display
> (Windows) as a Listbox or DropDownList.  So - display Listbox, do Mouse
> selection, tells you which object (index) in the collection your are
pointing
> at, then 'unpack' the object back into an intrinsic before you can
manipulate
> text or numbers.
>
> Obviously the example for Howard was "ofValues" - really just a more
flexible
> approach to non-OO Table features.
>
> Just to show nothing is Black or White in COBOL. Like Richard I abhor
'ranges'
> in programs, although in Howard's case A/c's 5000-5999 is pretty hard-set.
That
> gives him a neat starting point with Key >= 5000. But it does go belly-up
when
> some clown comes along and asks him to change the program, because the
'select
> group', in addition to 5000-5999 now contains 7010 - 7060, but ignore 7035
!
>
> Ideally,  the alternative is to allow for flags which can be used as an
> alternate key, at the INITIAL design stage.  (Remember Eileen's horrible
list of
> Account Numbers ?). As so many people include file definitions in the body
of
> their programs, as opposed to a separate DBI(DataBase Interface), if,
after a
> period of 'calm' you suddenly change the meaning of the file layout - you
can be
> faced with horrendous testing for quite a small change, plus a Read and
Rewrite
> if you add a brand new alternate key.
>
> Jimmy
>
>
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 12)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-30T23:32:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDF386E.69C01EA2@home.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDDB79E.62C74700@home.com> <UwoD7.146579$3d2.5041999@bgtnsc06-news.ops.worldnet.att.net> <3BDE2948.5A94F091@home.com> <jgFD7.148441$3d2.5129403@bgtnsc06-news.ops.worldnet.att.net>`

```


Warren Simmons wrote:

> Mainly to DD and James J.
>
…[8 more quoted lines elided]…
>

Gotcha. I'll write to you via TinyCOBOL. I hope others here will do so as well.

Jimmy
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-30T07:01:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BDE5032.B686087A@Azonic.co.nz>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
> I really wish CoBOL would allow us to define a table range.
…[6 more quoted lines elided]…
> 

The main reason that I can see for this perceived need is where the
program is dealing with specific codes, such as account codes, in some
particular range.  Building this type of constraint into the program
leads to artificial restrictions in the actual system.  What happens if
the accountants decide that the they have enough 5000s and want to use
some spare 8000s ?  What if this program is to be used for another
company, division or department where they use a different range of
accounts ?

The easiest way to deal with this is to make the table occur 10000 for
accounts 0001 to 9999 or add offset 1 to the account code to get 0000 -
9999.  If it only actually uses the 5000 - 5999 part of the array there
is little loss.

I generally abhor building codes into the program.  I would build the
table with each item having the account-code and switch and start
storing the accounts as found.  In fact it wouldn't even need the switch
as the presence of the code in the table indicates it has been found. 
While this takes quite a bit of searching it doesn't even restrict the
codes to being numeric, let alone a specific range.

Alternately set the 'found' switch on the account record (after clearing
all switches in the file at start of run) and have a permanent record of
which accounts were found.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 9)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-29T13:32:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cghD7.5891$6h5.656373@news20.bellglobal.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDE5032.B686087A@Azonic.co.nz>`

```
While it will not allow variable array sizes at run time, the figurative
constant section will allow variable array sizes at compile time ...

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3BDE5032.B686087A@Azonic.co.nz...
> Howard Brazee wrote:
> >
…[32 more quoted lines elided]…
> which accounts were found.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-29T19:19:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rka0k$ce2$1@peabody.colorado.edu>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDE5032.B686087A@Azonic.co.nz> <cghD7.5891$6h5.656373@news20.bellglobal.com>`

```

On 29-Oct-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:

> While it will not allow variable array sizes at run time, the figurative
> constant section will allow variable array sizes at compile time ...
…[12 more quoted lines elided]…
> > >      88  ACCOUNT-FOUND                          VALUE 'Y'.

How does that help?
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 11)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-29T14:32:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3iD7.19507$az4.987589@news20.bellglobal.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDE5032.B686087A@Azonic.co.nz> <cghD7.5891$6h5.656373@news20.bellglobal.com> <9rka0k$ce2$1@peabody.colorado.edu>`

```
My mistake, Howard ... i thought it was the array size that you wanted to
vary ...

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:9rka0k$ce2$1@peabody.colorado.edu...
>
> On 29-Oct-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:
…[17 more quoted lines elided]…
> How does that help?
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-29T19:18:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rk9un$cac$1@peabody.colorado.edu>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDE5032.B686087A@Azonic.co.nz>`

```

On 30-Oct-2001, Richard Plinston <riplin@Azonic.co.nz> wrote:

> > 01  ACCOUNT-TABLE   OCCURS 1000 TIMES FROM 5000 TO 5999  VALUE ALL 'N'.
> >      05  ACCOUNT-TABLE-SWITCH   PIC X.
…[10 more quoted lines elided]…
> accounts ?

In the case of 00000 thru 99999 that works fine.   But if our code looks for
5000s and the users decide to use 8000s, we have to change our program no
matter how the table is subscripted.

> The easiest way to deal with this is to make the table occur 10000 for
> accounts 0001 to 9999 or add offset 1 to the account code to get 0000 -
> 9999.  If it only actually uses the 5000 - 5999 part of the array there
> is little loss.

Except we are tricking the program to have data which isn't straightforward.
 That should be for C, not CoBOL.

> I generally abhor building codes into the program.  I would build the
> table with each item having the account-code and switch and start
…[3 more quoted lines elided]…
> codes to being numeric, let alone a specific range.

I understand, but hash tables are so much quicker.   Also I can have a wild
card account and move 'Y" to the whole table!  I am not worried about
duplicate account numbers, I don't have to sort it for a faster search - but
you're right - I do have to do a NUMERIC check.

> Alternately set the 'found' switch on the account record (after clearing
> all switches in the file at start of run) and have a permanent record of
> which accounts were found.

Already have that.
```

###### ↳ ↳ ↳ Re: Subscript wish

_(reply depth: 10)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-10-30T02:47:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%woD7.146580$3d2.5041219@bgtnsc06-news.ops.worldnet.att.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <9rjt19$2vm$1@peabody.colorado.edu> <3BDE5032.B686087A@Azonic.co.nz> <9rk9un$cac$1@peabody.colorado.edu>`

```
Perhaps O.T.

In my experience, industrial engineers often are forced to adopt values that
do not fit into ranges of values. As a result, the incentive plan can not be
completely calculated to determine a position in
a sequence, but there are ways, I'm told to over come that.

Warren Simmons

Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:9rk9un$cac$1@peabody.colorado.edu...
>
> On 30-Oct-2001, Richard Plinston <riplin@Azonic.co.nz> wrote:
>
> > > 01  ACCOUNT-TABLE   OCCURS 1000 TIMES FROM 5000 TO 5999  VALUE ALL
'N'.
> > >      05  ACCOUNT-TABLE-SWITCH   PIC X.
> > >      88  ACCOUNT-FOUND                          VALUE 'Y'.
…[11 more quoted lines elided]…
> In the case of 00000 thru 99999 that works fine.   But if our code looks
for
> 5000s and the users decide to use 8000s, we have to change our program no
> matter how the table is subscripted.
…[6 more quoted lines elided]…
> Except we are tricking the program to have data which isn't
straightforward.
>  That should be for C, not CoBOL.
>
…[7 more quoted lines elided]…
> I understand, but hash tables are so much quicker.   Also I can have a
wild
> card account and move 'Y" to the whole table!  I am not worried about
> duplicate account numbers, I don't have to sort it for a faster search -
but
> you're right - I do have to do a NUMERIC check.
>
…[4 more quoted lines elided]…
> Already have that.
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 7)_

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-30T15:47:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PYzD7.5933$xS6.6664@www.newsranger.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net>`

```
On Fri, 26 Oct 2001 16:41:09 GMT, in article
<FmgC7.10250$ym4.449477@iad-read.news.verio.net>,   NA stated 
>
>In article <sYfC7.67$VF.215295@newsrump.sjc.telocity.net>,
…[3 more quoted lines elided]…
>
A good programmer realizes there are different programming 
languages with differrent rules and that is the way it is.
Each programming language works the way it was designed to work.
COBOL has been around for a long time.  Let the neweby programming
languages change their compilers to be in line with COBOL.
A person should not have to start counting at zero, the compiler 
should let you start counting at one and the compiler should have to
subtract one, not the programmer.  It makes no sense to have to 
design a program in C++ or Java where you have to subtract one from
what makes common sense every time you want to use an array.  

This is just lousy compiler implementation.

Why make an object oriented compiler that lets you make up your own 
english names for all of your code and then subtract 1 from what makes
sense to normal people.  I don't want to have to subtract one from 
everything because someone failed to make a good compiler.  It just doesnt
make sense to force people to do something so unnatural.  Programs should 
be made to serve people; People should not have to be slaves to a computer.


Charles
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-11-01T20:06:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BE1AB30.724557E2@Azonic.co.nz>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <PYzD7.5933$xS6.6664@www.newsranger.com>`

```
Charles wrote:
> 
> A person should not have to start counting at zero, the compiler
…[3 more quoted lines elided]…
> what makes common sense every time you want to use an array.

It _isn't_ 'counting', it is numerating, a completely different thing.

Counting is where you determine how many things there are.  In an array
one may count how many of the array items have data in them, if the only
items with data are those numbered 2, 7 and 9 then counting these gives
3.

Numerating is giving numbers to things.  In the case of array items
numerating gives a number to each item by which it may be referenced. 
Usually these are sequential and contiguous, though they need not be,
all that is required is a predictable and repeatable numeration.

'What makes common sense' is entrirely what one is used to.  You can't
cope with numerations other than those used in Cobol.  This doesn't make
Cobol's better or 'common sense', it just makes you less able to cope
with other mechanisms.
 
> This is just lousy compiler implementation.

It has nothing to do with 'compiler implementation', it is a language
design issue.


> Why make an object oriented compiler that lets you make up your own
> english names for all of your code and then subtract 1 from what makes
> sense to normal people.  

So now you assert that Cobol programmers are 'normal' and others are
not.

As Object Orientated _Languages_ allow one to write one's own way of
programming then it is inherent in any OOL that whatever numeration
required can be implemented and used. If you feel that something is
'normal' for you then feel free to do this in the OOL, because it will
allow it.


> I don't want to have to subtract one from
> everything because someone failed to make a good compiler.  

It is nothing to do with the compiler, it is a language design issue.

And given that the OOL will allow you to use it is any way that you care
to implement, then it will only be your failure (and not the language's
or the compiler's) if it doesn't work the way that you require.

> It just doesnt
> make sense to force people to do something so unnatural.  

All numerations are 'unnatural', they are all completely artificial
being the invention of man.

> Programs should
> be made to serve people; People should not have to be slaves to a computer.

Yet you seem to be a slave to a numeration starting at 1 and
incrementing by 1.

I say: let people be free to create whatever numerations they wish. 
There is absolutely no reason why the numerations of an array should be
contiguous, evenly incrementing, or indeed in sequence.

If I want an array with items: 42, 7, 19, 55, 72, -3 - a total of 6
occurances, then why not.

       01  My-Table.
           03  My-Table-Item                OCCURS 6 
                                            INDEXES 42, 7, 19, 55, 72,
-3
                                            INDEXED BY My-Index
            05 My-Table-Flag                PIC X.

          MOVE "Y"             TO My-Table-Flag(55).

          PERFORM
              VARYING My-Index OVER INDEXES
    
              IF ( My-Table-Flag(My-Index) = "Y" )
                  ...
          END-PERFORM
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 9)_

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-11-01T19:11:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G7hE7.8992$xS6.12437@www.newsranger.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <PYzD7.5933$xS6.6664@www.newsranger.com> <3BE1AB30.724557E2@Azonic.co.nz>`

```
On Thu, 01 Nov 2001 20:06:08 +0000, in article <3BE1AB30.724557E2@Azonic.co.nz>,
Richard Plinston stated 
>
>Charles wrote:

Starting to count at Zero and numerating are two different things.

What I was saying is this:  
The COBOL compiler has an index that starts at Zero, but it lets the 
programmer start counting at 1.  Then the compiler subtracts one
to made up the difference.  Using this system when the programmer wants the 
number 3 item in a list of occurs, then he just says move table-item (3) to a
given location or whatever.  This is simpler for a human being to figure out,
and makes perfect sense.  

I say the COBOL compiler's approach to this subject makes more common sense 
than C++ or JAVA.  That is my personal opinion.  I took classes in all three
languages and I know there are plenty of things each language does better than
the other.  Pascal also lets you select the starting and ending number in an
array and do a number of complicated techniques to construct complex data types
on the fly.

COBOL can't really enumerate.  You can build an index inside the table that can
be searched with the search verb, but that isnt exactly the same thing, and
takes up valuabel space.  You could also convert your bin number to the occurs
just like in C++ you would have to subtract 1 to find the right array element.

>> 
>> A person should not have to start counting at zero, the compiler
…[11 more quoted lines elided]…
>
Numerating is a valid concept, but it has nothing to do with starting to count
at zero.  Numerating is giving an alternate token or variable name to a
variable, and allowing the alternate variable name to be used in its place.

>Numerating is giving numbers to things.  In the case of array items
>numerating gives a number to each item by which it may be referenced. 
…[12 more quoted lines elided]…
>
The COBOL language was designed to let the programmer start counting at one, 
and the compiler was forced to implement that concept to meets the needs of
the COBOL standard.
>
>> Why make an object oriented compiler that lets you make up your own
…[5 more quoted lines elided]…
>
It doesn't make sense to count starting at zero???????

I don't go to the store and say here take zero cents and give the clerk 
a penny.  Do you do that?  Would that be normal to you?

Get real!


Just because some computer language forced you to count starting at zero,
doesnt make it normal.  Why should anyone be forced to do such an insane thing.
Computers should be user friendly.  The whole concept behind the development of
COBOL was that it was suppose to be a language that was written in a readable 
fashion.  

But now you are still waiting to make your first Zero million dollars.

Does this make sense to you?

I admit  that COBOL can not enumerate.  I suggest you turn your idea into the
standards committe and wait 20 years to see if it happens.  Either that or get a
compiler manufacturer to add it in as an extra add-on to their compiler, or get
an object oriented compiler.  If you could build a hash code for the index that
might be interesting.  Instead of an array you could make a set!

I could still be waiting to earn my Zero'th Dollar!!!!!
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-11-02T16:12:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BE2C5F7.1D4E8BE8@Azonic.co.nz>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <PYzD7.5933$xS6.6664@www.newsranger.com> <3BE1AB30.724557E2@Azonic.co.nz>`

```
Charles wrote:

> The COBOL compiler has an index that starts at Zero, 

No.  It has nothing that 'starts at zero'.  Items in Working Storage
start at whatever byte address after the previous item.

> but it lets the programmer start counting at 1.

It _isn't_ 'counting', it is numerating, a completely different thing.

> Then the compiler subtracts one to made up the difference. 

No, usually it multiplies by the item size and adds an offset to some
point in the data area to arrive at the correct byte address. I doubt
that you will actually find any compiler that 'subracts 1'. The actual
details are usually not particularly relevant anyway.

>  Using this system when the programmer wants the 
> number 3 item in a list of occurs, then he just says move table-item (3) to a
> given location or whatever.  This is simpler for a human being to figure out,
> and makes perfect sense.  

What makes 'perfect sense' is usually entirely what one is used to.

One thread here has a request to be able to access 'number 3' with
table-item(5002).  In general my array accesses are done with variables
as subscripts, I doubt that there is _any_ program that I have written
with 'table-item(3)', nor indeed many programmers that would use literal
subscripts to any great extent.  Your example is a straw-man.

> Numerating is a valid concept, but it has nothing to do with starting 
> to count at zero.  

Array indexing or subscripting has nothing to do with counting. 

> Numerating is giving an alternate token or variable name to a
> variable, and allowing the alternate variable name to be used in its place.
 
Numerating is giving numbers to things.  In the case of array items
numerating gives a number to each item by which it may be referenced. In
the case of Cobol all arrays are numerated as 1, 2, 3, 4, ... n.

I don't know where you got the idea of an _alternate_ token, but there
may be a case where this is _also_ a form of numerating.

Other examples of numerating are House numbers in a street, Post Office
box numbers, car licence plates, Bank accounts.  Some start at 1, some
at zero, some at other numbers, such as 1001.

> The COBOL language was designed to let the programmer start counting at one, 
> and the compiler was forced to implement that concept to meets the needs of
> the COBOL standard.

Array indexing or subscripting has nothing to do with counting. 

I don't see the compiler being 'forced' to implement anything, it does
so willingly.  I also don't see that your original:

>> This is just lousy compiler implementation.

has any meaning.  Was it 'forced' to be 'lousy' ?  Of course not, it
just implemented the language.

> It doesn't make sense to count starting at zero???????

Array indexing or subscripting has nothing to do with counting. 

> I don't go to the store and say here take zero cents and give the clerk 
> a penny.  Do you do that?  Would that be normal to you?
 
I also don't give 200 individual cents for a $2.00 item.  Giving money
to a clerk has nothing to do with array indexing, or numerating. 

> Just because some computer language forced you to count starting at zero,
> doesnt make it normal.

Array indexing or subscripting has nothing to do with counting. 

> I admit  that COBOL can not enumerate. 

I am not sure why you 'admit' this.  I suspect that you are taking a
very limited specific view of what 'enunmeration' is, such as defined
for 'enum' in the C language, and believing that to be the only
definition.

While Cobol does not do 'C enum' it does actually enumerate the arrays,
giving each array item a number.
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 10)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-11-02T03:29:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tqoE7.10776$ym4.470848@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <PYzD7.5933$xS6.6664@www.newsranger.com> <3BE1AB30.724557E2@Azonic.co.nz> <3BE2C5F7.1D4E8BE8@Azonic.co.nz>`

```
In article <3BE2C5F7.1D4E8BE8@Azonic.co.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:

Mr Plinston asserts -

>What makes 'perfect sense' is usually entirely what one is used to.

I'm not sure that I agree with this... but how long does it take to get
used to?

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-11-03T21:37:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BE46381.B28CC116@Azonic.co.nz>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <FmgC7.10250$ym4.449477@iad-read.news.verio.net> <PYzD7.5933$xS6.6664@www.newsranger.com> <3BE1AB30.724557E2@Azonic.co.nz>`

```
NA wote:

> >What makes 'perfect sense' is usually entirely what one is used to.
> 
> I'm not sure that I agree with this...

Perhaps because you are used to rigidly thinking of there being only one
way that makes 'perfect sense' (the way _you_ are used to), and can't
contemplate that others think that _different_ ways make perfect sense
to them, because that is what they are used to.

> but how long does it take to get used to?

Maybe another 30 years for you.    ;-)
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 10)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-11-03T12:59:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7TRE7.10895$ym4.475319@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <PYzD7.5933$xS6.6664@www.newsranger.com> <3BE1AB30.724557E2@Azonic.co.nz> <3BE46381.B28CC116@Azonic.co.nz>`

```
In article <3BE46381.B28CC116@Azonic.co.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>NA wote:
>
…[7 more quoted lines elided]…
>to them, because that is what they are used to.

... or perhaps because I am familiar with Goedel and applied the
Incompleteness Theorem to the assertion given.
>
>> but how long does it take to get used to?
>
>Maybe another 30 years for you.    ;-)

It might be less... might you have found it to be more clear were there to
have been included an emoticon for sarcasm?

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 11)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-11-03T16:03:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MzUE7.3$H17.4577@paloalto-snr1.gtei.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <PYzD7.5933$xS6.6664@www.newsranger.com> <3BE1AB30.724557E2@Azonic.co.nz> <3BE46381.B28CC116@Azonic.co.nz> <7TRE7.10895$ym4.475319@iad-read.news.verio.net>`

```
NA <docdwarf@clark.net> wrote in message
news:7TRE7.10895$ym4.475319@iad-read.news.verio.net...
>
>  might you have found it to be more clear were there to
> have been included an emoticon for sarcasm?

You mean this is NOT the emoticon for sarcasm?

> DD

MCM
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 12)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-11-03T22:44:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<er_E7.10920$ym4.476714@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3BE46381.B28CC116@Azonic.co.nz> <7TRE7.10895$ym4.475319@iad-read.news.verio.net> <MzUE7.3$H17.4577@paloalto-snr1.gtei.net>`

```
In article <MzUE7.3$H17.4577@paloalto-snr1.gtei.net>,
Michael Mattias <michael.mattias@gte.net> wrote:
>NA <docdwarf@clark.net> wrote in message
>news:7TRE7.10895$ym4.475319@iad-read.news.verio.net...
…[6 more quoted lines elided]…
>> DD

Answering a question with a question is no answer at all, Mr Mattias.

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-27T10:36:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bd9d899_7@news.newsgroups.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net>`

```
You are quite correct James.

Since Man first started enumerating things, using his fingers as an analog,
the number "one" has represented the FIRST item...

It's true in EVERY language and culture that I have ever had contact with
(and a number that I have only read about).

It's interesting that some primitive cultures only count as far as three and
after that, use their word for "many".

ZERO was introduced MUCH later and then only when the need for additive
identity was recognized, as Mathematics began to develop... (It is
interesting that the Romans (for example) managed to build a complex and
advanced society and culture WITHOUT recognising zero or having a symbol for
it...).

It is sad to see the Doc, who usually argues logically and well, going
completely off the point here. As you pointed out, displacements and dumps
have NOTHING to do with counting. (But then, to be fair, Volker started it
by saying the first entry in a table is 1...

I think the Doc has been having a few beers with Grumpy and has picked up
some of his mannerisms...

Or maybe in the Dwarf world they have a completely different concept of
number...<G>

Pete.




"James" <mangogrower@telocity.com> wrote in message
news:sYfC7.67$VF.215295@newsrump.sjc.telocity.net...
> Actually counting starts at 1.  If you have ZERO items, you can't start
> counting!
> OFFSETS are not counting but rather adding a displacement to something.
> That's what in 'C' et al, my_array[0] actually does just like in
assembler.
> Its says, get address of start of my_array, add 0, use this address.
> In COBOL, we're saying   access the element at displacement position n.
…[7 more quoted lines elided]…
> > If simple errors did that, Mr Bandke, then I would spend my life
sounding
> > like a Yankee peddler.
> >
…[10 more quoted lines elided]…
> > Table displacements are one thing, Mr Bandke, but a Good Programmer
needed
> > - again, in the Oldene Dayse - the ability to 'shoot a dump' to
determine
> > errors.  Displacements in the dump (a snapshot of the core, or 'The
Temple
> > of Truth') begin at zero.
> >
…[19 more quoted lines elided]…
>





-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-10-26T21:54:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BD9DD34.1C3E0597@home.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com>`

```


"Peter E. C. Dashwood" wrote:

> You are quite correct James.
>
…[27 more quoted lines elided]…
>

As the centurion said to the Praetorian Guard - "From the right number !". To
which they responded, "I", "I, I", "I, I, I", "I, V", "V", "V, I",  etc.... <G>
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-27T12:15:55+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bd9ef15_5@news.newsgroups.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com> <3BD9DD34.1C3E0597@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3BD9DD34.1C3E0597@home.com...
>
> As the centurion said to the Praetorian Guard - "From the right number !".
To
> which they responded, "I", "I, I", "I, I, I", "I, V", "V", "V, I",
etc.... <G>
>
LOL! (But I note they started at "i"...) Must have been fun to hear them
marching..."Sinister, dexter, sinister, dexter..."

Many years ago as a young whippersnapper (as opposed to the mature
whippersnapper keying this...<G>) I remember passing an afternoon writing a
module for the mainframe which converted numbers to Roman. We used it to
produce one of the major Company financial reports, just for our own
amusement...

I wonder if anyone out there is using something similar to produce Excel
spreadsheets in Roman Numerals on April Fool's day, for example...?

Pete.

>



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 7)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-10-26T19:12:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rcvpl02njl@enews3.newsguy.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com>`

```
This link seems to apply:

http://www.theonion.com/onion3311/microsoftpatents.html

If not, at least it's funny.
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 7)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-27T02:03:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eCoC7.10304$ym4.451161@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com>`

```
In article <3bd9d899_7@news.newsgroups.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>You are quite correct James.
>
…[7 more quoted lines elided]…
>after that, use their word for "many".

... and they also lived to an average age of what, twenty-seven?

>
>ZERO was introduced MUCH later and then only when the need for additive
…[3 more quoted lines elided]…
>it...).

The Romans had such things... but they did not, as I recall - but my
memory is, admittedly, porous - have very many Good Programmers, the
subject of my assertion.

>
>It is sad to see the Doc, who usually argues logically and well, going
>completely off the point here.

You mean, Mr Dashwood, that an argument cannot be 'off the point' and yet
still be logical?

>As you pointed out, displacements and dumps
>have NOTHING to do with counting.

With all due respect, Mr Dashwood... how are you defining 'displacement'?
If you are using a variation of the common 'difference between an initial
position and any later position' then it would be interesting to know just
how this difference is determined *without* measurement... as most
measurements, of course, involve enumeration of units.  It is reather
difficult to enumerate without counting, last I looked.

>(But then, to be fair, Volker started it
>by saying the first entry in a table is 1...
…[5 more quoted lines elided]…
>number...<G>

I think it would be *much* more interesting to point out the flaws you
perceive in my assumptions, logics or conclusions... but, of course,
'interesting' is in the mind of the beholder.

DD

>"James" <mangogrower@telocity.com> wrote in message
>news:sYfC7.67$VF.215295@newsrump.sjc.telocity.net...
…[64 more quoted lines elided]…
>-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 8)_

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-10-27T13:34:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iJyC7.1140994$ai2.86713311@bin2.nnrp.aus1.giganews.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com> <eCoC7.10304$ym4.451161@iad-read.news.verio.net>`

```

" NA" <docdwarf@clark.net>
>
> With all due respect, Mr Dashwood... how are you defining 'displacement'?
…[5 more quoted lines elided]…
>

Then I guess "He's gone over to the Dark Side(tm)" doesn't count.
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 9)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-27T19:10:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NEDC7.10338$ym4.452872@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bd9d899_7@news.newsgroups.com> <eCoC7.10304$ym4.451161@iad-read.news.verio.net> <iJyC7.1140994$ai2.86713311@bin2.nnrp.aus1.giganews.com>`

```
In article <iJyC7.1140994$ai2.86713311@bin2.nnrp.aus1.giganews.com>,
JerryP <news@bisusa.com> wrote:
>
>" NA" <docdwarf@clark.net>
…[9 more quoted lines elided]…
>Then I guess "He's gone over to the Dark Side(tm)" doesn't count.

I don't see how it is enumerating anything, no.

('What about Bottles... doesn't *she* count?'  'Only to ten, Mudhead')

(Firesign Theatre reference)

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 10)_

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-10-27T22:33:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YCGC7.45111$W87.2555650@bin4.nnrp.aus1.giganews.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bd9d899_7@news.newsgroups.com> <eCoC7.10304$ym4.451161@iad-read.news.verio.net> <iJyC7.1140994$ai2.86713311@bin2.nnrp.aus1.giganews.com> <NEDC7.10338$ym4.452872@iad-read.news.verio.net>`

```

" NA" <docdwarf@clark.net> wrote in message
news:NEDC7.10338$ym4.452872@iad-read.news.verio.net...
> In article <iJyC7.1140994$ai2.86713311@bin2.nnrp.aus1.giganews.com>,
> JerryP <news@bisusa.com> wrote:
…[3 more quoted lines elided]…
> >> With all due respect, Mr Dashwood... how are you defining
'displacement'?
> >> If you are using a variation of the common 'difference between an
initial
> >> position and any later position' then it would be interesting to know
just
> >> how this difference is determined *without* measurement... as most
> >> measurements, of course, involve enumeration of units.  It is reather
…[5 more quoted lines elided]…
> I don't see how it is enumerating anything, no.

Well, it IS a change from 'an initial position and any later position.'
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 11)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-28T01:46:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ErJC7.10360$ym4.453667@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <iJyC7.1140994$ai2.86713311@bin2.nnrp.aus1.giganews.com> <NEDC7.10338$ym4.452872@iad-read.news.verio.net> <YCGC7.45111$W87.2555650@bin4.nnrp.aus1.giganews.com>`

```
In article <YCGC7.45111$W87.2555650@bin4.nnrp.aus1.giganews.com>,
JerryP <news@bisusa.com> wrote:
>
>" NA" <docdwarf@clark.net> wrote in message
…[18 more quoted lines elided]…
>Well, it IS a change from 'an initial position and any later position.'

I see... and what is the difference between the two positions, then?

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 8)_

- **From:** Robaire <robaireRemoveThis@sympatico.ca>
- **Date:** 2001-10-27T10:50:28-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ailttovcvtdofbv5dccfdmhm7ul31q5hk@4ax.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com> <eCoC7.10304$ym4.451161@iad-read.news.verio.net>`

```
On Sat, 27 Oct 2001 02:03:54 GMT, docdwarf@clark.net (  NA) wrote:

>In article <3bd9d899_7@news.newsgroups.com>,
>Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
<snip>
>The Romans had such things... but they did not, as I recall - but my
>memory is, admittedly, porous - have very many Good Programmers, the
>subject of my assertion.

Some of us would also have memory troubles 
if we were trying to recall our days among the Romans.

Robaire
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 9)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-27T19:12:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8GDC7.10339$ym4.452914@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bd9d899_7@news.newsgroups.com> <eCoC7.10304$ym4.451161@iad-read.news.verio.net> <9ailttovcvtdofbv5dccfdmhm7ul31q5hk@4ax.com>`

```
In article <9ailttovcvtdofbv5dccfdmhm7ul31q5hk@4ax.com>,
Robaire  <robaireRemoveThis@sympatico.ca> wrote:
>On Sat, 27 Oct 2001 02:03:54 GMT, docdwarf@clark.net (  NA) wrote:
>
…[8 more quoted lines elided]…
>if we were trying to recall our days among the Romans.

It was just before the Days of Stability... when folks were just roamin'
around.

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-28T09:31:26+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdb1a7a_2@news.newsgroups.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com> <eCoC7.10304$ym4.451161@iad-read.news.verio.net>`

```
Responses below, Doc.

" NA" <docdwarf@clark.net> wrote in message
news:eCoC7.10304$ym4.451161@iad-read.news.verio.net...
> In article <3bd9d899_7@news.newsgroups.com>,
> Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
> >You are quite correct James.
> >
> >Since Man first started enumerating things, using his fingers as an
analog,
> >the number "one" has represented the FIRST item...
> >
…[3 more quoted lines elided]…
> >It's interesting that some primitive cultures only count as far as three
and
> >after that, use their word for "many".
>
> ... and they also lived to an average age of what, twenty-seven?
>
Nope. They lived to an age of "many"...<G>

> >
> >ZERO was introduced MUCH later and then only when the need for additive
> >identity was recognized, as Mathematics began to develop... (It is
> >interesting that the Romans (for example) managed to build a complex and
> >advanced society and culture WITHOUT recognising zero or having a symbol
for
> >it...).
>
…[3 more quoted lines elided]…
>
Well, it's a ways back in the thread now, but I'm not convinced the "subject
of your assertion" was, in fact, "good programmers"... Let's have a look...

"What's all this fancy stuff?  Mr Bandke, with all due respect... need it
be pointed out to you that All Good Programmers start counting at 0?"

Ah, yes, I see.

So let's examine this a bit more...(hey, it's an overcast Sunday here and I
have nothing pressing to do...<G>)

"ALL Good Programmers..."

That's a sweeping statement. If there is ONE single "Good Programmer" who
DOESN'T start counting at zero, then the assertion is logically false.

I have worked with a number of VERY good programmers over the years. None of
them started counting at zero. I therefore contend that the premise is false
by reason of contradictory example...<G>


> >
> >It is sad to see the Doc, who usually argues logically and well, going
…[4 more quoted lines elided]…
>
Yes. While it can be philosophically entertaining and amusing, it cannot
establish the truth or falsity of the "point" unless the premises remain
pertinent to it. This establishment of truth or otherwise is one definition
of "logical". You COULD have a logical argument about some OTHER point (the
famous "put up a smokescreen and sidetrack your antagonist" arguing
device... as a basically honest debater I don't know much about this...<G>),
but it would not be logical as far as the point under discussion is
concerned. (See "non sequitur"...)

> >As you pointed out, displacements and dumps
> >have NOTHING to do with counting.
>

> With all due respect, Mr Dashwood... how are you defining 'displacement'?

While I commend your politeness, it cuts no ice... I KNOW you have no
respect for anyone other than Snow White, and that's only because she clips
you round the ear when you pick on Dopey...<G>

> If you are using a variation of the common 'difference between an initial
> position and any later position' then it would be interesting to know just
…[4 more quoted lines elided]…
>
1. I am not defining "displacement". (I'll accept your definition above).
2. The "difference" is determined by calculation, NOT by "measurement". The
calculation includes whether the offset is from 1 or 0 because BOTH types of
displacement are valid. Not ALL systems use zero displacement. There is a
great big world outside IBM mainframes Doc...
3. As "enumerate" and "count" are synonyms in the English language, your
last sentence above resolves to "It is rather difficult to count without
counting"... Well....duhhhh.
4. A discussion on "displacements" is only of passing pertinence to the
premise that "All good programmers start counting at zero".

> >(But then, to be fair, Volker started it
> >by saying the first entry in a table is 1...
…[10 more quoted lines elided]…
>
Well, I hope the above has proved "interesting" for you, Doc.

I certainly found it amusing and entertaining so I guess that would be one
definition of "interesting"...<G>

Pete.





-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 9)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-28T01:44:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FpJC7.10359$ym4.453706@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bd9d899_7@news.newsgroups.com> <eCoC7.10304$ym4.451161@iad-read.news.verio.net> <3bdb1a7a_2@news.newsgroups.com>`

```
In article <3bdb1a7a_2@news.newsgroups.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>Responses below, Doc.
>
…[17 more quoted lines elided]…
>Nope. They lived to an age of "many"...<G>

In the words of a Wise Philosopher: says who?

>
>> >
…[16 more quoted lines elided]…
>Ah, yes, I see.

Or so you say, Mr Dashwood... let it roll along, then...

>
>So let's examine this a bit more...(hey, it's an overcast Sunday here and I
>have nothing pressing to do...<G>)
>
>"ALL Good Programmers..."

Emphasis not original, of course.
>
>That's a sweeping statement. If there is ONE single "Good Programmer" who
…[4 more quoted lines elided]…
>by reason of contradictory example...<G>

A good try, Mr Dashwood, but examine the original assertion as it was
stated, not as you rephrased it:

'... All Good Programmers start counting at 0'

Given this, Mr Dashwood, then if you worked with someone who did not start
counting at 0 then... they were not Good Programmers (caps original), as
'All Good Programmers start counting at 0'.

QED, and suchlike.

>
>
…[9 more quoted lines elided]…
>pertinent to it.

What does 'establish(ing) the truth or falsity' of *anything* have to do
with logic, Mr Dashwood?

>This establishment of truth or otherwise is one definition
>of "logical".

Please be so kind as to provide a citing for this definition, Mr
Dashwood; it appeast to be utterly idiosyncratic.

 You COULD have a logical argument about some OTHER point (the
>famous "put up a smokescreen and sidetrack your antagonist" arguing
>device... as a basically honest debater I don't know much about this...<G>),
>but it would not be logical as far as the point under discussion is
>concerned. (See "non sequitur"...)

Mr Dashwood, you seem to have an understanding of 'logic' which is a
bit... curious, to say the least.

>
>> >As you pointed out, displacements and dumps
…[7 more quoted lines elided]…
>you round the ear when you pick on Dopey...<G>

I'll take that, Mr Dashwood, as 'I had no definition at hand so I threw
out a smokescreen'.

>
>> If you are using a variation of the common 'difference between an initial
…[6 more quoted lines elided]…
>1. I am not defining "displacement". (I'll accept your definition above).

How ever kind of you.

>2. The "difference" is determined by calculation, NOT by "measurement".

What is calculated, Mr Dashwood, outside of something measured?

>The
>calculation includes whether the offset is from 1 or 0 because BOTH types of
>displacement are valid.

Nothing was ever stated to the contrary, Mr Dashwood... it was stated
which one was used by Good Programmers.

>Not ALL systems use zero displacement. There is a
>great big world outside IBM mainframes Doc...

This was never contested, Mr Dashwood.

>3. As "enumerate" and "count" are synonyms in the English language, your
>last sentence above resolves to "It is rather difficult to count without
>counting"... Well....duhhhh.

Exactly... you, however, took issue with displacement being measured and
suggested that it was calculated; the question becomes 'what is calculated
except for that-which-is-measured'.

>4. A discussion on "displacements" is only of passing pertinence to the
>premise that "All good programmers start counting at zero".

Not when it comes to counting displacements, no.

>
>> >(But then, to be fair, Volker started it
…[15 more quoted lines elided]…
>definition of "interesting"...<G>

*That*, Mr Dashwood, is where the delight begins... as Nietzsche said, one
should try to re-gain the seriousness of a child at play.

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 10)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-28T16:14:28+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdb787c_8@news.newsgroups.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bd9d899_7@news.newsgroups.com> <eCoC7.10304$ym4.451161@iad-read.news.verio.net> <3bdb1a7a_2@news.newsgroups.com> <FpJC7.10359$ym4.453706@iad-read.news.verio.net>`

```
Hahaha! Good stuff, Doc...

It's raining here now so  the beach is out...I  just have time for a quick
response before closing the system...

See below.

" NA" <docdwarf@clark.net> wrote in message
news:FpJC7.10359$ym4.453706@iad-read.news.verio.net...
> In article <3bdb1a7a_2@news.newsgroups.com>,
> Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
…[8 more quoted lines elided]…
> >> >Since Man first started enumerating things, using his fingers as an
analog,
> >> >the number "one" has represented the FIRST item...
> >> >
> >> >It's true in EVERY language and culture that I have ever had contact
with
> >> >(and a number that I have only read about).
> >> >
> >> >It's interesting that some primitive cultures only count as far as
three and
> >> >after that, use their word for "many".
> >>
…[5 more quoted lines elided]…
>

I don't know what wise philospher that was, but it is axiomatic that if the
people lived more than 3 years, THEY would consider their lifespan to be
"many" years... They have no other word for it.

> >
> >> >
> >> >ZERO was introduced MUCH later and then only when the need for
additive
> >> >identity was recognized, as Mathematics began to develop... (It is
> >> >interesting that the Romans (for example) managed to build a complex
and
> >> >advanced society and culture WITHOUT recognising zero or having a
symbol for
> >> >it...).
> >>
…[4 more quoted lines elided]…
> >Well, it's a ways back in the thread now, but I'm not convinced the
"subject
> >of your assertion" was, in fact, "good programmers"... Let's have a
look...
> >
> >"What's all this fancy stuff?  Mr Bandke, with all due respect... need it
…[7 more quoted lines elided]…
> >So let's examine this a bit more...(hey, it's an overcast Sunday here and
I
> >have nothing pressing to do...<G>)
> >
…[7 more quoted lines elided]…
> >I have worked with a number of VERY good programmers over the years. None
of
> >them started counting at zero. I therefore contend that the premise is
false
> >by reason of contradictory example...<G>
>
…[3 more quoted lines elided]…
> '... All Good Programmers start counting at 0'

The only difference is the emphasis on ALL. Whether you emphasise it or you
don't, it is STILL a sweeping statement...<G>

>
> Given this, Mr Dashwood, then if you worked with someone who did not start
> counting at 0 then... they were not Good Programmers (caps original), as
> 'All Good Programmers start counting at 0'.
>
Ah, but the problem here is that your assertion is NOT given. On the
contrary, it is being hotly contested... I agree that if it WERE given, then
my case would be lost. My "good try" stands and is more than good enough to
refute this particular argument...<G>


> QED, and suchlike.
>
Nope. Neither "Quite Easily Done" nor "Quod Erat Demonstrandum..."

"Quantifiably Erroneous Deduction" perhaps...<G>
> >
> >
…[4 more quoted lines elided]…
> >> You mean, Mr Dashwood, that an argument cannot be 'off the point' and
yet
> >> still be logical?
> >>
…[12 more quoted lines elided]…
>
Take it up with Socrates. His philosophy was based on a two valued (true or
false) logic system. Anyway, the argument from Authority proves nothing
(except that you need an equal and opposite Authority to refute it). I said
it was ONE definition of "logic". Whether it is idiosyncratic or not has no
bearing on the value of the idea...

>  You COULD have a logical argument about some OTHER point (the
> >famous "put up a smokescreen and sidetrack your antagonist" arguing
> >device... as a basically honest debater I don't know much about
this...<G>),
> >but it would not be logical as far as the point under discussion is
> >concerned. (See "non sequitur"...)
…[3 more quoted lines elided]…
>

Despite formal training in the subject  (a major handicap which I urge all
students reading this to discard immediately...<G>) I have learned across
many years the recognition of straight and crooked thinking, and the
difference between them.

(You wouldn't have bothered to reply if you didn't think I was worth the
effort, Doc...<G>, "curious" logic or not...)


> >
> >> >As you pointed out, displacements and dumps
…[3 more quoted lines elided]…
> >> With all due respect, Mr Dashwood... how are you defining
'displacement'?
> >
> >While I commend your politeness, it cuts no ice... I KNOW you have no
> >respect for anyone other than Snow White, and that's only because she
clips
> >you round the ear when you pick on Dopey...<G>
>
…[4 more quoted lines elided]…
> >> If you are using a variation of the common 'difference between an
initial
> >> position and any later position' then it would be interesting to know
just
> >> how this difference is determined *without* measurement...
> >> as most
…[12 more quoted lines elided]…
> >calculation includes whether the offset is from 1 or 0 because BOTH types
of
> >displacement are valid.
>
> Nothing was ever stated to the contrary, Mr Dashwood... it was stated
> which one was used by Good Programmers.

They can (and are) both be used by Good Programmers, depending on the
requirements. The recognition of this is one of the contributing factors
that makes a programmer "good".
>
> >Not ALL systems use zero displacement. There is a
…[10 more quoted lines elided]…
> except for that-which-is-measured'.

The last resort, "query the definition"... You'll really need to do better
than that, Doc...<G>

There is a  subtle difference between calculating something and measuring
it. The process is different. The end result may well give the same
assessment, but the process is what we are concerned with here.

Displacements may be calculated in Hex, Octal, and or decimal (or any other
"shorthand" form of binary), but we don't normally COUNT in these bases.
Even if you were counting bytes into a hex displacement, it is most likely
you would count in decimal then convert to a hex address.
>
> >4. A discussion on "displacements" is only of passing pertinence to the
…[3 more quoted lines elided]…
>
If the requirement is to start at 1 (and you have agreed elsewhere that it
could be, here's the quote: "> >The
> >calculation includes whether the offset is from 1 or 0 because BOTH types
of
> >displacement are valid.
>
> Nothing was ever stated to the contrary, Mr Dashwood... "),  then anyone
using this system (displacement from 1 required) cannot be a good
programmer, according to your definition...

That is patently absurd, so I propose the following:

I'll allow you the displacement  measurement/calculation stuff, if you will
retract or modify your original statement regarding "All Good Programmers",
and we call it a draw <G> How's that?

> >
> >> >(But then, to be fair, Volker started it
> >> >by saying the first entry in a table is 1...
> >> >
> >> >I think the Doc has been having a few beers with Grumpy and has picked
up
> >> >some of his mannerisms...
> >> >
> >> >Or maybe in the Dwarf world they have a completely different concept
of
> >> >number...<G>
> >>
…[6 more quoted lines elided]…
> >I certainly found it amusing and entertaining so I guess that would be
one
> >definition of "interesting"...<G>
>
> *That*, Mr Dashwood, is where the delight begins... as Nietzsche said, one
> should try to re-gain the seriousness of a child at play.
>
Absolutely!

Pete.



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 11)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-28T09:42:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lqQC7.10373$ym4.454605@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bdb1a7a_2@news.newsgroups.com> <FpJC7.10359$ym4.453706@iad-read.news.verio.net> <3bdb787c_8@news.newsgroups.com>`

```
In article <3bdb787c_8@news.newsgroups.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>Hahaha! Good stuff, Doc...

Pfoo... you'se jes' easily amused.

>
>It's raining here now so  the beach is out...I  just have time for a quick
…[34 more quoted lines elided]…
>"many" years... They have no other word for it.

'They' are not here, Mr Dashwood... but you are, hence my asking.

>
>> >
…[42 more quoted lines elided]…
>don't, it is STILL a sweeping statement...<G>

If that is 'the only difference', Mr Dashwood, then there's little need to
worry about discarding it.

>
>>
…[7 more quoted lines elided]…
>refute this particular argument...<G>

Mr Dashwood, do tell... how could this assertion be contested if it had
not been given?

>
>
…[4 more quoted lines elided]…
>"Quantifiably Erroneous Deduction" perhaps...<G>

Saying so doesn't make it true, Mr Dashwood.  As noted above: you cannot
contest what has not been given.  You contest the assertion 'all Good
Programmers start counting at 0', therefore the assertion has been given.

>> >
>> >
…[20 more quoted lines elided]…
>Take it up with Socrates.

I will when he starts posting, Mr Dashwood... did he count 'one, two,
many', as well?

>His philosophy was based on a two valued (true or
>false) logic system.

Mr Dashwood, you seem to be confusing Socrates and Aristotle... the
Principle of Non-Contradiction belongs to the latter.

>Anyway, the argument from Authority proves nothing
>(except that you need an equal and opposite Authority to refute it).

Is this why you mention Socrates?

>I said
>it was ONE definition of "logic". Whether it is idiosyncratic or not has no
>bearing on the value of the idea...

It has not been shown that this is even 'one definition', Mr Dashwood...
and it says in *my* dictionary, clearly and unambiguously, that 'The 
establishment of truth or otherwise is *in no wise* (emphasis original) 
one definition of "logical"'... granted it says this in crayon, on a
back-page... but it is said nonetheless.

>
>>  You COULD have a logical argument about some OTHER point (the
…[12 more quoted lines elided]…
>difference between them.

Mr Dashwood, one learns many things which one no longer applies... when
was the last time you used a soldering-iron?

>
>(You wouldn't have bothered to reply if you didn't think I was worth the
>effort, Doc...<G>, "curious" logic or not...)

Mr Dashwood, not 'you'... Truth!  Note the questions have not been about
you, my questions have been about your arguments; the two are readily
separable.

>
>
…[40 more quoted lines elided]…
>that makes a programmer "good".

And who says *this*, Mr Dashwood... you, Socrates or one of those 'one,
two, many' counting-folks?

>>
>> >Not ALL systems use zero displacement. There is a
…[13 more quoted lines elided]…
>than that, Doc...<G>

Mr Dashwood, the first step is to establish definitions... how else can
one know what one is talking about?

>
>There is a  subtle difference between calculating something and measuring
>it. The process is different. The end result may well give the same
>assessment, but the process is what we are concerned with here.

Oh... you wouldn't happen to be able to specify this 'subtle difference',
would you?... or is it like 'Art', and you just 'know what you like'?

>
>Displacements may be calculated in Hex, Octal, and or decimal (or any other
>"shorthand" form of binary), but we don't normally COUNT in these bases.

Plural majestatus est, Mr Dashwood... and most folks normally aren't Good
Programmers.

>Even if you were counting bytes into a hex displacement, it is most likely
>you would count in decimal then convert to a hex address.

See above about what most folks normally aren't.

>>
>> >4. A discussion on "displacements" is only of passing pertinence to the
…[12 more quoted lines elided]…
>programmer, according to your definition...


Eh?  What sausages were you eating before you had the dream that *this*
happened?  The attributions are rather difficult to follow here, Mr
Dashwood, and clarification would be appreciated.

>
>That is patently absurd,

(some people take *forever* to catch on!)

>so I propose the following:
>
>I'll allow you the displacement  measurement/calculation stuff, if you will
>retract or modify your original statement regarding "All Good Programmers",
>and we call it a draw <G> How's that?

You ask that I retract or modify what you've already shown is given, Mr
Dashwood, by the fact that you have contested it and that it is impossible
to contest that which is not given.

>
>> >
…[21 more quoted lines elided]…
>Absolutely!

Well, then... mumblety-peg, anyone?

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 12)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-31T12:12:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdf346d_3@news.newsgroups.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bdb1a7a_2@news.newsgroups.com> <FpJC7.10359$ym4.453706@iad-read.news.verio.net> <3bdb787c_8@news.newsgroups.com> <lqQC7.10373$ym4.454605@iad-read.news.verio.net>`

```
Positively last post from me on this, Doc. The sun is out again and I have
some more worthwhile things to do...<G>

Besides, your five minutes is up and you'll have to pay if you wish to
continue the argument (See Monty Python... "The Argument")

There are just three points I need to comment on:

1. I said "Socrates" when I should have said "Aristotle" as you quite
correctly pointed out... <Blushes with embarrassment and goes off to find
some hemlock...>.

I put this down to the fact that it is now just over 35 years since I did
Philosophy 101, but nevertheless, I was quite wrong on that. As we both
know, the Socratic method has very little application in this NG.
Aristotelian logic on the other hand is very pertinent to computers<G>.

2. You definitely have a different definition of "given".

When building a syllogism the premises are merely "propositions". They are
NOT "given" until both sides agree to their truth. (hence..."OK, I'll GIVE
you that...)

If you are postulating an argument, then a premise may be "given"
TEMPORARILY, just to see where the consequences will lead.
 In other words, IF it is true, the conclusions follow.

For example: "Given that Pete drinks Jack Daniels,  he probably has some in
his house."  A temporary premise.

I contest the truth of your assertion and it is therefore NOT given as far
as I am concerned, because there is no way that it is true.

(It is not true because it is a sweeping statement (these are rarely true
unless they are axiomatic like "All islands
are surrounded by water" ...self evidently true because the definition of an
island is that it must be surrounded by water), your attribution to "good
programmers" that they must start counting from zero" is not in this
category...

You could argue that the definition of a good programmer is someone who
starts counting at zero, but that is a different (and just as unsupportable)
argument. (However, it would be refuted by a different arguing device...)

3. By a very spooky coincidence, I last used a soldering iron
yesterday...<G>

As usual, an enjoyable exchange. Which just goes to show that things can be
fun even when nothing is achieved.  (You are right, I am easily amused...)

Pete.




-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 13)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-30T18:40:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JSGD7.9113$Fy2.1667972@news20.bellglobal.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bdb1a7a_2@news.newsgroups.com> <FpJC7.10359$ym4.453706@iad-read.news.verio.net> <3bdb787c_8@news.newsgroups.com> <lqQC7.10373$ym4.454605@iad-read.news.verio.net> <3bdf346d_3@news.newsgroups.com>`

```
Don't you just hate it when item (1) is the second item? When I count the
items, I always start with the first.  The reason is quite simple. If there
are no items, I cannot count them.  It is logically impossible to count
anything before anything exists, which would be the case if I counted the
0th item first.  The philosopher you actually want is actually Pythagorous,
who started with a single point, though you might also want one of the
french existentionalists to back you up on the fact that if nothing exists,
in cannot be counted. The only place it really matters, of course, is in
fitting angels on the head of a pin.

Donald

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3bdf346d_3@news.newsgroups.com...
> Positively last post from me on this, Doc. The sun is out again and I have
> some more worthwhile things to do...<G>
…[25 more quoted lines elided]…
> For example: "Given that Pete drinks Jack Daniels,  he probably has some
in
> his house."  A temporary premise.
>
…[5 more quoted lines elided]…
> are surrounded by water" ...self evidently true because the definition of
an
> island is that it must be surrounded by water), your attribution to "good
> programmers" that they must start counting from zero" is not in this
…[3 more quoted lines elided]…
> starts counting at zero, but that is a different (and just as
unsupportable)
> argument. (However, it would be refuted by a different arguing device...)
>
…[3 more quoted lines elided]…
> As usual, an enjoyable exchange. Which just goes to show that things can
be
> fun even when nothing is achieved.  (You are right, I am easily amused...)
>
…[8 more quoted lines elided]…
> -----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 13)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-31T03:47:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bvKD7.10604$ym4.463432@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <3bdb787c_8@news.newsgroups.com> <lqQC7.10373$ym4.454605@iad-read.news.verio.net> <3bdf346d_3@news.newsgroups.com>`

```
In article <3bdf346d_3@news.newsgroups.com>,
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>Positively last post from me on this, Doc. The sun is out again and I have
>some more worthwhile things to do...<G>
>
>Besides, your five minutes is up and you'll have to pay if you wish to
>continue the argument (See Monty Python... "The Argument")

Really, Mr Dashwood... it can be argued that we've both already paid
double what it's worth.

>
>There are just three points I need to comment on:
…[3 more quoted lines elided]…
>some hemlock...>.

No need for the hemlock... yew'll do just fine without it.

[snippage]

>2. You definitely have a different definition of "given".

Than whom?

>
>When building a syllogism the premises are merely "propositions". They are
>NOT "given" until both sides agree to their truth. (hence..."OK, I'll GIVE
>you that...)

Ummmmm... do you have a cite for this?  I'm not sure I'll give you that.

>
>If you are postulating an argument, then a premise may be "given"
…[7 more quoted lines elided]…
>as I am concerned, because there is no way that it is true.

Mr Dashwood, clip out a modifying clause and see what you've just written:

'I contest the truth of your assertion... because there is no way that it
is true.'

That Phil 101 course *must* have been long ago, Mr Dashwood... proof by
assertion?

>
>(It is not true because it is a sweeping statement (these are rarely true
…[4 more quoted lines elided]…
>category...

Getting close, Mr Dashwood... a mention of attribution...

>
>You could argue that the definition of a good programmer is someone who
>starts counting at zero, but that is a different (and just as unsupportable)
>argument. (However, it would be refuted by a different arguing device...)

Bingo!  *Now*, Mr Dashwood, consider the original statement in the light
you've just accidentally flipped on:

'All Good Programmers begin counting at zero.'

... and ask yourself 'Is this a statement of attribution or of
definition?  What logical steps am I taking to arrive at that conclusion?'

(for extra credit the statement can be considered in light of
Wittgenstein's question 'What is the difference between a symptom and a
criterion?'... but perhaps that might be saved for the Extra-Credit
Question.)

(and now... I can almost hear the snorts of annoyance and utterings of 'Is
*that* what he's been going on about for the past umpty-sknorg postings?
*I* thought this was about programming; where does this stuff about 'how
can you tell if a statement is one of attribution or definition' come
from?  Hmmmm... and what *is* the difference between a symptom and a
criterion... hmmmmmmm.....)

>
>3. By a very spooky coincidence, I last used a soldering iron
>yesterday...<G>

I'm sure it was a Really Hot Time.

>
>As usual, an enjoyable exchange. Which just goes to show that things can be
>fun even when nothing is achieved.  (You are right, I am easily amused...)

Glad you enjoyed, old boy.

DD
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 7)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-10-27T01:09:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jrC7.18620$MG4.3455760@news20.bellglobal.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com>`

```
If god had wanted us to count in decimal, we would not have been given four
fingers and a parity thumb on each hand.

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3bd9d899_7@news.newsgroups.com...
> You are quite correct James.
>
> Since Man first started enumerating things, using his fingers as an
analog,
> the number "one" has represented the FIRST item...
>
…[3 more quoted lines elided]…
> It's interesting that some primitive cultures only count as far as three
and
> after that, use their word for "many".
>
…[3 more quoted lines elided]…
> advanced society and culture WITHOUT recognising zero or having a symbol
for
> it...).
>
…[36 more quoted lines elided]…
> > > (explanation: back in the Oldene Dayse, when folks who sold things -
and
> > > just about everyone else, for that matter - travelled by
horse-and-wagon
> > > things in transit tended to make more noise... whether the Yankees
were
> > > more prone towards audible expressions than anyone else has never been
> > > documented)
…[21 more quoted lines elided]…
> > > >And of course I always count in binary, I only pronounce it in
decimal
> > > >(that's why I used text, not numerals
> > >
> > > You use text to count in binary?  That can make for problems;
> > > zeroonezeroonezeroone onezeroonezeroonezero does not maintain
half-word
> > > alignment, aber auf Deutsch nulleinsnulleinsnulleins
> > > einsnulleinsnulleinsnull ganz gut ist.
…[13 more quoted lines elided]…
> -----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 8)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-10-27T12:38:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<601493250C71D9B0.B3B462BE64DECB29.56330DABE5151B20@lp.airnews.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com> <6jrC7.18620$MG4.3455760@news20.bellglobal.com>`

```
On Sat, 27 Oct 2001 01:09:01 -0400, "Donald Tees"
<donald_tees@sympatico.ca> enlightened us:

>If god had wanted us to count in decimal, we would not have been given four
>fingers and a parity thumb on each hand.
>

In the same vein, if God had intended for man to use the metric
system, Jesus would have only had ten disciples!


>"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
>news:3bd9d899_7@news.newsgroups.com...
…[108 more quoted lines elided]…
>

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I live in my own little world, 
but it's OK, they know me here.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 9)_

- **From:** "JerryP" <news@bisusa.com>
- **Date:** 2001-10-27T22:37:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HGGC7.1145717$ai2.87133107@bin2.nnrp.aus1.giganews.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com> <6jrC7.18620$MG4.3455760@news20.bellglobal.com> <601493250C71D9B0.B3B462BE64DECB29.56330DABE5151B20@lp.airnews.net>`

```

"SkippyPB" <swiegand@nospam.neo.rr.com> wrote in message
news:601493250C71D9B0.B3B462BE64DECB29.56330DABE5151B20@lp.airnews.net...
> On Sat, 27 Oct 2001 01:09:01 -0400, "Donald Tees"
> <donald_tees@sympatico.ca> enlightened us:
>
> >If god had wanted us to count in decimal, we would not have been given
four
> >fingers and a parity thumb on each hand.
> >
…[3 more quoted lines elided]…
>

He did. Ten Commandments, Orders of Mishnah, Righteous Men, Plagues, etc.

Some just didn't get the word (or Word, depending).
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-10-27T12:10:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9vxC7.4$aS2.39195@paloalto-snr2.gtei.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com>`

```
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
news:3bd9d899_7@news.newsgroups.com...
>
> It's interesting that some primitive cultures only count as far as three
and
> after that, use their word for "many".

Hmm.. I gues that explains the products of the Chicago Public Schools....


MCM
```

###### ↳ ↳ ↳ Re: How do you count?

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-10-28T09:35:26+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bdb1b0a_1@news.newsgroups.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <ii0ittokkoovdshb7ns237v32kqj90r4e0@4ax.com> <QEaC7.10217$ym4.448729@iad-read.news.verio.net> <o6gitt4o1k73s101rn9ovdm53ms772o9j0@4ax.com> <56dC7.10232$ym4.448959@iad-read.news.verio.net> <sYfC7.67$VF.215295@newsrump.sjc.telocity.net> <3bd9d899_7@news.newsgroups.com> <9vxC7.4$aS2.39195@paloalto-snr2.gtei.net>`

```
I've never been to Chicago, Michael.

You realise that now, if I ever do, I'll be checking every restaurant bill
and receipt...

Thanks...I think...<G>

Pete.
"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:9vxC7.4$aS2.39195@paloalto-snr2.gtei.net...
> Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
> news:3bd9d899_7@news.newsgroups.com...
…[12 more quoted lines elided]…
>



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

#### ↳ Re: How do you count?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-10-26T10:07:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aBaC7.10216$ym4.448583@iad-read.news.verio.net>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com>`

```
In article <Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com>,
Gary Crowley <gc817@hotmail.com> wrote:
>I'm writing a program that reads a record (80 char long) and counts the
>number of lines in the data file. The data file consist of 2 poems.

Please do your own homework.

DD
```

#### ↳ Re: How do you count?

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-26T15:35:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<upfC7.1555$xS6.2143@www.newsranger.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com>`

```
On Fri, 26 Oct 2001 03:06:23 GMT, in article
<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com>, Gary Crowley stated 
>
>I'm writing a program that reads a record (80 char long) and counts the
…[8 more quoted lines elided]…
>
I will give you some Hints.

In COBOL compilers there are some figurative constants that define commonly used
data with an english-like name.  One of them is Space or Spaces.  There are
others like NUMERIC.  Another useful one is ZERO.

In your program you have to count blank lines and lines with text.  I would use
at least 2 numeric fields; I would suggest 3 fields.
Put the fields in your WORKING-STORAGE section.
We usually use something like:

01  WS-FIELDS.
05  WS-LINES          PIC 9(02) VALUE ZERO.    
05  WS-BLANK-LINES    PIC 9(02) VALUE ZERO.
05  WS-TEXT-LINES     PIC 9(02) VALUE ZERO.  

WS is a common prefix for fields used to do computations and store data.
The value statements set the counting field to zero.  If you use a numeric field
without first setting it to some value, your program will compile and then
probably abort the  first time you use it.  You will attempt a command like an
ADD and if the memory location is not numeric ADD will not work.  If it has a
numeric value in it already it may be something like 53 or some random number;
so you better set it to zero.

Then you just read the file one record at a time.  While you are reading the
file do 2 things.
1- ADD 1 TO WS-LINES.
2- IF IN-RECORD = SPACES
ADD 1 TO WS-BLANK-LINES
END-IF
(it is also permissible to end an if like this:
IF IN-RECORD = SPACES
ADD 1 TO WS-BLANK-LINES.                 
END-IF may be easier to see and more explicit   )
Keep doing it till you get to the end of the file.

Usually at the  end of a program you have an END-OF-JOB routine that closes the
files.  When you reach it you add a compute statement.
COMPUTE (WS-TEXT-LINES = WS-LINES - WS-BLANK-LINES).
Then you can move all three numerical values to a print line and print out the
results.  The print line usually has fields that edit the numbers so the leading
zeros would not print.

Nomally the END-OF-JOB  OR EOJ routine does not have the actually compute
statement or anything like that.  Usually it will have a PERFORM  statement like
"PERFORM TOTALS-ROUTINE".  Then you make a paragraph with all of the totals
routine inside of it to keep it separate.  You have to compute the lines of text
and then move the totals to the totals print line and then write the totals
print line out to your report, which usually has a heading  also.
Often in payroll programs many different fields would be totaled at the end, so
this is quite a common practice.  If you were doing a report you would count the
lines printed and after about 50 - 65 lines you would go to the next page and
print headings and start where you left off, so counting the lines printed is a
necessity in almost any program.

This is really an easy task, you just read a record and increment a counter.
You just have to test each line to see if it is a blank line or one with text.
You dont necessarily have to test the whole line you could pick a field to test.
If these are printed lines, they you just count the lines as you print them.
Either way, it is not too difficult.  This basic technique is used in almost
every program I have ever written.

You could add extra functionality and find a way to count the stanza's in the
poem and the average lines per stanza, the average words per line, or the total
number of consonants and vowels in the poem.  I will let you figure that out.
```

#### ↳ Re: How do you count?

- **From:** "Mike Kinasz" <mkinasz@cbspayroll.com>
- **Date:** 2001-10-28T05:46:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nZMC7.36370$pb4.18778102@news2.rdc2.tx.home.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com>`

```
Could you do a "CBL_CHECK_FILE_EXIST" to get the filesize and then divide
that by 80 (or 81 or 82 depending upon linefeeds/carriage returns in the
file)?
Mike


"Gary Crowley" <gc817@hotmail.com> wrote in message
news:Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com...
> I'm writing a program that reads a record (80 char long) and counts the
> number of lines in the data file. The data file consist of 2 poems. I must
> count the blank ones also.
> Any idea what I need to do to read all the lines to create a summary of
the
> number of lines in the data file?
>
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: How do you count?

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-10-29T03:35:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U74D7.4158$xS6.3359@www.newsranger.com>`
- **References:** `<Pq4C7.12962$W91.84957@news1.wwck1.ri.home.com> <nZMC7.36370$pb4.18778102@news2.rdc2.tx.home.com>`

```
Butt out Mike. Can't you see we're not into problem solving here; philosophy is
our game. <G>



In article <nZMC7.36370$pb4.18778102@news2.rdc2.tx.home.com>, Mike Kinasz
says...
>
>Could you do a "CBL_CHECK_FILE_EXIST" to get the filesize and then divide
…[19 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
