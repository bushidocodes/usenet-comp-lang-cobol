[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help requested - total learner

_2 messages · 2 participants · 1999-08_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Help requested - total learner

- **From:** Roger Sansom <roger@wantree.com.au>
- **Date:** 1999-08-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37BBF5BA.7F3B189C@wantree.com.au>`

```
Could someone please assist. I download a file daily which I need to use
to update numerous files.

The file I download, eg 19990816.csv, contains records as follows (of no
fixed length):

Code, date, open, close, high, low, volume
AAA, 19990816, 2.4, 2.37, 2.5, 2.35, 2000000
AAB, etc
AAC, Etc

Each code (AAA, AAB, AAC etc) has its own historical file.

The historical files are AAA.prn, AAB.prn, AAC.prn etc.

What I need to do is open the daily file, eg 1999016.csv, read each
record, open the .prn file that corresponds to the code of each record
(AAA, AAB, AAC etc) and append certain fields in that record.

I cant get the .prn files to open as I am confused as to how to declare
them etc.

Any help would be appreciated.

Thanks

Roger
```

#### ↳ Re: Help requested - total learner

- **From:** robj <robj@pdq.net>
- **Date:** 1999-08-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FB999594F1937CBC.17D6589116539841.6F2BC3DB1DF7068E@lp.airnews.net>`
- **References:** `<37BBF5BA.7F3B189C@wantree.com.au>`

```
in MF cobol

         you should get the idea of this code.
   don't forget to close!
   make sure no spaces are embedded in my-new-file.
   check your status codes.
   the DYNAMIC is the keyword.

 rob


           SELECT my-file      ASSIGN TO DYNAMIC MYFILE


       01 my-new-file.
  05 filler   pic x(03) value 'c:\'.
  05 part1    pic x(03).
   05 filler   pic x(04) value '.prn'.


            example:

     move your-record-code to part1.
     move my-new-file to myfile.
     open extend my-file.
  write reocrd.
     close my-

Roger Sansom wrote:

> Could someone please assist. I download a file daily which I need to use
> to update numerous files.
…[24 more quoted lines elided]…
> Roger
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
