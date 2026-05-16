[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable Rcord Length

_3 messages · 3 participants · 2000-10_

---

### Variable Rcord Length

- **From:** "NICHOLAS CREMIDIS" <NICK.CREMIDIS@prodigy.net>
- **Date:** 2000-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8sd8nf$6hmg$1@newssvr05-en0.news.prodigy.com>`

```

Hi folks;

I need help in reading and writing a variablke record length file....

Thanks

Pedro
```

#### ↳ Re: Variable Rcord Length

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2000-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8sdamp$4eb$1@nnrp1.deja.com>`
- **References:** `<8sd8nf$6hmg$1@newssvr05-en0.news.prodigy.com>`

```
In article <8sd8nf$6hmg$1@newssvr05-en0.news.prodigy.com>,
  "NICHOLAS  CREMIDIS" <NICK.CREMIDIS@prodigy.net> wrote:
>
> Hi folks;
…[7 more quoted lines elided]…
>

In your FD, specify RECORD IS VARYING IN SIZE FROM "Integer-1"
to "Integer-2" DEPENDING ON WS-FILE-LGTH.

03 WS-FILE-LGTH PIC 9(08) BINARY.

Note that WS-FILE-LGTH must be an UNSIGNED Numeric Variable. I prefer
to use BINARY Fullwords. You can use whatever you'd like.

After issuing a READ, WS-FILE-LGTH will be set to the length of the
actual record just read.

When issuing a WRITE, WS-FILE-LGTH must be set to your desired record
length. The value of WS-FILE-LGTH must be NOT LESS THAN "Integer-1" and
NOT GREATER THAN "Integer-2".

HTH....

Bill


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Variable Rcord Length

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8sj11v06ol@enews4.newsguy.com>`
- **References:** `<8sd8nf$6hmg$1@newssvr05-en0.news.prodigy.com> <8sdamp$4eb$1@nnrp1.deja.com>`

```
Also, in OS390 at least, that length takes up 4 bytes, so in the JCL be sure
to make the LRECL 4 bytes larger than it is in the FD.

Jeff

----------
In article <8sdamp$4eb$1@nnrp1.deja.com>, WOB Consulting
<wobconsult@sprynet.com> wrote:


> In article <8sd8nf$6hmg$1@newssvr05-en0.news.prodigy.com>,
>   "NICHOLAS  CREMIDIS" <NICK.CREMIDIS@prodigy.net> wrote:
…[32 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
