[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do I disable Ctrl+C and Ctrl+Break in MS COBOL 5.0?

_2 messages · 2 participants · 2001-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How do I disable Ctrl+C and Ctrl+Break in MS COBOL 5.0?

- **From:** "Leo Elsenberg" <elsenberg@t-online.de>
- **Date:** 2001-05-02T09:17:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9coc8b$4js$07$1@news.t-online.com>`

```
Could someone explain how one disables the Ctrl+C and Ctrl+Break keys in a
COBOL program. I am using Microsoft COBOL 5.0. I have tried Adiscf and
Keybcf, but no success. The sample program found in the MS COBOL 5.0 System
Reference, pages 42-46, does not seem to explain the problem fully.
```

#### ↳ Re: How do I disable Ctrl+C and Ctrl+Break in MS COBOL 5.0?

- **From:** "Steven O. Ellis" <soellis@soltec.net>
- **Date:** 2001-05-03T19:17:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AF1F537.302884D4@soltec.net>`
- **References:** `<9coc8b$4js$07$1@news.t-online.com>`

```
Alister seems to have covered it, for the MS compiler.

I just ran into the same type of problem running RM/COBOL on AIX.  I
wanted not to disable, but to capture Ctrl-C when firing off a system
call.  I wanted to know if the user pressed Ctrl-C while the system
command was executing.  No go.  I even put in a work request with Liant
Software, and they agreed that the return code was not getting picked up
by RM/COBOL on AIX, when the user presses Ctrl-C during a system call.

RM/COBOL always sees the return code from a UNIX script, however, so
coded my COBOL program to create a temporary script on the fly and then
fire off a system call to execute the script.

I got it to work, but the time investment testing the nonworking
function before I coded the work-around was considerable.  :(

Steven


Leo Elsenberg wrote:
> 
> Could someone explain how one disables the Ctrl+C and Ctrl+Break keys in a
> COBOL program. I am using Microsoft COBOL 5.0. I have tried Adiscf and
> Keybcf, but no success. The sample program found in the MS COBOL 5.0 System
> Reference, pages 42-46, does not seem to explain the problem fully.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
