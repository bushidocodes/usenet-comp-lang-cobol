[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can you wakeUp cobol please?...

_11 messages · 6 participants · 2005-02_

---

### Can you wakeUp cobol please?...

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-21T13:36:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com>`

```
Hello everyone,

I have catch-22 dilemma and need your kind help, again.  I made
a simple graphical window program I will call "Parent", the parent
will launch a console-window (characterBase) program I will call
"child", by using the win32 API "CreateProcess" function, and will
Wait for this program INFINITELY by using the win32 API function
"WaitForSingleObject", until it returns control back to the parent.

the child needs to send a message to the parent during its active
execution time  and request a service operation, for example:
(generate & sort a text file, or launch a GUI-Graphical Program).
however, when the child is active --- the parent is hibernating in
the background in its waiting-state, until it receives the return
code from the child program along with the returned OS control.

My Dilemma? how can I wakeup the parent to respond to the message
it will receive from the child while keeping the status quo??

the workaround is for the child to exit with a special ReturnCode,
and have the parent respond to that request accordingly, and then
the parent would Re-Launch back again the child program so it can
continue its Previous Process --- however, when the child gets
Re-Launched, the end-user will not be able to pickup from where
he or she leftoff the last operation with the child.  Also, Only
the parent program is capabl of launching a Graphical Window
program by using the win32 API "CreateProcess" function.

I am hoping that you have a wakeup call for cobol or me.
thanks a lot for the generous help, Kellie.
```

#### ↳ Re: Can you wakeUp cobol please?...

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-21T13:42:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109022179.254443.235370@g14g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com>`

```
> (generate & sort a text file, or launch a GUI-Graphical Program).

Perhaps you should make those separate callable programs that can be
called by either the parent or by the child.
```

##### ↳ ↳ Re: Can you wakeUp cobol please?...

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-21T14:07:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109023679.089341.194510@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1109022179.254443.235370@g14g2000cwa.googlegroups.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com> <1109022179.254443.235370@g14g2000cwa.googlegroups.com>`

```
if the callable program is a GUI-program like a
ListView window, the child is NOT capable of
calling or launching it either.
Kellie.
```

###### ↳ ↳ ↳ Re: Can you wakeUp cobol please?...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-21T22:23:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WbtSd.34738$by5.23361@newssvr19.news.prodigy.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com> <1109022179.254443.235370@g14g2000cwa.googlegroups.com> <1109023679.089341.194510@c13g2000cwb.googlegroups.com>`

```
"Kellie Fitton" <KELLIEFITTON@YAHOO.COM> wrote in message
news:1109023679.089341.194510@c13g2000cwb.googlegroups.com...

> I made a simple graphical window program I will call "Parent", the parent
>will launch a console-window (characterBase) program I will call
>"child", by using the win32 API "CreateProcess" function, and will
>Wait for this program INFINITELY by using the win32 API function
>"WaitForSingleObject", until it returns control back to the parent.

>the child needs to send a message to the parent during its active
>execution time  and request a service operation, for example:
…[3 more quoted lines elided]…
>code from the child program along with the returned OS control

[added later] [but you shouldn't have, because this is absolutely possible.
Not too wise, but 'do-able' nonetheless]
> if the callable program is a GUI-program like a
> ListView window, the child is NOT capable of
> calling or launching it either.

The parent program must be multi-threaded: One thread to do nothing but
launch the child and wait for it to complete; one thread to service requests
(which I would trigger with named event, also in a WaitForSingleObject or
WaitForMultipleObjects Loop); and of course, your main thread servicing the
parent's GUI window(s), which must be disabled during the execution of the
child process. You can, of course, have the main thread of 'parent' handle
the service requests, but that gets a little trickier (you need to use a
MsgWaitForMultipleObjects loop isnteaqd of a 'standard' Windows message
loop, call, or arrange for the child to do virtual allocation of memory in
the parent's address space), so let's forget about those options when
multi-threading  is available.

Or, take the easy way out: instead of using CreateProcess to launch another
program, write the 'child' program as a DLL and just call it from within the
process space of 'parent.'  No muss, no fuss, no bother. Control is sure a
lot easier this way (service requests become a simple CALL). .

If your compiler does not support multi-threaded programs and/or creation of
dynamic link libraries, uh, er, not sure what to do next, except perhaps (he
shamelessly added) ..If you really need this, I can create something like
this on a professional basis.
```

###### ↳ ↳ ↳ Re: Can you wakeUp cobol please?...

_(reply depth: 4)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-21T15:20:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109028054.544972.327560@l41g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<WbtSd.34738$by5.23361@newssvr19.news.prodigy.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com> <1109022179.254443.235370@g14g2000cwa.googlegroups.com> <1109023679.089341.194510@c13g2000cwb.googlegroups.com> <WbtSd.34738$by5.23361@newssvr19.news.prodigy.com>`

```
I will try to create the console-program as a .dll module and see if
the parent will
wait for it to complete its job first, before it goes back and reclaim
the control.
thanks a lot for the wakeUp call, Kellie.
```

###### ↳ ↳ ↳ Re: Can you wakeUp cobol please?...

_(reply depth: 4)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-21T19:34:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109043245.791839.246970@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<WbtSd.34738$by5.23361@newssvr19.news.prodigy.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com> <1109022179.254443.235370@g14g2000cwa.googlegroups.com> <1109023679.089341.194510@c13g2000cwb.googlegroups.com> <WbtSd.34738$by5.23361@newssvr19.news.prodigy.com>`

```
Hello Michael,

in case you are wondering about the cobol wakeUp call:
when I compiled the file (child) as a .DLL file, the Net Express
cobol compiler was NOT able to resolve the entry-point call and gave
me an error messgae that said :
"error LNK2001:unresolved external symbol DisplayAboutScreen@4"
and when I included the file (child) in the cobol project and compiled
it as an .OBJ file, the entry-point call was resolved fine ---
However,
the parent program did NOT wait for the child to complete it job first,
before it re-claimed control back from the call to the child. So, I am
back to square one with the win32 API "CreateProcess" function. In
this case here, I need the parent to wait for the child until the end
of its job cycle ---  and just like I said before,  its a catch-22. :-)

thanks a lot, Kellie.
```

###### ↳ ↳ ↳ Re: Can you wakeUp cobol please?...

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-02-22T14:10:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y3HSd.35076$by5.33733@newssvr19.news.prodigy.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com> <1109022179.254443.235370@g14g2000cwa.googlegroups.com> <1109023679.089341.194510@c13g2000cwb.googlegroups.com> <WbtSd.34738$by5.23361@newssvr19.news.prodigy.com> <1109043245.791839.246970@f14g2000cwb.googlegroups.com>`

```
"Kellie Fitton" <KELLIEFITTON@YAHOO.COM> wrote in message
news:1109043245.791839.246970@f14g2000cwb.googlegroups.com...
> Hello Michael,
>
…[12 more quoted lines elided]…
> of its job cycle ---  and just like I said before,  its a catch-22. :-)

Since I don't know the compiler, I could be way off base here, but.....

If you were able to link the DLL, either at compile time (an OBJ file
handled by the linker) or at program load time (the way the Windows system
DLLs are linked), then you don't need any "WaitFor" functions except if you
call an external process (another EXE) from somewhere... the ENTRYs in your
DLL are simply called with a CALL statement and your program WILL NOT
continue until that called procedure (ENTRY) has completed.

If the procedure in your DLL is in turn calling other ENTRYs in your 'main'
code, the same rule applies.

Therefore, if you have some code continuing when it shouldn't, it's because
it's coded that way. How you'd code that is unknown to me because AFAIK that
can't be done. (Unless you are calling an external with CreateProcess and
not waiting for it?).

I mean your entire program should be something like

 * MAIN
  MAIN.
      Other stuff
      ......
      CALL   My-Entry-in-my-dll  USING whatever RETURNING whatever
     .....

      EXIT PROGRAM or GOBACK or however you end a program

====
* DLL
  ENTRY My-ENTRY-In-my-dll
    USING  whatever
    yadda, yadda
   * ***************************
   * call an entry in main module
   * *************************
   CALL ENTRY-IN-MAIN USING whatever
   do other stuff
   * ***************************
   * call external program
   * *************************
   Call CreateProcess (parameters)
   Call WaitForSingleObject (process handle returned in ProcessInformation
Structure parameter passed to createProcess).


But as I said, I don't know the compiler, and I am not sure how OBJ files
are handled. Someone else here will know that. But the above is a 'generic'
program using a DLL, calling both external programs and ENTRYs in the
'parent' (in this case 'parent' is a misnomer) program..

This DOES assume that MAIN is compiled with correct options and properly
written to avoid any reentrancy problems.

MCM
```

###### ↳ ↳ ↳ Re: Can you wakeUp cobol please?...

_(reply depth: 6)_

- **From:** "Kellie Fitton" <KELLIEFITTON@YAHOO.COM>
- **Date:** 2005-02-22T11:21:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109100072.896886.253890@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<y3HSd.35076$by5.33733@newssvr19.news.prodigy.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com> <1109022179.254443.235370@g14g2000cwa.googlegroups.com> <1109023679.089341.194510@c13g2000cwb.googlegroups.com> <WbtSd.34738$by5.23361@newssvr19.news.prodigy.com> <1109043245.791839.246970@f14g2000cwb.googlegroups.com> <y3HSd.35076$by5.33733@newssvr19.news.prodigy.com>`

```
Hello,

thanks a lot for All the feedback and the great help from everyone.

I have found a win32 API at the MSDN that will wakeUp cobol with
a jolt of a large cappuccion --- it looks devilishly clever to solve my
catch-22 dilemma. Below is the code that I need to work with.

Regards, Kellie.

*>--- source code  ------>*

   call winapi "CreateSemaphoreA" using
           by value 0 size 4
           by value 4 size 4
           by value 4 size 4
           by reference lpszReadSem
        returning       hSemRead
    end-call.

    call winapi "OpenSemaphoreA" using
          by value     SEMAPHORE-ALL-ACCESS
          by value     0 size 4
          by reference lpszReadSem
        returning      hTmpSemRead
    end-call.

    call winapi "GetCurrentThreadID"
        returning dwParentThreadId
    end-call.

    set ChildThreadProc to entry "ChildThreadProc"
    call winapi "CreateRemoteThread" using
          by value     hRemoteProcess
          by value     0 size 4
          by value     0 size 4
          by value     ChildThreadProc
          by value     0 size 4
          by value     0 size 4
          by reference dwChildThreadId
        returning        hChildThread
    end-call.

   entry "ChildThreadProc" winapi.
   ...................
   ...................

   exit program returning 0.

   call winapi "ReleaseSemaphore" using
          by value hSemRead
          by value 1 size 4
          by value 0 size 4
       returning   return-code
   end-call.

   call winapi "CloseHandle" using
          by value hTmpSemRead
       returning   return-code
   end-call.

*>-------   end   ----------*>
```

###### ↳ ↳ ↳ Re: Can you wakeUp cobol please?...

_(reply depth: 7)_

- **From:** epc8@juno.com
- **Date:** 2005-02-22T11:53:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1109101989.433629.204580@c13g2000cwb.googlegroups.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com> <1109022179.254443.235370@g14g2000cwa.googlegroups.com> <1109023679.089341.194510@c13g2000cwb.googlegroups.com> <WbtSd.34738$by5.23361@newssvr19.news.prodigy.com> <1109043245.791839.246970@f14g2000cwb.googlegroups.com> <y3HSd.35076$by5.33733@newssvr19.news.prodigy.com> <1109100072.896886.253890@z14g2000cwz.googlegroups.com>`

```

Kellie Fitton wrote:
> Hello,
>
…[3 more quoted lines elided]…
> a jolt of a large cappuccion --- it looks devilishly clever to solve
my
> catch-22 dilemma. Below is the code that I need to work with.
>
> Regards, Kellie.
>

I'd still go with experience (Michael Mattias) vs the manual (MSDN).
Why go out of process when in-process is so much simpler? For example
in Fortran, CALL SYSTEM(command_string) waits until the command
specified finishes before resuming execution. Which makes it, in
effect, a rather large subroutine call!
```

#### ↳ Re: Can you wakeUp cobol please?...

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2005-02-21T23:43:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<smuSd.459318$Xk.415848@pd7tw3no>`
- **In-Reply-To:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com>`

```
Kellie Fitton wrote:
> Hello everyone,
> 
> I have catch-22 dilemma and need your kind help, again.

You sure pick 'em :-). As you are comfortable with APIs, no doubt you 
will follow Michael's suggestions.

Could be done with OO, using just bare bones class syntax, passing 
object handles between the two programs(classes), so that on given 
'events' (i.e. your own defined exit/swap point), each program object 
could invoke the other, back and forth, back and forth......., until 
your final 'EXIT' - triggered by either program.

Jimmy
```

#### ↳ Re: Can you wakeUp cobol please?...

- **From:** Adrien Plisson <aplisson-news@stochastique.net>
- **Date:** 2005-02-22T10:11:04+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<421af728$0$23955$ba620e4c@news.skynet.be>`
- **In-Reply-To:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com>`
- **References:** `<1109021784.833317.81710@f14g2000cwb.googlegroups.com>`

```
Kellie Fitton wrote:

> Hello everyone,
> 
…[5 more quoted lines elided]…
> "WaitForSingleObject", until it returns control back to the parent.
[snip]

don't use WaitForSingleObject. instead try MsgWaitForMultipleObject: 
it is the same as WaitForMultipleObject but also returns if their is 
an event in the message queue. this way, your child program can send a 
message to the parent and should be able to wake it up.

(the actual implementation is left as an exercise for the reader)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
