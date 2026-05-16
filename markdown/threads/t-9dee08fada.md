[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# working storage

_6 messages · 4 participants · 1998-11_

---

### working storage

- **From:** gvwmoore@ix.netcom.com (G Moore)
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364229dd.180703@nntp.ix.netcom.com>`

```
ok, if you have two modules

working-storage section.
01	someitem	pic	99.

procedure division.
move 1 to someitem.

working-storage section.
01	someitem	pic	99.

procedure division.
display someitem.

if you run one, and then the other, does someitem have the value from
the first?


gvwmoore@ix.spam.netcom.com to reply remove the spam
```

#### ↳ Re: working storage

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71tdsv$eh7$1@news.igs.net>`
- **References:** `<364229dd.180703@nntp.ix.netcom.com>`

```
No, they are different programs.  Each is a completely separate
entity.

G Moore wrote in message <364229dd.180703@nntp.ix.netcom.com>...
>ok, if you have two modules
>
…[16 more quoted lines elided]…
>gvwmoore@ix.spam.netcom.com to reply remove the spam
```

##### ↳ ↳ Re: working storage

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36424942.B6F@swbell.net>`
- **References:** `<364229dd.180703@nntp.ix.netcom.com> <71tdsv$eh7$1@news.igs.net>`

```
Donald Tees wrote:
> 
> No, they are different programs.  Each is a completely separate
> entity.

Strictly speaking that's true.  If the two variables are in two 
different WORKING STORAGE sections, declared as shown in the original
post, then they are distinct.  The similarity of name and PIC makes no 
difference.

However, there are arrangements whereby two modules may share a common 
variable (depending on what features are supported by your compiler):

1. You declare the variable as EXTERNAL.

2. In nested programs, you declare the variable as GLOBAL.

3. You provide multiple entry points for a single module.  Since
those entry points use the same WORKING STORAGE, they may access the
same variables.  This isn't really a sharing between modules, since
it's the same module.  However, the distinction is not obvious from
the standpoint of the calling code, since the CALL statements look
the same whether the entry points are in the same module or not.

Each technique has its advantages and disadvantages.  In my own work
I use the third approach extensively, and I have never used the other
two.  Others may have different tastes and probably do.

> G Moore wrote in message <364229dd.180703@nntp.ix.netcom.com>...
> >ok, if you have two modules
…[17 more quoted lines elided]…
> >gvwmoore@ix.spam.netcom.com to reply remove the spam

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: working storage

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71tmm8$a4s$1@news.igs.net>`
- **References:** `<364229dd.180703@nntp.ix.netcom.com> <71tdsv$eh7$1@news.igs.net> <36424942.B6F@swbell.net>`

```

Michael C. Kasten wrote in message <36424942.B6F@swbell.net>...

The global external methodology is very handy for sharing
data between either main program and DLL, or between
DLL modules.

>>> No, they are different programs.  Each is a completely separate
>> entity.
…[46 more quoted lines elided]…
>http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: working storage

_(reply depth: 4)_

- **From:** "Charlie Ebert" <kd5ob@theshop.net>
- **Date:** 1998-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2v112.634$yA2.10136@newsfeed.slurp.net>`
- **References:** `<364229dd.180703@nntp.ix.netcom.com> <71tdsv$eh7$1@news.igs.net> <36424942.B6F@swbell.net> <71tmm8$a4s$1@news.igs.net>`

```
External area's or global,
WATCH OUT FOR THAT $SET DEFAULT BYTE compiler command at the top of your
software!
Don't put it in any .dll's you might be using external clauses with!

Charlie



Donald Tees wrote in message <71tmm8$a4s$1@news.igs.net>...
>
>Michael C. Kasten wrote in message <36424942.B6F@swbell.net>...
…[55 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: working storage

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<722chs$b8v$1@news.igs.net>`
- **References:** `<364229dd.180703@nntp.ix.netcom.com> <71tdsv$eh7$1@news.igs.net> <36424942.B6F@swbell.net> <71tmm8$a4s$1@news.igs.net> <2v112.634$yA2.10136@newsfeed.slurp.net>`

```
Charlie Ebert wrote in message <2v112.634$yA2.10136@newsfeed.slurp.net>...
>External area's or global,
>WATCH OUT FOR THAT $SET DEFAULT BYTE compiler command at the top of your
>software!
>Don't put it in any .dll's you might be using external clauses with!


I am not familiar with that directive (is it Fujitsu?).  What
does it do?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
