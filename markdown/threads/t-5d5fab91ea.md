[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MICROFOCUS COBOL YEAR 2000 COMPLIANCY PROBLEMS??

_6 messages · 5 participants · 1998-02_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### MICROFOCUS COBOL YEAR 2000 COMPLIANCY PROBLEMS??

- **From:** "mr scott" <ua-author-3874961@usenetarchives.gap>
- **Date:** 1998-02-04T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6bddm1$qvs@news2.force9.net>`

```

Is MF COBOL fully year 2000 compliant??

When we use the WB 4.0 function CBL_CHECK_FILE_EXIST with a file with an
amendment date greater than 01/01/2000 the program crashes with a run-time
error "119 - Memory Out Of Bounds".

We are using NT 4 with UK Locale settings - with all the latest patches and
service packs applied to NT and WB.

Is this a problem anybody else has experienced (if even checked for yet), or
is it something peculiar to us?
Microfocus support seemed to be unaware of any such problem so it *may* be
peculiar to us - if not it is a very MAJOR bug.
```

#### ↳ Re: MICROFOCUS COBOL YEAR 2000 COMPLIANCY PROBLEMS??

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1998-02-05T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d5fab91ea-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6bddm1$qvs@news2.force9.net>`
- **References:** `<6bddm1$qvs@news2.force9.net>`

```

Hi.

Mr Scott wrote:
› When we use the WB 4.0 function CBL_CHECK_FILE_EXIST with a file with an
› amendment date greater than 01/01/2000 the program crashes with a run-time
› error "119 - Memory Out Of Bounds".
 
› Do you mean "119 - Symbol Redefined" or "114 - Memory Out Of Bounds" ?
 
› Is this a problem anybody else has experienced (if even checked for yet), or
› is it something peculiar to us?
› Microfocus support seemed to be unaware of any such problem so it *may* be
› peculiar to us - if not it is a very MAJOR bug.

There was a problem with CBL_CHECK_FILE_EXIST giving a 114 error with WB
4.0.
This was due to a limitation in the ANSI C library date routines (which
will
only cope with dates up to the year 2038), and was fixed in the latest
release
of Workbench (4.0.32).

We have tried to reproduce this at Micro Focus with 4.0.32, and cannot
get it
to fail. To help resolve this, can you please do the following:

1) Clarify which RTS error you are getting.
2) Confirm that a date of 2-Jan-2000 will give this error (or is it only
dates
greater than 2038) ?
3) Give the *full* version of WB 4.0 that you are using.
4) Give the *full* version/build/service pack number of NT you are
using.
5) Post a small example program which reproduces the problem every time.
Include details as to the exact way you changed the date/time on the
file.

Cheers,
Kev.

PS. In response to your initial question, please visit:

http://www.microfocus.com/year2000/y2katmf.htm
```

#### ↳ Re: MICROFOCUS COBOL YEAR 2000 COMPLIANCY PROBLEMS??

- **From:** "m..." <ua-author-1148957@usenetarchives.gap>
- **Date:** 1998-02-05T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d5fab91ea-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6bddm1$qvs@news2.force9.net>`
- **References:** `<6bddm1$qvs@news2.force9.net>`

```

"Mr Scott" wrote:

› Is MF COBOL fully year 2000 compliant??
› 
…[3 more quoted lines elided]…
› 

I think this was actually a problem with C libraries which our COBOL
run time was using. I believe we worked around the problem in the
COBOL Workbench V4.0.32 update.

You don't say which version you're using, if it is V4.0.32, my
apologies and please raise it with your local support representative.

Regards,
Mark Warren
Micro Focus
Micro Focus Ltd., The Lawn, Old Bath Rd., Newbury, Berks. UK RG14 1QN
```

##### ↳ ↳ Re: MICROFOCUS COBOL YEAR 2000 COMPLIANCY PROBLEMS??

- **From:** "mr scott" <ua-author-3874961@usenetarchives.gap>
- **Date:** 1998-02-07T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d5fab91ea-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5d5fab91ea-p3@usenetarchives.gap>`
- **References:** `<6bddm1$qvs@news2.force9.net> <gap-5d5fab91ea-p3@usenetarchives.gap>`

```

Mark Warren wrote in message <34db1ec1.20362263@hyperion>...
›› When we use the WB 4.0 function CBL_CHECK_FILE_EXIST with a file with an
›› amendment date greater than 01/01/2000 the program crashes with a run-time
…[7 more quoted lines elided]…
› apologies and please raise it with your local support representative.


We certainly have 4.0.32 but I will check with the developer to find out.
We already raised it with MF UK who seemed to know nothing about the error,
until we phoned back after dicovering the caused aftre 2 days of
investigation.

The quality of telephone support in the UK is appalling.
```

#### ↳ Re: MICROFOCUS COBOL YEAR 2000 COMPLIANCY PROBLEMS??

- **From:** "john karr" <ua-author-6589171@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d5fab91ea-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6bddm1$qvs@news2.force9.net>`
- **References:** `<6bddm1$qvs@news2.force9.net>`

```


Hello:

>From 1988 to 1990 I did COBOL programming in an IBM system 34 environment.
Then I spent the next 4 years teaching at the high school level.
Eventually I decided to return to the field of computers. I am using two
main strategies to achieve this goal.

In 1995 I started an MBA (MIS concentration at University of Connecticut)
and completed same in December 1997. Because of the current huge demand for
COBOL programmers I plan to resume programming in this language.

But first I would like to familiarize myself with my new environment. I am
therefore contemplating a one week attachment ( as an apprentice to someone
who is already in the field) before launching out on my own. SALARY NOT
NECESSARY DURING ATTACHMENT!

If this Ad. catches your eye then please email me ASAP for a copy of my
resume and cover letter .

I have included a copy of my resume and a cover letter below for your
convenience.


Thanks,
```

##### ↳ ↳ Re: MICROFOCUS COBOL YEAR 2000 COMPLIANCY PROBLEMS??

- **From:** "randy van de loo" <ua-author-6589188@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5d5fab91ea-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5d5fab91ea-p5@usenetarchives.gap>`
- **References:** `<6bddm1$qvs@news2.force9.net> <gap-5d5fab91ea-p5@usenetarchives.gap>`

```

› From 1988 to 1990 I did COBOL programming in an IBM system 34 environment.
› Then I spent the next 4 years teaching at the high school level.
› Eventually I decided to return to the field of computers.  I am using two
› main strategies to achieve this goal.
 
› Because of the current huge demand for
› COBOL programmers I plan to resume programming in this language.
 
› But first I would like to familiarize myself with my new environment.  I am
› therefore contemplating a one week attachment ( as an apprentice to someone
…[4 more quoted lines elided]…
› resume and cover letter .


Hmmmm.. So, one of us is supposed to take you under our wing for a week
and show you which ropes ring what bells and then we can turn you loose
on the world. And. As a side benefit you will require NO SALARY for
this week of "receipt of mentorship". During this week our productivity
will drop considerably. I am curious as to how much this training would
be worth to you? Understanding that you are a "pretty quick study" are
you still certain that one week would be sufficient? There aren't that
many System 34's around these days. AS400's are around but you don't
see/read a lot of ads requiring programmers for them.

---------------------------------------------
> Randy  Van de Loo  -  PRO/teus Technology <
> remove NOSPAM from E-mail address before  <
> replying.                                 <
---------------------------------------------
Bait for spammers (With credit to E. Needham):
root@localhost
postmaster@localhost
admin@localhost
abuse@localhost
pos··.@127··0.1
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
