[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Send email from MVS cobol

_11 messages · 7 participants · 2007-11 → 2009-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Send email from MVS cobol

- **From:** Bill Gentry <billgentry2@hotmail.com>
- **Date:** 2007-11-30T06:56:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com>`

```
Hi All,

Have an interesting challenge.  I have a requirement that dictates
that email be sent from an MVS (z/OS) cobol program.   In
oversimplified terms, this means that I'd read a file that would
contain email addresses and based on various criteria send email to
any number of those addresses.  I know how to send email from JCL, but
require more precision than JCL can give me.

Anyone ever try this?

Thanks
BG
```

#### ↳ Re: Send email from MVS cobol

- **From:** docdwarf@panix.com ()
- **Date:** 2007-11-30T15:05:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fip8s8$o9q$1@reader1.panix.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com>`

```
In article <7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com>,
Bill Gentry  <billgentry2@hotmail.com> wrote:
>Hi All,
>
…[5 more quoted lines elided]…
>require more precision than JCL can give me.

Let me see if I have this straight... you have a dataset containing email 
addresses and you want to select a sub-set of these addresses to which an 
email will be sent?  

It seems like there needs to be something along with the email addresses 
to differentiate them into lists or groups before you can do this.  How 
are the email addresses to be chosen for mailings?

DD
```

##### ↳ ↳ Re: Send email from MVS cobol

- **From:** Bill Gentry <billgentry2@hotmail.com>
- **Date:** 2007-11-30T07:10:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c9435867-fb0c-4e49-8658-f0c77fc67167@d4g2000prg.googlegroups.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com> <fip8s8$o9q$1@reader1.panix.com>`

```
On Nov 30, 10:05 am, docdw...@panix.com () wrote:
> In article <7c04ecdf-2eff-4a68-8d83-9eb9ab08a...@d61g2000hsa.googlegroups.com>,
> Bill Gentry  <billgent...@hotmail.com> wrote:
…[18 more quoted lines elided]…
> DD

Not necessarily.   How I determine who needs to be emailed isn't
entirely relevant.  What i need is a subroutine or operating system
call that'll actually send the email.
```

###### ↳ ↳ ↳ Re: Send email from MVS cobol

- **From:** docdwarf@panix.com ()
- **Date:** 2007-11-30T15:28:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fipa7g$j5i$1@reader1.panix.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com> <fip8s8$o9q$1@reader1.panix.com> <c9435867-fb0c-4e49-8658-f0c77fc67167@d4g2000prg.googlegroups.com>`

```
In article <c9435867-fb0c-4e49-8658-f0c77fc67167@d4g2000prg.googlegroups.com>,
Bill Gentry  <billgentry2@hotmail.com> wrote:
>On Nov 30, 10:05 am, docdw...@panix.com () wrote:
>> In article
…[22 more quoted lines elided]…
>call that'll actually send the email.

I'm still confused.  Using JCL to send mail, in my experience, employs a 
dataset that contains email instructions, like the from:, to: and subject: 
lines.  Your program determines that (address) needs to get an email... so 
(address) gets written to a dataset and then the JCL gets kicked off.

What am I missing?

DD
```

#### ↳ Re: Send email from MVS cobol

- **From:** CG <Carl.Gehr.ButNoSPAMStuff5@MCGCG.Com>
- **Date:** 2007-11-30T10:41:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<23396$47502f26$d06620ed$29399@FUSE.NET>`
- **In-Reply-To:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com>`

```
On 11/30/07 09:56 am, Bill Gentry wrote:
> Hi All,
> 
…[7 more quoted lines elided]…
> Anyone ever try this?

Bill,
While I've never tried it, since you said you know how to do it with 
JCL, a very simplified approach would be to include a DD-statement for 
the JES2 Internal Reader and send the JCL there.  Probably not very 
efficient, but it should work until you find a better way.  [If you're 
using JES3, I assume JES3 has a similar function, but it's been too long 
since I've looked at it.]

Not pretty, but the function is there.
Carl
```

#### ↳ Re: Send email from MVS cobol

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-11-30T09:37:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dte0l3tu2kqv97p82so6gqueg48b47s5pc@4ax.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com>`

```
On Fri, 30 Nov 2007 06:56:09 -0800 (PST), Bill Gentry
<billgentry2@hotmail.com> wrote:

>Have an interesting challenge.  I have a requirement that dictates
>that email be sent from an MVS (z/OS) cobol program.   In
…[3 more quoted lines elided]…
>require more precision than JCL can give me.

I'm guessing your problem is how to run an unknown number of JCL or
procs from the output of your CoBOL extract program.   Is this
correct?
```

##### ↳ ↳ Re: Send email from MVS cobol

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-11-30T11:13:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sjk0l3976ntv9lvbfddg4833ek0klbapjt@4ax.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com> <dte0l3tu2kqv97p82so6gqueg48b47s5pc@4ax.com>`

```
There are some replies you can see in the newsgroup copy of the IBM
listserve.

bit.listserv.ibm-main
```

###### ↳ ↳ ↳ Re: Send email from MVS cobol

- **From:** sro0220@gmail.com
- **Date:** 2007-12-02T13:54:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0b3f684c-d138-481e-9d9b-fd15a3c62b35@l1g2000hsa.googlegroups.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com> <dte0l3tu2kqv97p82so6gqueg48b47s5pc@4ax.com> <sjk0l3976ntv9lvbfddg4833ek0klbapjt@4ax.com>`

```
On Nov 30, 12:13 pm, Howard Brazee <how...@brazee.net> wrote:
> There are some replies you can see in the newsgroup copy of the IBM
> listserve.
>
> bit.listserv.ibm-main

I believe the man just wants to send email from a cobol program on a
ibm mainframe.
isn't there a call from cobol on an ibm machine to do this?
there is on a unisys clearpath.
```

###### ↳ ↳ ↳ Re: Send email from MVS cobol

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-12-03T00:43:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ViI4j.42844$5R1.13354@fe03.news.easynews.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com> <dte0l3tu2kqv97p82so6gqueg48b47s5pc@4ax.com> <sjk0l3976ntv9lvbfddg4833ek0klbapjt@4ax.com> <0b3f684c-d138-481e-9d9b-fd15a3c62b35@l1g2000hsa.googlegroups.com>`

```
There isn't any "IBM-supplied - built-in" call to do this (on MVS).  There are a 
NUMBER of "3rd party products" that will do this (via a call from COBOL) but the 
"traditional" way is to direct the output to the interregnal reader for SMTP 
handling.
```

###### ↳ ↳ ↳ Re: Send email from MVS cobol

_(reply depth: 5)_

- **From:** sro0220@gmail.com
- **Date:** 2007-12-03T19:33:21-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8d693d14-0177-4234-93bd-d03a5403edb4@w34g2000hsg.googlegroups.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com> <dte0l3tu2kqv97p82so6gqueg48b47s5pc@4ax.com> <sjk0l3976ntv9lvbfddg4833ek0klbapjt@4ax.com> <0b3f684c-d138-481e-9d9b-fd15a3c62b35@l1g2000hsa.googlegroups.com> <ViI4j.42844$5R1.13354@fe03.news.easynews.com>`

```
On Dec 2, 6:43 pm, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> There isn't any "IBM-supplied - built-in" call to do this (on MVS).  There are a
> NUMBER of "3rd party products" that will do this (via a call from COBOL) but the
…[22 more quoted lines elided]…
> - Show quoted text -

another shortcoming of an ibm mainframe - or do they call that a
'feature'?
```

#### ↳ Re: Send email from MVS cobol

- **From:** Ubiquitous <weberm@polaris.net>
- **Date:** 2009-10-22T11:21:28-04:00
- **Newsgroups:** alt.cobol,alt.comp.lang.cobol,comp.lang.cobol,ibm.software.cobol
- **Message-ID:** `<BPudncE3TIrk5X3XnZ2dnUVZ_jadnZ2d@giganews.com>`
- **References:** `<7c04ecdf-2eff-4a68-8d83-9eb9ab08a2d3@d61g2000hsa.googlegroups.com>`

```
billgentry2@hotmail.com wrote:

>Have an interesting challenge.  I have a requirement that dictates
>that email be sent from an MVS (z/OS) cobol program.   In
…[5 more quoted lines elided]…
>Anyone ever try this?

Why yes, I do! In fact, I was about to ask an advanced question about sending
email!

I have a JCL set up to email reports by merging the headers and body (report)
and copying it to a file with destination TCPSMTP. This creates an email
which contains a report, but I would like to be able to send a data file
as an email attachment. Has anyone else attempted this?

Thanks,
Ubi
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
