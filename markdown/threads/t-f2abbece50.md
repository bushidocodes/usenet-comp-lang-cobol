[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Deleting escape sequences from a string?

_4 messages · 4 participants · 2002-05_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Deleting escape sequences from a string?

- **From:** sjolund@iobox.com (Xedra Roland)
- **Date:** 2002-05-22T00:21:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d43e3ef.0205212321.5744f5dc@posting.google.com>`

```
Can you delete all the escape sequences from a string somehow?

We have these form-templates, that include those strange escape-things
(printer commands actually, for example ^[(s1B). Now, instead of
printing, the form can be sent via e-mail. Of course, the
escape-things show up in the mail too. Are the only solutions to
either check the whole string one character at a time or to make whole
new form-templates (which is not what I'd like to do)?

- Xedra
```

#### ↳ Re: Deleting escape sequences from a string?

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-05-22T09:01:12+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avjmeu871us0ktc0be3nqekqadveocct17@4ax.com>`
- **References:** `<4d43e3ef.0205212321.5744f5dc@posting.google.com>`

```
On 22 May 2002 00:21:19 -0700, sjolund@iobox.com (Xedra Roland) wrote:

>Can you delete all the escape sequences from a string somehow?
>
…[5 more quoted lines elided]…
>new form-templates (which is not what I'd like to do)?

As you do not wish to redesign, a good option would be to create a
"pdf" file and send this file instead (if doing this in windows/unix
it is easy enough)


FF
```

#### ↳ Re: Deleting escape sequences from a string?

- **From:** "JerryMouse" <nospam@invalid.com>
- **Date:** 2002-05-22T14:48:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6dOG8.102552$fU2.10398531@bin8.nnrp.aus1.giganews.com>`
- **References:** `<4d43e3ef.0205212321.5744f5dc@posting.google.com>`

```

"Xedra Roland" <sjolund@iobox.com> wrote in message
news:4d43e3ef.0205212321.5744f5dc@posting.google.com...
> Can you delete all the escape sequences from a string somehow?
>
…[5 more quoted lines elided]…
> new form-templates (which is not what I'd like to do)?

You have a print file with PCL commands (to set the margins, fonts, etc.).

The character displayed as "^" is really the ESC character X'1B'.

PCL strings are of indefinite length, but almost always start with the ESC
character and USUALLY end with an upper-case letter.

Anyway, to answer your question: You'll have to do it a character at a
time - but that's not hard; it's a four or five-line perform statement.
```

#### ↳ Re: Deleting escape sequences from a string?

- **From:** "Georgi Kozinakov" <gjokok@yahoo.com>
- **Date:** 2002-05-24T19:13:35+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cee7439@news.mt.net.mk>`
- **References:** `<4d43e3ef.0205212321.5744f5dc@posting.google.com>`

```
Xedra,

I had the similar problem with a LINE FEED character last month.
The procedure for removing it is the same like for ESC character:
In working-storage:
...
01 esc-ch pic 99 comp value 27.
01 esc-bug redefines esc-ch pic x.
01 space-ch pic x value " ".

in procedure division:
...
    PERFORM CHECK-LINES UNTIL ... (EOF or something)


CHECK-LINES.
    READ FILE AT END ... move 1 to eof.
    INSPECT LINE-OF-TEXT REPLACING ALL ESC-BUG BY SPACE-ch (or something
else)

HTH
Georgi

"Xedra Roland" <sjolund@iobox.com> wrote in message
news:4d43e3ef.0205212321.5744f5dc@posting.google.com...
> Can you delete all the escape sequences from a string somehow?
>
…[7 more quoted lines elided]…
> - Xedra
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
