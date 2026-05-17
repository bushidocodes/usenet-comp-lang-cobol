[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCobol & Internet

_5 messages · 4 participants · 2019-08 → 2020-02_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### PowerCobol & Internet

- **From:** "jmfg11" <ua-author-14501829@usenetarchives.gap>
- **Date:** 2019-08-02T05:39:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d2f7fc7d-3366-4ee4-a3cf-1d3ab21609b4@googlegroups.com>`

```
Is there any possibility / tool, that allow to do something like this:

SELECT MYISAMFILE ASSIGN TO "55.1.1.1\FILE.DAT"
ORGANIZATION INDEXED
...

"55.1.1.1" being an external IP


Regards,
Joe
```

#### ↳ Re: PowerCobol & Internet

- **From:** "kerry.liles" <ua-author-7511031@usenetarchives.gap>
- **Date:** 2019-08-02T09:56:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0b3bc85ef3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<d2f7fc7d-3366-4ee4-a3cf-1d3ab21609b4@googlegroups.com>`
- **References:** `<d2f7fc7d-3366-4ee4-a3cf-1d3ab21609b4@googlegroups.com>`

```
On 8/2/2019 5:39 AM, JM wrote:
› Is there any possibility / tool, that allow to do something like this:
› 
…[9 more quoted lines elided]…
› 

Sorry, no idea - but:

My first reaction was to think about all the things that could possibly
go wrong with directly reading a file over the network and wondering why
not download the file to a local file first and then discard it *if* it
was successfully read and processed?

>From an auditing point of view you then also have the opportunity to
archive the input file to allow later debugging of any complaints about
whether a record was received or not etc.

In the proposed scenario the COBOL program would be hard pressed to
provide any sort of error recovery or even avoid outright stalling if
any network error occurs.
```

##### ↳ ↳ Re: PowerCobol & Internet

- **From:** "jmfg11" <ua-author-14501829@usenetarchives.gap>
- **Date:** 2019-08-02T11:43:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0b3bc85ef3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0b3bc85ef3-p2@usenetarchives.gap>`
- **References:** `<d2f7fc7d-3366-4ee4-a3cf-1d3ab21609b4@googlegroups.com> <gap-0b3bc85ef3-p2@usenetarchives.gap>`

```
sexta-feira, 2 de Agosto de 2019 Ã s 14:56:43 UTC+1, Kerry Liles escreveu:
› On 8/2/2019 5:39 AM, JM wrote:
›› Is there any possibility / tool, that allow to do something like this:
…[25 more quoted lines elided]…
› any network error occurs.



Well, the goal was to have the data in the "cloud" (in a ISAM FILE setting). It would not be a problem using client/server database (MariaDB for example). But here the goal is really to use files (file system).

Regards
```

#### ↳ Re: PowerCobol & Internet

- **From:** "kilgasto" <ua-author-14501876@usenetarchives.gap>
- **Date:** 2020-01-30T17:40:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0b3bc85ef3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<d2f7fc7d-3366-4ee4-a3cf-1d3ab21609b4@googlegroups.com>`
- **References:** `<d2f7fc7d-3366-4ee4-a3cf-1d3ab21609b4@googlegroups.com>`

```
fredag den 2. august 2019 kl. 11.39.44 UTC+2 skrev JM:
› Is there any possibility / tool, that allow to do something like this:
› 
…[8 more quoted lines elided]…
› Joe

what you are using here is a simple way to connect a logical filename to a physical file name on a local disk. it was never meant to support what you are trying to do.

you really need to make this file locally available, either by mounting a network drive and giving this path to the program.

it's a good idea in a way, what you write, but was never the intention.
```

##### ↳ ↳ Re: PowerCobol & Internet

- **From:** "federico.priolo" <ua-author-14501445@usenetarchives.gap>
- **Date:** 2020-02-02T14:57:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0b3bc85ef3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0b3bc85ef3-p4@usenetarchives.gap>`
- **References:** `<d2f7fc7d-3366-4ee4-a3cf-1d3ab21609b4@googlegroups.com> <gap-0b3bc85ef3-p4@usenetarchives.gap>`

```
A way could be use the opensource wget tool for example:

c:\yourpath>wget http:/55.1.1.1/FILE.DAT (enter) and then manage locally the file you have downloaded from in ..

Federico
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
