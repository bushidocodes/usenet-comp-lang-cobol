[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Stack and Heap concept in COBOL

_7 messages · 5 participants · 2002-01_

---

### Stack and Heap concept in COBOL

- **From:** menonshyam@yahoo.com (shyam menon)
- **Date:** 2002-01-21T22:57:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10986fae.0201212257.6f9e5ec2@posting.google.com>`

```
Hi,  
  I am new to this group.I am a bit confused about the memory
allocation in COBOL. Till now i was under the impression that there is
no dynamic allocation of memory in COBOL and the Working storage
variables are allocated memory when the load module is loaded.
  But i found the following information about Working storage
variables in an IBM manual:
Usage of Stack and Heap Storage by Language Environment-Conforming
Languages

Language  Stack                       Heap  
COBOL    Intrinsic functions          WORKING-STORAGE variables      
         Library routines                                            
         LOCAL-STORAGE variables(1)                                  
  

 STACK        Used by library routine stack frames that can reside
                 anywhere in storage
 HEAP         Allocates storage for user-controlled dynamically
                 allocated variables  

  Could anyone help me with understanding this?

Thanks in advance,
Shyam Menon.
```

#### ↳ Re: Stack and Heap concept in COBOL

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2002-01-22T12:57:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020122075724.12654.00000169@mb-fr.aol.com>`
- **References:** `<10986fae.0201212257.6f9e5ec2@posting.google.com>`

```
Shyam Menon writes ...

>Hi,  
>  I am new to this group.I am a bit confused about the memory
…[19 more quoted lines elided]…
>  Could anyone help me with understanding this?

There is no _explicit_ dynamic allocation of memory in COBOL '85, even with the
'89 amendment. There may be some in COBOL 2002, but I haven't looked at the new
proposed standard yet.

But the IBM mainframe COBOL compiler uses dynamic allocation behind the scenes
as you described. In addition, all supported IBM compilers now require the use
of a facility called "Language Environment" (LE). LE includes callable
functions to dynamically allocate, resize, and free Heap storage.

Hope this helps.

Kind regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: Stack and Heap concept in COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-22T19:01:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2l20r$59i$1@nntp9.atl.mindspring.net>`
- **References:** `<10986fae.0201212257.6f9e5ec2@posting.google.com> <20020122075724.12654.00000169@mb-fr.aol.com>`

```
FYI-
  The (opposed/draft) 2002 Standard *does* introduce the ALLOCATE and FREE
statements for "explicit" dynamic storage allocation.

It also distinguishes Working-Storage from Local-Storage.  In *most*
implementations (although this is NOT specified in the draft Standard), I
would expect Local-Storage to be allocated from "stack storage".  IBM (along
with Micro Focus - and possibly some others) already supports Local-Storage
as an EXTENSION to the '85/'89/'91 Standard.
```

###### ↳ ↳ ↳ Re: Stack and Heap concept in COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-22T20:03:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2l5l3$8et$1@slb7.atl.mindspring.net>`
- **References:** `<10986fae.0201212257.6f9e5ec2@posting.google.com> <20020122075724.12654.00000169@mb-fr.aol.com> <a2l20r$59i$1@nntp9.atl.mindspring.net>`

```
Talk about a "typo"  <G> (aka Freudian slip)

That "(opposed/draft) 2002 Standard" was SUPPOSED to be "proposed/draft"
```

#### ↳ Re: Stack and Heap concept in COBOL

- **From:** daniel.jacot@winterthur.ch (Daniel Jacot)
- **Date:** 2002-01-22T06:15:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f3c351f.0201220615.57ffb089@posting.google.com>`
- **References:** `<10986fae.0201212257.6f9e5ec2@posting.google.com>`

```
menonshyam@yahoo.com (shyam menon) wrote in message news:<10986fae.0201212257.6f9e5ec2@posting.google.com>...
> Hi,  
>   I am new to this group.

Well, hello and welcome to CLC!

> I am a bit confused about the memory allocation in COBOL.

Don't mind, others are confused, too &-))

> Till now i was under the impression that there is
> no dynamic allocation of memory in COBOL and the Working storage
> variables are allocated memory when the load module is loaded.

Yes, you are right. WORKING-STORAGE is allocated when the program is
executed for the first time in a thread and remains allocated (and in
its last used state) if you call the program again. So , variables in
WORKING-STORAGE behave like they where static variables of a C or PL/I
program.

>   But i found the following information about Working storage
> variables in an IBM manual:
…[6 more quoted lines elided]…
>          LOCAL-STORAGE variables(1) 

OK, now we are talking of LOCAL-STORAGE instead of WORKING-STORAGE.
Variables which are declared in the LOCAL-STORAGE Section are
allocated in the STACK rather than in the HEAP. They are intialized at
every entry of the program and freed as soon as the program reaches
its end.
You will not be too surprised if I tell you that this kind of
variables is called automatic in C and PL/I. You need LOCAL-STORAGE
variables if you need a COBOL program to be called recursive (and of
course you need at least one variable in WORKING-STORAGE to be able to
stop the recursion).

OK, and the library routines and the intrinsic functions use the STACK
too. Probably, these routines are written in C and use automatic
storage. No problem, let them use what they have to use!
                                 
>   
> 
>  STACK        Used by library routine stack frames that can reside
>                  anywhere in storage

I'd guess you are now in another chapter of the manual. In which
chapter?

>  HEAP         Allocates storage for user-controlled dynamically
>                  allocated variables 

If a user-program ALLOCATEs storage, it gets HEAP storage. In COBOL,
there is no verb for ALLOCATE, you have to CALL CEEGTST.
 
> 
>   Could anyone help me with understanding this?

OK, now exactly WHAT are you trying to understand? If you are aware of
the (writable) static and the automatic concept in C, you should be
happy to see that COBOL is able to handle these kind of storage too.
But, to be honest, most people know that in COBOL all variables are in
its last used state, so they forget about the VALUE clause and they
are just happy.

> 
> Thanks in advance,
> Shyam Menon.

Daniel
```

##### ↳ ↳ Re: Stack and Heap concept in COBOL

- **From:** nivas_shyam@indiatimes.com (shyam nivas)
- **Date:** 2002-01-24T19:59:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c02fd744.0201241959.5182fbc9@posting.google.com>`
- **References:** `<10986fae.0201212257.6f9e5ec2@posting.google.com> <7f3c351f.0201220615.57ffb089@posting.google.com>`

```
Hi,
                Referring to your reply "WORKING-STORAGE is allocated
when the program is executed for the first time in a thread and
remains allocated (and in its last used state)".
                Now my concern  is if WORKING-STORAGE is defined at
run time then at compile time why I have to compile with REGION = 0M
When length of data defined in WORKING-STORAGE is too high?
               when I tried with REGION=6M I got MAXCC=16?These two
are contradicting each other.
              Please clear my doubts.
Thanks and Regards.
shyam
*******************************************************************************
daniel.jacot@winterthur.ch (Daniel Jacot) wrote in message news:<7f3c351f.0201220615.57ffb089@posting.google.com>...
> menonshyam@yahoo.com (shyam menon) wrote in message news:<10986fae.0201212257.6f9e5ec2@posting.google.com>...
> > Hi,  
…[71 more quoted lines elided]…
> Daniel
```

###### ↳ ↳ ↳ Re: Stack and Heap concept in COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-01-24T23:19:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2qptt$s9u$1@slb0.atl.mindspring.net>`
- **References:** `<10986fae.0201212257.6f9e5ec2@posting.google.com> <7f3c351f.0201220615.57ffb089@posting.google.com> <c02fd744.0201241959.5182fbc9@posting.google.com>`

```
The amount of storage needed to compile a program has (close to) NOTHING to
do with the amount of storage allocated at run-time.  As you are using an
IBM mainframe compiler, check out your value for the SIZE *compiler-option".

For a RENT compiled program, the size of the load module *will* include the
size of all literals (both user-defined and compiler-defined) as well as (at
least one copy) of WS.  The amount of "virtual storage" needed to COMPILE a
program has LOTS to do with the "complexity" of the program, its source code
length, and many, MANY other items - with the size of WS being a "miniscule"
part of the equation.  The amount of virtual storage needed to RUN a COBOL
program (RENT, NORENT, with dynamic or static calls, whatever) *does* have a
lot to do with WS (and file section, and procedure division) and many, MANY
other things - most of which can be INFERRED from the load module size.

Shyam,
  I hate to keep coming back to this, but it really, REALLY sounds to me as
if you are approaching IBM mainframe COBOL development with

 A) inadequate training
 B) "misconceptions" based on different programming languages and operating
systems
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
