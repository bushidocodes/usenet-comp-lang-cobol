[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF COBOL 132 COLUMN DISPLAY ISSUE

_10 messages · 4 participants · 2003-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-03-06T09:34:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0303060934.5ece0c26@posting.google.com>`

```
Before I call MF and ask them what is going on, I figured I'd post
here and see if anyone has some insight to offer.

Background Info
---------------
OS: HP-UX 11i B.13.45 using vt100 emulation
MF: Object Cobol 4.1.4


Issue
-----

I am using a call to "cobtermmode" to switch between 80 & 132 column
display screens. Everything is working great, except for one little
quirk - on line 24, coulmns 80-83 appear to be inaccessable. Even a
simple statement like:

DISPLAY "HELLO THERE"
  AT LINE 24 COLUMN 80
END-DISPLAY

doesn't yield the desired results. Instead I end up with just "O
THERE" starting at line 24, column 84.

I know it is not the terminal database, since the DECALN escape
sequence (<ESC>#8) fills the screen completely with E's as it is
supposed to, including the four positions in question.

This is very puzzling - any ideas?

Thanks,
Chris
```

#### ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-07T00:35:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e67a066.112431880@news.optonline.net>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com>`

```
ctaliercio@yahoo.com (Chris) wrote:

>Before I call MF and ask them what is going on, I figured I'd post
>here and see if anyone has some insight to offer.
…[26 more quoted lines elided]…
>This is very puzzling - any ideas?

I have seen the same bug. 

Try using a different terminal type, perhaps ANSI. The problem is not in Micro
Focus; it is in either termcap or your terminal emulator.
```

##### ↳ ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-07T16:43:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b494m6$b7h$2@aklobs.kc.net.nz>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com> <3e67a066.112431880@news.optonline.net>`

```
Robert Wagner wrote:

> I have seen the same bug.

It is not a bug, it is a feature.
 
> Try using a different terminal type, perhaps ANSI. The problem is not in
> Micro Focus; it is in either termcap or your terminal emulator.

It is not in the terminal emulator or in termcap, it is MicroFocus.
```

##### ↳ ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-03-07T07:38:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0303070738.46b57709@posting.google.com>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com> <3e67a066.112431880@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e67a066.112431880@news.optonline.net>...
> ctaliercio@yahoo.com (Chris) wrote:
> 
…[33 more quoted lines elided]…
> Focus; it is in either termcap or your terminal emulator.

Robert,

I can't see how it is a bug with the termcap or my emulator - as I
said in the OP, the DECALN feature does exactly what it is supposed
to.

Chris
```

###### ↳ ↳ ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-07T17:42:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e68d9c4.37109843@news.optonline.net>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com> <3e67a066.112431880@news.optonline.net> <8cc07162.0303070738.46b57709@posting.google.com>`

```
ctaliercio@yahoo.com (Chris) wrote:

>robert@wagner.net (Robert Wagner) wrote in message
news:<3e67a066.112431880@news.optonline.net>...
>> ctaliercio@yahoo.com (Chris) wrote:
>> 
…[32 more quoted lines elided]…
>> Try using a different terminal type, perhaps ANSI. The problem is not in
Micro
>> Focus; it is in either termcap or your terminal emulator.
>
…[4 more quoted lines elided]…
>to.

Gael's explanation sounds correct. 

I was thinking DECALN might be using a different command to the 'terminal', some
kind of fill command rather than painting the screen one byte at a time.
```

#### ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-03-07T16:41:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b494io$b7h$1@aklobs.kc.net.nz>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com>`

```
Chris wrote:

> I am using a call to "cobtermmode" to switch between 80 & 132 column
> display screens. Everything is working great, except for one little
> quirk - on line 24, coulmns 80-83 appear to be inaccessable. Even a
> simple statement like:

MF does reserve a small area for user indicators such as 'I' for being in 
insert mode in ACCEPT statements and ">" as the off end of field.

From the manual:

"""The following code disables display of the Insert/Replace indicator and  
   enables display of the Off end of field indicator:

    move 56 to bit-pair-number
    move 3 to bit-pair-setting
        call x"AF" using set-bit-pairs
                         parameter-block
    move 57 to bit-pair-number
    move 0 to bit-pair-setting
        call x"AF" using set-bit-pairs
                         parameter-block

"""

This is probably output into 2480 on your terminal, it may be possible to 
move it, otherwise disable.
```

##### ↳ ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-03-07T07:33:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0303070733.1a8a6e02@posting.google.com>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com> <b494io$b7h$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<b494io$b7h$1@aklobs.kc.net.nz>...
> Chris wrote:
> 
…[25 more quoted lines elided]…
> move it, otherwise disable.

Richard,

Thanks for the suggestion, but unfortunately it did not provide a
solution. Those four bytes still seem mysteriously unavailable, even
after disabling all of the Adis indicators (56, 57 & 58).

Chris
```

#### ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** "Gael Wilson" <gael.wilson@nospam.microfocus.com>
- **Date:** 2003-03-07T12:51:08
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4a4mq$1dh$1@hyperion.microfocus.com>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com>`

```
>
> I am using a call to "cobtermmode" to switch between 80 & 132 column
…[11 more quoted lines elided]…
> Chris

Chris,

This is because you are using the extended ACCEPT/DISPLAY functionality and
by default the status fields are displayed at those positions. You can alter
the positions by using the ADISCF utility, selecting Alter and then
Positions tho change the settings.
```

##### ↳ ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-03-07T11:01:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0303071101.6e2cb5b7@posting.google.com>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com> <b4a4mq$1dh$1@hyperion.microfocus.com>`

```
"Gael Wilson" <gael.wilson@nospam.microfocus.com> wrote in message news:<b4a4mq$1dh$1@hyperion.microfocus.com>...
> >
> > I am using a call to "cobtermmode" to switch between 80 & 132 column
…[18 more quoted lines elided]…
> Positions tho change the settings.

Gael,

Again, thanks for the suggestion, but this didn't work either.

Chris
```

#### ↳ Re: MF COBOL 132 COLUMN DISPLAY ISSUE

- **From:** ctaliercio@yahoo.com (Chris)
- **Date:** 2003-03-07T07:40:33-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8cc07162.0303070740.57de763@posting.google.com>`
- **References:** `<8cc07162.0303060934.5ece0c26@posting.google.com>`

```
ctaliercio@yahoo.com (Chris) wrote in message news:<8cc07162.0303060934.5ece0c26@posting.google.com>...
> Before I call MF and ask them what is going on, I figured I'd post
> here and see if anyone has some insight to offer.
…[29 more quoted lines elided]…
> Chris

Just a follow up to provide more clues: this only happens when I use
the "cobtermmode" call to switch to 132 columns from within the
application. If I switch my TERM to vt100-w before starting the COBOL
run unit, this is not an issue - the four bytes in question all
display properly. It must be something in the "cobtermmode" call that
is interfering with these four bytes.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
