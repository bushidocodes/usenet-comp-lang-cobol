[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using MF for off loading COBOL deve.

_4 messages · 4 participants · 1995-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Using MF for off loading COBOL deve.

- **From:** "buer..." <ua-author-17087657@usenetarchives.gap>
- **Date:** 1995-02-07T15:15:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3h8kdq$v7r@watt.oedison.com>`

```
I'm investigating using Micro Focus to off load COBOL development from an
MVS environment to a PC platform. Can anyone tell what I really need to
purchase from MF to develop applications for batch, CICS, and DB2?
```

#### ↳ Re: Using MF for off loading COBOL deve.

- **From:** "jbe..." <ua-author-14978945@usenetarchives.gap>
- **Date:** 1995-02-10T17:16:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7d97bca5ec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3h8kdq$v7r@watt.oedison.com>`
- **References:** `<3h8kdq$v7r@watt.oedison.com>`

```
bue··.@wat··n.com (Peter Buerling) wrote:
› I'm investigating using Micro Focus to off load COBOL development from an
› MVS environment to a PC platform. Can anyone tell what I really need to
› purchase from MF to develop applications for batch, CICS, and DB2?

Just Workbench for Cobol alone. Micro Focus Transaction System (MTS) for
CICS development. Then buy OS/2 DB2/2 or XDB (not MF products) to simulate
DB2 calls, or buy a gateway to the mainframe to go directly against the mainframe
from the workstation.

Or call Micro Focus, 800-872-6265, they would love to help you.

Jeffrey Benner * Senior Programmer Analyst * Loyola University Medical Center
INET: jbe··.@l··.edu * Voice (708) 216-6885 * Fax (708) 216-8713
```

##### ↳ ↳ Re: Using MF for off loading COBOL deve.

- **From:** "cpu..." <ua-author-17087602@usenetarchives.gap>
- **Date:** 1995-02-13T17:51:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7d97bca5ec-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7d97bca5ec-p2@usenetarchives.gap>`
- **References:** `<3h8kdq$v7r@watt.oedison.com> <gap-7d97bca5ec-p2@usenetarchives.gap>`

```
In <3hgor8$9.··.@apo··c.edu>, jbe··.@l··.edu (Jeffrey Benner) writes:
› bue··.@wat··n.com (Peter Buerling) wrote:
›› I'm investigating using Micro Focus to off load COBOL development from an
…[7 more quoted lines elided]…
› 

I've found that XDB provides better DB/2 compatibility than DB2/2. The only
variation which I've found between XDB and DB/2 so far are some slight differences
in datatypes in the XDB system tables.
```

##### ↳ ↳ Re: Using MF for off loading COBOL deve.

- **From:** "gl..." <ua-author-3965476@usenetarchives.gap>
- **Date:** 1995-02-24T12:40:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7d97bca5ec-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-7d97bca5ec-p2@usenetarchives.gap>`
- **References:** `<3h8kdq$v7r@watt.oedison.com> <gap-7d97bca5ec-p2@usenetarchives.gap>`

```
Jeffrey Benner (jbe··.@l··.edu) wrote:
: bue··.@wat··n.com (Peter Buerling) wrote:
: >I'm investigating using Micro Focus to off load COBOL development from an
: >MVS environment to a PC platform. Can anyone tell what I really need to
: >purchase from MF to develop applications for batch, CICS, and DB2?

: Just Workbench for Cobol alone. Micro Focus Transaction System (MTS) for
: CICS development. Then buy OS/2 DB2/2 or XDB (not MF products) to simulate
: DB2 calls, or buy a gateway to the mainframe to go directly against the mainframe
: from the workstation.

: Or call Micro Focus, 800-872-6265, they would love to help you.

: Jeffrey Benner * Senior Programmer Analyst * Loyola University Medical Center
: INET: jbe··.@l··.edu * Voice (708) 216-6885 * Fax (708) 216-8713

We are using the workbench with the IBM CICS/OS/2 (supplied by
MicroFocus). I have used the MF CICS emulator, and the Realia CICS
emulator, and I personally prefer the IBM product. The main difference is
that the IBM/OS/2 is not an emulator, but an actual functioning multi-user
CICS, which can run as a server. It gives me alot more options, since I
can *really* test the programs.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
