[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem in calling btrieve functions thru Fujitsu ocobl 3.0

_1 message · 1 participant · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Problem in calling btrieve functions thru Fujitsu ocobl 3.0

- **From:** TKS-Schmitteck@t-online.de (Paul Schmitteck)
- **Date:** 1998-09-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tbkje$n3v$1@news00.btx.dtag.de>`

```
Hello everybody.
	We have a problem in calling the btrieve requester "BTRCALL" under  WIN
95.
We tried a sample program to access the btrieve files. The sample program
is very much similar to the sample program "FJ2BTRV .CBL" developed by Mr.
Todd A. Yancey of fujitsu corporation. In his program he calls the btrieve
requester "BTRCALL" as follows.

CALL "BTRCALL" WITH STDCALL USING   BTRIEVE-OPRERATION-CODE
							  	BTRIEVE-STATUS-CODE
								BTRIEVE-POSITION-BLOCK
								BTRIEVE-DATA-BUFFER
								BTRIEVE-DATA-BUFFER-LENGTH
								BTRIEVE-FILE-NAME
								BTRIEVE-KEY-NUMBER.

We compiled the program and tried to link it with the btrieve library file
W3BTRV7.LIB
When linking the following error occurs.

UNRESOLVED EXTERNAL  _BTRCALL@24.

Please explain the steps to link to the correct library file to access the
btrieve files.
Very urgent.
Practical answers are appreciable.

Thanks In Advance,
PAUL SCMITTECK.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
