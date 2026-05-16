[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL.NET : DateTime.Now access?

_3 messages · 2 participants · 2002-03_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### COBOL.NET : DateTime.Now access?

- **From:** christian@wenz.org (Christian Wenz)
- **Date:** 2002-03-26T07:42:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<27938ff7.0203260742.f78d920@posting.google.com>`

```
Hi,

I was playing around with COBOL.NET and wrote a tiny application that
reads the current time from the system and prints it in an <asp:labal
/> field.
This is what I got so far:

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
REPOSITORY.
    PROPERTY PROP-TEXT AS "Text"
    CLASS SYS-DATETIME AS "System.DateTime"
    CLASS SYS-STRING AS "System.String"
    CLASS SYS-OBJECT AS "System.Object"
    CLASS EVENTARGS AS "System.EventArgs".
OBJECT.
PROCEDURE DIVISION.
METHOD-ID. BUTTON-CLICK.
DATA DIVISION.
WORKING-STORAGE SECTION.
77 DATENOW OBJECT REFERENCE SYS-DATETIME.
77 DATE OBJECT REFERENCE SYS-STRING.
LINKAGE SECTION.
77 EVENT-SOURCE OBJECT REFERENCE SYS-OBJECT.
77 EVENT OBJECT REFERENCE EVENTARGS.
PROCEDURE DIVISION USING BY VALUE EVENT-SOURCE EVENT.
    INVOKE DATENOW "ToString"
        RETURNING DATE.
    SET PROP-TEXT OF OUTPUT TO DATE.
END METHOD BUTTON-CLICK.
END OBJECT.


My problem now is that I cannot find out the current date. Usually,
this could be done by using DateTime.Now and then invoke "ToString" on
the result. However, this code will not work:

    INVOKE DATUMNOW "Now" 
        RETURNING DATUMNOW.

-- it just says that method "Now" cannot be found.

If I am using this:
    INVOKE DATUMNOW "get_Now" 
        RETURNING DATUMNOW.

--- it says that no method get_Now with the provided interface exists.
Can anyone shed some light here please? Thanks!
```

#### ↳ Re: COBOL.NET : DateTime.Now access?

- **From:** "ronald leenheer" <r.leenheer@wanadoo.nl>
- **Date:** 2002-03-27T00:20:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1f8o8.22$LI.217@castor.casema.net>`
- **References:** `<27938ff7.0203260742.f78d920@posting.google.com>`

```
Why not the old fashioned way?

WORKING STORAGE.
 01   SYS-DATE     PIC 9(6).
 01   SYS-DATE-RED REDEFINES SYS-DATE.
        03  SYS-YY        PIC 99.
        03  SYS-MM       PIC 99.
        03  SYS-DD        PIC 99.

And in your procedure area:

        ACCEPT SYS-DATE  FROM DATE.


gr. Ronald Leenheer

"Christian Wenz" <christian@wenz.org> schreef in bericht
news:27938ff7.0203260742.f78d920@posting.google.com...
> Hi,
>
…[45 more quoted lines elided]…
> Can anyone shed some light here please? Thanks!
```

##### ↳ ↳ Re: COBOL.NET : DateTime.Now access?

- **From:** christian@wenz.org (Christian Wenz)
- **Date:** 2002-03-27T08:35:08-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<27938ff7.0203270835.6f36b50d@posting.google.com>`
- **References:** `<27938ff7.0203260742.f78d920@posting.google.com> <1f8o8.22$LI.217@castor.casema.net>`

```
Hi,

"ronald leenheer" <r.leenheer@wanadoo.nl> wrote in message news:<1f8o8.22$LI.217@castor.casema.net>...
> Why not the old fashioned way?
> 
…[9 more quoted lines elided]…
>         ACCEPT SYS-DATE  FROM DATE.

thanks, would work, yes, but it's a proof-of-concept, so I do want to
use the .NET framework classes (and may want to use others of them in
a similar way). Any ideas what I could do?

Regards
Christian
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
