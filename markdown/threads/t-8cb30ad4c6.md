[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol's hanging by a thread...

_13 messages · 6 participants · 2004-12_

---

### Cobol's hanging by a thread...

- **From:** KELLIEFITTON@YAHOO.COM
- **Date:** 2004-12-13T11:42:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com>`

```
Hello Everyone,

I need your kind help again -- what is the difference between
a Module, a Thread and a Process when programming for windows?
case in point: if I make a GUI cobol program (Kellie.exe) that
utilizes the use of win32 API functions, Is that a Module,
a Thread or a Process when I execute the program?
thanks for the kind help, Kellie.
```

#### ↳ Re: Cobol's hanging by a thread...

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-12-13T20:53:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<djnvd.503254$%k.344584@pd7tw2no>`
- **In-Reply-To:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com>`

```
KELLIEFITTON@YAHOO.COM wrote:

>Hello Everyone,
>
…[8 more quoted lines elided]…
>
Li'l bit tricky, because folks put different meanings on the words. 
Perhaps once a year I might refer to it - knew it would come in handy 
sometime - so from the Microsoft Press Computer Dictionary :-

 >>MODULE :

A collection of routines and data structures that performs a particular 
task or implements a particular abstract type. Modules usualy consist of 
two parts: an interlace, which lists the constants, data types, 
variables and routines that can be accessed by other modules or 
routines, and an implementation, which is private (accessible only to 
the module) and which contains the source code that actually implements 
the routines in the module........<<

Back when I started designing for mainframes we would talk about the 
'Invoicing System" or 'Sales Ledger System";  I don't recall we ever 
used the words 'application' or 'project'. We also used to refer to it 
as the "Sales Ledger suite of programs", to convey a 'grouping' of 
programs. Now I visualise an application - Accounts Receivable 
Application, with a Master Menu from which the user selects a 'module' 
to execute - say Edit Customers, Print a List etc. Sure enough my 
approach to 'modules' follows the above meaning using a three-tier 
System design approach (1) Business Program (Problem Domain) - which is 
the 'Controller', (2) DBI (Database Interface) be it COBOL files or an 
(R)DBMS and (3) UI = User Interface = GUI

THREAD :

As you aren't clear - it's for sure you are using SINGLE THREAD  :-)

 >> A process that is part of a larger process or program. In a tree 
data structure, a pointer that identifies the particular node and is 
used to facilitate traversal of the tree.....<<

 >> Multi-threading - The running of several processes in rapid sequence 
(multitasking) within a single program. See also 'thread'.....<<

Not too helpful. As background look at the N/E 4.0 on-line books - 
there's one I believe devoted entirely to Threading.

PROCESS ;

 >> A program or a part of a program; a coherent sequence of steps 
undertaken by a program <<

---------------

My own suspicion is that KELLIE.EXE  is *ONE* program ? If so you've 
broken the cardinal rule - look at Module and three-tier systems design 
above.

Have a nice Christmas down there.

Jimmy, Calgfary AB
```

##### ↳ ↳ Re: Cobol's hanging by a thread...

- **From:** KELLIEFITTON@YAHOO.COM
- **Date:** 2004-12-13T13:22:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1102972941.342364.228530@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<djnvd.503254$%k.344584@pd7tw2no>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <djnvd.503254$%k.344584@pd7tw2no>`

```

James J. Gavan wrote:
> KELLIEFITTON@YAHOO.COM wrote:
>
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Cobol's hanging by a thread...

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-12-14T15:12:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cpmvtk$99e$1@peabody.colorado.edu>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <djnvd.503254$%k.344584@pd7tw2no>`

```
We use CoBOL because most of the software we bought was written in CoBOL.   When
this gets replaced, we will primarily use whatever language the software we buy
is written in.

CoBOL's continued success may be decided by companies that sell these packages.
```

###### ↳ ↳ ↳ Re: Cobol's hanging by a thread...

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-12-14T21:48:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3lnur097njpp0mvpf8hia9chh3rniej88p@4ax.com>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <djnvd.503254$%k.344584@pd7tw2no> <cpmvtk$99e$1@peabody.colorado.edu>`

```
On Tue, 14 Dec 2004 15:12:16 GMT, "Howard Brazee" <howard@brazee.net>
wrote:

>We use CoBOL because most of the software we bought was written in CoBOL.   When
>this gets replaced, we will primarily use whatever language the software we buy
>is written in.
>
>CoBOL's continued success may be decided by companies that sell these packages.

Lawson is written in Cobol. Other ERPs drop support if you touch their
source code, so it doesn't matter what they're written in. You're
expected to enhance SAP with ABAP code, PeopleSoft and Oracle with
SQR.
```

###### ↳ ↳ ↳ Re: Cobol's hanging by a thread...

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-12-14T21:59:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cpnnoh$o2o$1@peabody.colorado.edu>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <djnvd.503254$%k.344584@pd7tw2no> <cpmvtk$99e$1@peabody.colorado.edu> <3lnur097njpp0mvpf8hia9chh3rniej88p@4ax.com>`

```

On 14-Dec-2004, Robert Wagner <spamblocker-robert@wagner.net> wrote:

> >We use CoBOL because most of the software we bought was written in CoBOL.
> >When
…[10 more quoted lines elided]…
> SQR.

We won't buy a package that we can't modify and build upon.   I haven't seen
that to be a limitation so far.
```

###### ↳ ↳ ↳ Re: Cobol's hanging by a thread...

_(reply depth: 5)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2004-12-14T17:33:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41BF7849.53FABF8A@mb.sympatico.ca>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <djnvd.503254$%k.344584@pd7tw2no> <cpmvtk$99e$1@peabody.colorado.edu> <3lnur097njpp0mvpf8hia9chh3rniej88p@4ax.com> <cpnnoh$o2o$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
> On 14-Dec-2004, Robert Wagner <spamblocker-robert@wagner.net> wrote:
…[9 more quoted lines elided]…
> that to be a limitation so far.

When you say "modify", do you mean to change or replace the vendor's
code?  Or to build reports etc. that the package doesn't provide?  

If you can "replace" a function or report by making the program loader
find your version first (i.e., by setting the path to look in your
homegrown directory first) then it's probably OK to do so; but if you
modify the vendor's code I'd say the vendor is justified in refusing to
support you - as Howard Brazee points out.

PL
```

###### ↳ ↳ ↳ Re: Cobol's hanging by a thread...

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-12-15T14:57:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cppjde$5a2$1@peabody.colorado.edu>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <djnvd.503254$%k.344584@pd7tw2no> <cpmvtk$99e$1@peabody.colorado.edu> <3lnur097njpp0mvpf8hia9chh3rniej88p@4ax.com> <cpnnoh$o2o$1@peabody.colorado.edu> <41BF7849.53FABF8A@mb.sympatico.ca>`

```

On 14-Dec-2004, Peter Lacey <lacey@mb.sympatico.ca> wrote:

> > We won't buy a package that we can't modify and build upon.   I haven't seen
> > that to be a limitation so far.
>
> When you say "modify", do you mean to change or replace the vendor's
> code?

Yes.   Of course, what we modify won't fit patches they make for the code.   So
sub-systems that get updated a lot to meet federal regulations stay unmodified
by us.

> Or to build reports etc. that the package doesn't provide?

Yes.

> If you can "replace" a function or report by making the program loader
> find your version first (i.e., by setting the path to look in your
> homegrown directory first) then it's probably OK to do so; but if you
> modify the vendor's code I'd say the vendor is justified in refusing to
> support you - as Howard Brazee points out.

Sure.    But when their code doesn't quite do what we want we change it.  
Installing a significant upgrade takes a long time as we modify it to fit our
needs.
```

###### ↳ ↳ ↳ Re: Cobol's hanging by a thread...

_(reply depth: 5)_

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-12-15T02:12:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<imsur09j6c6ll1sdk6i5jj8dgi85cb5ph8@4ax.com>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <djnvd.503254$%k.344584@pd7tw2no> <cpmvtk$99e$1@peabody.colorado.edu> <3lnur097njpp0mvpf8hia9chh3rniej88p@4ax.com> <cpnnoh$o2o$1@peabody.colorado.edu>`

```
On Tue, 14 Dec 2004 21:59:09 GMT, "Howard Brazee" <howard@brazee.net>
wrote:

>
>On 14-Dec-2004, Robert Wagner <spamblocker-robert@wagner.net> wrote:
…[16 more quoted lines elided]…
>that to be a limitation so far.

You will. All mainframe shops had that attitude in the good old days.
I did. The rules have changed.
```

#### ↳ Re: Cobol's hanging by a thread...

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-12-14T10:16:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<326f5tF3ir827U1@individual.net>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com>`

```

<KELLIEFITTON@YAHOO.COM> wrote in message
news:1102966934.640140.134700@c13g2000cwb.googlegroups.com...
> Hello Everyone,
>
…[7 more quoted lines elided]…
>
Kellie, your .exe is a PROCESS. It is a single run unit in COBOL terms and
it will utilize a single THREAD.

If you wrote it as a .DLL that could have various functions loaded by
calling (or invoking, for OO) those would be MODULES.

Easy way to remember:

You run a PROCESS. (which might, though not usually in COBOL, spawn other
process THREADS)

You CALL or INVOKE a MODULE.

HTH,

Pete.
```

##### ↳ ↳ Re: Cobol's hanging by a thread...

- **From:** KELLIEFITTON@YAHOO.COM
- **Date:** 2004-12-13T15:20:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1102980035.380891.49490@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<326f5tF3ir827U1@individual.net>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <326f5tF3ir827U1@individual.net>`

```

Pete Dashwood wrote:
> <KELLIEFITTON@YAHOO.COM> wrote in message
> news:1102966934.640140.134700@c13g2000cwb.googlegroups.com...
> Kellie, your .exe is a PROCESS. It is a single run unit in COBOL
terms and
> it will utilize a single THREAD.
> If you wrote it as a .DLL that could have various functions loaded by
…[3 more quoted lines elided]…
> You run a PROCESS. (which might, though not usually in COBOL, spawn
other
> process THREADS)
>
…[10 more quoted lines elided]…
>
```

#### ↳ Re: Cobol's hanging by a thread...

- **From:** Robert Wagner <spamblocker-robert@wagner.net>
- **Date:** 2004-12-13T21:41:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c2sr0lpm604pcr4cnelu6456c0i5k6lvb@4ax.com>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com>`

```
On 13 Dec 2004 11:42:14 -0800, KELLIEFITTON@YAHOO.COM wrote:

>Hello Everyone,
>
…[5 more quoted lines elided]…
>thanks for the kind help, Kellie.

It's all three. Your one-process program could launch other processes
to run in parallel with it. Each would show up on the Task
List/Processes with a PID (Process ID) assigned to it. Threads are a
similar concept. A one-thread process can launch additional threads to
run in parallel within a single process id. An example would be
background recalc of a spreadsheet. 

If you're just using the Win32 API, you're not using multi-process nor
multi-thread. If you're using COM, there's a chance it is using
multi-threading, but you don't need to worry about it.
```

##### ↳ ↳ Re: Cobol's hanging by a thread...

- **From:** KELLIEFITTON@YAHOO.COM
- **Date:** 2004-12-13T15:22:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1102980164.860439.69660@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<7c2sr0lpm604pcr4cnelu6456c0i5k6lvb@4ax.com>`
- **References:** `<1102966934.640140.134700@c13g2000cwb.googlegroups.com> <7c2sr0lpm604pcr4cnelu6456c0i5k6lvb@4ax.com>`

```
Kellie Wrote:

thanks a lot, robert.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
