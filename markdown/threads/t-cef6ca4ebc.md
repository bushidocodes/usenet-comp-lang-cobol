[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Checking for value in linkage section variable

_4 messages · 4 participants · 2009-01_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: Checking for value in linkage section variable

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-01-26T17:10:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<497DEE68.6F0F.0085.0@efirstbank.com>`

```
>>> On 1/26/2009 at 2:36 PM, in message
<982e07bb-5a61-4c41-87c3-481dc102679d@f13g2000yqj.googlegroups.com>,
Pakku<pakku@soccermail.com> wrote:
> 
> First things first, this is Ent Cobol 3.something on z/OS.
…[30 more quoted lines elided]…
> So...any suggestions would be most welcome

I am having some bad deja vu here!! :-)

I have brought up this same issue in the past, and the answer always seems
to be that you can't do what you want to do here.  Plain and simple.  There
is no way on z/OS (or z/VSE) for a Cobol subroutine to be *inherently* able
to determine how many parameters were passed to it from the calling
program.

It's simple in assembler, if using standard linkage.  The high-order bit is
set for the last parameter.  But IBM Cobol has no way to interrogate this.

With newer z/OS compilers you can call with OMITTED.  But as Bill says, this
has to be done explicitly by the caller.  In other words...

CALL 'SUBR' USING PARM-1, PARM-2, OMITTED
is *not* the same as
CALL 'SUBR' USING PARM-1, PARM-2

In fact, as far as I can tell the former is exactly the same as:
SET ADDRESS OF NULL-PARM TO NULL
CALL 'SUBR' USING PARM-1, PARM-2, NULL-PARM
(where NULL-PARM is in the linkage section)

For the latter, the address of "PARM-3" is not null, but is in fact the
address of PARM-3 from the last time the routine was called (in this
runtime) with three parms.  If it was never called with three parms then the
address of PARM-3 is undefined.

Howard stated the following:
"IBM Mainframes pass in a length of the variables.   I wonder if your
compiler has something similar.  In my experience, this has been
compiler dependent.

e.g.
 LINKAGE SECTION.                                  
 01  PASSED-RECORD.                                
     05  PASSED-LENGTH     PIC 9(4)  COMP.         
     05  PASSED-UPDATE-PARM.            
"

But this only works for getting PARM data from an EXEC card.

Now that's not to say you couldn't code subroutines to work this way, but
you'd have make sure the caller populates the length field explicitly. 
Yuck.  Plus this does not really address mulitple parameters.  This example
is a single parameter (PASSED-RECORD) that happens to have two sub-fields.

Cobol...standard Cobol, in any case, just doesn't appear to give you any way
to do what you (and I) want to do.

Yes, very frustrating.  If I were you I'd just resign myself to changing and
recompiling all callers of your subroutine.  You can choose to use OMITTED
for the new parm for callers who don't care about it, or just pass in a
"real" parm-3 (of the proper length) and have the caller ignore it.  If you
choose to use OMITTED make sure that the subroutine checks for it (see the
link Bill posted) and doesn't try to write to that parm if it was omitted.

Frank
```

#### ↳ Re: Checking for value in linkage section variable

- **From:** Pakku <pakku@soccermail.com>
- **Date:** 2009-01-26T18:15:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<57f8d7b8-2059-4682-b6db-6a07b37075e8@u18g2000pro.googlegroups.com>`
- **References:** `<497DEE68.6F0F.0085.0@efirstbank.com>`

```
On Jan 26, 7:10 pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
wrote:
> >>> On 1/26/2009 at 2:36 PM, in message
>
…[103 more quoted lines elided]…
> Lakewood, CO  USA

Thanks all.  In a sense it is gratifying to see that someone else has
had the same situation and that there is no solution.  Bill- your
explanation on why this isn't possible helps to have a better
comprehension.

I wonder if I can convince the testing folks that the only change I
made to some of the programs was to add an OMITted 'parm' and so they
don't require full blown regression testing!
Our attitude has been, if it is being promoted then we will test the h
out of it.
```

##### ↳ ↳ Re: Checking for value in linkage section variable

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-01-27T11:08:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<poaun4hg9j8b97dfgicbg2ah6t827bo37r@4ax.com>`
- **References:** `<497DEE68.6F0F.0085.0@efirstbank.com> <57f8d7b8-2059-4682-b6db-6a07b37075e8@u18g2000pro.googlegroups.com>`

```
On Mon, 26 Jan 2009 18:15:00 -0800 (PST), Pakku <pakku@soccermail.com>
wrote:

>On Jan 26, 7:10ï¿½pm, "Frank Swarbrick" <Frank.Swarbr...@efirstbank.com>
>wrote:
…[116 more quoted lines elided]…
>out of it.

As you may have realized by now based on the responses to your
question, it doesn't look like you can do what you want to do....in
COBOL.

However, if this is really a necessary function of your system then
you may want to look into a slightly different solution.

IBM Assembler has the ability to detect the number of arguments passed
in a CALL statement from any language.  It can know whether 1, 2, 3 or
how ever many arguments are passed in the CALL statement.

Therefore, one solution is to write an Assembler Program with the same
name as the COBOL Subroutine you are trying to modify.  You'll
obviously need to rename the COBOL Subroutine to something else.

In the Assembler subroutine you detect how many arguments were passed
from the calling program and you set up an address list to just pass
those along to your COBOL subroutine.  For the arguments that are not
passed you use a constant in your Assembler program that just has a
value of high values and you pass the address of it as the third
argument.

You then call your COBOL subroutine passing all 3 (if that's the max)
arguments.  Remember Calls only pass addresses so you are passing the
address of the arguments in the original Call statement and possibly
the address of your constant if a third argument was not originally
passed.
 
In your COBOL subroutine you check your third argument for high
values.  If equal, you know not to use it.

It may not be the solution you are looking for, but it is a solution.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"Last night I dreamed I ate a ten-pound marshmallow, 
and when I woke up the pillow was gone."
-- Tommy Cooper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Checking for value in linkage section variable

- **From:** docdwarf@panix.com ()
- **Date:** 2009-01-27T16:58:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<glnefk$kpn$1@reader1.panix.com>`
- **References:** `<497DEE68.6F0F.0085.0@efirstbank.com> <57f8d7b8-2059-4682-b6db-6a07b37075e8@u18g2000pro.googlegroups.com> <poaun4hg9j8b97dfgicbg2ah6t827bo37r@4ax.com>`

```
In article <poaun4hg9j8b97dfgicbg2ah6t827bo37r@4ax.com>,
SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:
>On Mon, 26 Jan 2009 18:15:00 -0800 (PST), Pakku <pakku@soccermail.com>
>wrote:
…[5 more quoted lines elided]…
>>> Pakku<pa...@soccermail.com> wrote:

[snip]

>>> > Now, we too have a standard in place about
>>> > linkage section layout in copybooks but I was thinking to leverage on
>>> > the flexibility provided by dynamic linking to change the subroutine
>>> > without necessarily modifying and recompiling all the calling
>>> > programs.

[snip]

>>I wonder if I can convince the testing folks that the only change I
>>made to some of the programs was to add an OMITted 'parm' and so they
>>don't require full blown regression testing!
>>Our attitude has been, if it is being promoted then we will test the h
>>out of it.

There are a few reasons for such procedures... some might say they fall 
under the heading of 'maintaining power and procedures and the status quo 
while keeping the code so simple that a 2-year programmer can fix it on a 
3:am call while denying Truly Superior Coders a chance to demonstrate 
techniques hitherto avoided', others might say they fall under the heading 
of 'data are sacred and anything which touches data must meet certain 
standards of quality and reliability'.

>
>As you may have realized by now based on the responses to your
…[12 more quoted lines elided]…
>obviously need to rename the COBOL Subroutine to something else.

... or you can re-code the copybooks, recompile the affected programs and 
say 'As I pointed out earlier this is not an 'all ya gotta do is...' 
problem; someone's budget has to allow for the processes which Those Of 
Appropriate Responsibility have deemed... appropriate.'

I'm not sure what's going on here... whether you are edging close to the 
thin ice of 'Look, Ma, I'm a Programmer!' code or someone is trying to 
slip in a mod under the radar-screen of the testers in order to save time 
and money or something else, entire.

What seems to be the case is that you're trying to find a way around the 
'We've Always Done It This Way' dictum... and that can be very, very 
dangerous.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
