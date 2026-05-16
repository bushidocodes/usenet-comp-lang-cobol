[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VSAM record-length

_2 messages · 2 participants · 2000-12_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Re: VSAM record-length

- **From:** JOSEPH SHANE <jbwshane@nac.net>
- **Date:** 2000-12-09T19:34:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A32CF89.E1D825E8@nac.net>`
- **References:** `<901ecb$q6p$1@rohrpostix.uta4you.at> <906ubt$5ekv$1@ID-39920.news.dfncis.de> <Ag+EuAA8IWK6EwjP@ld50macca.demon.co.uk> <90egl3$jac$1@nntp9.atl.mindspring.net> <jvyyrzubevmbagrfvasbezngvpnpbz.g51i0q0.pminews@news.wanadoo.es>`

```
My understanding of the VSAM RDW was that it would appear preceding the
logical record when the VSAM KSDS was reeled off in logical order onto a
tape, thus adding the four bytes of the RDW to the physical length of
the backup.  In its sequential form, wouldn't the LRECL be thus exposed
(through the RDW which is now the first four bytes of the physical
record)?

Willem Clements wrote:
> 
> On Sun, 3 Dec 2000 16:14:14 -0600, William M. Klein wrote:
…[50 more quoted lines elided]…
> http://www.brainbench.com
```

#### ↳ Re: VSAM record-length

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-12-10T18:22:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g5do010.pminews@news.wanadoo.es>`
- **References:** `<901ecb$q6p$1@rohrpostix.uta4you.at> <906ubt$5ekv$1@ID-39920.news.dfncis.de> <Ag+EuAA8IWK6EwjP@ld50macca.demon.co.uk> <90egl3$jac$1@nntp9.atl.mindspring.net> <jvyyrzubevmbagrfvasbezngvpnpbz.g51i0q0.pminews@news.wanadoo.es> <3A32CF89.E1D825E8@nac.net>`

```
On Sat, 09 Dec 2000 19:34:17 -0500, JOSEPH SHANE wrote:

>My understanding of the VSAM RDW was that it would appear preceding the
>logical record when the VSAM KSDS was reeled off in logical order onto a
…[4 more quoted lines elided]…
>

A variable length file on tape always contains length fields preceeding the
records, independent of the origin of the data. These four bytes are not the
same as a VSAM RDF. VSAM RDF's are just three bytes long and appear in pairs,
one containing lengths and the other one a record count. The only way to
access those RDF's is to process the VSAM file by CI.

Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
