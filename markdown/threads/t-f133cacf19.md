[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (IBM) SHARE - LNGC requirements

_1 message · 1 participant · 2004-03_

---

### Re: (IBM) SHARE - LNGC requirements

- **From:** robin <robin_v@bigpond.mapson.com>
- **Date:** 2004-03-20T14:25:48+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1,ibm.software.cobol,ibm.software.le,ibm.software.pli
- **Message-ID:** `<MvY6c.117466$Wa.51328@news-server.bigpond.net.au>`

```
From: "Mark Yudkin" <myudkinATcompuserveDOTcom@nospam.org>, CompuServe Interactive Services
Date: Fri, 19 Mar 2004 13:12:33 +0100

| I think I see what you're getting at.
|
…[13 more quoted lines elided]…
| correct base, calculation is carried out using decimal arithmetic.
.
No, when the arguments are fixed binary, and the result is
scaled, the result of ADD, SUBTRACT, MULTIPLY, and DIVIDE
is always FIXED DECIMAL, as I said before.
.
Furthermore, the precision & scale expressed to these functions
e.g., 31 and 5 in     DIVIDE (J, K, 31, 5)
are taken as the number of DECIMAL digits, not BINARY digits.
.
Might be a good idea to check this out on your system.
.
Try (with 31 digit decimal):
MULT:
   PROC OPTIONS (MAIN);
      DECLARE (J, K) FIXED BINARY (31);
      J = 1234; K = 1233;
      PUT LIST (DIVIDE(J, K, 31, 25));
END MULT;
.
       1.0008110300081103000811030 
.
| "robin" <robin_v@bigpond.mapson.com> wrote in message news:5uM5c.106620$Wa.11848@news-server.bigpond.net.au...
| > "John W. Kennedy" <jwkenne@attglobal.net> writes: > robin wrote:
…[20 more quoted lines elided]…
| > > John W. Kennedy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
