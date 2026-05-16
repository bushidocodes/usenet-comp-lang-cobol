[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Metadata

_8 messages · 5 participants · 2000-03_

---

### Metadata

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PF83OBBw07z4Ewwn@ld50macca.demon.co.uk>`

```
I've seen you guys refering to Metadata (most recently in the thread
about adding support for csv files to Cobol compilers) but, please, what
is metadata?
```

#### ↳ Re: Metadata

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7GPz4.22430$Hq3.483524@news2.rdc1.on.home.com>`
- **References:** `<PF83OBBw07z4Ewwn@ld50macca.demon.co.uk>`

```
Metadata is data that defines the data. For example:

    Given:    MY-VAR        PIC 9(6)

    The metadata might be something like:
        field name = MY-VAR
        field length = 6
        field type = NUMERIC
        field usage = DISPLAY

In the context of a csv file, a common practice is to provide the names of
all the fields in the first row. The weakness of csv is that it fails to
provide any means of explaining the data type of each of the fields, the
delimiter, how embedded delimiters are to be handled, or any of that good
stuff. Rather it depends on both the sender and receiver agreeing on a set
of rules that are syncronized outside of the context of the data itself.
More robust transfer mechanisms embed information about the data within the
data itself.

Karl Wagner

"Alistair Maclean" <LD50Macca@ld50macca.demon.co.uk> wrote in message
news:PF83OBBw07z4Ewwn@ld50macca.demon.co.uk...
> I've seen you guys refering to Metadata (most recently in the thread
> about adding support for csv files to Cobol compilers) but, please, what
…[8 more quoted lines elided]…
> you find out how strong they are.
```

#### ↳ Re: Metadata

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#cbLBQqj$GA.265@cpmsnbbsa02>`
- **References:** `<PF83OBBw07z4Ewwn@ld50macca.demon.co.uk>`

```

Alistair Maclean <LD50Macca@ld50macca.demon.co.uk> wrote in message
news:PF83OBBw07z4Ewwn@ld50macca.demon.co.uk...
> I've seen you guys refering to Metadata (most recently in the thread
> about adding support for csv files to Cobol compilers) but, please, what
> is metadata?
> --
Metadata is data about the data.

A data dictionary is one form of metadata.

In mainframe DB2 the SYSIBM tables are a form of metadata.

Metadata, as well as data dictionaries, seems to be loosely defined.
Although there may be strict definitions, it appears that they are rarely
respected.
```

##### ↳ ↳ Re: Metadata

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S4XA4CA$a+z4EwhQ@ld50macca.demon.co.uk>`
- **References:** `<PF83OBBw07z4Ewwn@ld50macca.demon.co.uk> <#cbLBQqj$GA.265@cpmsnbbsa02>`

```
Thanks to all for the answers. I am illuminated (brightly lit?).
```

###### ↳ ↳ ↳ Re: Metadata

- **From:** "DennisHarley" <LegacyBlue@email.msn.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uNs6ffrj$GA.256@cpmsnbbsa04>`
- **References:** `<PF83OBBw07z4Ewwn@ld50macca.demon.co.uk> <#cbLBQqj$GA.265@cpmsnbbsa02> <S4XA4CA$a+z4EwhQ@ld50macca.demon.co.uk>`

```
Thanks, but I thought Karl Wagner gave a better answer.

Alistair Maclean <LD50Macca@ld50macca.demon.co.uk> wrote in message
news:S4XA4CA$a+z4EwhQ@ld50macca.demon.co.uk...
> Thanks to all for the answers. I am illuminated (brightly lit?).
> --
…[6 more quoted lines elided]…
> you find out how strong they are.
```

#### ↳ Re: Properties WAS Metadata

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38D004BE.38C6D0F9@home.com>`
- **References:** `<PF83OBBw07z4Ewwn@ld50macca.demon.co.uk>`

```


Alistair Maclean wrote:
> 
> I've seen you guys refering to Metadata (most recently in the thread
> about adding support for csv files to Cobol compilers) but, please, what
> is metadata?

Thanks, so you've given a definition on Metadata to Alistair, (and yours
truly). So let me ask another one, but which seems to be more closely
associated with Windowing.

Properties. I think I understand, but what does that word mean to you -
seems to me it is very closely linked to the word Metdata ????

Jimmy
```

##### ↳ ↳ Re: Properties WAS Metadata

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tbUz4.23314$Hq3.496805@news2.rdc1.on.home.com>`
- **References:** `<PF83OBBw07z4Ewwn@ld50macca.demon.co.uk> <38D004BE.38C6D0F9@home.com>`

```
Properties are a subset of metadata, since metadata encompasses every aspect
of data. Properties are the description of an attribute. Attributes are
aggregated into entities, and entities into databases. Databases can be
warehoused and so on....

In a nutshell, metadata describes a data set, including:
- what is in the data set    (properties are grouped in here somewhere)
- who produced the data set
- why the data set was created
- how the data set was created
- how reliable is the data set
- what outstanding problems remain in the data set
- how to retrieve the data set
- who wrote the metadata    (a bit recursive isn't)

Karl


"James J. Gavan" <jjgavan@home.com> wrote in message
news:38D004BE.38C6D0F9@home.com...
>
>
…[13 more quoted lines elided]…
> Jimmy
```

##### ↳ ↳ Re: Properties WAS Metadata

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-03-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38d060c5.609746177@news.cox-internet.com>`
- **References:** `<PF83OBBw07z4Ewwn@ld50macca.demon.co.uk> <38D004BE.38C6D0F9@home.com>`

```
On Wed, 15 Mar 2000 21:53:23 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[12 more quoted lines elided]…
>

Jimmy,

Do you have COBOL Unleashed?

Anyway, Properties are an OO thing!  They are the "values" of the data
items within your object.  Each one is a property of the object.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
