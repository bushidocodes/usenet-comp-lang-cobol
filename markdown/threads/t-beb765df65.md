[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol in-state program

_12 messages · 8 participants · 2001-02_

---

### cobol in-state program

- **From:** alex <alexinaustin@bwn.net-3>
- **Date:** 2001-02-13T06:50:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A892D9C.D94FACC@bwn.net-3>`

```
does anybody know how to create a program that will maintain
its previous state.  i mean, that all variables will retain their values

between calls.  of course this implies that the code is resident???
```

#### ↳ Re: cobol in-state program

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 2001-02-13T09:11:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A89409A.1963C7FC@yahoo.com>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3>`

```
alex wrote:
> 
> does anybody know how to create a program that will maintain
> its previous state.  i mean, that all variables will retain their values
> 
> between calls.  of course this implies that the code is resident???

Yes, you simply call the program as a dynamic call and all the working
storage maintains the state when called next.  To free the storage
occupied by the program issue a CANCEL call.  On an IBM Mainframe the
call statement must use a working-storage variable to hold the name of
the subprogram.

Joe

Joe
```

##### ↳ ↳ Re: cobol in-state program

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-13T09:37:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96bkb3$5bh$1@slb4.atl.mindspring.net>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3> <3A89409A.1963C7FC@yahoo.com>`

```
On IBM mainframes, you do NOT need to use CALL identifier to get a dynamic
CALL - you may *also* use the DYNAM compiler option with CALL "literal".
HOWEVER, there are some environments (most notably CICS) where the use of
the DYNAM compiler option is not allowed.

FYI,  if you are looking for information related to the original question,
check your documentation (language reference manual and/or text book) for
the term "last used state".

NOTE: In addition to using CANCEL to "end" the last-used state, it is also
possible (in current but not older compilers) to put the INITIAL attribute
on the program-id paragraph.
```

##### ↳ ↳ Re: cobol in-state program

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 2001-02-13T10:44:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A89565F.27732A7E@yahoo.com>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3> <3A89409A.1963C7FC@yahoo.com>`

```
Joseph Kohler wrote:
> 
> alex wrote:
…[14 more quoted lines elided]…
> Joe

Alex,

Once the first call to a dynamically called module is
made the program will occupy a storage area and keep
it until the job ends.  If you just need different
programs to call a "black box" program, and they are
all within the same jobstream, a dynamically called
module should work.  If you need something running all
the time independent of a single jobstream then you
need a transaction monitor type program that can stay
active and wait for calls from other processes.

Joe
```

#### ↳ Re: cobol in-state program

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-02-14T12:14:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8A76C1.61B28F32@Azonic.co.nz>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3>`

```
alex wrote:
> 
> does anybody know how to create a program that will maintain
> its previous state.  i mean, that all variables will retain their values
> 
> between calls.  of course this implies that the code is resident???

If you have a routine that is CALLed several times from another program
(or from more than one other) then by default each CALL will find it in
the state it was when it did its last EXIT PROGRAM.

To change this so that it is reloaded to its initial state on a CALL it
should be CANCELed or it should have IS INITIAL PROGRAM in its
Program-Id paragraph.

So the answer to your question is "nothing".
```

##### ↳ ↳ Re: cobol in-state program

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2001-02-14T00:41:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010213194126.24359.00000771@ng-mc1.aol.com>`
- **References:** `<3A8A76C1.61B28F32@Azonic.co.nz>`

```

Other posters have responded literally, with excellent comments.

An alternative to consider is to actually place the data you are interested in
preserving in the _calling_ program and provide addressability to such area(s)
via linkage section in the _called_ module. As long as the _calling_ module
survives its current invocation, the area(s) should stay 'static', even as you
bound in and out of the submodule that might manipulate the area(s) for you.  

This side steps the issue of dynamic/static call and the INITIAL attribute on
the submodule's PROGRAM-ID statement. ((CICS is doing this kind of thing with
getmain services and comareas, but you can do it too, ... as long as the
program that has the info in its working storage never exits, it's working
storage will survive, no matter how many submodules it invokes providing access
to the area(s).


Robert Rayhawk
rayhawk@alum.calberkeley.org
```

##### ↳ ↳ Re: cobol in-state program

- **From:** alex <alexinaustin@bwn.net-3>
- **Date:** 2001-02-14T10:57:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8AB907.73C22263@bwn.net-3>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3> <3A8A76C1.61B28F32@Azonic.co.nz>`

```
Richard Plinston wrote:

> alex wrote:
> >
…[13 more quoted lines elided]…
> So the answer to your question is "nothing".

let me restate this.  if I had a called program that increments a number and
returns it to the calling program, how do i preserve this value so that when
this program is called by ANOTHER program, I can increment the value
and return it???? .
```

###### ↳ ↳ ↳ Re: cobol in-state program

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-02-14T18:16:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IXzi6.16555$Sl.737412@iad-read.news.verio.net>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3> <3A8A76C1.61B28F32@Azonic.co.nz> <3A8AB907.73C22263@bwn.net-3>`

```
In article <3A8AB907.73C22263@bwn.net-3>, alex  <alexinaustin@bwn.net-3> wrote:

[snippage]

>let me restate this.  if I had a called program that increments a number and
>returns it to the calling program, how do i preserve this value so that when
>this program is called by ANOTHER program, I can increment the value
>and return it???? .

Ow... consider the following scenario:

User01 runs PROGA which calls INVRTN.  INVRTN verifies a CUSTNO and
returns an INVNUM to PROGA to generate an invoice.

User02 runs PROGA which calls INVRTN.  INVRTN verifies another CUSTNO and
returns the next sequential INVNUM to PROGA to generate an invoice.

User03 runs PROGA... and a bug in another program brings the system down.

Everyone curses at the screen and goes for coffee.

Everyone returns.

User03 runs PROGA which calls INVRTN... how does INVRTN know what was the
last valid INVNUM?

Might be best to write data which are needed by different applications to
a file.

DD
```

###### ↳ ↳ ↳ Re: cobol in-state program

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-14T12:36:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96ej62$7vp$1@nntp9.atl.mindspring.net>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3> <3A8A76C1.61B28F32@Azonic.co.nz> <3A8AB907.73C22263@bwn.net-3>`

```
You don't state in this "revision" whether the two separate CALLs are within
the same run-unit.

If your calling structure is:

  ProgA calls Keep-Prog (and returns to ProgA)
  ProgA calls ProgB which calls Keep-Prog (which returns to ProgB which
returns to Progra
  ProgA calls ProgC which calls Keep-Prog (which returns to ProgC which
returns to Progra

then (unless you CANCEL or use INITIAL attribute) Keep-Prog will be in "last
used state" each time you call it after the first program.

If, on the other hand, your structure is

 ProgA calls Keep-Prog (and returns to ProgA)
 ProgA does a "stop run" (or GoBack in systems that support it)
 ProgB calls Keep-Prog (and returns to ProgB)
 ProgB does a "stop run"

There there is *no* way to have Keep-Prog "remember" data values between
run-units.  You must "write" such values out to a file and then read them in
again.  No part of the COBOL data division "persists" across run-units.
```

###### ↳ ↳ ↳ Re: cobol in-state program

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-14T11:57:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8AD517.87DAAE1C@brazee.net>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3> <3A8A76C1.61B28F32@Azonic.co.nz> <3A8AB907.73C22263@bwn.net-3>`

```
alex wrote:

> let me restate this.  if I had a called program that increments a number and
> returns it to the calling program, how do i preserve this value so that when
> this program is called by ANOTHER program, I can increment the value
> and return it???? .

Write it to a file.   I used to do this with relative files.  The data entry
program would read record #1 and find where to write the next record.  It would
then add one to this number, and write record #1 out before writing the data
record.

The obvious concern here is record/file locking.  If two different programs want
to increment at the same time, the first program must open this file for update,
increment and close it before the second one can read it.
```

###### ↳ ↳ ↳ Re: cobol in-state program

_(reply depth: 4)_

- **From:** alex <alexinaustin@bwn.net-3>
- **Date:** 2001-02-15T06:22:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8BC9EA.CE945806@bwn.net-3>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3> <3A8A76C1.61B28F32@Azonic.co.nz> <3A8AB907.73C22263@bwn.net-3> <3A8AD517.87DAAE1C@brazee.net>`

```
here's my real problem.  i have coded a remote procedure call that's used
by many client programs.  This called procedure retrieves many DB2 rows
from many DB2 tables.  The result set is used by the client programs to cache
the values to be used locally on the desktop.

The problem is that each call to the remote procedure call by each client
program takes too damn long.  I was hoping for a way for the remote procedure
program to only read the DB2 tables one time, store the result set in working
storage and return the data from working storage only after the initial DB2
query.

Am I making any sense?????
```

###### ↳ ↳ ↳ Re: cobol in-state program

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-02-15T16:53:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8C0B26.55752EE3@home.com>`
- **References:** `<3A892D9C.D94FACC@bwn.net-3> <3A8A76C1.61B28F32@Azonic.co.nz> <3A8AB907.73C22263@bwn.net-3> <3A8AD517.87DAAE1C@brazee.net> <3A8BC9EA.CE945806@bwn.net-3>`

```


alex wrote:

> here's my real problem.  i have coded a remote procedure call that's used
> by many client programs.  This called procedure retrieves many DB2 rows
…[9 more quoted lines elided]…
> Am I making any sense?????

Yes, you are. Now I recall back in Micro Focus Compuserve days, Michael Mattias
describing Relative Files being used as 'temporary working storage'. Isn't this
what you are after. Depending upon how you want to get at those rows and columns,
seems to me an easy way would be to create a temporary file ISAM, sequential or
relative - it doesn't  sound like an onerous task. Given that you are using DB2
maybe you want to stick with that approach - create a separate temporary DB2 file
that they can access, but on the latter I'm speculating as I don't use DB2.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
