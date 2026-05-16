[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# text file format

_6 messages · 5 participants · 2001-07_

---

### text file format

- **From:** "Ray Gurganus" <ray@<nospam>gurganus.org>
- **Date:** 2001-07-28T22:01:33-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g9K87.27$NC.18814@news.abs.net>`

```
I need to produce a text file to be imported into someone else's database,
and from the specs I have, it appears to be COBOL?  At least that's what it
looks like from some web searching I've done.

I list some of the stuff below, and I'm supposed to output a text file in
this format.  Could someone translate this into English for me?  Thanks.

fd  assrecdc
    record contains 823 characters
    value of filename    is assrecdc-fil
             library     is assrecdc-lib
             volume      is assrecdc-vol
    label records are standard.
01  assrecdc-record.
    05 as-key.
       07 as-caseno                    pic x(010).
    05 as-affiliate.
       07 as-a-name1                   pic x(025).
       07 as-a-name2                   pic x(025).
       07 as-a-addr1                   pic x(025).
       07 as-a-addr2                   pic x(025).
       07 as-a-csz                     pic x(025).
       07 as-a-phone                   pic x(025).
    05 as-affil redefines as-affiliate pic x(025) occurs 8.
    05 as-airport                      pic x(003).
    05 as-cityst                       pic x(028).
```

#### ↳ Re: text file format

- **From:** Ed Guy <ed_guy@paralynx.com>
- **Date:** 2001-07-28T19:56:31-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B637B5F.7C16@paralynx.com>`
- **References:** `<g9K87.27$NC.18814@news.abs.net>`

```
Ray Gurganus <ray@ wrote:
> 
> I need to produce a text file to be imported into someone else's database,
…[24 more quoted lines elided]…
>     05 as-cityst                       pic x(028).

Assuming that the field names are meaningful to you, these are just alphanumeric fields 
of the lengths in the pic x(XXX) bits. Consider the other lines like "sub headings" in 
the description.

You'll need to know exactly what the user wants for a label record and add this at the 
front and you won't want to write CR/LFs at the end of the line unless they ask you to.

Ignore the line with "redefines", it's just another view of the "as-affiliate" group but 
I'd ask why the redefines is 8 occurrences (in most other languages that's just called 
an 8 element array) when the bit being redefined is only 6.
```

#### ↳ Re: text file format

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-07-29T19:05:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_7Z87.5847$bl1.890520@newsread1.prod.itd.earthlink.net>`
- **References:** `<g9K87.27$NC.18814@news.abs.net>`

```

"Ray Gurganus gurganus.org

  Could someone translate this into English for me?  Thanks.

The neat thing about COBOL is that it IS in ENGLISH.

"Pic" is an abbreviation for PICTURE - the byte layout of the field;
"X" means alphanumeric; (nn) means repeat 'nn' times. What else do you
need?

I assume you have some data: with the data, the record layout, and the
above clues, you should be able to decode the data.

>
> fd  assrecdc
…[22 more quoted lines elided]…
>
```

#### ↳ Re: text file format

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2001-07-30T21:34:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9k555q$2lldi$1@ID-39920.news.dfncis.de>`
- **References:** `<g9K87.27$NC.18814@news.abs.net>`

```

Ray Gurganus gurganus.org> <ray@<nospam> wrote in message
news:g9K87.27$NC.18814@news.abs.net...
> I need to produce a text file to be imported into someone else's database,
> and from the specs I have, it appears to be COBOL?  At least that's what
it
> looks like from some web searching I've done.
>
…[22 more quoted lines elided]…
>

This layout doesn't even make sense.  The RECORD CONTAINS clause tells you
that the record created will be 823 bytes long.  The record layout, as
shown, is 191 bytes long (and includes an invalid redefinition).

As it sits though, you appear to have the following fields:

case number - 10 bytes
name 1 - 25 bytes
name 2 - 25 bytes
address line 1 - 25 bytes
address line 2 - 25 bytes
city/state/zip - 25 bytes
phone number - 25 bytes
airport code - 3 bytes
city/state (airport?) - 28 bytes

You should have the files, as well as the rest of the layout, to figure out
the rest...
```

#### ↳ Re: text file format

- **From:** "Ray Gurganus" <ray@--nospam--gurganus.org>
- **Date:** 2001-07-31T00:41:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QFq97.184$ia5.27574@news.abs.net>`
- **References:** `<g9K87.27$NC.18814@news.abs.net>`

```
Thanks, all.  The code that I posted is not complete, as I didn't want to
type it all in.  So this would account for the numbers not adding up.  So
I'll go with it and see what they say with what I generate....  Thanks again
```

##### ↳ ↳ Re: text file format

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2001-07-31T12:58:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B66ABAC.D866DA51@cusys.edu>`
- **References:** `<g9K87.27$NC.18814@news.abs.net> <QFq97.184$ia5.27574@news.abs.net>`

```


Ray Gurganus wrote:

> Thanks, all.  The code that I posted is not complete, as I didn't want to
> type it all in.  So this would account for the numbers not adding up.  So
> I'll go with it and see what they say with what I generate....  Thanks again

So what is your environment that you can't FTP the source code down to the PC so
you didn't need to type your source by hand?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
