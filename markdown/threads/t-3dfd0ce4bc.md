[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Alternate index question

_5 messages · 5 participants · 1998-02_

---

### Alternate index question

- **From:** "jas..." <ua-author-1023767@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34d7c07b.1316933@news.earthlink.net>`

```

I am running into problem using a VSAM file with an alternate index
with duplicate alternate index keys allowed. After successfully
writing out 119 records to the file (all with the identical alternate
index key) I am getting a logic error on the next write. If I
redefine the file and increase the CI size specification I can write
more records but eventually run into the same problem Does anyone
know how the CI size parameter and the number of "allowable" duplicate
keys on the alternate index are related? Any help is much
appreciated.
```

#### ↳ Re: Alternate index question

- **From:** "sco..." <ua-author-4518283@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3dfd0ce4bc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34d7c07b.1316933@news.earthlink.net>`
- **References:** `<34d7c07b.1316933@news.earthlink.net>`

```

jas··.@ear··k.net (John Asnin) wrote:

› I am running into problem using a VSAM file with an alternate index
› with duplicate alternate index keys allowed.  After successfully
…[6 more quoted lines elided]…
› appreciated.

If I remember correctly, the alternate key records are variable length
with the format something like key value/rba of first record/rba of
second record/etc. Since there is only one record for each key value,
the maximum number of records would be limited by ci size less the
length of the key field. I think the RBA fields are full word (32-bit)
fields but I can't swear to it. So yes, number of records is
definitely a function of the maximum record length possible in the CI.


Scott Peterson
```

##### ↳ ↳ Re: Alternate index question

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1998-02-04T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3dfd0ce4bc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3dfd0ce4bc-p2@usenetarchives.gap>`
- **References:** `<34d7c07b.1316933@news.earthlink.net> <gap-3dfd0ce4bc-p2@usenetarchives.gap>`

```

Scott Peterson wrote:
› jas··.@ear··k.net (John Asnin) wrote:
› 
…[17 more quoted lines elided]…
› 

I believe each record in the alternate index contains the alternate key,
the primary key (not the RBA) of all records containing that alternate
key, plus a few control bytes (5?). If you can't make the AIX DATA CISZ
large enough to handle the worst case with nonunique alternate keys, I
believe there is also an option to define the AIX to allow a record to
span multiple CI's, although this also has some performance and space
efficiency side effects.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

##### ↳ ↳ Re: Alternate index question

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3dfd0ce4bc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-3dfd0ce4bc-p2@usenetarchives.gap>`
- **References:** `<34d7c07b.1316933@news.earthlink.net> <gap-3dfd0ce4bc-p2@usenetarchives.gap>`

```

Scott Peterson wrote:
› 
› jas··.@ear··k.net (John Asnin) wrote:
…[4 more quoted lines elided]…
›  Any help is much> >appreciated.
I ran into this problem when working for one of the large car-rental
agencies. The alternate index was on 'the owner of the car who hit our
firm's car (TOOTCWHOC)'. Turned out that TOOTCWHOC was often the other
car-rental firms, abecause the renters were playing bumper-tag in the
airport parking lots. So after a few months in production, my index
filled up with duplicate owner-names.

The low-tech solution I went to was to use a numeric suffix in the key,
generated as 'the next sequential number' for TOOTCWHOC. For example,
AVIS000000001, AVIS000000002, were used as a key. I just would read the
last record for AVIS and added one to what I found to create the next
alternate key.

Then I used logic in the program to strip out the numeric when
displaying the name on a screen or writing a letter to Avisnnnnnnnnn.
(And, of course, had to do a work-around so the letter didn't get
addressed to Mr. Avis or Mr. Budget or Mr. Hertz, etc.)

John
```

#### ↳ Re: Alternate index question

- **From:** "a..." <ua-author-17084061@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3dfd0ce4bc-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34d7c07b.1316933@news.earthlink.net>`
- **References:** `<34d7c07b.1316933@news.earthlink.net>`

```

In article <34d··.@new··k.net>, jas··.@ear··k.net
(John Asnin) wrote:

› I am running into problem using a VSAM file with an alternate index
› with duplicate alternate index keys allowed.  After successfully
…[6 more quoted lines elided]…
› appreciated.

Each data record of an alternate index is a variable length record
containing the alternate key value and a list of the primary keys of all
base cluster records having that alternate key value. So, for example, if
the alternate key is 20 bytes long, and your base cluster's key is 10 bytes
long, and you have 200 records with the same alternate key, your alternate
index record length would be 20 + (200 * 10) + 5 = 2025. The data
component of your alternate index would have to be defined to support a
record of that size.

Here is what the IDCAMS manual says about RECORDSIZE for DEFINE
ALTERNATEINDEX:

RECORDSIZE(average maximum|4086 32600)
specifies the average and maximum length, in bytes, of an alternate
index record.

An alternate index record can span control intervals, so RECORDSIZE
can be larger than CONTROLINTERVALSIZE. average and maximum are any
integer values that do not exceed the capacity of a control area. You
can identify the records as fixed length by specifying the same value
for average and maximum.

You can use the following formulas to determine the size of the
alternate index record when the alternate index supports:

 A key sequenced base cluster

RECSZ = 5 + AIXKL + (n x BCKL)

 An entry sequenced base cluster

RECSZ = 5 + AIXKL + (n x 4)

where:

- RECSZ is the average record size.

- AIXKL is the alternate-key length (see the KEYS parameter).

- BCKL is the base cluster's prime-key length (you can issue the
access method services LISTCAT command to determine the base
cluster's prime-key length).

- n = 1 when UNIQUEKEY is specified (RECSZ is also the maximum
record size).

- n = the number of data records in the base cluster that contain
the same alternate-key value, when NONUNIQUEKEY is specified.

When you also specify NONUNIQUEKEY, the record size you specify should
be large enough to allow for as many key pointers or RBA pointers as
you anticipate. The record length values apply only to the alternate
index's data component.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
