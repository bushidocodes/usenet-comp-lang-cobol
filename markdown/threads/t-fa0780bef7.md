[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# pause execution for screen update

_3 messages · 3 participants · 1999-02_

---

### pause execution for screen update

- **From:** "don ferrario" <don@ferrario.com>
- **Date:** 1999-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a4c30$h4j$1@news1.epix.net>`

```
PowerCobol again...

Subprogram is in a loop, possibly reading through
thousands of records in a search.  Results are to be
written to screen elements as the search finds them.

PROBLEM:  So long as the subprogram is executing,
the screen is not updated.  The results are not shown
until the search is totally completed.

QUESTION:  Is there something analagous to a PAUSE
statement, that will interrupt the loop, allow the display to
be updated, and then return to the loop?  The PAUSE
could be executed every so-many interations of the loop,
as desired.

I remember from my limited exposure to VisualBasic there was
something like this.  It was important because the program
wouldn't check for any other events until the loop was finished.

A typical example of the need would be to offer the user a "cancel"
button to end the search before completion, if needed.

don ferrario
http://www.ferrario.com/don
```

#### ↳ Re: pause execution for screen update

- **From:** "John Hicks (Remove \\"nospam\\" from address before replying)" <johnhicks@ibm.net>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36CA5A2A.2C558F78@ibm.net>`
- **References:** `<7a4c30$h4j$1@news1.epix.net>`

```
A don't know about PowerCobol, but the general way is to periodically
call your operating system to check for keyboard input. You probably
don't want to do this with each iteration of your loop since such calls
add a lot of overhead, so you can set up a counter and do a call every
100 or 1000 iterations. The MS-DOS call is Int 21h AH=0Bh. Your compiler
probably has a standard call for all operating systems.

--John

don ferrario wrote:
> 
> PowerCobol again...
…[23 more quoted lines elided]…
> http://www.ferrario.com/don
```

#### ↳ Re: pause execution for screen update

- **From:** "Gary Roush" <gkr@adtools.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7adurf$rmt$1@remarQ.com>`
- **References:** `<7a4c30$h4j$1@news1.epix.net>`

```
Don,

If you're using Version 4 of PowerCOBOL, there is a "timer" feature that you
can incorporate to your form.  You can then tell this timer what you want to
use the time for and when.  Works quite well.   For example, you want the
timer to check something every ten seconds. You install the timer, and then
insert code that you want to be done. Use the code there to do some checking
and then return control back to what you're doing.

Gary Roush
Fujitsu COBOL support

don ferrario wrote in message <7a4c30$h4j$1@news1.epix.net>...
>PowerCobol again...
>
…[24 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
