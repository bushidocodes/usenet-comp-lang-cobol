[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tables and Moves

_2 messages · 2 participants · 1999-07_

---

### RE: Tables and Moves

- **From:** "Thompson, William" <wthompson@okc.disa.mil>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90491CB93918D21189BD00805FBE300B01442E51@voyager.okc.disa.mil>`

```
Yea, but then it would just have the last length in it.....

-----Original Message-----
From: francois millet [mailto:francois.millet@dial.oleane.com]
Sent: Saturday, July 24, 1999 10:26 PM
To: comp.lang.cobol@list.deja.com
Subject: Re: Tables and Moves


 Message from the Deja.com forum: 
 comp.lang.cobol
 Your subscription is set to individual email delivery

In article <932842906.937363@gorgoroth.esoterica.pt>, Josua S. wrote:
> 
> TBSRC and the table TABLE-SRC are 'filled' with a call to another program.

Here is the problem: the length of the table TABLE-SRC is re-calculated only

when your program (not another program) changes explicitly TBSRC.

I am quite sure that if you insert ADD 0 to TBSRC after your call, all will
be 
fine...






 _____________________________________________________________
 Deja.com: Share what you know. Learn what you don't.
 http://www.deja.com/
 * To modify or remove your subscription, go to
 http://www.deja.com/edit_sub.xp?group=comp.lang.cobol
 * Read this thread at
 http://www.deja.com/thread/%3CVA.00000066.00477629%40francoim%3E
```

#### ↳ Re: Tables and Moves

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-07-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A19A9B.6C512186@zip.com.au>`
- **References:** `<90491CB93918D21189BD00805FBE300B01442E51@voyager.okc.disa.mil>`

```
"Thompson, William" wrote:
> 
> Yea, but then it would just have the last length in it.....
…[21 more quoted lines elided]…
> will be fine...

1. I am fairly certain that the optimizing compiler will remove an
explicit 'add 0 '.

2.  If the call explicitly passes a value into the call then the
returned value should be checked 'by the compiler' upon return.  If
this caused an error I would consider it a bug.

3.  What I would not be sure of is if you set a longer value inside
the module than was set externally does the size of the array
automatically grow.  I would consider this undefined (even if it is
defined in the standard I would consider it risky).

The answer has been delivered on this one BTW.
Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
