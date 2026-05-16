[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Acu-Cobol and Acu-4GL

_6 messages · 4 participants · 2000-04_

---

### Acu-Cobol and Acu-4GL

- **From:** "Ray Smith" <Ray.Smith@fujitsu.com.au>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cgl06$eck@newshost.fujitsu.com.au>`

```
Hi,

This question is for anyone who has used Acu-4GL from AcuCorp or has
experience with a product that automatically links standard cobol IO
instructions to RDBMS SQL commands.

The performance we achieve is about 6 times slower than using the standard
Vision file system. I was wondering if anyone else has experiance in this
area and what performance levels they achieved.

We use the "where" clause to limit "most" of our calls using Acu-4GL.  This
has improved our performance to about 6 times slower than Vision.

Any feedback will be most welcomed.

Thanks

Ray Smith
```

#### ↳ Re: Acu-Cobol and Acu-4GL

- **From:** "Anton" <a.rusbach@coss.nl>
- **Date:** 2000-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8che2i$702$1@news1.xs4all.nl>`
- **References:** `<8cgl06$eck@newshost.fujitsu.com.au>`

```
> instructions to RDBMS SQL commands.

What RDBMS?

grtx,
Anton
```

##### ↳ ↳ Re: Acu-Cobol and Acu-4GL

- **From:** "Ray Smith" <Ray.Smith@fujitsu.com.au>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cj0qo$ej2@newshost.fujitsu.com.au>`
- **References:** `<8cgl06$eck@newshost.fujitsu.com.au> <8che2i$702$1@news1.xs4all.nl>`

```
We use Sybase.

With a small amount of re-designing I am down to about 4 times slower than
vision, which is an improvement but still significant.

Anton <a.rusbach@coss.nl> wrote in message
news:8che2i$702$1@news1.xs4all.nl...
> > instructions to RDBMS SQL commands.
>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Acu-Cobol and Acu-4GL

- **From:** "support" <cobol@doya.url.com.tw>
- **Date:** 2000-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cn08e$es8$1@news.seed.net.tw>`
- **References:** `<8cgl06$eck@newshost.fujitsu.com.au> <8che2i$702$1@news1.xs4all.nl> <8cj0qo$ej2@newshost.fujitsu.com.au>`

```
    In fact, using Acu4GL should be slower than using Vision. Vision is
Acucobol's default file system,
but Acu4GL is through DB engine to get the data. You can think what had
happened when you execute a I/O statement. The Acu4GL transfers the
statement to SQL, and passes it into the DB engine; DB engine
executes the SQL and gets the data and returned the result back to Acu4GL(or
Acucobol's generic file system).
    The file structures and the program's I/O statements will also be the
performance issue. Maybe you
can check your programs to see whether somewhere can modify to improve the
performance.


Ray Smith <Ray.Smith@fujitsu.com.au> wrote in message
news:8cj0qo$ej2@newshost.fujitsu.com.au...
> We use Sybase.
>
…[14 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Acu-Cobol and Acu-4GL

_(reply depth: 4)_

- **From:** "Ray Smith" <Ray.Smith@fujitsu.com.au>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cr0m5$p4c@newshost.fujitsu.com.au>`
- **References:** `<8cgl06$eck@newshost.fujitsu.com.au> <8che2i$702$1@news1.xs4all.nl> <8cj0qo$ej2@newshost.fujitsu.com.au> <8cn08e$es8$1@news.seed.net.tw>`

```
Thanks to everone who responded.

Yes, any RDMS is going to be slower than an ISAM system.  I understand that
but didn't mention it in my first email.

With a small amount of re-programming and making sure all IO starts have a
where clause it seems most of our applications can achieve a 1.5 to 3 times
slower performance than the ISAM vision file system.

I think we will have to be happy with that ... now just to make our clients
happy with that ...

support <cobol@doya.url.com.tw> wrote in message
news:8cn08e$es8$1@news.seed.net.tw...
>     In fact, using Acu4GL should be slower than using Vision. Vision is
> Acucobol's default file system,
…[3 more quoted lines elided]…
> executes the SQL and gets the data and returned the result back to
Acu4GL(or
> Acucobol's generic file system).
>     The file structures and the program's I/O statements will also be the
…[9 more quoted lines elided]…
> > With a small amount of re-designing I am down to about 4 times slower
than
> > vision, which is an improvement but still significant.
> >
…[13 more quoted lines elided]…
>
```

#### ↳ Re: Acu-Cobol and Acu-4GL

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mphpesop39h4m3kqv3r16je2alvjs0fa62@4ax.com>`
- **References:** `<8cgl06$eck@newshost.fujitsu.com.au>`

```
"Ray Smith" <Ray.Smith@fujitsu.com.au> wrote:

>
>This question is for anyone who has used Acu-4GL from AcuCorp or has
…[5 more quoted lines elided]…
>area and what performance levels they achieved.

>We use the "where" clause to limit "most" of our calls using Acu-4GL.  This
>has improved our performance to about 6 times slower than Vision.

i am going out on a limb here (and i don't know the first thing about
vision or a gl) but i do know that in sql the where clause operates
differently than cobols start and read commands. in using indexed io
(read and start) you can decide which index gets used first. the same
may or may not be true depending on sql. also, sql might return it one
record at a time, 10, or all of them.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
