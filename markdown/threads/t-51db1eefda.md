[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Input problem using accept statement

_5 messages · 4 participants · 2003-02_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Input problem using accept statement

- **From:** snakess@hotmail.com (Nagraj Kini)
- **Date:** 2003-02-03T07:10:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<451a6377.0302030710.7281af2d@posting.google.com>`

```
hello,
   My problem is as follows. I am using a fujitsu compiler 3.0 the
free one. I have a variable as
01    AMOUNT    PIC 9(4).
When I use it as 
ACCEPT AMOUNT LINE 04 COLUMN 30.
On the input sceen the I see highlighted areas. I have to delete it
before inputing any values. Or need to input the values as 0004 and
not just 4.
And also when i say
01   AMOUNT     PIC 9(4)  VALUE ZEROS.
It is filled with zeros. And if I just need 4 I need to type 0004
cause if i just typed 4 it takes the value as 4000.
In the RM/COBOL compiler this gives me no problem at all. 
Thanking you in advance.

Nagraj.
```

#### ↳ Re: Input problem using accept statement

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-04T07:17:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1mbq4$1ib$2@aklobs.kc.net.nz>`
- **References:** `<451a6377.0302030710.7281af2d@posting.google.com>`

```
Nagraj Kini wrote:

>    My problem is as follows. I am using a fujitsu compiler 3.0 the
> free one. I have a variable as
…[9 more quoted lines elided]…
> cause if i just typed 4 it takes the value as 4000.

That is how the Fujitsu Cobol ACCEPT statement works - badly.
```

#### ↳ Re: Input problem using accept statement

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-02-03T21:06:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2476673.1044306407@dbforums.com>`
- **References:** `<451a6377.0302030710.7281af2d@posting.google.com>`

```

TRY  AMOUNT PIC  ZZZ9  VALUE ZEROS.

ITS  WORKS FINE

cARLOS lAGES
```

##### ↳ ↳ Re: Input problem using accept statement

- **From:** snakess@hotmail.com (Nagraj Kini)
- **Date:** 2003-02-04T00:03:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<451a6377.0302040003.a752adf@posting.google.com>`
- **References:** `<451a6377.0302030710.7281af2d@posting.google.com> <2476673.1044306407@dbforums.com>`

```
Carlos lages <member129@dbforums.com> wrote in message news:<2476673.1044306407@dbforums.com>...
I tried it. But that solution is not for fujitsu compiler. Still the
same problem :-( . It is same as specifying AMOUNT PIC 9(4) VALUE
ZEROS. Just as Richard said I guess that is the problem with the
ACCEPT statement.

Thanks,
Nagraj.

> TRY  AMOUNT PIC  ZZZ9  VALUE ZEROS.
> 
> ITS  WORKS FINE
> 
> cARLOS lAGES
```

#### ↳ Re: Input problem using accept statement

- **From:** "BRaTaX CK" <bratax@pandora.be>
- **Date:** 2003-02-05T14:09:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lW80a.31921$Jd.4244@afrodite.telenet-ops.be>`
- **References:** `<451a6377.0302030710.7281af2d@posting.google.com>`

```
maybe you can try this:

01 AMOUNT PIC 9(4).
01 E-AMOUNT PIC ZZZ9.

ACCEPT E-AMOUNT LINE 04 COLUMN 30
MOVE E-AMOUNT TO AMOUNT

explanation:
you make an extra variable, called e-amount, which is working with edited
fields (PIC Z)
but since the compiler can't count with edited fields, you have to do a MOVE
E-AMOUNT TO AMOUNT
same thing if you want to display it
then you do MOVE AMOUNT TO E-AMOUNT
DISPLAY E-AMOUNT

greetz,
bratax

"Nagraj Kini" <snakess@hotmail.com> schreef in bericht
news:451a6377.0302030710.7281af2d@posting.google.com...
> hello,
>    My problem is as follows. I am using a fujitsu compiler 3.0 the
…[14 more quoted lines elided]…
> Nagraj.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
