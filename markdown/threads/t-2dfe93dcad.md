[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help COBOL DMSII -

_2 messages · 2 participants · 1997-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help COBOL DMSII -

- **From:** "hami..." <ua-author-17072340@usenetarchives.gap>
- **Date:** 1997-07-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33d7cfc1.0@139.134.5.33>`

```

A dataset in DMSII database is defined as:
DDA DATA SET
(
dda-brch-nbr number (04) Null 0;
dda-key group
(
dda-inst-nbr "*req" number (04) req;
dda-proc-ctl number (04);
dda-acct-nbr number (12) null 0;
);
....
...
....
dda-stax-group group
(
dda-stax-option number (01) null;
dda-stax-ex-cert alpha (06);
. .....
. .....
);



A cobol program reads the dataset and tries to dump into a flat file.

I am trying to do straight move and avoid null value with the
following if statement.

IF DDA-STAX-EX-CER NULL
MOVE SPACES TO XDDA-STAX-EX-CERT
ELSE
MOVE DDA-STAX-EX-CER TO XDDA-STAX-CERT.

If there is no value in DDA-STAX-EX-CERT, I am still getting
"??????".

Any suggestion how to overcome this problem.

Thanks


Hamid Adan
Sydeny
If there is no value in dda-stax-ex-cert the extract file
```

#### ↳ Re: Help COBOL DMSII -

- **From:** "wds" <ua-author-1064034@usenetarchives.gap>
- **Date:** 1997-07-23T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2dfe93dcad-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33d7cfc1.0@139.134.5.33>`
- **References:** `<33d7cfc1.0@139.134.5.33>`

```

Hamid Ibrahim wrote:
› 
› A dataset in DMSII database is defined as:
…[23 more quoted lines elided]…
› 
You did not mention the platform upon which your DMSII database and your
COBOL program are running, so this reply may or may not help.

I believe that DMSII will flood empty records with HIGH-VALUES, so this
might be a useful quantity against which to compare.

Also, DMSII provides utility functions to write the database to a flat
file. If they fit your needs, this may help save you from reinventing
the wheel. Refer to Vol. 3 of the DMSII documentation.

Good luck.
Reply Addr:-->WDavid dot Simon at atl dot frb dot org<--
-------------------De··y@Spa··r.Trasher----------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
