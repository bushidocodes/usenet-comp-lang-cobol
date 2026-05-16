[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# how to avoid Abend D37 during close

_3 messages · 3 participants · 2004-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### how to avoid Abend D37 during close

- **From:** Juergen Spiekermann <Juergen.Spiekermann@t-online.de>
- **Date:** 2004-08-23T19:01:50+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cgd7tv$qj1$1@news.sdm.de>`

```
Hello,
I have the following problem on VSII COBOL on OS390.

When writing a sequential file (BLKSIZE=0,RECFM=FB,LRECL=80) it happens 
that the close statement causes an abend D37 due to limited space 
defined in th DD-Statement in the JCL.

Whereas evaluating the FILE STATUS after the WRITE statement works well 
it does not work when closing. It seems that the last write statement 
(to the buffer) works well, but the close statement afterwards causes 
the abend (probably when physically writing the pending data).

Is there any way to avoid this abend?

Greetings Juergen
```

#### ↳ Re: how to avoid Abend D37 during close

- **From:** "x.ray" <pasbon@noos.fr>
- **Date:** 2004-08-23T19:59:11+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<412a3087$0$20503$79c14f64@nan-newsreader-04.noos.net>`
- **References:** `<cgd7tv$qj1$1@news.sdm.de>`

```

"Juergen Spiekermann" <Juergen.Spiekermann@t-online.de> a ï¿½crit dans le
message de news:cgd7tv$qj1$1@news.sdm.de...
> Hello,
> I have the following problem on VSII COBOL on OS390.
…[3 more quoted lines elided]…
> defined in th DD-Statement in the JCL.

and what about the SPACE STATEMENT : SPACE=(CYL,(10,2)),DISP=(NEW,
CATLG,DELETE)
```

#### ↳ Re: how to avoid Abend D37 during close

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-08-24T00:43:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sl3li0l5vd1p34aja48312cvp75ltkl6uq@4ax.com>`
- **References:** `<cgd7tv$qj1$1@news.sdm.de>`

```
On Mon, 23 Aug 2004 19:01:50 +0200, Juergen Spiekermann
<Juergen.Spiekermann@t-online.de> wrote:

>Hello,
>I have the following problem on VSII COBOL on OS390.
…[10 more quoted lines elided]…
>Is there any way to avoid this abend?

Delete the SPACE clause, let ACS manage space .. assuming you have
SMS.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
