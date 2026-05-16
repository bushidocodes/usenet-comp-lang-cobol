[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM announces new release of z/OS (OS/390) compiler

_38 messages · 14 participants · 2001-11 → 2001-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM announces new release of z/OS (OS/390) compiler

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-11-27T12:19:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net>`

```
See full announcement at:

 http://www.ibmlink.ibm.com/usalets&parms=H_201-343


"At a Glance
IBM Enterprise COBOL for z/OS and OS/390 V3R1 provides the following new
functions:

 - Java interoperability
 - WebSphere interoperation
 - Extensible Markup Language (XML) support
 - CICS� translator integration
 - Unicode support
 - Enhancements to z/OS and OS/390 UNIX� System Services support for thread
and asynchronous signal toleration"

"Planned Availability Dates
    November 30, 2001, Alternate Function Offering
    March 29, 2002, Full-Function Offering"
```

#### ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-11-27T12:33:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u0mer$1vl$1@slb5.atl.mindspring.net>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net>`

```
(Replying to myself)

  A few other things to note.

1) This is a NEW version (not just a new release).  In "IBM-ese" that means
you need to buy it "again" and not get it as a "maintenance" upgrade.

2) "Compatibility: The following summarizes the compatibility
characteristics of IBM Enterprise COBOL for z/OS and OS/390 V3. Full details
will be provided in the Migration Guide and the Licensed Programming
Specifications.

IBM Enterprise COBOL for z/OS and OS/390 V3 provides source code and object
code compatibility with its predecessor product, IBM COBOL for OS/390 & VM
Version 2, with the following exceptions:

 - The CMPR2 compiler option has been removed, so source programs still
using VS COBOL II R1 or 2 level syntax must be migrated to conform to
ANS/ISO COBOL 85 standard rules before they can be compiled with IBM
Enterprise COBOL V3.
 - SOM�-based object-oriented (OO) COBOL applications are no longer
supported. Object Oriented COBOL syntax is retargeted for Java�-based OO
programming. Further, the primary purpose of the OO syntax is not
stand-alone OO COBOL programming, rather the syntax is intended to
facilitate interoperation of COBOL and Java.
 - Support for the VM/CMS environment is not provided in this product.
 - New reserved words are defined.
 - In addition to CMPR2, the ANALYZE, FLAGMIG, IDLGEN, and TYPECHK compiler
options are removed.
 - The pseudo-assembly listing produced by the LIST compiler option is
slightly changed, which may impact development tools that process the
listing. IBM recommends that such tools use the ADATA compiler option to
obtain desired information about the compilation, rather than the listing."
```

##### ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-27T19:05:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cuRM7.76138$8q.10290172@bin2.nnrp.aus1.giganews.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net>`

```

On 27-Nov-2001, "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

> Further, the primary purpose of the OO syntax is not
> stand-alone OO COBOL programming, rather the syntax is intended to
> facilitate interoperation of COBOL and Java.

Interesting.  This is what I have been saying I saw as the future of OO on
the mainframe.  Apparently other customers have been saying the same thing.

Mainframe users don't like interdependency, with user maintained components
requiring massive testing whenever they change.  But we do like
connectivity.  Moving towards standard, powerful connectivity tools is very
important.   The ability to pick and choose tools is useful as well.

If I could see examples of successful implementation of OO business
environment on the mainframe, I could change my mind.  But apparently IBM
couldn't find such examples, and is adjusting.
```

##### ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-11-28T12:27:41+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c04255b_5@Usenet.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net>`

```
William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:9u0mer$1vl$1@slb5.atl.mindspring.net...
> (Replying to myself)
>
That's worse than talking to yourself, Bill...:-)

>  - SOM�-based object-oriented (OO) COBOL applications are no longer
> supported. Object Oriented COBOL syntax is retargeted for JavaT-based OO
> programming. Further, the primary purpose of the OO syntax is not
> stand-alone OO COBOL programming, rather the syntax is intended to
> facilitate interoperation of COBOL and Java.

So IBM have blown OO COBOL out of the water.

(Probably for the best...most mainframers couldn't handle it anyway...<G>)

This will be in response to user reaction from people who THINK they know
about OO ("...it's just modular programming re-invented...")

So all those people who resisted it so strongly will now have to learn Java
instead, or watch all the good jobs evaporate to the guys who DO know OO and
Java... Or keep on maintaining Batch COBOL. There's a kind of irony there.

Fortunately, OO COBOL (with and without Java) is still alive and well in the
Client Server arena. It is still fulfilling the role of a BUSINESS oriented
OO language and I, for one, am using it on a daily basis for both Client
apps, and server side CGI code.

To endorse COBOL WITHOUT OO is folly when we look to the future.

This short sightedness from IBM (albeit in response to User feedback) is
really sad. Would it have hurt  so bad to maintain SOM? I hope it bites them
in the arse in a few years time...<G>

Pete.




 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2001-11-28T21:51:46+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<281120012151462287%josephk@iinet.net.au>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com>`

```
In article <3c04255b_5@Usenet.com>, Peter E. C. Dashwood
<dashwood@nospam.enternet.co.nz> wrote:

> 
> So IBM have blown OO COBOL out of the water.
> 
You say they blew it. The customer base - which is what I presume IBM
will be aiming this release at must think otherwise.
> (Probably for the best...most mainframers couldn't handle it anyway...<G>)
> 
tch tch jealousy is a curse ;)
> This will be in response to user reaction from people who THINK they know
> about OO ("...it's just modular programming re-invented...")
> 
The thing is IT IS modular programming re-invented. There is absolutely
NOTHING that OO can do that can't be done with discipline and a good
library interface.
> So all those people who resisted it so strongly will now have to learn Java
> instead, or watch all the good jobs evaporate to the guys who DO know OO and
> Java... Or keep on maintaining Batch COBOL. There's a kind of irony there.
> 
Peter, people are not resisting it for technical reasons. They just
don't see any reason to change. To me, personally, I find that the
various OO flavours of COBOL take an already wordy language and clutter
it up with extra layers of fluff.
> Fortunately, OO COBOL (with and without Java) is still alive and well in the
> Client Server arena. It is still fulfilling the role of a BUSINESS oriented
…[4 more quoted lines elided]…
> 
Actually, I suspect that OO will slowly go the way of other languages
and techniques that have attempted to displace COBOL as the king of
transactional processing.

In case you missed it, the announcement shows that IBM has made
enhancements in all the right areas. CICS, JAVA, posix, Unicode. All
the areas designed to support vast online transaction systems.
> This short sightedness from IBM (albeit in response to User feedback) is
> really sad. Would it have hurt  so bad to maintain SOM? I hope it bites them
> in the arse in a few years time...<G>
> 
Well I guess history will show :)
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-11-29T02:56:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C05A457.1142E5DE@shaw.ca>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au>`

```


Joseph Katnic wrote:

> In article <3c04255b_5@Usenet.com>, Peter E. C. Dashwood
> <dashwood@nospam.enternet.co.nz> wrote:
…[5 more quoted lines elided]…
> will be aiming this release at must think otherwise.

Which is of course the argument used by other vendors not to do anything about
OO.  I can only speculate, but I seriously doubt that OO was introduced to COBOL
at "user requests". Bill, please put thinking cap on - originally how did OO get
onto the J4 agenda - motivation from one or two vendors ?.

>
> > (Probably for the best...most mainframers couldn't handle it anyway...<G>)
…[7 more quoted lines elided]…
> library interface.

Yes in a sense it is a revamped set of modular techniques, but with its own
particular twists and turns. "NOTHING that OO can do that can't be done with
discipline and a good library interface". That's a pretty broad statement and
exactly what do you mean by a good library interface - C++, Java or whatever ?

We could flog this one to death, but there's no point, because the majority are
just not going to switch. So on the basis non-OO can parallel OO, how would you do
the following. No cheating now - entry points are not and will not be a part of
the COBOL standard. :-

*>-------------------caller1.cbl -------------------------------
Program-id.        Caller1.
Class-Control.     Caller2          is class "caller2".
Working-storage section.
01 n                                pic 9(03).
01 charx                            pic x.
01 ws-Counter                       pic 9(03) value 0.
01 ws-Number                        pic 9(03).
Object-Storage section.
01 os-Program  occurs 4             object reference.
01 ws-Object                        object reference.
Procedure Division.
 perform varying n from 1 by 1 until n > 4
   Evaluate true
     when n = 1 move "A" to charx
     when n = 2 move "B" to charx
     when n = 3 move "C" to charx
     when n = 4 move "D" to charx
   End-evaluate
   invoke Caller2 "new" using charx returning os-Program(n)
 End-perform
 move 6 to ws-Counter
 perform varying n from 1 by 1 until n > 10
   Evaluate true
     when n = 1 or 5  set ws-Object to os-Program(1)
     when n = 2 or 6  set ws-Object to os-Program(2)
     when n = 3 or 7  set ws-Object to os-Program(3)
     when other       set ws-Object to os-Program(4)
   End-evaluate
  add n to ws-counter
  invoke ws-object "getDisplay" using ws-counter
 End-perform
 STOP RUN.
*>--------------------------------------------------------------
*>-------------------caller2-------------------------------
Class-id.          Caller2
                   inherits from Base.
Class-Control.     Caller2                is class "caller2".
*>--------------------------------------------------------------
FACTORY.
*>--------------------------------------------------------------
Method-id. "new".
*>--------------------------------------------------------------
Linkage section.
01 lnk-charx                    pic x.
01 lnk-self                     object reference.
Procedure Division  using lnk-charx returning lnk-self.
 invoke super "new" returning lnk-self
 invoke lnk-self "setProgramName" using lnk-charx
End Method "new".
*>--------------------------------------------------------------
END FACTORY.
*>--------------------------------------------------------------
OBJECT.
*>--------------------------------------------------------------
OBJECT-STORAGE SECTION.
01 ThisInstanceName        pic x(08).
01 ThisCounter             pic 9(03) value 0.
*>--------------------------------------------------------------
Method-id. "getDisplay".
*>--------------------------------------------------------------
Linkage section.
01 lnk-counter                  pic 9(03).
Procedure Division using lnk-Counter.
  add lnk-counter to ThisCounter
  display ThisInstanceName, " Counter : " ThisCounter
End Method "getDisplay".
*>--------------------------------------------------------------
Method-id. "setProgramName".
*>--------------------------------------------------------------
Linkage section.
01 lnk-charx                     pic x.
Procedure Division using lnk-charx.
  string "Program"      delimited by size
         lnk-charx      delimited by size
         into ThisInstanceName
  End-string
End Method "setProgramName".
*>--------------------------------------------------------------
End OBJECT.
End CLASS Caller2.
>---------------------------------------------------------------

The result of the above displays :-

    ProgramA    Counter        7
    ProgramB    Counter        9
    ProgramC    Counter        12
    ProgramD    Counter        16
    ProgramA    Counter        28
    ProgramB    Counter        36
    ProgramC    Counter        46
    ProgramD    Counter        58
    ProgramD    Counter        109
    ProgramD    Counter        170

The above looks pretty dumb doesn't it ? And yet it's the above technique that I
use to have only ONE Class(Program) to access a virtually UNLIMITED choice of
ISAM/Relative/Sequential/Line Sequential  files. (Clarify that - there are a total
of four classes - one per file type). Pity - wont work with SQL where the DB
package calls the shots.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-29T14:51:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca>`

```

On 28-Nov-2001, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> The above looks pretty dumb doesn't it ? And yet it's the above technique
> that I
…[5 more quoted lines elided]…
> DB package calls the shots.

There are things OO can do well.  But most of these things are not things
that I want done in a mainframe environment.

I have to admit that I don't know OO CoBOL well enough to tell exactly what
you're doing here, but I HAVE worked in environments where we use called
programs for I/O.   The reasons for these called programs are some of the
same reasons given for using OO, but in actual practice I find that they
obscure errors, and make it much, much more difficult to test when this
called program gets changed.

So what is the advantage in having that "ONE Class(Program)", that overcomes
these two big costs?  (costs being that the method is hidden - making
debugging hard, and that everybody uses it - making acceptance testing real,
real hard)
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 6)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-29T10:32:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<twsN7.15850$Ju6.2650746@news20.bellglobal.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message news:0YrN7.86817

> There are things OO can do well.  But most of these things are not things
> that I want done in a mainframe environment.
>
> I have to admit that I don't know OO CoBOL well enough to tell exactly
what
> you're doing here, but I HAVE worked in environments where we use called
> programs for I/O.   The reasons for these called programs are some of the
…[4 more quoted lines elided]…
> So what is the advantage in having that "ONE Class(Program)", that
overcomes
> these two big costs?  (costs being that the method is hidden - making
> debugging hard, and that everybody uses it - making acceptance testing
real,
> real hard)

Well, one of the things it does is FORCE compliance to the rules.  Perhaps
an example.

What i want is to have absolutely standardized I/O.  Using the traditional
method, I create three copybooks ... select clause, fd, and procedures. I
then make it a standard that all I/O has to be done using performs in the
procedure division copy. In theory, I can change the three copies to
anything I want, and the rest of the code is unchanged.

In fact, after a few years, I start to find patches ... programs that do
actual I/O rather than use the standard.  Those might be simple one-ups,
things like file conversion between versions, but each and everyone of them
"breaks" the standard.  I also have to recompile everything that uses the
copybook(s) if there are any changes.  The fact remains, though, that
something like a new index changes every program that uses the routines.

If I do the same thing with OOP, I get a much simpler situation.  The only
thing that now has to be consistant is the record layout of the master file.
The indices are now burried in one program that handles all the I/O for that
class of objects.  No program cares about indices, or about methods of
updating that are not used by it.  The only thing the application level does
is get and store records. Stuff like file-locking, record sharing, etc., are
totally imbeded.  I execute things like
"INCREMENT-CUSTOMER-TRANSACTION-TOTAL" with a total disregard as to the
methodology involved ... it can change from a simple one user procedure that
reads, adds, and writes to a multi-user procedure that reads and locks,
increments, then writes and unlocks without the application having a clue
that it even happened.  None of the apps have to even be re-compiled, even
if I change the indexing methods, and the complete organization.

Sure, you can accomplish the same thing by judicious use of copybooks,
standards, etc. This is simply a different tool that happens to do it
better, along with lots of other benefits at the same time.

Donald.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-29T16:18:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u5mvi$6r4$1@peabody.colorado.edu>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com>`

```

On 29-Nov-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:

> > So what is the advantage in having that "ONE Class(Program)", that
> overcomes
…[12 more quoted lines elided]…
> anything I want, and the rest of the code is unchanged.

If you have these in copybooks or objects you had better not change them. 
Changing code that is in a thousand programs means you have to user
acceptance test a thousand programs.

> In fact, after a few years, I start to find patches ... programs that do
> actual I/O rather than use the standard.  Those might be simple one-ups,
…[4 more quoted lines elided]…
> something like a new index changes every program that uses the routines.

I don't care about the compiling them nearly as much as the testing -
especially user acceptance testing.

> If I do the same thing with OOP, I get a much simpler situation.  The only
> thing that now has to be consistant is the record layout of the master
…[14 more quoted lines elided]…
> if I change the indexing methods, and the complete organization.

Fine, as long as everything works fine and your method never needs to be
changed.

> Sure, you can accomplish the same thing by judicious use of copybooks,
> standards, etc. This is simply a different tool that happens to do it
> better, along with lots of other benefits at the same time.

Agreed.  But the problem appears to be just as big with copybooks and called
programs.

We have a program that does KSDS I/O.  I have no idea why - it is harder to
access that program than it is to do things directly.   But it has a couple
of problems:
1.  It doesn't pass the VSAM status code to the calling program when there
is an error - it simply passes on an error code signifying failure.
2.  It doesn't know that VSAM status code 97 is a good status.  When this
happens, it tells the calling program the command failed, and the calling
program aborts.   We don't know why it aborts though - if we run it again
and it works, we might assume a code 97 was the initial cause, but that's
just a guess.

OK, so the called program needs to be fixed.   But if we change this called
program, we have to test, system test, and user acceptance test every single
program that calls this routine.   Costs too much.   It is cheaper to call
programmers in periodically to try to guess what caused the program than to
go through all of this.

Fortunately, we are phasing out VSAM, so the problem will go away.

Let's replace this called program with an OO object.   Will that make it not
need maintenance?  No.  Will that maintenance require extensive testing,
systems testing, and user acceptance testing on every application that
accesses that object?   Yes.

Which is easier - coding or user acceptance testing?   Which is more
expensive?   Which is likely to become even more expensive in the future?

We need some integration - but interdependencies are costly when they have
to be maintained.

That's not to say that there isn't a place for OO in the mainframe world.  
But one of its highly touted advantages is also a big disadvantage in
environments where I have worked.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 8)_

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-11-29T16:35:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lttN7.42390$xS6.71385@www.newsranger.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu>`

```
Let's take Howards example and his legitimate concern about user acceptance.
Say we have to change something fairly basic in an OO class that is used
systemically, but we don't have time or inclination to go through the user
acceptance on the thousands of programs that utilize that class.  The solution
is to either create an Interface that utilizes that class or to create a new
class that inherits from the old.  The programs get the benefit of the tired and
true class but don't have the cost of the global user acceptance testing.


In article <9u5mvi$6r4$1@peabody.colorado.edu>, Howard Brazee says...
>
>
…[93 more quoted lines elided]…
>environments where I have worked.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-29T17:35:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PluN7.70859$YD.5989953@news2.aus1.giganews.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <lttN7.42390$xS6.71385@www.newsranger.com>`

```

On 29-Nov-2001, Thane Hubbell <nospam@newsranger.com> wrote:

> Let's take Howards example and his legitimate concern about user
> acceptance.
…[7 more quoted lines elided]…
> testing.


The old way of doing this was to have multiple versions of a copylib member,
or to ignore the standards that say to use a copy member.

In this case, we could fix the called program, give it a new name, and put
it in the library.  Each time a programmer gets called in the middle of the
night, the fix would be to change what program is called.  Gradually, it
gets implemented.   The total cost is greater, but it is spread out over
time and user.  Ugly, but doable.

I think you're proposing pretty much the same thing.  (correct me if I'm
wrong)

In both cases, the elegance of the component based design is lost, replaced
with an ugly solution.  But sometimes ugly is all that we can do.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 8)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-29T13:07:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HIuN7.15409$3i2.2609566@news20.bellglobal.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:9u5mvi$6r4$1@peabody.colorado.edu...
>
> On 29-Nov-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:
…[8 more quoted lines elided]…
> > Well, one of the things it does is FORCE compliance to the rules.
Perhaps
> > an example.
> >
> > What i want is to have absolutely standardized I/O.  Using the
traditional
> > method, I create three copybooks ... select clause, fd, and procedures.
I
> > then make it a standard that all I/O has to be done using performs in
the
> > procedure division copy. In theory, I can change the three copies to
> > anything I want, and the rest of the code is unchanged.
…[4 more quoted lines elided]…
>

No Howard, that is simply not true.  Putting a new method in an object does
NOT change any existing methods, and in fact, is very simple to do. Every
method in an object is isolated from every other method.  When I put a new
method in a program, I only have to test the ONE new program that uses that
new method. Existing code could NOT have used it ... it was not there.

> We have a program that does KSDS I/O.  I have no idea why - it is harder
to
> access that program than it is to do things directly.   But it has a
couple
> of problems:
> 1.  It doesn't pass the VSAM status code to the calling program when there
…[7 more quoted lines elided]…
> OK, so the called program needs to be fixed.   But if we change this
called
> program, we have to test, system test, and user acceptance test every
single
> program that calls this routine.   Costs too much.   It is cheaper to call
> programmers in periodically to try to guess what caused the program than
to
> go through all of this.
>

That is where you are making your error, and OOP would solve this problem.

IF the program was OOP, you could have it coded so that a single method
handles errors. Changing that method CANNOT affect other modules, it only
gets used when the system is about to crash.  Therefore you can make changes
with relative impunity, they cannot affect anything but error returns.

You could make a change that did a dump, and get some answers.  You could
also change things to remedy errors that are correctable, and simply fix
them.

> Fortunately, we are phasing out VSAM, so the problem will go away.

In other words, your methodology CANNOT be fixed, it is too complex a job.
So the correct methodology is do do nothing, and refuse to use methods that
are fixable, trusting that the problem will dissappear with time. What a
wonderfull reason for not using anything new.

> Let's replace this called program with an OO object.   Will that make it
not
> need maintenance?  No.  Will that maintenance require extensive testing,
> systems testing, and user acceptance testing on every application that
> accesses that object?   Yes.
>

No, that is not true.  You only need to test methods that use the changed
methods. Introducing a new method that is used in a single test program does
not require any testing of existing routines at all.  They are isolated by
the oop methodology.  Further to that, since you are writing the new code
using and inheriting existing methods(with bugs), you will get the advantage
of all the debugging that has been done to date.  You need only concern
yourself with situations that the existing methods fail on(the bugs you
inherited).

> Which is easier - coding or user acceptance testing?   Which is more
> expensive?   Which is likely to become even more expensive in the future?
…[6 more quoted lines elided]…
> environments where I have worked.

You keep making the claim that you cannot make any change to any system
without re-testing the entire system from scratch.  The claim is not only
wrong, but simply dumb.  If it were true, then changing a single line of
Cobol on a computer would require re-testing the operating system,
re-testing every line of JCL on every system running on the computer,
re-testing every compiler that was used on the system, and retesting the
hardware down to the point that the on/off switch still worked.

The entire idea of lowering maintenance costs revolves about isolating
modules in such a way that a change in one place cannot affect another.
That reduces maintenance.  This we have operating systems vs. languages,
such as Cobol.  Changing a Cobol program cannot change the OS, and does not
require re-testing of every program that uses the OS. Changing the OS
requires re-testing Cobol, because it is a lower level module. The name of
the game is isolating pieces of code into levels, and designing an interface
to keep them isolated. You only have to test from the change up, and you
only have to test the interface.

You keep claiming that every system written in Cobol must be one vast
monolithic structure, and cannot be isolated into levels of code in the same
way.  You then make the claim that since it HAS to be one vast monolithic
structure, that a method of coding into levels of compexity that are
isolated cannot not work.  Well duh.  Of course it cannot not work. Not if
you can only use it to write one vast monolithic structure.  You actually
have to design the system to be easily maintained first, then you have to
code it.

What you are doing is taking code like

SPAGETTI-CODE.
    * awhole bunch of shitty code

and changing it to

MAINLINE.
    perform spagetti-code thru spagetti-code exit.
    stop run.
SPAGETTI-CODE.
    * awhole bunch of shitty code
spagetti-code-exit.
    continue.

Then ranting that structure is of no use to you because it obviously makes
the code more complex.

You actually have to use a concept to make it useful. If your main reason
for using it is to do the same things the same way you always did, while
proving the new context useless, then do not expect it to help an iota. The
only reason that you can do everything that oop does with "copybooks and
subroutines" is because the only thing you have tried to do with it is
replace copybooks and subroutines.  I've been coding in Cobol for over
thirty years too, and I can do all sorts of things with OOP that I could not
do with copybooks and subroutines.  At least not without multiplying my
maintenance by a factor of twenty.

Donald
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-29T19:25:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u61v9$fb7$1@peabody.colorado.edu>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com>`

```

On 29-Nov-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:

> You keep making the claim that you cannot make any change to any system
> without re-testing the entire system from scratch.  The claim is not only
…[4 more quoted lines elided]…
> hardware down to the point that the on/off switch still worked.

It may be dumb or not, but it certainly is the way mainframe shops operate
when code is changed.  Until upper management & users are confident that
procedures can be safely changed, it will continue to be the same.

Maybe the question lies in how to persuade upper management & users that our
business applications can comfortably be as reliable as our web applications
are, and that if maintaining them at the failure level of our web
applications is good enough.


> You actually have to use a concept to make it useful. If your main reason
> for using it is to do the same things the same way you always did, while
…[8 more quoted lines elided]…
> maintenance by a factor of twenty.

Were you able to persuade management and users in a mainframe shop that you
didn't need to do such testing when you changed code in an application?  If
so, please tell us how you were able to achieve such success?

It could be that the problems with our OO systems are much smaller because
they are OO, and that the only reason they can work at all is because we
have moved beyond old technology.   But the powers that be don't look at
methodologies - they look at results.   Maybe they're all timid - all
waiting for some other shop to be the first to replace their existing
business code with OO.

I know that the steps that are OO like (called programs and copy members),
cause more problems than they solve - but it is faulty for me to assume that
going all the way OO will do the same thing.  I admit that.   I also have
not advised any of the powers that be whether they should or should not
migrate their business applications to OO.  They all have made their
decisions in that regard without me.  And apparently they all made the same
decision.

Maybe they are all wrong.  Maybe they value their current level of
reliability too much.  Maybe we should strive for the level of reliability
demonstrated by Windows and the Web.




> What you are doing is taking code like
>
…[14 more quoted lines elided]…
> the code more complex.

You assume too much.   Why not replace that performed shitty code with a
shitty object?  They all can happen.  While I am a strong advocate for good
structured code, I also see that one way of writing good structured code is
via objects.   It isn't the code design I am arguing about here, it is the
reusability which is the big question.
The more applications that use that shitty code, the more shitty
applications we have.

Wherever the shitty code is, I want to find it and fix it.  Whatever
programs are effected by that code should be tested - at least until
management deems this unnecessary.

How do you persuade management that this time, our code is safe?
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 10)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-29T15:04:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MuwN7.16004$Ju6.2755037@news20.bellglobal.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <9u61v9$fb7$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message news:9u61v9$fb7

> Maybe they are all wrong.  Maybe they value their current level of
> reliability too much.  Maybe we should strive for the level of reliability
> demonstrated by Windows and the Web.

harumph ... what a wonderfull  arguement ...


> Wherever the shitty code is, I want to find it and fix it.  Whatever
> programs are effected by that code should be tested - at least until
> management deems this unnecessary.
>
> How do you persuade management that this time, our code is safe?

The purpose of OOP is to reduce the number of modules that are affected by a
code change by isolating them.  It was started by splitting code into two
different OBJECTS ... OS's and applications.  Bringing OOP into Cobol simply
allows that decoupling to be continued into the system design, so
fundamental parts of the Cobol system can also be sealed off from tampering.
Instead of being limited to a two level design, you can make the design as
many levels as you wish, each being decoupled from the previous.

I do not know how you persuade your management to use it ... I do not know
your code or management.  It is your job, not mine, to educate your
management.

I do *my* job, though, and that is to explain to *my* management new
techniques, and how to use them to reduce the maintenance workload. It is
also my job to figure out how to do that. OOP has been quite a powerfull
tool to do just that.

I will grant that our stuff is different.  It has to run 24/7, and run
reliably, just as yours does.  The difference is that it has to work for
dozens of instalations, running different OS's, different company policies,
and different methods of doing things in various places.  We CANNOT test it
at every location, even if we wanted to. Our only recourse is to de-couple
the installation dependent stuff from the standard stuff.

Donald
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-29T20:30:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u65ot$i29$1@peabody.colorado.edu>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <9u61v9$fb7$1@peabody.colorado.edu> <MuwN7.16004$Ju6.2755037@news20.bellglobal.com>`

```

On 29-Nov-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:

> I will grant that our stuff is different.  It has to run 24/7, and run
> reliably, just as yours does.  The difference is that it has to work for
…[5 more quoted lines elided]…
> the installation dependent stuff from the standard stuff.

That makes sense.  Do you know of any business that has moved its mainframe
enterprise applications to OO CoBOL on the mainframe?  Maybe if they saw a
success story...
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 12)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-29T17:05:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IgyN7.16043$Ju6.2801221@news20.bellglobal.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <9u61v9$fb7$1@peabody.colorado.edu> <MuwN7.16004$Ju6.2755037@news20.bellglobal.com> <9u65ot$i29$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:9u65ot$i29$1@peabody.colorado.edu...
>

> That makes sense.  Do you know of any business that has moved its
mainframe
> enterprise applications to OO CoBOL on the mainframe?  Maybe if they saw a
> success story...

No, I do not.  I have used minis and then micro's most of my career, and
have not been involved in mainframes for years and years ... early 70's.
However, I think I can layout an example of what I mean, and just how it
makes the code easier.

Lets say that I am using a traditional design, and traditional Cobol
methodology.  I have a product master file, along with some two or three
dozen programs that use it. The file is Vsam/Isam, keyed on product code.
In it is the standard stuff ... product name, prices, inventory levels, etc.
etc.

I use copy statements to copy the FD and the SELECT, along with a procedural
copy to handle all the low level stuff ... read and lock, write unlock,
open, close, etc. That is all standard, and nicely together.  The real
problem is the methods used on the product file ... they are going to be
scattered all over creation.  I am going to have them in the standard file
update program that changes things like product name.  Then I am going to
use them again in the order system, the shipping system, the inventory
control system, the invoicing system, the plant scheduling system, etc.,
etc.  I might have two or three hundred programs using that file, and any
change in the copy books have to be tested for all, as you say.  If I have a
bug that corupts the product master file, I have two or three hundred
programs to look through to find the bug, as well as the same number to test
if I make a change in the copies.

Now, I go to OOP.  I write a single program that handles product objects. At
the top are all my low level routines ... the same ones that use to be in
the procedure copy converted to methods.  At the bottom, I have all the
methods that do things with that file ...  a method for standard field
updates, a method of incrementing invoice additions, an method of
decrementing invoice usage, a method of finding all of one particular
product, a method for moving it from one location to another, etc., etc.
The bug is going to be in that single program, and the only thing I now have
to test is that single program. I have, as part of the system design, a test
program for exactly that.  I can test every method in that OOP library by
creating a single test product, then running each method in the test object
using my test program.  I do not have to test 2-300 programs, because not
one of them updates the product file. What they do is decide the amounts
that the product file need be updated by, and the product code of the
product that needs updating.  Unless they need to print a total, they do not
need to even know what the totals are, they simply do something like

        INVOKE
             PRODUCT-OBJECT "ADD-TO-INVENTORY"
                USING AMOUNT-RECEIVED, PRODUCT-CODE.

When I change the object, I have to test that the ADD-TO-INVENTORY method
still works, but I do not have to even look at or recompile the routine that
uses it. The only change that would require such a test is if I changed the
name of the routine, or the format of one of the two arguements. That cuts
my maintenance down VERY significantly, as does the fact that I do not have
to look at more than one program to know where the buggy code is.  I also
find it much easier to see what other systems do ... the code that increases
the inventory of for the warehouse system is in the same module that
decreases it for the order entry system, even though it is in a separate
method, and isolated from it.

The major difference in design is organizational.  With traditional design,
the organization is in the code.  Data is passed from program to program,
using different procedures in different programs. The fact that it is the
same data in each program is handled by copies and repeating the
descriptions over and over. With OOP, the organization is in the data.
Similar sets of data (records for example) are considered as instances of a
single class of object, and all the code dealing with that class of data are
in the single program that deals with that data.  The data description only
exists once, in the object program. Copy libraries disappear, and the data
names are imbeded in the object, so that they are standardized. They are not
even used in working storage ... if I need to print a product description, I
am going to MOVE PRODUCT-DESCRIPTION of PRODUCT-OBJECT TO somewhere.

The biggest problem that I see is historic.  I am not sure that converting
existing systems is worth the effort, as it takes a MAJOR revision in design
to really get the benefit.  It also takes a system or two to get the hang of
it ... which is a major problem in a shop that does not currently use oop.
Using OOP code to write the old style just confuses the issue, and probably
produces worse code than using either method by itself.  I've done two OOP
systems now.  The first I tried to convert, and I am now redoing.  The
second I took the approach of a new design, using the old system as a user
viewpoint model.  I was able to salvage a lot of chunks of code, and the
project worked out much better.

Donald
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-30T14:38:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u85fl$6at$1@peabody.colorado.edu>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <9u61v9$fb7$1@peabody.colorado.edu> <MuwN7.16004$Ju6.2755037@news20.bellglobal.com> <9u65ot$i29$1@peabody.colorado.edu> <IgyN7.16043$Ju6.2801221@news20.bellglobal.com>`

```

On 29-Nov-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:

> The biggest problem that I see is historic.  I am not sure that converting
> existing systems is worth the effort, as it takes a MAJOR revision in
…[10 more quoted lines elided]…
> project worked out much better.

I have seen time and time again where the second choice works better. 
Bosses seem to think "simple conversions" are the way to go, but they don't
end up being simpler.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 9)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-11-30T12:46:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c06cce4_3@Usenet.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com>`

```
I have studiously avoided this argument because I was unable to formulate
all the advantages of OO into a concise easily assimilable package that
would have a chance of being understood by people who are unfamiliar with
it, and I also don't think it is so important that I'm prepared to
evangelize it.

But Don has done a brilliant job here.

Congratulations Don!

My hat is off to you.

I endorse 100% what you wrote, and without being critical of Howard (who is
usually one of the voices of Reason here) I believe that your analysis of
his resistance to these ideas is accurate...

The fact is that no minds are likely to be changed by this debate. Joe will
continue to see OO as "modular programming re-invented" because he has never
really used it in any other way, exactly as Howard sees it as a poor
substitute for Copy books because he has not used it  (or thought about
using it)in any other way.

There are no "rights" or "wrongs" here and all of us will continue to use
what works for us.

But as a piece of clear and "right to the point" prose, Don's post is the
best I have seen here in many years. It is certainly better expressed than I
could've done.

I'm saving it, Don <G>.

Pete.

Donald Tees <donald_tees@sympatico.ca> wrote in message
news:HIuN7.15409$3i2.2609566@news20.bellglobal.com...
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
> news:9u5mvi$6r4$1@peabody.colorado.edu...
…[5 more quoted lines elided]…
> > > > these two big costs?  (costs being that the method is hidden -
making
> > > > debugging hard, and that everybody uses it - making acceptance
testing
> > > real,
> > > > real hard)
…[7 more quoted lines elided]…
> > > method, I create three copybooks ... select clause, fd, and
procedures.
> I
> > > then make it a standard that all I/O has to be done using performs in
…[4 more quoted lines elided]…
> > If you have these in copybooks or objects you had better not change
them.
> > Changing code that is in a thousand programs means you have to user
> > acceptance test a thousand programs.
> >
>
> No Howard, that is simply not true.  Putting a new method in an object
does
> NOT change any existing methods, and in fact, is very simple to do. Every
> method in an object is isolated from every other method.  When I put a new
> method in a program, I only have to test the ONE new program that uses
that
> new method. Existing code could NOT have used it ... it was not there.
>
…[5 more quoted lines elided]…
> > 1.  It doesn't pass the VSAM status code to the calling program when
there
> > is an error - it simply passes on an error code signifying failure.
> > 2.  It doesn't know that VSAM status code 97 is a good status.  When
this
> > happens, it tells the calling program the command failed, and the
calling
> > program aborts.   We don't know why it aborts though - if we run it
again
> > and it works, we might assume a code 97 was the initial cause, but
that's
> > just a guess.
> >
…[4 more quoted lines elided]…
> > program that calls this routine.   Costs too much.   It is cheaper to
call
> > programmers in periodically to try to guess what caused the program than
> to
…[7 more quoted lines elided]…
> gets used when the system is about to crash.  Therefore you can make
changes
> with relative impunity, they cannot affect anything but error returns.
>
…[7 more quoted lines elided]…
> So the correct methodology is do do nothing, and refuse to use methods
that
> are fixable, trusting that the problem will dissappear with time. What a
> wonderfull reason for not using anything new.
…[9 more quoted lines elided]…
> methods. Introducing a new method that is used in a single test program
does
> not require any testing of existing routines at all.  They are isolated by
> the oop methodology.  Further to that, since you are writing the new code
> using and inheriting existing methods(with bugs), you will get the
advantage
> of all the debugging that has been done to date.  You need only concern
> yourself with situations that the existing methods fail on(the bugs you
…[3 more quoted lines elided]…
> > expensive?   Which is likely to become even more expensive in the
future?
> >
> > We need some integration - but interdependencies are costly when they
have
> > to be maintained.
> >
> > That's not to say that there isn't a place for OO in the mainframe
world.
> > But one of its highly touted advantages is also a big disadvantage in
> > environments where I have worked.
…[12 more quoted lines elided]…
> such as Cobol.  Changing a Cobol program cannot change the OS, and does
not
> require re-testing of every program that uses the OS. Changing the OS
> requires re-testing Cobol, because it is a lower level module. The name of
> the game is isolating pieces of code into levels, and designing an
interface
> to keep them isolated. You only have to test from the change up, and you
> only have to test the interface.
>
> You keep claiming that every system written in Cobol must be one vast
> monolithic structure, and cannot be isolated into levels of code in the
same
> way.  You then make the claim that since it HAS to be one vast monolithic
> structure, that a method of coding into levels of compexity that are
…[25 more quoted lines elided]…
> proving the new context useless, then do not expect it to help an iota.
The
> only reason that you can do everything that oop does with "copybooks and
> subroutines" is because the only thing you have tried to do with it is
> replace copybooks and subroutines.  I've been coding in Cobol for over
> thirty years too, and I can do all sorts of things with OOP that I could
not
> do with copybooks and subroutines.  At least not without multiplying my
> maintenance by a factor of twenty.
…[4 more quoted lines elided]…
>



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 10)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-29T23:28:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cTDN7.17260$Ju6.3031760@news20.bellglobal.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <3c06cce4_3@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message

> Congratulations Don!
>
> My hat is off to you.
>
> I endorse 100% what you wrote, and without being critical of Howard (who
is
> usually one of the voices of Reason here) I believe that your analysis of
> his resistance to these ideas is accurate...
>

Thank you ... high praise indeed.

It is the very fact that Howard is one of the voices of reason that I find
it so frustrating. The damned stuff works really well once you get the hang
of it. If it had been a dumy, I would have stayed out of it too.(Sorry
Howard, but I got annoyed). Maybe the type of work we do is that different,
but I cannot see how it is so.

Donald
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-30T14:52:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u86au$6ub$1@peabody.colorado.edu>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <3c06cce4_3@Usenet.com> <cTDN7.17260$Ju6.3031760@news20.bellglobal.com>`

```

On 29-Nov-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:

> Thank you ... high praise indeed.
>
…[5 more quoted lines elided]…
> different, but I cannot see how it is so.

Thanks.   I get frustrated as well.  I would really love to do a pilot
program working with this stuff in an enterprise environment.  But if you
think I am a hard sell, you haven't worked with the type of management that
you will find making these decisions all over the world.  I am saving off
your replies.

Lots of my arguing here is part of wishful thinking.  I want to get
arguments back that are convincing enough for me to use in the future - on
the side of OO.   And I am not going to get these without coming up with
good arguments on the other side.

(My fear is that the only way OO will come in is by having the Web take over
critical business functions - and CoBOL will be replaced by C++ and Java).
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 12)_

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-11-30T15:20:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<otNN7.43869$xS6.73850@www.newsranger.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <3c06cce4_3@Usenet.com> <cTDN7.17260$Ju6.3031760@news20.bellglobal.com> <9u86au$6ub$1@peabody.colorado.edu>`

```
On Fri, 30 Nov 2001 14:52:43 GMT, in article
<9u86au$6ub$1@peabody.colorado.edu>, Howard Brazee stated 
>
>
…[23 more quoted lines elided]…
>critical business functions - and CoBOL will be replaced by C++ and Java).

How much OO is required simply to make a report from existing data?  

I always wondered how well an OO language interacts with a database, or whether
most databases were designed with a specific language in mind the way that
Access works well with VB, etc.

I have written some crude programs in java that do payroll type functions based
on the Object type, but it takes a lot more code than I thought it would simply
to document and code all the class files.  I feel if there  were more systems
written in other languages for the mainfram the business community might have a
baseline to compare them on.  If all the systems you have seen on a mainframe
are basically COBOL, then it is hard to make a real judgement.  I think this is
the real problem.  Maybe Management types need to spend a little more money on R
& D so they can see the possibilities.  We decided since we had all of these
programs in COBOL, to use the COBOL programs to make the data and to use other
languages like Javascript and CGI to transport the information to the Web.    It
is kind of hard to find a good experienced COBOL programmer, but it would take a
huge investment to hire all new staff to convert and reprogram hundreds of
existing functions over to another language.  This kind of thing is hard to
justify economically on paper.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 12)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-30T12:26:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ocPN7.16965$3i2.3151010@news20.bellglobal.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <3c06cce4_3@Usenet.com> <cTDN7.17260$Ju6.3031760@news20.bellglobal.com> <9u86au$6ub$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:9u86au$6ub$1@peabody.colorado.edu...
>
> On 29-Nov-2001, "Donald Tees" <donald_tees@sympatico.ca> wrote:
…[3 more quoted lines elided]…
> > It is the very fact that Howard is one of the voices of reason that I
find
> > it so frustrating. The damned stuff works really well once you get the
> > hang of it. If it had been a dumy, I would have stayed out of it
…[6 more quoted lines elided]…
> think I am a hard sell, you haven't worked with the type of management
that
> you will find making these decisions all over the world.  I am saving off
> your replies.
…[6 more quoted lines elided]…
> (My fear is that the only way OO will come in is by having the Web take
over
> critical business functions - and CoBOL will be replaced by C++ and Java).

I'd like to take on a sample project, that showed the versatility ... maybe
make it public domain.

Donald
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 13)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-11-30T19:14:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C07DB27.5EE15B24@shaw.ca>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <3c06cce4_3@Usenet.com> <cTDN7.17260$Ju6.3031760@news20.bellglobal.com> <9u86au$6ub$1@peabody.colorado.edu> <ocPN7.16965$3i2.3151010@news20.bellglobal.com>`

```


Donald Tees wrote:

> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
> news:9u86au$6ub$1@peabody.colorado.edu...
…[18 more quoted lines elided]…
> make it public domain.

Interesting idea Don - but until we have a 'true' OO COBOL standard available
and portability ????

Howard's comment about "He'd love to get involved". Anybody playing with the big
monsters who wants to give it a shot, where they have access to mainframe 00 -
it goes without saying, Bill, Don, Pete, Thane and many others, including yours
truly, can be looked upon as a resource to get you started.

For our own gratification it makes sense to see you 'big guys' using OO.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 14)_

- **From:** "Donald Tees" <donald_tees@sympatico.ca>
- **Date:** 2001-11-30T15:35:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SYRN7.17297$3i2.3215593@news20.bellglobal.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <3c06cce4_3@Usenet.com> <cTDN7.17260$Ju6.3031760@news20.bellglobal.com> <9u86au$6ub$1@peabody.colorado.edu> <ocPN7.16965$3i2.3151010@news20.bellglobal.com> <3C07DB27.5EE15B24@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3C07DB27.5EE15B24@shaw.ca...
>
> > I'd like to take on a sample project, that showed the versatility ...
maybe
> > make it public domain.
>
> Interesting idea Don - but until we have a 'true' OO COBOL standard
available
> and portability ????
>

That, in fact, is the project I am thnking of doing ... an OOP module that
standardizes OOP cobol .... call it an OOP preprocessor and compiler
implementor ... after all, a compiler can be viewed as a basic OOP method,
as can a linker.  All that is left is the actual Cobol program that uses
them.  The project should be able to recompile itself and completely test
itself on any platform that has Cobol, and be inheritable by any system that
that uses it to build itself.

Donald
;<)
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-30T14:45:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u85ts$6n4$1@peabody.colorado.edu>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <9u5mvi$6r4$1@peabody.colorado.edu> <HIuN7.15409$3i2.2609566@news20.bellglobal.com> <3c06cce4_3@Usenet.com>`

```

On 29-Nov-2001, "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
wrote:

> I endorse 100% what you wrote, and without being critical of Howard (who
> is
…[8 more quoted lines elided]…
> using it)in any other way.

Actually, I see it as not obviously getting rid of the problems that occur
with copies and calls - at least not without a change in the mind sets of
bosses and users.

I have used OO and have a masters in OO, but I haven't used it with CoBOL,
nor in an enterprise environment.   Some of the difference between
environments where OO has been used successfully and where it hasn't are
based upon attitude.  Others are by extrapolating what features cause the
enterprises the most headaches (connectivity and interdependency).

In forums where OO is preached, I tend to be on the other side - but in a
typical enterprise environment, I am perceived quite the opposite.  Either
way, I want to get discussion that includes costs as well as benefits.   ALL
choices have costs and benefits.

Well, maybe I was unable to get on the side of spaghetti code in a
discussion last year - but I did recognize the argument.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 7)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2001-11-30T01:45:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C06E4D1.B71A1089@istar.ca>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com>`

```
I have maintained vendor packages on the mainframe that did all of the
VSAM I-O via dynamically called COBOL subroutines.  They were able to
switch routines and update DB2 tables instead (or ADABAS if you got that
version). One sub-routine for each file.

Clark Morris.

Donald Tees wrote:
> 
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message news:0YrN7.86817
…[53 more quoted lines elided]…
> Donald.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-30T14:53:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u86d0$740$1@peabody.colorado.edu>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <twsN7.15850$Ju6.2650746@news20.bellglobal.com> <3C06E4D1.B71A1089@istar.ca>`

```

On 29-Nov-2001, "Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:

> I have maintained vendor packages on the mainframe that did all of the
> VSAM I-O via dynamically called COBOL subroutines.  They were able to
> switch routines and update DB2 tables instead (or ADABAS if you got that
> version). One sub-routine for each file.

Don't have them.  Our VSAM files were accessed primarily by IDMS, and they
are being replaced by IDMS.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-11-29T21:23:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C06A7D2.6D4C7627@shaw.ca>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com>`

```


Howard Brazee wrote:

> There are things OO can do well.  But most of these things are not things
> that I want done in a mainframe environment.

Well remember - my reply was a challenge to Joe for his non-OO solution <G>

>
> I have to admit that I don't know OO CoBOL well enough to tell exactly what
…[4 more quoted lines elided]…
> called program gets changed.

Well I *really* like that - honesty about what you know and an admission about
the 'unknowns'. Same goes for me; the klutz who started from scratch on OO, made
some *glaring* mistakes en route, now feels more and more comfortable with the
topic day-by-day - BUT - there's still a lot I haven't yet figured. Case in
point, using Internet interfaces - I know zippo - but I'll get there.

Rather than refer back to the original I'll repeat the source and explain here.
If I hit  the wrong note on the piano keyboard, Bill, Don, Pete or Thane, step
in.

Firstly, let me emphasize something which is an absolute MUST with OO, and
vendors please note where necessary  :-

- A 'prompter' telling you, suggesting which 'canned' methods you should use. I
believe it might be a feature of Fujitsu and certainly is with other OO
languages. Currently it isn't in Net Express; I can bring up an on-line help of
method names by class - but that isn't as nifty as a 'prompter'

- LOTS and LOTS of use for copybooks to pass data through Linkage (I'll
elaborate below). Don's really come on as one of the 'converted' and has
stressed this copybook approach.

- Which methods need changing. I know you have many tools on the mainframe, but
this one is a particular boon in the Net Express IDE. I can search, in seconds,
against a project's source files to see which programs/classes use method-name
"do-this-right-now". You'll appreciate the significance of this when you are
making a method change.

So now back to that original code :-

*>-------------------caller1.cbl -------------------------------
Program-id.        Caller1.
Class-Control.     Caller2          is class "caller2".
Working-storage section.
01 n                                pic 9(03).
01 charx                            pic x.
01 ws-Counter                       pic 9(03) value 0.
01 ws-Number                        pic 9(03).
Object-Storage section.
01 os-Program  occurs 4             object reference.
01 ws-Object                        object reference.
Procedure Division.
 perform varying n from 1 by 1 until n > 4
   Evaluate true
     when n = 1 move "A" to charx
     when n = 2 move "B" to charx
     when n = 3 move "C" to charx
     when n = 4 move "D" to charx
   End-evaluate
   invoke Caller2 "new" using charx returning os-Program(n)
 End-perform
 move 6 to ws-Counter
 perform varying n from 1 by 1 until n > 10
   Evaluate true
     when n = 1 or 5  set ws-Object to os-Program(1)
     when n = 2 or 6  set ws-Object to os-Program(2)
     when n = 3 or 7  set ws-Object to os-Program(3)
     when other       set ws-Object to os-Program(4)
   End-evaluate
  add n to ws-counter
  invoke ws-object "getDisplay" using ws-counter
 End-perform
 STOP RUN.
*>--------------------------------------------------------------

The numbers used in the Counter are meaningless, just showing some code. The
important thing to notice is that Caller1 invokes Caller2 to create four
instances (instantiation) of itself, returning each as lnk-self which becomes
os-Program(n) as an object reference (HANDLE) in Caller1.  There is only ONE
copy of Caller2 loaded but the *instances* hold values applicable to each, in
this case ThisInstanceName and the Counter. The methods shown in the OBJECT
SECTION of Caller2 are COMMON to all four instances - and they are not operative
until specifically invoked, nor do they retain values - you can only retain
values by storing them in the Working Storage (J4 Standard) and currently N/E
Object-Storage Section.. I know that N/E caches 'most used methods' so you are
not constantly loading and unloading..

When I invoke Caller2 I have four handles (object references) and when I look
through the Animator they are :-

Instance1 (ProgramA)    2F 00 00 00
Instance2 (ProgramB)    30 00 00 00
Instance3 (ProgramC)    32 00 00 00
Instance4 (ProgramD)    31 00 00 00

*>-------------------caller2-------------------------------
Class-id.          Caller2
                   inherits from Base.
Class-Control.     Caller2                is class "caller2".
*>--------------------------------------------------------------
FACTORY.
*>--------------------------------------------------------------
Method-id. "new".
*>--------------------------------------------------------------
Linkage section.
01 lnk-charx                    pic x.
01 lnk-self                     object reference.
Procedure Division  using lnk-charx returning lnk-self.
 invoke super "new" returning lnk-self
 invoke lnk-self "setProgramName" using lnk-charx
End Method "new".
*>--------------------------------------------------------------
END FACTORY.
*>--------------------------------------------------------------
OBJECT.
*>--------------------------------------------------------------
OBJECT-STORAGE SECTION.
01 ThisInstanceName        pic x(08).
01 ThisCounter             pic 9(03) value 0.
*>--------------------------------------------------------------
Method-id. "getDisplay".
*>--------------------------------------------------------------
Linkage section.
01 lnk-counter                  pic 9(03).
Procedure Division using lnk-Counter.
  add lnk-counter to ThisCounter
  display ThisInstanceName, " Counter : " ThisCounter
End Method "getDisplay".
*>--------------------------------------------------------------
Method-id. "setProgramName".
*>--------------------------------------------------------------
Linkage section.
01 lnk-charx                     pic x.
Procedure Division using lnk-charx.
  string "Program"      delimited by size
         lnk-charx      delimited by size
         into ThisInstanceName
  End-string
End Method "setProgramName".
*>--------------------------------------------------------------
End OBJECT.
End CLASS Caller2.
>---------------------------------------------------------------

Now let's translate that to file handling, (and Don could make the same case for
OOP and Screen Section). Caller1 becomes CustomerEdit and I need four ISAM
files, and Caller2 becomes the Class ISAMFile. So I create four INSTANCES of
Class ISAMFile passing to each the individual file pathnames; note each instance
also stores its own SEPARATE file-status.

Remember about a month back you said "File handling is easy....". Well it is for
us grey hairs but not for the Newbies <G>. The solution, "Here kid. Here's a
class which will handle all ISAM Files". Because it is easy, very definitive
VERBs, then it is an ideal candidate for segregating off into a separate class.
Prove it once and you you use it over and over again.

Extend that further - I have a program that requires five different dialogs. All
my Windows dialog creation/display/entries/droplists/listboxes.radio button
methods etc., I have stored as methods in a class MyDialog. Now I can create
five instances of MyDialog  and send and receive values independently for each
Window back to Customer Edit. (OK before he jumps in - Pete does it with his
components <G>).

>
> So what is the advantage in having that "ONE Class(Program)", that overcomes
> these two big costs?  (costs being that the method is hidden - making
> debugging hard, and that everybody uses it - making acceptance testing real,
> real hard)

I know you still don't buy it but the advantage is reusability of proven code.
Nothing is 'buried' as you imply - KISS - common classes should have simple
methods. I'm, working with SQL now, but if I harkened back to my original ISAM
Class design I would have separate methods for Open Input, Open Output, Open
I-O, Start, Read PrimeKey, Read Next. Close :-

*>----------
Method-id. "openAsInput".
*>----------------
Linkage section.
01 lnk-result                            pic x(4) comp-5.
Procedure Division returning lnk-result.
  move zeroes to lnk-result
 Open Input ISAMFile (*note I don't have to worry about whether I called it
 Customer-History or Customer-History-File in CustomerEdit Class)

 if file-status <> "00"
   invoke FileErrors using ws-filename, ws-fileStatus
  (which does a messagebox error window)
  move 99 to lnk-result
End-if
End Method "openAsInput".
*>---------------------------

There are no dark hidden secrets in this code - simplicity itself. Nor does
EVERY user program have to be tested against this - initially test against one
or two files. Errors that occur will result from the Business
Logic(CustomerEdit) doing something daft which corrupts the file data - the File
class is a holding tank, it makes no decisions. And note that we can, as a
check, validate your wretched mainframe VSAM Error 97.

The above (files and dialogs) also introduce that delightful buzzword
POLYMORPHISM. Both the FileClass and DialogClass are polymorphic because they
accept parameters from unlike objects (different record formats for files, or
different screen layouts for dialogs).

So we want to change a method - and what is its impact ?

*>-----------------------------------------------------------
Method-id. "met-to-imp".
*>-----------------------------------------------------------
Linkage section.
01 lnk-mms                      pic 9(03)v9(02) comp-3.
01 lnk-inches                   pic 9(03)v9(03) comp-3.

Procedure Division using     lnk-mms
                   returning lnk-inches.

   if    lnk-mms <> zeroes
         compute lnk-inches  = lnk-mms * 0.0393

   else  move zeroes to lnk-inches
   End-if
End Method "met-to-imp".
*>-----------------------------------------------------------

It works just fine, but after a year's use we realize the above computation
isn't accurate enough. We need to change it to record more accurately :-

    compute lnk-inches rounded = lnk-mms * 0.03937

Only ONE program needs to be re-compiled, Convert.cbl which contains the above
method; then we run it against a couple of programs just to be happy. It does
not require you to recompile or test 100 different programs that access this
method in a large application.

Another change - we have methods "GallonsToLitres" and "LitresToGallons". They
work just fine in Canada where I'm using Imperial Gallons. Then we sell the
system to a US corporation - Oops ! We need US Gallons. Well the problem here is
how many times is this method invoked from the application. (Easy with the N/E
Search - I can find all the programs utilizing this method). Depends how complex
the problem is, but we have several options. For starters, as the application is
being used in both the US and Canada then we need to have a country-flag to tell
us what to do, perhaps held as one of several parameters in a Default or Control
file for the application.. So we have choices :-

"GallonsToLitres"     ) change both of these methods so that they accept a
"LitresToGallons"    ) flag indicating Imperial or US

introduce :-

"ImpGallonsToLitres"
"LitresToImpGallons"
"USGallonsToLitres"
"LitresToUSGallons"

and this is probably the best bet. This means that in searching original caller
source you have to add something like :-

    Evaluate true
      when Canada invoke os-Convert "ImpGallonsToLitres" using xxx returning xx
      when US        invoke os-Convert "USGallonsToLitres" using xxx returning
xx
      when etc....

Again, having got these two methods right you don't have to test 100 programs
that use them.

Another alternative, forget about the first two but change their coding :-

*>--------------------------
Method-id. "GallonsToLitres".
*>---------------------------
Procedure Division.
 Display "You need to change your programs to specify whether Imperial or US"
 accept charx
STOP RUN

Sure drastic - but makes sure no corrupted data wings its way through your
application.

You can't be definitive about changes to be made - depends upon what the
application is and its size (number of source).

Just did a recap on Thane's message. As an alternative he suggested creating a
new sub-class, so you get :-

            ISAMFile inherits from Base
            ISAMSubClass inherits from ISAMFile

  invoke os-ISAMSubClass "readPrimeKey" using xx returning xxx

Not over enthused with that one, but it has merit.

To re-iterate, to overcome your boondoggle of 'maintenance' - keep library
invoked methods short and crisp - KISS !

Copybooks - nearly forgot to comment. An absolute must, not just for record
formats but also for sets of 'longish' parameters being passed through Linkage.
I use several options when creating dialogs and sometimes I need x, y, w and h
co-ordinates when dynamically creating controls. Even though I don't use every
individual paramater on an invoke, I pass them as a common set (dilgparm.cpy)
just referencing those I require per method - this avoids debugging where a test
run tells me parameters are missing or invalid.

Your other message :-

"That makes sense.  Do you know of any business that has moved its mainframe
enterprise applications to OO CoBOL on the mainframe?  Maybe if they saw a
success story..."

This thread was about IBM OS/390 and OO. Get to it ! Be brave and confront
somebody so that you get into a small project and give IBM OO a shot ! You have
the new tools, even if not completely there, it *must have* as a minimum,
support for the examples I give above The proof of the pudding is in the eating.
Why can't it be the "U of Colorado Success Story" ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-11-29T21:57:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u6aqu$m3d$1@peabody.colorado.edu>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <3C06A7D2.6D4C7627@shaw.ca>`

```

On 29-Nov-2001, "James J. Gavan" <jjgavan@shaw.ca> wrote:

> It works just fine, but after a year's use we realize the above
> computation
…[10 more quoted lines elided]…
> method in a large application.

Let's say your computation needs to return a different type of result.   Say
your subcodes now are alphanumeric, your zip codes now are 10 digits, or can
now contain spaces, you now pass a country code, or the table you return is
now larger.  You can come up with many similar cases.

Typically with called programs, some will work, some will break.  Sometimes
the change can be subtle, as someone made an unwarranted assumption in a
called program that worked until now.   Maybe there was an implicit
limitation that was used (a bug became a feature).  Are objects immune to
this type of breakage?  Or will they need to be tested.

Sure not all changes need such extensive testing.  But programmers tend to
error on the wrong side here.

Thanks for the detailed description of that program.  I have printed it off
and will peruse it as I get time.
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 7)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-11-30T02:10:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xUBN7.241681$W8.8474471@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <3C06A7D2.6D4C7627@shaw.ca>`

```
James,

Your detail though still a little fuzzy in  my old tired mind calls to
attention something we did on the Univac I.

Grace would say, oh, we did that, we just didn't have a name for it.

Here is my example for your review.

The world of DP is mainly TAB, with it's restrictions.

The printer is 150 lines a minute, and has no programmable control.

Forms are blank pages, and reports are listings with some blank space in
either direction.

We now have a U I.  It has all kinds of features we never dreamed of...

The boss says, why can't you make that report look like it came from a
typewriter?

Oh, oh, we can.

Using extraction, shifting, etc. we can make any field look like it was
typed.

Well, we can but it takes more memory than we have.

That's O.K. We will write a routine that does it once for any numeric field
up to a certain size.
To use it, move the number to the "input field" of the routine.
Execute the routine.
Grab the results from the allocated place, and move it to where you need it.

=====

Like I/O in those days, routines like that were in all programs that needed
them. You didn't code them
if someone else had already done it. You copied it manually.  The biggest
problem with this kind of thing.

Now, substitute a uniform copy, and all do this procedure the same way.

With Flowmatic, I/O became the first standard routines in my memory.

Question?

Am I getting the idea?

Warren

James J. Gavan <jjgavan@shaw.ca> wrote in message
news:3C06A7D2.6D4C7627@shaw.ca...
>
>
> Howard Brazee wrote:
>
> > There are things OO can do well.  But most of these things are not
things
> > that I want done in a mainframe environment.
>
> Well remember - my reply was a challenge to Joe for his non-OO solution
<G>
>
> >
> > I have to admit that I don't know OO CoBOL well enough to tell exactly
what
> > you're doing here, but I HAVE worked in environments where we use called
> > programs for I/O.   The reasons for these called programs are some of
the
> > same reasons given for using OO, but in actual practice I find that they
> > obscure errors, and make it much, much more difficult to test when this
> > called program gets changed.
>
> Well I *really* like that - honesty about what you know and an admission
about
> the 'unknowns'. Same goes for me; the klutz who started from scratch on
OO, made
> some *glaring* mistakes en route, now feels more and more comfortable with
the
> topic day-by-day - BUT - there's still a lot I haven't yet figured. Case
in
> point, using Internet interfaces - I know zippo - but I'll get there.


Removed the good stuff to keep the band width  to a minimum. <G>

Warren Simmons
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 8)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2001-11-30T05:43:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C071D08.F8564B24@shaw.ca>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au> <3C05A457.1142E5DE@shaw.ca> <0YrN7.86817$8q.11538966@bin2.nnrp.aus1.giganews.com> <3C06A7D2.6D4C7627@shaw.ca> <xUBN7.241681$W8.8474471@bgtnsc04-news.ops.worldnet.att.net>`

```


Warren Simmons wrote:

> James,
>
…[48 more quoted lines elided]…
>

Yes Warren you are getting real close.

However those sub-routines - you copied them manually. Think on the word "class"
= classification, where you group like-minded routines into one class. A good
example would be metric/imperial conversions. One of the problems with OO is the
academics talk in terms of classes as being a hierarchy, an animal, four legged,
a cow, elk, moose, God knows what else. Like so many people I react "What the
hell has that got to do with dollars and cents or inventory levels ?"

>That's O.K. We will write a routine that does it once for any numeric field
>up to a certain size.
>To use it, move the number to the "input field" of the routine.
>Execute the routine.
>Grab the results from the allocated place, and move it to where you need it.

Now that to my mind is real close to Pete's components concept. I'm not gong to
steal his thunder - let him expand if sees fit.

Let me back-track on a couple of things from other messages :

1. Thane's suggestion of a sub-class, and I came up with :-

>            ISAMFile inherits from Base
>            ISAMSubClass inherits from ISAMFile

>  invoke os-ISAMSubClass "readPrimeKey" using xx returning xxx.

Thinking on that last line - that's terrible, every program accessing would have
to be changed from "invoke ISAMFile" to "invoke ISAMSubClass". Nothing really to
do with the OO methodology but to illustrate its flexibility.

a) Leave ISAMFile as is - don't change anything
b) introduce a new ISAMSubClassFile with only the pertinent methods required to
extend the operation.Calling programs requiring this have the syntax :-

    invoke ISAMSubClassFile "get-new-method" using .... returning .....

c) Don't like (a) and (b) - 1. Rename ISAMSubClass to ISAMFile, and 2. Rename
ISAMFile to ISAMSuperFile :-

        ISAMSuperFile inherits from Base (the original ISAMFile)
        ISAMFile inherits from ISAMSuperFile (this is a renamed ISAMSubClass
                with a couple of new methods)

So now we compile these two files. Your calling programs still contain :-

    invoke ISAMFile "this-method" using......returning.......

First port of call for your caller is ISAMFile - your method name is one of the
'old ones' so the message bypasses ISAMFile and finds what it wants in
ISAMSuperFile. If it is one of the new messages then it is going to be found in
the current ISAMFile.

I'm not suggesting you should do it this way - but it indicates the flexibility
- one recompile on the renamed file and a new compile for the latter.

2.  File handling - two approaches, mine culled from Will Price (objectz.com)
and Don's - both are valid given the options in OO COBOL. Let's take Don's from
what he has written :-

[Program 1]
[Program 2]    ..................each of these invokes....[ ProductFile]
[Program 3] etc....

As Don indicated, ProductFile has methods such as following :-

method-id. open
method-id. read
method-id. write
method-id rewrite
method-id close etc....
then :-
method-id. increment invoice addition
method-id decrement invoice usage
method-id find all 'particular' records (just like an SQL cursor and SELECT

DISTINCT)
method-id. move from 'a' to'b'
method-id etc....

A self-contained handler for the Product file accessed by 300 programs if
necessary. He needs a new method - so, (1) add the method to Product file and
(2) invoke it from a new program. That source change only affects the two
programs noted.

Now my version, slightly different twist. Recall me saying the FileClass doesn't
do any decision making - just contains methods for file VERBS. Back to Don's
diagram above; what I didn't include for Howard, to avoid confusion, was my
DBI(Data Base Interface) a 'go-between' the calling programs and ProductFile :-

[Program 1]
[Program 2]    ......each of these invokes..[ ProductDBI]...which in turn
invokes
[Program 3]
etc....
{ProductFile}

My Product file is the 'bare bones' containing just the file VERBS. Don's
"extras",
Methods - increment invoice addition,  decrement invoice usage,  find all
'particular' records, move from 'a' to'b' are contained in my ProductDBI,
together with methods to create collections/dictionaries, (primarily for
droplists/listboxes). Note Don invokes ProductFile direct - I don't, I invoke
ProductDBI - and if it doesn't find the method, the message further searches in
super (ProductFile).

Program 26 contains :-

    invoke ProductDBI "createCollection" using..... returning........

        within the ProductDBI :-
        method-id. "createCollection"
    --------------------------
        set FileNotFinis to true
        perform until FileFinis
            invoke super (ProductFile) "readNext" returning ls-results
            if not FileError do something with the returned record
       End-perform
        when finished return the collection to Program 26.

Having taken that approach, then I realized that my file handling, (I originally
had a separate class for ProductFile, OrderFile, CustomerFile etc.) could be
vanilla flavoured and 'generic'. That's where Bill K. helped when he suggested
:-

    01 Myrecord.
         05 pic x occurs 0 to xxxx depending on ws-CharacterCount

So I was able to take it one step further - get rid of my individual File
classes and substitute ISAMFile class. I still have the DBI classes because they
contain methods specific to each  particular file. Example, CustomerDBI is
invoked for "getAddressData" - this gets the complete record from CustomerFile
but strips off just the address info which is returned to the calling program -
and to get this right the Caller and CustomerDBI contain a copyfile for address
data.

Just illustrates, like all things COBOL, how different approaches can be
effective.

3. Howard made some queries :-

> Let's say your computation needs to return a different type of result.   Say
> your subcodes now are alphanumeric, your zip codes now are 10 digits, or can
> now contain spaces, you now pass a country code, or the table you return is
> now larger.  You can come up with many similar cases.

I would need to know specifics to answer some of the above. But some 'off the
cuff'.
This one jumps immediately to mind 'your subcodes now are alphanumeric'. I have
exactly that situation. The old RM/COBOL system contained two digit numeric
codes to tell me points being inspected, e.g. :-
01 = Top
02 =  Bottom
03 =  North
04 = South
44 = Scan Low Reading
48 = Weld Seam Pitting
49 = External Pitting

Fine, if you can remember numeric codes - but for newcomers ? After some ten
years of a static system the user then threw a zinger - 44 and 49 above were
'exception conditions', along with some others. Lordy, lordy - build a table to
check for 'exceptions', (echoes of Eileen's lousy account numbers <G>)..

So in the revamp I decided to use mnemonics :-
T    = Top
B    = Bottom
XSL = Scan Low Reading
WSP = Weld Seam Pitting
XEP = External Pitting

And to cover those exceptions I started them with an "X". Converting from RM to
MF I search a table and translate from numeric to uppercase Alpha. Same goes for
Howard. If you have  :-

*>-------------------------
method-id. "gertPointName"
*>-------------------------
Local-storage section.
01 ls-alpha                    pic x(04).
Linkage section.
01 lnk-key                    pic x(04).
01 lnk-name                 pic x(20).
Procedure Division using lnk-key returning lnk-name

if lnk-key(1:1) is numeric
   invoke self "convertCode" using lnk-key" returning ls-Alpha
    ("convertCode" is a PRIVATE method in the same class as this method solely
        there to serve this particular method)

 else move lnk-key to ls-Alpha
end-if

 invoke os-DescripsDBI "getName" using ls-Alpha returning lnk-Name
*>-------------

Other points Howard made were changing the size of descriptions. Well that
really isn't manageable by anything is it. That goes back to the original
design. The file record contained 60 characters and now the record contains 83
characters. You are talking a different file structure, so firstly a file
conversion followed by a check on all programs accessing the file.(Again that
N/E Search for inclusion of a method-name helps here).

'The table you return is larger.....". That's not a problem if you are using
collections/dictionaries - as I illustrated elsewhere - they are open ended :-

    - create MyCollection
    - invoke MyCollection "size" returning ls-size.

Jimmy
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

_(reply depth: 4)_

- **From:** <gnlsn3@charter.net>
- **Date:** 2001-12-30T15:07:58-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u2v09qaqjg4g21@corp.supernews.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com> <281120012151462287%josephk@iinet.net.au>`

```
why are there still punk kids that thing Mainframe programmers are dump - I
have a PhD and have been on both sides - the issue is Consolidated or
Distributed - but that is too complex for a newbie to understand -

"Joseph Katnic" <josephk@iinet.net.au> wrote in message
news:281120012151462287%josephk@iinet.net.au...
> In article <3c04255b_5@Usenet.com>, Peter E. C. Dashwood
> <dashwood@nospam.enternet.co.nz> wrote:
…[6 more quoted lines elided]…
> > (Probably for the best...most mainframers couldn't handle it
anyway...<G>)
> >
> tch tch jealousy is a curse ;)
> > This will be in response to user reaction from people who THINK they
know
> > about OO ("...it's just modular programming re-invented...")
> >
…[3 more quoted lines elided]…
> > So all those people who resisted it so strongly will now have to learn
Java
> > instead, or watch all the good jobs evaporate to the guys who DO know OO
and
> > Java... Or keep on maintaining Batch COBOL. There's a kind of irony
there.
> >
> Peter, people are not resisting it for technical reasons. They just
…[3 more quoted lines elided]…
> > Fortunately, OO COBOL (with and without Java) is still alive and well in
the
> > Client Server arena. It is still fulfilling the role of a BUSINESS
oriented
> > OO language and I, for one, am using it on a daily basis for both Client
> > apps, and server side CGI code.
…[11 more quoted lines elided]…
> > really sad. Would it have hurt  so bad to maintain SOM? I hope it bites
them
> > in the arse in a few years time...<G>
> >
> Well I guess history will show :)
```

###### ↳ ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-11-28T17:38:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ui9N7.40997$xS6.69054@www.newsranger.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u0mer$1vl$1@slb5.atl.mindspring.net> <3c04255b_5@Usenet.com>`

```
I think too much is being read into what was said.

Their present syntax may be insufficient (it certainly was BEFORE with just
SOM!) for full COBOL OO Development.  If they implement the next standard, then
you should be able to do full OO COBOL programming on the IBM mainframe
platform.

Truth be told, others have better OO implementations.  When I looked at it on
the OS/390 (when I had one) it was simply too lean of an implementation to be
useful.  All they are saying is that is still the case.


In article <3c04255b_5@Usenet.com>, Peter E. C. Dashwood says...
>
>William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
…[42 more quoted lines elided]…
>                http://www.usenet.com
```

#### ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-11-27T20:11:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20011127151110.11118.00001531@mb-bd.aol.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net>`

```
Bill,

Do you have a feeling how this compiler will [or will not] satisfy requirements
for the almost-approved 2002 ANSI/ISO standard?

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-11-27T15:03:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u0v57$rn5$1@slb7.atl.mindspring.net>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <20011127151110.11118.00001531@mb-bd.aol.com>`

```
My GUESS is that it has very LITTLE to do with the draft Standard.  I
wouldn't be surprised if the OO syntax is closer to what is in the draft
Standard, then the current IBM implementation, but I don't see much for
VALIDATE, common exception handling, standard arithmetic, etc.

It *DOES* say that it support Unicode - and my guess is that it PROBABLY
uses what is in the draft standard for that, but what IBM has in COBOL for
this-and-that V2R2 isn't TOO far off for that already.
```

#### ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** "Ron" <Ron@NoSpamForMe.Com>
- **Date:** 2001-11-28T10:17:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9u32mb$ltc$1@suaar1ac.prod.compuserve.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net>`

```
Tried to look at the link and got the following output.
Hope this isn't a bad omen about its subject.
Anyone have a link that works?



----------------------------------------------------------------------------
----

Abnormal Program Termination

Module: GenerateOutput
Function: see the "TRACEBACK Calls" section
Reason: Segmentation violation.
When: Wed Nov 28 08:11:54 2001
Elapse: 1.684 secs

----------------------------------------------------------------------------
----
Debug info:
TOTAL RESOURCE Usage

CPU (user/system) =   0.280 secs (0.090/0.190)
Priority          =      20
Resident Memory   =    2776 KB
Shared Memory     =   26267 KB
Unshared Memory   =  261644 KB
Minor Page Faults =    1209
Major Page Faults =       2
Swaps             =       0
Block Input       =       0
Block Ouput       =       0
Vol. Context Sw   =      88
Invol. Context Sw =      49
Master Stack Size =     272
CPU Time Limit    =      60 secs
Run Time Limit    =     300 secs

CONTENT OF Master Request Block

Client IP Address = 166.33.131.188
Client Name       = 166.33.131.188
Client Browser    = Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 4.0;
Q312461)
Request Method    = GET QUERY_STRING
Server Name       = www2.ibmlink.ibm.com
Secured Server    = N
Secured Path      = N
User Type         = G
Advantis Account  =
Advantis Userid   = GUEST
Link Userid       = GUEST
Host Userid       =
initial logon     = Wed Nov 28 08:11:52 2001
last logon        = Wed Nov 28 08:11:52 2001
request           = announcements
parms             = H_201-343
External handle   = pw7OxRowGshzIp1
Internal handle   = 24235
Namespace         = usa
Language          = english
Icon Location     = B
Icon Format       = T
Frame option      = N
Content Override  =
Pushed URL        =
Crawler Defense   = Y
Create Core File  = N

CONTENT OF entries[4]

xh                = logon
xu                = GUEST
request           = usa.announcements
parms             = H_201-343

TRACEBACK Calls (50 entries max)

Filename: ???  - ??? ??? ???
Function: rightmost

Filename: ???  - ??? ??? ???
Function: realloc

Filename: ???  - ??? ??? ???
Function: buildQueryString

Filename: ???  - ??? ??? ???
Function: HandleTOOL_BAR

Filename: ???  - ??? ??? ???
Function: handleTAG_HEADER

Filename: ???  - ??? ??? ???
Function: GenerateOutput

Filename: ???  - ??? ??? ???
Function: WWW_DS_Error

Filename: ???  - ??? ??? ???
Function: WWW_DSIF_DOCUMENT

Filename: ???  - ??? ??? ???
Function: masterControl

Filename: ???  - ??? ??? ???
Function: Execute

Filename: ???  - ??? ??? ???
Function: processRequest

Filename: ???  - ??? ??? ???
Function: main

Filename: ???  - ??? ??? ???
Function: __start

--------------------------------------------------------------------------

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9u0lg9$jcb$1@slb6.atl.mindspring.net...
> See full announcement at:
>
…[12 more quoted lines elided]…
>  - Enhancements to z/OS and OS/390 UNIX� System Services support for
thread
> and asynchronous signal toleration"
>
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** Gary Mazo <m.a.z.o.i@yahoo.com>
- **Date:** 2001-11-28T15:44:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3C0576E0.3564368B@nospamformetoo.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u32mb$ltc$1@suaar1ac.prod.compuserve.com>`

```
It looks like your browser crashed.
Have you tried a different browser (I mean other than MS IE 6.0) ?
Or checked Microsoft support?

Ron wrote:

> Tried to look at the link and got the following output.
> Hope this isn't a bad omen about its subject.
…[143 more quoted lines elided]…
> >
```

##### ↳ ↳ Re: IBM announces new release of z/OS (OS/390) compiler

- **From:** Daniel Jacot<daniel.jacot@winterthur.ch>
- **Date:** 2001-11-29T16:37:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dvtN7.42392$xS6.71396@www.newsranger.com>`
- **References:** `<9u0lg9$jcb$1@slb6.atl.mindspring.net> <9u32mb$ltc$1@suaar1ac.prod.compuserve.com>`

```
On Wed, 28 Nov 2001 10:17:12 -0600, in article
<9u32mb$ltc$1@suaar1ac.prod.compuserve.com>, Ron stated...
>
>Tried to look at the link and got the following output.
>Hope this isn't a bad omen about its subject.
>Anyone have a link that works?
>

Try http://isource.ibm.com/cgi-bin/goto?it=eme_announ&on=ZP010450

-------------------------------------------------
With kind regards
Daniel Jacot
-------------------------------------------------
visit us at: http://www.winterthur.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
