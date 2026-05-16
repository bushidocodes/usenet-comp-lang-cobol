[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "Minor" Enhancement in IBM COBOL for OS/390 & VM (V2R2)

_1 message · 1 participant · 2000-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### "Minor" Enhancement in IBM COBOL for OS/390 & VM (V2R2)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8t1hn0$jed$1@slb6.atl.mindspring.net>`

```
Every few months either the IBM-MAIN list or the comp.lang.cobol newsgroup
gets into a discussion of WHY can't you get the address of a Working-Storage
item using the SET pointer-item to ADDRESS OF syntax.  Up until now, you had
to use the "artificial" technique of creating a nested program, call it -
and let it get the address from linkage section.

I just noticed in the V2R2 "changes" section, that this restriction is being
removed (and IBM will join MERANT and other vendors who already support this
syntax - that is included in the draft of the next Standard).

See:
 http://www.s390.ibm.com/bookmgr-cgi/bookmgr.exe/BOOKS/IGYLR205/FRONT_2%2e1

OBVIOUSLY, it will be a while before this is available in every (most?)
shops - but it does give you at least one reason to upgrade (along with the
MORE IMPORTANT issues such as TRUNC(BIN) performance enhancements and
31-digit number support)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
