[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ADVISE: Read random files

_2 messages · 2 participants · 1995-09_

---

### ADVISE: Read random files

- **From:** "dga..." <ua-author-17088171@usenetarchives.gap>
- **Date:** 1995-09-07T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42po1e$i6@news1.halcyon.com>`

```
This is my project: Suppose to create a report that will read the file
in random and pickup a certain date in random again for a certain
doctor. Say the file has 500 records with different doctors in the
doctors field, s well as different dates. The original file it was
suppose to read it from is indexed.

I would like to know if access mode = random will do it. If it does, how
do you properly code the file to be read and create this report. Suppose
to come up with ten data. Same doctor but different dates. I tried this
but i get errors after i compiled the source file.

The system i am using is Wang VMS, if this helps. Let me know if you
need more info. I need all the advise i could get, since i have been
pulling my hair since friday figuring things out.

I was able to create the ancient way, but i prefer the random format
since you can always process this over and over without getting the same
results.

Any info is much appreciated. Thanks in advance.


diana
dga··.@kue··m.net
```

#### ↳ Re: ADVISE: Read random files

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-09-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8efc7bc20b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<42po1e$i6@news1.halcyon.com>`
- **References:** `<42po1e$i6@news1.halcyon.com>`

```
Diana Garcia (dga··.@sab··m.net) wrote:
: This is my project: Suppose to create a report that will read the file
: in random and pickup a certain date in random again for a certain
: doctor. Say the file has 500 records with different doctors in the
: doctors field, s well as different dates. The original file it was
: suppose to read it from is indexed.

: I would like to know if access mode = random will do it. If it does, how
: do you properly code the file to be read and create this report. Suppose
: to come up with ten data. Same doctor but different dates. I tried this
: but i get errors after i compiled the source file.

Access Mode Random means that you are supplying the keys and are only doing
vectored reads as opposed to sequential reads, not that you are asking the
file system to supply you with records in a random fashion.

You may want to set Access Mode Dynamic and if the Doctor and Date fields
share a key, load the key and Start on it. Then read sequentially using
the appropriate records. If there is no key structure that will limit
your reads, you may have to Start the file at the beginning and read in
each record and use only the appropriate records.

: The system i am using is Wang VMS, if this helps. Let me know if you
: need more info. I need all the advise i could get, since i have been
: pulling my hair since friday figuring things out.

: I was able to create the ancient way, but i prefer the random format
: since you can always process this over and over without getting the same
: results.

: Any info is much appreciated. Thanks in advance.


: diana
: dga··.@kue··m.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
