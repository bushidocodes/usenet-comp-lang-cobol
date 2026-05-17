[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCobol & Status 30

_7 messages · 4 participants · 2022-04_

---

### PowerCobol & Status 30

- **From:** "jmfg11" <ua-author-14501829@usenetarchives.gap>
- **Date:** 2022-04-01T05:19:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com>`

```
Some customers have been given status 30 on programs/files that are 100% operational. The program terminates abnormally.
Apparently there are no hardware problems.

Development environment: Windows 11 / PowerCobol v9
Clients: Windows 10 and Windows 7.
Any suggestions?
Thanks
```

#### ↳ Re: PowerCobol & Status 30

- **From:** "vbcoen" <ua-author-14501880@usenetarchives.gap>
- **Date:** 2022-04-01T09:29:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9de6b0bf01-p2@usenetarchives.gap>`
- **In-Reply-To:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com>`
- **References:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com>`

```
Hello JM!

Friday April 01 2022 10:19, JM wrote to All:

> Some customers have been given status 30 on programs/files that are
> 100% operational. The program terminates abnormally. Apparently there
> are no hardware problems.

> Development environment: Windows 11 / PowerCobol v9
> Clients: Windows 10 and Windows 7.
> Any suggestions?
> Thanks


Not knowing PowerCobol and did not know it existed but error 30 for
GnuCOBOL is permanent I/O error and this 'could' be not having correct
access rights to the directory and the files in question.
Check the settings and one other could be lack of free disk space or if
using SSD that it has not had a garbage collection run lately (and this
should be done on busy system daily if not every 12 hours) assuming it is
one of the better brands with good controllers that is installed.


Vincent
```

#### ↳ Re: PowerCobol & Status 30

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2022-04-01T17:05:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9de6b0bf01-p3@usenetarchives.gap>`
- **In-Reply-To:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com>`
- **References:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com>`

```

[posted and emailed]

In article ,
JM wrote:
› Some customers have been given status 30 on programs/files that are 100%
› operational.

Customers? Sounds like money is involved. What kind of rate, or range of
rates, is associated with the position(s) offered?

DD
```

##### ↳ ↳ Re: PowerCobol & Status 30

- **From:** "jmfg11" <ua-author-14501829@usenetarchives.gap>
- **Date:** 2022-04-06T09:32:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9de6b0bf01-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9de6b0bf01-p3@usenetarchives.gap>`
- **References:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com> <gap-9de6b0bf01-p3@usenetarchives.gap>`

```
A sexta-feira, 1 de abril de 2022 Ã (s) 22:05:16 UTC+1, doc··.@pa··x.com escreveu:
› [posted and emailed] 
› 
…[7 more quoted lines elided]…
› DD

More or less a billion!
```

###### ↳ ↳ ↳ Re: PowerCobol & Status 30

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2022-04-06T10:57:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9de6b0bf01-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9de6b0bf01-p4@usenetarchives.gap>`
- **References:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com> <gap-9de6b0bf01-p3@usenetarchives.gap> <gap-9de6b0bf01-p4@usenetarchives.gap>`

```
In article ,
JM wrote:
› A sexta-feira, 1 de abril de 2022 ??(s) 22:05:16 UTC+1,
› doc··.@pa··x.com escreveu:
…[9 more quoted lines elided]…
› More or less a billion!

That might work. How much more? How long's the contract?

DD
```

#### ↳ Re: PowerCobol & Status 30

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2022-04-08T00:49:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9de6b0bf01-p6@usenetarchives.gap>`
- **In-Reply-To:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com>`
- **References:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com>`

```
On 1/04/2022 22:19, JM wrote:
› Some customers have been given status 30 on programs/files that are 100% operational. The program terminates abnormally.
› Apparently there are no hardware problems.
…[4 more quoted lines elided]…
› Thanks

These are indexed files?

This is a problem with the underlying ACM library used for Fujitsu File
access.

You need to run Fujitsu housekeeping file utility on the offending
files. Select "File Utility" from the Project Manager "Tools" menu.

If you didn't write the software and/or have no access to the source
code and the Fujitsu IDE, then check the delivered Fujitsu Run Time
directory and look for a program called:
COBFUT32.exe

Select the "Reorganize" command and, if it fails, select the "Recovery"
command.

You should write a script for Clients to run this program on your
delivered files at least once a year and more frequently on files that
are subject to heavy updating.

You COULD leave it until you start getting 30 response codes on OPEN,
but I wouldn't do that.

Do that, and if you still have a problem, contact me privately.

Pete.

I used to write *COBOL*; now I can do *anything*...
```

##### ↳ ↳ Re: PowerCobol & Status 30

- **From:** "jmfg11" <ua-author-14501829@usenetarchives.gap>
- **Date:** 2022-04-08T12:17:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9de6b0bf01-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9de6b0bf01-p6@usenetarchives.gap>`
- **References:** `<a5d4bbbf-9624-40a5-8cff-8ee747af9779n@googlegroups.com> <gap-9de6b0bf01-p6@usenetarchives.gap>`

```
A sexta-feira, 8 de abril de 2022 Ã (s) 05:49:35 UTC+1, das··.@ent··o.nz escreveu:
› On 1/04/2022 22:19, JM wrote: 
›› Some customers have been given status 30 on programs/files that are 100% operational. The program terminates abnormally. 
…[34 more quoted lines elided]…
› I used to write *COBOL*; now I can do *anything*...

Thanks Pete for the suggestions. Yes, I'm the developer and I have access to cobfut32.
Regards
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
