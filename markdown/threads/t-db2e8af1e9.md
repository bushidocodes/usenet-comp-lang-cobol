[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need help with COBOL MVS functions

_2 messages · 2 participants · 1999-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Need help with COBOL MVS functions

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<933077114.24511@www.remarq.com>`
- **References:** `<7n5d40$6f1$1@news.tdh.state.tx.us>`

```
No, the LENGTH function as well as the LENGTH OF special
register returns the current amount of bytes that are used
in main storage. This function does not know which
characters you want to exclude. Try the INSPECT verb
instead (INSPECT xxx TALLYING yyy FOR LEADING SPACES)!

Instead of SUBSTRING, you can use the reference modification
in COBOL. Its sysntax is xxxx(m:n) where m and n are numeric
literals or numeric variables. You can use this statement on
both sides of a MOVE, IF or EVALUATE. m means the starting
position, n the lenght. in your sample, WS-NAME(2:2) would
be 'OT'.

And to answer your third question, no, you cannot define
your own functions. AFAIK, this will be allowed in the next
release of the standard, but I don't know whether IBM has
planned such functions for the next releases fo the COBOL
compiler. The most current is 'IBM COBOL for OS/390 & VM
Version 2 Release 1 Modification 1' and this one doesn't
allow you to write your own functions.

You might want to read the Language Reference. If you don't
have it in printed form, you could consult the following
URL:
http://www.s390.ibm.com:80/bookmgr-cgi/bookmgr.cmd/BOOKS/IGY
LR204/CCONTENTS
(all on one line!)
Or you could order the manual in printed form. It's the
COBOL Language Reference, Document Number SC26-9046-03.

Cheers

Daniel



* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: Need help with COBOL MVS functions

- **From:** "Vic Hariton" <vic.hariton@cpa.state.tx.us>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nkhbj$3kp$1@news.tdh.state.tx.us>`
- **References:** `<7n5d40$6f1$1@news.tdh.state.tx.us> <933077114.24511@www.remarq.com>`

```
I ended up using the INSPECT statement.  I was excited to see functions
being provided in COBOL and wanted to try them out.  Got to say I was a
little disappointed not to see the same functionality as other languages
have.  Maybe it's a performance thing.

I will try using the "reference modification" approach for substring.

Thanks for your help,
 Vic
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
