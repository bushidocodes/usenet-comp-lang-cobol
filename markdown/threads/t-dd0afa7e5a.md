[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol and Arab charsets

_6 messages · 5 participants · 2004-04_

---

### Cobol and Arab charsets

- **From:** louloux3@lefumoir.com (Da LoU)
- **Date:** 2004-04-26T11:34:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<762d7a0b.0404261034.25e98886@posting.google.com>`

```
Hi

I want to convert a software to make it work with an arab compatible
charset.

The users run the soft from a terminal emulator (Putty) under windows
and the software is actually running under linux. I have server
express 4 installed on SuSE Linux 8

It is easy to display arab characters using the charset ISO-8859-6
(Latin/arab) is stead of CP437 (my current charset). I had no problem
with that.

My problem is how do I do an accept ?

Arab is written from right to left and I can't find anything in cobol
that allows me to do that.
Moreover the arab charset is made of special characters that display
only when certain combinations of characters are typed... It gets
complicated ...

any help is really needed !!!

Thanks 

Philippe
```

#### ↳ Re: Cobol and Arab charsets

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-04-26T14:24:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F9qdnXM744p-_BDdRVn-jg@giganews.com>`
- **References:** `<762d7a0b.0404261034.25e98886@posting.google.com>`

```
Da LoU wrote:
> Hi
>
…[19 more quoted lines elided]…
> any help is really needed !!!

Probably easier to teach your users English.
```

#### ↳ Re: Cobol and Arab charsets

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-04-26T19:34:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Sudjc.13624$e4.5164@newsread2.news.pas.earthlink.net>`
- **References:** `<762d7a0b.0404261034.25e98886@posting.google.com>`

```
Which compiler are you using?  In the 2002 COBOL Standard (and as an extension
in many '85 Standard compilers) there is support for ISO 10646 as "national"
characters.   It is SUPPOSED to handle mixed "left-to-right" and "right-to-left"
applications - but I don't know how well it really does.

Certainly if you ENTIRE program was just set up for "right-to-left" and you used
an appropriate terminal emulation, I would THINK that it would all work for you
without any specific programming requirements.  If you get into your emulator -
does it expect input in left-to-right or right-to-left?  I would expect COBOL
ACCEPT to work just like your "native" interface.
```

##### ↳ ↳ Re: Cobol and Arab charsets

- **From:** louloux3@lefumoir.com (Da LoU)
- **Date:** 2004-04-27T02:08:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<762d7a0b.0404270108.24bc52a9@posting.google.com>`
- **References:** `<762d7a0b.0404261034.25e98886@posting.google.com> <Sudjc.13624$e4.5164@newsread2.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<Sudjc.13624$e4.5164@newsread2.news.pas.earthlink.net>...
> Which compiler are you using?  In the 2002 COBOL Standard (and as an extension
> in many '85 Standard compilers) there is support for ISO 10646 as "national"
…[39 more quoted lines elided]…
> > Philippe

I'm using the Microfocus Cobol compiler provided in server express 4.
I'm under linux (english linux, there is no official arab version of
linux).

You're talking about ISO 10646 : I'm trying not to use it because
otherwise I THINK I need to change the lengths of every pic x.
ISO 8859-6 is 8 bits long and has all the arabic characters I need.

So I'm using ISO 8859-6 and a linux terminal emulation with putty. I
installed an arab keyboard drivers (regional settings in windows
control panel).
Now when I type the A key, I get an arab character in cobol.
To right form right to left, I just need to be able to change the
keyboard configuration :
I need to replace a strike on the A key by a strike on the A key + a
strike on the left arrow key.

How can I do that ?
```

###### ↳ ↳ ↳ Re: Cobol and Arab charsets

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2004-04-27T13:17:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20040427091757.17730.00000486@mb-m16.aol.com>`
- **References:** `<762d7a0b.0404270108.24bc52a9@posting.google.com>`

```
If your compiler includes the REVERSE intrinsic function, that might solve your
problem. It's a little hard to tell without more information, but REVERSE was
designed to work with Arabic and Hebrew, two single-byte character sets written
from right to left.

Hope this helps.

Kind regards,


-Steve Comstock
800-993-9716
303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

#### ↳ Re: Cobol and Arab charsets

- **From:** Vaclav Snajdr <vsn@snajdr.de>
- **Date:** 2004-04-27T07:38:07+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6kqvv$nkp$03$1@news.t-online.com>`
- **References:** `<762d7a0b.0404261034.25e98886@posting.google.com>`

```
Perhaps you write a "common acept" youself. Instead to write
accept name-1 line 10 col 20 with size 25
you use an call for it

call "myaccept" using my-line my-col my-size my-acc
move my-acc to  name-1

in myaccept:

01  my-acc              pic x(80).
01  red-field redefines  my-acc
 3  red-occ             occurs 80.
  5 m-a                 pic x.

  acc-sec section.  
        compute start-col =  my-col + my-size
  do-acc.
        accept m-a      line my-line start-col

        if m-a  =       some-thing-for-me-end  exit section.
       
        subtract 01 from start-pos
        if start-pos    =   my-col    exit section
        go to           do-acc.


A routime writte in this way needs little more execution
time but it is not more the problem today. I use such one
for editor functionality in the application and have not
problems with the users.   



Da LoU wrote:

> Hi
> 
…[23 more quoted lines elided]…
> Philippe
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
