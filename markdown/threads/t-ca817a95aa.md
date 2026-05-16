[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INDEXES: BTRIEVE vs EXTFH

_8 messages · 3 participants · 2006-06 → 2006-07_

---

### INDEXES: BTRIEVE vs EXTFH

- **From:** "alexandretalbert@gmail.com" <alexandretalbert@gmail.com>
- **Date:** 2006-06-30T06:51:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com>`

```
Hi folks!

I have some betrieve files created by Microfocus Cobol (trough
FILETYPE"6" directive), and accessed trough DDF files created with
"CREATE TABLE" statements. My (BIG) problem concern to the INDEXES.
With BUTIL -STAT, I can see that every index on the data file is
created eith type=String.

So, the DDF index definition will never match. For example, for the
table:

       FD  DC0030.
       01  DC0030-REG.
           2 DC0030-CODE                 PIC  9(3).
           2 DC0030-NAME                PIC  X(50).

           SELECT DC0030 ASSIGN TO WS0030-CAM-GERAL
           ORGANIZATION IS INDEXED
           ACCESS MODE  IS DYNAMIC
           LOCK   MODE  IS AUTOMATIC
           FILE STATUS  IS WS-8005-STATUS
           RECORD KEY IS DC0030-CODE
           .

I have the following CREATE TABLE:

CREATE TABLE DC0030 USING 'DC0030.MKD' (CODE NUMERIC(3,0), NAME
CHAR(50),PRIMARY KEY(CODE))

Then the PRIMARY INDEX CODE is NUMERIC on DDF but STRING on the data
file....For this reason, some queries doesn´t work.....

Any suggestion??

Thanks!!!!
```

#### ↳ Re: INDEXES: BTRIEVE vs EXTFH

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-06-30T18:22:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zZdpg.108811$iF6.25960@pd7tw2no>`
- **In-Reply-To:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com>`
- **References:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com>`

```
alexandretalbert@gmail.com wrote:
> Hi folks!
> 
…[33 more quoted lines elided]…
>


Don't know whether it will help at all but check out the following N/E 
4.0 example which writes Btrieve records :-

http://supportline.microfocus.com/examplesandutilities/nesamp.asp

Under the heading "General" download btrvtest.zip

Jimmy
```

##### ↳ ↳ Re: INDEXES: BTRIEVE vs EXTFH

- **From:** "alexandretalbert@gmail.com" <alexandretalbert@gmail.com>
- **Date:** 2006-06-30T12:19:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151695162.260057.246900@d56g2000cwd.googlegroups.com>`
- **In-Reply-To:** `<zZdpg.108811$iF6.25960@pd7tw2no>`
- **References:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com> <zZdpg.108811$iF6.25960@pd7tw2no>`

```
Thanks James...I´ll check it out.

James J. Gavan wrote:
> alexandretalbert@gmail.com wrote:
> > Hi folks!
…[44 more quoted lines elided]…
> Jimmy
```

###### ↳ ↳ ↳ Re: INDEXES: BTRIEVE vs EXTFH

- **From:** "alexandretalbert@gmail.com" <alexandretalbert@gmail.com>
- **Date:** 2006-07-03T11:37:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1151951821.620062.13450@b68g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1151695162.260057.246900@d56g2000cwd.googlegroups.com>`
- **References:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com> <zZdpg.108811$iF6.25960@pd7tw2no> <1151695162.260057.246900@d56g2000cwd.googlegroups.com>`

```
One more detail: I only have problems when I try to query a table with
a SEGMENTED KEY. For example:

        FD  DC0099.
        01  DC0030-REG.
            2 DC0099-ORDER.
               3 DC0099-DOC-CODE                PIC  9(1).
               3 DC0099-ORDER-CODE           PIC  9(6).
            2 DC0099-ORDER-DESCR            PIC  X(30).

           SELECT DC0099 ASSIGN TO "DC0099"
            ORGANIZATION IS INDEXED
            ACCESS MODE  IS DYNAMIC
            LOCK   MODE  IS AUTOMATIC
            FILE STATUS  IS WS-8005-STATUS
            RECORD KEY IS DC0099-ORDER


The FD / SELECT above, cause Microfocus to create a btrieve data file
with one KEY (1) which contains only ONE STRING SEGMENT ( 7 caracters
length (1+6) ).

 But when I run the CREATE STATEMENT for the table, the INDEX will be
formed by 2 SEGMENTS (NUMERIC LENGTH 1   + NUMERIC LENGTH 6). Then my
queries don´t work properly.

select * from dc0099 where doc_code  = 1  (doesn´t work)

select * from dc0099 where convert(doc_code,sql_numeric) = 1 (works,
but using no index)


Thanks again!


alexandretalbert@gmail.com wrote:
> Thanks James...I´ll check it out.
>
…[47 more quoted lines elided]…
> > Jimmy
```

###### ↳ ↳ ↳ Re: INDEXES: BTRIEVE vs EXTFH

_(reply depth: 4)_

- **From:** "James J. Gavan" <jgavandeletethis@shaw.ca>
- **Date:** 2006-07-03T20:36:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Edfqg.117721$Mn5.40691@pd7tw3no>`
- **In-Reply-To:** `<1151951821.620062.13450@b68g2000cwa.googlegroups.com>`
- **References:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com> <zZdpg.108811$iF6.25960@pd7tw2no> <1151695162.260057.246900@d56g2000cwd.googlegroups.com> <1151951821.620062.13450@b68g2000cwa.googlegroups.com>`

```
alexandretalbert@gmail.com wrote:
> One more detail: I only have problems when I try to query a table with
> a SEGMENTED KEY. For example:
…[28 more quoted lines elided]…
> 

I don't know Btrieve. Period. If you don't get an answer here join the 
Forum at microfocus.com - it's free ! Post a question under your product 
- if it's old and not listed put your query under 'Other Micro Focus 
Products".


Jimmy
```

###### ↳ ↳ ↳ Re: INDEXES: BTRIEVE vs EXTFH

_(reply depth: 4)_

- **From:** "Blondie" <gordcrawshaw@hotmail.com>
- **Date:** 2006-07-14T07:42:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1152888143.581014.20310@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1151951821.620062.13450@b68g2000cwa.googlegroups.com>`
- **References:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com> <zZdpg.108811$iF6.25960@pd7tw2no> <1151695162.260057.246900@d56g2000cwd.googlegroups.com> <1151951821.620062.13450@b68g2000cwa.googlegroups.com>`

```
alexandretalbert@gmail.com wrote:
> One more detail: I only have problems when I try to query a table with
> a SEGMENTED KEY.

In order for Btrieve to recognize the segments defined in your program
they must be defined in your SELECT statement (in MicroFocus anyway).
Instead of refering to the group name as the key use an undefined name
and specify the segments:

            SELECT DC0099 ASSIGN TO "DC0099"
             ORGANIZATION IS INDEXED
             ACCESS MODE  IS DYNAMIC
             LOCK   MODE  IS AUTOMATIC
             FILE STATUS  IS WS-8005-STATUS
             RECORD KEY IS DC0099-ORDER-KEY = DC0099-DOC-CODE,

   DC0099-ORDER-CODE

Cheers,
Gord
```

###### ↳ ↳ ↳ Re: INDEXES: BTRIEVE vs EXTFH

_(reply depth: 4)_

- **From:** "Blondie" <gordcrawshaw@hotmail.com>
- **Date:** 2006-07-14T07:44:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1152888272.083608.136240@35g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1151951821.620062.13450@b68g2000cwa.googlegroups.com>`
- **References:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com> <zZdpg.108811$iF6.25960@pd7tw2no> <1151695162.260057.246900@d56g2000cwd.googlegroups.com> <1151951821.620062.13450@b68g2000cwa.googlegroups.com>`

```
alexandretalbert@gmail.com wrote:
> One more detail: I only have problems when I try to query a table with
> a SEGMENTED KEY.

In order for Btrieve to recognize the segments defined in your program
they must be defined in your SELECT statement (in MicroFocus anyway).
Instead of refering to the group name as the key use an undefined name
and specify the segments:

            SELECT DC0099 ASSIGN TO "DC0099"
             ORGANIZATION IS INDEXED
             ACCESS MODE  IS DYNAMIC
             LOCK   MODE  IS AUTOMATIC
             FILE STATUS  IS WS-8005-STATUS
             RECORD KEY IS DC0099-ORDER-KEY = DC0099-DOC-CODE,

   DC0099-ORDER-CODE

Cheers,
Gord
```

###### ↳ ↳ ↳ Re: INDEXES: BTRIEVE vs EXTFH

_(reply depth: 5)_

- **From:** "Blondie" <gordcrawshaw@hotmail.com>
- **Date:** 2006-07-14T07:47:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1152888446.876122.217360@75g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1152888272.083608.136240@35g2000cwc.googlegroups.com>`
- **References:** `<1151675511.860322.279320@y41g2000cwy.googlegroups.com> <zZdpg.108811$iF6.25960@pd7tw2no> <1151695162.260057.246900@d56g2000cwd.googlegroups.com> <1151951821.620062.13450@b68g2000cwa.googlegroups.com> <1152888272.083608.136240@35g2000cwc.googlegroups.com>`

```
sorry about the double post - is that what preview does?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
