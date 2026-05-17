[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling COBOL programs from REXX

_6 messages · 3 participants · 1996-11_

---

### Calling COBOL programs from REXX

- **From:** "10057..." <ua-author-463630@usenetarchives.gap>
- **Date:** 1996-11-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<329c9b07.250436175@news.compuserve.co.uk>`

```

I have developed a method of calling COBOL programs from REXX (in an
IBM/MVS/TSO environment). If anyone is interested, then please e-mail
me for details.

If there is enough interest, I will post it to these newsgroups.
```

#### ↳ Re: Calling COBOL programs from REXX

- **From:** "binyami..." <ua-author-932190@usenetarchives.gap>
- **Date:** 1996-11-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2e11eae94a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<329c9b07.250436175@news.compuserve.co.uk>`
- **References:** `<329c9b07.250436175@news.compuserve.co.uk>`

```

On Wed, 27 Nov 1996 19:51:21 GMT 100··.@com··e.com (Ken MacKenzie)
wrote:

[Posted and mailed]

:>I have developed a method of calling COBOL programs from REXX (in an
:>IBM/MVS/TSO environment). If anyone is interested, then please e-mail
:>me for details.

Wouldn't there be two easy ways:

ADDRESS TSO "CALL 'lib(pgm)' '"parms"'"

and

ADDRESS LINKMVS "pgm parms"

:>If there is enough interest, I will post it to these newsgroups.

Curious to know what is unique about your approach.

:>--
:>Ken MacKenzie
```

##### ↳ ↳ Re: Calling COBOL programs from REXX

- **From:** "10057..." <ua-author-463630@usenetarchives.gap>
- **Date:** 1996-11-27T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2e11eae94a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2e11eae94a-p2@usenetarchives.gap>`
- **References:** `<329c9b07.250436175@news.compuserve.co.uk> <gap-2e11eae94a-p2@usenetarchives.gap>`

```

Bin··.@the··e.net (Binyamin Dissen) wrote:

› On Wed, 27 Nov 1996 19:51:21 GMT 100··.@com··e.com (Ken MacKenzie)
› wrote:
…[26 more quoted lines elided]…
› Director, Dissen Software, Bar & Grill - Israel
Sorry, I didn't make my message clear enough. What I meant was, my
routine will allow you to call a COBOL program as a REXX
function/subroutine. The COBOL program will have access to the EFPL
and will be able to return a result.
```

#### ↳ Re: Calling COBOL programs from REXX

- **From:** "neid..." <ua-author-16069100@usenetarchives.gap>
- **Date:** 1996-11-28T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2e11eae94a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<329c9b07.250436175@news.compuserve.co.uk>`
- **References:** `<329c9b07.250436175@news.compuserve.co.uk>`

```

In <329··.@new··o.uk>, 100··.@com··e.com (Ken MacKenzie) writes:
› I have developed a method of calling COBOL programs from REXX (in an
› IBM/MVS/TSO environment).  If anyone is interested, then please e-mail
› me for details.
› 
› If there is enough interest, I will post it to these newsgroups.
Post it

Peter
```

#### ↳ Re: Calling COBOL programs from REXX

- **From:** "10057..." <ua-author-463630@usenetarchives.gap>
- **Date:** 1996-11-29T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2e11eae94a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<329c9b07.250436175@news.compuserve.co.uk>`
- **References:** `<329c9b07.250436175@news.compuserve.co.uk>`

```

It seems that there is enough interest, so here goes.
I am sending the actual code as an attachment. I have never done this before
so, be prepared for me getting it wrong!

Note that I recommend a dynamic call but, it's up to you
how you do it. Of course, the assumption is that you are using COBOL2 or
COBOL/370.

Have fun - if you need to allocate a return area (EVALBLOCK) bigger than 250
bytes and are not sure how, just drop me a line and I will help you out.

The next thing I will investigate is the use of "shared variables", this will
allow me to manipulate REXX variables within my COBOL programs. Watch this
space ...
```

#### ↳ Re: Calling COBOL programs from REXX

- **From:** "10057..." <ua-author-463630@usenetarchives.gap>
- **Date:** 1996-11-29T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2e11eae94a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<329c9b07.250436175@news.compuserve.co.uk>`
- **References:** `<329c9b07.250436175@news.compuserve.co.uk>`

```

begin 644 rxefpl.txt

0("`@("`@("`@("`@("`-"@``
`
end
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
