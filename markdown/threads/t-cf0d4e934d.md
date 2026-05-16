[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP:MF COBOL 1.2 ON Windows NT Server 4.0 (SP3)

_2 messages · 2 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### HELP:MF COBOL 1.2 ON Windows NT Server 4.0 (SP3)

- **From:** "Dataware ���������" <dataware@otenet.gr>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t2mjb$m40$1@ns1.otenet.gr>`

```
I have a program running on a network, using as server  Windows NT 4.0 with
Service Pack 3 and as terminals PCs with Windows 95 B (the hard disk drives
are formatted with FAT 32). The protocol is TCP/IP. The connection is using
a Hub (UTP).The compiler i am using is Microfocus Cobol 1.2

The problem i have is that files get corrupted every day (9-041) [Corrupt
indexed file].
When i've copied all files and programs to one PC and ran the program there,
no problem occured.

If you've met this situation and found some solution please let me know.




Thank you


Goulioumis Fotis
```

#### ↳ Re: HELP:MF COBOL 1.2 ON Windows NT Server 4.0 (SP3)

- **From:** "J���rgen Ibelgaufts" <ibelgaufts@gfc-net.de>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F54759.5B95ACB5@gfc-net.de>`
- **References:** `<6t2mjb$m40$1@ns1.otenet.gr>`

```
In case you run the program on the win95 client and the files live on
the winnt server, you are opening the files across the network. my
solution for this would simply be: do not open files across networks
because the files break when you have communication problems. 

This means that the programs have to run on the nt server and only send
their screens to the win95 clients.

(maybe this won't help you much becaus it is a completely different
architecture)

juergen ibelgaufts

----------------------------------------------------------------------

Dataware ï¿½ï¿½ï¿½ schrieb:
> 
> I have a program running on a network, using as server  Windows NT 4.0 with
…[13 more quoted lines elided]…
> Goulioumis Fotis
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
