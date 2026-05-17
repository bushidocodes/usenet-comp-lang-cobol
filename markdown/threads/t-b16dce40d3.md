[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WAIT or similar function in COBOL

_3 messages · 3 participants · 1997-01 → 1997-02_

---

### WAIT or similar function in COBOL

- **From:** "kalpataru barman" <ua-author-17071492@usenetarchives.gap>
- **Date:** 1997-01-29T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32F0DF3B.34F3@mail-me.com>`

```

I am dealing with a program in VS COBOL II ( IBM Mainframe/MVS ), where
I need to submit this program which will check a DB2 table every 15
minutes until reaches a specified time.
The program is written with the following logic :
ACCEPT s time and checks if the difference is 15 minutes in a loop

I dont want to hold CPU time. I read in the manual about WAIT verb,
but it is not ANSI ( so, not supported in VS COBOL ) , it is a
CODASYL standard verb.
Is there any other way to put the program in a wait status for a
specified period of time ( In CICS I could use "EXEC CICS WAIT...",
but this is a COBOL/DB2 program ).
```

#### ↳ Re: WAIT or similar function in COBOL

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-01-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b16dce40d3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32F0DF3B.34F3@mail-me.com>`
- **References:** `<32F0DF3B.34F3@mail-me.com>`

```

No way provided in VS COBOL II.

A simple assembler routine could issue a STIMER WAIT,BINTIVL=loc where loc
was a fullword containing the wait interval in .01 seconds (as I recall).

See the VS COBOL II programmer's guide for a skeletal program.

I recently implemented a routine like this, seems like it must have been
10 lines total. In the particular case, the application needed to delay
sending output to a on-line terminal (simulated 3270, but not really very
well simulated), since the terminal would saturate if multiple messages
arrived too quickly.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: WAIT or similar function in COBOL

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-02-02T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b16dce40d3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32F0DF3B.34F3@mail-me.com>`
- **References:** `<32F0DF3B.34F3@mail-me.com>`

```



Arn Burkhoff wrote in article
<32F··.@inj··y.com>...
› Kalpataru Barman wrote:
›› 
…[16 more quoted lines elided]…
› 

How about an EXEC CICS START with the time option? (I think this is what
you were advocationg, just wanted to make it clearer).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
