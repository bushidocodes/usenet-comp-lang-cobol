[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# call-convention

_2 messages · 2 participants · 2002-10_

---

### call-convention

- **From:** "dsoans" <dsoans@rogers.com>
- **Date:** 2002-10-25T23:50:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tNku9.75740$Q3S.18214@news01.bloor.is.net.cable.rogers.com>`

```
I have code that was written in Micro Focus COBOL and is using the
CALL-CONVENTION statement as:
CALL-CONVENTION 2 IS ODBCAPI

I need to now compile with CA-Realia II and have problems with this line. I
get the error:
81 ( 10) 0508 E EBCDIC or STANDARD-N expected; found '2'

81 ( 10) 0112 E Unrecognizable word or literal 'IS'

81 ( 10) 0508 E EBCDIC or STANDARD-N expected; found '.'



Is the CALL-CONVENTION statement specific to Micro Focus COBOL or is it part
of the general COBOL standard? If anyone has any ideas on how I can recode
this please share them with me.

Thank you.

Dennis
```

#### ↳ Re: call-convention

- **From:** <thepla@attglobal.net>
- **Date:** 2002-10-25T21:47:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3dba0650_1@news1.prserv.net>`
- **References:** `<tNku9.75740$Q3S.18214@news01.bloor.is.net.cable.rogers.com>`

```
I use Realia Workbench but do not use the CALL-CONVENTION. It seems that the
programmer was trying to access a data file via ODBC. I do use ODBC and
Realia all the time and it is done via a pre-compiler that you set up via
the Workbench. I hope this helps.

"dsoans" <dsoans@rogers.com> wrote in message
news:tNku9.75740$Q3S.18214@news01.bloor.is.net.cable.rogers.com...
> I have code that was written in Micro Focus COBOL and is using the
> CALL-CONVENTION statement as:
> CALL-CONVENTION 2 IS ODBCAPI
>
> I need to now compile with CA-Realia II and have problems with this line.
I
> get the error:
> 81 ( 10) 0508 E EBCDIC or STANDARD-N expected; found '2'
…[7 more quoted lines elided]…
> Is the CALL-CONVENTION statement specific to Micro Focus COBOL or is it
part
> of the general COBOL standard? If anyone has any ideas on how I can recode
> this please share them with me.
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
