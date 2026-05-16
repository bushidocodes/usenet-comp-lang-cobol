[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACUODBC internation characters

_3 messages · 2 participants · 2006-09_

---

### ACUODBC internation characters

- **From:** "bruno" <bruno.goonissen@skynet.be>
- **Date:** 2006-09-29T08:50:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1159545042.312095.210710@i42g2000cwa.googlegroups.com>`

```
Hi !

Can anyone help me with this problem ?

- When I want to load the data from the ACUfiles in to f.e. Ms Excel,
special characters like è, é, ö, ... are replaced by others.  Reason
would be that  AcuCocol works with the PC-8 charcter set, while windows
works with the ANSI-charcter set.

- In the 'ACUODBC advanced options' of the DSN-settings, I specified a
mapfile to solve this problem (the hex.dec. code for the client and the
DB are mentioned), but it still doesn't the conversion ...

f.e. : the file mappings.txt contains the following lines:
0xFC 0x81
0xF6 0x94
0xD6 0x99
0xDC 0x9A

D6 hexadecimal = 214 decimal = Ö in ANSI
99 hexadecimal =  153 decimal = Ö in PC-8

Kind regards
Bruno
```

#### ↳ Re: ACUODBC internation characters

- **From:** sgbojo@gmail.com
- **Date:** 2006-09-29T09:15:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1159546509.424825.97350@i3g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1159545042.312095.210710@i42g2000cwa.googlegroups.com>`
- **References:** `<1159545042.312095.210710@i42g2000cwa.googlegroups.com>`

```

bruno wrote:
> Hi !
>
…[19 more quoted lines elided]…
>

When setting up the DSN for AcuODBC there is an advanced option where
you can choose the ANSI character set. This should help.
> Kind regards
> Bruno
```

##### ↳ ↳ Re: ACUODBC internation characters

- **From:** "bruno" <bruno.goonissen@skynet.be>
- **Date:** 2006-09-29T14:01:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1159563680.773274.213360@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1159546509.424825.97350@i3g2000cwc.googlegroups.com>`
- **References:** `<1159545042.312095.210710@i42g2000cwa.googlegroups.com> <1159546509.424825.97350@i3g2000cwc.googlegroups.com>`

```
It works !!!!!
Thanks !!!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
