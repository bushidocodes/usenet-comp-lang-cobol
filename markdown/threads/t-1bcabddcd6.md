[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Animating my program

_2 messages · 2 participants · 2000-04_

---

### Animating my program

- **From:** "Barney" <neil_harrison@bigfoot.com>
- **Date:** 2000-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eid58$lvh$1@news8.svr.pol.co.uk>`

```
Hi,
    In a program I have written I have a dataname PART-NUM which is a PIC
9(8) field. This field is to be tested for numeracy within the program. When
I place valid data for it into my dummy file everything goes as planned.
However, when I place non-numeric data into it, my program is supposed to
detect this and Perform an error routine. When I try to animate my program
with this invalid data in the dummy file I get an error message telling me
of this invalid data. The problem I then face is that to continue animating
the rest of the program I have to skip the statement where this invlid data
is read in. Thus my error routine is not carried out. Can anybody shed any
light on this for me please. I am using Microfocus Personal COBOL for
Windows.
   Regards,
    Barney.
```

#### ↳ Re: Animating my program

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eifpu$6qp$1@slb1.atl.mindspring.net>`
- **References:** `<8eid58$lvh$1@news8.svr.pol.co.uk>`

```
You haven't shown us your exact code, but PROBABLY the thing to do is to keep
your numeric definition of the field - but add a REDEFINES of it which is PIC
X(8).  Then test that field (the PIC X field) for "IF NUMERIC" before trying
to reference the numeric field.  If this fails the IF NUMERIC test, you
should perform your error routine - if not, continue processing the numeric
version of the field.

ALTERNATIVELY (and not as good an idea) check into running/animating the
program with the "-F" run-time switch.  (I assume it is a 163 run-time error
that you are seeing).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
