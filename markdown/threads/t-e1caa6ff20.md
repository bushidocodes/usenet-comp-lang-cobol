[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sample COBOL Program

_5 messages · 5 participants · 2002-05_

---

### Sample COBOL Program

- **From:** "News Netvisao" <alexandre.albino.2@netvisao.pt>
- **Date:** 2002-05-05T13:05:59+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1020600196.927637@newsfront2>`

```
Hi all... I'm from Portugal, my name is Alex and I'm new to the list...

I am starting to study the COBOL language. I've been developing in VB and
Delphi for some years now...
I have this request...(I think it's a modest one) Does anybody can provide
me with a sample COBOL program with the basic DB statments... (Insert,
Delete, Modify and Search) ? I've been searching for a sample demo like this
and can't seem to find one. I don't know any cobol programmers....so it
makes it diffucult to have such examples...


Thanks in advance,
Alex
```

#### ↳ Re: Sample COBOL Program

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-05-05T12:43:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EN9B8.2973$Ez1.206@nwrddc03.gnilink.net>`
- **References:** `<1020600196.927637@newsfront2>`

```
News Netvisao <alexandre.albino.2@netvisao.pt> wrote in message
news:1020600196.927637@newsfront2...
>
> I am starting to study the COBOL language. I've been developing in VB and
…[3 more quoted lines elided]…
> Delete, Modify and Search) ?

Unlike VB and Delphi, COBOL does not have any "database" functions beyond
OPEN, CLOSE, READ and WRITE. Inserts, Deletes, Modifies and Searches must be
constructed from combinations of these lower-level verbs.

That said, some COBOL compiler vendors do offer extensions to 'standard'
COBOL; however, the syntax for database access are specific to the brand
name of COBOL compiler.

There is one exception to this, however. Many vendors offer an "embedded
SQL" option; while the method for including this varies slightly from vendor
to vendor, the SQL language is common; and the syntax for embedding SQL
statments is also common:

EXEC SQL
    sql_statement
END-EXEC

Compilers which support embedded SQL do so by converting the 'EXEC SQL
sql_statement   END-EXEC' code blocks into 'standard' COBOL verbs (e.g.,
MOVE, CALL).

I'm pretty sure there are examples of this available on the Internet: do a
search on "+COBOL +embedded +SQL" using your faviorite search engine; and
check out the COBOL FAQ at http://www.cobolreport.com/faqs/cobolfaq.htm to
see if there is anything Bill Klein may have included in that document.

(Bill Klein:  if this question does not appear in the FAQ, it might be a
good addition)
```

#### ↳ Re: Sample COBOL Program

- **From:** Carlos Lages <clages@attglobal.net>
- **Date:** 2002-05-05T19:01:36-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CD5ABC0.3B99BB61@attglobal.net>`
- **References:** `<1020600196.927637@newsfront2>`

```
Alex, go to this site, its in Portuguese,  a lot of people from Brasil and
Portugal
are there.

Join us in the user cobol group

Carlos Lages
http://www.abpc.com.br/



News Netvisao gravada:

> Hi all... I'm from Portugal, my name is Alex and I'm new to the list...
>
…[9 more quoted lines elided]…
> Alex
```

#### ↳ Re: Sample COBOL Program

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-05-05T23:00:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CD5B93F.79EBA5AD@shaw.ca>`
- **References:** `<1020600196.927637@newsfront2>`

```


News Netvisao wrote:

> Hi all... I'm from Portugal, my name is Alex and I'm new to the list...
>
…[9 more quoted lines elided]…
> Alex

Surely can't be complete coincidence : -

"Alexandre (CaboVisao)" <alexandre.albino.2@netvisao.pt>,  and
"News Netvisao <alexandre.albino.2@netvisao.pt>"

In response to your private 'Thank you' - Did you get my message of  Sat, 04 May
2002 16:11:45 -0600 with the zipfile attachment,  particularly as you said you
already had a copy of N/E. But for a quickie, (assuming N/E V 3.1), go to ESQL
Assistant and select the various queries.

If language, (English) is a problem for you, please pass my samples on to the
Portuguese Newsgroup, which Carlos mentioned, for any additional help you may
need.

Jimmy, Calgary AB
```

#### ↳ Re: Sample COBOL Program

- **From:** jarl@mimer.com (Jarl Hermansson)
- **Date:** 2002-05-10T05:13:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2aaa8682.0205100413.74375485@posting.google.com>`
- **References:** `<1020600196.927637@newsfront2>`

```
"News Netvisao" <alexandre.albino.2@netvisao.pt> wrote in message news:<1020600196.927637@newsfront2>...
> Hi all... I'm from Portugal, my name is Alex and I'm new to the list...
> 
…[10 more quoted lines elided]…
> Alex

Hi Alex,

You can find a few (pretty simple) examples of embedded SQL in COBOL
at our site: http://developer.mimer.com/

Just do a search for COBOL and you'll find what you are looking for.


Regards,
Jarl
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
