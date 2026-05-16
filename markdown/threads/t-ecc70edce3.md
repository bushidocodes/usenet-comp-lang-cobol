[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using an XML File

_2 messages · 2 participants · 2006-03_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Using an XML File

- **From:** "Guillaume Lucazeau" <glucazeau@gmail.com>
- **Date:** 2006-03-24T03:36:17-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1143197878.580992.48710@v46g2000cwv.googlegroups.com>`

```
Hello,

I'm trying to parse an XML File with enterprise Cobol for z/OS

The code is ok, I'm using this example to handle events :
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/FRAMESET/igy3pg20/5.0

But I've got a problem :
if I have some new lines between roots tag and others tags, there is an
exception (code 2) at the execution

For example, exception with this :
<?xml version="1.0" encoding="ibm-1140" standalone="yes" ?>
<personnes>
   <personne><nom>Hauchon</nom><prenom>Paul</prenom></personne>
</personnes>

OK with this :
<?xml version="1.0" encoding="ibm-1140" standalone="yes" ?>
<personne><nom>Hauchon</nom><prenom>Paul</prenom></personne>

Does anybody know what's the problem ?

Is there a special File Definition to define an XML file ?

I have read a lot of documentation and a lot of messages in this group,
but I'm a newbie in Cobol, and I haven't found any answers

I would be great if someone could explain me how define an XML file :)
Thank you
```

#### ↳ Re: Using an XML File

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2006-03-24T08:02:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%4SUf.9959$ji6.579535@news20.bellglobal.com>`
- **References:** `<1143197878.580992.48710@v46g2000cwv.googlegroups.com>`

```
There is nothing special about the file definition, but you have to read the 
entire document into an array (or STRING it into a large PIC X field) before 
running it through XML PARSE.
"Guillaume Lucazeau" <glucazeau@gmail.com> wrote in message 
news:1143197878.580992.48710@v46g2000cwv.googlegroups.com...
> Hello,
>
…[28 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
