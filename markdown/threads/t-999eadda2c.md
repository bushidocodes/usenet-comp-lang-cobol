[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Acu: Right click in an entry-field

_4 messages · 2 participants · 2001-08_

---

### Acu: Right click in an entry-field

- **From:** "Erlend Moen" <erlend.moen@disystemer.no>
- **Date:** 2001-08-28T16:52:30+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mgb6r$jq1$1@stockholm.tele1europe.no>`

```
I have an entry-field that is initially read-only. However I would like to
detect if the user right-clicks in the field and thereby activate a
function.

I've tried to play with the mouse-flags without any luck. I've tried to play
with the KEYSTROKE-environment-variable. No matter what I do, the
copy/cut/paste/undo/select all-menu pops up when I right click. There must
be a way to solve this? Anyone?

Regards,

Erlend
```

#### ↳ Re: Acu: Right click in an entry-field

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 2001-08-28T23:13:52+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UX$KVIAgeBj7IwGg@rcav8r.demon.co.uk>`
- **References:** `<9mgb6r$jq1$1@stockholm.tele1europe.no>`

```
Hi Erlend,

The only thing you can do is declare your own right-click ('popup') menu 
for that entry field (use the POP-UP MENU phrase). You can then detect a 
menu selection in the normal way. Hope this helps!

Best regards

Nigel

In article <9mgb6r$jq1$1@stockholm.tele1europe.no>, Erlend Moen 
<erlend.moen@disystemer.no> writes
>I have an entry-field that is initially read-only. However I would like to
>detect if the user right-clicks in the field and thereby activate a
…[14 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Acu: Right click in an entry-field

- **From:** "Erlend Moen" <erlend.moen@disystemer.no>
- **Date:** 2001-08-30T07:49:53+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mkk55$g3b$1@stockholm.tele1europe.no>`
- **References:** `<9mgb6r$jq1$1@stockholm.tele1europe.no> <UX$KVIAgeBj7IwGg@rcav8r.demon.co.uk>`

```
"Nigel Eaton" <nigele@rcav8r.demon.co.uk> wrote in message
news:UX$KVIAgeBj7IwGg@rcav8r.demon.co.uk...
>
> The only thing you can do is declare your own right-click ('popup') menu
> for that entry field (use the POP-UP MENU phrase). You can then detect a
> menu selection in the normal way. Hope this helps!

Ok... that will help. Thanks, Nigel!

Erlend
```

###### ↳ ↳ ↳ Re: Acu: Right click in an entry-field

- **From:** Nigel Eaton <nigele@rcav8r.demon.co.uk>
- **Date:** 2001-08-30T10:27:27+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YG4ZhtA$bgj7Iw2R@rcav8r.demon.co.uk>`
- **References:** `<9mgb6r$jq1$1@stockholm.tele1europe.no> <UX$KVIAgeBj7IwGg@rcav8r.demon.co.uk> <9mkk55$g3b$1@stockholm.tele1europe.no>`

```
Actually, on reflection, there may be another approach. You could use 
(instead of an entry-field) a one row, one column grid control.

This will look and feel much like an entry-field but has the advantage 
of generating both MSG-GRID-RBUTTON-DOWN and MSG-GRID-RBUTTON-UP events.

It may introduce different "challenges" (I haven't actually tried this 
lately) but may give a more seamless appearance if you need it.

Best regards

Nigel





In article <9mkk55$g3b$1@stockholm.tele1europe.no>, Erlend Moen 
<erlend.moen@disystemer.no> writes
>"Nigel Eaton" <nigele@rcav8r.demon.co.uk> wrote in message
>news:UX$KVIAgeBj7IwGg@rcav8r.demon.co.uk...
…[12 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
