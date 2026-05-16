[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# A simple exercise

_4 messages · 2 participants · 2000-09_

---

### A simple exercise

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qi5g5$jhg$1@nnrp1.deja.com>`

```



Hi:

With FILE-STATUS versus DECLARATIVES being the warm topic of the
day, I thought people might do an exercise.

Take any old program which reads a file.

Recompile the program changing the record format somehow.

Remove DECLARATIVES and all FILE-STATUS checks.

Run the program and see what happens. And tell us about it.

THanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: A simple exercise

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qi7hc$lpe$1@nnrp1.deja.com>`
- **References:** `<8qi5g5$jhg$1@nnrp1.deja.com>`

```

> Run the program and see what happens. And tell us about it.
>

Hi:

OK, I've got nothing better to do.

Since I have never written a program without FILE-STATUS in it,
I didn't know quite what to expect.

It terminated with a file-status of 139. (Inconsistent format)

On the other hand, I have experienced strange things with
inconsistent formats which did not produce any errors - program
appeared to run yet produced no output.

Thanks

Tony Dilworth



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: A simple exercise

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-09-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39CF6101.754FE4F7@brazee.net>`
- **References:** `<8qi5g5$jhg$1@nnrp1.deja.com>`

```
Foodman wrote:

> Hi:
>
…[9 more quoted lines elided]…
> Run the program and see what happens. And tell us about it.

Typically nothing would happen (provided you have appropriate AT-END
logic).  These checks are to allow you to handle abnormal conditions.
To test, one needs to supply those abnormal conditions, but one can't
test EVERY abnormal condition.

Sometimes the environment handles most abnormal conditions just nicely -
in this case it might be appropriate to let it.  Sometimes the
programmer wants to handle particular conditions (and then making sure
it aborts normally with unanticipated conditions).

For instance, in a mainframe environment, if a file is protected when a
batch program tries to write to it, or if it has used up the space
allocated for it when you try to write - we usually abort - which is
sufficient to notify the operator and stop dependent jobs from running.
The operator looks at the abort message, then corrects the problem and
follows restart procedures.

In an on-line environment, the user needs to get a message explaining
what is wrong.  If the user can't fix it himself, he  typically makes a
screen print or calls system support with the information required.  If
a Windows based CoBOL program gets a "file not found" error, is it
difficult to pull up Windows routines to locate the appropriate file and
retry?
```

##### ↳ ↳ Re: A simple exercise

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-09-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8qpv2i$6gs$1@nnrp1.deja.com>`
- **References:** `<8qi5g5$jhg$1@nnrp1.deja.com> <39CF6101.754FE4F7@brazee.net>`

```
If a Windows based CoBOL program gets a "file not found" error, is it
difficult to pull up Windows routines to locate the appropriate file and
retry?

Hi:

I think that with SP2, you can get access to the directory. Presumably,
you could then go through the file-names provided looking for
what you wanted. I have never tried this.

In a real application, I don't think you would want to go
searching for a file with the right name, it might have the
right name but the wrong content.

BTW, the reason I made this thread was primarily for Deek, et al.
My impression is that newcomers don't get taught much about
File-Status checks and what can happen in the real world.

I spent some time playing around doing things like moving the
.DAT file from one file to the .DAT file for another. Sometimes,
you get an AT-END, sometimes, the program would read the file
with no problem although the application might bomb out with
a 163 (non-numeric data).

My point is that file-handlers, although very good, are not
totally infallible and that newcomers should be aware of that
fact.

In addition to my obsession with checking file-status, I also
sequence-check sequential files. Years ago, I remember asking
someone to always sequence-check the files they were reading.
One guy refused to do this saying that the file just got sorted
so why bother sequence checking it. Anyway, (this was in the
days when JCL was on cards) one day, they had a jam and a
card containing the sort parameters was incorrectly made over.
This resulted in the sort being incorrect. It also resulted
in the guy's program breaking control on every record with
the result that it skipped to a new page each time. The
oprerators finally realized something was wrong after they
loaded the eleventh box of three-part paper.

Newcomers should not assume that things will be the way that
they are supposed to be because the time will come when they
are not.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
