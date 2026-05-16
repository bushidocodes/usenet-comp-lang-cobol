[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help With Cobol Syntax

_6 messages · 6 participants · 1998-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help With Cobol Syntax

- **From:** limlc@purdue.edu (Lim)
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a37769.5097377@news.purdue.edu>`

```
Hi,
Need some advice.. What's the easiest way to check each and every
character and make sure it's alphbet.  The word is stored in a PIC X.
How can I go from character to character?
Thanks
L.C. Lim
```

#### ↳ Re: Help With Cobol Syntax

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a37a3f.0@news1.ibm.net>`
- **References:** `<35a37769.5097377@news.purdue.edu>`

```

Lim wrote in message <35a37769.5097377@news.purdue.edu>...
>Need some advice.. What's the easiest way to check each and every
>character and make sure it's alphbet.  The word is stored in a PIC X.
>How can I go from character to character?


01  test-me-ok                   pic x(20)   value "is alphabetic".
01  test-me-not-ok            pic x(20)   value "a'int alphabetic".

if test-me-ok is  alphabetic
     perform xxxx
.
if test-me-not-ok is not alphabetic
     perform zzzz
```

#### ↳ Re: Help With Cobol Syntax

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998070813574900.JAA06390@ladder03.news.aol.com>`
- **References:** `<35a37769.5097377@news.purdue.edu>`

```
L.C.Lim writes ...

>Hi,
>Need some advice.. What's the easiest way to check each and every
>character and make sure it's alphbet.  The word is stored in a PIC X.
>How can I go from character to character?
>Thanks

Sounds like homework to me. We don't generally do homework for people. But
here's a hint: alphabetic, alphabetic-lower, alphabetic-upper.

Cheers,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Help With Cobol Syntax

- **From:** docdwarf@clark.net ()
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o00r4$at4$1@clarknet.clark.net>`
- **References:** `<35a37769.5097377@news.purdue.edu>`

```
In article <35a37769.5097377@news.purdue.edu>, Lim <limlc@purdue.edu> wrote:
>Hi,
>Need some advice.. What's the easiest way to check each and every
…[3 more quoted lines elided]…
>L.C. Lim

Please do your own homework.

DD
```

#### ↳ Re: Help With Cobol Syntax

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o0329$160$1@juliana.sprynet.com>`
- **References:** `<35a37769.5097377@news.purdue.edu>`

```
Lim,

    The ALPHABETIC test will be true if the field contains any Alphabetic
Character as well as a SPACE.

    Subsequently, I believe you could test the field for ALPHABETIC and NOT
EQUAL TO SPACE to ensure Alphabetic only.

Cheers,

WOB,
Atlanta

Lim wrote in message <35a37769.5097377@news.purdue.edu>...
>Hi,
>Need some advice.. What's the easiest way to check each and every
…[3 more quoted lines elided]…
>L.C. Lim
```

##### ↳ ↳ Re: Help With Cobol Syntax

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-8d5Ib0wJ9Nbb@Dwight_Miller.iix.com>`
- **References:** `<35a37769.5097377@news.purdue.edu> <6o0329$160$1@juliana.sprynet.com>`

```
On Wed, 8 Jul 1998 18:26:59, "WOB" <wobconsult@sprynet.com> wrote:

> Lim,
> 
…[5 more quoted lines elided]…
> 

BZZZZT.  Wrong.  that would mean that the field could contain embedded
spaces and still be considered alphabetic.

One way is to change the spaces to something else with an inspect then
do the alphabetic test.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
