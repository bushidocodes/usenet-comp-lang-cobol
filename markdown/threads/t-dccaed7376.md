[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DFSORT Y2K: Full Date Formats for COBOL and More

_1 message · 1 participant · 1998-11_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Date and calendar processing`](../topics.md#dates)

---

### DFSORT Y2K: Full Date Formats for COBOL and More

- **From:** fyaeger5@vnet.ibm.com
- **Date:** 1998-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71ljgq$8ca$1@nnrp1.dejanews.com>`

```
DFSORT's new generation of Year 2000 features handle CH, ZD and PD
full dates like yymmdd, yyddd, yymm, yyq, mmddyy, dddyy, mmyy and qyy,
and their special indicators like zeros and nines. You no longer have
to split dates into year and non-year pieces, and you don't need
E61 exits to handle special indicators.  You can now compare dates to
constants and other dates, transform CH, ZD and PD two-digit year
dates to CH and PD four-digit year dates and more!

This new generation of Year 2000 features is available for Release 13
via PTF UQ22533 and for Release 14 via PTF UQ22534 (the APAR is
PQ19684).

Our updated SORT2000 paper explains how to use DFSORT's new full date
formats, as well as the earlier year formats, in the SORT, MERGE,
INCLUDE, OMIT and OUTFIL statements.  You can look up a particular
date and go directly to examples of the DFSORT control statements
you need.

SORT2000 also explains how to use DFSORT's new Year 2000 features with
COBOL, either automatically with COBOL MLE or explicitly without MLE.

You can browse or download SORT2000 from the DFSORT home page at URL:

http://www.ibm.com/storage/dfsort/

Frank Yaeger - DFSORT Team (Specialties: Y2K, Symbols, OUTFIL, ICETOOL)
fyaeger@vnet.ibm.com





-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
