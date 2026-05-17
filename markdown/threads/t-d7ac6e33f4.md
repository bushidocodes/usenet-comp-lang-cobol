[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problems with MicroFocus NetExpress and multithreading

_1 message · 1 participant · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Problems with MicroFocus NetExpress and multithreading

- **From:** "pit..." <ua-author-11006638@usenetarchives.gap>
- **Date:** 1998-07-30T09:31:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35c06f9e.263365@news21.bellglobal.com>`

```
I have encountered a problem that I hope someone here can help me with. I'm
getting an intermittant Windows NT Access Violation abend in CBLRTSM.DLL. My
programs run in a multithreaded environment, and may be active in many threads
at once. These abends don't seem to be application code related, as the exact
same code runs on MVS properly, and has been stable in that environment for over
a year now.

Our code provides a generic communications interface to other applications and
our execution environment consists of:

C++ 'server' application programs
which use RPC to converse to C++ 'transaction dispatcher' programs
which call my COBOL communications API program (in multiple threads)
which calls various communications protocol APIs (CPIC/Winsock/MQSeries)

These programs run under Windows NT 3.51 and Windows NT 4.0 servers, and use
various levels of SNA Server (for CPIC), MQSeries/NT, and Winsock.

My COBOL program is the head of a DLL chain that extends about 5 levels deep,
and consists of mostly NetExpress COBOL (with some MS VC 5 application DLLs for
WinSock interfacing).

The failing suite is a release above the last successfull suite; some logic
changes were made (which work in a less-loaded multi-threaded environment and on
MVS), but my primary suspect for our problems is our new use of LOCAL-STORAGE in
addition to THREAD-LOCAL-STORAGE.

The abends we see are Access Violations, and a stack trace shows the failing
instruction at address 600b116b in CBLRTSM.DLL. CBLRTSM.DLL was invoked directly
from my mainline module (the first COBOL DLL in the chain) and storage dumps of
TLS show fields that indicate no subsequent CALLs have been performed.
Examination of storage/disassembly of the logic in the COBOL program prior to
the failing call to CBLRTSM shows an access to a storage area that presently
contains the string 'THREAD_PROGRAM_UNLOCK'.

We are using NetExpress V2.0, revision 017, and the CBLRTSM.DLL is 444416 bytes
long (dated 12/6/97).

If anyone has encountered similar problems with NetExpress, and wouldn't mind
sharing your experiences, I'd appreciate a reply (either here or by email).


Thanks...




Lew Pitcher
System Consultant, Delivery Systems Architecture
Toronto Dominion Bank

(pit··.@tdb··k.ca)


(Opinions expressed are my own, not my employer's.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
