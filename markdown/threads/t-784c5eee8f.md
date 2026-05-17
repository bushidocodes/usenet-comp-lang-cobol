[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help for COBOL in VAX/VMS

_3 messages · 3 participants · 1997-08_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help for COBOL in VAX/VMS

- **From:** "alberto magalhaes" <ua-author-13460321@usenetarchives.gap>
- **Date:** 1997-08-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bca0b3$b3302bc0$eafc41c2@albertom>`

```

Hi...
How can i get the system date like this:

YYYY/MM/DD


Thanks....

(Alberto Magalhaes)
```

#### ↳ Re: Help for COBOL in VAX/VMS

- **From:** "alain chappuis" <ua-author-17072993@usenetarchives.gap>
- **Date:** 1997-08-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-784c5eee8f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bca0b3$b3302bc0$eafc41c2@albertom>`
- **References:** `<01bca0b3$b3302bc0$eafc41c2@albertom>`

```

Alberto Magalhaes wrote:

Hello Alberto,

› =
 
› Hi...
›            How can i get the system date like this:
› =
 
›                               YYYY/MM/DD

Now the little program;

Identification Division.
Program-id. DATEJOUR.
Data Division.
Working-Storage Section.
01 DATE-STAMP.
05 AAAAMMJJ PIC 9(8).
05 RESTE PIC X(13).
01 DEDT.
05 EDT PIC 9999/99/99.
Procedure Division.
Begin.
DISPLAY "Hello, Welcome!" =

LINE 1 COLUMN 1
BOLD UNDERLINED
ERASE END SCREEN.
DISPLAY " ".
MOVE FUNCTION CURRENT-DATE TO DATE-STAMP.
MOVE AAAAMMJJ TO EDT.
DISPLAY "R=E9sult:" DEDT " " RESTE.
STOP RUN.
End Program DATEJOUR.

Alain.
-- =

+----------------------+-------------------------------------------+
| Alain Chappuis | Responsable du systeme cmu.unige.ch |
| Analyste programmeur | Decnet : UGCMU::CHAPPUIS |
…[7 more quoted lines elided]…
| ----------- | Tel. : +41 (22) [70]25.073 |
+----------------------+-------------------------------------------+
```

#### ↳ Re: Help for COBOL in VAX/VMS

- **From:** "donts..." <ua-author-8744626@usenetarchives.gap>
- **Date:** 1997-08-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-784c5eee8f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bca0b3$b3302bc0$eafc41c2@albertom>`
- **References:** `<01bca0b3$b3302bc0$eafc41c2@albertom>`

```

On 20 Aug 1997 23:16:14 GMT, "Alberto Magalhaes"
wrote:

› Hi...
›           How can i get the system date like this:
…[6 more quoted lines elided]…
›                           (Alberto Magalhaes)
01 today pic xxxx/xx/xx.
move function current-date to today.

ought to work with any modern compiler.

George Trudeau
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
