[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CBL_ERROR_PROC - NetExpress

_1 message · 1 participant · 2001-01_

---

### CBL_ERROR_PROC - NetExpress

- **From:** "Neil Hayes" <NeilH@syspro.co.za>
- **Date:** 2001-01-18T09:55:06+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a66a0ee$0$226@hades.is.co.za>`

```
Can any one tell me is CBL_ERROR_PROC a cobol call that is operating system
specific ? NetExpress online help does not seem to mention anything and it
seems my code does not run through the error trap routine.

In the main program I have $set initcall(errtrap) to ensure that it loads
and then in errtrap.cbl

call "CBL_ERROR_PROC" using install-flag

                                            install-address

                                            returning status-code.

etc as per the example in the help. But when I get error 173 I expect the
program errtrap to be called  and enter at the entry point but to no avail.



Neil

NeilH@syspro.co.za
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
