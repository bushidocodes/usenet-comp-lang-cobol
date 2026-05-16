[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# working in the buffers

_2 messages · 2 participants · 1998-08 → 1998-09_

---

### Re: working in the buffers

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-1hvpjDj3F6uV@Dwight_Miller.iix.com>`
- **References:** `<35df03f8.20027739@netnews.worldnet.att.net> <6rn21n$cpt$1@nnrp03.primenet.com> <35E1F0DE.714C@hpohp2.wgw.bt.co.uk>`

```
On Mon, 24 Aug 1998 23:01:50, Jeremy Coast 
<coastjf@hpohp2.wgw.bt.co.uk> wrote:

>> 
> Mike,
…[6 more quoted lines elided]…
> Regards,


I'm not Mike - but having been recently bitten, I'll take a stab at 
it.

First there are a few places where you get into trouble on some 
implenentations.  You can't move data to the buffer before a file is 
opened or after it is closed.

I have a habit of not opening a file in a particular program until its
first use.  Very clean and efficient, but don't try to build the 
record in the buffer before the file is open!

Secondly, wrote a program, simple file in and out, and - read a 
record, moved some fields and created others, then wrote the record.  
Simple.

I then went back into this program and added, without thinking, some 
post write processing.

The records I referenced in my processing were to be the ones just 
written. This is a serious No No.  The actual data my program found 
was from several hundred records ago.  It was a real mess.  Just 
produced strange, very strange results.

If I had not worked in the buffers - as a rule - I would not have seen
this problem.

However, do I still advocate buffer abstinance ?  No.  I think if you 
follow the rules, and understand what is happening, you can safely 
work in the buffers.  Just don't address the area when the file is 
closed, and don't reference the data in the buffer after a write.

Blast away.
```

#### ↳ Re: working in the buffers

- **From:** jcj0347@aol.com (JCJ0347)
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998090302453200.WAA08477@ladder03.news.aol.com>`
- **References:** `<Jl0PnHJ5PvPd-pn2-1hvpjDj3F6uV@Dwight_Miller.iix.com>`

```
>The records I referenced in my processing were to be the ones just 
>written. This is a serious No No.  The actual data my program found 
…[5 more quoted lines elided]…
>
Hmmmm.  Been there, done that, too Thane.

It just took one nasty little bug to make a believer out of me.   Sure
you can work in the buffers, as long as the record is there.  I now 
assume that after the record is passed to the I-O, nothing is there but
garbage swept up off the floor of the processor.

James
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
