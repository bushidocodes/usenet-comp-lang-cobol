[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# BACKGROUND SCREEN COLORS FOR RM-COBOL/85

_8 messages · 4 participants · 2006-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### BACKGROUND SCREEN COLORS FOR RM-COBOL/85

- **From:** diego.gda@gmail.com
- **Date:** 2006-10-20T11:05:01-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161367501.199762.192390@b28g2000cwb.googlegroups.com>`

```
Hello to everybody. I am trying to develop a program with RM-COBOL/85
but I do not know how to  make the whole screen change color! I know
how to change the color of specific displays, but not of the entire
screen. I would really appreciate if someone could help me by telling
me how. 
Thanks in advance.
```

#### ↳ Re: BACKGROUND SCREEN COLORS FOR RM-COBOL/85

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-20T19:57:38+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c07ij21org3hq0b4odu1fh54dpofq7j9ri@4ax.com>`
- **References:** `<1161367501.199762.192390@b28g2000cwb.googlegroups.com>`

```
On 20 Oct 2006 11:05:01 -0700, diego.gda@gmail.com wrote:

>Hello to everybody. I am trying to develop a program with RM-COBOL/85
>but I do not know how to  make the whole screen change color! I know
…[3 more quoted lines elided]…
>Thanks in advance.
Please state compiler version, runtime version and OS used 


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: BACKGROUND SCREEN COLORS FOR RM-COBOL/85

- **From:** "d_gda@yahoo.com" <diego.gda@gmail.com>
- **Date:** 2006-10-20T12:16:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161371803.044031.242300@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<c07ij21org3hq0b4odu1fh54dpofq7j9ri@4ax.com>`
- **References:** `<1161367501.199762.192390@b28g2000cwb.googlegroups.com> <c07ij21org3hq0b4odu1fh54dpofq7j9ri@4ax.com>`

```
It is version 6 and I am running it in Windows.
```

###### ↳ ↳ ↳ Re: BACKGROUND SCREEN COLORS FOR RM-COBOL/85

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-20T20:29:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qs8ij2hile2qeh6784p2q6af64vcurgssr@4ax.com>`
- **References:** `<1161367501.199762.192390@b28g2000cwb.googlegroups.com> <c07ij21org3hq0b4odu1fh54dpofq7j9ri@4ax.com> <1161371803.044031.242300@h48g2000cwc.googlegroups.com>`

```
On 20 Oct 2006 12:16:43 -0700, "d_gda@yahoo.com" <diego.gda@gmail.com>
wrote:

>It is version 6 and I am running it in Windows.

full version please.

V6 can run in Windows mode or in DOS mode .


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: BACKGROUND SCREEN COLORS FOR RM-COBOL/85

_(reply depth: 4)_

- **From:** "d_gda@yahoo.com" <diego.gda@gmail.com>
- **Date:** 2006-10-20T14:24:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161379464.336513.42280@e3g2000cwe.googlegroups.com>`
- **In-Reply-To:** `<qs8ij2hile2qeh6784p2q6af64vcurgssr@4ax.com>`
- **References:** `<1161367501.199762.192390@b28g2000cwb.googlegroups.com> <c07ij21org3hq0b4odu1fh54dpofq7j9ri@4ax.com> <1161371803.044031.242300@h48g2000cwc.googlegroups.com> <qs8ij2hile2qeh6784p2q6af64vcurgssr@4ax.com>`

```
MS-DOS mode... Thank you
```

#### ↳ Re: BACKGROUND SCREEN COLORS FOR RM-COBOL/85

- **From:** Donald Tees <donald_tees@donald-tees.ca>
- **Date:** 2006-10-20T17:56:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ehbgli$1tg$1@aioe.org>`
- **References:** `<1161367501.199762.192390@b28g2000cwb.googlegroups.com>`

```
diego.gda@gmail.com wrote:
> Hello to everybody. I am trying to develop a program with RM-COBOL/85
> but I do not know how to  make the whole screen change color! I know
…[4 more quoted lines elided]…
> 

Display space with background-color.

Donald
```

##### ↳ ↳ Re: BACKGROUND SCREEN COLORS FOR RM-COBOL/85

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2006-10-20T23:18:47+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eliij2d8pc560hbndmjs3rqkp95aouk5v8@4ax.com>`
- **References:** `<1161367501.199762.192390@b28g2000cwb.googlegroups.com> <ehbgli$1tg$1@aioe.org>`

```
On Fri, 20 Oct 2006 17:56:46 -0400, Donald Tees
<donald_tees@donald-tees.ca> wrote:

>diego.gda@gmail.com wrote:
>> Hello to everybody. I am trying to develop a program with RM-COBOL/85
…[9 more quoted lines elided]…
>Donald
RM/COBOL does not have that keyword.

Way to do it is by using the CONTROL option of the DISPLAY.

eg.
display spaces line 1 position 1 erase eos
   control "FCOLOR=BLUE, BCOLOR=WHITE"


where the valid colors are

Valid Color Names	High-Intensity Color Values (Defaults)
Black 		Gray
Blue 			Light Blue
Green 		Light Green
Cyan 			Light Cyan
Red 			Light Red
Magenta 		Light Magenta
Brown 		Yellow
White		 	High-Intensity White


Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

###### ↳ ↳ ↳ Re: BACKGROUND SCREEN COLORS FOR RM-COBOL/85

- **From:** "Alba" <diego.gda@gmail.com>
- **Date:** 2006-10-20T15:40:21-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1161384021.797487.230590@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<eliij2d8pc560hbndmjs3rqkp95aouk5v8@4ax.com>`
- **References:** `<1161367501.199762.192390@b28g2000cwb.googlegroups.com> <ehbgli$1tg$1@aioe.org> <eliij2d8pc560hbndmjs3rqkp95aouk5v8@4ax.com>`

```
thank you

Frederico Fonseca ha escrito:

> On Fri, 20 Oct 2006 17:56:46 -0400, Donald Tees
> <donald_tees@donald-tees.ca> wrote:
…[36 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
