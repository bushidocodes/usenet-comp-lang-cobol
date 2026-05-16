[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PowerCobol and calling

_4 messages · 2 participants · 2000-05 → 2000-06_

---

### Re: PowerCobol and calling

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sVkX4.1542$ET3.258513@nnrp1.sbc.net>`
- **References:** `<8ga2dq$nvn$1@otis.netspace.net.au>`

```
In addition to RETURNING xxxx, you can define data as GLOBAL EXTERNAL
(in both the caller and called programs) and send a whole bunch of
stuff back and forth.

Kevin Kelly <kkelly@netspace.net.au> wrote in message
news:8ga2dq$nvn$1@otis.netspace.net.au...
> Does anyone know the correct syntax for calling another cobol
program from
> Fujitsu PowerCobol and then havine that program pass values back to
the
> PowerCobol window?
>
…[3 more quoted lines elided]…
>
```

#### ↳ Re: PowerCobol and calling

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gvers$ubn$1@slb6.atl.mindspring.net>`
- **References:** `<8ga2dq$nvn$1@otis.netspace.net.au> <sVkX4.1542$ET3.258513@nnrp1.sbc.net>`

```
GLOBAL is not needed (unless the CALLed program is a nested one)
```

##### ↳ ↳ Re: PowerCobol and calling

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VDtZ4.258$fE6.139649@nnrp1.sbc.net>`
- **References:** `<8ga2dq$nvn$1@otis.netspace.net.au> <sVkX4.1542$ET3.258513@nnrp1.sbc.net> <8gvers$ubn$1@slb6.atl.mindspring.net>`

```
GLOBAL is necessary if the called program is a DLL (which is the way I
read the original poster's question, although I now realize 'another
COBOL program' could, in fact, and probably is, a sub-program).

William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8gvers$ubn$1@slb6.atl.mindspring.net...
> GLOBAL is not needed (unless the CALLed program is a nested one)
>
…[5 more quoted lines elided]…
> > In addition to RETURNING xxxx, you can define data as GLOBAL
EXTERNAL
> > (in both the caller and called programs) and send a whole bunch of
> > stuff back and forth.
…[5 more quoted lines elided]…
> > > Fujitsu PowerCobol and then havine that program pass values back
to
> > the
> > > PowerCobol window?
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: PowerCobol and calling

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h5q0n$934$1@slb2.atl.mindspring.net>`
- **References:** `<8ga2dq$nvn$1@otis.netspace.net.au> <sVkX4.1542$ET3.258513@nnrp1.sbc.net> <8gvers$ubn$1@slb6.atl.mindspring.net> <VDtZ4.258$fE6.139649@nnrp1.sbc.net>`

```
"Huh?"

what does DLL have to do with GLOBAL?  The "GLOBAL" attribute in COBOL  is
*only* useful for nested programs.  Is there some implementation where this
isn't true?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
