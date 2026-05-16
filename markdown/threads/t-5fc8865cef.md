[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# generate rtsora with error and return value from rtsora

_1 message · 1 participant · 2003-10_

---

### generate rtsora with error and return value from rtsora

- **From:** PRE <member38102@dbforums.com>
- **Date:** 2003-10-09T11:51:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3407745.1065714687@dbforums.com>`

```

hi



1. I try to generate rtsora but i obtain the next missing error:

 /usr/ccs/bin/make -f ins_precomp.mk rtsora

/usr/ccs/bin/make -f
/export/home/oracle/OraHome1/precomp/lib/ins_precomp.mk rel

ink EXENAME=rtsora

Linking /export/home/oracle/OraHome1/precomp/lib/rtsora

cob64: can not execute as

cob64: error(s) in assembling /var/tmp/cobAAAVHa4mm/ldtab.s



i dont be able to correct the problem.

Is mandatory to generate rtsora or  can i use rtsora provided by Oracle?



2. Using this rtsora:

From Ux Solaris 8 to control the return value of an rtsora cobol
operation.



Is there some precompiler/compiler or run directives/parameter by o
indicate th return value, for example 0 for success and >4 for fail?



In this moment, we obtain several values >0 when success.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
