[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus Cobol and Web Services Question

_3 messages · 2 participants · 2004-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Web, XML, modern integration`](../topics.md#web)

---

### Micro Focus Cobol and Web Services Question

- **From:** agsantiago@snopud.com (Andy)
- **Date:** 2004-01-27T12:08:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1aec4564.0401271208.34447e10@posting.google.com>`

```
Hello,

First of all, I am not familiar with Micro Focus Cobol so please 
forgive the ignorance of my question.

Any rate, here is my situation.

We have a vendor package that was written using 3-tier architecture. 
The middle tier(business tier) is written in Micro Focus Cobol. It runs
is a Unix AIX server. The client is a windows application that passes
request to the business tier through Tuxedo. The business tier does all
the database service request to the Oracle backend.

My organization wants to expose the Micro Focus Cobol business tier as
web services that can be called by other applications(mostly .Net web
applications).

My question is this:
1. We would like to put a wrapper(Facade Pattern) around the legacy 
business tier. This wrapper will be exposed as web services. Could you
guide on how is it possible to do with Micro Focus Cobol? In other words,
does MF Cobol has the capability/tools? that would create a web service
application in Unix that calls a legacy Unix .dll? If so, can you share
samples/articles on how to do this?

2. Is this the best approach in exposing a legacy MF Cobol dll hosted in
Unix as web services? Please note that the dll(business tier) is a 
vendor software and we cannot modify it, only call it.

Thanks in advance.
```

#### ↳ Re: Micro Focus Cobol and Web Services Question

- **From:** Vaclav Snajdr <vsn@snajdr.de>
- **Date:** 2004-01-28T08:11:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bv7mq0$t9i$03$1@news.t-online.com>`
- **References:** `<1aec4564.0401271208.34447e10@posting.google.com>`

```
MF brings now the Server Express v4.0 for Unix/Linux - I think it
will do it.

Andy wrote:

> Hello,
> 
…[27 more quoted lines elided]…
> Thanks in advance.
```

##### ↳ ↳ Re: Micro Focus Cobol and Web Services Question

- **From:** agsantiago@snopud.com (Andy)
- **Date:** 2004-01-28T08:46:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1aec4564.0401280846.20aab106@posting.google.com>`
- **References:** `<1aec4564.0401271208.34447e10@posting.google.com> <bv7mq0$t9i$03$1@news.t-online.com>`

```
Thanks Vaclav.  I will check out Server Express v4.0.


Vaclav Snajdr <vsn@snajdr.de> wrote in message news:<bv7mq0$t9i$03$1@news.t-online.com>...
> MF brings now the Server Express v4.0 for Unix/Linux - I think it
> will do it.
…[32 more quoted lines elided]…
> > Thanks in advance.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
