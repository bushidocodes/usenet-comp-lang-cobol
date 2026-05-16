[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Power x MS-SQL

_6 messages · 4 participants · 2003-07_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Power x MS-SQL

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-07-21T22:54:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3136193.1058828090@dbforums.com>`

```

hi, How I define a date field as Host variable to be used
with MS-SQL

In Power Manual i only find out
Decimal, Char, Vchar, etc but nothing about DATE

any help will be apreciated

Tks
Carlos Lages
```

#### ↳ Re: Power x MS-SQL

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-21T19:29:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vhp1c2lqa4jt5a@corp.supernews.com>`
- **In-Reply-To:** `<3136193.1058828090@dbforums.com>`
- **References:** `<3136193.1058828090@dbforums.com>`

```
Carlos lages wrote:

> hi, How I define a date field as Host variable to be used
> with MS-SQL
> 
> In Power Manual i only find out
> Decimal, Char, Vchar, etc but nothing about DATE

If it's similar to other dates I've encountered, it'll be a Pic X(10), 
in the format CCYY-MM-DD.
```

##### ↳ ↳ Re: Power x MS-SQL

- **From:** pvieira@emporsoft.pt (Paulo Vieira)
- **Date:** 2003-07-22T04:29:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b5b8d7c7.0307220329.202e349@posting.google.com>`
- **References:** `<3136193.1058828090@dbforums.com> <vhp1c2lqa4jt5a@corp.supernews.com>`

```
LX-i <LXi0007@Netscape.net> wrote in message news:<vhp1c2lqa4jt5a@corp.supernews.com>...
> Carlos lages wrote:
> 
…[19 more quoted lines elided]…
> ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Olï¿½ Carlos,
Primeiro, obrigado pelo cï¿½digo que me enviou.
Acerca da questï¿½o que coloca, eu defino sempre os campos "data" como
PIC X(23) o que permite acomodar uma data no formato 'AAAA-MM-DD
HH:mm.sss.ccc'. Embora MS SQL Server guarde as datas sob o nome
DateTime ou SamllDateTime que sï¿½o inteiros e representam o nï¿½mero de
"ticks" que passaram desde uma data base (1 de Janeiro de 1584 ou 1900
dependendo do tipo de coluna), nunca percebi qual a relaï¿½ï¿½o que
existia entre estes inteiros e os dados pelas funï¿½ï¿½es "data" do COBOL.
Por isso limito-me a passar as datas como caractere e assegurar-me que
o "parser" da base de dados conhece o formato em que lhe sï¿½o enviadas.

Now in English:
Hi Carlos,
First, thank you for the code you sent.
As to your question, I always define date fields as PIC X(23) which
can acommodate a date in the format 'YYYY-MM-DD hh:mm:ss.ccc'.
Although MS SQL Server stores dates as DateTime or SmallDateTime which
are integers and represent the amout of ticks elapsed since a given
base date, it wasn't clear to me how those integers related to the
COBOL date functions, so I simply pass them as char data and in the
stored procedure make shure that the format is well understood by the
parser. For example:

CREATE PROCEDURE dbo.something
@char_dt char(23)
AS                                     
set dateformat ymd 
declare @w_dt  datetime
set @w_dt=@char_dt
INSERT ...

Cumprimentos
best regards

Paulo Vieira, Emporsoft
```

#### ↳ Re: Power x MS-SQL

- **From:** gmspano <member9303@dbforums.com>
- **Date:** 2003-07-24T22:59:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3150312.1059087568@dbforums.com>`
- **References:** `<3136193.1058828090@dbforums.com>`

```

Hi Carlos

If you have an User name and password to access Fujitsu Service Wise,
you can look at this link:

]http://software.fsw.fujitsu.com/FS/TxSwDownload/e2f302d7e2f302dce2-
f302dde2f302ca/H00004.htm[/url]

There are some explanations about the date and Sql.

Hope in this help

Gianni
```

##### ↳ ↳ Re: Power x MS-SQL

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-07-28T01:44:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3154922.1059356674@dbforums.com>`
- **References:** `<3150312.1059087568@dbforums.com>`

```

Gianni
I dont

Carlos Lages
```

##### ↳ ↳ Re: Power x MS-SQL

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-07-28T01:59:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3154925.1059357563@dbforums.com>`
- **References:** `<3150312.1059087568@dbforums.com>`

```

Tks
Gianni

I got the Information

Carlos Lages
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
