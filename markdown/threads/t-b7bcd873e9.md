[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL DB2 PROBOLM

_3 messages · 3 participants · 1999-08_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### COBOL DB2 PROBOLM

- **From:** "Nuno" <nmourapires@mail.pt>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37c27df6@discussions>`

```

Hello,

How can i call, from a cobol program, an aplication that runs 
under DB2 to
execute my SQL statements. This aplication requires an input 
file (sql code) and an output file (result of the sql).

It is possible to do this?

Thanks in advanced.


--Posted from EarthWeb Discussions. http://discussions.earthweb.com
```

#### ↳ Re: COBOL DB2 PROBOLM

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-08-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37C296AD.CCC1DC5@zip.com.au>`
- **References:** `<37c27df6@discussions>`

```
Nuno wrote:
> 
> Hello,
…[10 more quoted lines elided]…
> --Posted from EarthWeb Discussions. http://discussions.earthweb.com


Yes - look up dynamic SQL.  You do not need to leave you cobol app to
do this by the way.

Ken
```

#### ↳ Re: COBOL DB2 PROBOLM

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-08-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HWGw3.687$dT2.29978@dfiatx1-snr1.gtei.net>`
- **References:** `<37c27df6@discussions>`

```
You already have an explanation of some of the general parameters for using
DB2 in COBOL programs, but it sounds like you want to do DYNAMIC SQL - i.e.,
the SQL statements are constructed at run-time. In your case, you are
reading the statments from a file, but makes no difference.

In pseudo-code
  Read Statement from statement file
  Move statement to area reserved for the SQL statements.
  EXEC SQL
     PREPARE statement     <<< I think?
  END-EXEC
  call SQL engine (DB2)
  Write the output to your file.


I haven't done this in a number of years, so I don't recall the exact
syntax.

Also, if you are using an IBM mainframe for the DB2, there is a batch
utility you can run where the SYSIN dataset is the SQL statement and you can
diect the output to another dataset. (This is handy if you don't want to
write a program to do the above).

Maybe someone else knows the details, but "dynamic sql" is what you are
looking to do.


Michael Mattias
Tal Systems
Racine WI USA
michael.mattias@gte.net
Nuno wrote in message <37c27df6@discussions>...
>
>Hello,
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
