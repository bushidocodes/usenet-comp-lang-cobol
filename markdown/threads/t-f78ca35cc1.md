[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Linking Cobol program which calling C progran & vice versa

_1 message · 1 participant · 1998-12_

---

### Linking Cobol program which calling C progran & vice versa

- **From:** saarg@hotmail.com (Saar Ginzburski)
- **Date:** 1998-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367e6a6c.8856034@soint1>`

```
Hi,

We are trying to link a Cobol program, which call a C program, which
call another Cobol program.

The link command we are using is for creating an RTS file in order to
debug the parent Cobol program.

We keep getting the error message:
ld: Duplicate symbol "SYMBOL_NAME" in files C_LIBRARY.a(Cfile.o) and
/var/tmp/cob24453/%cob0.o

SYMBOL_NAME is the name of the function from within her we are calling
the Cobol program.
C_LIBRARY.a is a library containing al my C objects.
Cfile.o is the name of the object where the SYMBOL_NAME exist.

Does anyone have any idea ?

Thanks in advance,
Saar Ginzburski,
Amdocs (Israel) Ltd.
saarg@amdocs.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
