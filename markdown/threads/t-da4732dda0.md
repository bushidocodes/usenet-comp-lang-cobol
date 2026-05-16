[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Tables(2)

_2 messages · 2 participants · 1999-05_

---

### Tables(2)

- **From:** "Rana S Alexander" <JOSHNYA@prodigy.net>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7gn1vt$39b0$1@newssvr04-int.news.prodigy.com>`

```
Yes I am in an introductory course.  I do know how to access them just I
don't know how to set them up.
This is what I have so far:

       01  EMP-TABLE.
           05 LOCATION-CODE
               OCCURS 3 TIMES                         PIC 9(2).
              10 PERFORMANCE-CODE
               OCCURS 2 TIMES                         PIC 9.
.
   .
     .
       01  PROGRAM-SUBSCRIPTS.
           05 LOCATION-SUB                             PIC 9(4) COMP.
           05 PERFORMANCE-SUB                          PIC 9(4) COMP.

If anyone can give me some help on the synatx I would be very thankful.
                                                                Angie D.S.
```

#### ↳ Re: Tables(2)

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4%GX2.4371$Nn6.931765@news3.mia>`
- **References:** `<7gn1vt$39b0$1@newssvr04-int.news.prodigy.com>`

```
Rana S Alexander wrote
>Yes I am in an introductory course.  I do know how to access them
>just I don't know how to set them up.
…[6 more quoted lines elided]…
>               OCCURS 2 TIMES                         PIC 9.

The problem with this has absolutely nothing to do with it being a
table.  The problem is that LOCATION-CODE has a PIC, therefore cannot
also be a group level item.  The proper way to set it up can only be
determined *after* you have defined what the table is to store, and
how it is to be organized.  For example, do you have values which must
be stored under LOCATION-CODE, or all of them to be stored under
PERFORMANCE-CODE?  For example:

This table allows ET-LOCATION-CODE to be stored and referenced by only 1
subscript: ET-LOCATION-CODE(subscript)
but field ET-PERFORMANCE-CODE may only be referenced using 2 subscripts:
ET-PERFORMANCE-CODE(subscript1, subscript2)

       01  EMPLOYEE-TABLE.
           05  ET-LOCATION                OCCURS 3 TIMES.
               07  ET-LOCATION-CODE           PIC 9(02).
               07  ET-PERFORMANCE-CODE        OCCURS 2 TIMES.
                                                  PIC  9(01).

This table does not have ET-LOCATION-CODE, but ET-PERFORMANCE-CODE works
the same way as above.

       01  EMPLOYEE-TABLE.
           05  ET-LOCATION                OCCURS 3 TIMES.
               07  ET-PERFORMANCE-CODE        OCCURS 2 TIMES.
                                                  PIC  9(01).

This table has several fields which may all be referenced using two
subscripts: ET-xxxxx(subscript1, subscript2)

       01  EMPLOYEE-TABLE.
           05  ET-LOCATION                OCCURS 3 TIMES.
               07  ET-PERFORMANCE             OCCURS 2 TIMES.
                   09  ET-xxxxx                   PIC  ...
                   09  ET-xxxxx                   PIC  ...
                   09  ET-xxxxx                   PIC  ...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
