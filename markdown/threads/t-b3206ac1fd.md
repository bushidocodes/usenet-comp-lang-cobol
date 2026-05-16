[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM (mainframe) COBOL - upgrades and related topics

_1 message · 1 participant · 1998-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM (mainframe) COBOL - upgrades and related topics

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vr861$a8o@dfw-ixnews5.ix.netcom.com>`

```
I thought I would start a new thread based on a couple of other threads that
are going on in the newsgroup.

1) IBM *fully* support Report Writer with every release of COBOL for MVS,
OS/390, CMS, and VSE.  As mentioned elsewhere, it does require a separate
product - but that product has been maintained and enhanced as each release
of the compiler came out.  If you don't know about this product, contact
IBM, look in IBMLink, or review this newsgroup (via DejaNews).  This is
particularly important to understand as report writer will become a required
part of the next Standard.

2) The migration from OS/VS COBOL (or DOS/VS COBOL) to the new IBM COBOL
compilers is FAR FROM TRIVIAL.  I wrote a book on it ("OldBOL to NewBOL - a
COBOL migration tutorial") as have several others inside and outside of IBM.
I would be the last person to call such a migration easy - but I would also
be the first to say that a decade and a half after it became obvious - it
should be well progressed before having to deal with Y2K.

3) IBM's CCCA product (along with several other 3rd party products) can
handle well over 90% of all source code migration issues.  Furthermore, the
interaction with other (IBM and 3rd party) products that were real migration
inhibitors in the '80s really should NOT be a problem now. If your shop is
really so down-level on all of its software to run into problems with
interactions between new COBOL and old products, I would say you have more
serious problems that just migrating COBOL.

4) If it "ain't broke - don't fix it" works fine in a static environment.
But if your existing "not broke" application must interface with other
systems, applications, software, or hardware that will be growing and
changing, you better plan on HOW to "maintain" your not-broke application -
or you are really in for some unpleasant problems in the future.  There are
plenty of books and software that can help you cost justify a change now -
to avoid major problems (anyone hear of Y2K?) in the future.

5) No matter where you are in an IBM mainframe (or any?) migration/upgrade,
please do remember the two most important (and easy to ignore) steps:

   TRAIN your people to use the new facility
   TEST your application for upward compatibility of performance (both same
results and same execution-performance)

Finally, if you are doing any type of IBM COBOL migration, "pretty please"
DO read the IBM Migration Guides.  They really do answer most of the
questions (on file status changes, syntax changes, reserved words, planning
and co-existence, etc)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
