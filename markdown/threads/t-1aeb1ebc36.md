[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# working-storage vs. local-storage

_125 messages · 26 participants · 2000-03 → 2000-04_

---

### working-storage vs. local-storage

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 2000-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bhkat$621$1@slb2.atl.mindspring.net>`

```
I only know VS COBOL II (in the VSE environment), so I don't know much about
these new-fangled features.  I've seen some reference to a local-storage
section.  Relating COBOL to C, am I correct in thinking that

program-id. test.
working-storage section.
01  var1       pic x.
local-storage section
01  var2       pic x.
procedure division.
    move var1 to var2
    exit program.

would be somewhat similar to the following C code:

void test(void)
{
    static char var1;
    char var2;

    var2 = var1;
    return;
}

In other words, working-storage being static storage, while local-storage is
'automatic' (being created anew each time the program/function is entered).
Is this the case?

Actually, now that I think of it, perhaps I'm wrong.  Doesn't COBOL allow
you to declare a field as 'initial'?  I've never found a need to use it, so
I'm not sure if that's correct.

*Anyway*, please define local-storage for me.  Thanks.

(BTW, yes I know my example is not terrible useful in real life.)
```

#### ↳ Re: working-storage vs. local-storage

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bhkj5$2pq$1@nntp9.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net>`

```
I won't swear to it but BASICALLY, I think that the difference between
Working-Storage and Local-Storage is totally "invisible" UNLESS you are using
recursive programs (see the program-id paragraph in the LE  COBOL for VSE).
In that case, local-storage is "fresh" for each occurrence - while
working-storage exists (more or less in "last used state") across
occurrences.
```

##### ↳ ↳ Re: working-storage vs. local-storage

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DC67CA.EC97DA70@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bhkj5$2pq$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> I won't swear to it but BASICALLY, I think that the difference between
…[5 more quoted lines elided]…
> 
Frank,

In case you are referring to recent examples I wrote under OO Learning -
I'm guessing Bill has got it right above. Now this is purely speculative
because I'm an analyst rather than a programmer. I have asked the
question of Merant on Answerlab - but didn't get an answer :-

Question : Do I get any mileage from not using Global W/S, i.e. using it
'locally' within a method.

Actually within my code I try to keep any W/S down to zero in "Factory"
which usually kick-starts a program with invoke xyz "new" and store any
global W/S in the Object part of the class/program, which is where the
bread-and-butter stuff is being done.

As Bill says each re-use of a Local Storage is a 'refresh" and in OO
that means the method is "thrown away" after use. But that's wasteful
because you might reiterate on that method n times in a program/class.
So the compilers do cache your most frequent method requests - how, I
don't know, but some quick reference where they can recall from the
compiled source.

If you look at my OO examples, within a method I use both W/S and L/S
under certain circumstances - now whether or not the compiler treats
them as one and the same thing for a particular method I don't know.
However, think back to those humungous tables of variables we have in a
typically structured program - if I can place W/S items in a specific
method - say like the standard header-lines for a print report, and
assemble them there - programmer-wise I can focus on that function
clearly within the method, without doing Ctrl-Page-Up to see what I
called things up at the top of the source in Global W/S - and to me
that's a real plus, regardless of what the compiler actually does with
it.

At the method level whether or not you are referencing W/S or L/S for
'counters' - you will always be at an initial state. A 'counter' can
only be incremented ( i.e. previous-state + n ) at the Global level.
Back to my OO examples - I can use the Merant (part of future standard)
Level 78's either in method W/S or L/S with their constant values.

Local Storage is part of the new standard for structured also - so I'm
guessing it must function parallel to what I'm doing.

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bi4c2$4gb$1@news.inet.tele.dk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bhkj5$2pq$1@nntp9.atl.mindspring.net> <38DC67CA.EC97DA70@home.com>`

```
LS is for re-cursive calls.

A separate copy of local storage is made for each call. The lifetime of the
copy is equal to the call.

So, Local-Storage is a playground for recursive calls - and a good advice:
Kill the recursives when not needed any longer.

I just happened to know.

Regards
Ib
James J. Gavan skrev i meddelelsen <38DC67CA.EC97DA70@home.com>...
>
>
…[3 more quoted lines elided]…
>> Working-Storage and Local-Storage is totally "invisible" UNLESS you are
using
>> recursive programs (see the program-id paragraph in the LE  COBOL for
VSE).
>> In that case, local-storage is "fresh" for each occurrence - while
>> working-storage exists (more or less in "last used state") across
…[45 more quoted lines elided]…
>Jimmy
```

##### ↳ ↳ Re: working-storage vs. local-storage

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DD5D82.E99C229D@zip.com.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bhkj5$2pq$1@nntp9.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> I won't swear to it but BASICALLY, I think that the difference
…[45 more quoted lines elided]…
> > *Anyway*, please define local-storage for me.  Thanks.

The other not obvious thing is that local comes and goes with the
actual calls.  So if you want to a counter of every invocation of the
module you must use working storage because local keeps being
destroyed all the time.  Avoid local on MVS if you can, it does not
like allocation and free of memory.

I use the persistence of working storage with a first-time flag to
load up an in memory table for fast table lookup in a module.  If I
used local the table would be loaded with every call.

Frank

In case you need it,  your example is exactly correct from C to Cobol.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

#### ↳ Re: working-storage vs. local-storage

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bible$c0i$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net>`

```
In article <8bhkat$621$1@slb2.atl.mindspring.net>,
"Frank Swarbrick" <infocat@sprynet.com> wrote:
> I only know VS COBOL II (in the VSE environment), so I don't know
much about
> these new-fangled features. I've seen some reference to a local-
storage
> section.

Hi:

I'm sorry but I must be in a bad mood this morning.
IMO (My O is not H) it is stuff like this which makes programming
such a horrible mess. It isn't enough that the programmer has
to worry about the application, but when people who probably
never actually wrote a real application (the compilerwriters)
keep inventing stuff like this which then gets used, well, no
wonder the DP world is such a mess.

Do we REALLY NEED local-storage??? I don't think so.

I am sure that lots of people can come up with examples of
where it might be used, but they would have to be contrived.


Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: working-storage vs. local-storage

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bigoe$a9s$1@slb7.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com>`

```
Once you find the need for "recursive calls" (which COBOL has survived
without for years - but which does add some real functionality), then this is
a distinction that is required.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bku64$5j$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net>`

```
In article <8bigoe$a9s$1@slb7.atl.mindspring.net>,
"William M. Klein" <wmklein@nospam.netcom.com> wrote:
> Once you find the need for "recursive calls" (which COBOL has survived
> without for years - but which does add some real functionality), then
this is
> a distinction that is required.
>
> --
> Bill Klein

Hi:

I must live in some other world, but I have never found
the need for 'recursive calls', do not expect to, and don't
know what one is anyway.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8blaac$ofo$1@news.igs.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com>`

```
Foodman wrote in message <8bku64$5j$1@nnrp1.deja.com>...
>Hi:
>
…[5 more quoted lines elided]…
>
Is that a question or an answer?

I suspect that you never will find a use for recursive calls as long as you
do not know what they are.

I also expect that you will never find out what they are as long as you
think ignorance a virtue.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bniq8$oci$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com> <8blaac$ofo$1@news.igs.net>`

```
In article <8blaac$ofo$1@news.igs.net>,
"donald tees" <donald@willmack.com> wrote:
> I suspect that you never will find a use for recursive calls as long
as you
> do not know what they are.
>
> I also expect that you will never find out what they are as long as
you
> think ignorance a virtue.
>


Ignorance is bliss, especially when I never get calls at three am.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E0A0E9.E8E5C63F@istar.ca>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com> <8blaac$ofo$1@news.igs.net> <8bniq8$oci$1@nnrp1.deja.com>`

```
As someone who has dealt with COBOL since COBOL 63 on an RCA 301, I
believe that the constructs in the 1985 standard have enabled me to
write programs faster and more reliably (less testing and fewer
production problems).  I would like to be able to herd the various
standards committees into a room and tell them they can't leave until a
new standard is approved with all of the well defined parts in the
current proposal and with Bill Klein's objections properly handled. 
This is because I want true binary, usage bit and COPY ... REPLACING
LEADING ... plus I might use some of the other new things.  The three
features I mentioned would have been extremely useful in writing
business programs at my shop over 30 years ago on a 360 model 30.  In a
sense it speaks poorly for our community that it has taken this long for
them to be incorporated in the language.   

I have not used the recursion capabilities in the current COBOL for MVS
and VM compiler that was available at my previous contract but it was
nice to know they were there.

I highly recommend reading and learning the 1985 standard.  Your
programs will be cleaner and more efficient if you exploit the
capabilities that match the problems you are dealing with. 

Clark Morris, CFM Technical Programming Services Inc., cfmtech@istar.ca 

Foodman wrote:
> 
> In article <8blaac$ofo$1@news.igs.net>,
…[17 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000326113253.03047.00000130@nso-fw.aol.com>`
- **References:** `<8bku64$5j$1@nnrp1.deja.com>`

```
In article <8bku64$5j$1@nnrp1.deja.com>, Foodman <foodman123@aol.com> writes:

>I must live in some other world, but I have never found
>the need for 'recursive calls', do not expect to, and don't
>know what one is anyway.
>

I, myself, have never found it necessary to work with any type of 
recursion.  But I have seen internal sort logic that could make good
use of recursive logic.
I would say that any manually written binary search logic might be a
good candidate as well.   Having some really heavy techno-weenies 
around to find all the whiz-bang extensions and way-out logic algorithms
that can optimize a process is where I would see the 'recursion' thing
getting used the most.  
The day-to-day drudge workers are very un-likely to hit on the need to 
use this kind of logic, without it being provided from some advanced 
technical group.   I must face, on a daily basis, coaching some 'programmer
analysts' how to place even the simplest of logic into existing programs
without negtively impacting the existing program function.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DE5265.C745351B@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <8bigoe$a9s$1@slb7.atl.mindspring.net>,
…[14 more quoted lines elided]…
> 
Sorry - but I think that is where you have it completely WRONG - 'Can't
see need BUT don't know what it is about'.

My approach - I don't know SP2, DBs, SQL, ActiveX, Net stuff like HTML
etc. etc..... BUT I don't write them off because I don't know them.
Given time, I will study some of these as appropriate (allied to a
desktop) - THEN and only then will I make a judgement call as to whether
or not they have any relevance to me.

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bnjcm$ovp$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com> <38DE5265.C745351B@home.com>`

```
In article <38DE5265.C745351B@home.com>,
"James J. Gavan" <jjgavan@home.com> wrote:
>
> My approach - I don't know SP2, DBs, SQL, ActiveX, Net stuff like HTML
> etc. etc..... BUT I don't write them off because I don't know them.
> Given time, I will study some of these as appropriate (allied to a
> desktop) - THEN and only then will I make a judgement call as to
whether
> or not they have any relevance to me.
>
> Jimmy
>

Hi:

My application software was originally written in 1986 and thereafter.
It was MF DOS stuff. In order to survive, I had to convert to Windows.
In order to convert to Windows I HAD to learn SP2. Since I make
my living via my website, I HAD to learn HTML. So, when I come up
against some obstacle to my survival, I will learn whatever I need
to in order to survive.

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DF57CF.D9DA9BF3@zip.com.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> In article <8bigoe$a9s$1@slb7.atl.mindspring.net>,
> "William M. Klein" <wmklein@nospam.netcom.com> wrote:

> > Once you find the need for "recursive calls" (which COBOL has
> > survived without for years - but which does add some real
…[4 more quoted lines elided]…
> know what one is anyway.

Tony,

I have used simple recursion for parsing the last line of an address. 
If I did not have a complete line (suburb, state, and postcode) I
simply called myself again to continue the process.  There were other
ways to write it, it was simpler in logic terms and therefore code to
do that.

The problem hit with the following:

  xyz-paragraph.
	....
        if not finished
		perform xyz-paragraph
        end-if.

This worked for two iterations (one recursion) on MVS (i.e. 99.9% of
the time for my solution) when you hit it three times it never
returned to the caller, the recursion failed.

You may be using recursion without knowing about it.  Are you glad you
have this group for edification.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E06BE1.503D9F20@Azonic.co.nz>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com> <38DF57CF.D9DA9BF3@zip.com.au>`

```
Ken Foskey wrote:
> 
> The problem hit with the following:
…[9 more quoted lines elided]…
> returned to the caller, the recursion failed.

The above is invalid Cobol.  However a GO TO xyz-paragraph would have
worked as would an external PERFORM xyz-paragraph UNTIL finished (given
that the code was catering correctly for these).
 
> You may be using recursion without knowing about it.  Are you glad you
> have this group for edification.

If it is incompetently using recursion then you may find 
out that it is at 3am.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E09EF4.C80CB56B@zip.com.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com> <38DF57CF.D9DA9BF3@zip.com.au> <38E06BE1.503D9F20@Azonic.co.nz>`

```
Richard Plinston wrote:
> 
> Ken Foskey wrote:
…[15 more quoted lines elided]…
> (given that the code was catering correctly for these).

It is invalid on MVS cobol but it works on some PC cobol's (if not
all).  PC cobol is stack based in that the perform pointer is pushed
onto a stack.  MVS does not use a stack.

I did rewrite it to exactly what you said.  Obviously there was a lot
more code to restructure than just that though.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38df8a48.1602553125@news.cox-internet.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com>`

```
On Sun, 26 Mar 2000 12:01:10 GMT, Foodman <foodman123@aol.com> wrote:

>In article <8bigoe$a9s$1@slb7.atl.mindspring.net>,
>"William M. Klein" <wmklein@nospam.netcom.com> wrote:
…[13 more quoted lines elided]…
>

Here's one I use presently.  I have to port it to Fujitsu - which DOES
NOT YET support recursion at the program level.  You can get it with
OO, but not with "procedural" programming.  I do this in Realia
presently.

I have a record display.  A tree view of related records can be called
up.  In that view one can click on a record and call up the edit
screen.  I don't want to lose my original edit, or my place, so I
recursively call the edit program with parms from the other edit
program.  WS is NOT shared in Realia. (Meaning the program is NOT
re-entrant recursive, but instead just recursive) so I lose nothing.  

With Fujitsu, to get this behavior I need to have a second copy of the
program named something else.  With MicroFocus I would put all the
Working-Storage into Local Storage so as to not interfere with the
other running version.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v95vdscatu7q3qd32j29pgvrn35711ev80@4ax.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com>`

```
On Sun, 26 Mar 2000 12:01:10 GMT, Foodman <foodman123@aol.com> wrote:

>I must live in some other world, but I have never found
>the need for 'recursive calls', do not expect to, and don't
…[4 more quoted lines elided]…
>Tony Dilworth
Of course you do not expect to find the need for something that you don't know.....

A recursive function is something like this

FAC(0) := 1

FAC(n) := FAC(n-1) * N, for N > 1

If COBOL, you can program it like this to display the first 10 factorials
Of course, factorials can be more easily calculated using a dirct algorithm, but there are
other problems hich are more easily tackled using recursion:  Think about processing a
directory tree (or any tree of undetermined size, for that matter)

But as promised, here is the COBOL recirsion example.  (and if you are very advanturous,
look up the Ackerman function and try to
  a)  calculate ACK(5,5)  using an algorithm
  b)  calculate ACK(5,5) using recursion.

Have fun
       IDENTIFICATION DIVISION.
        PROGRAM-ID. FACMAIN.
       DATA DIVISION.
        WORKING-STORAGE SECTION.
         01 I                 PIC S9(4) BINARY VALUE 0.
         01 FAC-I             PIC S9(9) BINARY VALUE 0.
       PROCEDURE DIVISION.
           PERFORM VARYING I FROM 0 BY 1 UNTIL I > 10
              CALL 'FAC' USING I RETURNING FAC-I
              DISPLAY I '! =' FAC-I
           END-PERFORM
           GOBACK
           .
        END PROGRAM FACMAIN.

       IDENTIFICATION DIVISION.
        PROGRAM-ID. FAC IS RECURSIVE.
       DATA DIVISION.
        WORKING-STORAGE SECTION.
         01 Invokation-number PIC S9(9) BINARY VALUE 0.
        LOCAL-STORAGE SECTION.
         01 N-1               PIC S9(4) BINARY.
         01 Faculty-of-n-1    PIC S9(9) BINARY.
        Linkage Section.
         01 N                 PIC S9(4) BINARY.
         01 Faculty-of-n      PIC S9(9) BINARY.
       PROCEDURE DIVISION    USING N RETURNING Faculty-of-n.
           ADD 1 TO Invokation-number
           IF N = 0 THEN
              MOVE 1 TO Faculty-of-n
           ELSE
              SUBTRACT 1 FROM N GIVING N-1
              CALL 'FAC' USING N-1 RETURNING Faculty-of-n-1
              COMPUTE Faculty-of-n = n * Faculty-of-n-1
           END-IF
           GOBACK
           .
        END PROGRAM FAC.



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         What does CICS mean? - Can Improve Customer's Spirit
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8boe7p$n76$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com> <v95vdscatu7q3qd32j29pgvrn35711ev80@4ax.com>`

```
In article <v95vdscatu7q3qd32j29pgvrn35711ev80@4ax.com>,
vbandke@bsp-gmbh.com wrote:
>
> What does CICS mean? - Can Improve Customer's Spirit
>
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DFE2C8.4601C85A@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bigoe$a9s$1@slb7.atl.mindspring.net> <8bku64$5j$1@nnrp1.deja.com> <v95vdscatu7q3qd32j29pgvrn35711ev80@4ax.com>`

```


Volker Bandke wrote:
> 
> On Sun, 26 Mar 2000 12:01:10 GMT, Foodman <foodman123@aol.com> wrote:
…[7 more quoted lines elided]…
>          What does CICS mean? - Can Improve Customer's Spirit

AND ABOUT TIME TOO ! The cat is back :-)

Jimmy
```

##### ↳ ↳ Re: working-storage vs. local-storage

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<st5D4.7567$0o4.54457@iad-read.news.verio.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com>`

```
In article <8bible$c0i$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>In article <8bhkat$621$1@slb2.atl.mindspring.net>,
>"Frank Swarbrick" <infocat@sprynet.com> wrote:
…[14 more quoted lines elided]…
>Do we REALLY NEED local-storage??? I don't think so.

You've got *that* right... and hey, what about those whacky inline
PERFORMS, neh?  Nobody needed those from, when, 1962 onwards... what
changed *so* much that they just *can't* be done without *now*?  And
scope-delimiters... who needs those?  *Any* coder worth a paycheck can
trace down a nested IF, right?

Come to think of it... if nobody came up with a third-generation language
we'd all be programming in BAL, as the Pope intended... or still patching
boards with cords, as the Pope's Boss intended...

... pardon my sarcasm, Mr Dilworth, but I trust that it has made my point
clear; the arguments you have brought forth can be levelled against *any*
change (notice I did not use the word 'advance') in
technology.  MRI?  Pfah, exploratory surgery is good enough... after all,
there are these newfangled anaesthetics!

Now, if you'll excuse me, I need to code up some ALTERs, a few GO TO
DEPENDING ONs... and a couple o' 66 RENAMES, just to make sure such things
do not go softly into the Programmer's Graveyard.

DD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bkurk$od$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net>`

```

> ... pardon my sarcasm, Mr Dilworth, but I trust that it has made my
point
> clear; the arguments you have brought forth can be levelled against
*any* change.

---It is ridiculous to say that 'arguments. . can be levelled against
---ANY change'. Just come up with a good argument FOR changes.


> Now, if you'll excuse me, I need to code up some ALTERs, a few GO TO
> DEPENDING ONs... and a couple o' 66 RENAMES, just to make sure such
things
> do not go softly into the Programmer's Graveyard.

---What does ALTER, DEPENDING ON, etc. have to do with LOCAL-STORAGE?

---Remember, sarcasm is the lowest form of wit.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IXoD4.8535$0o4.59943@iad-read.news.verio.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <8bkurk$od$1@nnrp1.deja.com>`

```
In article <8bkurk$od$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>
>> ... pardon my sarcasm, Mr Dilworth, but I trust that it has made my point
…[3 more quoted lines elided]…
>---ANY change'.

That is an interesting assertion, Mr Dilworth... now, do you have anything
that resembles a reasoned argument to support it?

>Just come up with a good argument FOR changes.

That is very easy to do, Mr Dilworth... if you are capable of setting up
the qualifications for what 'good' is.  Take your time, of course; and
make it a sound structure.

>
>
…[4 more quoted lines elided]…
>---What does ALTER, DEPENDING ON, etc. have to do with LOCAL-STORAGE?

Those are techniques which were superseded by 'unnecessary' newer ones, Mr
Dilworth, just as LOCAL-STORAGE might supersede present techniques.

>
>---Remember, sarcasm is the lowest form of wit.

Remember, Mr Dilworth, that if this is the case I have been far more
generous than you appear to deserve.

DD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net>`

```
docdwarf@clark.net () wrote:

>>Do we REALLY NEED local-storage??? I don't think so.

>You've got *that* right... and hey, what about those whacky inline
>PERFORMS, neh?  Nobody needed those from, when, 1962 onwards... what
>changed *so* much that they just *can't* be done without *now*?  And
>scope-delimiters... who needs those?  *Any* coder worth a paycheck can
>trace down a nested IF, right?

the only time i have ever seen a recursive call of any use is in
building an indexing engine, or game trees.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NKpD4.8547$0o4.60216@iad-read.news.verio.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com>`

```
In article <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com>,
G Moore  <gvwmoore@spam.ix.netcom.com> wrote:
>docdwarf@clark.net () wrote:
>
…[9 more quoted lines elided]…
>building an indexing engine, or game trees.

And from this statement what might be concluded, Mr Moore... that the
language should contain consrtucts and possibilities that only you and Mr
Dilworth have seen to be useful or can be convinced of such?

DD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8blo6s$qjd$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net>`

```

>
> And from this statement what might be concluded, Mr Moore... that the
> language should contain consrtucts and possibilities that only you
and Mr
> Dilworth have seen to be useful or can be convinced of such?
>
> DD

Hi:

I have a partially-open mind. Why don't you go ahead and convince
Mr. Moore and I that local-storage and recursive calls are of
value to the COBOL programmer. Remembering that COBOL programmers
write BUSINESS APPLICATIONS and not games, etc.

IMO, there are two types of programmers: 1. Those who
get their kicks from developing applications in the simplest
way possible and who develop applications that don't need
'on-call' programmers at three in the morning, and, 2.
those who, at their employers' expense, use every weird
trick in the book to satisfy their technological ego and
wind up being on-call at three am.

As you might guess, I am a type-1 programmer.

Thanks

TOny Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DEA6A8.49B18B75@worldnet.att.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
(snip)
> 
> IMO, there are two types of programmers: 1. Those who
…[7 more quoted lines elided]…
> As you might guess, I am a type-1 programmer.

Do you think this post might be a little self-serving, even for USENET?

Bill Lynch
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bnht6$nfi$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <38DEA6A8.49B18B75@worldnet.att.net>`

```
In article <38DEA6A8.49B18B75@worldnet.att.net>,
wblynch@worldnet.att.net wrote:
> Foodman wrote:
> >
…[12 more quoted lines elided]…
> Do you think this post might be a little self-serving, even for
USENET?
>
> Bill Lynch


I just want people to know where I am coming from. Are you a type-1
or a type-2?

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DjzD4.8631$0o4.63269@iad-read.news.verio.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com>`

```
In article <8blo6s$qjd$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>
>>
…[10 more quoted lines elided]…
>value to the COBOL programmer.

It might be worth remembering, Mr Dilworth, that nowhere have you or Mr
Moore stated what you would consider to be a 'convincing argument'; I have
no desire to open fire at targets you can move, at will.  Mr Svalgaard has
posted a URL to code which uses recursion as best as the language
presently allows; I, for one, would not dream of saying '*I* cannot think
of it, therefore it cannot be done!'.

>Remembering that COBOL programmers
>write BUSINESS APPLICATIONS and not games, etc.

They do that *now*, Mr Dilworth, with the constructs which the language
presently supports.  Who knows what the future brings?

>
>IMO, there are two types of programmers: 1. Those who
…[7 more quoted lines elided]…
>As you might guess, I am a type-1 programmer.

There is a difference between developing KISS code, in which I believe
most strongly, and slavishly adhering to the familiar path, which you seem
to be advocating.  As for Type I versus Type II programmers, you might
deign to check out:

<http://www.deja.com/=dnc/[ST_rn=ps]/qs.xp?ST=PS&svcclass=dnyr&QRY=%2Blook+%28%2Bma+OR+%2BMom%29+%2Bprogrammer&defaultOp=AND&DBS=1&OP=dnquery.xp&LNG=ALL&subjects=&groups=comp.lang.cobol&authors=&fromdate=&todate=&showsort=date&maxhits=100>

... and see who has been saying what about for a while.

(note to the amused and bemused... while searching for the above I came
across:

<http://x44.deja.com/=dnc/[ST_rn=ps]/getdoc.xp?AN=456766496&search=thread&CONTEXT=954121896.1644036102&HIT_CONTEXT=954121896.1644036102&HIT_NUM=6&hitnum=22>

... which lead me back to:

<http://x44.deja.com/=dnc/[ST_rn=ps]/getdoc.xp?AN=456654114&search=thread&CONTEXT=954121896.1644036102&HIT_CONTEXT=954121896.1644036102&HIT_NUM=6&hitnum=20>

... which contains:

--begin quoted text:

>Other may prefer programming languages with more modern 
>constructs.

Others may, sure... but let them *try* to get some code past a review and
implemented into Prod!

'What is *this* stuff?  EVALUATE TRUE WHEN cond-1 imperative statement...
you call this COBOL?!?'

'Oh, please, Mr Standards-and-Practises Reviewmeister, it is exactly what
is allowed by the ANSI '85 Standard.'

'ANSI '85?  Crap, I *knew* things were goin' ta hell in a handbasket when
we allowed them fancy ANSI '74 constructs in a couple a' years back...
look, 1985 is only 14 years ago, we oughta wait until the technology is
Really Proven before we implement it.  Go back and rewrite this in *real*
COBOL, then try again.'

--end quoted text

... once again proving that, at times, the Digressions are the best part
of the process)

Please, Mr Dilworth, be so kind as to 'share' with the group, here... when
was the last time you learned something new *and* 'useful' (by your
definitions, of course) about COBOL?

DD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bnho9$n85$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <DjzD4.8631$0o4.63269@iad-read.news.verio.net>`

```
In article <DjzD4.8631$0o4.63269@iad-read.news.verio.net>,
docdwarf@clark.net () wrote:
> Please, Mr Dilworth, be so kind as to 'share' with the group, here...
when
> was the last time you learned something new *and* 'useful' (by your
> definitions, of course) about COBOL?
>
> DD
>

I am sorry to be so annoying but I just think that there is so much
hogwash in the programming world.  To be honest, I haven't learned
anything new and useful about COBOL in years and I don't make the
attempt. Since I work for myself, I must have a very high degree
of portability and that makes me stick to the basics which serve
my needs perfectly.

With head in sand. . .

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JdJD4.8904$0o4.65422@iad-read.news.verio.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8blo6s$qjd$1@nnrp1.deja.com> <DjzD4.8631$0o4.63269@iad-read.news.verio.net> <8bnho9$n85$1@nnrp1.deja.com>`

```
In article <8bnho9$n85$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>In article <DjzD4.8631$0o4.63269@iad-read.news.verio.net>,
>docdwarf@clark.net () wrote:
…[8 more quoted lines elided]…
>hogwash in the programming world.

Not to worry overmuch, Mr Dilworth; I, among others, have been called
'annoying' and I agree that there is much hogwash and fad-of-the-week, as
well.

>To be honest, I haven't learned
>anything new and useful about COBOL in years and I don't make the
>attempt.

This seems to be in accord with the view you've presented, aye.

>Since I work for myself, I must have a very high degree
>of portability and that makes me stick to the basics which serve
>my needs perfectly.

Ahhhh... there are all manner of Admonishing Aphorisms about such
a... balanced existence, such as 'Shoemaker, stick to your last' and 'The
worm in horseradish thinks his life is the sweetest'; these, of course,
are countered with 'What a Wonderful World it is that has new things to
learn in it!'

>
>With head in sand. . .

I would suggest caution, Mr Dilworth; such a posture can leave other
portions of one's anatomy vulnerable to... sophisticated assaults.

DD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DF5C0F.CA4F2B6E@zip.com.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <DjzD4.8631$0o4.63269@iad-read.news.verio.net> <8bnho9$n85$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> I am sorry to be so annoying but I just think that there is so much
…[7 more quoted lines elided]…
> 
Tony

I agree, there is a lot of hogwash in programming.  To assume ALL is
hogwash is to not take the 'best practice' from many options.  

For example:  OO shows great promise, like structured in the 70's it
is considered heresy by the traditionalists.  Will it be an end result
of only a stepping stone to something better, I personally do not
know.  I can tell you I have followed OO for many years and only after
much investigation will I firmly say 'Yes, OO is a good thing'.  OO is
not so much for program code so much as the design elements, these
work hand in hand.  Without good design programming is simply hacking.

I read several books a year and by this I have learned to view the
world as a sceptic.  My scepticism can be over come.  If I build a
wall why bother even looking.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EqMD4.9093$0o4.66909@iad-read.news.verio.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <DjzD4.8631$0o4.63269@iad-read.news.verio.net> <8bnho9$n85$1@nnrp1.deja.com> <38DF5C0F.CA4F2B6E@zip.com.au>`

```
In article <38DF5C0F.CA4F2B6E@zip.com.au>,
Ken Foskey  <waratah@zip.com.au> wrote:

[snippage]

>I read several books a year and by this I have learned to view the
>world as a sceptic.

... and that is for absolutely sure?

DD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.134a88ef4324daa89899e9@news.mersinet.co.uk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <DjzD4.8631$0o4.63269@iad-read.news.verio.net> <8bnho9$n85$1@nnrp1.deja.com> <38DF5C0F.CA4F2B6E@zip.com.au>`

```
I noticed that Ken Foskey as waratah@zip.com.au said...
> 
> I agree, there is a lot of hogwash in programming.  To assume ALL is
> hogwash is to not take the 'best practice' from many options.  

I have a heavy degree of scepticism when "new" methodologies come around 
that is maybe based on experience of evangelical crusades in the 70s and 
80s and their general failure to make improvements.  All of my programs 
are structured, not so-called "structured", but they have a clear logical 
path by which the solution is achieved and contain sufficient comment to 
tell the story along the way.
 
> For example:  OO shows great promise, like structured in the 70's it
> is considered heresy by the traditionalists.  Will it be an end result
…[4 more quoted lines elided]…
> work hand in hand.  Without good design programming is simply hacking.

I'm not entirely convinced by OO but acknowledge that it does seem to 
provide a genuine framework by which genuine results can be achieved.  
However, as mentioned in another thread, it needs to be an installation-
wide transition because the structural concepts are quite differently 
implemented than with traditional code.

BTW I do like the XP ideas as they reflect very much what happened on a 
most enjoyable high-intensity project that I was engaged on a few years 
ago - it seems we were using XP before it had been invented.  It isn't 
often, though, that you get that sort of user commitment.
 
> I read several books a year and by this I have learned to view the
> world as a sceptic.  My scepticism can be over come.  If I build a
> wall why bother even looking.

I'm currently re-reading "Grunts" by Mary Gentle.  Though I have little 
idea what this has to do with programming, I'm always willing to learn.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com>`

```
"Foodman" <foodman123@aol.com> wrote in message
news:8blo6s$qjd$1@nnrp1.deja.com...
>
> >
…[13 more quoted lines elided]…
>

OK - start with the fact that the business programs that ARE written in
Standard COBOL today are (by definition) without recursion (because it is
explicitly dis-allowed in the '85 Standard).  Therefore, what you are looking
for is some BUSINESS application that cannot be written (or cannot be written
easily) in COBOL.

Two examples where recursion (and recursive programming languages) are
absolutely required are:

  Weather forecasting
  Oil/Mineral ground/resource analsysis

Both of those are "real world" business applications that require the type of
mathmatics that MUST use recursive logic.  I won't go into the type of logic
that they use (most of which is WELL beyond me) - but with recurssion it
would (theoretically) be able to do that type of business programming in
COBOL - without it, it would be impossible.

The bottom-line is that IF all you want to do is write programs that do
exactly the same TYPE of thing that your current business programs do, then
you probably will never need recursion.  If, on the other hand, you want to
do some business programs that have never been given to COBOL programmers,
then recurssion MAY make this possible.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38df5bd7_4@news3.prserv.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net>`

```

William M. Klein <wmklein@nospam.netcom.com> wrote in message
> > I have a partially-open mind. Why don't you go ahead and convince
> > Mr. Moore and I that local-storage and recursive calls are of
…[6 more quoted lines elided]…
> explicitly dis-allowed in the '85 Standard).  Therefore, what you are
looking
> for is some BUSINESS application that cannot be written (or cannot be
written
> easily) in COBOL.

Bill, as I have repeatedly shown, recursion CAN be done even in COBOL
74 or older. Guess what, you can even do it in assembler. The extra
housekeeping (return stack and local variables) is not difficult. In any
realistic application the machinery for recursion is such a small part
of the whole as to be insignificant.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E06A71.7416D504@Azonic.co.nz>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net>`

```
Leif Svalgaard wrote:
> 
> Bill, as I have repeatedly shown, recursion CAN be done even in COBOL
> 74 or older. 

I would challenge you to do it in an implementation of Cobol 74 that I
have here.  In fact you are most likely _NOT_ saying that it can be done
in 'Cobol 74', but in a particular implementation of Cobol 74 that
includes
extensions.

> Guess what, you can even do it in assembler. 

What a relief that it doesn't have to be coded by using the bit switches
on 
the console.

> The extra
> housekeeping (return stack and local variables) is not difficult. In any
> realistic application the machinery for recursion is such a small part
> of the whole as to be insignificant.

The whole issue of recursion is usually insignificant.  Anything that
can be
done with a recursive algoritm can be done with an iteritive one, and
usually
faster (due to being able to control the overheads).

However a related topic, re-entrancy, can be significant, such as when
writing
Windows API programs.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e00705_1@news3.prserv.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net> <38E06A71.7416D504@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:38E06A71.7416D504@Azonic.co.nz...
> Leif Svalgaard wrote:
> >
…[7 more quoted lines elided]…
> extensions.

1. Towers of Hanoi
In a monastery in Hanoi there are three diamond rods. God placed 64 gold
disks of different sizes - each with a central hole- on rod number 1 such
that the largest disk is at the bottom of the stack and the smallest disk is
on top. The monks' mission is to move all the disks onto rod number 2. Only
one disk may be moved at a time and never may a larger disk be placed on a
smaller one. If needed, disks may temporarily be placed on the third rod,
again in such a manner that no larger disk rests on a smaller one.
This classical problem can be solved by a recursive procedure that first
moves all disks except the last one from the source rod to the spare rod,
then moves the last - and largest - disk from the source rod to its final
position on the destination rod, and finally moves all disks from the spare
rod to the destination rod. Moving N-1 disks is then performed in the same
manner recursively until all disks have been moved:

               BEGIN INTEGER M;

                  PROCEDURE MOVE (N, SOURCE, DEST, SPARE);
                  INTEGER N; STRING SOURCE, DEST, SPARE;
                  BEGIN
                     IF N > 1 THEN MOVE (N-1, SOURCE, SPARE, DEST);
                     WRITE (OUT, "MOVE DISK ", N,
                                   " FROM ", SOURCE,
                                    " TO " ,  DEST);
                     IF N > 1 THEN MOVE (N-1, SPARE, DEST, SOURCE)
                  END;

                  WRITE (OUT, "NBR OF DISKS = "); READ (IN, M);
                  IF M > 0 THEN MOVE (M, "SOURCE", "DEST", "SPARE")
               END

The COBOL version of the program follows below. As we wish to illustrate
pseudo-recursion rather than input/output, we exceptionally tolerate a
non-portable program that uses ACCEPT and DISPLAY. The program counter is
explicitly managed with the variable WHAT-TO-DO and parameters (which are in
a sense local to each invocation of the procedure) are stacked along with
the program counter. The call of the procedure in the main program is
simulated by stacking the first set of parameters.
             000100 IDENTIFICATION DIVISION.
             000200 PROGRAM-ID.    HANOI.
             000300
             000400 AUTHOR.        LEIF SVALGAARD.
             000500 DATE-WRITTEN.  91/04/22
             000600     -REVISED:  91/05/01.
             000700
             000800 ENVIRONMENT DIVISION.
             000900
             001000 CONFIGURATION SECTION.
             001100 SOURCE-COMPUTER. ALMOST-PORTABLE.
             001200 OBJECT-COMPUTER. ALMOST-PORTABLE.
             001300
             001400 DATA DIVISION.
             001500
             001600 WORKING-STORAGE SECTION.
             001700
             002000 01  STACK-SPACE.
             002100     02  STACK-PTR               PIC S9(3)  COMP.
             002200     02  STACK-ITEM                         OCCURS 64.
             002300         03  DISK-NBR            PIC 9(2).
             002400         03  SOURCE-ROD          PIC X(6).
             002500         03  DEST-ROD            PIC X(6).
             002600         03  SPARE-ROD           PIC X(6).
             002700         03  WHAT                PIC 9(1).
             002800
             002900 01  LOCAL-VARIABLES.
             003000     02  THE-DISK-NBR            PIC 9(2).
             003100     02  THE-SOURCE-ROD          PIC X(6)   VALUE
"SOURCE".
             003200     02  THE-DEST-ROD            PIC X(6)   VALUE "DEST".
             003300     02  THE-SPARE-ROD           PIC X(6)   VALUE
"SPARE".
             003400     02  THE-WHAT                PIC 9(1).
             003500
             003600 01  GLOBAL-VARIABLES.
             003700     02  SWAP-ROD                PIC X(6).
             003800     02  WHAT-TO-DO              PIC 9(1).
             003900
             004000 PROCEDURE DIVISION.
             004100 BEGIN-PROGRAM.
             004200     DISPLAY "NBR OF DISKS = " NO ADVANCING
             004300     ACCEPT THE-DISK-NBR
             004400
             004500     IF THE-DISK-NBR > ZERO
             004600         MOVE 1 TO STACK-PTR, WHAT-TO-DO
             004700         MOVE LOCAL-VARIABLES TO STACK-ITEM (1)
             004800         PERFORM MOVE-DISK
             004900           UNTIL STACK-PTR = ZERO
             005000     .
             005100     STOP RUN
             005200     .
             005300
             005400 MOVE-DISK.
             005500     MOVE STACK-ITEM (STACK-PTR) TO LOCAL-VARIABLES
             005600     IF WHAT-TO-DO = 1
             005700         PERFORM MOVE-DISKS-AWAY
             005800     ELSE
             005900     IF WHAT-TO-DO = 2
             006000         PERFORM SHOW-DISK-MOVED
             006100     ELSE
             006200     IF WHAT-TO-DO = 3
             006300         PERFORM MOVE-DISKS-BACK
             006400     ELSE
             006500         MOVE WHAT (STACK-PTR) TO WHAT-TO-DO
             006600         SUBTRACT 1 FROM STACK-PTR
             006700     .
             006800
             006900 MOVE-DISKS-AWAY.
             007000     MOVE THE-SPARE-ROD TO SWAP-ROD
             007100     MOVE THE-DEST-ROD  TO THE-SPARE-ROD
             007200     MOVE SWAP-ROD      TO THE-DEST-ROD
             007300     PERFORM MOVE-THE-DISKS
             007400     .
             007500
             007600 MOVE-THE-DISKS.
             007700     ADD 1 TO WHAT-TO-DO
             007800     IF THE-DISK-NBR > 1
             007900         SUBTRACT 1 FROM THE-DISK-NBR
             008000         MOVE WHAT-TO-DO TO THE-WHAT
             008100         ADD 1 TO STACK-PTR
             008200         MOVE LOCAL-VARIABLES TO STACK-ITEM (STACK-PTR)
             008400     .
             008500
             008600 SHOW-DISK-MOVED.
             008700     ADD 1 TO WHAT-TO-DO
             008800     DISPLAY "MOVE DISK " THE-DISK-NBR
             008900               " FROM "   THE-SOURCE-ROD
             009000                " TO "    THE-DEST-ROD
             009100     .
             009200
             009300 MOVE-DISKS-BACK.
             009400     MOVE THE-SPARE-ROD  TO SWAP-ROD
             009500     MOVE THE-SOURCE-ROD TO THE-SPARE-ROD
             009600     MOVE SWAP-ROD       TO THE-SOURCE-ROD
             009700     PERFORM MOVE-THE-DISKS
             009800     .
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E01E06.9F0A5109@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net> <38E06A71.7416D504@Azonic.co.nz> <38e00705_1@news3.prserv.net>`

```


Leif Svalgaard wrote:
> 
> 1. Towers of Hanoi
> In a monastery in Hanoi there are three diamond rods. God placed 64 gold
> disks of different sizes - each with a central hole- on rod number 1 such etc...

Thanks Leif. Now I just wonder why I prefer your version to the cryptic
version I find in Win 32 Programming - Rector & Newcomer - no I haven't
copied it in here - there is just too much - 21 c, h, rc, res, makefiles
etc. in a sub-folder ! I'll be a little gentle with them though - they
do include the Windows API jazz.

(Leif's version '91, theirs '96 - No Mr. Microsoft, Leif didn't need
Windows to figure it out).

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.134abcddcd9f31899899f9@news.mersinet.co.uk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net> <38E06A71.7416D504@Azonic.co.nz> <38e00705_1@news3.prserv.net>`

```
I noticed that Leif Svalgaard as lsvalg@ibm.net said...
> 
> Richard Plinston <riplin@Azonic.co.nz> wrote in message
…[12 more quoted lines elided]…
> 1. Towers of Hanoi

Oh, bollocks.  I'm fed up with ridiculous illustrations of points that 
have little or no bearing on the commercial environment that is COBOL's 
natural home.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 11)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e0b66b_1@news3.prserv.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net> <38E06A71.7416D504@Azonic.co.nz> <38e00705_1@news3.prserv.net> <MPG.134abcddcd9f31899899f9@news.mersinet.co.uk>`

```
Charles F Hankel <charles@hankel.mersinet.co.uk> wrote in message
news:MPG.134abcddcd9f31899899f9@news.mersinet.co.uk...
> I noticed that Leif Svalgaard as lsvalg@ibm.net said...
> >
…[4 more quoted lines elided]…
> > > > Bill, as I have repeatedly shown, recursion CAN be done even in
COBOL
> > > > 74 or older.
> > >
> > > I would challenge you to do it in an implementation of Cobol 74 that I
> > > have here.  In fact you are most likely _NOT_ saying that it can be
done
> > > in 'Cobol 74', but in a particular implementation of Cobol 74 that
> > > includes
…[6 more quoted lines elided]…
> natural home.

Charles, the reason silly little things like 'the towers of Hanoi' are
used is to show the point without being lengthy. It is hard to be
more realistic without using a lot of bandwith. But, since you raised
thpoint, here is a more realistic example. Don't worry that it also
calls various subrotines and uses something called a 'dialog'
These are things real applications might do. The example
shows how to analyze a tree of called programs. Similar
solutions could be used for any hierarchial data and business
has a lot of that kind. So, apologizing for the size of this,
there goes:

2. Structure Analyser

This tool prints out the structure of programs called in an application.
This structure resembles a tree, with the root being the main program.  A
typical call tree looks like this:

CALC
`------ CALCPK
        `------ MATHPK

As we look at the design of this tool, we shall see how to use complex
lists, stacks, and pseudo-recursive programming to solve a real problem.

a. General Design
The basic problem is broken into two pieces: first build the call tree, then
print it out.  Both of these problems can be attacked in a recursive manner:

 � To build the tree: start with the root program.  Attach this to the tree,
and look for all CALL statements in the source code.  For each of these
called programs, repeat the process.

 � To print the tree: start with the root of the tree.  Print the program's
name and look at the list of called programs.  For each of these, repeat the
process.

The `tree' structure will be a complex linked-list where each program points
to a doubly-linked list of called programs:

 +------+    +---------+
(� head �====� program �)
 +------+    +---------+
                  |
                  |
               +------+    +---------+    +---------+
              (� head �====� program �====� program �)
               +------+    +---------+    +---------+
                               |               :
                               |
                            +------+    +---------+    +---------+
                           (� head �====� program �====� program �)
                            +------+    +---------+    +---------+
                                            |              |
                                            |              |
                                         +------+       +------+
                                        (� head �)     (� head �)
                                         +------+       +------+

This is a slight simplification of the fully-general complex list, since a
node can have only a single sub-list.  Thus, rather than using a
doubly-linked list between `program' and `head', we use a single pointer.
When a program calls no others, the head points to itself, signifying an
empty list.

b. The Main Data Structures

The main data structure is adapted from the doubly-linked list described
previously.  The nodes contain an extra pointer, NODE-CHILD, which points to
the sub-list of called programs.  We also define some extra pointers such as
PARENT-NODE and CHILD-HEAD for use in the program:

003900 01  LIST-POINTERS.
91/02/09
004000     02  EMPTY-PTR               PIC S9(3)  COMP  VALUE ZERO.
91/02/09
004100     02  FREE-POOL               PIC S9(3)  COMP  VALUE +1.
91/02/09
004200     02  LIST-HEAD               PIC S9(3)  COMP  VALUE +2.
91/02/09
004300     02  FIRST-NODE              PIC S9(3)  COMP  VALUE +3.
91/02/09
004400     02  LAST-NODE               PIC S9(3)  COMP  VALUE +998.
91/02/09
004500     02  NODE-NBR                PIC S9(3)  COMP.
91/02/09
004600     02  LIST-PTR                PIC S9(3)  COMP.
91/02/09
004700     02  PREV-PTR                PIC S9(3)  COMP.
91/02/09
004800     02  NEXT-PTR                PIC S9(3)  COMP.
91/02/09
004900     02  PARENT-NODE             PIC S9(3)  COMP.
91/02/09
005000     02  CHILD-HEAD              PIC S9(3)  COMP.
91/02/09
005100
91/02/09
005200 01  LIST-NODES.
91/02/09
005300     02  LIST-NODE                          OCCURS 998 TIMES.
91/02/09
005400         03  NODE-PREV           PIC S9(3)  COMP.
91/02/09
005500         03  NODE-NEXT           PIC S9(3)  COMP.
91/02/09
005600         03  NODE-CHILD          PIC S9(3)  COMP.
91/02/09
005700         03  NODE-NAME           PIC X(8).
91/02/09

A separate structure holds a table of all known programs.  Before looking in
detail at a program, we look in this table, so that a program will not be
analyzed twice (this keeps the resulting call tree simpler).  We use an
extra entry in the table to act as a sentinel:

006000 01  PROGRAM-TABLE.
91/02/09
006100     02  PROGRAM-COUNT           PIC S9(3)  VALUE ZERO COMP.
91/02/09
006200     02  PROGRAM-MAX             PIC S9(3)  VALUE +100 COMP.
91/02/09
006300     02  PROGRAM-NAME            PIC X(8)   OCCURS 101 TIMES.
91/02/09
006400
91/02/09

A stack of requests will drive the pseudo-recursive code.  The stack holds
local data needed by the `build' and `print' algorithms:

006600 01  REQUEST-STACK.
91/02/09
006700     02  STACK-PTR               PIC S9(3)            COMP.
91/02/09
006800     02  STACK-MAX               PIC S9(3)  VALUE +100 COMP.
91/02/09
006900     02  STACK-ENTRY                        OCCURS 100 TIMES.
91/02/09
007000         03  STACK-TOKEN         PIC X(8).
91/02/09
007100         03  STACK-NODE          PIC S9(3)  COMP.
91/02/09
007200         03  STACK-LEVEL         PIC S9(3)  COMP.
91/02/09

We initialize these data structures as follows:

051800 INIT-DATA-STRUCTURES.
91/02/09
051900     MOVE ZERO TO PROGRAM-COUNT
91/02/09
052000     PERFORM INIT-LINKED-LIST
91/02/09
052100     .
91/02/09
052200
91/02/09
052300 INIT-LINKED-LIST.
91/02/09
052400     MOVE LIST-HEAD TO LIST-PTR
91/02/09
052500     PERFORM CLEAR-THE-LIST
91/02/09
052600     MOVE FREE-POOL TO LIST-PTR
91/02/09
052700     PERFORM CLEAR-THE-LIST
91/02/09
052800
91/02/09
052900     PERFORM ATTACH-NODE-TO-LIST
91/02/09
053000       VARYING NODE-NBR FROM FIRST-NODE BY 1
91/02/09
053100         UNTIL NODE-NBR > LAST-NODE
91/02/09
053200     .
91/02/09
053300
91/02/09
053400 CLEAR-THE-LIST.
91/02/09
053500     MOVE LIST-PTR TO NODE-NEXT (LIST-PTR)
91/02/09
053600                      NODE-PREV (LIST-PTR)
91/02/09
053700     .
91/02/09
053800
91/02/09

Note how the LAST-NODE cannot have a value of 999 when NODE-NBR has a
picture like S9(3) because of the overflow of NODE-NBR when it reaches 999.
This subtle error will not occur if computational values are stored
internally as binary numbers with a range larger than 999, so we have here
the potential for a non-portable bug that will strike on some systems, but
not on others.

Attaching a node to a list is straight-forward once the list has been
initialized to empty (i.e. pointing to itself):

053900 ATTACH-NODE-TO-LIST.
91/02/09
054000     MOVE NODE-PREV (LIST-PTR) TO PREV-PTR
91/02/09
054200     MOVE LIST-PTR TO NODE-NEXT (NODE-NBR)
91/02/09
054300     MOVE NODE-NBR TO NODE-NEXT (PREV-PTR)
91/02/09
054400     MOVE PREV-PTR TO NODE-PREV (NODE-NBR)
91/02/09
054500     MOVE NODE-NBR TO NODE-PREV (LIST-PTR)
91/02/09
054600     .
91/02/09

c. The Program's Dialog

Most of the dialog is concerned with the `build' algorithm.  The request
stack is initialized to contain a single request, i.e. to parse the root
program.  The main dialog loop gets the next request off the stack and
parses the program specified.  An inner loop reads each line of source code;
whenever it finds a CALL statement, it stacks a request to parse the called
program.  This continues until the request stack is empty:

 .-------------------.
( AFTER-INIT          )
!`-------------------'
!
.-------------------.
( OK              )- - - - - - - - - - - - - - - - - ->
REQUEST        )
!                    ( GET-THE-PARAMETERS            )
`-------------------'
!                    ( INITIALISE-REQUEST-STACK      )
!                    ( GET-NEXT-REQUEST              )
!
.-------------------.
( ERROR           )- - - - - - - - - - - - - - - - - ->
 )
                     ( TERMINATE-THE-PROGRAM         )
`-------------------'

 .-------------------.
( HAVE-REQUEST        )
!`-------------------'
!
.-------------------.
( OK              )- - - - - - - - - - - - - - - - - ->
ECORD         )
!                    ( CHECK-PROGRAM-NOT-KNOWN       )
`-------------------'
!                    ( OPEN-SOURCE-FILE              )
!                    ( GET-NEXT-RECORD               )
!                    ( CLASSIFY-THE-RECORD           )
!
.-------------------.
( NO-MORE         )- - - - - - - - - - - - - - - - - ->
 )
!                    ( PRINT-PROGRAM-STRUCTURE       )
`-------------------'
!                    ( TERMINATE-THE-PROGRAM         )
!
.-------------------.
( EXCEPTION       )- - - - - - - - - - - - - - - - - ->
REQUEST        )
                     ( GET-NEXT-REQUEST              )
`-------------------'

 .-------------------.
( HAVE-RECORD         )
!`-------------------'
!
.-------------------.
( CALL-STATEMENT  )- - - - - - - - - - - - - - - - - ->
ECORD         )
!                    ( STORE-CALLED-PROGRAM          )
`-------------------'
!                    ( GET-NEXT-RECORD               )
!                    ( CLASSIFY-THE-RECORD           )
!
.-------------------.
( OTHER           )- - - - - - - - - - - - - - - - - ->
ECORD         )
!                    ( GET-NEXT-RECORD               )
`-------------------'
!                    ( CLASSIFY-THE-RECORD           )
!
.-------------------.
( NO-MORE         )- - - - - - - - - - - - - - - - - ->
REQUEST        )
                     ( CLOSE-SOURCE-FILE             )
`-------------------'
                     ( GET-NEXT-REQUEST              )

 .-------------------.
( DEFAULTS            )
!`-------------------'
!
.-------------------.
( EXCEPTION       )- - - - - - - - - - - - - - - - - ->
 )
                     ( TERMINATE-THE-PROGRAM         )
`-------------------'

d. Getting the Parameters

Like all batch programs, STRUCT gets its parameters through PARMPK.  In this
case, it expects a single filename, with no switches or other controls:

012700 01  PARMPK-CONTROL.
91/02/09
012800     02  PARMPK-TASK-ID          PIC X(4).
91/02/09
012900     02  PARMPK-OPERATION        PIC X      VALUE "G".
91/02/09
013000     02  PARMPK-FEEDBACK         PIC X.
91/02/09
013100     02  PARMPK-FILENAME         PIC X(8)   VALUE "STRUCT".
91/02/09
013200
91/02/09
013300 01  PARMPK-DATA.
91/02/09
013400     02  PARMPK-COUNT            PIC S9(3)  COMP.
91/02/09
013500     02  PARMPK-VALUES                      VALUE SPACES.
91/02/09
013600         03  PARAM-FILENAME      PIC X(8)   OCCURS 64 TIMES.
91/02/09
013700     02  PARMPK-SWITCH-DATA.
91/02/09
013800         03  SWITCH-LIST.
91/02/09
013900             04  FILLER          PIC X(64)  VALUE SPACES.
91/02/09
014000         03  SWITCH-CONTROL.
91/02/09
014100             04  FILLER          PIC X(8)   VALUE SPACES.
91/02/09
014200         03  SWITCH-VALUES.
91/02/09
014300             04  FILLER          PIC X(64)  VALUE SPACES.
91/02/09

To get the parameters we call PARMPK:

055400 GET-THE-PARAMETERS.
91/02/09
055500     CALL "PARMPK"
91/02/09
055600         USING PARMPK-CONTROL
91/02/09
055700               PARMPK-DATA
91/02/09
055800
91/02/09
055900     IF PARMPK-FEEDBACK > SPACE
91/02/09
056000         MOVE "PARAMETER FILE `STRUCT' NOT FOUND" TO DISPLAY-DATA
91/02/09
056100         PERFORM RAISE-THE-EXCEPTION
91/02/09
056200     .
91/02/09
056300
91/02/09
056400 RAISE-THE-EXCEPTION.
91/02/09
056500     PERFORM RAISE-EXCEPTION
91/02/09
056600     PERFORM DISPLAY-THE-MESSAGE
91/02/09
056700     .
91/02/09
056800
91/02/09
056900 RAISE-EXCEPTION.
91/02/09
057000     MOVE      "YES"      TO EXCEPTION-RAISED
91/02/09
057100     MOVE EXCEPTION-EVENT TO THE-EXCEPTION-EVENT
91/02/09
057200     .
91/02/09
057300
91/02/09
057400 DISPLAY-THE-MESSAGE.
91/02/09
057500     CALL "DISPPK"
91/02/09
057600         USING DISPLAY-CONTROL
91/02/09
057700               DISPLAY-DATA
91/02/09
057800     .
91/02/09

e. Building the Call Tree

Each time a request to parse a program is taken from the stack, the program
specified is attached somewhere to the call tree.  This `somewhere' is
always the head of appropriate list.  We attach the root program to
LIST-HEAD:

058200 INITIALISE-REQUEST-STACK.
91/02/09
058300     MOVE 1 TO STACK-PTR
91/02/09
058400     MOVE PARAM-FILENAME (1) TO STACK-TOKEN (STACK-PTR)
91/02/09
058500     MOVE LIST-HEAD          TO STACK-NODE  (STACK-PTR)
91/02/09
058600     .
91/02/09

Note, that we assume that at least one parameter is always present
(PARAM-FILENAME (1)).  This should be checked by the procedure that invokes
the structure analyzer, so there is no need for checking it again here.

If there are no more requests, the NO-MORE-EVENT is signaled.  Otherwise,
the top request is taken off the stack, and two nodes are attached: one to
hold the program, and one to act as the head for the list of called
programs, if any.  This head is always immediately attached, to simplify the
general algorithm:

059000 GET-NEXT-REQUEST.
91/02/09
059100     IF STACK-PTR > ZERO
91/02/09
059200         MOVE STACK-TOKEN (STACK-PTR) TO THE-TOKEN
91/02/09
059300         MOVE STACK-NODE  (STACK-PTR) TO LIST-PTR
91/02/09
059400         SUBTRACT 1 FROM STACK-PTR
91/02/09
059500         PERFORM ATTACH-PROGRAM-NAME-TO-LIST
91/02/09
059600         PERFORM ATTACH-PROGRAM-CHILD-HEAD
91/02/09
059700         PERFORM SET-OK
91/02/09
059800     ELSE
91/02/09
059900         MOVE NO-MORE-EVENT TO THE-NEXT-EVENT
91/02/09
060000     .
91/02/09
060100
91/02/09
060200 ATTACH-PROGRAM-NAME-TO-LIST.
91/02/09
060300     PERFORM GET-NODE-FROM-FREE-POOL
91/02/09
060400     IF NODE-NBR NOT = FREE-POOL
91/02/09
060500         PERFORM ATTACH-NODE-TO-LIST
91/02/09
060600         MOVE THE-TOKEN TO NODE-NAME (NODE-NBR)
91/02/09
060700         MOVE NODE-NBR  TO PARENT-NODE
91/02/09
060800     .
91/02/09
060900
91/02/09
061000 GET-NODE-FROM-FREE-POOL.
91/02/09
061100     MOVE NODE-NEXT (FREE-POOL) TO NODE-NBR
91/02/09
061200     PERFORM REMOVE-NODE-FROM-LIST
91/02/09
061300     IF NODE-NBR = FREE-POOL
91/02/09
061400         MOVE "PROGRAM STRUCTURE IS TOO COMPLEX" TO DISPLAY-DATA
91/02/09
061500         PERFORM RAISE-THE-EXCEPTION
91/02/09
061600     .
91/02/09
061700
91/02/09
061800 REMOVE-NODE-FROM-LIST.
91/02/09
061900     MOVE NODE-PREV (NODE-NBR) TO PREV-PTR
91/02/09
062000     MOVE NODE-NEXT (NODE-NBR) TO NEXT-PTR
91/02/09
062100     MOVE NEXT-PTR TO NODE-NEXT (PREV-PTR)
91/02/09
062200     MOVE PREV-PTR TO NODE-PREV (NEXT-PTR)
91/02/09
062300     .
91/02/09
062400
91/02/09
062500 ATTACH-PROGRAM-CHILD-HEAD.
91/02/09
062600     PERFORM GET-NODE-FROM-FREE-POOL
91/02/09
062700     IF NODE-NBR NOT = FREE-POOL
91/02/09
062800         MOVE NODE-NBR TO NODE-CHILD (PARENT-NODE)
91/02/09
062900                          CHILD-HEAD
91/02/09
063000                          LIST-PTR
91/02/09
063100         PERFORM CLEAR-THE-LIST
91/02/09
063200     .
91/02/09

If the program has already been processed before, we attach it to the tree,
but do not parse it:

003300 01  VARIOUS-INDICES.
91/02/09
003400     02  SENTINEL-PTR            PIC S9(3)  COMP.
91/02/09
003500     02  SCAN-PTR                PIC S9(3)  COMP.
91/02/09

063600 CHECK-PROGRAM-NOT-KNOWN.
91/02/09
063700     PERFORM LOOK-FOR-PROGRAM-IN-TABLE
91/02/09
063800     IF SCAN-PTR < SENTINEL-PTR
91/02/09
063900         PERFORM RAISE-EXCEPTION
91/02/09
064000     ELSE
91/02/09
064100         IF SENTINEL-PTR < PROGRAM-MAX
91/02/09
064200             MOVE SENTINEL-PTR TO PROGRAM-COUNT
91/02/09
064300         ELSE
91/02/09
064400             MOVE "TOO MANY DIFFERENT PROGRAMS" TO DISPLAY-DATA
91/02/09
064500             PERFORM RAISE-THE-EXCEPTION
91/02/09
064600     .
91/02/09
064700
91/02/09
064800 LOOK-FOR-PROGRAM-IN-TABLE.
91/02/09
064900     COMPUTE SENTINEL-PTR = PROGRAM-COUNT + 1
91/02/09
065000     MOVE THE-TOKEN TO PROGRAM-NAME (SENTINEL-PTR)
91/02/09
065100     PERFORM LOOK-FOR-PROGRAM-NAME
91/02/09
065200       VARYING SCAN-PTR FROM 1 BY 1
91/02/09
065300         UNTIL THE-TOKEN = PROGRAM-NAME (SCAN-PTR)
91/02/09
065400     .
91/02/09
065500
91/02/09
065600 LOOK-FOR-PROGRAM-NAME.
91/02/09
065700     EXIT
91/02/09
065800     .
91/02/09

We use PROGPK to open, read, and later, close the source file.  This has the
advantage of expanding COPY statements automatically:

007500 01  PROGPK-CONTROL.
91/02/09
007600     02  PROGPK-TASK-ID          PIC X(4).
91/02/09
007700     02  PROGPK-OPERATION        PIC X.
91/02/09
007800     02  PROGPK-FEEDBACK         PIC X.
91/02/09
007900         88  END-OF-PROGRAM                 VALUE IS ".".
91/02/09
008000     02  PROGPK-FILENAME         PIC X(8).
91/02/09
008100     02  PROGPK-FILE-TYPE        PIC X.
91/02/09
008200         88  FILE-IS-SOURCE                 VALUE IS "S".
91/02/09
008300         88  FILE-IS-COPY-BOOK              VALUE IS "C".
91/02/09
008400     02  PROGPK-TOKEN-TYPE       PIC X(2).
91/02/09
008500     02  PROGPK-TOKEN-VALUE      PIC X(30).
91/02/09
008600
91/02/09
008700 01  PROGPK-DATA.
91/02/09
008800     02  PROGRAM-SEQ-NBR         PIC 9(6).
91/02/09
008900     02  PROGRAM-LINE.
91/02/09
009000         03  PROGRAM-CONT-CHAR   PIC X.
91/02/09
009100         03  PROGRAM-AREA-A      PIC X(4).
91/02/09
009200         03  PROGRAM-AREA-B      PIC X(61).
91/02/09
009300     02  PROGRAM-COMMENT         PIC X(8).
91/02/09

066200 OPEN-SOURCE-FILE.
91/02/09
066300     MOVE THE-TOKEN TO PROGPK-FILENAME
91/02/09
066400     MOVE  "INPUT"  TO PROGPK-OPERATION
91/02/09
066500     PERFORM CALL-PROGPK
91/02/09
066600     IF PROGPK-FEEDBACK > SPACE
91/02/09
066700         PERFORM RAISE-EXCEPTION
91/02/09
066800         PERFORM CLOSE-SOURCE-FILE
91/02/09
066900     .
91/02/09
067000
91/02/09
067100 CALL-PROGPK.
91/02/09
067200     CALL "PROGPK"
91/02/09
067300         USING PROGPK-CONTROL
91/02/09
067400               PROGPK-DATA
91/02/09
067500     .
91/02/09
067600
91/02/09
067900 GET-NEXT-RECORD.
91/02/09
068000     MOVE "GET" TO PROGPK-OPERATION
91/02/09
068100     PERFORM CALL-PROGPK
91/02/09
068200     .
91/02/09
068300
91/02/09
073600 CLOSE-SOURCE-FILE.
91/02/09
073700     MOVE "CLOSE" TO PROGPK-OPERATION
91/02/09
073800     PERFORM CALL-PROGPK
91/02/09
073900     .
91/02/09

After a get operation, PROGPK indicates the type of source line returned.
If the line contains a COBOL verb (PROGPK-TOKEN-TYPE = "CV"), and the verb
is "CALL", we use the STRNPK word operation to pick up the name of the
program:

068600 CLASSIFY-THE-RECORD.
91/02/09
068700     IF END-OF-PROGRAM
91/02/09
068800         MOVE NO-MORE-EVENT TO THE-NEXT-EVENT
91/02/09
068900     ELSE
91/02/09
069000         MOVE OTHER-EVENT TO THE-NEXT-EVENT
91/02/09
069100         IF  PROGPK-TOKEN-TYPE  = "CV"
91/02/11
069200         AND PROGPK-TOKEN-VALUE = "CALL"
91/02/09
069300             PERFORM PICK-UP-PROGRAM-NAME
91/02/09
069400             PERFORM CHECK-IF-TOKEN-IS-PROGRAM
91/02/11
069500     .
91/02/09
069600
91/02/09
069700 PICK-UP-PROGRAM-NAME.
91/02/09
069800     MOVE PROGRAM-LINE TO STRING-TEXT
91/02/09
069900     PERFORM GET-NEXT-WORD
91/02/09
070000     MOVE STRING-CONCAT TO STRING-TEXT
91/02/09
070100     PERFORM GET-NEXT-WORD
91/02/09
070200     MOVE STRING-TEXT TO THE-TOKEN
91/02/09
070300     .
91/02/09
070400
91/02/09
070500 GET-NEXT-WORD.
91/02/09
070600     MOVE QUOTES TO STRING-FILL-CHAR
91/02/09
070700     MOVE "WORD" TO STRING-OPERATION
91/02/09
070800     PERFORM CALL-STRNPK
91/02/09
070900     .
91/02/09
071000
91/02/09
071100 CALL-STRNPK.
91/02/09
071200     CALL "STRNPK"
91/02/09
071300         USING STRING-CONTROL
91/02/09
071400     .
91/02/09

Since most dialog programs call a standard set of packages (SCRNIO, PROMPT,
PANLIO...), we test for these, and ignore them if they occur in a copy book.
The result is a cleaner and more useful call tree:

002400 01  VARIOUS-VALUES.
91/02/09
002500     02  THE-TOKEN               PIC X(8).
91/02/09
002600         88  STANDARD-DIALOG-PACKAGE        VALUE IS "SCRNIO"
91/02/11
002700                                                     "PROMPT"
91/02/11
002800                                                     "EMSGPK"
91/02/11
002900                                                     "PANLIO"
91/02/11
003000                                                     "DMERR"
91/02/11
003100                                                     "DHELP".
91/02/11

071600 CHECK-IF-TOKEN-IS-PROGRAM.
91/02/11
071700     IF  FILE-IS-COPY-BOOK
91/02/11
071800     AND STANDARD-DIALOG-PACKAGE
91/02/11
071900         NEXT SENTENCE
91/02/11
072000     ELSE
91/02/11
072100     IF THE-TOKEN > SPACES
91/02/11
072200         MOVE CALL-STATEMENT-EVENT TO THE-NEXT-EVENT
91/02/11
072300     .
91/02/11

When we finally find an interesting program name, we place this on the
stack:

072700 STORE-CALLED-PROGRAM.
91/02/09
072800     IF STACK-PTR < STACK-MAX
91/02/09
072900         ADD 1 TO STACK-PTR
91/02/09
073000         MOVE THE-TOKEN  TO STACK-TOKEN (STACK-PTR)
91/02/09
073100         MOVE CHILD-HEAD TO STACK-NODE  (STACK-PTR)
91/02/09
073200     .
91/02/09

The observant reader will have noticed by now that programs will be
processed in reverse.  That is, if a program calls three others, A, B, and
C, these will be processed in reverse order; namely C, B, and then A.  The
resulting linked list will be back-to-front.  This is due to the way a stack
works.  This poses no real problems.  Firstly, since the linked lists have
pointers in both directions, we can process the nodes backwards as easily as
forwards.  Secondly, since the `print' phase also stacks its requests, the
order of the programs will be reversed once more.

f. Printing the Call Tree

To print the call tree we use a standard pseudo-recursive loop which
processes requests from a stack until the stack is empty.  The result is
sent to a print file managed by PRNTIO:

074300 PRINT-PROGRAM-STRUCTURE.
91/02/09
074400     PERFORM OPEN-PRINT-FILE
91/02/09
074500     PERFORM INIT-PRINT-REQUEST-STACK
91/02/09
074600     PERFORM PROCESS-PRINT-REQUEST
91/02/09
074700       UNTIL STACK-PTR = ZERO
91/02/09
074800
91/02/09
074900     PERFORM CLOSE-PRINT-FILE
91/02/09
075000     .
91/02/09

The print file takes the name of the root program:

011700 01  PRNTIO-CONTROL.
91/02/09
011800     02  PRNTIO-TASK-ID          PIC X(4).
91/02/09
011900     02  PRNTIO-OPERATION        PIC X.
91/02/09
012000     02  PRNTIO-FEEDBACK         PIC X.
91/02/09
012100     02  PRNTIO-FILENAME         PIC X(8).
91/02/09
012200
91/02/09
012300 01  PRNTIO-DATA.
91/02/09
012400     02  PRNTIO-TOKEN            PIC X(8)   OCCURS 15 TIMES.
91/02/09

075200 OPEN-PRINT-FILE.
91/02/09
075300     MOVE       SPACES       TO PRNTIO-DATA
91/02/09
075400     MOVE PARAM-FILENAME (1) TO PRNTIO-FILENAME
91/02/09
075500     MOVE       "OPEN"       TO PRNTIO-OPERATION
91/02/09
075600     PERFORM CALL-PRNTIO
91/02/09
075700     .
91/02/09
075800
91/02/09
075900 CALL-PRNTIO.
91/02/09
076000     CALL "PRNTIO"
91/02/09
076100         USING PRNTIO-CONTROL
91/02/09
076200               PRNTIO-DATA
91/02/09
076300     .
91/02/09
076400
91/02/09
082400 CLOSE-PRINT-FILE.
91/02/09
082500     MOVE "CLOSE" TO PRNTIO-OPERATION
91/02/09
082600     PERFORM CALL-PRNTIO
91/02/09
082700     .
91/02/09

The print phase needs different local storage from the build phase; we now
use the STACK-LEVEL item to indicate the indentation on the page (the root
program is at level 1), and the STACK-TOKEN item to indicate whether the
program is the last one for that parent or not:

076500 INIT-PRINT-REQUEST-STACK.
91/02/09
076600     MOVE     1      TO STACK-PTR, STACK-LEVEL (STACK-PTR)
91/02/09
076700     MOVE NODE-NEXT (LIST-HEAD) TO STACK-NODE  (STACK-PTR)
91/02/09
076800     MOVE  SPACES               TO STACK-TOKEN (STACK-PTR)
91/02/11
076900     .
91/02/09

To process the next print request, we take the information off the stack,
print the line or lines needed for that program, and stack the requests for
all the programs it calls:

003300 01  VARIOUS-INDICES.
91/02/09
003600     02  CUR-LEVEL               PIC S9(3)  COMP.
91/02/09
003700     02  PREV-LEVEL              PIC S9(3)  COMP.
91/02/11

077100 PROCESS-PRINT-REQUEST.
91/02/09
077200     MOVE STACK-LEVEL (STACK-PTR) TO CUR-LEVEL
91/02/09
077300     MOVE STACK-NODE  (STACK-PTR) TO NODE-NBR
91/02/09
077400     MOVE STACK-TOKEN (STACK-PTR) TO THE-TOKEN
91/02/09
077500     MOVE NODE-CHILD  (NODE-NBR)  TO CHILD-HEAD
91/02/11
077600     SUBTRACT 1 FROM STACK-PTR
91/02/09
077700
91/02/09
077800     PERFORM PRINT-LINES-FOR-THIS-PROGRAM
91/02/11
077900     PERFORM STACK-PRINT-CHILD-REQUESTS
91/02/09
078000     .
91/02/09

Some careful code ensures that the printed text looks good.  Firstly, a
called program which is followed by others for the same parent is printed
so:

:------ program

while the last program in a list is printed so:

`------ program

Further, a `:' character must be placed in the previous column so that
further children are properly connected.  The value in THE-TOKEN
accomplishes a dual purpose; if it is a space, it signals the last of a list
of children; otherwise it contains the connector character:

078200 PRINT-LINES-FOR-THIS-PROGRAM.
91/02/11
078300     COMPUTE PREV-LEVEL = CUR-LEVEL - 1
91/02/11
078400     IF PREV-LEVEL > ZERO
91/02/11
078500         IF THE-TOKEN > SPACES
91/02/11
078600             MOVE ":------" TO PRNTIO-TOKEN (PREV-LEVEL)
91/02/11
078700         ELSE
91/02/11
078800             MOVE "`------" TO PRNTIO-TOKEN (PREV-LEVEL)
91/02/11
078900     .
91/02/09
079000     MOVE NODE-NAME (NODE-NBR) TO PRNTIO-TOKEN (CUR-LEVEL)
91/02/09
079100     PERFORM PRINT-THE-LINE
91/02/09
079200
91/02/09
079300     IF PREV-LEVEL > ZERO
91/02/11
079400         MOVE THE-TOKEN TO PRNTIO-TOKEN (PREV-LEVEL)
91/02/11
079500         MOVE  SPACES   TO PRNTIO-TOKEN (CUR-LEVEL)
91/02/09
079600         IF  THE-TOKEN = SPACES
91/02/11
079700         AND NODE-NEXT (CHILD-HEAD) = CHILD-HEAD
91/02/11
079800             PERFORM PRINT-THE-LINE
91/02/11
079900     .
91/02/09
080000
91/02/09
080100 PRINT-THE-LINE.
91/02/09
080200     MOVE "PRINT" TO PRNTIO-OPERATION
91/02/09
080300     PERFORM CALL-PRNTIO
91/02/09
080400     .
91/02/09

As a last step, a request is stacked for each program in the list of
children.  Because the print file was opened with the standard operation
code "OPEN", the print line is 120 characters wide, so it is limited to 15
levels.  Other operation codes provide for different page widths.  Programs
at deeper levels are ignored:

001900 01  VARIOUS-CONSTANTS.
91/02/09
002000     02  MAX-PRINT-LEVEL         PIC S9(3)  VALUE +15 COMP.
91/02/09

080600 STACK-PRINT-CHILD-REQUESTS.
91/02/09
080700     MOVE NODE-NEXT (CHILD-HEAD) TO NEXT-PTR
91/02/09
080800     MOVE  SPACES                TO THE-TOKEN
91/02/11
080900     IF CUR-LEVEL < MAX-PRINT-LEVEL
91/02/09
081000         PERFORM STACK-PRINT-CHILD-REQUEST
91/02/09
081100           UNTIL NEXT-PTR = CHILD-HEAD
91/02/09
081200     .
91/02/09
081300
91/02/09
081400 STACK-PRINT-CHILD-REQUEST.
91/02/09
081500     ADD 1 TO STACK-PTR
91/02/09
081600     ADD 1 CUR-LEVEL GIVING STACK-LEVEL (STACK-PTR)
91/02/09
081700     MOVE NEXT-PTR       TO STACK-NODE  (STACK-PTR)
91/02/09
081800     MOVE THE-TOKEN      TO STACK-TOKEN (STACK-PTR)
91/02/09
081900
91/02/09
082000     MOVE NODE-NEXT (NEXT-PTR) TO NEXT-PTR
91/02/09
082100     MOVE    ":"               TO THE-TOKEN
91/02/11
082200     .
91/02/09


g. Using the Structure Analyser

The following MS-DOS procedure, STRUCT, creates a parameter file and calls
the structure analyser, $STRUCT :

 @echo off
 echo ,%1 > struct.par
 $struct

To run the analyzer, give the command:

 C:\DEV>struct program

The procedure should not be as simple as here.  At least it should check
that at least one parameter is present and show a help screen if not.
The result arrives in a listing file with the same name as the root program.
You can look at or print this file as you like.  The result for a typical,
complex program is:

LCHEM
:------ DMACT
:       :------ DMHLP
:       :------ PANLIO
:       :------ STRNPK
:       `------ DMSERV
:
:------ DMHLP
:------ DMPOP
:------ DMSHO
:       :------ DMHLP
:       :------ DMSERV
:       `------ LINEIO
:
:------ DMWIN
:       :------ DMHLP
:       :------ DMPOP
:       :       :------ DMHLP
:       :       :       :------ DMPOPH
:       :       :       :       :------ DMSERV
:       :       :       :       `------ STRNPK
:       :       :       :
:       :       :       :------ STRNPK
:       :       :       :------ HKEYIO
:       :       :       :------ DMSERV
:       :       :       :------ HELPPK
:       :       :       :       :------ HELPIO
:       :       :       :       :------ CONVPK
:       :       :       :       `------ STRNPK
:       :       :       :
:       :       :       `------ CONVPK
:       :       :
:       :       :------ DMSERV
:       :       `------ STRNPK
:       :
:       :------ PANLIO
:       :------ DMSERV
:       :       `------ EMSGPK
:       :
:       :------ NAMEPK
:       `------ STRNPK
:
:------ LOGIO
:------ DIRPK
:------ TEXTIO
:------ ERRLOG
`------ CHEMPK
        :------ TEXTIO
        :------ CONVPK
        :------ HELPIO
        :------ HKEYIO
        `------ EMSGIO

Note, that if a program is called several times (e.g. DMHELP) its call-tree
is only shown once in order not to clutter up the diagram.  If a program is
called twice form the same program, it is shown twice.  You should always
isolate the call of a program in a separate paragraph.  STRUCT shows you, if
you didn't follow that advice.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 12)_

- **From:** Charles F Hankel <charles@hankel.freedombird.net>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.134b68c5ce7faef1989a17@news.mersinet.co.uk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net> <38E06A71.7416D504@Azonic.co.nz> <38e00705_1@news3.prserv.net> <MPG.134abcddcd9f31899899f9@news.mersinet.co.uk> <38e0b66b_1@news3.prserv.net>`

```
I noticed that Leif Svalgaard as lsvalg@ibm.net said...
> Charles F Hankel <charles@hankel.mersinet.co.uk> wrote in message
> news:MPG.134abcddcd9f31899899f9@news.mersinet.co.uk...
…[24 more quoted lines elided]…
> used is to show the point without being lengthy.

It's got no bearing on anything that I've come across in over a quarter 
of a century's working at the coalface.  If you can give an example that 
has some relevance, I'll be prepared to listen but all I can see is an 
academic exercise that has no relevance to real life.  So far, I've seen 
nothing of a commercial programming nature that needs recursion and that 
can't be done by iteration.

Fine, do your Tower of Hanoi thing but, frankly, if I ever needed it I'd 
buy it in from whoever wrote it in whatever language they wrote it.  And 
the same goes for spreadsheets, although I already have relational 
databases for rows and columns manipulation.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 13)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e2985b_2@news3.prserv.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net> <38E06A71.7416D504@Azonic.co.nz> <38e00705_1@news3.prserv.net> <MPG.134abcddcd9f31899899f9@news.mersinet.co.uk> <38e0b66b_1@news3.prserv.net> <MPG.134b68c5ce7faef1989a17@news.mersinet.co.uk>`

```

Charles F Hankel <charles@hankel.freedombird.net> wrote in message
> > > Oh, bollocks.  I'm fed up with ridiculous illustrations of points that
> > > have little or no bearing on the commercial environment that is
COBOL's
> > > natural home.
> >
…[14 more quoted lines elided]…
>
Charles, the reason silly little things like 'the towers of Hanoi' are
used is to show the point without being lengthy. It is hard to be
more realistic without using a lot of bandwidth. But, since you raised
the point, here is a more realistic example. Don't worry that it also
calls various subroutines and uses something called a 'dialog'
These are things real applications might do. The example
shows how to analyze a tree of called programs. Similar
solutions could be used for any hierarchical data and business
has a lot of that kind.
I have already posted that example, but either you didn't see
it or didn't spend the time to read it. Remember, that when you
ask for realistic code, it will always be long:

2. Structure Analyser

This tool prints out the structure of programs called in an application.
This structure resembles a tree, with the root being the main program.  A
typical call tree looks like this:

CALC
`------ CALCPK
        `------ MATHPK

As we look at the design of this tool, we shall see how to use complex
lists, stacks, and pseudo-recursive programming to solve a real problem.

a. General Design
The basic problem is broken into two pieces: first build the call tree, then
print it out.  Both of these problems can be attacked in a recursive manner:

 � To build the tree: start with the root program.  Attach this to the tree,
and look for all CALL statements in the source code.  For each of these
called programs, repeat the process.

 � To print the tree: start with the root of the tree.  Print the program's
name and look at the list of called programs.  For each of these, repeat the
process.

The `tree' structure will be a complex linked-list where each program points
to a doubly-linked list of called programs:

 +------+    +---------+
(� head �====� program �)
 +------+    +---------+
                  |
                  |
               +------+    +---------+    +---------+
              (� head �====� program �====� program �)
               +------+    +---------+    +---------+
                               |               :
                               |
                            +------+    +---------+    +---------+
                           (� head �====� program �====� program �)
                            +------+    +---------+    +---------+
                                            |              |
                                            |              |
                                         +------+       +------+
                                        (� head �)     (� head �)
                                         +------+       +------+

This is a slight simplification of the fully-general complex list, since a
node can have only a single sub-list.  Thus, rather than using a
doubly-linked list between `program' and `head', we use a single pointer.
When a program calls no others, the head points to itself, signifying an
empty list.

b. The Main Data Structures

The main data structure is adapted from the doubly-linked list described
previously.  The nodes contain an extra pointer, NODE-CHILD, which points to
the sub-list of called programs.  We also define some extra pointers such as
PARENT-NODE and CHILD-HEAD for use in the program:

003900 01  LIST-POINTERS.
004000     02  EMPTY-PTR               PIC S9(3)  COMP  VALUE ZERO.
004100     02  FREE-POOL               PIC S9(3)  COMP  VALUE +1.
004200     02  LIST-HEAD               PIC S9(3)  COMP  VALUE +2.
004300     02  FIRST-NODE              PIC S9(3)  COMP  VALUE +3.
004400     02  LAST-NODE               PIC S9(3)  COMP  VALUE +998.
004500     02  NODE-NBR                PIC S9(3)  COMP.
004600     02  LIST-PTR                PIC S9(3)  COMP.
004700     02  PREV-PTR                PIC S9(3)  COMP.
004800     02  NEXT-PTR                PIC S9(3)  COMP.
004900     02  PARENT-NODE             PIC S9(3)  COMP.
005000     02  CHILD-HEAD              PIC S9(3)  COMP.
005100
005200 01  LIST-NODES.
005300     02  LIST-NODE                          OCCURS 998 TIMES.
005400         03  NODE-PREV           PIC S9(3)  COMP.
005500         03  NODE-NEXT           PIC S9(3)  COMP.
005600         03  NODE-CHILD          PIC S9(3)  COMP.
005700         03  NODE-NAME           PIC X(8).

A separate structure holds a table of all known programs.  Before looking in
detail at a program, we look in this table, so that a program will not be
analyzed twice (this keeps the resulting call tree simpler).  We use an
extra entry in the table to act as a sentinel:

006000 01  PROGRAM-TABLE.
006100     02  PROGRAM-COUNT           PIC S9(3)  VALUE ZERO COMP.
006200     02  PROGRAM-MAX             PIC S9(3)  VALUE +100 COMP.
006300     02  PROGRAM-NAME            PIC X(8)   OCCURS 101 TIMES.
006400

A stack of requests will drive the pseudo-recursive code.  The stack holds
local data needed by the `build' and `print' algorithms:

006600 01  REQUEST-STACK.
006700     02  STACK-PTR               PIC S9(3)            COMP.
006800     02  STACK-MAX               PIC S9(3)  VALUE +100 COMP.
006900     02  STACK-ENTRY                        OCCURS 100 TIMES.
007000         03  STACK-TOKEN         PIC X(8).
007100         03  STACK-NODE          PIC S9(3)  COMP.
007200         03  STACK-LEVEL         PIC S9(3)  COMP.

We initialize these data structures as follows:

051800 INIT-DATA-STRUCTURES.
051900     MOVE ZERO TO PROGRAM-COUNT
052000     PERFORM INIT-LINKED-LIST
052100     .
052200
052300 INIT-LINKED-LIST.
052400     MOVE LIST-HEAD TO LIST-PTR
052500     PERFORM CLEAR-THE-LIST
052600     MOVE FREE-POOL TO LIST-PTR
052700     PERFORM CLEAR-THE-LIST
052800
052900     PERFORM ATTACH-NODE-TO-LIST
053000       VARYING NODE-NBR FROM FIRST-NODE BY 1
053100         UNTIL NODE-NBR > LAST-NODE
053200     .
053300
053400 CLEAR-THE-LIST.
053500     MOVE LIST-PTR TO NODE-NEXT (LIST-PTR)
053600                      NODE-PREV (LIST-PTR)
053700     .
053800

Note how the LAST-NODE cannot have a value of 999 when NODE-NBR has a
picture like S9(3) because of the overflow of NODE-NBR when it reaches 999.
This subtle error will not occur if computational values are stored
internally as binary numbers with a range larger than 999, so we have here
the potential for a non-portable bug that will strike on some systems, but
not on others.

Attaching a node to a list is straight-forward once the list has been
initialized to empty (i.e. pointing to itself):

053900 ATTACH-NODE-TO-LIST.
054000     MOVE NODE-PREV (LIST-PTR) TO PREV-PTR
054200     MOVE LIST-PTR TO NODE-NEXT (NODE-NBR)
054300     MOVE NODE-NBR TO NODE-NEXT (PREV-PTR)
054400     MOVE PREV-PTR TO NODE-PREV (NODE-NBR)
054500     MOVE NODE-NBR TO NODE-PREV (LIST-PTR)
054600     .

c. The Program's Dialog

Most of the dialog is concerned with the `build' algorithm.  The request
stack is initialized to contain a single request, i.e. to parse the root
program.  The main dialog loop gets the next request off the stack and
parses the program specified.  An inner loop reads each line of source code;
whenever it finds a CALL statement, it stacks a request to parse the called
program.  This continues until the request stack is empty:

 .-------------------.
( AFTER-INIT          )
!`-------------------'
!                                          .-------------------.
( OK    )- - - - - - - - - - - - - - - -> ( HAVE-REQUEST        )
!           ( GET-THE-PARAMETERS        )   `-------------------'
!           ( INITIALISE-REQUEST-STACK  )
!           ( GET-NEXT-REQUEST          )
!                                          .-------------------.
( ERROR )- - - - - - - - - - - - - - - -> (                     )
            ( TERMINATE-THE-PROGRAM    )   `-------------------'

 .-------------------.
( HAVE-REQUEST        )
!`-------------------'
!                                            .-------------------.
( OK        )- - - - - - - - - - - - - - -> ( HAVE-RECORD         )
!              ( CHECK-PROGRAM-NOT-KNOWN )   `-------------------'
!              ( OPEN-SOURCE-FILE        )
!              ( GET-NEXT-RECORD         )
!              ( CLASSIFY-THE-RECORD     )
!                                            .-------------------.
( NO-MORE   )- - - - - - - - - - - - - - -> (                     )
!              ( PRINT-PROGRAM-STRUCTURE )   `-------------------'
!              ( TERMINATE-THE-PROGRAM   )
!                                            .-------------------.
( EXCEPTION )- - - - - - - - - - - - - - -> ( HAVE-REQUEST        )
               ( GET-NEXT-REQUEST        )   `-------------------'

 .-------------------.
( HAVE-RECORD         )
!`-------------------'
!                                            .-------------------.
( CALL-STATEMENT)- - - - - - - - - - - -  > ( HAVE-RECORD         )
!                 ( STORE-CALLED-PROGRAM )   `-------------------'
!                 ( GET-NEXT-RECORD      )
!                 ( CLASSIFY-THE-RECORD  )
!                                            .-------------------.
( OTHER         )- - - - - - - - - - - - -> ( HAVE-RECORD         )
!                  ( GET-NEXT-RECORD     )   `-------------------'
!                  ( CLASSIFY-THE-RECORD )
!                                            .-------------------.
( NO-MORE       )- - - - - - - - - - - - -> ( HAVE-REQUEST        )
                   ( CLOSE-SOURCE-FILE   )   `-------------------'
                   ( GET-NEXT-REQUEST    )

 .-------------------.
( DEFAULTS            )
!`-------------------'
!                                              .-------------------.
( EXCEPTION     )- - - - - - - - - - - - - -> (                     )
                   ( TERMINATE-THE-PROGRAM )   `-------------------'

d. Getting the Parameters

Like all batch programs, STRUCT gets its parameters through PARMPK.  In this
case, it expects a single filename, with no switches or other controls:

012700 01  PARMPK-CONTROL.
012800     02  PARMPK-TASK-ID          PIC X(4).
012900     02  PARMPK-OPERATION        PIC X      VALUE "G".
013000     02  PARMPK-FEEDBACK         PIC X.
013100     02  PARMPK-FILENAME         PIC X(8)   VALUE "STRUCT".
013200
013300 01  PARMPK-DATA.
013400     02  PARMPK-COUNT            PIC S9(3)  COMP.
013500     02  PARMPK-VALUES                      VALUE SPACES.
013600         03  PARAM-FILENAME      PIC X(8)   OCCURS 64 TIMES.
013700     02  PARMPK-SWITCH-DATA.
013800         03  SWITCH-LIST.
013900             04  FILLER          PIC X(64)  VALUE SPACES.
014000         03  SWITCH-CONTROL.
014100             04  FILLER          PIC X(8)   VALUE SPACES.
014200         03  SWITCH-VALUES.
014300             04  FILLER          PIC X(64)  VALUE SPACES.

To get the parameters we call PARMPK:

055400 GET-THE-PARAMETERS.
055500     CALL "PARMPK"
055600         USING PARMPK-CONTROL
055700               PARMPK-DATA
055800
055900     IF PARMPK-FEEDBACK > SPACE
056000         MOVE "PARAMETER FILE `STRUCT' NOT FOUND" TO DISPLAY-DATA
056100         PERFORM RAISE-THE-EXCEPTION
056200     .
056300
056400 RAISE-THE-EXCEPTION.
056500     PERFORM RAISE-EXCEPTION
056600     PERFORM DISPLAY-THE-MESSAGE
056700     .
056800
056900 RAISE-EXCEPTION.
057000     MOVE      "YES"      TO EXCEPTION-RAISED
057100     MOVE EXCEPTION-EVENT TO THE-EXCEPTION-EVENT
057200     .
057300
057400 DISPLAY-THE-MESSAGE.
057500     CALL "DISPPK"
057600         USING DISPLAY-CONTROL
057700               DISPLAY-DATA
057800     .

e. Building the Call Tree

Each time a request to parse a program is taken from the stack, the program
specified is attached somewhere to the call tree.  This `somewhere' is
always the head of appropriate list.  We attach the root program to
LIST-HEAD:

058200 INITIALISE-REQUEST-STACK.
058300     MOVE 1 TO STACK-PTR
058400     MOVE PARAM-FILENAME (1) TO STACK-TOKEN (STACK-PTR)
058500     MOVE LIST-HEAD          TO STACK-NODE  (STACK-PTR)
058600     .

Note, that we assume that at least one parameter is always present
(PARAM-FILENAME (1)).  This should be checked by the procedure that invokes
the structure analyzer, so there is no need for checking it again here.

If there are no more requests, the NO-MORE-EVENT is signaled.  Otherwise,
the top request is taken off the stack, and two nodes are attached: one to
hold the program, and one to act as the head for the list of called
programs, if any.  This head is always immediately attached, to simplify the
general algorithm:

059000 GET-NEXT-REQUEST.
059100     IF STACK-PTR > ZERO
059200         MOVE STACK-TOKEN (STACK-PTR) TO THE-TOKEN
059300         MOVE STACK-NODE  (STACK-PTR) TO LIST-PTR
059400         SUBTRACT 1 FROM STACK-PTR
059500         PERFORM ATTACH-PROGRAM-NAME-TO-LIST
059600         PERFORM ATTACH-PROGRAM-CHILD-HEAD
059700         PERFORM SET-OK
059800     ELSE
059900         MOVE NO-MORE-EVENT TO THE-NEXT-EVENT
060000     .
060100
060200 ATTACH-PROGRAM-NAME-TO-LIST.
060300     PERFORM GET-NODE-FROM-FREE-POOL
060400     IF NODE-NBR NOT = FREE-POOL
060500         PERFORM ATTACH-NODE-TO-LIST
060600         MOVE THE-TOKEN TO NODE-NAME (NODE-NBR)
060700         MOVE NODE-NBR  TO PARENT-NODE
060800     .
060900
061000 GET-NODE-FROM-FREE-POOL.
061100     MOVE NODE-NEXT (FREE-POOL) TO NODE-NBR
061200     PERFORM REMOVE-NODE-FROM-LIST
061300     IF NODE-NBR = FREE-POOL
061400         MOVE "PROGRAM STRUCTURE IS TOO COMPLEX" TO DISPLAY-DATA
061500         PERFORM RAISE-THE-EXCEPTION
061600     .
061700
061800 REMOVE-NODE-FROM-LIST.
061900     MOVE NODE-PREV (NODE-NBR) TO PREV-PTR
062000     MOVE NODE-NEXT (NODE-NBR) TO NEXT-PTR
062100     MOVE NEXT-PTR TO NODE-NEXT (PREV-PTR)
062200     MOVE PREV-PTR TO NODE-PREV (NEXT-PTR)
062300     .
062400
062500 ATTACH-PROGRAM-CHILD-HEAD.
062600     PERFORM GET-NODE-FROM-FREE-POOL
062700     IF NODE-NBR NOT = FREE-POOL
062800         MOVE NODE-NBR TO NODE-CHILD (PARENT-NODE)
062900                          CHILD-HEAD
063000                          LIST-PTR
063100         PERFORM CLEAR-THE-LIST
063200     .

If the program has already been processed before, we attach it to the tree,
but do not parse it:

003300 01  VARIOUS-INDICES.
003400     02  SENTINEL-PTR            PIC S9(3)  COMP.
003500     02  SCAN-PTR                PIC S9(3)  COMP.

063600 CHECK-PROGRAM-NOT-KNOWN.
063700     PERFORM LOOK-FOR-PROGRAM-IN-TABLE
063800     IF SCAN-PTR < SENTINEL-PTR
063900         PERFORM RAISE-EXCEPTION
064000     ELSE
064100         IF SENTINEL-PTR < PROGRAM-MAX
064200             MOVE SENTINEL-PTR TO PROGRAM-COUNT
064300         ELSE
064400             MOVE "TOO MANY DIFFERENT PROGRAMS" TO DISPLAY-DATA
064500             PERFORM RAISE-THE-EXCEPTION
064600     .
064700
064800 LOOK-FOR-PROGRAM-IN-TABLE.
064900     COMPUTE SENTINEL-PTR = PROGRAM-COUNT + 1
065000     MOVE THE-TOKEN TO PROGRAM-NAME (SENTINEL-PTR)
065100     PERFORM LOOK-FOR-PROGRAM-NAME
065200       VARYING SCAN-PTR FROM 1 BY 1
065300         UNTIL THE-TOKEN = PROGRAM-NAME (SCAN-PTR)
065400     .
065500
065600 LOOK-FOR-PROGRAM-NAME.
065700     EXIT
065800     .

We use PROGPK to open, read, and later, close the source file.  This has the
advantage of expanding COPY statements automatically:

007500 01  PROGPK-CONTROL.
007600     02  PROGPK-TASK-ID          PIC X(4).
007700     02  PROGPK-OPERATION        PIC X.
007800     02  PROGPK-FEEDBACK         PIC X.
007900         88  END-OF-PROGRAM                 VALUE IS ".".
008000     02  PROGPK-FILENAME         PIC X(8).
008100     02  PROGPK-FILE-TYPE        PIC X.
008200         88  FILE-IS-SOURCE                 VALUE IS "S".
008300         88  FILE-IS-COPY-BOOK              VALUE IS "C".
008400     02  PROGPK-TOKEN-TYPE       PIC X(2).
008500     02  PROGPK-TOKEN-VALUE      PIC X(30).
008600
008700 01  PROGPK-DATA.
008800     02  PROGRAM-SEQ-NBR         PIC 9(6).
008900     02  PROGRAM-LINE.
009000         03  PROGRAM-CONT-CHAR   PIC X.
009100         03  PROGRAM-AREA-A      PIC X(4).
009200         03  PROGRAM-AREA-B      PIC X(61).
009300     02  PROGRAM-COMMENT         PIC X(8).

066200 OPEN-SOURCE-FILE.
066300     MOVE THE-TOKEN TO PROGPK-FILENAME
066400     MOVE  "INPUT"  TO PROGPK-OPERATION
066500     PERFORM CALL-PROGPK
066600     IF PROGPK-FEEDBACK > SPACE
066700         PERFORM RAISE-EXCEPTION
066800         PERFORM CLOSE-SOURCE-FILE
066900     .
067000
067100 CALL-PROGPK.
067200     CALL "PROGPK"
067300         USING PROGPK-CONTROL
067400               PROGPK-DATA
067500     .
067600
067900 GET-NEXT-RECORD.
068000     MOVE "GET" TO PROGPK-OPERATION
068100     PERFORM CALL-PROGPK
068200     .
068300
073600 CLOSE-SOURCE-FILE.
073700     MOVE "CLOSE" TO PROGPK-OPERATION
073800     PERFORM CALL-PROGPK
073900     .

After a get operation, PROGPK indicates the type of source line returned.
If the line contains a COBOL verb (PROGPK-TOKEN-TYPE = "CV"), and the verb
is "CALL", we use the STRNPK word operation to pick up the name of the
program:

068600 CLASSIFY-THE-RECORD.
068700     IF END-OF-PROGRAM
068800         MOVE NO-MORE-EVENT TO THE-NEXT-EVENT
068900     ELSE
069000         MOVE OTHER-EVENT TO THE-NEXT-EVENT
069100         IF  PROGPK-TOKEN-TYPE  = "CV"
069200         AND PROGPK-TOKEN-VALUE = "CALL"
069300             PERFORM PICK-UP-PROGRAM-NAME
069400             PERFORM CHECK-IF-TOKEN-IS-PROGRAM
069500     .
069600
069700 PICK-UP-PROGRAM-NAME.
069800     MOVE PROGRAM-LINE TO STRING-TEXT
069900     PERFORM GET-NEXT-WORD
070000     MOVE STRING-CONCAT TO STRING-TEXT
070100     PERFORM GET-NEXT-WORD
070200     MOVE STRING-TEXT TO THE-TOKEN
070300     .
070400
070500 GET-NEXT-WORD.
070600     MOVE QUOTES TO STRING-FILL-CHAR
070700     MOVE "WORD" TO STRING-OPERATION
070800     PERFORM CALL-STRNPK
070900     .
071000
071100 CALL-STRNPK.
071200     CALL "STRNPK"
071300         USING STRING-CONTROL
071400     .

Since most dialog programs call a standard set of packages (SCRNIO, PROMPT,
PANLIO...), we test for these, and ignore them if they occur in a copy book.
The result is a cleaner and more useful call tree:

002400 01  VARIOUS-VALUES.
002500     02  THE-TOKEN               PIC X(8).
002600         88  STANDARD-DIALOG-PACKAGE        VALUE IS "SCRNIO"
002700                                                     "PROMPT"
002800                                                     "EMSGPK"
002900                                                     "PANLIO"
003000                                                     "DMERR"
003100                                                     "DHELP".

071600 CHECK-IF-TOKEN-IS-PROGRAM.
071700     IF  FILE-IS-COPY-BOOK
071800     AND STANDARD-DIALOG-PACKAGE
071900         NEXT SENTENCE
072000     ELSE
072100     IF THE-TOKEN > SPACES
072200         MOVE CALL-STATEMENT-EVENT TO THE-NEXT-EVENT
072300     .

When we finally find an interesting program name, we place this on the
stack:

072700 STORE-CALLED-PROGRAM.
072800     IF STACK-PTR < STACK-MAX
072900         ADD 1 TO STACK-PTR
073000         MOVE THE-TOKEN  TO STACK-TOKEN (STACK-PTR)
073100         MOVE CHILD-HEAD TO STACK-NODE  (STACK-PTR)
073200     .

The observant reader will have noticed by now that programs will be
processed in reverse.  That is, if a program calls three others, A, B, and
C, these will be processed in reverse order; namely C, B, and then A.  The
resulting linked list will be back-to-front.  This is due to the way a stack
works.  This poses no real problems.  Firstly, since the linked lists have
pointers in both directions, we can process the nodes backwards as easily as
forwards.  Secondly, since the `print' phase also stacks its requests, the
order of the programs will be reversed once more.

f. Printing the Call Tree

To print the call tree we use a standard pseudo-recursive loop which
processes requests from a stack until the stack is empty.  The result is
sent to a print file managed by PRNTIO:

074300 PRINT-PROGRAM-STRUCTURE.
074400     PERFORM OPEN-PRINT-FILE
074500     PERFORM INIT-PRINT-REQUEST-STACK
074600     PERFORM PROCESS-PRINT-REQUEST
074700       UNTIL STACK-PTR = ZERO
074800
074900     PERFORM CLOSE-PRINT-FILE
075000     .

The print file takes the name of the root program:

011700 01  PRNTIO-CONTROL.
011800     02  PRNTIO-TASK-ID          PIC X(4).
011900     02  PRNTIO-OPERATION        PIC X.
012000     02  PRNTIO-FEEDBACK         PIC X.
012100     02  PRNTIO-FILENAME         PIC X(8).
012200
012300 01  PRNTIO-DATA.
012400     02  PRNTIO-TOKEN            PIC X(8)   OCCURS 15 TIMES.

075200 OPEN-PRINT-FILE.
075300     MOVE       SPACES       TO PRNTIO-DATA
075400     MOVE PARAM-FILENAME (1) TO PRNTIO-FILENAME
075500     MOVE       "OPEN"       TO PRNTIO-OPERATION
075600     PERFORM CALL-PRNTIO
075700     .
075800
075900 CALL-PRNTIO.
076000     CALL "PRNTIO"
076100         USING PRNTIO-CONTROL
076200               PRNTIO-DATA
076300     .
076400
082400 CLOSE-PRINT-FILE.
082500     MOVE "CLOSE" TO PRNTIO-OPERATION
082600     PERFORM CALL-PRNTIO
082700     .

The print phase needs different local storage from the build phase; we now
use the STACK-LEVEL item to indicate the indentation on the page (the root
program is at level 1), and the STACK-TOKEN item to indicate whether the
program is the last one for that parent or not:

076500 INIT-PRINT-REQUEST-STACK.
076600     MOVE     1      TO STACK-PTR, STACK-LEVEL (STACK-PTR)
076700     MOVE NODE-NEXT (LIST-HEAD) TO STACK-NODE  (STACK-PTR)
076800     MOVE  SPACES               TO STACK-TOKEN (STACK-PTR)
076900     .

To process the next print request, we take the information off the stack,
print the line or lines needed for that program, and stack the requests for
all the programs it calls:

003300 01  VARIOUS-INDICES.
003600     02  CUR-LEVEL               PIC S9(3)  COMP.
003700     02  PREV-LEVEL              PIC S9(3)  COMP.

077100 PROCESS-PRINT-REQUEST.
077200     MOVE STACK-LEVEL (STACK-PTR) TO CUR-LEVEL
077300     MOVE STACK-NODE  (STACK-PTR) TO NODE-NBR
077400     MOVE STACK-TOKEN (STACK-PTR) TO THE-TOKEN
077500     MOVE NODE-CHILD  (NODE-NBR)  TO CHILD-HEAD
077600     SUBTRACT 1 FROM STACK-PTR
077700
077800     PERFORM PRINT-LINES-FOR-THIS-PROGRAM
077900     PERFORM STACK-PRINT-CHILD-REQUESTS
078000     .

Some careful code ensures that the printed text looks good.  Firstly, a
called program which is followed by others for the same parent is printed
so:

:------ program

while the last program in a list is printed so:

`------ program

Further, a `:' character must be placed in the previous column so that
further children are properly connected.  The value in THE-TOKEN
accomplishes a dual purpose; if it is a space, it signals the last of a list
of children; otherwise it contains the connector character:

078200 PRINT-LINES-FOR-THIS-PROGRAM.
078300     COMPUTE PREV-LEVEL = CUR-LEVEL - 1
078400     IF PREV-LEVEL > ZERO
078500         IF THE-TOKEN > SPACES
078600             MOVE ":------" TO PRNTIO-TOKEN (PREV-LEVEL)
078700         ELSE
078800             MOVE "`------" TO PRNTIO-TOKEN (PREV-LEVEL)
078900     .
079000     MOVE NODE-NAME (NODE-NBR) TO PRNTIO-TOKEN (CUR-LEVEL)
079100     PERFORM PRINT-THE-LINE
079200
079300     IF PREV-LEVEL > ZERO
079400         MOVE THE-TOKEN TO PRNTIO-TOKEN (PREV-LEVEL)
079500         MOVE  SPACES   TO PRNTIO-TOKEN (CUR-LEVEL)
079600         IF  THE-TOKEN = SPACES
079700         AND NODE-NEXT (CHILD-HEAD) = CHILD-HEAD
079800             PERFORM PRINT-THE-LINE
079900     .
080000
080100 PRINT-THE-LINE.
080200     MOVE "PRINT" TO PRNTIO-OPERATION
080300     PERFORM CALL-PRNTIO
080400     .

As a last step, a request is stacked for each program in the list of
children.  Because the print file was opened with the standard operation
code "OPEN", the print line is 120 characters wide, so it is limited to 15
levels.  Other operation codes provide for different page widths.  Programs
at deeper levels are ignored:

001900 01  VARIOUS-CONSTANTS.
002000     02  MAX-PRINT-LEVEL         PIC S9(3)  VALUE +15 COMP.

080600 STACK-PRINT-CHILD-REQUESTS.
080700     MOVE NODE-NEXT (CHILD-HEAD) TO NEXT-PTR
080800     MOVE  SPACES                TO THE-TOKEN
080900     IF CUR-LEVEL < MAX-PRINT-LEVEL
081000         PERFORM STACK-PRINT-CHILD-REQUEST
081100           UNTIL NEXT-PTR = CHILD-HEAD
081200     .
081300
081400 STACK-PRINT-CHILD-REQUEST.
081500     ADD 1 TO STACK-PTR
081600     ADD 1 CUR-LEVEL GIVING STACK-LEVEL (STACK-PTR)
081700     MOVE NEXT-PTR       TO STACK-NODE  (STACK-PTR)
081800     MOVE THE-TOKEN      TO STACK-TOKEN (STACK-PTR)
081900
082000     MOVE NODE-NEXT (NEXT-PTR) TO NEXT-PTR
082100     MOVE    ":"               TO THE-TOKEN
082200     .


g. Using the Structure Analyser

The following MS-DOS procedure, STRUCT, creates a parameter file and calls
the structure analyser, $STRUCT :

 @echo off
 echo ,%1 > struct.par
 $struct

To run the analyzer, give the command:

 C:\DEV>struct program

The procedure should not be as simple as here.  At least it should check
that at least one parameter is present and show a help screen if not.
The result arrives in a listing file with the same name as the root program.
You can look at or print this file as you like.  The result for a typical,
complex program is:

LCHEM
:------ DMACT
:       :------ DMHLP
:       :------ PANLIO
:       :------ STRNPK
:       `------ DMSERV
:
:------ DMHLP
:------ DMPOP
:------ DMSHO
:       :------ DMHLP
:       :------ DMSERV
:       `------ LINEIO
:
:------ DMWIN
:       :------ DMHLP
:       :------ DMPOP
:       :       :------ DMHLP
:       :       :       :------ DMPOPH
:       :       :       :       :------ DMSERV
:       :       :       :       `------ STRNPK
:       :       :       :
:       :       :       :------ STRNPK
:       :       :       :------ HKEYIO
:       :       :       :------ DMSERV
:       :       :       :------ HELPPK
:       :       :       :       :------ HELPIO
:       :       :       :       :------ CONVPK
:       :       :       :       `------ STRNPK
:       :       :       :
:       :       :       `------ CONVPK
:       :       :
:       :       :------ DMSERV
:       :       `------ STRNPK
:       :
:       :------ PANLIO
:       :------ DMSERV
:       :       `------ EMSGPK
:       :
:       :------ NAMEPK
:       `------ STRNPK
:
:------ LOGIO
:------ DIRPK
:------ TEXTIO
:------ ERRLOG
`------ CHEMPK
        :------ TEXTIO
        :------ CONVPK
        :------ HELPIO
        :------ HKEYIO
        `------ EMSGIO

Note, that if a program is called several times (e.g. DMHELP) its call-tree
is only shown once in order not to clutter up the diagram.  If a program is
called twice form the same program, it is shown twice.  You should always
isolate the call of a program in a separate paragraph.  STRUCT shows you, if
you didn't follow that advice.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 14)_

- **From:** Charles F Hankel <charles@hankel.freedombird.net>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1351d881c934a3c989a4d@news.mersinet.co.uk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net> <38E06A71.7416D504@Azonic.co.nz> <38e00705_1@news3.prserv.net> <MPG.134abcddcd9f31899899f9@news.mersinet.co.uk> <38e0b66b_1@news3.prserv.net> <MPG.134b68c5ce7faef1989a17@news.mersinet.co.uk> <38e2985b_2@news3.prserv.net>`

```
I noticed that Leif Svalgaard as lsvalg@ibm.net said...
> 
> Charles F Hankel <charles@hankel.freedombird.net> wrote in message
…[37 more quoted lines elided]…
> typical call tree looks like this:

With the greatest respect this has no bearing on anything that I have 
been asked to write or maintain in over a quarter of a century's working 
in the commercial environment.  It may well be laudable in its niche, but 
I have no interest in it and I would argue that it has no relevance to 
most COBOL work that anyone undertakes.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E302A2.2C56A94A@Azonic.co.nz>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net>`

```
> I noticed that Leif Svalgaard as lsvalg@ibm.net said...
> >
…[13 more quoted lines elided]…
> > 1. Towers of Hanoi

The 'Towers of Hanoi' is an example of something that _might_ be done
recursively or it may be done iteritively.  If the program source code
is explicitly maintaining a stack and indexing into it then it is being
done _iteritively_ regardless of whether it uses performs or go tos, or
even calls.

For recursion there must be a stack maintained by the system and
usabable by a called routine calling itself (or a performed paragraph
performing itself) in sucha a way that the system can unwind the calls
correctly.

Now if you can provide an example of _recursion_ that I can compile and
run using the Cobol 74 compiler that I have here then you may score a
point.

You would get a further point if you could show a _useful_ example, eg
one that is easier to code and understand and doesn't run slower than an
iteritive one.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e294eb_4@news3.prserv.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38df5bd7_4@news3.prserv.net> <38E302A2.2C56A94A@Azonic.co.nz>`

```

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:38E302A2.2C56A94A@Azonic.co.nz...
> > I noticed that Leif Svalgaard as lsvalg@ibm.net said...
> > >
…[4 more quoted lines elided]…
> > > > > Bill, as I have repeatedly shown, recursion CAN be done even in
COBOL
> > > > > 74 or older.
> > > >
> > > > I would challenge you to do it in an implementation of Cobol 74 that
I
> > > > have here.  In fact you are most likely _NOT_ saying that it can be
done
> > > > in 'Cobol 74', but in a particular implementation of Cobol 74 that
> > > > includes
…[13 more quoted lines elided]…
> correctly.

If there is a stack it is recursion no matter who maintains the stack.
Recursion is a 'mindset' rather than a technical point. It is possible
to do the Factorial iteratively without a stack or recursively with
a stack. The recursive version is here slower, but it is not possible
to do Towers iteratively without a stack, it must be done recursively.
I did post a more *realistic" example, but the problem with such
an example is that it quickly becomes so long that nobody cares
to read an study it. BTW, the stack maintenance is about the same
work no matter how big the program is, but gets completely lost
in large *realistic" programs.

Richard, I do not wish to split hairs about the definition of
recursion.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DFE81A.DDE127F4@melbpc.org.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net>`

```
Recursion does not add any power in theory to a programming
language. You can always simulate recursion by hand managing a
stack. Just as you can simulate perform/call with variables and
goto - which is what compilers do. But it would not be sensible
to do so.

I am aware of a number of COBOL programs in production that do
kind of stack simulation - mainly when managing complex data
structures. In many  cases recursion is a natural fit for the
problem at hand and produces smaller, simpler more comprehensible
code than the alternatives.

The new cobol standard is turning cobol into C++. Not just local
variables, lots more as well.

Tim Josling

"William M. Klein" wrote:
> 
> OK - start with the fact that the business programs that ARE written in
…[3 more quoted lines elided]…
> easily) in COBOL...
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.134abe04ba19a2729899fa@news.mersinet.co.uk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38DFE81A.DDE127F4@melbpc.org.au>`

```
I noticed that Tim Josling as tej@melbpc.org.au said...
> 
> The new cobol standard is turning cobol into C++. Not just local
> variables, lots more as well.

Which is why I don't like it.  If I need to use C++, I'll use it and I 
don't need it's influences screwing up the basic tenets of COBOL and all 
that this means.  Just because C++ people have a generally hard time in 
understanding how to get the best out of COBOL, why should COBOL change 
to pander to their limits?  When C++ can deal simply with simple concepts 
like packed decimals and files, maybe I'll start to listen.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s4j2eskgvkdoeh1f72bkceuhva3tpki0rk@4ax.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38DFE81A.DDE127F4@melbpc.org.au> <MPG.134abe04ba19a2729899fa@news.mersinet.co.uk>`

```
Charles F Hankel <charles@hankel.mersinet.co.uk> wrote:

>When C++ can deal simply with simple concepts 
>like packed decimals and files, maybe I'll start to listen.

perhaps you haven't heard of open-edition c


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** Charles F Hankel <charles@hankel.freedombird.net>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1351d8b4a30f8fb0989a4e@news.mersinet.co.uk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38DFE81A.DDE127F4@melbpc.org.au> <MPG.134abe04ba19a2729899fa@news.mersinet.co.uk> <s4j2eskgvkdoeh1f72bkceuhva3tpki0rk@4ax.com>`

```
I noticed that G Moore as gvwmoore@spam.ix.netcom.com said...
> Charles F Hankel <charles@hankel.mersinet.co.uk> wrote:
> 
…[3 more quoted lines elided]…
> perhaps you haven't heard of open-edition c

Perhaps not :-)

Is it part of any internationally recognised standard?
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 11)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<msthesgrgllhamdo34t5j1n7i0fevtdmjl@4ax.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38DFE81A.DDE127F4@melbpc.org.au> <MPG.134abe04ba19a2729899fa@news.mersinet.co.uk> <s4j2eskgvkdoeh1f72bkceuhva3tpki0rk@4ax.com> <MPG.1351d8b4a30f8fb0989a4e@news.mersinet.co.uk>`

```
Charles F Hankel <charles@hankel.freedombird.net> wrote:

>I noticed that G Moore as gvwmoore@spam.ix.netcom.com said...
>> Charles F Hankel <charles@hankel.mersinet.co.uk> wrote:

>> perhaps you haven't heard of open-edition c

>Perhaps not :-)

>Is it part of any internationally recognised standard?

well, it's from *international* business machines, hehe.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 12)_

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.135680525426aa9c9896a7@news.freedombird.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com> <NKpD4.8547$0o4.60216@iad-read.news.verio.net> <8blo6s$qjd$1@nnrp1.deja.com> <8bmu1j$r0j$1@nntp9.atl.mindspring.net> <38DFE81A.DDE127F4@melbpc.org.au> <MPG.134abe04ba19a2729899fa@news.mersinet.co.uk> <s4j2eskgvkdoeh1f72bkceuhva3tpki0rk@4ax.com> <MPG.1351d8b4a30f8fb0989a4e@news.mersinet.co.uk> <msthesgrgllhamdo34t5j1n7i0fevtdmjl@4ax.com>`

```
I noticed that G Moore as gvwmoore@spam.ix.netcom.com said...
> Charles F Hankel <charles@hankel.freedombird.net> wrote:
> 
…[9 more quoted lines elided]…
> well, it's from *international* business machines, hehe.

I think I've heard of them.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** frlsfly@aol.com (FRLSFLY)
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000328214523.02474.00005107@ng-ca1.aol.com>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net>`

```
I cannot conceive of a problem soluble thru recursion that cannot be solved by
iteration; nor can I find any authority that so claims.

ALL recursive solutions have an iterative equivalent.  I would further claim
that for large or variable data problems, particularly those where the code
must execute in shared environments, the iterative solution is superior both in
reliability and in resource use.

There is an argument to be made that in some circumstances the recursive
solution is conceptually simpler, and in stand-alone scientific/engineering
environments the fragility and inefficency of recursive solutions are not
critical. I have no experience of such environments, so I cannot judge if these
arguments have validity.

 It is my experience that in shared business environments, recursive code is a
serious mistake, particularly for any process that queues. 





>Two examples where recursion (and recursive programming languages) are
>absolutely required are:
…[14 more quoted lines elided]…
>then recurssion MAY make this possible.



Nathan Meyer
Berkeley, CA
"Big Endian" is what I like.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com>`

```
On 29 Mar 2000 02:45:23 GMT, frlsfly@aol.com (FRLSFLY) wrote:

>I cannot conceive of a problem soluble thru recursion that cannot be solved by
>iteration; nor can I find any authority that so claims.
>
>ALL recursive solutions have an iterative equivalent.

Where is the authority that claims this?  I would be very much surprosed, as anybody
claiming this is not an authority <g>

There is a proven theory that certain (mathematical) functions that are defined
recursively cannot be defined in a iterative algorithmic way.  I mentioned this before -
Look at hte Ackerman function.  It is recursively defined, and try to design a iterative
method

>I would further claim
>that for large or variable data problems, particularly those where the code
>must execute in shared environments, the iterative solution is superior both in
>reliability and in resource use.

Resouce usage - maybe.   But reliability?  Why should the iterative method be more
reliable than the recursive method?
>
>There is an argument to be made that in some circumstances the recursive
>solution is conceptually simpler, and in stand-alone scientific/engineering
>environments the fragility and inefficency of recursive solutions are not
>critical.

Again - where is the authority on this?  Fragility?  Inefficency?  Where, when, how?

>I have no experience of such environments, so I cannot judge if these
>arguments have validity.
…[30 more quoted lines elided]…
>"Big Endian" is what I like.

     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         You still need the last file you removed.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** frlsfly@aol.com (FRLSFLY)
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000329021019.23345.00001055@ng-fv1.aol.com>`
- **References:** `<ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com>`

```
Nathan wrote, Volker responded:

>>ALL recursive solutions have an iterative equivalent.
>
…[36 more quoted lines elided]…
>>
Dear Volker,

I have never seen a textbook or book on algorithims that ever said anything
else!
I've got a couple here at hand: "Algorithmics" by David Harel ( Who has nice
iterative solution to the Towers Of Hanoi problem) and "Algorithims and Data
Structures- An approach in  C"  by Bowman.   And, gee every 'C' and C++ text I
own!   I suppose they could all be wrong...?

Could you cite the source of your proven theory?

I find iterative solutions are more reliable, because they are more predictable
in their resource consumption.  By storing intermediate results then returning;
 you are far less likely to get bounds problems that clobber memeory, or
resource conflicts that cause process failure. Simple arithmetic overflow
checks will not protect your recursive functions. 

As to the Ackerman Function, if I recall correctly that is simply a solution to
the problem of "for Integer N, exponentiate N by itself N times".  I don't have
an iterative solution in my back pocket, but I could probably code one this
weekend- don't how I'd prove it's function rigorously though!  Numbers are too
big..anybody got an idea?

By the by,  last time I heard of anybody using the Ackerman function outside of
CS classes it was for Denial Of Service attacks- if you can get a task that
does that sort of exponentiation running recursively, it will bring any system
to its' knees!   So, that kinda supports my feelings v. recursive functions!   

Regards,



Nathan Meyer
Berkeley, CA
"Big Endian" is what I like.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pib4es4sldp7qs15vgkv53g74q7ugde86a@4ax.com>`
- **References:** `<ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <20000329021019.23345.00001055@ng-fv1.aol.com>`

```
On 29 Mar 2000 07:10:19 GMT, frlsfly@aol.com (FRLSFLY) wrote:

>Dear Volker,
>
…[32 more quoted lines elided]…
>"Big Endian" is what I like.
Hello Nathan,

thanks for your thoughtful note.  I cannot defute it out of hand, because I am sitting in
a hotel room right now with no access to my references.  That will be available on the
weekend

One thing, though - Possibly we have diffent ideas of what ALGORITHMIC means as opposed to
RECURSIVE.

For me, an algorithmic approach means that the wanted result can be expressed in a closed
mathematical formula

For you, an algorithmic approach means the the wanted result can be achieved by a certain
set of manipulations (program statements, e.g.)

Taking the second approach, then every recursive problem is also solvable algorithmically.
If not - just take the object module created by the compiler that supports recursive
invocation, disassemble it, and use the resulting instruction as "The Algorithm"

What I had in mind though is the following:

f(0) := 1
f(n) := n * f(n-1), if n > 0

is a simple recursive definition, which can be iterative solved as
f(n) = 2 * 3 * 4 * .... *n

given the system
f(0) := 1
f(1) := 1
f(n) := f(n-1) + f(n-2)

it is already a little bit more difficult to find a closed formula.  (it does exist, just
check on Fibbonaci numbers)

The Ackerman function is NOT n**n, but something altogether weird.  I am quoting from
memory, and that is admittedly faulty, and I came across this more than 20 years ago while
studying math, so I can't give the formula now.  I will do my best to get the correct one
on the weekend.

The idea behind the simplified Ackerman function looks something like this

A(1,1) :=1 
A(m,n) = A(m-1,A(???))

where ??? is some expression made from m an n
This expression can become larger than any number for which A(m-1,....) has been
previously calculted, i.e you need LATER elemnts of the recursion to compute the current
value

There is no closed formula for the simplefied Ackerman function.  That's what is asserted
by the named Theorem (stated by Ackerman, of course <g>) 



I also believe that we speak different languages when talking about reliability.

A process is RELIABLE, when, given a defined set of data that it is designed to process,
always gives the same set of results matching the input data.

In that sense both recursive and algorithmic methods are reliable.

An yes, recursive methods can take up huge amount of resources.  I once sent a large
system into limbo when I thought I let it compute A(10,10)  <g>  The amount of CPU used
grows exponentially with each iteration.....

This doesn't make the method less reliable, just more expensive (especially, if you have
no alternative)

     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         Mathematician do it to the limit


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         Hidden I/O Functions instructions: SCL SET CURSER TO LOUD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 11)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e295d2_2@news3.prserv.net>`
- **References:** `<ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <20000329021019.23345.00001055@ng-fv1.aol.com> <pib4es4sldp7qs15vgkv53g74q7ugde86a@4ax.com>`

```

Volker Bandke <vbandke@bsp-gmbh.com> wrote in message
> The Ackerman function is NOT n**n, but something altogether weird.  I am
quoting from
> memory, and that is admittedly faulty, and I came across this more than 20
years ago while
> studying math, so I can't give the formula now.  I will do my best to get
the correct one
> on the weekend.
>
…[6 more quoted lines elided]…
> This expression can become larger than any number for which A(m-1,....)
has been
> previously calculted, i.e you need LATER elemnts of the recursion to
compute the current
> value

The Ackerman function is also one the slowest growing functions known.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jb4cesotshd6tph325db6r8c7v4dmlco7o@4ax.com>`
- **References:** `<ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <20000329021019.23345.00001055@ng-fv1.aol.com>`

```
On 29 Mar 2000 07:10:19 GMT, frlsfly@aol.com (FRLSFLY) wrote:

>
>As to the Ackerman Function, if I recall correctly that is simply a solution to
…[3 more quoted lines elided]…
>big..anybody got an idea?
Dear Nathan,

I found the definition of the ackerman function, which is included below

       A(m,n) := n+1             for m=0
              := A(m-1,1)        for n = 0
              := A(m-1,A(m,n-1)) otherwise

A recursive COBOL program is included to calculate the Ackerman function.

       IDENTIFICATION DIVISION.
      *----------------------------------------------------------------
      * Unfortunately, COBOL does not yet provide userdefined functions,
      * therefore the programming of a solution looks a little bit
      * awkward.  In REXX or PLI the programming is even more straight
      * forward:
      *
      *     ackermann:
      *        procedure(m,n) returns(fixed) recursive;
      *        declare (m,n) fixed;
      *        if m = 0 then
      *           return(n+1);
      *        if n = 0 then
      *           return(ackermann(m-1,1));
      *        return(ackermann(m-1,ackermann(m,n-1)));
      *     end ackermann;
      *
      *----------------------------------------------------------------

        PROGRAM-ID. ACKER IS RECURSIVE.
       DATA DIVISION.
        WORKING-STORAGE SECTION.
         01 Inv-count  PIC S9(9) BINARY VALUE 0.
         01 N1         PIC S9(9) BINARY VALUE 1.
        LOCAL-STORAGE SECTION.
         01 AckerMN-1  PIC S9(9) BINARY.
         01 M-1        PIC S9(9) BINARY.
         01 N-1        PIC S9(9) BINARY.
        LINKAGE SECTION.
         01 M          PIC S9(9) BINARY.
         01 N          PIC S9(9) BINARY.
         01 AckerMN    PIC S9(9) BINARY.
       PROCEDURE DIVISION USING     M, N
                          RETURNING AckerMN.

           ADD 1 TO Inv-count
              ON SIZE ERROR
                 DISPLAY 'Overflow in invokation count'
                 DISPLAY 'Last value was Inv-count=' Inv-count
                 DISPLAY 'M = ' M
                 DISPLAY 'N = ' N
                 STOP RUN
           END-ADD
           EVALUATE TRUE
              WHEN M = 0
                 COMPUTE AckerMN = N + 1
              WHEN N = 0
                 COMPUTE M-1 = M - 1
                 CALL 'ACKER' USING M-1, N1
                              RETURNING AckerMN
              WHEN OTHER
                 COMPUTE M-1 = M - 1
                 COMPUTE N-1 = N - 1
                 CALL 'ACKER' USING     M, N-1
                              RETURNING AckerMN-1
                 CALL 'ACKER' USING     M-1, AckerMN-1
                              RETURNING AckerMN
           END-EVALUATE
           GOBACK
           .

I think the implementation is quite readable.  What about designing an iterative method of
providing, lets say, A(5,9)?
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 11)_

- **From:** frlsfly@aol.com (FRLSFLY)
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000404235131.21135.00000854@ng-fn1.aol.com>`
- **References:** `<jb4cesotshd6tph325db6r8c7v4dmlco7o@4ax.com>`

```
Dear Volker:

Sorry to have been so tardy in replying, life has been a bit compacted lately-
I still have to get my Xmas cards mailed, for one thing. 

Thank you for the example in COBOL.  I'll have to sit and mull it over.  In the
meantime, I've found a bone for you, here:
http://www.dur.ac.uk/~dcs0mpw/martin/papers/ack-t.ps.gz.

It's a paper entitled "Iterative Procedures For Computing Ackermans Function". 
I've only just skimmed it- much of it is over my head, I think- but he has a
cute idea, which is to formulate algorithims recursively, so that they are
capable of being proved, then implement the algorithim iteratively, so that  it
can execute efficiently.

Some time when I've had more sleep I'd like to discuss the meaning of reliable
vs trustworthy with you..I suspect that what you call reliable, I call
trustworthy, ie a proven function.  


Nathan Meyer
Berkeley, CA
"Big Endian" is what I like.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 12)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ju74fsgo0eerpiefqd7vu51coilmcv0frc@4ax.com>`
- **References:** `<jb4cesotshd6tph325db6r8c7v4dmlco7o@4ax.com> <20000404235131.21135.00000854@ng-fn1.aol.com>`

```
On 05 Apr 2000 03:51:31 GMT, frlsfly@aol.com (FRLSFLY) wrote:

Dear Nathan,

>In the
>meantime, I've found a bone for you, here:
>http://www.dur.ac.uk/~dcs0mpw/martin/papers/ack-t.ps.gz.
>
And what a bone it is - with lots of meat still on it <g>.  I spent quite a few hours this
weekend reading the paper (well, this is one way of passing the time, waiting at an
airport for a connecting flight, and then sitting in the plane), but I admit that my
progress is really slow.

I worked through to page 9, chapter 6.1, and think I understood everything so far .  But,
of course, there wasn't really anything new until here - it was just specified in a more
formal way than usual

But then I started out on chapter 7, and am still struggling a bit.  (or a Byte.  or more
exactly, a real big byte (like MB)).  Somehow I can seem to follow his steps, and will
have to invest some more time with this paper.

I will come back to you when I have some more insights (one way or the other).  But this
will definitely take till May

     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         Some things have to be believed to be seen.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E1E596.B0DF4314@melbpc.org.au>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com>`

```
Volker,

Read 'Computability and Complexity from a Programming
Perspective' by Neil D Jones (MIT Press 1997), wherein the author
proves the equivalence of many classes of programming language,
incidentally demolishing your claim below. You can do everything
with GOTO and a few basic operations. Can, not should. 

Tim Josling

Volker Bandke wrote:
> 
> On 29 Mar 2000 02:45:23 GMT, frlsfly@aol.com (FRLSFLY) wrote:
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ekb4escto9p3q5tctfs02i31sat3cqddd9@4ax.com>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au>`

```
On Wed, 29 Mar 2000 21:14:30 +1000, Tim Josling <tej@melbpc.org.au> wrote:

>Volker,
>
…[5 more quoted lines elided]…
>

Languages, language, language...  See my reply to Nathan

Of course you can do everuthing with GOTO and a few operations, that is what every
compiler does (and that's what I do when I program in assembler)

But this still does not mean that any recursively defined function can also be expressed
in a closed formula for algorithmic processing

With kind regards


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         I don't want to be young again, I just don't want to get any older.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au>`

```
On Wed, 29 Mar 2000 21:14:30 +1000, Tim Josling <tej@melbpc.org.au> wrote:

>Tim Josling
>
…[7 more quoted lines elided]…
>> >ALL recursive solutions have an iterative equivalent.

Dear Tim,

if this is true, please provide an iterative solution for the Ackerman function, which is
defined as such:

       A(m,n) := n+1             for m=0
              := A(m-1,1)        for n = 0
              := A(m-1,A(m,n-1)) otherwise

A recursive COBOL program is included

       IDENTIFICATION DIVISION.
        PROGRAM-ID. ACKER IS RECURSIVE.
       DATA DIVISION.
        WORKING-STORAGE SECTION.
         01 N1         PIC S9(9) BINARY VALUE 1.
        LOCAL-STORAGE SECTION.
         01 AckerMN-1  PIC S9(9) BINARY.
         01 M-1        PIC S9(9) BINARY.
         01 N-1        PIC S9(9) BINARY.
        LINKAGE SECTION.
         01 M          PIC S9(9) BINARY.
         01 N          PIC S9(9) BINARY.
         01 AckerMN    PIC S9(9) BINARY.
       PROCEDURE DIVISION USING     M, N
                          RETURNING AckerMN.
           EVALUATE TRUE
              WHEN M = 0
                 COMPUTE AckerMN = N + 1
              WHEN N = 0
                 COMPUTE M-1 = M - 1
                 CALL 'ACKER' USING M-1, N1
                              RETURNING AckerMN
              WHEN OTHER
                 COMPUTE M-1 = M - 1
                 COMPUTE N-1 = N - 1
                 CALL 'ACKER' USING     M, N-1
                              RETURNING AckerMN-1
                 CALL 'ACKER' USING     M-1, AckerMN-1
                              RETURNING AckerMN
           END-EVALUATE
           GOBACK
           .


The "driver program" would be

       IDENTIFICATION DIVISION.
        PROGRAM-ID. ACKTEST IS INITIAL.
       DATA DIVISION.
        WORKING-STORAGE SECTION.
         01 M         PIC S9(9) BINARY.
         01 N         PIC S9(9) BINARY.
         01 M-MAX     PIC S9(9) BINARY VALUE 10.
         01 N-MAX     PIC S9(9) BINARY VALUE 10.
         01 AckerMN   PIC S9(9) BINARY.
        PROCEDURE DIVISION.
           PERFORM VARYING M FROM 0 BY 1 UNTIL M > M-MAX
              PERFORM VARYING N FROM 0 BY 1 UNTIL N > N-MAX
                 CALL 'ACKER' USING M, N
                              RETURNING AckerMN
                 DISPLAY 'ACKER(' M ',' N ')=' AckerMN
              END-PERFORM
           END-PERFORM
           GOBACK
           .

I think the implementation is quite readable and rather straight forwar (PLI or REXX would
be even simpler).  Now - I really would like a nice iteratice solution....
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 11)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E6F0E1.427501FF@Azonic.co.nz>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com>`

```
Volker Bandke wrote:
> >>
> >> >I cannot conceive of a problem soluble thru recursion that cannot be solved by
…[6 more quoted lines elided]…
> if this is true, please provide an iterative solution for the Ackerman function,

'Recursion' is only an artifact of the computer language used, it is
where, within a function, that function is reactivated. It is a feature
of the language whether this is allowed, it is often a feature of the
source code whether this will work as intended.

At the hardware level there is no recursion, only iteration. Therefore
anything that can be done 'recursively' is actually _being_ done
iteritively.

To convert the ackerman function to remove recursion it is only
necessary to understand what is happening in the recursive version and
code around what is happening implicitly and make it explicit.

  *Recursion is a way of making repitition.

   Replace this by having PERFORM UNTIL DONE
                              acker code
                                  that eventually sets done
                          END-PERFORM

  *Recursion stacks up LOCAL-STORAGE

   Replace this by having a W-S array holding the items
   in L-S and an index that has the current stack pointer.

I leave the details to those that give a damn about Ackerman.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 12)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e680e4_3@news3.prserv.net>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com> <38E6F0E1.427501FF@Azonic.co.nz>`

```
you are, of course, correct in the details: at the lowest
level there is no recursion, but you miss the whole point:
recursion is about not the lowest level, but about the
*highest* level. Did your formulate and express your
problem in recursive terms or is your problem
naturally recursive (like walking a tree), then you
are using recursion, even if it is *implemented*
(as it ultimately must) non-recursively.
Consider the trivial factorial:

recursive thinking:  fac(n) = n * fac (n-1)
iterative thinking: s=1; for i=1 step 1 until n do s=s*i

the actual machine may (but then might not) be the same
in both cases, depending on your compiler and its
optimizer. But that is irrelevant. What matters is
what YOU thought when you tried to solve the
problem.

Specifically for Ackerman's function, NOBODY has
any clue how to formulate it without thinking recursively.

One more time: who cares how the machine does
it (or what you or your compiler must do to simulate recursion)?
What matters is how did YOU think about the solution.
You will find that almost always, finding a recursive
solution is a lot less thought than finding an iterative
one, and that is the value of recursion.

Richard Plinston <riplin@Azonic.co.nz> wrote in message
news:38E6F0E1.427501FF@Azonic.co.nz...
> Volker Bandke wrote:
> > >>
> > >> >I cannot conceive of a problem soluble thru recursion that cannot be
solved by
> > >> >iteration; nor can I find any authority that so claims.
> > >> >
…[4 more quoted lines elided]…
> > if this is true, please provide an iterative solution for the Ackerman
function,
>
> 'Recursion' is only an artifact of the computer language used, it is
…[24 more quoted lines elided]…
> I leave the details to those that give a damn about Ackerman.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 13)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E8366F.1B990F9C@Azonic.co.nz>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com> <38E6F0E1.427501FF@Azonic.co.nz> <38e680e4_3@news3.prserv.net>`

```
Leif Svalgaard wrote:
> 
> you are, of course, correct in the details: at the lowest
> level there is no recursion, but you miss the whole point:

The 'whole point' was that there is an iteritive solution for every
recursive problem, as claimed. amd that recursion is not required as a
language feature in order to solve problems.

> recursion is about not the lowest level, but about the
> *highest* level. Did your formulate and express your
…[3 more quoted lines elided]…
> (as it ultimately must) non-recursively.

So, it seems, that your claim that 'recursion' can be implemented in
Cobol 74 is based on it not being actual recursion.  You seem to
imaginge that if the program is 'Towers of Hanoi' or 'Factorials' or
'Ackerman' then this is enough to 'prove' that the language does
recursion.

> Consider the trivial factorial:
> 
…[7 more quoted lines elided]…
> problem.

So you think that the iteritive solution is recursion ?

Actually you are quite wrong.  Recursion is a specific thing in a
computer language.  It is when a routine 'recurses' or realls itself
regardless of the problem being solved.

For example:

    Paragraph-A.

        ....
          PERFORM Paragraph-A
        .

Or:
    PROGRAM-ID.       RoutineA.
    ...
          CALL "RoutineA"
              USING ....

These are recursion, iteration is not recursion.


> Specifically for Ackerman's function, NOBODY has
> any clue how to formulate it without thinking recursively.

Can you provide references for this wild and outlandish claim ?
 
> One more time: who cares how the machine does
> it (or what you or your compiler must do to simulate recursion)?

On the subject of Towers of Haboi, or Ackerman or factorials, then (in
this group) "who cares" ?

> What matters is how did YOU think about the solution.
> You will find that almost always, finding a recursive
> solution is a lot less thought than finding an iterative
> one, and that is the value of recursion.

Given that the problem set faced by Cobol programmers and the solution
set appropriate for recursion are disparate then this is largely
irrelevant.

But I would challenge your 'lot less thought' claim.  It may be true
that someone who has been taught to use recursion may naturally try to
use it and may find it hard to think iteritively (even to the point that
they make claims that things cannot be done iteritively).  It may be
true that it took _you_ a long time to think of an iteritive mechanism,
but you are wrong to generalise this to everyone.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 14)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2e9fess698dhofcn0pat6o772jmtb1ksov@4ax.com>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com> <38E6F0E1.427501FF@Azonic.co.nz> <38e680e4_3@news3.prserv.net> <38E8366F.1B990F9C@Azonic.co.nz>`

```
On Mon, 03 Apr 2000 07:13:03 +0100, Richard Plinston <riplin@Azonic.co.nz> wrote:

>Leif Svalgaard wrote:
>> 
…[5 more quoted lines elided]…
>language feature in order to solve problems.

Sorry,

you (and Tim) REALLY miss the point big time. 
The recursive definition of a problem solution will define the final result at 1oo%,
without any need IN THE ALGORITHM to cater for things like stacks, linked lists, dynamic
memory, whatever.  When writing a program to computes ACK(100,100), I just use the
recursive definition, and that's it-can you provide a program that computes A(M,N) for
every conceivable pair of M and N and is "as simple or simpler"?  The claim was: Recursion
does not add anything to the functions and facilities of a programming language. O.K. :
Hic Rhodos, hic salta!


Try a pseudo-iterative approach - How big would you define the array A(I,J)?

Try a real iterative approach --> closed formula:
While Fibonaccis numbers are easily (?) solved with a simple (?) formula (see my message
to Tim Josling), no such formula exists for the Ackerman function.  This is just what
Ackermann proved in his Theorem - The Recursice Ackerman Function cannot be reduced to
primitive-recursive function (i.e. back to +, -, *, / etc)  Thus Leif's claim is not
'outlandish'

Again - The set of recursive functions is identical to the set of programmable functions
on a Register machine / Turing machine.  This is undisputed.  But some problems cannot be
expressed in a closed iterative approach

>
>Actually you are quite wrong.  Recursion is a specific thing in a
>computer language.  It is when a routine 'recurses' or realls itself
>regardless of the problem being solved.

You are absolutely correct on this one.  Leif just proposed a mechanism to work around the
current COBOL limitations that don't allow this recursion.  His technique provides limited
recursion technology in an non-recursive compiler, but is not strictly recursion
>
>
…[3 more quoted lines elided]…
>Can you provide references for this wild and outlandish claim ?

Can you guess why it is called the Ackermann function?  Could it have something to do with
the fact the F.W. Ackermann, 1896 - 1962 (with 2 n's, BTW) was working with recursion
theory??  And one of the results he found is that "his" function is not
primitive-recursive

>But I would challenge your 'lot less thought' claim.  It may be true
>that someone who has been taught to use recursion may naturally try to
…[3 more quoted lines elided]…
>but you are wrong to generalise this to everyone.

But some things can be generalized, even if one doesn't know all the possible objects of
the generalization.  For example it is easy to show that between any two rational numbers
there must be an irrational number, and vive  versa - but I do not know all the
irrationals  -  and the rationals ar far and few between (pun intended)+




     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



         Strike while the iron is hot.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 15)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E7AE87.172A20E5@melbpc.org.au>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com> <38E6F0E1.427501FF@Azonic.co.nz> <38e680e4_3@news3.prserv.net> <38E8366F.1B990F9C@Azonic.co.nz> <2e9fess698dhofcn0pat6o772jmtb1ksov@4ax.com>`

```
You have now redefined recursion ("primitive-recursive") as any
program that uses dynamic memory. This is not a generally
accepted definition of recursion. In Australia we call this
'moving the goal posts' (changing the rules after the game
started). 

In fact you can implement a recursive algorithm without the use
of a language feature called recursion (where a function calls
itself directly or indirectly), we all agree.

Now any deterministic program with a finite memory resource is
just a state machine and there are large classes of problems they
cannot solve, as we know from CS101. Ack may  well be one of
them.

Tim Josling

Volker Bandke wrote:
> Sorry,
> 
…[12 more quoted lines elided]…
> primitive-recursive
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 11)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E657B4.FE14B6A6@melbpc.org.au>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com>`

```
To convert a recursive program to a non-recursive one, simply
simulate the recurson using your own stack, or using iterative
dynamic memory allocation. It is trivial but tedious - using
recursive calls is more elegant in many cases, which I why I
think having recursion is a good thing. 

What you are saying is that you don't believe that the Ackerman
function can be immplemented in COBOL 85. It can be. Again I
refer you to the literature which shows the equivalence of all
the major paradigms in terms of the problems they can solve
(though not in terms of speed - there are some problems that may
be significantly slower in a *pure* functional language).

I will make a deal with you. I will provide a non-recursive
implementation of ack, provide you agree that if I succeed you
will

- publicly admit - in this NG - that you know nothing about
Computer Science
- not question any future claims I make in this NG.

Alternatively I will do it for $US500. We can organise it via
Ebay.

Tim Josling

Volker Bandke wrote:
> 
> On Wed, 29 Mar 2000 21:14:30 +1000, Tim Josling <tej@melbpc.org.au> wrote:
…[14 more quoted lines elided]…
> if this is true, please provide an iterative solution for the Ackerman function...
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 12)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E6ED83.D7341B31@zip.com.au>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com> <38E657B4.FE14B6A6@melbpc.org.au>`

```
Tim Josling wrote:
> 
> To convert a recursive program to a non-recursive one, simply
…[11 more quoted lines elided]…
> 

It is always possible to convert a recursive function to an iterative
approach. The question is it desirable?  Is it more readable?  Is it
as efficient?  The answer to this is no, but all the time.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 12)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1c5ees0910hk2runvj80ls9g72teeatjjt@4ax.com>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com> <38E657B4.FE14B6A6@melbpc.org.au>`

```
On Sun, 02 Apr 2000 06:10:28 +1000, Tim Josling <tej@melbpc.org.au> wrote:

>To convert a recursive program to a non-recursive one, simply
>simulate the recurson using your own stack, or using iterative
>dynamic memory allocation. It is trivial but tedious - using
>recursive calls is more elegant in many cases, which I why I
>think having recursion is a good thing. 

I have already stated that reverse engineering the machine code of (e.g. my Ackermann)
program would present an iterative approach.  But, is it an iterative Solution?

Look at the following:

f(0) := 1
f(1) := 1
f(n) := f(n-1) + f(n-2)

This is a recursive function (actually primitive-recursive)  and can be easily programmed
using recursion in PLI, REXX, C, and even COBOL

You can try to solve this iteratively using an array/table to contain all previously
computed values of f, but then, of course, your function evaluation range is limited by
the size of your table.  Only a partial solution.

An full iterative solution would be

(use a monospaced font here)

K := SQRT(5)  (Square Root)

             .-              n+1                 n+1  -.
        1    |  .-  1 + K  -.       .-  1 - K  -.      |
f(n) = --- * |  |  -------  |   -   |  -------  |      |
        K    |  |_    2    _|       |_    2    _|      |
             |_                                       _|                      

Which will give you a result for any value of n.

My claim is/was:  There is no such iterative solution to the Ackerman function.

>What you are saying is that you don't believe that the Ackerman
>function can be immplemented in COBOL 85. 

Oh, it can - I have done so - using recursion.

>It can be. 

Yes, using recursion.  When you implement your own stack - then you are using recursion.
Even if you don't call it recursion.  Actually, the space of recursive functions is
identical to the space of functions that can be computed using a register based machine or
a Turing machine - that is a well known fact 

What this shows is  that recursion DOES add value/feature to a programming language, as it
allows to handle recursive problem without having to resort to the nitty gritty details of
stack manioulation, dynamic memory management, etc.  If you state that recursion does NOT
add anything to a languages capabilities, then - why are you programming in COBOL anyways?
Wouldn't it be equivalent to code in Assembler, or, for that matter, in machine code
directly:  COPY CON: MYPGM.EXE

>Again I refer you to the literature which shows the equivalence of all
>the major paradigms in terms of the problems they can solve
>(though not in terms of speed - there are some problems that may
>be significantly slower in a *pure* functional language).

The equivalence of all major paradigms?  Sorry, either my command of the English language
is not as good as I thought, or my AC/BS protector has kicked in
(AC as in a major consulting company, BS as in Baloney)


>
>I will make a deal with you. I will provide a non-recursive
…[10 more quoted lines elided]…
>

Tim, I file the above under "belated April Fool Joke"
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 13)_

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E7A96B.86BFBE98@melbpc.org.au>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com> <38E657B4.FE14B6A6@melbpc.org.au> <1c5ees0910hk2runvj80ls9g72teeatjjt@4ax.com>`

```
This reminds me of the old Monty Python joke where a person pays
to have an argument with someone. They go into the the room and
say, "I'm here for my argument". "No you're not" etc. You
obviously enjoy an argument. 

At this stage everyone agrees I think that with a stack you can
implement a recursive algorithm. You don't need language support
for programs calling themselves to do this. The texts also show
that as long as you have dynamic memory allocation, you can also
implement these algorithms without even the need for a stack. You
don't actually need a stack. You can use a linked list, or a tree
structure. I think it is a stretch to call this recursive. You
might argue a stack is just faking recursion, but a linked
list??? I could do ack with a tree structure, which I think shows
that it does not 'need' recursion.

Without access to some form of unlimited memory, every
deterministic program is just a state machine. In the real world
there are memory limits. Our programs are state machines not
Turing machines. But it is a lot easier in many ways to reason
about programs as though they had unlimited memory.

The interesting thing though is the desirability of recursion as
defined above. I think we both agree that it can be more natural
and cleaner to implement some algorithms using true recursion.
The compiler handles all the book keeping, which you have to do
yourself if you fake it. But some people think recursion is too
dangerous, or that Cobol should only be used for certain
problems, etc. I think recursion is a very useful tool to be used
when appropriate. 

Tim Josling

Volker Bandke wrote:
> 
> I have already stated that reverse engineering the machine code of (e.g. my Ackermann)
…[14 more quoted lines elided]…
> (AC as in a major consulting company, BS as in Baloney)

For example one book I read, he had langauges called 'goto'
'while' 'function' etc, which implemented the different
types/styles/paradigms of programming languages. Provided they
had some in theory unlimited storage area, they can all do the
same thing.

I have seen AC in action too, and their presentations certainly
are buzzword compliant, if that's what you mean. In this case I
think paradigm is quite an appropriate word.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 14)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e7b01e_2@news3.prserv.net>`
- **References:** `<8bmu1j$r0j$1@nntp9.atl.mindspring.net> <20000328214523.02474.00005107@ng-ca1.aol.com> <ui23es4hvgv88ko53p9fe18rnegoq0aeet@4ax.com> <38E1E596.B0DF4314@melbpc.org.au> <bl4ces0d0ta8ahu9e4ofb9nj96reo11adv@4ax.com> <38E657B4.FE14B6A6@melbpc.org.au> <1c5ees0910hk2runvj80ls9g72teeatjjt@4ax.com> <38E7A96B.86BFBE98@melbpc.org.au>`

```

Tim Josling <tej@melbpc.org.au> wrote in message >
>  But some people think recursion is too
> dangerous, or that Cobol should only be used for certain
> problems, etc. I think recursion is a very useful tool to be used
> when appropriate.

absolutely agree. Very useful even if you have to simulate it.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38de38af_2@news3.prserv.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <ue9sdsoqttovlnfq5hqot378pvec7dhh0n@4ax.com>`

```

G Moore <gvwmoore@spam.ix.netcom.com> wrote in message
> the only time i have ever seen a recursive call of any use is in
> building an indexing engine, or game trees.

There are very many instances where a recursive approach
is the right one. Walking trees as you mentioned is a typical
one, because trees are very common in any form of hierarchical
structure. You don't really NEED full support from the language
to use recursion. Here is an example of that:
http://www.etk.com/papers/sorting/pseudor.htm

Leif
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

- **From:** Charles F Hankel <charles@hankel.mersinet.co.uk>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.134a87a7764f23719899e8@news.mersinet.co.uk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net>`

```
I noticed that docdwarf@clark.net as docdwarf@clark.net said...
> In article <8bible$c0i$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
> >In article <8bhkat$621$1@slb2.atl.mindspring.net>,
…[19 more quoted lines elided]…
> trace down a nested IF, right?

Oof, lowest form of wit, etc.  Scope delimiters don't make tracing down a 
nested IF any easier - they just seem to add to the complications that 
are encouraged by punctuation-free code.  If they didn't exist, I 
wouldn't have had a nightmare week back in sunny August with a 300-line 
undocumented heavily-nested IF that caused an 0C7 on a live system - 
there were three of us working on it at one point, just trying to 
disentangle the code - and users screaming for the output.

KISS was about as far from the original programmer's mind as it could 
possibly be.  The real pain was that he had left the company about six 
weeks before to trek off to India with his girlfriend, and was 
untraceable.  So, no thanks from here for scope-delimiters - punctuation 
would have acted as a brake on this sort of coding nightmare with its 
heavy nesting and inline performs.  Some poor b*st*rd has to sort this 
crap out and I was that poor b*st*rd this time.
 
> Come to think of it... if nobody came up with a third-generation language
> we'd all be programming in BAL, as the Pope intended... or still patching
> boards with cords, as the Pope's Boss intended...

My next engagement is application programming in Assembler with some 
COBOL thrown in for variety.  It's like going back thirty years and I 
like the idea.  At the interview I was told that they had already 
interviewed four people and I asked if we all had a full head of hair 
between us.  I didn't think it was that funny but the interviewer got a 
fit of the giggles.
 
> ... pardon my sarcasm, Mr Dilworth, but I trust that it has made my point
> clear; the arguments you have brought forth can be levelled against *any*
> change (notice I did not use the word 'advance') in
> technology.  MRI?  Pfah, exploratory surgery is good enough... after all,
> there are these newfangled anaesthetics!

Change is OK provided that there is a purpose other than change per se.  
So, yes, I'll use intrinsic functions but you can keep your scope 
delimiters, local storage and recursions to yourself, thank you very 
much.  I may be a dinosaur but at least my code works and is easily 
maintainable by all.
 
> Now, if you'll excuse me, I need to code up some ALTERs, a few GO TO
> DEPENDING ONs... and a couple o' 66 RENAMES, just to make sure such things
> do not go softly into the Programmer's Graveyard.

Good idea, mate.  Code that does something instead of satisfying dogma.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PK2E4.9389$0o4.73161@iad-read.news.verio.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk>`

```
In article <MPG.134a87a7764f23719899e8@news.mersinet.co.uk>,
Charles F Hankel  <charles@hankel.mersinet.co.uk> wrote:
>I noticed that docdwarf@clark.net as docdwarf@clark.net said...
>> In article <8bible$c0i$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
…[22 more quoted lines elided]…
>Oof, lowest form of wit, etc.

I thought that a pun was the lowest form of wit... but it seems others
disagree.

>Scope delimiters don't make tracing down a 
>nested IF any easier - they just seem to add to the complications that 
>are encouraged by punctuation-free code.

Ummmmm... *any* kind of code can be written badly, last I looked.

>If they didn't exist, I 
>wouldn't have had a nightmare week back in sunny August with a 300-line 
>undocumented heavily-nested IF that caused an 0C7 on a live system - 
>there were three of us working on it at one point, just trying to 
>disentangle the code - and users screaming for the output.

You might nothave had that particular difficulty, no... but you have had
others, I assume, very nicely and without them.

Call me 'lazy' but I *like* the ability to put a new condition, clearly
and cleanly, inside of a nested mare's-nest of linguine that was written
some time around the Profumo scandal and be able to maintain flow with a
mere END-IF.

(on the other hand... I have been criticised for 'excessive use of
periods/full stops'... there's no pleasing everyone.)

>
>KISS was about as far from the original programmer's mind as it could 
>possibly be.

How far was it from Quality Assurance/Production Implementation's?  Who
let the garbage into Prod?

>The real pain was that he had left the company about six 
>weeks before to trek off to India with his girlfriend, and was 
…[3 more quoted lines elided]…
>crap out and I was that poor b*st*rd this time.

We've all run into bad code and lived to tell the tale... dead coders
don't post to UseNet.

> 
>> Come to think of it... if nobody came up with a third-generation language
…[5 more quoted lines elided]…
>like the idea.

It seems that Mr Dilworth is not alone, then.

>At the interview I was told that they had already 
>interviewed four people and I asked if we all had a full head of hair 
>between us.  I didn't think it was that funny but the interviewer got a 
>fit of the giggles.

As my Respected Father  - whose forehead seemed to start somewhere behind
his ears - said, many times: 'Women, children and eunuchs have hair.'

> 
>> ... pardon my sarcasm, Mr Dilworth, but I trust that it has made my point
…[9 more quoted lines elided]…
>maintainable by all.

I'm sure that was thought by the lad traipsing about the Subcontinent, as
well... as stated previously, any code can be written badly.

> 
>> Now, if you'll excuse me, I need to code up some ALTERs, a few GO TO
…[3 more quoted lines elided]…
>Good idea, mate.  Code that does something instead of satisfying dogma.

But it *does* satisfy dogma... and the dogma is:

IF PROGRAM-RUNS
    PERFORM NEXT-ASSIGNMENT
ELSE
    PERFORM CODE-LIKE-HELL UNTIL DAMNED-THING-WORKS.

DD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E110D5.A672EB80@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net>`

```


docdwarf@clark.net wrote:
> 
> Call me 'lazy' but I *like* the ability to put a new condition, clearly
> and cleanly, inside of a nested mare's-nest of linguine that was written
> some time around the Profumo scandal and be able to maintain flow with a
> mere END-IF.

Phew ! There's an admission of age. No doubt you reflect back on
Christine Keeler and Randy Rice Davies too. Me, when I think of poor
John, I reminisce about his wife Valerie Hobson playing Anna in "The
King and I" at Drury Lane. Just how far back do you go - do you remember
her in the first version of "The Four Feathers" ?

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E115C0.87462BD0@cusys.edu>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com>`

```
"James J. Gavan" wrote:
> 
> docdwarf@clark.net wrote:
…[12 more quoted lines elided]…
> Jimmy

He didn't admit he was coding back then (I don't know if I have even
seen code that old).  As an American, I have to admit that I don't
picture any of the above.  I suppose I saw their faces during the
scandal in the newspaper and TV, but I don't remember.  Back then, we
figured sex scandals were a British thing, our scandals were more likely
to be about money.  If you had mentioned Rice-Davies out of context, I
probably wouldn't have placed her.  (maybe your nickname might have
given me a clue, but I don't know if I ever heard it before).

Back on topic.  If we replaced WORKING-STORAGE by LOCAL-STORAGE in
existing stand-alone programs, wouldn't that be what is normally
desired?  (with no real change in functionality).
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<On43FgQm$GA.307@cpmsnbbsa04>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu>`

```

Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:38E115C0.87462BD0@cusys.edu...
>
> Back on topic.  If we replaced WORKING-STORAGE by LOCAL-STORAGE in
> existing stand-alone programs, wouldn't that be what is normally
> desired?  (with no real change in functionality).

LOCAL-STORAGE is not the same as WORKING-STORAGE.
It would not be a good idea to use it in place of WS.
Additional code is generated to obtain and initialize the LOCAL
storage.
It is meant to be used for recursive programs.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E17CF2.289A8C92@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04>`

```


DennisHarley wrote:
> 
> Howard Brazee <howard.brazee@cusys.edu> wrote in message
…[10 more quoted lines elided]…
> It is meant to be used for recursive programs.

Possibly recursive when using structured - but not with OO - give it
another name 'Temporary Working Storage' - use it then Phoof - gone.

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bs003$59r$1@slb2.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message
news:38E17CF2.289A8C92@home.com...
>
>
…[18 more quoted lines elided]…
> Jimmy

Jimmy,
  Are you certain about this?  My understanding is that "local-storage" is
associated with each iteration of a program.  This means that you get "new
copies" every time that you go one more level deep in iteration.  HOWEVER, as
(if) you "unwind" your application and go back up the iteration chain, that
you get the local storage as it was - when you last "left" that iteration.
This obviously DOES mean that there is some (significant?) overhead in
keeping all your "stack" of local-storages available - until you either get
back to the top of the chain - or somehow tell the world that you never plan
on coming "back" to this iteration.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E27241.7093E7C@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> "James J. Gavan" <jjgavan@home.com> wrote in message
…[33 more quoted lines elided]…
>
 
OK perhaps my comment requires a little clarification - and I'm talking
purely OO. (Just re-read your query - and I think we are saying the
same thing with slightly different words). I think the following example
should cover your query - if not get back and ask me to code some more:-

For obvious reasons I use the "non-nested-method".

-----------------------------------------------------------------------
Structered Program (Syntax.cbl) :-

PROCEDURE DIVISION.                                              
                                                                 
 *> This is taking inches to 3 decimals and converting to Metric 
                                                                 
  invoke Syntax2 "new" returning os-Syntax2                      
  move 1.234 to ws-value                                         
  invoke os-Syntax2 "non-nested-method" using ws-value           
                                        returning ws-metric      
  invoke os-Syntax2 "nested-method"     using ws-value           
                                        returning ws-metric      
  invoke os-Syntax2 "non-nested-method" using ws-value           
                                        returning ws-metric      
  invoke os-Syntax2 "nested-method"     using ws-value           
                                        returning ws-metric      

  *> Both 'iterations' above give you garbage in L/S fields not yet
  *> used in a
method                                                               
  STOP RUN.                                                      

-----------------------------------------------------------------------

Class Syntax2.cbl

*> All the tests below DO display "Counter not numeric" and where I add 
*> to counter they are incremented as indicated

       *>-------------------------------------------------------------
       Method-id. "non-nested-method".
       *>-------------------------------------------------------------
       Local-storage section.
       01 ls-counter                  pic 9(02).
       78 ls-ImptoMet                 value 25.4.
       Linkage section.
       01 lnk-Imperial                pic 9(01)v9(03) comp-3.
       01 lnk-Metric                  pic 9(03)v9(02) comp-3.

       Procedure Division  using     lnk-Imperial
                           returning Lnk-Metric.

          if ls-counter not numeric
             display "Non-Nested - Counter - not numeric"  
          End-if

          compute lnk-Metric rounded = lnk-Imperial * ls-ImptoMet

       Exit Method
       End Method "non-nested-method".
       *>-------------------------------------------------------------
       Method-id. "nested-method".
       *>-------------------------------------------------------------
       Local-storage section.
       01 ls-counter                  pic 9(02).
       01 ls-display                  pic zzz.99.
       78 ls-ImptoMet                 value 25.4.
       01 ls-value                    pic 9(03)v9(02) comp-3.
       Linkage section.
       01 lnk-Imperial                pic 9(01)v9(03) comp-3.
       01 lnk-Metric                  pic 9(03)v9(02) comp-3.

       Procedure Division  using     lnk-Imperial
                           returning Lnk-Metric.

          if ls-counter not numeric
             display "Nested - Counter - not numeric"
          End-if

          move 1 to ls-counter
          invoke self "nested-2" using lnk-Imperial
                                 returning ls-value
          display ls-counter
          move 2 to ls-counter
          invoke self "nested-3" using ls-value
                                 returning ls-display
          move ls-display to lnk-Metric
          display ls-counter
       Exit Method
       End Method "nested-method".
       *>-------------------------------------------------------------
       Method-id. "nested-2".
       *>-------------------------------------------------------------
       Local-storage section.
       01 ls-counter                  pic 9(02).
       01 ls-display                  pic zzz.99.
       78 ls-ImptoMet                 value 25.4.
       Linkage section.
       01 lnk-Imperial                pic 9(01)v9(03) comp-3.
       01 lnk-Metric                  pic 9(03)v9(02) comp-3.

       Procedure Division  using     lnk-Imperial
                           returning Lnk-Metric.

          if ls-counter not numeric
             display "Nested 2 - Counter - not numeric"
          End-if

          compute lnk-Metric rounded = lnk-Imperial * ls-ImptoMet

       Exit Method
       End Method "nested-2".
       *>-------------------------------------------------------------
       Method-id. "nested-3".
       *>-------------------------------------------------------------
       Local-storage section.
       01 ls-counter                  pic 9(02).
       01 ls-display                  pic zzz.99.
       Linkage section.
       01 lnk-Value                   pic 9(03)v9(02) comp-3.
       01 lnk-Display                 pic zzz.99.

       Procedure Division  using     lnk-Value
                           returning Lnk-Display.

          if ls-counter not numeric
             display "Nested 3 - Counter - not numeric"
          End-if

          move lnk-Value to ls-display
          move ls-display to lnk-Display

       Exit Method
       End Method "nested-3".
       *>-------------------------------------------------------------

-----------------------------------------------------------------------

As you correctly observe there is an overhead in keeping tabs on your
Local-storage as you 'climb-back' through the invokes - one reasons why
the M/F documentation says 'keep the list of variables in L/S to a
(minimum) small number'. Still, it works efficiently; invoke
"show-screen" and it pops up at you without any delay.

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 11)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e2811b.63616697@news.cox-internet.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net> <38E27241.7093E7C@home.com>`

```
On Wed, 29 Mar 2000 21:21:19 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[42 more quoted lines elided]…
>

Uh -- the whole "Local Storage" argument is mute in OO.
Working-Storage of a method is local to that method and a new "copy"
is created for every object that is created - it's not shared between
objects.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bu2qb$kg9$1@nntp9.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net> <38E27241.7093E7C@home.com> <38e2811b.63616697@news.cox-internet.com>`

```
"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
  <snip>
> >OK perhaps my comment requires a little clarification - and I'm talking
> >purely OO. (Just re-read your query - and I think we are saying the
…[8 more quoted lines elided]…
>

Thane (and others),
  This seems to be my day for asking "are you certain"?  (Probably showing my
lack of "real" understanding of OO).

According to General Rule 1 of Working-Storage on page 237 (of CD 1.8),

"1) Data items in the working-storage section of a program that does not have
the initial attribute, a function, a factory, an object, or a method are
static data."

which seems to call WS data as "static" for methods.

Compare this to GR1 of Local-Storage on page 238

"1) Data items in the local-storage section are automatic data."

See
  "14.7.1.1.2 Initial and last-used states of data"
(on page 388 for a discussion on automatic vs static data)
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 13)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e2d661.5538892@news.cox-internet.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net> <38E27241.7093E7C@home.com> <38e2811b.63616697@news.cox-internet.com> <8bu2qb$kg9$1@nntp9.atl.mindspring.net>`

```
Posted and mailed.

On Wed, 29 Mar 2000 17:14:57 -0600, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>> Uh -- the whole "Local Storage" argument is mute in OO.
>> Working-Storage of a method is local to that method and a new "copy"
…[15 more quoted lines elided]…
>

Ok, I made an assumption - and in my experiments it appears I am
right.  With MF OO there is Object-Storage.  The standard has no such
animal - they simply use Working-Storage when coding a class.  Now,
when I invoke the "New" method I should get a completely new copy of
Working storage - this is the objects data, it must be protected.  And
so I experimented - This is the case.  WS is in first used state upon
each NEW invocation, and in each existing object it is in last uses
state.  So changing a WS item on one object won't change data in
another - that is important and required by OO.  

So let's re-read your excerpt.... (Scrolling up and back down)....

It says it is static ONLY if it does not have a Method, Object,
Factory etc - in OO you obviously DO have a Method- that tells me that
for METHODS WS is "Automatic".  Each instance of the object gets new
WS.  

Do you agree?
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 14)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bumev$kf2$1@nntp9.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net> <38E27241.7093E7C@home.com> <38e2811b.63616697@news.cox-internet.com> <8bu2qb$kg9$1@nntp9.atl.mindspring.net> <38e2d661.5538892@news.cox-internet.com>`

```
Thane, I think (but am not positive) that you are missing the significance
(that is fairly well hidden) of a comma.   I *believe* that the rule is
intended to be parsed as:

"1) Data items in the working-storage section of a program that does not have
the initial attribute,

>>  or data items in the working-storage section of

a function, a factory, an object, or a method

are static data."

Compare page 388 which states,

"Static data is placed in the initial state:
1) The first time the function, method, or program in which it is described
is activated in a run unit."
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 15)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e39198.53473842@news.cox-internet.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net> <38E27241.7093E7C@home.com> <38e2811b.63616697@news.cox-internet.com> <8bu2qb$kg9$1@nntp9.atl.mindspring.net> <38e2d661.5538892@news.cox-internet.com> <8bumev$kf2$1@nntp9.atl.mindspring.net>`

```
On Wed, 29 Mar 2000 22:49:54 -0600, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>Thane, I think (but am not positive) that you are missing the significance
>(that is fairly well hidden) of a comma.   I *believe* that the rule is
>intended to be parsed as:
>

Bill and I had a long drawn out conversation via email last night
about this.  It appears that Working-Storage is always static unless
INITIAL is specified.  

That said - Multiple instances of an object get separate new copies of
Working-Storage.  Changing the value of a working-storage item in one
object instance does not change the corresponding value in another
instance of the same object.

Bill has asked J4 for an interpretation on the questionable
documentation and is forwarding a detailed request from me to confirm
that indeed separate instances of the same object get separate (but
still static within that instance) working-storage.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E1FB5C.6D3078EB@zip.com.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> 
…[10 more quoted lines elided]…
> on coming "back" to this iteration.

I trust not.  Could we get a clarification on this.

I would expect that the local storage would be initialized on every
entry.  How the compiler vendor implements the stack is their own
concern. I would find it unlikely that they do not use the stack to do
this, in which case the data on the stack would be from the last call
which may or may not be the module in question.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bu3ad$khr$1@nntp9.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net> <38E1FB5C.6D3078EB@zip.com.au>`

```
"14.7.1.1.2.2 Last-used"  on page 389 (of CD 1.8) states,
   "Static and external data are the only data that are in the last-used
state. External data is always in the last-used state except when the run
unit is activated. Static data is in the last-used state except when it is in
the initial state as defined above."

Page 238 states,
  "The local-storage section describes automatic data."

Therefore, it does appear that I was wrong and locale-storage data is NOT in
"last used state".  There is some other statements that make me think that
there MIGHT be conflicting statements about data in "activated" elements -
but I think this at least answers the INTENT of the draft.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bu5cf$gj9$1@slb7.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <38E115C0.87462BD0@cusys.edu> <On43FgQm$GA.307@cpmsnbbsa04> <38E17CF2.289A8C92@home.com> <8bs003$59r$1@slb2.atl.mindspring.net> <38E1FB5C.6D3078EB@zip.com.au> <8bu3ad$khr$1@nntp9.atl.mindspring.net>`

```
(worse that "talking to myself" - I am telling myself that I was WRONG <G>)

After further review of the draft revision, I am BACK saying that you do get
your "local-storage" as you left it (not called "last used state") when you
"unwind" your way up thru multiple instances.

Page 114 (of CD 1.8) makes this clear when it states,

"Data items defined in the local-storage section are automatic items. They
are set to their initial state each time the runtime element containing them
is activated. Each activated instance of the runtime element has its own copy
of the item, which persists while the runtime element is in active state."

When you combine this with the statement on page 387,
  "A function, method, or program may be activated recursively. Therefore,
several instances of a function, method, or program may be active at once.
When a rule indicates that the active state of a runtime element is tested,
it is in the active state if any instance of the element is active."

It becomes clear (at least to me) that a conforming implementation MUST keep
the values of local-storage items UNTIL that specific instance is "exited"
(or the whole run unit is stopped).
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G39E4.9459$0o4.75318@iad-read.news.verio.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com>`

```
In article <38E110D5.A672EB80@home.com>,
James J. Gavan <jjgavan@home.com> wrote:
>
>
…[7 more quoted lines elided]…
>Phew ! There's an admission of age.

Not necessarily... perhaps it is just the odd bit of period-reference.

>No doubt you reflect back on
>Christine Keeler and Randy Rice Davies too.

Christine Keeler?  Pfah, a mere child... now *Ruby* Keeler, *there* was a
gal!  A hoofer with a heart of gold and a set of gams from here to
Saskatoon... ahhhh, I can see her now, beltin' out a ditty about little
'nifties', from the '50's, innocent and sweet... shady ladies, from the
'80's, who are indiscrete!  They're side-by-side, they're glorified, where
the underworld can meet the elite... Forty-Second Street!

Ahem... sorry, don't know what came over me... now, what were you saying?

DD
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1356854bf55199559896a9@news.freedombird.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net> <38E110D5.A672EB80@home.com> <G39E4.9459$0o4.75318@iad-read.news.verio.net>`

```
I noticed that docdwarf@clark.net as docdwarf@clark.net said...
> In article <38E110D5.A672EB80@home.com>,
> James J. Gavan <jjgavan@home.com> wrote:
…[16 more quoted lines elided]…
> Christine Keeler?

She was on tv a few months ago, still a good-looking woman, what they 
call around here a "fit bird".
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.13568491900b34249896a8@news.freedombird.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <PK2E4.9389$0o4.73161@iad-read.news.verio.net>`

```
I noticed that docdwarf@clark.net as docdwarf@clark.net said...
> In article <MPG.134a87a7764f23719899e8@news.mersinet.co.uk>,
> Charles F Hankel  <charles@hankel.mersinet.co.uk> wrote:
…[11 more quoted lines elided]…
> disagree.

There's saying over here that sarcasm is the lowest form of wit, not 
that it stops it being funny.
 
> >Scope delimiters don't make tracing down a 
> >nested IF any easier - they just seem to add to the complications that 
> >are encouraged by punctuation-free code.
> 
> Ummmmm... *any* kind of code can be written badly, last I looked.

For sure, but having to punctuate it does lay down a few limitations IMO.
 
> >If they didn't exist, I 
> >wouldn't have had a nightmare week back in sunny August with a 300-line 
…[13 more quoted lines elided]…
> periods/full stops'... there's no pleasing everyone.)

How could proper use possibly be considered excessive? :)
 
> >KISS was about as far from the original programmer's mind as it could 
> >possibly be.
> 
> How far was it from Quality Assurance/Production Implementation's?  Who
> let the garbage into Prod?

QA?  You're kidding - this was on a site where the major (only?) 
development effort was being undertaken by a bunch of Oracle consultants 
who hadn't even got the basic concepts of inter-system communication.  
When I mentioned that there were three of us involved in untangling the 
code, perhaps I should have mentioned that we were the mainframe support 
- there wasn't anyone else.  The company is a large multinational whose 
products are household names in most countries.
 
> We've all run into bad code and lived to tell the tale... dead coders
> don't post to UseNet.

Thanks - it proves I'm still kicking.

> >> Come to think of it... if nobody came up with a third-generation language
> >> we'd all be programming in BAL, as the Pope intended... or still patching
…[6 more quoted lines elided]…
> It seems that Mr Dilworth is not alone, then.

It's a perversion, maybe, and it's on the payroll too.  I haven't been on 
the payroll anywhere since 1976 so it's all a bit of an adventure.  On 
Monday I have to fly to London for "induction" and on Friday, the 
company's having a jolly somewhere else.  If being on the payroll means 
three-day weeks and being paid for jaunting around the country, then it's 
a life I might like to get used to.  I'll let you know after payday.
 
> >At the interview I was told that they had already 
> >interviewed four people and I asked if we all had a full head of hair 
…[4 more quoted lines elided]…
> his ears - said, many times: 'Women, children and eunuchs have hair.'

A wise man, your father.
 
> >> Now, if you'll excuse me, I need to code up some ALTERs, a few GO TO
> >> DEPENDING ONs... and a couple o' 66 RENAMES, just to make sure such things
…[9 more quoted lines elided]…
>     PERFORM CODE-LIKE-HELL UNTIL DAMNED-THING-WORKS.

Touch�!  I can only agree with that statement.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage-getting OT

_(reply depth: 4)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f5k2ess9qg7e076smbmt91kt9c6ku65khb@4ax.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk>`

```
Charles F Hankel <charles@hankel.mersinet.co.uk> wrote:

>My next engagement is application programming in Assembler with some 
>COBOL thrown in for variety.  It's like going back thirty years and I 
>like the idea.

assembler... blecch. the only use i have ever had for assembler is
knowing how to read it. can't write it worth a damn, but can port it
to compiler-specific c (sure, you have the same portability problems,
but you get the economic advantage of more programmers).

i don't think there will ever be a language which doesn't require a
3rd gen programmer somewhere. and i know all the embedded chips surely
don't work in 4th gen programming.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage-getting OT

_(reply depth: 5)_

- **From:** Charles F Hankel <charles@hankel.freedombird.net>
- **Date:** 2000-04-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1351dc651efe2eb989a50@news.mersinet.co.uk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <f5k2ess9qg7e076smbmt91kt9c6ku65khb@4ax.com>`

```
I noticed that G Moore as gvwmoore@spam.ix.netcom.com said...
> Charles F Hankel <charles@hankel.mersinet.co.uk> wrote:
> 
…[11 more quoted lines elided]…
> don't work in 4th gen programming.

Well, I start next week and I'm quite looking forward to it.  During the 
interview, one of the ladies (all my interviewers were ladies) said that 
they had been surprised by the number of people who had applied.  I was 
the last of six men to be interviewed and asked if we, the applicants, 
were able to summon up a full head of hair between us.  It sort of put 
her off the next question.  It seemed that all applicants were of a 
certain age.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage-getting OT

_(reply depth: 5)_

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.135686bd912e9d829896aa@news.freedombird.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <f5k2ess9qg7e076smbmt91kt9c6ku65khb@4ax.com>`

```
I noticed that G Moore as gvwmoore@spam.ix.netcom.com said...
> Charles F Hankel <charles@hankel.mersinet.co.uk> wrote:
> 
…[7 more quoted lines elided]…
> but you get the economic advantage of more programmers).

I should point out that it's S/370 Assembler, which is a whole lot easier 
to work with than every other assembler that I've seen.  For a start 
there's an excellent tutorial/manual called Principles Of Operation that 
makes good reading - often better than the Language Reference.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage-getting OT

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cie23$aqt$1@slb1.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <f5k2ess9qg7e076smbmt91kt9c6ku65khb@4ax.com> <MPG.135686bd912e9d829896aa@news.freedombird.net>`

```
Probably "off-topic" - but are you going to be using HLASM?  I have heard
that it does make S/390 coding a LOT easier than Assembler H/F, etc.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage-getting OT

_(reply depth: 7)_

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1357aeaceab53cb89896b5@news.freedombird.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <st5D4.7567$0o4.54457@iad-read.news.verio.net> <MPG.134a87a7764f23719899e8@news.mersinet.co.uk> <f5k2ess9qg7e076smbmt91kt9c6ku65khb@4ax.com> <MPG.135686bd912e9d829896aa@news.freedombird.net> <8cie23$aqt$1@slb1.atl.mindspring.net>`

```
I noticed that William M. Klein as wmklein@nospam.ix.netcom.com said...
> Probably "off-topic" - but are you going to be using HLASM?  I have heard
> that it does make S/390 coding a LOT easier than Assembler H/F, etc.

There was no direct mention of it at the interviews except from me.  They 
never flinched, so I can only assume that it isn't unknown.  The project 
is maintaining a system that was written in the late 60s/early 70s, along 
with the usual business changes, while another super-hip one is developed 
by the Department of Terribly Bright Ideas.  Apparently it's mainly 
Assembler with some more modern modules in COBOL but the main requirement 
in the job advert was for Assembler applications people and I thought it 
might be nice change, totally unrelated to a couple of private projects 
that I've got on the go.
```

##### ↳ ↳ Re: working-storage vs. local-storage

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bj2c8$j6g$1@news.inet.tele.dk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com>`

```
Inspired from the other answers you've got, I can add this with a smile:

Yes the DP world is a mess, and the mess is caused by the people in the DP
world - you, I and a few other nice fellows around. We are asking for new
features in our favorite language, and when we get them, somebody (as you
did) will say 'Do we need it'. If we want to isolate the data for a certain
process, the answer is YES.

In this strange (PC)world we went from character based personal systems to
GUI applications for multi-user environments. In that process we re-evented
the multi-session and multi-tasking techniques and suddenly somebody cried
'OO'. In that process one of the other guys in this funny DP world needed to
run recursive calls with paired data to each call. Then they evented the
Local-Storage. I am trying to live with that.

- Remember, the DP world is us, and we mess it up.
- Y2K problems are bugs, and we put them there.
- Computers are stupid, until we make them completely worthless.
- Lazy programmers need large computers. Large computers enables the
programmers to become even     more lazy - I'm quit dizzy when I think too
much about the business.

The DP world is also a free world. I could use Local Storage if I needed to,
but I would never ever pollute my programs with an ALTER.

Neither would I use nested IF's in many levels. If you are on call, you do
not need an enemy, if you have friends to fill the programs with nested
IF's. At 3 o'clock in the morning you don't like  a data-exception in a
10-level nested IF messed up with ELSE on 23 pages of code. Yeah. we are
messing up the DP world ourselves.

Talking about being dizzy:
Did any of you ever tell mr. Gates what we need?
Did anyone ever tell IBM what we need?
Did any of you ever tell anyone in Taipei or Silicon Valley what we need
from a computer?

Let me help you - the answer is NO. But we get computers don't we? If I want
a green one, I can buy a Mac. If I do not like a Mac, I can get a gray one,
saying 'access violation' or 'requested program is not responding....'.

The world belongs to 'Billy Windoza' and whenever he allows me to, I will
love Cobol - even with Local-Storage.

Sorry, but I needed this - I'm calm now.

Regards
Ib

Foodman skrev i meddelelsen <8bible$c0i$1@nnrp1.deja.com>...
>In article <8bhkat$621$1@slb2.atl.mindspring.net>,
>"Frank Swarbrick" <infocat@sprynet.com> wrote:
…[28 more quoted lines elided]…
>Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bja17$djg$1@slb6.atl.mindspring.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk>`

```

"Ib Tanding" <ib@tanding.dk> wrote in message
news:8bj2c8$j6g$1@news.inet.tele.dk...
 <much snipage>
>
> Talking about being dizzy:
…[5 more quoted lines elided]…
> Let me help you - the answer is NO. But we get computers don't we? If I
want
> a green one, I can buy a Mac. If I do not like a Mac, I can get a gray one,
> saying 'access violation' or 'requested program is not responding....'.
>

The answer is that YES (as far as IBM goes) they have had for DECADES user
groups that submit requirements.  I have written more than my fair share of
them.  They also provide the REQUEST facility for entering "user requests".

Please see separate thread about how users SHOULD find out how to create
"enhancement requests" for their "vendor of choice" - AND should use this
facility.

Vendors *do* listen - but are not "mind readers".
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bjlnq$43i$1@news.inet.tele.dk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8bja17$djg$1@slb6.atl.mindspring.net>`

```
You are right there. IBM do listen.

Remember AD-Cycle. The concept were designed to protect business. The
majority of customers told (not asked) IBM to show the way, or they would
invest elsewhere. It lived because of the users, but died when the new
chairman began to listen to share-holders instead of users.

Remember all the nice IBM dialects or rather non standard language features.
You must admit that IBM in the past didn't care much for ISO or ANSI
standards - we got a set of IBM standards. Still they had the nerve to talk
about compatibility.

Nowadays IBM is much more open for impulses from the surrounding world, and
I think, they learned it the hard way. I even believe that the process
started with AD-Cycle and all the red-books.

IBM will always be exactly where the money are. I know about a very old
female profession with the same view upon business. Customers have to pay a
fortune to be satisfied - special requests can be taken care of if the
customer is willing to pay even more.

Regards
Ib


William M. Klein skrev i meddelelsen
<8bja17$djg$1@slb6.atl.mindspring.net>...
>
>"Ib Tanding" <ib@tanding.dk> wrote in message
…[11 more quoted lines elided]…
>> a green one, I can buy a Mac. If I do not like a Mac, I can get a gray
one,
>> saying 'access violation' or 'requested program is not responding....'.
>>
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e3a4ac.15051476@news.epix.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8bja17$djg$1@slb6.atl.mindspring.net> <8bjlnq$43i$1@news.inet.tele.dk>`

```
"Ib Tanding" <ib@tanding.dk> wrote:

[snip]
>
>IBM will always be exactly where the money are. I know about a very old
>female profession with the same view upon business. Customers have to pay a
>fortune to be satisfied - special requests can be taken care of if the
>customer is willing to pay even more.

Ib:

Are you speaking of waitresses in expensive restaurants?

;-)

...sorry, couldn't resist!


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c4loh$6ad$1@news.inet.tele.dk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8bja17$djg$1@slb6.atl.mindspring.net> <8bjlnq$43i$1@news.inet.tele.dk> <38e3a4ac.15051476@news.epix.net>`

```
I can see that you are a noble person. It could be your version - Kids could
be reading the newsgroup.
But when I think about it. Your version might fit in. Customers will have to
wait a long time to be served - yeah it could be.

Ib

Bob Wolfe skrev i meddelelsen <38e3a4ac.15051476@news.epix.net>...
>"Ib Tanding" <ib@tanding.dk> wrote:
>
…[3 more quoted lines elided]…
>>female profession with the same view upon business. Customers have to pay
a
>>fortune to be satisfied - special requests can be taken care of if the
>>customer is willing to pay even more.
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DD4A79.E737EC27@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk>`

```


Ib Tanding wrote:
> 
> Talking about being dizzy:
> Did any of you ever tell mr. Gates what we need?

Well kinda. Back when I was using MS/COBOL had a problem. Phoned support
in Ontario. No reply. So two weeks later phone again. 'Send your problem
on a diskette'. Two weeks later - still no reply. Phoned again, 'Haven't
got your diskette'.

Now I was r-e-a-l-l-y  pissed. What's that guy called, oh yes Gates.
(Didn't know he already had enough greenbacks to paper over Mt. St
Helens to stop it ever blowing its top). So looking at the map and
seeing the guy lives there in the sunshine S.W. of me, I phone. "Can I
please speak to Mr. Gates ?". For real, I actually got his secretary who
deftly fielded the query and said she would get back to me.

Hot shot trouble-shooter gets on phone and makes damn sure I get the
answer I was after. Regrettably I think the guy in Ontario got the shove
- sorry, but I'd paid my bucks and wanted answers.

Would've been nice to say to Bill, "Your support is the pits" - but the
message got there anyway.

So now back to your point - why should I phone Billy G. because of what
I want in COBOL ? He can bugger around as much as he wants with his
Windows. I want to talk to COBOL people. And in COBOL nobody but nobody
ever asked me what I wanted (and I'm thinking primarily about snail-mail
days) - until - Merant sent a questionnaire out last year - good for
them.

Communication is a two-way street - and to those who wish to continue
negatively bitching - get with it and make positive suggestions to
vendors, J4 or WG4, ISO etc.

	There once was a Scanda name of Ib
	Truth is he ne'er told a fib
	Could kinda get a little tizzy
	And that made him kinda dizzy
	So his Trollish friends did suggest
	More in seriousness than in jest
	A Troll-like circle we shall form
	This will follow our Scanda norm
	Hands we join in expectation
	Six turns back, reversed rotation
	Then six, for foward motivation

	Hey ! He aint dizzy no more !	(Name of poet unknown)

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bjotr$dqn$1@news.inet.tele.dk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <38DD4A79.E737EC27@home.com>`

```
I wonder if somebody assisted the 'unknown' poet with some of the rimes.  It
was fun, and I will keep it.

Well, my point about 'questions never asked' was this.

When new features, designs or products are born, we often say 'why' or 'do
we need that?'. In a very short period of time, the marketing tells you that
you cannot live without it. Eventually you buy it, but the quality is not
what you expected.

Now, you cannot get to the boss himself, and the vendor cannot find the time
to answer all the angry letters from customers so they go for the standard
procedure in that situation - they start a user-group. Now they can reply
all the angry letters with 'Thank you so much for your interest in our new
product......' and 'do not disturb us - write to the user-group (while we
count our money)'.

All respectable products in this business have their very own user-group.
Dedicated people who works half a lifetime for free. A few years after the
first release, the product name is what's left - the quality is remarkably
improved, thanks to all the free resources,

If vendors created user-groups to assist in the design phase, they could
produce higher quality for the initial release. Why isn't it so? We do it
all the time, when we create programs for customers.

Regards
Ib
BTW: I will be away for a week. I will spend some days at Merant in Newbury
and some nights in The Lion in West Street.


James J. Gavan skrev i meddelelsen <38DD4A79.E737EC27@home.com>...
>
>
…[49 more quoted lines elided]…
>Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8blpit$rs3$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk>`

```
In article <8bj2c8$j6g$1@news.inet.tele.dk>,
"Ib Tanding" <ib@tanding.dk> wrote:
> Inspired from the other answers you've got, I can add this with a
smile:
>
> Yes the DP world is a mess, and the mess is caused by the people in
the DP
> world - you, I and a few other nice fellows around. We are asking for
new
> features in our favorite language, and when we get them, somebody (as
you
> did) will say 'Do we need it'. If we want to isolate the data for a
certain
> process, the answer is YES.


Sorry, but why would one want to 'isolate the data' in the first place
and to 'isolate' it from what?


>
> In this strange (PC)world we went from character based personal
systems to
> GUI applications for multi-user environments. In that process we re-
evented
> the multi-session and multi-tasking techniques and suddenly somebody



Surely, 'multi-session' and 'multi-tasking' are OS functions and not
application functions - please explain if otherwise.



cried
> 'OO'. In that process one of the other guys in this funny DP world
needed to
> run recursive calls with paired data to each call. Then they evented
the
> Local-Storage.


But, why did they do that? Show me the advantage.



> The DP world is also a free world. I could use Local Storage if I
needed to,

But then, your successor would need to know how to use it too. The DP
world is not free if you work for someone else.  For sure, any
programmer working for me would use only what I allowed, we don't pay
programmers to explore their horizons, or do we?

> but I would never ever pollute my programs with an ALTER.


Neither would any normal person.


>
> Neither would I use nested IF's in many levels.


Nor would I.


 If you are on call, you do
> not need an enemy, if you have friends to fill the programs with
nested
> IF's. At 3 o'clock in the morning you don't like a data-exception in a
> 10-level nested IF messed up with ELSE on 23 pages of code.


If the system had been properly designed and programmed, it wouldn't
require these 3 o'clock calls.



> Did any of you ever tell mr. Gates what we need?


Probably not, but he wouldn't get it anyway. Even if he did get it
he wouldn't like it.



> Did anyone ever tell IBM what we need?


IBM, being a hardware manufacturer first and foremost, wants
their customers to stick to their hardware.  They could do that
by making their software incompatible with everyone elses and too
expensive to convert to something else.



> Did any of you ever tell anyone in Taipei or Silicon Valley what we
need
> from a computer?


Computers are like screwdrivers and hammers. You can build houses
with screwdrivers and hammers. The basic instruction set on any
computer would do everything that a COBOL programmer might want to
do.



>
> Let me help you - the answer is NO. But we get computers don't we? If
I want
> a green one, I can buy a Mac. If I do not like a Mac, I can get a
gray one,
> saying 'access violation' or 'requested program is not
responding....'.


Actually, I got a black one but it still did those things...



>
> The world belongs to 'Billy Windoza' and whenever he allows me to, I
will
> love Cobol - even with Local-Storage.
>
> Sorry, but I needed this - I'm calm now.
>


Yeah, you're calm, what about everybody else?

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38df8f4a.1603834955@news.cox-internet.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com>`

```
On Sun, 26 Mar 2000 19:48:47 GMT, Foodman <foodman123@aol.com> wrote:

 
>Sorry, but why would one want to 'isolate the data' in the first place
>and to 'isolate' it from what?
>
>

I want to isolate it from me, and from you.  I don't want you touching
my data while I am working with it.  Of all the "early morning"
telephone calls I have ever had, 90% of them have not been Blatant
bugs, but instead are data dependant errors that cause a certain wierd
set of conditions to execute is a certain wierd order that causes a
certain wierd result.  Different data no bug.   Often the error is not
in the code exhibiting symptoms.  Many times it is in seemingly
unrelated code that is called, or used via copy book, or in some
strange prepatory step where somone changed a data item, or a layout,
without realizing the ramifications.  I see this all the them.

THIS is what OO can help cure, via data hiding and common methods to
access this data.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bobd7$k1o$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com>`

```
In article <38df8f4a.1603834955@news.cox-internet.com>,
thaneH@softwaresimple.com (Thane Hubbell) wrote:
>
> I want to isolate it from me, and from you. I don't want you touching
> my data while I am working with it.


Hi Thane:

I don't want to be more cantankerous than usual, but, I don't
know how I can get at your data. If your data is in your data
division, how could I get at it?  If your data is in a file, then
you would lock it until you were done.

No?

Thanks

Tony Dilworth

>
> THIS is what OO can help cure, via data hiding and common methods to
> access this data.
>
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E0A2D6.29FD1E13@zip.com.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <8bobd7$k1o$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> I don't want to be more cantankerous than usual, but, I don't
> know how I can get at your data. If your data is in your data
> division, how could I get at it?  If your data is in a file, then
> you would lock it until you were done.

The problem is of protection.  If I code up a solution and include an
open interface to my data.  I then work out a totally different
algorithm with different data patterns.  However you have used some of
the data in my routine for your own purposes.  I cannot now replace
the algorithm, I have to duplicate the solution and slowly migrate the
code across.

I cannot really think of a great example but here is what I protect:

I am writing a fairly complex sort.  I pass the information for a
record and a key for the record.  Once I have processed all keys I
optimize the sort, and then call a function that returns the keys one
by one.

The method of the sort is totally hidden. If I need two of these sorts
in a program concurrently, I cannot use a routine with hidden working
storage method anymore.  Using routines I must pass enough information
for me to continue processing based upon the list passed.  I have
exposed my private data.  OO I can create an object which combines
routines and data together and I can have more than one.  This makes
it very easy to create multiple instances of my above sort.  The data
is implicitly passed with the routine calls and is not exposed to your
program where you might make assumptions on the process that breaks
later.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e0dafe.1688763946@news.cox-internet.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <8bobd7$k1o$1@nnrp1.deja.com>`

```
On Mon, 27 Mar 2000 19:05:25 GMT, Foodman <foodman123@aol.com> wrote:

>In article <38df8f4a.1603834955@news.cox-internet.com>,
>thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[12 more quoted lines elided]…
>No?

It's a maintenance issue.  With one shared area of WS you are free to
come into the program later, changing something unrelated, but using
one of my existing working-storage items.  *I* could even do that -
doesn't have to be a different programmer.   And I'll break my own
code.  I HAVE done this - on numerous occasions actually.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bqu4j$gc4$1@nnrp1.deja.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <8bobd7$k1o$1@nnrp1.deja.com> <38e0dafe.1688763946@news.cox-internet.com>`

```
In article <38e0dafe.1688763946@news.cox-internet.com>,
thaneH@softwaresimple.com (Thane Hubbell) wrote:
>
> It's a maintenance issue. With one shared area of WS you are free to
…[4 more quoted lines elided]…
>

Hi (feeling dense):

Sorry, I didn't know you were talking about sharing source code.

I have 'one shared area of WS' which I have used since the sixties.
It contains common things required in every program, like subscripts,
date and time fields, page counts, commonly-used edited fields, work
areas for standard subroutines, etc. It is automatically included in
every program ever written by me and my cohorts (when I had any).

Certainly, going in willy-nilly and changing something in that copy
could have unkown consequences elsewhere when those elsewheres were
recompiled. However, it is forbidden to make changes to that copy for
any reason without permission from Authority.

To avoid the situation you describe, without resorting to OO, would
be to physically insert the standard copy into your NEW program when
first written which would allow you to change stuff as required (but it
shouldn't be required) in that program's 'private' copy. The master
copy is never changed and never COPIED at compile-time. Sure, there
may be disadvantages to this, but I can't think of any which don't
have simple solutions.


Based on what I have read and failed to comprehend about OO so far,
and given the desire to solve the problem you describe, that is what
I would do.


Thanks

Tony Dilworth




Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E11323.4C46F42D@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <8bobd7$k1o$1@nnrp1.deja.com> <38e0dafe.1688763946@news.cox-internet.com> <8bqu4j$gc4$1@nnrp1.deja.com>`

```


Foodman wrote:
> 
> In article <38e0dafe.1688763946@news.cox-internet.com>,
…[4 more quoted lines elided]…
> I would do.

Put it this way - OO is not a religion. So far as COBOL is concerned it
does add some new features, (agreed, they are paralleled in structured).
My own thoughts are that it offers some additiional flexibility.

You take your pick and make your choices - and you aren't destined for
the stake if you don't buy into it.

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 9)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E12486.D9373F10@cusys.edu>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <8bobd7$k1o$1@nnrp1.deja.com> <38e0dafe.1688763946@news.cox-internet.com> <8bqu4j$gc4$1@nnrp1.deja.com> <38E11323.4C46F42D@home.com>`

```
"James J. Gavan" wrote:
> 
> Put it this way - OO is not a religion. So far as COBOL is concerned it
> does add some new features, (agreed, they are paralleled in structured).
> My own thoughts are that it offers some additiional flexibility.

I am wondering though what the net effect will be of this migration of
Cobol towards the OO standards.  Will significant amounts of shops
decide Cobol is the best tool because it has these features? 

If they are not now using Cobol, will it now be a consideration?

If they have trained Cobol programmers, will they be more likely to pick
OO Cobol over a different, more "contemporary" language?

I suppose it depends on how they perceive the labor market to be more
than anything else.  I don't see that there is a significant advantage
in having old Cobol programmers going to OO Cobol vs Java - the learning
curve won't be that different - and with turnover it may be easier to
find new Java programmers.

Do they care which language actually does a better job?  Probably -
especially which one is easier to maintain.  But do they have the facts
to make this determination and to put a value on it?  I doubt it.

Does this change process make decision makers think Cobol is vibrant and
current, or that it is desperately playing catch-up?

Or does it make any difference whatsoever as companies go more towards
turnkey solutions and datamart tools?
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E17C63.7761B66D@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <8bobd7$k1o$1@nnrp1.deja.com> <38e0dafe.1688763946@news.cox-internet.com> <8bqu4j$gc4$1@nnrp1.deja.com> <38E11323.4C46F42D@home.com> <38E12486.D9373F10@cusys.edu>`

```


Howard Brazee wrote:
> 
> "James J. Gavan" wrote:
…[28 more quoted lines elided]…
> turnkey solutions and datamart tools?

Two issues Howard :

(1) COBOL is always playing catch-up. Don't want to labour it, but until
the Standards procedure is faster ???? Meanwhile people are looking for
tools to talk to - Windows. That's what the 'newer' languages responded
to. So we've lost a lot of potential COBOL developers - and no I don't
think they will dramatically switch back to COBOL even with OO type
enhancements.

(2) DataMarts - I'm speaking now as a 'systems' man not a programmer. I
just don't buy into the DataMart thing - small users yes, where they are
prepared to take 'generics' - but the Walmarts, Safeways etc. who have
to have aggressive marketing - jut doesn't cut it.

Give you a simple example about 'customized' - back in my Department
store days. New Food A/P system - I proposed the system should allow you
to enter data as received and THEN - per vendor record, you put how many
weeks to cycle it before we paid. One large dairy company we bought only
yogurt from and paid them every week - BUT - we paid them some 20 weeks
LATER after the original product had been sold 19 weeks EARLIER. The
accountants blanched at the suggestion - the Food Director was thrilled
- real nice on our cash flow.

You just aren't going to get that type of cut and thrust from Datamarts.
(Was it ethical - yes - if the vendor was too bloody stupid not to have
a better control on his A/R).

BTW - The dairy company wasn't Unigate that I had moved from - they
latched on straight away  - sent us invoices attached to a WEEKLY
statement - pay up or else :-). On a visit I made subsequently they
grinned and told me they knew who had introduced that particular 'twist'
!

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 10)_

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81k2esklv5b0kj31ks9qk597pb18p0l979@4ax.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <8bobd7$k1o$1@nnrp1.deja.com> <38e0dafe.1688763946@news.cox-internet.com> <8bqu4j$gc4$1@nnrp1.deja.com> <38E11323.4C46F42D@home.com> <38E12486.D9373F10@cusys.edu>`

```
Howard Brazee <howard.brazee@cusys.edu> wrote:

>I am wondering though what the net effect will be of this migration of
>Cobol towards the OO standards.  Will significant amounts of shops
>decide Cobol is the best tool because it has these features? 

the net effect will be the use of linkage, local , thread storage
sections, calls (i don't think many people will use method syntax
anytime soon (i know i won't)), and evaluate compiler-version.

local storage is good, as is linkage section, and might eventually
drive out the working-storage section (local would store the variables
per thread, and linkage would be called globally).

strangely enough, i have never used 88, 77, or 66 level variables, so
i also don't see a future in the set-variable oo clause (and i hope j4
doesn't put it in).

if a linkage call by content or value has multiple (prepare for oo
buzzword) instances of data, i don't see the point of local storage
period.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e2215e.39103498@news.cox-internet.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <8bobd7$k1o$1@nnrp1.deja.com> <38e0dafe.1688763946@news.cox-internet.com> <8bqu4j$gc4$1@nnrp1.deja.com>`

```
On Tue, 28 Mar 2000 18:37:09 GMT, Foodman <foodman123@aol.com> wrote:

>In article <38e0dafe.1688763946@news.cox-internet.com>,
>thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[22 more quoted lines elided]…
>

We are almost there.  I am talking about some portion of a program
recieveing maintenance that changes a VALUE of a WS item that I depend
on in my routine, causing my routine to break even though not one line
of source code was changed in my routine.  This kind of thing happens
all the time.  A WS copybook won't fix it.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 5)_

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E0B4A4.CFB076B7@iinet.net.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com>`

```

Thane Hubbell wrote:
> 
> THIS is what OO can help cure, via data hiding and common methods to
> access this data.
However, one of my pet peeves about OO, is that most OO languages force you
to set the hidden data by invoking methods. This is not a problem in itself,
but when you have an object with 50 data elements and you need 50 methods to
set the data and 50 methods to retrieve the data, then this is clearly getting
out of hand.

I'm not totally up to date with the COBOL OO language spec, but if there was a
way to do the equivalent of:

	Call Set_Private_Data Using
		Data_element1
		...
		Data_element50

Then this would be a good thing.

By the way, there is nothing to stop you from doing data verification calls
from the Set_Private_Data, just as you can put the verification into each of
the 50 set data methods.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38e0e6ee.1691820395@news.cox-internet.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <38E0B4A4.CFB076B7@iinet.net.au>`

```
On Tue, 28 Mar 2000 21:33:24 +0800, Joseph Katnic
<josephk@iinet.net.au> wrote:

>
>Thane Hubbell wrote:
…[8 more quoted lines elided]…
>

COBOL has the advantage of seeing the mistakes and poor
implementations from other languages, as well as what has been done
well.  To set and get properties in COBOL all you need to do is a
simple MOVE.  It's painless.
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E10EDE.7C2A8338@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <38E0B4A4.CFB076B7@iinet.net.au>`

```


Joseph Katnic wrote:
> 
> Thane Hubbell wrote:
…[22 more quoted lines elided]…
> 
Joe,

If you have any OO COBOL references - the following will accommodate
your above "peeves" :-

   colllections/dictionaries and callbacks

- using callbacks against the collections using "do", the collection of
objects being those DataElements you refer to. (PS: As yet I'm
'uncomfortable' with callbacks - though Ken assures me I am currently
using them :-). I think you are into C++ - so probably you've got a
better handle on what callbacks are).

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E1FE1C.A1068793@zip.com.au>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <38E0B4A4.CFB076B7@iinet.net.au>`

```
Joseph Katnic wrote:
> 
> Thane Hubbell wrote:
…[22 more quoted lines elided]…
> into each of the 50 set data methods.

Firstly:  What is to stop a single method returning a structure should
you want that.  One call all the data in it.

Second:  fifty elements appears very high you would have to convince
me that they were directly related.  Object my contain other objects
and so on.  You may have 50 in theory but each are smaller.

Third:  Get and Set are BAD!!!!

The basic concept is that object work on themselves and do not expose
their internal data.  If we look at the fraction example (sorry Thane)
when the values are accessed the three values are displayed in a
sequence.  This would be better built as a string function that
returns the fraction for display (one function three internal
values).  The setter would typically be the reverse, a string input
that is interpreted by the best logic you have.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 7)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-03-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bubup$t00$1@news.igs.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <38E0B4A4.CFB076B7@iinet.net.au> <38E1FE1C.A1068793@zip.com.au>`

```
God Ken, you can get carried away. <G>.  Just tell him to use a record
instead of a data field.  That way he can set whole 01 level groups of data
across at a time.  This is Cobol.  He can send a whole Isam File in one file
name.  He can pass an URL and set *billions* of attributes at a time.  Fifty
methods to set fifty attributes shows a decided lack of imagination.

Ken Foskey wrote in message <38E1FE1C.A1068793@zip.com.au>...
>Joseph Katnic wrote:
>>
…[46 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E2CD60.6E0DBDF6@home.com>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com> <38df8f4a.1603834955@news.cox-internet.com> <38E0B4A4.CFB076B7@iinet.net.au> <38E1FE1C.A1068793@zip.com.au> <8bubup$t00$1@news.igs.net>`

```


donald tees wrote:
> 
> God Ken, you can get carried away. <G>.  Just tell him to use a record
…[4 more quoted lines elided]…
> 
Don,

I think this is where you have to make a distinction between what is
practical/desirable and following what the gurus say is the right way to
use OO. Now if you look at the examples where I am passing Local-storage
- I can kind of see where M/F were coming from in one of their demos -
and that code made Pete Dashwood want to throw up. (I didn't throw-up,
but I was bloody close - saying to myself if this is OO 'Forget it!).

- Firstly, they were aware (having written their compiler) of the
possible penalty in using too much space for L/S

- Second, following the above thought, they then followed the 'accepted'
way of using OO by passing (Set) and getting (GET)
each individual field (from memory about 10 fields). Now turn that 10
into say 30 for a large name-address record plus credit limit, rating,
last purchase, last transaction date etc. then that gives you :-

	(a) a lot of coding doing the same thing
	(b) the obvious possibility of typos in coding - hence 
	    more desk and test-checking

In the above I'm assuming you are after a complete record for editing as
opposed to selective fields to say print a report showing last
transaction date and total purchases.

To my mind - your way represents the more practical :-
	
(a) Use an 01 to pass a whole record -
	copy "myRecord.cpy" replacing ==(tag)== by ==ls==.
	(My preferred method when editing - using three-tier
	system approach, business logic, file handling and screen
	displays)

(b) In the case of collections/dictionaries pass the
	01 Level object reference which embraces n to n+....... 
	individual objects, and which may in turn contain sub-objects.
	(Ideal approach for passing contents of droplists or
	listboxes)

Para (a) above definitely 'breaks' the cautionary note by M/F about too
much use of L/S - and doesn't sit well with the "SET" or "GET"
technique.  Take the short-cut to get the job done effectively, with
reduced code, less prone to error.

Jimmy
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38DEA6EB.A669DE9@worldnet.att.net>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> In article <8bj2c8$j6g$1@news.inet.tele.dk>,
…[15 more quoted lines elided]…
> and to 'isolate' it from what?

Say no more, Tony D.

Bill Lynch
```

###### ↳ ↳ ↳ Re: working-storage vs. local-storage

_(reply depth: 4)_

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c4prh$get$1@news.inet.tele.dk>`
- **References:** `<8bhkat$621$1@slb2.atl.mindspring.net> <8bible$c0i$1@nnrp1.deja.com> <8bj2c8$j6g$1@news.inet.tele.dk> <8blpit$rs3$1@nnrp1.deja.com>`

```
Still smiling - look below:
Foodman skrev i meddelelsen <8blpit$rs3$1@nnrp1.deja.com>...
>In article <8bj2c8$j6g$1@news.inet.tele.dk>,
>"Ib Tanding" <ib@tanding.dk> wrote:
…[16 more quoted lines elided]…
>

From other processes of course. The good old language is a procedural thing,
but in a dialog with a user, you sometimes need to switch to another,
similar process. With local storage, you can do that, without loosing your
present data. Set current process in hold, start another one, start one
more, switch between them and close them down when they aren't needed any
more. Seems to be a good service for users, who needs simutaneous to use the
same sub-program for information desks, telephone service etc.

It's a new feature in the language - even if you don't like it.
>
>>
…[10 more quoted lines elided]…
>

You are right - just trying to be historic.
>
>
…[9 more quoted lines elided]…
>

Look above.
>
>
…[7 more quoted lines elided]…
>

We pay programmers to make programs. We pay the programmers to be loyal to
the company, they work for and to be loyal to the programming standards in
that company.

Unfortunately many companies have a very narrow-minded management. They buy
C++ compilers or Delphi to be able to do, what you can do with local-storage
in Cobol.

If one of your programmers came to you and said that you could save
thousands of dollars, would you fire him? If he said that you could save
money for education in new languages, new compilers, would you be offended?

I would like to look upon the problem from another angle: Customers are
requesting applications. If your company can meet the requests with the
current technology, your turn-over will be more attractive. That is what
Cobol does for you.

>> but I would never ever pollute my programs with an ALTER.
>
…[20 more quoted lines elided]…
>

You are right again, but I wonder - why are people on call in any larger
computer site all over the world, and  why did we work so hard with Y2K?
I'll tell you why. Because in the real life bugs exists. Perhaps you didn't
test Y2K leap year back in '86, and perhaps the input changed over the
years. Integrated systems receives data from external sources and something
undocumented can happen.

And, of course, poorly educated programmers could make a bad program, but
quality in testing would leave that out - wouldn't it.


>
>
…[5 more quoted lines elided]…
>

Bingo!
>
>
…[8 more quoted lines elided]…
>
Bingo again.
>
>> Did any of you ever tell anyone in Taipei or Silicon Valley what we
…[8 more quoted lines elided]…
>

Yeah, but who evented 307 different modem-cards, 134 different memory-cards,
203 different sound-cards etc. etc.  Everything must be installed different
and invoked different from your software. Standars are set by the vendor and
they don't get a shit about ISO, OSI, ANSII or other difficulties to
introduce their junk on the market. You cannot depend upon 'Plug-and-Play' -
often you must Plug and PRAY.

>
>
…[10 more quoted lines elided]…
>

Black humor? What I meant was that colors would make us happy from time to
time - Why not a yellow one for Easter and a green one in summer-time.
>
>
…[9 more quoted lines elided]…
>Yeah, you're calm, what about everybody else?

>

Sorry about that. I learned the trick from my Mother-in-Law.

When she woke up in the night, she couldn't sleep - she became stressed by
the whole family sleeping. She went to the toilet and opened the water. Then
she scratched at the front door with her nails and their stupid dog went
crazy and ran all over the house barking. After that she went to bed and
fell asleep. The whole family sneeked around, calmed the dog and closed the
water - whispering to each other so she wouldn't be disturbed. Her husband
were completely unaware of her little trick until their 25th aniversary

many regards
Ib

>Thanks
>
…[5 more quoted lines elided]…
>Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
