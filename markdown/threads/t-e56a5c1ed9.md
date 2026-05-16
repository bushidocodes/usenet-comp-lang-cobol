[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Display Upon Console - Highlight Msg?

_2 messages · 2 participants · 2002-04 → 2002-05_

---

### Display Upon Console - Highlight Msg?

- **From:** Fir <fir@eskimo.com>
- **Date:** 2002-04-29T23:17:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aakka7$jbb$1@eskinews.eskimo.com>`

```
IBM Mainframe converting VS cobol to Cobol 390.
This program has display upon console and accept commands
to verify alignment and beginning and ending check numbers
for printing checks.

Under the old version those messages were highlighted on the console.
Under cobol 390 they no longer highlight and thus scroll away.

The systems programmer will intercept them based on message text
so they don't scroll but it seems to me if I didn't change the
message text, they should behave the same under Cobol 390 as
they do under VS cobol.  Any ideas?  Thanks.
```

#### ↳ Re: Display Upon Console - Highlight Msg?

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2002-05-01T18:23:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aappg5$os9$1@slb6.atl.mindspring.net>`
- **References:** `<aakka7$jbb$1@eskinews.eskimo.com>`

```
If you have no other solution, then you'd be better off with an ASSEMBLER
sub-program that issues a WTO, with the proper parameter values for
highlighting and non-scroll off the Console.

I couldn't tell you why it was highighted in VS COBOL but not for OS/390.

E-Mail me offline if you need an example sub-program.

Bill

"Fir" <fir@eskimo.com> wrote in message
news:aakka7$jbb$1@eskinews.eskimo.com...
> IBM Mainframe converting VS cobol to Cobol 390.
> This program has display upon console and accept commands
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
