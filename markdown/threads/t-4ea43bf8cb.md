[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Passing Parameters

_10 messages · 7 participants · 1999-10_

---

### Passing Parameters

- **From:** hank_heng@hotmail.com
- **Date:** 1999-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tmgm5$oah$1@nnrp1.deja.com>`

```
Hi,

  I am very new in Cobol language, hope that what I ask will not make
you laugh.. :)

  Anyway, can a variable being passing back to the caller?

  e.g :

  I have p1.cbl and p2.cbl.

  p1.cbl CALL p2.cbl and pass a variable to p2.cbl.

  So, can p2.cbl pass back a variable or change the contain of a
variable that being decalre in p1.cbl ?

  It is like return a value back to the caller program, how is it
posible ?

  Thanks for reading this, please help me out.

Hank


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Passing Parameters

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tml0c$j0g$1@nntp9.atl.mindspring.net>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com>`

```
There are two ways to pass a value "back" from a called subprogram to the
calling program.

Method 1 (and this is the MOST portable and will work with ALL COBOL
compilers)

1) Define a field in the Working-Storage of the CALLING program and then pass
it (BY REFERENCE - which is the default) to the CALLED subprogram.

2) Subprogram defines the field in its LINKAGE SECTION - and updates it - and
then returns  control to the CALLING program (via EXIT PROGRAM - or GoBack -
if your compiler has this - not all do)

3) The value that was updated in the called subprogram now is in the
Working-Storage field of the CALLING program.

    ***

Method 2 (not currently portable - but many compilers do support it)

Check to see if your compiler supports the RETURNING phrase on
  - the CALL statement, or
 - the Exit Program (or GoBack) statement, or
 - the Procedure Division header.

Depending upon which (if any) of these are supported by your compiler, you
can use this phrase to "pass bacK" a value (often restricted to a numeric
value) to the CALLING program from the CALLED subprogram.
```

##### ↳ ↳ Re: Passing Parameters

- **From:** frederico_fonseca@eudoramail.com (Frederico Fonseca)
- **Date:** 1999-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38002abf.1022152@news.indigo.ie>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com> <7tml0c$j0g$1@nntp9.atl.mindspring.net>`

```
Third method, portable depending on the COBOL version
used.

Define a variable in working (even file section)
of both programs with the same name and PIC as EXTERNAL.

ex: 01  W01-VALUE     PIC 9(8) EXTERNAL.

This way the variable contents is available for all 
programs that define this variable the same way.

FF


On Sat, 9 Oct 1999 00:48:18 -0500, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>There are two ways to pass a value "back" from a called subprogram to the
>calling program.
…[25 more quoted lines elided]…
>value) to the CALLING program from the CALLED subprogram.
```

###### ↳ ↳ ↳ Re: Passing Parameters

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37FFF0DE.6A210B40@zip.com.au>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com> <7tml0c$j0g$1@nntp9.atl.mindspring.net> <38002abf.1022152@news.indigo.ie>`

```
Frederico Fonseca wrote:
> 
> Third method, portable depending on the COBOL version
…[10 more quoted lines elided]…
> FF

Please do not recommend this practice.  It creates a maintenance
nightmare.  I have coded like this in C and it has always caused more
problems than it solves.

rule 1:
This should only be used where efficiency comes into play.

rule 2:
Efficiency comes into play extremely rarely.  Passing a single pointer
around does not cost much and it makes the interface more explicit.


The easiest way to reuse code is to program to an interface.
Ken
```

###### ↳ ↳ ↳ Re: Passing Parameters

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tp4hg$fph$1@nntp3.atl.mindspring.net>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com> <7tml0c$j0g$1@nntp9.atl.mindspring.net> <38002abf.1022152@news.indigo.ie> <37FFF0DE.6A210B40@zip.com.au>`

```
We have had previous discussions in comp.lang.cobol about whether using the
EXTERNAL attribute for "passing" parameters is good, bad, easy-to-maintain,
hard-to-maintain, error-prone, or whatever.  There is no UNIVERSAL consensus
on this - but what Ken says is certainly a very common view.

The one exception that I would make is that it is often QUITE useful to
define a FILE as "EXTERNAL" (in the FD definition).  I really, REALLY, like
being able to OPEN and CLOSE a file in one program - and then "process it"
(READ, WRITE, REWRITE, whatever) in another.  This often fits into my
"modular" application design.

The ONLY way to do this (in a Standard way) is by using the EXTERNAL
attribute (Well, GLOBAL would work - if the other programs were nested - but
that isn't the design that I am thinking about.)

Now, I know that it is possible to use
  A) ENTRY statements (not portable) for OPEN, READ, CLOSE, etc - all in the
same program
  B) A "switch" telling a single program what I/O operation to do.

However, I find that the EXTERNAL approach is SOMETIMES a much better way to
go.

Obviously, this is just a "personal opinion" and your shop (or individual)
standards may prohibit it - but it is at least a good target for EXTERNAL -
where there is no other "good" way to distribute your I/O among separate
programs.
```

###### ↳ ↳ ↳ Re: Passing Parameters

_(reply depth: 5)_

- **From:** "pacman" <mike@thecolberts.freeserve.co.uk>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tpl8c$u2$1@news8.svr.pol.co.uk>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com> <7tml0c$j0g$1@nntp9.atl.mindspring.net> <38002abf.1022152@news.indigo.ie> <37FFF0DE.6A210B40@zip.com.au> <7tp4hg$fph$1@nntp3.atl.mindspring.net>`

```
Another use for external is when creating your own file drivers, (MF)
as the file driver is called during the open,read etc the variables cannot
be passed so the only way of passing variables is by external.
(tell me if i'm wrong)

But apart from these external is like a go to (should never be used apart
from if this is the only option), it can create many problems
which are nearly impossible to solve.





William M. Klein wrote in message <7tp4hg$fph$1@nntp3.atl.mindspring.net>...
>We have had previous discussions in comp.lang.cobol about whether using the
>EXTERNAL attribute for "passing" parameters is good, bad, easy-to-maintain,
>hard-to-maintain, error-prone, or whatever.  There is no UNIVERSAL
consensus
>on this - but what Ken says is certainly a very common view.
>
…[7 more quoted lines elided]…
>attribute (Well, GLOBAL would work - if the other programs were nested -
but
>that isn't the design that I am thinking about.)
>
>Now, I know that it is possible to use
>  A) ENTRY statements (not portable) for OPEN, READ, CLOSE, etc - all in
the
>same program
>  B) A "switch" telling a single program what I/O operation to do.
>
>However, I find that the EXTERNAL approach is SOMETIMES a much better way
to
>go.
>
…[40 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Passing Parameters

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<380008A1.2F42B435@home.com>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com> <7tml0c$j0g$1@nntp9.atl.mindspring.net> <38002abf.1022152@news.indigo.ie> <37FFF0DE.6A210B40@zip.com.au>`

```


Ken Foskey wrote:
> 
> Frederico Fonseca wrote:
…[16 more quoted lines elided]…
> problems than it solves.<snip>

May I offer a suggestion allied to parameter passing for the
'youngsters' to the language; not the old hands who have established
their style. Lay down some ground rules how you pass parameters; in big
shops they may already have documented standards.

I do a lot of parameter passing in OO, reference to other classes and
file DB interfaces. I have a simple rule, (for myself) :-

	first - object references - alphabetized
	text (pic 9s or pic x)    - alphabetized, so :-

Linkage Section.
01 os-ClientsDBI		object reference.
01 os-DateandTime		object reference.
01 os-DescripsDBI		object reference.
01 os-MetricConversion		object reference.
01 os-ParentWindow		object reference.
01 os-ResourceFile		object reference.
01 mynum1			pic 9(04) comp-5
01 mynum2			pic 9(05) comp-5.
01 mytext1			pic x(10).
01 mytext2      		pic x(02).

Procedure Division using (above.....)

(Typically, the above 'handles' could be passed from a selection from
the Main Menu).

It sure saves you a lot of headaches. And in the case of OO, if you try
and access the wrong object, because your sequence is out of kilter -
Woweeee !

OK, if you are doing Windows API calls or other third-party calls, you
have no choice - you have to discipline yourself into their specific
parameter passing sequence.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Passing Parameters

_(reply depth: 5)_

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u04o5$na5$1@neptunium.btinternet.com>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com> <7tml0c$j0g$1@nntp9.atl.mindspring.net> <38002abf.1022152@news.indigo.ie> <37FFF0DE.6A210B40@zip.com.au> <380008A1.2F42B435@home.com>`

```

James J. Gavan wrote in message <380008A1.2F42B435@home.com>...
>
>
…[57 more quoted lines elided]…
>Jimmy, Calgary AB

The only thing I hate about this Jimmy, is that you have to define different
variable names for each class, I hate this.


Simon R Hart
Eaton, Ottery, St. Mary, UK.
```

###### ↳ ↳ ↳ Re: Passing Parameters

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38039C1C.3FEF61BB@home.com>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com> <7tml0c$j0g$1@nntp9.atl.mindspring.net> <38002abf.1022152@news.indigo.ie> <37FFF0DE.6A210B40@zip.com.au> <380008A1.2F42B435@home.com> <7u04o5$na5$1@neptunium.btinternet.com>`

```


Simon R Hart wrote:
> 
> James J. Gavan wrote in message <380008A1.2F42B435@home.com>...
…[11 more quoted lines elided]…
> >

Watch it Simon - they'll think this is turning into a love-fest between
you and me <G>.

True, I am 'spelling them out' - but it is unambiguous and perhaps the
most important point about parameter passing. As an alternative you can
use things like anObject - but I hate it, OK when it's localized,
(Local-Storage Section) but from a Working/Object-Storage Section - I
find that as confusing as hell. Another alternative -

01 Lnk-SetofObjects.
   05 lnk-Object occurs 4	object reference.

and that is making it even more convoluted.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Passing Parameters

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3800108F.4FA387DA@home.com>`
- **References:** `<7tmgm5$oah$1@nnrp1.deja.com> <7tml0c$j0g$1@nntp9.atl.mindspring.net>`

```


"William M. Klein" wrote:
> 
> There are two ways to pass a value "back" from a called subprogram to the
…[27 more quoted lines elided]…
> 

Interesting quote you give Bill - I've been away from structured now for
so long...

Merant OO - Do NOT use p1 as sending and receiving, otherwise you are
going to get indeterminate results, so :-

  Working(Local)-storage seciton.
  01 ws-Primekey.
     05 p-rectype		pic 9(02).
     05 p-key			pic x(04).
  01 ws-values.
     05 ws-result		pic x(4) comp-5.
     05 ws-CustomerName 	pic x(30).    

  invoke MyOtherClass "get-name" using  ws-PrimeKey
		      returning ws-values (or ls-values)

   if ws-result <> zeroes
      .............

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
