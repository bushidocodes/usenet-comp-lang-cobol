[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Deploying over IIS and VB

_16 messages · 5 participants · 2004-03 → 2004-04_

---

### Deploying over IIS and VB

- **From:** orzo617@hotmail.com (sb)
- **Date:** 2004-03-20T14:00:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e66a875b.0403201400.5c5ee637@posting.google.com>`

```
Hello,

I have Cobol Dlls written in Net Express Cobol and precompiled using
oracle 9i compiler.  I am trying to deploy these so IIS web server. 
The basic architecture is the following:

IIS spawns DLLHost.exe --> calls VB.dll (COM+ Object) --> Cobol.dll.

I have very little/no knowledge of Cobol but need to use this
Cobol.dll as a lot of business logic is written in it.

VB dll is compiled as apartment threaded, multiuse.
Cobol dll is compiled as shared, multithreaded.

Problem:
When servicing one request from a browser, everything seems to work
fine.  But when I issue two or more request concurrently or very close
to each other, I get error message "error '800706be'" Which in
Microsoft world translates to "Procedure call failed."  Can someone
enlighten me as to what is going on here?  I had thought that DLLHost
would have a separate copy of Cobol.dll for each request coming in. 
But it seems as though it only keeps on copy to service requests.  So
I suspect this is a cobol dll compilation issue.  But I am at loss;
agin no knowledge of COBOL!

As I need to get this completed SOON I would appreciate ANY
pointers/help/suggestion with this matter.
Thank you
SB
```

#### ↳ Re: Deploying over IIS and VB

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-03-21T06:35:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0403210635.59a62084@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com>`

```
orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403201400.5c5ee637@posting.google.com>...
> Hello,
> 
…[17 more quoted lines elided]…
> enlighten me as to what is going on here? 

There is  a whole lot of stuff you haven't mentioned.

Is this running as CGI or ASAPI code on IIS? (CGI is not
multi-threaded, no matter how you compile it...)

Are you using MTS to handle the database COMMIT and ROLLBACK? (if you
are, you need a transaction context as well as an object context; if
you're not, you may be in trouble with synchronising).

What settings do you have in component services for the COM+
component?Try "REQUIRES New transaction". If this fails, experiment
with the other settings for this parameter.

> I had thought that DLLHost
> would have a separate copy of Cobol.dll for each request coming in.

No. But if it has the right transaction and object contexts it can
behave as though it does. It looks as though the COBOL .dll is not a
COM server in its own right, but is simply called from the VB COM
server. This is fraught. No new instances can be instantiated and it
is little wonder you are having trouble when you try concurrent
threads. The VB COM+ server needs to get a new instance of the COBOL
.dll each time it (VB) is instantiated. It can only do this if the
COBOL .dll is also a COM server (or it is able to multiply instantiate
the object context it is running in). If the DB access is carried out
in the COBOL .dll, don't be surprised if everything grinds to a halt.

The problem is not with compile options, it is with design. 
 
> But it seems as though it only keeps on copy to service requests.  So
> I suspect this is a cobol dll compilation issue.  But I am at loss;
> agin no knowledge of COBOL!
> 

Your best chance of a quick fix is to tweak DLLHOST.EXE, using the
component services on the server. In particular, see if you can get
the VB COM+ server to run in a MTS environment, and try different
settings of the transaction support parameter for the COM+ server.

The real solution is to rebuild (not re-compile) the COBOL application
so it is a true COM+ server. Then VB can instantiate it any time it
needs to.

I have had some very painful experience implementing COM+ with IIS and
the real solution is to make COBOL another COM+ server just like
everything else. Once you do this, it works beautifully. Both IIS and
COM+ are good technologies. I don't know how MF supports the building
of COM servers in COBOL, as I use Fujitsu, but I should think there
will be equivalent functionality.

There is not enough hard information here to properly diagnose your
problem, but on the evidence, it would seem that a standard COBOL .dll
is being used with an OO COM+ component written in VB. This is like
tying an anchor to a cat and wondering why it can't get over the wall.
The COBOL needs to be OO and wrapped as a standard COM server.
Specifying "multithreading" at compile time is not enough in and of
itself, to get multiple instances. Without this capability, your
application will only ever be good for one thread.

Hope this helps.

I am no longer frequenting CLC (I look in occasionally) but would be
interested to hear how you get on.

Pete.

> As I need to get this completed SOON I would appreciate ANY
> pointers/help/suggestion with this matter.
> Thank you
> SB
```

##### ↳ ↳ Re: Deploying over IIS and VB

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-03-22T15:01:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3mv4801opb@enews1.newsguy.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com>`

```

In article <b3638c46.0403210635.59a62084@posting.google.com>, dashwood@enternet.co.nz (Peter E. C. Dashwood) writes:
> orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403201400.5c5ee637@posting.google.com>...
> > 
…[16 more quoted lines elided]…
> multi-threaded, no matter how you compile it...)

It's running under DLLHost.exe, thus it's ISAPI.  (We could draw the
same conclusion from the fact that there's no application .exe
involved - all the application code is in DLLs.)

Offhand, I'd suggest checking the reentrancy model the COBOL code was
compiled in.  In MF COBOL, thread-safe modules can be compiled with
one of three compiler directives: REENTRANT(1), REENTRANT(2), or
SERIAL.

REENTRANT(1) separates compiler-generated storage areas by thread,
but working-storage, FDs, etc are shared across threads, and the
program must serialize access to them manually.  This is the
directive to use for a threading model which is similar to the shared
heap / private stack one typically used with C-like languages.

REENTRANT(2) makes all non-external user data per-thread.  In effect,
modules compiled with REENTRANT(2) are unaware of threading; their
data is private.

SERIAL allows only one thread to be in the module at a time; the
compiler inserts a mutex around the entire module.

I note that the NX4 documentation recommends REENTRANT(2) for ISAPI
modules.

This seems like a question that's best answered by the Net Express
documentation, in fact.  There's a whole chapter on writing ISAPI
modules, and IIRC a tutorial on it as well.
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

- **From:** orzo617@hotmail.com (sb)
- **Date:** 2004-03-22T12:32:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e66a875b.0403221232.689eb0a6@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <c3mv4801opb@enews1.newsguy.com>`

```
mwojcik@newsguy.com (Michael Wojcik) wrote in message news:<c3mv4801opb@enews1.newsguy.com>...
> In article <b3638c46.0403210635.59a62084@posting.google.com>, dashwood@enternet.co.nz (Peter E. C. Dashwood) writes:
> > orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403201400.5c5ee637@posting.google.com>...
…[46 more quoted lines elided]…
> modules, and IIRC a tutorial on it as well.

Yes.  Thank You for answering on by behalf.  Indeed, I have looked
into
REENTRANT(1), REENTRANT(2) directives.  But it turns out (as per
advice from someone at Microfocus) that REENTRANT(2) clause "can not
be used with procedure division overlays; SECTIONS;"  That I need to
use the NOSEG clause.  Which I tried without success.
 
I have looked at some Cobol documentation.  Even considered the
Internet Application Wizard.  This wizard can take a legacy Cobol
source and convert it to appropriate Web Pages.  But apparently, that
version of Application Wizard does not like Indexed Fields. I was not
able to determine which version I need.  Currently I am using Net
Express version 3.1.  I am not able to find any discussion on Micro
Focus about Indexed Fields problem with this wizard.

Any ideas/pointers would be much appreciated.
SB
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 4)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-03-23T19:34:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3q3fm01s0m@enews4.newsguy.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <c3mv4801opb@enews1.newsguy.com> <e66a875b.0403221232.689eb0a6@posting.google.com>`

```

In article <e66a875b.0403221232.689eb0a6@posting.google.com>, orzo617@hotmail.com (sb) writes:
> mwojcik@newsguy.com (Michael Wojcik) wrote in message news:<c3mv4801opb@enews1.newsguy.com>...
> > 
…[7 more quoted lines elided]…
> use the NOSEG clause.  Which I tried without success.

You lost me.  You're using segmentation in this COBOL DLL (that is, it
has non-zero segment numbers specified after SECTION word)?  Why?

I wasn't aware that segmentation couldn't be used with REENTRANT(2),
but it doesn't surprise me.

In any event, your module needs to be either REENTRANT(1) or
REENTRANT(2) (or perhaps SERIAL), regardless of what other options
you use, to operate correctly in a multithreaded environment.  And
I'd definitely recommend getting rid of segmentation; it might be
possible to get that working in this environment, but it's a
tremendous complication.
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 5)_

- **From:** orzo617@hotmail.com (sb)
- **Date:** 2004-03-24T11:06:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e66a875b.0403241106.7707796c@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <c3mv4801opb@enews1.newsguy.com> <e66a875b.0403221232.689eb0a6@posting.google.com> <c3q3fm01s0m@enews4.newsguy.com>`

```
mwojcik@newsguy.com (Michael Wojcik) wrote in message news:<c3q3fm01s0m@enews4.newsguy.com>...
> In article <e66a875b.0403221232.689eb0a6@posting.google.com>, orzo617@hotmail.com (sb) writes:
> > mwojcik@newsguy.com (Michael Wojcik) wrote in message news:<c3mv4801opb@enews1.newsguy.com>...
…[21 more quoted lines elided]…
> tremendous complication.

I am afraid I have almost NO/VERY little knowledge of COBOL.  I will
try to explain as best as I can.  I am not sure if this program is
using segmentation.  But code does have non-zero segment numbers. 
That is, there are statements in the program that read "exit section" 
Clearly, there no number acter the SECTION clause.  And the code also
has statements that read "2000-save-rating section."  Again no number
after the SECTION clause.  Is this what you mean by segmentation?  I
also see embedded SQL SECTION clause like "EXEC SQL BEGIN DECLARE
SECTION END-EXEC"  I have asked the Micro Focus person who suggested I
remove REENTRANT(2) directive to explain what he means, as he has all
the associated code.

Thanks
Saurabh
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2004-03-24T14:15:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3smoe$9p4$1@panix5.panix.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <e66a875b.0403221232.689eb0a6@posting.google.com> <c3q3fm01s0m@enews4.newsguy.com> <e66a875b.0403241106.7707796c@posting.google.com>`

```
In article <e66a875b.0403241106.7707796c@posting.google.com>,
sb <orzo617@hotmail.com> wrote:
>mwojcik@newsguy.com (Michael Wojcik) wrote in message news:<c3q3fm01s0m@enews4.newsguy.com>...

[snip]

>> In any event, your module needs to be either REENTRANT(1) or
>> REENTRANT(2) (or perhaps SERIAL), regardless of what other options
…[5 more quoted lines elided]…
>I am afraid I have almost NO/VERY little knowledge of COBOL.

This is becoming more and more clear.  It might be interesting to know the 
name of the company that is outsourcing to you.

DD
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 7)_

- **From:** orzo617@hotmail.com (sb)
- **Date:** 2004-03-25T07:52:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e66a875b.0403250752.37a3d1e8@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <e66a875b.0403221232.689eb0a6@posting.google.com> <c3q3fm01s0m@enews4.newsguy.com> <e66a875b.0403241106.7707796c@posting.google.com> <c3smoe$9p4$1@panix5.panix.com>`

```
docdwarf@panix.com wrote in message news:<c3smoe$9p4$1@panix5.panix.com>...
> In article <e66a875b.0403241106.7707796c@posting.google.com>,
> sb <orzo617@hotmail.com> wrote:
…[16 more quoted lines elided]…
> DD

Come again??  Did I miss a beat?  There is no outsourcing of any kind.
 I happen to work for a firm that has cobol modules.  I need to deploy
them on our website.  I don't have COBOL experience so I thought I
would solicit advice here (period)
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2004-03-25T11:08:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3v06q$3bs$1@panix5.panix.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <e66a875b.0403241106.7707796c@posting.google.com> <c3smoe$9p4$1@panix5.panix.com> <e66a875b.0403250752.37a3d1e8@posting.google.com>`

```
In article <e66a875b.0403250752.37a3d1e8@posting.google.com>,
sb <orzo617@hotmail.com> wrote:
>docdwarf@panix.com wrote in message news:<c3smoe$9p4$1@panix5.panix.com>...
>> In article <e66a875b.0403241106.7707796c@posting.google.com>,
…[18 more quoted lines elided]…
>Come again??  Did I miss a beat?  There is no outsourcing of any kind.

That's nice to hear.

> I happen to work for a firm that has cobol modules.  I need to deploy
>them on our website.  I don't have COBOL experience so I thought I
>would solicit advice here (period)

You might want to solicit the person who assigned you this task for the 
reasons that it was given to someone with 'NO/VERY little knowledge' (caps 
original) of the matter being worked with.

DD
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 6)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-03-25T17:00:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3v38201bsm@enews2.newsguy.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <c3mv4801opb@enews1.newsguy.com> <e66a875b.0403221232.689eb0a6@posting.google.com> <c3q3fm01s0m@enews4.newsguy.com> <e66a875b.0403241106.7707796c@posting.google.com>`

```

In article <e66a875b.0403241106.7707796c@posting.google.com>, orzo617@hotmail.com (sb) writes:
> mwojcik@newsguy.com (Michael Wojcik) wrote in message news:<c3q3fm01s0m@enews4.newsguy.com>...
> > In article <e66a875b.0403221232.689eb0a6@posting.google.com>, orzo617@hotmail.com (sb) writes:
…[16 more quoted lines elided]…
> using segmentation.  But code does have non-zero segment numbers. 

No, it doesn't, based on the information you provide below:

> That is, there are statements in the program that read "exit section" 

Those are "exit section" statements.  They're not section numbers.
They're not related to section numbers.  (They're obviously not
numbers, so why would you think they were section numbers?)

> Clearly, there no number acter the SECTION clause.

Then you don't have non-zero section numbers, and you don't have
segmentation, so you can ignore everything you've been told about
segmentation and the NOSEG compiler directive.  It has no bearing
on the problem whatsoever.

> And the code also has statements that read "2000-save-rating section."

That's a section header.  The "2000-save-rating" is a label.

> Again no number
> after the SECTION clause.  Is this what you mean by segmentation?

No, I meant segmentation, which is a feature of COBOL syntax.

> I also see embedded SQL SECTION clause like "EXEC SQL BEGIN DECLARE
> SECTION END-EXEC"

That's not a "section" in the COBOL sense of the term.

Look.  You're not going to get very far with this without some
understanding of COBOL syntax, because the suggestions you're
getting from people refer to COBOL syntax.  Posting queries to
comp.lang.cobol is not going to be very productive if you don't
know anything about COBOL.  This is a forum for people who have
some degree of specialized knowledge to discuss topics in that
arena.

> I have asked the Micro Focus person who suggested I
> remove REENTRANT(2) directive to explain what he means,

That would be a good idea.

However, as I noted before: your COBOL program *will not work in a
multithreaded environment* without one of REENTRANT(1), REENTRANT(2),
or SERIAL.  Will.  Not.  Work.
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2004-03-22T23:14:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0403222314.3f3294dc@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <c3mv4801opb@enews1.newsguy.com>`

```
mwojcik@newsguy.com (Michael Wojcik) wrote in message news:<c3mv4801opb@enews1.newsguy.com>...
> In article <b3638c46.0403210635.59a62084@posting.google.com>, dashwood@enternet.co.nz (Peter E. C. Dashwood) writes:
> > orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403201400.5c5ee637@posting.google.com>...
…[5 more quoted lines elided]…
> involved - all the application code is in DLLs.)

Hmmm...that's interesting, Michael. I have CGI code that also invokes
COM+ components. DLLHost hosts the process but it is NOT ISAPI. I
would need to convert my CGI apps to ISAPI if I wanted to use ISAPI.

Maybe it runs in ISAPI as a single thread and I am just not aware of
it. Are you sure that DLLHost ONLY runs as a multithreaded ISAPI app.?


> 
> Offhand, I'd suggest checking the reentrancy model the COBOL code was
…[13 more quoted lines elided]…
> 

This sounds like the right stuff. 


> SERIAL allows only one thread to be in the module at a time; the
> compiler inserts a mutex around the entire module.
…[3 more quoted lines elided]…
>

Yes, that's what I would have expected.
 
> This seems like a question that's best answered by the Net Express
> documentation, in fact.  There's a whole chapter on writing ISAPI
> modules, and IIRC a tutorial on it as well.

But maybe he's posting here because he just doesn't have time to do a
crash course in MF ISAPI...?

It looks like RENTRANT(2) could be a good option.

Pete.
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 4)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-03-23T19:21:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c3q2nt015ij@enews1.newsguy.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <c3mv4801opb@enews1.newsguy.com> <b3638c46.0403222314.3f3294dc@posting.google.com>`

```

In article <b3638c46.0403222314.3f3294dc@posting.google.com>, dashwood@enternet.co.nz (Peter E. C. Dashwood) writes:
> mwojcik@newsguy.com (Michael Wojcik) wrote in message news:<c3mv4801opb@enews1.newsguy.com>...
> > In article <b3638c46.0403210635.59a62084@posting.google.com>, dashwood@enternet.co.nz (Peter E. C. Dashwood) writes:
…[10 more quoted lines elided]…
> would need to convert my CGI apps to ISAPI if I wanted to use ISAPI.

Hmm.  I think I just wasn't sufficiently specific, but it's possible
I'm unaware of some additional weird pseudo-CGI facility IIS supports.

CGI is a facility for an HTTP server to run an external program to
process an HTTP request and generate the response (more or less -
except for NPH mode, the CGI program actually generates the HTTP
content-body and some of the HTTP headers, but not the entire
response).  CGI/1.1 (which is just a draft anyway; there is no
CGI specification, technically speaking) does allow the CGI "script"
to be within the server process rather than external, but I wasn't
aware that IIS supported that.  I just checked the MSDN Library I
have installed and it claims that IIS-hosted CGI scripts are in
fact separate programs (but it's somewhat out of date because I
haven't been able to move to VS.NET yet, and newer versions of the
Library aren't compatible with earlier versions of VS).

So for the moment I'm assuming that IIS only supports CGI scripts
that are in fact external programs.

Given that, if the OP's *entire* application is a DLL running under
DLLHost, it must not be CGI.  For CGI, they'd need *some* executable
piece that was executed by IIS for each request.

Now, it's certainly possible to have CGI scripts that invoke COM+
components, and those components may very well run under DLLHost.exe
(the system surrogate process for in-process COM components).  But
I don't believe DLLHost.exe can itself serve as a CGI script; for
that to work, DLLHost.exe would need to support the CGI interface,
which is orthogonal to its actual job of hosting COM+ components.

Of course, as I said, I could be unaware of new IIS features for
supporting the CGI interface to "scripts" that aren't separate
executables.
```

##### ↳ ↳ Re: Deploying over IIS and VB

- **From:** orzo617@hotmail.com (sb)
- **Date:** 2004-03-24T11:09:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e66a875b.0403241109.17adf59b@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com>`

```
dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote in message news:<b3638c46.0403210635.59a62084@posting.google.com>...
> orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403201400.5c5ee637@posting.google.com>...
> > Hello,
…[89 more quoted lines elided]…
> > SB


Pete,

Thank you for you suggestions with this matter.  I realize now I may
have to go the OO Cobol route.  But still need to find out how to
pre-compile OO Cobol with Oracle Precompiler.

Saurabh.
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

- **From:** chris.glazier@microfocus.com (Chris Glazier)
- **Date:** 2004-03-29T10:43:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<260cd566.0403291043.78724c70@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <e66a875b.0403241109.17adf59b@posting.google.com>`

```
orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403241109.17adf59b@posting.google.com>...
> dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote in message news:<b3638c46.0403210635.59a62084@posting.google.com>...
> > orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403201400.5c5ee637@posting.google.com>...
…[99 more quoted lines elided]…
> Saurabh.

Just a few more tidbits of information regarding the problem that you
are experiencing.

One thing that you don't really mention is, at what point during the
execution of your application is the error message being displayed? Is
it when the VB .DLL is being called or when the COBOL .DLL is being
called, or some other point altogether?

If you wait for the first request to complete and then wait a few
seconds before issuing another request does it work correctly?

Your .DLL needs to be compiled with REENTRANT"2" and needs to be
linked with the multi-threaded / dynamic shared run-time system.

If you specify REENTRANT"1", then you need to add thread
synchronization code to your program in order to resolve data
contention between multiple threads. This involves a lot of work in
most cases.

Since this .DLL is not actually an ISAPI application itself but is
instead called by one then it should not be compiled with the
WEBSERVER"ISAPI" directive on. This directive can only be used for a
main COBOL .DLL which is being loaded directly by IIS.

If you are using embedded SQL statements in your program, then it must
also have the correct SQL directives turned on for compilation. If you
are using Oracle then it can either be setup to use the COBSQL
precompiler, which actually passes control to the Oracle precompiler,
or it can be setup to use OpenESQL which is the Net Express
preprocessor for generating SQL programs to be used with an ODBC
driver.

The COBSQL preprocessor for Oracle will only work with procedural
COBOL code. It will not work if the embedded SQL statements are
present within an OO COBOL program or within a nested program. In this
case the OpenESQL preprocessor must be used.

The alternative to this would be to use the Net Express OO Class
Wizard to generate a wrapper for a COBOL COM object which could then
be instantiated by the VB COM object. The COBOL COM Object could then
make calls to the procedural COBOL programs containing the embedded
SQL statements.

If you are using OpenESQL then you would also need to set the SQL
directive for THREAD=ISOLATE in order for an SQL COBOL program to be
thread-safe at run-time.
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 4)_

- **From:** orzo617@hotmail.com (sb)
- **Date:** 2004-03-30T09:41:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e66a875b.0403300941.1a15b541@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <e66a875b.0403241109.17adf59b@posting.google.com> <260cd566.0403291043.78724c70@posting.google.com>`

```
chris.glazier@microfocus.com (Chris Glazier) wrote in message news:<260cd566.0403291043.78724c70@posting.google.com>...
> orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403241109.17adf59b@posting.google.com>...
> > dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote in message news:<b3638c46.0403210635.59a62084@posting.google.com>...
…[109 more quoted lines elided]…
> 
I believe the error happens at the Cobol.dll.
> If you wait for the first request to complete and then wait a few
> seconds before issuing another request does it work correctly?
Yes, I believe the error happens at the COBOL.dll level because if I
issue one request, then wait for the first reqest to finish before
issuing the second request, everything works fine.
> Your .DLL needs to be compiled with REENTRANT"2" and needs to be
> linked with the multi-threaded / dynamic shared run-time system.
I have added the REENTRANT"2" directive but with no success.  This
main Cobol.dll calls other cobol.dlls to do the work.  I read
somewhere that "if you call a COBOL routine more than once, the
Working-Storage Section data remains unchanged between call unless you
have canceled the program." (Micro Focus Document: "Web-Enabling COBOL
Applications with Net Express"; Page 4).  So I issued an explicit
"cancel <program name>" after every call to sub cobol.dlls.  This
still did not solve the problem.  Yes, the main Cobol.dll and sub
cobol.dlls are all compiled as shared and multi-threaded.  Dynamic
binding box is NOT checked.
> If you specify REENTRANT"1", then you need to add thread
> synchronization code to your program in order to resolve data
…[6 more quoted lines elided]…
> main COBOL .DLL which is being loaded directly by IIS.
Yes since this not an ISAPI application (i.e. it does not run under
IIS Context) I do not use this directive.
> If you are using embedded SQL statements in your program, then it must
> also have the correct SQL directives turned on for compilation. If you
…[4 more quoted lines elided]…
> driver.
I belive that the Cobol.dll compiles fine as the Oracle Precompiler
does not complain.
> 
> The COBSQL preprocessor for Oracle will only work with procedural
> COBOL code. It will not work if the embedded SQL statements are
> present within an OO COBOL program or within a nested program. In this
> case the OpenESQL preprocessor must be used.
Thank you I did not know this -- valuable information.

> The alternative to this would be to use the Net Express OO Class
> Wizard to generate a wrapper for a COBOL COM object which could then
> be instantiated by the VB COM object. The COBOL COM Object could then
> make calls to the procedural COBOL programs containing the embedded
> SQL statements.
I lost you here.  If i wrap the conventional procedural COBOL program
containing embedded SQL Stmts, can I use the Oracle Precompiler.  If I
convert these DLL to COM objects then I can bypass VB.dll altogether
and create an instance of COBOL.Dll from vbscript/ASP.  But somewhere
I read that $set ooctrl(+p) directive for object cobol restricts the
number of parameters that can be passed in a function to 34.  Is this
correct.  If so I would have another potential problem.
> If you are using OpenESQL then you would also need to set the SQL
> directive for THREAD=ISOLATE in order for an SQL COBOL program to be
> thread-safe at run-time.

Thanks
SB
```

###### ↳ ↳ ↳ Re: Deploying over IIS and VB

_(reply depth: 5)_

- **From:** chris.glazier@microfocus.com (Chris Glazier)
- **Date:** 2004-04-01T06:07:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<260cd566.0404010607.d86eb24@posting.google.com>`
- **References:** `<e66a875b.0403201400.5c5ee637@posting.google.com> <b3638c46.0403210635.59a62084@posting.google.com> <e66a875b.0403241109.17adf59b@posting.google.com> <260cd566.0403291043.78724c70@posting.google.com> <e66a875b.0403300941.1a15b541@posting.google.com>`

```
orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403300941.1a15b541@posting.google.com>...
> chris.glazier@microfocus.com (Chris Glazier) wrote in message news:<260cd566.0403291043.78724c70@posting.google.com>...
> > orzo617@hotmail.com (sb) wrote in message news:<e66a875b.0403241109.17adf59b@posting.google.com>...
…[173 more quoted lines elided]…
> SB

Just to close out this thread, the problem was occuring because the
other .DLLS that were being called by the main COBOL .DLL were NOT
compiled with the REENTRANT"2" directive.

When creating a multi-threaded Net Express COBOL application, then ALL
of the programs within the application need to be compiled with one of
the multi-threaded directives, "SERIAL", REENTRANT"1" or REENTRANT"2".

It is not enough just to link these programs with the multi-threaded
run-time system.

There were also a few matters of CALL-CONVENTION from VB to COBOL and
some .ASP/IIS settings that had to be changed since this application
was not running under COM+, but instead it was handling database
transactions through COMMIT/ROLLBACK statements within the COBOL
programs.

It seems to working fine now...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
