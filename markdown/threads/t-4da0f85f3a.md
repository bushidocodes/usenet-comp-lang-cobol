[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (OT) need off-list help with MS Access (reports)

_2 messages · 2 participants · 2009-04_

---

### (OT) need off-list help with MS Access (reports)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-04-14T16:49:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xx7Fl.152922$UQ6.6748@en-nntp-03.dc1.easynews.com>`

```
I know that there are specific fora for asking questions about this, but I was 
wondering if any of the "usual CLC participants" might be relatively experienced 
using MS Access' report features and might be able to help me with some 
(beginners) questions?  If so, please send me a note off-list.

These are NOT "do your own homework" questions,but they are certainly 
"beginner's" questions that I *should* be able to answer on my own, but just 
haven't been able to (yet).
```

#### ↳ Re: (OT) need off-list help with MS Access (reports)

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-04-15T11:50:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74klpkF148ce3U1@mid.individual.net>`
- **References:** `<xx7Fl.152922$UQ6.6748@en-nntp-03.dc1.easynews.com>`

```
William M. Klein wrote:
> I know that there are specific fora for asking questions about this,
> but I was wondering if any of the "usual CLC participants" might be
…[5 more quoted lines elided]…
> but just haven't been able to (yet).

Bill,

I'd strongly recommend that you DON'T use Access Reports for anything except 
the most simple (temporary or interim) reporting, to solve an immediate 
problem, understanding that it will be replaced with a proper solution. 
(Yes, I know that "temporary solutions" often abide for decades; that's 
partly why I wouldn't advocate using it at all...).

The problems I see with it are:

1. It locks you in to Access and is not scalable.
2. It is limited in its capability and requires VBA knowledge if you want to 
do anythig remotely useful with it.

Generally, MS ACCESS works really well as a data repository for small 
(ish)/medium applications with less than 17 workstations sharing it. After 
that you should use SQL Server, or another RDBMS. Access gets in trouble 
when you start using it to develop Access applications for anything but the 
most trivial jobs. As a repository (being accessed by something else) it is 
excellent; as an application (using the built in facilities), not so good.

Many people find Crystal Reports to be an excellent tool... and it works 
against almost ANY RDB. There are demo versions available for free (or there 
used to be... haven't used it for a while and I have a licensed copy of 
version 8); I'm sure you could pick up a second hand copy very cheap.

SQL Server has a reporting capability which I haven't tried, but have heard 
very good things about. (SQL Server Express is free).

Open Source DBs like MySQL and PostgreSQL can use most third party reporting 
tools. I find StimulSoft is outstanding (partly because it integrates 
seamlessly with VS 2008, but mainly because it does provide a true WYSIWYG 
GUI interface where you can simply drag and drop report elements, and it is 
a bit less "complex" than Crystal.) I spent three days playing with 
StimulSoft and was pretty facile with it by the end of that time. It really 
is outstanding.

Having said all of the above, I'll be happy to help you off list.

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
