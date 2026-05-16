[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sort on BS2000 and OS390 /Sort-Control

_2 messages · 2 participants · 2004-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`VSAM, files, sorting`](../topics.md#files)

---

### Sort on BS2000 and OS390 /Sort-Control

- **From:** Joerg.Brehe@set-software.de (j?rg brehe)
- **Date:** 2004-06-21T03:20:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f6b3f56.0406210220.10834e32@posting.google.com>`

```
I try to code a routine in cobol on IBM and BS2000 systems. I will
write some options into a dataset which controls my sort. I give the
average length of my records and the filesize. I use the sort-control
register, and give a ddname of my temporary dataset, which i have
allocate dynamical. I see this works by IBM/OS390 systems. I have
found dfsort don't care about the SORT-MODE-SIZE. I get the message,
dfsort will have better performance, if i give the average length. so
I try it with my dataset options "averagelength" and it works.

However I see no register for the bs2000 system. It seems there is no
sort-control. Can I work on BS2000 with the "SORT-MODE-SIZE" and
"SORT-FILE-SIZE" and it's works? I can't test this on our system.

The next question: If i use Syncsort. can it be, that Synsort works
well, if i use the "SORT-MODE-SIZE" and "SORT-FILE-SIZE"? I can't find
an option in SYNCSORT with the name "averagelength". And the syntax of
the parameters is not like dfsort in some cases. In DFSORT I begin
with "Option = ..."
In SYNCSORT i shall not use the word "option".-

thanks forward

jï¿½rg
```

#### ↳ Re: Sort on BS2000 and OS390 /Sort-Control

- **From:** Karl Kiesel <Karl.Kiesel@fujitsu-siemens.com>
- **Date:** 2004-06-22T08:32:38+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40D7D286.BC11F0BA@fujitsu-siemens.com>`
- **References:** `<7f6b3f56.0406210220.10834e32@posting.google.com>`

```
j?rg brehe schrieb:
> 
> I try to code a routine in cobol on IBM and BS2000 systems. I will
…[11 more quoted lines elided]…
> 
With both COBOL Compilers on BS2000 (COBOL85 rsp COBOL2000) a
sort-control register is not supported; possible special options for
sorting are supported by language means (sliding window for 2 digit
century date rsp special code sets); both Compilers support
SORT-MODE-SIZE and SORT-FILE-SIZE for improving sorting efficiency.

Karl Kiesel
Fujitsu Siemens Computer. Mï¿½nchens
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
