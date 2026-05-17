[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Static vs Dynamic Linking ?

_6 messages · 5 participants · 1996-08_

---

### Static vs Dynamic Linking ?

- **From:** "andy styles" <ua-author-8438810@usenetarchives.gap>
- **Date:** 1996-08-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<320B618C.722C@ibmmail.com>`

```

Hi all,

I'm on contract at Ford Motor Company in England at present. Here, we use
static linking, with COBOL/370, IMS-DC & DB2. At my last place, it was
also static linking. At the place before that (where I was permanent), we
used dynamic linking.

Now, to my mind, dynamic linking is far superior to static linking.
Anyone else have any comments, or reasons why it isn't ?

Andy Styles. 

     /o/-------------------------------------/o/
    /o/ EMail: usf··.@ibm··l.com (work)  /o/
   /o/       and··.@dir··o.uk  (home)   /o/  
   \o\. . . . . . . . . . . . . . . . . . .\o\
   /o/ My opinions are my own, and do not  /o/
  /o/ reflect those of Ford Motor Company /o/
```

#### ↳ Re: Static vs Dynamic Linking ?

- **From:** "arthur e. gould" <ua-author-16705253@usenetarchives.gap>
- **Date:** 1996-08-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9bdd737ae-p2@usenetarchives.gap>`
- **In-Reply-To:** `<320B618C.722C@ibmmail.com>`
- **References:** `<320B618C.722C@ibmmail.com>`

```

dynamic linking and static linking server different purposes. You have
to choose the method best suited for the environment in which your
programs will run. You mention IMS DC, which since version 4.1 of
IMS/ESA is now referred to as IMS TM (Transaction Manager); apologies if
you already knew that :-).

Anyway... in an on-line environment like IMS TM additional overhead is
occurred when calling a module which is dynamically loaded. Unless
memory is extremely tight and unable to accomodate a load module
produced with everything static linked - unlikely - static linking is
preferred for performance reasons; your transactions will run faster.
```

#### ↳ Re: Static vs Dynamic Linking ?

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-08-09T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9bdd737ae-p3@usenetarchives.gap>`
- **In-Reply-To:** `<320B618C.722C@ibmmail.com>`
- **References:** `<320B618C.722C@ibmmail.com>`

```

Static Linking Versus Dynamic Linking - a topic near and dear to Topic 4
of my Planning COBOL Migration course.

Dynamic linking: upsides -
instant effectiveness of any change to subroutines across multiple callers

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: Static vs Dynamic Linking ?

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-08-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9bdd737ae-p4@usenetarchives.gap>`
- **In-Reply-To:** `<320B618C.722C@ibmmail.com>`
- **References:** `<320B618C.722C@ibmmail.com>`

```


Static versus dynamic linkage to subroutines.

(at least for IBM mainframe users)

A small extract of several hours of discussion from my Planning COBOL
Migration course materials...

Static Linkage:
Plusses
Best Performance (especially in online environments)
Ability to automatically generate routine cross-references
using only load modules (usefull for impact analysis)
Minuses
Easy to miss usage of routines used across many programs.
(A tool that I developed solves this problem automatically)
Necissity to relink all users of a routine
(same tool fixes this as well).
No "built-in" feature in run-times to handle AMODE / RMODE
mismatch issues.
Dynamic Linkage
Plusses
Automatic update of all users of a routine
Run-time handles most AMODE / RMODE difference issues
across CALLs
May be able to acheive better performance by pre-loading
common routines (i.e. date converters) used across many
applications.
Minuses
Performance is lower, especially with very intense call to other
verb density, or online, response oriented applications.
No way to easily dictionay CALL tree structure.
source analysis will help for CALL 'literal'
no help for CALL dataname

Bottom line - Without (blatent commercial) auto - relinker and impact
anaysis tool Static CALLs were turkeys to manage, especially when a
routine was deployed across dozens to hundreds to thousands of load
modules. Static structures nearly always provide higher levels of
performance.

Dynamic Calls are simpler, especially in a test environment.
Cross-reference issue can be a significant factor in both static and
dynamic environment.

Auto mode switching / checking can be a significant factor in cases where
old technology (OS/VS COBOL or earlier) must be mixed with 31-bit
capability (VS COBOL II, COBOL/370 or COBOL for MVS and VM).

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

##### ↳ ↳ Re: Static vs Dynamic Linking ?

- **From:** "fr..." <ua-author-16633589@usenetarchives.gap>
- **Date:** 1996-08-11T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9bdd737ae-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c9bdd737ae-p4@usenetarchives.gap>`
- **References:** `<320B618C.722C@ibmmail.com> <gap-c9bdd737ae-p4@usenetarchives.gap>`

```

In article <4ukv7u$d.··.@new··l.com>, rwi··.@a··.com (RWidmer) writes:
› Static versus dynamic linkage to subroutines.
› 
…[48 more quoted lines elided]…
› survive in a legacy based world.

In general, these are all true and correct. But in some specific cases the
tradeoffs might be more complicated: Static linkages provide better performance
than dynamic calls that search many large libraries for many subroutines; but
for a large number of big, infrequently used subroutines the initial load time
of the static module that includes them all might outweigh any savings. Or a big
load module might cause the memory management routine to thrash around and push
other modules out.

The change control issue also varies for every shop. Dynamic subprogram calls
are not used in some places because they take effect without relinking,
possibly skipping a quality assurance regression test step.
```

##### ↳ ↳ Re: Static vs Dynamic Linking ?

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-08-11T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9bdd737ae-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c9bdd737ae-p4@usenetarchives.gap>`
- **References:** `<320B618C.722C@ibmmail.com> <gap-c9bdd737ae-p4@usenetarchives.gap>`

```

rwi··.@a··.com (RWidmer) wrote:
› 
› Static versus dynamic linkage to subroutines.
…[49 more quoted lines elided]…
› survive in a legacy based world.

This is good information. If the question is, should I use static or
dynamic subprogram linkage in an IBM mainframe environment, then I would
suggest the following recommendations:

If the subprogram is general purpose, and will be called by many
different programs (like a date routine, for example), it should be
dynamically linked. You don't want to re-link every calling program if
the subprogram changes. This is true even in a CICS environment. The
overhead is small compared to the maintenance nightmares.

If the subprogram is only called from one program (for example, you want
to break up a very large program into smaller modules for ease of
understanding or to put multiple programmers on the same program), then
static linking is okay. It will execute slightly faster, and you don't
have the same maintenance headaches. You still have to re-link the main
program if any subprogram is changed.

Just my two cents.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
