[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Evaluate statement in CobolII

_67 messages · 27 participants · 2000-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### Evaluate statement in CobolII

- **From:** "Green" <john@green.com>
- **Date:** 2000-09-10T01:33:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c01abe$552b8dc0$ef7accd1@default>`

```
A small question. Can you use relational operators in an evaluate
statement?

Ex:

Evaluate State and Stateind
  when 'NJ' and >1
    perform 0600-Rtn
End Evaluate

pardon some of the syntax
```

#### ↳ Re: Evaluate statement in CobolII

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2000-09-10T02:19:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-klXdN5HhgKye@tcpserver>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default>`

```
On Sun, 10 Sep 2000 01:33:57, "Green" <john@green.com> wrote:

> A small question. Can you use relational operators in an evaluate
> statement?
…[8 more quoted lines elided]…
> pardon some of the syntax

I'd use this form

Evaluate true
    when (state = "NJ" and Stateind > 1)
        perform yadda-yadda
end-evaluate
```

#### ↳ Re: Evaluate statement in CobolII

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-09-09T21:24:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8perb4$cdf0d$1@ID-39920.news.cis.dfn.de>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default>`

```

Green <john@green.com> wrote in message
news:01c01abe$552b8dc0$ef7accd1@default...
> A small question. Can you use relational operators in an evaluate
> statement?
…[8 more quoted lines elided]…
> pardon some of the syntax

Yes, and no...

You can use relational operators when evaluating a condition:

EVALUATE TRUE
   WHEN STATE = 'NJ' AND STATEIND > 1
       PERFORM 0600-RTN...
END-EVALUATE.

When you are evaluating a field, you cannot use relational operators:

EVALUATE STATE ALSO STATEIND
   WHEN 'NJ' ALSO 1 THRU 99
       PERFORM 0600-RTN...
END-EVALUATE.

Hope this helps...

Dave
```

#### ↳ Re: Evaluate statement in CobolII

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-09T21:38:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pes6f$fq6$1@slb7.atl.mindspring.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default>`

```
Expanding (slightly) upon other replies,  the statement

* Note change from "and" to "also"
 Evaluate State also Stateind
   when 'NJ' also >1
     perform 0600-Rtn
 End Evaluate

is NOT valid in the current ANSI Standard - and is not accepted by MANY COBOL
compilers.  It is, however, supported in the draft of the NEXT COBOL Standard
and at least MERANT - if no one else - already supports it.   As others have
pointed out, you can already (in all '85 Standard compilers) code,

* notice use of " instead of ' - for alphanumeric literal
 Evaluate State also True
   when "NJ" also Stateind >1
     perform 0600-Rtn
 End Evaluate
```

##### ↳ ↳ Re: Evaluate statement in CobolII

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-10T11:15:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pfqgk$4hk$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8pes6f$fq6$1@slb7.atl.mindspring.net>`

```
In article <8pes6f$fq6$1@slb7.atl.mindspring.net>,
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> Expanding (slightly) upon other replies,  the statement
>
…[6 more quoted lines elided]…
> is NOT valid in the current ANSI Standard - and is not accepted by
MANY COBOL
> compilers.  It is, however, supported in the draft of the NEXT COBOL
Standard
> and at least MERANT - if no one else - already supports it.   As
others have
> pointed out, you can already (in all '85 Standard compilers) code,
>
…[5 more quoted lines elided]…
>
Hi Bill:

Why did you suggest using " rather than '?

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-10T13:35:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bb8e27.125711477@207.126.101.100>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8pes6f$fq6$1@slb7.atl.mindspring.net> <8pfqgk$4hk$1@nnrp1.deja.com>`

```
' is an extension " is defined in the '85 (and prior) standards.

On Sun, 10 Sep 2000 11:15:38 GMT, Foodman <foodman123@aol.com> wrote:

>In article <8pes6f$fq6$1@slb7.atl.mindspring.net>,
>  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
…[30 more quoted lines elided]…
>Before you buy.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Evaluate statement in CobolII

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-10T13:34:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bb8d5e.125510736@207.126.101.100>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default>`

```
Yes, but the syntax is just slightly different....

Evaluate State ALSO Stateind
   When "NJ" ALSO 1
        ......
End-Evaluate

On Sun, 10 Sep 2000 01:33:57 GMT, "Green" <john@green.com> wrote:

>A small question. Can you use relational operators in an evaluate
>statement?
…[8 more quoted lines elided]…
>pardon some of the syntax

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Evaluate statement in CobolII

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-10T12:06:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pgf2n$1fn$1@slb1.atl.mindspring.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39bb8d5e.125510736@207.126.101.100>`

```
Thane,
  You example is QUITE different from the original.  The original is asking
for a test of "greater than" 1 - while yours is checking for "equal to" 1.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-09-10T16:09:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SPSu5.176$dU6.65560@nnrp1.sbc.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39bb8d5e.125510736@207.126.101.100> <8pgf2n$1fn$1@slb1.atl.mindspring.net>`

```
How about:

WHEN "NJ" ALSO 1 THRU 999999999


"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:8pgf2n$1fn$1@slb1.atl.mindspring.net...
> Thane,
>   You example is QUITE different from the original.  The original is
asking
> for a test of "greater than" 1 - while yours is checking for "equal
to" 1.
>
> --
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-11T03:51:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39bc56a6.5250645@207.126.101.100>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39bb8d5e.125510736@207.126.101.100> <8pgf2n$1fn$1@slb1.atl.mindspring.net>`

```
You are correct.  My bad.

On Sun, 10 Sep 2000 12:06:17 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>Thane,
>  You example is QUITE different from the original.  The original is asking
…[32 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Evaluate statement in CobolII

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-09-10T19:41:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ph9lr$d7fpm$1@ID-39920.news.cis.dfn.de>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39bb8d5e.125510736@207.126.101.100>`

```

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:39bb8d5e.125510736@207.126.101.100...
> Yes, but the syntax is just slightly different....
>
…[4 more quoted lines elided]…
>
No, no, no.  I think Thane misunderstood the question.  You cannot use the
relational operator as you did in the original example.  Thane's example is
using a straight value...


> On Sun, 10 Sep 2000 01:33:57 GMT, "Green" <john@green.com> wrote:
>
…[14 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Evaluate statement in CobolII

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39BFD224.E6D2274F@boeing.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default>`

```
Green wrote:
> 
> A small question. Can you use relational operators in an evaluate
…[8 more quoted lines elided]…
> 

I have used 

Evaluate State
    when 'NJ'
        if statind > 1
	    perform something
	end-if
    when BETWEEN 'AA' and 'KK'
	perform otherthing
    when other
       perform exception-thing
end-evaluate.

	regards Susan
```

##### ↳ ↳ Re: Evaluate statement in CobolII

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ponlg$eho$1@slb0.atl.mindspring.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com>`

```
I sure have NEVER heard of any implementation supporting a "BETWEEN" option.

Susan (or anyone else) can you tell me which compiler supports this?
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C2B776.6A865092@boeing.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com> <8ponlg$eho$1@slb0.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> I sure have NEVER heard of any implementation supporting a "BETWEEN" option.
…[3 more quoted lines elided]…
> -

my bad!  I have been writing stored procedures (with embedded SQL),
BETWEEN is an SQL statement, I should have coded THRU  (such as 

Evaluate Wages
    when 000 thru 999
	perform no-tax
    when 1000 thru 9999
	perform mid-tax
    when other
	perform big-tax
end-evalute.

regards

	Susan
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FCJw5.524$eo6.33501@dfiatx1-snr1.gtei.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com> <8ponlg$eho$1@slb0.atl.mindspring.net> <39C2B776.6A865092@boeing.com>`

```
Susan Allen <susan.a.allen@boeing.com> wrote in message
news:39C2B776.6A865092@boeing.com...
> "William M. Klein" wrote:
> >
> > I sure have NEVER heard of any implementation supporting a "BETWEEN"
option.
> >
> >
…[4 more quoted lines elided]…
>

BETWEEN is a member of  "phrases which *should* be part of COBOL but
aren't."

Others include, "ALMOST", "[NOT][NEARLY] ENOUGH" and "[PRETTY] CLOSE [TO]."

MCM
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c38496.3013850@207.126.101.100>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com> <8ponlg$eho$1@slb0.atl.mindspring.net> <39C2B776.6A865092@boeing.com> <FCJw5.524$eo6.33501@dfiatx1-snr1.gtei.net>`

```
Suggest it as an addition to a future standard to your J4 rep.

On Sat, 16 Sep 2000 12:23:01 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>Susan Allen <susan.a.allen@boeing.com> wrote in message
>news:39C2B776.6A865092@boeing.com...
…[21 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C63B10.F109EAD2@dced.state.ak.us>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com> <8ponlg$eho$1@slb0.atl.mindspring.net> <39C2B776.6A865092@boeing.com> <FCJw5.524$eo6.33501@dfiatx1-snr1.gtei.net> <39c38496.3013850@207.126.101.100>`

```
But don't forget to distinguish between CLOSE (your verb) and CLOSE (the verb
already in COBOL). Sometimes I think English wasn't the best language on which
to base COBOL.

Thane Hubbell wrote:

> Suggest it as an addition to a future standard to your J4 rep.
>
…[30 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EDwx5.801$D83.54668@nnrp3.sbc.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com> <8ponlg$eho$1@slb0.atl.mindspring.net> <39C2B776.6A865092@boeing.com> <FCJw5.524$eo6.33501@dfiatx1-snr1.gtei.net> <39c38496.3013850@207.126.101.100> <39C63B10.F109EAD2@dced.state.ak.us>`

```

"Calvin Crumrine" <Calvin_Crumrine@dced.state.ak.us> wrote in message
news:39C63B10.F109EAD2@dced.state.ak.us...
> But don't forget to distinguish between CLOSE (your verb) and CLOSE
(the verb
> already in COBOL). Sometimes I think English wasn't the best
language on which
> to base COBOL.

Think there's any market for a Pig Latin COBOL precompiler?

(I already have a routine to translate the Bible into Pig Latin - for
the preacher who has every other translation - and into Morse Code, so
it wouldn't be too much trouble.)
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AE35C955EDB78D8E.99C5BBE8597E9A06.E552B6214ADC0B79@lp.airnews.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com> <8ponlg$eho$1@slb0.atl.mindspring.net> <39C2B776.6A865092@boeing.com> <FCJw5.524$eo6.33501@dfiatx1-snr1.gtei.net>`

```
On Sat, 16 Sep 2000 12:23:01 GMT, "Michael Mattias"
<michael.mattias@gte.net> enlightened us:

>Susan Allen <susan.a.allen@boeing.com> wrote in message
>news:39C2B776.6A865092@boeing.com...
…[20 more quoted lines elided]…
>

And don't forget SHOULD BE

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Never raise your hands to your kids. 
It leaves your groin unprotected.
 

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q2mv0$7d9$1@news.igs.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com> <8ponlg$eho$1@slb0.atl.mindspring.net> <39C2B776.6A865092@boeing.com> <FCJw5.524$eo6.33501@dfiatx1-snr1.gtei.net>`

```
You missed
    INVOKE ONIPOTENT-ROUTINE "WHAT_THE_HELL_IS_WRONG" RETURNING NEW-CODE.

Michael Mattias wrote in message ...
>Susan Allen <susan.a.allen@boeing.com> wrote in message
>news:39C2B776.6A865092@boeing.com...
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** Jeffry Kennedy <jakcert@attglobal.net>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C62E26.D3AF9EBF@attglobal.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <39BFD224.E6D2274F@boeing.com> <8ponlg$eho$1@slb0.atl.mindspring.net> <39C2B776.6A865092@boeing.com> <FCJw5.524$eo6.33501@dfiatx1-snr1.gtei.net>`

```
I'm in need of a "what I really meant" if you can get me one.

PatH

Michael Mattias wrote:

> Susan Allen <susan.a.allen@boeing.com> wrote in message
> news:39C2B776.6A865092@boeing.com...
…[17 more quoted lines elided]…
> MCM
```

#### ↳ Re: Evaluate statement in CobolII

- **From:** "ulisse" <kenob@libero.it>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8prhhs$2j6$1@nslave2.tin.it>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default>`

```
scusate l'intromissione e l'italiano,
avete veramente tempo da perdere nel discutere di niente, perche' non
tornate tutti al buon vecchio cobol elementare????

 if State = "NJ" and Stateneid > 1
    perform 0600-Rtn .

possibile che bisogna sempre reinventare l'acqua calda??

"Green" <john@green.com> ha scritto nel messaggio
news:01c01abe$552b8dc0$ef7accd1@default...
> A small question. Can you use relational operators in an evaluate
> statement?
…[8 more quoted lines elided]…
> pardon some of the syntax
```

##### ↳ ↳ Re: Evaluate statement in CobolII

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pt9pp$om0$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it>`

```
In article <8prhhs$2j6$1@nslave2.tin.it>,
  "ulisse" <kenob@libero.it> wrote:
> scusate l'intromissione e l'italiano,
> avete veramente tempo da perdere nel discutere di niente, perche' non
…[5 more quoted lines elided]…
> possibile che bisogna sempre reinventare l'acqua calda??

Hi:

Although I do not speak Italian, it is evident that
he is asking the same question I would ask:

Who needs EVALUATE?

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** Support@ScreenIO.com (Kevin J. Hansen)
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c24b33.348430196@news>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com>`

```
On Fri, 15 Sep 2000 13:56:21 GMT, Foodman <foodman123@aol.com> wrote:

>Although I do not speak Italian, it is evident that
>he is asking the same question I would ask:
>
>Who needs EVALUATE?

Hi, Tony,

It's true that some of the EVALUATE syntax is confusing, but I think
that EVALUATE is just another step in improving COBOL just as
structured coding was.  Consider this:

EVALUATE TRUE

  WHEN 88-condition-1
    PERFORM condition-1-routine

  WHEN 88-condition-2
    PERFORM condition-2-routine

  WHEN OTHER
    PERFORM condition-not-handled (or error-routine)

END-EVALUATE

Is much easier to follow than:

IF 88-condition-1
  PERFORM condition-1-routine
ELSE
  IF 88-condition-2
    PERFORM condition-2-routine
  ELSE
    PERFORM condition-not-handled (or error-routine)
  END-IF
END-IF

The EVALUATE structure is clear and much easier to maintain, too.  If
it's contained within an inline PERFORM or some other structure, you
don't need to count ELSE and END-IFs when you add a new condition; you
just add another WHEN.

I began using EVALUATE about 4 years ago and I've never looked back...

Regards,
Kevin
Norcom - COBOL Programming Tools
GUI ScreenIO - A Windows UI for COBOL
http://www.screenio.com
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ljsw5.1337$l35.24908@iad-read.news.verio.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com>`

```
In article <8pt9pp$om0$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>In article <8prhhs$2j6$1@nslave2.tin.it>,
>  "ulisse" <kenob@libero.it> wrote:
…[14 more quoted lines elided]…
>Who needs EVALUATE?

Not this again... the same question was asked about second-generation
languages.

DD
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** shine98@my-deja.com
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ptl8d$7qi$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com>`

```
FoodDude my opinion of why to use an evaluate statement is that when
you use end-if's for the block structuring (and you have to sometimes,
if you write in the structured style), the formating gets unwieldy like
this

if cond-a do...
else if cond-b do...
else if cond-c do...
else if cond-d do...
else if cond-e do...
else if cond-f do...
else if cond-g do...
else if cond-h do...
else if cond-i do...
else if cond-j do...
else if cond-k do...
end-if
end-if
end-if
end-if
end-if
end-if
end-if
end-if
end-if
end-if

evaluate condition
  when a do...
  when b do...
  when c do...
  when d do...
  when e do...
  when f do...
  when g do...
  when h do...
  when i do...
  when j do...
  when k do...
End-evaluate

but otherwise, evaluate is no more or less easy to read once you learn
the rules. I go both ways and occaisionally convert eval's to if's when
it makes sense to do so, and vice versa.

have a good one, you deserve it!

~shine




In article <8pt9pp$om0$1@nnrp1.deja.com>,
  Foodman <foodman123@aol.com> wrote:
> In article <8prhhs$2j6$1@nslave2.tin.it>,
>   "ulisse" <kenob@libero.it> wrote:
> > scusate l'intromissione e l'italiano,
> > avete veramente tempo da perdere nel discutere di niente, perche'
non
> > tornate tutti al buon vecchio cobol elementare????
> >
…[18 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-16T00:09:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pudmm$4mv$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <8ptl8d$7qi$1@nnrp1.deja.com>`

```
In article <8ptl8d$7qi$1@nnrp1.deja.com>,
  shine98@my-deja.com wrote:
> FoodDude my opinion of why to use an evaluate statement is that when
> you use end-if's for the block structuring (and you have to sometimes,
> if you write in the structured style), the formating gets unwieldy
like this

Hi:

Thanks for the comment.  As someone else just said, we've been
here before and people get sick of my harping on minimalist ways. . .

However, I avoid using ELSE and NEVER use END-IF and ALWAYS use
punctuation and NEVER use structured methods so my IF
would never look like the example you gave which is admittedly
horrible.

Thanks again

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C31C51.541DF5F6@optonline.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <8ptl8d$7qi$1@nnrp1.deja.com> <8pudmm$4mv$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> In article <8ptl8d$7qi$1@nnrp1.deja.com>,
…[14 more quoted lines elided]…
> horrible.

And you brag about this in public?

LiamD (Assuming he's a troll)
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pvgk5$a1m$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <8ptl8d$7qi$1@nnrp1.deja.com> <8pudmm$4mv$1@nnrp1.deja.com> <39C31C51.541DF5F6@optonline.net>`

```

> And you brag about this in public?

Hi:

See my reply to docdwarf's nasty comment.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6jLw5.1475$l35.33291@iad-read.news.verio.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8pudmm$4mv$1@nnrp1.deja.com> <39C31C51.541DF5F6@optonline.net> <8pvgk5$a1m$1@nnrp1.deja.com>`

```
In article <8pvgk5$a1m$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>
>> And you brag about this in public?
…[3 more quoted lines elided]…
>See my reply to docdwarf's nasty comment.

Nasty?  Mr Dilworth, in your reply you agreed that my memory was accurate.
Odd bit of 'nastiness', that.

DD
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ISSw5.5111$3y3.129307@typhoon.austin.rr.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8pudmm$4mv$1@nnrp1.deja.com> <39C31C51.541DF5F6@optonline.net> <8pvgk5$a1m$1@nnrp1.deja.com> <6jLw5.1475$l35.33291@iad-read.news.verio.net>`

```
hey guys, knock it off, will ya?

NA <docdwarf@clark.net> wrote in message
news:6jLw5.1475$l35.33291@iad-read.news.verio.net...
> In article <8pvgk5$a1m$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com>
wrote:
> >
> >> And you brag about this in public?
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-16T01:32:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<25Aw5.1410$l35.28679@iad-read.news.verio.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8pt9pp$om0$1@nnrp1.deja.com> <8ptl8d$7qi$1@nnrp1.deja.com> <8pudmm$4mv$1@nnrp1.deja.com>`

```
In article <8pudmm$4mv$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>In article <8ptl8d$7qi$1@nnrp1.deja.com>,
>  shine98@my-deja.com wrote:
…[13 more quoted lines elided]…
>horrible.

If my memory, admittedly porous as it is, has it correctly you also never
write code which has to pass a Production Standards review and you've been
doing the Exact Same Thing for the past few decades.

DD
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8pvggj$9qh$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8pt9pp$om0$1@nnrp1.deja.com> <8ptl8d$7qi$1@nnrp1.deja.com> <8pudmm$4mv$1@nnrp1.deja.com> <25Aw5.1410$l35.28679@iad-read.news.verio.net>`

```

>
> If my memory, admittedly porous as it is, has it correctly you also
never
> write code which has to pass a Production Standards review and you've
been
> doing the Exact Same Thing for the past few decades.
>
> DD

Hi:

Since I establish my own standards and work for myself I thankfully
don't have to put up with know-nothings reviewing my work.

I do the Exact Same Thing because it works. My programs are lean,
fast, compact, totally dependable, easy to maintain, highly portable,
self-explanatory requiring no external documentation, easy on the eye,
run under any flavor of Windows and require no support.

Can you say the same things about yours and would you be prepared
to demonstrate your superior methods?

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2hLw5.1473$l35.33278@iad-read.news.verio.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8pudmm$4mv$1@nnrp1.deja.com> <25Aw5.1410$l35.28679@iad-read.news.verio.net> <8pvggj$9qh$1@nnrp1.deja.com>`

```
In article <8pvggj$9qh$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>
>>
…[9 more quoted lines elided]…
>don't have to put up with know-nothings reviewing my work.

Likewise you do not get the benefits of those who know more... but you
*know* that such people cannot exist, correct?

My memory was correct, you do not deal with Production Standards.

>
>I do the Exact Same Thing because it works.

... and, once again, my memory was correct.  Years ago I was taught the
catchphrase of 'Perfection is Stagnation'.

>My programs are lean,
>fast, compact, totally dependable, easy to maintain, highly portable,
>self-explanatory requiring no external documentation, easy on the eye,
>run under any flavor of Windows and require no support.

Oh... I forgot to mention that you're modest, too.

>
>Can you say the same things about yours and would you be prepared
>to demonstrate your superior methods?

Mr Dilworth, what I can say and what I will say are can be entirely 
different things; what I have have you've already verified... that you
never write code which has to pass a Production Standards review and that
you've been doing the same thing for decades.

If you are capable, of course, to point out where I described any methods
I use, let alone ascribed to them the adjective of 'superior', I'll be
happy to consider your offer.  Until then please address what I've
written, not what you wished me to have written.

I *will* write, clearly and unambiguously, that in my knowledge of the
employment situations of COBOL programmers yours is an anomaly.  I, for
one, am wary of applying the opinions of one who inhabits an anomaly to
the situations of those who inhabit the less-anomalous.

DD
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39c384c7.3062625@207.126.101.100>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com>`

```
Ok - I need evaluate.  Because my brain can only nest so far.
Evaluate is ideal for code that used to look like this:

IF X-Function = "A" 
    Perform Function-A
    ELSE 
       If X-Function = "B"
          Perform Function-B
       ELSE
         If X-Function = "C"
            Perform Function-C.

Anywhere I see ELSE immediately followed by IF I consider using an
EVALUATE instead.

EVALUATE X-Function
  When "A"
     PERFORM FUNCTION-A
  When "B"
     PERFORM FUNCTION-B
  WHEN "C"
     PERFORM FUNCTION-C
END-EVALUATE 



On Fri, 15 Sep 2000 13:56:21 GMT, Foodman <foodman123@aol.com> wrote:

>In article <8prhhs$2j6$1@nslave2.tin.it>,
>  "ulisse" <kenob@libero.it> wrote:
…[23 more quoted lines elided]…
>Before you buy.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 4)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q03f6$t6l$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100>`

```
In article <39c384c7.3062625@207.126.101.100>,
  thaneH@softwaresimple.com (Thane Hubbell) wrote:
> Ok - I need evaluate.  Because my brain can only nest so far.
> Evaluate is ideal for code that used to look like this:
…[8 more quoted lines elided]…
>             Perform Function-C.

Hi:

What is so wrong with the following?

IF X-FUNCTION = 'A' PERFORM FUNCTION-A.
IF X-FUNCTION = 'B' PERFORM FUNCTION-B.
IF X-FUNCTION = 'C' PERFORM FUNCTION-C.

I like this because it is neat and columnar. So what if all the IFs
are executed each time through - does it matter on 500mhz PCs? No
ELSE required, no nesting, just simple code. If you had lots of
them it is easy to duplicate them with your editor rather than
typing those nested things. This is highly readable and comprehensible,
too. All upper case, faster to type.

Thanks

Tony Dilworth

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q11go$76p$1@slb6.atl.mindspring.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com>`

```
"Foodman" <foodman123@aol.com> wrote in message news:8q03f6
>
> Hi:
…[6 more quoted lines elided]…
>

There is NOTHING "wrong" with that, but it is FUNCTIONALLY different from an
EVALUATE.  Particularly if there is any chance that the routines FUNCTION-A
or FUNCTION-B *might* (now or in the future) actually CHANGE the value of
X-FUNCTION.

Either the ELSE IF or the EVALUATE statement allows the selected routine to
"modify" the value included in the test.  You example does a NEW check after
the first routine has been performed. (Personally, I prefer the EVALUATE
solution, but at least the ELSE IF solution is logically equivalent to the
original "issue").

FYI, related to the END-xxx functionality, the "classic" case where this adds
SIGNIFICANTLY to the "understandability" of code is something like:

If Field1 = "A"
   If Field-2 = "B"
       Perform A-and-B
   Else
       Perform A-not-B
   end-if
   Perform All-A
 Else
   Perform Not-A
 End-if

Without the "END-IF" construct (which was made part of Standard COBOL 15
years ago), you needed to "nest" a perform where the nested IF is in this
example (again, especially if the routines A-and-B and A-not-B "modify" the
value of Field-1) - or add some additional "switches".
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com>`

```
On Sat, 16 Sep 2000 15:26:45 GMT, Foodman <foodman123@aol.com> wrote:

>In article <39c384c7.3062625@207.126.101.100>,
>  thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[19 more quoted lines elided]…
>
A lot!

 Evaluate TRUE
	WHEN Salary > 1000000 PERFORM Pay-lots-of taxes
	WHEN Salary >  100000 PERFORM Pay-still-lots-of taxes
	WHEN Salary >   10000 PERFORM Pay-taxes
	WHEN OTHER perform PERFORM Pay-no-taxes
 END-EVALUATE

Is different from
IF Salary > 1000000 PERFORM Pay-lots-of taxes.
IF Salary >  100000 PERFORM Pay-still-lots-of taxes
IF Salary >   10000 PERFORM Pay-taxes
PERFORM Pay-no-taxes




     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      Experience is what you get when you were expecting something else.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RMSw5.5107$3y3.129246@typhoon.austin.rr.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com>`

```
> >What is so wrong with the following?
> >
…[17 more quoted lines elided]…
> PERFORM Pay-no-taxes

But Volker, you are changing the rules a bit. The original
had mutually exclusive clauses, so is ok (although most
of the time poor style and inefficient). Another case where
the repeated if-clauses may be needed is if any
of the perform statements change X-FUNCTION.

What is basically wrong is the poor style. Since there is
no ELSE, the reader is forced to go and understand
each (potentially large) PERFORM statement in order
to understand the structure.

Leif
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q29je$7lo$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com> <RMSw5.5107$3y3.129246@typhoon.austin.rr.com>`

```

> > >
> > >IF X-FUNCTION = 'A' PERFORM FUNCTION-A.
> > >IF X-FUNCTION = 'B' PERFORM FUNCTION-B.
> > >IF X-FUNCTION = 'C' PERFORM FUNCTION-C.

> What is basically wrong is the poor style. Since there is
> no ELSE, the reader is forced to go and understand
…[3 more quoted lines elided]…
> Leif

Hi:

Not in this trivial case. Actually, it is much easier to read
because of its columnar arrangement. You can eyball the variables and
the perform-name in a flash. Putting in ELSE only clutters it up.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ba5x5.5666$WK6.54134@typhoon.austin.rr.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com> <RMSw5.5107$3y3.129246@typhoon.austin.rr.com> <8q29je$7lo$1@nnrp1.deja.com>`

```

Foodman <foodman123@aol.com> wrote in message
news:8q29je$7lo$1@nnrp1.deja.com...
>
> > > >
…[13 more quoted lines elided]…
> Not in this trivial case.

====> that is exactly the point. YOU know it is a trivial case and that
there is no new assigments to X-FUNCTION. But your reader of the
program does NOT know that. You can TELL him that with an ELSE.
If you are so much in love with your format you can have it both ways
by replacing the dot at the end of the line (except the last one) with
an ELSE. Then everybody is happy.



>Actually, it is much easier to read
> because of its columnar arrangement. You can eyball the variables and
…[8 more quoted lines elided]…
> Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 8)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C63DC3.16E8B328@dced.state.ak.us>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com> <RMSw5.5107$3y3.129246@typhoon.austin.rr.com> <8q29je$7lo$1@nnrp1.deja.com>`

```
Foodman wrote:

> > > >
> > > >IF X-FUNCTION = 'A' PERFORM FUNCTION-A.
…[18 more quoted lines elided]…
> Tony Dilworth

I'll agree about ELSE cluttering it up, but note that the example is
limited to 3 comparisons for brevity. In some of our programs, which run
on a PC by the way, we EVALUATE a 4-digit numeric code. Currently it only
has about 200 possible values, but we keep adding more. I've never
compared the performance but I believe the difference would be
noticeable, if not now then eventually. For performance it should either
be IF...ELSE (nested) or EVALUATE. For clarity, between those two I'll
take EVALUATE.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2000-09-19T08:39:01+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C71815.F32B0442@Azonic.co.nz>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com> <RMSw5.5107$3y3.129246@typhoon.austin.rr.com> <8q29je$7lo$1@nnrp1.deja.com>`

```
Foodman wrote:
> 
> > > >
…[7 more quoted lines elided]…
> > to understand the structure.

 
> Not in this trivial case. Actually, it is much easier to read
> because of its columnar arrangement. 

What is 'much easier to read' is entirely dependent on what one is used
to.  Those used to a columnar style with full stops everywhere will find
that style easier, others will find different styles easier.  Because,
it seems, that you only know one style you will probably get very
confused by what others find easy.

> You can eyball the variables and
> the perform-name in a flash. Putting in ELSE only clutters it up.

This is also true of EVALUATE, though you may not think so because you
are not used to it.  The same is also true of _my_ code to me.  You need
to get a wider experience before you could possibly comment on how
others see code.

What is fundementally different between your code and an IF ... ELSE or
EVALUATE is that there is no guarantee in your code that only one
PERFORM is done.  Function-A may change the value of X-Function to 'B'
or 'C' either intentionally or accidentally.  There is no indication in
your code that this is the case.

In other words your code is not as clear as you think it is, and it
would require a search of the whole program to determine what actually
happens.

No wonder you have to spend an hour getting rid of 76 bugs  ;-)
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r6hbss0p31rpc38ei3fdonbi0k6prdvv1t@4ax.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com> <RMSw5.5107$3y3.129246@typhoon.austin.rr.com>`

```
On Sat, 16 Sep 2000 22:48:17 GMT, "Leif Svalgaard" <leif@leif.org> wrote:

>But Volker, you are changing the rules a bit. The original
>had mutually exclusive clauses, so is ok (although most
>of the time poor style and inefficient). Another case where
>the repeated if-clauses may be needed is if any
>of the perform statements change X-FUNCTION.


Yes, I did (guilty as charged).  Mr. Dilworths example implied equivalence of two
structures, which were only equivalent in a simplistic case, not in general.

Also, of course, this is not even true

look at this

   IF X-function = 'A' THEN PERFFORM Run-a.
   IF X-function = 'B' THEN PERFFORM Run-b.
   IF X-function = 'C' THEN PERFFORM Run-c.
...

Run-a.
   PERFORM some-thing
   MOVE 'B' TO X-function 
   .


Then even this simplistic examples fails the equivalence test

   




     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      Reality is for those who can't face Science Fiction.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OVSw5.150$Y24.84033@nnrp1.sbc.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com>`

```
Good catch.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q28v2$725$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <vic7ssk3tfklu81groj1g4hn279iia8ccg@4ax.com>`

```

> >> Ok - I need evaluate.  Because my brain can only nest so far.
> >> Evaluate is ideal for code that used to look like this:
…[25 more quoted lines elided]…
>  END-EVALUATE


Hi Volker:

But, your's is not to mine as mine was to Thane's.

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<483F34D8FB541460.E127F5D8724BF4A1.A1D3AA024B6E0C98@lp.airnews.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com>`

```
On Sat, 16 Sep 2000 15:26:45 GMT, Foodman <foodman123@aol.com>
enlightened us:

>In article <39c384c7.3062625@207.126.101.100>,
>  thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[19 more quoted lines elided]…
>

What's wrong with it is it is inefficient.  You are forcing the
computer to make 3 comparisons when it doesn't really have to.  In
Thane's example as soon as an IF is true, none of the other
comparisons are necessary and are therefore bypassed.  In your example
that doesn't happen.

Now this might amount to a few nano seconds of computer time, but if a
large program is written in this manner, those nano seconds can add up
and if whole systems are written this way, then they can really add up
to increased, unnecessary run time.

And even if it just a small program, there is no need to compromise
efficiency.  Just because CPUs are much faster doesn't mean
programmers should scrap writing efficient code.


>I like this because it is neat and columnar. So what if all the IFs
>are executed each time through - does it matter on 500mhz PCs? No
…[15 more quoted lines elided]…
>Before you buy.

Regards,


          ////
         (o o)
-oOO--(_)--OOo-

Never raise your hands to your kids. 
It leaves your groin unprotected.
 

Boycott Mitsubishi Industries
For more info, please see:  
http://www.ran.org/ran/ran_campaigns/mitsubishi/background.html

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q29ar$7cd$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <483F34D8FB541460.E127F5D8724BF4A1.A1D3AA024B6E0C98@lp.airnews.net>`

```


> And even if it just a small program, there is no need to compromise
> efficiency.  Just because CPUs are much faster doesn't mean
> programmers should scrap writing efficient code.


Hi:

The biggest single cost in application development is people time.
Computer-time is totally irrelevant in the majority of cases.

To reduce the cost of development, simplify the process.

To simplify the process, reduce the number of tools.

See thread 'Only for COBOL newbies' for a perfect example.

Thanks

TOny Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-09-17T00:15:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000916201552.29365.00000940@nso-ba.aol.com>`
- **References:** `<483F34D8FB541460.E127F5D8724BF4A1.A1D3AA024B6E0C98@lp.airnews.net>`

```
In article <483F34D8FB541460.E127F5D8724BF4A1.A1D3AA024B6E0C98@lp.airnews.net>,
SkippyPB <swiegand@neo.rr.com.nospam> writes:

>And even if it just a small program, there is no need to compromise
>efficiency.  Just because CPUs are much faster doesn't mean
>programmers should scrap writing efficient code.
>


This smacks of the voice of a long term mainframer.  :-)
I continually get the opposite reaction from co-workers who develop
for the PC.  They don't seem terribly concerned about performance.
Any short comings in performance will be overcome in future processor
upgrades that will out-strip the current CPU speeds.

I personally agree that code should be developed to be as efficient
as possible the first time around.  As I have found that there is seldom
ever any time to 'come back later' and 'clean it up'.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C64DC7.87DCB924@brazee.net>`
- **References:** `<483F34D8FB541460.E127F5D8724BF4A1.A1D3AA024B6E0C98@lp.airnews.net> <20000916201552.29365.00000940@nso-ba.aol.com>`

```


Sff5ky wrote:

> >And even if it just a small program, there is no need to compromise
> >efficiency.  Just because CPUs are much faster doesn't mean
…[11 more quoted lines elided]…
> ever any time to 'come back later' and 'clean it up'.

I am a long term mainframer who believes the design should be efficient - with
modifications to make maintenance easier and better.  Know which efficiencies are
important, and above all understand your data structure - then compromise on the
little stuff to increase clarity and to allow a new programmer to make changes
without screwing up your efficient but obscure code.

The whole idea of structured code is based upon the fact that maintenance now costs
more than CPU time!
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C64C21.190E9728@brazee.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <483F34D8FB541460.E127F5D8724BF4A1.A1D3AA024B6E0C98@lp.airnews.net>`

```

SkippyPB wrote:

> >What is so wrong with the following?
> >
…[6 more quoted lines elided]…
> computer to make 3 comparisons when it doesn't really have to.

I am willing to spend that very small amount of time for clarity.  But I am
not willing to pay it for an increased likelihood of error (when FUNCTION-B
changes X-FUNCTION).
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C3E02B.8285EE04@zip.com.au>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com>`

```
Foodman wrote:

> In article <39c384c7.3062625@207.126.101.100>,
>   thaneH@softwaresimple.com (Thane Hubbell) wrote:
…[26 more quoted lines elided]…
>

You have shown the new rules of computing, inefficient computing now flies
due to hardware advances.  First work on clarity rather than efficiency.
If this is a one off there is no major problem but if it is called in a
tight loop then the following will out perform your code:

Evaluate X-function
    when 'a'
            perform function-a
    when 'b'
            perform funciton-b
    when 'c'
            perform function-c
   when other
            perform default-function
end-evaluate.

Of course if I was using OO then I could eliminate the evaluate statement
entirely because the object knows which one it wants and does not directly
rely on data.

   invoke  my-function from my-object.

One line instead of three, no growing list of functions repeated in many
places.

Mr Dilworth I still believe that dinosaurs exist in this world,   what you
consider maintain able is trash to another person.  Because you are
familiar with every nook and cranny it gives the single developer the
perception of efficiency and clarity.   Get someone new to look at your
code and then see how it really fairs,  this is the world the rest of us
work in.  Personally I cannot work without inspections,  they give me a
deeper understanding of the problems others have with my code.

What about the user interface, do you make the same pronouncements about
it,  or do you listen to your customers.  In programming our customers are
the next programmer to work with us or following us.

I appreciate the reminder of the 1960's view of programming,  please
continue to give us this walk down memory lane,

Now that's rude I thought DD was uncharacteristically polite!

Ken
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q28r8$71i$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au>`

```

> >
>
> You have shown the new rules of computing, inefficient computing now
flies
> due to hardware advances.  First work on clarity rather than
efficiency.


Hi Ken:

I really don't see a problem with what I presented.  As I mentioned
elsewhere, my concern is speed of development - who cares about
efficiency when PCs are so ridiculously fast.  I would rather save
coding-time than execution-time which is invisible anyway. Wouldn't
a designer KNOW whether he was going to have execution-time problems
BEFORE the program was written and take appropriate action?

If what I wrote is not utterly clear, then I don't know what to say.


>
> What about the user interface, do you make the same pronouncements
about
> it,  or do you listen to your customers

Of course I listen to my customers. However, I do not let my
customers dictate HOW things are implemented. They tell me what
they want and I decide how it will look and work.  As you may recall
I have vertical-market POS software for the food-service industry.
My customers are restaurant owners and the like. If I just did
what they thought was needed it would be a horrible mess.

In the olden days, when I was a MIS director, I used to see
horrible things which had, in effect, been designed by the end-user.
The problem with letting the user get too involved in the design
is that they do not understand the constraints of the hardware and
software.  The user has to state his requirement in business terms,
the designer then creates something to meet his requirement and
asks for the user's blessing.

So far as the user interface is concerned, I do not use the
conventional Windows approach of buttons and drop-down thingies, etc.
which assume the use of the mouse.  All my programs are keyboard-
oriented and easier and faster to use than they would otherwise be.
They are, therefore, supremely efficient.

> I appreciate the reminder of the 1960's view of programming,  please
> continue to give us this walk down memory lane,

I like being a dinosaur.

Earlier this year, I rated myself at 76 debugged lines of code per hour.
The reason I can achieve such a rate is because of my minimalist
approach. To me the most time-consuming aspect of programming is the
time it takes to type the program.  The simpler the code, the faster
it is to write.  The fewer tools one uses, the faster one goes. See
the Only for COBOL newbies thread. . . (Let's not get into a LOC
harangue, LOC obviously changes from application to application. In
the application I timed myself on it came to 76.)

How many debugged lines per hour can you achieve using your more
modern methods?

The biggest single cost in system development is people cost. Computer
time is insignificant.  If I can produce programs which meet the
application requirement plus all the other advantages previously
mentioned, using my minimalist approach, why should I change it?

Finally, the proof of the pudding is in the eating. If you would
like to see something I wrote go to foodman123.com/tcs.htm. If
you would like to see the software I sell for a living, let me
know and I will email you a copy of one of them.

(p.s., I should apologize to docdwarf (why doesn't he use that
name anymore?), he wasn't nasty, just pointless.

(p.p.s. Somewhere, someone accused me of bragging. I don't think
I am, I am just stating facts from my point of view. I have a tendency
to be blunt. The fact that most of the denizens of CLC think I am an
idiot doesn't bother me at all. All I have to do is look at my track
record.)

Thanks

Tony DIlworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q03x5.1714$l35.39423@iad-read.news.verio.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au> <8q28r8$71i$1@nnrp1.deja.com>`

```
In article <8q28r8$71i$1@nnrp1.deja.com>, Foodman  <foodman123@aol.com> wrote:
>
>> >
…[7 more quoted lines elided]…
>Hi Ken:

>I would rather save
>coding-time than execution-time which is invisible anyway.

Mr Dilworth, have you ever heard of something called 'CPU Chargeback'?

>Wouldn't
>a designer KNOW whether he was going to have execution-time problems
>BEFORE the program was written and take appropriate action?

Mr Dilworth, 'execution-time problems' can be a result of change in
data-volume; what is appropriate for, say, 20,000 transactions/day is a
bottleneck for 20,000,000.

>
>If what I wrote is not utterly clear, then I don't know what to say.

How about saying, as Mencken did, 'For every complex problem there is a
readily-apparent and simple solution... which is *wrong*'?

[snippage]

>(p.s., I should apologize to docdwarf (why doesn't he use that
>name anymore?), he wasn't nasty, just pointless.

Pointless?  Pardon me for being obscure, Mr Dilworth; let me clarify what
I wass trying to get across:

Your situation, by your admission, is an anomaly.  Attempting to apply
techniques which satisfy the requirements of an anomaly to less-anomalous
situations do not always have the most desirable results.

Is that clearer?

DD
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q2uf1$b8k$1@news.igs.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au> <8q28r8$71i$1@nnrp1.deja.com>`

```
Foodman wrote in message <8q28r8$71i$1@nnrp1.deja.com>...

>Earlier this year, I rated myself at 76 debugged lines of code per hour.
>The reason I can achieve such a rate is because of my minimalist
…[9 more quoted lines elided]…
>

On the same platform that you mention, I did 35,000 lines in the last two
months.  Of course, I used every trick in the book, the most important of
which is a superlative text editor.  Not that it means a damned thing. A
minimalist approach can work for a simple project. For a more advanced
project it works less well.  For a really complex project, sophisticated
tools can save lots of time and prevent dozens of errors.

Your approach of "there is only one way to program" sucks.  There are
thousands of ways.  There are dozens of tools.  While I'd agree that jumping
on every bandwagon that comes along wastes time, and that the learning curve
for new stuff can seriously impact your production, hiding your head in the
sand is even worse.  Just a few months ago, you were claiming that GUI's
were stupid, unnecessary, and that you would *never* use one.  Now you are
programming in SP2.  The world ain't gonna adapt to you, Tony.

Donald <an old fart, but not quite fossilised yet>
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 8)_

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q3uiu02944@enews4.newsguy.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au> <8q28r8$71i$1@nnrp1.deja.com> <8q2uf1$b8k$1@news.igs.net>`

```


----------
In article <8q2uf1$b8k$1@news.igs.net>, "donald tees" <donald@willmack.com>
wrote:
> I used every trick in the book, the most important of
> which is a superlative text editor.

-- Couldn't agree more.


Before that, DocDwarf wrote...

> Mr Dilworth, 'execution-time problems' can be a result of change in
> data-volume; what is appropriate for, say, 20,000 transactions/day is a
> bottleneck for 20,000,000.

-- Couldn't agree more.  As I said before, there is no such thing as a fast
program.

Jeff
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 8)_

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q5155$6vt$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au> <8q28r8$71i$1@nnrp1.deja.com> <8q2uf1$b8k$1@news.igs.net>`

```
Just a few months ago, you were claiming that GUI's
> were stupid, unnecessary, and that you would *never* use one.  Now
you are programming in SP2.  The world ain't gonna adapt to you, Tony.
> Donald <an old fart, but not quite fossilised yet>
>
Hi:

I categorically never said that GUI's were stupid, etc.

I have been using the SP2 GUI for at least THREE YEARS,
long before I ever heard of CLC. I praise SP2 whenever
I get the opportunity.

What I have said is that I do not use the conventional
windows goodies like drop-down lists, combo boxes and
all the other stuff.

The windows API presumes that the primary input device
is the mouse.

The mouse is not an efficient device.

The keyboard is a better input device.

Therefore, design for the keyboard using the API but not its
features.

If you wish to see an example of this approach go to
foodman123.com/tcs.htm

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C63FB4.A18D6FA1@dced.state.ak.us>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au> <8q28r8$71i$1@nnrp1.deja.com>`

```
Foodman wrote:

> > >
> >
…[80 more quoted lines elided]…
> Tony DIlworth

To me the test of maintainability is not how easy it is for *you* to
understand and change the code you write but how easy it is for *others* to
do so. Locally there are a few programmers whose code I won't touch. When
asked for an estimate on changes to an application they wrote I give an
estimate for a total rewrite. From their viewpoint these programmers are
smart. They've locked their customers into themselves as a proprietary
solution, which ensures them a continuing income until the last of their
customers quit using their applications. They get very few new customers but
that's probably because they've developed a local reputation, and it's
pretty bad. Sounds like you're striving for a national reputation which is
harder to get.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C65228.18185A6C@brazee.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au> <8q28r8$71i$1@nnrp1.deja.com>`

```

Foodman wrote:

> I really don't see a problem with what I presented.  As I mentioned
> elsewhere, my concern is speed of development - who cares about
…[3 more quoted lines elided]…
> BEFORE the program was written and take appropriate action?

I find speed and accuracy of maintenance to be much more important than
speed of development.  But I am basing my opinion from working in a shop
where people have to maintain other people's code.


>  To me the most time-consuming aspect of programming is the
> time it takes to type the program.  The simpler the code, the faster
> it is to write.

Writing code is the fastest element of programming - at least for
experienced programmers who have developed techniques.  It is almost
trivial.  Analysis, testing, and maintenance take up much more time.


> How many debugged lines per hour can you achieve using your more
> modern methods?

I am not familiar with this way of measuring.  I am trying to picture it and
am failing.  How many lines does a typical bug take?  How many buggy lines
do you have in a program?  For me, usually debugging means I find out
something is wrong, I create test conditions and reproduce the error, I find
the error in the code, I test the fix, I run system tests.  I certainly
can't work on 76 problems in an hour, even if I have programs with more than
one known bugs.

Maybe one reason I consider coding the quickest portion of programming is
that  I don't work on more than a handful of programs at a time, so I have
no chance to see 76 lines of buggy code in an hour.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 6)_

- **From:** Jeff York <jeff@jakfield.xu-netx.com>
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o0aessscchcjahmtvsopjpjn2vfa0gkmlm@4ax.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au>`

```
Ken Foskey <waratah@zip.com.au> wrote:

>Foodman wrote:
>
…[44 more quoted lines elided]…
>end-evaluate.

<cat amongst pigeons>

if you're really worried about performance then

if x-function = "A" perform function-a go to 100-next-bit.
if x-function = "B" perform function-b go to 100-next-bit.
if x-function = "C" perform function-c go to 100-next-bit.
perform default-function.
       100-next-bit.
..etc..

It would be interesting to see the amount of object code generated by
different compilers when presented with the numerous
functionally-similar examples..    :-)

</cat amongst pigeons>

>Of course if I was using OO then I could eliminate the evaluate statement
>entirely because the object knows which one it wants and does not directly
…[5 more quoted lines elided]…
>places.

..at the cost of all the overheads that OO seems to create..

>Mr Dilworth I still believe that dinosaurs exist in this world,   what you
>consider maintain able is trash to another person.  Because you are
…[8 more quoted lines elided]…
>the next programmer to work with us or following us.

Agreed absolutely in principle..  However,  the thing that annoys me
is the automatic assumption that "structured code" is "good" and
anything else is "bad"..   In my 30+ years in the trade I've seen some
so-called "structured" code that is an impenetrable mess and I've seen
some "spaghetti" that's a model of clarity and clear-thinking.   It's
not the tools that we use,  it's the way that we use them.  I own an
expensive set of carpentry equipment - but my shelves still fall off
the wall because I'm a crap carpenter..

>I appreciate the reminder of the 1960's view of programming,  please
>continue to give us this walk down memory lane,

Very useful to be mindful of the 60's views of programming - you may
still have to maintain stuff written in the 60s..  :-)
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C768AE.847E21FF@brazee.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com> <39C3E02B.8285EE04@zip.com.au> <o0aessscchcjahmtvsopjpjn2vfa0gkmlm@4ax.com>`

```
Jeff York wrote:

> if you're really worried about performance then
>
…[5 more quoted lines elided]…
> ..etc..

Why not go whole hog - does the ALTER command still work?

Like I said earlier - significant performance gains aren't in saving an extra
IF statement, they are in moving stuff out of loops, and above all,
understanding your data and process flow.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C64AF7.2BFA23E0@brazee.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100> <8q03f6$t6l$1@nnrp1.deja.com>`

```
Foodman wrote:

> What is so wrong with the following?
>
> IF X-FUNCTION = 'A' PERFORM FUNCTION-A.
> IF X-FUNCTION = 'B' PERFORM FUNCTION-B.
> IF X-FUNCTION = 'C' PERFORM FUNCTION-C.

That works fine.  Until FUNCTION-A changes the value of X-FUNCTION to 'B'.
Sometimes it is best to make sure that the maintenance programmer doesn't
have to worry about changing logic away from his maintenance code.
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7rNw5.381$qu1.118740@paloalto-snr1.gtei.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100>`

```
Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:39c384c7.3062625@207.126.101.100...
> Ok - I need evaluate.  Because my brain can only nest so far.
> Evaluate is ideal for code that used to look like this:
…[9 more quoted lines elided]…
>

If it "looked" like that, you're lucky. All the stuff I inherited looked
like..

 IF X-Function = "A"
     Perform Function-A
 ELSE
 IF X-Function = "B"
     Perform Function-B
 ELSE
 IF X-Function = "C"
      Perform Function-C
 ELSE
 IF X-Function = "D"....

(for twenty or so iterations)...

MCM
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 4)_

- **From:** Liam Devlin <liamddd@optonline.net>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39C3D4E6.D205AFC7@optonline.net>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100>`

```
Thane Hubbell wrote:
> 
> Ok - I need evaluate.  Because my brain can only nest so far.
…[21 more quoted lines elided]…
> END-EVALUATE

Right, if it's *really* A or B, then IF/THEN/ELSE/END-IF is the proper
construct. Anything more than that really calls for Evaluate, i.e., case
structure. I'll sometimes use an Evaluate in an A or B situation if I
anticipate additional cases being added (with a comment, of course).

As far as the format goes, the same way we (most of us, anyway) code:

IF ....
	.....
ELSE
	....
END-IF

indicating the same logical level, I extended the same philosophy to
Evaluate, as in:

EVALUATE	something
WHEN		XXX
	do something1
WHEN		YYY
WHEN		ZZZ
	do something2
.
.
.
WHEN		OTHER
	do the last resort
END-EVALUATE

which, IMHO, makes the idea of the same logical level quite plain
(except to Dilworth, perhaps <g>). I'm not, BTW, saying Thane is
"wrong", just offering an alternative POV.

LiamD
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@leif.org>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ORSw5.5110$3y3.129510@typhoon.austin.rr.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com> <39c384c7.3062625@207.126.101.100>`

```
But written like this:
> IF X-Function = "A"
>     Perform Function-A
…[6 more quoted lines elided]…
> .
it has all the looks of an EVALUATE statement
and is portable to older compilers without one.
No mental stacking necessary

Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:39c384c7.3062625@207.126.101.100...
> Ok - I need evaluate.  Because my brain can only nest so far.
> Evaluate is ideal for code that used to look like this:
…[55 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Evaluate statement in CobolII

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2000-09-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0ob7sskm3sa3jddf7vom6bq7hrnet5r6mo@4ax.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default> <8prhhs$2j6$1@nslave2.tin.it> <8pt9pp$om0$1@nnrp1.deja.com>`

```
On Fri, 15 Sep 2000 13:56:21 GMT, Foodman <foodman123@aol.com> wrote:

>
>Who needs EVALUATE?
>
>Thanks

I do.  Having a decision table like this

 						1	2	3	4	5	6
 is-customer					y	n	y	y	/	
 is-reliable					y	n	y	y	n	
 current credit < max credit			y	n	y	y	/	
 wanted credit <= max credit - current credit	y	n	n	y	/	
 wanted credit > min credit			y	n	y	n	/	
 grant credit					x					
 decline credit						x			x	
 decrease credit to maximum					x			
 suggest higher credit							x		
 suggest new negotiation								


 you can easily transform it (one to one) to an evaluate statement like the following
x

 EVALUATE is-customer 
    ALSO is-reliable
    ALSO current-credit < max-credit
    ALSO wanted-credit <= (max-credit - current-credit)
    ALSO wanted-credit > min-credit
  WHEN TRUE ALSO TRUE ALSO TRUE ALSO TRUE ALSO TRUE
    PERFORM grant-credit
  WHEN FALSE ALSO FALSE ALSO FALSE ALSO FALSE ALSO FALSE
    PERFORM decline-credit
  WHEN TRUE ALSO TRUE ALSO TRUE ALSO FALSE ALSO TRUE
    PERFORM decrease-credit
  WHEN TRUE ALSO TRUE ALSO TRUE ALSO TRUE ALSO FALSE
    PERFORM increase-credit
  WHEN ANY ALSO FALSE ALSO ANY ALSO ANY ALSO ANY 
    PERFORM decline-credit
  WHEN OTHER
    PERFORM new-negotiate
END-EVALUATE


Also, when a new business case is added, it is way easier to modify the evaluate statement
than a set of gazillion nested IFs....

My built in stack processor can't do that many nested levels of IFs.  I tell my students -
If more than 2 levels need to be nested, it is usually better (read: more readable, and
more maintainable) than nested ifs



     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)



      "If you lived today as if it were your last, you'd buy up a box of rockets and fire them all off, wouldn't you?"  - Garrison Keillor
```

#### ↳ Re: Evaluate statement in CobolII

- **From:** jacksleight@my-deja.com
- **Date:** 2000-09-17T03:57:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8q1fe6$ch6$1@nnrp1.deja.com>`
- **References:** `<01c01abe$552b8dc0$ef7accd1@default>`

```
Hi John,

You and your small questions. See what you started here? Forty three
replies and a cat fight! Any way, if your indicator ranges from
1 to n, I think you can use:

       when 'NJ' also NOT 1

Regards, Jack.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
