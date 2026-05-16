[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# mf.. run a batch file (.bat) or or dos command inside colbol program without black screen appear

_3 messages · 3 participants · 2000-05_

---

### mf.. run a batch file (.bat) or or dos command inside colbol program without black screen appear

- **From:** trinh <trinhNOtrSPAM@aol.com.invalid>
- **Date:** 2000-05-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<00a8fdce.bcf230e6@usw-ex0104-028.remarq.com>`

```
i have micro focus netexpress cobol .. can anyone tell me how
can i run or execute a dos command or a batch file (.bat) inside
my cobol program without the black screen appear.

thanks. ... give example if u can.

* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network *
The fastest and easiest way to search and participate in Usenet - Free!
```

#### ↳ Re: mf.. run a batch file (.bat) or or dos command inside colbol program without black screen appear

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g4kf3$2b$1@news.inet.tele.dk>`
- **References:** `<00a8fdce.bcf230e6@usw-ex0104-028.remarq.com>`

```
The only way is CALL X'91' (function 35). Look in the NX documentation under
Library Routines.

I cannot promise you that it is done without 'flicker'.

Regards
Ib
trinh skrev i meddelelsen <00a8fdce.bcf230e6@usw-ex0104-028.remarq.com>...
>i have micro focus netexpress cobol .. can anyone tell me how
>can i run or execute a dos command or a batch file (.bat) inside
…[4 more quoted lines elided]…
>* Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
>The fastest and easiest way to search and participate in Usenet - Free!
>
```

#### ↳ Re: mf.. run a batch file (.bat) or or dos command inside colbol program without black screen appear

- **From:** "Randy Zimmerman" <rzmerant@execpc.com>
- **Date:** 2000-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3926978b$0$73585@news.execpc.com>`
- **References:** `<00a8fdce.bcf230e6@usw-ex0104-028.remarq.com>`

```
You need to call the "CreateProcessA" api for win32 (documented in the MSDN
sdk docs) if it is a 32bit program. If invoking a 16bit program you can call
the "WinExec" api (there is a sample of that in the MERANT websync site).

If you send a e-mail to me at rzmerant@execpc.com I will e-mail you back an
example since it is fairly complex.



"trinh" <trinhNOtrSPAM@aol.com.invalid> wrote in message
news:00a8fdce.bcf230e6@usw-ex0104-028.remarq.com...
> i have micro focus netexpress cobol .. can anyone tell me how
> can i run or execute a dos command or a batch file (.bat) inside
…[4 more quoted lines elided]…
> * Sent from RemarQ http://www.remarq.com The Internet's Discussion Network
*
> The fastest and easiest way to search and participate in Usenet - Free!
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
