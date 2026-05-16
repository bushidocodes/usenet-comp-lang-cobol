[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Postscript

_1 message · 1 participant · 2004-11_

---

### Re: Postscript

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-11-09T15:26:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2vao75F2ih7gdU1@uni-berlin.de>`
- **References:** `<kt3vo0hfase0ju3qt62rtk5pbg3bg5f72s@4ax.com>`

```
Alain,

you have received good responses to your post. I'll simply add a couple of
cents worth.

see below...

<Alain Reymond> wrote in message
news:kt3vo0hfase0ju3qt62rtk5pbg3bg5f72s@4ax.com...
> Hello,
>
> I have been trying to find a library to make the production os
> postscript file easier from our cobol programs.
>

Richard has a valid point when he says this is best done outside of COBOL.
There is much merit in using "layered software" and the production of actual
output (whether to a screen,  a printer, a microfiche, or a T-shirt...)
should properly be another tier in the system design (software or hardware).

However, Jimmy has also made some good points for actually doing what you
propose, and he has carefully covered differences you may encounter in
different OO compilers. I endorse his basic statement that it is really
important to keep this kind of code NEUTRAL.

> Finally, I have begun to write a library in OO cobol largely inspired
> from the C pslib library. I have just finished to prepare the
> interface of the different methods and write a few methods.
>

Richard asked whether you were simply wrapping the C PSLib as OO COBOL or
re-inventing it. From the above its would appear you are re-inventing it. I
don't personally think that is wrong; sometimes things need to be
re-invented (although I don't use PS enough to be in a position to comment
on that specifically), but even if it is redundant you want to do it and the
learning experience alone may justify doing it. If you then share that
experience with everyone, I can't see how anybody is the poorer for it.

> Teh generation of postscript file could then be:
> invoke PSDoc "PSOpenFile" using z"myfile.ps"
…[6 more quoted lines elided]…
>

It is certainly easier to read for an OO COBOL programmer...

> I thought that it might be an interesting project for an open source
> library in cobol.

Yes, certainly.

>There are too few projects for the most used
> programming language in the world.
>
Er... what world do you live on <G>?  This statement was true 40 years ago,
today COBOL is not even in the top three...

> This is just an mail to see if anyone would be interested before
> placing it on the web.
>
It's a good project... go for it.

Best of Luck,

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
