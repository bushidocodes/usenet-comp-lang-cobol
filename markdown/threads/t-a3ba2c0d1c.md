[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Purdue university's solution to the "year 2000 problem"

_8 messages · 7 participants · 1997-04_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Purdue university's solution to the "year 2000 problem"

- **From:** "stephen chai" <ua-author-1945210@usenetarchives.gap>
- **Date:** 1997-04-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<335D3B3F.3395@global.california.com>`

```

Hi, all

I read in the machine design magezine that Purdue University has come up
with a solution to solve the year 2000 problem without having to change
the existing database. All the modifications are done in the existing
program code. However, the article did not say what exactly is the
solution. I was wondering if anyone knows what the secret is.

BTW, I was thinking that the problem can be solved simply by treating
the year 2000 as year 100, 2001 as 101, and so on. That way the
existing data stayed the same, just add code that will interpret year
100 as 2000, 101 as 2001.. Right?

Stephen Chai
sc··.@cal··a.com
```

#### ↳ Re: Purdue university's solution to the "year 2000 problem"

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-04-22T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ba2c0d1c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<335D3B3F.3395@global.california.com>`
- **References:** `<335D3B3F.3395@global.california.com>`

```

In article <335··.@glo··a.com>,
Stephen Chai wrote:

› Hi, all
› 
…[12 more quoted lines elided]…
› sc··.@cal··a.com

look at "The PROGRAMMERS" responce to a y2k self-study ?? a few letters befor this for a very
good discription of the REAL problem.
Greg Amos
amo··.@ix.··m.com
```

#### ↳ Re: Purdue university's solution to the "year 2000 problem"

- **From:** "wbbla..." <ua-author-2262561@usenetarchives.gap>
- **Date:** 1997-04-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ba2c0d1c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<335D3B3F.3395@global.california.com>`
- **References:** `<335D3B3F.3395@global.california.com>`

```


On Tue, 22 Apr 1997 15:27:11 -0700, Stephen Chai
wrote, in part:

› 
› Hi, all
…[11 more quoted lines elided]…
› 


Umm ... Steven, have you ever tried moving a value of 100 to
a 9(2) field? Did it work?



Bill

------------------------ Address Notice ------------------------
Since there are automated programs which mine Usenet posts
for e-mail addresses for junk mail, I have a dummy address
given in the "From:" message field. My actual address is
given in the "Reply-to:" field - if you reply to any message
I send, it will be addressed correctly, to wbb··.@po··x.com
-----------------------------------------------------------------
```

#### ↳ Re: Purdue university's solution to the "year 2000 problem"

- **From:** "joe denicola" <ua-author-17072504@usenetarchives.gap>
- **Date:** 1997-04-23T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ba2c0d1c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<335D3B3F.3395@global.california.com>`
- **References:** `<335D3B3F.3395@global.california.com>`

```

Treating the year 2000 as 100, 2001 as 101, etc. won't work if the date is
being stored in files as YYMMDD in a PIC 9(6) field. You can't fit 101
into a PIC 99.

Stephen Chai wrote in article
<335··.@glo··a.com>...
› Hi, all
› 
…[13 more quoted lines elided]…
›
```

#### ↳ Re: Purdue university's solution to the "year 2000 problem"

- **From:** "fjam..." <ua-author-17071808@usenetarchives.gap>
- **Date:** 1997-04-26T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ba2c0d1c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<335D3B3F.3395@global.california.com>`
- **References:** `<335D3B3F.3395@global.california.com>`

```

In article <335··.@glo··a.com>,
sc··.@glo··a.com says...
› 
› 
…[14 more quoted lines elided]…
› sc··.@cal··a.com

**********************************************************************

This uses a three digit year which is not available in existing
databases which are YYMMDD or even YYJJJ.

It seems that one could take a date like 1930 an consider anything
between 00 and 29 to be 2000 to 2029 and anything from 30 to 99 to be
1930 to 1999. Employees over 70 years of age will have to have their
birtdates resent to 1930. They'll be a few years younger.

Won't work for pension plans and life annuities, but will for
most things.

***********************************************************************

Another approach is to set up a half word binary field which is
the number of years since "year zero" or a full word binary field which
is the number of days since "day zero". Then after full conversion there
is more space in the database instead of less because six character fields
YYMMDD have been replaced with 4 byte binaries.

Frank Jameson

********************************************************************
```

##### ↳ ↳ Re: Purdue university's solution to the "year 2000 problem"

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1997-04-26T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ba2c0d1c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a3ba2c0d1c-p5@usenetarchives.gap>`
- **References:** `<335D3B3F.3395@global.california.com> <gap-a3ba2c0d1c-p5@usenetarchives.gap>`

```

Frank Jameson wrote in article
<5jv7bo$1rn$2.··.@car··c.ca>...

[...snip...]

› 
› 	It seems that one could take a date like 1930 an consider anything
…[20 more quoted lines elided]…
› 

Frank Jameson ??

On your 1930 suggestion: that's the way it's been implemented in the COBOL/400
world, except IBM picked 1940 instead of 1930. It's a fob, but it works...
kinda.

On your HW binary suggestion: that's the way it's been implemented in MS
Access, and Microsoft picked 1/1/0001 as date zero. Only difference is that the
date/time data type is a double, with the date portion (days since 1/1/0001) on
the left side of the decimal, and the time portion (seconds since midnight) on
the right. Works great.

All wonderful implementations & suggestions. Still don't change nothing.
Whichever suggestion is chosen, the implementation will still require
researching each and every one of the thousands of existing programs, to
determine exactly where and how the dates are being used. Then, the logic will
have to be changed to use the new date format. The underlying data in each and
every file (or table) would have to be converted. And, then, every application
system would have to be tested thoroughly to make sure that the fixes applied
haven't broken anything (gleefully ignoring the fact that this process
›› will<< uncover no end of dormant bugs, which will just add to the existing
work load).

So, we're right back to where we started: Y2k -- a misery no matter which way
you slice it.

Of course, once all that converting and changing and testing and verifying is
complete and ready to be rolled into production... ::hehehehehehehe::...

...(::here comes the really messy part that no one in these newsgroups seem to
want to mention... probably because it requires an extra large bottle of
Excederin::)... ... ...

...(::do I even *want* to mention this particular topic in this particular
newsgroup??::)... ... ...

...what about all those years of backup tapes (disks, diskettes, cartridges,
whatever) containing all that non-compliant data and all those non-compliant
programs that everyone has been storing?? Someone, somewhere, is gonna have to
tell upper level management that, suddenly, all the company's backups are now
worthless (in as far as dates go). Think about it. We hit the year 2000, and
don't anyone dare even think about attempting to retrieve information off a
backup made ten years before, because, it ain't gonna work no more. Unless, of
course, all the backup data is also converted (forget about the backup of the
source code) to new versions of backup data.

Yeah, yeah, yeah... I know... buy an extra extra large bottle of Excederin:
some for the IS department, the rest for the execs in the penthouse suites.
```

###### ↳ ↳ ↳ Re: Purdue university's solution to the "year 2000 problem"

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-04-27T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ba2c0d1c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a3ba2c0d1c-p6@usenetarchives.gap>`
- **References:** `<335D3B3F.3395@global.california.com> <gap-a3ba2c0d1c-p5@usenetarchives.gap> <gap-a3ba2c0d1c-p6@usenetarchives.gap>`

```

› Frank Jameson ??
› 
› On your 1930 suggestion: that's the way it's been implemented in the COBOL/400
› world, except IBM picked 1940 instead of 1930. It's a fob, but it works...
› kinda.

Also called Interpretation and by far the CHEAPEST and easiest to impliment, but not a
total solution.
› 
› On your HW binary suggestion: that's the way it's been implemented in MS
…[15 more quoted lines elided]…
› 
 
› Here, Here !!!!!
 
› So, we're right back to where we started: Y2k -- a misery no matter which way
› you slice it.
…[23 more quoted lines elided]…
› 
Just wait untill the IRS or some other agency asks for a archived file from ...oh,
lets see .... 5 years back ....say 1995 ??..... Oh what do you mean you can't
retrieve the info for me? :):):):):):):):):):)
```

###### ↳ ↳ ↳ Re: Purdue university's solution to the "year 2000 problem"

- **From:** "scott hutter" <ua-author-14168@usenetarchives.gap>
- **Date:** 1997-04-28T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a3ba2c0d1c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a3ba2c0d1c-p6@usenetarchives.gap>`
- **References:** `<335D3B3F.3395@global.california.com> <gap-a3ba2c0d1c-p5@usenetarchives.gap> <gap-a3ba2c0d1c-p6@usenetarchives.gap>`

```

Although it may seem a bit hasty, consider that any programs written
that did not consider the year 2000 problem are probably very old code
anyway. My solution to this problem is simple. Buy / write a new
program. And all you programmers should love this solution - it means
BIG JOBS!

Why try to fix old programmer's mistakes and lack of foresight. Take
advantage of this situation to make a real buck.

Besides, having some COBOL education, I would much rather re-write an
entire accounting package in one of the newer languages (VB, Access, or
even the newest versions of COBOL) than to waste my time bleeding
through old, dead, unstructured code.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
