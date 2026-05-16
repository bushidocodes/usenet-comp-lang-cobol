[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Errorcode 114 when calling Netexpress OLE EXE from VB

_3 messages · 3 participants · 1999-03_

---

### Errorcode 114 when calling Netexpress OLE EXE from VB

- **From:** oklein@my-dejanews.com
- **Date:** 1999-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cj7bj$sgh$1@nnrp1.dejanews.com>`

```
Hi, I'm working with a Cobol EXE build with Netexpress. This EXE is called
from a Visual Basic Modul. It's late bind. Now I get Errorcode 114: "Attempt
to access item beyond bounds of memory". The error occurs when Visual Basic
set the Cobol Object to nothing. "Set Obj = Nothing" Only some machines show
this behaviour. On others the application runs fine. In Debugmode the error
doesn't occur.


Thanks for your help.

Oliver Klein

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Errorcode 114 when calling Netexpress OLE EXE from VB

- **From:** smb@mfltdz.co.ukz (Steve Biggs)
- **Date:** 1999-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cjgtf$1n3@hyperion.mfltd.co.uk>`
- **References:** `<7cj7bj$sgh$1@nnrp1.dejanews.com>`

```
OKLEIN@WAC.de wrote:
>Hi, I'm working with a Cobol EXE build with Netexpress. This EXE is called
>from a Visual Basic Modul. It's late bind. Now I get Errorcode 114: "Attempt
…[3 more quoted lines elided]…
>doesn't occur.

Oliver,
You don't say which version of Net Express you are running.
Whichever version you are using, please download the latest Net Express 
RTS FixPack from WebSync, which has fixes for this area.

Steve.
```

##### ↳ ↳ Re: Errorcode 114 when calling Netexpress OLE EXE from VB

- **From:** "Donald Tees" <donald@wilmack.com>
- **Date:** 1999-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7cjvo4$9u7$2@news.igs.net>`
- **References:** `<7cj7bj$sgh$1@nnrp1.dejanews.com> <7cjgtf$1n3@hyperion.mfltd.co.uk>`

```
Thast is normally caused by a subscript out of bounds.  I would suspect an
unititialized subscript, particularly in light of the fact that it does not
always happen.

Steve Biggs wrote in message <7cjgtf$1n3@hyperion.mfltd.co.uk>...
>OKLEIN@WAC.de wrote:
>>Hi, I'm working with a Cobol EXE build with Netexpress. This EXE is called
>>from a Visual Basic Modul. It's late bind. Now I get Errorcode 114:
"Attempt
>>to access item beyond bounds of memory". The error occurs when Visual
Basic
>>set the Cobol Object to nothing. "Set Obj = Nothing" Only some machines
show
>>this behaviour. On others the application runs fine. In Debugmode the
error
>>doesn't occur.
>
…[8 more quoted lines elided]…
>E-mail replies: please remove all the "z"s from my address.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
