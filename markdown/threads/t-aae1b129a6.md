[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# indicator field

_4 messages · 4 participants · 1999-01_

---

### indicator field

- **From:** carlwenrich@mindspring.com (Carl Wenrich)
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368ed8d7.1066507@news.mindspring.com>`

```
Can anyone tell me what the legal entries for the indicator field are,
and what they mean?
```

#### ↳ Re: indicator field

- **From:** bbello5778@aol.com (BBello5778)
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990102214825.21429.00006715@ng-fp1.aol.com>`
- **References:** `<368ed8d7.1066507@news.mindspring.com>`

```
If you are refering to the indicator field used when accesing DB2. It is used
with fields that may have null values. It is used to tell DB2 if a column being
inserted/updated  is null or not. If you do a select DB2 will update the
indicator field appropriately. I believe a -1 means it's null and 1 means it's
not null.

Someone in the NG can probably explain better.


Good luck

Bosun

BBello5778@aol.com 
http://members.aol.com/bbello5778/bosun.htm
Programmer/Analyst. Bloomington, IL
```

#### ↳ Re: indicator field

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368f0308.45794817@netnews>`
- **References:** `<368ed8d7.1066507@news.mindspring.com>`

```
'Twas Sun, 03 Jan 1999 02:42:15 GMT, when carlwenrich@mindspring.com (Carl
Wenrich) illuminated comp.lang.cobol thusly:

>Can anyone tell me what the legal entries for the indicator field are,
>and what they mean?

Gladly:

-    Continuation.  The last token on the previous line continues onto
     this line
D    Debugging line.  This line is a comment unless USE FOR DEBUGGING
     was specified.
*    Comment line.
/    Comment line, print this line at the top of a new page.

These are the only ones defined in the standard.  Unisys uses $ in the
indicator position for compiler directives.
```

##### ↳ ↳ Re: indicator field

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76nvf5$ske$1@news.igs.net>`
- **References:** `<368ed8d7.1066507@news.mindspring.com> <368f0308.45794817@netnews>`

```

Randall Bart wrote in message <368f0308.45794817@netnews>...
>'Twas Sun, 03 Jan 1999 02:42:15 GMT, when carlwenrich@mindspring.com (Carl
>Wenrich) illuminated comp.lang.cobol thusly:
…[14 more quoted lines elided]…
>indicator position for compiler directives.


You can do the same in Fujitsu.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
