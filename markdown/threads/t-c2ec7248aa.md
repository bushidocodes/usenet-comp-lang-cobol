[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS question

_4 messages · 4 participants · 1996-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS question

- **From:** "juanita r. alvarez" <ua-author-17087323@usenetarchives.gap>
- **Date:** 1996-10-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<325230B0.77E4@tophat.pima.gov>`

```

Hi Everyone,
I have a CICS question and it probably is a very stupid mistake but
I can't find it for the life of me. On our ancient machine, we are
using CICS 2.1.2 and our debugger is CEDF. When I simply go into the
main menu and pick a transaction to go to, my terminal hangs up and it
has to be brought out of service and back into service to clear things
up. However when I use CEDF, to try to see what the problem is,
everything works as slick as a whistle, no problems, no hanging up,
nothing!!!!
I'm sure it something really simple and stupid that I'm overlooking
but I can see. Comm area is ok, logic flow looks ok, checked all the
periods they look fine. Any suggestions would be appreciated.
Thanks,
Juanita
```

#### ↳ Re: CICS question

- **From:** "ets..." <ua-author-17072749@usenetarchives.gap>
- **Date:** 1996-10-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ec7248aa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<325230B0.77E4@tophat.pima.gov>`
- **References:** `<325230B0.77E4@tophat.pima.gov>`

```

In <325··.@top··a.gov>, "Juanita R. Alvarez" writes:
› Hi Everyone,
›     I have a CICS question and it probably is a very stupid mistake but
…[11 more quoted lines elided]…
› 		Juanita


Juanita,

You mentioned a 'menu'. Is it possible that when you 'go in via the menu' and
when you use EDF you're possibly execing something different ?

Also, is it possible that the BMS data (I assume you're using BMS) has junk
in it that's hanging your tube ?

Do you have a system monitor such as TMON (woops, showing my age) ?

Is the system (VTAM?) giving you any error messages ? Do you have
access to the system console to see it ??!!

Generally speaking, EDF won't change the execution of your code so I'm at
a bit of a loss to explain your predicament.

Hope this at least gives you somewhere to look...


Ethan Schultz
Rosebud Management Systems
```

#### ↳ Re: CICS question

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-10-06T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ec7248aa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<325230B0.77E4@tophat.pima.gov>`
- **References:** `<325230B0.77E4@tophat.pima.gov>`

```

"Juanita R. Alvarez" wrote:

› Hi Everyone,
›     I have a CICS question and it probably is a very stupid mistake but
…[11 more quoted lines elided]…
› 		Juanita


Hmm, if your shop is like my shop and you could use EDF in the test
region but not in production. It maybe possible that a program didn't
compile correctly into production. Could it be a runaway transaction
(that is a endless looping program between CICS RETURN calls)? Try to
get your computer center to print off a dump the next time your
production program hangs up.

Just my 1.5 cents worth, adjusted for inflation
Boyce Williams
```

#### ↳ Re: CICS question

- **From:** "stev..." <ua-author-565738@usenetarchives.gap>
- **Date:** 1996-10-14T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2ec7248aa-p4@usenetarchives.gap>`
- **In-Reply-To:** `<325230B0.77E4@tophat.pima.gov>`
- **References:** `<325230B0.77E4@tophat.pima.gov>`

```

In article <325··.@top··a.gov>, "Juanita R. Alvarez"
writes:

› When I simply go into the
› main menu and pick a transaction to go to, my terminal hangs up and it
…[3 more quoted lines elided]…
› nothing!!!!

I had one like this several years ago, and it took forever to figure out.
Problem was, a bad subroutine in the linklist. When I finally convinced
the system gurus to check the linklist items, they found a VSE CICS module
(we were on MVS XA at the time). Never did find out how it got there.
This may not be your problem, but for what it is worth...
Good luck.

Steven L. Newton
Milwaukee, WI
Asimov, Heinlein, and Zappa are still the best
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
