[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# number check...

_9 messages · 5 participants · 2001-02_

---

### number check...

- **From:** "Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com>
- **Date:** 2001-02-12T11:36:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<968ecg$bhn$1@rohrpostix.uta4you.at>`

```
Hi folks,
    how do i compare to a field defined as PIC +9(3)???
Im using mf-cobol, and the coding looks like

move 100 to f001.
if f001 = 100
   display 'true1'.
if f001 = +100
   display 'true2'.
if f002 = '+100'
   display 'true3'.

all 3 variations produce a false result.

Thanks for reading,
Wolf
```

#### ↳ Re: number check...

- **From:** "Paulo Vieira" <pvieira@emporsoft.pt>
- **Date:** 2001-02-12T10:58:09
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<968fp8$8l0$1@venus.telepac.pt>`
- **References:** `<968ecg$bhn$1@rohrpostix.uta4you.at>`

```
What is the definition for f002?
It seems that if you test f001, which I assume is PIC +9(3), you will get a
true.
On the other hand, it is possible that what you are looking for, is an
unedited numeric field, something like PIC S9(3).
regards,
Paulo Vieira
"Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com> wrote in
message news:968ecg$bhn$1@rohrpostix.uta4you.at...
> Hi folks,
>     how do i compare to a field defined as PIC +9(3)???
…[15 more quoted lines elided]…
>
```

#### ↳ Re: number check...

- **From:** "Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com>
- **Date:** 2001-02-12T12:06:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<968g3s$clg$1@rohrpostix.uta4you.at>`
- **References:** `<968ecg$bhn$1@rohrpostix.uta4you.at>`

```
...sorry, i was too fast, variant 3 gives true, of coarse.
so please disregard.
Wolf
"Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com> schrieb im
Newsbeitrag news:968ecg$bhn$1@rohrpostix.uta4you.at...
> Hi folks,
>     how do i compare to a field defined as PIC +9(3)???
…[15 more quoted lines elided]…
>
```

##### ↳ ↳ Re: number check...

- **From:** "Steven Lalewicz" <strl@mfltd.co.uk>
- **Date:** 2001-02-12T11:17:36
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<968lmd$el2$1@hyperion.mfltd.co.uk>`
- **References:** `<968ecg$bhn$1@rohrpostix.uta4you.at> <968g3s$clg$1@rohrpostix.uta4you.at>`

```
Hmm! For me the first two statements to work and the third one to fails.
In the third IF statement you have f002, so I'm not sure this is the
complete
program, or you missed something small but relevant when typing it in. Are
the ? in +9(3)??? repeated question marks for effect or do they represent
another edit field?

Regards,
Steve.

Wolf Grossi wrote in message <968g3s$clg$1@rohrpostix.uta4you.at>...
>...sorry, i was too fast, variant 3 gives true, of coarse.
>so please disregard.
…[22 more quoted lines elided]…
>
```

#### ↳ Re: number check...

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-02-12T08:19:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<968nii$6a6$1@news.igs.net>`
- **References:** `<968ecg$bhn$1@rohrpostix.uta4you.at>`

```
Compare them to numbers.  (+1, -1, etc.).  As long as you are comparing a
number to an ASCII string, then you will have maintenance problems.

"Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com> wrote in
message news:968ecg$bhn$1@rohrpostix.uta4you.at...
> Hi folks,
>     how do i compare to a field defined as PIC +9(3)???
…[15 more quoted lines elided]…
>
```

#### ↳ Re: number check...

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-12T07:14:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A87EFCE.3D2F803F@brazee.net>`
- **References:** `<968ecg$bhn$1@rohrpostix.uta4you.at>`

```
PIC +9(3) is only used for output, although there is a function
available to convert it to the type of number the computer uses.
What you want is PIC S9(3), in which case all three of your comparisons
will work.   You were actually comparing a number with an alphanumeric
display.

Oh, in real life, we like to use CoBOL's self documenting feature -
maintenance is a big, big part of CoBOL.  Variable names such as f001
are almost always counter to this.

Wolf Grossi wrote:

> Hi folks,
>     how do i compare to a field defined as PIC +9(3)???
…[13 more quoted lines elided]…
> Wolf
```

#### ↳ Re: number check...over and out

- **From:** "Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com>
- **Date:** 2001-02-12T21:27:24+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<969gvr$4kn$1@rohrpostix.uta4you.at>`
- **References:** `<968ecg$bhn$1@rohrpostix.uta4you.at>`

```
Thanks to all for your comments... and f001 is just used in this sample...
Wolf
"Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com> schrieb im
Newsbeitrag news:968ecg$bhn$1@rohrpostix.uta4you.at...
> Hi folks,
>     how do i compare to a field defined as PIC +9(3)???
…[15 more quoted lines elided]…
>
```

#### ↳ Re: number check...

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2001-02-12T16:28:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<969k2f$jii$1@slb0.atl.mindspring.net>`
- **References:** `<968ecg$bhn$1@rohrpostix.uta4you.at>`

```
Is this defined as "SIGN LEADING SEPARATE", where the "+" or "-" is a
separate byte ahead of the numeric value ?

Bill

"Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com> wrote in
message news:968ecg$bhn$1@rohrpostix.uta4you.at...
> Hi folks,
>     how do i compare to a field defined as PIC +9(3)???
…[15 more quoted lines elided]…
>
```

#### ↳ Re: number check...

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-02-12T21:46:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96a6ri$nj$1@news.igs.net>`
- **References:** `<968ecg$bhn$1@rohrpostix.uta4you.at>`

```
Wolf, please accept apologies for yesterday's completely erroneous answer.
Howard gave you the correct one.  I misread the post.
:<(


"Wolf Grossi" <wg@*NoEMail*PleaseRespond*NG*ID*magro-soft.com> wrote in
message news:968ecg$bhn$1@rohrpostix.uta4you.at...
> Hi folks,
>     how do i compare to a field defined as PIC +9(3)???
…[15 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
