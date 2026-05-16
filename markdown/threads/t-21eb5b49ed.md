[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need help on cobol

_5 messages · 3 participants · 2006-08_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: Need help on cobol

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-08-05T14:02:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154811724.365569.217930@m73g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<1154797366.419417.233450@m73g2000cwd.googlegroups.com>`
- **References:** `<1154797366.419417.233450@m73g2000cwd.googlegroups.com>`

```

florence wrote:
> I had two Physical Sequnetial files both are sorted by CUST ID no.
>
…[6 more quoted lines elided]…
> output file.

You haven't specified whther it is the file1 matching records or the
file2 matching records that are written to output, or both.

Given custids of:

File1:  B D E E F ...

File2: A(1) A(2) B(1) C(1) D(1) D(2) E(1) E(2) E(3) F(1) ...

(n) indicating there are 2 A records, 3 E records.

Which records will be output ?  Those from file1 ? those from file2 ?
both ? If there are two records with the same custid in file1 (is this
possible) do you need to output all the matching file2 records for
each, duplicating the output ?

>  Here I am thinking two possible solutions:
>
>        1. Fetch each record from FIle1 and compare with file2
> sequentilly until the cust ID in file1 greater then file2 cust id.
> Match is found write ouput record.

You imply that it would be necessary to start again at the beginning of
file2 for each record in file1.  You said that the files are sorted by
Cust-Id.  For each record in File1 it is only necessary to read forward
in file2 because all the records already read in file2 must be lower
CustId than the current File1 CustId. That is the nature of them being
sorted.

>        2. Put all the 22 million rows in a table and use SEARCH ALL for
> each every record on file1.

SEARCH ALL does not give you 'all' the records that match, it only
gives one but it may use a binary chop search (or any other method) and
the one that it finds need not be the first of that key. That is it
might 'search all' the table when searching.

> I want to know which method is preferrable.

Neither probably.

>  questions:
>
>        1.  If I store 22 million records in table declaration, how much
> storage is needed. Is this ok to use this method.

Simple 22,000,000 x table item size.  Are you allowed to use a Gigabyte
of RAM or so ?  Note that a SERCH ALL (which is unlikely to be what you
want anyway) will potentially access all parts of the table for each
SEARCH and so will hammer the virtual memory mercilessly and will
thrash.  The operators will kill your program.

>         2. Sequntial processing it is taking very very llong time.

Are you reading the whole of file2 for each file1 record ? why ?
```

#### ↳ Re: Need help on cobol

- **From:** "florence" <hari_junk1@yahoo.com>
- **Date:** 2006-08-05T14:22:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154812937.617123.278860@i42g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1154811724.365569.217930@m73g2000cwd.googlegroups.com>`
- **References:** `<1154797366.419417.233450@m73g2000cwd.googlegroups.com> <1154811724.365569.217930@m73g2000cwd.googlegroups.com>`

```
Thank you very much for your analysis.Thats excellent.

       I will need to match file1(No duplicate CUST IDS in this file)
with file2 custids(Duplicate CUST IDS in this file).

      Once CUST ID matches, then based on  status category in file2
field I need to pass
one filed data to one of seven output fields in the output record.  All
other output fields in the output record would be populated by file2
fields only, and output record would be "PIPE" delimeted.

FIle1 LRECL  20( It has 10000)
File2 LRECL 120(It has 22 millian records)

I hope this helps.

What is PIPE delimeted(it is JUST putting "|" after each filed in the
output record?)

Once again appreciated your help.

Thanks




Richard wrote:
> florence wrote:
> > I had two Physical Sequnetial files both are sorted by CUST ID no.
…[63 more quoted lines elided]…
> Are you reading the whole of file2 for each file1 record ? why ?
```

##### ↳ ↳ Re: Need help on cobol

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-08-05T14:58:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1154815087.822242.263090@m79g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<1154812937.617123.278860@i42g2000cwa.googlegroups.com>`
- **References:** `<1154797366.419417.233450@m73g2000cwd.googlegroups.com> <1154811724.365569.217930@m73g2000cwd.googlegroups.com> <1154812937.617123.278860@i42g2000cwa.googlegroups.com>`

```

florence wrote:
> Thank you very much for your analysis.Thats excellent.
>
…[10 more quoted lines elided]…
> File2 LRECL 120(It has 22 millian records)

Then you probably need:

    PERFORM UNTIL File1-CustId = HIGH-VALUE
        READ file1
              AT END MOVE HIGH-VALUES TO File1-CustId
        END-READ
        PERFORM Read-File2
               UNTIL File2-CustId >= File1-CustId
        PERFORM
               UNTIL File1-CustId = HIGH-VLUES
                    OR File2-CustId > File1-CustId

               * deal with matching file2 record here

               PERFORM Read-File2
        END-PERFOM
    END-PERFORM
    .

Read-File2.

    READ file2
          AT END MOVE HIGH-VALUES TO File2-CustId
    END-READ
    .

> What is PIPE delimeted(it is JUST putting "|" after each filed in the
> output record?)

Yes, it would likely be variable output length but might be done by:

          STRING field1  "|" field2 "|" field3 ...
                 DELIMITED BY ...
                 INTO output-record
```

###### ↳ ↳ ↳ Re: Need help on cobol

- **From:** "L ü ko Willms" <l.willms@domain.invalid>
- **Date:** 2006-08-08T07:31:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<czd2LKcn8EGd-pn2-YXGsLHFxfXUd@lueko.willms.dialin.t-online.de>`
- **References:** `<1154797366.419417.233450@m73g2000cwd.googlegroups.com> <1154811724.365569.217930@m73g2000cwd.googlegroups.com> <1154812937.617123.278860@i42g2000cwa.googlegroups.com> <1154815087.822242.263090@m79g2000cwm.googlegroups.com>`

```
Am Sat, 5 Aug 2006 21:58:07 UTC,  schrieb "Richard" 
<riplin@Azonic.co.nz>  auf comp.lang.cobol :

> Then you probably need:
>  
…[22 more quoted lines elided]…
>     .

   Easier and clearer: 

   READ file1
   READ file2
   *>  file1 is the control file. 
   *>  it is assumed that Customer-ID is unique within file1, 
   *>  while many duplicates can exist in file2
   *>  probably file1 is the customer master file, 
   *>    while file2 is some transaction file
   *>
   PERFORM UNTIL EOF IN FILE-STATUS-file1 
              OR EOF IN FILE-STATUS-file2
      EVALUATE TRUE
         WHEN Customer-ID IN file1 < Customer-ID IN file2 THEN
           READ file1
         WHEN Customer-ID IN file1 > Customer-ID IN file2 THEN
           READ file2
         OTHERWISE           *> i.e. Customer-ID IN file1 = the one in
file2
           PERFORM UNTIL EOF IN FILE-STATUS-file2
                      OR Customer-ID in file1 < Customer-ID IN file2
              PERFORM collect-information-and-write-out
              READ file2
           END-PERFORM
       END-EVALUATE
   END-PERFORM




Yours, 
L.W.
```

###### ↳ ↳ ↳ Re: Need help on cobol

_(reply depth: 4)_

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-08-07T23:30:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1155018658.238273.279880@75g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<czd2LKcn8EGd-pn2-YXGsLHFxfXUd@lueko.willms.dialin.t-online.de>`
- **References:** `<1154797366.419417.233450@m73g2000cwd.googlegroups.com> <1154811724.365569.217930@m73g2000cwd.googlegroups.com> <1154812937.617123.278860@i42g2000cwa.googlegroups.com> <1154815087.822242.263090@m79g2000cwm.googlegroups.com> <czd2LKcn8EGd-pn2-YXGsLHFxfXUd@lueko.willms.dialin.t-online.de>`

```

Lüko Willms wrote:

>    Easier and clearer:

What is 'easier and clearer' is entirely what one is used to.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
