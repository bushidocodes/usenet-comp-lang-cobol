[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CreateProcess WIN32API Part 3

_3 messages · 2 participants · 2000-06_

---

### CreateProcess WIN32API Part 3

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2000-06-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000619163905.11814.00002283@ng-fs1.aol.com>`

```
Good Afternoon,

I am using the CreateProcess API to run a MS-DOS batch (BAT) file.  The system
executes the batch file fine, but does not shut down the window that gets
created to run the batch file.  Once I shut the window down processing
continues as normal.  Does anyone know of a way to tell the CreateProcess API
to close a MS-DOS window when the command have been completed ?

Thanks,
Bob Hennessey
```

#### ↳ Re: CreateProcess WIN32API Part 3

- **From:** "David Sands" <davs@mfltd.co.uk>
- **Date:** 2000-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8injc2$n8m$1@hyperion.mfltd.co.uk>`
- **References:** `<20000619163905.11814.00002283@ng-fs1.aol.com>`

```
Hi Bob,

By default Win9x will leave the console on the screen to see any message.
If you want to make sure it closes then use some code along the lines of:-

           move z"command.com /C batchfile.bat" to executable
      * We create the process
           call WINAPI CreateProcess using
               by value 0 size 4,
               by reference executable,
               by value 0 size 4,
               by value 0 size 4,
               by value 0 size 4,
               by value CREATE-DEFAULT-ERROR-MODE,
               by value 0 size 4,
               by value 0 size 4,
               by reference StartupInfo,
               by reference ProcessINFO
               returning ws-Okay
           end-call

The /C switch makes sure that the window is closed.

Regards
David.

Bob7536 <bob7536@aol.com> wrote in message
news:20000619163905.11814.00002283@ng-fs1.aol.com...
> Good Afternoon,
>
> I am using the CreateProcess API to run a MS-DOS batch (BAT) file.  The
system
> executes the batch file fine, but does not shut down the window that gets
> created to run the batch file.  Once I shut the window down processing
> continues as normal.  Does anyone know of a way to tell the CreateProcess
API
> to close a MS-DOS window when the command have been completed ?
>
> Thanks,
> Bob Hennessey
```

##### ↳ ↳ Re: CreateProcess WIN32API Part 3

- **From:** bob7536@aol.com (Bob7536)
- **Date:** 2000-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000620082309.00143.00003089@ng-co1.aol.com>`
- **References:** `<8injc2$n8m$1@hyperion.mfltd.co.uk>`

```
Hi David,

Thanks for the help I will give that a try.

Bob Hennessey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
