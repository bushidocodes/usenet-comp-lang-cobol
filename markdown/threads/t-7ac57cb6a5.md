[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Developing with graphic and character screens with MF

_2 messages · 2 participants · 1998-09_

---

### Developing with graphic and character screens with MF

- **From:** "Euromercante" <EUROMERCANTE@MAIL.TELEPAC.PT>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdd7e6$ec584660$LocalHost@p200>`

```

Our development with Netexpress and Dialog System (V2),  under Windows98/NT
has graphic and character screens.

The main screen is graphic, and when we call a second screen witch is
character, the screen appears,
but with no "Focus". We need to click with mouse to get it active. When
second screen is graphic, it
works ok.

Other problem is how can i control the caracter windows, because until  the
moment i call a character screen
program, and when i exit, this character window continue maximized.

Can i have controle to minimize/maximize  or close this kind of window?


Many Thanks
EP
```

#### ↳ Re: Developing with graphic and character screens with MF

- **From:** "Gael Wilson" <gw@mfltd.co.uk>
- **Date:** 1998-09-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdd817$2ca266d0$905481c1@gw-nt>`
- **References:** `<01bdd7e6$ec584660$LocalHost@p200>`

```
You can obtain the window handle for the text window by calling
PC_WIN_HANDLE. Once it has been obtained you can call the ShowWindow API to
set focus or maximize/minimize. However, you should not attempt to close
the window because that will cause the run-time to execute a STOP RUN.

Euromercante <EUROMERCANTE@MAIL.TELEPAC.PT> wrote in article
<01bdd7e6$ec584660$LocalHost@p200>...
> 
> Our development with Netexpress and Dialog System (V2),  under
Windows98/NT
> has graphic and character screens.
> 
…[6 more quoted lines elided]…
> Other problem is how can i control the caracter windows, because until 
the
> moment i call a character screen
> program, and when i exit, this character window continue maximized.
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
