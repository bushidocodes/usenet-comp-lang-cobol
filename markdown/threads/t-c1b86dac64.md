[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol 370

_4 messages · 4 participants · 1996-08_

---

### Cobol 370

- **From:** "philip" <ua-author-18201@usenetarchives.gap>
- **Date:** 1996-08-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4unjhf$in6@lantana.singnet.com.sg>`

```

I have a problem here and i hope all you kind experts can help.
Currently we are developing cobol 370 programs in CICS MVS. We also
have a number of programs that are still in OS COBOL and VS COBOL.
We notice that some of our call subroutines do no work well in the
CICS 3.3.
Has to got to do with the AMODE and RMODE linkage option ?

What are the rules for a program calling another programs ?

Can a OS cobol call a VS cobol program ?

Are there some universal cobol compilation options that work in all
cases ?

We have sub-routines that are used by both batch and online CICS
programs and they do not seem to work well when in CICS 3.3. Has it
got to do with the CICS ? Can experts on CICS 3.3 comment on this.
```

#### ↳ Re: Cobol 370

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-08-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1b86dac64-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4unjhf$in6@lantana.singnet.com.sg>`
- **References:** `<4unjhf$in6@lantana.singnet.com.sg>`

```


The total answer to this takes several hours of lecture and dozens of
foils
in the course "Planning COBOL Migration" which I authored and teach thru
Edge
Information Group.

Dependancies - AMODE / RMODE capability of CALLed program
AMODE / RMODE of CALLed program
how are they connected COBOL static CALL,
COBOL dynamic
CALL
CICS
mechanisms
where is the data which is passed
what compile time options were used - especially
RES/NORES
which run-time modules are used in each component.

Bottom line, this is a quite complex topic to answer generally, lots of
pitfalls, made even more complex by the introduction of CICS.

But it is soluable. Examine each CALLer / CALLed program as a pair. It
does
not matter how big the total application is, if each CALL pair is valid,
then
the entire application is valid.

How to automate - use the Edge Portfolio Analyzer to examine all of the
components. It can do 10,000 load modules in less than 1 hour e.t. and a
minute or so of CPU time. An output file then contains all of the
information to thoroughly examine most of the cases (excluding some
dynamic
linkage situations which leave no clues until execution time).

I would be happy to provide some additonal information, but it is hard to
type a half day's lecture into an e-mail.

If I had to mention just a minimum approach it would be to deal with
subroutines first, then mainlines. This way the higher capability is
introduced from the bottom of the structure and you do not have the case
of
"low function" being called by "high function".

If you would like to schedule a phone discussion, e-mail me. I am hard to
catch by phone, but with advance notice a call can usually be set up.


Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: Cobol 370

- **From:** "7161..." <ua-author-17086533@usenetarchives.gap>
- **Date:** 1996-08-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1b86dac64-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4unjhf$in6@lantana.singnet.com.sg>`
- **References:** `<4unjhf$in6@lantana.singnet.com.sg>`

```

›› We have sub-routines that are used by both batch and online CICS
›› programs and they do not seem to work well when in CICS 3.3. 
›› Has it got to do with the CICS ? Can experts on CICS 3.3 comment 
›› on this.  
I'm not a real expert on this but here goes...Prior to CICS 3.3
the system didn't really look at whether a program "modified" its
own code or not. The working storage section in your COBOL module
is handled as a CICS dynamically acquired storage area and is
protected by CICS. OTOH, any linked subroutine would be invisible
to CICS...Now, if that subroutine had working storage (and most
do) CICS would perceive that the program was "self-modifying".
CICS 3.3 now takes special actions to inhibit these programs from
harming themselves which does cause performance to suffer...I'm
not sure that there's an answer to this but I know it happens
since I wrote a program in COBOL that made extensive use of an
internal table (provided via an assembler subroutine) to control
information required during the entire CICS system duration; this
protection mechanism raised it's head in CICS 3.3 (ran great in
3.2 and prior releases since 1.7). Unfortunately, I'm aware of
the problem but didn't have the opportunity to go into a great
deal of the investigation and re-write. BTW, the application
included full gating logic and was specifically disigned to handle
multi-threaded operations once the gate was unlocked but there
seemed no way that you could communicate this to CICS (from what
I'm told) short of writing the application in assembler.

Kevin P Corkery
Independent Consultant
716··.@Com··e.com
```

##### ↳ ↳ Re: Cobol 370

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-08-15T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c1b86dac64-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c1b86dac64-p3@usenetarchives.gap>`
- **References:** `<4unjhf$in6@lantana.singnet.com.sg> <gap-c1b86dac64-p3@usenetarchives.gap>`

```

Kevin P Corkery <716··.@Com··e.COM> wrote:
››› We have sub-routines that are used by both batch and online CICS
››› programs and they do not seem to work well when in CICS 3.3. 
…[27 more quoted lines elided]…
› 716··.@Com··e.com

This is very interesting. At my shop I wrote a date routine in COBOL II
for batch programs. Another programmer expressed interest in using it in
a CICS 3.3 region, and said it should work. He just called it
dynamically (the program does not use any CICS services, obviously). It
works like a champ.

I was most interested in your comments on using a table throught an
entire CICS system. We do something that sounds like that, and have
never had any problem. The technique is essentially unchanged from CICS
version 1.61 to 1.7 to 2.1.1 to 2.1.2 to 3.3. We have a number of
in-core tables. Each is an assembler program consisting only of DC
(Define Constant) statements to allocate space for the maximum number of
entries. The table programs are practically the only assembler in the
system. Everything else is COBOL II.

At CICS startup time, all the table programs are loaded into memory using
EXEC CICS LOAD commands. The table programs are populated with data, and
finally the addresses, element lengths, and element counts are stored in
one master table. Then we write a temp storage queue containing the
address of the master table.

The application which uses the tables consists of multiple long-running
conversational tasks. Each task reads the temp storage queue to obtain
the address of the master table, then all the addresses of the data
tables are obtained and copied into the task's TWA (Transaction Work
Area). From that point on, any program that needs to reference any table
(including updating it) simply copies the address from the TWA, performs
a SET ADDRESS OF linkage-section-record-name TO pointer-name, and we have
our tables mapped in.

The technique works quite well, and we had no problems migrating from
CICS 2.1.2 to CICS 3.3.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
