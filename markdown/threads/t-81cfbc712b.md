[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "invalid" source code (END-IF, Next Sentence, and missing periods)

_1 message · 1 participant · 2001-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: "invalid" source code (END-IF, Next Sentence, and missing periods)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-05T13:00:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9i2a02$lu5$1@slb6.atl.mindspring.net>`
- **References:** `<9fjsu2$4c0$1@slb0.atl.mindspring.net> <9fllv7$5ko$1@news.netmar.com> <3B2521F3.3FFAE797@Azonic.co.nz> <CNw07.2515$xp1.250458@newsread1.prod.itd.earthlink.net> <76I07.206$_93.29600957@newssvr15.news.prodigy.com> <ZtO07.30484$J91.1061302@bgtnsc06-news.ops.worldnet.att.net>`

```

"Russell Styles" <rwstyles@worldnet.att.net> wrote in message
news:ZtO07.30484$J91.1061302@bgtnsc06-news.ops.worldnet.att.net...
>
> "Terry Heinze" <terryheinze@prodigy.net> wrote in message
> news:76I07.206$_93.29600957@newssvr15.news.prodigy.com...
 <snip> >
>
>     You can handle the EXIT PROGRAM problem by ALWAYS following
…[3 more quoted lines elided]…
>

FYI - following an EXIT PROGRAM statement by a STOP RUN is an extension
(common in many '85 Standard compilers - but still NOT conforming).  I
(personally) see no advantage of using that than using the "equally common"
extension of GOBACK - which does the same thing.

FYI - *both* GoBack and following EXIT STATEMENT with STOP RUN are allowed
in the draft of the next Standard - so neither of these have any advantage
in that way.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
