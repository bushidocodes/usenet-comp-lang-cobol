[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# length of

_3 messages · 3 participants · 2003-03_

---

### length of

- **From:** "Paul" <paulhbliu@hotmail.com>
- **Date:** 2003-03-13T16:03:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4n6ca.527$qc4.50736@news20.bellglobal.com>`

```
Hi

In mainframe, the compiler can tell the "length of file" function
what's the equavalent function in other compiler such as open-cobol or
fujitsu cobol ?

many thanks
Paul
```

#### ↳ Re: length of

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-03-13T17:49:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4r5e9$r5r$1@slb3.atl.mindspring.net>`
- **References:** `<4n6ca.527$qc4.50736@news20.bellglobal.com>`

```
Paul,
  If you really mean what is the length of a specific record in a variable
length file, then use the

    Record Varying in Size ... Depending on WS-item

syntax to get the record length in WS-Item after each READ.

If you want to get the length of a data division group or elementary item,
then use the intrinsic function
    Function Length (data-item)
syntax.  I don't know if open-cobol has intrinsic functions yet (or not) but
this is Standard COBOL.
```

#### ↳ Re: length of

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-13T18:14:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jm6dnWlTkuV8geyjXTWcig@giganews.com>`
- **References:** `<4n6ca.527$qc4.50736@news20.bellglobal.com>`

```

"Paul" <paulhbliu@hotmail.com> wrote in message
news:4n6ca.527$qc4.50736@news20.bellglobal.com...
> Hi
>
> In mainframe, the compiler can tell the "length of file" function
> what's the equavalent function in other compiler such as open-cobol or
> fujitsu cobol ?

In Fujitsu, it's:

CALL 'CBL_CHECK_FILE_EXISTS2' USING
   FILE-NAME
   FILE-CHARACTERISTICS (one of which is file size)
   RETURNING STATUS-CODE.

Sorry, I don't know about open-cobol. We don't use any open source software
here, believing, as we do, that open-source stuff is a Communist plot ("from
each according to his ability...").
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
