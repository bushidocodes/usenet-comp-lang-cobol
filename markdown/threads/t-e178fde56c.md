[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with REDEFINES error needed!

_8 messages · 5 participants · 2000-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### Help with REDEFINES error needed!

- **From:** Darek M <>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com>`

```
Hi, could anyone give me a pointer why the code below gives me the
mentioned  error? 


############################################
 10.85        01 UP-LIST.
 11.00            05 PIC X(16) VALUE '0000125599999915'.
 12.00            05 PIC X(16) VALUE '0023511238502399'.
 13.00            05 PIC X(16) VALUE '0099927599999914'.
 14.00            05 PIC X(16) VALUE '1086593299431599'.
 15.00            05 PIC X(16) VALUE '1086777499999925'.
 16.00            05 PIC X(16) VALUE '1089631940107513'.
 17.00            05 PIC X(16) VALUE '1222340932365099'.
 18.00            05 PIC X(16) VALUE '2333315831125510'.
 19.00            05 PIC X(16) VALUE '2387777335570099'.
 20.00            05 PIC X(16) VALUE '5427855542372507'.
 21.00            05 PIC X(16) VALUE '5551190099999911'.
 22.00            05 PIC X(16) VALUE '9836754940999900'.
 23.00        01 UP-TABLE REDEFINES UP-LIST.
 25.50             05 UP-LIST OCCURS 12 TIMES 
                                      ASCENDING KEY U-ID INDEXED BY I.
 26.00                10 U-ID PIC X(8).
 27.00                10 U-HOURS PIC 99.
 28.00                10 U-RATE PIC 99V99.
 29.0                  10 U-DED PIC V99.

 789 ==000023==> IGYSC2025-W "UP-TABLE" OR ONE OF ITS SUBORDINATES WAS
REFERENCED, BUT "UP-TABLE" WAS A "LINKAGE SECTION" ITEM THAT DID NOT
HAVE ADDRESSABILITY.  THIS REFERENCE WILL NOT BE RESOLVED SUCCESSFULLY
AT EXECUTION.
###########################################

The table will be then searched with SEARCH ALL if that is any help or
to give you an idea of the program.

Thank you for any responses.
```

#### ↳ Re: Help with REDEFINES error needed!

- **From:** "mangogwr" <mangogwr@bellsouth.net>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v%FT4.485$d36.122235@news1.mco>`
- **References:** `<uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com>`

```
The Compiler msg says 'WAS A LINKAGE-SECTION' Item and
did not have addressality.  That means you have coded

LINKAGE SECTION.
01 UP-LIST.

PROCEDURE DIVISION.

Whereas you should have coded:
PROCEDURE DIVISION using UP-LIST.

ANything in the 'LINKAGE' SECTION is OUTSIDE of your CODE.
Therefore the COMPILER knows this and has warned you that since you
didn't Code PROCEDURE DIVISION USING UP-LIST, it has no address to
associate with the Name.



<Darek M> wrote in message news:uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com...
> Hi, could anyone give me a pointer why the code below gives me the
> mentioned  error?
…[33 more quoted lines elided]…
> Thank you for any responses.
```

##### ↳ ↳ Re: Help with REDEFINES error needed!

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-05-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SnIT4.651$%g1.13022@news.swbell.net>`
- **References:** `<uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com> <v%FT4.485$d36.122235@news1.mco>`

```

mangogwr <mangogwr@bellsouth.net> wrote in message
news:v%FT4.485$d36.122235@news1.mco...
> The Compiler msg says 'WAS A LINKAGE-SECTION' Item and
> did not have addressality.  That means you have coded
…[14 more quoted lines elided]…
>
Not only that, but if the item is, in fact, a LINKAGE SECTION item,
VALUE statements are not permitted.
```

###### ↳ ↳ ↳ Re: Help with REDEFINES error needed!

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3920C6BF.4887E9DE@worldnet.att.net>`
- **References:** `<uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com> <v%FT4.485$d36.122235@news1.mco> <SnIT4.651$%g1.13022@news.swbell.net>`

```
Jerry P wrote:

> mangogwr <mangogwr@bellsouth.net> wrote in message
> news:v%FT4.485$d36.122235@news1.mco...
…[18 more quoted lines elided]…
> VALUE statements are not permitted.

Should this table be in Working Storage instead of the Linkage Section?

HTH,
Bill Lynch
```

###### ↳ ↳ ↳ Re: Help with REDEFINES error needed!

_(reply depth: 4)_

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zuoU4.918$Lj2.17060@news.swbell.net>`
- **References:** `<uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com> <v%FT4.485$d36.122235@news1.mco> <SnIT4.651$%g1.13022@news.swbell.net> <3920C6BF.4887E9DE@worldnet.att.net>`

```

William Lynch <wblynch@worldnet.att.net

> > >
> > Not only that, but if the item is, in fact, a LINKAGE SECTION
item,
> > VALUE statements are not permitted.
>
> Should this table be in Working Storage instead of the Linkage
Section?

Usually. Storage space (and definitions) are defined in the calling
program. The Linkage Section is used by the called program to locate
where the passed data are in memory and assign attributes to these
data. So, it normally works out as:
----
PROGRAM-ID. CALLER.
....
WORKING-STORAGE SECTION.
01  PASS-PARAMS.
   02  PASS-2  VALUE 'A'  PIC X.
   02  etc.

PROCEDURE DIVISION.
...
     CALL 'SUBPGM' USING PASS-PARAMS.

------
PROGRAM-ID. SUBPROG.

LINKAGE SECTION.
01  LINK-PASS.
    02  LINK-PASS-2    PIC X.
    02  etc.

PROCEDURE DIVISION USING LINK-PASS.

-------

Now since LINK-PASS is but a redefinition of PASS-PARMS, the VALUE
clause does not make sense (nor is it permitted) in the LINKAGE
SECTION. At the trivial level, you may be assigning different values
to the same memory location.
```

###### ↳ ↳ ↳ Re: Help with REDEFINES error needed!

_(reply depth: 5)_

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3922B5AD.63F22E90@worldnet.att.net>`
- **References:** `<uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com> <v%FT4.485$d36.122235@news1.mco> <SnIT4.651$%g1.13022@news.swbell.net> <3920C6BF.4887E9DE@worldnet.att.net> <zuoU4.918$Lj2.17060@news.swbell.net>`

```
Jerry P wrote:
> 
> William Lynch <wblynch@worldnet.att.net
…[12 more quoted lines elided]…
> data. 

Of course, but I don't remember seeing anything about this program being
called. If it is, he needs the USING on a Linkage Section item.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Help with REDEFINES error needed!

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gtvlr$pjn$1@slb6.atl.mindspring.net>`
- **References:** `<uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com> <v%FT4.485$d36.122235@news1.mco> <SnIT4.651$%g1.13022@news.swbell.net>`

```
FYI,
  As the message was an IGY-one, this was an IBM compiler. They (like the
next revision of COBOL) *do* allow VALUE clauses in Linkage Section.
HOWEVER, they are ignored - so this is probably NOT what the programmer
really wanted to do.

FYI2,
  The reason for allowing such VALUE clauses (which might seem to be
"useless") is to support COPY statements - that are shared between WS and
Linkage.  They will actually be "useful" in the next Standard when you can
(finally) do an INITIALIZE TO VALUE statement.
```

#### ↳ Re: Help with REDEFINES error needed!

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92ST4.46$xM5.25394@dfiatx1-snr1.gtei.net>`
- **References:** `<uhUfOc82pUQxsMAcZboDllDN1lxy@4ax.com>`

```
I don't understand the LINKAGE problem, but you have the dataname UP-LIST
defined twice, differently.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
