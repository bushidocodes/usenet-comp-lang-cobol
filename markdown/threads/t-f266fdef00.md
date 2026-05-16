[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Capturing Text And Display Attributes From Terminal Emulator

_8 messages · 5 participants · 1998-11_

---

### Capturing Text And Display Attributes From Terminal Emulator

- **From:** nick@asheath.demon.co.uk (Nick & Carol Lucas-White)
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364f02d4.961210@news.demon.co.uk>`

```
I've got a handy routine that I use under Unix to read the graphics
adaptor card to capture both test and display attributes (colours)
using "C". Does anyone know of a way to capture these from a terminal
emulator or perhaps know of a terminal emulator that can "dump" this
information to a file ? I use this to "read" existing displays I've
created using MicroFocus Cobol and then put the display and attributes
into my own version of their Screens editor that then generates what
they descibe as generic display attributes which can be used with
"CBL_WRITE_CHATTR". Any help would be most appreciated but please
don't try and sell me "Flexus", thanks.

Nick Lucas
```

#### ↳ Re: Capturing Text And Display Attributes From Terminal Emulator

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72nebv$hm9$1@news.igs.net>`
- **References:** `<364f02d4.961210@news.demon.co.uk>`

```
If you can run them under DOS, then I have a TSR that
might do the job for you ... it traps the screen print key and
dumps to an ASCII file ... I use it for stage one documentation.
It does not capture attributes, though I can give you source
and you could modify it to do that as well.  The routine is not
terribly elegant, you can only stop it by re-booting, and it
is only designed to grab up to 100 screens, but it does work
pretty reliably. (And it will work in a windows95 dos window).

Nick & Carol Lucas-White wrote in message
<364f02d4.961210@news.demon.co.uk>...
>I've got a handy routine that I use under Unix to read the graphics
>adaptor card to capture both test and display attributes (colours)
…[9 more quoted lines elided]…
>Nick Lucas
```

#### ↳ Re: Capturing Text And Display Attributes From Terminal Emulator

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72nfgu$k5g$1@news.igs.net>`
- **References:** `<364f02d4.961210@news.demon.co.uk>`

```
Further to that last message.  I just tested the TSR
running in the background while I ran a DOS terminal
emulator in a '95 window (an older version of
ProComm), and it was able to capture the "terminal"
screen quite nicely. ProComm can emulate most of
the common terminals, so it should work quite well
if you have a PC you can run as your terminal.  You
would have to do a bit of modification to get to
write attributes as well, but the code is well written
and easy to read. (My "rules" for assembler specify
a comment for every line, so you have code on the
left and a running commentary on the right).

Nick & Carol Lucas-White wrote in message
<364f02d4.961210@news.demon.co.uk>...
>I've got a handy routine that I use under Unix to read the graphics
>adaptor card to capture both test and display attributes (colours)
…[9 more quoted lines elided]…
>Nick Lucas
```

##### ↳ ↳ Re: Capturing Text And Display Attributes From Terminal Emulator

- **From:** nop06685@mail.telepac.pt (Frederico Fonseca)
- **Date:** 1998-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364f605e.9871290@news.indigo.ie>`
- **References:** `<364f02d4.961210@news.demon.co.uk> <72nfgu$k5g$1@news.igs.net>`

```
>Nick & Carol Lucas-White wrote in message
><364f02d4.961210@news.demon.co.uk>...
…[12 more quoted lines elided]…
>

Hi.

One terminal emulator that allows you do do that is TUN-EMUL from
www.esker.fr.
You can contact you local distributor of this product and as for a
demo cd (it will run for 15 days after installation) and test it
for you purposes.

best

Frederico Fonseca
```

#### ↳ Re: Capturing Text And Display Attributes From Terminal Emulator

- **From:** "Thane Hubbell" <redsky@ibm.net>
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be10f6$dbeb9040$87bc48a6@default>`
- **References:** `<364f02d4.961210@news.demon.co.uk>`

```


Nick & Carol Lucas-White <nick@asheath.demon.co.uk> wrote in article
<364f02d4.961210@news.demon.co.uk>...
> I've got a handy routine that I use under Unix to read the graphics
> adaptor card to capture both test and display attributes (colours)
…[7 more quoted lines elided]…
> don't try and sell me "Flexus", thanks.

MicroFocus has two routines to do what you want CBL_READ_SCR_CHAR and
CBL_READ_SCR_ATTR.  The syntax is documented in the "Library Routines" of
the manual.
```

##### ↳ ↳ Re: Capturing Text And Display Attributes From Terminal Emulator

- **From:** nick@asheath.demon.co.uk (Nick & Carol Lucas-White)
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36506fb2.2025032@news.demon.co.uk>`
- **References:** `<364f02d4.961210@news.demon.co.uk> <01be10f6$dbeb9040$87bc48a6@default>`

```
>
>MicroFocus has two routines to do what you want CBL_READ_SCR_CHAR and
>CBL_READ_SCR_ATTR.  The syntax is documented in the "Library Routines" of
>the manual.
>

Thanks for all the replies - I'd quite like to try your TSR Donald if
you'd like to send me the source. The two routines above are great if
you've already got them built into the application but they can't be
used to read another terminal window.
```

###### ↳ ↳ ↳ Re: Capturing Text And Display Attributes From Terminal Emulator

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365077c3.0@news1.ibm.net>`
- **References:** `<364f02d4.961210@news.demon.co.uk> <01be10f6$dbeb9040$87bc48a6@default> <36506fb2.2025032@news.demon.co.uk>`

```

Nick & Carol Lucas-White wrote in message
<36506fb2.2025032@news.demon.co.uk>...
>>
>>MicroFocus has two routines to do what you want CBL_READ_SCR_CHAR and
…[8 more quoted lines elided]…
>

you can find Donald's TSRs at http://www.etk.com/links/tees
```

###### ↳ ↳ ↳ Re: Capturing Text And Display Attributes From Terminal Emulator

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72q1le$4fm$1@news.igs.net>`
- **References:** `<364f02d4.961210@news.demon.co.uk> <01be10f6$dbeb9040$87bc48a6@default> <36506fb2.2025032@news.demon.co.uk>`

```
I have forwarded the code to Leif, and we are in the
process of setting it up as available on his web page.
I will keep you informed in here.

Nick & Carol Lucas-White wrote in message
<36506fb2.2025032@news.demon.co.uk>...
>>
>>MicroFocus has two routines to do what you want CBL_READ_SCR_CHAR and
…[8 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
