[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Netexpress 3.01 rts error 9/199

_5 messages · 3 participants · 2003-09_

---

### Netexpress 3.01 rts error 9/199

- **From:** djames <member39085@dbforums.com>
- **Date:** 2003-09-11T04:46:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3356706.1063270017@dbforums.com>`

```

Compiling on Netexpress 3.01.4 no SP.  When opening an index sequential
file get I/O error 9/199.  Through investigation have found out that
this is actually 9/209 which highlights an unexpected network problem.
Have tried updating netwrok drivers to no avail.  The PC is running
Windows 2000 Pro with SP4.  Anything which could help solve this problem
would be greatly appreciated.



Duncan
```

#### ↳ Re: Netexpress 3.01 rts error 9/199

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-09-11T11:58:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0309111058.5dea1d33@posting.google.com>`
- **References:** `<3356706.1063270017@dbforums.com>`

```
djames <member39085@dbforums.com> wrote 

> Compiling on Netexpress 3.01.4 no SP.  When opening an index sequential
> file get I/O error 9/199.  Through investigation have found out that
> this is actually 9/209 

Are there any spaces in the path to the file name ?
```

##### ↳ ↳ Re: Netexpress 3.01 rts error 9/199

- **From:** djames <member39085@dbforums.com>
- **Date:** 2003-09-12T10:13:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3362999.1063376003@dbforums.com>`
- **References:** `<3356706.1063270017@dbforums.com> <217e491a.0309111058.5dea1d33@posting.google.com>`

```

Originally posted by Richard 

> djames <member39085@dbforums.com> wrote

>

> > Compiling on Netexpress 3.01.4 no SP.  When opening an index
>     sequential

> > file get I/O error 9/199.  Through investigation have found out
>     that

> > this is actually 9/209 

>

> Are there any spaces in the path to the file name ? 



no spaces in filename, the same program is used on many other different
machines successfully.
```

#### ↳ Re: Netexpress 3.01 rts error 9/199

- **From:** annojoerg@arcor.de (annojoerg)
- **Date:** 2003-09-11T12:58:47-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4368c973.0309111158.671b0592@posting.google.com>`
- **References:** `<3356706.1063270017@dbforums.com>`

```
djames <member39085@dbforums.com> wrote in message news:<3356706.1063270017@dbforums.com>...
> Compiling on Netexpress 3.01.4 no SP.  When opening an index sequential
> file get I/O error 9/199.  Through investigation have found out that
…[7 more quoted lines elided]…
> Duncan


hi,
in all my cases was the reason for your porb an defect networkcard or
his option (example, auto, vollduplex,half a.so)

annojoerg
```

##### ↳ ↳ Re: Netexpress 3.01 rts error 9/199

- **From:** djames <member39085@dbforums.com>
- **Date:** 2003-09-12T10:16:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3363000.1063376196@dbforums.com>`
- **References:** `<3356706.1063270017@dbforums.com> <4368c973.0309111158.671b0592@posting.google.com>`

```

Originally posted by Annojoerg 

> djames <member39085@dbforums.com> wrote in message
> news:<3356706.1063270017@dbforums.com>...

> > Compiling on Netexpress 3.01.4 no SP.  When opening an index
>     sequential

> > file get I/O error 9/199.  Through investigation have found out
>     that

> > this is actually 9/209 which highlights an unexpected network
>     problem.

> > Have tried updating netwrok drivers to no avail.  The PC is
>     running

> > Windows 2000 Pro with SP4.  Anything which could help solve this
>     problem

> > would be greatly appreciated.

> > 

> > 

> > 

> > Duncan

>

>

> hi,

> in all my cases was the reason for your porb an defect networkcard or

> his option (example, auto, vollduplex,half a.so)

>

> annojoerg 







thanx for the reply.  you might have a point as the program works fine
on other machines.  wouldn't a defect networkcard not even allow the
machine to access the program, which is trying to open the file, in the
first place though?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
