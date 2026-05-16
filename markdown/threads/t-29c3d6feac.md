[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q: UNIX: OUTPUT-FILE assigned by environment variable

_2 messages · 2 participants · 2000-01_

---

### Q: UNIX: OUTPUT-FILE assigned by environment variable

- **From:** Uwe Wahser <uwe.wahser@mlp-ag.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387C3275.2F127161@mlp-ag.com>`

```
Hello all,

we have some cobol-jobs running under UNIX which assign an output file
by ASSIGN TO '$OUTFILE' (organization sequential, access sequential).
OUTFILE has been properly assigned in the calling batch file.

For some reason the OPEN statement will produce a file status 35,
sometimes 37, for some jobs. A workaround was to read the environment
variable into a unix variable, and to do the assign via that
unix-variable. Is that a solution? or are we only hiding a problem?
which reason could be behind the problem?

thanks, uwe
```

#### ↳ Re: UNIX: OUTPUT-FILE assigned by environment variable

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85ih41$dpc$1@nntp8.atl.mindspring.net>`
- **References:** `<387C3275.2F127161@mlp-ag.com>`

```
Which COBOL are you using?  There are some COBOLs (and with some compiler
options) where using $OUTFILE *without* the quotes will work (do exactly what
you want).

I know that Micro Focus has some an option - and I am pretty certain that IBM
does too.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
