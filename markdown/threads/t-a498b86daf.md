[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# need help to debug a cobol program with RM/COBOL-85

_4 messages · 3 participants · 2008-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### need help to debug a cobol program with RM/COBOL-85

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2008-02-05T18:01:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<foa3bi$4k6$1@s1.news.oleane.net>`

```
Hi,

As it is wrote in the subject, i must debug a cobol program.
I read the user's guide and i found that i should enter the D option in 
the RM/COBOL-85 Runtime Command to execute program for debugging.

But, in fact, there are many long programs and I want set a breakpoint 
but i don't understand how to do this.

The user's guide tells this :
The syntax for the A command is as follows :
A [line[+intraline][,[prog-name][,[count]]]]

I tried to do :
A 596,FGCENT
this at the prompt but it doesn't work.

Where is the problem ?

Best regards

Jerome
```

#### ↳ Re: need help to debug a cobol program with RM/COBOL-85

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2008-02-05T18:47:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dpbhq3djsd4cn898g69hbb2rtje2rcqj2f@4ax.com>`
- **References:** `<foa3bi$4k6$1@s1.news.oleane.net>`

```
On Tue, 05 Feb 2008 18:01:43 +0100, Jerome <j.aubert1@free.fr> wrote:

>Hi,
>
…[19 more quoted lines elided]…
>Jerome

Please state OS and COBOL Version you are using.

It may be possible that you can use the source debugger, and you wont
have that type of issues.


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: need help to debug a cobol program with RM/COBOL-85

- **From:** Jerome <j.aubert1@free.fr>
- **Date:** 2008-02-06T09:00:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fobo06$ohu$1@s1.news.oleane.net>`
- **In-Reply-To:** `<dpbhq3djsd4cn898g69hbb2rtje2rcqj2f@4ax.com>`
- **References:** `<foa3bi$4k6$1@s1.news.oleane.net> <dpbhq3djsd4cn898g69hbb2rtje2rcqj2f@4ax.com>`

```
Frederico Fonseca a ï¿½crit :

> 
> Please state OS and COBOL Version you are using.

Windows XP Pro
Runtime Cobol version 6.07.00 for DOS 3.3+
Compiler Cobol version 5.36.00 for DOS 2.00+
> 
> It may be possible that you can use the source debugger, and you wont
> have that type of issues.
> 

The source debugger ! What is this strange animal :-) ?

Best regards (and thank you for your help)

Jerome
```

###### ↳ ↳ ↳ Re: need help to debug a cobol program with RM/COBOL-85

- **From:** t.morrison@liant.com
- **Date:** 2008-02-07T05:20:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf999b3b-5e48-47c2-b64f-31cbfe273501@u10g2000prn.googlegroups.com>`
- **References:** `<foa3bi$4k6$1@s1.news.oleane.net> <dpbhq3djsd4cn898g69hbb2rtje2rcqj2f@4ax.com> <fobo06$ohu$1@s1.news.oleane.net>`

```
On Feb 6, 2:00 am, Jerome <j.aube...@free.fr> wrote:
> Windows XP Pro
> Runtime Cobol version 6.07.00 for DOS 3.3+
> Compiler Cobol version 5.36.00 for DOS 2.00+

We have replied in private email.

Tom Morrison
Liant Software Corporation
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
