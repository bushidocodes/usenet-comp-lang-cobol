[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Program errors

_3 messages · 3 participants · 2001-08_

---

### Program errors

- **From:** pa@schaubroeck.be (Peter Alluyn)
- **Date:** 2001-08-23T09:08:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b84c532.11660138@news.eunet.be>`

```
Hello,

A cobol program on a unix machine gives me the following error message


--------------------------------------------------------------------------------
Date : 23/08/2001  Time  : 10:17:46
Execution error : file './name of the program
error code: 114, pc=320, call=15, seg=0
114     Attempt to access item beyond bounds of memory (Signal11) 
key to continue...

Can I retrieve the line of the cobol program on wich the error occured
with these information (pc=320, call=15, seg=0). ?????


Thanks Peter
```

#### ↳ Re: Program errors

- **From:** "Robert Sales" <Robert.Sales@merant.com>
- **Date:** 2001-08-23T12:22:01+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9m2ped$a5h$1@hyperion.eu.merant.com>`
- **References:** `<3b84c532.11660138@news.eunet.be>`

```
The error looks as though this is a Micro Focus compiler - probably the
easiest approach is to use the Animator to debug through the program.  If
this error arises during an animation session execution should stop with the
offending line highlighted.

"Peter Alluyn" <pa@schaubroeck.be> wrote in message
news:3b84c532.11660138@news.eunet.be...
> Hello,
>
…[3 more quoted lines elided]…
> --------------------------------------------------------------------------
------
> Date : 23/08/2001  Time  : 10:17:46
> Execution error : file './name of the program
…[8 more quoted lines elided]…
> Thanks Peter
```

#### ↳ Re: Program errors

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-08-23T17:08:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B853951.DE95F338@home.com>`
- **References:** `<3b84c532.11660138@news.eunet.be>`

```


Peter Alluyn wrote:

> Hello,
>
…[12 more quoted lines elided]…
> Thanks Peter

As Robert said it looks suspiciously like you are using a Micro Focus compiler. As
suggested  use the Animator. A likely cause is a screw-up on your Linkage section
using and returning parameters - all sorts of combinations, so these are just some
:-

    - call xyz using One(pic x(12), Two(pic 9(03)) returning Three(Three being a
        Level 01, 05 pic x(06) and 05 pic 9(02))
    - OR call xyz returning Three
    xyz - Linkage Section
             01  One
             01 Three
            Procedure Division using One, Two returning Three

OR

            Procedure Division using Two returning Three

I could go on an on, but likely a combination of the above having 'extras', leaving
out some, not returning or returning and not correct info at 05 Levels.

Some of the above the compiler catches like Procedure header Linkage is checked
against Linkage section  - but it isn't aware of what you are doing between
programs.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
