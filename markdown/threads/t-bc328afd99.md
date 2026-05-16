[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# more cics pains

_28 messages · 10 participants · 1998-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### more cics pains

- **From:** "Jason" <superj@door.net>
- **Date:** 1998-10-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7169rh$b8b$1@supernews.com>`

```
Thanks for the help to those who replied to my last message about problems
with entering data to a map, THAT NOW WORKS!  Now on to another problem.  I
have a simple statement that when evaluated as TRUE sends the control back
to another program.  I thought this was relatively easy as far as examples
in class and in the book showed but now that it is programmed, any time the
aid key is hit to exit or go to another program I get an abend.
This is how it is coded:


when eibaid = dfhpf3
       exec cics                                      this is all in an
evaluate statement,
             return
       end-exec
when eibaid = dfhpf12
        exec cics
              xctl program('a001')
         end-exec

My logic, as I now know, doesn't ever seem to flow in the same direction as
a program's does (especially OO C++), so I have problems following.  Any
books that teach living life as an algorithm, would be great!
```

#### ↳ Re: more cics pains

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3636a627.40551489@news3.ibm.net>`
- **References:** `<7169rh$b8b$1@supernews.com>`

```
On Tue, 27 Oct 1998 23:20:58 -0600, "Jason" <superj@door.net> wrote:

Jason,

Did you, by any chance, forget the NOHANDLE (or the RESP) option on the EXEDC CICS RECEIVE
command?  Run your program through CEDF and check if you get a MAPFAIL (or another) error
while receiving the map.

Of course, all of these problems you encounter should be covered in any beginner's course
for CICS application

HTH

>Thanks for the help to those who replied to my last message about problems
>with entering data to a map, THAT NOW WORKS!  Now on to another problem.  I
…[22 more quoted lines elided]…
>

with kind regards

Volker Bandke
(BSP GmbH)
```

#### ↳ Re: more cics pains

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363937fc.4757669@news-server>`
- **References:** `<7169rh$b8b$1@supernews.com>`

```
On Tue, 27 Oct 1998 23:20:58 -0600, "Jason" <superj@door.net>
enlightened us:

>Thanks for the help to those who replied to my last message about problems
>with entering data to a map, THAT NOW WORKS!  Now on to another problem.  I
…[22 more quoted lines elided]…
>

What abend are you getting and are you getting it when PF12 is
pressed?

Cheers,

          ////
         (o o)
-oOO--(_)--OOo-
Cats know how we feel. They don't give a damn, but they know.
 Steve
```

##### ↳ ↳ Re: more cics pains

- **From:** "Jason" <superj@door.net>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7192tp$qik$1@supernews.com>`
- **References:** `<7169rh$b8b$1@supernews.com> <363937fc.4757669@news-server>`

```
This is the error I am getting:

DFHAC2206 00:42:28 CICSD Transaction B191 has failed with abend AEI0.
Resource
  backout was successful.

And it does happen with the F12 aid key.
```

###### ↳ ↳ ↳ Re: more cics pains

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981029050029.24005.00000805@ng-fd1.aol.com>`
- **References:** `<7192tp$qik$1@supernews.com>`

```
On Thu, 29 Oct 1998 00:41:46 -0600
"Jason" <superj@door.net>

>>
This is the error I am getting:

DFHAC2206 00:42:28 CICSD Transaction B191 has failed with abend AEI0.
Resource  backout was successful.

And it does happen with the F12 aid key.
<<

AEIO  DUPKEY condition not handled

You are accessing a file. It is possible that you have succeeded in invoking
program 'A001'.  And it does not yet work, or the file it is after is broken.

The logic behind CICS error condition processing is that:
  a) for a given command most conditions can't even happen because they don't
relate to that command 
  b) of the several condition that do relate the default may be to pass the
condition back to the program so you can do anything you want; this is what
RESP and RESP2 are for, and
   c) of the several conditions that do relate the default may be to not tell
you, not give control back to your program, just flat out abend.

For this third category, you can change CICS behavior.  Before the command, you
issue a CICS HANDLE command for that specific condition. This overrides the
abend default and will send control back to your program.

The HANDLE command works like a delayed GO TO, and can be very tricky to deal
with from within a structured program that has PERFORMS within PERFORMS.

HANDLE condition statements are still widely used, and you will need to
understand them. They are specifically discouraged by the software vendor.

Instead you can do an IGNORE 
condition command (just prior to the command that may encounter that condition.
 This too will disable CICS's default behavior. But rather than jump off to
some wild place with GO TO like semantics, IGNORED conditions just pass control
back at the end of the failing command, and then you can interrogate RESP and
RESP2.

Your text book should illustrate both HANDLE and IGNORE.

If you have any VSAM file processing in your top program, the problem could be
there. But with what you have shown so far it looks like it is in 'A001' (or
lower if that module invokes others).  Do you have access to the source code
for 'A001'? Is it your module, or a shop module, or your prof's module?

The code in that program may actually be putting (or attempting to put) the
duplicate record onto the file, or maybe it is reading the file and encounters
a duplicate record.

BTW, this could be a VSAM problem in a way.  A keyed VSAM file can be defined
as having UNIQUE or NONUNIQUE keys. The VSAM file defintion might be wrong, and
it may be that the program is supposed to be dealing in duplicate records.

Who owns this file? Did you  load it? Did you define it with IDCAMS?  Was the
DELETE/DEFINE done correctly?

A third possibility is that the program is basically correct, the file
definition is basically correct. But you have had mulitple test runs that have
tried to add the record repeatedly. That will happen a lot, especially when you
are first bring a system up in test or in production.  Frequently the first try
does not work.

The mistake in this latter situation is that perhaps we neglect to refresh the
file after a failed run.  At any rate the VSAM file processing CICS commands do
need to check for DUPlicate KEYs. And you can not check for that if CICS
insists upon abending. So you must override that default with a HANDLE or an
IGNORE.

There is a glitch here. When you suspend CICS's default it remains suspended
(and set to your HANDLE) until you reset it.  This is the most subtle problem
in CICS.  

A coder can get it really clear that they must override a default, so they
issue the HANDLE condition command, then they issue the basic command they are
interested in. Every thing is fine, no problem, no condition, no handle. But
somewhere ten miles down stream another command encounters the condition (which
maybe the programmer did not know could happen). Presto the system jumps way
back to that other handle paragraph, which can be real pathological.

The solution is to code IGNORE instead, or to be rigorous in reseting the
HANDLEs after the command of interest, or perhaps set the handles exhaustively
in lengthy expressions in front of every command. Some caommands also permit a
NOHANDLE parm on a specific call. 
A program can be very complex in the overall pattern of HANDLE / NOHANDLE, and
IGNORE.  But really it all comes down to one command at a time.

Do you have abend-aid in your environment, or some other instrument that lists
the abends in the CICS region you are using?

Also, note that this is a design issue you are facing.  It may be appropriate
to abend the program on duplicate key for the spefic call in the specific
situation.  Do not misunderstand the notion of overriding CICS default
behaviour.  Sometimes the default is fine, other times not (even within a
single module).


Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 4)_

- **From:** nan_forrant@bigfoot.com
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71al5j$33f$1@nnrp1.dejanews.com>`
- **References:** `<7192tp$qik$1@supernews.com> <19981029050029.24005.00000805@ng-fd1.aol.com>`

```
In article <19981029050029.24005.00000805@ng-fd1.aol.com>,
  rkrayhawk@aol.com (RKRayhawk) wrote:
> On Thu, 29 Oct 1998 00:41:46 -0600
> "Jason" <superj@door.net>
…[24 more quoted lines elided]…
> For this third category, you can change CICS behavior.  Before the command,
you
> issue a CICS HANDLE command for that specific condition. This overrides the
> abend default and will send control back to your program.
…[8 more quoted lines elided]…
> condition command (just prior to the command that may encounter that
condition.
>  This too will disable CICS's default behavior. But rather than jump off to
> some wild place with GO TO like semantics, IGNORED conditions just pass
control
> back at the end of the failing command, and then you can interrogate RESP and
> RESP2.
…[13 more quoted lines elided]…
> as having UNIQUE or NONUNIQUE keys. The VSAM file defintion might be wrong,
and
> it may be that the program is supposed to be dealing in duplicate records.
>
…[5 more quoted lines elided]…
> tried to add the record repeatedly. That will happen a lot, especially when
you
> are first bring a system up in test or in production.  Frequently the first
try
> does not work.
>
> The mistake in this latter situation is that perhaps we neglect to refresh the
> file after a failed run.  At any rate the VSAM file processing CICS commands
do
> need to check for DUPlicate KEYs. And you can not check for that if CICS
> insists upon abending. So you must override that default with a HANDLE or an
…[9 more quoted lines elided]…
> somewhere ten miles down stream another command encounters the condition
(which
> maybe the programmer did not know could happen). Presto the system jumps way
> back to that other handle paragraph, which can be real pathological.
…[19 more quoted lines elided]…
>
This depends on if it is a "AEI0(number) or AEIO leterr O) if it is a letter o
you are correct its a dupkey if its a Number 0 then the abend is that the
Program its trying to execute does not Exist----

nancy

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 5)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981029175626.00971.00000961@ng122.aol.com>`
- **References:** `<71al5j$33f$1@nnrp1.dejanews.com>`

```
On Thu, 29 Oct 1998 21:02:43 GMT

From: nan_forrant@bigfoot.com

Corrected my error. Thankyou, Nancy

It was numeric-0 AEI0, not alphabetic-O AEIO.  Ooops!  Another poster addressed
the actual problem effectively.


Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: more cics pains

- **From:** swiegand@neo.rr.com (SkippyPB)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363a88b3.3324090@news-server>`
- **References:** `<7169rh$b8b$1@supernews.com> <363937fc.4757669@news-server> <7192tp$qik$1@supernews.com>`

```
On Thu, 29 Oct 1998 00:41:46 -0600, "Jason" <superj@door.net>
enlightened us:

>This is the error I am getting:
>
…[5 more quoted lines elided]…
>
AEI0 is a Program Id error.  In other words, CICS could not find the
program you were trying to link to when the PF12 key was pressed.

Cheers,

          ////
         (o o)
-oOO--(_)--OOo-
Cats know how we feel. They don't give a damn, but they know.
 Steve
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-tcWDd44Zd7nD@Dwight_Miller.iix.com>`
- **References:** `<7169rh$b8b$1@supernews.com> <363937fc.4757669@news-server> <7192tp$qik$1@supernews.com> <363a88b3.3324090@news-server>`

```
On Thu, 29 Oct 1998 15:29:51, swiegand@neo.rr.com (SkippyPB) wrote:

> On Thu, 29 Oct 1998 00:41:46 -0600, "Jason" <superj@door.net>
> enlightened us:
…[11 more quoted lines elided]…
> 


I think the problem is that he is trying to link to the TRANSACTION Id
instead of the PROGRAM Id.

Maybe?
```

###### ↳ ↳ ↳ Re: more cics pains

- **From:** wobconsult@sprynet.com
- **Date:** 1998-10-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71f5em$2vd$1@nnrp1.dejanews.com>`
- **References:** `<7169rh$b8b$1@supernews.com> <363937fc.4757669@news-server> <7192tp$qik$1@supernews.com>`

```
In article <7192tp$qik$1@supernews.com>,
  "Jason" <superj@door.net> wrote:
> This is the error I am getting:
>
…[6 more quoted lines elided]…
>
Jason,

IBM introduced a facility in CICS/ESA 3.2.1 to lookup error conditions
On-Line. It was known as transaction CMAC. If it is installed at your site,
check it out.

Usually, AEI0 indicates that either a HANDLE CONDITION was not specified for
the particular error or the RESP or NOHANDLE parameters were not included (or
acted upon) in a CICS Command.

HTH....

Cheers,

WOB

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: more cics pains

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com>`
- **References:** `<7169rh$b8b$1@supernews.com>`

```
On Wed, 28 Oct 1998 05:20:58, "Jason" <superj@door.net> wrote:

> Thanks for the help to those who replied to my last message about problems
> with entering data to a map, THAT NOW WORKS!  Now on to another problem.  

Just curious - what was the cure to the problem?
```

##### ↳ ↳ Re: more cics pains

- **From:** "Jason" <superj@door.net>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7193ai$alt$1@supernews.com>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com>`

```

Thane Hubbell wrote in message ...
>On Wed, 28 Oct 1998 05:20:58, "Jason" <superj@door.net> wrote:
>
>> Thanks for the help to those who replied to my last message about
problems
>> with entering data to a map, THAT NOW WORKS!  Now on to another problem.
>
>Just curious - what was the cure to the problem?

Answer:  Adding,  MOVE LOW-VALUES TO ENTRYFO as the first statement of the
PROCEDURE DIVISION.  I had tried something close to that before this came
from the newsgroup.  My problem was I think I used ENTRYFF and LOW-VALUE and
it wasn't the very first statement.
Our Prof. briefly went over the suffixes, are you very familiar with their
operations.  I've been getting by with just playing around with F, O, I, and
L but not really sure what they are doing.

Thanks
```

###### ↳ ↳ ↳ Re: more cics pains

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com>`

```
On Thu, 29 Oct 1998 06:47:58, "Jason" <superj@door.net> wrote:

> 
> Thane Hubbell wrote in message ...
…[15 more quoted lines elided]…
>

Thanks for the update.

I and O are the input and output definitions of your fields in the 
symbolic map.

L is the length attribute.

Off the top of my head, I can't recall what the F is for!  Some CICS 
programmer eh?  Anyone?
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 4)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71a7sm$7b2$1@callisto.clark.net>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com>`

```
In article <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com>,
Thane Hubbell <redsky@ibm.net> wrote:

[snippage]

>Off the top of my head, I can't recall what the F is for!  Some CICS 
>programmer eh?  Anyone?

Off the top of my head... Field Attribute Character?

DD
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-VDPk9jxqXZ4i@Dwight_Miller.iix.com>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com> <71a7sm$7b2$1@callisto.clark.net>`

```
On Thu, 29 Oct 1998 17:16:06, docdwarf@clark.net () wrote:

> In article <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com>,
> Thane Hubbell <redsky@ibm.net> wrote:
…[8 more quoted lines elided]…
> 

Thats it.  I remembered just before you said it.  Yeah.
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 6)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363ccdbe.18424282@news3.ibm.net>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com> <71a7sm$7b2$1@callisto.clark.net> <Jl0PnHJ5PvPd-pn2-VDPk9jxqXZ4i@Dwight_Miller.iix.com>`

```
On 29 Oct 98 19:24:33 GMT, redsky@ibm.net (Thane Hubbell) wrote:

>On Thu, 29 Oct 1998 17:16:06, docdwarf@clark.net () wrote:
>
…[12 more quoted lines elided]…
>Thats it.  I remembered just before you said it.  Yeah.  


Unfortunately, though, your memory is failing you...<g>  See my reply to the little one
with the academic title...

with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 7)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-ZYhL0N0PnLWe@Dwight_Miller.iix.com>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com> <71a7sm$7b2$1@callisto.clark.net> <Jl0PnHJ5PvPd-pn2-VDPk9jxqXZ4i@Dwight_Miller.iix.com> <363ccdbe.18424282@news3.ibm.net>`

```
On Thu, 29 Oct 1998 20:21:55, vbandke@ibm.net (Volker Bandke) wrote:

> Unfortunately, though, your memory is failing you...<g>  See my reply to the little one
> with the academic title...
> 
> with kind regards
>

You know ... EVERYBODY gets old.... that includes you! <G>
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 8)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36394cea.50977041@news3.ibm.net>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com> <71a7sm$7b2$1@callisto.clark.net> <Jl0PnHJ5PvPd-pn2-VDPk9jxqXZ4i@Dwight_Miller.iix.com> <363ccdbe.18424282@news3.ibm.net> <Jl0PnHJ5PvPd-pn2-ZYhL0N0PnLWe@Dwight_Miller.iix.com>`

```
On 29 Oct 98 23:41:13 GMT, redsky@ibm.net (Thane Hubbell) wrote:

>On Thu, 29 Oct 1998 20:21:55, vbandke@ibm.net (Volker Bandke) wrote:
>
…[6 more quoted lines elided]…
>You know ... EVERYBODY gets old.... that includes you! <G>


oh, wouldn't I know it! <bg>
with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 8)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71clnl$udv$1@callisto.clark.net>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-VDPk9jxqXZ4i@Dwight_Miller.iix.com> <363ccdbe.18424282@news3.ibm.net> <Jl0PnHJ5PvPd-pn2-ZYhL0N0PnLWe@Dwight_Miller.iix.com>`

```
In article <Jl0PnHJ5PvPd-pn2-ZYhL0N0PnLWe@Dwight_Miller.iix.com>,
Thane Hubbell <redsky@ibm.net> wrote:
>On Thu, 29 Oct 1998 20:21:55, vbandke@ibm.net (Volker Bandke) wrote:
>
…[6 more quoted lines elided]…
>You know ... EVERYBODY gets old.... that includes you! <G>

Well, I cannot say things about 'everybody'... but for most folks I know
getting older beats the alternative, aye.

DD
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 5)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363bcca5.18143959@news3.ibm.net>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com> <71a7sm$7b2$1@callisto.clark.net>`

```
On 29 Oct 1998 17:16:06 GMT, docdwarf@clark.net () wrote:

>In article <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com>,
>Thane Hubbell <redsky@ibm.net> wrote:
…[8 more quoted lines elided]…
>DD
Nope,

xxxxF is a FLAG byte. it contains X"00" when nothind special has happened during a RECEIVE
MAP.  It will contain X'80" if the field xxxx has been ERASED using the Erase to End of
Field key, and it will contain X'02' iff a) CURSLOC=YES was specified on the MAP
definition, and b) the cursor was in the field when the AID (Attention Identifier) was
pressed

HTH
with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 6)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36395EA8.DB308FBC@att.net>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com> <71a7sm$7b2$1@callisto.clark.net> <363bcca5.18143959@news3.ibm.net>`

```
Volker Bandke wrote:
> 
(snip)
> xxxxF is a FLAG byte. it contains X"00" when nothind special has happened during a RECEIVE
> MAP.  It will contain X'80" if the field xxxx has been ERASED using the Erase to End of
> Field key, and it will contain X'02' iff a) CURSLOC=YES was specified on the MAP
> definition, and b) the cursor was in the field when the AID (Attention Identifier) was
> pressed

Thank you, Volker! This is better than sliced bread.

Bill Lynch
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 6)_

- **From:** docdwarf@clark.net ()
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71clpt$765$1@clarknet.clark.net>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com> <71a7sm$7b2$1@callisto.clark.net> <363bcca5.18143959@news3.ibm.net>`

```
In article <363bcca5.18143959@news3.ibm.net>,
Volker Bandke <vbandke@bsp-gmbh.com> wrote:
>On 29 Oct 1998 17:16:06 GMT, docdwarf@clark.net () wrote:
>
…[15 more quoted lines elided]…
>Field key, and it will contain X'02' iff a) CURSLOC=YES was specified on the MAP

Well, so much for the top of my head, then... maybe I should bring it in
for re-sharpening.  Greatly appreciated, old man.

DD
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 4)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-10-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36395E1D.E953B5B4@att.net>`
- **References:** `<7169rh$b8b$1@supernews.com> <Jl0PnHJ5PvPd-pn2-HzM07RnPoIM9@Dwight_Miller.iix.com> <7193ai$alt$1@supernews.com> <Jl0PnHJ5PvPd-pn2-vj4iBoBogU9L@Dwight_Miller.iix.com>`

```
Thane Hubbell wrote:
> 
> On Thu, 29 Oct 1998 06:47:58, "Jason" <superj@door.net> wrote:
…[28 more quoted lines elided]…
> programmer eh?  Anyone?

field-name.F is the flag byte (if it contains x'80', the field was
erased - don't know if there are any other possible values for this
field; field-name.A is the attribute byte).

I understand it's difficult when learning a new subject, especially one
like COBOL, to think about refining what your Prof. presents; but the
field names on the DFHMDI macro aren't limited to 7 characters plus the
BMS suffix (that's an Assembler limitation from before AsmH - speaking
MVS here), plus you can code them like COBOL names, e.g.:

MAP-TIME  DFHMDI POS=(1,1),LENGTH=55,ATTRB=...

          DFHMDI POS=(3,1),LENGTH=11,INITIAL='Trade Date:',ATTRB=ASKIP
MAP-TRADE-DATE  DFHMDI  POS=(3,12),ATTRB=(UNPROT,IC)

etc.

Yes, the blank line are legal, now. The DSECT run (we discussed this
just a week or two ago) will create a data structure in COBOL notation,
with the names specified, plus the BMS suffixes (A, L, I, O, as
described elsewhere). I think the name field has a maximum of 30
characters (including the BMS suffix), but cannot guarantee it (it might
be bigger with HLASM).

If your Prof. doesn't cover this in class, think how impressed he/she'll
be when you use it and it works! (This was always good for extra credit
when I was a student/teacher).

Bill Lynch

PS: the above is from memory, if the keyword for attribute is supposed
to be ATTRIB instead of ATTRB, go with that. While HLASM supports mixed
case input, BMS does not. BMS keywords must be in caps, e.g., "ASKIP" &
"BRT" are valid values for the attribute byte, but "askip" & "brt" are
not.
```

#### ↳ Re: more cics pains

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 1998-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36375C40.FB888D2B@yahoo.com>`
- **References:** `<7169rh$b8b$1@supernews.com>`

```
Jason wrote:

> Thanks for the help to those who replied to my last message about problems
> with entering data to a map, THAT NOW WORKS!  Now on to another problem.  I
…[18 more quoted lines elided]…
> books that teach living life as an algorithm, would be great!

You are most likely getting a MAPFAIL condition on your RECEIVE of an empty
map.  You must code for this.  Check your books!
```

##### ↳ ↳ Re: more cics pains

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981028163700.29716.00000180@ng37.aol.com>`
- **References:** `<36375C40.FB888D2B@yahoo.com>`

```
Jason Wrote:
>>
...any time the aid key is hit to exit or go to another program I get an
abend...
<<
What is the error message at abend? When you do your work, what do you find is
the explanation given in the manual for the error code indicated within the
message?  What corrective action does the error message manual tell you to take
specifically in that specific situation?

It is very rare to get an ambiguous abend. An abend is not vague. It has a code
that tells you what is wrong. When YOU do YOUR work, what explanation do YOU
find in YOUR error message manual(s)?

Abends also tell you where the problem happens. Where is this AID key problem
happening? If you know where the problem is happening, you will then know
almost automatically what is wrong.

CICS work IS, in part, the resolution of error codes within error messages. It
is not just coding activity.

This comes as a mild surprise to some people. Programmers spend lots of time
with errors and exception handling.  Surely you are begining to see this. But
you did not start with and abend number in you post. You didn't even mention
one. You did not quote the error message, or even list the reason code present
therein. So maybe this is the point at which that which you almost already know
becomes even more clear to you. The message manuals are your primary tool. 

The message and error code manauals are much more important than the reference
manuals that explain syntax.

Have you looked up the error message yet? Have you learned how to trace an
abend back to the exact statement that crashes? Once you learn that pathway
back to the source code statement, you will find that, more often then not, you
will immediately see what is wrong.

Problems usually do not occur vaguely 'somewhere' in EVALUATE statements.  When
you abend there is an exact location. 

Admitedly, charlie-fours can sometimes require some second guessing. 

At any rate, you display two WHEN clauses from the EVALUATE. It is generally a
good idea to code a WHEN OTHER clause (if you have not done so).  In this case
it would do something like send a error message to the screen indicating an
unrecognized key or unrecognized condition.

In an academic environment, and even professionally in early testing, it is not
a bad idea to display return codes from service software like CICS, IMS or DB2
when something unexpected happens.

In production code we would normally not bother a user with too much detail in
that area.  And actually on the communication side it can be a dangerous habit
to echo error codes back to a terminal, as this could be just what a hacker is
looking for to break-in. Sensitive systems will sometimes log much detail, but
just tell the user in polite language to contact the Help Desk.   But in the
begining, go ahead and send the codes back out to the screen to educate your
self.

If it is not what you expect then what is it? But the sad news is, in CICS you
are frequently dealing with values formatted in a way that you should not send
as raw data to the screen. Response code, and response code two, and the
attention identifier would need some proper formatting before sending  to the
screen within an error message.

At this stage you are probably capable of coding an X(N) field to receive any
of these values, redefine it as a binary numeric, and then move form the
numeric definition to a display numeric (either within an error message, or in
preparation for a move to a message area).  

But even if you are ready for this, truthfully you already are being told what
the problem is. You just need to look up the error code and also learn how the
abend points back to the exact location of the detection of the problem. It
happens right there or perhaps just before the location that the abend
identifies.

A good guess is that you have left something out (we all do that, it happens a
little more often for beginners). Beyond a shadow of a doubt the most common
omission is response code checking.  This is repeating a slightly adding to
another poster's comment.  Did you check the response code on all CICS
invocations prior to the evaluate statement?  

Do all response code checks 
  a) have a WHEN OTHER clause for EVALUATE statement interrogation, or 
 b) have ELSE clauses coded for all IF-THEN clauses checking the response code?


As an aside let me comment that the RETURN statement in your listed code seems
a little curious because you have not indicated that you do a SEND prior to
this, I think that is going to leave your primary facility (the teminal)
orphaned. This coudl lead to subsequent confusing errors.

On the other portion of the EVALUATE presented; can you confirm that program
'a001' actually exists?  Is it in the library that CICS can reach? Your posting
is displaying lower case letters.  I know that you might even being working the
internet on a device separate from your CICS work.  But it is worth asking;
could there be a difference here between 'a001' and 'A001'?

Most modern COBOLs will support text in upper and lower case. But linkage
editors and service software like CICS may not necessarily do this for you
readily.

In addition to telling you where in a program a problem is detected, an abend
tells you (yes this is basic) which program abended. That is important here,
becasue either now or in the very near future you will get to 'a001', and you
could abend there. Be sure to learn how to determine which program you are in
when you study the error message.

Let us know how it goes. You are doing very well to be juggling COBOL, CICS,
the source code editor and the internet at the same time! It won't be long and
you will be teaching us.











Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: more cics pains

- **From:** "Jason" <superj@door.net>
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<719674$q3d$1@supernews.com>`
- **References:** `<36375C40.FB888D2B@yahoo.com> <19981028163700.29716.00000180@ng37.aol.com>`

```
Thank you for your help.  First all, I noticed you used "YOU" and "YOUR" in
your message, I took as though you think I am trying to get someone else to
do my work.  Please rest easy if that is the case, I want to learn what I am
doing.  It is just that I very often have problems finding very basic stuff.
My professor is a very busy man and only has about four hours a week to see
300 some odd students outside of class (gets a little hectic when
deliverables are due).  I come to this newsgroup for professional
information and a kick in the right direction.  I thank you and the others
for your advice.

1.)Where can I get access to message and error code manuals?  My professor
has a link to an IBM site, but IBM redirects the link to their homepage.  Do
you know how hard it is to get a hardcopy of these manuals?  Or do you know
of another web site with these messages?  This is where my Prof's link takes
me :
http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/DFHLG408/CCONT
ENTS

2.)Now,  I have coded a WHEN OTHER for any invalid keys, that displays an
error message in the map and it is working fine.  The program does recognize
F12 and F3, but it doesn't know where to go.

3.)I am not real sure what displaying the return codes means?  Are you
talking about when I am going through the CEDF and to display a message
there at some point?

4.)Yes the program 'A001' does exist, it is a program accessible by students
that the Prof has created.  My account has been set up to use only UPPER
case (in COBOL) all the way through, so the lower case 'a' was my fault in
posting the portion of code.


5.) I appreciate the your help, you are showing me a tremendous amount of
help.  I was wondering if you could tell me (you sound like you would know)
where COBOL is going?  I hear that lots of companies are going to other
languages, but I also know that there are many companies that have too much
code and data to make a change over that wouldn't cost millions (AT&T I know
of for sure).  I am also wondering does it ever get easier with more
experience, you make sound like so, or are you  the person who picked it all
up in 15 minutes?

Jason
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 4)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981029040102.24005.00000795@ng-fd1.aol.com>`
- **References:** `<719674$q3d$1@supernews.com>`

```
Date: Thu, 29 Oct 1998 01:35:48 -0600
"Jason" <superj@door.net> 
wrote in part

>>
5.) I appreciate the ... help, you are showing me a tremendous amount of
help.  I was wondering if you could tell me (you sound like you would know)
where COBOL is going?  I hear that lots of companies are going to other
languages, but I also know that there are many companies that have too much
code and data to make a change over that wouldn't cost millions (AT&T I know
of for sure).  I am also wondering does it ever get easier with more
experience, you make sound like so, or are you  the person who picked it all
up in 15 minutes?
<<

It is excesively generous of you to ask for such a comment. But being not
bashful, I will share the notions I have encountered which seem reasonable.

It all just keeps getting bigger and more complex. Fundamentals like the COBOL
language are here to stay, and will no doubt increase in usage. The whole data
processing domain is increasing at a rate that is basically impossible to
actually comprehend.  COBOL's relative share has declined as other disciplines
arrived, but the raw count of COBOL code does not seem to have decreased. A
very large portion of all the world's data is in files and databases
maintanined by COBOL programs.

Interestingly enough, the supply of COBOL programmers declined very very
rapidly since the late 70's (as I would mark it). So an imbalance exists in the
market place.  Demand is high, supply is low, prices are currently rather high
for COBOL programmers.

There is a vast amount of Business Oriented Code in existence, and it is
producing very substantial accumulation of wealth for large corporations. A
gigantic portion of business code is written in COBOL.

The central fact of the very verbose and English like syntax of COBOL is that
code written by one person can be fairly easily understood by another person.
That is essential for auditing, and definitely keeps maintenance cost under
control.

Other, more terse languages, like C/C++ offer a magnificently expressive medium
for a coder. But the artifacts left behind are much more difficult to
understand than the more mundane COBOL source code. 

The key to COBOL's staying power is that it is not a functional language, it is
not algebraic, but is instead very literal.

Traditionally COBOL is not recursive (that is changing), it is linear.  So
COBOL is much more accessible by a much wider group of people than other
languages.

All existing programs are potentially subject to the Y2K time bomb.  The size
of the concern about this issue in business code is simply in proportion to the
size of the existing code (mostly in COBOL). But I think there is a much more
surprising time bomb building in C/C++ systems, and especially C++.

As the shear quantity of C++ code accumulates, we will eventually learn that
there are major system that can not be maintained at all, because no one will
know what they do. 

Such monster definitely exist in COBOL. But it is much easier to try to root
out the meaning of a system when it is represented in the literal style of
COBOL than it will be to scrutinize C++ code.

The exact problem with the alternative languages, is that they are much more
cerebral. The abstraction needed for C++ simply puts that kind of source code
beyond the reach of a significant portion of the populace available for coding.

There are many other languages, but what we have found is that there really is
a need for only one popular, basic, and easily comprehendible language for
business. Just as FORTRAN functioned for an amazing period as the only needed
scientific (formulaeic) language.

So as far as where COBOL is going, regrettably it is now going to become
somewhat functional, and somewhat recursive. What is happening is convergence,
and workers will not be COBOL programmers OR C programmers.  They will need to
be both. Atleast to some extent.

Their will remain a large amount of work that is essentially pure COBOL, with
service package attachments (like CICS teleprocesing engines, and SQL database
engines).

More Later, ...











Subject: Re: more cics pains
Path:
lobby01.news.aol.com!newstf02.news.aol.com!portc01.blue.aol.com!news-peer.
gip.net!news.gsl.net!gip.net!news.maxwell.syr.edu!worldfeed.news.gte.net!S
upernews73!supernews.com!Supernews69!not-for-mail
From: "Jason" <superj@door.net>
Newsgroups: comp.lang.cobol
Date: Thu, 29 Oct 1998 01:35:48 -0600

Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: more cics pains

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-YhFs87xkgT2Q@Dwight_Miller.iix.com>`
- **References:** `<36375C40.FB888D2B@yahoo.com> <19981028163700.29716.00000180@ng37.aol.com> <719674$q3d$1@supernews.com>`

```
On Thu, 29 Oct 1998 07:35:48, "Jason" <superj@door.net> wrote:

> 
> 5.) I appreciate the your help, you are showing me a tremendous amount of
…[7 more quoted lines elided]…
> 

I see more and more messages these days about people with COBOL 
systems trying to take them to something else.  Why, I don't know. I 
have not heard of much success, but then again it might not get 
reported here.  

That said, I see a LOT of NEW development in COBOL happening too.  
Mostly by those who know better.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
