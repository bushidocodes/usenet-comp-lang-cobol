[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# text centering in COBOL

_6 messages · 6 participants · 2000-03 → 2000-04_

---

### text centering in COBOL

- **From:** <jacasey@bajor.its.deakin.edu.au>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jAfF4.9$ie.2127@news.deakin.edu.au>`

```
Hi,

I am doing a COBOL course and just wondering are there any functions to
center text etc?  my target platform will be Acu cobol on Solaris.
```

#### ↳ Re: text centering in COBOL

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c41pi$bhia$1@newssvr03-int.news.prodigy.com>`
- **References:** `<jAfF4.9$ie.2127@news.deakin.edu.au>`

```

I'm not aware of any, but it's fairly easy to write a routine yourself  to
accomplish the task.  Try using a combination of counting trailing blanks
and then using reference modification.

<jacasey@bajor.its.deakin.edu.au> wrote in message
news:jAfF4.9$ie.2127@news.deakin.edu.au...
> Hi,
>
…[6 more quoted lines elided]…
>
```

#### ↳ Re: text centering in COBOL

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8c6u9i$161$1@news.cerf.net>`
- **References:** `<jAfF4.9$ie.2127@news.deakin.edu.au>`

```
<jacasey@bajor.its.deakin.edu.au> wrote in message
news:jAfF4.9$ie.2127@news.deakin.edu.au...
> Hi,
>
> I am doing a COBOL course and just wondering are there any functions to
> center text etc?  my target platform will be Acu cobol on Solaris.

With Acucobol you got a function C$JUSTIFY, check it out.

Syntax:
    CALL "C$JUSTIFY" USING DATA-ITEM, JUSTIFY-TYPE

Cheesle
```

##### ↳ ↳ Re: text centering in COBOL

- **From:** jacasey.invalid@bajor.its.deakin.edu.au
- **Date:** 2000-04-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SzZF4.17$ie.3810@news.deakin.edu.au>`
- **References:** `<jAfF4.9$ie.2127@news.deakin.edu.au> <8c6u9i$161$1@news.cerf.net>`

```
Cheesle <cheesle@online.nospamplease.no> wrote:
> <jacasey@bajor.its.deakin.edu.au> wrote in message
> news:jAfF4.9$ie.2127@news.deakin.edu.au...
>> Hi,

Cool thanks guys :)

>>
>> I am doing a COBOL course and just wondering are there any functions to
>> center text etc?  my target platform will be Acu cobol on Solaris.

> With Acucobol you got a function C$JUSTIFY, check it out.

> Syntax:
>     CALL "C$JUSTIFY" USING DATA-ITEM, JUSTIFY-TYPE

> Cheesle
```

#### ↳ Re: text centering in COBOL

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<27LlOHT2InjPLq+iMWHbFUux011o@4ax.com>`
- **References:** `<jAfF4.9$ie.2127@news.deakin.edu.au>`

```
On Sat, 01 Apr 2000 05:13:51 GMT, <jacasey@bajor.its.deakin.edu.au>
wrote:

>Hi,
>
>I am doing a COBOL course and just wondering are there any functions to
>center text etc?  my target platform will be Acu cobol on Solaris.


If you only need that to do "displays" then you can do the following

display "Welcome" line 1, size 40, centered,


But the best is still to create you own program do do this.
It will take around 30-40 lines of code.

FF
```

#### ↳ Re: text centering in COBOL

- **From:** Fim Wästberg <fim.wastberg@fimator.se>
- **Date:** 2000-04-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E5D914.A34C5667@fimator.se>`
- **References:** `<jAfF4.9$ie.2127@news.deakin.edu.au>`

```

Use CALL "C$JUSTIFY" ......

jacasey@bajor.its.deakin.edu.au wrote:

> Hi,
>
…[5 more quoted lines elided]…
> webpage: http://www.deakin.edu.au/~jacasey
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
