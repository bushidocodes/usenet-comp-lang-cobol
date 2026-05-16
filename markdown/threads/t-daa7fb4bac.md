[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and ODBC

_5 messages · 5 participants · 1999-08_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### COBOL and ODBC

- **From:** "Hartmut Wieczorek" <hwieczorek@meyermeyer.de>
- **Date:** 1999-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7p0ss6$2e2r$1@mars.ms.tlk.com>`

```
I'm not a cobol programmer, but my Q is :
is there a way to have access with a cobol app on
a Informix DB with the help of ODBC ?
I know the way to build the connect in other languages,
but what is the source code in cobol.
What exactly must I do to get the handle
if my ODBC datasource is "db1"
username "informix" and passwd "informix"

TIA
Hartmut
```

#### ↳ Re: COBOL and ODBC

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lbXs3.10072$Co3.90972@news1.mia>`
- **References:** `<7p0ss6$2e2r$1@mars.ms.tlk.com>`

```
Check out EXEC, EXECUTE and SQL.
```

#### ↳ Re: COBOL and ODBC

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7p1sfv$4gq$1@news.cerf.net>`
- **References:** `<7p0ss6$2e2r$1@mars.ms.tlk.com>`

```
Hartmut Wieczorek wrote in message <7p0ss6$2e2r$1@mars.ms.tlk.com>...
>I'm not a cobol programmer, but my Q is :
>is there a way to have access with a cobol app on
…[5 more quoted lines elided]…
>username "informix" and passwd "informix"

Most Cobols support access to RDBM's. Many do also support the use of ODBC.

You do not specify which Cobol you talk of, in case you are looking for one
that does both SQL and ODBC native, check out: www.acucorp.com.

Cheesle
```

#### ↳ Re: COBOL and ODBC

- **From:** "peter dashwood" <dashwood@freewebaccess.co.uk>
- **Date:** 1999-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37b6ce46@eeyore.callnetuk.com>`
- **References:** `<7p0ss6$2e2r$1@mars.ms.tlk.com>`

```

Hartmut Wieczorek wrote in message <7p0ss6$2e2r$1@mars.ms.tlk.com>...
>I'm not a cobol programmer, but my Q is :
>is there a way to have access with a cobol app on
…[10 more quoted lines elided]…
>
You don't need a 'handle'. The COBOL syntax is:
CONNECT  [TO] datasource name [AS connection name] [USER] or [DEFAULT]
(User and password are optional; if you don't specify USER the system takes
the DEFAULT, which must be specified on the server.)

So, for your example...
EXEC SQL
     CONNECT TO "db1" AS "conn1"   USER "informix/informix"
END-EXEC

or, if you don't like writing...
EXEC SQL
    CONNECT "db1"   (You will be logged on as default).
END-EXEC

Note that you can set several connections (conn1, conn2, etc. in my example)
and use the SET CONNECTION  syntax in COBOL to switch between them.

SQLSTATE is set by the CONNECT command so you can check if your connection
was successful.

Hope this helps,

Pete.
```

#### ↳ Re: COBOL and ODBC

- **From:** "Paddy Coleman" <paddy.coleman@merant.com>
- **Date:** 1999-08-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7p94ht$2fd$1@hyperion.mfltd.co.uk>`
- **References:** `<7p0ss6$2e2r$1@mars.ms.tlk.com>`

```
Hartmut,

Micro Focus' Net Express 3.0 product comes with a pre-processor called
OpenESQL.  This
allows SQL to be embedded in to your programs via EXEC SQL syntax.  This is
then converted
in to ODBC calls as part of the compilation process.  Your COBOL program can
then access
any ODBC datasource e.g. Informix, Oracle, Access etc.

Hope this helps.

Paddy Coleman
Manager, E-Business Support, EMEA
MERANT Micro Focus International.

Hartmut Wieczorek <hwieczorek@meyermeyer.de> wrote in message
news:7p0ss6$2e2r$1@mars.ms.tlk.com...
> I'm not a cobol programmer, but my Q is :
> is there a way to have access with a cobol app on
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
