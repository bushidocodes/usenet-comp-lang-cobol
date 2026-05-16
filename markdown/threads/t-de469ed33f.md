[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Html + Cobol

_3 messages · 3 participants · 2003-04 → 2003-05_

**Topics:** [`Web, XML, modern integration`](../topics.md#web)

---

### Html + Cobol

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-04-29T10:38:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2819276.1051612700@dbforums.com>`

```

Respected Gentlemen,

In MS-Windows I use a lot GAINED-FOCUS, SET-FOCUS
How is that procedure treated in Web?

Respectfully
Marcos Antonio de Souza
Brasil
```

#### ↳ Re: Html + Cobol

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-30T01:38:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3eae8078_1@127.0.0.1>`
- **References:** `<2819276.1051612700@dbforums.com>`

```

"mfcobol2002" <marcos_as@terra.com.br> wrote in message
news:2819276.1051612700@dbforums.com...
>
> Respected Gentlemen,
…[3 more quoted lines elided]…
>
GAINED-FOCUS is an EVENT
SET-FOCUS is an ACTION

Both can be achieved with JavaScript, VBScript, or ASP.

As far as I am aware, you can't do it with COBOL unless you manipulate the
DOM of the Web Page. That would mean using OO COBOL and OLE or COM. (I did
this on one occasion and decided that ASP and JavaScript were MUCH better
options...)

You COULD do it with COBOL if you generated the entire Web Page with CGI or
ASAPI code, but you would still need to generate ASP or one of the scripts
to interrogate the actual event and manipulate the properties of the field
where you want the focus.

COBOL is NOT the right tool for THIS job...

Pete.





----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

##### ↳ ↳ Re: Html + Cobol

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2003-05-01T11:42:28+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b8qten$n7r$1@hyperion.microfocus.com>`
- **References:** `<2819276.1051612700@dbforums.com> <3eae8078_1@127.0.0.1>`

```
And Net Express has the feature to create and edit these by right-clicking
on your control while in Form Designer.

www.microfocus.com

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3eae8078_1@127.0.0.1...
>
> "mfcobol2002" <marcos_as@terra.com.br> wrote in message
…[17 more quoted lines elided]…
> You COULD do it with COBOL if you generated the entire Web Page with CGI
or
> ASAPI code, but you would still need to generate ASP or one of the scripts
> to interrogate the actual event and manipulate the properties of the field
…[10 more quoted lines elided]…
> ----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet
News==----
> http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000
Newsgroups
> ---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption
=---
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
