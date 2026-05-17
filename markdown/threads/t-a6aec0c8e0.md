[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HOW TO INSERT NULL IN TABLE_COLUMN

_4 messages · 3 participants · 1998-07_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HOW TO INSERT NULL IN TABLE_COLUMN

- **From:** "news.onaustralia.com.au" <ua-author-17074068@usenetarchives.gap>
- **Date:** 1998-07-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdb4c5$9a30fa60$1811868b@default>`

```
Hi,
I am new to DB2-COBOL programming, I have following problem.

I need to insert NULL value in a column when the supplied value
is spaces.

Example

IF LOCALITY_CODE = ' '
INSERT LOCALITY_CODE_COL VALUE (NULL)
ELSE
INSERT LOCALITY_CODE_COL VALUE(LOCALITY_CODE)

Can I do it simply writing a single INSERT Statement

Your comment will be highly appricate.

Regard
Sam
```

#### ↳ Re: HOW TO INSERT NULL IN TABLE_COLUMN

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-07-24T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6aec0c8e0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bdb4c5$9a30fa60$1811868b@default>`
- **References:** `<01bdb4c5$9a30fa60$1811868b@default>`

```
In article <01bdb4c5$9a30fa60$1811868b@default>, "news.onaustralia.com.au"
writes:

›       IF LOCALITY_CODE = '     '    
›         INSERT LOCALITY_CODE_COL VALUE (NULL)
›      ELSE
›        INSERT LOCALITY_CODE_COL VALUE(LOCALITY_CODE)

Define a host variable to be an indicator variable, COMP PIC S9(4). (I am
assuming you are dealing with an IBM mainframe since you mentioned DB2; if not,
adjust accordingly.) In the following code, I am using LOCALITY-CODE-IND as the
indicator variable.

IF LOCALITY-CODE = SPACES
MOVE -1 TO LOCALITY-CODE-IND
ELSE
MOVE 0 TO LOCALITY-CODE-IND
END-IF

EXEC SQL
INSERT LOCALITY_CODE_COL, other_columns
VALUE(:LOCALITY-CODE :LOCALITY-CODE-IND, :other-host-vars)
INTO table_name
END-EXEC

Note: indicator variables must be half-word binary host variables. In SQL
statements, indicator variables follow the host variable, no punctuation other
than the : to indicate it is a host variable. -1 means a null value will be
inserted or set, 0 means the host variable has the value to be inserted.

Coming back the other way (e.g., from a SELECT), negative means the value is
null; zero or positive means a value is being returned, positive indicating a
truncation of value (e.g., number of characters truncated off of the right if
the host variable is not long enough to contain the value in a char or varchar
column, or seconds being returned in a TIME field when the host variable is too
small to hold the seconds).

Mark A. Young
```

##### ↳ ↳ Re: HOW TO INSERT NULL IN TABLE_COLUMN

- **From:** "news.onaustralia.com.au" <ua-author-17074068@usenetarchives.gap>
- **Date:** 1998-07-25T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6aec0c8e0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6aec0c8e0-p2@usenetarchives.gap>`
- **References:** `<01bdb4c5$9a30fa60$1811868b@default> <gap-a6aec0c8e0-p2@usenetarchives.gap>`

```
Thanks a LOT, for explaning the handeling of NULL, Yes i am using DB2,
but i new to this product
Thanks Again
Regards
Sam



Mark0Young wrote in article
<199··.@lad··l.com>...
› In article <01bdb4c5$9a30fa60$1811868b@default>,
› "news.onaustralia.com.au"
…[46 more quoted lines elided]…
›
```

#### ↳ Re: HOW TO INSERT NULL IN TABLE_COLUMN

- **From:** "m. boudreau" <ua-author-17074240@usenetarchives.gap>
- **Date:** 1998-07-27T13:55:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6aec0c8e0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bdb4c5$9a30fa60$1811868b@default>`
- **References:** `<01bdb4c5$9a30fa60$1811868b@default>`

```
news.onaustralia.com.au wrote:
› 
› Hi,
…[12 more quoted lines elided]…
› Can I do it simply writing a single INSERT Statement

I have not tried this in DB2, you may wish to test first
INSERT LOCALITY_CODE_COL VALUE RTRIM(LOCALITY_CODE)

The rtrim() syntax may be incorrect for DB2, if so replace it with the
correct right trim function


Mike Boudreau

(when replying remove 'NoJunkMail' from my e-mail address)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
