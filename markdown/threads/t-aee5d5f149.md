[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBSQL Oracle 9i and MF Cobol

_2 messages · 2 participants · 2004-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### COBSQL Oracle 9i and MF Cobol

- **From:** "Mike Kinasz" <ng_spam_1@kinasz.com>
- **Date:** 2004-10-15T22:59:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10n1hclotbipk1e@corp.supernews.com>`

```
Anything I should watch out for using MF Net Express 3.1 (no can't use 4.0) 
with COBSQL to access Oracle 9i PL/SQL stored procedures?
Yesterday I found a tidbit saying you can't use 88 level switches that I 
hadn't seen before.....   (bummer).    Anybody else been down the COBSQL 
road that might be willing to throw some tips my way?

Thanks,
Mike K
```

#### ↳ Re: COBSQL Oracle 9i and MF Cobol

- **From:** "Simon Tobias" <Simon.Tobias@nospam.microfocus.com>
- **Date:** 2004-10-19T09:20:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cl2hok$m4$1@hyperion.microfocus.com>`
- **References:** `<10n1hclotbipk1e@corp.supernews.com>`

```
Hi Mike.

You can use level 88 switches in your application, but not within a host
variable definition. That restriction is a Pro*COBOL limitation, rather than
Cobsql, per the Pro*COBOL Programmer's Guide :

--- start of text ---

Level Numbers

When declaring host variables, you can use level numbers 01 through 49, and
77.
Pro*COBOL does not allow variables containing the VARYING clause or
pseudo-type variables (these datatypes are prefixed with "SQL- ") to be
declared
level 49 or 77.

--- end of text ---

SimonT.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
