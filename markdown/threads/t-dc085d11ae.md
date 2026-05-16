[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu 6.1 COPY support

_4 messages · 3 participants · 2002-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### Fujitsu 6.1 COPY support

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2002-11-20T12:09:17+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<arfqou$i6d$1@reader12.wxs.nl>`

```
When building one of my projects in Fujitsu COBOL 6.1 (RM/85 mode) I get the
following error message :

d:\project\copyfile\STROUTINES.PRD 204: JMN5525I-S  IDENTIFIER SPECIFIED
JUST AFTER INVOKE MUST BE OBJECT IDENTIFIER. INVOKE STATEMENT IS IGNORED.

The error points to a line in a copyfile where the following is coded :

033960 MELD                            SECTION.
033970*
033980 ME-00.
033990*
                  INVOKE POW-SELF "DisplayMessage"
                         USING    B-SCHAP
                          "Systeemmelding".
034030*
034040 ME-900.
034050*
034060     EXIT.

The same section I use in another project (without copyfiles however) and it
works fine there.

Any clou ?

Kind regards, Danny.
```

#### ↳ Re: Fujitsu 6.1 COPY support

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-11-20T07:57:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DDBB0D6.10907@Sympatico.ca>`
- **References:** `<arfqou$i6d$1@reader12.wxs.nl>`

```
The problem has nothing to do with "copy".  It has to do with the fact 
that the identifier specified
just after the invoke (clue ... that is the word POW-SELF) is not an 
object identifier. Maybe you
should ask the person whose code you copied.

Donald

Danny Maijer wrote:

>When building one of my projects in Fujitsu COBOL 6.1 (RM/85 mode) I get the
>following error message :
…[29 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Fujitsu 6.1 COPY support

- **From:** "Danny Maijer" <info@liveartists.com>
- **Date:** 2002-11-20T16:52:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<argbbq$gsv$1@reader12.wxs.nl>`
- **References:** `<arfqou$i6d$1@reader12.wxs.nl> <3DDBB0D6.10907@Sympatico.ca>`

```
I took the code out of the copyfile and copied it into the main program. Now
it does works. And by the way, the code was written by myself somewhere in
1988.......I am porting it to a GUI with the Fujitsu IDE.

Regards, Danny.

"Donald Tees" <Donald_Tees@Sympatico.ca> schreef in bericht
news:3DDBB0D6.10907@Sympatico.ca...
> The problem has nothing to do with "copy".  It has to do with the fact
> that the identifier specified
…[8 more quoted lines elided]…
> >When building one of my projects in Fujitsu COBOL 6.1 (RM/85 mode) I get
the
> >following error message :
> >
…[17 more quoted lines elided]…
> >The same section I use in another project (without copyfiles however) and
it
> >works fine there.
> >
…[9 more quoted lines elided]…
>
```

#### ↳ Re: Fujitsu 6.1 COPY support

- **From:** "R. Hendriks" <R.Hendriks_1@uvt.nl>
- **Date:** 2002-11-20T17:33:14+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<argdjv$nqe$1@mailnews.kub.nl>`
- **References:** `<arfqou$i6d$1@reader12.wxs.nl>`

```
Danny,

The POW-SELF object refers to the current form you're working on, and
apparently the compiler can't find this form. Are you using this code in
PowerCOBOL, or in COBOL97? The latter cannot work with the object POW-SELF.

One thing to remember is that PowerCOBOL uses a pre-compiler in which it
renames stuff like form-names, control-names etc. The COPY statement is
compiler after the pre-compiling by PowerCOBOL. Try using INCLUDE in stead
of COPY since the INCLUDE statement IS used by the pre-compiler.

Kind regads,

Rik Hendriks

"Danny Maijer" <info@liveartists.com> wrote in message
news:arfqou$i6d$1@reader12.wxs.nl...
> When building one of my projects in Fujitsu COBOL 6.1 (RM/85 mode) I get
the
> following error message :
>
…[17 more quoted lines elided]…
> The same section I use in another project (without copyfiles however) and
it
> works fine there.
>
…[6 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
