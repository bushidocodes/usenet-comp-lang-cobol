[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How COPY statement is handled by COBOL complier

_5 messages · 4 participants · 1999-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Re: How COPY statement is handled by COBOL complier

- **From:** AnhMy Tran <anhmytran@hotmail.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s6hst5pd5k2122@corp.supernews.com>`
- **References:** `<83200k$gsv$1@nnrp1.deja.com>`

```

sujayg wrote:
> 
> 
…[3 more quoted lines elided]…
> REPLACING.


To my understanding, COPY is a statement that takes a single parameter
which is a variable name, not a file name. That makes sense to me.
When the compiler meets the statements, it inserts the proper variables
and their format into the exact codes.
```

#### ↳ Re: How COPY statement is handled by COBOL complier

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84b22k$hq$1@nntp9.atl.mindspring.net>`
- **References:** `<83200k$gsv$1@nnrp1.deja.com> <s6hst5pd5k2122@corp.supernews.com>`

```
AnhMy Tran <anhmytran@hotmail.com> wrote in message
news:s6hst5pd5k2122@corp.supernews.com...
>
> sujayg wrote:
…[15 more quoted lines elided]…
> http://www.help.com/

Just not true.  The names referenced in the COPY member are *not* variables
(although I think some compilers allow this as an extension).  Now how the
implementor "translates" a name in the COPY statement to a physical file is
implementor-defined. (For example, IBM mainframe compilers use the "of
library-name" to point to a DDName - other vendors allow you to automatically
add a ".cpy" or ".cbl" extension to the file-name) - but no Standard
conforming implementation treats these names as "variables" - when running in
Standard conforming mode.
```

#### ↳ Re: How COPY statement is handled by COBOL complier

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lxxa4.320$zp.4764@news3.mia>`
- **References:** `<83200k$gsv$1@nnrp1.deja.com> <s6hst5pd5k2122@corp.supernews.com>`

```
the COPY statement can be continued on multiple lines:  I've done
10 lines.  You MUST NOT break any words or text

AnhMy Tran <anhmytran@hotmail.com> wrote in message
news:s6hst5pd5k2122@corp.supernews.com...
>
> sujayg wrote:
…[15 more quoted lines elided]…
> http://www.help.com/
```

##### ↳ ↳ Re: How COPY statement is handled by COBOL complier

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84egck$ok4$1@nntp9.atl.mindspring.net>`
- **References:** `<83200k$gsv$1@nnrp1.deja.com> <s6hst5pd5k2122@corp.supernews.com> <Lxxa4.320$zp.4764@news3.mia>`

```
James King <mangogwr@bellsouth.net> wrote in message
news:Lxxa4.320$zp.4764@news3.mia...
> the COPY statement can be continued on multiple lines:  I've done
> 10 lines.  You MUST NOT break any words or text
>

Sorry, this is another incorrect statement.  The following is perfectly valid
in any ANSI'85 conforming compiler:

       Co
-         py   aMemb
-                 er of what
-                  ever Replacing  =="ABC
-                                                "def"==    b
-                                                             y a-COBOL-
-                                                                word .

Now, I am *NOT* recommending anyone to code ANY source statement like that -
but the (existing) Standard requires that a conforming implementation MUST
support such code.
```

###### ↳ ↳ ↳ Re: How COPY statement is handled by COBOL complier

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386B56E2.58759FE6@melbpc.org.au>`
- **References:** `<83200k$gsv$1@nnrp1.deja.com> <s6hst5pd5k2122@corp.supernews.com> <Lxxa4.320$zp.4764@news3.mia> <84egck$ok4$1@nntp9.atl.mindspring.net>`

```
Yes, the committee were even asked for a ruling on this and said
"Bill is Right". See Cobol Information Bulletin CIB-25,
clarification A-52. The example they considered was 

7   12
    C
-   O
-   P
-   Y text1. 

And another where text1 was continued.

Both were ruled valid.

Tim Josling

William M. Klein wrote:
> > 10 lines.  You MUST NOT break any words or text
> Sorry, this is another incorrect statement.  The following is perfectly valid
…[7 more quoted lines elided]…
> -                                                                word .
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
