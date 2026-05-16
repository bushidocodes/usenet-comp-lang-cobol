[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Deperate student requires help with COBOL program

_1 message · 1 participant · 1998-06_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Re: Deperate student requires help with COBOL program

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1998-06-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<358FA798.50BCAB18@zip.com.au>`
- **References:** `<357864C7.54A9@virgin.net> <357AEF20.4D41@virgin.net> <357B38E3.8AF@nac.net> <-1306982101510001@a138009.san1.as.crl.com> <6m3ami$2rg_001@news.netdirect.net> <-1606981901340001@a138015.san1.as.crl.com> <6m8udm$1cg_001@news.netdirect.net> <-1706982253330001@a138003.san1.as.crl.com> <6mbcvb$hfa@dfw-ixnews9.ix.netcom.com> <358BB546.98C74350@zip.com.au> <6mmf6a$29c_002@news.netdirect.net>`

```

(Doug Miller) wrote:
> 
> In article <358BB546.98C74350@zip.com.au>,
…[14 more quoted lines elided]…
> things down too much? Sorry, but this just doesn't make sense.

Thinks....  er um you are right.  If I am doing the check why can't I do
the check cleanly.

In my defense a simple abend routine adds far less overhead on code than
trying to continue when things do screw up.  I have seen a deep looping
program that tried to recover from a problem and every second statement
ended up IF NOT ERROR multiply this but millions of transactions and...
It does come down to the 90/10 rule.

Sometimes the simple solution is the simple solution.  Use you own
training to determine when and where to apply the generic rules and when
to break them.

The final point is even with a cleanly defined interface things can and
do go wrong. For example unlabelled tapes coming from offsite get
shuffled and cause havoc in production programs that have been running
for years.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
