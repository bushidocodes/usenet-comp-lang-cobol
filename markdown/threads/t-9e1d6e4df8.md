[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Unresolved external with MFC

_2 messages · 2 participants · 1999-03_

---

### Unresolved external with MFC

- **From:** Sudsy <pselby@ibm.net>
- **Date:** 1999-03-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36FC686E.96893C00@ibm.net>`

```
I'm using MicroFocus COBOL 4.0 on SCO OpenServer 5.0.4 and have run into

a problem. I've RTFM, checked the Merant web site, searched Yahoo and
Deja
News, but haven't seen my problem described. I apologize in advance if
this
question has already arisen and been answered, but here it is anyway.
Following the instructions in the manual for creating an executable from
a .cbl
file, I type 'cob -x pgmname.cbl -L /usr/lib'. The '-L /usr/lib' is
there since the
environment variable LD_LIBRARY_PATH is not being utilized. I get the
following message from ld:
    Unresolved symbol(s):
        _DYNAMIC
I'd be eternally grateful if someone could tell me how to resolve this
problem,
as all my attempts to date (using '-X _DYNAMIC', dummy functions, etc.)
have generated an executable which runs but fails on termination. You
can
either post here or send me e-mail at sudsy3333@geocities.com. Thanks in

advance for any assistance.
```

#### ↳ Re: Unresolved external with MFC

- **From:** jm.bain-cornu@silly.spam.sis-france.com (jean-michel)
- **Date:** 1999-03-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37007030.1015875@news.easynet.fr>`
- **References:** `<36FC686E.96893C00@ibm.net>`

```
On Sat, 27 Mar 1999 00:11:11 -0500, Sudsy <pselby@ibm.net> wrote:

>Following the instructions in the manual for creating an executable from
>a .cbl
>file, I type 'cob -x pgmname.cbl -L /usr/lib'. The '-L /usr/lib' is
Why do you need "-L /usr/lib" ?
Did you try without ? (I did not try with your version, but usually,
it's not needed, just -x)

:-) Please remove the silly spam from the address !
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
