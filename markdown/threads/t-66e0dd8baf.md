[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Stop Run?

_3 messages · 2 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Stop Run?

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uof4c$hou$1@news.igs.net>`

```
This is probably a really stupid question, but how do
you stop a Version 4 PowerCobol program?  The
standard "stop run" gives an error message,
that it is illegal, though it does stop.  I have tried
invoke the "terminate" method of the main form,
and that does not seem to work.  I have tried to
call "CLOSESHEET" of the main form, no luck. I have
scanned the documentation for "stop" "end" "close"
"run", etc, and cannot seem to find a method that
terminates a program.  I just want to abort the damned
thing after an error.
```

#### ↳ Re: Fujitsu Stop Run?

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361028A8.E5968591@mindspring.com>`
- **References:** `<6uof4c$hou$1@news.igs.net>`

```
EXIT PROGRAM?  it's what i use.  STOP RUN made fsc 3.0 hurl on me too
```

##### ↳ ↳ Re: Fujitsu Stop Run?

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uq5ih$9c9$1@news.igs.net>`
- **References:** `<6uof4c$hou$1@news.igs.net> <361028A8.E5968591@mindspring.com>`

```

skidmike wrote in message <361028A8.E5968591@mindspring.com>...
>EXIT PROGRAM?  it's what i use.  STOP RUN made fsc 3.0 hurl on me too

No, exit program is a subroutine exit.  In a code fragment (a
GUI event), it only exits from the event.  It does not abort the
entire program.  I did eventually discover the problem -- the
correct command was what I tried first:
INVOKE "Terminate" OF MAINFORM.

However, the manual shows it as
INVOKE "Terminate" USING form RETURNING ERROR.

Now, the interesting thing is that if you call it with an error
return, it fails and returns no error. (IE-it returns, and it should
not, as it is supposed to end the program).  However, if you
omit the RETURNING clause, it never returns, which is
correct.  Go figure.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
