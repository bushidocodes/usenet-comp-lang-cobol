[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# LOW-VALUES as SPACES, HIGH-VALUES as ALL "9"

_1 message · 1 participant · 2003-07_

---

### LOW-VALUES as SPACES, HIGH-VALUES as ALL "9"

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-07-07T16:29:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<becvpe$2n9a$1@si05.rsvl.unisys.com>`

```
As best I can determine from the documentation for three very different
implementations of ANSI X3.23-1968 COBOL, the definitions for LOW-VALUES and
HIGH-VALUES in that standard did NOT specify the character set in which
these figurative constants occupied the lowest and highest positions.  The
only character set that appears to have been defined in that standard is
indeed the COBOL character set -- which, when represented in the character
set native to one particular system of my acquaintance, had the space as its
lowest value and the digit 9 as its highest value.   Thus, the choice of
SPACES for LOW-VALUES and ALL "9" for HIGH-VALUES does not seem to have been
in conflict with *that standard* (or any earlier ones).

It appears to me that ANSI X3.23-1974, with its introduction of the PROGRAM
COLLATING SEQUENCE clause and its explicit definition of these figurative
constants in terms of the applicable collating sequence used in comparisons
within the program specifically precludes the selection from the narrower
*COBOL* character set.  Thus, it would take a mighty peculiar collating
sequence for HIGH-VALUES to be equated to "9" and LOW-VALUES to the space
character in any implementation compliant with ANSI X3.23-1974 or later
standards.

Implementations conformant with standards issuedmore than three decades ago
could indeed treat LOW-VALUES as equivalent to SPACES and remain conformant.
Implementations conformant with any standard issued in the last twenty-nine
years, however, could almost certainly not do so except under *very*
limited, and *very* unlikely circumstances.

    -Chuck Stevens
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
