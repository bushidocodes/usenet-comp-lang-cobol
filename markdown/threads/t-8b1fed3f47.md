[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

_8 messages · 5 participants · 2018-01 → 2018-02_

**Topics:** [`Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)`](../topics.md#open-source) · [`Language features and syntax`](../topics.md#syntax) · [`Databases and SQL`](../topics.md#databases)

---

### Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

- **From:** "vonnie.bartlett" <ua-author-14501838@usenetarchives.gap>
- **Date:** 2018-01-23T11:14:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com>`

```
I am working on a project to migrate our cobol from Micro Focus cobol on AIX to gnu cobol on Linux.
We have a need to have multiple databases open at the same time.
exec sql connect :username identified by :password at :db-id using :db-string
is not working in gnu cobol on Linux. It's giving an invalid name or password error, but the same syntax and credentials work on AIX.

This syntax with the same credentials works fine on linux.
exec sql connect :single-connect-str end-exec.

Has anyone else run into this error and have a solution? Your help is appreciated.
```

#### ↳ Re: Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

- **From:** "vbcoen" <ua-author-7065949@usenetarchives.gap>
- **Date:** 2018-01-23T20:05:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b1fed3f47-p2@usenetarchives.gap>`
- **In-Reply-To:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com>`
- **References:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com>`

```
Hello vonnie!

Tuesday January 23 2018 16:14, you wrote to All:

> Subject: exec sql connect :username identified by :password at :db-id
> using :db-string not working in gnu cobol

> I am working on a project to migrate our cobol from Micro Focus cobol
> on AIX to gnu cobol on Linux. We have a need to have multiple
…[3 more quoted lines elided]…
> but the same syntax and credentials work on AIX.

> This syntax with the same credentials works fine on linux.
> exec sql connect :single-connect-str end-exec.

> Has anyone else run into this error and have a solution? Your help is
> appreciated.

I looked at this issue (lightly) when trying to migrate some rdb data
access modules to Oracle from SQL server but I could not find a mechanism
to support doing so but I did try ad read the full Oracle manual.
I installed 12.1.0.2 along with the C client package under Linux.

Luckily I found a way around it, again lightly but decided to migrate to
Mysql first and look again when coding is tested.

Please advise if you find a solution.

Vince
```

#### ↳ Re: Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-01-27T18:22:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b1fed3f47-p3@usenetarchives.gap>`
- **In-Reply-To:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com>`
- **References:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com>`

```
On 24/01/2018 5:14 AM, von··t@cs··i.com wrote:
› I am working on a project to migrate our cobol from Micro Focus cobol on AIX to gnu cobol on Linux.
› We have a need to have multiple databases open at the same time.
› exec sql connect :username identified by :password  at :db-id using :db-string
› is not working in gnu cobol on Linux.  It's giving an invalid name or password error, but the same syntax and credentials work on AIX.

Are you saying it works for GNU COBOL in AIX but not in Linux? That
certainly would be an error...
›
› This syntax with the same credentials works fine on linux.
› exec sql connect :single-connect-str end-exec.

Can you show us the run time contents of the host variable
:single-connect-string?
›
› Has anyone else run into this error and have a solution? Your help is appreciated.
›
Connection strings to RDBs have long been a source of chagrin for
programmers and there are web sites dedicated to the differences in
connection strings for different RDBMS.

You didn't state what your RDBMS is.

As far as syntax for Embedded SQL in COBOL goes, I would EXPECT it to
vary across different COBOL systems (because completely different SQL
pre-processors are involved) so I would not see it as an "Error" if the
syntax needed for GNU COBOL is different from the Micro Focus
implementation. (If GNU COBOL can accommodate the Micro Focus syntax,
then kudos to GNU COBOL, but if it can only do so under Linux, then that
does look like an error (unless their documentation states that it is
intended for Linux only...)

I no longer use Embedded SQL (having moved to a Data Access Layer driven
by LINQ some years ago) but, when I did, I used Fujitsu NetCOBOL which
uses an external "ODBC info" file. I mention this in passing, just to
point out that different COBOL systems will have different ways of
approaching ESQL.

I would expect the syntax to be:

EXEC SQL
CONNECT OR
"DEFAULT" (where the DEFAULT DB is noted in the external information
file...)
... then...

USER (or this information can be
placed in the external file so that credentials are not hard coded in
the program; the credentials are encrypted in the external file and
managed by a provided tool so that different credentials can be provided
without having to recompile....)

The above is just another way of getting the 3 vital pieces of information:

1. DB name
2. UserID
3. Password

I think your problem is that a syntax which works with GNU COBOL under
AIX does not do so under Linux? (Not clear in your post...)

While this may be an error, you noted that if you provide a "connection
string" it works.

The obvious solution, then, is to provide the connection string... :-)

(You might need to do some global edits (or write a small COBOL
program....) to process your sources and detect where CONNECTS are being
made, then replace the "bad" syntax with the new single connection string.)

IMO, the BEST solution is to remove all CONNECTS (and, indeed, all SQL
access) out of your application code into a separate Data Access Layer
(DAL). Applications request data from the DAL (or push data to the DAL)
through an interface that is actually a COBOL record layout...

There is then no impact on applications when future RDBMS conversions
are required, and there is no duplicated SQL in the system either...

Maybe this will cause some re-evaluation of the whole business of
embedding SQL in COBOL.

My thoughts on why this is NOT a good idea are covered across 3 pages on
the PRIMA web site, starting here:

https://primacomputing.co.nz/PRIMAMetro/RDBandSQL.aspx

(You will be no worse off if you take 10 minutes and read these pages;
it may even stimulate some ideas for you going forward... :-))

I'll respond to questions, comments and observations if you post them here.

Pete.
I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2018-01-28T00:31:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b1fed3f47-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b1fed3f47-p3@usenetarchives.gap>`
- **References:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com> <gap-8b1fed3f47-p3@usenetarchives.gap>`

```
On 1/27/2018 5:22 PM, pete dashwood wrote:
› On 24/01/2018 5:14 AM, von··t@cs··i.com wrote:
›› I am working on a project to migrate our cobol from Micro Focus cobol 
…[93 more quoted lines elided]…
› Pete.

It appears there was some activity on this subject in the GnuCOBOL Forum:

https://sourceforge.net/p/open-cobol/discussion/cobol/thread/3825cabe/


I don't completely understand the problem, which seems to be related to
differing rules for truncation and padding with spaces between Oracle
and GnuCOBOL. They may have a workaround that includes some minor code
changes.

Kind regards,


http://www.arnoldtrembley.com/

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-02-05T18:21:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b1fed3f47-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b1fed3f47-p4@usenetarchives.gap>`
- **References:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com> <gap-8b1fed3f47-p3@usenetarchives.gap> <gap-8b1fed3f47-p4@usenetarchives.gap>`

```
On 28/01/2018 6:31 PM, Arnold Trembley wrote:
› On 1/27/2018 5:22 PM, pete dashwood wrote:
›› On 24/01/2018 5:14 AM, von··t@cs··i.com wrote:
…[111 more quoted lines elided]…
› 
Thanks for the link, Arnold.

I went and had a look, and the problem can be easily solved by reference
modification. (It really comes down to the lack of a variable length
field facility in COBOL. This leads to a contrived "PIC X OCCURS
DEPENDING...", which is a horror show, so instead of doing that, an
extension has been used that is not Standard COBOL.)

It could be solved (with standard COBOL) by simply using refmodding on
the moves that set the Host Variables for DB, Account and Password, and
attaching a x'00' byte to the string being moved in each case (Or
initializing these fields to LOW-VALUES and STRINGing... DELIMITED BY SIZE).

It may be that the ORACLE pre-processor won't support refmodding on a
Host Variable (because the HV is recognized by a colon, and the refmod
uses colon to separate position and length.) In which case you'd need to
set 3 work fields and then move those to the HVs.

A standard COBOL solution would be better, in my opinion than the
current extension with 'Arr', but it appears that refmodding has not
been considered.

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

_(reply depth: 4)_

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2018-02-06T00:57:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b1fed3f47-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b1fed3f47-p5@usenetarchives.gap>`
- **References:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com> <gap-8b1fed3f47-p3@usenetarchives.gap> <gap-8b1fed3f47-p4@usenetarchives.gap> <gap-8b1fed3f47-p5@usenetarchives.gap>`

```
On 2/5/2018 5:21 PM, pete dashwood wrote:
› (SNIP) 
› Thanks for the link, Arnold.
…[23 more quoted lines elided]…
› 

Checking the GnuCOBOL Programmers Guide (Version 3.0 RC1), there is
another option using the CONCATENATE intrinsic function:

===begin quote===

So, GnuCOBOL programmers expecting to pass strings to or receive strings
from C programs had best be prepared to deal with the null-termination
issue, as follows:
1. Pass a quoted literal string from GnuCOBOL to C as a
zero-delimited string literal (Z’’).
2. Pass alphanumeric (PIC X) or alphabetic (PIC A) data items to C
subroutines by appending an ASCII NULL character (X’00’) to
them. For example, to pass the 15-character LastName data item
described above to a C subroutine:
01 LastName-Arg-to-C PIC X(16).
...
MOVE FUNCTION CONCATENATE(LastName,X’00’) TO LastName-Arg-to-C

And then pass LastName-Arg-to-C to the C subprogram!

===end quote===

Kind regards,


http://www.arnoldtrembley.com/

---
This email has been checked for viruses by Avast antivirus software.
https://www.avast.com/antivirus
```

###### ↳ ↳ ↳ Re: Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2018-02-06T18:06:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b1fed3f47-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8b1fed3f47-p6@usenetarchives.gap>`
- **References:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com> <gap-8b1fed3f47-p3@usenetarchives.gap> <gap-8b1fed3f47-p4@usenetarchives.gap> <gap-8b1fed3f47-p5@usenetarchives.gap> <gap-8b1fed3f47-p6@usenetarchives.gap>`

```
On 6/02/2018 6:57 PM, Arnold Trembley wrote:
› On 2/5/2018 5:21 PM, pete dashwood wrote:
›› (SNIP) Thanks for the link, Arnold.
…[49 more quoted lines elided]…
› 
Yes, that's pretty good, but it is NOT standard COBOL...

Refmodding or Stringing are both standard across all versions of COBOL.

Personally, I like intrinsic functions, but I like an attempt at
"platform independence" with COBOL (by using standard constructs) even more.

I guess it really depends on the personal preferences of the Programmer
or Site.

Cheers,

Pete.

I used to write COBOL; now I can do anything...
```

#### ↳ Re: Exec sql connect :username identified by :password at :db-id using :db-string not working in gnu cobol

- **From:** "mattjdean1" <ua-author-14501792@usenetarchives.gap>
- **Date:** 2018-02-08T10:24:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8b1fed3f47-p8@usenetarchives.gap>`
- **In-Reply-To:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com>`
- **References:** `<80887a6d-c3b1-4fff-862a-d59173f036f9@googlegroups.com>`

```
On Tuesday, January 23, 2018 at 11:14:56 AM UTC-5, von··.@cs··i.com wrote:
› I am working on a project to migrate our cobol from Micro Focus cobol on AIX to gnu cobol on Linux.  
› We have a need to have multiple databases open at the same time.  
…[6 more quoted lines elided]…
› Has anyone else run into this error and have a solution?  Your help is appreciated.


If you were to examine the intermediate code generated by the compiler (the c code it generates) on AIX and Linux, you might be able to see something. Just a suggestion if you are stuck.

Best Regards,

Matt Dean
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
