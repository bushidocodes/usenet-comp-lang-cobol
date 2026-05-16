[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFoucus Cobol and Microsoft Access

_3 messages · 3 participants · 1998-10_

---

### MicroFoucus Cobol and Microsoft Access

- **From:** jnickles@home.com
- **Date:** 1998-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70q2jm$d51$1@nnrp1.dejanews.com>`

```
Is there a way to connect to the data files stored by a MicroFocus Cobol
application from Microsoft Access?  How would I accomplish this?  Any help or
insight into this problem would be greatly appreciated.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: MicroFoucus Cobol and Microsoft Access

- **From:** "Sven Brueggemann" <Sven.Brueggemann@brem.ftn.de>
- **Date:** 1998-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00040aef@ftn.de>`
- **References:** `<70q2jm$d51$1@nnrp1.dejanews.com>`

```

j> Is there a way to connect to the data files stored by a MicroFocus
j> Cobol application from Microsoft Access?  How would I accomplish this?
j> Any help or insight into this problem would be greatly appreciated.

Do you have access to the file descriptions? If so, you can access the  
files via ODBC with Transoft's (www.transoft.com) U/SQL or Liant's  
(www.liant.com) Relational Data Bridge.

Best regards

Sven
```

#### ↳ Re: MicroFoucus Cobol and Microsoft Access

- **From:** "Karl Wagner" <kewagner@home.com>
- **Date:** 1998-10-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Mv0Y1.6524$s_4.1825748@news.rdc1.on.wave.home.com>`
- **References:** `<70q2jm$d51$1@nnrp1.dejanews.com>`

```
jnickles@home.com wrote in message <70q2jm$d51$1@nnrp1.dejanews.com>...
>Is there a way to connect to the data files stored by a MicroFocus Cobol
>application from Microsoft Access?  How would I accomplish this?  Any help
or
>insight into this problem would be greatly appreciated.
>
>-----------== Posted via Deja News, The Discussion Network ==----------
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own

Micro Focus has a package called OpenESQL which provides ODBC access to anMS
Access database, or via Microsoft's SQL Server product. It ships with
NetExpress and is optional extra with Workbench.

What doesn't ship with NetExpress (at least I haven't been able to find it)
is an XDB precompiler, which is strange given that Micro Focus owns XDB.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
