[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCobol V3 - Table-Item

_3 messages · 2 participants · 1999-01_

---

### PowerCobol V3 - Table-Item

- **From:** "Hajo Schepker" <schepker@geocities.com>
- **Date:** 1999-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<782h27$6re$1@namib.north.de>`

```
Hello,
The table-item does not display a "&" even I declared a field as pic x.
What must I change?

Thanks.
H. Schepker
```

#### ↳ Re: PowerCobol V3 - Table-Item

- **From:** sbricklin@aol.com (SBRICKLIN)
- **Date:** 1999-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990123132813.29152.00000980@ng01.aol.com>`
- **References:** `<782h27$6re$1@namib.north.de>`

```
display in hex mode
```

##### ↳ ↳ Re: PowerCobol V3 - Table-Item

- **From:** "Hajo Schepker" <schepker@geocities.com>
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78l0a3$ofo$1@namib.north.de>`
- **References:** `<782h27$6re$1@namib.north.de> <19990123132813.29152.00000980@ng01.aol.com>`

```
How do mean it?

I put the data in a variable like "display-text pic x(40)" and then I call
the routine
CALL SETCELLTEXT OF TABLE1
       USING display-text row column
end-call


SBRICKLIN schrieb in Nachricht
<19990123132813.29152.00000980@ng01.aol.com>...
>display in hex mode
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
