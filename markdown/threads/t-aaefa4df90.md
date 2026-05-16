[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Get name of calling module

_1 message · 1 participant · 2000-07_

---

### Re: Get name of calling module

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-14T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<8kohfn$bnp$1@slb2.atl.mindspring.net>`
- **References:** `<20000713.6272297@knigge.local.net>`

```
1) Generally, you may find that you will get answers more targeted at "poor
COBOL coders" if you ask this type of question in comp.lang.cobol rather than
via IBM-MAIN.

2) For those relying on a "set" order and number of items in the back-chain
list, you might want to look at: (also, I believe - but am not positive that
this changed between VS COBOL II and IBM COBOL for this-and-that)
 http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/CEEA5010/2%2e5

3) You might want to look at the following for finding the TGT
 http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYMG201/5%2e1%2e5

4) Under LE, there is a "way" (somewhat complicated - but can be done in
COBOL without requiring Assembler) to "register" a condition handler in your
calling program - and then test which program "set" this condition handler in
your subprogram.

5) Finally, I believe there was a discussion about submitting a SHARE
requirement to get the name of the CALLing program via an LE callable
service.  I don't know what happened with this - or even if such a
requirement was submitted.  If you are a member of SHARE, you might want to
look into this.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
