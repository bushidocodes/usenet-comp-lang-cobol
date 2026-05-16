[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# External program call from Netexpressprg

_4 messages · 3 participants · 1998-11_

---

### External program call from Netexpressprg

- **From:** BOSsysteme@t-online.de (BOSsysteme)
- **Date:** 1998-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71pp58$ppv$1@news01.btx.dtag.de>`

```
Hello all,

i'm new to this group and I think that my question is a very easy one,
procedure and failure report follows:

I'm writing an application in MF-Cobol/NetExpress 2.0 (Win95/98/NT) from
within that app I call a program written in Borland-Delphi 4 using these
lines:

01  command-li        pic x(8) value "delphi.exe"
01  command-line-len  pic x(4) comp-5 value 8.
01  run-unit-id       pic x(8) comp-5 value 0.
01  stack-size        pic x(4) comp-5 value 0.
01  flags             pic x(4) comp-5 value 1.
01  tty-cmd           pic x(4) value space.
01  tty-cmd-len       pic x(4) comp-5 value 0.
01  status-code       pic xx comp-5.

call "CBL_EXEC_RUN_UNIT"   using command-li
                           by value command-line-len
                           by reference run-unit-id
                           by value stack-size
                                    flags
                           by reference tty-cmd
                           by value     tty-cmd-len
                           returning status-code.


This works up to here but when I perform a ShellExecute from within the
Delphi-Exe the program halts.

Killing the Netexpressprg (by Taskmangager e.g.) the Delphi Exe and the
second called program work fine.
If I start the Delphiprg with 'dubbleclick' it works perfecly.

Another problem in the same situation is that it seems the window of the
calling Netexpressprg is not been updated anymore after the call to the
Delphi-Exe.


Any suggestions, any help would be appreciated.

- What does my call in detail?
- Is there a better way to call external executables?


Thank you in advance.

Florian
```

#### ↳ Re: External program call from Netexpressprg

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364F4E76.B3F29D7C@IMN.nl>`
- **References:** `<71pp58$ppv$1@news01.btx.dtag.de>`

```
How could it ever work?

BOSsysteme wrote:
8<

> 01  command-li        pic x(8) value "delphi.exe"

Display command-li would show "delphi.e"
The Frog.
```

##### ↳ ↳ Re: External program call from Netexpressprg

- **From:** Boudewijn Schokker <schokker@xs4all.nl>
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3656B9F4.EAA386DC@xs4all.nl>`
- **References:** `<71pp58$ppv$1@news01.btx.dtag.de> <364F4E76.B3F29D7C@IMN.nl>`

```
Dear Huib,

What about extending you Pic to an x(10)??

Best regards,


Boudewijn Schokker

"COBOL Frog (Huib Klink)" wrote:
> 
> How could it ever work?
…[18 more quoted lines elided]…
>   (Download ICQ at http://www.icq.com/)
```

###### ↳ ↳ ↳ Re: External program call from Netexpressprg

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1998-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365ABB9E.E18D8693@IMN.nl>`
- **References:** `<71pp58$ppv$1@news01.btx.dtag.de> <364F4E76.B3F29D7C@IMN.nl> <3656B9F4.EAA386DC@xs4all.nl>`

```
Boudewijn Schokker wrote:

> Dear Huib,
>
> What about extending you Pic to an x(10)??

you mean(s) your?: It wasn't my picture, it was BOSsysteme's picture. (And his
problem).
The Frog

> Best regards,
>
> Boudewijn Schokker

Reg. too, Boudewijn. HDYD?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
