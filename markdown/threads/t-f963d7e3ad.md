[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# clipboard

_7 messages · 7 participants · 2001-01 → 2001-02_

---

### clipboard

- **From:** "Philip Foncke" <philip.foncke@advalvas.be>
- **Date:** 2001-01-25T15:04:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZfXb6.2937$yz3.99955@iguano.antw.online.be>`

```
Is there a possibility to copy some strings (4 lines pic x(20)) to the
clipboard of windows
```

#### ↳ Re: clipboard

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-01-25T16:11:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EeYb6.242381$59.60912910@news3.rdc1.on.home.com>`
- **References:** `<ZfXb6.2937$yz3.99955@iguano.antw.online.be>`

```
Yes. I suspect one of the tool vendors in the group will pipe up with "buy
our product" which is probably the easiest approach.

If you're feeling brave about the Win32 API then look in the MSDN
documentation for "Clipboard Operations". You have to make a number of calls
to get things to work. They will involve:

OpenClipboard()         - locks the clipboard
SetClipboardData()    - publishes your data
GetClipboardData()    - retrieves your data
EmptyClipboard()        - cleans up the clipboard
CloseClipboard()        - unlocks the clipboard


SetClipboardData requires a memory handle which is returned by
GlobalAlloc(), which means you will need to define a linkage item and also
deal with these APIs to dynamically allocate memory:

GlobalAlloc()    - allocate global memory
GlobalLock()    - locks global memory and returns a pointer
GlobalUnlock() - unlocks global memory
GlobalFree()    - releases global memory


Pseudo-code to write to the clipboard looks something like:

    call GlobalAlloc()
    call GlobalLock()
    set address of my-linkage to (value of pointer returned by GlobalLock)
    move my-workingstorage to my-linkage

    call OpenClipboard()
    call SetClipboardData        ... probably using CF_OEMTEXT clipboard
format
    call CloseClipboard()

    call GlobalUnlock()
    call GlobalFree()

Of course, none of this is tested so use at your own risk. It's always a
good idea to test the return codes from these API functions.

Karl


"Philip Foncke" <philip.foncke@advalvas.be> wrote in message
news:ZfXb6.2937$yz3.99955@iguano.antw.online.be...
> Is there a possibility to copy some strings (4 lines pic x(20)) to the
> clipboard of windows
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: clipboard

- **From:** Support@ScreenIO.com (Kevin J. Hansen)
- **Date:** 2001-01-25T18:08:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a7069a5.166491542@news>`
- **References:** `<ZfXb6.2937$yz3.99955@iguano.antw.online.be> <EeYb6.242381$59.60912910@news3.rdc1.on.home.com>`

```
On Thu, 25 Jan 2001 16:11:16 GMT, "Oscar T. Grouch" <dustbin@home.com>
wrote:

>Yes. I suspect one of the tool vendors in the group will pipe up with "buy
>our product" which is probably the easiest approach.

>"Philip Foncke" <philip.foncke@advalvas.be> wrote in message
>news:ZfXb6.2937$yz3.99955@iguano.antw.online.be...
…[3 more quoted lines elided]…
>> philip.foncke@advalvas.be
===========
Karl,

Since you mentioned it <G> GUI ScreenIO does provide a function that
makes it easy to copy data to the clipboard, although we haven't
published the documentation yet.  It wouldn't be a big deal for us to
do so...

Your description is pretty accurate as to how it's done when you do it
the hard way.  Basically, you:

- Allocate some memory
- Copy your data to that memory
- Pass the memory handle to the Windows clipboard, along with some
indication as to what sort of data you are passing

You can then forget about the memory because you've given it to the
Windows clipboard.  You don't need to release the memory (in fact you
had better not) because the clipboard will release it when
appropriate.  You'd only free the memory if your call passing the
memory to the clipboard failed.

It's not terribly difficult if you're alreading calling Windows APIs
in your application but would be a hassle if this is your first
exposure to low-level Windows stuff.

Kevin
Norcom - COBOL Programming Tools
GUI ScreenIO - A Windows UI for COBOL
http://www.screenio.com
```

##### ↳ ↳ Re: clipboard

- **From:** "Paul Barnett" <paul.barnett@merant.com>
- **Date:** 2001-01-29T16:09:03
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9549g5$dlb$1@hyperion.mfltd.co.uk>`
- **References:** `<ZfXb6.2937$yz3.99955@iguano.antw.online.be> <EeYb6.242381$59.60912910@news3.rdc1.on.home.com>`

```
OK Oscar,

Buy Our Product, Net Express 3.1.

Seriously though, this kind of thing is supported easily with the INVOKE
statement. Not COBOL 85 but I expect it will be in the next standard. The
standards committee members who hang out in this group will probably correct
me if I'm wrong.

Regards,
Paul

"Oscar T. Grouch" <dustbin@home.com> wrote in message
news:EeYb6.242381$59.60912910@news3.rdc1.on.home.com...
> Yes. I suspect one of the tool vendors in the group will pipe up with "buy
> our product" which is probably the easiest approach.
>
> If you're feeling brave about the Win32 API then look in the MSDN
> documentation for "Clipboard Operations". You have to make a number of
calls
> to get things to work. They will involve:
>
…[47 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: clipboard

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-02-03T03:01:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A7B75E0.2F9E120@home.com>`
- **References:** `<ZfXb6.2937$yz3.99955@iguano.antw.online.be> <EeYb6.242381$59.60912910@news3.rdc1.on.home.com> <9549g5$dlb$1@hyperion.mfltd.co.uk>`

```
Well, a quick answer to that one Paul. It may be available in N/E but it will be
light years before it's available as an OO feature. J4 haven't even looked at
the initial Standard classes, from memory, prepared back in '96. With the
current target for COBOL 200X set as Dec 2002 - standard classes don't stand a
chance.

Jimmy, Calgary AB

Paul Barnett wrote:

> OK Oscar,
>
…[67 more quoted lines elided]…
> >
```

#### ↳ Re: clipboard

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-01-26T08:06:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A71300F.BDEB64DC@Azonic.co.nz>`
- **References:** `<ZfXb6.2937$yz3.99955@iguano.antw.online.be>`

```
Philip Foncke wrote:
> 
> Is there a possibility to copy some strings (4 lines pic x(20)) to the
> clipboard of windows

You didn't specify the compiler or even the environment you were working
in.  If it is a Windows program (ie compiled by Gujitsu or Netexpress as
Windows executable) then you should be able to just use the Windows API.

If it is a DOS program running in a Windows DOS box the there is the
'WINOLDAP' that allows DOS programs access to some Windows functions. 
see 'PC Interrupts' by Brown and Kyle.

WINOLDAP uses the multiplex interrupt x'2F' with AX=function so you need
to be able to action interrupts directly (MF can do this).

    AX=h1700 identifies the version of Windows -> AL major version, AH
minor
    AX=h1701 opens clipboard -> AX=0 is fail, AX/=0 is success
    AX=h1702 clears clipboard
    AX=h1703 set clipboard data
       ES:BX -> data
       CX    size
       DX    type (01h = text, ...)
    ...
    AX=h1708 close clipboard
```

#### ↳ Re: clipboard

- **From:** "Costas Giannoulis" <diavasi@otenet.gr>
- **Date:** 2001-01-26T15:00:45+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94rt8v$r8b$1@usenet.otenet.gr>`
- **References:** `<ZfXb6.2937$yz3.99955@iguano.antw.online.be>`

```
If you are using NE you can use the class Clipboard ("clipbrd") which comes
with the class library. It is  easy to write into the clipboard : invoke
Clipboard "write" using aRecord. Where aRecord is a characterArray delimited
by null (x"00"). I believe something like this exists in Fujitsu cobol.

Costas


Philip Foncke <philip.foncke@advalvas.be> wrote in message
news:ZfXb6.2937$yz3.99955@iguano.antw.online.be...
> Is there a possibility to copy some strings (4 lines pic x(20)) to the
> clipboard of windows
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
