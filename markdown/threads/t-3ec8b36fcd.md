[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

_8 messages · 4 participants · 2003-04_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-04-04T09:16:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0304040916.76f0d407@posting.google.com>`

```
I've created a new run time system (which I've named rtsora64) using
the make file provided by Oracle. Its running great, but I'm having
trouble getting one of the great features of SE working with the new
rtsora: unsolicited dynamic attachment.

As a test, I've compiled the tictac.cbl program supplied with SE to an
animatable .gnt file. If I use cobrun (which is a link to rts64) to
start tictac.gnt the from another session use anim (which is a link to
anim64) and the PID of the original rts64 process - the animator
window pops up and I am able to "take control" in the animator of the
remote process. However, when I use rtsora to start tictac.gnt, then
use anim from another session, I am unable to do anything in the
animator window.

Here is the command line I used (provided by Oracle) to build the new
rtsora64:

cob64 -C nolist -o /orasoft/app/oracle/product/9.2.0/precomp/lib/rtsora64
-t
-xe  /orasoft/app/oracle/product/9.2.0/precomp/lib/cobsqlintf.o
/orasoft/app/oracle/product/9.2.0/lib/scorept.o
/orasoft/app/oracle/product/9.2.0/lib/sscoreed.o
/orasoft/app/oracle/product/9.2.0/rdbms/lib/kpudfo.o -L
/orasoft/app/oracle/product/9.2.0/lib/ -lclntsh

My best guess is that anim64 is not entirely compatible with the new
rtsora64 that I've created. My questions then would be:

1) Has anyone else gotten this to work?

2) Is it possible for me to re-build anim64 into animora64 using a
build command similar to the one used above to create rtsora64?

Any help here would be appreciated.

Thanks,
Chris
```

#### ↳ Re: Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-04-04T17:59:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E8DC90C.6A2DCA26@shaw.ca>`
- **References:** `<8cc07162.0304040916.76f0d407@posting.google.com>`

```
Have you tried raising your question at M/F's Answer Exchange under Server
Express ?

Jimmy, Calgary AB

Chris wrote:

> I've created a new run time system (which I've named rtsora64) using
> the make file provided by Oracle. Its running great, but I'm having
…[34 more quoted lines elided]…
> Chris
```

#### ↳ Re: Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

- **From:** Wiggy <wignomore@btopenworld.com>
- **Date:** 2003-04-04T22:26:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6l0q4$q6t$1@hercules.btinternet.com>`
- **References:** `<8cc07162.0304040916.76f0d407@posting.google.com>`

```
Hi Chris.

Firstly, cobrun shouldn't be a link to rts64. The run-time executables
provided with Server Express -- rts32[_t] and rts64[_t] are separate
from the cobrun triggers. You shouldn't need to rebuild the anim* triggers,
nor the cobrun* triggers for working with Oracle. Rebuilding the run-time
(as you have) should be sufficient.

As the rtsora64 was linked with the -t cob flag -- i.e. it's built for
use with the threaded run-time  -- if anything, you should replace
rts64_t under $COBDIR/bin with this new executable.

I'd suggest you try this. I can't guarantee that it will resolve your
problem, but it's more likely to work. If you're still having problems,
then as Jimmy suggested, please contact Micro Focus Supportline.

Regards.

Simon.
```

##### ↳ ↳ Re: Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-04-07T10:44:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0304070944.642e6d4a@posting.google.com>`
- **References:** `<8cc07162.0304040916.76f0d407@posting.google.com> <b6l0q4$q6t$1@hercules.btinternet.com>`

```
Wiggy <wignomore@btopenworld.com> wrote in message news:<b6l0q4$q6t$1@hercules.btinternet.com>...
> Hi Chris.
> 
…[16 more quoted lines elided]…
> Simon.


Simon,

Thanks for the clarification. You are correct - I would have been
better off naming the new module rtsora64_t. I've corrected that - and
its a non-issue now.

After playing with this problem all weekend I did manage to get the
Unsolicited Dynamic Attachment working with some limited success. I
used anim64_t PID to connect to and animate an rtsora64_t process
running in a separate session. It is odd though - when animator is
first invoked, I have no control over the code until the first "CALL"
statement is executed. Until that point the animator window is
completely blank.

After that I am somewhat confused about the functionality -
Perform/Exit does not work as it does with earlier versions of MF
COBOL. That may be a problem related to SE in and of itself as opposed
to my particular problem.

So - I am about 75% of the way home - if I can just figure out why the
initial attach doesn not appear to work successfully until after the
1st CALL statement is executed I'll be in great shape.

Thanks,
Chris
```

###### ↳ ↳ ↳ Re: Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2003-04-08T17:51:15+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6uuo3$8ot$1@hyperion.microfocus.com>`
- **References:** `<8cc07162.0304040916.76f0d407@posting.google.com> <b6l0q4$q6t$1@hercules.btinternet.com> <8cc07162.0304070944.642e6d4a@posting.google.com>`

```
Hi Chris. A few further questions for you :

1. Which version of Server Express & Oracle are you using?

2. Did you compile your COBOL app using Cobsql, or by
    invoking procob directly, and compiling the output?

    If the former, when animating, you should see the
    original source code. If the latter, then you will see
    the code generated by Pro*COBOL.

    Within your user code, at the time of attaching to the
    process, are you executing EXEC SQL statements, calls
    to third party APIs etc.?

3. Are you executing your app in int code, or in
    gnt/shared object/exe ?

Simon.
```

###### ↳ ↳ ↳ Re: Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

_(reply depth: 4)_

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-04-09T06:40:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0304090540.78307312@posting.google.com>`
- **References:** `<8cc07162.0304040916.76f0d407@posting.google.com> <b6l0q4$q6t$1@hercules.btinternet.com> <8cc07162.0304070944.642e6d4a@posting.google.com> <b6uuo3$8ot$1@hyperion.microfocus.com>`

```
"Simon Tobias" <Simon.Tobias@nospam.microfocus.com> wrote in message news:<b6uuo3$8ot$1@hyperion.microfocus.com>...
> Hi Chris. A few further questions for you :
> 
…[16 more quoted lines elided]…
> Simon.


Simon,

Here are the answers to your questions:

1) Server Express - 2.0.11, Oracle 9.2.0

2) We are invoking Pro*COBOL directly and compiling the output.

3) We are executing animatable .gnt code (compiled with the -g flag).

What I am seeing when I first try to attach is the pop-up box with a
single line in it that is an entry for ADIS (which it says is not
animatable). If I then hit escapse - it closes the pop-up and leaves
me in a completely empty animator window. When the running code hits
its first CALL statement to a new COBOL module ( CALLs to SQLADR or
SQLBEX are bypassed ), then the animator window refreshes and gains
control of the app at the first line of execution in the called
module.

Doesn't seem to make much sense. If it can pick up animation at the
first CALL statement, why can't it pick it up directly upon
attachment? I don't believe it has anything to do with the Oracle
libraries because I can duplicate the behavior using the rts64_t and
the tictac.cbl program supplied with SE.

Thanks,
Chris
```

###### ↳ ↳ ↳ Re: Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

_(reply depth: 5)_

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2003-04-09T15:33:30+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b71b2f$go0$1@hyperion.microfocus.com>`
- **References:** `<8cc07162.0304040916.76f0d407@posting.google.com> <b6l0q4$q6t$1@hercules.btinternet.com> <8cc07162.0304070944.642e6d4a@posting.google.com> <b6uuo3$8ot$1@hyperion.microfocus.com> <8cc07162.0304090540.78307312@posting.google.com>`

```
> Doesn't seem to make much sense. If it can pick up animation at the
> first CALL statement, why can't it pick it up directly upon
> attachment? I don't believe it has anything to do with the Oracle
> libraries because I can duplicate the behavior using the rts64_t and
> the tictac.cbl program supplied with SE.

Hi Chris. I've spoken with a couple of colleagues, and this appears to
be resolved in a product update (SX 2.0.11 SP1) for HP-UX.

I'd suggest you download the latest update from under
http://supportline.microfocus.com , and that if you're still getting
issues with the dynamic attachment, to contact Micro Focus
SupportLine, who can assist you further.

Regards.

Simon.
```

###### ↳ ↳ ↳ Re: Animation issue with MF SERVER EXPRESS and ORACLE on HP-UX

_(reply depth: 6)_

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-04-15T05:48:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0304150448.8eb8925@posting.google.com>`
- **References:** `<8cc07162.0304040916.76f0d407@posting.google.com> <b6l0q4$q6t$1@hercules.btinternet.com> <8cc07162.0304070944.642e6d4a@posting.google.com> <b6uuo3$8ot$1@hyperion.microfocus.com> <8cc07162.0304090540.78307312@posting.google.com> <b71b2f$go0$1@hyperion.microfocus.com>`

```
"Simon Tobias" <Simon.Tobias@nospam.microfocus.com> wrote in message news:<b71b2f$go0$1@hyperion.microfocus.com>...
> > Doesn't seem to make much sense. If it can pick up animation at the
> > first CALL statement, why can't it pick it up directly upon
…[14 more quoted lines elided]…
> Simon.

Thanks Simon.

I will apply the update and see what happens. I'll post the results
here to let everyone know the outcome. Wish me luck.

Chris
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
