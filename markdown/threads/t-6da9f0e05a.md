[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Output file passed to Davox where money field appears incorrect.

_2 messages · 2 participants · 2004-11 → 2004-12_

---

### Output file passed to Davox where money field appears incorrect.

- **From:** chlebsco@enter.net (Scott J. Chlebove)
- **Date:** 2004-11-18T12:22:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a4d6da2.0411181222.13c24502@posting.google.com>`

```
A COBOL program generates an output file, which is further transferred
to a predictive dialer system known as Davox. A partial listing of the
file layout with the relevant money field is as follows...

COBOL...                                    DAVOX....
....                                        ....
   VS-AT-CUT-OUT-PEND   PIC 9(8)V(2)        OVERDUE     MONEY 9
....                                        INOVERDUE   CHAR 1
                                            ....


"VS-AT-CUT-OUT-PEND"   maps to   "OVERDUE", though, when viewed in
Davox, the units place from the cents of "VS-AT-CUT-OUT-PEND" winds up
in "INOVERDUE". Something else that may be relevant is, it appears
that on the Davox side, two zeroes pad the rightmost portion of
"OVERDUE". From my own inpection, Eighteen-hundred thirty-three
dollars and sixty-nine cents appears properly on the COBOL output file
(1833.69), but after loaded to Davox it looks (so I am told) much
different (183.3600 in "OVERDUE"; 9 in "INOVERDUE").

We have no one on site to modify Davox, so I am charged with looking
at resolving this from the "supply" side (COBOL). I'd tried to change
VS-AT-CUT-OUT-PEND to PIC 9(7)V(2) and added a PIC X(1) FILLER field,
though it was NOT output correctly, as a matter of fact, the same
dollar amount became 183.36 in VS-AT-CUT-OUT-PEND and 9 in FILLER,
when I'd viewed the output file.

My thoughts are that I may need to somehow REDEFINE
"VS-AT-CUT-OUT-PEND" as I'd noted ( PIC 9(7)V(2) ), though I'm not
certain how to do this.
Maybe convert PIC 9(8)V(2) to character (PIC X (11)) then to PIC
9(7)V(2)???

Any suggestions?
```

#### ↳ Re: Output file passed to Davox where money field appears incorrect.

- **From:** carlos_avalos1@yahoo.com
- **Date:** 2004-12-06T06:10:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1102342203.137083.17680@z14g2000cwz.googlegroups.com>`
- **In-Reply-To:** `<6a4d6da2.0411181222.13c24502@posting.google.com>`
- **References:** `<6a4d6da2.0411181222.13c24502@posting.google.com>`

```

Scott J. Chlebove wrote:
> A COBOL program generates an output file, which is further
transferred
> to a predictive dialer system known as Davox. A partial listing of
the
> file layout with the relevant money field is as follows...
>
…[8 more quoted lines elided]…
> Davox, the units place from the cents of "VS-AT-CUT-OUT-PEND" winds
up
> in "INOVERDUE". Something else that may be relevant is, it appears
> that on the Davox side, two zeroes pad the rightmost portion of
> "OVERDUE". From my own inpection, Eighteen-hundred thirty-three
> dollars and sixty-nine cents appears properly on the COBOL output
file
> (1833.69), but after loaded to Davox it looks (so I am told) much
> different (183.3600 in "OVERDUE"; 9 in "INOVERDUE").
…[14 more quoted lines elided]…
> Any suggestions?

Did you ever figure this one out?  Normally Davox takes a text file and
imports it into a call table.  Head that txt file for me and I will
probably be able to help you.
you can email me at carlos_avalos1@yahoo.com too.

-Carlos
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
