[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Printing a rectangle -help

_4 messages · 2 participants · 2000-05 → 2000-06_

---

### Printing a rectangle -help

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2000-05-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gk2me$mut$1@duke.telepac.pt>`

```
Have anyone made a program  using the Api of the windows to make rectangle
in the printer? I have try many times somethinh like above but without
sucess.
I apreciate any help. Thanks
Raimundo Carvalho

      *    CALL WINAPI32 "Rectangle"        USING
      *                                 printer-handle
      *                        by value box-te
      *                        by value box-td
      *                        by value box-be
      *                        by value box-bd
      *      end-call.
```

#### ↳ Re: Printing a rectangle -help

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gm8ui$l44$1@news.cerf.net>`
- **References:** `<8gk2me$mut$1@duke.telepac.pt>`

```
"Raimundo Carvalho" <ray@mail.telepac.pt> wrote in message
news:8gk2me$mut$1@duke.telepac.pt...
> Have anyone made a program  using the Api of the windows to make rectangle
> in the printer? I have try many times somethinh like above but without
…[10 more quoted lines elided]…
>       *      end-call.

You don't say much about what is the problem. Your sample looks okay, a few
questions though:
Have you assigned a pen to printer, have you assigned a brush? Have you
called StartDoc and BeginPage functions?

I assume you use valid values for all the parameters.

May you say precisely what happens?

Cheesle
```

##### ↳ ↳ Re: Printing a rectangle -help

- **From:** "Raimundo Carvalho" <ray@mail.telepac.pt>
- **Date:** 2000-06-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h6a0d$p43$1@duke.telepac.pt>`
- **References:** `<8gk2me$mut$1@duke.telepac.pt> <8gm8ui$l44$1@news.cerf.net>`

```
No i did not. How can i do it?
Thanks
Raimundo Carvalho


Cheesle <cheesle@online.NoSpamPlease.no> wrote in message
news:8gm8ui$l44$1@news.cerf.net...
> "Raimundo Carvalho" <ray@mail.telepac.pt> wrote in message
> news:8gk2me$mut$1@duke.telepac.pt...
> > Have anyone made a program  using the Api of the windows to make
rectangle
> > in the printer? I have try many times somethinh like above but without
> > sucess.
…[11 more quoted lines elided]…
> You don't say much about what is the problem. Your sample looks okay, a
few
> questions though:
> Have you assigned a pen to printer, have you assigned a brush? Have you
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Printing a rectangle -help

- **From:** "Cheesle" <cheesle@online.NoSpamPlease.no>
- **Date:** 2000-06-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8h8joh$hs8$1@news.cerf.net>`
- **References:** `<8gk2me$mut$1@duke.telepac.pt> <8gm8ui$l44$1@news.cerf.net> <8h6a0d$p43$1@duke.telepac.pt>`

```
"Raimundo Carvalho" <ray@mail.telepac.pt> wrote in message
news:8h6a0d$p43$1@duke.telepac.pt...
> No i did not. How can i do it?

This gives you a solid brush:
SelectObject(hDC,CreateSolidBrush(RGB(r,g,b))))

This gives you the pen
hPen = SelectObject(hDC,GetStockObject(BLACK_PEN));
            SelectObject(hDC,hPen);

Where hDC is the handle to your printer device context. Look up this
functions in MSDN for an explanation.

Cheesle
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
