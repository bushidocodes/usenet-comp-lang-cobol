[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Realia COBOL - Embedded SQL

_2 messages · 2 participants · 2007-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### Realia COBOL - Embedded SQL

- **From:** bradthomasss@gmail.com
- **Date:** 2007-11-16T12:25:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29ec5cee-6571-4cb8-8357-b3781d371bb7@n20g2000hsh.googlegroups.com>`

```
Does anyone know how to access a MS Access database using embedded sql
for Realia COBOL??

All I want to do at this point is insert rows in the db.

Thanks for any help.

Brad
```

#### ↳ Re: Realia COBOL - Embedded SQL

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2007-11-17T10:01:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0706a1a6-fc90-4f4b-aaec-7c4575816b7c@e23g2000prf.googlegroups.com>`
- **References:** `<29ec5cee-6571-4cb8-8357-b3781d371bb7@n20g2000hsh.googlegroups.com>`

```
On Nov 17, 9:25 am, bradthoma...@gmail.com wrote:
> Does anyone know how to access a MS Access database using embedded sql
> for Realia COBOL??
…[5 more quoted lines elided]…
> Brad

Embedded SQL usually requires a preprocessor that will convert the
EXEC SQL ... into calls to the library. If you do not have a pre-
processor then you can write the calls into your code as the pre-
processor would. This has the problem that there would be no checking
or validation that the pre-processor does so it may take some time to
get it working.

You probably want to call ODBC. A C language tutorial is here:

http://www.easysoft.com/developer/languages/c/odbc_tutorial.html

If can can get Realia to call the C library (which I think it can)
then just (?) work through the tutorial and make sure that your
strings are null terminated.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
