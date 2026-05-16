[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to do GOTO in ANSI85 COBOL

_6 messages · 5 participants · 1994-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards) · [`Help requests and how-to`](../topics.md#help)

---

### How to do GOTO in ANSI85 COBOL

- **From:** brunelle@info.polymtl.ca (Frederic Brunelle)
- **Date:** 1994-12-01T20:48:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3blcr9$dsl@charles.cdec.polymtl.ca>`

```
Hi. I was the original poster of this thread. I know you're not
supposed to use GOTOs but the thing is, I am not writting new
code. I must convert some kind of pseudo-code file to a COBOL
file. Because of the structure of the pseudo-code file, I
needed the GOTO statement to simulate a <while> loop. And thanks
to the information some of you gave me, I have been able to use
the goto statement with success (even though the produced COBOL
file is not what you might called good structured programming).

F. Brunelle
```

#### ↳ Re: How to do GOTO in ANSI85 COBOL

- **From:** mgphl@crl.com (Michael G. Phillips)
- **Date:** 1994-12-02T18:58:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bomti$bt5@crl6.crl.com>`
- **References:** `<3blcr9$dsl@charles.cdec.polymtl.ca>`

```
	Ye Gads!  Whats to "simulate" ????
	Didn't you see *anything* at all about
	the PERFORM statement you were scanning
	doc for help with the GO TO?

Frederic Brunelle (brunelle@info.polymtl.ca) wrote:
: Hi. I was the original poster of this thread. I know you're not
: supposed to use GOTOs but the thing is, I am not writting new
: code. I must convert some kind of pseudo-code file to a COBOL
: file. Because of the structure of the pseudo-code file, I
: needed the GOTO statement to simulate a <while> loop. And thanks
: to the information some of you gave me, I have been able to use
: the goto statement with success (even though the produced COBOL
: file is not what you might called good structured programming).

: F. Brunelle
```

#### ↳ Re: How to do GOTO in ANSI85 COBOL

- **From:** bcdiver@freenet.vancouver.bc.ca (Ron Ross)
- **Date:** 1994-12-03T05:26:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bovis$s4b@freenet.vancouver.bc.ca>`
- **References:** `<3blcr9$dsl@charles.cdec.polymtl.ca>`

```
Frederic Brunelle (brunelle@info.polymtl.ca) wrote:
: Hi. I was the original poster of this thread. I know you're not
: supposed to use GOTOs but the thing is, I am not writting new
: code. I must convert some kind of pseudo-code file to a COBOL
: file. Because of the structure of the pseudo-code file, I
: needed the GOTO statement to simulate a <while> loop. And thanks
: to the information some of you gave me, I have been able to use
: the goto statement with success (even though the produced COBOL
: file is not what you might called good structured programming).

: F. Brunelle

    For a while loop you can use an in-line perform statement instead of 
a GO TO.

    PERFORM  UNTIL <condition>
        ...
        INSERT CODE HERE
        ...
    END-PERFORM.

    No GO TO's required.  Ever.
```

##### ↳ ↳ Re: How to do GOTO in ANSI85 COBOL

- **From:** brunelle@info.polymtl.ca (Frederic Brunelle)
- **Date:** 1994-12-04T21:13:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3btbdr$cau@charles.cdec.polymtl.ca>`
- **References:** `<3blcr9$dsl@charles.cdec.polymtl.ca> <3bovis$s4b@freenet.vancouver.bc.ca>`

```
Hi, I used PERFORM UNTIL and it worked just fine. You have helped me solve my
problem. Thank you.
```

#### ↳ Re: How to do GOTO in ANSI85 COBOL

- **From:** Stephen Frost <frostbyt@ozemail.com.au>
- **Date:** 1994-12-06T20:38:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<941207$073510$7848frostbyt@ozemail.com.au>`
- **References:** `<3bomti$bt5@crl6.crl.com> <3blcr9$dsl@charles.cdec.polymtl.ca>`

```
Jeez I'm sick of the CAN use GO TO, CAN'T use GO TO debate...
As far as I'm converned, if its supported in the language (and always will be)
feel free to use it.
If you want to write spaghetti code, that's up to you - just don't ask me to
support it!!!
IMHO, you can use GO TO <carefully> without ending up with spaghetti.
We have a new trainee programmer at work, and the lengths he goes to to avoid
GO TO is amazing (when a single GO TO would do the trick).

GO TO it.....

Steve
```

#### ↳ Re: How to do GOTO in ANSI85 COBOL

- **From:** RDNoyes@ix.netcom.com (Robert Noyes)
- **Date:** 1994-12-12T01:21:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cg8ia$43k@ixnews1.ix.netcom.com>`
- **References:** `<3blcr9$dsl@charles.cdec.polymtl.ca>`

```
In <3blcr9$dsl@charles.cdec.polymtl.ca> brunelle@info.polymtl.ca 
(Frederic Brunelle) writes: 

>
>Hi. I was the original poster of this thread. I know you're not
…[10 more quoted lines elided]…
>

I'm just an old COBOL hack that has been writing this stuff for a few 
years and I have never seen a good reason to use a "GO TO." They always 
wind up biting either there when they are coded or somewhere down the 
road. Just say no to "GO TO's."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
