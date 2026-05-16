[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL screen redefinition question

_2 messages · 1 participant · 2007-05_

---

### COBOL screen redefinition question

- **From:** "John B." <jlb@computac.com>
- **Date:** 2007-05-22T14:51:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179859928.887746@nfs-db1.segnet.com>`

```
I have the following field on a screen in a COBOL program...

         06 F-RCV-DATE         PIC X(08)        ROW 08 COLUMN 64
            SOURCE IS S-RCV-DATE
            OBJECT IS S-RCV-DATE.

...defined as...

       03 S-RCV-DATE       PIC X(08).
       03 FILLER REDEFINES S-RCV-DATE.
          04 S-SPL-LIST    PIC X(02).
          04 F-SPL-QTY     PIC X(01).
          04 S-SPL-QTY     PIC Z(05).

Using a PF-KEY switch, I'm either moving something into S-RCV-DATE or the
three redifined fields.  Problem is, even though S-SPL-QTY is defined as a
"Z" field, it acts like an "X".  (Example:  I key in a "20", which stays
left-justified and is ultimately saved as "20000".)  Is there any EASY way
to get what I'm looking for here without creating a whole second "twin"
screen or performing wacky routines to make the "X" into a "Z"????  Thanks!

John B.
```

#### ↳ Re: COBOL screen redefinition question

- **From:** "John B." <jlb@computac.com>
- **Date:** 2007-05-22T15:23:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1179861829.217928@nfs-db1.segnet.com>`
- **References:** `<1179859928.887746@nfs-db1.segnet.com>`

```
Well, I came up with a clunky solution...  Moving the S-SPL-QTY with
conversion to the numeric field I want it to end up in.  Doesn't make for a
pretty screen upon hitting enter, but it saves it correctly and brings it up
next time as such.

John B.

"John B." <jlb@computac.com> wrote in message
news:1179859928.887746@nfs-db1.segnet.com...
> I have the following field on a screen in a COBOL program...
>
…[17 more quoted lines elided]…
> screen or performing wacky routines to make the "X" into a "Z"????
Thanks!
>
> John B.
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
