[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Threads and NetExpress- Unresolved external

_13 messages · 6 participants · 1999-07_

---

### Re: Threads and NetExpress- Unresolved external

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7m59ct$snl$1@nntp3.atl.mindspring.net>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk>`

```
OK...We have narrowed this down to the line of code causing the unresolved
external...It has something to do with the cobol monitor(s)...


Set monitor-name to writing converting from browsing



is the statement causing the unresolved external reference...

Anyone out there use the cobol monitor(s)...???
```

#### ↳ Re: Threads and NetExpress- Unresolved external

- **From:** Stephen Gennard <stephen.gennard@merant.com>
- **Date:** 1999-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378630F8.72BB6511@merant.com>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net>`

```
Ken Mullins wrote:
> 
> OK...We have narrowed this down to the line of code causing the unresolved
…[6 more quoted lines elided]…
> Anyone out there use the cobol monitor(s)...???

If I fail to open the monitor I get a unresolved external, however if
I open the monitor it links okay....

For the purpose of testing the link stage I tried...

        working-storage section.
        01 monitor-name usage monitor-pointer.
        procedure division.
                open monitor-name
                set monitor-name to writing converting from browsing
                close monitor-name.

Have you opened the monitor?
```

##### ↳ ↳ Re: Threads and NetExpress- Unresolved external

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7m5ju2$rt4$1@nntp9.atl.mindspring.net>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com>`

```
Stephen...

Many thanks...Seems the open monitor statement must be ""physically"" before
any set statement for the monitor...In our case, the monitor is opened, but
in a performed routine that is physically after the set monitor
statement...The following code causes an unresolved external in error...

         working-storage section.
         01 monitor-name usage monitor-pointer.
         procedure division.
                   perform open-monitors
                   set monitor-name to writing converting from browsing
                   close monitor-name.
                   exit program
           open-monitors.
                   open monitor-name
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

- **From:** Stephen Gennard <stephen.gennard@merant.com>
- **Date:** 1999-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3789CF92.C2088D83@merant.com>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net>`

```
Ken Mullins wrote:
> 
> Stephen...
…[14 more quoted lines elided]…
>                    open monitor-name

Hi Ken,

I too can reproduce the issue when you compile your application
above.  However the application should be compiled with either one of the
two reentrant (1/2) directives as this is the threaded application.

If you use reentrant"2" it works.  Hope this helps.

        $set reentrant"2"
         working-storage section.
         01 monitor-name usage monitor-pointer.
         procedure division.
                   perform open-monitors
                   set monitor-name to writing converting from browsing
                   close monitor-name.
                   exit program.
           open-monitors.
                   open monitor-name
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

_(reply depth: 4)_

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1999-07-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378B0304.462CF453@merant.com>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net> <3789CF92.C2088D83@merant.com>`

```
Stephen Gennard wrote:
> If you use reentrant"2" it works.  Hope this helps.
> 
…[9 more quoted lines elided]…
>                    open monitor-name

I agree with what Stephen has said, however I should point out that
the purpose of the reentrant"2" directive is to make your DATA DIVISION
thread-local (ie, it's a way of introducing certain legacy modules into
a threaded environment without any program source changes).

Because of this, you would be using monitors to synchronise access to
thread-local data, which is pointless. As Stephen says in his other
message, use the CBL_ calls rather than COBOL syntax to manipulate your
monitors or install the appropriate checker WebSync when it is released.

Cheers, Kev.
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

_(reply depth: 4)_

- **From:** "ber" <barry.rosetti@merant.com>
- **Date:** 1999-07-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mlako$5vm$1@hyperion.mfltd.co.uk>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net> <3789CF92.C2088D83@merant.com>`

```
I just wanted to follow up on this issue so that those of you
that use the multi-threading features of MERANT Micro Focus
COBOL (either Net Express or Server Express) use the right
compiler directives and techniques.

First - the directives.
If your program is going to be executed in a multithreaded
environment then you should use one of the following checker
directives:
  SERIAL    - this directive ensures that only one thread is active
              in your COBOL program at a time.  Any other programs in
              your COBOL application that are directly called _only_
              from the program compiled with the SERIAL directive
              are implicitly serialized as well.
              Access to working storage items do not need to be
              synchronized, however access to external data items
              will need to be.
  REENTRANT - this directive allows multiple threads to enter the program
              at the same time.
              All access to WORKING-STORAGE items or EXTERNAL data items
              must be synchronized with MUTEXes, MONITORS or some other
              technique.
REENTRANT(2)- this directive allows multiple threads to enter the program
              at the same time.  Working-storage is effectively
              THREAD-LOCAL (ie. persistant from call to call within a
              thread, but different for each thread).
              Access to EXTERNAL data items must be synchronized.

Programs compiled with none of these directives MUST be called only from
one thread at a time.

Second - the techniques (this unfortunate bug aside).
0) Read and understand the Multi-threading white-paper in the docs
   or have a good previous grounding in multi-threaded application
   development.

1) You should usually check that the run-time you are using really is
   the multi-threaded run-time system.  The code to do this looks like
   this:
      01  my-thread-id  usage thread-pointer.
      call 'CBL_THREAD_SELF' using my-thread-id
      on exception
          display "NO CBL_THREAD API SUPPORT"
          stop run
      end-call
      if  return-code == 1008
          display "CANNOT RUN MULTI-THREADED APPLICATION"
          stop run
      end-if

2) You must only initialize a synchronization object ONCE in a run-unit.
   This is usually done in 'first time in' code of a reentrant program
   that looks like this:
       01  my-monitor usage monitor-pointer.
       01  pic x value 'Y'.
           88  first-time-in    value 'Y' false 'N'.
       IF  first-time-in
           call 'CBL_THREAD_PROG_LOCK'
           if  first-time-in
               open my-monitor
           end-if
           call 'CBL_THREAD_PROG_UNLOCK'
       end-if
   If your MONITOR-POINTER is EXTERNAL then the 'first-time-in' flag
   must also be external.

3) MONITOR/MUTEX/EVENT-POINTERs can be provided explicitly to the
   matching RTS APIs.  In order to work around the bug that prompted
   this note, you would replace:
       set monitor-name to writing converting from browsing
   with:
       call 'CBL_MONITOR_BROWSE_TO_WRITE' using monitor-name
       if  return-code not = 0
           display "something bad has happened - return code " return-code
           stop run
       end-if

4) In a REENTRANT program, if possible use LOCAL-STORAGE data-items
   for work items, rather than THREAD-LOCAL-STORAGE or WORKING-STORAGE.
   There is a significant impact on program-entry speed when
   THREAD-LOCAL-STORAGE is used within that program.
   Using WORKING-STORAGE (of course) requires synchronization constructs.
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378F5CA1.643880B2@home.com>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net> <3789CF92.C2088D83@merant.com> <7mlako$5vm$1@hyperion.mfltd.co.uk>`

```
ber wrote:
> 
> I just wanted to follow up on this issue so that those of you
> that use the multi-threading features of MERANT Micro Focus
> COBOL (either Net Express or Server Express) use the right
> compiler directives and techniques. <snip> 

Thanks for the advice. 

Concentrating on getting my app finished I haven't even considered
multi-thread at this stage. Can you recommend any generalised document
that covers 'How to...." and the issues involved in going multi-thread ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

_(reply depth: 6)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mo58v$s1g$1@news.igs.net>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net> <3789CF92.C2088D83@merant.com> <7mlako$5vm$1@hyperion.mfltd.co.uk> <378F5CA1.643880B2@home.com>`

```
The issues involved in going multi-thread are really no different than the
issues of going multi-user.  They consist basically of file lockout, plus
communication between simultaneous programs(if required).

If you have written stuff that runs on multiple machines, you probably know
everything that you need to know beyond the simple mechanics of starting new
threads.

James J. Gavan wrote in message <378F5CA1.643880B2@home.com>...
>ber wrote:
>>
…[11 more quoted lines elided]…
>Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378FA695.8C58236F@home.com>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net> <3789CF92.C2088D83@merant.com> <7mlako$5vm$1@hyperion.mfltd.co.uk> <378F5CA1.643880B2@home.com> <7mo58v$s1g$1@news.igs.net>`

```
donald tees wrote:
> 
> The issues involved in going multi-thread are really no different than the
…[21 more quoted lines elided]…
> >Jimmy, Calgary AB

Well I did write 'stuff' but that was a loooong while ago on a Radio
Shack Model 16 using RM/COBOOL and Microsoft Xenix. (The company was
taken over by Corporation "X" who sent up an analyst to have a look at
the system. The office staff told me he was quite impressed with what
one person had achieved on a clunker like Radio Shack).

From a 'systems' point of view I question that my end-user needs to go
multi-thread. He operates away from base 500-600 miles north of Calgary
out in the boonies at isolated oil/gas plants, and although Calgary is
extremely high-tech, even cell phones don't perform well in the vast
North. About a year ago he mused about bouncing data from his PC in his
van, via satellite, to his home office in Calgary - he was serious.

With that kind of tecchie I'm sometimes asked to make PCs do cartwheels.

Essentially I've designed the current application so that he can access 
and edit "description files" from the Class/Program he is using without
needing to start up another thread. However, he could be editing for
Client A and at the same time want to create a thread which allows him
to print reports for Client B - and then as an afterthought he will want
to do some editing for Client B. Generally speaking he would be
accessing data files particular to a Client, although there are four
'generic' files applicable to all clients.

If it really is parallel to multi-user - then maybe it's no big deal
when I scrape the rust from my memory.

PS. Wasn't deliberate - Corporation "X" - big chemical corporation, the
name is on the tip of tongue - they had that misfortune in Bhopal,
India.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

_(reply depth: 8)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mppt1$sko$1@news.igs.net>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net> <3789CF92.C2088D83@merant.com> <7mlako$5vm$1@hyperion.mfltd.co.uk> <378F5CA1.643880B2@home.com> <7mo58v$s1g$1@news.igs.net> <378FA695.8C58236F@home.com>`

```

James J. Gavan wrote in message <378FA695.8C58236F@home.com>...

>If it really is parallel to multi-user - then maybe it's no big deal
>when I scrape the rust from my memory.
>ETC.

It sounds just the opposite of the type of thing I am doing, but the
multiple user issues are the same.  One of my typical systems has a single
user running six-seven CPU's.  Each is a separate but simultaneous process,
running in real time.

From a systems point of view, each process runs as an semi-invisible user on
a central data base.  However, the central data base is simply a common disk
area.  All the machines are within 5 feet of each other, and only the
sensors extend out into the field.  The one exception to that is short range
Ethernet-radio to the PC's mounted in moving equipment.

If you think of that model, though, the concept is identical to running two
threads. Each computer using the central data-base happens to have it's own
CPU. Threading just emulates that on a single CPU.

Once you start a second Thread, you have two Cobol programs running at once
in a common data space.
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

_(reply depth: 6)_

- **From:** "ber" <barry.rosetti@merant.com>
- **Date:** 1999-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mocgu$h2q$1@hyperion.mfltd.co.uk>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net> <3789CF92.C2088D83@merant.com> <7mlako$5vm$1@hyperion.mfltd.co.uk> <378F5CA1.643880B2@home.com>`

```
>Concentrating on getting my app finished I haven't even considered
>multi-thread at this stage. Can you recommend any generalised document
>that covers 'How to...." and the issues involved in going multi-thread ?

Well, yes, the "Multi-threaded Programming" Programmers Guide on Net
Express and Server Express is a decent introduction.  To warn you, though,
I've been told it gets a bit heavy, a bit quickly (IMHO that's the nature
of the beastie).  If you don't have Net Express or Server Express you
don't have to worry about it because you can't do it :-)) (well actually
you can write multi-threaded programs with one other product I know, but
your execution overhead is enourmous).
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-07-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<378FB1D7.1937CF55@home.com>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net> <3789CF92.C2088D83@merant.com> <7mlako$5vm$1@hyperion.mfltd.co.uk> <378F5CA1.643880B2@home.com> <7mocgu$h2q$1@hyperion.mfltd.co.uk>`

```
ber wrote:
> 
> >Concentrating on getting my app finished I haven't even considered
…[9 more quoted lines elided]…
> your execution overhead is enourmous).

I'm using NetExpress Version 3, but -

 > I've been told it gets a bit heavy, a bit quickly ......

Tha'ts why I asked ! Same with the 'Bible' I have to read to put the 
finished package together (Redistribution), to send to the user.

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Threads and NetExpress- Unresolved external

- **From:** Stephen Gennard <stephen.gennard@merant.com>
- **Date:** 1999-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3789F49B.D8F0944B@merant.com>`
- **References:** `<7m246l$vti$1@nntp9.atl.mindspring.net> <7m2kpv$r9f$1@hyperion.mfltd.co.uk> <7m59ct$snl$1@nntp3.atl.mindspring.net> <378630F8.72BB6511@merant.com> <7m5ju2$rt4$1@nntp9.atl.mindspring.net>`

```
Hi Ken,

I have just spoken to the compiler group and asked them about
this issue.  I was told to inform you that a  RPI has been
raised to cover this issue.  The RPI number is : 516420 (Sev 1).

The checker guys are not happy with the code generated for this
syntax and would recommend you get a fix for the issue or use 
the appropriate CBL_ threading calls.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
