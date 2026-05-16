[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Telecommuter woes

_1 message · 1 participant · 1999-12_

---

### Re: Telecommuter woes

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rec52LAOTXW4IwjP@rcav8r.demon.co.uk>`
- **References:** `<38568a79$0$16152@fountain.mindlink.net>`

```
In article <38568a79$0$16152@fountain.mindlink.net>, Robert
Annandale <snarfle99@hotmail.com> writes
>Hello,
>
>To those of you who have Linux/AcuServer experience
>I appeal to you for help.
>

Robert,

Have you contacted Acucorp support with your problem (we're
usually pretty friendly!). 

You might want to try starting Acuserver with the command:

acuserve -start -le /tmp/trace.log -t3

This will give you a trace (in /tmp/trace.log) of all attempted
accesses. Be aware that it can generate a *lot* of information, so
be prepared to restrict access while you test the remote
accesses. The trace should give you as clue as to what is going
on. If not then forward the trace (with a problem description) to
<support@acucorp.com>. They will either deal with the problem
directly or forward it to the appropriate place.

If you don't get what you need this way (and I really believe you
will), please feel free to email me (neaton@acucorp.com) and I
will do my best to sort the problem out.

Please note that 'reply to' on this message will hit my private email
address which gets monitored sporadically. 'Join Acucorp and
see the world' they said. They were not kidding........   ;^)


Best regards

Nigel
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
