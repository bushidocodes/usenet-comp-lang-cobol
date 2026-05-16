[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Open UNIX Command Line From Within MF Server Express

_1 message · 1 participant · 2005-05_

---

### Open UNIX Command Line From Within MF Server Express

- **From:** "Chris" <ctaliercio@yahoo.com>
- **Date:** 2005-05-10T13:25:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1115756711.616046.132870@o13g2000cwo.googlegroups.com>`

```
Hi all.

Quick info: MF Server Express 4.0 SP1 running on HP-UX 11i.

I have a small problem. I need to open an single interactive UNIX shell
from within my COBOL application. The key word here is SINGLE.

If I code the following into my app:

call
  "SYSTEM"
using
  "${SHELL} -o vi"
& x"00"
end-call

I get what I am looking for - an interactive UNIX shell process. But,
it is actually secondary to the shell process that is created by the
intial call to "SYSTEM". So, I changed it to this:

call
  "SYSTEM"
using
  "exec ${SHELL} -o vi"
& x"00"
end-call

Now I get very close to what I am looking for - which is a single child
shell process relative to the COBOL application. So far so good - but
here comes a BIG wrinkle ...

I have the ENV environment variable set, which is necessary in order to
have the proper environment in the child shell process. The problem is,
the ENV gets executed twice - once for the call "SYSTEM" and another
time for the "exec ${SHELL} ..." that I am passing along. This is bad
because the ENV script is incrementing counters and doing some other
stuff that is rather lengthy. The associated problems with having it
execute twice are quite burdensome.

So - I came up with this final tweak:

display "ENV" upon environment-name
display spaces upon environment-value

call
  "SYSTEM"
using
  "export ENV=mystuff.env; exec ${SHELL} -o vi"
& x"00"
end-call


I'm thinking this is rather clumsy, and perhaps I am overlooking
something obvious. Does anybody have any better suggestions for a
"cleaner" way to accomplish this?

Thanks in advance!

Chris
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
