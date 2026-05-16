[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP: Cobol 4.1 rev 30 and AIX 4.3.3 on an F80

_1 message · 1 participant · 2001-03_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HELP: Cobol 4.1 rev 30 and AIX 4.3.3 on an F80

- **From:** james@rubiconcs.co.uk (James Garwood)
- **Date:** 2001-03-03T09:21:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3aa0b58c.599602@news.dircon.co.uk>`

```
Do you by any chance have Micro Focus (Merant) Cobol 4.1 rev 30
working on an IBM RS/6000 F80 with AIX 4.3.3. The F80 has a dual RS64
III processor card so is running bos.64bit.

Basically I have a customers machine in this configuration and at
random the cobol run-time will fail to open sequential files with the
MFIO error file containing an errno = 22 error on the file open. The
last status is either 3/5 or 0/0. 

The problem is not isolated to our application sequential files as
they also get errors against the ADISCTRL and cobkeymp files from
/usr/lib/ocobol which causes them screen display and key mapping
issues.

We never get errros related to open our ISAM files and the problem can
manifest when we have a single users on the system or 40 plus.

Thanks for your help/time.

James Garwood
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
