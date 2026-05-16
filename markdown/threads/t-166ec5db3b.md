[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus CBL_READ_SCR_CHARS on HP-UX

_7 messages · 3 participants · 2008-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus CBL_READ_SCR_CHARS on HP-UX

- **From:** ferranp@gmail.com
- **Date:** 2008-07-16T09:07:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4abc3eef-f2c9-4095-a828-b028e55e8397@m73g2000hsh.googlegroups.com>`

```
Hello,

Is there anyone who has experience on using the calls
CBL_READ_SCR_CHARS/CBL_READ_SCR_ATTRS and CBL_WRITE_SCR_CHARS/
CBL_WRITE_SCR_ATTRS on HP-UX or Unix using Microfocus COBOL ?.

Some time ago, I've used this functions to save the contents of the
screen and redraw it later on MS-DOS, now I'm trying to use this
funcions on HP-UX and it does'nt worked well, it redraws the screen
with errors and without colors. I don't know if I have problems with
the terminals (terminfo etc...) or if this does'nt work on unix.

Thanks in advance.
```

#### ↳ Re: Microfocus CBL_READ_SCR_CHARS on HP-UX

- **From:** Vaclav Snajdr <snajdr.vaclav@t-online.de>
- **Date:** 2008-07-17T08:34:01+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g5mp4l$2vo$01$1@news.t-online.com>`
- **References:** `<4abc3eef-f2c9-4095-a828-b028e55e8397@m73g2000hsh.googlegroups.com>`

```
I use for save and restore screen since 1985 the function X"B8" (TISV,
HP-UX, Linux). I mean the older versions of MF-Cobol for Unix (< 4.xx)
do not support CBL_READ etc. But with X"B8" you can do it.


ferranp@gmail.com wrote:

> Hello,
> 
…[10 more quoted lines elided]…
> Thanks in advance.
```

##### ↳ ↳ Re: Microfocus CBL_READ_SCR_CHARS on HP-UX

- **From:** ferranp@gmail.com
- **Date:** 2008-07-18T07:50:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1b03c031-6286-40be-b74f-f457650b1612@s21g2000prm.googlegroups.com>`
- **References:** `<4abc3eef-f2c9-4095-a828-b028e55e8397@m73g2000hsh.googlegroups.com> <g5mp4l$2vo$01$1@news.t-online.com>`

```
On 17 Jul, 08:34, Vaclav Snajdr <snajdr.vac...@t-online.de> wrote:
> I use for save and restore screen since 1985 the function X"B8" (TISV,
> HP-UX, Linux). I mean the older versions of MF-Cobol for Unix (< 4.xx)
> do not support CBL_READ etc. But with X"B8" you can do it.
>

Hi,

How do you use the x'b8' function ?  I cannot find information about
this function in the manuals.
```

###### ↳ ↳ ↳ Re: Microfocus CBL_READ_SCR_CHARS on HP-UX

- **From:** Vaclav Snajdr <snajdr.vaclav@t-online.de>
- **Date:** 2008-07-18T17:11:59+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g5qbuj$ta7$01$1@news.t-online.com>`
- **References:** `<4abc3eef-f2c9-4095-a828-b028e55e8397@m73g2000hsh.googlegroups.com> <g5mp4l$2vo$01$1@news.t-online.com> <1b03c031-6286-40be-b74f-f457650b1612@s21g2000prm.googlegroups.com>`

```
In this way:
        

* 1093 COPY "wsxmatr".
  1094 01  XX-B8.
  1095     03 B8-FUN               PIC 99      COMP VALUE ZERO.
  1096     03 B8-PARA.
  1097        05 B8-LENGTH         PIC 9999    COMP VALUE ZERO.
  1098        05 B8-POS-SC         PIC 9999    COMP VALUE ZERO.
  1099        05 B8-POS-SC-R REDEFINES B8-POS-SC.
  1100           7   ZL-SC         pic 99  comp-x.
  1101           7  POS-SC         pic 99  comp-x.
  1102        05 B8-POS-BF         PIC 9999    COMP VALUE ZERO.
 


  1145 01  SR-MASKE.
  1146     03 SR-MASKE-O           OCCURS 24.
  1147        05 SR-MASK-T         PIC X(80).
  1148

  1149 01  SR-ATTR.
  1150     03 SR-ATTR-O            OCCURS 24.
  1151        05 SR-ATTR-T         PIC X(80).
  1152 01  RSR-ATTR   REDEFINES    SR-ATTR.
  1153     03 RSR-ATTR-O           OCCURS 1920.
  1154        05 RSR-ATT-T         PIC X.


        

       SCREEN-SAVE SECTION.
  3528     MOVE ZERO         TO    B8-FUN.
  3529     PERFORM                 SCREEN-WORK.
  3530 SCREEN-REST SECTION.
  3531     MOVE EINS         TO    B8-FUN.
  3532     PERFORM                 SCREEN-WORK.
  3533 SCREEN-WORK SECTION.
  3534     MOVE 1920         TO    B8-LENGTH.
  3535     MOVE EINS         TO    B8-POS-SC, B8-POS-BF.
  3536     CALL X"B8"        USING B8-FUN,    B8-PARA,
  3537                             SR-MASKE,  SR-ATTR.


ferranp@gmail.com wrote:

> On 17 Jul, 08:34, Vaclav Snajdr <snajdr.vac...@t-online.de> wrote:
>> I use for save and restore screen since 1985 the function X"B8" (TISV,
…[7 more quoted lines elided]…
> this function in the manuals.
```

#### ↳ Re: Microfocus CBL_READ_SCR_CHARS on HP-UX

- **From:** razor <iruddock@blueyonder.co.uk>
- **Date:** 2008-07-17T00:49:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<953c66a5-0ff0-434d-a95d-5bb6b14e1c3b@d45g2000hsc.googlegroups.com>`
- **References:** `<4abc3eef-f2c9-4095-a828-b028e55e8397@m73g2000hsh.googlegroups.com>`

```
Hi

I don't know if its been fixed, but I used to have a problem with a
bug in the CBL_WRITE_SCR_CHATTRS call. It didn't refresh the
attributes correctly, so I have to write the attributes separately. I
use the following code to do this.

       01  CBL-SCREEN-POSITION.
           03  CBL-ROW-NUMBER                PIC X COMP-X.
           03  CBL-COL-NUMBER                PIC X COMP-X.
       01  CBL-CHAR-BUFFER                   PIC X(2000).
       01  CBL-ATTR-BUFFER                   PIC X(2000).
       01  CBL-STRING-LENGTH                 PIC X COMP-X.

In common initialisation I also have


	   MOVE 00 TO CBL-ROW-NUMBER CBL-COL-NUMBER.
	   MOVE SPACES TO CBL-CHAR-BUFFER CBL-ATTR-BUFFER.
	   MOVE 2000 TO CBL-STRING-LENGTH.






       CBL-SAVE-SCREEN SECTION.
           CALL "CBL_READ_SCR_CHATTRS" USING
                        CBL-SCREEN-POSITION
                        CBL-CHAR-BUFFER
                        CBL-ATTR-BUFFER
                        CBL-STRING-LENGTH.

       CBL-WRITE-SCREEN SECTION.
           CALL "CBL_WRITE_SCR_CHATTRS" USING
                        CBL-SCREEN-POSITION
                        CBL-CHAR-BUFFER
                        CBL-ATTR-BUFFER
                        CBL-STRING-LENGTH.
           CALL "CBL_WRITE_SCR_ATTRS" USING
                        CBL-SCREEN-POSITION
                        CBL-ATTR-BUFFER
                        CBL-STRING-LENGTH.

This is a bit of a sledge hammer to crack a nut. I ALWAYS just copy
the whole screen even if the popup I use is a fraction of the screen.
As I see no performance problems with a few extra bytes in what is
after all an interactive program then I don't really lose any sleep
over it.

Hope this helps.

Regards
```

##### ↳ ↳ Re: Microfocus CBL_READ_SCR_CHARS on HP-UX

- **From:** ferranp@gmail.com
- **Date:** 2008-07-18T07:54:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<225b500a-5ed3-4947-9d26-3f3d99e751e6@b2g2000prf.googlegroups.com>`
- **References:** `<4abc3eef-f2c9-4095-a828-b028e55e8397@m73g2000hsh.googlegroups.com> <953c66a5-0ff0-434d-a95d-5bb6b14e1c3b@d45g2000hsc.googlegroups.com>`

```


On 17 Jul, 09:49, razor <irudd...@blueyonder.co.uk> wrote:
> Hi
>
…[35 more quoted lines elided]…
>


Thank you for your help, but I have tried all this functions and it
steel doesn't work.
I can write the chars correctly but when I write the atributes all the
screen gets messed up, I lose the colors and get strange chars on the
screen.
```

#### ↳ Re: Microfocus CBL_READ_SCR_CHARS on HP-UX

- **From:** ferranp@gmail.com
- **Date:** 2008-07-18T08:10:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68be3b2c-e790-4ad2-94ce-839a32564d2f@h1g2000prh.googlegroups.com>`
- **References:** `<4abc3eef-f2c9-4095-a828-b028e55e8397@m73g2000hsh.googlegroups.com>`

```
On 16 Jul, 18:07, ferr...@gmail.com wrote:
> Hello,
>
…[10 more quoted lines elided]…
> Thanks in advance.


At last, I've solved my problems using the functions CBL_SCR_SAVE and
CBL_SCR_RESTORE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
