[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Making and printing barcode

_5 messages · 5 participants · 1998-04_

---

### Making and printing barcode

- **From:** "wim gelders" <ua-author-4864534@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<353DCB9F.4F4EE65C@glo.be>`

```

Our Company, ASP Software in Belgium, works with Micro Focus Cobol 3.2.

Is there anyone who knows how you could make a
barcode from a variable or file-field
and how you print one on a paper ?

I don't know if there are modules in Micro Focus Cobol 3.2
to do so.


Is there anyone who has experience with it ?

Tanx anyway
```

#### ↳ Re: Making and printing barcode

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1998-04-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b78f7ceb3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<353DCB9F.4F4EE65C@glo.be>`
- **References:** `<353DCB9F.4F4EE65C@glo.be>`

```

Wim,

Currently my company is using a different approach. We are using
Windows95 to print the bar code labels. In our Unix Cobol program, we
create an ASCII Comma delimited file with the info for the price tag.
Then in Win95 we are using a program called LabelRight. The user
clicks on an icon and the LabelRight program reads the ASCII file and
prints beautiful price tags on a laser printer.

Just thought I would offer another approach for you.

Paul

Wim Gelders wrote:

› Our Company, ASP Software in Belgium, works with Micro Focus Cobol 3.2.
› 
…[14 more quoted lines elided]…
›
```

#### ↳ Re: Making and printing barcode

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b78f7ceb3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<353DCB9F.4F4EE65C@glo.be>`
- **References:** `<353DCB9F.4F4EE65C@glo.be>`

```

Wim Gelders wrote:

› Our Company, ASP Software in Belgium, works with Micro Focus Cobol 3.2.
› 
…[5 more quoted lines elided]…
› to do so.

You can use the Flexus COBOL FormPrint product. All you need is a set
of True Type barcode fonts.

Contact our distribution agent, Easirun Software GmbH for more
information. You can download an evaluation version of FormPrint at:

http://www.flexus.com

You can also obtain the contact information for Easirun from our web
site.


›
›
…[6 more quoted lines elided]…
›

Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: Making and printing barcode

- **From:** "charles goodman" <ua-author-901347@usenetarchives.gap>
- **Date:** 1998-04-23T07:03:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b78f7ceb3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<353DCB9F.4F4EE65C@glo.be>`
- **References:** `<353DCB9F.4F4EE65C@glo.be>`

```

You have two more choices:

1. get a printer that has barcode fonts, write out approppriate escape
sequences.

2. get manual for your printer and write out appropriate escape
sequences to print dot patterns. You need technical knowledge of bar
code format.

I have written code for 2. for Epson and HP.
Have you got anything to trade? Waffles?

Wim Gelders wrote:
› 
› Our Company, ASP Software in Belgium, works with Micro Focus Cobol 3.2.
…[10 more quoted lines elided]…
› Tanx anyway
```

#### ↳ Re: Making and printing barcode

- **From:** "simon cordingley" <ua-author-6589258@usenetarchives.gap>
- **Date:** 1998-04-23T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b78f7ceb3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<353DCB9F.4F4EE65C@glo.be>`
- **References:** `<353DCB9F.4F4EE65C@glo.be>`

```

Yes, we have done using the product Fujitsu Form called from a Casegen COBOL
for Windows program compiled with Fujitsu.

I don't know if this product works with MF ? Ask Fujitsu at
www.adttools.com.

Simon Cordingley
si··.@cas··o.uk




Wim Gelders wrote in message <353··.@g··.be>...
› Our Company, ASP Software in Belgium, works with Micro Focus Cobol 3.2.
› 
…[14 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
