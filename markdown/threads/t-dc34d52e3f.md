[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Prefixing 'autonumber'

_4 messages · 3 participants · 2008-06_

---

### Prefixing 'autonumber'

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2008-06-04T02:14:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e36ccb45-f69e-49a2-8843-1ae334fa2cb5@f24g2000prh.googlegroups.com>`

```
Got a MySQL data with an autonumbering format. Looking at the records
however, the autonumber has prefix.... example: ID4002, ID4003,
ID4003.

If I have to INSERT a record in Cobol as indicated below, how could I
add the prefix "ID" in customer-info-cust-code which is an autonumber
field?

EXEC SQL
 INSERT INTO customer_info_head
 (cust_code
 ,cust_lname
 ,cust_mname
 ,cust_fname
 ,cust_company
 ) VALUES
 (:customer-info-cust-code
 ,:customer-info-cust-lname
 ,:customer-info-cust-mname
 ,:customer-info-cust-fname
 ,:customer-info-cust-company
)
END-EXEC

The table "already" included this format... using direct SQL command.
```

#### ↳ Re: Prefixing 'autonumber'

- **From:** Zbikow <zbikow1@wp.pl>
- **Date:** 2008-06-04T04:47:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<792b86b6-6cbc-4955-b230-7d2024a588a6@m45g2000hsb.googlegroups.com>`
- **References:** `<e36ccb45-f69e-49a2-8843-1ae334fa2cb5@f24g2000prh.googlegroups.com>`

```
On 4 Cze, 11:14, Rene_Surop <infodynamics...@yahoo.com> wrote:
> Got a MySQL data with an autonumbering format. Looking at the records
> however, the autonumber has prefix.... example: ID4002, ID4003,
…[22 more quoted lines elided]…
> The table "already" included this format... using direct SQL command.

hmmm....

What is the definition for this "auto" field. Should be numeric. If so
how it can contain values like "ID*". If it is not numeric what do you
mean by calling it "autonumer"?
Can you send DDL for the table?

regards
Zbikow
```

#### ↳ Re: Prefixing 'autonumber'

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-06-04T07:47:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5aw1k.4053$co7.1113@nlpi066.nbdc.sbc.com>`
- **References:** `<e36ccb45-f69e-49a2-8843-1ae334fa2cb5@f24g2000prh.googlegroups.com>`

```
> If I have to INSERT a record in Cobol as indicated below, how could I
> add the prefix "ID" in customer-info-cust-code which is an autonumber
> field?

???

Autonumber means the DBMS will 'automatically' number it, you don't INSERT 
it yourself.

MCM
```

##### ↳ ↳ Re: Prefixing 'autonumber'

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2008-06-04T20:43:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c730b6c-bde6-4ab3-97c0-b1066667b7ee@f24g2000prh.googlegroups.com>`
- **References:** `<e36ccb45-f69e-49a2-8843-1ae334fa2cb5@f24g2000prh.googlegroups.com> <5aw1k.4053$co7.1113@nlpi066.nbdc.sbc.com>`

```
On Jun 4, 8:47 pm, "Michael Mattias" <mmatt...@talsystems.com> wrote:
> > If I have to INSERT a record in Cobol as indicated below, how could I
> > add the prefix "ID" in customer-info-cust-code which is an autonumber
…[7 more quoted lines elided]…
> MCM


My mistake, the field is NOT auto-increment (just viewed the data
design)... so the prefix is manipulated. Thanks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
