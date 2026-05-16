[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Program teminating at STOP RUN.

_2 messages · 2 participants · 1999-07_

---

### Program teminating at STOP RUN.

- **From:** Thomas Kolomaznik <kolomaznik@teleweb.at>
- **Date:** 1999-07-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379A1C04.E21C74B9@teleweb.at>`

```
Hi!

I'm using the MF Workbench 3.5 under MS-Dos and Betrieve as the
Database.
I've the problem that all programs work right when im running under
the animator of the workbench. When I'm running under dos i've the
problem that some programs terminate with the error message 
"Call parameter not suplied".
So I debugged the prog's and i found out that the parameters in 
the linkage section are supplied (under animator and dos) but the
program terminates before the exit programm and stop run statements
after the last statement of the program.
If you have any idea how to solve that problem or what can cause it
please mail me: onchoc@hotmail.com

Thanx a lot
Oncho
```

#### ↳ Re: Program teminating at STOP RUN.

- **From:** docdwarf@clark.net ()
- **Date:** 1999-07-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OeLm3.1375$Gu2.49659@iad-read.news.verio.net>`
- **References:** `<379A1C04.E21C74B9@teleweb.at>`

```
In article <379A1C04.E21C74B9@teleweb.at>,
Thomas Kolomaznik  <kolomaznik@teleweb.at> wrote:
>Hi!
>
…[11 more quoted lines elided]…
>please mail me: onchoc@hotmail.com

Post it here, read it here... try changing your STOP RUNs to GOBACKs.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
