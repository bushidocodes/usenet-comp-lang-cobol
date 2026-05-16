[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM DFSORT vs SyncSort

_4 messages · 4 participants · 2000-06_

---

### IBM DFSORT vs SyncSort

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ip36j02ekm@enews4.newsguy.com>`

```
Our shop implemented DFSORT, taking out trusty SyncSort on Sunday evening.
By Monday morning, I was having problems with some test jobs.  Apparently
DFSORT doesn't allow concatenated datasets for sort space (SORTWK).  My boss
was prepared to stop the schedule when I told him, but it pressed on (poor
judgement).  As soon as our heavy batch window hit at 6:00PM, several jobs
abended.  SyncSort was rolled back in and the mainframe IPLed (30 minutes
lost in production LPAR batch window).

They haven't put DFSORT back in yet; waiting for some answers from IBM.

Sad part is, the only reason we switched was to 'standardize' with our
larger, mother company.  I suppose it will pay off in the long run.

Anyone else seen these abnormalities?

Jeff
```

#### ↳ Re: IBM DFSORT vs SyncSort

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-06-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<L_V35.3063$uf2.4594@news4.mia>`
- **References:** `<8ip36j02ekm@enews4.newsguy.com>`

```
IBM's response will be something like
    " read the manual.  The examples for SORTWKdd, do not mention
concatenation
of work data sets.  Since with BLOCKSET you can have 255 SORTWKdd, and w/o
up to 32, there should be no need to use this technique."

Jeff Baynard <union27@macconnect.com> wrote in message
news:8ip36j02ekm@enews4.newsguy.com...
> Our shop implemented DFSORT, taking out trusty SyncSort on Sunday evening.
> By Monday morning, I was having problems with some test jobs.  Apparently
> DFSORT doesn't allow concatenated datasets for sort space (SORTWK).  My
boss
> was prepared to stop the schedule when I told him, but it pressed on (poor
> judgement).  As soon as our heavy batch window hit at 6:00PM, several jobs
…[10 more quoted lines elided]…
> Jeff
```

#### ↳ Re: IBM DFSORT vs SyncSort

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lbd1ls8ck9dq8d79l0j1spgo2372blu0gv@4ax.com>`
- **References:** `<8ip36j02ekm@enews4.newsguy.com>`

```
On Tue, 20 Jun 2000 20:45:04 -0400 "Jeff Baynard" <union27@macconnect.com>
wrote:

:>Our shop implemented DFSORT, taking out trusty SyncSort on Sunday evening.
:>By Monday morning, I was having problems with some test jobs.  Apparently
:>DFSORT doesn't allow concatenated datasets for sort space (SORTWK).  My boss
:>was prepared to stop the schedule when I told him, but it pressed on (poor
:>judgement).  As soon as our heavy batch window hit at 6:00PM, several jobs
:>abended.  SyncSort was rolled back in and the mainframe IPLed (30 minutes
:>lost in production LPAR batch window).

:>They haven't put DFSORT back in yet; waiting for some answers from IBM.

:>Sad part is, the only reason we switched was to 'standardize' with our
:>larger, mother company.  I suppose it will pay off in the long run.

:>Anyone else seen these abnormalities?

Question out of curiosity:

Why do you concatenate SORTWK rather than specifying additional SORTWK
ddnames?
```

#### ↳ Re: IBM DFSORT vs SyncSort

- **From:** Frank Yaeger <fyaeger5@vnet.ibm.com>
- **Date:** 2000-06-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3950DFAE.7907D736@vnet.ibm.com>`
- **References:** `<8ip36j02ekm@enews4.newsguy.com>`

```
Jeff Baynard wrote:

> ... Apparently
> DFSORT doesn't allow concatenated datasets for sort space (SORTWK).

Yes, that's true.  You should have received the following message:

ICE148A 0 SORTWKdd CONCATENATION NOT ALLOWED

I'm sorry you ran into this problem with your migration, but the two products,
though similar, are NOT identical.  The DFSORT hotline (sort@vnet.ibm.com) can
help you with differences you find.

In this case, you need to change your concatenated SORTWKs to separate DD
statements.  Alternatively, you can use dynamic allocation of work space instead
of JCL SORTWKs.  One way to do that without changing your JCL is to use ICEMAC
option DYNAUTO=IGNWKDD.  This tells DFSORT to deallocate your JCL SORTWKs and
use dynamic allocation instead.  For some more information on dynamic
allocation, see:

http://www.storage.ibm.com/software/sort/srtmadyn.htm

For general information on DFSORT, see the DFSORT home page at:

http://www.ibm.com/storage/dfsort/

You can access all of the DFSORT publications online from:

http://www.storage.ibm.com/software/sort/srtmpub.htm

Frank Yaeger - DFSORT Team (Specialties: Symbols, Y2K, OUTFIL, ICETOOL)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
