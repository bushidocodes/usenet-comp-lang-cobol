[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EBCDIC to ASCII translation for Mainframe Express

_3 messages · 2 participants · 2007-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### EBCDIC to ASCII translation for Mainframe Express

- **From:** "Panos Zotos" <pzotos@syntax.gr>
- **Date:** 2007-01-08T20:54:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Rbyoh.103224$uv5.1379914@twister1.libero.it>`

```
Hi,

I am using Micro Focus Mainframe Express 3.0 and I am trying to setup a 
custom translation table that will map IBM's EBCDIC 875 table (Greek EBCDIC) 
to Windows 1253 (Greek ANSI). My objective is to create a map file that will 
be compiled via the CODECOMP utility. So far I have searched the internet 
and found a few 875 <--> 1253 tables but none of them is complete, covering 
all 256 characters and a few runtime errors I get from MFE make me suspect 
that the incomplete or inaccurate mapping are the cause.

I wonder if someone knows any internet source where I could possibly find a 
complete 875 to 1253 translation table. Moreover, I would appreciate if 
someone that has gone through the same task for any non-English language, 
could offer any advice for things that need to be considered.

Regards
Panos Zotos
(Athens, Greece)
```

#### ↳ Re: EBCDIC to ASCII translation for Mainframe Express

- **From:** "Brian Crane" <brian.crane@microfocus.com>
- **Date:** 2007-01-10T11:16:07
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12q9iqukn849j77@corp.supernews.com>`
- **References:** `<Rbyoh.103224$uv5.1379914@twister1.libero.it>`

```
Hi Panos,

I've just been speaking to a couple of people here at Micro Focus. We 
remember discussing this topic with you last year, but we suspect that 
something else could be causing your runtime errors, so it would be worth 
logging a call with SupportLine to check this out.

Best regards,

Brian Crane
Product Director, Micro Focus.




"Panos Zotos" <pzotos@syntax.gr> wrote in message 
news:Rbyoh.103224$uv5.1379914@twister1.libero.it...
> Hi,
>
…[17 more quoted lines elided]…
>
```

#### ↳ Re: EBCDIC to ASCII translation for Mainframe Express

- **From:** "Brian Crane" <brian.crane@microfocus.com>
- **Date:** 2007-01-10T11:17:46
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12q9iqvjkhip179@corp.supernews.com>`
- **References:** `<Rbyoh.103224$uv5.1379914@twister1.libero.it>`

```
Hi Panos,

I've just been speaking to a couple of people here at Micro Focus. We
remember discussing this topic with you last year, but we suspect that
something else could be causing your runtime errors, so it would be worth
logging a call with SupportLine to check this out.

Best regards,

Brian Crane
Product Director, Micro Focus.




"Panos Zotos" <pzotos@syntax.gr> wrote in message
news:Rbyoh.103224$uv5.1379914@twister1.libero.it...
> Hi,
>
…[17 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
