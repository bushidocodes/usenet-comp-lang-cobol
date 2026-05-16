[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Initializing 3-d Table?

_1 message · 1 participant · 1999-01_

---

### Re: Initializing 3-d Table?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77lkrt$erj@dfw-ixnews3.ix.netcom.com>`
- **References:** `<369b90af.5665969@news> <369c6df8.14705415@news3.ibm.net> <369e4e89.6823352@news>`

```
IBM did some APAR fixes for INITIALIZE performance several years ago.  If
you are running on a current or currently maintained IBM mainframe COBOL,
you shouldn't see real serious problems with INITIALIZE performance.  If you
do, I think IBM would like to hear about this ASAP.  There are (I think)
some problems still in cases where you have an ODO (Occurs Depending ON) -
but I don't recall the details on this.

If you are still running an early version of VS COBOL II without much
maintenance applied, then YES, you will see serious performance hits with
INITIALIZE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
