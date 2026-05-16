[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WinAPI Sleep function solved - Thanks to all.

_1 message · 1 participant · 2003-08_

---

### WinAPI Sleep function solved - Thanks to all.

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-08-22T12:27:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f456442_4@news.athenanews.com>`

```
Due to the fantastic help from you guys I was able to solve this and it
didn't hurt as much as I thought it would <G>.

Here is the comedy of errors and the solutions:

1. PROBLEM: Trying to compile and link a Fujitsu NETCobol V6.1 CGI program
that is a main program with 5 nested subprograms, I received a message from
the Linker regarding an unresolved external reference on the WinAPI function
"Sleep", which was used in the main program.

ATTEMPTED SOLUTION:  Dimly recall from previous experience with the WinAPI
that the Fujitsu ALPHAL(WORD) option needs to be set. Set it (after
grappling with the Fujitsu IDE that has help in pidgin English and is not
always clear or intuitive when you want to do things that deviate from the
defaults) for the Main program and recompiled. Disaster! Hundreds of knock
on errors from COPY books not found.

Under pressure to get this working, post to CLC and comment out the Sleep
function.

Responses are all valuable. JerryMouse confirms it works on his system with
ALPHAL(WORD), Bill gives the References that explain what ALPHAL does,
Michael offers to write a .DLL! Other posts correctly identify problem with
Entry point and exports. (I am blown away by the response...sincere thanks
to everybody.)

2. Armed with confidence that it works if ALPHAL(WORD) is used, go back and
address this problem. Used IDE and manually set the ALPHAL(WORD) option AND
the LIB entry to point to my Libraries for the main program. Re-built the
project. Unresolved reference is gone, COPY books are all included, but now
we have a sad message from the Linker saying "Entry point must be
specified..."   No clues... there are 6 programs in this compile and no
indication of WHICH one doesn't contain the required Entry point, or WHICH
required Entry point is not there. (At least the previous message quoted the
SLEEP entry as being problematic.)

Gave up on the IDE as counter intuitive and checked the .CBI file (this
contains the compiler options) directly. Sure enough, the ALPHAL entry was
set to NOALPHAL. Fixed it manually, checked that the LIB entry was intact,
rebuilt the lot, and everything worked fine.

I can only assume that my clumsy attempts with the IDE, setting options for
the main program only, must have blown away the LIB entry  that would point
to the COPY libraries.  (It should be noted that JerryMouse suggested
exactly this as a possible cause of the problem.)  Then, having got that bit
right, I was apparently in conflict with the main COBOL options...

BOTTOM LINE:

Sometimes the development environment is more problematic than the
application.

I have been using the Fujitsu IDE for some years now and, in general, find
it useful. However, when it comes to more esoteric things like changing
options for nested programs, it is not immediately obvious what is required
and the help is irritating and NOT helpful. Who has time to read pages of
documentation (the Fujitsu docs are generally "good"...now) when under
pressure to have something working as quickly as possible?

On-line help needs to be helpful and simple; diagnostic messages need to be
to the point and specific.

And I need to do more homework and take a break occasionally <G>.

Thanks again to all who contributed.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
