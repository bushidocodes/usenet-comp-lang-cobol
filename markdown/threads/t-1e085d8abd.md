[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error

_3 messages · 2 participants · 2005-05_

---

### Error

- **From:** "G. Ferraro" <giufer1@virgilio.it>
- **Date:** 2005-05-04T06:25:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sVZde.1327701$35.49590760@news4.tin.it>`

```
when I start a programm receive the following error:

load error :file 'kwrunprg
error code:173, pc=0, call=1, seg=0
173 error message text not found

What is is happen?
Thank you of all
G. Ferraro
```

#### ↳ Re: Error

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-05-04T00:37:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1115192227.938110.234990@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<sVZde.1327701$35.49590760@news4.tin.it>`
- **References:** `<sVZde.1327701$35.49590760@news4.tin.it>`

```
We have to guess that it is MicroFocus Cobol ?

> load error :file 'kwrunprg
> error code:173, pc=0, call=1, seg=0

The program 'kwrunprg' has tried to call a program but cannot find it.
You should have found '173' in the manual 'Error Message' for your
compiler.

> 173 error message text not found

The run-time cannot find the error message text file
This contains descriptions of the errors and would have said something
like 'Called program not found'.
```

##### ↳ ↳ Re: Error

- **From:** "G. Ferraro" <giufer1@virgilio.it>
- **Date:** 2005-05-04T09:17:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<br0ee.1328447$35.49601094@news4.tin.it>`
- **References:** `<sVZde.1327701$35.49590760@news4.tin.it> <1115192227.938110.234990@f14g2000cwb.googlegroups.com>`

```
Thank a lot.
G. Ferraro

"Richard" <riplin@Azonic.co.nz> ha scritto nel messaggio 
news:1115192227.938110.234990@f14g2000cwb.googlegroups.com...
> We have to guess that it is MicroFocus Cobol ?
>
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
