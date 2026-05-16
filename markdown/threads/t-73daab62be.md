[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL & SQLCODE

_4 messages · 4 participants · 1999-05_

---

### COBOL & SQLCODE

- **From:** "Victoria Monta���ez" <vicky@correo.ulima.edu.pe>
- **Date:** 1999-05-11T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol
- **Message-ID:** `<7h8hbg$247$1@ucayali.unired.net.pe>`

```
hi there,

is it possible to capture the sqlcode when running an .exe (cobol) ?

TIA,

Vicky
```

#### ↳ Re: COBOL & SQLCODE

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-05-11T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<Iw_Z2.1134$Yy4.23069@dfiatx1-snr1.gtei.net>`
- **References:** `<7h8hbg$247$1@ucayali.unired.net.pe>`

```
The sqlcode (OK, not found, database not open, etc, I presume you mean) can
be detected in the COBOL program; in fact, it SHOULD be, and the programmer
should handle any "not-OK" situation.

Once the program is compiled, though, the user has no access to the calls or
the results of the SQL calls to the database services. If there are
"not-OK" SQL codes not being handled in the program, contact the prgrammer
and demand repairs or a refund.

MCM


Victoria Monta�ez wrote in message <7h8hbg$247$1@ucayali.unired.net.pe>...
>hi there,
>
…[6 more quoted lines elided]…
>
```

#### ↳ Re: COBOL & SQLCODE

- **From:** sven_schneider@my-dejanews.com
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol
- **Message-ID:** `<7hbooh$s4o$1@nnrp1.deja.com>`
- **References:** `<7h8hbg$247$1@ucayali.unired.net.pe>`

```
In article <7h8hbg$247$1@ucayali.unired.net.pe>,
  "Victoria Monta�ez" <vicky@correo.ulima.edu.pe> wrote:
> hi there,
>
…[6 more quoted lines elided]…
>

yes.

in your program should be a test of the sqlcode.

If you have a problem with a 'foreign' program and your are not able to
change the code, then you must use a database utility. i'm working with
DB2 on MVS/OS390 and the DB2-system protocols each error occured on
database. with a special tool you can look at the protocol and find out
what was wrong. I have no idea about this tool on other systems or
databases. Please ask your database-administrator for this tool.
```

#### ↳ Re: COBOL & SQLCODE

- **From:** Matthew Son <esmks@email.ais.unc.edu>
- **Date:** 1999-05-13T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol
- **Message-ID:** `<373B0A44.AE0DFB07@email.ais.unc.edu>`
- **References:** `<7h8hbg$247$1@ucayali.unired.net.pe>`

```
Victoria,

I assume you are not running on a mainframe, so I can't help you
directly.  I work on a mainframe and you can "capture" sqlcode by doing
a display or print of it to an output medium (e.g. file) immediately
after the exec sql section.  A new sqlcode is generated each time you
use an exec sql statement, so depending on your input file, you could
get a lot of data.

exec sql
 ...
end-exec.

display "sqlcode for reading/writing is " sqlcode.
display "soc-sec-num                    " soc-sec-num.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
