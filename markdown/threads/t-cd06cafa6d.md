[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Timer exit

_5 messages · 3 participants · 2000-05_

---

### Timer exit

- **From:** "Peter" <Peter.vanDaal@nl.origin-it.com>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0E16861EE7BCD111BE9400805FE6841F0FEACDB3@c1s5x001.cor.srvfarm.origin-it.com>`

```
Hi group,
I am using Merant cobol compiler for Windows (Netexpress) and Unix (Server
express).
Does anybody have an example of setting a timer (with exit) in a cobol
program (signal ?). When the timer expires the application must terminate.
Peter
```

#### ↳ Re: Timer exit

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391B346B.224D8A9B@boeing.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0FEACDB3@c1s5x001.cor.srvfarm.origin-it.com>`

```
Peter wrote:
> 
> Hi group,
…[4 more quoted lines elided]…
> Peter

well a quick and dirty answer is to set a time stamp when you start the
program and then check it in some sort of perform loop

such as perform b-do-stuff thru b-do-stuff end
            until eof-stuff
               or time > max-time

in the b-stuff-loop you would execute a new time stamp and compare it to
the original stamp set up in the set up part of your code.

	Susan A  - mainframe analyst and cobol hack ;-)
```

##### ↳ ↳ Re: Timer exit

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391B52F5.D0EB7A8C@home.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0FEACDB3@c1s5x001.cor.srvfarm.origin-it.com> <391B346B.224D8A9B@boeing.com>`

```


Susan Allen wrote:
> 
>         Susan A  - mainframe analyst and cobol hack ;-)

Well we've had some recent discussion on esoteric titles. COBOL hack I
can understand; systems analyst I understand. Reluctantly I'll even buy
into analyst/programmer. Mainframe Analyst - now is that something like
a medical examiner for a mainframe ? Still who knows what you people are
doing there in Seattle with air/aero-planes  :-)

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Timer exit

- **From:** "Peter" <Peter.vanDaal@nl.origin-it.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0E16861EE7BCD111BE9400805FE6841F0FEED045@c1s5x001.cor.srvfarm.origin-it.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0FEACDB3@c1s5x001.cor.srvfarm.origin-it.com> <391B346B.224D8A9B@boeing.com>`

```

Susan Allen wrote in message <391B346B.224D8A9B@boeing.com>...
>Peter wrote:
>>
>> Hi group,
>> I am using Merant cobol compiler for Windows (Netexpress) and Unix
(Server
>> express).
>> Does anybody have an example of setting a timer (with exit) in a cobol
>> program (signal ?). When the timer expires the application must
terminate.
>> Peter
>
…[10 more quoted lines elided]…
> Susan A  - mainframe analyst and cobol hack ;-)

Susan
In the "b-stuff-loop" there is a socket "recv" which could never end when
the Server
side is not responding. Therefor i need an exit which would be activated
when
the timer expires and could terminate the program in a correct way by
telling the
customer the Server is not responding.
Any ideas ?
Peter
```

###### ↳ ↳ ↳ Re: Timer exit

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39205DE7.3E7D4D1A@boeing.com>`
- **References:** `<0E16861EE7BCD111BE9400805FE6841F0FEACDB3@c1s5x001.cor.srvfarm.origin-it.com> <391B346B.224D8A9B@boeing.com> <0E16861EE7BCD111BE9400805FE6841F0FEED045@c1s5x001.cor.srvfarm.origin-it.com>`

```
Peter wrote:
> 
> In the "b-stuff-loop" there is a socket "recv" which could never end when
…[6 more quoted lines elided]…
> Any ideas ?

Uh-oh, you caught me out.  I program on the mainframe and not the
servers, so I know very nearly nothing about servers, except that I know
time outs are handled extensively by most of the interface packages I
have to deal with, there must be a dozen or more experts here who could
better answer your question (now that you have explained the problem in
more detail)

	good luck -- Susan
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
