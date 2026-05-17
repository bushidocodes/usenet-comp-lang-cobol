[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pl/sql in pro*cobol

_3 messages · 2 participants · 1998-05_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Pl/sql in pro*cobol

- **From:** "martin meadows" <ua-author-13499763@usenetarchives.gap>
- **Date:** 1998-05-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3550FB12.45EB@indy.net>`

```

Hi,

I'm trying to compile the following pl/sql code inside a
pro*cobol program:

validate-emp-number.
exec sql execute
begin
select 'x' into :placeholder
from payroll_employee_master
where emp_# = :emp-number-o;
exception
when no_data_found then
:employee-number-flag := 0;
end;
end exec.

I've tried several variations of this but I consistently
get
"identifier 'payroll_employee_master' must be declared"
when I compile it.

What's the problem? It's had me hung up for a couple of
hours and I'm bummed ...

Thanks,
Martin Meadows
```

#### ↳ Re: Pl/sql in pro*cobol

- **From:** "steffen prietz" <ua-author-16631798@usenetarchives.gap>
- **Date:** 1998-05-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0d77f3c9bc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3550FB12.45EB@indy.net>`
- **References:** `<3550FB12.45EB@indy.net>`

```

I think you'r working with an Oracle DB. Then the advice maybe : create
a stored procedure an call this procedure from within your Cobol-Code
like this:

1st: Your real SQL-Code here:
create procedure validate-emp-number(emp-number-i in
payroll_employee_master.emp_number%type,

placeholder out payroll_employee_master.'x'%type,

errcode in out varchar2)
as
.....


2nd:Your Cobol-Code.
EXEC SQL
exec validate-emp-number(:Cob-Emp-number-i, :Cob-Placeholder,
:Cob-Errcode)
END-EXEC

Hop this helps.
Steffen Prietz



Martin Meadows wrote:

› Hi,
› 
…[24 more quoted lines elided]…
›    Martin Meadows
```

#### ↳ Re: Pl/sql in pro*cobol

- **From:** "martin meadows" <ua-author-13499763@usenetarchives.gap>
- **Date:** 1998-05-08T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0d77f3c9bc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3550FB12.45EB@indy.net>`
- **References:** `<3550FB12.45EB@indy.net>`

```

Seems like there's disagreement among the experts on this question and
it sure seems like the question is getting tougher.

I just created a very simple table called meadows while logged
in on my own account. I replaced payroll_employee_master with
meadows ... of which there is no doubt that I am the owner. I then
attempted, once again, to compile this thing. I got the same error
message (only with 'meadows' now instead of payroll_employee_master).
Is it still an ownership problem?

The full error message is:
end-exec.
^
........
pcc-s-0061: error at line 445, column 22, pls-201: identifier
'MEADOWS' must be declared
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
