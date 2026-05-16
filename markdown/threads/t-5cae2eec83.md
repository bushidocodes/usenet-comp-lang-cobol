[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# printer

_2 messages · 2 participants · 2001-04_

---

### printer

- **From:** "[PHH]Apollo" <swartenbroekxro@wanadoo.be>
- **Date:** 2001-04-28T18:53:38+02:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<9cesi6$1cu1$1@scavenger.euro.net>`

```
How do you print with a standard cobol 85 compiler (Micro Focus 2.0) to a
printer connected to lpt1?
```

#### ↳ Re: printer

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-04-28T17:49:25+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-dPfkLjWVKgo7@24-108-102-82.ivideon.com>`
- **References:** `<9cesi6$1cu1$1@scavenger.euro.net>`

```
On Sat, 28 Apr 2001 16:53:38, "[PHH]Apollo" 
<swartenbroekxro@wanadoo.be> wrote:

> How do you print with a standard cobol 85 compiler (Micro Focus 2.0) to a
> printer connected to lpt1?
> 
> 

Specify a file assignment to "lpt1:"

Specify the file as "organization line sequential"

open it extend or output

write to the file

close the file

---- selected code bits ------------

select out-file assign "lpt1:"
organization line sequential.

FD out-file.
01  a-record-name.
02  filler pic x(200)


open extend out-file
move "some stuff to print" to a-record-name
write a-record-name
close out-file

------ end code btis -------------

Good luck
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
