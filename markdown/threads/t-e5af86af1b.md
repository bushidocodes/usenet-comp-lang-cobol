[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 3-tier

_2 messages · 2 participants · 2000-03_

---

### Re: 3-tier

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E40A24.5EA4D120@home.com>`
- **References:** `<v1t5esssoi5cim6v4a7290hgmee69i118j@4ax.com>`

```


G Moore wrote:
> 
> someone said in cobol they seperate thw tiers into file handling,
> screen and business logic. i guess my question is, how do you abstract
> file handling? like so (general skeleton)?
> 
(1) Structured :
Can't give you an example, but some 4 (?) months back a couple of people
did state they were doing this in structured - vague - but I think they
were calling individual files as separate programs. Again can't remember
specifics but they got over the problem of file-status because it was
available to both the caller and sub-program (?????). Didn't see any
source, but logically the file accesses would be made either by a flag (
1 = Open as input, 2 = Open as output etc...) coupled with EVALUATES or
getting into the file-program with entry points.

If anybody recalls that thread - perhaps they can spell it out in more
detail.

(2) OO :
If you are interested in an OO approach - see attached zip (posted
here last July).

(3) General :
The really important thing, whether structured or OO (and VITALLY
IMPORTANT for the latter, I believe), is this three-tier approach (1)
Business Logic - what you want the 'program' to do (2) Screen
Handling/Windows - display and get data from a 'dumb terminal' and (3)
DB/flat-file handling - keep the three pieces separate and you can
change one without adversely affecting the other two.

Jimmy, Calgary AB
```

#### ↳ Re: 3-tier

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-03-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E4A67D.E1FA1F70@zip.com.au>`
- **References:** `<v1t5esssoi5cim6v4a7290hgmee69i118j@4ax.com> <38E40A24.5EA4D120@home.com>`

```
"James J. Gavan" wrote:
> 
> G Moore wrote:
…[12 more quoted lines elided]…
> can change one without adversely affecting the other two.


As Jimmy states, this is a general practice, not specific to any
implementation.

You business logic is where your real knowledge of what you do is. 
With the current shift from Mainframe CICS to windows front end we
have many programs that have all the CICS calls ripped out and
replaced by windows calls.  A long arduous and error prone task.

If instead we move all the common logic between CICS and Windows into
a module then we have a product that can run on two platforms and
produce reliable results.

The back end is another area of protection.  When we move from
mainframe CICS / DB2 we might move to ODBC drivers on Windows.  It
would be great that the database (or file or indexed file) access was
isolated in a common module.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
