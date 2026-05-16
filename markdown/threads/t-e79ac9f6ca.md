[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rm/Cobol and Btrieve (Pervasive SQL 7)

_2 messages · 2 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### Rm/Cobol and Btrieve (Pervasive SQL 7)

- **From:** Mario Gauci <mgauci@hotmail.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.databases.btrieve,alt.cobol,comp.lang.cobol
- **Message-ID:** `<fqchOKUvgQR0H6NCI0zADdmOhKSY@4ax.com>`

```
We are using own written RM/Cobol programs to access files under
Pervasive SQL ver.7. We are using the BEGIN/END/ABORT Transaction in
C$BTRV.DLL. When an update transaction is complete the first file
which was originally locked with the READ statement is not being
unlocked notwithstanding that we have issued the UNLOCK command. The
only time the record is released is when the file is CLOSED.

If anybody can help, please let us know.


Many Thanks


Mario


mgauci@hotmail.com or dwallbank@gasan.com
```

#### ↳ Re: Rm/Cobol and Btrieve (Pervasive SQL 7)

- **From:** "Roberto Stern" <rhstern@uol.com.br>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.databases.btrieve,alt.cobol,comp.lang.cobol
- **Message-ID:** `<7vsnul$j15$1@ash.prod.itd.earthlink.net>`
- **References:** `<fqchOKUvgQR0H6NCI0zADdmOhKSY@4ax.com>`

```
Mario

Are you issuing the begin trans before opening the file ? I have one
customer doing that and it had the effect of having the file locked , even
after a end/abort trans.

Regards

Roberto Stern

Mario Gauci <mgauci@hotmail.com> wrote in message
news:fqchOKUvgQR0H6NCI0zADdmOhKSY@4ax.com...
> We are using own written RM/Cobol programs to access files under
> Pervasive SQL ver.7. We are using the BEGIN/END/ABORT Transaction in
…[16 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
