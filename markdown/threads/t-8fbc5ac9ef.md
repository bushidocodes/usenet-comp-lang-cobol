[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SUID bit set on a COBOL executable uner a HP-UX like OS - disable library search paths.

_2 messages · 2 participants · 2006-10_

---

### SUID bit set on a COBOL executable uner a HP-UX like OS - disable library search paths.

- **From:** robwlindsay@gmail.com
- **Date:** 2006-10-05T18:45:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160099105.345967.142020@m7g2000cwm.googlegroups.com>`

```
Has anyone seen this before?

The scenario:
We are setting the SUID bit on an executable so it will run as the
owner. This works fine in our Tru64 Unix, COBOL 4.1.30 environment.

Under HP-UX 11.23i MicroFocus Server Express the executable cannot find
it's libraries as the library search paths defined in LD_LIBRARY_PATH
and SHLIBPATH are ignored. See the excerpt from HP-UX dlopen man page
below:

"WARNINGS
      The environment variable LD_LIBRARY_PATH and SHLIB_PATH should
contain
      a colon-separated list of directories, in the same format as the
PATH
      variable (see sh(1)).  LD_LIBRARY_PATH and SHLIB_PATH will be
ignored
      if the process' real user id is different from its effective user
id
      or its real group id is different from its effective group id
(see
      exec(2))."

Does anyone have a workaround for this issue?

TIA
```

#### ↳ Re: SUID bit set on a COBOL executable uner a HP-UX like OS - disable library search paths.

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-10-06T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WIxVg.105385$R63.99095@pd7urf1no>`
- **In-Reply-To:** `<1160099105.345967.142020@m7g2000cwm.googlegroups.com>`
- **References:** `<1160099105.345967.142020@m7g2000cwm.googlegroups.com>`

```
robwlindsay@gmail.com wrote:
etc....

If you haven't already done so, join the Micro Focus Forum at 
microfocus.com and post your question under Server Express.

Jimmy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
