[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF ISAM PROBLEMS.

_1 message · 1 participant · 2004-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### MF ISAM PROBLEMS.

- **From:** Donald Tees <donald_tees@sympatico.ca>
- **Date:** 2004-11-18T14:54:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B87nd.28457$rc.1613166@news20.bellglobal.com>`

```


I am working on a system that makes extensive use of Isam to build 
sorted tag files ... that is, the transactions are built into a file by 
key value, then the file re-read sequentially to link back to the 
original transactions during the report stage.  The compiler is MF 
3.0.14 running on Windows familly machines.

A strange Isam problem keeps cropping up ... when the file is read back, 
several records will be missing. This will happen one time out of every 
several thousand times the program is run, but when it does, it is 
absolutely repeatable. Same data, same problem.  I can even dump the 
file to line sequential(using rebuild), and *see* the records that were 
dropped. I trace through, and "read next" blows right by them as if they 
were not there, even though the dump dumps them out in exactly the right 
place.

If I change the key size by a character or two (stuff is strung into a 
key 50 to 100 characters long, and there is lots of trailing space) then 
re-run with the exact same data, the problem goes away. Change the key 
size back, the problem comes back. I leave it changed, and ship it off 
to the customer.

Three or four months later, using the new key size, the problem will 
come back with a different set of data.  It will work for thousands of 
runs before this happens. I change it back to what it was three-four 
months previously ... the problem goes away for another several months.

It is pretty obviously some obscure Isam bug, has anybody run into 
anything like it before?  If so, is there a solution?

Donald
PS to Jimmy.  I have already checked knowledge base <G>.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
