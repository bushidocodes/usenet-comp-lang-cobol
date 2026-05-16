[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Decimal values

_9 messages · 6 participants · 2001-06_

---

### Decimal values

- **From:** "CyberWizzard" <cyberwizzard@pandora.be>
- **Date:** 2001-06-12T16:55:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be>`

```
Hello,

i have an exam tomorrow and i don't know how i can put a decimal value into
a variable with ACCEPT.

the picture of the variable should be 9V9 if i want to use numbers between
0.0 and 9.9 isn't it?

when i enter 3.5 the value in my variable is 0.0.  why is this.  thank u for
any help, i'm really in trouble.
```

#### ↳ Re: Decimal values

- **From:** jacksleight@hotmail.com
- **Date:** 2001-06-12T17:52:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_FsV6.5505$pb1.213974@www.newsranger.com>`
- **References:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be>`

```
Hi CW,

Try pic 9.9

Jack

In article <bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be>, CyberWizzard
says...
>
>Hello,
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Decimal values

- **From:** "CyberWizzard" <cyberwizzard@pandora.be>
- **Date:** 2001-06-12T21:32:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fUvV6.30912$mR5.3660832@afrodite.telenet-ops.be>`
- **References:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be> <_FsV6.5505$pb1.213974@www.newsranger.com>`

```
Thanx Jack but that doesn't work either.
I can input integers like 3 : this gives 3.0
but when i use a decimal number like 3.5 i get 0.0

i tried 3.5 as well as 3,5 , but it still doesn't work.

Maybe its the compiler.  I don't know what compiler it is.  I got i from my
teacher and he got it because it was included with a book.  It looks likes
EDIT from DOS.  and it is an editor, compiler and linker all in one.  If you
know how i can solve the problem, even if my exam will already be over,
please tell me.

Thanx.

CW

<jacksleight@hotmail.com> a �crit dans le message news:
_FsV6.5505$pb1.213974@www.newsranger.com...
> Hi CW,
>
…[9 more quoted lines elided]…
> >i have an exam tomorrow and i don't know how i can put a decimal value
into
> >a variable with ACCEPT.
> >
> >the picture of the variable should be 9V9 if i want to use numbers
between
> >0.0 and 9.9 isn't it?
> >
> >when i enter 3.5 the value in my variable is 0.0.  why is this.  thank u
for
> >any help, i'm really in trouble.
> >
> >
>
>
```

###### ↳ ↳ ↳ Re: Decimal values

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-06-12T21:57:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YewV6.273744$sP6.15235077@news3.aus1.giganews.com>`
- **References:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be> <_FsV6.5505$pb1.213974@www.newsranger.com> <fUvV6.30912$mR5.3660832@afrodite.telenet-ops.be>`

```
Compiler errors, along with memory bit-rot, should be the last thing
to worry about.

Editing symbols (as in 9.9) are used to format output, not input
(except, sometimes, with exotic compilers).

It is up to you to convert the user's input to something useful. In
your case:

01  USER-VAL        PIC X(5).
01  COMPUTER-VAL    PIC 9(3)V99.

ACCEPT USER-VAL.
COMPUTE COMPUTER-VAL = FUNCTION NUMVAL(USER-VAL).

Of course, this fails if the user types "ASSHO"

"CyberWizzard" <cyberwizzard@pandora.be> wrote in message
news:fUvV6.30912$mR5.3660832@afrodite.telenet-ops.be...
> Thanx Jack but that doesn't work either.
> I can input integers like 3 : this gives 3.0
…[4 more quoted lines elided]…
> Maybe its the compiler.  I don't know what compiler it is.  I got i
from my
> teacher and he got it because it was included with a book.  It looks
likes
> EDIT from DOS.  and it is an editor, compiler and linker all in one.
If you
> know how i can solve the problem, even if my exam will already be
over,
> please tell me.
>
…[12 more quoted lines elided]…
> > In article <bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be>,
CyberWizzard
> > says...
> > >
> > >Hello,
> > >
> > >i have an exam tomorrow and i don't know how i can put a decimal
value
> into
> > >a variable with ACCEPT.
> > >
> > >the picture of the variable should be 9V9 if i want to use
numbers
> between
> > >0.0 and 9.9 isn't it?
> > >
> > >when i enter 3.5 the value in my variable is 0.0.  why is this.
thank u
> for
> > >any help, i'm really in trouble.
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Decimal values

_(reply depth: 4)_

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-06-13T17:27:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_nNV6.7084$pb1.269924@www.newsranger.com>`
- **References:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be> <_FsV6.5505$pb1.213974@www.newsranger.com> <fUvV6.30912$mR5.3660832@afrodite.telenet-ops.be> <YewV6.273744$sP6.15235077@news3.aus1.giganews.com>`

```
Jerry,

I'm sure you don't consider IBM's COBOLII or any of its LE versions "exotic".

Regards, Jack.

In article <YewV6.273744$sP6.15235077@news3.aus1.giganews.com>, Jerry P says...
>
>Compiler errors, along with memory bit-rot, should be the last thing
…[73 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Decimal values

_(reply depth: 5)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-06-13T23:47:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KYSV6.21434$JS1.1192777@bin2.nnrp.aus1.giganews.com>`
- **References:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be> <_FsV6.5505$pb1.213974@www.newsranger.com> <fUvV6.30912$mR5.3660832@afrodite.telenet-ops.be> <YewV6.273744$sP6.15235077@news3.aus1.giganews.com> <_nNV6.7084$pb1.269924@www.newsranger.com>`

```

"John H Sleight Jr" <nospam@newsranger.com> wrote in message
news:_nNV6.7084$pb1.269924@www.newsranger.com...
> Jerry,
>
> I'm sure you don't consider IBM's COBOLII or any of its LE versions
"exotic".
>
> Regards, Jack.
>

You mean these compilers can ACCEPT dataname, allow the user to type
"3.5", multiply dataname by, say, 3, and get 10.5?

I'm impressed.
```

###### ↳ ↳ ↳ Re: Decimal values

_(reply depth: 6)_

- **From:** John H Sleight Jr <nospam@newsranger.com>
- **Date:** 2001-06-14T20:40:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jj9W6.8882$pb1.339929@www.newsranger.com>`
- **References:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be> <_FsV6.5505$pb1.213974@www.newsranger.com> <fUvV6.30912$mR5.3660832@afrodite.telenet-ops.be> <YewV6.273744$sP6.15235077@news3.aus1.giganews.com> <_nNV6.7084$pb1.269924@www.newsranger.com> <KYSV6.21434$JS1.1192777@bin2.nnrp.aus1.giganews.com>`

```
What I meant was that you can read a record (e.g. from a report page on disk)
into a rec descr that contains a num-ed pic (e.g. $,$$9.99), 
then move that field to a numeric item [9(4)V99] and multiply  it by 3 and get
the numerically correct result.  


In article <KYSV6.21434$JS1.1192777@bin2.nnrp.aus1.giganews.com>, Jerry P
says...
>
>
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Decimal values

- **From:** aflinsch <avflinsch@att.net>
- **Date:** 2001-06-13T13:41:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B27A5C2.D6C5995F@att.net>`
- **References:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be> <_FsV6.5505$pb1.213974@www.newsranger.com> <fUvV6.30912$mR5.3660832@afrodite.telenet-ops.be>`

```
CyberWizzard wrote:
> 
> Thanx Jack but that doesn't work either.
…[4 more quoted lines elided]…
> 

try the following....


w-s

    value-to-accept     pic 9v9.
    value-to-display    pic 9.9.


procedure
    accept value-to-accept from console
    move value-to-accept to value-to-display
    display 'value entered was:' value-to-display



from terminal, enter 35, not 3.5
```

#### ↳ Re: Decimal values

- **From:** Barry Steinholtz <Bazza@OptOnline.Net>
- **Date:** 2001-06-12T21:57:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B26903B.F5357CCE@OptOnline.Net>`
- **References:** `<bQrV6.29648$mR5.3518368@afrodite.telenet-ops.be>`

```
Hi:

     Your problem is that anything coming in from ACCEPT must be treated as
alphanumeric, then within the program changed back to numeric. In other words,
your 3.5 is taking 3 physical places with the decimal point. You'll have to
figure out the rest for yourself.

Barry Steinholtz

CyberWizzard wrote:

> Hello,
>
…[7 more quoted lines elided]…
> any help, i'm really in trouble.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
