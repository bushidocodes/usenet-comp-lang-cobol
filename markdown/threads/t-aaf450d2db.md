[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing with AcuCOBOL

_3 messages · 2 participants · 1999-08 → 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Printing with AcuCOBOL

- **From:** "Robert Annandale" <rob _ a @ unipharm . com>
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cc29dd$0$20181@fountain.mindlink.net>`

```
I am trying to print a report using different fonts and appearances.
Lets say I have a variable

01 heading-1.
     05 filler          pic x(14) value "This is a test".

and I wish to print it to my printer in font 'Courier New'
size 14, bold and underlined.

How do I go about doing this?

I have AcuCOBOL 4.2

Regards,
----------------------------------------------------------------------------
----
Robert Annandale

e-mail address has been modified to thwart spam.
```

#### ↳ Re: Printing with AcuCOBOL

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LVWy3.9819$914.620160@typ11.nn.bcandid.com>`
- **References:** `<37cc29dd$0$20181@fountain.mindlink.net>`

```
You might need to look up the command sequence and insert the codes in what
you print;  there should be some documentation in your Printer User's Guide.
I added part of what might be needed in your example if you have a HP
LaserJet.  HTH

Robert Annandale > wrote in message
<37cc29dd$0$20181@fountain.mindlink.net>...
>I am trying to print a report using different fonts and appearances.
>Lets say I have a variable
>
>01 heading-1.
        05 filler          pic x value x"1b".
        05 filler          pic x(17) value "(s0p.14h0s3b4099T".
>     05 filler          pic x(14) value "This is a test".
>
…[3 more quoted lines elided]…
>I have AcuCOBOL 4.2
```

#### ↳ Re: Printing with AcuCOBOL

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qjfrj$oec$1@news.cerf.net>`
- **References:** `<37cc29dd$0$20181@fountain.mindlink.net>`

```
Robert Annandale > wrote in message
<37cc29dd$0$20181@fountain.mindlink.net>...
>I am trying to print a report using different fonts and appearances.
>Lets say I have a variable

I assume you are talking of printing using Windows.

If so:

    It is pretty much straight forward, have you looked at their
winspool.cbl sample program?

    Do that, and let me know if you still need help.

otherwise

    escape sequences... Prepare to read a manual :-)

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
