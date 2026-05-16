[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# newbie seeking help: Fujitsu Cobol: WINEXEC-Console doesn't recognize 'Return' key

_3 messages · 2 participants · 2000-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Tutorials, books, learning`](../topics.md#learning)

---

### newbie seeking help: Fujitsu Cobol: WINEXEC-Console doesn't recognize 'Return' key

- **From:** "Claude Kaber" <ckaber@pt.lu>
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38bc1373@news.vo.lu>`

```
Hello,
I'm new to Cobol and i'm currently trying Fujitsu Cobol 3.0.
When i am executing programs (with the WINEXEC program from fujitsu), the
Console Window reacts strangely to the 'Return' key:
When i  hit the 'Return'-key for terminating an input (demanded by an ACCEPT
statment in within the program), the cursor simply moves to the next line of
the console window (like if i were typing text in a text editor), but the
input is not accepted.
The 'Return' key is not accepted until i type in as many Characters as there
are in the Variable filled by the ACCEPT statment.  EG: if i have a variable
of PIC X(100), i would need typing 100 characters !!! before the
WINEXEC-console window will accept the input. If i understand well the COBOL
standard, it should be possible to terminate the input by hitting 'Return' ,
it should not be necessary to type all the characters .
Is this a bug in the Fujitsu-WINEXEC program or am i missing something ?

Any help is much appreciated,
Claude Kaber
```

#### ↳ Re: newbie seeking help: Fujitsu Cobol: WINEXEC-Console doesn't recognize 'Return' key

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89h6dj$efq$1@nntp8.atl.mindspring.net>`
- **References:** `<38bc1373@news.vo.lu>`

```
I believe that this is a "documented feature" (i.e. not considered a bug) by
Fujitsu.  Most other compilers do NOT work this way, but there is nothing in
the Standard to say that is wrong.  I know it has been discussed before in
comp.lang.cobol - so you may want to check out www.deja.com

I will check this out with Fujitsu to see if there is any option to "overcome
it".
```

##### ↳ ↳ Re: newbie seeking help: Fujitsu Cobol: WINEXEC-Console doesn't recognize 'Return' key

- **From:** "Claude Kaber" <ckaber@pt.lu>
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38bc414c$1@news.vo.lu>`
- **References:** `<38bc1373@news.vo.lu> <89h6dj$efq$1@nntp8.atl.mindspring.net>`

```
Hello,
Thanks for the 'deja.com' tip. The topic was indeed discussed earlier.
One (the) solution consists in adding 'FROM Console' to the ACCEPT statment:

eg: 'ACCEPT myvariable FROM Console'   (instead of simply 'ACCEPT
myvariable').
You may then hit 'Return' for terminating the input within the
WINEXEC-console window.

many thanks for the prompt reply,
Claude Kaber

William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:89h6dj$efq$1@nntp8.atl.mindspring.net...
> I believe that this is a "documented feature" (i.e. not considered a bug)
by
> Fujitsu.  Most other compilers do NOT work this way, but there is nothing
in
> the Standard to say that is wrong.  I know it has been discussed before in
> comp.lang.cobol - so you may want to check out www.deja.com
>
> I will check this out with Fujitsu to see if there is any option to
"overcome
> it".
>
…[6 more quoted lines elided]…
> > When i am executing programs (with the WINEXEC program from fujitsu),
the
> > Console Window reacts strangely to the 'Return' key:
> > When i  hit the 'Return'-key for terminating an input (demanded by an
> ACCEPT
> > statment in within the program), the cursor simply moves to the next
line
> of
> > the console window (like if i were typing text in a text editor), but
the
> > input is not accepted.
> > The 'Return' key is not accepted until i type in as many Characters as
…[6 more quoted lines elided]…
> > standard, it should be possible to terminate the input by hitting
'Return'
> ,
> > it should not be necessary to type all the characters .
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
