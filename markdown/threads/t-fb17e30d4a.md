[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie: ?'s on DISPLAY and a status code

_6 messages · 6 participants · 2000-02_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Newbie: ?'s on DISPLAY and a status code

- **From:** "Robin Webber" <r.webber@cmich.edu>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3899f343@news.cmich.edu>`

```
Hi,   I'm very new to COBOL and having a hard time with my first program. I
get a status code of 48 when trying to run it. I have successfully, I think,
linked the correct files, etc. Could anyone tell me what that code means?

Also,  I have tried using DISPLAY statements so I can see what's going on
before it crashes, but I cannot get the compiler to accept them. It
complains about being in area A, so I move them to area B, then it says
"Display was invalid."

I will really appreciate anyone's help here.

Thanks a lot!
```

#### ↳ Re: Newbie: ?'s on DISPLAY and a status code

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87cu4p$3bp2$1@newssvr03-int.news.prodigy.com>`
- **References:** `<3899f343@news.cmich.edu>`

```

Robin Webber <r.webber@cmich.edu> wrote in message
news:3899f343@news.cmich.edu...
> Hi,   I'm very new to COBOL and having a hard time with my first program.
I
> get a status code of 48 when trying to run it. I have successfully, I
think,
> linked the correct files, etc. Could anyone tell me what that code means?
>
…[7 more quoted lines elided]…
> Thanks a lot!

Could you include the platform you're using for your COBOL program?  Is the
48 a FILE-STATUS return code?  What does the exact code look like for your
DISPLAY statement?  What field name or literal are you trying to display?
```

##### ↳ ↳ Re: Newbie: ?'s on DISPLAY and a status code

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87dg0m$5jg$1@aklobs.kc.net.nz>`
- **References:** `<3899f343@news.cmich.edu> <87cu4p$3bp2$1@newssvr03-int.news.prodigy.com>`

```

: Robin Webber <r.webber@cmich.edu> wrote in message
:> Hi,   I'm very new to COBOL and having a hard time with my first program.
: I
:> get a status code of 48 when trying to run it. I have successfully, I
: think,
:> linked the correct files, etc. Could anyone tell me what that code means?

A WRITE operation has been tried on a file not opened OUTPUT
or I-O or EXTEND mode or on a file open I-O in the sequential
access mode.

You have probably got a file where the SELECT .. ASSIGN has
ACCESS SEQUENTIAL (or no ACCESS which then defaults to SEQUENTIAL),
you have opened it I-O and then tried to WRITE.

Make the SELECT .. ACCESS DYNAMIC, or OPEN OUTPUT the file.
```

#### ↳ Re: Newbie: ?'s on DISPLAY and a status code

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3899FB91.1628AE8F@NOSPAMwebaccess.net>`
- **References:** `<3899f343@news.cmich.edu>`

```


Robin Webber wrote:

> Hi,   I'm very new to COBOL and having a hard time with my first program. I
> get a status code of 48 when trying to run it. I have successfully, I think,
> linked the correct files, etc. Could anyone tell me what that code means?

Status codes are in most COBOL manuals.  In MVS a status code of 48 is the same
for flat files as for VSAM files, so you can check the following URL:
http://mvshelp.com/vsamretn.htm .  I recently got that error when I converted a
program from an old ANSI COBOL to COBOL for MVS where the old program opened the
file I-O, did a READ, and then tried to do a WRITE.  The solution was to change
the WRITE to a REWRITE.


> Also,  I have tried using DISPLAY statements so I can see what's going on
> before it crashes, but I cannot get the compiler to accept them. It
…[3 more quoted lines elided]…
> I will really appreciate anyone's help here.

You didn't give us enough information to find your error.  Typically, you need
to tell us your compiler, your OS, and your code.  In this case, we may need to
look at the DISPLAY command as well as the definition of the field (s) being
displayed.
```

#### ↳ Re: Newbie: ?'s on DISPLAY and a status code

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oKom4.228$rc4.2747@news.swbell.net>`
- **References:** `<3899f343@news.cmich.edu>`

```
*Probably* a file status of 48 means:

4 = Logical file error
8 = WRITE statement attempted against an unopened file or a file
opened for input.


Robin Webber <r.webber@cmich.edu> wrote in message
news:3899f343@news.cmich.edu...
> Hi,   I'm very new to COBOL and having a hard time with my first
program. I
> get a status code of 48 when trying to run it. I have successfully,
I think,
> linked the correct files, etc. Could anyone tell me what that code
means?
>
> Also,  I have tried using DISPLAY statements so I can see what's
going on
> before it crashes, but I cannot get the compiler to accept them. It
> complains about being in area A, so I move them to area B, then it
says
> "Display was invalid."
>
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Newbie: ?'s on DISPLAY and a status code

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-02-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87eg5k$kna$1@news.igs.net>`
- **References:** `<3899f343@news.cmich.edu>`

```
I suspect that the problem with your displays is that you are attempting to
display a file record, which Fujitsu (I am assuming Fujitsu as well) does
not allow.  Move the data to working storage, and display that instead.  It
is much easier to debug something when you have some idea of the code, the
compiler, and the computer it is running on.

Robin Webber wrote in message <3899f343@news.cmich.edu>...
>Hi,   I'm very new to COBOL and having a hard time with my first program. I
>get a status code of 48 when trying to run it. I have successfully, I
think,
>linked the correct files, etc. Could anyone tell me what that code means?
>
…[9 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
