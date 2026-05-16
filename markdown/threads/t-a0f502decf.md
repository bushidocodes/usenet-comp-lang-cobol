[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Jackson Structured Programming

_3 messages · 2 participants · 2000-10 → 2000-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Jackson Structured Programming

- **From:** "mark.croft" <mark.croft@ic24.net>
- **Date:** 2000-10-26T07:56:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VzQJ5.7917$sZ2.26893@news1-hme0>`

```
Does this still happen in the world of COBOL?

I have used it quite a lot in the real world with complex reports with dbf &
c code. I was trained in JSP at college , and all of the course work with
the programming modules where based around JSP methodology.

Any tools available still? I remember using one in DOS , sorry can't
remember name?

Whats do other think about? I remember a lot of people didn't like using,
and found that design wasn't there cup of tea :)

Mark
```

#### ↳ Re: Jackson Structured Programming

- **From:** "Kjeld Paab���l Hansen" <paabol@12mail.dk>
- **Date:** 2000-10-28T02:11:13+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nUoK5.1809$262.166612@news010.worldonline.dk>`
- **References:** `<VzQJ5.7917$sZ2.26893@news1-hme0>`

```
When I started as a COBOL programmer some 13 years ago on a IBM mainframe
site, we still used JSP. A couple of years later we abandoned it completely.

The problem with JSP was that, although it forced some structure into your
programming, it was a precompiled language which generated ugly COBOL code,
with almost unrecognizable paragraph names and lots of go tos. After
precompilation an ordinary compilation generated object code which was
link-edited into executables, but during debugging you could only relate to
the precompiled COBOL source code, while you had to make corrections in the
JSP source. The JSP precompiler could generate structure charts of your
program, but given the limited graphics capabilities on output devices
(character graphics!), these charts often spanned 3-4 times as many pages as
the printed code, making them impossible to work with.

Now COBOL syntax let you make far more structured code than at that time,
thus making JSP obsolete.

Kjeld

mark.croft skrev i meddelelsen ...
>Does this still happen in the world of COBOL?
>
>I have used it quite a lot in the real world with complex reports with dbf
&
>c code. I was trained in JSP at college , and all of the course work with
>the programming modules where based around JSP methodology.
…[12 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Jackson Structured Programming

- **From:** "mark.croft" <mark.croft@ic24.net>
- **Date:** 2000-11-01T09:50:02
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RHRL5.3$yx.147@news1-hme0>`
- **References:** `<VzQJ5.7917$sZ2.26893@news1-hme0> <nUoK5.1809$262.166612@news010.worldonline.dk>`

```
interesting , I never really used a tool in anger in industry , the one I
used was at college.

I disagree that JSP is cause of the unstructurise of the code being made ,
its down to the tool. I found JSP a wonderful way of producing very neat
solutions. The time I have spent using JSP was doing it long hand with
penicl & paper. Converting the program structures into code with the need
for goto commands , backtracking does use this but even jackson stressed the
need to use the tech sparely.


Mark

Kjeld Paab�l Hansen <paabol@12mail.dk> wrote in message
news:nUoK5.1809$262.166612@news010.worldonline.dk...
> When I started as a COBOL programmer some 13 years ago on a IBM mainframe
> site, we still used JSP. A couple of years later we abandoned it
completely.
>
> The problem with JSP was that, although it forced some structure into your
> programming, it was a precompiled language which generated ugly COBOL
code,
> with almost unrecognizable paragraph names and lots of go tos. After
> precompilation an ordinary compilation generated object code which was
> link-edited into executables, but during debugging you could only relate
to
> the precompiled COBOL source code, while you had to make corrections in
the
> JSP source. The JSP precompiler could generate structure charts of your
> program, but given the limited graphics capabilities on output devices
> (character graphics!), these charts often spanned 3-4 times as many pages
as
> the printed code, making them impossible to work with.
>
…[8 more quoted lines elided]…
> >I have used it quite a lot in the real world with complex reports with
dbf
> &
> >c code. I was trained in JSP at college , and all of the course work with
…[15 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
