[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# arcsinus

_10 messages · 6 participants · 2008-06 → 2008-07_

---

### arcsinus

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-06-30T23:12:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com>`

```
Hi i have a big problem!

I need the asinus/arcsinus of a value, but i just have the sinus
function,
does anyone of u know a solution for me, how to calculate the arcsinus
just with the sin function?
tks!!!
```

#### ↳ Re: arcsinus

- **From:** epc8@juno.com
- **Date:** 2008-06-30T23:55:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<023f1688-732c-433d-b992-a0cf484caea0@j22g2000hsf.googlegroups.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com>`

```
On Jul 1, 2:12 am, mario <mmc_vw1...@hotmail.com> wrote:
> Hi i have a big problem!
>
…[4 more quoted lines elided]…
> tks!!!

1. Are you certain that your COBOL does not have the ASIN intrinsic
function?

2. Why in COBOL?

3. If you are determined to solve the problem as you describe, how
about Newton's Method?

let Y = sin(X), solve for X by iteration

- e
```

#### ↳ Re: arcsinus

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-01T09:21:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g4csvn$cf0$1@reader2.panix.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com>`

```
In article <8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com>,
mario  <mmc_vw1200@hotmail.com> wrote:
>Hi i have a big problem!
>
…[3 more quoted lines elided]…
>just with the sin function?

Please do your own homework.

DD
```

##### ↳ ↳ Re: arcsinus

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-07-01T03:56:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9aed5964-acb0-414b-be71-acd7d8d7a61c@l64g2000hse.googlegroups.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com> <g4csvn$cf0$1@reader2.panix.com>`

```
i need it because of a production parameter of iron helices and
they are cutted in special angles and for those parameters i  need the
arcsin function

so i thought that maybe someone else had become in touch with that
problem,
that´s why i´m asking in that forum (@DD) not for solving my school
homework

and i rather need a quick solution  because i need the correct values
for the parameters!!
```

###### ↳ ↳ ↳ Re: arcsinus

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-01T11:53:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g4d5s5$jo$1@reader2.panix.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com> <g4csvn$cf0$1@reader2.panix.com> <9aed5964-acb0-414b-be71-acd7d8d7a61c@l64g2000hse.googlegroups.com>`

```
In article <9aed5964-acb0-414b-be71-acd7d8d7a61c@l64g2000hse.googlegroups.com>,
mario  <mmc_vw1200@hotmail.com> wrote:
>i need it because of a production parameter of iron helices and
>they are cutted in special angles and for those parameters i  need the
>arcsin function

There are many needs for the arcsin function; that might be a reason that 
easier methods were developed to solve for it.

>
>so i thought that maybe someone else had become in touch with that
>problem,
>that�s why i�m asking in that forum (@DD) not for solving my school
>homework

Homework is not limited to schools.

>
>and i rather need a quick solution  because i need the correct values
>for the parameters!!

Knowledge is power... but information is money.  The information you seek 
is available in the manual (depending, of course, on what version of COBOL 
you are using).

DD
```

###### ↳ ↳ ↳ Re: arcsinus

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-07-01T07:54:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wOpak.8684$89.6187@nlpi069.nbdc.sbc.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com> <g4csvn$cf0$1@reader2.panix.com> <9aed5964-acb0-414b-be71-acd7d8d7a61c@l64g2000hse.googlegroups.com>`

```
"mario" <mmc_vw1200@hotmail.com> wrote in message 
news:9aed5964-acb0-414b-be71-acd7d8d7a61c@l64g2000hse.googlegroups.com...
>i need it because of a production parameter of iron helices and
>they are cutted in special angles and for those parameters i  need the
…[3 more quoted lines elided]…
>for the parameters!!

Someone suggested an iterative solution...

PERFORM VARYING X ..
   E = SIN (X)
  IF E CLOSE ENOUGH TARGET
     EXIT PERFORM
  END-IF
END-PERFORM

.. and I would think you should be able to find a series expansion formula 
for arcsin somewhere on the Internet. Try your favorite search engine with 
"ARCSIN SERIES EXPANSON" and take it from there.

(Hell, if you can have EQUAL and GREATER and LESS operators, why not a CLOSE 
ENOUGH?)
```

###### ↳ ↳ ↳ Re: arcsinus

_(reply depth: 4)_

- **From:** mario <mmc_vw1200@hotmail.com>
- **Date:** 2008-07-01T06:08:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2d7613ab-3b5f-40ec-a0ec-9f84e4d22b5d@m3g2000hsc.googlegroups.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com> <g4csvn$cf0$1@reader2.panix.com> <9aed5964-acb0-414b-be71-acd7d8d7a61c@l64g2000hse.googlegroups.com> <wOpak.8684$89.6187@nlpi069.nbdc.sbc.com>`

```
TKS i´ll try to approximate the value, it this will not be close
enouth i´ll  call a c-programm or something



(dear dd-doc: noone forces you to answer my "stupid" question, so if
you dont want to answer them don´t flame forums with uselss
"information" noone wants to read,
if u dislike my postings pls ignore them or let us talk via mail, i
dont think that other users are interessted in your personal attitude)

all others - THANK you for ur quick help!
```

###### ↳ ↳ ↳ Re: arcsinus

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-07-01T13:31:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g4dbkb$nq4$1@reader2.panix.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com> <9aed5964-acb0-414b-be71-acd7d8d7a61c@l64g2000hse.googlegroups.com> <wOpak.8684$89.6187@nlpi069.nbdc.sbc.com> <2d7613ab-3b5f-40ec-a0ec-9f84e4d22b5d@m3g2000hsc.googlegroups.com>`

```
In article <2d7613ab-3b5f-40ec-a0ec-9f84e4d22b5d@m3g2000hsc.googlegroups.com>,
mario  <mmc_vw1200@hotmail.com> wrote:
>TKS i�ll try to approximate the value, it this will not be close
>enouth i�ll  call a c-programm or something
…[7 more quoted lines elided]…
>dont think that other users are interessted in your personal attitude)

Others can speak for themselves... and other can find information that's 
in manuals.

DD
```

#### ↳ Re: arcsinus

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-07-01T14:19:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N1rak.157985$I42.79281@fe04.news.easynews.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com>`

```
What compiler and operating system are you using?

As someone pointed out MOST current COBOL compilers have the ASIN intrinsic 
function - which is what I think you need/want.
```

#### ↳ Re: arcsinus

- **From:** Robert <no@e.mail>
- **Date:** 2008-07-01T11:59:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h9ok641lahef5ajcl82ergqu0tcccmb5gu@4ax.com>`
- **References:** `<8d606d12-9ca2-4d89-bf76-e11c33d71e74@k37g2000hsf.googlegroups.com>`

```
On Mon, 30 Jun 2008 23:12:41 -0700 (PDT), mario <mmc_vw1200@hotmail.com> wrote:

>Hi i have a big problem!
>
…[4 more quoted lines elided]…
>tks!!!

Cobol programs can call functions in C libraries. They are not limited to Cobol functions.
Just say 

 call 'cos' using (float-long) returniing (flat-long)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
