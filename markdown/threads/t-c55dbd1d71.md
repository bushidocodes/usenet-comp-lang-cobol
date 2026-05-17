[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call C from COBOL? how?

_5 messages · 5 participants · 1995-05 → 1995-06_

---

### Call C from COBOL? how?

- **From:** "bhoopes" <ua-author-17088137@usenetarchives.gap>
- **Date:** 1995-05-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1995May31.154303.1@uabpa>`

```
S.O.S
How does one go about calling a C routine from Microfocus COBOL and return
a value/record to the calling COBOL routine?

Please, please help...your my only hope :-)

Branden
MIS, UofArizona
```

#### ↳ Re: Call C from COBOL? how?

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-05-31T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c55dbd1d71-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1995May31.154303.1@uabpa>`
- **References:** `<1995May31.154303.1@uabpa>`

```
On 31 May 95 15:43:03 MST, TAPEWORM (bhoopes@uabpa) wrote:
› S.O.S
› How does one go about calling a C routine from Microfocus COBOL and return
› a value/record to the calling COBOL routine?
 
› Please, please help...your my only hope :-)

Try this:

CALL 'cprog' USING BY REFERENCE ADDRESS OF cobol-record

Your C program would receive a pointer to address of cobol-record, and
could change it as needed.
```

##### ↳ ↳ Re: Call C from COBOL? how?

- **From:** "barry jelbert" <ua-author-11050868@usenetarchives.gap>
- **Date:** 1995-06-01T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c55dbd1d71-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c55dbd1d71-p2@usenetarchives.gap>`
- **References:** `<1995May31.154303.1@uabpa> <gap-c55dbd1d71-p2@usenetarchives.gap>`

```
jts··.@pri··t.com (Joseph I. Tsatskin) wrote:
› Try this:
› 
…[3 more quoted lines elided]…
› could change it as needed.

If you're doing lots of C calls, call prototyping will make it easier.
If anyone's interested, mail me and I'll send you an ascii how-to file.

Barry Jelbert
b.··.@mfl··o.uk
Micro Focus, West Street, Newbury, UK
```

##### ↳ ↳ Re: Call C from COBOL? how?

- **From:** "martyn woerner" <ua-author-15047705@usenetarchives.gap>
- **Date:** 1995-06-01T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c55dbd1d71-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c55dbd1d71-p2@usenetarchives.gap>`
- **References:** `<1995May31.154303.1@uabpa> <gap-c55dbd1d71-p2@usenetarchives.gap>`

```
› On 31 May 95 15:43:03 MST, TAPEWORM (bhoopes@uabpa) wrote:
›› S.O.S
›› How does one go about calling a C routine from Microfocus COBOL and return
›› a value/record to the calling COBOL routine?
› 

Try using CALL "cprog" USING ... RETURNING dataname
where dataname is no bigger than 4 bytes and if binary must be
described as USAGE COMP-5 or can be USAGE POINTER or USAGE
PROCEDURE-POINTER.


Martyn      (m.··.@mfl··o.uk)
Phone: +44 (0)6135 565 358, fax +44 (0)6135 565 567
```

#### ↳ Re: Call C from COBOL? how?

- **From:** "ha..." <ua-author-816025@usenetarchives.gap>
- **Date:** 1995-06-01T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c55dbd1d71-p5@usenetarchives.gap>`
- **In-Reply-To:** `<1995May31.154303.1@uabpa>`
- **References:** `<1995May31.154303.1@uabpa>`

```
TAPEWORM (bhoopes@uabpa) wrote:
: How does one go about calling a C routine from Microfocus COBOL and return
: a value/record to the calling COBOL routine?

There seem to be several examples in the COBOL Users Guide on page 6-8,
don't any of them return a value?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
