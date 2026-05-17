[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COPY REPLACING

_3 messages · 3 participants · 1997-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### COPY REPLACING

- **From:** "j lenz" <ua-author-17071373@usenetarchives.gap>
- **Date:** 1997-08-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33F11423.3CE0@arlington.net>`

```

Greetings,

I am trying to use the COPY REPLACING with no success using IBM DOS/VS
COBOL (VSE/ESA).

My COPYBOOK, CBCMFDD, layout looks as follows:

000001*01 CUSTOMER-MASTER-FILE.
000002 05 CMF-RECORD-KEY.
000003 10 CMF-BRANCH-NUMBER PIC X(3).
000004 10 CMF-CUSTOMER-NUMBER PIC X(8).
000005 05 CMF-CUSTOMER-NAME PIC X(30).
000006 05 CMF-CUSTOMER-ADDRESS-1 PIC X(30).
000007 05 CMF-CUSTOMER-ADDRESS-2 PIC X(30).
000008 05 CMF-CUSTOMER-CITY PIC X(30).
000009 05 CMF-CUSTOMER-STATE PIC X(2).
000010 05 CMF-CUSTOMER-COUNTRY PIC X(2).
000011 05 CMF-CUSTOMER-ZIP-CODE PIC X(9).
000012 05 CMF-.....more data fields follow,
but you get the idea...

What I am trying to accomplish is to copy the layout into my program,
but change CMF- to WSC- in the process.

In the DATA DIVISION, my code looks as follows:

000040
000050 01 CUSTOMER-MASTER-FILE. COPY CBCMFDD REPLACING
==CMF== BY ==WSC==.
000060

I have also tried variations of this, but with no success.

Does anyone know why this is not working? Can I COPY REPLACING a
partial field name in COBOL?

I can get it to work when I code COPY CBCMFDD REPLACING CMF-RECORD-KEY
BY WSC-RECORD-KEY, but I don't want to hardcode like this - I want the
compiler to do the work. I also know how the COPY REPLACING works in
COBOL II and can get it to work, but the requirements for COBOL II
(:TAG:) don't fit my copybook layout, and don't I see my copybooks
changing to that type of naming convention.

Any help would be appreciated.

Thanks in advance.

Joseph Lenz
TTI, Inc.
Fort Worth, TX

Remove "_ns" in my email address to reply directly to me.
```

#### ↳ Re: COPY REPLACING

- **From:** "li..." <ua-author-464752@usenetarchives.gap>
- **Date:** 1997-08-13T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08bb9cfe35-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33F11423.3CE0@arlington.net>`
- **References:** `<33F11423.3CE0@arlington.net>`

```

Copy replacing will not do a partial field name replace in any IBM version
of COBOL. I am not sure of other COBOL compilers, but according to
language specification COPY REPLACING will replace only full field names.
Too bad! If you want to chage cmf-customer-number to wsc-customer-number
you should give
COPY CBCMFDD REPLACING CMF-CUSTOMER-NUMBER BY WSC-CUSTOMER-NUMBER.
Currently the only way you can do is to create a new copy book!
Bye
Hari Gangadharan
http://members.aol.com/harinair
```

##### ↳ ↳ Re: COPY REPLACING

- **From:** "arn b" <ua-author-2587922@usenetarchives.gap>
- **Date:** 1997-08-13T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08bb9cfe35-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-08bb9cfe35-p2@usenetarchives.gap>`
- **References:** `<33F11423.3CE0@arlington.net> <gap-08bb9cfe35-p2@usenetarchives.gap>`

```

Lians wrote:
› 
› Copy replacing will not do a partial field name replace in any IBM version
…[8 more quoted lines elided]…
› http://members.aol.com/harinair

This is not true!

In COBOL II and beyond, partial field replace is possible if the field
is imbedded within : characters. The problem as I understand it is this
was to be done in DOS/VS COBOL and at that level of the compiler, I too
have been unable to get partial field replacing to work. Additionally,
older versions of IBM COBOL regurge when fed a copybook coded with the :
characters. This can be a bit of a problem in a mixed COBOL environment.
The original author was aware of this situation.

To do a Partial field replace in COBOL II
Code a copy member as follows:
000001 01 :CMF-RECORD:
000002 05 :CMF:-RECORD-KEY.
000003 10 :CMF:-BRANCH-NUMBER PIC X(3).
000004 10 :CMF:-CUSTOMER-NUMBER PIC X(8).
000005 05 :CMF:-CUSTOMER-NAME PIC X(30).
000006 05 :CMF:-CUSTOMER-ADDRESS-1 PIC X(30).

In the program code:
COPY member-name REPLACING ==:CMF:== by ==ANYALPHA==.

Arn Burkhoff
Warren, NJ
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
