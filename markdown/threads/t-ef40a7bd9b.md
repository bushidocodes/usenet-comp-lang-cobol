[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Extract a piece of information from a txt file

_2 messages · 2 participants · 2004-06_

---

### Extract a piece of information from a txt file

- **From:** "TekSoft" <eute@sapo.pt>
- **Date:** 2004-06-18T18:07:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40d311f6$0$1777$a729d347@news.telepac.pt>`

```
Hi,
    I've a txt file with several lines with not fixed length and I use
PowerCobol v7.
    I want to extract a number between this character "@" and "\n" (carriage
return/line feed). For example:

4555599544455.455565@555555
59.214@1.184@60.398   >> this is it
1144@555555@58588888888888888@89898

and I want to extract this number "60.398" from the second line. I can I do
it?

Thanks
JM
Euromercante
```

#### ↳ Re: Extract a piece of information from a txt file

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-06-18T22:02:01+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<htl6d0tub0v4ickjc0andlu165274hmg3k@4ax.com>`
- **References:** `<40d311f6$0$1777$a729d347@news.telepac.pt>`

```
On Fri, 18 Jun 2004 18:07:00 +0100, "TekSoft" <eute@sapo.pt> wrote:

>Hi,
>    I've a txt file with several lines with not fixed length and I use
…[14 more quoted lines elided]…
>
Use the unstring statement with a delimiter of "@".

e.g.
unstring fieldx delimited by all "@"
into field1, field2, field3, field4

On the above case result would be

line 1
field1 4555599544455.455565
field2 555555

Line 2
field1 59.214@1.184
field2 60.398

Line 3
field1 1144
field2 555555
field3 58588888888888888
field4 89898




Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
