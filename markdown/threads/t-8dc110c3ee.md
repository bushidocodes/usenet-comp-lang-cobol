[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# LIKE command in DB2-SELECT with lowercase

_2 messages · 2 participants · 2004-05_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### LIKE command in DB2-SELECT with lowercase

- **From:** stephan.schenk@swissonline.ch (S Schenk)
- **Date:** 2004-05-15T03:10:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2a33192c.0405150210.3be15d59@posting.google.com>`

```
I have troubles with a DB2-Select containing a LIKE-Statement. I try
select all persons from a usertable with generic searchfields.

05  W-USER-NAME-LOW              PIC X(50).
05  W-USER-VORNAME-LOW           PIC X(50).

-------------

DECLARE CURSOR_2400 CURSOR FOR 
SELECT     name, givenname
FROM       usertable
WHERE      LOWER (name)            = :W-USER-NAME-LOW    
AND        LOWER (givenname)    LIKE :W-USER-GIVENNAME-LOW 
ORDER BY   name, givenname
FOR FETCH ONLY                                           

--------------

I expect that all users are found matching to the inputstrings.
Example: miller (name) p% (givennamen) -> Result: Miller Peter, Miller
Paul, Miller Paul-Henry, ...

The execution of the code above returning NOTFOUND (+100) after the
FETCH CURSOR_2400. If i execute the select-statement native in QMF,
Platinum or in a JCL, the result is as i expect.

Got anybody a solution for my problem or is it basically not possible?
Thanks for any comment.
```

#### ↳ Re: LIKE command in DB2-SELECT with lowercase

- **From:** robert.deletethis@wagner.net (Robert Wagner)
- **Date:** 2004-05-15T17:40:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40a65557.388708955@news.optonline.net>`
- **References:** `<2a33192c.0405150210.3be15d59@posting.google.com>`

```
stephan.schenk@swissonline.ch (S Schenk) wrote:

>I have troubles with a DB2-Select containing a LIKE-Statement. I try
>select all persons from a usertable with generic searchfields.
…[22 more quoted lines elided]…
>Platinum or in a JCL, the result is as i expect.

It is failing because of trailing spaces in given name. When you type it into
QMF et al, you say LIKE 'p%'. The string has no trailing spaces. Try

AND LOWER (givenname) LIKE RTRIM(:W-USER-GIVENNAME-LOW)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
