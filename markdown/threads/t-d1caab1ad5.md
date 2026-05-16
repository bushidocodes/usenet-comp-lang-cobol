[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error Questions

_4 messages · 2 participants · 2000-09_

---

### Error Questions

- **From:** "GT" <gtroussel@nsbs.com>
- **Date:** 2000-09-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fXhw5.775$0j.470278@news.uswest.net>`

```
If I had a program on a network that ran on top of Cobol 6, what would I
look for when I'm getting error like "error code: 104", and "error code:
93,02." ?

TIA

GT
```

#### ↳ Re: Error Questions

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oNbBOSN8XrkIPyS5pKVWPbKEC4bn@4ax.com>`
- **References:** `<fXhw5.775$0j.470278@news.uswest.net>`

```
First of all you should start reading the users manual in section
RUNTIME MESSAGES.

Anyway error 104 is either a subscript error or a program that
tried to reference a linkage item that was not include in the
"USING" part of the call issued by the calling program, 
(and this includes the parameters in the command line).

Error 93,02 is file locked by another user (process).


FF

On Thu, 14 Sep 2000 22:48:18 -0700, "GT" <gtroussel@nsbs.com> wrote:

>If I had a program on a network that ran on top of Cobol 6, what would I
>look for when I'm getting error like "error code: 104", and "error code:
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Error Questions

- **From:** "GT" <gtroussel@nsbs.com>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g7rw5.70$Mn3.79061@news.uswest.net>`
- **References:** `<fXhw5.775$0j.470278@news.uswest.net> <oNbBOSN8XrkIPyS5pKVWPbKEC4bn@4ax.com>`

```
I appreciate your quick response to my question, thank you.  When you
explained the "104" error, I feel that I am still a little in the dark on
your answer, would you follow up with example possibly?  Thanks again!!

GT
"Frederico Fonseca" <frederico_fonseca@eudoramail.com> wrote in message
news:oNbBOSN8XrkIPyS5pKVWPbKEC4bn@4ax.com...
> First of all you should start reading the users manual in section
> RUNTIME MESSAGES.
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Error Questions

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2000-09-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PHbCOU08awjd93aDHhNEwlaxrDgO@4ax.com>`
- **References:** `<fXhw5.775$0j.470278@news.uswest.net> <oNbBOSN8XrkIPyS5pKVWPbKEC4bn@4ax.com> <g7rw5.70$Mn3.79061@news.uswest.net>`

```
On Fri, 15 Sep 2000 09:15:36 -0700, "GT" <gtroussel@nsbs.com> wrote:

>I appreciate your quick response to my question, thank you.  When you
>explained the "104" error, I feel that I am still a little in the dark on
>your answer, would you follow up with example possibly?  Thanks again!!
You are doing things the wrong way.

As per the following statement (yourï¿½s) you already had the error.

>> >If I had a program on a network that ran on top of Cobol 6, what would I
>> >look for when I'm getting error like "error code: 104", and "error code:
>> >93,02." ?

So you only have to tell US when and what you were doing at the time
it happened.

What I have told you should be enough for you to figure it out.
But just as another clue, and this for the 93,02 it can happen if you
have two instances of the same program running at the same time in the
same machine.

As for the 104.
Either you are starting the program with the wrong number (or type) of
parameters, or there is an "coding" error in one of the programs.
In either case you should speak with whoever coded the program.

FF
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
