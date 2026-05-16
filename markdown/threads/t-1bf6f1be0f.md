[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INSPECT BEFORE/AFTER phrase 2002/2008

_3 messages · 2 participants · 2006-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### INSPECT BEFORE/AFTER phrase 2002/2008

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-10-27T12:24:29+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ehsmp0$pc$01$1@news.t-online.com>`

```
Am I missing something ? -
Page 462 (2002), page 492 (2008), on
the after-before-phrase, should there not be
a "..." after the phrase ? ie. The BEFORE/AFTER can be repeated.

85 allows this and is born out by the test suite eg. NC216A :

168900     INSPECT WC-XN-83 TALLYING WRK-DU-999-1 FOR ALL SPACES
169000             AFTER  "C."
169100             BEFORE "DO".
```

#### ↳ Re: INSPECT BEFORE/AFTER phrase 2002/2008

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-10-27T12:34:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ehsnc1$1tq$01$1@news.t-online.com>`
- **References:** `<ehsmp0$pc$01$1@news.t-online.com>`

```
Answering myself, is this catered for by definition of the "bars" around the 
syntax ?
Not quite clear to me.

"Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag 
news:ehsmp0$pc$01$1@news.t-online.com...
> Am I missing something ? -
> Page 462 (2002), page 492 (2008), on
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: INSPECT BEFORE/AFTER phrase 2002/2008

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2006-10-27T11:08:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12k488ma4v42u30@corp.supernews.com>`
- **References:** `<ehsmp0$pc$01$1@news.t-online.com> <ehsnc1$1tq$01$1@news.t-online.com>`

```

"Roger While" <simrw@sim-basis.de> wrote in message
news:ehsnc1$1tq$01$1@news.t-online.com...
> "Roger While" <simrw@sim-basis.de> schrieb im Newsbeitrag
> news:ehsmp0$pc$01$1@news.t-online.com...
…[11 more quoted lines elided]…
> Answering myself, is this catered for by definition of the "bars" around
the
> syntax ?
> Not quite clear to me.

FDIS 1989:2002, page 18, 5.1.5.3 Choice indicators,
"Choice indicators are a pair of bars '|' surrounded by
braces or by brackets that enclose a portion of a general
format. When enclosed by braces, one or more of the
alternatives contained within the choice indicators shall be
specified, but any single alternative shall be specified only
once. When enclosed by brackets, zero or more of the
alternatives contained within the choice indicators shall be
specified, but any single alternative may be specified
only once. The alternatives may be specified in any order."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
