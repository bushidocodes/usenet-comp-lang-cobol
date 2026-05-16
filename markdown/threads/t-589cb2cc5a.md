[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Succesful Status code (was: Request for testing of Reltive File status

_1 message · 1 participant · 2009-05_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Re: Succesful Status code (was: Request for testing of Reltive File status

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2009-05-19T16:18:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4A12DBE8.6F0F.0085.0@efirstbank.com>`

```
>>> On 5/18/2009 at 12:37 PM, in message
<8%hQl.291402$Za7.196706@en-nntp-08.dc1.easynews.com>, William M.
Klein<wmklein@nospam.ix.netcom.com> wrote:
> The most common  non-"00" code that you might get on an OPEN; is "05" if 
> you 
…[6 more quoted lines elided]…
> world of CBLQDA(ON) - where files are "created" when there isn't a JCL DD

> for 
> them.  This is such a *HATED* (but required by the Standard) behavavior, 
…[7 more quoted lines elided]…
> many IBM mainframe shops would want.

Never before having heard ot CBLQDA(ON) I tried it out.  Umm, interesting.

It could be useful for a temporary file that, within the same jobstep
(program) you open for output, write to it, close, then open for input and
read it.  But what is the default space allocation?

Another thing I find interesting is with a regular temporary file
(DISP=(NEW,DELETE)) you get something like this:
IGD105I SYS09139.T160846.RA000.CBLQDA.R0101298       DELETED,  
DDNAME=MYFILE

But for the dynamically allocated file there is no such message, and yet the
file appears to be deleted anyway.

What would perhaps be more useful is if you could (following the 2002
standard) say something like 
SELECT MY-FILE ASSIGN USING MY-FILE-NAME.

77  MY-FILE-NAME PIC X(50).

MOVE 'FJS.MY.FILE' TO MY-FILE-NAME
OPEN OUTPUT MY-FILE

Of course even there I don't know how you would assign the proper DISP,
so...

I know that there is some way in Enterprise Cobol to do something like this
using an "environment variable".  I have not yet tried it.

Frank
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
