[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accessing A Modem From MF Cobol

_1 message · 1 participant · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: Accessing A Modem From MF Cobol

- **From:** "David Mowat" <dsmowat@clear.net.nz>
- **Date:** 1998-07-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6nq2r9$i16$1@fep5.clear.net.nz>`
- **References:** `<355ba18d.89040623@news.mci2000.com> <359dfeec.36304581@news.comcen.com.au>`

```

You can open a file whose file name is "Com2:"
Here is an example :-

SELECT COMM-STRING
   ORGANIZATION IS SEQUENTIAL
   ACCESS MODE IS SEQUENTIAL
   ASSIGN TO COMM-FILE-NAME
   FILE STATUS IS FILE-STATUS.

   FD COMM-STRING.
   01 C-STRING                   PIC X(80).

Regards ...
David Mowat
DSMowat Computer Consulting
D&M Computer & Technology Services Ltd
dsmowat@clear.cut.net.nz (remove cut)
If you want to start a Debt Collection Department or Agency, or go on the
Web, I have the Software.




>---- unless the
>COBOL open-file statement can be pointed at a
>COMMS port (I haven't tried that -- too obvious?)
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
