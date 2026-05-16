[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and Dynamic SQL

_2 messages · 2 participants · 2000-10_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### COBOL and Dynamic SQL

- **From:** "Michel" <mm@glo.be>
- **Date:** 2000-10-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8sk7og$3cc$1@news0.skynet.be>`

```
Does anyone knows how the SQL PREPARE statement works in COBOL ? I always
get the SQLCODE -104 (illegal symbol) when i execute the SQL
PREPARE-statement

Thanks,

Michel
```

#### ↳ Re: COBOL and Dynamic SQL

- **From:** "Brad Prothero" <brad.prothero@clarica.com>
- **Date:** 2000-10-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s9iH5.71$1p2.12408@news.corpcomm.net>`
- **References:** `<8sk7og$3cc$1@news0.skynet.be>`

```

Michel <mm@glo.be> wrote in message news:8sk7og$3cc$1@news0.skynet.be...
> Does anyone knows how the SQL PREPARE statement works in COBOL ? I always
> get the SQLCODE -104 (illegal symbol) when i execute the SQL
…[6 more quoted lines elided]…
>

My guess is the string that you are preparing is not in correct SQL syntax.
Here is a code snipet that I have working in my code. STMVAR is defined in
the SQL Declare section. This code is being passed the index in the Database
where the information is located. This will setup the cursor to grab that
information.

            01  SELECT-STRING.
                02 FILLER                            PIC X(34)
                    VALUE 'SELECT * FROM BENEFITS WHERE ID = '.
                02 SEL-IDX                         PIC 99.
            MOVE PASSINDEX TO SEL-IDX.
            MOVE SELECT-STRING TO STMVAR.
            Exec SQL
                Declare Cur2 Cursor for STMIDT
            End-Exec.
            Exec SQL
                Prepare STMIDT From :STMVAR
            End-Exec.

Brad Prothero
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
