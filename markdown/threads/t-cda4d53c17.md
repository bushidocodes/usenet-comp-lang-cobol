[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AcuCobol: Copy - Paste an marked string with key

_2 messages · 2 participants · 2001-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### AcuCobol: Copy - Paste an marked string with key

- **From:** "David Neidinger" <d.neidinger@muffenrohr.de>
- **Date:** 2001-04-12T09:41:49+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b3maj$o7t$03$1@news.t-online.com>`

```
Hello,

i have problems to put the copy - paste function to <strg>+<c> and
<strg>+<v>.

In the manual i found something but i it will not work.

it should work over "SET EXCEPTION".
Have anyone an example-code to put this function in my programm?

David Neidinger


----------------------------------------------------------------
Muffenrohr GmbH
Gï¿½terstr. 13
77833 Ottersweier

Tel.: 07223 2803-45
Fax.: 07223 2803-88
```

#### ↳ Re: AcuCobol: Copy - Paste an marked string with key

- **From:** "Erlend Moen" <erlend.moen@disys.no>
- **Date:** 2001-04-17T09:21:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9bgqsr$3eb$1@oslo-nntp.eunet.no>`
- **References:** `<9b3maj$o7t$03$1@news.t-online.com>`

```
David Neidinger <d.neidinger@muffenrohr.de> skrev i
news:9b3maj$o7t$03$1@news.t-online.com
>
> i have problems to put the copy - paste function to <strg>+<c> and
…[3 more quoted lines elided]…
>
The code looks like this in our system:

           SET     ENVIRONMENT      "KEYSTROKE" TO
                                    "Exception=31  ^C".
           SET     ENVIRONMENT      "KEYSTROKE" TO
                                    "Exception=32  ^V".
           SET     ENVIRONMENT      "KEYSTROKE" TO
                                    "Exception=33  ^X".
           SET     ENVIRONMENT      "KEYSTROKE" TO
                                    "Exception=34  ^Z".
           SET     EXCEPTION        31 TO COPY-SELECTION.
           SET     EXCEPTION        32 TO PASTE-SELECTION.
           SET     EXCEPTION        33 TO CUT-SELECTION.
           SET     EXCEPTION        34 TO UNDO.

The first four statements overrides the default exception-values because we
have already assigned for instance the F1-key to exception 3 - the same
value that Ctrl-C give us. Beside of that the four last statements is the
trick to make it work.

Good luck!

Erlend Moen
Norway
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
