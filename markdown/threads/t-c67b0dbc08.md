[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Find job-name etc in a cobol program?

_6 messages · 3 participants · 2003-03_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs)

---

### Find job-name etc in a cobol program?

- **From:** Einar Clementz <eclementz@bigfoot.com>
- **Date:** 2003-03-25T15:02:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E80615E.3030908@bigfoot.com>`

```
Hi.

I remember once seeing a cobol program on this group that found the 
MVS-id, job-name etc. Now I need this feature and cannot find back to it.

Does anyone know about how this can be done?


Thanx, Einar Clementz, Oslo, Norway
```

#### ↳ Re: Find job-name etc in a cobol program?

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-03-25T11:11:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DC9CDA8FDD9D3697.DD616700C0FCAAA1.8A01390C9EEF31CD@lp.airnews.net>`
- **References:** `<3E80615E.3030908@bigfoot.com>`

```
On Tue, 25 Mar 2003 15:02:06 +0100, Einar Clementz
<eclementz@bigfoot.com> enlightened us:

>Hi.
>
…[6 more quoted lines elided]…
>Thanx, Einar Clementz, Oslo, Norway

Originally written by CLC member Gilbert Saint-flour, here it is:

      Identification Division.
         Program-ID. Cob2Job.
         Author. Gilbert Saint-flour. 
       Data Division.
        Working-Storage Section.
         01 job-name Pic x(8).
         01 proc-step Pic x(8).
         01 step-name Pic x(8).
         01 job-number Pic x(8).
         01 program-name Pic x(8).
         01 user-id Pic x(8).
         01 group-name Pic x(8).
         01 user-name Pic x(20).
         01 four-bytes. 05 full-word Pic s9(8) Comp.
        Linkage Section.
         01 cb1.  05 ptr1 Pointer Occurs 256.
         01 cb2.  05 ptr2 Pointer Occurs 256.
       Procedure Division.
 PSA       SET Address Of cb1 To NULL.
 TCB       SET Address Of cb1 To ptr1(136)
 TIOT      SET Address Of cb2 To ptr1(4)
           MOVE cb2(1:8) To job-name
           MOVE cb2(9:8) To proc-step
           MOVE cb2(17:8) To step-name
 JSCB      SET Address Of cb2 To ptr1(46)
           MOVE cb2(361:8) To program-name
 SSIB      SET Address Of cb2 To ptr2(80)
           MOVE cb2(13:8) To job-number
 PSA       SET Address Of cb1 To NULL.
 ASCB      SET Address Of cb1 To ptr1(138)
 ASXB      SET Address Of cb2 To ptr1(28)
           MOVE cb2(193:8) To user-id
 ACEE      SET Address Of cb2 To ptr2(51)
           MOVE cb2(31:8) To group-name
 UNAM      SET Address Of cb1 To ptr2(26)
           MOVE zero to full-word.
           MOVE cb1(1:1) To four-bytes(4:1)
           MOVE cb1(2:full-word) To user-name
           DISPLAY job-name ' '
                   proc-step ' '
                   step-name ' '
                   job-number ' '
                   program-name ' '
                   user-id ' '
                   group-name  ' '
                   user-name  ' '
           GOBACK.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #111

The Tao that is seen
Is not the true Tao - until
You bring fresh toner.
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: Find job-name etc in a cobol program?

- **From:** Einar Clementz <eclementz@bigfoot.com>
- **Date:** 2003-03-25T17:29:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E8083F0.80600@bigfoot.com>`
- **References:** `<3E80615E.3030908@bigfoot.com> <DC9CDA8FDD9D3697.DD616700C0FCAAA1.8A01390C9EEF31CD@lp.airnews.net>`

```
Thanx for this fast respone

Cheers, Einar


SkippyPB wrote:
> On Tue, 25 Mar 2003 15:02:06 +0100, Einar Clementz
> <eclementz@bigfoot.com> enlightened us:
…[79 more quoted lines elided]…
> Steve
```

##### ↳ ↳ Re: Find job-name etc in a cobol program?

- **From:** Einar Clementz <eclementz@bigfoot.com>
- **Date:** 2003-03-26T17:20:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E81D362.3000607@bigfoot.com>`
- **References:** `<3E80615E.3030908@bigfoot.com> <DC9CDA8FDD9D3697.DD616700C0FCAAA1.8A01390C9EEF31CD@lp.airnews.net>`

```
Hi group

I have a follow up question.
Is it possible to find what type of subsystem the program is running under?
Is it CICS, IMS, TSO batch, batch?

We try to set up a submodule to give the real environment. Then we can 
choose what kind if interface stubs to use against MQ in this case. But 
this will certainly be usefull in other situations.

Thanx, Einar Clementz, Oslo, Norway
---------------

SkippyPB wrote:
> On Tue, 25 Mar 2003 15:02:06 +0100, Einar Clementz
> <eclementz@bigfoot.com> enlightened us:
…[79 more quoted lines elided]…
> Steve
```

###### ↳ ↳ ↳ Re: Find job-name etc in a cobol program?

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-03-27T08:11:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-0A9B2B.08110127032003@corp.supernews.com>`
- **References:** `<3E80615E.3030908@bigfoot.com> <DC9CDA8FDD9D3697.DD616700C0FCAAA1.8A01390C9EEF31CD@lp.airnews.net> <3E81D362.3000607@bigfoot.com>`

```
In article <3E81D362.3000607@bigfoot.com>,
 Einar Clementz <eclementz@bigfoot.com> wrote:

> Hi group
> 
…[6 more quoted lines elided]…
> this will certainly be usefull in other situations.


If you use the program name out of the JSCB it should tell you.  CICS is 
DFHSIP, TSO is IKJFT??, IMS is DFS??000 -- I can't remember the exact 
names, but a quick look at that will give you your environment.
```

###### ↳ ↳ ↳ Re: Find job-name etc in a cobol program?

_(reply depth: 4)_

- **From:** Einar Clementz <eclementz@bigfoot.com>
- **Date:** 2003-03-27T15:29:36+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E830AD0.2060207@bigfoot.com>`
- **References:** `<3E80615E.3030908@bigfoot.com> <DC9CDA8FDD9D3697.DD616700C0FCAAA1.8A01390C9EEF31CD@lp.airnews.net> <3E81D362.3000607@bigfoot.com> <joe_zitzelberger-0A9B2B.08110127032003@corp.supernews.com>`

```
Certainly. One of those "why did I not think of that"

Thanx, Einar

-----------------
Joe Zitzelberger wrote:
> In article <3E81D362.3000607@bigfoot.com>,
>  Einar Clementz <eclementz@bigfoot.com> wrote:
…[16 more quoted lines elided]…
> names, but a quick look at that will give you your environment.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
