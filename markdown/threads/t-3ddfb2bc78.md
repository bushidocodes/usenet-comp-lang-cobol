[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cut/Paste in ISPF

_6 messages · 5 participants · 1999-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Cut/Paste in ISPF

- **From:** john_mindock@my-deja.com
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tikll$3n$1@nnrp1.deja.com>`

```
At my last two code-bustin' stops, the ISPF option 2 permitted a poor
typist to CC/CC some lines from PDS member 1, then type 'CUT' on top,
then PASTE them (A)fter a line in PDS member 2.
Where I'm currently at, it complains about typing CUT on top.
I vaguely remember setting some option when I started at a previous
client's office, but can't find anything that looks pertinent at this
one.
Any clues?
Help appreciated in advance.

John



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Cut/Paste in ISPF

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37FCDAD7.F4A@saif.com>`
- **References:** `<7tikll$3n$1@nnrp1.deja.com>`

```
john_mindock@my-deja.com wrote:
> 
> At my last two code-bustin' stops, the ISPF option 2 permitted a poor
…[12 more quoted lines elided]…
> Before you buy.


Yea, CUT and PASTE are two REXX EXECs you need to install.

you can e-mail me at petwir@saif.com if you want me to ship you a copy. 
(Use at your own risk, of course!)

Pete
```

##### ↳ ↳ Re: Cut/Paste in ISPF

- **From:** john_mindock@my-deja.com
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tit6b$6m1$1@nnrp1.deja.com>`
- **References:** `<7tikll$3n$1@nnrp1.deja.com> <37FCDAD7.F4A@saif.com>`

```
In article <37FCDAD7.F4A@saif.com>,
  petwir@saif.com wrote:
> john_mindock@my-deja.com wrote:
> >
…[4 more quoted lines elided]…
> you can e-mail me at petwir@saif.com if you want me to ship you a
copy.
> (Use at your own risk, of course!)
>
> Pete
>
Thanks for the response/offer - can't bring in any alien code here.
The grunt PC method works page by page so we can fall back to that or
other kludgy activities.
John


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Cut/Paste in ISPF

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BMr9N3y5GusQVZmIuTy0Pw33DBmI@4ax.com>`
- **References:** `<7tikll$3n$1@nnrp1.deja.com> <37FCDAD7.F4A@saif.com> <7tit6b$6m1$1@nnrp1.deja.com>`

```
On Thu, 07 Oct 1999 19:44:14 GMT john_mindock@my-deja.com wrote:

:>In article <37FCDAD7.F4A@saif.com>,
:>  petwir@saif.com wrote:
:>> john_mindock@my-deja.com wrote:

:>> Yea, CUT and PASTE are two REXX EXECs you need to install.

:>> you can e-mail me at petwir@saif.com if you want me to ship you a
:>copy.
:>> (Use at your own risk, of course!)

:>Thanks for the response/offer - can't bring in any alien code here.
:>The grunt PC method works page by page so we can fall back to that or
:>other kludgy activities.

Code is in ISRCUT and ISRPASTE in SYS1.SISPSAMP.

Alias them and add to your SYSEXEC.
```

#### ↳ Re: Cut/Paste in ISPF

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991007151144.22841.00000056@ng-fd1.aol.com>`
- **References:** `<7tikll$3n$1@nnrp1.deja.com>`

```
john_mindock writes...



>At my last two code-bustin' stops, the ISPF option 2 permitted a poor
>typist to CC/CC some lines from PDS member 1, then type 'CUT' on top,
…[6 more quoted lines elided]…
>Help appreciated in advance.

First, I always taught my students the proper way was to do a block copy
(cc...cc) followed by a "create temp" command in the source file, then get into
the target file, place an 'a' or 'b' (after or before) in the line number then
enter "move temp". This copied in the created lines and then deleted the 'temp'
member.

I did this because not every shop installed the CUT and PASTE execs.

Many emulators support cut and paste using the mouse.

Now, in the new version of ISPF (available this month) CUT and PASTE are now
standard primary commands. For shops that used the CUT and PASTE execs, you
might watch out for command conflicts when you install the new ISPF.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: Cut/Paste in ISPF

- **From:** "Dave Sanders" <davesanders@fuse.net>
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rvsrckthh1s71@corp.supernews.com>`
- **References:** `<7tikll$3n$1@nnrp1.deja.com> <19991007151144.22841.00000056@ng-fd1.aol.com>`

```
FWIW, with PC/3270, I modified the keyboard layout to specify ctrl-C &
ctrl-V as COPY & PASTE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
