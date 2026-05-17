[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ANSI display statement (MF/Unix)

_2 messages · 2 participants · 1995-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### ANSI display statement (MF/Unix)

- **From:** "b..." <ua-author-3811534@usenetarchives.gap>
- **Date:** 1995-12-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4aj7nt$e8b@tyndall2.tyndall.com.au>`

```
In a nutshell, I am having a little difficulty with the way the ANSI
display statement is implemented by MF on a Unix box and was wondering
if there was any way to modify the behaviour. Consider:

display somevar "text2" someothervar.

Assuming that somevar & someothervar were defined as, say pic x(5) and
contained "text1" and "text3" respectively, I would expect to see

text1text2text3

followed by a newline output to the stdout. I do, but I would have
thought that this would be implemented as:

write(1, "text1text2text3\n", 16);

What is _actually_ happening is:

write(1, "text1", 5);
write(1, "text2", 5);
write(1, "text3", 5);
write(1, "\n", 1);

``So what?'' I hear you say. Well the output of the application is
not a terminal, stdout has been redirected to a named pipe - at the
other end of which is a process that manipulates the data then stuffs
it down an X.25 circuit. Multiple copies of the application are
writing to the same pipe, with each output line prefixed by an
identifier unique to that invocation, so the server can sort out what
has to be done with each line. Writes are atomic, so if the whole line
is output in one statement, it is not a problem ... but this piece-meal
output is allowing lines to intermix.

Note that even if you only display one variable, the newline is still
written seperately.

As a temporary work-around, I have piped the output through a kludge
which puts the lines together before they reach the named pipe.

I could of course, re-write the application to open the pipe directly
and use write instead of display, or stuff all the fields into one
variable with an embedded newline (x"0a") at the end and display with
no advancing, but if it is a simple matter of a compile- or run-time
switch, that would be _lots_ more appealing.

Regards,
Brendan O'Dea                                         b.··.@tyn··m.au
Compusol Pty. Limited                   (NSW, Australia)  +61 2 809 0133
```

#### ↳ Re: ANSI display statement (MF/Unix)

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1995-12-16T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dc4dad480c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4aj7nt$e8b@tyndall2.tyndall.com.au>`
- **References:** `<4aj7nt$e8b@tyndall2.tyndall.com.au>`

```
b.··.@tyn··m.au (Brendan O Dea) wrote:

› In a nutshell, I am having a little difficulty with the way the ANSI
› display statement is implemented by MF on a Unix box and was wondering
› if there was any way to modify the behaviour.  Consider:
 
›    display somevar "text2" someothervar.

many cobols have the DISPLAY text WITH NO ADVANCING.....
check it out
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
