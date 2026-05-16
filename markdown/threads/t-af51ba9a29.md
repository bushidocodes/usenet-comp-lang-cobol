[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How Can I look for a next event in Dialog System?

_2 messages · 2 participants · 1998-12_

---

### How Can I look for a next event in Dialog System?

- **From:** "Micael Chiampo" <semnet@tin.it>
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74drg6$3of$1@nslave1.tin.it>`

```
Hi,
I have the need to know where the user clicks when I received a LOST-FOCUS
event in DS 3.0.
The best is to know the control that will receive the next event, I can do
this with the pf-get-next-event function in panels v2, but I dont want to
lose the event.
Anyone have suggestions?
Thanks
Micael
```

#### ↳ Re: How Can I look for a next event in Dialog System?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-12-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<366aabbd.393508127@news1.ibm.net>`
- **References:** `<74drg6$3of$1@nslave1.tin.it>`

```
On Sun, 6 Dec 1998 12:57:26 +0100, "Micael Chiampo" <semnet@tin.it>
wrote:

>Hi,
>I have the need to know where the user clicks when I received a LOST-FOCUS
…[6 more quoted lines elided]…
>Micael

My method of handling this is a bit tedious but I never found a better
solution (other than giving up Dialog).

Make sure that the LOST-FOCUS event is coded on EACH object that you
want to test.  Don't code it in the Window (unless you want to test
the window losing focus) or at the Global level - code it on each
object.

Then set a switch.  Move the object handle to a data area or move a
literal (the literal is eaisier to understand and work with - I never
could get integrity with object handles).

I'd be interested in hearing any other solutions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
