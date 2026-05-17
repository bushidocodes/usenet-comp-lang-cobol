[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [HELP] With MF *.idx files

_2 messages · 2 participants · 1995-11_

---

### [HELP] With MF *.idx files

- **From:** "win..." <ua-author-3391892@usenetarchives.gap>
- **Date:** 1995-11-19T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<48qcvj$nt7@Mercury.mcs.com>`

```
Here's a tough question..maybe not for some of you. :-)

We need to parse a micro focus IDX file correctly to
read the index.

Is the micro focus IDX file format known? If someone
can help, please email: win··.@m··.com

Thanks in advance.

windsor
```

#### ↳ Re: [HELP] With MF *.idx files

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1995-11-20T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dda1db00ec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<48qcvj$nt7@Mercury.mcs.com>`
- **References:** `<48qcvj$nt7@Mercury.mcs.com>`

```
In message <<48qcvj$n.··.@Mer··s.com>> win··.@M··.COM writes:
› 
› We need to parse a micro focus IDX file correctly to 
…[3 more quoted lines elided]…
› can help, please email: win··.@m··.com

I have done a simple C utility that reads the .idx file and
displays the header data: record length, key structure etc.
It can also step down the data file counting the valid records
(undeleted) to give a % of used space against actual space.

But this only works for the Level II format (IDXFORMAT"2").
I started on code to step down the indecies but while it
did actually find the index blocks I never finished it.

The CISAM format is described and Level II is a modified form
of this. I haven't worked out the Cobol/2 default format.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
