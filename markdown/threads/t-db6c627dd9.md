[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Oracle 7.3,sqlnet v 2.x, and realia cobol

_2 messages · 2 participants · 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Databases and SQL`](../topics.md#databases)

---

### Oracle 7.3,sqlnet v 2.x, and realia cobol

- **From:** "con..." <ua-author-17074216@usenetarchives.gap>
- **Date:** 1998-03-19T10:09:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ercc2$c54$1@nnrp1.dejanews.com>`

```

We are in the process of going to version 7.3 of oracle with sqlnet v 2.X.
We currently use realia cobol 4.221. I've been told by our DBA that
sqlpme and sqlspx cannot be invoked from sqlnet 2.x. He was told by Oracle
that we have to go to a 32-bit compiler. I've read some articles about Micro
Focus 4.0 and I see that Oracle will support Micro Focus under Oracle8 for NT.
We have over 200 programs written in Realia so I would like to migrate to
Realia Workbench 3.0, but I want to know if it's presently possible to
precompile Oracle programs using Workbench 3.0 and sqlnet 2.0. with Oracle
or Realia precompiler tools? If so, how since I currently have to invoke
sqlpme to precompile a program and invoke sqlspx to execute the program.

We are eventually going to an NT environment. I have many batch procedures
which execute one or more programs. Any comments/suggestion? Also can
Micro Focus read Realia Cobol Indexed files?


-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Oracle 7.3,sqlnet v 2.x, and realia cobol

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-db6c627dd9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6ercc2$c54$1@nnrp1.dejanews.com>`
- **References:** `<6ercc2$c54$1@nnrp1.dejanews.com>`

```

con··.@mai··i.us wrote:

› We are eventually going to an NT environment. I have many batch procedures
› which execute one or more programs. Any comments/suggestion? Also can
› Micro Focus read Realia Cobol Indexed files?

I can answer only the last query. No, Micro Focus cannot read Realia
files. You could use REALCOPY to create ASCII from them, then the Micro
Focus WFL to make them MF COBOL format.

CA-Realia is hostile to PC development with their WorkBench 3.0, and you
will not get technical support from them for using it to create PC
hosted applications. Tell them to change their minds on this stance
when you talk to them.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
