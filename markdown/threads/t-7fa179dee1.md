[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "Rewinding" files in COBOL

_5 messages · 4 participants · 2000-06_

---

### "Rewinding" files in COBOL

- **From:** "Troy" <visrealm@camtech.net.au>
- **Date:** 2000-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ODl_4.8069$N4.300460@ozemail.com.au>`

```
Hi All,
    I'm new to COBOL and was wondering if there is a way to move to the
start of a file besides closing and re-opening it.

Regards

Troy
```

#### ↳ Re: "Rewinding" files in COBOL

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3939E9D4.45578BEB@worldnet.att.net>`
- **References:** `<ODl_4.8069$N4.300460@ozemail.com.au>`

```
Troy wrote:
> 
> Hi All,
>     I'm new to COBOL and was wondering if there is a way to move to the
> start of a file besides closing and re-opening it.

If IBM mainframe, batch or CICS? The technique is the same, but the
verbs/commands are different.

Bill Lynch
```

#### ↳ Re: "Rewinding" files in COBOL

- **From:** "Troy" <visrealm@camtech.net.au>
- **Date:** 2000-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q8m_4.8116$N4.301484@ozemail.com.au>`
- **References:** `<ODl_4.8069$N4.300460@ozemail.com.au>`

```
Just on a PC using RMCOBOL??

Troy <visrealm@camtech.net.au> wrote in message
news:ODl_4.8069$N4.300460@ozemail.com.au...
> Hi All,
>     I'm new to COBOL and was wondering if there is a way to move to the
…[6 more quoted lines elided]…
>
```

#### ↳ Re: "Rewinding" files in COBOL

- **From:** docdwarf@clark.net (NA)
- **Date:** 2000-06-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M8r_4.3409$HD6.71184@iad-read.news.verio.net>`
- **References:** `<ODl_4.8069$N4.300460@ozemail.com.au>`

```
In article <ODl_4.8069$N4.300460@ozemail.com.au>,
Troy <visrealm@camtech.net.au> wrote:
>Hi All,
>    I'm new to COBOL and was wondering if there is a way to move to the
>start of a file besides closing and re-opening it.

That depends, I believe, on what kind of file it is.

DD
```

#### ↳ Re: "Rewinding" files in COBOL

- **From:** "Luis Saraiva" <lfs@inforauto.pt>
- **Date:** 2000-06-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8hg40q$s2v$1@duke.telepac.pt>`
- **References:** `<ODl_4.8069$N4.300460@ozemail.com.au>`

```
If it is an indexed or relative file, just use the START command with the
appropriate indexed or relative key fullfilled, and then READ ... NEXT.

"Troy" <visrealm@camtech.net.au> escreveu na mensagem
news:ODl_4.8069$N4.300460@ozemail.com.au...
> Hi All,
>     I'm new to COBOL and was wondering if there is a way to move to the
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
