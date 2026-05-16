[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Redefine mismatches

_2 messages · 2 participants · 2000-02_

---

### Redefine mismatches

- **From:** "Tim Mueller" <tmiller16@yahoo.com>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38b6a154$1_2@news2.one.net>`

```
We are using both COBOL 74 and COBOL for VSE on two different boxes in our
shop.  If you mistakenly use a longer length to redefine a field, for
example, taking a 6 position field and redefining it using  8 positions, the
COBOL 74 compiler will flag the error, but the COBOL for VSE compiler does
not.

Is there any way to make the COBOL for VSE compiler flag that error?
```

#### ↳ Re: Redefine mismatches

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<896g7n$255$1@nntp2.atl.mindspring.net>`
- **References:** `<38b6a154$1_2@news2.one.net>`

```
Are you compiling with FLAG(I I)?  I can't remember if the VSE compiler has
an informational message for this, but it might.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
