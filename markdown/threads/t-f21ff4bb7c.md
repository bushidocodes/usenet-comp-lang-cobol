[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Environment Variables...

_2 messages · 2 participants · 1998-09_

---

### Environment Variables...

- **From:** paulr@bix.com (paulr)
- **Date:** 1998-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sifqd$klf@lotho.delphi.com>`

```

Anyone have a pointer on how to get IBM Visualage COBOL
to go out and retrieve an environment variable? 
I'm definately spoiled. 

   accept variable-name from environment "env-var-name"

Works fine in AcuCobol, but that is of course, a 
proprietary extension. 

-Paul
```

#### ↳ Re: Environment Variables...

- **From:** AS-DATA@t-online.de (Andreas Strzoda)
- **Date:** 1998-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6sit89$grd$2@news01.btx.dtag.de>`
- **References:** `<6sifqd$klf@lotho.delphi.com>`

```
paulr schrieb:

> Anyone have a pointer on how to get IBM Visualage COBOL
> to go out and retrieve an environment variable?
…[7 more quoted lines elided]…
> -Paul

In fujitsu it goes like this:

 SPECIAL-NAMES.
    ENVIRONMENT-NAME  IS ENV-NAME
    ENVIRONMENT-VALUE IS ENV-VALUE.
...
     DISPLAY "comspec" UPON ENV-NAME.
     ACCEPT  VAR-VALUE        FROM ENV-VALUE
             ON EXCEPTION MOVE SPACE TO VAR-VALUE.

so VAR-VALUE is empty or contents the COMSPEC-environment
Greatings

AS
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
