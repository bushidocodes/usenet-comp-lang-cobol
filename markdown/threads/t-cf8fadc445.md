[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DB2 Precomplier option

_3 messages · 3 participants · 1998-06 → 1998-07_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### DB2 Precomplier option

- **From:** "news.onaustralia.com.au" <ua-author-17074068@usenetarchives.gap>
- **Date:** 1998-06-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bda268$09597cc0$d111868b@default>`

```

Hi,

Do know DB2 precomplier PARM to resolve COPYLIB first and then precomplie.

I have all my code in COPYLIB, precomplier does't insert comment(*) before
EXEC SQL.(because its copied from COPYLIB).

Regards
Sam
```

#### ↳ Re: DB2 Precomplier option

- **From:** "joseph kohler" <ua-author-6589497@usenetarchives.gap>
- **Date:** 1998-06-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cf8fadc445-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bda268$09597cc0$d111868b@default>`
- **References:** `<01bda268$09597cc0$d111868b@default>`

```

news.onaustralia.com.au wrote:
› 
› Hi,
…[7 more quoted lines elided]…
› Sam
The DB2 precompiler cannot pull in any copylibs. You can only get other
members via EXEC SQL INCLUDE. The copylib inclusion is a function of
the COBOL or PL/I compiler.

Joe.
+-----------------------------------------------------------+
| E-mail:  joe··.@ya··o.com                             |
|                                                           |
| Nothing is foolproof to a sufficiently talented fool!     |
+-----------------------------------------------------------+
```

#### ↳ Re: DB2 Precomplier option

- **From:** "AEDComS" <AEDComS@ix.netcom.com>
- **Date:** 1998-07-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MlBo1.1614$Xe6.1153740@news2.randori.com>`
- **References:** `<01bda268$09597cc0$d111868b@default>`

```
use EXEC SQL INCLUDE copylib member END-EXEC

and make sure your copylib dataset is part of your SYSLIB on the precompile
step


news.onaustralia.com.au wrote in message
<01bda268$09597cc0$d111868b@default>...
>Hi,
>
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
