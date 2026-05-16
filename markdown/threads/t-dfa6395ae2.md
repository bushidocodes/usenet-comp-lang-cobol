[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Net Express question.

_3 messages · 1 participant · 2003-05_

---

### Net Express question.

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-08T12:15:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jovua.11058$VJ.631345@news20.bellglobal.com>`

```
I am trying to read a tab delimited file under MF NetExpress.  How is the
best way to do it?  I wanted to read it using organization line sequential,
but that changes all my tabs to spaces.  Is there a way to turn this
"feature" off?

Donald
```

#### ↳ Re: Net Express question.

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2003-05-08T13:27:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b9e407$f5e$1@nntp2-cm.news.eni.net>`
- **References:** `<jovua.11058$VJ.631345@news20.bellglobal.com>`

```

"Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
news:jovua.11058$VJ.631345@news20.bellglobal.com...
> I am trying to read a tab delimited file under MF NetExpress.  How is the
> best way to do it?  I wanted to read it using organization line
sequential,
> but that changes all my tabs to spaces.  Is there a way to turn this
> "feature" off?
…[3 more quoted lines elided]…
>

See the NE help file for the following run time switches...This can also be
controlled on a file by file basis via the call x'91' function which is also
in the help file...

T - Tab Switch
 The tab switch is set off (-T) by default. The tab switch compresses extra
spaces to tab characters (x"09"), for line sequential files. This saves
space in the file. If you write a file with +T set, you must use +T when
reading the file and if you write a file with -T set, you must use -T when
reading the file.

N - Null Switch
 When +N is used (which is the default), all characters less than x"1B" are
preceded by a null byte (x"00"). If -N is used, characters less that x"1B"
are treated as control characters; for example, x"1A" is treated as the
end-of-file marker. If a file is created from an application running
with -N, the file must be read back with an application running the same
way; the same is true for files created from applications running with +N.
```

##### ↳ ↳ Re: Net Express question.

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-05-08T13:57:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5Uwua.4473$vS4.532325@news20.bellglobal.com>`
- **References:** `<jovua.11058$VJ.631345@news20.bellglobal.com> <b9e407$f5e$1@nntp2-cm.news.eni.net>`

```
"Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s> wrote in
message news:b9e407$f5e$1@nntp2-cm.news.eni.net...
>
> "Donald Tees" <Donald_Tees@sympatico.ca> wrote in message
> news:jovua.11058$VJ.631345@news20.bellglobal.com...
> > I am trying to read a tab delimited file under MF NetExpress.  How is
the
> > best way to do it?  I wanted to read it using organization line
> sequential,
…[7 more quoted lines elided]…
> See the NE help file for the following run time switches...This can also
be
> controlled on a file by file basis via the call x'91' function which is
also
> in the help file...
>
> T - Tab Switch
>  The tab switch is set off (-T) by default. The tab switch compresses
extra
> spaces to tab characters (x"09"), for line sequential files. This saves
> space in the file. If you write a file with +T set, you must use +T when
…[4 more quoted lines elided]…
>  When +N is used (which is the default), all characters less than x"1B"
are
> preceded by a null byte (x"00"). If -N is used, characters less that x"1B"
> are treated as control characters; for example, x"1A" is treated as the
…[5 more quoted lines elided]…
|Thanks, Ken.  I am doing this project online, over the net, and I am not
use to not having a full set of hardbound manuals.  I have some old versions
of MF here, I think I can find that in them.

Donald
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
