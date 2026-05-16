[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# redefining

_6 messages · 6 participants · 1999-11_

---

### redefining

- **From:** "STERN FAN" <p.limitone@gte.net>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GqT_3.267$lT.6467@dfiatx1-snr1.gtei.net>`

```
hello group,

i have a question about redefine statements.  i know you can redefine
something once, but can you call the same thing two different names for use
in a program?

ie: 02    hours-in    pic 99.
     02   hours redefines hours-in    pic 99.
     02   more-hours redefines hours-in   pic 99.

sorry if you think this is a dumb post, but i am a student and want to have
this question answered before i get back to school on monday.  i need to
know for a program i am writing.

thank you

phil
```

#### ↳ Re: redefining

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81hcsn$9b7$1@news.igs.net>`
- **References:** `<GqT_3.267$lT.6467@dfiatx1-snr1.gtei.net>`

```
Yes you can.  You can redefine it as many times as you wish ... in fact that
is the exact mechanism that I always use for setting up various print line
formats.  For example:

01 print-line                    picture x(132).
01 dumy-line-one    redefines print-line.
    02 column1-5            picture x(5).
    02 filler                       picture x.
    02 column7-8            picture 99.
            etc.
 01 dumy-line-two redefines print-line.
    02 filler                       picture xx.
    02 column3-10          picture x(8).
            etc.
 01 dumy-line-three redefines print-line.
    02 etc.

The advantage is that you can then use a standardized print routine as
follows.

        move data to column1-5.
        perform print-routine.


print-routine.
        if line-count is greater than page-limit
            perform new-page.
        move print-line to print-record.
        write print-record.
        move space to line-for-print.

One thing that you should note: some compilers require that each redefines
reference the original name, while others require that you reference the
previous.  I do not know what the standard says, perhaps Bill can tell us.
However, I have used compilers that would crap out on the above, demanding
that dumy-line-two should redefine dumy-line-one rather than the original
print-line.

STERN FAN wrote in message ...
>hello group,
>
…[17 more quoted lines elided]…
>
```

##### ↳ ↳ Re: redefining

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383C3B1D.B948B00@NOSPAMhome.com>`
- **References:** `<GqT_3.267$lT.6467@dfiatx1-snr1.gtei.net> <81hcsn$9b7$1@news.igs.net>`

```
donald tees wrote:

> One thing that you should note: some compilers require that each redefines
> reference the original name, while others require that you reference the
…[3 more quoted lines elided]…
> print-line.

Also, some compilers don't want you to redefine 01 levels, and/or only
allow 01 levels redefined in WORKING-STORAGE.  But these limits are easy
to adjust around.
```

###### ↳ ↳ ↳ Re: redefining

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9w__3.1027$Wo6.15844@typhoon01.swbell.net>`
- **References:** `<GqT_3.267$lT.6467@dfiatx1-snr1.gtei.net> <81hcsn$9b7$1@news.igs.net> <383C3B1D.B948B00@NOSPAMhome.com>`

```
Plus some (all?) compilers complain when the redefining object
is longer than the redefined one,

02  ITEM-1                    PIC X(100).
02  ITEM-2 REDEFINES ITEM-1 PIC X(200).

or has an occurs depending on,
yak-yak-yak.

We're really telling you more than you want to know.


Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:383C3B1D.B948B00@NOSPAMhome.com...
> donald tees wrote:
>
> > One thing that you should note: some compilers require that each
redefines
> > reference the original name, while others require that you
reference the
> > previous.  I do not know what the standard says, perhaps Bill can
tell us.
> > However, I have used compilers that would crap out on the above,
demanding
> > that dumy-line-two should redefine dumy-line-one rather than the
original
> > print-line.
>
> Also, some compilers don't want you to redefine 01 levels, and/or
only
> allow 01 levels redefined in WORKING-STORAGE.  But these limits are
easy
> to adjust around.
```

#### ↳ Re: redefining

- **From:** Fred Zinner <technik@aktiv.co.at>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383C09FA.E6E864ED@aktiv.co.at>`
- **References:** `<GqT_3.267$lT.6467@dfiatx1-snr1.gtei.net>`

```
STERN FAN wrote:
> 
> hello group,
…[15 more quoted lines elided]…
> phil
this makes no sence...
but maybe this

02 act-time pic 999999.

02 act-time-special redefines act-time.
  05 act-hours pic 99.
  05 act-minutes pic 99.
  05 act-secundes pic99.

hope it helps
cu
fred
```

#### ↳ Re: redefining

- **From:** "The Programmer" <someone@somewhere.com>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<RHU_3.50281$Hk.457169@news1.mia>`
- **References:** `<GqT_3.267$lT.6467@dfiatx1-snr1.gtei.net>`

```
As far as COBOL is concerned, you can redefine any data item (elemental or group) as many
times as you want. There may be some practical considerations, of course... like
attempting to redefine something ten thousand times. Mind you, in some MSA programs I saw
items redefined up to 300 times. Talk about difficult to follow logic... :o

Though not practical, or useful, the example you quoted with the three redefinitions is
therefore, perfectly valid. In fact, depending on the compiler, you can have HOURS
redefine HOURS-IN, and then have MORE-HOURS redefine HOURS. Assuming that "HOURS" isn't a
reserved word, of course... I don't think it is.

The COBOL REDEFINES clause is just the ORG instruction with an address.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
