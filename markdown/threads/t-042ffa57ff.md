[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help: Need to get COBOL alphanumeric (binary) data into SQL Server 7.0

_2 messages · 2 participants · 2000-09_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Help: Need to get COBOL alphanumeric (binary) data into SQL Server 7.0

- **From:** chipling@hotmail.com
- **Date:** 2000-09-18T00:00:00
- **Newsgroups:** microsoft.public.sqlserver.programming,comp.lang.cobol,microsoft.public.sqlserver.migration
- **Message-ID:** `<39C68BF7.9409FCF3@hotmail.com>`
- **References:** `<39B02C31.55640E2A@eaglesoft.com>`

```
Jeff,

Different vendor using different way to store their binary data. Two things you
need to know before you can directly load your data to SQL server.

First is to identify the data definition on the COBOL program for that particular
field. I suspect it will be something like PIC 9(?)V99 COMP.

Second, you need to contact the cobol compiler company (or read thru their manual)
and find out how they convert that numeric data to binary form.

Rgds,
Chip Ling

P.S. If your COBOL program can directly read in the data, why not using the same
data definition in COBOL and write out a text file and use that file to import to
the SQL server.

Jeff Burris wrote:

> Hi,
>     I have a flat file that I read into a COBOL structure.  I want to write
…[18 more quoted lines elided]…
> EAGLE Software, Inc.                    Salina, Kansas, USA
```

#### ↳ Help: Need to get COBOL alphanumeric (binary) data into SQL Server 7.0

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 2000-09-19T00:00:00
- **Newsgroups:** microsoft.public.sqlserver.programming,comp.lang.cobol,microsoft.public.sqlserver.migration
- **Message-ID:** `<v2vtOUAtOzx5Iw7z@rcav8r.demon.co.uk>`
- **References:** `<39B02C31.55640E2A@eaglesoft.com> <39C68BF7.9409FCF3@hotmail.com>`

```
>>   How does one get binary data into SQL using AcuCOBOL and SQL
>Server 7.0?
>> All help is appreciated.
>>

Jeff,

You could write the data directly from your Acucobol-GT program into the 
database if that would be easier. This can be achieved in one of two 
ways. Either through the use of embedded SQL, or by the use of Acu4GL 
which would allow you to use standard COBOL I/O syntax (WRITE, etc.) to 
update the SQL Server table.

Other than that I'm afraid I'm not sure what's causing your problem.

Feel free to contact me at <neaton@acucorp.com> (don't reply to this 
email please, it's my home account and doesn't get checked all that 
often). I'll try to put you in touch with the appropriate person.

Best regards

Nigel
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
