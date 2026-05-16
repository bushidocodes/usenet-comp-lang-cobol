[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus COBOL error

_2 messages · 2 participants · 1998-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus COBOL error

- **From:** phight@flash.net (Patrick Hight)
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,umbc.ifsm.cobol
- **Message-ID:** `<6vlp92$c9e$1@excalibur.flash.net>`

```
I have encountered an error in MF COBOL for which i cannot locate a 
resolution.
The error description i receive is: "File is a directory." This 
runstream is executed in 4DOS and aborts consistently at the same 
program step (an internal sort?). When the job is restarted at this 
step, the runstream executes normally and completes without error. 
Nothing is changed to restart the runstream! This is a 
very-poorly-described Error 21.

Any and all help would be appreciated.
```

#### ↳ Re: Microfocus COBOL error

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,umbc.ifsm.cobol
- **Message-ID:** `<6vltrq$a3q$1@news.igs.net>`
- **References:** `<6vlp92$c9e$1@excalibur.flash.net>`

```
If you have a network, you might try creating a drive to run
it on.  If the problem then disappears on a dedicated drive,
you might actual have a directory that the system is attempting
to open as a file.

Patrick Hight wrote in message <6vlp92$c9e$1@excalibur.flash.net>...
>I have encountered an error in MF COBOL for which i cannot locate a
>resolution.
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
