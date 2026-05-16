[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Job name

_5 messages · 5 participants · 1998-07_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs)

---

### Job name

- **From:** "Svein Gr���e" <svein.grae@fou.telenor.no>
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6nvsse$s1k@info.telenor.no>`

```
Hi,

I would like to know if there is a simple way to obtain the job name
dynamically from a Cobol program. The environment is OS390 and Cobol II. A
solution is of course to write an assembly routine which I can call from my
program, but assembly programmers are so hard to come across these days.
Hope someone can help.

Svein Gr�e
```

#### ↳ Re: Job name

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o01i9$qn2$1@juliana.sprynet.com>`
- **References:** `<6nvsse$s1k@info.telenor.no>`

```
Svein,

    I'm unaware as to how to obtain this information from COBOL.

    Why not submit your question to the comp.lang.asm370 Mainframe ASSEMBLER
newsgroup.

Cheers,

WOB,
Atlanta

Svein Gr�e wrote in message <6nvsse$s1k@info.telenor.no>...
>Hi,
>
…[8 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Job name

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a3a924.0@news1.ibm.net>`
- **References:** `<6nvsse$s1k@info.telenor.no> <6o01i9$qn2$1@juliana.sprynet.com>`

```

WOB wrote in message <6o01i9$qn2$1@juliana.sprynet.com>...
>    I'm unaware as to how to obtain this information from COBOL.
>Svein Gr�e wrote in message <6nvsse$s1k@info.telenor.no>...
…[4 more quoted lines elided]…
>>solution is of course to write an assembly routine which I can call from
my
>>program, but assembly programmers are so hard to come across these days.

I think there was a post to the Cobol newsgroup with a solution to this
problem a couple of weeks ago. Try to search back thru old stuff.
```

##### ↳ ↳ Re: Job name

- **From:** "AM" <AM69107@glaxowellcome.com>
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdaa88$def58b30$c58c3398@us0071826>`
- **References:** `<6nvsse$s1k@info.telenor.no> <6o01i9$qn2$1@juliana.sprynet.com>`

```
this came from another thread...  it helped me... hope it does the same for
you...


       Identification Division.
         Program-ID. Cob2Job.
         Author. Gilbert Saint-flour <gsf@ibm.net>.
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


WOB <wobconsult@sprynet.com> wrote in article
<6o01i9$qn2$1@juliana.sprynet.com>...
| Svein,
| 
|     I'm unaware as to how to obtain this information from COBOL.
| 
|     Why not submit your question to the comp.lang.asm370 Mainframe
ASSEMBLER
| newsgroup.
| 
…[9 more quoted lines elided]…
| >dynamically from a Cobol program. The environment is OS390 and Cobol II.
A
| >solution is of course to write an assembly routine which I can call from
my
| >program, but assembly programmers are so hard to come across these days.
| >Hope someone can help.
…[6 more quoted lines elided]…
|
```

#### ↳ Re: Job name

- **From:** zberger@ldl.net
- **Date:** 1998-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o5hgr$k7l$1@nnrp1.dejanews.com>`
- **References:** `<6nvsse$s1k@info.telenor.no>`

```
In article <6nvsse$s1k@info.telenor.no>,
  "Svein Gr�e" <svein.grae@fou.telenor.no> wrote:
> Hi,
>
…[8 more quoted lines elided]…
> this one is easy:

working-storage section.
01 cvt.
 02 cvt-addr pic s9(8) comp value +16.
 02 cvt-ptr  pointer redefines cvt-addr.

linkage section.
01 ptrs.
 02 ptr-area.
  03 ptr-0  pointer.
  03 ptr-4  pointer.
  03 ptr-8  pointer.
  03 ptr-12 pointer.
 02 dat-area redefines ptr-area.
  03 jobname  pic x(8).
  03 procname pic x(8).
  03 stepname pic x(8).

procedure division.

* address communications vector table
  set address of ptrs to cvt-ptr

* address task control block list
  set address of ptrs to ptr-0

* address current tcb
  set address of ptrs to ptr-0

* address tiot
  set address of ptrs to ptr-0

  display 'jobname  : ' jobname
  display 'procname : ' procname
  display 'stepname : ' stepname
  goback

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
