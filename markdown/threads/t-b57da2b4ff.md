[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Precompiler Microfocus and Oracle

_1 message · 1 participant · 1999-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### Precompiler Microfocus and Oracle

- **From:** Johan den Boer <jj.den.boer@hccnet.nl>
- **Date:** 1999-06-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3761F5CC.E6A57817@hccnet.nl>`

```
Hi,

Is there a difference between compiling with cobsql from microfocus and
procob from Oracle.
I have some strange things in my cobol programs. I use embedded sql from

oracle in my cobol sources and I have problems with the declarations of
the
cobol variables which access the database tables.
Suppose a table has a field myfield number(6) in oracle. In one program
I had to declare the host variables as :

01    ws-myfield        pic s9(06) comp.

and in an other program I had to declare it as

01    ws-myfield        pic s9(07) comp.

If take the same declarations for ws-myfield in program B from program A
I don't
get the right answers from my sql query ?

Does anyone have the solution. Is there a standard way to declare
your cobol host variables.

regards : Johan den Boer

email : jj.den.boer@hccnet.nl
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
