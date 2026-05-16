[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sample "solutions" to the "Right Justify" Question(s)

_1 message · 1 participant · 1999-09_

---

### Re: Sample "solutions" to the "Right Justify" Question(s)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7s0lt5$j7t@dfw-ixnews12.ix.netcom.com>`
- **References:** `<7rnb8v$l32@dfw-ixnews9.ix.netcom.com> <CnMD3.1757$eJ2.18573@news1.mia> <37dfa498@news3.prserv.net> <QnSD3.2465$eJ2.25322@news1.mia> <37e03c3a@news3.prserv.net> <37e03e80@news3.prserv.net> <7rq246$1em$11@ssauraab-i-1.production.compuserve.com> <37e0e12d@news3.prserv.net> <37E0EF39.D8012591@zip.com.au> <37e18a86@news3.prserv.net> <37E34920.FA92BF20@att.net> <37e36c45@news3.prserv.net>`

```

Leif Svalgaard <lsvalg@ibm.net> wrote in message
news:37e36c45@news3.prserv.net...
> so COBOL II was not conforming to the standard.
>

Leif,
  Actually with VS COBOL II, it WAS conforming - because (as the
"substantive change" text indicates in the next Standard), the ONLY
conforming source code that would ever have any different at run-time was
one which references the Intrinsic Fucntion "RANDOM" (because of
"side-effects" of each reference) and VS COBOL II doesn't support Intrinsic
Functions.  Although I have (in the other part of this thread) pointed out
ways to "test" various compilers using invalid data and subscript
violations, these really canNOT test whether a compiler is "conforming" or
not - because all of these "data problems" produce "unpredictable results"
in the '85 Standard - and anything that you do is OK.

THEREFORE, (with the VERY RARE case of someone who actually cares how far
along a RANDOM "chain" gets) there is NO WAY that you can call an '85
Standard "non-conforming" because it does the evaluation in the other
order - as the '85 Standard only tells you what results to get - not how to
get there.

HAVING SAID THAT,  I am glad that the next Standard will get rid of this
"problem" and would encourage people to get their current compiler vendors
to work the "new" way.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
