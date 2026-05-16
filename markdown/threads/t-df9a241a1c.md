[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# read at end ... not at end, etc

_22 messages · 15 participants · 2000-05_

---

### read at end ... not at end, etc

- **From:** shine98@my-deja.com
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gjqs9$kko$1@nnrp1.deja.com>`

```
Do you think that the COBOLization of COBOL with statements like "not
at end" as in:

	read file at end ... not at end end-read

will lead to even further degradation such as:


	read file

		at end ...

		not at end ...

		at beginning ...

		at first-record ...

		at after-first-record ...

		at last-record ...

		at before-last-record ...

		when major-key-break ...

		when intermediate-key-break ...

		when minor-key-break ...

		at detail ...

	end read


and that we'd be better off if we simply dropped the "at end" phrase
and just stuck with the read and a separate test after?

I do!

I envision whole programs choked up around the read statement. Pity.
Thank goodness nobody around here does this sort of madness.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: read at end ... not at end, etc

- **From:** "The Riddler" <riddler_cubed@nospam.yahoo.com>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gmc8k$3am$1@news.cis.ohio-state.edu>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com>`

```
I've read that one thought behind adding the "NOT AT END" clause was so that
the practice of the "priming read" can be easily avoided. According to some
views of structured programming reading from a file in two different places
in the program (the priming read and then again at the end of the processing
loop) goes against good coding practices.

Personally, I don't like it. As someone in this thread stated, it's getting
the READ too involved in processing and program flow. As far as the "at
first record" stuff goes, didn't we once have that kind of thing in old, old
COBOL with the "ON 1"? That was removed (with COBOL 74, I think). It was a
bitch to convert to newer versions.

While we're on a soapbox I'll also add that I do not like the INVALID KEY,
NOT INVALID KEY (you know, VALID KEY would've been better, to avoid the
double negative) clauses for direct reads/writes/rewrites/etc. Lumping all
"bad" file statuses into one group can't be a good idea.


<shine98@my-deja.com> wrote in message news:8gjqs9$kko$1@nnrp1.deja.com...
> Do you think that the COBOLization of COBOL with statements like "not
> at end" as in:
…[16 more quoted lines elided]…
> <snip>
```

##### ↳ ↳ Re: read at end ... not at end, etc

- **From:** tscoffey@my-deja.com
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gmf7q$hm6$1@nnrp1.deja.com>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu>`

```
In article <8gmc8k$3am$1@news.cis.ohio-state.edu>,
  "The Riddler" <riddler_cubed@nospam.yahoo.com> wrote:

<snip>

> didn't we once have that kind of thing in old, old
> COBOL with the "ON 1"? That was removed (with COBOL 74, I think). It
was a
> bitch to convert to newer versions.
>

Why would an 'ON 1' be difficult to convert?


   77   ON-1-A  PIC 9 VALUE 0.

        IF ON-1-A = 0 THEN
           :
           MOVE 1 to ON-1-A
        END-IF.


Or do I miss something?




Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oKCX4.863$wW2.166103@dfiatx1-snr1.gtei.net>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <8gmf7q$hm6$1@nnrp1.deja.com>`

```
Because when the person who had to convert one of these constructs (me) had
never seen it used before, it took extra time for him (me) to try to figure
out what it meant. AFTER that, it was pretty easy.
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392F0FD9.44957C52@istar.ca>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <8gmf7q$hm6$1@nnrp1.deja.com>`

```
The difference is that ON 1 didn't require any data division entries.  A
useful declarative would be USE ON INITIAL ENTRY to give the same
result.  If eough old timers and the person from the shop where they
used the ON 1 construct for first time initialization were to request it
in the standard after next we might get a good replacement for ON 1
which doesn't require any data division entries.

I would use the construct if it were available.  It would be useful in
sub-routines.

Clark Morris, CFM Technical Programming Services Inc., cfmtech@istar.ca  

tscoffey@my-deja.com wrote:
> 
> In article <8gmc8k$3am$1@news.cis.ohio-state.edu>,
…[22 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

_(reply depth: 4)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392FC5A2.4572D109@cusys.edu>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <8gmf7q$hm6$1@nnrp1.deja.com> <392F0FD9.44957C52@istar.ca>`

```


"Clark F. Morris, Jr." wrote:
> 
> The difference is that ON 1 didn't require any data division entries.  A
…[4 more quoted lines elided]…
> which doesn't require any data division entries.

The other command which was handy was EXHIBIT NAMED and EXHIBIT NAMED
CHANGED.  It was real easy to add to code.   The CHANGED now is a pain.

I dislike indices.  Sure they're necessary for SEARCH, but they're
clumsy to DISPLAY,  and it is ridiculous to SET MY-INDEX TO 1 then SET
MY-INDEX DOWN BY 1 to prime a table build.  Aren't subscripts just as
efficient with modern optimizers?
```

###### ↳ ↳ ↳ Subscript versus index was Re: read at end ... not at end, etc

_(reply depth: 5)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39301F82.CDA7D10C@istar.ca>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <8gmf7q$hm6$1@nnrp1.deja.com> <392F0FD9.44957C52@istar.ca> <392FC5A2.4572D109@cusys.edu>`

```
In general if virtually all of the manipulations can be done using
constants and/or other indexes for the same table, indexes should be
faster than subscripts because only addition, subtraction and move are
involved.  Indexes are kept as a displacement from the start of the
table.  Subscripts are kept as the actual number and must be multiplied
by the size of the entry and adjusted.    

Now there are some interesting  complications.  If the indexes for two
different tables have to be compared this is less efficient than
comparing two subscripts because the indexes must be converted to
subscripts before being compared.  In addition if the index would have
to be obtained from another data field (or from the index of another
table), it may be more efficient or as efficient to use subscripts.

On the IBM COBOL 85 mainframe compilers if the subscript is a field with
a value clause that is never updated (effectively a constant), the
compiler will calculate the position at compile time and treat the
subscript as a literal.  This boggled my mind the first time I saw it. 
I had a program where WS20-01 was PIC 99 DISPLAY VALUE 01.  In the
PROCEDURE DIVISION there was a MOVE WS40-ENTRY (WS20-01) TO WORK-ENTRY. 
Since there were a number of instances of similar code I thought I had
found a performance improvement opportunity.  I looked at the generated
code expecting to find PACK, CVB - convert to binary, SH - subtract
half-word or maybe BCTR, MH - multiply half word, L - load word, AR -
add register, and MVC - move characters found only MVC. 

In short the relative efficiency depends on how the subscript/index is
obtained in the program and with the exception I noted above has little
or nothing to do with the optimizing capabilities of the compiler. 
Whether you notice the difference may have more to do with how
efficiently the binary multiply instructions are implemented.

Clark Morris, CFM Technical Programming Services Inc., cfmtech@istar.ca

Howard Brazee wrote:
> 
> "Clark F. Morris, Jr." wrote:
…[14 more quoted lines elided]…
> efficient with modern optimizers?
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392F4C7A.770225FC@worldnet.att.net>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <8gmf7q$hm6$1@nnrp1.deja.com>`

```
tscoffey@my-deja.com wrote:
> 
> In article <8gmc8k$3am$1@news.cis.ohio-state.edu>,
…[19 more quoted lines elided]…
> Or do I miss something?

I don't think so. I would simply count the no. of input records. If you
have trouble determining which record is the first you probably should
find another line of work (like management, for instance).

Bill Lynch
```

##### ↳ ↳ Re: read at end ... not at end, etc

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392ec05d.149134822@news.cox-internet.com>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu>`

```
On Fri, 26 May 2000 13:22:36 -0400, "The Riddler"
<riddler_cubed@nospam.yahoo.com> wrote:

>I've read that one thought behind adding the "NOT AT END" clause was so that
>the practice of the "priming read" can be easily avoided. According to some
…[3 more quoted lines elided]…
>

I like the Not at End, because I can do the following.  I find it
clear, concise and reliable.

Perform Process-File Until All-Done.

Process-File.
   Read the-file At end set all-done to true
                       Not at end perform whatever-record-process-is
   End-Read
   .

Or:

Perform until file-status not = "00"
    Read the-file at end continue
                         not at end process-the-record
    end-read
 End-Perform


No IF for checking file status, no second level flags, etc.
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gn3l4$o9n$1@news.inet.tele.dk>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <392ec05d.149134822@news.cox-internet.com>`

```
True, I like that structure too, but I wonder: If you have 4 input files in
a match/merge, and you are supposed to write group totals and a grand total.
Wouldn't that stress the nice structure a bit :-)

Regards
Ib
Thane Hubbell skrev i meddelelsen
<392ec05d.149134822@news.cox-internet.com>...
>On Fri, 26 May 2000 13:22:36 -0400, "The Riddler"
><riddler_cubed@nospam.yahoo.com> wrote:
>
>>I've read that one thought behind adding the "NOT AT END" clause was so
that
>>the practice of the "priming read" can be easily avoided. According to
some
>>views of structured programming reading from a file in two different
places
>>in the program (the priming read and then again at the end of the
processing
>>loop) goes against good coding practices.
>>
…[22 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393115a8.3296518@news.cox-internet.com>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <392ec05d.149134822@news.cox-internet.com> <8gn3l4$o9n$1@news.inet.tele.dk>`

```
On Sat, 27 May 2000 02:12:43 +0200, "Ib Tanding" <ib@tanding.dk>
wrote:

>True, I like that structure too, but I wonder: If you have 4 input files in
>a match/merge, and you are supposed to write group totals and a grand total.
>Wouldn't that stress the nice structure a bit :-)
>


Nah... I'd use Merge with an Output procedure <G>.
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

_(reply depth: 5)_

- **From:** Charles Haatvedt Jr. <clastname@nospam.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.139b891314bd34a19896c9@news>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <392ec05d.149134822@news.cox-internet.com> <8gn3l4$o9n$1@news.inet.tele.dk> <393115a8.3296518@news.cox-internet.com>`

```
In article <393115a8.3296518@news.cox-internet.com>, 
thaneH@softwaresimple.com says...
> On Sat, 27 May 2000 02:12:43 +0200, "Ib Tanding" <ib@tanding.dk>
> wrote:
…[9 more quoted lines elided]…
> 
doesn't a MERGE imply that all the input files be of the same format ???
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

_(reply depth: 6)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39325b59.73478101@news.cox-internet.com>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <392ec05d.149134822@news.cox-internet.com> <8gn3l4$o9n$1@news.inet.tele.dk> <393115a8.3296518@news.cox-internet.com> <MPG.139b891314bd34a19896c9@news>`

```
On Mon, 29 May 2000 01:51:19 GMT, Charles Haatvedt Jr.
<clastname@nospam.com> wrote:

>In article <393115a8.3296518@news.cox-internet.com>, 
>thaneH@softwaresimple.com says...
…[14 more quoted lines elided]…
>--

Yes - which is really why I think it is rarely used.  The above was my
attempt at humor based on another thread.
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

_(reply depth: 7)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gtg81$1keq$1@news.hitter.net>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <392ec05d.149134822@news.cox-internet.com> <8gn3l4$o9n$1@news.inet.tele.dk> <393115a8.3296518@news.cox-internet.com> <MPG.139b891314bd34a19896c9@news> <39325b59.73478101@news.cox-internet.com>`

```

Thane Hubbell wrote in message <39325b59.73478101@news.cox-internet.com>...
>On Mon, 29 May 2000 01:51:19 GMT, Charles Haatvedt Jr.
><clastname@nospam.com> wrote:
…[6 more quoted lines elided]…
>>> >True, I like that structure too, but I wonder: If you have 4 input
files in
>>> >a match/merge, and you are supposed to write group totals and a grand
total.
>>> >Wouldn't that stress the nice structure a bit :-)
>>> >
…[10 more quoted lines elided]…
>attempt at humor based on another thread.

I think it is rarely used because some authors of popular books on
COBOL do not discuss MERGE. ;-)

The same comment applies to Report Writer. ;-)

[My attempt at humor based on another thread.]
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392F4CDF.5592237@worldnet.att.net>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <392ec05d.149134822@news.cox-internet.com>`

```
Thane Hubbell wrote:
> 
(snip)
> 
> I like the Not at End, because I can do the following.  I find it
…[18 more quoted lines elided]…
> No IF for checking file status, no second level flags, etc.

Amen, Thane, that's the way to do it. 

Bill Lynch
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<393017CD.D9C25D59@istar.ca>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <392ec05d.149134822@news.cox-internet.com> <392F4CDF.5592237@worldnet.att.net>`

```
No it isn't the way to do it.  If you check for status code on a file
(or even have it defined for the file), you must check for it
immediately after all I-O operations for that file.  When a file
contains the STATUS clause on the SELECT statement, the compiler assumes
all error handling is done either by DECLARATIVES or by checking of the
status code.  The default system action for the specific error is NOT
taken.  If you have a tolerant compiler (all IBM COBOL 85 compilers for
MVS/OS390 and VM are), you don't need the AT END clause and can rely
solely on status code checking (10 and possibly one other value for AT
END).

Clark Morris, CFM Technical Programming Services Inc. cfmtech@istar.ca   

William Lynch wrote:
> 
> Thane Hubbell wrote:
…[26 more quoted lines elided]…
> Bill Lynch
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-05-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3931166b.3491075@news.cox-internet.com>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu> <392ec05d.149134822@news.cox-internet.com> <392F4CDF.5592237@worldnet.att.net> <393017CD.D9C25D59@istar.ca>`

```
I knew I should have put some context in here.  I only use this
construct when reading sequentially through a file that I intend to
read from beginning to end.  FOR THAT PURPOSE the construct is
complete and valid.   Any "strange" - and they would be unusual in the
above described context - file status values are handled by a catch
all declarative that displays the error for the operator or user.

For random reads, or dynamic access to an indexed file more robust
file status checking is used.

On Sat, 27 May 2000 15:45:33 -0300, "Clark F. Morris, Jr."
<cfmtech@istar.ca> wrote:

>No it isn't the way to do it.  If you check for status code on a file
>(or even have it defined for the file), you must check for it
…[42 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

- **From:** frlsfly@aol.com (FRLSFLY)
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000527045433.29107.00000259@ng-fv1.aol.com>`
- **References:** `<392ec05d.149134822@news.cox-internet.com>`

```
It's always been possible to put the main program control in a Read paragraph. 
I've never liked it, as it seems to cause problems in any program dealing with
more than one file.

One reason I like the priming/unique first readis  because it makes it easier
to code for error handling that I might only want to do on the first fetch
attempt.  

An  example of where this comes into play is with server processes that get
fired up and 'hang a read" on an input file.  Time-out parameters for that
first read are often specific to that situation.

Coding  something along the lines of "IF FIRST-READ-SET ..ELSE" is a royal
pain.

I also find that the priming read makes both the main and nested loop logic
easier for me to keep straight, particularly when I am trying to track multiple
commits/aborts to data-bases that are logically one transaction.  

All a matter a taste, I suppose.

>I like the Not at End, because I can do the following.  I find it
>clear, concise and reliable.
…[25 more quoted lines elided]…
>


Nathan Meyer
Berkeley, CA
"Big Endian" is what I like.
```

###### ↳ ↳ ↳ Re: read at end ... not at end, etc

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gp7kt$leb$1@news.igs.net>`
- **References:** `<392ec05d.149134822@news.cox-internet.com> <20000527045433.29107.00000259@ng-fv1.aol.com>`

```
I like a pre-read as well, though I suppose a lot of the reason is that I am
use to it ... the older Cobols pretty well forced you to do it that way.
Once use to it though, there are a lot of advantages, like you say.

FRLSFLY wrote in message <20000527045433.29107.00000259@ng-fv1.aol.com>...
>It's always been possible to put the main program control in a Read
paragraph.
>I've never liked it, as it seems to cause problems in any program dealing
with
>more than one file.
>
>One reason I like the priming/unique first readis  because it makes it
easier
>to code for error handling that I might only want to do on the first fetch
>attempt.
…[9 more quoted lines elided]…
>easier for me to keep straight, particularly when I am trying to track
multiple
>commits/aborts to data-bases that are logically one transaction.
>
…[34 more quoted lines elided]…
>"Big Endian" is what I like.
```

##### ↳ ↳ Re: read at end ... not at end, etc

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392F4C06.F5B1DD23@worldnet.att.net>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com> <8gmc8k$3am$1@news.cis.ohio-state.edu>`

```
The Riddler wrote:
> 
> I've read that one thought behind adding the "NOT AT END" clause was so that
…[6 more quoted lines elided]…
> the READ too involved in processing and program flow.

I don't see how the "not at end" involves the READ any further than it
already is. If you're reading a file sequentially, "at end" / "not at
end" is an issue which must be solved, regardless of coding style or
READ verb options (although I have seen a few programs which did not
separate the two (they were from the income group <g>)). These tended to
get into huge loops, reading forever after the "at end" they ignored.
These tended to chew up an enormous amount of resources in production
CICS regions.

Bill Lynch
```

#### ↳ Re: read at end ... not at end, etc

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gvfv0$ldr$1@slb7.atl.mindspring.net>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com>`

```
This thread has gone in several directions, but just to make it clear there
is NO intention (and/or desire) in the Standards committees to allow MORE
than 1 type of conditional statement for a single use of a single verb.  You
can use READ AT END or READ INVALID KEY - but not both together.  There is a
"not" variation for every positive conditional statement (except for ON
OVERFLOW for a CALL - but that has an "obscure reason" for a rationale).

FYI, the next Standard will relax the rules so that the NOT form may be coded
before OR after the positive form, e.g.

  Read whatever
     Not at end
        Perform your-post-common-code
     At end
       Set EOF to true
   End-Read

P.S.  If you really DO have "multiple" conditions to check, then probably an
EVALUATE is the way to go - but this would depend on what you were actually
trying to check.
```

#### ↳ Re: read at end ... not at end, etc

- **From:** pknudsen@gw.total-web.net (Paul Knudsen)
- **Date:** 2000-05-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39340886.2188105@news.gw.total-web.net>`
- **References:** `<8gjqs9$kko$1@nnrp1.deja.com>`

```
Wow, what a great idea!  Send it to the standards committe right away!

In any event, I totally fail to see why at end--not at end is a
"degradation".  Don't use it if you don't like it.

On Thu, 25 May 2000 18:20:11 GMT, shine98@my-deja.com wrote:

>Do you think that the COBOLization of COBOL with statements like "not
>at end" as in:
…[43 more quoted lines elided]…
>Before you buy.

---------------------------------------------------------------
SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
