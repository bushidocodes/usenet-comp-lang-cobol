[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accessing MS-SQL Server from within ACU-Cobol

_9 messages · 6 participants · 2004-01_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Accessing MS-SQL Server from within ACU-Cobol

- **From:** Daniel Klopfer <dk@grunecker.de>
- **Date:** 2004-01-14T12:11:35+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com>`

```
Hi all,

I am trying to access a SQL-Server database from within an Cobol
program. 
The first attempts were succesful, but now I've got a problem with
some record-dscriptions: The variable-types "INT" , "INT NOT NULL"
and "VARCHAR(nn)" can be  represented by PIC 9(9), PIC S9(9) and PIC X
clauses.

What PIC must I use for variable-type "DATETIME" and "DECIMAL(X,Y)???

Any hint is welcome.......

Thanks
Daniel
```

#### ↳ Re: Accessing MS-SQL Server from within ACU-Cobol

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-15T02:59:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40054bea_1@news.athenanews.com>`
- **References:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com>`

```

"Daniel Klopfer" <dk@grunecker.de> wrote in message
news:r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com...
> Hi all,
>
…[8 more quoted lines elided]…
>

Dates are problematic. If you really must store them as DATETIME (I store
them as CHAR (YYYYMMDD) and do all the arithmetic and conversion in my
Programs, using a standard component I wrote) then try  "USAGE COMP-2" (NO
Picture clause). Dates are actually stored on the database as 64 bit
floating point numbers. You can also get away with PIC 9(18) the maximum
numeric size in COBOL that hasn't implemented the new standard. Use your
debugger to see what is actually returned in these fields.

DECIMAL (X,Y) is PIC 9(X)v(Y). so, 123.45678 is PIC 9(3)v9(5).

HTH,

Pete.
```

##### ↳ ↳ Re: Accessing MS-SQL Server from within ACU-Cobol

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-14T11:25:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401141125.465d2e7b@posting.google.com>`
- **References:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com> <40054bea_1@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> DECIMAL (X,Y) is PIC 9(X)v(Y). so, 123.45678 is PIC 9(3)v9(5).

DECIMAL (X,Y) is PIC S9(Z)v9(Y) where Z is X - Y.  The X is the total
number of digits, Y of which are the decimal part.

     DECIMAL (10,2) is PIC S9(8)V99.
```

###### ↳ ↳ ↳ Re: Accessing MS-SQL Server from within ACU-Cobol

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-15T09:57:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4005adb4$1_2@news.athenanews.com>`
- **References:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com> <40054bea_1@news.athenanews.com> <217e491a.0401141125.465d2e7b@posting.google.com>`

```
Oops!

Thanks for that. Haven't CREATEd any DBs for a while <G>.

Pete.

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0401141125.465d2e7b@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
…[5 more quoted lines elided]…
>      DECIMAL (10,2) is PIC S9(8)V99.
```

###### ↳ ↳ ↳ Re: Accessing MS-SQL Server from within ACU-Cobol

_(reply depth: 4)_

- **From:** Daniel Klopfer <dk@grunecker.de>
- **Date:** 2004-01-15T08:25:08+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mqfc0096u95hsdp8keqo4k412qn9advuke@4ax.com>`
- **References:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com> <40054bea_1@news.athenanews.com> <217e491a.0401141125.465d2e7b@posting.google.com> <4005adb4$1_2@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> schrieb:

>>
>> DECIMAL (X,Y) is PIC S9(Z)v9(Y) where Z is X - Y.  The X is the total
…[3 more quoted lines elided]…
>

Thanks for the information. For myself I wouldnt use DATETIME, but I
have to access an existing database in which the dates are defined in
this way.

So thank you again and greetings from Germany
Daniel
```

###### ↳ ↳ ↳ Re: Accessing MS-SQL Server from within ACU-Cobol

_(reply depth: 5)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-01-15T08:32:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0401150832.6ef2d0d7@posting.google.com>`
- **References:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com> <40054bea_1@news.athenanews.com> <217e491a.0401141125.465d2e7b@posting.google.com> <4005adb4$1_2@news.athenanews.com> <mqfc0096u95hsdp8keqo4k412qn9advuke@4ax.com>`

```
Daniel Klopfer <dk@grunecker.de> wrote in message news:<mqfc0096u95hsdp8keqo4k412qn9advuke@4ax.com>...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> schrieb:
> 
…[12 more quoted lines elided]…
> Daniel

For Oracle I formated them using SQL (date/Time fields) so they are
passed and updated in a more "traditional" and not "native" format.  I
don't have an example handy but someone here will.
```

###### ↳ ↳ ↳ Re: Accessing MS-SQL Server from within ACU-Cobol

_(reply depth: 5)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-16T12:52:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40072857$1_2@news.athenanews.com>`
- **References:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com> <40054bea_1@news.athenanews.com> <217e491a.0401141125.465d2e7b@posting.google.com> <4005adb4$1_2@news.athenanews.com> <mqfc0096u95hsdp8keqo4k412qn9advuke@4ax.com>`

```

"Daniel Klopfer" <dk@grunecker.de> wrote in message
news:mqfc0096u95hsdp8keqo4k412qn9advuke@4ax.com...
>
> So thank you again and greetings from Germany
>
Das war fuer mich ein vergnugung, und gleichfalls mit der Grussen, von Neu
Seeland <G>

Pete.
```

###### ↳ ↳ ↳ Re: Accessing MS-SQL Server from within ACU-Cobol

_(reply depth: 5)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2004-01-20T01:33:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<builjl0jvb@enews1.newsguy.com>`
- **References:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com> <40054bea_1@news.athenanews.com> <217e491a.0401141125.465d2e7b@posting.google.com> <4005adb4$1_2@news.athenanews.com> <mqfc0096u95hsdp8keqo4k412qn9advuke@4ax.com>`

```
"Daniel Klopfer" <dk@grunecker.de> wrote:
> Thanks for the information. For myself I wouldnt use DATETIME, but I
> have to access an existing database in which the dates are defined in
> this way.

Just a bit of info about DATETIME in MS parlance -- that's an 8-byte IEEE
floating point.  It is a simple offset from a fixed zero date (December 30,
1899 if I remember correctly.)
```

#### ↳ Re: Accessing MS-SQL Server from within ACU-Cobol

- **From:** Jon Scally <jscally@sbcglobal.net>
- **Date:** 2004-01-16T07:34:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pan.2004.01.16.07.34.57.266000@sbcglobal.net>`
- **References:** `<r98a00hd6jkol8i681i9gnui8iu3el3o3j@4ax.com>`

```
On Wed, 14 Jan 2004 12:11:35 +0100, Daniel Klopfer wrote:

> Hi all,
> 
…[12 more quoted lines elided]…
> Daniel

For a DATE field you would want to use a PIC 9(8), but you will also need
to use the DATE directive for Acu4GL for MS SQL to identify to the
database that it knows the field is a DATE field:

01 MY-REC.
$XFD DATE=YYYYMMDD
   05 DATE-FLD		PIC 9(8).

Hope that helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
