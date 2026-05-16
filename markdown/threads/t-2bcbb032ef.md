[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM/Cobol losing cursor

_3 messages · 3 participants · 2001-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### RM/Cobol losing cursor

- **From:** "Hi-Tech Software, Inc." <hitech@kynd.net>
- **Date:** 2001-06-19T12:59:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9go06g$nrl$1@news.chatlink.com>`

```
Hello Ladies and Gentlemen of the Jury;

I am hoping someone has run into this similar situation and can shed some
light or point us in a direction.

We have a client running an NT network, with about 200 workstations all
running Windows 98.  They are running the text based version of our software
using an RM/Cobol 85 Ver. 5.36 Runtime.  Up until last week everything was
running smoothly.  They tell me nothing has changed on their end and I know
that we haven't changed anything, but all of a sudden when they are doing
data entry, the cursor disappears from the screen.  They can type and hit
the Enter key and the program will proceed to the next field, it just isn't
obvious where they are on the screen and makes it rather hard for input.

Has anyone ever heard of something like this happening before?

We have contacted RM.  They searched their data base and the only thing they
could come up with was to reconfigure the runtime with a TERM-INTERFACE DOS
and then set DEVICE=ANSI.SYS in the CONFIG.SYS.  I tried that on one of our
systems here but when I tried to run a program the runtime didn't handle the
windowing aspects of the program and wigged out the display.  (You could see
the program amongst the hex-values, but I think we would get some
complaints)

I am still not convinced that it has anything to do with our system.  I
believe that they loaded something on the server and pushed it down to the
workstations, but they are still telling me they haven't changed anything.

Any suggestions or help would be greatly appreciated.

Bill
Hi-Tech Software, Inc.
```

#### ↳ Re: RM/Cobol losing cursor

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2001-06-19T19:55:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h7vit0e9t9g73g58k87eu8gaj1bq62qnm@4ax.com>`
- **References:** `<9go06g$nrl$1@news.chatlink.com>`

```
On Tue, 19 Jun 2001 12:59:27 -0400, "Hi-Tech Software, Inc."
<hitech@kynd.net> wrote:

>Hello Ladies and Gentlemen of the Jury;
>

>We have a client running an NT network, with about 200 workstations all
>running Windows 98.  They are running the text based version of our software
…[7 more quoted lines elided]…
>Has anyone ever heard of something like this happening before?
Yes.


Being a company of this size I will assume they have some kind of
Virus product installed in each and every PC.

A possbile upgrade of this software (which is normally done
automatically) will be one of the possible causes of this problem.

If this is happening in all workstations, and every single day then I
would ask them to disable some or all of this Software options in one
Workstation (of someone they know will not try to introduce a Virus,
or that will not be sugject to external access (email, Web access)).
and see if it still happens.

Apart from this it can happen if you are doing CALL SYSTEM to execute
some other programs and one of this has been changed or doesn't have
all "requirements" available any more.


Sorry if I can not be more helpfull, but these type of things are
always hard to figure out.

cheers

Frederico Fonseca
Memosis
Liant technical support (and distributors) in Portugal
```

##### ↳ ↳ Re: RM/Cobol losing cursor

- **From:** merhottin@aol.com (Merhottin)
- **Date:** 2001-06-20T00:07:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010619200733.12461.00000131@ng-ma1.aol.com>`
- **References:** `<8h7vit0e9t9g73g58k87eu8gaj1bq62qnm@4ax.com>`

```
Frederico made a good point.  We just upgraded our virus software, and found
problems that interfered with other programs.  While the upgrade did not effect
our COBOL programs, they did effect other programs.  We actually have to
disable the virus protection to run some applications.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
