[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Data Validation Student Project (0/1)

_5 messages · 4 participants · 1999-11_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Data Validation Student Project (0/1)

- **From:** Larry <mesaboogy@yahoo.com>
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2EQ7OHy1Qw3wXspgcFkN0OJyacZ0@4ax.com>`

```
Hi,
I've attached the source and input data file for a data validation
project for an introductory COBOL course. If anyone wants to look at
it and make some suggestions for better code, please do. It works the
way it is supposed to now, I just wanted to improve upon it. Thanks.

BTW, we use Microfocus Personal COBOL 2.0 for DOS.
```

#### ↳ Re: Data Validation Student Project (0/1)

- **From:** "Simon R Hart" <hart1@technologist.com>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81jrvo$1na$1@neptunium.btinternet.com>`
- **References:** `<2EQ7OHy1Qw3wXspgcFkN0OJyacZ0@4ax.com>`

```

Larry wrote in message <2EQ7OHy1Qw3wXspgcFkN0OJyacZ0@4ax.com>...
>Hi,
>I've attached the source and input data file for a data validation
…[4 more quoted lines elided]…
>BTW, we use Microfocus Personal COBOL 2.0 for DOS.


One tip, you could refrain from using periods (.) after every line of
code, this is unnecessary and very "old" this is why we have END-*
statements nowadays.

Another tip, code in lowercase - it looks better and easier to read IMHO.

As for logic I only browsed your code, keep up the good work.

Simon R Hart.
```

##### ↳ ↳ Re: Data Validation Student Project (0/1)

- **From:** Larry <mesaboogy@yahoo.com>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8aA+OEFS+VirAFhQMw5pffcIOMVc@4ax.com>`
- **References:** `<2EQ7OHy1Qw3wXspgcFkN0OJyacZ0@4ax.com> <81jrvo$1na$1@neptunium.btinternet.com>`

```
On Thu, 25 Nov 1999 17:33:47 -0800, "Simon R Hart"
<hart1@technologist.com> wrote:

Thanks for the tips and encouragement. I'll try using lowercase, but
I'll have to wait until after the class to try losing the periods - my
instructor requires this in our coding guidelines. 

<snip>
>One tip, you could refrain from using periods (.) after every line of
>code, this is unnecessary and very "old" this is why we have END-*
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Data Validation Student Project (0/1)

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3842C04F.62F91A85@NOSPAMhome.com>`
- **References:** `<2EQ7OHy1Qw3wXspgcFkN0OJyacZ0@4ax.com> <81jrvo$1na$1@neptunium.btinternet.com>`

```
Simon R Hart wrote:

> One tip, you could refrain from using periods (.) after every line of
> code, this is unnecessary and very "old" this is why we have END-*
…[3 more quoted lines elided]…
> 

But if you start working at our shop, put those periods back in.  I bet
you would have a problem getting lower case to be accepted here as well.
```

###### ↳ ↳ ↳ Re: Data Validation Student Project (0/1)

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1B04.925$%N1.119404@typ11.nn.bcandid.com>`
- **References:** `<2EQ7OHy1Qw3wXspgcFkN0OJyacZ0@4ax.com> <81jrvo$1na$1@neptunium.btinternet.com> <3842C04F.62F91A85@NOSPAMhome.com>`

```

Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:3842C04F.62F91A85@NOSPAMhome.com...
> Simon R Hart wrote:
>
…[4 more quoted lines elided]…
> > Another tip, code in lowercase - it looks better and easier to read
IMHO.
> >
>
> But if you start working at our shop, put those periods back in.  I bet
> you would have a problem getting lower case to be accepted here as well.

Amen.  A former supervisor in this shop had a small revolt over this issue,
especially when the code ended up in mixed upper/lower case.  While putting
together a script to perform automated changes to programs checked out for
Y2K, I was able to add a program to convert all non-commented, non-quoted
text to uppercase.  That program was named in his honor <g>.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
