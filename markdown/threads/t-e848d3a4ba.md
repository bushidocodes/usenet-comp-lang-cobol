[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL 2000

_6 messages · 4 participants · 2002-07 → 2002-08_

---

### COBOL 2000

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2002-07-29T22:43:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ryj19.44866$A35.6534710@twister.nyroc.rr.com>`

```
I haven't followed all the proposed COBOL2000 changes, (except that I like
EXIT PARAGRAPH), but I wondered if there were any changes to the COMPUTE
verb to improve clarity.

Consider filling a number of variables, VAR1 - VAR5:
MOVE                   VAR-A    TO                                  VAR1
SUBTRACT          VAR-B     FROM                            VAR2
ADD                      VAR-C     TO  VAR-D  GIVING    VAR3
ADD                       1             TO
VAR4
COMPUTE            VAR5   =    (VAR-D +  VAR-E)  /  2

Does anyone else think it would be clearer if you could code:

COMPUTE           (VAR-D +  VAR-E)  /  2   GIVING   VAR5
or
COMPUTE           (VAR-D +  VAR-E)  /  2   INTO        VAR5
or some other construct with the destination at the end, to match the other
constructs?
```

#### ↳ Re: COBOL 2000

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2002-07-29T22:48:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SCj19.44903$A35.6539570@twister.nyroc.rr.com>`
- **References:** `<ryj19.44866$A35.6534710@twister.nyroc.rr.com>`

```
Trying to fix the formatting for the VAR4 line

"William Bub" <fathafluff@hotmail.com> wrote in message
news:ryj19.44866$A35.6534710@twister.nyroc.rr.com...
> I haven't followed all the proposed COBOL2000 changes, (except that I like
> EXIT PARAGRAPH), but I wondered if there were any changes to the COMPUTE
…[5 more quoted lines elided]…
> ADD                      VAR-C     TO  VAR-D  GIVING    VAR3
   ADD                       1             TO
VAR4
> COMPUTE            VAR5   =    (VAR-D +  VAR-E)  /  2
>
…[5 more quoted lines elided]…
> or some other construct with the destination at the end, to match the
other
> constructs?
>
>
```

##### ↳ ↳ Re: COBOL 2000

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2002-07-29T22:49:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_Dj19.44915$A35.6540816@twister.nyroc.rr.com>`
- **References:** `<ryj19.44866$A35.6534710@twister.nyroc.rr.com> <SCj19.44903$A35.6539570@twister.nyroc.rr.com>`

```
I give up! VAR4 is supposed to be under VAR3.

"William Bub" <fathafluff@hotmail.com> wrote in message
news:SCj19.44903$A35.6539570@twister.nyroc.rr.com...
> Trying to fix the formatting for the VAR4 line
>
> "William Bub" <fathafluff@hotmail.com> wrote in message
> news:ryj19.44866$A35.6534710@twister.nyroc.rr.com...
> > I haven't followed all the proposed COBOL2000 changes, (except that I
like
> > EXIT PARAGRAPH), but I wondered if there were any changes to the COMPUTE
> > verb to improve clarity.
…[20 more quoted lines elided]…
>
```

##### ↳ ↳ Re: COBOL 2000

- **From:** "Ronald Leenheer" <r.leenheer@wanadoo.nl>
- **Date:** 2002-08-02T04:10:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KCn29.30$So4.1730@castor.casema.net>`
- **References:** `<ryj19.44866$A35.6534710@twister.nyroc.rr.com> <SCj19.44903$A35.6539570@twister.nyroc.rr.com>`

```
No clearer to me would be:

COMPUTE    VAR5  =    (VAR-D +  VAR-E)  /  2


Regards Ronald

"William Bub" <fathafluff@hotmail.com> schreef in bericht
news:SCj19.44903$A35.6539570@twister.nyroc.rr.com...
> Trying to fix the formatting for the VAR4 line
>
> "William Bub" <fathafluff@hotmail.com> wrote in message
> news:ryj19.44866$A35.6534710@twister.nyroc.rr.com...
> > I haven't followed all the proposed COBOL2000 changes, (except that I
like
> > EXIT PARAGRAPH), but I wondered if there were any changes to the COMPUTE
> > verb to improve clarity.
…[20 more quoted lines elided]…
>
```

#### ↳ Re: COBOL 2000

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-07-30T02:27:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VPm19.3258$cm.219049@bin3.nnrp.aus1.giganews.com>`
- **References:** `<ryj19.44866$A35.6534710@twister.nyroc.rr.com>`

```

"William Bub" <fathafluff@hotmail.com> wrote in message
news:ryj19.44866$A35.6534710@twister.nyroc.rr.com...

No. Your proposed construct doesn't look anything like FORTRAN.
```

#### ↳ Re: COBOL 2000

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-07-30T12:05:06+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D4672E2.5588668F@Azonic.co.nz>`
- **References:** `<ryj19.44866$A35.6534710@twister.nyroc.rr.com>`

```
William Bub wrote:

> Does anyone else think it would be clearer if you could code:

No.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
