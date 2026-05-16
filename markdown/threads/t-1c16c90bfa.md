[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Scrolling records

_4 messages · 4 participants · 1999-09_

---

### Scrolling records

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37E85E50.C7403A8E@home.com>`

```
Movie scenario : Our erstwhile hero/heroine breaks into a highly secure
classified installation, and typing at 1,200 words p.m., breaks the
security code - and Voila! - streams of records scroll for him/her -
you get the idea.

Now the real world - In a PC environment I can set up scroll tables,
(list boxes, dropdown lists), subject to memory constraints. For info
just how do you do it on the big-iron or multi-user systems with many
users accessing the same tables. How would corporations the size of say,
Amex or Visa do it. Logically you have to set some size limitation, and
restart a fresh scroll with Start Myfile Key > xxxx  or < xxxx(?) -
depending upon whether you want to scroll forward/backwards.

A brief description or pseudo code would be informative.

Jimmy, Calgary AB
```

#### ↳ Re: Scrolling records

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zz6G3.133$9r3.10246@dfiatx1-snr1.gtei.net>`
- **References:** `<37E85E50.C7403A8E@home.com>`

```

James J. Gavan wrote in message <37E85E50.C7403A8E@home.com>...
>... Voila! - streams of records scroll for him/her -....
>
…[3 more quoted lines elided]…
>users accessing the same tables....

Why not just capture it all to disk and query it later using START etc as
you have suggested, if your data capture file is indexed..

But if you capture the data to a non-indexed file, instead of keeping the
data
in a memory-based table, why not just keep the key and a relative record
number? Then you can just table up something like...

01 FILLER
    05 Scroll-Key OCCURS A LOT indexed by sk-index
         10  KeyValue                 PIC X(12)
         10  RRN                        PIC S9(07) COMP.

.. and when you need a record

     SEARCH Scroll-Key
      WHEN KeyValue (SK-Index) EQUAL Value-I-am-desparately-seeking
         MOVE RRN(Sk-index) TO Relative-key
         READ relative-file...


Just a thought.

MCM






just fetch the records as needed.



. How would corporations the size of say,
>Amex or Visa do it. Logically you have to set some size limitation, and
>restart a fresh scroll with Start Myfile Key > xxxx  or < xxxx(?) -
…[4 more quoted lines elided]…
>Jimmy, Calgary AB
```

#### ↳ Re: Scrolling records

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 1999-09-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90C968BF72979FD6.36517D9BADFF92CE.C060A6501B04F29A@lp.airnews.net>`
- **References:** `<37E85E50.C7403A8E@home.com>`

```
On Wed, 22 Sep 1999 04:34:54 GMT, "James J. Gavan" <jjgavan@home.com>
enlightened us:

>Movie scenario : Our erstwhile hero/heroine breaks into a highly secure
>classified installation, and typing at 1,200 words p.m., breaks the
…[13 more quoted lines elided]…
>Jimmy, Calgary AB

I've done something like you're describing on the Mainframe in a CICS
environment.  The file that was being displayed was an ESDS file.  The
program was pseudo-conversational.  The screen was defined as 22
lines, thus you would display 22 lines of data.  The other two were
used for heading information and PF Key display.  Basically, the first
key displayed on the screen and the last key displayed on the screen
were saved in a temp storage record.  If a user pressed the FORWARD PF
Key, I'd take the last key displayed, read the file, read next, save
the key as the first key, build the display line, read 21 more records
building display lines, save the last key; rewrite the temp storage
record.

HTH

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Laughing stock: cattle with a sense of humor.

Remove nospam to email me.

 Steve
```

#### ↳ OT - humor?

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37E9C1C7.A86F8EE0@att.net>`
- **References:** `<37E85E50.C7403A8E@home.com>`

```
"James J. Gavan" wrote:
> 
> Movie scenario : Our erstwhile hero/heroine breaks into a highly secure
> classified installation, and typing at 1,200 words p.m., breaks the
> security code - and Voila! - streams of records scroll for him/her -
> you get the idea.

If interested, check the BIT.LISTSERV.IBM-MAIN for a thread called
"Movie MIPS", roughly a year ago.

Bill Lynch
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
